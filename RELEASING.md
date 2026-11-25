# EquWord release procedure

## Current 1.0.2 preparation

The 1.0.2 package adds the guarded A3 manual-break reader and upright notation tokens in native superscripts as well as subscripts. It retains the seven-member installation bundle, CC BY-NC-SA 4.0 terms and Concept DOI. Read the current manifest for the exact candidate and archive identities. Preserve the published 1.0.1 tag, assets and receipt unchanged.

The focused private Windows predecessor passed native Format All on 22 examples, 33 notation probes, save/reopen and authored-content/field/bookmark/link preservation checks. The A3 predecessor passed its three-row selection merge and saved-file preservation checks. The final 1.0.2 rebuild changes only version declarations from the focused predecessor; its native compile/About/reopen evidence and source-preservation audit must be bound to its exact final hash before publication.

The author explicitly waived a further Mac run for this candidate on November 25, 2026. Exact-candidate Mac execution stays **UNVERIFIED**. A separate hash-bound packaging policy checks this decision, fixed focused-Windows receipt/source-audit/saved-result identities, the final version-only audit, all 63 retained guards and both form designers. The older 1.0.1 policy remains unchanged. Neither policy changes runtime equation-preservation checks or overrides a recorded native FAIL/BLOCKED.

The updated Quick Starts and Practice identify 1.0.2. Genuine installation screenshots may show earlier unchanged screens; do not manufacture new captures for a version label. Keep unresolved/raw serialization differences and verification limits disclosed. The public package must not contain private test documents, raw logs or source exports.

## Published 1.0.1

The author approved the exact reviewed 1.0.1 release, published November 3, 2026 (America/New_York; November 4 UTC). See `RELEASE_RECEIPT_1.0.1.json` for the frozen GitHub tag, assets and verified Zenodo archive. The released ZIP contains only seven package files. No package bytes changed during this repository-only publication metadata update. Preserve the existing GitHub/Zenodo linkage; later releases require separate final author approval.

`EquWord.zip` must be built from the contents of `package/`, containing exactly seven approved files at the ZIP root and in `Tutorial/`. For each future authorized draft, attach that ZIP and its `.sha256` sidecar. Do not upload a ZIP of the checkout or include repository scripts, instructions, manifests, private evidence or source exports in the installation bundle. GitHub's automatically generated repository archives are separate; `.gitattributes` limits future repository exports to `package/`, but their wrapper is not the flat installation ZIP. Direct users to the named `EquWord.zip` attachment.

Use the preferred all-version identifier https://doi.org/10.5281/zenodo.23935877 in current citation information. The 1.0.1 publication date and version-specific DOI are recorded in its receipt; current recommended citation information continues to use the Concept DOI. Preserve version-specific identifiers in historical receipts.

## Prepare and verify a future release

1. Follow the clean-state/start-work rules in `AGENTS.md` before changing the actual checkout. A preview without `.git` is local preparation only.
2. Transfer only approved public files. Keep installed templates, prior releases, raw results, editable guide masters and separate VBA exports unchanged and outside the distribution.
3. Edit only the root `README.md`. Run `python scripts/build_release.py --sync-readme` explicitly to generate the byte-identical package copy. This operation does not update the manifest or approval state.
4. Keep root/package citation and license pairs identical. Deliberately record final package, template and reproducible archive identities in `RELEASE_MANIFEST.json`. Record actual candidate-specific test scope, including UNVERIFIED, FAIL or BLOCKED findings without converting predecessor evidence into a new pass.
5. Run `python scripts/build_release.py --verify-only`, then build into ignored `dist/` or a new external output folder. The builder refuses different existing assets. Inspect the seven ZIP entries and verify the sidecar independently.
6. Inspect the public diff and staged files, then commit/push only when authorized. Create or update **only a draft** when draft preparation is authorized; do not trigger publication or Zenodo ingestion.
7. Present the exact version, target commit, ZIP and DOTM checksums, filenames, notes, open findings and actual native scope to the author before requesting final publication approval.

For the historical 1.0.1 candidate, the author explicitly accepted the recorded predecessor Mac evidence plus its exact version-only source audit without a further Mac rerun. That frozen policy remains limited to its original candidate, baseline and audit. It does not authorize later candidates.

`--publication-check --verify-only` requires completed author-review readiness and the current candidate's own validated evidence. Historical approval does not grant approval to later bytes. Verification/building never executes Word or publishes anything.

The historical 1.0.1 Windows evidence covered native compilation, final About/version, read-only reopen and unchanged file identity; it was not a processing regression. About still refers to README.txt although the supplied file is README.md. This pre-existing minor wording discrepancy is nonblocking; use the supplied README.md.

## Frozen prior 1.0.0 release

Version 1.0.0 was published November 3, 2026 (America/New_York; November 4 UTC). Its template SHA-256 is `b7fc3290227b244647fc15a548f683a443f064aa812e0288bdc82ea3d4383a76`; released `EquWord.zip` SHA-256 is `8888d3703267435150b1aac4a2431d241ff0938330178733514baed91fcc67bf`.

Keep `RELEASE_RECEIPT.json` byte-identical. It identifies the frozen tag, assets and Zenodo version record; it is not a receipt for 1.0.1. Do not move the v1.0.0 tag, replace its assets or alter its published record. The earlier post-publication DOI metadata snapshot was not a replacement release.
