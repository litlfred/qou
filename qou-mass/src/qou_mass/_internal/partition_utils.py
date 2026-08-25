"""
Partition / Young-diagram utilities — single source of truth.

Replaces the 20+ ad-hoc copies of ``hook_length`` / ``hook_lengths``
that used to live in individual computation scripts. Functions
return values in row-major order over cells of the Young diagram
and use 0-indexed (row, column) by default; a 1-indexed convenience
wrapper is provided for legacy callers.

A "partition" is a non-increasing sequence of positive integers,
represented as a ``tuple[int, ...]`` (or any sequence). Empty input
is handled (returns empty result / 1 for dimension).
"""

from __future__ import annotations

from functools import lru_cache
from typing import Sequence


def conjugate_partition(shape: Sequence[int]) -> tuple[int, ...]:
    """Conjugate (transpose) partition λ' of λ.

    ``λ'_j = #{ i : λ_i > j }`` (0-indexed columns).
    """
    if not shape:
        return ()
    conj = [0] * max(shape)
    for row in shape:
        for j in range(row):
            conj[j] += 1
    return tuple(conj)


def hook_length(shape: Sequence[int], i: int, j: int) -> int:
    """Hook length ``h_{(i, j)} = arm + leg + 1`` at cell (i, j),
    0-indexed.

    arm = cells to the right of (i, j) in row i
    leg = cells below (i, j) in column j
    """
    arm = shape[i] - j - 1
    leg = sum(1 for r in range(i + 1, len(shape)) if shape[r] > j)
    return arm + leg + 1


def hook_length_1based(shape: Sequence[int], i: int, j: int) -> int:
    """1-indexed convenience wrapper around :func:`hook_length`.

    Callers in :mod:`term7_chi5_basis`, :mod:`chirality_avg_content`,
    :mod:`term7_height6_partition_enum`, and
    :mod:`chirality_avg_content_chiral` use 1-indexed cells; this
    wrapper preserves that contract.
    """
    return hook_length(shape, i - 1, j - 1)


def hook_lengths(shape: Sequence[int]) -> list[int]:
    """Hook-length sequence ``[h_{(i, j)}]`` for cells of λ in
    row-major order (0-indexed)."""
    if not shape:
        return []
    conj = conjugate_partition(shape)
    return [
        (shape[i] - j - 1) + (conj[j] - i - 1) + 1
        for i in range(len(shape))
        for j in range(shape[i])
    ]


def hook_lengths_with_cells(
    shape: Sequence[int],
) -> list[tuple[int, int, int]]:
    """List of ``(i, j, hook)`` triples for cells of λ in row-major
    order (0-indexed)."""
    if not shape:
        return []
    conj = conjugate_partition(shape)
    return [
        (i, j, (shape[i] - j - 1) + (conj[j] - i - 1) + 1)
        for i in range(len(shape))
        for j in range(shape[i])
    ]


@lru_cache(maxsize=None)
def hook_lengths_cached(shape: tuple[int, ...]) -> tuple[int, ...]:
    """Memoized variant of :func:`hook_lengths`, returning a tuple
    so the result is hashable / safe to cache."""
    return tuple(hook_lengths(shape))


def dim_lambda(shape: Sequence[int]) -> int:
    """Dimension of the irreducible S_n / Specht / seminormal module V_λ
    (= number of standard Young tableaux of shape λ), via the hook-length
    formula ``d_λ = n! / ∏_cells hook``. Exact integer.

    Single source of truth — replaces ad-hoc ``partition_dim`` / ``syt_count``
    / ``hook_length_dim`` copies across compute scripts.
    """
    import math
    n = sum(shape)
    if n == 0:
        return 1
    prod = 1
    for h in hook_lengths(shape):
        prod *= h
    return math.factorial(n) // prod
