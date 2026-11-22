#!/usr/bin/env python3
"""gg_two_orientations_probe.py — γγ words in {V, V̄} on 3 strands (pre-registered, preregistration.md 9e4979bda52).

Bean qou-a1hh, PR #7741. mpmath, convention D, proton q₀. Hypothesis only; nothing adopted, selected or wired.
-- Ref: [manuscript] bean qou-a1hh; bean qou-qs1x; bean qou-ales
"""
from __future__ import annotations

import itertools
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "h2_gg_atom"))
sys.path.insert(0, str(HERE.parent / "gg_symmetry"))
import h2_gg_atom_probe as ga  # noqa: E402
import gg_symmetry_probe as gs  # noqa: E402

base, log, TOL = ga.base, ga.log, ga.TOL
ONE, ZERO, H = base.ONE, base.ZERO, base.H
from qou_substrate.witness import WitnessBuilder  # noqa: E402

LET = {"V": [(ONE, ZERO, 0), (ONE, -H, 1)], "B": [(ONE, -H, 0), (ONE, ZERO, 1)]}
S0P, S0M = (ONE, ZERO, 0), (ONE, -H, 0)


def word(p):
    return [t for c in p for t in LET[c]]


def dR(w):
    cp, cm = gs.chars(w + [S0P]), gs.chars(w + [S0M])
    return (cp[(2, (1, 1))] - cm[(2, (1, 1))]) - (cp[(2, (2,))] - cm[(2, (2,))])


def main() -> int:
    rows = {}
    passing = []
    for m in range(1, 7):
        for p in itertools.product("VB", repeat=m):
            p = "".join(p)
            c = gs.chars(word(p))
            ok = all(v >= -TOL for v in c.values())
            r = {"passes_alone": ok, "chars": {f"{a}:{b}": mp.nstr(v, 15) for (a, b), v in sorted(c.items())}}
            if ok:
                r["dR"] = mp.nstr(dR(word(p)), 12)
                passing.append(p)
            rows[p] = r
        log(f"m={m}: passing {[p for p in passing if len(p) == m]}")
    pure_ok = all((rows["V" * m]["passes_alone"] == (m % 3 == 0)) and (rows["B" * m]["passes_alone"] == (m % 3 == 0))
                  for m in range(1, 7))
    mixed = [p for p in passing if len(set(p)) > 1]
    log(f"[{'PASS' if pure_ok else 'FAIL'}] T0_pure_powers_match_gg_symmetry")
    log(f"OUTCOME {'(i)' if mixed else '(ii)'}: {len(mixed)} mixed passing words: {mixed}")
    for p in passing:
        log(f"  {p}: dR = {rows[p]['dR']}")
    wb = WitnessBuilder("gg-two-orientations", engine="mpmath", output_dir=HERE)
    wb.add_assertion("T0_pure_powers_match_gg_symmetry", computed="1" if pure_ok else "0", expected="1",
                     source="V^m, Vbar^m pass iff 3|m")
    wb.save({"q0Anchor": "proton", "q0AnchorReason": "via h2_gg_atom (cf.Q, proton pin)",
             "description": "PROBE (bean qou-a1hh, hypothesis): words in {V, Vbar} on 3 strands, m=1..6; reading 3 "
                            "alone at levels 1-3; one-photon sign dR. Pre-registered. Nothing adopted or wired.",
             "weight_family": "markov_y_lambda_convention_D", "passing": passing, "mixed_passing": mixed,
             "results": rows})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
