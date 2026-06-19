"""qbeta_bar_odd.py — shared Laurent / bar-odd utilities for the §4a tower probes.

Centralizes the `laurent_coeffs` + `bar_odd` helpers that were duplicated across the
brane-tower / eigenbasis probes (`chi_content_eigenbasis_probe`,
`chi_content_single_mode_probe`, `eigenbasis_structural_lemmas_probe`, and the merged
`bn_minus_bp_*` probes). Single source of truth, per the Gemini DRY review on PR #2502.

`Q` (the sympy symbol for the substrate variable) is passed in by the caller — every
caller already holds `from hoefsmit_symbolic import ..., Q`, so threading it explicitly
avoids any import-order coupling with the path-bridge.
"""
from __future__ import annotations

import sympy as sp


def laurent_coeffs(expr, Q) -> dict[int, "sp.Expr"]:
    """Exact `{exponent: coefficient}` map of a Laurent polynomial in `Q`.

    The expression must reduce to numerator / (monomial in Q) — i.e. a genuine Laurent
    polynomial. The monomial-denominator assertion guards against a non-monomial
    denominator silently yielding mathematically wrong "Laurent coefficients"
    (per the Gemini review note on PR #2502).
    """
    e = sp.cancel(sp.together(expr))
    num, den = sp.fraction(e)
    dpoly = sp.Poly(sp.expand(den), Q)
    if len(dpoly.monoms()) != 1:
        raise ValueError(
            f"laurent_coeffs: denominator is not a monomial in Q ({den}); "
            "expression is not a Laurent polynomial")
    md, cd = dpoly.monoms()[0][0], dpoly.coeffs()[0]
    npoly = sp.Poly(sp.expand(num), Q)
    return {m[0] - md: sp.cancel(c / cd)
            for m, c in zip(npoly.monoms(), npoly.coeffs())}


def bar_odd(expr, Q) -> dict[int, "sp.Expr"]:
    """Bar-odd (sinh) decomposition: `{k > 0: a_k - a_{-k}}` for nonzero entries.

    With `q = e^η`, the sinh(kη) coefficient of a Laurent polynomial `Σ a_j q^j` is
    `a_k - a_{-k}` (since `a_k q^k + a_{-k} q^{-k} = (a_k+a_{-k})cosh(kη)
    + (a_k-a_{-k})sinh(kη)`). Returns only the nonzero orders.
    """
    c = laurent_coeffs(expr, Q)
    orders = sorted({abs(k) for k in c if k != 0})
    out = {}
    for k in orders:
        if k <= 0:
            continue
        v = sp.cancel(c.get(k, 0) - c.get(-k, 0))
        if v != 0:
            out[k] = v
    return out
