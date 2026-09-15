#!/usr/bin/env python3
"""
check_structure.py - verifies the SimplyPpl folder matches the locked
file map in BUILD_RULES.md / brief section 26.

Run it from inside the SimplyPpl folder:

    python3 check_structure.py

Exit code 0 = matches exactly. Exit code 1 = something is missing, extra,
or in the wrong place - read the report before accepting the change.

This checks *shape*, not content: it won't tell you if Ppl's wording
drifted, but it will catch a file appearing somewhere it shouldn't, a
file going missing, or an app quietly growing extra files it hasn't
earned yet (rule 5).
"""

import os
import sys

# The locked map - section 26 of the build brief. Any change to this
# list is itself a deliberate, named decision (rule 10), not something
# to edit casually because a build added an extra file.
LOCKED_FILES = {
    "index.html",
    "BUILD_RULES.md",
    "check_structure.py",
    "business/index.html",
    "business/my-team/index.html",
    "business/ppl/index.html",
    "business/reminders/index.html",
    "business/meetings/index.html",
    "business/records/index.html",
    "community/index.html",
    "community/my-team/index.html",
    "community/meetings/index.html",
    "community/reminders/index.html",
    "community/records/index.html",
}

# Folders allowed to hold more than one file once an app has genuinely
# earned the complexity (rule 5/6). Empty for now - nothing has earned
# it yet. Add an entry here only as a deliberate decision, e.g.:
#   "business/ppl": {"index.html", "app.js", "styles.css"}
EARNED_COMPLEXITY = {}


def scan(root):
    found = set()
    for dirpath, dirnames, filenames in os.walk(root):
        # ignore hidden/system folders (git, etc.)
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for name in filenames:
            if name.startswith("."):
                continue
            rel = os.path.relpath(os.path.join(dirpath, name), root)
            found.add(rel.replace(os.sep, "/"))
    return found


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    found = scan(root)

    missing = LOCKED_FILES - found
    extra = found - LOCKED_FILES

    # allow extra files only inside folders that have earned complexity
    real_extra = set()
    for path in extra:
        folder = os.path.dirname(path)
        allowed = EARNED_COMPLEXITY.get(folder, set())
        if os.path.basename(path) not in allowed:
            real_extra.add(path)

    ok = not missing and not real_extra

    print(f"Checked: {root}")
    print(f"Locked files expected: {len(LOCKED_FILES)}")
    print(f"Files found: {len(found)}")
    print()

    if missing:
        print("MISSING (in the locked map, not on disk):")
        for m in sorted(missing):
            print(f"  - {m}")
        print()

    if real_extra:
        print("UNEXPECTED (on disk, not in the locked map or earned complexity):")
        for e in sorted(real_extra):
            print(f"  - {e}")
        print()

    if ok:
        print("MATCH - structure is exactly the locked map.")
    else:
        print("MISMATCH - review before accepting this change (rule 11).")

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()