"""
Shared utility: COMPACT quantum dilogarithm at MPFR precision.

**Terminology (corrected 2026-07-06).** The function below is the
**compact quantum dilogarithm** — a reciprocal q-Pochhammer / q-exponential

    phi_q(z) = ∏_{k≥1} (1 − q^{-k}·z)^{-1} = (q^{-1}z ; q^{-1})_∞^{-1}.

It is **NOT** the Faddeev *non-compact* quantum dilogarithm `Φ_b`, which is
the **modular-double** object (ratio of two products over `b` and `b^{-1}`;
kernel `sinh(zb)sinh(zb^{-1})`; poles at `c_b + ibℕ + ib^{-1}ℕ`;
`Φ_b = Φ_{b^{-1}}`). The legacy name `phi_q` and the historic "Faddeev Φ_q"
framing are **misleading** — retained here only for import stability
(production mass consumers import this symbol). Do not read this as `Φ_b`.
See [`docs/audits/2026-07-06-qbeta-faddeev-phi-b-modular-double-accuracy.md`].

**Which face this is correct for.** Evaluated at the *real* substrate
`q₀ > 1`, this compact form is the **real-q / Rogers-adjacent** object and
is the right one for the **MASS / bar-even / volume face** (m_p, m_n, m_e,
m_atom absolutes and m_p/m_e). It is bar-asymmetric under `q ↔ q^{-1}`, but
that asymmetry is **not** the full Chern–Simons/decay structure — that
requires the missing `b^{-1}` modular-dual factor (the `Φ_b` decay face,
open f-map). So this utility is correct where it is used (mass), but must
**not** be substituted for `Φ_b` on the Q_β/decay (bar-odd) face.

For BINDING context (B(K) = m_atom − Z·m_p − N·m_n, Δm_pn, isospin
differences) use `_li_2_q_util.py` instead — Li_2^q is the bar-symmetric
(pre-τ, R-side) form; binding energies are mass-differences where the
dimensional scale cancels, so the bar-symmetric form applies.

Empirical witness: substituting Li_2^q for Φ_q in the mass tower gives
m_p/m_e ≈ 3.31 (99.82% off CODATA 1836) — the bar-symmetric projection
kills the dimensional mass scale. See `m-p-m-e-li2q.witness.json`.

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
