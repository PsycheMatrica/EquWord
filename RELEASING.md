# EquWord release procedure

## Current 1.0.1 draft

The author authorized a **draft release only**, with a package-only download, updated internal version and the all-version Concept DOI. Do not publish the draft, create a public tag through publication, publish to Zenodo or update the website until the author gives separate final approval. Preserve the existing GitHub/Zenodo linkage.

`EquWord.zip` must be built from the contents of `package/`, containing exactly seven approved files at the ZIP root and in `Tutorial/`. Attach that ZIP and its `.sha256` sidecar to the draft. Do not upload a ZIP of the checkout or include repository scripts, instructions, manifests, private evidence or source exports in the installation bundle. GitHub's automatically generated repository archives are separate; `.gitattributes` limits future repository exports to `package/`, but their wrapper is not the flat installation ZIP. Direct users to the named `EquWord.zip` attachment.

Use the preferred all-version identifier https://doi.org/10.5281/zenodo.23935877 in current citation information. Do not assign a 1.0.1 publication date or version DOI before publication. Preserve version-specific identifiers in historical receipts.

## Prepare and verify

1. Follow the clean-state/start-work rules in `AGENTS.md` before changing the actual checkout. A preview without `.git` is local preparation only.
2. Transfer only approved public files. Keep installed templates, prior releases, raw results, editable guide masters and separate VBA exports unchanged and outside the distribution.
3. Edit only the root `README.md`. Run `python scripts/build_release.py --sync-readme` explicitly to generate the byte-identical package copy. This operation does not update the manifest or approval state.
4. Keep root/package citation and license pairs identical. Deliberately record final package, template and reproducible archive identities in `RELEASE_MANIFEST.json`. Record actual candidate-specific test scope, including UNVERIFIED, FAIL or BLOCKED findings without converting predecessor evidence into a new pass.
5. Run `python scripts/build_release.py --verify-only`, then build into ignored `dist/` or a new external output folder. The builder refuses different existing assets. Inspect the seven ZIP entries and verify the sidecar independently.
6. Inspect the public diff and staged files, then commit/push only when authorized. Create or update **only a draft** when draft preparation is authorized; do not trigger publication or Zenodo ingestion.
7. Present the exact version, target commit, ZIP and DOTM checksums, filenames, notes, open findings and actual native scope to the author before requesting final publication approval.

The author explicitly accepted the recorded predecessor Mac evidence plus the exact version-only source audit for this 1.0.1 candidate, without a further Mac rerun. Mac runtime remains **UNVERIFIED**, never PASS. The builder validates this narrow decision against fixed candidate, baseline and audit identities, explicit author-decision evidence and all required source-preservation facts. It refuses missing or mismatched acceptance evidence and cannot override native FAIL/BLOCKED or altered executable/form-designer/runtime-guard evidence. This policy does not change any equation-processing or preservation guard.

`--publication-check --verify-only` additionally requires `ready_for_author_review`; the current manifest deliberately remains `draft`, so that check refuses on draft status. When review readiness is explicitly recorded, the accepted evidence basis can satisfy the technical evidence gate without a Mac rerun, but the author's separate final publication approval remains mandatory. Draft verification/building never executes Word or publishes anything.

The Windows evidence covers compilation of the retained VBA, final About/version, read-only reopen and unchanged file identity, not a processing regression. About still refers to README.txt although the supplied file is README.md. This pre-existing minor wording discrepancy is nonblocking; use the supplied README.md. No additional VBA edit or recompilation is required on this account.

## Frozen 1.0.0 release

Version 1.0.0 was published November 3, 2026 (America/New_York; November 4 UTC). Its template SHA-256 is `b7fc3290227b244647fc15a548f683a443f064aa812e0288bdc82ea3d4383a76`; released `EquWord.zip` SHA-256 is `8888d3703267435150b1aac4a2431d241ff0938330178733514baed91fcc67bf`.

Keep `RELEASE_RECEIPT.json` byte-identical. It identifies the frozen tag, assets and Zenodo version record; it is not a receipt for 1.0.1. Do not move the v1.0.0 tag, replace its assets or alter its published record. The earlier post-publication DOI metadata snapshot was not a replacement release.
