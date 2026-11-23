#!/usr/bin/env python3
"""gg_twist_reading3_stage1b_probe.py — stage 1b: stage 1 re-run with L- = s1 s0 and the four-term photon.

Pre-registered in preregistration.md §Stage 1b and bean qou-99qc (2026-11-17 18:15Z) before this file. Beans qou-a1hh, qou-99qc.
Alphabet (a) {V, V^-1, L+, L-}, V = s0 s1^-1, L+ = s0 s1, L- = s1 s0 (the order prop:gamma-gamma-generates-particles
gives, not the inverse), lengths 1..6. Alphabet (b) adds e- = s0 s1 s0, lengths 1..5.
mpmath 40 dps, convention D, proton pin. Nothing fitted, selected or compared with measurement.

Scope note (2026-11-20). "Four-term photon" in this stage meant 1 + phi0 s0 + phi1 s1 + phi01 s0 s1.
By owner ruling (bean qou-99qc, 2026-11-18, confirmed 2026-11-20) def:photon's fourth term is the
chiral vertex s0 s1^-1 = V. The two forms are one family (gamma(phi0, phi1, phi01) =
gamma_straight(phi0 - h phi01, phi1, phi01)) and gamma*gamma reaches L+, L- and e- under both, so the
alphabets below are unaffected; e- is a two-photon-product letter, not a one-photon letter.

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
FLOOR = mp.mpf(10) ** -30
S = lambda g: (ONE, ZERO, g)       # sigma_g
SI = lambda g: (ONE, -H, g)        # sigma_g^{-1} = sigma_g - h
# letter -> (hecke word, signed generator list)
LET = {
    "V": ([S(0), SI(1)], [(0, 1), (1, -1)]),
    "Vi": ([S(1), SI(0)], [(1, 1), (0, -1)]),
    "Lp": ([S(0), S(1)], [(0, 1), (1, 1)]),
    "Lm": ([S(1), S(0)], [(1, 1), (0, 1)]),
    "E": ([S(0), S(1), S(0)], [(0, 1), (1, 1), (0, 1)]),
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
        # A value inside the precision floor is not a pass: on this word set such values are
        # ~1e-42 and change sign between 40 and 80 dps (checked by hand on V.E and E.E.V.E),
        # i.e. a zero at the precision of the inputs, not a positive character.
        "numerical_zero": bool(abs(mn) < FLOOR),
        "pass": bool(mn > FLOOR),
        "fails": [f"{m}:{mu}" for (m, mu), v in lc.items() if v <= 0],
    }


def run(alpha, maxlen):
    rows = []
    for m in range(1, maxlen + 1):
        for t in itertools.product(alpha, repeat=m):
            rows.append(evaluate(t))
    passing = [r for r in rows if r["pass"]]
    pure = [r for r in rows if r["components"] == 3]
    by_w, shortest = {}, {}
    for r in passing:
        by_w[r["writhe"]] = by_w.get(r["writhe"], 0) + 1
        L = len(r["word"].split("."))
        if r["writhe"] not in shortest or L < shortest[r["writhe"]][0]:
            shortest[r["writhe"]] = (L, r["word"], r["min_level_char"])
    return rows, {
        "words": len(rows), "passing": len(passing), "pure": len(pure),
        "pass_iff_pure": all(r["pass"] == (r["components"] == 3) for r in rows),
        "pure_failing": [r for r in pure if not r["pass"]][:40],
        "nonpure_passing": [r for r in passing if r["components"] != 3][:40],
        "passing_knots": [r for r in passing if r["components"] == 1],
        "passing_by_writhe": {str(k): v for k, v in sorted(by_w.items())},
        "shortest_passer_by_writhe": {str(k): list(v) for k, v in sorted(shortest.items())},
        "numerical_zero_words": [r["word"] for r in rows if r["numerical_zero"]][:200],
        "numerical_zero_count": sum(r["numerical_zero"] for r in rows),
        "pass_by_components": {str(c): [sum(1 for r in rows if r["components"] == c and r["pass"]),
                                        sum(1 for r in rows if r["components"] == c)] for c in (1, 2, 3)},
    }


def main() -> int:
    res, allrows = {}, {}
    for name, alpha, ml in (("a", ["V", "Vi", "Lp", "Lm"], 6), ("b", ["V", "Vi", "Lp", "Lm", "E"], 5)):
        allrows[name], res[name] = run(alpha, ml)
        r = res[name]
        print(name, {k: r[k] for k in ("words", "passing", "pure", "pass_iff_pure", "passing_by_writhe",
                                       "pass_by_components")}, flush=True)
        print("  shortest:", r["shortest_passer_by_writhe"], flush=True)
        print("  pure failing:", [(x["word"], x["fails"][:3]) for x in r["pure_failing"][:10]], flush=True)
        print("  nonpure passing:", [(x["word"], x["components"]) for x in r["nonpure_passing"][:10]], flush=True)
    wb = WitnessBuilder("gg-twist-reading3-stage1b", engine="mpmath", output_dir=HERE)
    wb.add_assertion("ran_alphabet_a", computed=str(res["a"]["words"]), expected="5460", source="4+16+...+4096")
    wb.add_assertion("ran_alphabet_b", computed=str(res["b"]["words"]), expected="3905", source="5+25+...+3125")
    wb.save({
        "q0Anchor": "proton",
        "q0AnchorReason": "via h2_one_rule (cf.Q, proton pin)",
        "description": "PROBE stage 1b (beans qou-a1hh, qou-99qc): stage 1 re-run with L- = s1 s0 (order, not "
                       "inverse) and the gamma-gamma product letter e- = s0 s1 s0 (called 'the four-term photon letter' "
                       "when run; scoped 2026-11-20: def:photon's fourth term is s0 s1^-1 by owner ruling, "
                       "alphabets unaffected). Pre-registered. Nothing selected.",
        "results": res,
    })
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
