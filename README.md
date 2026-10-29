# EquWord: Equation Conversion and Formatting for Microsoft Word

EquWord converts supported LaTeX into editable native Word equations and applies notation, font and equation-layout settings saved with a manuscript. It is a macro-enabled template for desktop Microsoft Word on Windows and Mac.

Version **1.0.0** is prepared for final author review. No public release or Zenodo DOI is assigned by this preparation. Every release requires the author's explicit final confirmation of the exact commit, files, checksums, notes and recorded test scope.

## Get started

1. When the approved release is available, download `EquWord.zip` from [GitHub Releases](https://github.com/PsycheMatrica/EquWord/releases) and extract it.
2. Read [README.txt](package/README.txt) and choose the [Windows Quick Start](package/Tutorial/EquWord_Quick_Start_Windows.pdf) or [Mac Quick Start](package/Tutorial/EquWord_Quick_Start_Mac.pdf).
3. Follow that guide to find Word's actual **Startup** folder. Close Word completely and copy only `EquWord.dotm` there. Preserve older formatter templates outside Startup; leave `Normal.dotm` and unrelated add-ins unchanged.
4. Start Word, run `EquWord_About` and confirm version 1.0.0. Save a working copy of [EquWord_Practice.docx](package/Tutorial/EquWord_Practice.docx), then review its profile with `EquWord_Settings`.

Startup installation makes the commands available automatically when Word starts. Templates and Add-ins remains an optional current-session loading method. No separate BAS, CLS or UserForm import is needed. Use your normal macro policy; do not enable all macros or change VBA-project access settings. Word for the web cannot execute this template.

## Features and commands

- Convert supported selected LaTeX or supported source throughout the main document body.
- Format native equations and apply selected categories without repeating every formatting step.
- Merge eligible adjacent derivation rows, align their main relations and set internal row spacing.
- Apply equation-number placement and keep eligible numbered blocks together.
- Check mathematical structure, number fields and bookmarks during processing.

New profiles use eligible multiline merging, 1.5-line internal spacing and a 12 pt number offset. Equation paragraphs follow body spacing; existing manuscript profiles retain their choices. Selective Reformat offers six categories, Select all/Deselect all and remembered choices. Follow current equation is separate. EquWord does not determine mathematical correctness, perform statistical analysis or support every LaTeX command. Work on copies and review results before saving.

| Macro | Use |
| --- | --- |
| `EquWord_Settings` | Review and save the current manuscript's settings. |
| `EquWord_About` | Show the loaded version and active settings. |
| `EquWord_FormatSelection` | Format selected native equations, or one at the cursor. |
| `EquWord_FormatAll` | Format native equations in the main document body. |
| `EquWord_ConvertLaTeXSelection` | Convert supported selected source, then format. |
| `EquWord_ConvertLaTeXAll` | Convert supported main-body source, then format. |
| `EquWord_SelectiveReformatSelection` | Apply selected categories to the selected equations. |
| `EquWord_SelectiveReformatAll` | Apply selected categories throughout the main body. |

## Recorded verification

The exact template SHA-256 is `3e876985b016db8e0bb242b57a2036aeb80ebc720201410e0e32698ece583a13`.

| Platform | Recorded environment | Verification of these candidate bytes |
| --- | --- | --- |
| Windows | Word 16.0.20430.20180, 64-bit; Windows 11 build 26300 | Seven settings/processing commands completed native runs with save, close and reopen. About was confirmed in the native interface. |
| Mac | Word 16.114.3 (26102720); macOS 26.7.2 (25G332), Apple silicon | Focused Selection and All Selective Reformat runs with all six categories passed, with merging, 1.5-line spacing, preservation and save/close/reopen. Startup loading after restart, About, Settings and reference navigation were also checked. |

The focused Mac runs took 80.9 and 135.5 seconds. The other four processing commands were listed, not rerun in that check. Separate automatic full-log saving was unavailable; all 18/20 pages of fallback review notes were retained privately. Mac does not provide Windows-style Esc polling. No fresh Windows Startup autoload/restart check is claimed for this branded candidate.

Earlier broader conversion/editing tests are predecessor evidence, not a full regression suite on every later binary. These results cover supplied fixtures and recorded installations; every Word build, manuscript, setting combination, large-document workload and over-height page case has not been tested. See the sanitized [release manifest](RELEASE_MANIFEST.json) for exact identities and scope.

## Download contents

The ZIP contains exactly seven files: `EquWord.dotm`, `README.txt`, `LICENSE.txt`, `CITATION.cff`, two operating-system Quick Start PDFs, and `Tutorial/EquWord_Practice.docx`. The guides contain three core example illustrations per platform. Screenshot account names are anonymized; Windows equation examples are native Word document excerpts, not screenshots of editing controls.

VBA remains embedded in the DOTM. Separate source exports, editable guide masters, private test files, raw screenshots and logs are outside this distribution and public repository.

## Development acknowledgment

GPT-6.1 Sol (OpenAI) assisted with developing EquWord and preparing its accompanying manual. The author reviewed the AI-assisted work and takes responsibility for the software and documentation.

## License and citation

Copyright (c) 2026 Gyeongcheol Cho. The software and accompanying original documentation are licensed under **CC BY-NC-SA 4.0**; see [LICENSE.txt](LICENSE.txt). Using the tool does not by itself apply that license to your manuscripts or equations. Microsoft interface elements and product names in screenshots retain their existing rights.

Citation in a manuscript is appreciated but is not required merely for using the tool. Attribution conditions still apply when sharing licensed material. See [CITATION.cff](CITATION.cff). Cite the version actually used in the Acknowledgments or another appropriate section.

> Equations were prepared in Microsoft Word using EquWord (Version 1.0.0; Cho, 2026).

If you also used ChatGPT for drafting and revision, this optional combined example may be appropriate:

> ChatGPT (OpenAI) assisted with drafting and revision. The authors reviewed the AI-assisted content and take responsibility for the final manuscript. Equations were prepared in Microsoft Word using EquWord (Version 1.0.0; Cho, 2026).

Use only statements that reflect your actual use. Adjust the tasks, tools, version and singular or plural author wording as needed.

Cho, G. (2026). *EquWord: Equation conversion and formatting for Microsoft Word* (Version 1.0.0) [Computer software]. https://github.com/PsycheMatrica/EquWord

Use the released version's verified DOI when available. After an author-approved GitHub release is archived by Zenodo, verify the actual version and Concept DOIs before updating citation or website metadata. Preserve released tags and assets.

## Maintenance

The public checkout is separate from private development; see [WORKFLOW.md](WORKFLOW.md). [RELEASING.md](RELEASING.md) describes preparation and final author approval. The packaging helper checks the exact seven members, recorded platform evidence and approved archive identity; it never executes Word or publishes anything.
