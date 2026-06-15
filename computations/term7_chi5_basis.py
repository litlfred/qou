"""term7_chi5_basis.py

Computes the **χ_5 partition-weight basis** at q_0 for A ∈ {2..6}
ahead of the full α_5 fit. Per `conj:shell-correction-term-seven`,

  χ_5(T_w) := Σ_{λ ⊢ 3A, ht(λ) = 6} w_λ(q) · χ^λ(T_w)

The Wedderburn weights w_λ = dim_q(λ)² / [n]_q! are numerically
computable from the partition basis without the canonical T_w
in H_{3A}(q). The χ^λ(T_w) factors require the GS-NF tracker
extension to H_n for n ≥ 4 (item 3 of the post-#579 close-batch).

This script reports:
  1. For each A ∈ {2..6}, the height-6 partitions of n = 3A.
  2. Their Wedderburn weights w_λ at q_0 (the *partition-side*
     of χ_5).
  3. The total weight Σ w_λ — an upper bound on |χ_5(T_w)|
     when |χ^λ(T_w)| ≤ 1 (which holds for sign / trivial reps
     at any specialisation of q).

The α_5 fit will combine this with the χ^λ(T_w) data once the
tracker extension lands.
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
# Ref: [manuscript] conj:shell-correction-term-seven
# Ref: [manuscript] term7_height6_partition_enum.py (basis)

import json
from q_parameter import Q_50_DIGIT_STR
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import mpmath
from mpmath import mp, mpf

from witness_base import WitnessBuilder  # noqa: E402
from partition_utils import hook_length_1based as hook_length  # noqa: E402


def partitions_of_height(n: int, height: int) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []

    def rec(remaining: int, max_part: int, parts: list[int]) -> None:
        if len(parts) == height:
            if remaining == 0:
                out.append(tuple(parts))
            return
        if remaining <= 0:
            return
        for p in range(min(remaining, max_part), 0, -1):
            if remaining - p >= (height - len(parts) - 1):
                rec(remaining - p, p, parts + [p])

    rec(n, n, [])
    return out


def q_int(k: int, q_val: mpf) -> mpf:
    if k == 0:
        return mpf(0)
    return (q_val ** k - 1) / (q_val - 1)


def q_factorial(k: int, q_val: mpf) -> mpf:
    out = mpf(1)
    for i in range(1, k + 1):
        out *= q_int(i, q_val)
    return out


def dim_q(lam: tuple[int, ...], n: int, q_val: mpf, n_fac_q: mpf) -> mpf:
    denom = mpf(1)
    for i, row_len in enumerate(lam, start=1):
        for j in range(1, row_len + 1):
            denom *= q_int(hook_length(lam, i, j), q_val)
    return n_fac_q / denom


def main() -> None:
    mp.dps = 60
    q_0 = mpf(Q_50_DIGIT_STR)
    A_values = [2, 3, 4, 5, 6]
    height = 6

    results = []
    for A in A_values:
        n = 3 * A
        parts = partitions_of_height(n, height)
        n_fac_q = q_factorial(n, q_0)

        partitions_data = []
        total_weight = mpf(0)
        for lam in parts:
            d = dim_q(lam, n, q_0, n_fac_q)
            w_lam = d * d / n_fac_q
            partitions_data.append({
                "partition": list(lam),
                "dim_q": mpmath.nstr(d, 30),
                "wedderburn_weight": mpmath.nstr(w_lam, 30),
            })
            total_weight += w_lam

        partitions_data.sort(
            key=lambda p: float(mpf(p["wedderburn_weight"])),
            reverse=True,
        )

        results.append({
            "A": A,
            "n_strands": n,
            "n_partitions_height_6": len(parts),
            "total_wedderburn_weight": mpmath.nstr(total_weight, 30),
            "top_5_partitions": partitions_data[:5],
        })

    payload = {
        "computation": "term7-chi5-basis",
        "description": (
            "Partition-side basis for χ_5(T_w) at q_0, for "
            "A ∈ {2..6}. Reports Wedderburn weights w_λ and the "
            "total Σ w_λ — an upper bound on |χ_5(T_w)| if "
            "|χ^λ(T_w)| ≤ 1. The α_5 fit awaits the χ^λ(T_w) "
            "values from the H_{3A} tracker extension."
        ),
        "contentBlock": "conj:shell-correction-term-seven",
        "precision_dps": 60,
        "q_0": str(q_0),
        "height": height,
        "A_values": A_values,
        "results": results,
        "open_dependency": (
            "α_5 fit requires χ^λ(T_w) for the canonical Hecke "
            "atomic-knot element T_w in H_{3A}(q) — depends on "
            "extending gb_filtration_jet_tracker.py to n ≥ 4. "
            "See gb_filtration_jet_tracker_extension_plan.md."
        ),
    }

    out = (
        WitnessBuilder.wrap_legacy(
            "term7-chi5-basis",
            payload,
            script_path=__file__,
            engine="mpmath",
        )
        .set_audit_only(
            "docs/audits/2026-05-09-refocused-1ppb-workplan-v3.md"
        )
        .save()
    )

    print("Term 7 χ_5 partition-weight basis:")
    for r in results:
        print(f"  A={r['A']} (n={r['n_strands']}): "
              f"{r['n_partitions_height_6']} partitions, "
              f"Σw_λ = {r['total_wedderburn_weight']}")
    print(f"\nWitness: {out}")


if __name__ == "__main__":
    main()
