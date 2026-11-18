#!/usr/bin/env python3
"""gg_photon_product_selection_probe.py — stage 7: canonical-word reselection from gamma(phi)gamma(psi).

Pre-registered in bean qou-99qc (PRE-REGISTRATION 2026-11-18 04:30Z) before this file was written.
Letters are the terms of the product of two four-term photons (def:photon, PR #8367), as braid words
before any Hecke reduction. Rule A (primary): the nine bilinear terms (both photons dressed). Rule B
(comparison arm, not selectable): all eleven non-identity terms. Selection is FrobeniusSelected
(bean qou-ales): reading 3, chi_lambda(w) >= 0 on every level with y_lambda > 0, convention D, proton
pin; cost = crossing count; every feasible word of minimal cost is reported. No tie is broken.
A value under 1e-30 is decided EXACTLY instead (sympy, q symbolic, exact_h3_level_chars.py): zero only if
the level character is identically zero as a rational function of q; a nonzero one that small is reported
"undecided" and counts as infeasible. This replaces the pre-registered 120-dps re-evaluation, which the
engine cannot do (q0 enters as a stored string); the exact test is strictly stronger.
Nothing is compared with measurement.
-- Ref: [leitner2026] bean qou-99qc; bean qou-ales
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
sys.path.insert(0, str(HERE))
import exact_h3_level_chars as ex  # noqa: E402

base = ga.base
from qou_substrate.witness import WitnessBuilder  # noqa: E402

MAXC = 12
FLOOR, ZERO_HI = mp.mpf(10) ** -30, mp.mpf(10) ** -100

# letter name -> generator list (all positive crossings)
BILINEAR = {
    "s0s0": [0, 0], "s0s1": [0, 1], "s1s0": [1, 0], "s1s1": [1, 1],
    "s0s0s1": [0, 0, 1], "s0s1s0": [0, 1, 0], "s0s1s1": [0, 1, 1], "s0s1s0s1": [0, 1, 0, 1],
}
# sigma1 sigma0 sigma1 = sigma0 sigma1 sigma0 in B_3, so the ninth bilinear term (phi1 psi01) is the
# same braid as s0s1s0 and is not a separate letter.
RULE_B = dict(BILINEAR, s0=[0], s1=[1])


def perm_cycles(gens):
    p = [0, 1, 2]
    for g in gens:
        p[g], p[g + 1] = p[g + 1], p[g]
    seen, c = set(), 0
    for i in range(3):
        if i not in seen:
            c += 1
            j = i
            while j not in seen:
                seen.add(j)
                j = p[j]
    return c


def chars(gens, dps):
    with mp.workdps(dps):
        one, zero = mp.mpf(1), mp.mpf(0)
        word = [(one, zero, g) for g in gens]
        return ga.level_chars(base.diag_of(word, 3), 3, 1)


def classify(gens):
    lc = chars(gens, 40)
    exact = None
    verdict = {}
    for k, v in lc.items():
        if v > FLOOR:
            verdict[k] = "+"
        elif v < -FLOOR:
            verdict[k] = "-"
        else:
            if exact is None:
                exact = ex.level_chars(list(gens))
            verdict[k] = "0" if exact[k] == 0 else "undecided"
    feasible = all(s in "+0" for s in verdict.values())
    return lc, verdict, feasible


def check_exact_engine():
    """The exact functional agrees with the mpmath engine at q0 on a fixed word list."""
    import sympy as sp
    q0 = sp.Float(mp.nstr(base.Q, 40), 40)
    worst = mp.mpf(0)
    for g in [(0,), (1,), (0, 1), (1, 0, 1), (0, 0, 1, 1, 0), (1, 1, 0, 1, 0, 0)]:
        e, n = ex.level_chars(list(g)), chars(list(g), 40)
        for k, v in n.items():
            worst = max(worst, abs(mp.mpf(str(sp.N(e[k].subs(ex.q, q0), 40))) - v))
    return worst


def words(letters, maxc):
    out = {}
    names = sorted(letters)
    def rec(seq, gens):
        if gens:
            key = tuple(gens)
            out.setdefault(key, []).append(".".join(seq))
        for n in names:
            g = letters[n]
            if len(gens) + len(g) <= maxc:
                rec(seq + [n], gens + g)
    rec([], [])
    return out


def run(letters, label):
    ws = words(letters, MAXC)
    rows, nzero, nund = [], [0], [0]
    for gens, spellings in sorted(ws.items(), key=lambda x: (len(x[0]), x[0])):
        lc, verdict, feas = classify(list(gens))
        if any(x == "0" for x in verdict.values()):
            nzero[0] += 1
        if any(x == "undecided" for x in verdict.values()):
            nund[0] += 1
        if feas:
            rows.append({"braid": "".join(f"s{g}" for g in gens), "crossings": len(gens),
                         "letters": spellings[:3], "n_spellings": len(spellings),
                         "components": perm_cycles(gens), "writhe": len(gens),
                         "chars": {f"{m}:{mu}": mp.nstr(v, 20) for (m, mu), v in lc.items()},
                         "signs": {f"{m}:{mu}": s for (m, mu), s in verdict.items()}})
    cmin = min((r["crossings"] for r in rows), default=None)
    sel = [r for r in rows if r["crossings"] == cmin]
    print(f"[{label}] candidate braids {len(ws)}, feasible {len(rows)}, min cost {cmin}, selected {len(sel)}")
    for r in sel:
        print("   ", r["braid"], r["letters"], "comp", r["components"], r["chars"])
    print(f"    exact zeros {nzero[0]}, undecided {nund[0]}")
    return {"candidates": len(ws), "exact_zero_words": nzero[0], "undecided_words": nund[0], "feasible": len(rows), "min_cost": cmin, "selected": sel,
            "feasible_by_cost": {c: sum(1 for r in rows if r["crossings"] == c) for c in range(1, MAXC + 1)}}


def main() -> int:
    worst = check_exact_engine()
    print("exact vs mpmath engine, max |diff| at q0:", mp.nstr(worst, 5))
    out = {"exact_engine_max_diff": mp.nstr(worst, 10),
           "ruleA_bilinear": run(BILINEAR, "A"), "ruleB_all_terms": run(RULE_B, "B")}
    wb = WitnessBuilder("gg-photon-product-selection-stage7", engine="mpmath", output_dir=HERE)
    wb.add_assertion("exact_engine_agrees", computed="1" if worst < mp.mpf(10) ** -30 else "0",
                     expected="1", source="exact_h3_level_chars vs h2_gg_atom_probe.level_chars")
    wb.add_assertion("ruleA_has_selection", computed="1" if out["ruleA_bilinear"]["selected"] else "0",
                     expected="1", source="pre-registration qou-99qc 2026-11-18 04:30Z")
    wb.save({"q0Anchor": "proton", "q0AnchorReason": "reading 3 at the proton pin, convention D",
             "description": "PROBE stage 7: canonical-word reselection over the letters of gamma(phi)gamma(psi) "
                            "(def:photon), FrobeniusSelected, cost = crossing count, all ties reported.",
             **out})
    return 0


if __name__ == "__main__":
    sys.exit(main())
