#!/usr/bin/env python3
"""Braid words per chiral fermion, and whether lepton number reads off them.

Bean qou-h0zz.  `sm-open-problems.md` records the hypercharge blocker as
"framework braid words per chiral fermion still missing".  This probe observes
that the corpus already fixes them, and tests the simplest state function they
admit.

Where the braid words come from (nothing new assumed)
-----------------------------------------------------
`lepton-number-categorical-properties.md`, the chi = -6 constraint:

    "The torus knot generators T(2, n) with odd n <= 7 exhaust the fermion
     spectrum.  The electron (T_{2,3}) and neutrino (K_{0_1} = T_{2,1}) are
     the lowest torus knots in this sequence."

`T(2, n)` is by definition the closure of `sigma_1^n` in `B_2`.  So the carrier
braid words are *determined* by the corpus's own assignment, and the writhe
(exponent sum) of `sigma_1^n` is `n`.  Antiparticles are the braid mirror
`sigma_i -> sigma_i^-1` (`AntiparticleCrossingReversalContext`), i.e.
`sigma_1^-n`, writhe `-n`.

The hadron sector already has its words:
    gluon unit        sigma_0 sigma_1^-1              writhe  +1 - 1 = 0
    Borromean baryon  B_3 = (sigma_0 sigma_1^-1)^3    writhe  3(+1-1) = 0

What is tested
--------------
The corpus assigns L = +1 to (e-, nu_e), L = -1 to (e+, nubar_e), L = 0 to
hadrons.  Against the braid words above, the candidate

    L(beta) = sign(writhe(beta))

is parameter-free.  We check it on every row the corpus states, and then check
the consequence for Y = B - L (proved in HyperchargeBatteryReduction.lean).

This is a CANDIDATE test, not a derivation: `sign` is a choice of function, and
the quark braid word is NOT established by the corpus (flagged below).  Exact
integer arithmetic; no floats, no fitted parameters.
"""

from __future__ import annotations

import json
from fractions import Fraction as F


def writhe(word: list[int]) -> int:
    """Exponent sum of a braid word given as signed generator indices."""
    return sum(1 if g > 0 else -1 for g in word)


def sigma1_pow(n: int) -> list[int]:
    """`sigma_1^n` as a braid word (T(2,n) is its closure)."""
    return [1] * n if n >= 0 else [-1] * (-n)


GLUON = [1, -2]                 # sigma_0 sigma_1^-1  (indices 1, 2; sign = crossing)
BORROMEAN = GLUON * 3           # B_3 = (sigma_0 sigma_1^-1)^3


def main() -> dict:
    # Carriers, from the chi = -6 torus-knot assignment.
    carriers = {
        "nu_e   (T(2,1))":  dict(word=sigma1_pow(1),  L_corpus=1),
        "e-     (T(2,3))":  dict(word=sigma1_pow(3),  L_corpus=1),
        "nubar_e(T(2,1)^s)": dict(word=sigma1_pow(-1), L_corpus=-1),
        "e+     (T(2,3)^s)": dict(word=sigma1_pow(-3), L_corpus=-1),
        "baryon (B_3)":     dict(word=BORROMEAN,      L_corpus=0),
        "gluon unit":       dict(word=GLUON,          L_corpus=0),
    }

    rows, all_ok = [], True
    for name, d in carriers.items():
        w = writhe(d["word"])
        L_pred = (w > 0) - (w < 0)          # sign(w), integer
        ok = (L_pred == d["L_corpus"])
        all_ok &= ok
        rows.append(dict(carrier=name, braid_word=d["word"], writhe=w,
                         L_predicted=L_pred, L_corpus=d["L_corpus"], match=ok))

    # Higher generations the same constraint supplies (no L stated in corpus).
    gens = [dict(generation=g, knot=f"T(2,{n})", word_exp=n, writhe=n,
                 L_predicted=1)
            for g, n in enumerate([1, 3, 5, 7], start=0)]

    # Consequence for Y = B - L on the left-handed sector.
    # B is the writhe-INDEPENDENT half (mu-bar_123 candidate); L = sign(w).
    yrows = []
    for name, B, w_assumed, Y_sm in [
        ("u_L", F(1, 3), 0, F(1, 3)),
        ("d_L", F(1, 3), 0, F(1, 3)),
        ("nu_L", F(0), 1, F(-1)),
        ("e_L", F(0), 3, F(-1)),
    ]:
        L = (w_assumed > 0) - (w_assumed < 0)
        Y = B - L
        yrows.append(dict(fermion=name, B=str(B), writhe_assumed=w_assumed,
                          L=L, Y_predicted=str(Y), Y_sm=str(Y_sm),
                          match=(Y == Y_sm)))
    y_ok = all(r["match"] for r in yrows)

    return {
        "braid_words_source": ("chi=-6 torus-knot assignment: T(2,n) = closure "
                               "of sigma_1^n; antiparticle = braid mirror"),
        "L_candidate": "L(beta) = sign(writhe(beta))  [parameter-free]",
        "carrier_rows": rows,
        "all_corpus_rows_match": bool(all_ok),
        "higher_generations": gens,
        "Y_consequence": dict(
            formula="Y = B - L, with B writhe-independent and L = sign(w)",
            rows=yrows, all_match=bool(y_ok)),
        "CAVEATS": [
            "sign() is a CHOICE of function, not derived from the framework.",
            "The QUARK braid word is NOT established by the corpus; w=0 is "
            "ASSUMED above (motivated by the gluon unit being writhe-balanced). "
            "Every quark row depends on that assumption.",
            "Chirality (L vs R) is still not represented: the corpus gives no "
            "distinct braid word for u_L vs u_R.",
            "L = sign(w) is writhe-DEPENDENT. That does not conflict with the "
            "hypercharge requirement: Y = B - L still fails to factor through w "
            "because B varies at fixed w. The 'second invariant independent of "
            "the writhe' is B, not L.",
        ],
    }


if __name__ == "__main__":
    res = main()
    print(f"L candidate: {res['L_candidate']}\n")
    for r in res["carrier_rows"]:
        print(f"  {r['carrier']:20s} w={r['writhe']:+3d}  "
              f"L_pred={r['L_predicted']:+2d}  L_corpus={r['L_corpus']:+2d}  "
              f"{'OK' if r['match'] else 'MISMATCH'}")
    print(f"\n  all corpus rows match: {res['all_corpus_rows_match']}")
    print(f"\nY = B - L consequence (quark writhe ASSUMED 0):")
    for r in res["Y_consequence"]["rows"]:
        print(f"  {r['fermion']:5s} B={r['B']:4s} L={r['L']:+2d}  "
              f"Y={r['Y_predicted']:5s} vs SM {r['Y_sm']:5s}  "
              f"{'OK' if r['match'] else 'MISMATCH'}")
    print(f"  all match: {res['Y_consequence']['all_match']}")
    print("\nCAVEATS:")
    for c in res["CAVEATS"]:
        print(f"  - {c}")
