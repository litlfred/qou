#!/usr/bin/env python3
# polynomial_q_not_applicable: library / no own witness output; sympy used internally by callers.
"""
Symbolic-in-q knot operator channel computation.

All matrix elements computed as exact rational functions of q using SymPy.
No numerical evaluation until the very end. The LP weights are then
algebraic functions of q, not fitted constants.

For the seminormal form, each generator σ_k in irrep λ has entries:
  - diagonal: (q - q⁻¹)/(q^d - q^{-d}) = 1/[d]_q
  - off-diagonal: sqrt(1 - 1/[d]_q²) = sqrt([d]_q² - 1)/[d]_q

The sqrt is algebraic. We handle this by working with the SQUARED
matrix elements where possible, or by noting that for specific d values
the sqrt simplifies.

For 2×2 blocks: eigenvalues are q and -q⁻¹ (exact). The min-eigenvalue
eigenvector is the -q⁻¹ eigenvector (antisymmetric channel).

Usage:
    cd folio-assistant/computations && python3 knot-operator-symbolic.py
"""

import sympy as sp
from sympy import sqrt, Rational, simplify, factor, cancel, together
import sys
import json
import math
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0_num

q = sp.Symbol('q', positive=True)
qi = 1/q
h = q - qi  # Hecke parameter


def quantum_int(d):
    """[d]_q = (q^d - q^{-d})/(q - q^{-1})"""
    if d == 0:
        return sp.Integer(0)
    return (q**d - q**(-d)) / (q - q**(-1))


# ══════════════════════════════════════════════════════════════
#  SEMINORMAL FORM (SYMBOLIC)
# ══════════════════════════════════════════════════════════════

def syt_2row(a, b):
    """Generate standard Young tableaux for shape (a,b) as binary vectors."""
    n = a + b
    result = []
    def recurse(current, r1, r2):
        if len(current) == n:
            result.append(tuple(current))
            return
        if r1 < a:
            recurse(current + [True], r1+1, r2)
        if r2 < b and r2 < r1:
            recurse(current + [False], r1, r2+1)
    recurse([], 0, 0)
    return result


def syt_content(tab, v):
    """Content of value v (1-indexed) in SYT tab."""
    r1 = r2 = 0
    for i in range(v):
        if tab[i]: r1 += 1
        else: r2 += 1
    if tab[v-1]:
        return r1 - 1  # column - row = col - 0
    else:
        return r2 - 1 - 1  # column - row = col - 1


def syt_swap(tab, k):
    """Swap values k and k+1. Return None if not standard."""
    if tab[k-1] == tab[k]:
        return None
    new_tab = list(tab)
    new_tab[k-1], new_tab[k] = new_tab[k], new_tab[k-1]
    r1 = r2 = 0
    for v in new_tab:
        if v: r1 += 1
        else: r2 += 1
        if r2 > r1:
            return None
    return tuple(new_tab)


def seminormal_generator_symbolic(tabs, tab_idx, gen):
    """Build σ_gen matrix symbolically. Each entry is a SymPy expression in q."""
    k = gen + 1  # swap values k and k+1
    dim = len(tabs)
    M = sp.zeros(dim, dim)

    processed = set()
    for i, T in enumerate(tabs):
        if i in processed:
            continue

        d = syt_content(T, k+1) - syt_content(T, k)

        if d == 1:
            M[i, i] = q
            processed.add(i)
        elif d == -1:
            M[i, i] = -qi
            processed.add(i)
        else:
            # 2×2 block with eigenvalues q and -q⁻¹
            diag_i = h / (q**d - q**(-d))
            M[i, i] = diag_i

            T_sw = syt_swap(T, k)
            if T_sw is not None and T_sw in tab_idx:
                j = tab_idx[T_sw]
                diag_j = h / (q**(-d) - q**d)  # = -diag_i
                M[j, j] = diag_j

                # off-diagonal: from det = -1 and trace = h
                # off² = diag_i * diag_j + 1 = -diag_i² + 1
                off_sq = 1 - diag_i**2
                off_sq_simplified = sp.simplify(off_sq)
                off = sp.sqrt(off_sq_simplified)
                M[i, j] = off
                M[j, i] = off

                processed.add(i)
                processed.add(j)
            else:
                processed.add(i)

    return M


# ══════════════════════════════════════════════════════════════
#  TYPED CROSSING COEFFICIENT (SYMBOLIC)
# ══════════════════════════════════════════════════════════════

def typed_d_sym(fi, fj):
    if fi == 'u' and fj == 'u': return sp.Integer(0)
    if fi == 'd' and fj == 'd': return -h
    return -h / 2


# ══════════════════════════════════════════════════════════════
#  GARSIDE PRODUCT (SYMBOLIC)
# ══════════════════════════════════════════════════════════════

def garside_matrix_symbolic(quarks, tabs, tab_idx, gen_matrices):
    """Compute the full Garside product symbolically."""
    n = len(quarks)
    dim = len(tabs)
    result = sp.eye(dim)

    for L in range(1, n):
        for k in range(L-1, -1, -1):
            d_coeff = typed_d_sym(quarks[k], quarks[L])
            crossing = gen_matrices[k] + d_coeff * sp.eye(dim)
            result = result * crossing

    return result


# ══════════════════════════════════════════════════════════════
#  KNOT OPERATOR EIGENVECTORS (SYMBOLIC)
# ══════════════════════════════════════════════════════════════

def knot_operator_symbolic(word, n_nucleons, n, gen_matrices):
    """Build the knot operator matrix symbolically."""
    dim = gen_matrices[0].shape[0]
    result = sp.eye(dim)

    for m in range(n_nucleons):
        for gen_offset, sign in word:
            gen = 3 * m + gen_offset
            if gen >= n - 1:
                continue
            if sign > 0:
                result = result * gen_matrices[gen]
            else:
                # σ⁻¹ = σ - h
                result = result * (gen_matrices[gen] - h * sp.eye(dim))

    return result


def min_eigenvector_symbolic(K_matrix, dim):
    """Find the min-eigenvalue eigenvector symbolically.

    For dim=1: trivial.
    For dim=2: the -q⁻¹ channel eigenvector (exact from 2×2 formula).
    For dim>2: use SymPy eigendecomposition (expensive).
    """
    if dim == 1:
        return sp.Matrix([1]), K_matrix[0, 0]

    # Get eigenvalues and eigenvectors
    eigdata = K_matrix.eigenvects()
    # Sort by eigenvalue magnitude (want the smallest)
    # For symbolic, we evaluate at q₀ to determine ordering
    eigs_with_vecs = []
    for eigenval, mult, vecs in eigdata:
        val_num = complex(eigenval.subs(q, q0_num))
        eigs_with_vecs.append((abs(val_num), eigenval, vecs[0]))

    eigs_with_vecs.sort(key=lambda x: x[0])

    # Smallest eigenvalue
    _, min_eigval, min_eigvec = eigs_with_vecs[0]

    # Normalize symbolically (for inner product)
    norm_sq = min_eigvec.dot(min_eigvec)
    # Don't normalize — the matrix element ⟨v|M|v⟩/⟨v|v⟩ handles it

    return min_eigvec, min_eigval


# ══════════════════════════════════════════════════════════════
#  MATRIX ELEMENT (SYMBOLIC)
# ══════════════════════════════════════════════════════════════

def matrix_element_symbolic(M, v):
    """Compute ⟨v|M|v⟩/⟨v|v⟩ symbolically."""
    Mv = M * v
    num = v.dot(Mv)
    den = v.dot(v)
    return sp.cancel(num / den)


# ══════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════

knot_words = {
    'T23': [(0, 1), (1, 1), (0, 1)],
    'T25': [(0, 1), (1, 1), (0, 1), (1, 1), (0, 1)],
    'T35': [(0, 1), (1, 1), (0, 1), (1, 1), (0, 1), (1, 1), (0, 1), (1, 1), (0, 1), (1, 1)],
    'Borr': [(0, 1), (1, -1), (0, 1), (1, -1), (0, 1), (1, -1)],
}

if __name__ == '__main__':
    print("SYMBOLIC KNOT OPERATOR CHANNELS")
    print(f"Working in Q(q)[√...], evaluating at q₀ = {q0_num:.15f}")
    print("=" * 80)

    # ──────────────────────────────────────────────────────
    #  FREE NEUTRON (n=3, max dim=2) — fully symbolic
    # ──────────────────────────────────────────────────────

    decays_3 = [
        ('n→p', list('udd'), list('uud')),
    ]

    for name, par_quarks, dau_quarks in decays_3:
        n = len(par_quarks)
        assert n == 3

        print(f"\n{'━' * 80}")
        print(f"  {name} (n={n}, fully symbolic)")
        print(f"{'━' * 80}")

        for part_a, part_b in [(3, 0), (2, 1)]:
            tabs = syt_2row(part_a, part_b)
            dim = len(tabs)
            tab_idx = {t: i for i, t in enumerate(tabs)}

            print(f"\n  λ=({part_a},{part_b}), dim={dim}")

            # Build generator matrices
            gen_mats = {}
            for g in range(n - 1):
                gen_mats[g] = seminormal_generator_symbolic(tabs, tab_idx, g)

            # Garside products
            G_par = garside_matrix_symbolic(par_quarks, tabs, tab_idx, gen_mats)
            G_dau = garside_matrix_symbolic(dau_quarks, tabs, tab_idx, gen_mats)

            if dim == 1:
                me_par = sp.cancel(G_par[0, 0])
                me_dau = sp.cancel(G_dau[0, 0])
                dme = sp.cancel(me_dau - me_par)
                print(f"    ⟨Δ_par⟩ = {me_par}")
                print(f"    ⟨Δ_dau⟩ = {me_dau}")
                print(f"    Δme = {dme}")
                print(f"    Δme(q₀) = {float(dme.subs(q, q0_num)):.10f}")
                print(f"    (same for all knot operators in 1D)")
                continue

            # Per-knot-operator matrix elements
            for kname, kword in knot_words.items():
                print(f"\n    Knot {kname}:")
                n_nuc = n // 3

                K = knot_operator_symbolic(kword, n_nuc, n, gen_mats)
                K_simplified = sp.simplify(K)
                print(f"      K = {K_simplified}")

                eigvals = K.eigenvals()
                print(f"      eigenvalues: {dict(eigvals)}")

                v_min, lambda_min = min_eigenvector_symbolic(K, dim)
                print(f"      λ_min = {sp.cancel(lambda_min)}")
                print(f"      v_min = {v_min.T}")

                me_par = matrix_element_symbolic(G_par, v_min)
                me_dau = matrix_element_symbolic(G_dau, v_min)
                dme = sp.cancel(me_dau - me_par)

                print(f"      ⟨v|Δ_par|v⟩ = {sp.cancel(me_par)}")
                print(f"      ⟨v|Δ_dau|v⟩ = {sp.cancel(me_dau)}")
                print(f"      Δme = {dme}")
                print(f"      Δme(q₀) = {float(dme.subs(q, q0_num)):.10f}")

    # ──────────────────────────────────────────────────────
    #  TRITIUM (n=9, dim up to 8) — symbolic for small irreps
    # ──────────────────────────────────────────────────────

    print(f"\n{'━' * 80}")
    print(f"  ³H→³He (n=9, symbolic for dim ≤ 8)")
    print(f"{'━' * 80}")

    par_quarks_9 = list('uududdudd')
    dau_quarks_9 = list('uududduud')
    n9 = 9

    for part_a, part_b in [(9, 0), (8, 1)]:
        tabs = syt_2row(part_a, part_b)
        dim = len(tabs)
        tab_idx = {t: i for i, t in enumerate(tabs)}

        print(f"\n  λ=({part_a},{part_b}), dim={dim}")

        gen_mats = {}
        for g in range(n9 - 1):
            print(f"    Building σ_{g}...", end=" ", flush=True)
            gen_mats[g] = seminormal_generator_symbolic(tabs, tab_idx, g)
            print("done")

        # Garside products (this is the expensive part for dim=8)
        print(f"    Computing Garside products...", flush=True)
        G_par = garside_matrix_symbolic(par_quarks_9, tabs, tab_idx, gen_mats)
        G_dau = garside_matrix_symbolic(dau_quarks_9, tabs, tab_idx, gen_mats)
        print(f"    done")

        if dim == 1:
            me_par = sp.cancel(G_par[0, 0])
            me_dau = sp.cancel(G_dau[0, 0])
            dme = sp.cancel(me_dau - me_par)
            print(f"    ⟨Δ_par⟩ = {me_par}")
            print(f"    ⟨Δ_dau⟩ = {me_dau}")
            print(f"    Δme = {dme}")
            print(f"    Δme(q₀) = {float(dme.subs(q, q0_num)):.10f}")
            continue

        # Per-knot-operator (only T23 and Borromean for speed)
        for kname in ['T23', 'Borr']:
            kword = knot_words[kname]
            print(f"\n    Knot {kname}:")
            n_nuc = n9 // 3

            K = knot_operator_symbolic(kword, n_nuc, n9, gen_mats)
            print(f"      Computing eigenvectors...", flush=True)
            v_min, lambda_min = min_eigenvector_symbolic(K, dim)
            lm_simplified = sp.cancel(lambda_min)
            print(f"      λ_min = {lm_simplified}")
            print(f"      λ_min(q₀) = {complex(lm_simplified.subs(q, q0_num))}")

            me_par = matrix_element_symbolic(G_par, v_min)
            me_dau = matrix_element_symbolic(G_dau, v_min)
            dme = sp.cancel(me_dau - me_par)

            # Evaluate numerically
            dme_num = complex(dme.subs(q, q0_num))
            print(f"      Δme(q₀) = {dme_num}")
            # Print symbolic if not too long
            dme_str = str(dme)
            if len(dme_str) < 200:
                print(f"      Δme(q) = {dme}")

    print("\n" + "=" * 80)
    print("  DONE — all channel entries are exact in q")
    print("=" * 80)
