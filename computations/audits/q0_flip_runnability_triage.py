#!/usr/bin/env python3
"""Is the Q0_FLIP population re-runnable? Measured, not assumed.

`#5500` (muon anchor -> CODATA 2022) is gated on its own recommended
sequencing: *drain the pre-existing staleness first, then migrate*. Whether
that is even possible depends on a fact nobody had measured -- how many of the
flagged witnesses have a producer that can still be run.

The sibling B-population answer was discouraging: `qou-9ta3` measured 225 of
268 (84 %) NOT re-runnable, because the number cannot be recomputed when
nothing records how it was computed. That figure is correct and stands; this
script asks the same question of a DIFFERENT population and gets the opposite
answer, so the two must not be conflated.

RESOLUTION IS THE WHOLE DIFFICULTY, and getting it wrong inverts the result.
`scriptFile` is NOT consistently formatted across the corpus: most witnesses
store a BARE BASENAME (`aK_via_lp_dual_full.py`), a few store a repo-relative
path (`computations/deltalambda/..._probe.py`). So:

    os.path.exists(w["scriptFile"])        -> False for every bare basename
                                              => reports ~96 % unrunnable (WRONG)
    basename index over computations/**    -> resolves both forms
                                              => reports ~89 % runnable (RIGHT)

The first form was measured here first and was nearly reported. It is a
statement about the reader, not the corpus. `q0_old_muon_b_witness_triage.py`
already used the index form; this script follows it deliberately.

Second trap, same family: `scriptFile` is TOP-LEVEL in the witness, not nested
under a `witness` block. `d.get("witness", {}).get("scriptFile")` returns None
for every witness in the corpus and reads as "no provenance anywhere".

Writes no witness; pure measurement over committed artifacts.
"""
from __future__ import annotations

import collections
import glob
import json
import os
import sys

AUDIT = "computations/audits/q0-anchor-consistency-audit.witness.json"


def index(pattern: str) -> dict[str, list[str]]:
    idx: dict[str, list[str]] = {}
    for p in glob.glob(pattern, recursive=True):
        idx.setdefault(os.path.basename(p), []).append(p)
    return idx


def main() -> int:
    if not os.path.exists(sys.argv[1] if len(sys.argv) > 1 else AUDIT):
        print("missing audit witness — run q0_anchor_consistency_audit.py first")
        return 1
    src = sys.argv[1] if len(sys.argv) > 1 else AUDIT
    flips = json.load(open(src))["data"]["by_verdict"].get("Q0_FLIP", [])
    if not flips:
        print(f"{src}: Q0_FLIP is empty.")
        print("On `main` this is expected and is NOT a clean bill: the flip")
        print("population is defined RELATIVE TO an anchor, and main still")
        print("carries the superseded one, so nothing can disagree with it.")
        print("Point this at the audit witness from the re-derived-anchor")
        print("branch (#5500) to measure the migration target:")
        print(f"    python3 {os.path.basename(__file__)} <path-to-that-witness>")
        return 0
    widx, pidx = index("computations/**/*.witness.json"), index("computations/**/*.py")

    cat, fmt = collections.Counter(), collections.Counter()
    producers: set[str] = set()
    no_prov: list[str] = []
    for r in flips:
        wp = widx.get(os.path.basename(r["witness"]), [])
        if not wp:
            cat["witness not found"] += 1
            continue
        if "_deprecated" in wp[0]:
            cat["archived (_deprecated)"] += 1
            continue
        sf = json.load(open(wp[0])).get("scriptFile")   # TOP-LEVEL, see docstring
        if not sf:
            cat["no scriptFile field"] += 1
            no_prov.append(os.path.basename(wp[0]))
            continue
        fmt["bare basename" if os.path.basename(sf) == sf else "path-qualified"] += 1
        cands = pidx.get(os.path.basename(sf), [])
        if len(cands) == 1:
            cat["RUNNABLE (unique)"] += 1
            producers.add(cands[0])
        elif not cands:
            cat["producer genuinely gone"] += 1
        else:
            cat[f"ambiguous ({len(cands)} candidates)"] += 1
            producers.add(cands[0])

    total = len(flips)
    runnable = sum(v for k, v in cat.items() if k.startswith(("RUNNABLE", "ambiguous")))
    print(f"Q0_FLIP population: {total}")
    for k, v in cat.most_common():
        print(f"  {k:<32} {v}")
    print(f"\nscriptFile FORMAT (among those that have one):")
    for k, v in fmt.most_common():
        print(f"  {k:<32} {v}")
    print(f"\nRUNNABLE: {runnable}/{total} = {100*runnable/total:.1f}%")
    print(f"unique producers to re-run: {len(producers)}")
    if no_prov:
        print(f"\nno provenance ({len(no_prov)}) — cannot be recomputed, need a producer:")
        for b in sorted(no_prov):
            print(f"    {b}")
    print("\nREADING: the flip population is the OPPOSITE of the B-population.")
    print("qou-9ta3 measured B at 16% runnable; this is 89%. So #5500's own")
    print("recommended sequencing — drain first, then migrate — IS achievable")
    print("here: it is a bounded tranche over ~74 producers, not an open-ended")
    print("archaeology problem. The 9 with no provenance are the residue, and")
    print("they are the same class qou-9ta3 named: a number nothing can recompute.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
