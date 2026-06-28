"""Shared, cached Young-diagram / symmetric quantum-dimension machinery.

Factored out of the lever-1 / W_λ / binding-Habiro probes (PR #2899, #2929, #2941, #2951), which
each re-implemented and re-computed the same partition / hook / `dim_q` / `S(m)` machinery
symbolically from scratch — the dominant cost. This module provides ONE cached implementation:

    partitions(n)      — partitions of n as weakly-decreasing lists
    conj(lam)          — conjugate partition
    cells(lam)         — list of (i, j) cells
    hook(lam, i, j)    — hook length (arm + leg + 1)
    content(i, j)      — j − i
    qint(k), qfact(n)  — symmetric q-integer [k]_q and q-factorial [n]_q!
    dim_q(lam)         — symmetric quantum dimension [n]_q! / ∏ [h_c]_q   (cached)
    S(m)               — Σ_{λ⊢m} dim_q(λ)  (the binding period; q=1 → involution numbers)  (cached)

`dim_q` and `S` are `functools.lru_cache`-memoised, so repeated / cross-probe calls are free after
the first. `q` is the module-level sympy symbol; callers substitute as needed.

Bean: z3a2 (compute infra). Migration of the existing in-repo probes to this module is queued
(bean z3a2 follow-up); new probes should import from here.
"""
from functools import lru_cache

import sympy as sp

q = sp.Symbol("q", positive=True)


@lru_cache(maxsize=None)
def partitions(n):
    """Partitions of `n` as a tuple of weakly-decreasing tuples (hashable for caching)."""
    if n == 0:
        return ((),)
    out = []
    for first in range(n, 0, -1):
        for rest in partitions(n - first):
            if not rest or rest[0] <= first:
                out.append((first,) + rest)
    return tuple(out)


def conj(lam):
    """Conjugate partition (as a tuple)."""
    if not lam:
        return ()
    return tuple(sum(1 for r in lam if r > c) for c in range(lam[0]))


def cells(lam):
    return [(i, j) for i, row in enumerate(lam) for j in range(row)]


def arm(lam, i, j):
    return lam[i] - j - 1


def leg(cj, i, j):
    return cj[j] - i - 1


def hook(lam, i, j, cj=None):
    cj = cj if cj is not None else conj(lam)
    return arm(lam, i, j) + leg(cj, i, j) + 1


def content(i, j):
    return j - i


def qint(k):
    """Symmetric q-integer [k]_q = (q^k − q^−k)/(q − q^−1)."""
    return (q ** k - q ** (-k)) / (q - 1 / q)


@lru_cache(maxsize=None)
def qfact(n):
    r = sp.Integer(1)
    for k in range(1, n + 1):
        r *= qint(k)
    return r


@lru_cache(maxsize=None)
def dim_q(lam):
    """Symmetric quantum dimension [n]_q! / ∏_c [h_c]_q (cancelled). `lam` must be a tuple."""
    cj = conj(lam)
    d = qfact(sum(lam))
    for (i, j) in cells(lam):
        d /= qint(hook(lam, i, j, cj))
    return sp.cancel(sp.together(d))


@lru_cache(maxsize=None)
def S(m):
    """S(m) = Σ_{λ⊢m} dim_q(λ); q=1 → involution numbers 1,1,2,4,10,26,76,232,764,…"""
    if m == 0:
        return sp.Integer(1)
    return sp.cancel(sp.together(sum(dim_q(lam) for lam in partitions(m))))


def _selftest():
    # q=1 limit of S(m) is the involution numbers
    invol = [1, 1, 2, 4, 10, 26, 76, 232, 764]
    for m in range(len(invol)):
        assert sp.simplify(S(m).subs(q, 1) - invol[m]) == 0, f"S({m}) q=1 mismatch"
    # known closed forms reproduced (cross-check with PR #2899)
    assert sp.simplify(S(3) / 3 - (q + 1) ** 2 / (3 * q)) == 0  # lw(2) = S(3)/3 = (q+1)²/(3q)
    assert sp.simplify(dim_q((2, 1)) - (q + 1 / q)) == 0  # dim_q([2,1]) = [2]_q = q + q⁻¹
    print("young_qdim self-test: OK (involution-number limit + lw(2) + dim_q([2,1]))")


if __name__ == "__main__":
    _selftest()
