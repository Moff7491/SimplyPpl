# SimplyPpl - Build SOP (never broken)

This file is the standing rule set for anyone - human or AI - making changes
to this repo. If a suggested change conflicts with this file, this file wins.
If this file needs to change, that is itself a deliberate, discussed change  - 
not something that happens as a side effect of another task.

## 1. One deliberate change at a time
No bundling. A request to fix Ppl does not become an opportunity to also
tidy Records. If something else looks wrong while working, it gets named,
not silently fixed.

## 2. Complete files, never fragments
Any file that changes is delivered whole - full content, not a diff to
mentally apply, not "add this snippet somewhere near the top." A file you
can't paste in and immediately have working is not a finished piece of work.

## 3. Branches are untouchable unless named
Fixing `business/` never touches `community/`, and the reverse. Fixing
`business/ppl/` never touches `business/records/`. Scope is the single
folder or file named in the request - nothing wider - unless the person
explicitly asks for wider scope.

## 4. Destructive commands are scoped and explicit
Before any delete/overwrite, the scope is stated in plain language first.
A command like `Remove-Item ".\business" -Recurse -Force` means Business
only - never bundled with another folder "while we're at it."

## 5. No infrastructure ahead of need
An app starts as a single `index.html`. `app.js` / `styles.css` /
`data/` / `functions/` get added only once real behaviour requires them  - 
not because a "proper app" is assumed to need them.

## 6. Size is not the problem - accidental complexity is
100-250 lines in one file is fine. Split into multiple files only when a
file is doing real, substantial work at 400-500+ lines. Splitting for its
own sake is not allowed.

## 7. Build order: navigation before behaviour
Prove the whole skeleton works - every launcher, every card, every "back"
link - before any single app gets real functionality. Don't build member
databases, reminder engines, and meeting logic all at once. One app becomes
real at a time, starting with Business -> Ppl.

## 8. Human First stays invisible
The person using SimplyPpl never sees "AI," "LLM," "workflow engine,"
"agent," "automation," or similar. They see plain questions: what happened,
what needs doing, who's involved, what's next, what was decided. Any
intelligence involved is backroom plumbing, never the interface.

## 9. Plain language only
No "Human Capital Management," "Employee Lifecycle," "Workflow
Orchestration," "Compliance Hub," or similar software-vendor language,
inside the product or in naming. Ordinary words: People, Meetings,
Records, Reminders, My Team.

## 10. The architecture is locked until deliberately reopened
The file map in section 26 of the build brief (root -> business/community ->
their five/four apps) is the agreed structure. Changing it is a named,
discussed decision - not something that happens as a byproduct of building
one app's functionality.

## 11. Verify before handing over
Before any build is delivered, the structure is checked against this SOP
and the locked file map - not assumed correct because it was generated
carefully. A directory listing or diff against the last known-good state
should back up any claim that "this is what changed."