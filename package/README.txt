EquWord: Equation Conversion and Formatting for Microsoft Word
Version 1.0.0

EquWord converts supported LaTeX to editable native Word equations and applies
document-specific notation, font and equation-layout choices. Use desktop
Microsoft Word for Windows or Mac with macros permitted by your normal Word
or organization policy. Word for the web cannot run this VBA template.
Work on a copy of your manuscript and review results before saving.

START HERE
Read the Quick Start PDF for your operating system in Tutorial/, then save a
working copy of Tutorial/EquWord_Practice.docx. The template is EquWord.dotm;
its nine public commands begin with EquWord_. No separate BAS, CLS, FRM or
UserForm import is required. VBA source remains embedded in the template.

INSTALL ON WINDOWS - AUTOMATIC STARTUP LOADING
1. Extract EquWord.zip to a folder you will keep.
2. Follow the Windows Quick Start to find this installation's actual Word
   Startup folder. Do not assume another computer uses the same location.
3. Close Word completely, then copy only EquWord.dotm into Startup. Keep the
   guides and practice document in your extracted folder. Preserve an older
   formatter outside Startup to avoid duplicate commands; leave Normal.dotm
   and unrelated templates unchanged.
4. Start Word. Press Alt+F8, run EquWord_About and confirm version 1.0.0.

Windows may block downloaded templates. If you trust this release and your
organization permits it, use the extracted DOTM's Properties > Unblock (if
shown), then load it again. Otherwise consult IT; do not lower Word security.

INSTALL ON MAC - AUTOMATIC STARTUP LOADING
1. Extract EquWord.zip. Follow the Mac Quick Start to find this installation's
   actual Word Startup folder. It shows Word > Preferences > File Locations
   and the read-only fallback used when Startup is blank. Other builds may
   call Preferences Settings; paths vary by user and installation.
2. Quit Word completely, then copy only EquWord.dotm into that Startup folder.
   Preserve older formatter templates outside Startup; leave Normal.dotm and
   unrelated templates unchanged.
3. Start Word. Choose Tools > Macro > Macros (Option+F8; Fn may be needed),
   run EquWord_About and confirm version 1.0.0.

Startup installation makes EquWord available automatically when Word starts,
including for other documents in that Word session. Optional current-session
loading is available through Templates and Add-ins: add EquWord.dotm and keep
it checked. That alternative normally needs repeating after Word restarts.
Your manuscript can remain DOCX. Follow your normal macro policy; do not enable
all macros or change VBA-project access settings for this tool. Reassign older
formatter toolbar/ribbon buttons to the EquWord_ commands below.

COMMANDS
EquWord_Settings                    Review and save this manuscript's settings.
EquWord_About                       Show the loaded version and settings.
EquWord_LastReport                  On Mac, open the last run report on request;
                                   on Windows, show reporting guidance.
EquWord_FormatSelection             Format selected native equations, or one at the cursor.
EquWord_FormatAll                   Format native equations in the main body.
EquWord_ConvertLaTeXSelection        Convert supported selected LaTeX, then format.
EquWord_ConvertLaTeXAll              Convert supported main-body LaTeX, then format.
EquWord_SelectiveReformatSelection  Apply chosen categories to selected equations.
EquWord_SelectiveReformatAll        Apply chosen categories throughout the main body.

New profiles merge eligible adjacent derivation rows with 1.5-line internal
spacing and a 12 pt rightward offset. Equation paragraphs follow body spacing.
Existing manuscript profiles retain their choices. Select the complete group
of equation rows to merge it; a cursor in one row requests single-equation work.
Selective Reformat provides six categories, Select all/Deselect all and
remembered choices. Multiline layout also applies line spacing; Follow current
equation is independent. Structure, number-field and bookmark guards remain on.

Review every result before saving. On Mac, a small progress window shows the
current task, item count and elapsed processing time. Stop, or the progress
window's close button, requests a stop at an existing safe checkpoint. A native
Word operation may delay updates or the stop response. Earlier edits remain in
the working copy. Switching to another document pauses processing; return to
the original document to resume. Follow current equation is a separate view
preference.

Each Mac run ends with one compact results dialog. Detailed timing and review
notes do not open automatically. Run EquWord_LastReport when you want the full
report; it opens as a protected, unsaved Word document and can be closed without
saving. The report belongs to the current Word session; the next run replaces
it. Before the first run, the command shows a short no-report message. Native
Esc polling and automatic standalone log-file saving remain unavailable on Mac.
On Windows, the title bar shows progress and Esc requests a stop at the next
safe checkpoint; the current Word operation may delay the response.

RECORDED VERIFICATION
Exact EquWord.dotm SHA-256:
b7fc3290227b244647fc15a548f683a443f064aa812e0288bdc82ea3d4383a76

This final author-review build changes the Mac progress-window caption to
EquWord - Progress. Its complete main code, Windows processing code and all
49 identified runtime preservation-check procedures match the tested R2
predecessor. The eight form-designer streams also match. Native-generated
form identifiers and two empty source lines were reviewed separately; the
literal audit differences remain recorded, with no executable or designer
defect identified in those bounded differences. No preservation guard was
removed, disabled or relaxed.

Windows: Word 16.0.20430.20180, 64-bit; Windows build 26300. The exact final
template was compiled, saved, closed and reopened in an isolated desktop Word
instance. No fresh equation-processing or form-interaction regression was
performed on these final bytes.

Mac: Word 16.114.3 (26102720); macOS 26.7.2 (25G332), Apple silicon. On the
exact final template, one EquWord_SelectiveReformatSelection invocation opened
the category form with readable controls. Cancel closed it cleanly. Run was
not selected: no equation processing, progress, result or report began. The
owned input closed without saving; the private template was unloaded and the
prior Word/template/source-filter state restored. The Mac evidence recorded
926 unchanged file identities. This was a form-opening/cancellation check,
not a new equation-processing, category-toggle, Startup or full regression.

Earlier Mac processing evidence is kept separate. The integrated R1 predecessor
completed five focused runs covering Selective Reformat Selection, Format All
with document-switch pause/resume, Stop and progress-window close cancellation,
and selected LaTeX conversion with an editable fraction and Greek alpha.
Completed outputs supported merging, alignment, 1.5-line internal spacing and
saved-reference checks within those cases. The R2 predecessor then passed one
Format All/Stop check: one complete result dialog, no repeated or trimmed
summary, one explicit full LastReport, and a saved partial that reopened with
working references. Those processing results remain tied to their predecessor
hashes; they are not a full processing regression of the final template.

Processed-document raw font, style, identifier, field-representation and
package differences remain documented. A separate no-command Word save/reopen
control reproduced specific math-font and unselected-equation changes. It
does not explain every difference or establish the displayed font of every
glyph. Unobtained report typography measurements remain unverified. Original
files and personal customizations were unchanged in the recorded checks.

Results cover supplied fixtures and recorded installations. Every Word build,
manuscript, option, workload and error path has not been exhaustively tested.
EquWord does not assess mathematical correctness or support every LaTeX command.
This package is for the author's final file review; it does not authorize a
release. The repository release manifest records identities and test limits.

DEVELOPMENT ACKNOWLEDGMENT
GPT-6.1 Sol (OpenAI) assisted with developing EquWord and preparing its
accompanying manual. The author reviewed the AI-assisted work and takes
responsibility for the software and documentation.

LICENSE AND CITATION
Copyright (c) 2026 Gyeongcheol Cho. CC BY-NC-SA 4.0; see LICENSE.txt.
Using the tool does not by itself apply this license to your own manuscripts
or equations. Microsoft interface elements shown in screenshots retain their
existing rights. Separate source exports are omitted; VBA source remains
embedded in the DOTM.

Citation for software use is appreciated, not required. Attribution when
sharing licensed material remains subject to the license. CITATION.cff gives
the author, version and title. An optional acknowledgment is:

  Equations were prepared in Microsoft Word using EquWord
  (Version 1.0.0; Cho, 2026).

Use this combined example only if you also used ChatGPT for drafting/revision:

  ChatGPT (OpenAI) assisted with drafting and revision. The authors reviewed
  the AI-assisted content and take responsibility for the final manuscript.
  Equations were prepared in Microsoft Word using EquWord
  (Version 1.0.0; Cho, 2026).

Use only statements reflecting your actual use; adjust tasks and author wording.

Cho, G. (2026). EquWord: Equation conversion and formatting for Microsoft Word
(Version 1.0.0) [Computer software]. https://github.com/PsycheMatrica/EquWord

Use the released version's verified DOI when available. No DOI is preassigned.
