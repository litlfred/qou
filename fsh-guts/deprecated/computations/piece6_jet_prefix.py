#!/usr/bin/env python3
# polynomial_q_not_applicable: library / no own witness output; sympy used internally by callers.
"""
Derive PIECE 6 of the unified mass formula: jet-level prefix corrections.

Formula (jet-filtered-knot-factor.md, marked OPEN in status table):

  a_{Z,N} = Π_{k=3}^{3A} a_k(β_k)

  a_k(β_k) = [Σ_{λ⊢k} w_λ · χ_λ(β_k)] / [Σ_{λ⊢k} w_λ · d_λ]

where:
  w_λ = d_q(λ)² / [k]_q!  (Plancherel weights)
  d_λ = classical dim of V_λ (Res^{H_k}_{H_3}(V_λ) dim = d_λ)
  β_k = PREFIX of full atomic braid word at strand-level k, i.e.,
        the sub-sequence of (c, d, gen) factors with gen ≤ k-2.

Algorithm:
  1. Expand atom(Z, N) → full (c, d, gen) braid-word via _step_chain_generic
  2. At each k ∈ {3, 4, ..., 3A}, extract prefix β_k (factors with gen ≤ k-2)
  3. Compute χ_λ(β_k) via Hoefsmit seminormal matrices for each λ ⊢ k
  4. Form a_k ratio and take product

For proton (A=1): only k=3 applies; a = a_3.
For D, T, ³He (A=2,3): product over k=3,...,3A.

Test: do values converge to asymptotic limit (paper conjectures
a → 1 as nucleon count grows)?
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 40
import numpy as np
import sympy as sp

from hecke_core import (_step_chain_generic, _PROTON_G0, _PROTON_G1,
                          _NEUTRON_G0, _NEUTRON_G1, h as H_A)
from hecke_characters import (build_seminormal_matrices, dim_q,
                                 partitions_of, young_hooks)
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP

Q0 = Q_MP  # was f64 roundtrip
QI = Q_INV_MP


def q_int(n):
    return (Q0**n - QI**n) / (Q0 - QI)


def q_fact(n):
    out = mp.mpf(1)
    for k in range(2, n + 1):
        out *= q_int(k)
    return out


def dim_q_mp(shape):
    n = sum(shape); hooks = young_hooks(shape)
    num = q_fact(n)
    den = mp.mpf(1)
    for h_ in hooks:
        den *= q_int(h_)
    return num / den


def classical_dim(shape) -> int:
    nn = sum(shape); hooks = young_hooks(shape)
    f = 1
    for k in range(2, nn + 1): f *= k
    hp = 1
    for x in hooks: hp *= x
    return f // hp


def atom_full_word(Z: int, N: int) -> list:
    """Expand atomic braid into explicit (c, d, gen) sequence."""
    A = Z + N
    n_strands = 3 * A
    n_gens = n_strands - 1
    ordering = ['p'] * Z + ['n'] * N
    full = []
    for k in range(A):
        chain_k = _step_chain_generic(ordering[k], ordering[:k],
                                        n_gens, include_inter=True)
        full.extend(chain_k)
    return full


def prefix_at_k(word: list, k: int) -> list:
    """Prefix of word at jet level k: keep factors with gen ≤ k-2
    (i.e., factors on generators σ_0, ..., σ_{k-2} of B_k)."""
    return [(c, d, g) for (c, d, g) in word if g <= k - 2]


def chi_lambda_on_word(shape, word) -> mp.mpc:
    """Compute χ_λ(β) via Hoefsmit seminormal matrices at q₀."""
    sigmas_sym, dim, _ = build_seminormal_matrices(shape)
    if dim == 0:
        return mp.mpc(0)
    q_sym = sp.Symbol('q')
    sigmas_num = []
    for S in sigmas_sym:
        try:
            fn = sp.lambdify(q_sym, sp.Matrix(S), modules='numpy')
            M = np.asarray(fn(complex(Q0_FLOAT)), dtype=complex)
        except Exception:
            M = np.zeros((dim, dim), dtype=complex)
        sigmas_num.append(M)
    I = np.eye(dim, dtype=complex)
    M = I.copy()
    for (c, d, g) in word:
        if g >= len(sigmas_num):
            return mp.mpc(0)
        F = c * sigmas_num[g] + d * I
        M = M @ F
    return mp.mpc(complex(np.trace(M)))


def a_k(word: list, k: int) -> mp.mpc:
    """Compute a_k = Σ w_λ χ_λ(β_k) / Σ w_λ d_λ at jet level k."""
    if k < 2:
        return mp.mpc(1)
    beta_k = prefix_at_k(word, k)
    nfac = q_fact(k)
    numerator = mp.mpc(0)
    denominator = mp.mpf(0)
    for shape in partitions_of(k):
        dq = dim_q_mp(shape)
        if dq == 0: continue
        d_cl = mp.mpf(classical_dim(shape))
        w = dq * dq / nfac
        chi = chi_lambda_on_word(shape, beta_k)
        numerator += w * chi
        denominator += w * d_cl
    if denominator == 0:
        return mp.mpc(0)
    return numerator / denominator


def piece_6(Z: int, N: int) -> dict:
    """Full piece 6 = Π_{k=3}^{3A} a_k(β_k)."""
    A = Z + N
    n_strands = 3 * A
    word = atom_full_word(Z, N)
    levels = []
    prod = mp.mpc(1)
    for k in range(3, n_strands + 1):
        a = a_k(word, k)
        levels.append({'k': k, 'n_factors_in_prefix': len(prefix_at_k(word, k)),
                        'a_k_re': float(a.real), 'a_k_im': float(a.imag),
                        'a_k_abs': float(mp.fabs(a))})
        prod *= a
    return {
        'Z': Z, 'N': N, 'A': A, 'n_strands': n_strands,
        'n_total_factors': len(word),
        'levels': levels,
        'piece_6_re': float(prod.real),
        'piece_6_im': float(prod.imag),
        'piece_6_abs': float(mp.fabs(prod)),
    }


def main() -> int:
    print("=" * 100)
    print("PIECE 6 DERIVATION — jet-level prefix corrections")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
    print()

    for name, Z, N in [("proton", 1, 0), ("neutron", 0, 1),
                           ("D", 1, 1), ("T", 1, 2), ("³He", 2, 1)]:
        print(f"  {'─' * 80}")
        print(f"  {name} (Z={Z}, N={N})")
        print(f"  {'─' * 80}")
        if 3 * (Z + N) > 11:
            print(f"  skipped (n={3*(Z+N)} > partition table K_MAX=11)")
            continue
        result = piece_6(Z, N)
        print(f"  {'k':<4} {'n_pref':>8} {'a_k':>40}")
        for lev in result['levels']:
            print(f"  {lev['k']:<4} {lev['n_factors_in_prefix']:>8} "
                  f"{lev['a_k_re']:+20.10f}"
                  f"{lev['a_k_im']:+20.10e}j")
        print(f"  total a (product) = {result['piece_6_re']:+.10f}"
              f"{result['piece_6_im']:+.2e}j  "
              f"|product| = {result['piece_6_abs']:.10f}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
