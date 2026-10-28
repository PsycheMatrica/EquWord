# Working on EquWord across Windows and Mac

The public repository is [PsycheMatrica/EquWord](https://github.com/PsycheMatrica/EquWord), titled **EquWord: Equation Conversion and Formatting for Microsoft Word**. Each computer has its own Git checkout outside Dropbox. Git carries completed public changes between computers. Dropbox holds private development, test handoffs, and dated Publish copies.

## One-time setup

Install Git and Python 3 on each computer and use your normal GitHub authentication. Do not put passwords, tokens, or machine-specific paths in the repository.

On Windows, use the approved folder `C:/Users/cheol/Published_Software/EquWord`. In PowerShell:

```powershell
New-Item -ItemType Directory -Force -Path "$HOME/Published_Software" | Out-Null
Set-Location "$HOME/Published_Software"
git clone https://github.com/PsycheMatrica/EquWord.git EquWord
Set-Location EquWord
python scripts/start_work.py
```

If your Windows Python launcher is `py`, use `py -3 scripts/start_work.py` instead. Do not clone over an existing folder; first inspect the existing checkout and preserve its work.

On a Mac, a suitable location is `~/Published_Software/EquWord`. This is a suggested location, not a claim about the Mac's current folder. In Terminal:

```sh
mkdir -p "$HOME/Published_Software"
cd "$HOME/Published_Software"
git clone https://github.com/PsycheMatrica/EquWord.git EquWord
cd EquWord
python3 scripts/start_work.py
```

SSH authentication may use `git@github.com:PsycheMatrica/EquWord.git` instead. Keep the checked-out branch `main` tracking `origin/main`. If those are not already correct, inspect the state and resolve it deliberately before using the helper.

## Each work session

1. Open the local EquWord checkout, read `AGENTS.md`, and check `git status --short --branch`.
2. If any changes are present, preserve them and stop to decide how to finish them. The helper also refuses a dirty working tree, an unfinished Git operation, an unexpected remote, or the wrong branch/upstream.
3. Run `python scripts/start_work.py` on Windows, or `python3 scripts/start_work.py` on Mac. It fetches `origin`, refuses local commits that need a push or reconciliation, and pulls `main` with `--ff-only`. It never stashes, resets, rebases, commits, or pushes.
4. Perform the authorized task and the relevant checks. Inspect the staged file list and diff so private materials cannot enter the public repository. Confirm protected release files remain unchanged when the task does not authorize replacing them.
5. Commit and push the completed public changes under the established task authorization. If the task is a local preview, leave it local. If a push is rejected, retain the commit and resolve the state with the user; never force push or rewrite history automatically.
6. Confirm the final status and report the commit and checks. Start the next computer's session by pulling before editing.

A request to change the repository does not automatically authorize a GitHub release, a release-asset upload, a Zenodo publication, or installation of a template into Word. Perform those only when explicitly requested. Before publishing any release, show its exact files, checksums, commit and release notes and obtain the author's explicit final confirmation. This is required every time, even after a general request to prepare a release or authorize Zenodo.

## What belongs where

| Location | Purpose |
| --- | --- |
| Local `Published_Software/EquWord` checkout on each computer | Public distribution files and documentation; edit, check, commit, and push here. |
| Dropbox private development folder | Private VBA exports, development versions, notes, and manuscripts. |
| Dropbox test handoff folder | Explicitly identified test candidates and feedback exchanged between computers. |
| Dropbox Publish folder | Dated copies exported from a known public commit or verified release, with version and checksum information. |

Do not synchronize an active `.git` folder with Dropbox. Do not edit a Publish snapshot and then copy it wholesale over the checkout. Review and transfer only the files explicitly intended for a public update. The public practice DOCX stays in the repository; private test documents do not.

The current 1.0.0 candidate is `package/ResearchEquationFormatter.dotm`, with SHA-256:

```text
60f3ccc2182b3d8a570796eb535ced40fb94946304233b57c9f9bec1491c4755
```

Windows rechecks of this exact candidate passed on the recorded fixtures; its Mac recheck is pending. Read `RELEASE_MANIFEST.json` for the current evidence and do not describe a pending platform as passed. The earlier V5 binary remains preserved in the 0.9.27 preparation history.

Keep the license, operating-system Quick Start PDFs, practice DOCX, and template bytes unchanged unless the task specifically authorizes replacing them. Retain the template's existing safety guards. Git ignores do not protect already tracked files; always review the actual staged contents.

## Reuse for other public software

Use a separate checkout per project under `Published_Software`, outside Dropbox, and start each session with the same clean-status and fast-forward-only routine. Each project must name and validate its own canonical remote, default branch, protected files, and release checks. Do not reuse the EquWord helper unchanged for another repository: its remote check intentionally accepts only `PsycheMatrica/EquWord`.
