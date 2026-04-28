"""Closed-form Alexander polynomials of torus links and knots.

Conventions
-----------
* Variable: a single SymPy symbol ``q`` (the substrate parameter).
* Normalisation: the *symmetric* Alexander polynomial, defined only
  up to a unit ``± q^k``.  The closed-form expressions below use the
  normalisation in which they are Laurent polynomials symmetric under
  ``q ↔ q⁻¹``.

Torus link / knot $T(2,N)$
--------------------------
* For **even** $N = 2m$ (a 2-component link):
  $$\\Delta_{T(2,2m)}(q) = \\frac{q^m - q^{-m}}{q - q^{-1}}
                          = q^{m-1} + q^{m-3} + \\cdots + q^{-(m-1)}.$$
* For **odd** $N = 2m+1$ (a knot):
  $$\\Delta_{T(2,2m+1)}(q)
        = \\frac{q^{2m+1} + q^{-(2m+1)}}{q + q^{-1}}.$$

Self-consistency
----------------
:func:`closed_form_consistency` verifies the defining identity
``Δ · (q - q⁻¹) == q^m - q^{-m}`` (even N) and the analogous
``Δ · (q + q⁻¹) == q^N + q^{-N}`` (odd N).

A reduced-Burau generator :func:`reduced_burau_generator` is also
provided for callers that want to build $(\\sigma_1 \\cdots
\\sigma_{N-1})^2$ symbolically; the resulting determinant differs
from :func:`alexander_T2N_closed` by a unit and is left to the caller
to normalise.

@module folio-assistant/computations/lib/alexander
"""

from __future__ import annotations

from typing import Iterable

import sympy as sp


# ── Canonical symbol ─────────────────────────────────────────────

q = sp.symbols("q", positive=True)


# ── Closed-form torus-link Alexander polynomials ─────────────────

def alexander_T2N_closed(N: int, var: sp.Expr | None = None) -> sp.Expr:
    """Return $\\Delta_{T(2,N)}$ in closed form.

    Parameters
    ----------
    N : int
        Second torus parameter ($N \\ge 1$).
    var : sympy expression, optional
        Variable to substitute for ``q``.  Defaults to the module symbol.
    """
    if N < 1:
        raise ValueError("N must be a positive integer")
    x = q if var is None else var
    if N % 2 == 0:
        m = N // 2
        # Symmetric Laurent form.
        expr = sum(x**(m - 1 - 2 * k) for k in range(m))
    else:
        # Torus knot T(2, 2m+1):  Δ = (q^N + q^{-N}) / (q + q^{-1}).
        expr = (x**N + x**(-N)) / (x + x**(-1))
    return sp.simplify(sp.expand(expr))


def alexander_T2N_at(N: int, q_val) -> sp.Expr:
    """Numerical/symbolic evaluation of $\\Delta_{T(2,N)}(q_\\text{val})$."""
    return sp.nsimplify(alexander_T2N_closed(N).subs(q, q_val))


# ── Burau representation cross-check ─────────────────────────────

def reduced_burau_generator(i: int, n: int, var: sp.Expr | None = None) -> sp.Matrix:
    """Reduced Burau image of $\\sigma_i \\in B_n$ as an $(n-1) \\times (n-1)$
    matrix.

    Uses the standard formula in variable ``t`` (we use ``q`` here):
      * $1 \\le i \\le n-1$;
      * Identity blocks above and below the $2\\times 2$ block at row/col $i$.
    """
    if not (1 <= i <= n - 1):
        raise ValueError("i must satisfy 1 ≤ i ≤ n-1")
    t = q if var is None else var
    size = n - 1
    M = sp.eye(size)
    j = i - 1  # 0-indexed
    if i == 1:
        M[0, 0] = -t
        if size >= 2:
            M[0, 1] = 1
    elif i == n - 1:
        M[size - 1, size - 2] = t
        M[size - 1, size - 1] = -t
    else:
        M[j, j - 1] = t
        M[j, j] = -t
        M[j, j + 1] = 1
    return M


# ── Alternative-form self-consistency check ──────────────────────

def closed_form_consistency(N: int) -> bool:
    """Verify the defining identity for the closed form.

    For even ``N = 2m``::

        Δ_{T(2,N)}(q) · (q − q⁻¹)  ==  q^m − q^{-m}.

    For odd ``N = 2m+1``::

        Δ_{T(2,N)}(q) · (q + q⁻¹)  ==  q^N + q^{-N}.
    """
    expr = alexander_T2N_closed(N)
    if N % 2 == 0:
        m = N // 2
        rhs = q**m - q**(-m)
        lhs = expr * (q - 1 / q)
    else:
        rhs = q**N + q**(-N)
        lhs = expr * (q + 1 / q)
    return sp.simplify(sp.expand(lhs - rhs)) == 0


# ── Symmetric-form normalisation helper ──────────────────────────

def normalise_symmetric(expr: sp.Expr, var: sp.Expr | None = None) -> sp.Expr:
    """Return ``expr`` divided by the unique unit ±q^k that makes it
    symmetric under $q \\leftrightarrow q^{-1}$ with positive leading
    coefficient.

    Works with Laurent polynomials by extracting the coefficient list
    via the highest negative power.
    """
    t = q if var is None else var
    e = sp.expand(sp.simplify(expr))
    # Convert to Laurent polynomial in t by multiplying by t^K for large K.
    K = 200
    poly_pos = sp.Poly(sp.expand(e * t**K), t)
    coeffs = poly_pos.all_coeffs()  # high-degree first
    deg = len(coeffs) - 1  # highest power present (after shift)
    # Find lowest nonzero index (lowest power)
    high = next((i for i, c in enumerate(coeffs) if c != 0), deg)
    low = next((i for i, c in enumerate(reversed(coeffs)) if c != 0), 0)
    high_pow = deg - high  # degree of the highest term
    low_pow = low          # degree of the lowest term (counted from 0 upward)
    centre = (high_pow + low_pow) // 2
    shift = centre - K  # net shift back relative to original expression
    candidate = sp.expand(e * t**shift)
    # Make leading coefficient positive (look at the centre coefficient).
    # Re-extract with the new shift.
    poly2 = sp.Poly(sp.expand(candidate * t**K), t)
    cs = poly2.all_coeffs()
    nonzero = [c for c in cs if c != 0]
    if nonzero and nonzero[0] < 0:
        candidate = -candidate
    return sp.simplify(candidate)


# ── Alexander weight (symbolic limit |q| → 1) ────────────────────

def alexander_weight_at_unit(N: int) -> sp.Expr:
    """Limit of $\\Delta_{T(2,N)}(q)$ as ``q → 1``."""
    return sp.limit(alexander_T2N_closed(N), q, 1)


def alexander_half_weight_ratio(N: int) -> sp.Expr:
    """Limit of $\\Delta_{T(2,N)}(q)/N$ as ``q → 1``.

    For even ``N`` this equals $1/2$; for odd ``N`` it equals $1/N$.
    """
    return sp.limit(alexander_T2N_closed(N) / N, q, 1)


# ── Convenience tabulator ────────────────────────────────────────

def tabulate(Ns: Iterable[int]) -> list[dict]:
    """Return a list of ``{N, Δ(q), Δ(1), Δ(1)/N, parity, components}``."""
    rows = []
    for N in Ns:
        expr = alexander_T2N_closed(N)
        rows.append({
            "N": N,
            "alexander": str(expr),
            "alexander_at_1": str(alexander_weight_at_unit(N)),
            "weight_per_atom": str(alexander_half_weight_ratio(N)),
            "parity": "even" if N % 2 == 0 else "odd",
            "components": 2 if N % 2 == 0 else 1,
        })
    return rows


__all__ = [
    "q",
    "alexander_T2N_closed",
    "alexander_T2N_at",
    "reduced_burau_generator",
    "normalise_symmetric",
    "alexander_weight_at_unit",
    "alexander_half_weight_ratio",
    "closed_form_consistency",
    "tabulate",
]
