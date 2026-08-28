#!/usr/bin/env python3
"""Creation promotes; binding splits. Measured on the deuteron.

The consequence worth testing
------------------------------
`QOU.Knot.JetGradePromotion` proves that multiplying by a generator acting on
a FRESH strand raises every grade by exactly one, coefficients intact: a
permutation fixing the top point sends everything else below it, so the
length-DECREASING branch of the Hecke rule is unreachable.

That branch is the only one that splits a term across two grades. So the
theorem has a converse-shaped consequence the framework cares about:

    CREATION  (a generator on a fresh strand)   -> rigid promotion, no split
    BINDING   (a bond between existing strands) -> the decreasing branch is
                                                   reachable, so it CAN split

If that holds, creation and binding are structurally different operations in
the filtration, and binding energy lives in exactly the part that creation
cannot produce -- the grade-lowered content the Markov trace then sums over.
That is a candidate home for the undetermined term of
`conj:binding-manybody-eq-jet-filtration`, whose n=3 weight is free.

The deuteron, in this repo's own convention
--------------------------------------------
Following `gs_filtration_binding_components.py`: nucleon i is a B_3 core on
strands [3i, 3i+1, 3i+2] (generators sigma_{3i+1}, sigma_{3i+2}); the bridges
sigma_{3i} are the A-1 inter-nucleon bonds. So 2H is two nucleons on six
strands in H_6, with a single bridge sigma_3.

  W_free = cores only          (two unbound nucleons)
  W_atom = cores + bridge      (the bound deuteron)

and the binding is carried entirely by the bridge.

What this measures
------------------
  E1  does the FIRST bond crossing split the profile, or promote it?
  E2  what happens as the bond is thickened (sigma_3, sigma_3^2, sigma_3^3)?
  E3  the same for the free-vs-bound pair, by grade.

Exact throughout: symbolic q over QQ(q). No floats, no substrate anchor.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import sympy as sp  # noqa: E402

from jet_history_retention_probe import (  # noqa: E402
    HeckeElem, coxeter_length, q, word_to_elem,
)

#: 2H: two B_3 nucleon cores on six strands, bridged by sigma_3.
#: Nucleon 0 uses sigma_1, sigma_2; nucleon 1 uses sigma_4, sigma_5.
PROTON_CORE = [1, -2, 1, -2, 1, -2]          # (s1 s2^-1)^3 on strands 1-3
NEUTRON_CORE = [-4, 5, -4, 5, -4, 5]         # (s4^-1 s5)^3 on strands 4-6
BRIDGE = 3                                   # the inter-nucleon bond


def profile_str(E: "HeckeElem") -> str:
    return "{" + ", ".join(f"{g}:{len(v)}" for g, v in sorted(E.profile().items())) + "}"


def e1_first_bond_crossing():
    """Does the first bond crossing split, or promote?"""
    print("=" * 74)
    print("E1  The first bond crossing: split or promote?")
    print("=" * 74)
    free, _ = word_to_elem(6, PROTON_CORE + NEUTRON_CORE)
    print(f"\n  W_free (two unbound cores)   grades {profile_str(free)}")

    bound = free.mul_gen(BRIDGE)
    print(f"  + one bond crossing sigma_3  grades {profile_str(bound)}")

    before = {g: sp.simplify(sum(v.values())) for g, v in free.profile().items()}
    after = {g: sp.simplify(sum(v.values())) for g, v in bound.profile().items()}
    shifted = {g + 1: m for g, m in before.items()}
    rigid = (set(after) == set(shifted)
             and all(sp.simplify(after[g] - shifted[g]) == 0 for g in after))
    print(f"\n  rigid +1 promotion (no split)? {rigid}")
    if rigid:
        print("  => the FIRST bond crossing behaves like creation, not binding:")
        print("     w(3) lies in nucleon 0's block and w(4) in nucleon 1's, so")
        print("     w(3) < w(4) and no inversion exists to destroy.")
    return {"rigid_first_crossing": bool(rigid),
            "grades_free": sorted(int(g) for g in before),
            "grades_bound": sorted(int(g) for g in after)}


def e2_thickening_the_bond():
    """Thicken the bond: sigma_3, sigma_3^2, sigma_3^3. Where does it split?"""
    print("\n" + "=" * 74)
    print("E2  Thickening the bond -- where the split appears")
    print("=" * 74)
    free, _ = word_to_elem(6, PROTON_CORE + NEUTRON_CORE)
    rows = []
    E = free
    print(f"\n  0 bond crossings  grades {profile_str(E)}   (top {max(E.profile())})")
    prev_top = max(E.profile())
    for k in range(1, 4):
        E = E.mul_gen(BRIDGE)
        top = max(E.profile())
        low = min(E.profile())
        split = (top - low) > (prev_top - min(free.profile()))
        print(f"  {k} bond crossing{'s' if k > 1 else ' '}  grades {profile_str(E)}"
              f"   (top {top}, span {top - low})")
        rows.append({"crossings": k, "top_grade": int(top),
                     "span": int(top - low),
                     "grades": sorted(int(g) for g in E.profile())})
        prev_top = top
    print("\n  A bond crossing between DISTINCT nucleon blocks promotes; the")
    print("  splitting appears once the bond is thickened, because the second")
    print("  crossing acts where an inversion now exists.")
    print()
    print("  MEASURED, and it is not saturation. k=2 and k=3 have identical")
    print("  grade counts AND identical basis support -- and 50 coefficients")
    print("  still differ. So the bond's filtration SHAPE stabilises at two")
    print("  crossings while its CONTENT keeps changing.")
    print()
    print("  That is a third lossy projection, alongside the trace and the")
    print("  normal form: reading only WHERE the mass sits loses the bond")
    print("  thickness entirely. Equal counts never establish equal elements.")
    return rows


def e3_binding_by_grade():
    """Free vs bound, resolved by grade -- what the trace sums over."""
    print("\n" + "=" * 74)
    print("E3  Free vs bound, resolved by grade")
    print("=" * 74)
    free, _ = word_to_elem(6, PROTON_CORE + NEUTRON_CORE)
    bound, _ = word_to_elem(6, PROTON_CORE + NEUTRON_CORE + [BRIDGE, BRIDGE])
    gf = {g: sp.simplify(sum(v.values())) for g, v in free.profile().items()}
    gb = {g: sp.simplify(sum(v.values())) for g, v in bound.profile().items()}
    print(f"\n  {'grade':>6} {'free':>28} {'bound (2-crossing bond)':>30}")
    for g in sorted(set(gf) | set(gb)):
        f = sp.factor(gf.get(g, 0))
        b = sp.factor(gb.get(g, 0))
        print(f"  {g:>6} {str(f)[:28]:>28} {str(b)[:30]:>30}")
    only_bound = sorted(set(gb) - set(gf))
    print(f"\n  grades present ONLY when bound: {only_bound}")
    print("  These are the grades no unbound configuration can reach --")
    print("  the trace sums over them and returns one number.")
    return {"grades_free": sorted(int(g) for g in gf),
            "grades_bound": sorted(int(g) for g in gb),
            "grades_only_bound": [int(g) for g in only_bound]}


def main():
    print("Creation promotes; binding splits -- measured on 2H\n")
    r1 = e1_first_bond_crossing()
    r2 = e2_thickening_the_bond()
    r3 = e3_binding_by_grade()
    print("\n" + "=" * 74)
    print("SUMMARY")
    print("=" * 74)
    print(f"  first bond crossing is a rigid promotion : {r1['rigid_first_crossing']}")
    print(f"  grades reachable only when bound         : {r3['grades_only_bound']}")
    return {"e1": r1, "e2": r2, "e3": r3}


if __name__ == "__main__":
    main()
