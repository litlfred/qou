#!/usr/bin/env python3
"""Where the p/n information sits in the coefficients -- and a correction.

Context
-------
`isospin_triplet_filtration_probe` (merged d5c779878) found that pn, pp and nn
share every grade count, grade-mass and basis support while 20 of 50
individual T_w coefficients differ. `isospin_trace_blindness_probe` (#5928)
then proved the Markov trace cannot separate them at any z.

"The information is present" and "the information is usable" are different
claims. This probe establishes only the first, and corrects a wording of mine
that overstated it.

## THE CORRECTION

PR #5920 says grade 5 is "reachable ONLY when bound" and calls it a grade "no
unbound configuration can reach". That conflates two things:

    BRIDGED  -- a construction choice: whether sigma_3 is in the word
    BOUND    -- a physical fact: whether a bound state exists

Measured here: pn (bound) and pp (unbound) BOTH have free top grade 4 and
bridged top grade 5, and their grade-5 coefficients are IDENTICAL. So grade 5
marks the presence of a bridge, not the existence of a bound state. The
original measurement compared free-vs-bridged for one system and read the
result as bound-vs-unbound; the isospin family separates the two, because
there the bridge is applied equally to a system that binds and two that
do not.

The measurement in #5920 stands. Its interpretation was one word too strong,
and this is the word.

## What the coefficient structure actually looks like

  - pp and nn differ from EACH OTHER in 28 of 50 coefficients, so this is not
    a two-class {bound} vs {unbound} split. All three are mutually distinct.
  - the differences sit in the MIDDLE grades. Grade 0 and grade 5 -- the two
    extremes -- are identical across all three; grades 1-4 carry every
    difference.
  - REFUTED: the pn vector is not bar-even and not bar-odd, and neither is
    pp, so bar-parity does not separate them.
  - REFUTED: pp and nn are not bar-images of one another either -- 39 of 50
    coefficients disagree under q -> 1/q.

So the p/n information is present but NOT organised by any of the three
symmetries tried. This probe does not exhibit a functional that ranks the
bound system above the two unbound ones, and does not claim one exists.

Exact throughout: symbolic q over QQ(q). No floats, no substrate anchor.
"""
from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import sympy as sp  # noqa: E402

from jet_history_retention_probe import coxeter_length, q, word_to_elem  # noqa: E402
from isospin_triplet_filtration_probe import (  # noqa: E402
    P_A, N_A, P_B, N_B, BRIDGE,
)

SYS = {"pn": (P_A, N_B), "pp": (P_A, P_B), "nn": (N_A, N_B)}


def build():
    return {k: word_to_elem(6, a + b + [BRIDGE, BRIDGE])[0] for k, (a, b) in SYS.items()}


def correction(E):
    """Grade 5 marks BRIDGED, not BOUND."""
    print("=" * 74)
    print("CORRECTION to PR #5920: grade 5 marks BRIDGED, not BOUND")
    print("=" * 74)
    for k in ("pn", "pp"):
        a, b = SYS[k]
        F, _ = word_to_elem(6, a + b)
        tag = "BOUND 2.2246 MeV" if k == "pn" else "UNBOUND"
        print(f"    {k} ({tag:<16}) free top grade {max(F.profile())}"
              f"  ->  bridged top grade {max(E[k].profile())}")
    same5 = all(sp.simplify(E["pn"].terms.get(w, 0) - E["pp"].terms.get(w, 0)) == 0
                for w in set(E["pn"].terms) | set(E["pp"].terms)
                if coxeter_length(w) == 5)
    print(f"\n    grade-5 coefficients identical, bound pn vs unbound pp: {same5}")
    print("    So the bridge opens grade 5 whether or not a bound state exists.")
    print("    #5920 compared free-vs-bridged for ONE system and read it as")
    print("    bound-vs-unbound. The measurement stands; the word does not.")
    return {"grade5_same_bound_vs_unbound": bool(same5)}


def structure(E):
    print("\n" + "=" * 74)
    print("Where the differences sit, and which symmetries do NOT explain them")
    print("=" * 74)
    dpp = [w for w in E["pn"].terms
           if sp.simplify(E["pn"].terms[w] - E["pp"].terms.get(w, 0)) != 0]
    dnn = [w for w in E["pp"].terms
           if sp.simplify(E["pp"].terms[w] - E["nn"].terms.get(w, 0)) != 0]
    print(f"\n    pn vs pp : {len(dpp)} of {len(E['pn'].terms)} coefficients differ")
    print(f"    pp vs nn : {len(dnn)} of {len(E['pp'].terms)} coefficients differ"
          "   -> NOT a two-class split; all three are mutually distinct")

    bg, tot = Counter(coxeter_length(w) for w in dpp), Counter(
        coxeter_length(w) for w in E["pn"].terms)
    print("\n    pn vs pp differences by grade:")
    for g in sorted(tot):
        print(f"      grade {g}: {bg.get(g, 0):>2} differ of {tot[g]:>2}")
    print("      -> the extremes (0 and 5) agree; every difference is interior")

    print("\n    Symmetries tried, and refuted:")
    for k in ("pn", "pp"):
        even = all(sp.simplify(c - c.subs(q, 1 / q)) == 0 for c in E[k].terms.values())
        odd = all(sp.simplify(c + c.subs(q, 1 / q)) == 0 for c in E[k].terms.values())
        print(f"      {k}: all coefficients bar-even {even}, bar-odd {odd}")
    nbar = sum(1 for w, c in E["pp"].terms.items()
               if sp.simplify(c.subs(q, 1 / q) - E["nn"].terms.get(w, 0)) != 0)
    print(f"      bar(pp) != nn in {nbar} of {len(E['pp'].terms)} coefficients")
    print("\n    None of the three symmetries organises the difference. The")
    print("    information is present; this probe does not make it usable.")
    return {"pn_vs_pp": len(dpp), "pp_vs_nn": len(dnn),
            "by_grade": {int(g): bg.get(g, 0) for g in tot},
            "bar_pp_ne_nn": nbar}


def main():
    E = build()
    r1 = correction(E)
    r2 = structure(E)
    assert r1["grade5_same_bound_vs_unbound"], "the correction's premise failed"
    return {"correction": r1, "structure": r2}


if __name__ == "__main__":
    main()
