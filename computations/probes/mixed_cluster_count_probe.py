#!/usr/bin/env python3
"""`t7qv`'s cluster count `M_n(K)` must count MIXED clusters only — and that is
half the story.

WHERE THIS SITS IN `t7qv`
--------------------------
The bean's 2026-07-11 frontier update localises the open jet weight as
**geometric**, not an algebraic kernel:

> per-cluster energy = `a_D^(n)` (deuteron-anchored ≈ 2.22 MeV/bond); the knot
> topology supplies the CLUSTER COUNT `M_n(K)`. Edge set = max-contact sphere
> packing (Part 13; `A ≤ 4` simplex = `C(A,2)`, `A ≥ 5` saturates below).

and flags the resulting light-nucleus match as tempting:

> the "C(A,n) body-order combinatorial weighting" (⁴He gets
> `6·a_D² + 4·a_D³ + 1·a_D⁴ ≈ 13.88×` vs `12.72×` exp — a tempting fit-free
> light-nucleus match) is exactly Part-13's `A ≤ 4` simplex bond-count AND the
> Part-5-refuted full tower.

This probe supplies one correction to `M_n`, measures exactly how far it goes,
and shows where the remaining freedom is.

THE CORRECTION: PURE-FLAVOUR CLUSTERS DO NOT BIND
---------------------------------------------------
`C(A,n)` counts every `n`-subset of nucleons. But the two-nucleon `¹S₀` channel
— where `pp` and `nn` are forced by Pauli — is **unbound** (virtual states,
`a_pp ≈ −17.3 fm`, `a_nn ≈ −18.7 fm`); the deuteron is the only bound
two-nucleon system. Likewise there is no bound `³Li` (`ppp`) or trineutron. So a
cluster contributes only if it contains **at least one proton and at least one
neutron**:

    M_n(Z,N) = C(A,n) − C(Z,n) − C(N,n)          [A = Z + N]

At `n = 2` this is the identity `M_2 = Z·N`. Nothing here is fitted: the count is
forced by `(Z, N)` and by which channels nature binds.

RESULT AT `A ≤ 4`, WHERE THE SIMPLEX IS COMPLETE
--------------------------------------------------
One anchor — `E = B(D) = 2.2246 MeV`, since `M_2(D)·a_D^(2) = 1` — and no
per-isotope freedom, because at `A ≤ 4` every pair is in contact and `M_n`
depends on `(Z,N)` alone. There is no arrangement to choose.

    B(K) = E · Σ_n M_n(Z,N) · a_D^(n)

    iso    M_n            C(A,n) count        mixed-only count
    -------------------------------------------------------------
    T      [2, 1]         +13.75 %            −12.48 %
    ³He    [2, 1]         +25.00 %            − 3.82 %
    ⁴He    [4, 4, 1]      + 9.13 %            − 6.60 %
    -------------------------------------------------------------
    worst                  25.00 %             12.48 %

**The worst error halves** [assertion 1], and ⁴He moves from `+9.13 %` to
`−6.60 %`. For comparison in the same lane: the pairwise chain gives ⁴He at
−76 %, the jet tower at unit weight −91 %.

Note also that the mixed-only count is *uniformly under*, where `C(A,n)` is
uniformly over. Signs that agree across three isotopes are worth more than the
magnitude — an over-count that becomes an under-count on removing exactly the
unbound channels is the behaviour a real correction has.

AND WHAT IT DOES NOT DO
-----------------------
**It does not rescue `A ≥ 5`** [assertion 2]. At ⁶Li both counts diverge — `C(A,n)`
by `+772.9 %`, mixed-only by `+712.6 %`. Part 5's refutation of the full tower
stands untouched: a super-exponential `a_D^(n)` against growing combinatorial
counts cannot be linear in `A`, and removing the pure-flavour clusters removes
only ~8 % of the excess.

So the flavour correction is **necessary and not sufficient**. The `A ≥ 5` fix
has to be the other one the bean already names: Part 13's geometric saturation.

THE GEOMETRIC CAP IS REAL — AND IT IS NOT YET FIT-FREE
--------------------------------------------------------
Take the contact graph seriously and `M_n` becomes the number of `n`-cliques in
it. For six close-packed spheres in an octahedral arrangement the contact graph
is `K_{2,2,2}`: 12 edges, 8 triangles, and **zero 4-cliques** [assertion 3] —
the geometric cap kills the `n ≥ 4` terms outright, which is exactly Part 13's
"`A ≥ 5` saturates below".

That collapses the divergence. But the *arrangement* of 3 protons and 3 neutrons
on those six sites is a free choice, and it matters enormously:

    M_2 = 6, M_3 = 6   →  31.193 MeV   −2.50 %     8 of 20 labelings
    M_2 = 8, M_3 = 8   →  41.590 MeV  +29.99 %    12 of 20 labelings

against `B(⁶Li) = 31.994`. **A 32.5-point spread from a choice with no
derivation behind it** [assertion 4] — and the *majority* labeling is the bad
one. The `−2.50 %` is what this route produces when you pick the good
arrangement, which is a fit, and it is exactly the member-picking this corpus
keeps having to withdraw.

Reported because the number is attractive enough to be dangerous. Anyone
carrying `−2.50 %` forward must first derive the arrangement.

WHAT THIS CHANGES FOR `t7qv`
-----------------------------
1. `M_n` should be the **mixed** count `C(A,n) − C(Z,n) − C(N,n)`, not `C(A,n)`.
   Unfitted, forced by the bound-channel content, and it halves the `A ≤ 4`
   error.
2. The `A ≥ 5` gate is **geometric only** — flavour does not touch it. Part 5's
   refutation and Part 13's saturation are the same open item seen from two
   sides.
3. The geometric route needs the **arrangement** derived before any number from
   it is quotable.

Usage:
    python3 computations/probes/mixed_cluster_count_probe.py
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from itertools import combinations
from math import comb
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import (
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
    AME_B_LI6_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
)
from codata_constants import AME_B_HE3_MEV_VALIDATION  # noqa: E402  (AME registry)

mp.mp.dps = 30

# SW jet-prolongation periods, transcribed from binding_manybody_jet_filtration.
A_D = {2: mp.mpf("1.0"), 3: mp.mpf("1.3370"), 4: mp.mpf("2.5328"),
       5: mp.mpf("5.3761"), 6: mp.mpf("13.5598")}

# (Z, N, B_AME in MeV). AME2020.
ISO = {"D": (1, 1, AME_B_DEUTERON_MEV_VALIDATION), "T": (1, 2, AME_B_TRITIUM_MEV_VALIDATION),
       "3He": (2, 1, AME_B_HE3_MEV_VALIDATION), "4He": (2, 2, AME_B_HE4_MEV_VALIDATION),
       "6Li": (3, 3, AME_B_LI6_MEV_VALIDATION)}

E_ANCHOR = ISO["D"][2]   # B(D); M_2(D)·a_D^(2) = 1, so this is the single anchor


def m_all(Z: int, N: int, n: int) -> int:
    """Complete-simplex count: every n-subset."""
    return comb(Z + N, n)


def m_mixed(Z: int, N: int, n: int) -> int:
    """Only clusters with at least one proton AND at least one neutron."""
    return comb(Z + N, n) - comb(Z, n) - comb(N, n)


def model_B(Z: int, N: int, counter) -> mp.mpf:
    A = Z + N
    return E_ANCHOR * sum(mp.mpf(counter(Z, N, n)) * A_D[n]
                          for n in range(2, min(A, 6) + 1))


def main() -> int:
    w = WitnessBuilder("mixed-cluster-count-probe")
    w.set_description(
        "t7qv's cluster count M_n(K) must count only clusters containing at least one "
        "proton and one neutron, since pp/nn/ppp/nnn are unbound. At A <= 4, where the "
        "simplex is complete and there is no arrangement freedom, this halves the worst "
        "error (25.0% -> 12.5%) on a single deuteron anchor. It does NOT rescue A >= 5, "
        "where Part 5's refutation stands and the fix is geometric -- and that geometric "
        "route still carries a 32.5-point arrangement freedom."
    )

    # ---- assertion 1: mixed-only halves the worst error at A <= 4 -----------
    light = ["T", "3He", "4He"]
    err_all, err_mix, rows = [], [], []
    for iso in light:
        Z, N, B = ISO[iso]
        ba, bm = model_B(Z, N, m_all), model_B(Z, N, m_mixed)
        ea, em = 100 * (ba - B) / B, 100 * (bm - B) / B
        err_all.append(abs(ea))
        err_mix.append(abs(em))
        rows.append({
            "isotope": iso, "Z": Z, "N": N,
            "M_n_all": [m_all(Z, N, n) for n in range(2, Z + N + 1)],
            "M_n_mixed": [m_mixed(Z, N, n) for n in range(2, Z + N + 1)],
            "B_all_MeV": mp.nstr(ba, 8), "B_mixed_MeV": mp.nstr(bm, 8),
            "B_AME_MeV": mp.nstr(B, 8),
            "err_all_percent": mp.nstr(ea, 5), "err_mixed_percent": mp.nstr(em, 5),
        })
    worst_all, worst_mix = max(err_all), max(err_mix)
    w.add_assertion(
        "mixed_only_cluster_count_halves_the_worst_error_at_A_le_4",
        computed="1" if worst_mix * 2 < worst_all else "0",
        expected="1",
        source=f"worst |error| over T, 3He, 4He with a single deuteron anchor: "
               f"C(A,n) gives {mp.nstr(worst_all, 6)}%, mixed-only gives "
               f"{mp.nstr(worst_mix, 6)}%. The mixed count M_n = C(A,n) - C(Z,n) - C(N,n) "
               f"is forced by (Z,N) and by which two- and three-body channels nature binds "
               f"(pp, nn, ppp, nnn all unbound); at A <= 4 the simplex is complete so there "
               f"is no arrangement freedom and nothing is fitted.",
    )

    # ---- assertion 2: it does NOT rescue A >= 5 -----------------------------
    Z6, N6, B6 = ISO["6Li"]
    b6a, b6m = model_B(Z6, N6, m_all), model_B(Z6, N6, m_mixed)
    e6a, e6m = 100 * (b6a - B6) / B6, 100 * (b6m - B6) / B6
    w.add_assertion(
        "mixed_only_does_not_rescue_the_A_ge_5_divergence",
        computed="1" if (e6a > 500 and e6m > 500) else "0",
        expected="1",
        source=f"at 6Li the C(A,n) tower gives {mp.nstr(e6a, 5)}% and the mixed-only tower "
               f"{mp.nstr(e6m, 5)}% — removing the pure-flavour clusters takes out only "
               f"~8% of the excess. Part 5's refutation of the full tower stands; the "
               f"A >= 5 fix is geometric (Part 13 saturation), not flavour.",
    )

    # ---- the octahedral contact graph, and its arrangement freedom ----------
    ANTI = {(0, 1), (2, 3), (4, 5)}
    adj = lambda a, b: tuple(sorted((a, b))) not in ANTI  # noqa: E731
    clique = lambda c: all(adj(*p) for p in combinations(c, 2))  # noqa: E731
    edges = [e for e in combinations(range(6), 2) if clique(e)]
    tris = [t for t in combinations(range(6), 3) if clique(t)]
    quads = [q for q in combinations(range(6), 4) if clique(q)]

    w.add_assertion(
        "octahedral_contact_graph_has_no_four_cliques",
        computed=str(len(quads)),
        expected="0",
        source=f"K_{{2,2,2}} (six close-packed spheres, octahedral): {len(edges)} edges, "
               f"{len(tris)} triangles, {len(quads)} 4-cliques. At most four spheres can be "
               f"mutually in contact in 3D and an octahedron achieves none, so the "
               f"geometric cap kills every n >= 4 term outright. This is Part 13's "
               f"'A >= 5 saturates below', made concrete.",
    )

    # arrangement enumeration
    by_count: dict[tuple[int, int], int] = {}
    for P in combinations(range(6), 3):
        Ps = set(P)
        mixed = lambda c: 0 < len(set(c) & Ps) < len(c)  # noqa: E731
        key = (sum(1 for e in edges if mixed(e)), sum(1 for t in tris if mixed(t)))
        by_count[key] = by_count.get(key, 0) + 1
    arr_rows = []
    for (m2, m3), mult in sorted(by_count.items()):
        b = E_ANCHOR * (m2 * A_D[2] + m3 * A_D[3])
        arr_rows.append({"M_2": m2, "M_3": m3, "B_MeV": mp.nstr(b, 8),
                         "err_percent": mp.nstr(100 * (b - B6) / B6, 5),
                         "labelings_of_20": mult})
    spread = (max(mp.mpf(r["err_percent"]) for r in arr_rows)
              - min(mp.mpf(r["err_percent"]) for r in arr_rows))
    best = min(arr_rows, key=lambda r: abs(mp.mpf(r["err_percent"])))
    w.add_assertion(
        "the_octahedral_arrangement_choice_is_worth_over_thirty_points",
        computed="1" if spread > 30 else "0",
        expected="1",
        source=f"the two distinct 3p3n labelings of K_{{2,2,2}} give "
               + " and ".join(f"{r['err_percent']}% ({r['labelings_of_20']}/20 labelings)"
                              for r in arr_rows)
               + f", a spread of {mp.nstr(spread, 5)} points. The good one is the MINORITY "
                 f"({best['labelings_of_20']}/20). Nothing derives the arrangement, so "
                 f"quoting its error would be member-picking.",
    )

    # ---- data ---------------------------------------------------------------
    w.add_parameter("E_anchor_MeV", mp.nstr(E_ANCHOR, 15))
    w.add_parameter("a_D", {str(k): mp.nstr(v, 8) for k, v in A_D.items()})
    w.add_data("formula", "B(K) = E · Σ_{n=2}^{A} M_n(Z,N) · a_D^(n), "
                          "M_n = C(A,n) − C(Z,n) − C(N,n), E = B(D) = 2.2246 MeV")
    w.add_data("light_isotopes_A_le_4", rows)
    w.add_data("worst_error_percent", {"C(A,n)": mp.nstr(worst_all, 6),
                                       "mixed_only": mp.nstr(worst_mix, 6)})
    w.add_data("sign_structure", "C(A,n) over-counts uniformly (+13.75, +25.00, +9.13); "
                                 "mixed-only under-counts uniformly (−12.48, −3.82, −6.60). "
                                 "An over-count that becomes an under-count on removing "
                                 "exactly the unbound channels is what a real correction "
                                 "looks like; the sign agreement across three isotopes "
                                 "carries more than the magnitude.")
    w.add_data("A_ge_5", {
        "6Li_C(A,n)_percent": mp.nstr(e6a, 5),
        "6Li_mixed_percent": mp.nstr(e6m, 5),
        "reading": "flavour removes ~8% of the excess and nothing more. Part 5's "
                   "refutation stands; the fix is geometric.",
    })
    w.add_data("octahedral_contact_graph", {
        "graph": "K_{2,2,2} — 12 edges, 8 triangles, 0 four-cliques",
        "why_it_matters": "n-clique counting caps the tower at n = 3 for six close-packed "
                          "spheres, which is Part 13's saturation made concrete.",
        "arrangements": arr_rows,
        "spread_points": mp.nstr(spread, 5),
        "warning": "the attractive number here is produced by CHOOSING the arrangement, "
                   "and the good one is the minority labeling. Nothing derives it. Do not "
                   "carry it forward without one.",
    })
    w.add_data("for_t7qv", [
        "M_n should be the MIXED count C(A,n) − C(Z,n) − C(N,n), not C(A,n). Unfitted, and "
        "it halves the A <= 4 worst error from 25.0% to 12.5%.",
        "The A >= 5 gate is geometric only — flavour does not touch it. Part 5's refutation "
        "and Part 13's saturation are one open item seen from two sides.",
        "The geometric route needs the ARRANGEMENT derived before any number from it is "
        "quotable; it currently carries 32.5 points of freedom at 6Li.",
    ])
    w.add_data("verdict", (
        "The cluster count M_n(K) in t7qv's geometric weight must count only mixed clusters "
        "— at least one proton and one neutron — because pp, nn, ppp and nnn are all "
        "unbound. M_n = C(A,n) − C(Z,n) − C(N,n), which is Z·N at n = 2. On a single "
        "deuteron anchor this halves the worst A <= 4 error, 25.0% -> 12.5%, with 4He at "
        "−6.60%, and flips a uniform over-count into a uniform under-count. It does not "
        "rescue A >= 5, where the divergence is geometric; and the geometric route still "
        "carries a 32.5-point arrangement freedom at 6Li whose favourable member is the "
        "minority labeling."
    ))

    out = w.save()
    print(f"wrote {out}")
    print(f"  {'iso':6}{'M_n mixed':>16}{'C(A,n) err':>13}{'mixed err':>12}")
    for r in rows:
        print(f"  {r['isotope']:6}{str(r['M_n_mixed']):>16}"
              f"{r['err_all_percent'] + '%':>13}{r['err_mixed_percent'] + '%':>12}")
    print(f"  worst |err| : {mp.nstr(worst_all, 5)}%  ->  {mp.nstr(worst_mix, 5)}%   "
          f"(single deuteron anchor, nothing fitted)")
    print()
    print(f"  6Li full tower : C(A,n) {mp.nstr(e6a, 5)}% , mixed {mp.nstr(e6m, 5)}%  "
          f"-- Part 5 refutation stands")
    print(f"  octahedral K(2,2,2): {len(edges)} edges, {len(tris)} triangles, "
          f"{len(quads)} 4-cliques")
    for r in arr_rows:
        print(f"    M_2={r['M_2']:<3} M_3={r['M_3']:<3} -> {r['B_MeV']:>10} MeV  "
              f"{r['err_percent']:>8}%   ({r['labelings_of_20']}/20 labelings)")
    print(f"  arrangement freedom: {mp.nstr(spread, 5)} points -- the good one is the "
          f"minority. Not fit-free.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
