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
its eight public commands begin with EquWord_. No separate BAS, CLS, FRM or
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

Review every result and note before saving. On Mac, review notes can span
several dialogs when a separate full-log file cannot be saved; native Esc
polling is unavailable. On Windows, Esc requests a stop at the next safe
checkpoint, which the current Word operation may delay.

RECORDED VERIFICATION
Exact EquWord.dotm SHA-256:
3e876985b016db8e0bb242b57a2036aeb80ebc720201410e0e32698ece583a13

Windows: Word 16.0.20430.20180, 64-bit; Windows 11 build 26300. All seven
settings/processing commands completed native runs on supplied fixtures and
were saved, closed and reopened. About was confirmed in the native interface.
These checks covered both conversion commands, native formatting and Selective
Reformat, with mathematical/prose/SEQ/REF/bookmark/PAGE preservation checks.

Mac: Word 16.114.3 (26102720); macOS 26.7.2, Apple silicon. The exact branded
candidate passed focused Selection and All Selective Reformat runs with all
six categories (80.9 s and 135.5 s). Both passed two-row merging, 1.5-line
internal spacing, preservation and native save-close-reopen; reference-link
navigation worked. Startup automatic loading after Word restart, About and
Settings were also checked. Separate automatic full-log saving was unavailable;
all 18/20 pages of fallback review notes were retained in the private evidence.
The other four processing commands were listed, not rerun in that focused Mac
check. Earlier broader conversion/editing tests are predecessor evidence,
not a full regression suite on this later binary.

Results apply to the supplied fixtures and recorded installations. Every
Word build, manuscript, setting combination, large-document workload and
over-height page case has not been exhaustively tested. EquWord does not
assess mathematical correctness or implement every LaTeX command.

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
