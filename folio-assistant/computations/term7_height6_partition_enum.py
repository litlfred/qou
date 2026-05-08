"""term7_height6_partition_enum.py

First numerical attempt at Term 7's α_5 from the structural side.

Per `conj:shell-correction-term-seven`, the shell-correction
projector is

  χ_5(T_w) := Σ_{λ ⊢ 3A,  ht(λ) = 6}  w_λ(q) · χ^λ(T_w)

with Wedderburn weights w_λ = dim_q(λ)² / [3A]_q!.  Term 7 = α_5 ·
χ_5, with α_5 < 0 (binding-enhancing) per the Mayer shell-closure
argument.

This script:
  1. Enumerates partitions λ ⊢ n of height 6 (number of parts) for
     n in {6, 9, 12, 15, 18}, corresponding to A ∈ {2, 3, 4, 5, 6}
     in the level-1 H_{3A}(q) framework.
  2. For each partition, computes the q-dimension dim_q(λ) via the
     hook-length formula at q = q_0 ≈ 1.10998.
  3. Reports the Wedderburn-weighted partition count |{λ : ht=6}|
     and the largest dim_q(λ)² contribution, giving a first
     numerical handle on the χ_5 magnitude.

This does NOT yet compute the full χ^λ(T_w) Hecke characters at
specific atomic-knot operators — that requires the
gb_filtration_jet_tracker output (extended in this PR for 4_1, 6_2,
8_11) plus Hoefsmit seminormal forms.  It does provide the
*partition basis* on which α_5 will be fit.
"""

# Ref: [manuscript] conj:shell-correction-term-seven
# Ref: [mayer1949] DOI 10.1103/PhysRev.75.1969

import json
from math import factorial
from pathlib import Path

import mpmath
from mpmath import mp, mpf


def partitions_of_height(n: int, height: int) -> list[tuple[int, ...]]:
    """All partitions of n with exactly `height` non-zero parts."""
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


def hook_length(lam: tuple[int, ...], i: int, j: int) -> int:
    """Hook length of cell (i, j) in partition lam (1-indexed)."""
    arm = lam[i - 1] - j
    # leg: rows below row i where column j is still in the diagram
    leg = sum(1 for r in range(i, len(lam)) if lam[r] >= j)
    return arm + leg + 1


def dim_q_of_partition(lam: tuple[int, ...], n: int, q_val: mpf) -> mpf:
    """q-dimension via hook-length:
       dim_q(λ) = [n]_q! / ∏_{x ∈ λ} [h_x]_q.
    """
    # [k]_q := (q^k - q^{-k}) / (q - q^{-1})  for symmetric form
    # We use the unsymmetric quantum integer (q^k - 1)/(q - 1)
    # which gives the same hook-length formula at q != 1.
    def q_int(k: int) -> mpf:
        if k == 0:
            return mpf(0)
        return (q_val ** k - 1) / (q_val - 1)

    def q_factorial(k: int) -> mpf:
        out = mpf(1)
        for i in range(1, k + 1):
            out *= q_int(i)
        return out

    numerator = q_factorial(n)
    denom = mpf(1)
    for i, row_len in enumerate(lam, start=1):
        for j in range(1, row_len + 1):
            h = hook_length(lam, i, j)
            denom *= q_int(h)
    return numerator / denom


def main() -> None:
    mp.dps = 60
    q_0 = mpf("1.1099785955541805")  # high-precision substrate parameter

    A_values = [2, 3, 4, 5, 6]
    height = 6

    results = []
    for A in A_values:
        n = 3 * A
        parts = partitions_of_height(n, height)
        # Compute dim_q for each, then Wedderburn weight ∝ dim_q²
        weights = []
        for lam in parts:
            d = dim_q_of_partition(lam, n, q_0)
            weights.append((lam, d, d * d))
        weights.sort(key=lambda t: -float(t[2]))  # descending by dim_q²

        results.append({
            "A": A,
            "n_strands": n,
            "n_partitions_height_6": len(parts),
            "top_5_partitions_by_weight": [
                {
                    "partition": list(lam),
                    "dim_q": str(d)[:40],
                    "dim_q_sq": str(dsq)[:40],
                }
                for lam, d, dsq in weights[:5]
            ],
            "total_weight_sum": str(
                sum(t[2] for t in weights)
            )[:40],
        })

    payload = {
        "computation": "term7-height6-partition-enum",
        "description": (
            "First numerical handle on Term 7 (conj:shell-correction-"
            "term-seven): enumerates height-6 partitions of 3A for "
            "A ∈ {2..6} and computes Wedderburn weights at q_0. "
            "Provides the partition basis on which α_5 will be fit "
            "once the gb_filtration_jet_tracker extension supplies "
            "the χ^λ(T_w) characters for the atomic knots."
        ),
        "contentBlock": "conj:shell-correction-term-seven",
        "precision_dps": 60,
        "q_0": str(q_0),
        "height": height,
        "A_values": A_values,
        "results": results,
        "interpretation": (
            "Height-6 partitions exist for A ≥ 2 (3A ≥ 6); count "
            "grows polynomially. The Wedderburn-weighted top-5 list "
            "per A identifies the dominant contributors to χ_5. "
            "Combined with the χ^λ(T_w) data for atomic knots, "
            "α_5 can be fit from the AME residual."
        ),
    }

    out_path = (
        Path(__file__).parent / "term7-height6-partition-enum.witness.json"
    )
    with out_path.open("w") as f:
        json.dump(payload, f, indent=2)

    print(f"Height-6 partition counts by A:")
    for r in results:
        print(f"  A={r['A']} (n={r['n_strands']}): "
              f"{r['n_partitions_height_6']} partitions")
    print(f"\nWritten to {out_path.name}")


if __name__ == "__main__":
    main()
