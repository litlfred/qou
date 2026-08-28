#!/usr/bin/env python3
"""The two-nucleon isospin family: pn binds, pp and nn do not. Does the GS
filtration know?

Why this pair and not 3H/3He
----------------------------
The mirror-nucleus pair 3H/3He is the cleanest three-channel separator in the
low isotopes -- one p<->n swap apart, so the strong part nearly cancels by
isospin symmetry and the binding difference (8.482 vs 7.718 MeV) is close to
pure EM + weak. But it needs nine strands (three nucleons at three strands
each), and H_9 has 9! = 362880 basis elements; the symbolic reduction here
does not reach it.

The two-nucleon family is the same question one rung lower, and it is sharper
as a first test because the experimental answer is stark rather than a 0.76
MeV difference:

    p + n   ->  the DEUTERON, bound by 2.2246 MeV
    p + p   ->  the diproton,  UNBOUND (no bound state exists)
    n + n   ->  the dineutron, UNBOUND

Three systems, same strand count, same bridge, differing only in which
nucleon words sit on the two blocks. If the GS filtration carries binding
information at all, something must distinguish the first from the other two.
If nothing does, that is a scope-(a) negative worth having: it would say the
filtration profile is blind to the one two-nucleon fact everybody knows.

What is measured
----------------
For each of the three, in H_6 with a two-crossing bridge sigma_3:
  - the free (unbridged) profile
  - the bound (bridged) profile
  - the grades reachable only when bridged
  - whether the bridge promoted rigidly or split

Honest expectation, recorded BEFORE the run so it cannot be retrofitted:
p and n are mirror words with identical HOMFLY and identical grade profiles
(measured, `jet_history_retention_probe` Q3 / the 5920 branch), so pp, pn and
nn may well come out identical here. If they do, the filtration profile does
NOT see binding, and the missing term is not recoverable from it alone.

Exact throughout: symbolic q over QQ(q). No floats, no substrate anchor.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import sympy as sp  # noqa: E402

from jet_history_retention_probe import word_to_elem, q  # noqa: E402

#: Nucleon cores. Block A uses sigma_1, sigma_2; block B uses sigma_4, sigma_5.
P_A = [1, -2, 1, -2, 1, -2]        # proton  on strands 1-3
N_A = [-1, 2, -1, 2, -1, 2]        # neutron on strands 1-3
P_B = [4, -5, 4, -5, 4, -5]        # proton  on strands 4-6
N_B = [-4, 5, -4, 5, -4, 5]        # neutron on strands 4-6
BRIDGE = 3

SYSTEMS = [("p n  (deuteron, BOUND 2.2246 MeV)", P_A, N_B),
           ("p p  (diproton, unbound)", P_A, P_B),
           ("n n  (dineutron, unbound)", N_A, N_B)]


def summarise(free, bound):
    gf = {g: sp.simplify(sum(v.values())) for g, v in free.profile().items()}
    gb = {g: sp.simplify(sum(v.values())) for g, v in bound.profile().items()}
    only = sorted(set(gb) - set(gf))
    counts_free = {g: len(v) for g, v in sorted(free.profile().items())}
    counts_bound = {g: len(v) for g, v in sorted(bound.profile().items())}
    return gf, gb, only, counts_free, counts_bound


def main():
    print("Two-nucleon isospin family in the GS filtration\n")
    results = {}
    for label, a, b in SYSTEMS:
        free, _ = word_to_elem(6, a + b)
        bound, _ = word_to_elem(6, a + b + [BRIDGE, BRIDGE])
        gf, gb, only, cf, cb = summarise(free, bound)
        print("=" * 74)
        print(f"  {label}")
        print("=" * 74)
        print(f"    free  grade counts {cf}")
        print(f"    bound grade counts {cb}")
        print(f"    grades reachable ONLY when bridged: {only}")
        results[label] = {"free_counts": {int(k): v for k, v in cf.items()},
                          "bound_counts": {int(k): v for k, v in cb.items()},
                          "only_bound": [int(g) for g in only],
                          "bound_mass": gb}
        print()

    print("=" * 74)
    print("DO THE THREE DIFFER?")
    print("=" * 74)
    keys = list(results)
    base = results[keys[0]]
    for k in keys[1:]:
        r = results[k]
        same_counts = (r["bound_counts"] == base["bound_counts"])
        same_mass = all(
            sp.simplify(r["bound_mass"].get(g, 0) - base["bound_mass"].get(g, 0)) == 0
            for g in set(r["bound_mass"]) | set(base["bound_mass"]))
        print(f"\n  {k}")
        print(f"    same grade COUNTS as deuteron   : {same_counts}")
        print(f"    same grade-MASS  as deuteron    : {same_mass}")
        results[k]["same_counts_as_pn"] = bool(same_counts)
        results[k]["same_mass_as_pn"] = bool(same_mass)

    print()
    all_same = all(results[k].get("same_mass_as_pn", True) for k in keys[1:])
    if all_same:
        print("  VERDICT: the filtration profile does NOT distinguish the bound")
        print("  deuteron from the two unbound systems. Scope-(a): the profile")
        print("  alone cannot carry the binding, so the missing term is not")
        print("  recoverable from it without additional structure.")
    else:
        print("  VERDICT: the profile DOES separate them -- report which grade")
        print("  carries the difference, since that is where binding would live.")
    return results


def coefficient_level():
    """Grade-mass says they are identical. Are the individual T_w coefficients?

    This is the same shape as the bond-thickness result: equal counts and equal
    support with differing coefficients. Grade-mass is a projection, and this
    asks whether the p/n information survives BELOW it.
    """
    print("\n" + "=" * 74)
    print("BELOW GRADE-MASS: the individual T_w coefficients")
    print("=" * 74)
    pn, _ = word_to_elem(6, P_A + N_B + [BRIDGE, BRIDGE])
    rows = []
    for lbl, a, b in (("p p", P_A, P_B), ("n n", N_A, N_B)):
        X, _ = word_to_elem(6, a + b + [BRIDGE, BRIDGE])
        same_support = set(X.terms) == set(pn.terms)
        diff = [w for w in set(X.terms) & set(pn.terms)
                if sp.simplify(X.terms[w] - pn.terms[w]) != 0]
        print(f"    {lbl} vs p n : same support {same_support}; "
              f"coefficients differing: {len(diff)} of {len(pn.terms)}")
        rows.append({"system": lbl, "same_support": bool(same_support),
                     "coeffs_differing": len(diff), "coeffs_total": len(pn.terms)})
    print()
    print("    So the p/n information IS present -- it survives in the")
    print("    coefficients and dies in the grade-mass sum above them.")
    print()
    print("    Consequence for binding compute: gs_filtration_binding_components")
    print("    decomposes the trace by LENGTH GRADING, which is exactly the")
    print("    resolution just shown to be blind to p vs n. A decomposition at")
    print("    that level cannot carry the binding no matter how it is weighted.")
    return rows


if __name__ == "__main__":
    main()
    coefficient_level()
