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

- Keep exactly the seven approved members in `package/`: `EquWord.dotm`, `README.md`, `CITATION.cff`, `LICENSE.txt`, `Tutorial/EquWord_Practice.docx` and the Windows/Mac Quick Start PDFs.
- Maintain only the repository-root `README.md`. `package/README.md` is a generated, byte-identical distribution copy. Run `python scripts/build_release.py --sync-readme` explicitly after editing the source; then review and update the README and archive identities in the manifest. Verification never repairs a stale copy or changes the manifest automatically.
- Keep the root and package citation files identical, and the two license files identical. The current license heading is `EquWord 1.0.2` with CC BY-NC-SA 4.0 terms.
- The frozen published 1.0.1 template has SHA-256 `a4b8c22f5fb99ce02fd667978f48b57f0e950a8822250465c957f66eab35aa55`; preserve its release asset unchanged. The current `package/EquWord.dotm` targets 1.0.2 with its own identity and checks in the manifest.
- Preserve all mathematical-structure, number-field, bookmark, selection and native-equation guards. Never remove or relax a guard to make a test pass.
- Read `RELEASE_MANIFEST.json` for candidate-specific scope. Version 1.0.2 builds on the hash-bound private Windows predecessor with 22 examples and 33 notation probes, the A3 merge/preservation check, and final native version confirmation. Exact-candidate Mac execution is UNVERIFIED under the author's separate November 25, 2026 waiver. The builder requires the fixed candidate, focused predecessor and final source-audit identities, 63 unchanged guard procedures, unchanged form designers, explicit author decision and native Windows evidence. It cannot waive a Mac FAIL/BLOCKED or claim an unperformed runtime PASS. Preserve all disclosed strict raw differences. The older 1.0.1 version-only acceptance remains frozen and cannot be reused for changed bytes. About’s pre-existing README.txt wording is a nonblocking discrepancy; the supplied README.md has the instructions. Mac separate automatic full-log saving remains unavailable and Windows-style Esc polling is not provided there.
- Preserve guide, practice, license and template bytes when their revision is outside the task. A documentation-only revision does not establish a fresh software runtime pass.
- Separate BAS/CLS/FRM/FRX exports, prototypes, manuscripts, raw fixtures, unredacted screenshots, editable guide masters and private test logs/results stay outside the public repository. `.gitignore` is a guard, not a substitute for reviewing staged files. Do not ignore all DOCX files: the public practice file is required.
- Do not copy a whole private review/handoff folder into this checkout. Transfer only explicitly approved public files and sanitized metadata. Private evidence paths and workstation account names do not belong in public metadata.

## Finish authorized public work

Run appropriate checks, inspect the actual diff and staged file list, and verify package/archive identities. Commit and push only when the task authorizes saving to the public repository. Keep local previews local. If a push fails, preserve the commit and report the cause; do not rewrite history or force-push automatically.

Keep build products in ignored `dist/` or a new external output directory. Existing different assets must not be overwritten. Refresh a dated Publish snapshot only from a known public commit or verified release, and identify review-only copies accurately.

## Mandatory final release confirmation

Before every GitHub release or Zenodo publication, present the exact version, target commit, artifact filenames and SHA-256 checksums, release notes and actual verification scope. Obtain the author's explicit final confirmation for that concrete release. General preparation instructions, repository commit/push authorization, Zenodo account access and elapsed time are not final publication approval.

Version 1.0.1 was published after explicit final author approval on November 3, 2026 (America/New_York). Preserve RELEASE_RECEIPT.json for 1.0.0 and RELEASE_RECEIPT_1.0.1.json for 1.0.1, together with their frozen tags and assets. That approval does not authorize another release, website changes or installed-template replacement. The builder's publication check never grants publication authorization.

See [WORKFLOW.md](WORKFLOW.md) and [RELEASING.md](RELEASING.md).
