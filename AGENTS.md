# EquWord public working instructions

This is the public distribution repository for **EquWord: Equation Conversion and Formatting for Microsoft Word**. Its canonical remote is `PsycheMatrica/EquWord`. Keep this public checkout outside Dropbox and other synchronized folders.

The author's separate private development checkout is `PsycheMatrica/EquWord-Dev`, managed inside `Dropbox/Software_Development/EquWords` by explicit user choice. Work on that private checkout from only one computer at a time and follow its own root `AGENTS.md`. The public helper's Dropbox restriction applies to this public repository; do not extend it into a blanket prohibition on the separately authorized private workflow.

## Start a public work session

1. Read these instructions and run `git status --short --branch` before editing the actual checkout.
2. If staged, modified or untracked work exists, preserve it and stop to resolve how to finish it. Never overwrite, stash, clean, reset or discard it automatically. Existing work is not permission to replace it wholesale.
3. From a clean actual checkout, run `python scripts/start_work.py` on Windows or `python3 scripts/start_work.py` on Mac. It validates `main`, upstream `origin/main`, the canonical remote and absence of unfinished Git operations, then fetches and pulls with `--ff-only` and automatic stashing disabled.
4. If validation, fetch or fast-forward fails, stop before editing. Do not automatically rebase, reset, force-push, change remotes or switch branches.

A workspace preview without `.git` is not the actual checkout. A request for preview preparation does not authorize promotion, Git mutations or publication.

## Public files and protected assets

- Keep exactly the seven approved members in `package/`: `EquWord.dotm`, `README.txt`, `CITATION.cff`, `LICENSE.txt`, `Tutorial/EquWord_Practice.docx` and the Windows/Mac Quick Start PDFs.
- Keep the root and package citation files identical, and the two license files identical. The current license heading is `EquWord 1.0.0` with CC BY-NC-SA 4.0 terms.
- The recorded candidate is `package/EquWord.dotm`, SHA-256 `b7fc3290227b244647fc15a548f683a443f064aa812e0288bdc82ea3d4383a76`. Preserve it unless a task explicitly authorizes a new candidate and its checks.
- Preserve all mathematical-structure, number-field, bookmark, selection and native-equation guards. Never remove or relax a guard to make a test pass.
- Read `RELEASE_MANIFEST.json` for candidate-specific scope. Exact-candidate Windows compile/reopen and Mac form opening/cancellation passed; focused processing checks on earlier binaries remain predecessor evidence; this is not a claim of a full branded Mac regression. Mac separate automatic full-log saving remains unavailable and Windows-style Esc polling is not provided there.
- Preserve guide, practice, license and template bytes when their revision is outside the task. A documentation-only revision does not establish a fresh software runtime pass.
- Separate BAS/CLS/FRM/FRX exports, prototypes, manuscripts, raw fixtures, unredacted screenshots, editable guide masters and private test logs/results stay outside the public repository. `.gitignore` is a guard, not a substitute for reviewing staged files. Do not ignore all DOCX files: the public practice file is required.
- Do not copy a whole private review/handoff folder into this checkout. Transfer only explicitly approved public files and sanitized metadata. Private evidence paths and workstation account names do not belong in public metadata.

## Finish authorized public work

Run appropriate checks, inspect the actual diff and staged file list, and verify package/archive identities. Commit and push only when the task authorizes saving to the public repository. Keep local previews local. If a push fails, preserve the commit and report the cause; do not rewrite history or force-push automatically.

Keep build products in ignored `dist/` or a new external output directory. Existing different assets must not be overwritten. Refresh a dated Publish snapshot only from a known public commit or verified release, and identify review-only copies accurately.

## Mandatory final release confirmation

Before every GitHub release or Zenodo publication, present the exact version, target commit, artifact filenames and SHA-256 checksums, release notes and actual verification scope. Obtain the author's explicit final confirmation for that concrete release. General preparation instructions, repository commit/push authorization, Zenodo account access and elapsed time are not final publication approval.

Draft preparation may continue, but creating a release, uploading assets, publishing to Zenodo, updating the website as released or replacing an installed Word template requires the relevant explicit authorization. The builder's publication check never grants that authorization.

See [WORKFLOW.md](WORKFLOW.md) and [RELEASING.md](RELEASING.md).
