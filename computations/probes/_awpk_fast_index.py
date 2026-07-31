"""_awpk_fast_index.py — exact-integer canonical-chamber engine for deep
I_Δ / I_{4₁} substrate evaluation.  NO floats anywhere in the series
arithmetic (owner directive 2026-07-31: no float64); coefficients are exact
Python ints, evaluation is mpmath at the session dps.

Helper for qbeta_awpk_perwinding_stokes_41_probe.py. Why the plain exact
engine (qbeta_g3_tetrahedron_index_exact.tet_index_exact + dict ser_mul)
cannot reach the substrate point: index coefficients grow ~e^{c√k}, so at
q̃ = 1/q₀ ≈ 0.9009 the series only begins to converge near q̃-order ~600,
and the dict-based per-n Pochhammer inversions cost ~18 min per winding at
x-order 1600 — while still under-covering high absolute exponents for the
deep-negative-shift factors (the corrected-assembly probe's "higher internal
order" truncation subtlety).

Two exact structural fixes:

1. CHAMBER CANONICALIZATION.  The certified S₃ triality
   (tetrahedron-index-triality-pin: reflection I(m,e) = I(−e,−m) ∘ cyclic
   I(m,e) = (−q^½)^m·I(−e−m, m)) gives the exact identity
       I_Δ(m,e) = (−q^½)^m · I_Δ(−m, e+m).
   In the m ≤ 0 chamber every term exponent n(n+1) − (2n+e)m is ≥ 0
   (for n ≥ max(0,−e), 2n+e ≥ 0), so the series has NO Laurent part: the
   shift is ≥ 0, absolute-exponent coverage is order+shift ≥ order, and the
   massive cancelling Laurent tails of the raw m > 0 representation never
   arise.  The monomial prefactor is an exact integer shift + sign.

2. INCREMENTAL POCHHAMMER + POINT EVALUATION.  Per tetrahedron factor the
   running product Pₙ = 1/((q;q)_n (q;q)_{n+e}) is updated
   Pₙ₊₁ = Pₙ · 1/(1−x^{2(n+1)}) · 1/(1−x^{2(n+1+e)}) by two ascending
   cumulative-sum passes (O(order) int additions each) — no per-n dict
   inversions.  And the eq-(4.18) flux sum is evaluated as
       I_{4₁}(m,e)(x) = Σ_{e₂} (±) x^{sh₁+sh₂} · f₁(x) · f₂(x)
   by evaluating each factor series at x with mpmath — no series
   convolution at all (the product of evaluations IS the evaluation of the
   product).

Convergence certification is by INTERNAL-ORDER stability: the caller
evaluates at two (or more) truncation orders and measures digits of
agreement — a diff ≥ 1 counts as 0 digits (no else-40 sentinel).
"""
from __future__ import annotations

import mpmath as mp


class CanonicalTetEngine:
    """Exact-integer tetrahedron-index series in the m ≤ 0 chamber."""

    def __init__(self, order: int):
        self.order = order

    def tet_series(self, m: int, e: int):
        """I_Δ(m,e) as (shift ≥ 0 after canonicalization?, sign, int-list).

        Returns (shift, sign, coeffs) with I_Δ(m,e) = sign · x^shift ·
        Σ_d coeffs[d]·x^d, coeffs exact ints, len(coeffs) = order+1.
        For m > 0 the canonical identity I_Δ(m,e) = (−q^½)^m·I_Δ(−m, e+m)
        is applied first; in the m ≤ 0 chamber min_expo ≥ 0."""
        pre_shift, pre_sign = 0, 1
        if m > 0:
            pre_shift, pre_sign = m, (-1 if m % 2 else 1)
            m, e = -m, e + m
        order = self.order
        lo = max(0, -e)
        # first n: P_lo = 1/((q;q)_lo (q;q)_{lo+e}); one of the two args is 0
        # (lo = 0 for e ≥ 0 gives (q;q)_0 = 1; lo = −e for e < 0 likewise),
        # so P_lo is a single inverse Pochhammer — build it incrementally too.
        P = [0] * (order + 1)
        P[0] = 1
        for j in range(1, max(lo, lo + e) + 1):
            for d in range(2 * j, order + 1):
                P[d] += P[d - 2 * j]
        out = [0] * (order + 1)
        n = lo
        min_expo = None
        while True:
            expo = n * (n + 1) - (2 * n + e) * m
            if min_expo is None or expo < min_expo:
                min_expo = expo
            if n > abs(m) + abs(e) + 2 and expo - min_expo > order:
                break
            off = expo - min_expo
            if off <= order:
                sgn = -1 if n % 2 else 1
                if sgn > 0:
                    for d in range(0, order + 1 - off):
                        out[off + d] += P[d]
                else:
                    for d in range(0, order + 1 - off):
                        out[off + d] -= P[d]
            # advance P to n+1: multiply by 1/(1−x^{2(n+1)})·1/(1−x^{2(n+1+e)})
            for j in (n + 1, n + 1 + e):
                if j > 0:
                    step = 2 * j
                    for d in range(step, order + 1):
                        P[d] += P[d - step]
            n += 1
        assert min_expo is not None and min_expo >= 0, \
            f"canonical chamber violated: min_expo={min_expo} for (m,e)=({m},{e})"
        return min_expo + pre_shift, pre_sign, out


def eval_I41_at(m: int, e: int, x_mp, order: int, e2_window: int):
    """I_{4₁}(m,e) evaluated at x = x_mp via DGG eq (4.18) point evaluation:
    Σ_{e₂} sign₁·sign₂ · x^{sh₁+sh₂} · f₁(x)·f₂(x), exact-int coefficients,
    mpmath arithmetic.  Returns the mp value."""
    eng = CanonicalTetEngine(order)
    # powers of x once
    xpow = [mp.mpf(1)] * (order + 1)
    for k in range(1, order + 1):
        xpow[k] = xpow[k - 1] * x_mp

    def eval_factor(sh, sign, coeffs):
        s = mp.fsum(c * xpow[d] for d, c in enumerate(coeffs) if c)
        return sign * (x_mp ** sh) * s

    total = mp.mpf(0)
    for e2 in range(-e2_window, e2_window + 1):
        f1 = eng.tet_series(m - e2, m + e - e2)
        f2 = eng.tet_series(e - e2, -e2)
        total += eval_factor(*f1) * eval_factor(*f2)
    return total
