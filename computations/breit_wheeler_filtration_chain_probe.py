#!/usr/bin/env python3
"""The gamma-gamma polarisation selection rule IS the promote/split dichotomy.

Where this comes from
---------------------
`content/.../mass-theory/breit-wheeler-vertex.md` gives the QOU reading of
gamma-gamma -> e-e+ entirely inside H_n(q), and states a selection rule:

  PARALLEL polarisation       sigma_i * sigma_i = (q - q^-1) sigma_i + 1
                              "No pair is created ... leaving a lower-energy
                              residue."
  PERPENDICULAR polarisation  sigma_0 * sigma_1 = L_+   (Hopf link, described
                              in that block as "a two-strand entangled state")
                              then L_+ * sigma_0 = sigma_0 sigma_1 sigma_0 = e-

Separately, `QOU.Knot.JetGradePromotion` (this branch) proves that a generator
meeting no existing inversion raises every grade by exactly one with
coefficients intact, because the length-DECREASING branch of the Hecke rule --
the only branch that splits a term across grades -- is unreachable.

Those are the same fact stated twice, and this probe checks that:

  parallel      = the SAME generator twice = an inversion exists = SPLIT
  perpendicular = a DIFFERENT generator    = no inversion        = PROMOTE

If it holds, the polarisation selection rule is not an extra postulate. It is
the Hecke length function, and "no pair is created" is "the profile split
instead of being promoted".

Scope: a structural identification, not a derivation of any rate or energy.
It does not compute a cross-section and does not touch binding.

Exact throughout: symbolic q over QQ(q). No floats, no substrate anchor.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import sympy as sp  # noqa: E402

from jet_history_retention_probe import HeckeElem, q, word_to_elem  # noqa: E402


def prof(E: "HeckeElem") -> str:
    return "{" + ", ".join(f"{g}:{len(v)}" for g, v in sorted(E.profile().items())) + "}"


def is_rigid_promotion(before: "HeckeElem", after: "HeckeElem") -> bool:
    b = {g: sp.simplify(sum(v.values())) for g, v in before.profile().items()}
    a = {g: sp.simplify(sum(v.values())) for g, v in after.profile().items()}
    shifted = {g + 1: m for g, m in b.items()}
    return (set(a) == set(shifted)
            and all(sp.simplify(a[g] - shifted[g]) == 0 for g in a))


def bw_parallel():
    """Parallel polarisation: the same generator twice."""
    print("=" * 74)
    print("PARALLEL polarisation -- the same generator twice")
    print("=" * 74)
    one = HeckeElem.one(3)
    g1 = one.mul_gen(1)
    g2 = g1.mul_gen(1)
    print(f"\n  vacuum                  {prof(one)}")
    print(f"  first photon  sigma_1   {prof(g1)}   rigid promotion: "
          f"{is_rigid_promotion(one, g1)}")
    print(f"  second photon sigma_1   {prof(g2)}   rigid promotion: "
          f"{is_rigid_promotion(g1, g2)}")
    print("\n  terms after the second photon:")
    for g, terms in sorted(g2.profile().items()):
        for w, c in terms.items():
            print(f"    grade {g}:  {sp.factor(c)}")
    print("\n  This is the Hecke relation sigma^2 = (q - q^-1) sigma + 1 --")
    print("  the block's 'lower-energy residue'. The profile SPLIT across two")
    print("  grades instead of being promoted; grade 0 (the vacuum term) is")
    print("  re-populated. No pair.")
    return {"split": not is_rigid_promotion(g1, g2),
            "grades": sorted(int(g) for g in g2.profile())}


def bw_perpendicular():
    """Perpendicular polarisation: different generators, then the substrate
    insertion that completes the trefoil."""
    print("\n" + "=" * 74)
    print("PERPENDICULAR polarisation -- different generators")
    print("=" * 74)
    one = HeckeElem.one(3)
    g1 = one.mul_gen(1)                     # first photon
    hopf = g1.mul_gen(2)                    # second photon, orthogonal -> L_+
    tref = hopf.mul_gen(1)                  # substrate Reeb insertion -> e-
    steps = [("vacuum", one, None),
             ("photon 1   sigma_1", g1, one),
             ("photon 2   sigma_2  -> L_+ (Hopf)", hopf, g1),
             ("Reeb insert sigma_1 -> e- (trefoil)", tref, hopf)]
    all_rigid = True
    for label, E, prev in steps:
        if prev is None:
            print(f"\n  {label:<38} {prof(E)}")
        else:
            r = is_rigid_promotion(prev, E)
            all_rigid &= r
            print(f"  {label:<38} {prof(E)}   rigid promotion: {r}")
    print("\n  Every step promotes rigidly. Nothing splits, nothing returns to")
    print("  grade 0: the chain climbs the filtration and the pair is created.")
    return {"all_rigid": bool(all_rigid),
            "final_grades": sorted(int(g) for g in tref.profile())}


def compare():
    print("\n" + "=" * 74)
    print("THE SELECTION RULE IS THE LENGTH FUNCTION")
    print("=" * 74)
    par = bw_parallel()
    perp = bw_perpendicular()
    print("\n" + "-" * 74)
    print(f"  parallel      splits            : {par['split']}")
    print(f"  perpendicular promotes throughout: {perp['all_rigid']}")
    print()
    print("  Same generator  -> an inversion already exists -> the Hecke")
    print("                     relation fires -> the profile SPLITS -> no pair.")
    print("  Different gens  -> no inversion to destroy -> rigid promotion")
    print("                     -> the pair is created.")
    print()
    print("  So the polarisation selection rule and the creation/binding")
    print("  asymmetry measured on 2H are ONE structural fact, not two.")
    return {"parallel": par, "perpendicular": perp}


if __name__ == "__main__":
    compare()
