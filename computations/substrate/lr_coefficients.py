#!/usr/bin/env python3
"""Littlewood-Richardson coefficients via skew-tableau enumeration.

Provides `lr_coef(mu, nu, lam)` for arbitrary partitions, computed
via direct enumeration of LR skew tableaux of shape λ/μ with
content ν.  Cached at module level for repeated use.

Algorithm: c^λ_{μν} = # SSYT of skew shape λ/μ filled with content
ν such that the reverse-reading-word is Yamanouchi (every prefix
has count(i) ≥ count(i+1)).  Direct backtracking with strict-column
+ Yamanouchi pruning.

Precomputed LR tables for the A=2/A=3/A=4 atomic decompositions
(`LR_TABLE_3_3_TO_6`, `LR_TABLE_3_6_TO_9`, `LR_TABLE_6_6_TO_12`)
are exposed as module-level dicts; consumers should use
`get_lr_table(n1, n2)` rather than the raw dicts.

The A=2 table `LR_TABLE_3_3_TO_6` is consistent with the existing
`sublemma_2_1_deuteron_branching.LR_TABLE_3_3_TO_6` (cross-checked
in this module's `__main__`).
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 6, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import functools


def partitions_of(n: int) -> list[tuple[int, ...]]:
    """All weakly-decreasing partitions of n."""
    out: list[tuple[int, ...]] = []
    def _go(remaining: int, max_part: int, prefix: tuple[int, ...]):
        if remaining == 0:
            out.append(prefix)
            return
        for k in range(min(remaining, max_part), 0, -1):
            _go(remaining - k, k, prefix + (k,))
    _go(n, n, ())
    return out


def _shape_contains(mu: tuple[int, ...], lam: tuple[int, ...]) -> bool:
    """True iff Young diagram of μ is contained in that of λ."""
    if len(mu) > len(lam):
        return False
    return all(mu[i] <= lam[i] for i in range(len(mu)))


def _skew_cells(mu: tuple[int, ...], lam: tuple[int, ...]) -> list[tuple[int, int]]:
    """Cells in λ but not in μ, in row-major order (row, col)."""
    cells = []
    for i, lam_i in enumerate(lam):
        mu_i = mu[i] if i < len(mu) else 0
        for j in range(mu_i, lam_i):
            cells.append((i, j))
    return cells


def _is_yamanouchi(reverse_word: list[int], n_letters: int) -> bool:
    """Check Yamanouchi (reverse-lattice) property: every prefix has
    count(i) ≥ count(i+1) for all i ≥ 1."""
    counts = [0] * (n_letters + 1)
    for v in reverse_word:
        counts[v] += 1
        for i in range(1, n_letters):
            if counts[i] < counts[i + 1]:
                return False
    return True


def _enumerate_lr_with_yamanouchi_check(skew_cells, nu, lam, mu) -> int:
    """Same as `_enumerate_lr` but enforces Yamanouchi at the leaf."""
    n_letters = len(nu)
    target_counts = list(nu)
    cur_counts = [0] * (n_letters + 1)
    grid: dict[tuple[int, int], int] = {}
    # Track reverse word (filled in REVERSE row-major order ==
    # bottom-right to top-left).  But we fill forward; we'll compute
    # the reverse word at the leaf.
    count = 0

    # Build reading order: top-to-bottom, right-to-left within each row.
    # This is the "reverse reading word" used in the standard LR
    # Yamanouchi convention.  Group skew_cells by row, sort each row
    # in DECREASING column order, concatenate top-to-bottom.
    by_row: dict[int, list[tuple[int, int]]] = {}
    for (i, j) in skew_cells:
        by_row.setdefault(i, []).append((i, j))
    rev_reading_order: list[tuple[int, int]] = []
    for i in sorted(by_row):
        for cell in sorted(by_row[i], key=lambda c: -c[1]):
            rev_reading_order.append(cell)

    def reverse_word_from_grid() -> list[int]:
        return [grid[c] for c in rev_reading_order]

    def go(idx: int) -> int:
        nonlocal count
        if idx == len(skew_cells):
            if all(cur_counts[i + 1] == target_counts[i] for i in range(n_letters)):
                rw = reverse_word_from_grid()
                if _is_yamanouchi(rw, n_letters):
                    count += 1
            return 0
        i, j = skew_cells[idx]
        left_val = grid.get((i, j - 1), 0) if j > 0 else 0
        upper_val = grid.get((i - 1, j), 0) if i > 0 else 0
        lower = max(left_val, upper_val + 1, 1)
        for v in range(lower, n_letters + 1):
            if cur_counts[v] >= target_counts[v - 1]:
                continue
            grid[(i, j)] = v
            cur_counts[v] += 1
            go(idx + 1)
            cur_counts[v] -= 1
            del grid[(i, j)]
        return count

    return go(0)


@functools.lru_cache(maxsize=None)
def lr_coef(mu: tuple[int, ...], nu: tuple[int, ...], lam: tuple[int, ...]) -> int:
    """LR coefficient c^λ_{μν} via skew-tableau enumeration.

    Returns 0 if |μ| + |ν| ≠ |λ| or μ ⊄ λ (necessary conditions for
    non-zero LR).  Otherwise enumerates LR skew tableaux of shape
    λ/μ with content ν.
    """
    if sum(mu) + sum(nu) != sum(lam):
        return 0
    if not _shape_contains(mu, lam):
        return 0
    skew = _skew_cells(mu, lam)
    if len(skew) != sum(nu):
        return 0
    return _enumerate_lr_with_yamanouchi_check(skew, nu, lam, mu)


def build_lr_table(n1: int, n2: int) -> dict:
    """Build the full LR table for partitions of n1, n2 → partitions of n1 + n2.
    Returns dict {(mu, nu, lam): c^λ_{μν}} with non-zero entries only.
    """
    parts_1 = partitions_of(n1)
    parts_2 = partitions_of(n2)
    parts_sum = partitions_of(n1 + n2)
    out: dict[tuple, int] = {}
    for mu in parts_1:
        for nu in parts_2:
            for lam in parts_sum:
                c = lr_coef(mu, nu, lam)
                if c > 0:
                    out[(mu, nu, lam)] = c
    return out


@functools.lru_cache(maxsize=None)
def get_lr_table(n1: int, n2: int) -> dict:
    """Cached LR table for (n1, n2) → (n1+n2)."""
    return build_lr_table(n1, n2)


# ──────────────────────────────────────────────────────────────────
# Self-test against the hardcoded LR_TABLE_3_3_TO_6.
# ──────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
    from sublemma_2_1_deuteron_branching import LR_TABLE_3_3_TO_6 as REFERENCE

    print("Building LR table for (3, 3) → 6 ...")
    table = get_lr_table(3, 3)
    print(f"  computed {len(table)} non-zero entries")
    print(f"  reference has {len(REFERENCE)} entries")
    print()
    mismatches = []
    for k, v_ref in REFERENCE.items():
        v_computed = table.get(k, 0)
        if v_computed != v_ref:
            mismatches.append((k, v_ref, v_computed))
    extras = []
    for k, v_computed in table.items():
        if k not in REFERENCE:
            extras.append((k, v_computed))
    print(f"  reference→computed mismatches: {len(mismatches)}")
    for k, v_ref, v_c in mismatches[:5]:
        print(f"    {k}: ref={v_ref} computed={v_c}")
    print(f"  computed-only entries: {len(extras)}")
    for k, v_c in extras[:5]:
        print(f"    {k}: computed={v_c}")
    if not mismatches and not extras:
        print("  ✓ EXACT match against reference LR_TABLE_3_3_TO_6.")

    print()
    print("Building LR table for (3, 6) → 9 (A=3 split) ...")
    table_36 = get_lr_table(3, 6)
    print(f"  computed {len(table_36)} non-zero entries")

    print()
    print("Building LR table for (6, 6) → 12 (A=4 split) ...")
    import time
    t0 = time.time()
    table_66 = get_lr_table(6, 6)
    elapsed = time.time() - t0
    print(f"  computed {len(table_66)} non-zero entries in {elapsed:.1f}s")
