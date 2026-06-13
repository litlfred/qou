#!/usr/bin/env python3
# polynomial_q_not_applicable: shared symbolic helpers for structural exploration.
"""qbeta_symbolic_utils — shared SYMBOLIC (sympy) helpers for the Q_β heat-route probes.

Single source of truth for the small *symbolic* utilities reused across the
`qbeta_*` structural-exploration probes (root-of-unity residue program,
per-cell / framing ζ₄ sub-probes, period-3/ζ₆ cancellation, higher-a_j carriers,
f-map exploration), so the same closed form is not re-typed (and silently
diverged) in multiple scripts.

This is the SYMBOLIC counterpart to `qbeta_utils.py` (which holds the
mpmath / NUMERIC ladder helpers). All exports use the single shared symbol
`q = sympy.symbols('q')`; probes must import `q` from here (not redeclare it)
so the helpers and the probe operate on the same symbol.

Convention notes (the Hecke content-Casimir tower):
  • [k]_q = (1 - q^k)/(1 - q)         — Jackson bracket (`jackson`)
  • content c of cell (row i, col j) = j - i      (`contents`)
  • Σ_□ [c]_q[c+1]_q                  — content-Casimir sum (`casimir_sum`)
  • μ_λ = ℏ_q² · Σ_□[c][c+1], ℏ_q=(q-1)/q          (`mu`)
  • κ_λ = (q-1)·μ_λ                   — the a_1 = -c_3 building block (`kappa`)
  • bar : q ↦ q⁻¹                     — the fibre involution (`bar`)

STRUCTURAL only; no c_3 value; flip-flop guard respected.
"""
from __future__ import annotations

import sympy as sp

# The single shared symbol. Probes import this (do NOT redeclare `q`).
q = sp.symbols('q')


def jackson(k):
    """Jackson bracket [k]_q = (1-q^k)/(1-q); [0]_q = 0. Valid for negative k
    (returns the Laurent form)."""
    if k == 0:
        return sp.Integer(0)
    return sp.cancel((1 - q ** k) / (1 - q))


def contents(part):
    """Cell contents c = col - row of a partition (row-major order)."""
    return [j - i for i, row in enumerate(part) for j in range(row)]


def partitions(n):
    """Yield every integer partition of `n` as a descending tuple."""
    def rec(rem, mx):
        if rem == 0:
            yield ()
            return
        for f in range(min(rem, mx), 0, -1):
            for r in rec(rem - f, f):
                yield (f,) + r
    yield from rec(n, n)


def per_cell(c):
    """Per-cell content-Casimir factor [c]_q[c+1]_q (one cell of content c)."""
    return sp.cancel(jackson(c) * jackson(c + 1))


def casimir_sum(part):
    """Content-Casimir sum Σ_□ [c]_q[c+1]_q over the cells of `part`
    (the ℏ_q² prefactor stripped)."""
    return sp.expand(sum(jackson(c) * jackson(c + 1) for c in contents(part)))


def mu(part):
    """Content-Casimir eigenvalue μ_λ = ℏ_q² · Σ_□[c][c+1], ℏ_q = (q-1)/q."""
    hbar2 = ((q - 1) / q) ** 2
    return sp.cancel(hbar2 * casimir_sum(part))


def kappa(part):
    """Per-mode rate κ_λ = (q-1)·μ_λ — the bar-parity-bearing a_1 building block."""
    return sp.cancel((q - 1) * mu(part))


def bar(expr):
    """The fibre bar involution q ↦ q⁻¹ applied to `expr` (cancelled)."""
    return sp.cancel(expr.subs(q, 1 / q))


def odd_part(expr):
    """Bar-ODD projection (expr - bar(expr)) / 2."""
    return sp.cancel((expr - bar(expr)) / 2)


def parity(expr):
    """Bar-parity label: 'ODD' if bar(expr) = -expr, 'EVEN' if bar(expr) = expr,
    '0' if expr is zero, '—' otherwise."""
    if sp.cancel(expr) == 0:
        return "0"
    if sp.simplify(bar(expr) + expr) == 0:
        return "ODD"
    if sp.simplify(bar(expr) - expr) == 0:
        return "EVEN"
    return "—"


def cyclotomic_carriers(expr, dmax=12):
    """Which Φ_d(q) (d = 2..dmax) divide numer(expr) — i.e. which roots of
    unity ζ_d the expression carries. Returns the sorted list of such d."""
    if sp.cancel(expr) == 0:
        return []
    num = sp.Poly(sp.numer(sp.cancel(expr)), q)
    out = []
    for d in range(2, dmax + 1):
        if not num.is_zero and num.rem(sp.Poly(sp.cyclotomic_poly(d, q), q)).is_zero:
            out.append(d)
    return out


def divides(phi, expr):
    """Does the (cyclotomic) polynomial `phi` divide numer(expr)?"""
    if sp.cancel(expr) == 0:
        return False
    num = sp.Poly(sp.numer(sp.cancel(expr)), q)
    return num.rem(sp.Poly(phi, q)).is_zero
