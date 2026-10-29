# Working on EquWord across Windows and Mac

Use separate locations for public distribution and private development. The public repository is `PsycheMatrica/EquWord`; each computer has its own checkout outside Dropbox. The author has separately chosen `PsycheMatrica/EquWord-Dev` inside `Dropbox/Software_Development/EquWords` for private development, with only one computer working on it at a time. Its own root `AGENTS.md` governs that private workflow.

## Public checkout setup

A suitable Windows location is `%USERPROFILE%\Published_Software\EquWord`; on Mac use `~/Published_Software/EquWord`. Install Git and Python 3, use normal GitHub authentication, and never put tokens or passwords in the repository. Inspect an existing folder before cloning; do not clone over it.

From the intended parent directory, clone `https://github.com/PsycheMatrica/EquWord.git` into `EquWord`. SSH may use `git@github.com:PsycheMatrica/EquWord.git`. Keep `main` tracking `origin/main`. Use `python scripts/start_work.py` on Windows or `python3 scripts/start_work.py` on Mac only from the actual clean checkout.

## Each public work session

1. Read `AGENTS.md` and check `git status --short --branch`.
2. Preserve and resolve existing work before pulling or editing. Never automatically stash, discard, reset or clean it.
3. Run the start helper. It validates the public remote/branch/upstream, fetches and pulls with `--ff-only`. It does not reconcile divergence or local commits automatically.
4. Make the authorized changes, run relevant checks, and inspect the actual staged contents for private material. Keep package/root citation and license files identical and verify the manifest.
5. Commit and push when authorized for the public repository. A local preview stays local. Preserve rejected pushes and resolve them deliberately.
6. Confirm the final working state and report the commit and checks. Begin on the next computer by checking and pulling before editing.

## Locations and boundaries

| Location | Purpose |
| --- | --- |
| Independent local `Published_Software/EquWord` checkout | Public seven-member package, sanitized metadata and packaging helpers. Keep this public `.git` outside Dropbox. |
| Private `Dropbox/Software_Development/EquWords` checkout | Private EquWord-Dev development under its own instructions; one active computer at a time. |
| Private cross-platform handoff folders | Explicit candidates, original inputs, native results and test evidence exchanged between computers. |
| Dated Publish copies | Snapshots from a known public commit or verified release; review-only packets remain labeled review-only. |

The public helper intentionally refuses a public checkout inside Dropbox. That restriction does not change the author's approved private EquWord-Dev location. Do not run this public helper against the private repository or copy its rules there without adapting them deliberately.

Never merge a Publish snapshot wholesale over the public checkout. Transfer only the public files selected for an authorized update. Keep editable guide masters, unredacted screenshots, separate source exports, manuscript files and private test logs outside the public repository. The practice DOCX is public and must remain included.

## Current package and recorded scope

The candidate is `package/EquWord.dotm`, version 1.0.0, SHA-256:

```text
3e876985b016db8e0bb242b57a2036aeb80ebc720201410e0e32698ece583a13
```

Windows native command checks and focused Mac Selective Reformat/Startup/About/Settings checks passed for these bytes on the recorded installations. Mac's other four processing commands were listed rather than rerun; separate automatic full-log saving was unavailable. Read `RELEASE_MANIFEST.json` for the complete scope and limitations. Preserve the candidate and safety guards unless the task expressly authorizes their revision.

The reviewed 1.0.0 archive is `EquWord.zip`, SHA-256 `7445ce7810992905ba826db6540eb87f57aa32d1e3b80303e50bff989e97d98d`. A different build must not silently replace that reviewed identity.

Repository work never implies a GitHub release, asset upload, Zenodo publication, website release announcement or installed-template replacement. Each release requires final author confirmation of its exact commit, files, checksums, notes and actual test scope. See [RELEASING.md](RELEASING.md).

## Other software projects

Use an independent public checkout and explicit instructions per project. The EquWord start helper validates its own public remote and should not be reused unchanged elsewhere. Private repository location and synchronization choices follow that project's explicit user instructions.
