#!/usr/bin/env python3
"""Partition-shape classification probe — tests the user's
"ragged vs fully populated" hypothesis empirically.

For each n in magic and non-magic samples, classifies the
canonical (most-square-like) self-conjugate partition by:
  - Pure shape: square (k×k) or staircase ([k, k-1, ..., 1]) — the
    "fully populated" extremes.
  - Frobenius rank d: number of diagonal hooks.
  - Hook-completeness: whether the diagonal hook 1 is present
    (saturation at diagonal = cannot grow by 1 to a self-conj).
  - Raggedness index: r(λ) = sum of |λ_i - λ_{i+1}| (total drop
    across consecutive rows).
  - Aspect: width / height of bounding rectangle.

Tests the hypothesis: magic n's canonical avoids pure-shape
extremes (squares + staircases) and has bounded raggedness.

Usage:
    python3 partition_shape_classification.py
"""

import sys
import json
from typing import Dict, List, Optional, Tuple

sys.path.insert(0, ".")
from enumerate_self_conjugate_partitions import (  # noqa: E402
    canonical_self_conjugate,
    conjugate_partition,
)


def is_pure_square(partition: List[int]) -> Tuple[bool, int]:
    """k×k square iff all rows have length k AND there are k rows."""
    if not partition:
        return False, 0
    k = partition[0]
    if len(partition) != k:
        return False, 0
    for r in partition:
        if r != k:
            return False, 0
    return True, k


def is_pure_staircase(partition: List[int]) -> Tuple[bool, int]:
    """Pure staircase: [k, k-1, ..., 1] for k = number of rows."""
    if not partition:
        return False, 0
    k = len(partition)
    expected = list(range(k, 0, -1))
    return partition == expected, k


def frobenius_rank(partition: List[int]) -> int:
    """Number of diagonal hooks d = #{i : λ_i ≥ i}, 1-indexed."""
    return sum(1 for i, r in enumerate(partition, start=1) if r >= i)


def diagonal_hook_lengths(partition: List[int]) -> List[int]:
    """Hook lengths along the main diagonal of a self-conjugate λ.
    For (i, i) cell: h(i, i) = (λ_i - i) + (λ'_i - i) + 1.
    For self-conj, λ' = λ so h = 2(λ_i - i) + 1 = 2 a_i + 1."""
    conj = conjugate_partition(partition)
    out = []
    d = frobenius_rank(partition)
    for i in range(1, d + 1):
        h = (partition[i - 1] - i) + (conj[i - 1] - i) + 1
        out.append(h)
    return out


def has_hook_one(partition: List[int]) -> bool:
    return 1 in diagonal_hook_lengths(partition)


def raggedness_index(partition: List[int]) -> int:
    """r(λ) = sum_i |λ_i - λ_{i+1}|. Pure square = 0, pure staircase = k."""
    if len(partition) < 2:
        return 0
    return sum(
        abs(partition[i] - partition[i + 1]) for i in range(len(partition) - 1)
    )


def classify(n: int) -> Dict:
    """Run the full classification on n's canonical self-conj partition."""
    canonical, count = canonical_self_conjugate(n)
    if not canonical:
        return {
            "n": n,
            "canonical": None,
            "self_conj_count": 0,
            "shape_classification": "DEGENERATE (no self-conj)",
        }
    is_sq, sq_k = is_pure_square(canonical)
    is_st, st_k = is_pure_staircase(canonical)
    d = frobenius_rank(canonical)
    hooks = diagonal_hook_lengths(canonical)
    return {
        "n": n,
        "canonical": canonical,
        "self_conj_count": count,
        "is_pure_square": is_sq,
        "square_k": sq_k if is_sq else None,
        "is_pure_staircase": is_st,
        "staircase_k": st_k if is_st else None,
        "frobenius_rank_d": d,
        "diagonal_hooks": hooks,
        "has_hook_one": has_hook_one(canonical),
        "raggedness_index": raggedness_index(canonical),
        "first_row": canonical[0],
        "n_rows": len(canonical),
        "aspect_ratio": canonical[0] / len(canonical) if canonical else None,
    }


MAGIC = [2, 8, 20, 28, 50, 82, 126]
NONMAGIC_PROBE = [1, 3, 4, 5, 6, 7, 9, 10, 12, 14, 15, 16, 18, 21, 24, 25, 27,
                   30, 36, 40, 45, 49, 64, 81, 100, 120, 121]
HIGHER_MAGIC_CANDIDATES = [184]  # Next theoretical superheavy magic


def main(argv: List[str]) -> int:
    targets = sorted(set(MAGIC + NONMAGIC_PROBE + HIGHER_MAGIC_CANDIDATES))

    rows = []
    for n in targets:
        r = classify(n)
        r["empirical_magic"] = n in MAGIC
        rows.append(r)

    # Print classification table.
    print(f"{'n':>4} {'magic?':>7} {'#SC':>5} {'shape':>14}"
          f" {'d':>3} {'hook1?':>7} {'rag':>4} {'first':>5} {'rows':>4}")
    print("-" * 80)
    for r in rows:
        if r["self_conj_count"] == 0:
            print(f"{r['n']:>4} {'★' if r['empirical_magic'] else ' ':>7}"
                  f" {0:>5} {'DEGENERATE':>14}")
            continue
        if r["is_pure_square"]:
            shape = f"square {r['square_k']}×{r['square_k']}"
        elif r["is_pure_staircase"]:
            shape = f"staircase k={r['staircase_k']}"
        else:
            shape = "ragged"
        print(
            f"{r['n']:>4} {'★' if r['empirical_magic'] else ' ':>7}"
            f" {r['self_conj_count']:>5} {shape:>14}"
            f" {r['frobenius_rank_d']:>3}"
            f" {'yes' if r['has_hook_one'] else 'no':>7}"
            f" {r['raggedness_index']:>4}"
            f" {r['first_row']:>5} {r['n_rows']:>4}"
        )

    # Hypothesis check: magic n avoids pure shapes
    print()
    magic_pure_sq = [r["n"] for r in rows
                      if r["empirical_magic"] and r.get("is_pure_square")]
    magic_pure_st = [r["n"] for r in rows
                      if r["empirical_magic"] and r.get("is_pure_staircase")]
    nonmagic_pure_sq = [r["n"] for r in rows
                         if not r["empirical_magic"] and r.get("is_pure_square")]
    nonmagic_pure_st = [r["n"] for r in rows
                         if not r["empirical_magic"] and r.get("is_pure_staircase")]

    print("Pure-shape hypothesis check:")
    print(f"  Magic with pure square canonical: {magic_pure_sq}")
    print(f"  Magic with pure staircase canonical: {magic_pure_st}")
    print(f"  Non-magic with pure square: {nonmagic_pure_sq}")
    print(f"  Non-magic with pure staircase: {nonmagic_pure_st}")
    print()

    # Hook-1-present hypothesis
    magic_hook1 = [r["n"] for r in rows
                    if r["empirical_magic"] and r.get("has_hook_one")]
    magic_no_hook1 = [r["n"] for r in rows
                       if r["empirical_magic"] and r.get("has_hook_one") is False
                       and r["self_conj_count"] > 0]
    print("Hook-1 hypothesis:")
    print(f"  Magic WITH hook 1 in canonical: {magic_hook1}")
    print(f"  Magic WITHOUT hook 1 in canonical: {magic_no_hook1}")
    print()

    # Higher-magic candidate
    print("Higher-magic candidate (n = 184, conjectural superheavy):")
    for r in rows:
        if r["n"] in HIGHER_MAGIC_CANDIDATES:
            print(
                f"  n={r['n']}: #SC={r['self_conj_count']},"
                f" canonical first row={r.get('first_row')},"
                f" Frobenius rank={r.get('frobenius_rank_d')},"
                f" hook 1 present? {r.get('has_hook_one')}"
            )

    # Save full report
    with open("partition_shape_classification_report.json", "w") as f:
        json.dump(rows, f, indent=2)
    print("\nFull report saved to partition_shape_classification_report.json")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
