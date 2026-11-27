#!/usr/bin/env python3
"""gg_twist_reading3_probe.py — stage 1: reading 3 on three strands with L± added to the γγ alphabet.

Pre-registered in preregistration.md (commit 72aa0c3f14b) before this file. Beans qou-a1hh, qou-99qc.
Alphabet {V, V^-1, L+, L-} at site 0, V = s0 s1^-1, L+ = s0 s1, L- = s0^-1 s1^-1. Words of length 1..6.
mpmath 40 dps, convention D, proton pin. Nothing fitted, selected or compared with measurement.

-- Ref: [leitner2026] bean qou-a1hh; bean qou-99qc
"""
from __future__ import annotations

import itertools
import sys
from pathlib import Path

import mpmath as mp

mp.mp.dps = 40
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "h2_gg_atom"))
import h2_gg_atom_probe as ga  # noqa: E402

base = ga.base
from qou_substrate.witness import WitnessBuilder  # noqa: E402

ONE, ZERO, H = mp.mpf(1), mp.mpf(0), base.H
S = lambda g: (ONE, ZERO, g)       # sigma_g
SI = lambda g: (ONE, -H, g)        # sigma_g^{-1} = sigma_g - h
# letter -> (hecke word, signed generator list)
LET = {
    "V": ([S(0), SI(1)], [(0, 1), (1, -1)]),
    "Vi": ([S(1), SI(0)], [(1, 1), (0, -1)]),
    "Lp": ([S(0), S(1)], [(0, 1), (1, 1)]),
    "Lm": ([SI(0), SI(1)], [(0, -1), (1, -1)]),
    "s0": ([S(0)], [(0, 1)]),
}


def perm_of(gens):
    p = [0, 1, 2]
    for g, _ in gens:
        p[g], p[g + 1] = p[g + 1], p[g]
    return tuple(p)


def ncycles(p):
    seen, c = set(), 0
    for i in range(3):
        if i not in seen:
            c += 1
            j = i
            while j not in seen:
                seen.add(j)
                j = p[j]
    return c


def evaluate(letters):
    word, gens = [], []
    for l in letters:
        word += LET[l][0]
        gens += LET[l][1]
    lc = ga.level_chars(base.diag_of(word, 3), 3, 1)
    mn = min(lc.values())
    p = perm_of(gens)
    return {
        "word": ".".join(letters),
        "writhe": sum(s for _, s in gens),
        "components": ncycles(p),
        "min_level_char": mp.nstr(mn, 20),
        "pass": bool(mn > 0),
        "fails": [f"{m}:{mu}" for (m, mu), v in lc.items() if v <= 0],
    }


def main() -> int:
    alpha = ["V", "Vi", "Lp", "Lm"]
    rows, checks = [], []
    for m in range(1, 7):
        n = 0
        for t in itertools.product(alpha, repeat=m):
            rows.append(evaluate(t))
            n += 1
        print(f"length {m}: {n} words, pass {sum(r['pass'] for r in rows[-n:])}", flush=True)
    controls = {name: evaluate(ls) for name, ls in
                {"Lp.s0 (trefoil)": ["Lp", "s0"], "V^3": ["V"] * 3, "V^6": ["V"] * 6}.items()}
    ok = controls["V^3"]["pass"] and controls["V^6"]["pass"]
    checks.append(("K1_V3_V6_pass_as_before", ok, "h2_gg_electron: V^3, V^6 pass on three strands"))
    passing = [r for r in rows if r["pass"]]
    chiral = [r for r in passing if r["writhe"] != 0]
    by_w = {}
    for r in passing:
        by_w.setdefault(r["writhe"], 0)
        by_w[r["writhe"]] += 1
    summary = {
        "words": len(rows), "passing": len(passing),
        "passing_by_writhe": {str(k): v for k, v in sorted(by_w.items())},
        "passing_nonzero_writhe": chiral,
        "min_length_nonzero_writhe_pass": min((len(r["word"].split(".")) for r in chiral), default=None),
        "passing_knots": [r for r in passing if r["components"] == 1],
        "controls": controls,
    }
    print({k: v for k, v in summary.items() if k not in ("passing_nonzero_writhe", "passing_knots")}, flush=True)
    print("nonzero writhe passing:", [(r["word"], r["writhe"], r["components"], r["min_level_char"]) for r in chiral][:40])
    wb = WitnessBuilder("gg-twist-reading3", engine="mpmath", output_dir=HERE)
    for name, good, src in checks:
        wb.add_assertion(name, computed="1" if good else "0", expected="1", source=src)
    wb.save({
        "q0Anchor": "proton",
        "q0AnchorReason": "via h2_one_rule (cf.Q, proton pin)",
        "description": "PROBE stage 1 (beans qou-a1hh, qou-99qc): reading 3 at levels 1..3 on three strands, words of "
                       "length 1..6 over {V, V^-1, L+, L-}. Pre-registered. Nothing fitted or selected.",
        "results": summary,
        "all_rows": rows,
    })
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
