#!/usr/bin/env python3
"""Safely update the clean EquWord main checkout before starting work.

Python standard library only. Run from the repository root. This script does
not stash, reset, rebase, switch branches, commit, push, or publish releases.
"""

import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import urlsplit


EXPECTED_REPOSITORY = "PsycheMatrica/EquWord"


class StopWork(RuntimeError):
    """A state that needs the user's attention before editing."""


def git(root, *args):
    env = os.environ.copy()
    env["GIT_TERMINAL_PROMPT"] = "0"
    try:
        result = subprocess.run(
            ["git", *args], cwd=root, env=env, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60,
        )
    except FileNotFoundError as exc:
        raise StopWork("Git is not installed or is not on PATH.") from exc
    except subprocess.TimeoutExpired as exc:
        raise StopWork("Git timed out. Inspect the checkout before retrying.") from exc
    if result.returncode:
        detail = result.stderr.strip() or result.stdout.strip()
        raise StopWork(f"git {' '.join(args)} failed: {detail}")
    return result.stdout.strip()


def github_repository(url):
    """Return owner/repository for a supported canonical GitHub remote."""
    scp = re.fullmatch(r"git@github\.com:([^/\s]+)/([^/\s]+?)(?:\.git)?/?", url, re.I)
    if scp:
        return f"{scp.group(1)}/{scp.group(2)}".casefold()
    try:
        parsed = urlsplit(url)
        if parsed.hostname != "github.com" or parsed.query or parsed.fragment:
            return None
        if parsed.scheme == "https":
            if parsed.username is not None or parsed.password is not None or parsed.port is not None:
                return None
        elif parsed.scheme == "ssh":
            if parsed.username != "git" or parsed.password is not None or parsed.port not in (None, 22):
                return None
        else:
            return None
        match = re.fullmatch(r"/([^/\s]+)/([^/\s]+?)(?:\.git)?/?", parsed.path)
        return f"{match.group(1)}/{match.group(2)}".casefold() if match else None
    except ValueError:
        return None


def verify_origin(root):
    expected = EXPECTED_REPOSITORY.casefold()
    for options in (("--all",), ("--push", "--all")):
        urls = git(root, "remote", "get-url", *options, "origin").splitlines()
        if not urls or any(github_repository(url) != expected for url in urls):
            raise StopWork(
                f"origin must use the canonical HTTPS or SSH remote for {EXPECTED_REPOSITORY}. "
                "No remote was changed."
            )


def verify_clean(root):
    status = git(root, "status", "--porcelain=v1", "--untracked-files=all")
    if status:
        raise StopWork("The working tree has staged, modified, or untracked files. Preserve them and ask how to proceed.")
    for marker in (
        "MERGE_HEAD", "CHERRY_PICK_HEAD", "REVERT_HEAD", "BISECT_LOG",
        "rebase-apply", "rebase-merge", "sequencer", "index.lock",
    ):
        path = Path(git(root, "rev-parse", "--git-path", marker))
        if not path.is_absolute():
            path = root / path
        if path.exists():
            raise StopWork(f"A Git operation or lock is present ({marker}). Inspect and finish it before editing.")


def start_work(root):
    root = Path(root).resolve()
    # Status is the first Git command. No network or working-file updates precede it.
    verify_clean(root)
    actual_root = Path(git(root, "rev-parse", "--show-toplevel")).resolve()
    if actual_root != root:
        raise StopWork("Run this helper from the repository root.")
    if any(part.casefold() == "dropbox" or part.casefold().startswith("dropbox (") for part in root.parts):
        raise StopWork("This checkout is inside a Dropbox folder. Use a local checkout outside Dropbox.")
    verify_origin(root)
    branch = git(root, "symbolic-ref", "--quiet", "--short", "HEAD")
    if branch != "main":
        raise StopWork(f"Expected branch main; found {branch}. No branch was changed.")
    upstream = git(root, "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{upstream}")
    if upstream != "origin/main":
        raise StopWork(f"Expected upstream origin/main; found {upstream}. No upstream was changed.")
    print(f"Validated {EXPECTED_REPOSITORY}: main -> origin/main; working tree clean.", flush=True)
    git(root, "fetch", "--no-tags", "origin")
    ahead, behind = map(int, git(root, "rev-list", "--left-right", "--count", "HEAD...origin/main").split())
    if ahead:
        raise StopWork(
            f"main has {ahead} local commit(s) and is {behind} commit(s) behind origin/main. "
            "Preserve this state and ask how to proceed."
        )
    verify_clean(root)
    output = git(
        root, "-c", "merge.autoStash=false", "-c", "rebase.autoStash=false",
        "pull", "--ff-only", "--no-rebase", "--no-autostash", "origin", "main",
    )
    verify_clean(root)
    print(output)
    print(git(root, "status", "--short", "--branch"))
    print(f"Ready to work. Commit: {git(root, 'rev-parse', '--short', 'HEAD')}")


def main():
    if len(sys.argv) != 1:
        print("Usage: run python scripts/start_work.py from the EquWord repository root.", file=sys.stderr)
        return 2
    try:
        start_work(Path.cwd())
    except StopWork as exc:
        print(f"STOP: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
