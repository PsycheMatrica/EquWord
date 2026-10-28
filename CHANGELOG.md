# Changelog

## 0.9.27 — first EquWord public release preparation

- Adopted **EquWord: Equation Conversion and Formatting for Microsoft Word** as the public-facing title. The tested template, macro names and in-app Research Equation Formatter name remain unchanged.
- Selected the exact V5 template tested in Word 16.113.4 on macOS 26.7.2 (Apple silicon) and Word 16.0.20430.20180 (64-bit) on Windows 11 build 26300.
- Verified supported selection/whole-body LaTeX conversion on supplied fixtures, including native fractions, Greek symbols, intentional inner brackets and an eligible multiline merge. Saved-file checks covered mathematical content, fields and bookmarks. Windows tests also exercised format/selective commands and saved native edits. Test coverage is limited to the recorded builds and fixtures.
- Updated installation and citation text for EquWord and the recorded cross-platform tests. Retained the tested V5 binary, Quick Start PDF, practice DOCX and CC BY-NC-SA 4.0 license without altering their bytes.
- Prepared `EquWord.zip` as the stable download filename. The first GitHub release and Zenodo publication remain pending; no DOI or publication date is asserted here.
