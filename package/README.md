# EquWord: Equation Conversion and Formatting for Microsoft Word

EquWord converts supported LaTeX into editable native Word equations and applies notation, font and equation-layout settings saved with a manuscript. It is a macro-enabled template for desktop Microsoft Word on Windows and Mac.

Version **1.0.2**. [Downloads](https://github.com/PsycheMatrica/EquWord/releases). Preferred citation identifier: [all-version Concept DOI](https://doi.org/10.5281/zenodo.23935877).

## Get started

1. Download the **`EquWord.zip` release attachment** from [GitHub Releases](https://github.com/PsycheMatrica/EquWord/releases) and extract it to a folder you will keep. This installation bundle contains only the seven distribution files. The automatically generated **Source code (zip)** is a repository archive, not the installation download.
2. Read the Quick Start PDF for your operating system. The extracted files are `Tutorial/EquWord_Quick_Start_Windows.pdf` and `Tutorial/EquWord_Quick_Start_Mac.pdf`; online copies are available in the [Windows guide](https://github.com/PsycheMatrica/EquWord/blob/main/package/Tutorial/EquWord_Quick_Start_Windows.pdf) and [Mac guide](https://github.com/PsycheMatrica/EquWord/blob/main/package/Tutorial/EquWord_Quick_Start_Mac.pdf).
3. Follow the guide to find your Word installation's actual **Startup** folder. Close Word completely, then copy only `EquWord.dotm` there. Keep the guides and practice document in the extracted folder. Preserve older formatter templates outside Startup to avoid duplicate commands; leave `Normal.dotm` and unrelated add-ins unchanged.
4. Start Word, run `EquWord_About` and confirm version 1.0.2. Save a working copy of `Tutorial/EquWord_Practice.docx`, then review its profile with `EquWord_Settings`. An [online practice copy](https://github.com/PsycheMatrica/EquWord/blob/main/package/Tutorial/EquWord_Practice.docx) is also available.

On **Windows**, Alt+F8 opens the Macros dialog. Windows may block downloaded templates. If you trust this release and your organization permits it, use the extracted DOTM's Properties > Unblock option, if shown, then load it again. Otherwise consult IT; do not lower Word security.

On **Mac**, choose Tools > Macro > Macros or press Option+F8; Fn may be needed. The guide uses Word > Preferences > File Locations and shows a read-only fallback when Startup is blank. Other Word builds may call Preferences Settings. Use the folder reported by your installation; paths vary by user and computer. Quit Word completely before replacing its template.

Startup installation makes the commands available automatically when Word starts, including for other documents in that session. Templates and Add-ins remains an optional current-session method: add `EquWord.dotm` and keep it checked. Loading from outside Startup normally needs repeating after Word restarts. Your manuscript can remain DOCX. No separate BAS, CLS, FRM or UserForm import is needed. Use your normal macro policy; do not enable all macros or change VBA-project access settings. Word for the web cannot execute this template. Reassign older formatter toolbar or Ribbon buttons to the `EquWord_` commands below.

## Features and commands

- Convert supported selected LaTeX or supported source throughout the main document body.
- Format native equations and apply selected categories without repeating every formatting step.
- Apply configured nonbold upright notation tokens in native subscripts and superscripts.
- Merge eligible adjacent derivation rows, align their main relations and set internal row spacing.
- Apply equation-number placement and keep eligible numbered blocks together.
- Check mathematical structure, number fields and bookmarks during processing.
- On Mac, show task, count and time in a progress window with safe-checkpoint Stop and close controls, followed by one compact result. Open detailed notes only when `EquWord_LastReport` is requested.

New profiles use eligible multiline merging, 1.5-line internal spacing and a 12 pt number offset. Equation paragraphs follow body spacing; existing manuscript profiles retain their choices. Select the complete group of equation rows to merge it; a cursor in one row requests single-equation work. Selective Reformat offers six categories, Select all/Deselect all and remembered choices. Multiline layout also applies line spacing; Follow current equation is independent. EquWord does not determine mathematical correctness, perform statistical analysis or support every LaTeX command. Work on copies and review results before saving.

| Macro | Use |
| --- | --- |
| `EquWord_Settings` | Review and save the current manuscript's settings. |
| `EquWord_About` | Show the loaded version and active settings. |
| `EquWord_LastReport` | On Mac, open the last run report on request; on Windows, show reporting guidance. |
| `EquWord_FormatSelection` | Format selected native equations, or one at the cursor. |
| `EquWord_FormatAll` | Format native equations in the main document body. |
| `EquWord_ConvertLaTeXSelection` | Convert supported selected source, then format. |
| `EquWord_ConvertLaTeXAll` | Convert supported main-body source, then format. |
| `EquWord_SelectiveReformatSelection` | Apply selected categories to the selected equations. |
| `EquWord_SelectiveReformatAll` | Apply selected categories throughout the main body. |

## Progress and reports

On Mac, the progress window shows the current task, item count and elapsed processing time. Stop, or the window's close button, requests a stop at an existing safe checkpoint. A native Word operation may delay updates or stopping. Earlier edits remain in the working copy. Switching to another document pauses processing; return to the original document to resume. Follow current equation is a separate view preference.

Each Mac run ends with one compact result dialog. Detailed timing and review notes do not open automatically. Run `EquWord_LastReport` for the full report, which opens as a protected, unsaved Word document and can be closed without saving. It belongs to the current Word session; the next run replaces it. Before the first run, the command shows a short no-report message. Native Esc polling and automatic standalone log-file saving remain unavailable on Mac.

On Windows, the title bar shows progress and Esc requests a stop at the next safe checkpoint. The current Word operation may delay the response. Review every result before saving.

## Recorded verification

Version 1.0.2 includes two changes tested in private Windows builds. A guarded native-equation reader accepts the proved plain-run/manual-break projection seen in A3. The configured nonbold upright token list applies to native superscripts as well as subscripts, including combined scripts and prescripts. Matching remains case-sensitive and whole-token based. Preserved tokens take precedence, bold tokens retain their existing rules, and operator limits keep their usual notation rules. Existing manuscript profiles retain their saved token lists.

The final 1.0.2 DOTM identity and native version-confirmation evidence are recorded in the release manifest. Its code differs from the focused 1.0.1 private build only in the version comment and constant. The audit preserves all 414 procedure bodies, 63 identified guard procedures and both form designer resources. Native Windows compilation, the actual About display and a read-only reopen confirmed the final version and unchanged candidate identity.

| Platform and build | Recorded scope |
| --- | --- |
| Windows, focused script-token predecessor | Word 16.0.20527 compiled the retained code and ran Format All on 22 examples in 94.309 seconds. All 33 notation probes passed, covering true sub/superscripts, combined and pre-scripts, nesting, Latin/Greek and multi-letter tokens, bold/Preserved precedence, body tokens and operator limits. Saved/reopened files retained mathematical structure, prose, SEQ/REF/PAGE fields, displayed values, bookmarks and authored links. |
| Windows, A3 predecessor | Word 16.0.20430 completed the three-row A3 selection in 78.320 seconds and merged it into one editable array. Saved/reopened-file checks retained mathematical content, 116 SEQ fields, 171 REF fields, a header PAGE field, 115 bookmark pairs and surrounding content. |
| Windows, exact 1.0.2 template | Word 16.0.20527 compiled the retained VBA. The final preserved-container DOTM reopened read-only, displayed 1.0.2 in EquWord_About and closed with its checksum unchanged. All 15 baseline non-VBA package parts and the native compiled VBA were retained exactly. No duplicate processing regression was performed solely for the two version declarations. |
| Mac, exact 1.0.2 template | **UNVERIFIED**. The author explicitly waived a Mac rerun for this candidate on November 25, 2026, accepting the recorded predecessor Mac evidence, focused Windows tests and matching source audit. Earlier Mac evidence remains predecessor evidence. |
| Mac, earlier integrated builds | Recorded focused checks covered selective merge/spacing, document pause/resume, Stop/progress-window close, editable LaTeX conversion, compact results, explicit LastReport, saved results and reference links. These checks were performed on earlier binaries. |

The source audit verifies the retained preservation/native-read guard procedures and both form designer resources. Word's regenerated hidden form identifiers and package serialization differences remain disclosed in the manifest. Saved-document verification resolves inherited fonts, equivalent simple/complex fields, default separator-only notes and reassigned relationship IDs while checking authored content and links. Initial strict comparisons are retained with those qualifications.

The packaging helper checks the exact candidate, focused predecessor and audit identities for the author's scoped Mac decision. Mac execution remains UNVERIFIED. Packaging and recorded evidence do not replace final author approval. Results cover the supplied fixtures and installations rather than every Word build, manuscript, workload or error path. See the sanitized [release manifest](https://github.com/PsycheMatrica/EquWord/blob/main/RELEASE_MANIFEST.json) for identities and actual scope.

About retains a pre-existing minor wording discrepancy that names `README.txt`. The distribution supplies `README.md`. The Quick Starts and Practice identify version 1.0.2. Genuine installation screenshots retain earlier version labels where the demonstrated controls are unchanged.

## Download contents

The ZIP contains exactly seven files: `EquWord.dotm`, `README.md`, `LICENSE.txt`, `CITATION.cff`, two operating-system Quick Start PDFs, and `Tutorial/EquWord_Practice.docx`. The guides contain three core example illustrations per platform. Screenshot account names are anonymized; Windows equation examples are native Word document excerpts, not screenshots of editing controls.

VBA remains embedded in the DOTM. Separate source exports, editable guide masters, private test files, raw screenshots and logs are outside this distribution and public repository.

## Development acknowledgment

GPT-6.1 Sol (OpenAI) assisted with developing EquWord and preparing its accompanying manual. The author reviewed the AI-assisted work and takes responsibility for the software and documentation.

## License and citation

Copyright (c) 2026 Gyeongcheol Cho. The software and accompanying original documentation are licensed under **CC BY-NC-SA 4.0**; see [LICENSE.txt](LICENSE.txt). Using the tool does not by itself apply that license to your manuscripts or equations. Microsoft interface elements and product names in screenshots retain their existing rights.

You are not required to cite EquWord simply for using it, but a citation would be appreciated. If you choose to cite it, you can include a brief statement in your manuscript’s Acknowledgments section, for example:

> Equations were prepared in Microsoft Word using EquWord (Version 1.0.2; Cho, 2026).

If you also used ChatGPT for drafting and revision, this optional combined example may be appropriate:

> ChatGPT (OpenAI) assisted with drafting and revision. The authors reviewed the AI-assisted content and take responsibility for the final manuscript. Equations were prepared in Microsoft Word using EquWord (Version 1.0.2; Cho, 2026).

Use only statements that reflect your actual use. Adjust the tasks, tools, version and singular or plural author wording as needed. Cite the version actually used; see [CITATION.cff](CITATION.cff) for citation metadata.

Attribution conditions still apply when sharing licensed material; see [LICENSE.txt](LICENSE.txt).

Cho, G. (2026). *EquWord: Equation conversion and formatting for Microsoft Word* (Version 1.0.2) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.23935877

Use the [Concept DOI](https://doi.org/10.5281/zenodo.23935877) for citations across releases, while stating the version actually used. The published 1.0.0 tag, ZIP and Zenodo record remain unchanged; their historical identities are retained in the [publication receipt](https://github.com/PsycheMatrica/EquWord/blob/main/RELEASE_RECEIPT.json).

## Maintenance

The repository-root `README.md` is the single maintained source for this document. The package contains an automatically synchronized copy. See the [development workflow](https://github.com/PsycheMatrica/EquWord/blob/main/WORKFLOW.md) and [release procedure](https://github.com/PsycheMatrica/EquWord/blob/main/RELEASING.md). The packaging helper checks the exact seven members, README/source equality, recorded platform evidence and archive identity; it never executes Word or publishes anything.
