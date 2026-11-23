#!/usr/bin/env python3
"""`A >= 5` saturation and the octahedron: the arrangement IS derivable. The labelling is not.

WHAT WAS OPEN
-------------
Bean `t7qv` carries two linked items: the `A >= 5` geometric saturation, and
*"deriving the octahedral arrangement"*. The contact graphs in
`gap2_irreducible_triple_bracket_probe.py::_deltahedron` are **hardcoded** with
the comment *"3-D packing fact"* — asserted, not derived — and the bean records
that on the resulting `6Li` numbers *"nothing derives the arrangement, so
-2.50 % is a member-pick"*.

This probe separates those into two questions with different answers.

1. THE SATURATION LAW IS EULER'S FORMULA
------------------------------------------
A convex polyhedron all of whose faces are triangles satisfies `2E = 3F`, so
`V - E + F = 2` gives

    E  =  3V - 6

with no packing input at all. Against the corpus's hardcoded deltahedra:

    A     |E| hardcoded    3A - 6    C(A,2)    saturates?
    2           1           n/a         1      no (complete)
    3           3            3          3      no (complete)
    4           6            6          6      no (complete)
    5           9            9         10      yes
    6          12           12         15      yes
    7          15           15         21      yes

Every hardcoded value **is** `3A - 6`. So the edge counts were never a free
choice; they are Euler's formula for a simplicial polyhedron.

2. THE `A <= 4` / `A >= 5` CROSSOVER IS A ROOT OF A QUADRATIC
---------------------------------------------------------------
The simplex count and the deltahedron count agree exactly when

    3A - 6  =  A(A-1)/2   <=>   A^2 - 7A + 12 = 0   <=>   (A - 3)(A - 4) = 0

so they coincide at **`A = 3` and `A = 4`** and `3A - 6 < C(A,2)` strictly for
`A >= 5`. **The crossover the corpus states as a modelling boundary is a root of
a quadratic.** That is the whole content of "`A <= 4` simplex, `A >= 5` saturates
below", and it is derived.

3. THE OCTAHEDRON IS FORCED AT `A = 6`
----------------------------------------
Given `A = 6` and `E = 12`, the degree sum is 24, so the graph is 4-regular on 6
vertices. Enumerated exhaustively: **15 labelled such graphs, exactly 1 up to
isomorphism**, and the corpus's graph is it. The reason is one line — the
complement of a 4-regular graph on 6 vertices is 1-regular, i.e. a perfect
matching, and all perfect matchings on 6 vertices are isomorphic. So the
octahedron `K_{2,2,2}` (three antipodal pairs, antipodes unbonded) is the unique
possibility.

**"Deriving the octahedral arrangement" is therefore done**, conditional on the
deltahedron hypothesis in §5.

4. THE LABELLING IS NOT DETERMINED — AND THE NATURAL PRINCIPLE PICKS THE WRONG ONE
-----------------------------------------------------------------------------------
The arrangement fixes the *graph*; it does not say which vertices are protons.
Since a cluster binds only if **mixed** (`mixed_cluster_count_probe`), the counts
`M_n` depend on that labelling. Enumerated over every labelling:

    6Li  Z=3 N=3, octahedron, 20 labellings
        (M2,M3,M4) = (8, 8, 0)   12 labellings  (60 %)
        (M2,M3,M4) = (6, 6, 0)    8 labellings  (40 %)

and with `a_D` anchored on `D` and `T` only:

        (6, 6, 0)  ->  B = 31.193 MeV   vs AME 31.994   ->   -2.50 %
        (8, 8, 0)  ->  B = 41.590 MeV   vs AME 31.994   ->  +29.99 %

reproducing the bean's two numbers exactly. **The favourable `-2.50 %` is the
MINIMUM-mixed class.** The obvious extremal principle — a bound state maximises
its binding contacts — selects `(8,8,0)`, the `+29.99 %` one. So:

  - max-mixed is derivable and gives the **worse** answer;
  - the better answer needs min-mixed, i.e. *minimising* the number of bonded
    mixed clusters, which nothing in the corpus motivates and which is the
    opposite of a binding principle.

The `-2.50 %` is therefore not merely a member-pick — it is a pick **against**
the only extremal principle available. That is a stronger statement than the
bean's, and it closes the "derive the arrangement" route as a way of rescuing it.

Geometrically the min-mixed class is the one where the three protons form a face
and the three neutrons the opposite face — maximal *like*-clustering. Whether
that is motivated is a modelling question this probe does not answer; it only
records that it is not a binding-maximisation.

The same indeterminacy at neighbouring `A`, for scale:

    5Li  Z=3 A=5, 10 labellings:  (6,7,2)x3, (6,6,2)x1, (5,6,2)x6
    7Li  Z=3 A=7, 35 labellings:  (10,10,0)x10, (9,9,0)x10, (8,8,0)x5, (7,7,0)x10
    6He  Z=2 A=6, 15 labellings:  (8,8,0)x3, (6,6,0)x12

`7Li` spans `M2 = 7..10` across labellings — a 43 % spread in the leading term
with nothing choosing between them.

5. SCOPE — WHAT IS HYPOTHESIS, NOT DERIVATION
-----------------------------------------------
Everything above is conditional on the arrangement being a **convex deltahedron**.
That is the corpus's modelling choice and this probe does not derive it. Two
consequences worth recording, both classification facts (Freudenthal–van der
Waerden) cited rather than proved here:

  - convex deltahedra exist only for `A` in `{4,5,6,7,8,9,10,12}` — **there is
    none with 11 vertices**, so the model has a hole at `A = 11` that no
    labelling argument can fill;
  - maximum-contact packings and convex deltahedra are not the same family in
    general, so "max-contact" and "deltahedron" should not be used
    interchangeably above `A = 9`.

Within `4 <= A <= 7`, where the corpus actually uses it, the two agree and
§§1-3 stand.

DISCIPLINE
----------
Euler and the quadratic are exact; the 4-regular enumeration is exhaustive; the
labelling distributions are exhaustive. `a_D` values are the corpus's own, used
only to reproduce the bean's two published figures — no fit, and no new binding
claim is made. No `B_AME` enters §§1-4 except in that reproduction.

-- Ref: [manuscript] bean t7qv; gap2_irreducible_triple_bracket_probe.py;
   mixed_cluster_count_probe.py
"""
from __future__ import annotations

import itertools
import sys
import warnings
from collections import Counter
from pathlib import Path

warnings.filterwarnings("ignore")

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))
import _path_bridge  # noqa: F401,E402

import networkx as nx  # noqa: E402
import sympy as sp  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION
from codata_constants import AME_B_LI6_MEV_VALIDATION  # noqa: E402  (AME registry)

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

# The corpus's own a_D, and B(D) as the single-bond anchor.
A_D = {2: 1.0, 3: 1.3370, 4: 2.5328}
B_D = AME_B_DEUTERON_MEV_VALIDATION
B_6LI_AME = float(AME_B_LI6_MEV_VALIDATION)


def deltahedron(A: int) -> set:
    """Verbatim re-implementation of `gap2_irreducible_triple_bracket_probe`."""
    E: set = set()
    add = lambda a, b: E.add(frozenset((a, b)))  # noqa: E731
    if A <= 4:
        for a, b in itertools.combinations(range(A), 2):
            add(a, b)
    elif A == 5:
        for a, b in itertools.combinations(range(3), 2):
            add(a, b)
        for ap in (3, 4):
            for e in range(3):
                add(ap, e)
    elif A == 6:
        for a, b in itertools.combinations(range(6), 2):
            if {a, b} not in ({0, 1}, {2, 3}, {4, 5}):
                add(a, b)
    elif A == 7:
        for e in range(5):
            add(e, (e + 1) % 5)
        for ap in (5, 6):
            for e in range(5):
                add(ap, e)
    else:
        raise ValueError(f"no deltahedron recorded for A={A}")
    return E


def cliques(A: int, E: set, k: int) -> list:
    return [c for c in itertools.combinations(range(A), k)
            if all(frozenset(p) in E for p in itertools.combinations(c, 2))]


def mixed_profile(A: int, E: set, protons) -> tuple:
    P = set(protons)
    return tuple(sum(1 for c in cliques(A, E, k)
                     if (set(c) & P) and (set(c) - P)) for k in (2, 3, 4))


def main() -> int:
    assertions = []
    print("t7qv — A >= 5 saturation, the octahedron, and the labelling")

    # ── A1. E = 3A - 6 reproduces every hardcoded deltahedron ─────────
    print("\n  1. Euler: a simplicial polyhedron has E = 3V - 6")
    print(f"     {'A':>3s} {'|E| hardcoded':>14s} {'3A-6':>7s} {'C(A,2)':>8s}  saturates?")
    rows, euler_ok = [], True
    for A in range(2, 8):
        E = deltahedron(A)
        c2 = A * (A - 1) // 2
        eu = 3 * A - 6 if A >= 3 else None
        match = (eu is None) or (len(E) == eu)
        if A >= 4:
            euler_ok = euler_ok and (len(E) == eu)
        rows.append({"A": A, "edges": len(E), "euler_3A_minus_6": eu,
                     "simplex_C_A_2": c2, "saturates": len(E) < c2})
        print(f"     {A:>3d} {len(E):>14d} {str(eu):>7s} {c2:>8d}  "
              f"{'yes' if len(E) < c2 else 'no (complete)'}")
    print(f"\n  A1  every hardcoded |E| equals 3A - 6 (A >= 4) ........... "
          f"{'PASS' if euler_ok else 'FAIL'}")
    print("      => the edge counts were never a free choice.")
    assertions.append(("hardcoded_deltahedra_are_euler_3A_minus_6", euler_ok,
                       str([(r["A"], r["edges"], r["euler_3A_minus_6"])
                            for r in rows])))

    # ── A2. The crossover is a root of a quadratic ────────────────────
    Asym = sp.symbols("A")
    roots = sorted(sp.solve(sp.Eq(3 * Asym - 6, Asym * (Asym - 1) / 2), Asym))
    ok = roots == [3, 4]
    print(f"\n  2. 3A - 6 = A(A-1)/2  <=>  A^2 - 7A + 12 = 0  <=>  "
          f"(A-3)(A-4) = 0")
    print(f"     roots: {roots}")
    print(f"\n  A2  the simplex/deltahedron crossover is exactly A in {{3,4}} "
          f"{'PASS' if ok else 'FAIL'}")
    print("      => 'A <= 4 simplex, A >= 5 saturates below' is a root of a")
    print("         quadratic, not a modelling boundary.")
    assertions.append(("crossover_is_the_quadratic_root_3_and_4", ok,
                       f"roots {roots}"))

    # ── A3. The octahedron is the unique 4-regular graph on 6 vertices ─
    pairs = list(itertools.combinations(range(6), 2))
    labelled, iso = 0, []
    for edges in itertools.combinations(pairs, 12):
        deg = [0] * 6
        for a, b in edges:
            deg[a] += 1
            deg[b] += 1
        if all(d == 4 for d in deg):
            labelled += 1
            g = nx.Graph()
            g.add_nodes_from(range(6))
            g.add_edges_from(edges)
            if not any(nx.is_isomorphic(g, hh) for hh in iso):
                iso.append(g)
    oct_g = nx.Graph()
    oct_g.add_nodes_from(range(6))
    oct_g.add_edges_from(tuple(sorted(e)) for e in deltahedron(6))
    ok = (len(iso) == 1) and nx.is_isomorphic(oct_g, iso[0])
    print(f"\n  3. A = 6, E = 12 forces 4-regularity (degree sum 24)")
    print(f"     4-regular graphs on 6 vertices: {labelled} labelled, "
          f"{len(iso)} up to isomorphism")
    print(f"     the corpus graph is that one: "
          f"{nx.is_isomorphic(oct_g, iso[0]) if iso else False}")
    print(f"\n  A3  the octahedron is FORCED at A = 6 .................... "
          f"{'PASS' if ok else 'FAIL'}")
    print("      (complement of a 4-regular graph on 6 vertices is a perfect")
    print("       matching, and all such are isomorphic.)")
    assertions.append(("octahedron_is_the_unique_4_regular_graph_on_6", ok,
                       f"{labelled} labelled, {len(iso)} iso class"))

    # ── A4. The labelling is undetermined, and max-mixed picks worse ──
    print("\n  4. the LABELLING is not fixed by the arrangement")
    dists = {}
    for lab, Z, A in (("5Li", 3, 5), ("6Li", 3, 6), ("7Li", 3, 7),
                      ("6He", 2, 6)):
        E = deltahedron(A)
        d = Counter(mixed_profile(A, E, P)
                    for P in itertools.combinations(range(A), Z))
        dists[lab] = d
        tot = sum(d.values())
        print(f"     {lab}  Z={Z} N={A - Z} A={A}  |E|={len(E)}  "
              f"{tot} labellings")
        for key in sorted(d, key=lambda k: (-k[0], -k[1])):
            print(f"        (M2,M3,M4) = {str(key):14s} x{d[key]:<3d} "
                  f"({100 * d[key] / tot:.1f} %)")

    d6 = dists["6Li"]
    print("\n     6Li binding per labelling class (a_D anchored on D and T):")
    preds = {}
    for key in sorted(d6):
        B = B_D * sum(key[i] * A_D[i + 2] for i in range(3))
        preds[key] = B
        print(f"        {str(key):14s} x{d6[key]:<3d}  B = {B:7.3f} MeV   "
              f"vs AME {B_6LI_AME}  ->  {100 * (B - B_6LI_AME) / B_6LI_AME:+6.2f} %")
    mx, mn = max(d6), min(d6)
    err = {k: abs(preds[k] - B_6LI_AME) for k in preds}
    max_mixed_is_worse = err[mx] > err[mn]
    ok = (len(d6) > 1) and max_mixed_is_worse
    print(f"\n  A4  max-mixed selects the WORSE labelling ................ "
          f"{'PASS' if ok else 'FAIL'}")
    print(f"      max-mixed {mx} -> "
          f"{100 * (preds[mx] - B_6LI_AME) / B_6LI_AME:+.2f} %;  "
          f"min-mixed {mn} -> {100 * (preds[mn] - B_6LI_AME) / B_6LI_AME:+.2f} %")
    print("      The obvious extremal principle — a bound state maximises its")
    print("      binding contacts — gives +29.99 %. The favourable -2.50 % is")
    print("      the MINIMUM-mixed class, i.e. a pick AGAINST the only")
    print("      principle available, not merely a member-pick.")
    assertions.append(("max_mixed_labelling_gives_the_worse_prediction", ok,
                       f"max {mx} err {err[mx]:.3f}; min {mn} err {err[mn]:.3f}"))

    print("\n### VERDICT: the ARRANGEMENT is derivable and now derived — the")
    print("    edge law is Euler (E = 3A - 6), the A<=4/A>=5 crossover is the")
    print("    root pair {3,4} of a quadratic, and the octahedron is the unique")
    print("    4-regular graph on 6 vertices. The LABELLING is not, and the")
    print("    only extremal principle available picks the worse of the two")
    print("    6Li classes. Deriving the arrangement does not rescue -2.50 %;")
    print("    it shows the rescue would have to come from somewhere else.")
    print("    All of §§1-3 is conditional on the convex-deltahedron")
    print("    hypothesis, which is the corpus's modelling choice and is NOT")
    print("    derived here — and which has no A = 11 member at all.")

    all_ok = all(a[1] for a in assertions)

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("geometric-saturation-and-labelling",
                                engine="python", output_dir=COMP)
            wb.set_description(
                "EXPLORATORY (bean t7qv): separates the two linked open items — "
                "the A >= 5 geometric saturation and 'deriving the octahedral "
                "arrangement' — into questions with different answers. DERIVED: "
                "(1) every hardcoded deltahedron edge count in "
                "gap2_irreducible_triple_bracket_probe IS Euler's E = 3A - 6 for "
                "a simplicial polyhedron, so the counts were never a free "
                "choice; (2) 3A - 6 = C(A,2) exactly at A = 3 and 4, since "
                "A^2 - 7A + 12 = (A-3)(A-4), so the 'A <= 4 simplex, A >= 5 "
                "saturates' boundary is a quadratic root; (3) at A = 6 the "
                "degree sum forces 4-regularity, and there are 15 labelled but "
                "exactly ONE isomorphism class of 4-regular graph on 6 vertices "
                "— the octahedron — so the arrangement is forced. NOT DERIVED, "
                "and worse than the bean recorded: the LABELLING. 6Li's 20 "
                "labellings fall into (8,8,0) x12 and (6,6,0) x8, giving "
                "+29.99 % and -2.50 %; the obvious extremal principle (a bound "
                "state maximises its binding contacts) selects the +29.99 % "
                "class, so the favourable -2.50 % is a pick AGAINST the only "
                "principle available, not merely a member-pick. 7Li spans "
                "M2 = 7..10 across labellings. All conditional on the convex-"
                "deltahedron hypothesis, not derived here, which has no A = 11 "
                "member. No fit; no new binding claim.")
            wb.add_data("euler_table", rows)
            wb.add_data("crossover_roots", [int(r) for r in roots])
            wb.add_data("four_regular_on_6", {"labelled": labelled,
                                              "iso_classes": len(iso)})
            wb.add_data("labelling_distributions",
                        {k: {str(kk): vv for kk, vv in v.items()}
                         for k, v in dists.items()})
            wb.add_data("li6_predictions",
                        {str(k): f"{v:.6f}" for k, v in preds.items()})
            for name, passed, detail in assertions:
                wb.add_assertion(name=name, computed=str(int(bool(passed))),
                                 expected="1", tolerance=0, source=str(detail))
            wb.add_caveat(
                "Everything in sections 1-3 is conditional on the arrangement "
                "being a CONVEX DELTAHEDRON — the corpus's modelling choice, "
                "not derived here. Two consequences, cited from the "
                "Freudenthal-van der Waerden classification rather than proved: "
                "convex deltahedra exist only for A in {4,5,6,7,8,9,10,12}, so "
                "there is NO A = 11 member and the model has a hole there that "
                "no labelling argument can fill; and maximum-contact packings "
                "and convex deltahedra are not the same family in general, so "
                "the two terms should not be used interchangeably above A = 9. "
                "Within 4 <= A <= 7, where the corpus uses it, they agree.")
            wb.add_caveat(
                "The a_D values and B(D) anchor are the corpus's own and are "
                "used ONLY to reproduce the two figures the bean already "
                "publishes (31.193 / -2.50 % and 41.590 / +29.99 %). No fit is "
                "performed and no new binding claim is made; the finding is "
                "about which labelling an extremal principle selects, not about "
                "the value.")
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:  # pragma: no cover
            print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
