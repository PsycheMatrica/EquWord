# Working on EquWord across Windows and Mac

Use separate locations for public distribution and private development. The public repository is `PsycheMatrica/EquWord`; each computer has its own checkout outside Dropbox. The author has separately chosen `PsycheMatrica/EquWord-Dev` inside `Dropbox/Software_Development/EquWords` for private development, with only one computer working on it at a time. Its own root `AGENTS.md` governs that private workflow.

## Public checkout setup

A suitable Windows location is `%USERPROFILE%\Published_Software\EquWord`; on Mac use `~/Published_Software/EquWord`. Install Git and Python 3, use normal GitHub authentication, and never put tokens or passwords in the repository. Inspect an existing folder before cloning; do not clone over it.

From the intended parent directory, clone `https://github.com/PsycheMatrica/EquWord.git` into `EquWord`. SSH may use `git@github.com:PsycheMatrica/EquWord.git`. Keep `main` tracking `origin/main`. Use `python scripts/start_work.py` on Windows or `python3 scripts/start_work.py` on Mac only from the actual clean checkout.

## Each public work session

1. Read `AGENTS.md` and check `git status --short --branch`.
2. Preserve and resolve existing work before pulling or editing. Never automatically stash, discard, reset or clean it.
3. Run the start helper. It validates the public remote/branch/upstream, fetches and pulls with `--ff-only`. It does not reconcile divergence or local commits automatically.
4. Make the authorized changes, run relevant checks, and inspect the actual staged contents for private material. Edit README content only in the root `README.md`, then explicitly run `python scripts/build_release.py --sync-readme` to generate its package copy. Review and update the resulting manifest and archive identities separately. Keep package/root README, citation and license files identical and verify the manifest.
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

Read `RELEASE_MANIFEST.json` for the current version, exact template identity, seven package files, reproducible archive checksum and candidate-specific validation scope. Historical candidate and archive hashes are not the current release target.

The current 1.0.1 draft has scoped Windows native compile/About/reopen evidence. Exact-candidate Mac execution remains UNVERIFIED; earlier 1.0.0 form and processing checks are predecessor evidence. For this exact version-only candidate the author accepted predecessor native evidence plus the matching source-preservation audit, without a Mac rerun; the builder validates the bounded decision and does not relabel Mac status PASS. Preserve all mathematical-structure, number-field and bookmark guards. The pre-existing About/README filename discrepancy is nonblocking; the supplied README.md is authoritative. Keep the current release in draft pending final author review.

Documentation revisions change the archive identity while leaving the template identity and its recorded tests unchanged. Use the current manifest and final author approval packet together. Preserve previous archives and do not silently replace approved assets.

The author has authorized a 1.0.1 GitHub draft and its package-only assets. Build the named `EquWord.zip` attachment from the seven files inside `package/`; do not upload a checkout ZIP as the installer. Future automatic repository exports are limited by `.gitattributes`, but remain distinct from the flat release attachment. Repository work and draft preparation do not authorize publication, Zenodo ingestion, website release announcements or installed-template replacement. Publication requires final author confirmation of the exact commit, files, checksums, notes and actual test scope, and the builder’s recorded-evidence gate, including the narrowly scoped version-only Mac acceptance. Use the all-version Concept DOI `10.5281/zenodo.23935877` for current citation information. See `RELEASING.md`.

## Other software projects

Use an independent public checkout and explicit instructions per project. The EquWord start helper validates its own public remote and should not be reused unchanged elsewhere. Private repository location and synchronization choices follow that project's explicit user instructions.
