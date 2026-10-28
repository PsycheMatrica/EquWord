# Changelog

## 1.0.0 — release candidate

- Prepare the first EquWord public release with an internal display version of 1.0.0. Preserve the V5 processing logic and all mathematical/field/bookmark guards; independently compare the native-built source against the baseline.
- Split the Quick Start into Windows and Mac PDFs. Add author, document version/date, Word environment, repository and license to their opening pages. Remove the misleading “Word for Windows 0.9.27” subtitle.
- Update the practice document and platform-specific keyboard instructions while preserving native equations, fields and bookmarks.
- Add concise, optional manuscript acknowledgment examples and a software reference to the README and both Quick Starts. Keep the ChatGPT example conditional on actual AI use. Remove the previous-version test-history sentence from the Mac guide cover. This documentation revision does not change the tested template or frozen Mac handoff.
- Record new-candidate verification explicitly. Windows rechecks passed on the recorded build with seven processing runs, saved native edits, preservation and restart checks. The exact-candidate Mac recheck remains pending; earlier 0.9.27 tests are baseline evidence.
- Configure the original Zenodo account connection. Obtain and verify the first DOI only after the approved release; no DOI is fabricated or preassigned.
- Add one line of space after guide titles and section headings. Simplify the Windows cover to match the Mac guide, keeping author, version, date and Word environment information together. Group procedural steps in single-cell tables, consolidate continuous instructions, and present supporting notes as bullets. Use 1.5-line spacing inside procedure boxes and retain double spacing outside. Add the EquWord Quick Start running head beside the native page-number field on every page. Retain screenshot provenance near the Windows instructions. Software and frozen test packets are unchanged.
- Keep the release unpublished until both platform checks and the author's final review are complete.


## 0.9.27 — first EquWord public release preparation

- Adopted **EquWord: Equation Conversion and Formatting for Microsoft Word** as the public-facing title. The tested template, macro names and in-app Research Equation Formatter name remain unchanged.
- Selected the exact V5 template tested in Word 16.113.4 on macOS 26.7.2 (Apple silicon) and Word 16.0.20430.20180 (64-bit) on Windows 11 build 26300.
- Verified supported selection/whole-body LaTeX conversion on supplied fixtures, including native fractions, Greek symbols, intentional inner brackets and an eligible multiline merge. Saved-file checks covered mathematical content, fields and bookmarks. Windows tests also exercised format/selective commands and saved native edits. Test coverage is limited to the recorded builds and fixtures.
- Updated installation and citation text for EquWord and the recorded cross-platform tests. Retained the tested V5 binary, Quick Start PDF, practice DOCX and CC BY-NC-SA 4.0 license without altering their bytes.
- Prepared `EquWord.zip` as the stable download filename. The first GitHub release and Zenodo publication remain pending; no DOI or publication date is asserted here.
