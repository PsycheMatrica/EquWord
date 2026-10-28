# EquWord working instructions

This is the public distribution repository for **EquWord: Equation Conversion and Formatting for Microsoft Word**. Its canonical remote is `PsycheMatrica/EquWord` on GitHub. Keep its live Git checkout outside Dropbox and other synchronized folders. Dropbox is for private development, test handoffs, and clearly dated Publish copies.

## Start every work session

1. Run `git status --short --branch` before editing. If there are staged, modified, or untracked files, stop and ask the user how to preserve or finish that work. Do not overwrite, stash, clean, reset, or discard it.
2. From the repository root, run `python scripts/start_work.py` on Windows or `python3 scripts/start_work.py` on macOS. The helper requires a clean working tree, no Git operation in progress, branch `main`, upstream `origin/main`, and the expected HTTPS or SSH remote. It fetches and then pulls with `--ff-only`, with automatic stashing disabled.
3. If validation, fetching, or pulling fails, stop before editing and report the actual state. Do not repair this by rebasing, resetting, force pushing, switching branches, or changing remotes without the user's direction.
4. Read the task and relevant documentation, then perform the authorized work. Do not use a Dropbox Publish copy as the working checkout.

## Scope and preservation

- This repository contains public distribution files and their documentation. Keep private VBA source exports (`.bas`, `.cls`, `.frm`, `.frx`), development notes, manuscripts, raw fixtures, private test documents, and test logs outside it. `.gitignore` is an extra guard, not a substitute for reviewing every staged file.
- Keep `package/Tutorial/REF_Practice.docx` public. Do not ignore or remove all Word documents.
- Preserve the template's existing safety checks and guards, including its selection and native-equation checks. Do not remove a guard to make a test pass.
- The tested v0.9.27 template is `package/ResearchEquationFormatter.dotm`, SHA-256 `70ca15d170dc48f93b3ea13b99bff3bd0f19728456c8927138ba6c416de3b35e`. Preserve those exact bytes unless a later task explicitly authorizes a new tested template. Do not rename internal macro or UI names as part of a display-name or repository-name change.
- Preserve the existing license, practice DOCX, and quick-start PDF bytes unless their revision is expressly within the task. Keep root and package citation/license metadata consistent.
- Before committing, review the staged file list and diff, check the applicable package checksums and archive contents, and run checks appropriate to the change. Do not describe unperformed Word or Mac tests as passed.

## Finish an authorized task

- Once the user-authorized work and its relevant checks are complete, make a clear commit and push to the validated upstream when that task's authorization includes saving the work to this public repository. For ordinary repository work, the established routine is to commit and push the completed change. If the user requests a local preview or explicitly withholds publishing, keep it local.
- Check `git status --short --branch` afterward and report what changed, what was checked, and the commit/push result. If pushing is rejected, preserve the local commit and report the reason; do not force push, rebase, or reset.
- Creating a GitHub release, uploading release assets, publishing to Zenodo, or replacing an installed Word template requires an explicit instruction for that action. A request to edit or commit repository files does not authorize these steps.
- Refresh a Dropbox Publish copy only from a known commit or verified release. Treat it as a dated snapshot, not a second checkout to edit or merge.

See [WORKFLOW.md](WORKFLOW.md) for the cross-platform setup and routine.
