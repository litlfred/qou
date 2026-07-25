"""Exact Fraction-coefficient truncated q-series — shared engine for the
B1.x Masbaum/GGM module-map probes.

A series to O(q^N) is a list of N `fractions.Fraction`. All operations
are exact; there are no numerics anywhere in this module. The H-series
generator is the exact port of A2's symbolic generator
(`qbeta_5two_stokes_barodd_index_probe.H_series` — identical formulas:
E1n/E2n geometric expansion, (q;q)_n inverse cube, same loop bounds),
first landed inside `qbeta_5two_masbaum_block_row_probe.py` (B1.3,
PR #4235) where it is re-gated against the 18 printed GGM tables; the
sympy route is intractable at order ≳ 30.

Domain note: `h_series` requires every term exponent to be ≥ 0, which
bounds the λ-grid — sign +1 needs λ ≥ −2 (expo = n(n+1)+nλ), sign −1
needs λ ≥ −1 (expo = n(n+1)/2+nλ). Callers must respect this; the
function raises on a negative exponent rather than silently wrapping.
"""
from __future__ import annotations

from fractions import Fraction


def s_new(n):
    return [Fraction(0)] * n


def s_const(v, n):
    s = s_new(n)
    s[0] = Fraction(v)
    return s


def s_add(a, b):
    return [x + y for x, y in zip(a, b)]


def s_scale(a, v):
    v = Fraction(v)
    return [x * v for x in a]


def s_mul(a, b):
    n = len(a)
    out = [Fraction(0)] * n
    for i, ai in enumerate(a):
        if ai:
            for j in range(n - i):
                if b[j]:
                    out[i + j] += ai * b[j]
    return out


def s_inv(a):
    """Multiplicative inverse of a truncated series with a[0] ≠ 0."""
    n = len(a)
    out = [Fraction(0)] * n
    out[0] = 1 / a[0]
    for k in range(1, n):
        acc = Fraction(0)
        for i in range(1, k + 1):
            if a[i]:
                acc += a[i] * out[k - i]
        out[k] = -acc / a[0]
    return out


def s_shift(a, m):
    n = len(a)
    if m >= n:
        return s_new(n)
    return [Fraction(0)] * m + a[: n - m]


def s_theta(a):
    """Euler operator θ = q·d/dq: coefficient-wise multiply by exponent."""
    return [Fraction(e) * c for e, c in enumerate(a)]


def qpoch_n_ser(n, ord_):
    """(q;q)_n as a truncated series."""
    s = s_const(1, ord_)
    for k in range(1, n + 1):
        f = s_new(ord_)
        f[0] = Fraction(1)
        if k < ord_:
            f[k] = Fraction(-1)
        s = s_mul(s, f)
    return s


def qpoch_inf_ser(ord_):
    """(q;q)_∞ exact to O(q^ord) (factors beyond q^{ord-1} contribute
    only above the truncation)."""
    s = s_const(1, ord_)
    for jj in range(1, ord_):
        f = s_new(ord_)
        f[0] = Fraction(1)
        f[jj] = Fraction(-1)
        s = s_mul(s, f)
    return s


def e_n_ser(n, ord_, weight=False):
    """Σ_{s≥1, s(n+1)<ord} [s·]q^{s(n+1)}/(1−q^s), geometric-expanded —
    the exact port of A2's E1n_ser (weight=False) / E2n_ser (True)."""
    out = s_new(ord_)
    for s in range(1, ord_ + 1):
        if s * (n + 1) < ord_:
            w = Fraction(s if weight else 1)
            e = s * (n + 1)
            while e < ord_:
                out[e] += w
                e += s
    return out


def h_term(sign, j, lam, n, ord_):
    """The single n-th term of H±_{j,λ} as an exact truncated series
    (the per-level object for the cyclotomic-level tests)."""
    expo = (n * (n + 1) + n * lam if sign > 0
            else n * (n + 1) // 2 + n * lam)
    if expo < 0:
        raise ValueError(f"negative exponent {expo} at sign={sign}, "
                         f"lam={lam}, n={n} — outside the λ domain")
    inv1 = s_inv(qpoch_n_ser(n, ord_))
    invp3 = s_mul(s_mul(inv1, inv1), inv1)
    e1 = e_n_ser(n, ord_)
    e2_0 = e_n_ser(0, ord_, weight=True)
    if sign > 0:
        p1 = s_add(s_const(1 + 2 * n + lam, ord_), s_scale(e1, -3))
        if j == 0:
            pj = s_const(1, ord_)
        elif j == 1:
            pj = p1
        else:
            e2 = e_n_ser(n, ord_, weight=True)
            pj = s_add(s_add(s_mul(p1, p1), s_const(Fraction(-1, 6), ord_)),
                       s_add(s_scale(e2, -3), s_scale(e2_0, 4)))
        return s_shift(s_mul(pj, invp3), expo)
    p1 = s_add(s_const(Fraction(1, 2) + n + lam, ord_), s_scale(e1, -3))
    if j == 0:
        pj = s_const(1, ord_)
    elif j == 1:
        pj = p1
    else:
        e2 = e_n_ser(n, ord_, weight=True)
        pj = s_add(s_add(s_mul(p1, p1), s_const(Fraction(-1, 12), ord_)),
                   s_add(s_scale(e2, -3), s_scale(e2_0, 2)))
    return s_scale(s_shift(s_mul(pj, invp3), expo), (-1) ** n)


def h_series(sign, j, lam, ord_):
    """H±_{j,λ}(q) exact to O(q^ord) — Σ_n h_term with A2's loop bounds."""
    total = s_new(ord_)
    n = 0
    while True:
        expo = (n * (n + 1) + n * lam if sign > 0
                else n * (n + 1) // 2 + n * lam)
        if expo >= ord_ and n > 0:
            break
        total = s_add(total, h_term(sign, j, lam, n, ord_))
        n += 1
        if n > 2 * ord_:
            break
    return total
