# EquWord: Equation Conversion and Formatting for Microsoft Word

EquWord converts supported LaTeX into editable native Word equations and applies notation, font and equation-layout settings saved with a manuscript. It is a macro-enabled template for desktop Microsoft Word on Windows and Mac.

Version **1.0.3**. [Downloads](https://github.com/PsycheMatrica/EquWord/releases). Preferred citation identifier: [all-version Concept DOI](https://doi.org/10.5281/zenodo.23935877).

## Get started

1. Download the **`EquWord.zip` release attachment** from [GitHub Releases](https://github.com/PsycheMatrica/EquWord/releases) and extract it to a folder you will keep. This installation bundle contains only the seven distribution files. The automatically generated **Source code (zip)** is a repository archive, not the installation download.
2. Read the Quick Start PDF for your operating system. The extracted files are `Tutorial/EquWord_Quick_Start_Windows.pdf` and `Tutorial/EquWord_Quick_Start_Mac.pdf`; online copies are available in the [Windows guide](https://github.com/PsycheMatrica/EquWord/blob/main/package/Tutorial/EquWord_Quick_Start_Windows.pdf) and [Mac guide](https://github.com/PsycheMatrica/EquWord/blob/main/package/Tutorial/EquWord_Quick_Start_Mac.pdf).
3. Follow the guide to find your Word installation's actual **Startup** folder. Close Word completely, then copy only `EquWord.dotm` there. Keep the guides and practice document in the extracted folder. Preserve older formatter templates outside Startup to avoid duplicate commands; leave `Normal.dotm` and unrelated add-ins unchanged.
4. Start Word, run `EquWord_About` and confirm version 1.0.3. Save a working copy of `Tutorial/EquWord_Practice.docx`, then review its profile with `EquWord_Settings`. An [online practice copy](https://github.com/PsycheMatrica/EquWord/blob/main/package/Tutorial/EquWord_Practice.docx) is also available.

On **Windows**, Alt+F8 opens the Macros dialog. Windows may block downloaded templates. If you trust this release and your organization permits it, use the extracted DOTM's Properties > Unblock option, if shown, then load it again. Otherwise consult IT; do not lower Word security.

On **Mac**, choose Tools > Macro > Macros or press Option+F8; Fn may be needed. The guide uses Word > Preferences > File Locations and shows a read-only fallback when Startup is blank. Other Word builds may call Preferences Settings. Use the folder reported by your installation; paths vary by user and computer. Quit Word completely before replacing its template.

Startup installation makes the commands available automatically when Word starts, including for other documents in that session. Templates and Add-ins remains an optional current-session method: add `EquWord.dotm` and keep it checked. Loading from outside Startup normally needs repeating after Word restarts. Your manuscript can remain DOCX. No separate BAS, CLS, FRM or UserForm import is needed. Use your normal macro policy; do not enable all macros or change VBA-project access settings. Word for the web cannot execute this template. Reassign older formatter toolbar or Ribbon buttons to the `EquWord_` commands below.

## Set up the current document

Run `EquWord_Settings` to review the 14 document options in **Font and style**, **Tokens**, **Layout and view**, and **Numbering**. Existing settings and saved token lists load when the window opens, including lists intentionally left empty. For a new document, the window starts with the built-in defaults. Hover over or click a field’s **?** button to read its full explanation. Click to keep the explanation open while you read it.

**Save** and **Cancel** stay in place across all four tabs. Save applies the draft to the current document. Save the Word document to keep the profile after closing it. Cancel discards the draft. On the **Tokens** tab, **Use default list** restores the 29 built-in forced-upright tokens to that field in the draft. Save applies the change. Selective Reformat still has its own six categories.

## Features and commands

- Convert supported selected LaTeX or supported source throughout the main document body.
- Format native equations and apply selected categories without repeating every formatting step.
- Apply configured nonbold upright notation tokens in native subscripts and superscripts.
- Format comma spacing in supported native inline confidence intervals. Preserve compact subscript indices and the existing spacing beside brackets written as ordinary Word text.
- Merge eligible adjacent derivation rows, align their main relations and set internal row spacing.
- Apply equation-number placement and keep eligible numbered blocks together.
- Check mathematical structure, number fields and bookmarks during processing.
- On Mac, show task, count and time in a progress window with safe-checkpoint Stop and close controls, followed by one compact result. Open detailed notes only when `EquWord_LastReport` is requested.

New profiles use eligible multiline merging, 1.5-line internal spacing and a 12 pt number offset. Equation paragraphs follow body spacing; existing manuscript profiles retain their choices. Select the complete group of equation rows to merge it; a cursor in one row requests single-equation work. Selective Reformat offers six categories, Select all/Deselect all and remembered choices. Multiline layout also applies line spacing; Follow current equation is independent. EquWord does not determine mathematical correctness, perform statistical analysis or support every LaTeX command. Work on copies and review results before saving.

| Macro | Use |
| --- | --- |
| `EquWord_Settings` | Review the current manuscript’s settings in one window and save its profile. |
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

- Exact 1.0.3 on Windows — **PASS**. Compiled the 1.0.3 VBA project in Word. The compiled VBA project was retained byte-for-byte in the exact release template. Reopened the exact release template read-only in Word; the native About command displayed 1.0.3 and returned. The hash matched after closing Word.
- Exact 1.0.3 on Mac — **PASS**. The native About command displayed 1.0.3. Settings opened at 13 pt with readable Save and Cancel labels. Return at 14 pt kept the form open; after Cancel, reopening Settings showed the original 13 pt. The unsaved fixture closed with its original SHA-256, Word’s prior add-in state was restored, and 22 protected file hashes matched.
  Settings Save, document save and reopen, Return in other fields, and equation processing remain unverified on this exact binary.
- The private Settings predecessor (`77e085e1`) passed focused native Settings save/reopen checks on Windows and Mac. The recorded checks preserved the fixture’s native equations, prose, numbered and reference fields, and bookmarks. The Mac check used Word 16.115.2 in Light appearance and verified Save/Cancel legibility, Return in both tested numeric fields and a reopened reference jump. Word save produced documented XML differences. Exact rendered math-font equivalence on Mac remains unverified.
- The separate confidence-interval and bracket predecessor completed six focused Windows runs and five focused Mac runs with save/reopen checks, including a Windows 22-equation Format All audit. The full original 428-equation manuscript remains unverified.

The version rebuild’s audit verifies that the existing runtime guards and form designer streams are retained. See the [release manifest](https://github.com/PsycheMatrica/EquWord/blob/main/RELEASE_MANIFEST.json) for exact candidate identities, run scopes and qualifications. Older releases retain their own historical records.

## Download contents

The ZIP contains exactly seven files: `EquWord.dotm`, `README.md`, `LICENSE.txt`, `CITATION.cff`, two operating-system Quick Start PDFs, and `Tutorial/EquWord_Practice.docx`. The guides contain three core example illustrations per platform. Screenshot account names are anonymized; Windows equation examples are native Word document excerpts, not screenshots of editing controls.

VBA remains embedded in the DOTM. Separate source exports, editable guide masters, private test files, raw screenshots and logs are outside this distribution and public repository.

## Development acknowledgment

GPT-6.1 Sol (OpenAI) assisted with developing EquWord and preparing its accompanying manual. The author reviewed the AI-assisted work and takes responsibility for the software and documentation.

## License and citation

Copyright (c) 2026 Gyeongcheol Cho. The software and accompanying original documentation are licensed under **CC BY-NC-SA 4.0**; see [LICENSE.txt](LICENSE.txt). Using the tool does not by itself apply that license to your manuscripts or equations. Microsoft interface elements and product names in screenshots retain their existing rights.

You are not required to cite EquWord simply for using it, but a citation would be appreciated. If you choose to cite it, you can include a brief statement in your manuscript’s Acknowledgments section, for example:

> Equations were prepared in Microsoft Word using EquWord (Version 1.0.3; Cho, 2026).

If you also used ChatGPT for drafting and revision, this optional combined example may be appropriate:

> ChatGPT (OpenAI) assisted with drafting and revision. The authors reviewed the AI-assisted content and take responsibility for the final manuscript. Equations were prepared in Microsoft Word using EquWord (Version 1.0.3; Cho, 2026).

Use only statements that reflect your actual use. Adjust the tasks, tools, version and singular or plural author wording as needed. Cite the version actually used; see [CITATION.cff](CITATION.cff) for citation metadata.

Attribution conditions still apply when sharing licensed material; see [LICENSE.txt](LICENSE.txt).

Cho, G. (2026). *EquWord: Equation conversion and formatting for Microsoft Word* (Version 1.0.3) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.23935877

Use the [Concept DOI](https://doi.org/10.5281/zenodo.23935877) for citations across releases, while stating the version actually used. The published 1.0.0 tag, ZIP and Zenodo record remain unchanged; their historical identities are retained in the [publication receipt](https://github.com/PsycheMatrica/EquWord/blob/main/RELEASE_RECEIPT.json).

## Maintenance

The repository-root `README.md` is the single maintained source for this document. The package contains an automatically synchronized copy. See the [development workflow](https://github.com/PsycheMatrica/EquWord/blob/main/WORKFLOW.md) and [release procedure](https://github.com/PsycheMatrica/EquWord/blob/main/RELEASING.md). The packaging helper checks the exact seven members, README/source equality, recorded platform evidence and archive identity; it never executes Word or publishes anything.
