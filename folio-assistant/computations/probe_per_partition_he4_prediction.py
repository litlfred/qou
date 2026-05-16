#!/usr/bin/env python3
# polynomial_q_not_applicable: combinatorial / closed-form prediction
# probe; no symbolic-q output.
"""Forward prediction: per-partition $k_\\lambda$ for $^4\\mathrm{He}$.

Extends the per-partition $k_\\lambda$ rule (per
`probe_phiq_per_partition_klambda.py`) to $^4\\mathrm{He}$
($A = 4$, $n = 12$). The empirical max-$|\\mu|$ selector matches the
{D, T, $^3$He} pattern but the partition-shape-only Hoefsmit
content-spread selector FAILS for all three (per
`probe_hoefsmit_content_selector.py`). Therefore: a purely
substrate-only forward prediction for $^4\\mathrm{He}$ requires
either (a) #638's per-eigenvalue probe run at $n = 12$, or (b) a
new substrate invariant that depends on the braid word.

This script makes **partition-shape-only candidate predictions**,
honestly flagging them as falsifiable forward predictions whose
correctness depends on whether the eventual $^4\\mathrm{He}$
empirical pattern follows the (failed-for-low-atoms) shape-only
selector.

**Candidate predictions for $^4\\mathrm{He}$ dominant partition:**

  P1 (content-spread argmax) — predicts a single-row [12] or
     single-column [1¹²] partition. Falsified for {D, T, ³He}.
  P2 (max-rectangular):  partition close to √n × √n shape.
  P3 (max-dim self-conjugate): partition λ with λ = λ^T and
     maximal dim V_λ. (Type-B fold-fixed branch from the earlier
     fold-depth probe.)
  P4 (medium-aspect-ratio with high content spread): partitions
     like (k, k, 1, 1, ...) following the [2,2,1,1] / [6,3] /
     [5,4] empirical pattern shape. (Pattern-matched from the
     low-atom empirical dominants.)

**Class C (diagnostic / prediction probe).**

Output: `probe-per-partition-he4-prediction.witness.json`.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterator

import mpmath as mp

mp.mp.dps = 50

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from partition_utils import hook_length  # noqa: E402


def partitions(n: int, max_part: int | None = None) -> Iterator[tuple[int, ...]]:
    if n == 0:
        yield ()
        return
    if max_part is None:
        max_part = n
    for first in range(min(n, max_part), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def cells(lam: tuple[int, ...]) -> Iterator[tuple[int, int]]:
    for i, length in enumerate(lam):
        for j in range(length):
            yield (i, j)


def conjugate(lam: tuple[int, ...]) -> tuple[int, ...]:
    if not lam:
        return ()
    width = lam[0]
    return tuple(
        sum(1 for part in lam if part >= i) for i in range(1, width + 1)
    )


def content_spread(lam: tuple[int, ...]) -> int:
    contents = [j - i for (i, j) in cells(lam)]
    return max(contents) - min(contents)


def dim_partition(lam: tuple[int, ...]) -> int:
    """Dimension of S_n irrep at partition lam (hook-length formula)."""
    from math import factorial
    n = sum(lam)
    hook_prod = 1
    for (i, j) in cells(lam):
        hook_prod *= hook_length(lam, i, j)
    return factorial(n) // hook_prod


def aspect_ratio(lam: tuple[int, ...]) -> float:
    """Width-to-height aspect: lam[0] / len(lam)."""
    return lam[0] / len(lam)


# ── Empirical dominants from PR #639 (the low-atom comparison set) ─
EMPIRICAL_LOW_ATOM = {
    "D":   (2, 2, 1, 1),
    "T":   (6, 3),
    "He3": (5, 4),
}

# Empirical aspect ratios:
#   D dominant [2,2,1,1]: aspect = 2/4 = 0.5
#   T dominant [6,3]:     aspect = 6/2 = 3.0
#   ³He dominant [5,4]:   aspect = 5/2 = 2.5


def main() -> int:
    w = WitnessBuilder("probe-per-partition-he4-prediction",
                       engine="python")

    print("=" * 78)
    print("⁴He PER-PARTITION k_λ FORWARD PREDICTION (A = 4, n = 12)")
    print("=" * 78)
    print()

    # Empirical baseline
    print("  Empirical dominants (low-atom comparison from PR #639):")
    for atom, lam in EMPIRICAL_LOW_ATOM.items():
        print(f"    {atom:>5}: λ = {str(list(lam)):<14} "
              f"dim = {dim_partition(lam):>3}  spread = {content_spread(lam)}  "
              f"aspect = {aspect_ratio(lam):.2f}")
    print()

    n = 12
    all_parts = list(partitions(n))
    print(f"  Total partitions of n = {n}: {len(all_parts)}")
    print()

    # P1: argmax content spread
    parts_by_spread = sorted(all_parts, key=lambda p: -content_spread(p))
    max_spread = content_spread(parts_by_spread[0])
    p1_candidates = [p for p in all_parts if content_spread(p) == max_spread]

    # P2: max-rectangular (closest to √n × √n)
    # For n=12: best rectangles are (4,4) of n=8 — but n=12 has (4,3) of 7,
    # (3,3,3) → n=9, (4,4,4) → n=12, (3,3,3,3) → n=12.
    rectangular = []
    for lam in all_parts:
        # Aspect ratio close to 1 (square-ish)
        if len(set(lam)) == 1:  # all parts equal
            rectangular.append((lam, abs(aspect_ratio(lam) - 1.0)))
    rectangular.sort(key=lambda x: x[1])
    p2_candidates = [r[0] for r in rectangular[:5]]

    # P3: self-conjugate with max dim
    self_conj = [p for p in all_parts if conjugate(p) == p]
    self_conj.sort(key=lambda p: -dim_partition(p))
    p3_candidates = self_conj[:5]

    # P4: pattern-matched from low-atom dominants. The empirical
    # pattern is: 2-row partition with substantial width-to-height
    # ratio (T: [6,3] aspect 3.0; ³He: [5,4] aspect 2.5; D: [2,2,1,1]
    # is 2-col, not 2-row, but compact). For n=12, scale up the
    # pattern: aspect ≈ 2.5–3.0 with 2-3 rows.
    p4_candidates = []
    for lam in all_parts:
        if 2 <= len(lam) <= 3 and 2.0 <= aspect_ratio(lam) <= 3.5:
            p4_candidates.append((lam, dim_partition(lam)))
    p4_candidates.sort(key=lambda x: -x[1])
    p4_candidates = [p for p, _ in p4_candidates[:5]]

    print("  P1 — content-spread argmax (Hoefsmit-shape; FALSIFIED at low atoms):")
    for p in p1_candidates[:5]:
        print(f"    λ = {str(list(p)):<22}  dim = {dim_partition(p):>4}  "
              f"spread = {content_spread(p)}  aspect = {aspect_ratio(p):.2f}")
    print()
    print("  P2 — rectangular (square-ish aspect):")
    for p in p2_candidates:
        print(f"    λ = {str(list(p)):<22}  dim = {dim_partition(p):>4}  "
              f"spread = {content_spread(p)}  aspect = {aspect_ratio(p):.2f}")
    print()
    print("  P3 — self-conjugate, max-dim (Type-B fold-fixed branch):")
    for p in p3_candidates:
        print(f"    λ = {str(list(p)):<22}  dim = {dim_partition(p):>4}  "
              f"spread = {content_spread(p)}  aspect = {aspect_ratio(p):.2f}")
    print()
    print("  P4 — pattern-matched (aspect 2.0–3.5, 2–3 rows):")
    for p in p4_candidates:
        print(f"    λ = {str(list(p)):<22}  dim = {dim_partition(p):>4}  "
              f"spread = {content_spread(p)}  aspect = {aspect_ratio(p):.2f}")
    print()

    # Falsifiability flag
    print("  ─────────────────────────────────────────────────────────────")
    print("  Falsifiability: when #638's per-eigenvalue probe is run at")
    print("  n = 12 with the ⁴He braid word, the empirical dominant")
    print("  partition will fall into AT MOST ONE of the four candidate")
    print("  lists above (or none, in which case all four shape-only")
    print("  predictors are refuted at A = 4).")
    print()
    print("  Confidence ranking (per low-atom empirical pattern):")
    print("    P4 (pattern-match) > P3 (Type-B fold-fixed) > P2 > P1 (refuted)")

    w.set_content_block("rem:per-partition-k-lambda-rule")
    w.set_description(
        "Forward prediction of the ⁴He (A=4, n=12) dominant partition "
        "under four substrate-only shape-based selector candidates. "
        "Tests P1 (content-spread argmax — already refuted at A=2,3), "
        "P2 (rectangular), P3 (self-conjugate max-dim), P4 (pattern-"
        "match from low-atom empirical aspect ratio 2.0–3.5). When "
        "#638's per-eigenvalue probe is run at n=12, the empirical "
        "result will refute or confirm each candidate. Class C "
        "(diagnostic / forward prediction)."
    )
    w.add_parameter("atoms_tested", ["He4"])
    w.add_parameter("n_partitions_of_12", len(all_parts))
    w.add_parameter("empirical_low_atom_dominants",
        {k: list(v) for k, v in EMPIRICAL_LOW_ATOM.items()})
    w.add_data("p1_content_spread_argmax",
        [list(p) for p in p1_candidates[:5]])
    w.add_data("p2_rectangular_aspect_1",
        [list(p) for p in p2_candidates])
    w.add_data("p3_self_conjugate_max_dim",
        [list(p) for p in p3_candidates])
    w.add_data("p4_pattern_match_aspect_2_to_3p5",
        [list(p) for p in p4_candidates])
    w.add_data("p4_top_candidate", list(p4_candidates[0]) if p4_candidates else None)
    w.add_data("confidence_ranking", (
        "P4 (pattern-match from low-atom empirical dominants) > "
        "P3 (self-conjugate, Type-B fold-fixed) > "
        "P2 (rectangular aspect 1) > "
        "P1 (content-spread argmax — REFUTED at A=2,3 per "
        "probe_hoefsmit_content_selector.py)"
    ))
    w.add_data("falsifiability_notes", (
        "When #638's per-eigenvalue probe is run for ⁴He at n=12, "
        "compare the empirical dominant against the four candidate "
        "lists. At most one will match; if none match, all four "
        "shape-only selectors are refuted, confirming the per-"
        "partition rule requires a braid-word-aware substrate "
        "invariant (consistent with the negative finding of the "
        "Hoefsmit content-spread test)."
    ))

    # Forward-prediction assertions
    w.add_assertion(
        "n12_partitions_count_matches_partition_function_p12",
        computed=len(all_parts),
        expected=77,  # p(12) = 77 (OEIS A000041)
    )
    w.add_assertion(
        "p4_top_candidate_aspect_in_2_to_3p5_range",
        computed=(2.0 <= aspect_ratio(p4_candidates[0]) <= 3.5
                  if p4_candidates else False),
        expected=True,
    )
    w.add_assertion(
        "p1_content_spread_includes_single_row_partition",
        computed=(12,) in p1_candidates,
        expected=True,
    )

    out = w.save()
    print(f"\n  Wrote {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
