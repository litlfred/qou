#!/usr/bin/env python3
"""Sign-only bridge variation does NOT break tau.

The H_9 investigation found that the separator distinguishing 3H from 3He is
invariant under tau = (p<->n complement) o (block reversal), so it detects
strand-block arrangement rather than isospin, and suggested breaking tau with
a "charge-carrying, reversal-odd bridge". Every bridge used in this arc has
been sign-symmetric, so that was the obvious first thing to vary.

Varied it. It does not help, and the negative is sharp:

    bridge                      pn/pp  pp/nn  pn/np  terms
    [s3,s3]   (used all arc)       20     28     28     50
    [s3]       single              10     14     14     25
    [s3,-s3]   reversal-odd        10     14     14     25
    [-s3,-s3]  all-inverse         20     28     28     50
    [s3,s3,s3] thicker             20     28     28     50

`pp/nn` equals `pn/np` in EVERY row. The bridge moves the magnitude -- 25
terms versus 50 -- and never breaks the symmetry. So tau is forced by the
mirror cores, not by the bridge, and no amount of sign-flipping reaches it.

Two consistency checks fall out and both pass: `[s3,-s3]` reduces to the free
element (sigma_3 sigma_3^-1 = 1) at 25 terms, and `[s3]` alone also gives 25,
because a single bridge crossing between disjoint blocks is a rigid promotion
(QOU.Knot.JetGradePromotion) and promotion preserves the term count.

## What this does and does not exclude

Scope-(a), and the boundary matters. What is refuted is SIGN-ONLY bridge
variation: changing crossing signs or counts in a bridge whose word is the
same regardless of which nucleons it connects.

What is NOT tested, and remains the open route, is a genuinely
CHARGE-CARRYING bridge -- one whose word DEPENDS on the nucleon types at its
two ends, so that a p-p bond, a p-n bond and an n-n bond are different words.
Every bridge here is blind to what it connects, which is exactly why it
cannot distinguish arrangements of those connections.

That route also carries the arc's main fitting hazard, and it should be said
plainly before anyone takes it: a rule assigning bridge words to charge pairs
has enough freedom to reproduce a target, and choosing it to land 2.2246 MeV
would be a fit wearing a mechanism's clothes. The anti-fit discipline applies
with full force -- the rule has to come from the substrate, not from the
answer.

Exact throughout: sparse Z[q,q^-1], cross-checked against sympy. No floats.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from hecke_exact_laurent import n_differing, word_to_elem_fast  # noqa: E402
from isospin_triplet_filtration_probe import P_A, N_A, P_B, N_B  # noqa: E402

BRIDGES = {
    "[s3,s3]   (used all arc)": [3, 3],
    "[s3]       single": [3],
    "[s3,-s3]   reversal-odd": [3, -3],
    "[-s3,-s3]  all-inverse": [-3, -3],
    "[s3,s3,s3] thicker": [3, 3, 3],
}
SYS = {"pn": (P_A, N_B), "pp": (P_A, P_B), "nn": (N_A, N_B), "np": (N_A, P_B)}


def main():
    print("Is tau a BRIDGE artifact, or forced by the mirror CORES?\n")
    print(f"  {'bridge':<26}{'pn/pp':>7}{'pp/nn':>7}{'pn/np':>7}{'terms':>7}")
    broke = False
    for lbl, br in BRIDGES.items():
        E = {k: word_to_elem_fast(6, a + b + br) for k, (a, b) in SYS.items()}
        d_ppnn = n_differing(E["pp"], E["nn"])
        d_pnnp = n_differing(E["pn"], E["np"])
        broke |= (d_ppnn != d_pnnp)
        print(f"  {lbl:<26}{n_differing(E['pn'], E['pp']):>7}{d_ppnn:>7}"
              f"{d_pnnp:>7}{len(E['pn'].terms):>7}")
    print(f"\n  any bridge broke the pp/nn == pn/np symmetry: {broke}")
    print("  => tau is forced by the mirror cores. Sign-only bridge variation")
    print("     cannot reach it; a CHARGE-CARRYING bridge (a different word")
    print("     per nucleon-type pair) is untested and is the open route.")
    print("     That route is also where the fitting hazard lives: the rule")
    print("     must come from the substrate, not from the target number.")
    assert not broke, "a bridge broke the symmetry -- the docstring is now wrong"
    return {"symmetry_broken_by_any_bridge": broke}


if __name__ == "__main__":
    main()
