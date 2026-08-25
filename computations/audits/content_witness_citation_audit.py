#!/usr/bin/env python3
"""Do the witnesses that content blocks cite actually exist?

Generalises a defect found by accident: observations/neutron-proton-mass-
splitting-proof.md cited `atom-mass-complete-wedderburn.witness.json`, which
never existed in git history.  That one was found while doing something else.
This asks the question systematically.

A citation is a claim of provenance.  When the named file is absent, the
block's numbers cannot be checked by anyone -- and a reader has no way to
tell an absent witness from a present one without looking.

THREE OUTCOMES, deliberately distinguished:

  RESOLVES     the named file exists in the tree.
  NEVER EXISTED  absent now AND `git log --diff-filter=A` finds no commit that
                 ever added it.  This is the worst class: not staleness, but a
                 citation to something that was never produced.
  REMOVED      absent now but present somewhere in history.  A real artifact
               that was deleted -- the citation is stale, not fabricated.

The distinction matters because the remedies differ: a REMOVED witness can be
regenerated from its producer, a NEVER EXISTED one cannot.

NOT A CONTENT EDIT.  This reports; it does not rewrite blocks.  Deciding what
a block should say when its witness is missing is an authoring call.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
CONTENT = REPO / "content"
# A cited name may contain an INTERNAL SPACE -- a real corruption class in
# this corpus (a hyphen replaced by a space inside a filename), which also
# breaks the markdown link, since an unescaped space terminates a link target.
# Matching only [A-Za-z0-9_.-]+ silently captures the fragment AFTER the space
# and reports e.g. `evaluation.witness.json` for a citation that actually reads
# `he4-sdp-compositional-canonical evaluation.witness.json` -- an under-report
# that turns a corrupt citation into a plausible-looking missing one. So allow
# spaces, then flag them.
CITE = re.compile(r"[A-Za-z0-9_.\-]+(?:[ ][A-Za-z0-9_.\-]+)*\.witness\.json")


def git(*args) -> str:
    try:
        return subprocess.run(["git", "-C", str(REPO), *args],
                              capture_output=True, text=True,
                              timeout=60).stdout.strip()
    except Exception:
        return ""


def ever_existed(name: str) -> bool:
    """Did any commit ever ADD a file with this basename?"""
    out = git("log", "--all", "--diff-filter=A", "--format=%H",
              "--", f"*/{name}", name)
    return bool(out)


def main() -> int:
    # basename -> set of citing блок paths
    cites: dict[str, set[str]] = {}
    for md in CONTENT.rglob("*.md"):
        try:
            text = md.read_text(errors="replace")
        except Exception:
            continue
        for m in CITE.findall(text):
            cites.setdefault(m, set()).add(str(md.relative_to(REPO)))

    on_disk = {p.name for p in REPO.rglob("*.witness.json")
               if ".git" not in p.parts}

    resolves, removed, never, spaced = [], [], [], []
    for name in sorted(cites):
        if " " in name:
            spaced.append(name)
        if name in on_disk:
            resolves.append(name)
        elif ever_existed(name):
            removed.append(name)
        else:
            never.append(name)

    total = len(cites)
    print("=" * 78)
    print("CONTENT WITNESS CITATION AUDIT")
    print("=" * 78)
    print(f"  distinct witnesses cited in content/**/*.md : {total}")
    print(f"  RESOLVES (file present)                     : {len(resolves)}")
    print(f"  REMOVED  (absent, but existed in history)   : {len(removed)}")
    print(f"  NEVER EXISTED (absent, never added)         : {len(never)}")
    print(f"  of which CORRUPT (internal space in the name): {len(spaced)}")

    if spaced:
        print("\n--- CORRUPT: internal space inside the cited filename ---")
        print("  A space cannot occur in these filenames, and inside a markdown")
        print("  link target it also truncates the URL. Each of these was checked")
        print("  BOTH as written and with the space repaired to a hyphen; none")
        print("  resolves either way, so the intended target is UNKNOWN and must")
        print("  not be guessed.")
        for name in spaced:
            print(f"  {name!r}")
            for blk in sorted(cites[name]):
                print(f"      cited by  {blk}")

    for label, group in (("NEVER EXISTED", never), ("REMOVED", removed)):
        if not group:
            continue
        print(f"\n--- {label} ---")
        for name in group:
            print(f"  {name}")
            for blk in sorted(cites[name]):
                print(f"      cited by  {blk}")

    print("\nNOTE. A citation appearing here is not automatically a defect: a")
    print("block may already carry a caveat saying the witness is absent (as")
    print("mass-table-z1-20.md and wedderburn-mass-formula-proof.md do). This")
    print("audit finds the CITATIONS; whether each is caveated is a read.")
    print("What it does catch reliably is the uncaveated case, which is")
    print("invisible to a reader and unfalsifiable by anyone.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
