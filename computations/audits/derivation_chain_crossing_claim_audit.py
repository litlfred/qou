#!/usr/bin/env python3
"""Guard: the atom derivation chains must not claim a CROSSING NUMBER.

WHY THIS EXISTS (bean `qou-1ucq`)
---------------------------------
`atom_braid_word_3A` returns a list of HECKE ELEMENTS. Its own step 4 in these
same chain documents states the object is not in the image of rho and so "has
no crossing number, no volume and no genus" -- 2 of the 11 letters in each A=1
word, and 5 of the 23 in the deuteron, lie outside rho(B_n).

A 2026-08-30 pass corrected step 4 of each chain and left "N crossings"
standing in OTHER steps of the SAME files: 7 surviving claims across 5 of the 6
documents, so a reader met the disclaimer and the contradicted claim in one
file. That partial drain is the failure this guard exists to prevent -- fixing
a wrong statement in one place and leaving it in four others is the single most
repeated defect in this corpus.

WHAT THIS CHECKS
----------------
Every `<atom>-tr-M-q0` and `markov-trace-assembly-<atom>` chain, for any string
asserting "<N> crossing(s)". Two exemptions, both narrow and both required:

  * text that is the DISCLAIMER itself, or the record of a SUPERSEDED premise
    (both necessarily quote the wording they retract -- "previously read",
    "no crossing number", "not crossings", "SUPERSEDED PREMISE",
    "used to assume"). A repaired step keeps the old premise on the record
    rather than deleting it, so the exemption has to cover that too; without
    it, repairing a step makes this audit fail on the repair;
  * text carrying an explicit unrepaired-flag marker, which is an honest record
    of a known-open premise error rather than a silent claim.

Everything else is a live claim and fails. The exemptions are matched on the
surrounding context, not on the whole field, so a disclaimer at the top of a
long note cannot launder a fresh claim at the bottom of it.

NO FLOAT64: this audit reads text; it computes no numbers.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHAINS = [f"{a}-tr-M-q0.derivation.json" for a in ("p", "n", "D")] + [
    f"markov-trace-assembly-{a}.derivation.json"
    for a in ("proton", "neutron", "deuteron")
]

_CLAIM = re.compile(r"(\d+)\s+crossings?\b", re.I)
_DISCLAIMER = ("previously read", "no crossing number", "not crossings",
               "SUPERSEDED PREMISE", "used to assume")
_FLAGGED = ("not repaired", "NOT repaired")
_WINDOW = 95  # chars of context either side that an exemption may cover


def scan(path: Path):
    """(live claims, flagged claims) for one chain document."""
    doc = json.loads(path.read_text())
    live, flagged = [], []
    for i, step in enumerate(doc.get("steps", [])):
        for field, val in step.items():
            if not isinstance(val, str):
                continue
            for m in _CLAIM.finditer(val):
                ctx = val[max(0, m.start() - _WINDOW): m.end() + 55]
                if any(t in ctx for t in _DISCLAIMER):
                    continue
                row = (i, step.get("name", "?")[:44], field, ctx.replace("\n", " ").strip())
                (flagged if any(t in ctx for t in _FLAGGED) else live).append(row)
    return live, flagged


def main() -> int:
    total_live = total_flagged = 0
    for name in CHAINS:
        p = ROOT / name
        if not p.exists():
            print(f"  MISSING  {name}")
            return 1
        live, flagged = scan(p)
        total_live += len(live)
        total_flagged += len(flagged)
        mark = "FAIL" if live else "ok  "
        print(f"  {mark}  {name:<46} live={len(live)}  flagged-open={len(flagged)}")
        for i, sname, field, ctx in live:
            print(f"          step[{i}] {sname} ({field})")
            print(f"            …{ctx[:150]}…")

    print()
    if total_flagged:
        print(f"{total_flagged} claim(s) carry an explicit unrepaired flag — known-open, "
              f"not a failure. These are premise errors (the proton word is not 6 "
              f"all-positive sigma), not naming.")
    if total_live:
        print(f"\nFAIL — {total_live} unflagged crossing-number claim(s). The atomic element "
              f"has none; say 'letters' and give the in-rho / outside-rho split.")
        return 1
    print("PASS — no unflagged crossing-number claim in any atom derivation chain.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
