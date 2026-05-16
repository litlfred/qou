"""
Shared utility: quantum dilogarithm Φ_q at MPFR precision.

Used by:
  - terms_2_3_atom_per_gen_mpfr_50dps.py    (electron, p, n, D, T, ³He)

Φ_q(z) = ∏_{k≥1} (1 − q^{-k}·z)^{-1}

Restored from `_deprecated/_phi_q_util.py` (audited-removed alongside
disjoint-product convention witnesses on 2026-05-08, but the Φ_q
utility itself is convention-agnostic and is the canonical Wedderburn-
block sum factor for the A=1 single-nucleon case where no
inter-nucleon interface ambiguity exists).
"""
from __future__ import annotations

from mpmath import mp, mpf


def phi_q(z_val: mpf, q_inv: mpf, max_k: int = 2000, eps: mpf | None = None) -> mpf:
    """Quantum dilogarithm Φ_q(z) = ∏_{k≥1} (1 − q^{-k}·z)^{-1}.

    Truncates the product when the term magnitude falls below ``eps``
    or after ``max_k`` factors, whichever comes first.  Default eps is
    10^{-(mp.dps − 5)} so the truncation floor stays well below the
    current precision.

    Returns ``mpf('inf')`` when the convergence radius is hit (``|z|
    ≥ q``), surfacing real pole hits as infinities rather than
    silently truncating.
    """
    if eps is None:
        eps = mpf(10) ** (5 - mp.dps)
    if mp.fabs(z_val) >= mpf(1) / q_inv:
        return mpf("inf")
    product = mpf(1)
    qi_pow = q_inv
    for _ in range(max_k):
        term = qi_pow * z_val
        factor = mpf(1) - term
        if mp.fabs(factor) < eps:
            return mpf("inf")
        product /= factor
        if mp.fabs(term) < eps:
            break
        qi_pow *= q_inv
    return product
