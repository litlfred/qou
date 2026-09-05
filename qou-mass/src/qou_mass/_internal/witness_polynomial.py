"""
Symbolic-polynomial witness helper for the symbolic-in-$q$
discipline (workplan P2.5).

Convention: every witness JSON exposes both a polynomial form
(symbolic in $q$) and the numerical evaluation at $q_0$. This
module factors the boilerplate so any sympy-using script can add
the dual exposure with one call.

Usage::

    import sympy as sp
    from witness_polynomial import expose_polynomial

    q = sp.Symbol("q", positive=True, real=True)
    expr = ...  # symbolic in q

    witness["my_quantity"] = expose_polynomial(expr, q)

Output dict::

    {
        "polynomial_q": "...",        # str(sp.simplify(expr))
        "polynomial_q_latex": "...",  # sp.latex(sp.simplify(expr))
        "value_at_q0": "...",          # str(sp.N(expr.subs(q, q0)))
    }

Caller can override q_0 (default = paper's canonical substrate
parameter from `q_parameter.Q`).
"""
from __future__ import annotations

from typing import Any

import sympy as sp

# q0 read BY NAME (bean qou-9ugp, 2026-09-04). This file bound the RETIRED
# self-certified muon pin A as a literal -- superseded 2026-08-22 by the
# CODATA-2022 derivation, so the value was ~46 ppb stale AND could not follow
# the anchor. This stem is not in `ideal_muon`, so `Q_50_DIGIT_STR` resolves to
# the PROTON pin, which the 2026-08-30 owner ruling makes the default.
import sys as _sys_qp  # noqa: E402
from pathlib import Path as _Path_qp  # noqa: E402
for _p_qp in (_Path_qp(__file__).resolve().parent,
              _Path_qp(__file__).resolve().parent / 'substrate',
              _Path_qp(__file__).resolve().parent.parent / 'computations',
              _Path_qp(__file__).resolve().parent.parent / 'computations' / 'substrate'):
    if str(_p_qp) not in _sys_qp.path:
        _sys_qp.path.insert(0, str(_p_qp))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402


def _default_q0() -> sp.Rational:
    """Return q_0 as an sp.Rational (50-digit precision)."""
    try:
        from q_parameter import Q as Q0_FLOAT  # type: ignore
        return sp.Rational(str(Q0_FLOAT))
    except ImportError:
        # Fallback to the canonical 50-digit pinning. Per
        # `prop:three-calibration-discipline`, q_0 is the H^1
        # calibration; this value is not a fit but the resolution
        # of the lepton-ratio constraint at 50dp.
        return sp.Rational(Q_50_DIGIT_STR)


def expose_polynomial(
    expr: sp.Expr,
    q: sp.Symbol,
    *,
    q0: sp.Rational | None = None,
    digits: int = 50,
    simplify: bool = True,
) -> dict[str, Any]:
    """Produce a {polynomial_q, polynomial_q_latex, value_at_q0}
    triple from a sympy expression symbolic in `q`.

    Parameters
    ----------
    expr : sympy expression in `q`.
    q : the Symbol used (so callers using their own Symbol object
        don't trip over sympy's structural equality).
    q0 : substitution value (default: q_parameter.Q as Rational).
    digits : precision for the numerical evaluation.
    simplify : whether to call sp.simplify on the polynomial form
        before exposure (default True; expensive for large expressions).

    Returns
    -------
    dict with three string fields suitable for direct JSON dump.
    """
    if q0 is None:
        q0 = _default_q0()
    poly = sp.simplify(expr) if simplify else expr
    value = sp.N(expr.subs(q, q0), digits)
    return {
        "polynomial_q": str(poly),
        "polynomial_q_latex": sp.latex(poly),
        "value_at_q0": str(value),
    }


def expose_polynomial_dict(
    exprs: dict[str, sp.Expr],
    q: sp.Symbol,
    *,
    q0: sp.Rational | None = None,
    digits: int = 50,
    simplify: bool = True,
) -> dict[str, dict[str, Any]]:
    """Apply `expose_polynomial` to a dict of named expressions.

    Useful when a witness script computes several quantities; one
    call exposes the full polynomial+numerical pair for each.
    """
    return {
        name: expose_polynomial(expr, q, q0=q0, digits=digits, simplify=simplify)
        for name, expr in exprs.items()
    }


def evaluate_with_polynomial(
    expr: sp.Expr,
    q: sp.Symbol,
    *,
    q0: sp.Rational | None = None,
    digits: int = 30,
    return_type: str = "float",
):
    """Drop-in replacement for `float(expr.subs(q, q0).evalf(digits))`
    that ALSO returns the polynomial form alongside the numerical value.

    Usage:
        # Before:
        h_val = float(h_sym.subs(q, q0).evalf(30))
        # After:
        h_val, h_poly = evaluate_with_polynomial(h_sym, q)
        witness["h_poly"] = h_poly  # add to witness JSON

    `return_type`: "float" | "complex" | "mpf" | "rational" — type of
    the first return value. Second is always the expose_polynomial dict.
    """
    if q0 is None:
        q0 = _default_q0()
    poly = expose_polynomial(expr, q, q0=q0, digits=digits)
    val = sp.N(expr.subs(q, q0), digits)
    if return_type == "float":
        try:
            num = float(val)
        except TypeError:
            num = complex(val)
    elif return_type == "complex":
        num = complex(val)
    elif return_type == "mpf":
        import mpmath
        num = mpmath.mpf(str(val))
    elif return_type == "rational":
        num = sp.Rational(val)
    else:
        raise ValueError(f"Unknown return_type: {return_type}")
    return num, poly
