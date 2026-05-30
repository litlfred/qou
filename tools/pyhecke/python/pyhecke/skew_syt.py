"""Skew standard Young tableau counts via Aitken-Steinberg determinant.

The number `f^{lambda/mu}` of standard Young tableaux of skew shape
`lambda/mu` is given by the Aitken-Steinberg determinant formula

    f^{lambda/mu} = (|lambda| - |mu|)! * det_{i,j} [ 1 / (lambda_i - mu_j - i + j)! ]

where i, j range over 1..ell(lambda), and `1/k! := 0` for k < 0.

Used by `UNIVERSAL-BRANCHING-PLAN.md` Gap #1 — atom character
expansion via universal branching rule

    chi_free(lambda) = sum_{(mu_1,...,mu_A), mu_i |- 3}
                       f^{lambda/(mu_1 sqcup ... sqcup mu_A)}
                       * prod_i chi^{mu_i}(K_i)

References:
  - Aitken (1943), "The monomial expansion of determinantal symmetric
    functions", Proc. Edinburgh Math. Soc. 7, 1-5.
  - Stanley, "Enumerative Combinatorics, Vol. 2", §7.16
    (Jacobi-Trudi / Aitken determinants for skew Schur functions).
  - Naruse (2014) hook formula for the cancellation-free analogue.

All arithmetic is exact (Fraction); the final determinant times
(n - |mu|)! is an integer.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial
from typing import Sequence


__all__ = [
    "skew_syt_count",
    "concatenate_partitions",
    "fits_inside",
]


def _inv_fact_frac(k: int) -> Fraction:
    """Return 1/k! as exact Fraction, or 0 for k < 0."""
    if k < 0:
        return Fraction(0)
    return Fraction(1, factorial(k))


def _det_fraction(matrix: list[list[Fraction]]) -> Fraction:
    """Exact determinant of a square Fraction matrix via Laplace expansion.

    Fine for small matrices (ell(lambda) <= ~12) where partition lengths in
    QOU atom-branching contexts live (A-nucleon atom -> lambda |- 3A,
    so ell(lambda) <= 3A; A <= 8 hits ell <= 24, which is the upper end).
    For larger shapes, swap in Bareiss / sympy.Matrix.det.
    """
    n = len(matrix)
    if n == 0:
        return Fraction(1)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    # Laplace expansion along row 0
    total = Fraction(0)
    for j in range(n):
        if matrix[0][j] == 0:
            continue
        minor = [row[:j] + row[j + 1 :] for row in matrix[1:]]
        sign = 1 if j % 2 == 0 else -1
        total += sign * matrix[0][j] * _det_fraction(minor)
    return total


def concatenate_partitions(partitions: Sequence[Sequence[int]]) -> tuple[int, ...]:
    """Concatenate a tuple of partitions into a single weakly-decreasing tuple.

    Used to build mu = mu_1 sqcup ... sqcup mu_A from per-nucleon
    H_3 partitions in the universal branching rule.

    Args:
        partitions: sequence of partitions (each weakly decreasing).

    Returns:
        Sorted-descending tuple of all parts (zeros dropped).
    """
    parts: list[int] = []
    for p in partitions:
        parts.extend(int(x) for x in p if int(x) > 0)
    parts.sort(reverse=True)
    return tuple(parts)


def fits_inside(mu: Sequence[int], lambda_: Sequence[int]) -> bool:
    """Return True iff mu is contained in lambda_ as Young diagrams."""
    mu_ = [int(x) for x in mu if int(x) > 0]
    lam = [int(x) for x in lambda_ if int(x) > 0]
    if len(mu_) > len(lam):
        return False
    return all(mu_[i] <= lam[i] for i in range(len(mu_)))


def skew_syt_count(
    lambda_: Sequence[int],
    mu: Sequence[int] = (),
) -> int:
    """Count standard Young tableaux of skew shape lambda/mu.

    Computes `f^{lambda/mu} = |SYT(lambda/mu)|` via the Aitken-Steinberg
    determinant formula. Returns an exact integer.

    Args:
        lambda_: outer partition (weakly decreasing positive ints).
        mu: inner partition (default empty -> straight shape).
            Need not be pre-padded; trailing zeros are accepted.

    Returns:
        Number of standard Young tableaux of shape lambda/mu.
        Returns 0 if mu is not contained in lambda_.

    Examples:
        >>> skew_syt_count((2, 1))           # f^{(2,1)} = 2
        2
        >>> skew_syt_count((3, 1))           # f^{(3,1)} = 3
        3
        >>> skew_syt_count((3, 2), (1,))     # f^{(3,2)/(1)} = 5
        5
        >>> skew_syt_count((2, 2), (2, 2))   # empty skew shape -> 1
        1
    """
    lam = [int(x) for x in lambda_ if int(x) > 0]
    L = len(lam)
    if L == 0:
        # Empty outer shape: only the empty skew is valid.
        return 1 if (sum(int(x) for x in mu) == 0) else 0

    m = [int(x) for x in mu]
    # Pad mu with zeros up to length L
    while len(m) < L:
        m.append(0)
    # Truncate if mu longer than lambda
    if any(m[i] > 0 for i in range(L, len(m))):
        return 0
    m = m[:L]

    # Containment check
    if any(m[i] > lam[i] for i in range(L)):
        return 0

    n = sum(lam) - sum(m)
    if n == 0:
        return 1

    # Aitken-Steinberg: M[i][j] = 1 / (lambda_{i+1} - mu_{j+1} - (i+1) + (j+1))!
    # i, j 0-indexed in code; +1 to match the formula.
    M = [
        [_inv_fact_frac(lam[i] - m[j] - (i + 1) + (j + 1)) for j in range(L)]
        for i in range(L)
    ]
    det = _det_fraction(M)
    result = factorial(n) * det
    # Result is provably an integer; assert and return.
    assert result.denominator == 1, (
        f"skew_syt_count({lambda_}, {mu}): non-integer result {result}"
    )
    return result.numerator
