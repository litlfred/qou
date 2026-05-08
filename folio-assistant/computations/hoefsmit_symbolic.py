#!/usr/bin/env python3
"""
hoefsmit_symbolic.py — Thin symbolic-q convenience layer over the
existing Hoefsmit engine in `hecke_character_symbolic`, plus
q-integer / q-factorial / dim_q symbolic helpers and Markov-trace /
pole-order utilities.

History.  An earlier draft of this module duplicated the seminormal
construction.  Per PR #546 review feedback (Copilot), the duplicate
build was removed and `chi_lambda_symbolic` / the matrix builder now
delegate to `hecke_character_symbolic.{hoefsmit_matrices_symbolic,
q_character_on_braid_word}`.  This guarantees a single source of truth
for the seminormal Hoefsmit matrices and the matrix-multiplication
order used to evaluate braid characters.

Hoefsmit conventions (matching the canonical engine):

  For SYT i with k-th and (k+1)-th entries at cells with axial
  contents differing by ρ = c(i+1) - c(i):

    1×1 block (no swap partner):
      σ_k acts as h / (1 − q^{−2ρ}) on SYT i
      (= q for ρ = +1, = −q^{−1} for ρ = −1)

    2×2 block on {i, j} (j = swap partner):
      M[i, i] = a  := h / (1 − q^{−2ρ})
      M[j, j] = a' := h / (1 − q^{2ρ})
      M[i, j] = M[j, i] = b   with   b² = a · a' + 1   (det = −1)

  Braid-word accumulation (canonical):
      M ← M · σ_k          for each crossing, left-to-right.

This convention matches the existing numerical implementation
exactly (verified at q_0 to 1e-6 for all proton-standalone partitions).
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from hecke_characters import standard_young_tableaux, partitions_of  # noqa: E402
from hecke_character_symbolic import (  # noqa: E402
    hoefsmit_matrices_symbolic,
    q_character_on_braid_word,
)

# ──────────────────────────────────────────────────────────────────
# Canonical sympy variable for symbolic q
# ──────────────────────────────────────────────────────────────────
Q = sp.symbols('q', positive=True)
H_SKEIN = Q - 1 / Q


# ──────────────────────────────────────────────────────────────────
# §1  Symbolic q-integer / q-factorial / dim_q
# ──────────────────────────────────────────────────────────────────

def q_int(n: int) -> sp.Expr:
    """[n]_q = (q^n − q^{−n}) / (q − q^{−1}) symbolically."""
    return (Q**n - Q**(-n)) / (Q - Q**(-1))


def q_fac(n: int) -> sp.Expr:
    """[n]_q! = ∏_{k=1..n} [k]_q symbolically."""
    return sp.prod([q_int(k) for k in range(1, n + 1)])


def young_hooks(shape) -> list[int]:
    cells = [(i, j) for i, row in enumerate(shape) for j in range(row)]
    out = []
    for (i, j) in cells:
        arm = shape[i] - j - 1
        leg = sum(1 for r in range(i + 1, len(shape)) if shape[r] > j)
        out.append(arm + leg + 1)
    return out


def dim_q(shape) -> sp.Expr:
    """q-dimension of irrep V_λ via hook formula, symbolic in q."""
    n = sum(shape)
    return sp.cancel(q_fac(n) / sp.prod([q_int(h) for h in young_hooks(shape)]))


# ──────────────────────────────────────────────────────────────────
# §2  Hoefsmit seminormal matrices + braid character (delegating)
# ──────────────────────────────────────────────────────────────────

def build_seminormal_matrices_symbolic(shape):
    """Symbolic σ_1, …, σ_{n−1} matrices for shape = λ.

    Thin wrapper around `hecke_character_symbolic.hoefsmit_matrices_symbolic`
    that pins the q-symbol to this module's canonical `Q`.  Returns
    `(matrices, dim)` (the canonical engine returns a 3-tuple including
    the SYT list; we drop it here for backward compatibility with the
    earlier signature in this module).
    """
    matrices, dim, _syts = hoefsmit_matrices_symbolic(tuple(shape), Q)
    return matrices, dim


def chi_lambda_symbolic(shape, crossings) -> sp.Expr:
    """Symbolic χ^λ(β) for braid word β = list of (k_gen, ctype).

    Delegates to `hecke_character_symbolic.q_character_on_braid_word`,
    which uses the canonical `M ← M · σ_k` accumulation order.

    crossings: list of (k_gen, ctype) where
      ctype ∈ {'sigma', 'sigma_inv', 'averaged'}.
    """
    return q_character_on_braid_word(tuple(shape), crossings, Q)


def tr_M_symbolic(crossings, n: int) -> sp.Expr:
    """Symbolic Markov trace tr_M(β) = Σ_λ w_λ · χ^λ(β) / f^λ
    where w_λ = dim_q(λ)² / [n]_q! and f^λ = #SYT(λ).
    """
    qfac_n = q_fac(n)
    total = sp.Integer(0)
    for shape in partitions_of(n):
        chi = chi_lambda_symbolic(tuple(shape), crossings)
        # standard_young_tableaux returns a 3-tuple (syts, cells, contents);
        # take element 0 to get the actual SYT list.
        syts, _, _ = standard_young_tableaux(list(shape))
        f_lam = len(syts)
        if f_lam == 0:
            continue
        d_q = dim_q(list(shape))
        w_lam = d_q * d_q / qfac_n
        total = total + sp.cancel(w_lam * chi / f_lam)
    return sp.cancel(total)


def pole_order_at_zero(expr: sp.Expr) -> tuple[int, sp.Expr]:
    """Return (pole_order, leading_coefficient) of `expr` at q=0.

    A "pole order k" means the lowest q-power in expr is q^{-k}.
    The leading coefficient is the coefficient of q^{-k} (i.e.,
    lim_{q→0} expr · q^k).
    """
    expr_c = sp.cancel(expr)
    if expr_c.is_zero:
        return 0, sp.Integer(0)
    num, den = sp.fraction(expr_c)
    num_p = sp.Poly(sp.expand(num), Q)
    den_p = sp.Poly(sp.expand(den), Q)
    num_low = min((m[0] for m in num_p.monoms()), default=0)
    den_low = min((m[0] for m in den_p.monoms()), default=0)
    lowest = num_low - den_low
    pole_order = -lowest if lowest < 0 else 0
    leading = sp.cancel(sp.limit(expr_c * Q**pole_order, Q, 0))
    return pole_order, leading


__all__ = [
    "Q",
    "H_SKEIN",
    "q_int",
    "q_fac",
    "dim_q",
    "build_seminormal_matrices_symbolic",
    "chi_lambda_symbolic",
    "tr_M_symbolic",
    "pole_order_at_zero",
]


if __name__ == "__main__":
    # Self-test: cross-validate symbolic vs numerical at q_0 for proton.
    import numpy as np
    from hecke_characters import build_seminormal_matrices
    from canonical_braid_crossings import atom_canonical_crossings as atomic_braid_to_crossings
    from q_parameter import Q as q_num

    proton = atomic_braid_to_crossings(1, 0, include_inter=False)
    print("Cross-validation: symbolic vs numerical χ^λ(proton) at q_0")
    print("-" * 70)
    for shape in [(3,), (2, 1), (1, 1, 1)]:
        chi_s = chi_lambda_symbolic(shape, proton)
        sym_at_q0 = float(sp.N(chi_s.subs(Q, q_num), 30))
        sigmas_num, dim_num, _ = build_seminormal_matrices(tuple(shape))
        M = np.eye(dim_num, dtype=complex)
        h_num = q_num - 1.0 / q_num
        for k_gen, ctype in proton:
            s_i = sigmas_num[k_gen]
            if ctype == 'sigma':
                step = s_i
            elif ctype == 'sigma_inv':
                step = s_i - h_num * np.eye(dim_num)
            elif ctype == 'averaged':
                step = s_i - (h_num / 2) * np.eye(dim_num)
            M = M @ step
        num = float(np.real(np.trace(M)))
        match = "✓" if abs(sym_at_q0 - num) < 1e-6 else "✗"
        print(f"  λ={str(shape):<10} sym={sym_at_q0:>+12.6f}  num={num:>+12.6f}  {match}")

    # Closed-form proton tr_M
    trM = tr_M_symbolic(proton, 3)
    pole, leading = pole_order_at_zero(trM)
    print()
    print(f"tr_M(proton) symbolic = {trM}")
    print(f"  pole order at q=0 = {pole}")
    print(f"  leading coefficient = {leading}")
