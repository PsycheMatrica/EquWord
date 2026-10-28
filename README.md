# EquWord: Equation Conversion and Formatting for Microsoft Word

EquWord converts supported LaTeX into editable native Word equations and applies document-specific notation, font and equation-layout choices. It is a macro-enabled template for desktop Microsoft Word.

**1.0.0 release candidate:** this first public release is being prepared. Its template displays 1.0.0 and retains the preceding V5 processing logic. The new Windows recheck passed; the exact-candidate Mac recheck remains pending before final author review. No public release or Zenodo DOI has been created. Connection to Zenodo is configured; it does not itself create a DOI.

## Choose your Quick Start

The planned download is **EquWord.zip**. Its seven distribution files are in [package/](package/).

1. Read [the installation and command guide](package/README.txt).
2. Choose [Quick Start for Windows](package/Tutorial/EquWord_Quick_Start_Windows.pdf) or [Quick Start for Mac](package/Tutorial/EquWord_Quick_Start_Mac.pdf).
3. Load `ResearchEquationFormatter.dotm` as a global template in desktop Word. No separate VBA source import is required.
4. Make a working copy of [REF_Practice.docx](package/Tutorial/REF_Practice.docx), run `AboutResearchEquationFormatter`, and confirm version 1.0.0.

**Research Equation Formatter is the legacy name inside EquWord.** The template filename and macro names remain the same so existing command shortcuts remain recognizable. Each Quick Start identifies its author, document version and date, relevant Word environment, repository and license on the first page. Windows screenshots and Mac instructions are provided in separate guides.

## What it does

- Converts supported selected LaTeX or supported LaTeX in the main document body.
- Formats native Word equations using settings saved with the document.
- Supports eligible multiline merging, relation alignment and internal row spacing.
- Applies equation-number table placement and selected formatting categories.
- Checks mathematical structure, number fields and bookmark preservation during processing.

Equations remain editable in Word. The tool does not assess mathematical correctness, perform statistical analysis or implement every LaTeX command. Work on a copy of a manuscript and review the result before saving.

## Validation status

| Candidate | Environment | Native verification |
| --- | --- | --- |
| 1.0.0 Windows | Word 16.0.20430.20180, 64-bit; Windows 11 build 26300 | PASS on supplied fixtures; seven processing runs |
| 1.0.0 Mac | Word 16.113.4 (16.113.26100421); macOS 26.7.2; Apple silicon | Pending exact-candidate Mac recheck |
| Earlier 0.9.27 V5 | Both environments above | Recorded fixture tests passed |

The earlier V5 Mac tests covered selection and whole-body LaTeX conversion, native fractions and Greek symbols, intentional inner brackets, an eligible two-row merge, preservation of supplied mathematical content/fields/bookmarks, save/reopen formatting, and template reload with About in a fresh Word session. Windows tests additionally exercised native format and selective-reformat commands, document-specific remembered choices, a saved native equation edit and repeat formatting after restarting the test Word process.

Earlier results are baseline evidence, not native execution of the new 1.0.0 binary. Results apply to the supplied fixtures and recorded installations. Compatibility with every Word build or manuscript, every Mac command, large-document performance, and forced over-height/page-boundary stress cases is not established. Word for the web cannot run this VBA template.

## Files and source packaging

The download contains the DOTM template, installation guide, license, citation metadata, two operating-system Quick Start PDFs and the practice DOCX. VBA code is embedded in the DOTM. Separate BAS, CLS and FRM exports, private test logs and raw fixtures are not part of this public package.

## License and citation

Copyright (c) 2026 Gyeongcheol Cho. The software and accompanying original documentation are licensed under **CC BY-NC-SA 4.0**. See [LICENSE.txt](LICENSE.txt). Its legacy Research Equation Formatter heading identifies the same software; the license terms and attribution are unchanged.

The license does not automatically apply to your own manuscripts or equations. Citation in a manuscript is appreciated and is not required merely for using the tool. Attribution conditions still apply when sharing licensed material. See [CITATION.cff](CITATION.cff).

The citation title is **EquWord: Equation Conversion and Formatting for Microsoft Word**. The GitHub integration cannot reserve a DOI before its first release. After the author-approved first release, the actual version DOI will be checked and added to current citation metadata. A Concept DOI can identify the software across versions. The archived tag and released ZIP will be preserved; any later guide revision will be identified explicitly.

### Acknowledgment examples

If EquWord contributed to equation preparation in your manuscript, please consider citing the software in the Acknowledgments or another appropriate section. Cite the version you actually used.

> Equations were prepared in Microsoft Word using EquWord (Version 1.0.0; Cho, 2026).

If you also used ChatGPT for drafting and revision, this optional combined example may be appropriate:

> ChatGPT (OpenAI) assisted with drafting and revision. The authors reviewed the AI-assisted content and take responsibility for the final manuscript. Equations were prepared in Microsoft Word using EquWord (Version 1.0.0; Cho, 2026).

Use only statements that reflect your actual use. Adjust the tools, tasks, software version, and singular or plural author wording as needed.

### Suggested reference

Cho, G. (2026). *EquWord: Equation conversion and formatting for Microsoft Word* (Version 1.0.0) [Computer software]. https://github.com/PsycheMatrica/EquWord

Use the released version's DOI when available.

Microsoft interface elements and product names in screenshots remain the property of Microsoft.

## Release procedure

See [CHANGELOG.md](CHANGELOG.md) and [RELEASING.md](RELEASING.md). Build a review ZIP with `python scripts/build_release.py --output-dir <absolute-new-directory>`. The builder reports pending platform verification. `--publication-check` refuses a candidate without matching native PASS evidence on both platforms, and never publishes anything. Every actual release requires the author's explicit final approval of the exact commit, artifacts, checksums, release notes and tests.
