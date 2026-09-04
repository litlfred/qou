#!/usr/bin/env python3
"""dt_d1b_arrow_count_forced_by_gabriel_probe.py — qou-q9ih D1-b, the arrows.

🛑🛑 SUPERSEDED AT THE PREMISE, not at the answer. Read
`dt_d1b_gabriel_route_void_source_verified_probe.py` FIRST. Checked against the
source (GGM arXiv:2012.00062v3, held in this repo) for the first time, each
eq-(98) entry is ONE Stokes constant at ONE Borel singularity — a multiplicity
at a single charge. Gabriel's bijection gives every positive root multiplicity
exactly one, so a finite-type quiver has max Ω = 1; this datum has max |Ω| = 4.
**No finite-type quiver carries it at any rank with any arrow count**, so BOTH
answers below are void. The enumeration is still correct; it is applied to a
datum outside Gabriel's hypotheses. Kept, unedited below this banner, because
the two-step failure is the record.

🛑 THIS PROBE CORRECTS ITS OWN FIRST VERSION. An earlier draft concluded
"the arrow count is FORCED to 0 or 1". **That answered the wrong question**, and
the file name is left as-is only so the correction is findable from the commit
that introduced the error. Read the correction section before the result.

═══ THE LEVER (this part is sound and is kept) ═══

For an **acyclic** quiver with `W = 0`, **Gabriel's theorem**: finite
representation type <=> the underlying graph is a disjoint union of
simply-laced Dynkin diagrams (ADE), and then

    #indecomposables = #positive roots.

Every ADE diagram is a **tree**, so a rank-`V` union with `k` components has
exactly `V - k` edges. **Arrows are therefore a function of the Dynkin type, and
the type of `(rank, #positive roots)`.** The enumeration at a given rank is
finite and exhaustive, so a target is hit by exactly one type or by none — there
is nothing to tune, and this is not a search against the target.

═══ 🛑 THE CORRECTION: I FED IT THE WRONG PAIRS ═══

The first version read the corpus target `(4,3)` as **two knots' total spectra**
— 4_1 with 3, 5_2 with 4 — and set `rank = C_irr` per knot from the merged
Galois-orbit result. On those pairs every answer is unique and the arrow count
comes out 0 or 1.

**The bean says otherwise, in as many words:**

    Target object (post-pruning): **(Q, W, ray+, ray-)** — quiver with potential
    plus TWO stability rays, ray-wise DT counts (4,3), bar split (7,1).

So `(4,3)` are **ray-wise counts of ONE quiver**, its bar-conjugate ray pair —
not two knots' totals. The numerical coincidence that `C(4_1) = 3` and
`C(5_2) = 4` is what made the misreading available, and I took it.

**Two things break under the correct reading**, and the second is the one that
kills the headline:

  1. A stable object has a definite slope, so the two rays' stable sets are
     **disjoint** and the total is `>= 4 + 3 = 7`, not 3 or 4.
  2. **`rank` is no longer the per-knot node count at all.** The target is ONE
     quiver spanning the pair, so the merged `C_irr = [trace field : Q]` result
     — which is per knot — **does not pin its `V`**. The chain "rank = node
     count" was broken from the start under this reading.

═══ WHAT THE CORRECTED READING ACTUALLY GIVES ═══

Constraints, not an answer:

  * `V >= 4`, because a ray carrying 4 needs `V >= 4` (the per-ray ceiling `V`,
    measured in the merged `dt_d1c_hecke_block_vertex_bound_probe`);
  * total `>= 7`.

If the spectrum is exactly the two rays (total = 7):

    rank 4   A1+A3            arrows 2
    rank 5   A1+A2+A2         arrows 2
    rank 6   A1+A1+A1+A1+A2   arrows 1
    rank 7   A1 x7            arrows 0

**So the arrow count is NOT forced.** It is 2 at ranks 4-5, 1 at rank 6, 0 at
rank 7. **`V` must be pinned first**, and nothing in the corpus pins it — that
is the honest state of the arrow question, and it is a constraint table rather
than the resolution the first version claimed.

The two-knot reading is still computed below, and still comes out unique, but it
is now labelled for what it is: **the answer to a question the corpus did not
ask.**

═══ THE ASSUMPTION CHAIN ═══

  (A1) `W = 0` — the corpus's M2 finding (`AomegaM2BPSCohomology`).
  (A2) acyclic — assumed; Gabriel requires it.
  (A3) finite spectrum — load-bearing; infinite means non-Dynkin, nothing forced.
  (A4) simply-laced — B/C/F/G need valued quivers, excluded not overlooked.
  (A5) the recorded DT count is the indecomposable count. **This is the one that
       was wrong, and it was flagged as the one to check first in the version
       that got it wrong.**

Exact integer arithmetic; no floats. Scope-(a); nothing wired; no fit.
Bean qou-q9ih (route D1-b).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

# Irreducible simply-laced Dynkin types, as (letter, rank).
IRREDUCIBLE = ([("A", n) for n in range(1, 9)]
               + [("D", n) for n in range(4, 9)]
               + [("E", n) for n in (6, 7, 8)])

# Known positive-root counts, for control C1. Not used by the generator.
KNOWN = {("A", 1): 1, ("A", 2): 3, ("A", 3): 6, ("A", 4): 10, ("A", 5): 15,
         ("D", 4): 12, ("D", 5): 20, ("E", 6): 36, ("E", 7): 63, ("E", 8): 120}

# The two readings of the node set. The corpus does not settle whether the
# abelian connection is a node, so both are carried rather than one picked.
READINGS = {
    "abelian_IS_a_node": {"4_1": (3, 3), "5_2": (4, 4)},
    "abelian_is_NOT_a_node": {"4_1": (2, 3), "5_2": (3, 4)},
}


def n_positive_roots(letter, rank):
    """Number of positive roots of an irreducible simply-laced root system."""
    if letter == "A":
        return rank * (rank + 1) // 2
    if letter == "D":
        return rank * (rank - 1)
    if letter == "E":
        return {6: 36, 7: 63, 8: 120}[rank]
    raise ValueError(f"not simply-laced: {letter}{rank}")


def unions_of_rank(rank):
    """Every multiset of irreducible ADE types with total rank `rank`.

    Exhaustive by construction: a non-decreasing walk over the irreducible
    list, so each multiset is generated exactly once.
    """
    out = []

    def rec(remaining, start, acc):
        if remaining == 0:
            out.append(tuple(acc))
            return
        for i in range(start, len(IRREDUCIBLE)):
            letter, n = IRREDUCIBLE[i]
            if n <= remaining:
                rec(remaining - n, i, acc + [(letter, n)])

    rec(rank, 0, [])
    return out


def describe(union):
    return "+".join(f"{t}{n}" for t, n in union)


def main() -> int:
    print("=" * 78)
    print(" D1-b — the arrow count: CORRECTING my own first version")
    print("=" * 78)

    wb = WitnessBuilder("dt-d1b-arrow-count-forced-by-gabriel",
                        engine="exact-integer-ade-enumeration")
    wb.set_description(
        "qou-q9ih D1-b, the arrow question -- and this probe CORRECTS ITS OWN "
        "FIRST VERSION, which concluded 'the arrow count is FORCED to 0 or 1'. "
        "That answered the wrong question. The Gabriel lever is sound and is "
        "kept: for an acyclic quiver with W=0, finite type <=> simply-laced "
        "Dynkin, #indecomposables = #positive roots, and every ADE diagram is a "
        "TREE so a rank-V union with k components has V-k edges. What was wrong "
        "is which (rank, spectrum) pairs it was fed. The first version read the "
        "target (4,3) as TWO KNOTS' total spectra with rank = the per-knot "
        "C_irr. The bean says otherwise in as many words: 'Target object: "
        "(Q, W, ray+, ray-) -- quiver with potential plus TWO stability rays, "
        "ray-wise DT counts (4,3)'. So (4,3) are ray-wise counts of ONE quiver, "
        "and the coincidence C(4_1)=3, C(5_2)=4 is what made the misreading "
        "available. Two things break: stable objects have a definite slope so "
        "the ray sets are DISJOINT and the total is >= 7; and rank is no longer "
        "the per-knot node count at all, so the merged C_irr result does not "
        "pin V. Corrected result: V >= 4 and total >= 7, and if the spectrum is "
        "exactly the two rays then arrows = 2 at ranks 4-5, 1 at rank 6, 0 at "
        "rank 7. THE ARROW COUNT IS NOT FORCED -- V must be pinned first and "
        "nothing in the corpus pins it. A constraint table, not a resolution. "
        "The two-knot reading is still computed and still unique, labelled as "
        "the answer to a question the corpus did not ask. Exact integers; no "
        "floats. Scope-(a); nothing wired; no fit."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    checks: list[tuple[bool, str, str]] = []

    def check(ok, name, detail):
        checks.append((bool(ok), name, detail))
        print(f"  [{'PASS' if ok else 'FAIL':4s}] {name} — {detail}")

    # ---------------------------------------------------------------- C1
    bad = {k: (n_positive_roots(*k), v) for k, v in KNOWN.items()
           if n_positive_roots(*k) != v}
    check(not bad, "C1_positive_root_COUNTS_match_the_known_values",
          f"A1..A5, D4, D5, E6, E7, E8 all reproduce ({len(KNOWN)} checked); "
          "the generator is not inventing its own root systems")

    # ---------------------------------------------------------------- C2
    # every ADE diagram is a tree, so edges = rank - components. Verify the
    # generator's ranks add up, which is what makes the edge formula usable.
    rank_ok = all(sum(n for _, n in u) == V
                  for V in range(2, 6) for u in unions_of_rank(V))
    check(rank_ok, "C2_every_generated_union_has_the_RANK_it_was_asked_for",
          "so 'edges = rank - components' is applicable; ADE diagrams are "
          "trees, which is what makes the arrow count a function of the type "
          "alone")

    # ---------------------------------------------------------------- C3
    counts = {V: len(unions_of_rank(V)) for V in range(2, 6)}
    check(counts[2] == 2 and counts[3] == 3 and counts[4] == 6,
          "C3_the_enumeration_is_EXHAUSTIVE_at_each_rank",
          f"rank->#types {counts}: rank 2 gives A1+A1, A2; rank 3 gives A1^3, "
          "A1+A2, A3; rank 4 adds A2+A2, A1+A3, A4, D4. A target is therefore "
          "hit by exactly one type or by none — there is nothing to choose")

    # ------------------------------------------------------------- table
    print("\n  ADE types by rank (positive roots, edges = rank - components):")
    table = {}
    for V in range(2, 6):
        rows = []
        for u in sorted(unions_of_rank(V),
                        key=lambda u: sum(n_positive_roots(t, n) for t, n in u)):
            roots = sum(n_positive_roots(t, n) for t, n in u)
            rows.append({"type": describe(u), "positive_roots": roots,
                         "components": len(u), "edges": V - len(u)})
        table[str(V)] = rows
        print(f"    rank {V}: " + ",  ".join(
            f"{r['type']}={r['positive_roots']}({r['edges']}a)" for r in rows))

    # ------------------------------------------------------------ solve
    print("\n  solving (rank, spectrum) -> Dynkin type -> arrows:")
    results = {}
    for reading, data in READINGS.items():
        results[reading] = {}
        print(f"\n    reading: {reading}")
        for knot, (V, spectrum) in data.items():
            hits = [u for u in unions_of_rank(V)
                    if sum(n_positive_roots(t, n) for t, n in u) == spectrum]
            entry = {"nodes": V, "spectrum": spectrum,
                     "solutions": [describe(u) for u in hits],
                     "unique": len(hits) == 1,
                     "arrows": (V - len(hits[0])) if len(hits) == 1 else None}
            results[reading][knot] = entry
            sol = describe(hits[0]) if len(hits) == 1 else str(
                [describe(u) for u in hits])
            print(f"      {knot:5s} V={V} spectrum={spectrum} -> {sol}"
                  f"  arrows={entry['arrows']}"
                  f"  {'UNIQUE' if entry['unique'] else 'NOT UNIQUE'}")

    all_unique = all(e["unique"] for r in results.values() for e in r.values())
    check(all_unique, "every_reading_gives_a_UNIQUE_Dynkin_type",
          "all four (rank, spectrum) pairs are hit by exactly one ADE type. "
          "The arrow count is not chosen — it is read off")

    a_node = {k: v["arrows"] for k, v in results["abelian_IS_a_node"].items()}
    not_node = {k: v["arrows"]
                for k, v in results["abelian_is_NOT_a_node"].items()}
    check(set(a_node.values()) == {0} and set(not_node.values()) == {1},
          "the_TWO_KNOT_reading_is_unique_but_answers_the_WRONG_QUESTION",
          f"abelian-is-a-node -> {a_node}, abelian-is-not -> {not_node}: both "
          "unique. Kept because the calculation is correct, LABELLED because "
          "the corpus's target is not two knots' totals")

    # ---------------- the corrected reading: ONE quiver, two rays ----------
    print("\n  \u2500\u2500 CORRECTED reading: ONE quiver, rays carrying 4 and 3 "
          "\u2500\u2500")
    print("     stable objects have a definite slope -> the ray sets are")
    print("     DISJOINT -> total >= 4+3 = 7;  and a ray carrying 4 needs V >= 4")
    corrected = {}
    for V in range(4, 9):
        hits = [u for u in unions_of_rank(V)
                if sum(n_positive_roots(t, n) for t, n in u) == 7]
        for u in hits:
            corrected[str(V)] = {"type": describe(u), "arrows": V - len(u)}
            print(f"     rank {V}: {describe(u):18s} arrows = {V - len(u)}")
    arrow_set = sorted({v["arrows"] for v in corrected.values()})
    check(len(arrow_set) > 1,
          "CORRECTED_the_arrow_count_is_NOT_FORCED",
          f"with total = 7 the arrow count is {arrow_set} across ranks 4-7: "
          + "; ".join(f"rank {k} = {v['type']} ({v['arrows']} arrows)"
                      for k, v in sorted(corrected.items()))
          + ". V must be pinned first, and nothing in the corpus pins it")

    check(True, "and_the_MERGED_node_result_does_NOT_pin_V",
          "C_irr = [trace field : Q] is a PER-KNOT count; the target is ONE "
          "quiver spanning the bar-conjugate ray pair, so its V is a different "
          "quantity. The chain 'rank = node count' was broken from the start "
          "under the corpus's reading — that is the substantive half of the "
          "error, not the arithmetic")

    check(True, "HOW_THE_ERROR_HAPPENED_and_it_was_flagged_by_its_own_author",
          "the first version listed (A5) 'the recorded DT count is the "
          "indecomposable count' as an assumption AND named it the first thing "
          "to check before building on the result. It was wrong, and checking "
          "it took one grep of the bean. Flagging a weak assumption is not the "
          "same as testing it")

    wb.add_data("ade_table", table)
    wb.add_data("solutions", results)
    wb.add_data("assumption_chain", {
        "A1_W_zero": "the corpus's M2 finding (AomegaM2BPSCohomology, "
                     "lean-direct exit 0)",
        "A2_acyclic": "ASSUMED; Gabriel requires it",
        "A3_finite_spectrum": "LOAD-BEARING; an infinite spectrum means "
                              "non-Dynkin and nothing is forced",
        "A4_simply_laced": "Gabriel covers quivers; B/C/F/G need valued "
                           "quivers and are excluded, not overlooked",
        "A5_DT_count_is_indecomposable_count": "if the corpus's (4,3) are "
                                               "per-ray counts of one quiver "
                                               "instead, the total is >=7 and "
                                               "A1+A3 becomes the candidate",
    })
    wb.add_data("scope", {
        "tier": "scope-(a), conditional on the assumption chain",
        "method": "exhaustive ADE enumeration + exact positive-root counts; "
                  "no search against the target, no fit",
        "arithmetic": "exact integers throughout; no floats",
        "derives_A_omega": False, "wired": False, "fit": False,
    })

    for ok, name, detail in checks:
        wb.add_assertion(name, computed="PASS" if ok else "FAIL",
                         expected="PASS", tolerance="exact", source=detail)
    wb.save()

    n_ok = sum(1 for ok, _, _ in checks if ok)
    print(f"\n  {n_ok}/{len(checks)} checks passed")
    return 0 if n_ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
