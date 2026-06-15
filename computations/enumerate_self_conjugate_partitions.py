#!/usr/bin/env python3
"""Enumerate self-conjugate Young partitions of given n via the
Frobenius bijection (distinct odd parts -> self-conjugate partition).

For each magic n in {2, 8, 20, 28, 50, 82, 126}, lists every
self-conjugate partition lambda |- n, verifies sum c(x) = 0 and
lambda = lambda', and picks a canonical "dominant" representative
(here: the one with the smallest first-row length, i.e., the most
"square-like" shape).

Used to fill in row-vector predictions in
folio-assistant/computations/double-magic-witnesses.json.

Usage:
    python3 enumerate_self_conjugate_partitions.py [n ...]

If no n is supplied, prints the magic ladder.
"""

import json
import sys
from typing import List, Tuple


def distinct_odd_partitions(n: int) -> List[List[int]]:
    """All partitions of n into distinct odd positive integers,
    each represented in decreasing order."""
    out: List[List[int]] = []

    def go(remaining: int, max_part: int, current: List[int]) -> None:
        if remaining == 0:
            out.append(list(current))
            return
        # Try each odd k from min(max_part, remaining) down to 1.
        start = min(max_part, remaining)
        if start % 2 == 0:
            start -= 1
        for k in range(start, 0, -2):
            if k <= remaining:
                current.append(k)
                go(remaining - k, k - 2, current)
                current.pop()

    go(n, n, [])
    return out


def partition_from_frobenius_arms(arms: List[int]) -> List[int]:
    """Given arms = [a_1 > a_2 > ... > a_d >= 0], build the
    self-conjugate partition with Frobenius coordinates (a_i, a_i).

    Returns row lengths in decreasing order.
    """
    if not arms:
        return []
    # Construct cell set.
    cells = set()
    for idx, a in enumerate(arms):
        j = idx + 1  # 1-indexed diagonal column
        # Diagonal cell
        cells.add((j, j))
        # Arm cells along row j
        for k in range(1, a + 1):
            cells.add((j, j + k))
        # Leg cells along column j
        for k in range(1, a + 1):
            cells.add((j + k, j))
    # Row lengths
    max_row = max(r for r, _ in cells)
    rows = [0] * max_row
    for r, _ in cells:
        rows[r - 1] += 1
    return rows


def conjugate_partition(rows: List[int]) -> List[int]:
    """Conjugate (transpose) of a Young diagram given by row lengths."""
    if not rows:
        return []
    max_col = rows[0]
    return [sum(1 for r in rows if r >= c) for c in range(1, max_col + 1)]


def content_sum(rows: List[int]) -> int:
    """Sum of Jucys-Murphy contents c(x) = j - i over cells of the
    Young diagram with given row lengths."""
    s = 0
    for i, length in enumerate(rows, start=1):
        for j in range(1, length + 1):
            s += j - i
    return s


def all_self_conjugate_partitions(n: int) -> List[List[int]]:
    """All self-conjugate partitions of n."""
    out = []
    for odd_parts in distinct_odd_partitions(n):
        arms = [(p - 1) // 2 for p in odd_parts]
        partition = partition_from_frobenius_arms(arms)
        # Verification
        assert sum(partition) == n, f"size mismatch: {partition} sum != {n}"
        assert partition == conjugate_partition(
            partition
        ), f"not self-conjugate: {partition} != {conjugate_partition(partition)}"
        assert content_sum(partition) == 0, f"non-zero content sum on {partition}"
        out.append(partition)
    # Sort by (first-row length, lex) for canonicalization.
    out.sort(key=lambda r: (r[0] if r else 0, r))
    return out


def canonical_self_conjugate(n: int) -> Tuple[List[int], int]:
    """Pick a canonical "dominant" self-conjugate partition of n:
    the one with the smallest first-row length (most "square-like").

    Returns (row_vector, total_count_of_self_conjugates).
    """
    all_sc = all_self_conjugate_partitions(n)
    if not all_sc:
        return ([], 0)
    return (all_sc[0], len(all_sc))


def main(argv: List[str]) -> int:
    magic_ladder = [2, 8, 20, 28, 50, 82, 126]
    targets = [int(a) for a in argv[1:]] if len(argv) > 1 else magic_ladder

    report = {}
    for n in targets:
        all_sc = all_self_conjugate_partitions(n)
        canonical, count = canonical_self_conjugate(n)
        report[str(n)] = {
            "n": n,
            "self_conjugate_count": count,
            "canonical_dominant": canonical,
            "all_self_conjugate": all_sc,
        }
        print(f"n = {n}: {count} self-conjugate partition(s)")
        for p in all_sc:
            print(
                f"  {p}  (sum={sum(p)},"
                f" content_sum={content_sum(p)},"
                f" self_conj={p == conjugate_partition(p)})"
            )
        if not all_sc:
            print("  (no self-conjugate partition exists; iff is degenerate at this n)")
        print()

    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
