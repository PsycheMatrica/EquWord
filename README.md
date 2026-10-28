# EquWord: Equation Conversion and Formatting for Microsoft Word

EquWord converts supported LaTeX into editable native Word equations and applies document-specific notation, font and equation-layout choices. It is a macro-enabled template for desktop Microsoft Word.

Version **0.9.27** is prepared here for the first EquWord public release. The repository is [PsycheMatrica/EquWord](https://github.com/PsycheMatrica/EquWord). The first GitHub release and Zenodo publication are pending; no Zenodo DOI has been assigned.

## Get started

The planned download asset is **EquWord.zip**. The unpacked distribution is in [package/](package/):

1. Read [the installation and command guide](package/README.txt).
2. Load `ResearchEquationFormatter.dotm` as a global template in desktop Word.
3. Open the [illustrated Quick Start PDF](package/Tutorial/Research_Equation_Formatter_Quick_Start.pdf) and make a working copy of [REF_Practice.docx](package/Tutorial/REF_Practice.docx).
4. Run `AboutResearchEquationFormatter` and confirm version 0.9.27 before trying the commands on the practice copy.

The template filename, macro names and in-app Research Equation Formatter name are retained from the tested build. **Research Equation Formatter is the legacy name used inside EquWord 0.9.27.** The Quick Start PDF and practice document are also preserved unchanged. The PDF shows Windows menus and screenshots; Mac users should use the Mac loading steps in `package/README.txt`.

## What it does

- Converts supported selected LaTeX or supported LaTeX in the main document body.
- Formats native Word equations using settings saved with the document.
- Supports eligible multiline merging, relation alignment and internal row spacing.
- Applies equation-number table placement and selected formatting categories.
- Checks mathematical structure, number fields and bookmark preservation during processing.

Equations remain editable in Word. The tool does not assess mathematical correctness, perform statistical analysis or implement every LaTeX command. Work on a copy of a manuscript and review the result before saving.

## Tested environments and scope

The exact V5 template included here was executed in both environments:

| Platform | Tested environment |
| --- | --- |
| Mac | Word 16.113.4 (16.113.26100421), macOS 26.7.2, Apple silicon |
| Windows | Word 16.0.20430.20180, 64-bit, Windows 11 build 26300 |

Mac tests covered selection and whole-body LaTeX conversion, native fraction and Greek-symbol output, intentional inner brackets, an eligible two-row merge, preservation of supplied mathematical content/fields/bookmarks, save/reopen formatting, and template reload with About in a fresh Word session. Windows tests additionally exercised the native format and selective-reformat commands, document-specific remembered choices, a saved native equation edit and repeat formatting after restarting the test Word process.

These results apply to the exact template, supplied fixtures and installations above. They do not establish compatibility with every Word build or manuscript. Large-document performance, forced over-height/page-boundary stress cases, and every notation or geometry option were not exhaustively tested. The tests did not establish feature parity for every command on Mac. Word for the web cannot run this VBA template.

## Files and source packaging

The download contains the DOTM template, installation guide, license, citation metadata, Quick Start PDF and practice DOCX. VBA code is embedded in the DOTM. Separate BAS, CLS and FRM exports are not included. Private test logs and raw test fixtures are not part of this public package.

## License and citation

Copyright (c) 2026 Gyeongcheol Cho. The software and accompanying original documentation are licensed under **CC BY-NC-SA 4.0**. See [LICENSE.txt](LICENSE.txt) for the unchanged license and attribution notices. The legacy Research Equation Formatter heading in that file identifies the same software distribution. EquWord is the public-facing name used in this preparation; the license terms are unchanged.

The license does not automatically apply to your own manuscripts or equations. Citation in a manuscript is appreciated and is not required merely for using the tool. Attribution conditions still apply when sharing licensed material. See [CITATION.cff](CITATION.cff); a version DOI can be added when a Zenodo record exists.

Microsoft interface elements and product names in the retained screenshots remain the property of Microsoft.

## Release history

See [CHANGELOG.md](CHANGELOG.md) for the 0.9.27 release-preparation entry. Maintainers can verify and build the download with `python scripts/build_release.py`; see [RELEASING.md](RELEASING.md) for the release procedure.
