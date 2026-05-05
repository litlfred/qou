#!/usr/bin/env python3
"""
hoefsmit_symbolic.py — Reusable symbolic-q seminormal-Hoefsmit
representation matrices for the Iwahori–Hecke algebra H_n(q),
plus q-integer / q-factorial / dim_q symbolic helpers.

Replaces the buggy 2×2 block construction in
ocneanu_cancellation_derivation.py (PR #544 audit) with the
correct Hoefsmit formulas — calibrated by direct cross-validation
against the existing numerical build_seminormal_matrices in
hecke_characters.py.

Hoefsmit formulas (symbolic in sympy q):

  For SYT i with k-th and (k+1)-th entries at cells with axial
  contents differing by ρ = c(i+1) - c(i):

    1×1 block (no swap partner):
      σ_k acts as h / (1 − q^{−2ρ}) on SYT i
      (= q for ρ = +1, = −q^{−1} for ρ = −1)

    2×2 block on {i, j} (j = swap partner):
      M[i, i] = a  := h / (1 − q^{−2ρ})
      M[j, j] = a' := h / (1 − q^{2ρ})    (= a evaluated at -ρ)
      M[i, j] = M[j, i] = b
      where b² = a · a' + 1   (constraint: det = −1)

This convention matches the existing numerical implementation
exactly (verified at q_0 to 1e-6 for all proton-standalone partitions).

The symbolic version yields exact closed-form characters:

  χ^(3)(proton)       = q^5/4 + q^3/2 + q/4
  χ^(2,1)(proton)     = (q^22 + q^20 + q^18 + q^14 − q^8 − q^4 − q^2 − 1) / (4 q^11)
  χ^(1,1,1)(proton)   = −(q^4 + 2 q^2 + 1) / (4 q^5)

  tr_M(proton)        = (q^20 + q^18 + 2 q^12 − 2 q^8 − q^2 − 1) / (12 q^10)

with pole order EXACTLY 10 at q=0 and leading coefficient −1/12.
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from hecke_characters import standard_young_tableaux, partitions_of  # noqa: E402

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
    return sp.simplify(q_fac(n) / sp.prod([q_int(h) for h in young_hooks(shape)]))


# ──────────────────────────────────────────────────────────────────
# §2  Hoefsmit seminormal-basis representation, symbolic in q
# ──────────────────────────────────────────────────────────────────

def build_seminormal_matrices_symbolic(shape):
    """Build symbolic σ_1, …, σ_{n−1} matrices in V_λ for shape = λ.

    Uses the canonical Hoefsmit formulas:
      a  = h / (1 − q^{−2ρ})   (diagonal at SYT i with axial diff ρ)
      a' = h / (1 − q^{2ρ})    (diagonal at swap partner j)
      b  = sqrt(a·a' + 1)      (off-diagonal, satisfying det = −1)

    Returns (matrices, dim) where matrices[k] = σ_{k+1}.
    """
    syts, cells, contents = standard_young_tableaux(shape)
    dim = len(syts)
    if dim == 0:
        return [], 0

    n = sum(shape)
    matrices = []
    for k in range(1, n):  # σ_k swaps entries k and k+1 in SYT
        M = sp.zeros(dim, dim)
        processed = set()
        for i in range(dim):
            if i in processed:
                continue
            ci_k = syts[i][k]
            ci_k1 = syts[i][k + 1]
            rho = contents[ci_k1] - contents[ci_k]
            a = H_SKEIN / (1 - Q**(-2 * rho))

            swap_map = dict(syts[i])
            swap_map[k] = ci_k1
            swap_map[k + 1] = ci_k
            j = None
            for jj in range(dim):
                if jj == i:
                    continue
                if syts[jj] == swap_map:
                    j = jj
                    break

            if j is None:
                # 1×1 block (eigenvalue +q for ρ=+1, −q^{−1} for ρ=−1)
                M[i, i] = a
                processed.add(i)
            else:
                # 2×2 block on {i, j}
                a_prime = H_SKEIN / (1 - Q**(2 * rho))
                b = sp.sqrt(a * a_prime + 1)
                M[i, i] = a
                M[j, j] = a_prime
                M[i, j] = b
                M[j, i] = b
                processed.add(i)
                processed.add(j)
        matrices.append(M)
    return matrices, dim


def chi_lambda_symbolic(shape, crossings) -> sp.Expr:
    """Symbolic χ^λ(β) for braid word β = list of (k_gen, ctype).

    crossings: list of (k_gen, ctype) where
      ctype ∈ {'sigma', 'sigma_inv', 'averaged'}
    matching the convention in hecke_character_symbolic.atomic_braid_to_crossings.
    """
    sigmas, dim = build_seminormal_matrices_symbolic(shape)
    if dim == 0:
        return sp.Integer(0)
    M = sp.eye(dim)
    Id = sp.eye(dim)
    for k_gen, ctype in crossings:
        s_k = sigmas[k_gen]
        if ctype == 'sigma':
            step = s_k
        elif ctype == 'sigma_inv':
            step = s_k - H_SKEIN * Id
        elif ctype == 'averaged':
            step = s_k - (H_SKEIN / 2) * Id
        else:
            raise ValueError(f"unknown crossing type {ctype}")
        M = step * M
    return sp.cancel(M.trace())


def tr_M_symbolic(crossings, n: int) -> sp.Expr:
    """Symbolic Markov trace tr_M(β) = Σ_λ w_λ · χ^λ(β) / f^λ
    where w_λ = dim_q(λ)² / [n]_q! and f^λ = #SYT(λ).
    """
    qfac_n = q_fac(n)
    total = sp.Integer(0)
    for shape in partitions_of(n):
        chi = chi_lambda_symbolic(tuple(shape), crossings)
        f_lam = len(standard_young_tableaux(list(shape)))
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
    leading = sp.simplify(sp.limit(expr_c * Q**pole_order, Q, 0))
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
    from hecke_character_symbolic import atomic_braid_to_crossings
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
            M = step @ M
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
