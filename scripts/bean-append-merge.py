#!/usr/bin/env python3
"""Resolve `.beans/*.md` merge conflicts that are pure concurrent APPENDS.

WHY THIS EXISTS
---------------
Beans are an append-only ledger, and several in-flight branches append a
session note to the same bean. Git sees two different additions at the same
end-of-file offset and calls it a conflict every time, even though the
resolution is never in doubt: keep both notes.

Measured on `main`, 2026-09-13:

    main                                  169 commits / 24 h  (~1 per 9 min)
    .beans/qou-brng--...derive-saturated    9 commits / 24 h
    .beans/qou-zlra--...is-graded-binding   6 commits / 24 h

so a branch that appends to `qou-brng` goes un-mergeable roughly every 2.7 h.
In one session, PRs #7237 / #7245 / #7251 / #7253 collided on these two files
five separate times; `qou-brng` alone conflicted three times in ~40 minutes,
twice while a resolution for the previous collision was being committed. Four
of the five collision surfaces across that cluster were these two ledgers.
None of them involved content, Lean, compute or a witness.

WHAT IT REFUSES TO DO
---------------------
It is deliberately narrow, because a bean can also be *edited*, and an edit is
a real conflict that a human must read. It exits 2 without writing anything
unless EVERY unmerged path is:

  * under `.beans/` and ending `.md`, and
  * a PURE APPEND on BOTH sides -- each side's text must literally start with
    the merge-base text, modulo the one `updated_at:` frontmatter line.

So a side that rewrote an existing paragraph, reordered notes, or deleted
anything is never touched. The failure mode is "refuses to help", never
"silently drops someone's edit".

WHAT IT GUARANTEES WHEN IT DOES WRITE
-------------------------------------
The merged file is asserted, before being written, to satisfy all of:

  * `theirs` (main) preserved byte-for-byte as a prefix;
  * `ours` (the branch's) new note present verbatim;
  * `len(merged) == len(theirs) + len(ours_note)` -- nothing invented;
  * exactly one `updated_at:` key, set to the later of the two timestamps.

If any assertion fails it raises rather than writing a half-merged ledger.

USAGE
-----
    git merge origin/main            # conflicts
    python3 scripts/bean-append-merge.py
    git commit

Exit codes: 0 = all conflicts resolved (or none present), 2 = at least one
conflict is not a pure append and needs a human.
"""
import subprocess
import re
import sys


def _show(stage: int, path: str):
    """Return one merge stage of `path`, or None if that stage is absent."""
    r = subprocess.run(["git", "show", f":{stage}:{path}"],
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def _mask_ts(text: str) -> str:
    """Blank the single `updated_at:` line so the append test ignores it."""
    return re.sub(r'^updated_at: .*$', 'updated_at: X', text, count=1, flags=re.M)


def _ts(text: str) -> str:
    m = re.search(r'^updated_at: (.*)$', text, flags=re.M)
    return m.group(1).strip() if m else ""


def main() -> int:
    paths = subprocess.run(["git", "diff", "--name-only", "--diff-filter=U"],
                           capture_output=True, text=True).stdout.split()
    if not paths:
        print("no unmerged paths")
        return 0

    refused = []
    for path in paths:
        if not (path.startswith(".beans/") and path.endswith(".md")):
            refused.append((path, "not a .beans/*.md ledger"))
            continue

        base, ours, theirs = _show(1, path), _show(2, path), _show(3, path)
        if base is None or ours is None or theirs is None:
            refused.append((path, "add/add or delete/modify -- no common base"))
            continue

        b, o, t = _mask_ts(base), _mask_ts(ours), _mask_ts(theirs)
        if not o.startswith(b):
            refused.append((path, "OURS is not a pure append (existing text changed)"))
            continue
        if not t.startswith(b):
            refused.append((path, "THEIRS is not a pure append (existing text changed)"))
            continue

        ours_note = ours[len(ours) - (len(o) - len(b)):]
        merged = re.sub(r'^updated_at: .*$',
                        f'updated_at: {max(_ts(ours), _ts(theirs))}',
                        theirs, count=1, flags=re.M)
        if not merged.endswith("\n"):
            merged += "\n"
        merged += ours_note

        m = _mask_ts(merged)
        assert m.startswith(t), f"{path}: main's text not preserved"
        assert o[len(b):] in m, f"{path}: the branch's note was lost"
        assert len(m) == len(t) + len(o) - len(b), f"{path}: length mismatch -- invented content?"
        assert merged.count("updated_at:") == 1, f"{path}: duplicate updated_at"

        with open(path, "w") as fh:
            fh.write(merged)
        subprocess.run(["git", "add", path], check=True)
        print(f"  resolved (lossless): {path}  [+{len(ours_note)} ch appended]")

    if refused:
        print("\nREFUSED -- these are not pure appends; resolve by hand:")
        for path, why in refused:
            print(f"  {path}: {why}")
        return 2

    print("all bean conflicts resolved")
    return 0


if __name__ == "__main__":
    sys.exit(main())
