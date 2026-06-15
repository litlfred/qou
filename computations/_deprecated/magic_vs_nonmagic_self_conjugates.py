#!/usr/bin/env python3
"""Compare self-conjugate-partition statistics between magic and
non-magic n, looking for structural patterns that might distinguish
the magic ladder.

Pattern probes implemented:
  - q(n) = number of self-conjugate partitions
  - max_durfee = max # distinct odd parts in any decomposition
  - hook_length_set = union of hook-length sets across decompositions
  - max_hook = largest part appearing in any decomposition
  - has_staircase = whether n is triangular (staircase [k, k-1, ..., 1])
  - has_perfect_square = whether n = k^2 (k×k square self-conjugate)
  - parts_count_signature = (count_2parts, count_4parts, count_6parts, ...)
  - canonical = most-square-like (smallest first row) self-conjugate
  - extremal_widest = largest first row across self-conjugates
  - extremal_tallest = largest number of rows across self-conjugates
  - aspect_range = max(rows) / min(rows) of canonical etc.

Run as:
    python3 magic_vs_nonmagic_self_conjugates.py
"""

import json
import sys
from typing import List, Tuple

sys.path.insert(0, ".")
from enumerate_self_conjugate_partitions import (  # noqa: E402
    all_self_conjugate_partitions,
    distinct_odd_partitions,
    canonical_self_conjugate,
    content_sum,
    conjugate_partition,
)


def is_triangular(n: int) -> Tuple[bool, int]:
    """Is n = k(k+1)/2 for some k? Return (yes, k) or (no, 0)."""
    k = int((-1 + (1 + 8 * n) ** 0.5) / 2)
    for cand in (k - 1, k, k + 1):
        if cand >= 0 and cand * (cand + 1) // 2 == n:
            return True, cand
    return False, 0


def is_perfect_square(n: int) -> Tuple[bool, int]:
    k = int(n**0.5)
    for cand in (k - 1, k, k + 1):
        if cand >= 0 and cand * cand == n:
            return True, cand
    return False, 0


def parts_count_histogram(odd_parts_list: List[List[int]]) -> dict:
    """Histogram of decomposition lengths."""
    hist = {}
    for parts in odd_parts_list:
        L = len(parts)
        hist[L] = hist.get(L, 0) + 1
    return hist


def max_hook(odd_parts_list: List[List[int]]) -> int:
    """Largest hook length seen across all decompositions
    (= largest part in any distinct-odd-parts decomposition)."""
    if not odd_parts_list:
        return 0
    return max(max(parts) if parts else 0 for parts in odd_parts_list)


def collect_metrics(n: int) -> dict:
    odd_parts_list = distinct_odd_partitions(n)
    self_conjs = all_self_conjugate_partitions(n)
    canonical, count = canonical_self_conjugate(n)

    # Dimensions of each self-conjugate
    widths = [p[0] if p else 0 for p in self_conjs]
    heights = [len(p) for p in self_conjs]

    is_tri, tri_k = is_triangular(n)
    is_sq, sq_k = is_perfect_square(n)

    # Triangular check: is the staircase [k, k-1, ..., 1] one of the
    # self-conjugates? (It always is when n is triangular.)
    has_staircase = False
    if is_tri and tri_k > 0:
        staircase = list(range(tri_k, 0, -1))
        has_staircase = staircase in self_conjs

    # Perfect-square check
    has_square = False
    if is_sq and sq_k > 0:
        square = [sq_k] * sq_k
        has_square = square in self_conjs

    return {
        "n": n,
        "q(n)": count,
        "decomposition_lengths": parts_count_histogram(odd_parts_list),
        "max_hook_length": max_hook(odd_parts_list),
        "max_durfee": (
            max(len(parts) for parts in odd_parts_list)
            if odd_parts_list
            else 0
        ),
        "min_durfee": (
            min(len(parts) for parts in odd_parts_list)
            if odd_parts_list
            else 0
        ),
        "is_triangular": is_tri,
        "is_perfect_square": is_sq,
        "has_staircase_self_conj": has_staircase,
        "has_square_self_conj": has_square,
        "canonical": canonical,
        "canonical_first_row": canonical[0] if canonical else 0,
        "canonical_height": len(canonical),
        "extremal_widest_first_row": max(widths) if widths else 0,
        "extremal_tallest_height": max(heights) if heights else 0,
        "extremal_narrowest_first_row": min(widths) if widths else 0,
    }


def main(argv: List[str]) -> int:
    magic = [2, 8, 20, 28, 50, 82, 126]
    nonmagic = [1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 18, 24, 30, 36, 40, 60, 100]
    all_n = sorted(set(magic + nonmagic))

    report = {}
    print(
        f"{'n':>4} {'q(n)':>5} {'magic':>5} {'tri':>3} {'sq':>3}"
        f" {'maxD':>4} {'minD':>4} {'maxhook':>7}"
        f" {'canon_w':>7} {'canon_h':>7}"
        f" {'wide':>4} {'tall':>4} {'narrow':>6}"
    )
    print("-" * 80)
    for n in all_n:
        m = collect_metrics(n)
        is_magic = n in magic
        report[n] = m
        report[n]["magic_ladder_member"] = is_magic
        print(
            f"{m['n']:>4} {m['q(n)']:>5}"
            f" {'★' if is_magic else ' ':>5}"
            f" {'T' if m['is_triangular'] else ' ':>3}"
            f" {'S' if m['is_perfect_square'] else ' ':>3}"
            f" {m['max_durfee']:>4} {m['min_durfee']:>4}"
            f" {m['max_hook_length']:>7}"
            f" {m['canonical_first_row']:>7} {m['canonical_height']:>7}"
            f" {m['extremal_widest_first_row']:>4}"
            f" {m['extremal_tallest_height']:>4}"
            f" {m['extremal_narrowest_first_row']:>6}"
        )

    print()
    print("Pattern probes:")
    print()

    # Probe 1: q(n) = 1 ("only one self-conjugate") iff n in some set?
    only_one = [n for n in all_n if report[n]["q(n)"] == 1]
    print(f"  q(n) = 1 (exactly one self-conjugate): n in {only_one}")
    print(f"    -> intersection with magic: {sorted(set(only_one) & set(magic))}")

    # Probe 2: max parts (max Durfee) at magic vs non-magic
    print()
    for n in magic:
        if n in report:
            print(
                f"  magic n={n}: max_durfee={report[n]['max_durfee']},"
                f" min_durfee={report[n]['min_durfee']},"
                f" q(n)={report[n]['q(n)']}"
            )
    print()

    # Probe 3: q(n) jumps (n where q increases sharply over q(n-1))
    print("  q(n) increments q(n) - q(n-1):")
    for n in all_n:
        if n - 1 in report:
            jump = report[n]["q(n)"] - report[n - 1]["q(n)"]
            tag = " ★MAGIC" if n in magic else ""
            print(f"    n={n}: q={report[n]['q(n)']}, q(n)-q(n-1)={jump:+d}{tag}")

    # Probe 4: aspect ratio / "squareness" of canonical self-conj
    print()
    print("  canonical aspect (width/height) at magic:")
    for n in magic:
        if n in report and report[n]["canonical_height"] > 0:
            w = report[n]["canonical_first_row"]
            h = report[n]["canonical_height"]
            print(
                f"    n={n}: canon=[{w},...,{h} rows], aspect w/h = {w/h:.3f}"
            )

    # Save full report
    with open("magic_vs_nonmagic_report.json", "w") as f:
        json.dump(
            {str(k): v for k, v in report.items()},
            f,
            indent=2,
        )
    print()
    print("Full report saved to magic_vs_nonmagic_report.json")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
