#!/usr/bin/env python3
"""D1-c's stated vertex assignment is EXCLUDED — H_3 has 3 blocks, the datum needs 4.

# Ref: .beans/qou-q9ih--d1-route-c-m1-construct-the-qw-reproducing-34-bar.md
# Ref: computations/qbeta/dt_d1a_small_quiver_two_ray_scan_probe.py
# Ref: computations/qbeta/dt_third_knot_trefoil_count_probe.py

WHAT D1-c PROPOSES. "Vertices from Wedderburn blocks of H3(q) (both knots are
3-braids), bar-graded per DTChiralityBarInvolutionLink; rays from the bar
involution on stability." It is the ONLY D1 route whose success would be a
DERIVATION rather than a candidate, and the 2026-08-22 assessment called its
entry test right but its inputs "under-specified": the exact (7,1) bar-split
target, and the blocks->spectrum "natural pairing" dictionary.

HALF OF THAT BLOCKER IS ALREADY GONE. `dt_d1a_small_quiver_two_ray_scan_probe`
Result 0 shows `(7,1)` is `(plus+minus, plus-minus)` — arithmetic on `(4,3)`,
zero independent information. So the target D1-c must hit is `(4,3)`, full stop;
there is no separate bar-split condition to specify. What remained was the
dictionary.

THIS PROBE SHOWS THE OTHER HALF DOES NOT NEED SPECIFYING, because the vertex
assignment is excluded before any dictionary is chosen.

THE MEASURED BOUND. Across every acyclic quiver on `V` vertices, the maximum
number of stable objects sharing ONE ray (slope) is exactly `V` — never more:

    V   quivers scanned   max per-ray stable count   ever exceeds V
    2         3                     2                    no
    3        27                     3                    no
    4       729                     4                    no

and for `V = 3` the cap is **not** an artifact of the enumeration box. Growing
the box grows the root system without ever lifting the cap:

    DMAX  TMAX   max #roots on a quiver   max per-ray count
      3     3            18                      3
      4     4            24                      3
      5     4            30                      3
      6     5            39                      3

The likely mechanism (stated as the reason, NOT proved here): at a fixed slope
the theta-semistable objects form an abelian category whose SIMPLE objects are
the theta-stables of that slope, and its rank is bounded by the rank of the
quiver's K-theory, which is `V`. Measured, not derived — see NOT CLAIMED.

THE CONSEQUENCE FOR D1-c. `H_3(q)` has exactly THREE Wedderburn blocks —
`(3)` dim 1, `(2,1)` dim 2, `(1^3)` dim 1. So D1-c's stated vertex assignment
gives `V = 3`, whose per-ray ceiling is 3. **The datum needs a ray carrying 4.**
D1-c as written therefore cannot produce `(4,3)`, whatever the blocks->spectrum
dictionary turns out to be. That is a bounded negative on the ASSIGNMENT, not on
the route.

Note this is the same bound the bean's D1-e anticipated ("the vertex lower bound
V>=4 from ray-count 4 is near-trivial pigeonhole"). What is new is not the bound
but WHERE IT LANDS: the bean lists D1-e and D1-c as separate entries, so nobody
had pointed the one at the other. D1-c's own vertex count violates it.

🛑 WHICH READING OF "VERTICES FROM WEDDERBURN BLOCKS"? The bean does not say,
and the two readings give DIFFERENT verdicts — so the exclusion above is
conditional on the one it names:

  * ONE VERTEX PER BLOCK  ->  V = 3   (blocks (3), (2,1), (1^3))     EXCLUDED
  * dimension-weighted    ->  V = 4   (dims 1 + 2 + 1)               clears it

"Vertices from Wedderburn blocks" reads most naturally as one vertex per block,
which is the V = 3 case and is excluded. But `H_3` has total dimension 4, so a
dimension-weighted vertex set clears the bound exactly — and the bean does not
disambiguate. The exclusion is therefore of the NATURAL READING, not of every
reading, and this probe reports both counts rather than picking one.

Worth noting: BOTH escapes land on V = 4 — the dimension-weighted reading, and
the blocks-plus-abelian repair below. That the two independent routes to a
workable vertex set agree on 4 is suggestive, and is not evidence.

A STRUCTURALLY-MOTIVATED REPAIR, PROPOSED AND NOT TESTED. The corpus's own
decomposition of the datum is

    total_connections = irreducible_points + abelian_connections   (abelian = 1)

— 4_1: 2 + 1 = 3, 5_2: 3 + 1 = 4, 3_1: 1 + 1 = 2. So the natural vertex set is
not the three blocks alone but **the three blocks TOGETHER WITH the abelian
connection**, giving `V = 4` and clearing the bound exactly. That reconciliation
comes from the corpus's own arithmetic rather than from fitting to 4, which is
why it is worth recording — but it is a PROPOSAL. Nothing here tests whether
such a quiver reproduces `(4,3)` at two rays, and a quiver whose only credential
is matching the datum would still be a labeled CANDIDATE (this bean's
anti-laundering rule).

NOT CLAIMED. That no quiver-with-potential reproduces the datum; `W = 0`
throughout and a potential can only cut further. That the `V` bound is a
theorem — it is measured over the stated ranges with a numerical proxy for King
stability, and the mechanism above is offered as the reason, not a proof. That
D1-c is dead: only its stated vertex assignment is excluded. Nothing derives
`A_omega`; the datum stays certified-imported. Scope-(a).

NO FLOAT64: integer and exact `Fraction` arithmetic; no floating point enters.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401,E402

from witness_base import WitnessBuilder  # noqa: E402

# H_3(q) Wedderburn blocks: partitions of 3, with their dimensions.
H3_BLOCKS = {"(3)": 1, "(2,1)": 2, "(1,1,1)": 1}
DATUM = {"4_1": 3, "5_2": 4, "3_1": 2}     # total connections; 5_2 needs a ray of 4


def tits(m, d):
    v = sum(x * x for x in d)
    n = len(d)
    for i in range(n):
        for j in range(n):
            if m[i][j]:
                v -= m[i][j] * d[i] * d[j]
    return v


def real_roots(m, n, dmax):
    return [d for d in itertools.product(range(dmax + 1), repeat=n)
            if any(d) and tits(m, d) == 1]


def slope_counts(roots, rootset, theta):
    mu = {d: Fraction(sum(t * x for t, x in zip(theta, d)), sum(d)) for d in roots}
    tally = {}
    for d in roots:
        if all(not (e != d and all(a <= b for a, b in zip(e, d)) and mu[e] >= mu[d])
               for e in rootset):
            tally[mu[d]] = tally.get(mu[d], 0) + 1
    return tally


def max_per_ray(n, arrow_max, dmax, tmax):
    """Largest number of stable objects sharing one slope, over all such quivers."""
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    best, nq, most_roots = 0, 0, 0
    for vals in itertools.product(range(arrow_max + 1), repeat=len(pairs)):
        m = [[0] * n for _ in range(n)]
        for (i, j), v in zip(pairs, vals):
            m[i][j] = v
        nq += 1
        roots = real_roots(m, n, dmax)
        if not roots:
            continue
        most_roots = max(most_roots, len(roots))
        rootset = set(roots)
        for th in itertools.product(range(-tmax, tmax + 1), repeat=n):
            if any(th):
                for c in slope_counts(roots, rootset, th).values():
                    best = max(best, c)
    return best, nq, most_roots


def main() -> int:
    w = WitnessBuilder("dt-d1c-hecke-block-vertex-bound", engine="python-int")
    w.set_description(
        "D1-c's stated vertex assignment is excluded: the maximum number of "
        "stable objects on one ray is the vertex count V, H_3(q) has 3 "
        "Wedderburn blocks, and the datum needs a ray carrying 4."
    )
    ok = []

    def check(name, passed, note=""):
        ok.append(bool(passed))
        w.add_assertion(name, computed="1" if passed else "0",
                        expected="1", tolerance="0")
        print(f"  [{'PASS' if passed else 'FAIL'}] {name} {note}")

    check("H3_has_exactly_THREE_Wedderburn_blocks",
          len(H3_BLOCKS) == 3 and sum(H3_BLOCKS.values()) == 4,
          "((3) dim 1, (2,1) dim 2, (1^3) dim 1 — three blocks, total dim 4)")
    check("the_datum_needs_a_ray_carrying_FOUR",
          max(DATUM.values()) == 4 and DATUM["5_2"] == 4,
          "(5_2 = 4; 4_1 = 3; 3_1 = 2)")

    # ---- the vertex bound ---------------------------------------------------
    print(f"\n  max stable objects on ONE ray, by vertex count:")
    print(f"    {'V':>2}{'quivers':>9}{'max per-ray':>13}{'exceeds V?':>12}")
    bound_rows = []
    for n, am in ((2, 2), (3, 2), (4, 2)):
        best, nq, _ = max_per_ray(n, am, 3, 3)
        bound_rows.append({"vertices": n, "quivers": nq, "max_per_ray": best,
                           "exceeds_V": best > n})
        print(f"    {n:>2}{nq:>9}{best:>13}{str(best > n):>12}")
    check("the_per_ray_ceiling_IS_the_vertex_count_and_is_never_exceeded",
          all(r["max_per_ray"] == r["vertices"] and not r["exceeds_V"]
              for r in bound_rows),
          "(V = 2,3,4 all cap at exactly V)")

    # ---- and it is not a box artifact --------------------------------------
    print(f"\n  V=3 box sensitivity (arrows 0..3) — does a bigger box reach 4?")
    print(f"    {'DMAX':>5}{'TMAX':>6}{'max #roots':>12}{'max per-ray':>13}")
    box_rows = []
    for dmax, tmax in ((3, 3), (4, 4), (5, 4)):
        best, _, mr = max_per_ray(3, 3, dmax, tmax)
        box_rows.append({"dmax": dmax, "tmax": tmax, "max_roots": mr,
                         "max_per_ray": best})
        print(f"    {dmax:>5}{tmax:>6}{mr:>12}{best:>13}")
    check("the_V3_cap_SURVIVES_growing_the_box",
          all(r["max_per_ray"] == 3 for r in box_rows)
          and box_rows[-1]["max_roots"] > box_rows[0]["max_roots"],
          f"(roots grow {box_rows[0]['max_roots']} -> {box_rows[-1]['max_roots']} "
          "while the cap stays 3 — so the cap is structural in V, not a "
          "truncation of the root system)")

    # ---- the consequence ----------------------------------------------------
    check("D1c_ONE_VERTEX_PER_BLOCK_reading_IS_EXCLUDED",
          len(H3_BLOCKS) < DATUM["5_2"],
          f"(H_3 gives V = {len(H3_BLOCKS)}, ceiling {len(H3_BLOCKS)}; the datum "
          f"needs {DATUM['5_2']}) — under THIS reading D1-c cannot produce (4,3) "
          "WHATEVER the blocks->spectrum dictionary turns out to be")
    check("but_the_DIMENSION_WEIGHTED_reading_clears_the_bound",
          sum(H3_BLOCKS.values()) == DATUM["5_2"],
          f"(dims 1+2+1 = {sum(H3_BLOCKS.values())}) — the bean does not "
          "disambiguate, so the exclusion is of the NATURAL reading, not of "
          "every reading")

    # ---- the repair, proposed not tested -----------------------------------
    check("blocks_PLUS_the_abelian_connection_clears_the_bound_exactly",
          len(H3_BLOCKS) + 1 == DATUM["5_2"],
          "(3 blocks + 1 abelian = 4 = the corpus's own "
          "total = irreducible + abelian decomposition) — PROPOSAL, untested")

    w.add_data("d1c_stated_assignment", {
        "vertices_from": "Wedderburn blocks of H_3(q)",
        "blocks": H3_BLOCKS, "V": len(H3_BLOCKS),
        "per_ray_ceiling": len(H3_BLOCKS),
        "datum_requires": DATUM["5_2"],
        "reading_one_vertex_per_block": {"V": 3, "ceiling": 3,
                                         "verdict": "EXCLUDED — the ceiling is "
                                                    "below the requirement, so "
                                                    "no dictionary rescues it"},
        "reading_dimension_weighted": {"V": sum(H3_BLOCKS.values()),
                                       "verdict": "clears the bound exactly"},
        "which_the_bean_means": "not disambiguated. 'Vertices from Wedderburn "
                                "blocks' reads most naturally as one per block "
                                "(V=3, excluded), but H_3 has total dimension 4 "
                                "so the weighted reading survives.",
        "note": "BOTH escapes land on V = 4 — the dimension-weighted reading and "
                "the blocks-plus-abelian repair. Suggestive, not evidence.",
    })
    w.add_data("vertex_bound", {"rows": bound_rows,
                                "statement": "max stable objects on one ray = V",
                                "mechanism_offered_not_proved":
                                    "at a fixed slope the theta-semistables form "
                                    "an abelian category whose simples are the "
                                    "theta-stables; its rank is bounded by the "
                                    "rank of K-theory, which is V"})
    w.add_data("box_sensitivity", {"rows": box_rows,
                                   "conclusion": "cap is structural in V, not a "
                                                 "truncation artifact"})
    w.add_data("proposed_repair_UNTESTED", {
        "vertex_set": "the three H_3 blocks TOGETHER WITH the abelian connection",
        "V": 4,
        "why_not_a_fit": "it is the corpus's own decomposition "
                         "total_connections = irreducible_points + "
                         "abelian_connections (abelian = 1), not a choice made "
                         "to reach 4: 4_1 = 2+1, 5_2 = 3+1, 3_1 = 1+1",
        "status": "PROPOSAL. Nothing here tests whether such a quiver reproduces "
                  "(4,3) at two rays, and a quiver whose only credential is "
                  "matching the datum stays a labeled CANDIDATE.",
    })
    w.add_data("what_this_does_NOT_close", {
        "D1c_the_route": "only the ONE-VERTEX-PER-BLOCK reading of the vertex assignment is excluded; the dimension-weighted reading survives, and the bean does not say which it means",
        "potential": "W = 0 throughout; a potential can only cut further",
        "the_bound_is_measured": "not proved — a numerical proxy for King "
                                 "stability over the stated ranges",
        "derives_A_omega": False,
    })

    passed = sum(ok)
    print(f"\n  {passed}/{len(ok)} checks passed")
    w.save()
    return 0 if passed == len(ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
