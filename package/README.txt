EquWord: Equation Conversion and Formatting for Microsoft Word
Version 0.9.27
Installation and quick use

EquWord converts supported LaTeX into editable Word equations and applies saved
notation, font and equation-layout choices. This package contains a Word
template, this guide, its license and citation information, plus an English
screenshot Quick Start PDF and a practice DOCX in Tutorial/.

Research Equation Formatter is the legacy name used inside EquWord 0.9.27.
The tested template filename ResearchEquationFormatter.dotm, macro names and
in-app name remain unchanged. The Quick Start PDF, practice DOCX and license
are also retained unchanged and may display that legacy name. Separate BAS,
CLS and FRM source exports are omitted; the template contains embedded VBA code.

REQUIREMENTS AND RECORDED TESTS

Use desktop Microsoft Word with macros permitted by your normal Word or
organization policy. Word for the web cannot run this VBA template.

The exact V5 template supplied here was tested on:
- Mac: Word 16.113.4 (16.113.26100421), macOS 26.7.2, Apple silicon.
- Windows: Word 16.0.20430.20180, 64-bit, Windows 11 build 26300.

Mac tests covered selection and whole-body LaTeX conversion, fractions, Greek
symbols, intentional inner brackets, an eligible two-row merge, saved-file
preservation checks, save/reopen formatting, and template reload with About in
a fresh Word session. Windows tests also exercised the native format and
selective-reformat commands, document-specific remembered choices, a saved
native equation edit and repeat formatting after a test Word-process restart.

These are results for the supplied fixtures, exact template and recorded
installations. They do not establish compatibility with every Word build or
manuscript, or feature parity for every command on Mac. Large-document
performance, forced over-height/page-boundary stress cases and every notation
or geometry option were not exhaustively tested. Work on copies and review
results before saving.

INSTALL ON WINDOWS

1. Extract EquWord.zip to a folder you will keep.
2. In Word, open File > Options > Add-ins. Under Manage, choose Word Add-ins,
   then Go. In Templates, under Global templates and add-ins, click Add.
3. Select ResearchEquationFormatter.dotm and leave its checkbox selected.
   Unload any older edition to avoid duplicate commands.
4. Open a working copy of your document. Press Alt+F8, choose
   AboutResearchEquationFormatter, then Run. Confirm version 0.9.27.

This loads the template for the current Word session. Load it again after
restarting Word. For automatic loading, place the template in Word's Startup
folder: File > Options > Advanced > General > File Locations shows its location.
Your manuscript can remain a .docx file. To unload, return to the Templates
dialog and clear the template's checkbox.

Windows may block downloaded templates. If you trust this release and your
organization permits it, right-click the extracted .dotm > Properties > Unblock
(if shown), apply and load it again. Otherwise consult your IT administrator.
Do not enable all macros or change VBA-project access settings for this tool.

INSTALL ON MAC

1. Extract EquWord.zip to a folder you will keep, then open desktop Word.
2. Choose Tools > Templates and Add-ins. Under Global templates and add-ins,
   add ResearchEquationFormatter.dotm and select its checkbox. If an older
   edition is selected, unload it to avoid duplicate commands.
3. Open a working copy of your document. Use Word's macro dialog to run
   AboutResearchEquationFormatter and confirm version 0.9.27.
4. Check that the template is loaded again after restarting Word. The recorded
   Mac restart test reloaded it through Tools > Templates and Add-ins.

Menu labels and controls can vary between Word builds. Use your normal macro
policy; do not lower security settings for this tool. The retained Quick Start
PDF uses Windows menus/screenshots, so use these Mac loading steps instead.

Microsoft's Windows template-loading instructions:
https://support.microsoft.com/en-us/word/load-or-unload-a-template-or-add-in-program
Microsoft-hosted guidance identifying the Mac Templates and Add-ins menu:
https://learn.microsoft.com/en-us/answers/questions/5208051/how-do-i-change-the-styles-in-my-template

USE

For a guided first run, open
Tutorial/Research_Equation_Formatter_Quick_Start.pdf, then make a working copy
of Tutorial/REF_Practice.docx and follow the illustrated steps. Both documents
use APA 7 formatting conventions; the practice equations stay editable.

Use Word's macro dialog to choose a command and run it. On Windows, Alt+F8
opens this dialog. First use offers settings saved in the current manuscript.
ConfigureCurrentDocument opens them again.

FormatEquationsInSelection
  Format native equations in the selection, or one equation at the cursor.
FormatAllEquations
  Format native equations throughout the main document body.
ConvertAndFormatLatexInSelection
  Convert supported selected LaTeX, then format equations in that area.
ConvertAndFormatAllLatex
  Convert supported LaTeX and format equations throughout the main body.
SelectiveReformatInSelection
  Apply chosen formatting categories to the selected area.
SelectiveReformatAllEquations
  Apply chosen categories throughout the main body.
ConfigureCurrentDocument
  Review and save this manuscript's settings.
AboutResearchEquationFormatter
  Show the version and this manuscript's settings.

New profiles merge eligible multiline groups with 1.5-line internal spacing.
Existing profiles retain their choices. Equation paragraphs follow body line
spacing. To merge several rows with a selection command, select the complete
group; a cursor inside one row requests single-equation processing.

Selective Reformat separates font/notation, punctuation/spaces, multiline
layout, line spacing, number-table placement and numbered-block pagination.
Select all/Deselect all and the last accepted choices are available. Multiline
layout also applies line spacing. Follow current equation is independent.

Equation-structure, number-field and bookmark preservation checks always run.
The Word caption shows the task and elapsed time. On Windows, Esc requests a
stop at the next safe checkpoint; a current Word operation may delay it.
Completed edits remain. Review results and review notes before saving.

LICENSE AND CITATION

The software and accompanying original documentation are licensed under
CC BY-NC-SA 4.0: https://creativecommons.org/licenses/by-nc-sa/4.0/
Noncommercial sharing and adaptation are permitted under the license.
When redistributing licensed material, retain attribution and license notices,
indicate changes, and share adaptations under the applicable ShareAlike terms.
See LICENSE.txt for the full unchanged license and its application to this
distribution. Its Research Equation Formatter heading identifies the legacy
name of EquWord; the license terms and attribution remain unchanged.

The original instructional text and practice content are included under this
license. Microsoft interface elements and product names shown in screenshots
remain the property of Microsoft; this notice does not relicense them.

Using the tool does not by itself apply this license to your own manuscripts
or equations. Citation in a manuscript is appreciated, but is not required
merely for using the tool. CITATION.cff contains citation information.
Attribution when sharing the software remains subject to the license.

This is a local preparation for the first EquWord public release. The repository
is https://github.com/PsycheMatrica/EquWord. The first GitHub release and Zenodo
publication are pending. No Zenodo DOI or publication date has been assigned
in this preparation.
