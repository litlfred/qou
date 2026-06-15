#!/usr/bin/env python3
"""
Character support analysis for per-irrep Garside computation.

Key insight: for 2-letter quark alphabet {u,d}, the Schur-Weyl
decomposition restricts the computation to:

1. Only 2-row partitions λ = (k, n-k) of S_n
2. Only those with k ≥ max(n_u, n_d)  [Kostka number K_{λ,(n_u,n_d)} = 1]
3. The weight-(n_u,n_d) subspace of irrep λ is 1-dimensional

This means:
  - The mass/energy of the specific quark state is a MATRIX ELEMENT,
    not the full trace
  - Each irrep contributes a 1D number: ⟨w_λ|ρ_λ(Δ)|w_λ⟩
  - Computing this requires O(dim) per crossing (sparse action),
    not O(dim²) for full matrix multiplication

For the Q-value:
  Q = |Σ_λ Schur_weight(λ) × [⟨w_λ(par)|Δ|w_λ(par)⟩ - ⟨w_λ(dau)|Δ|w_λ(dau)⟩]|

Usage:
    cd folio-assistant/computations && python3 character-support-qvalues.py
"""

import math
import numpy as np
import sys
import time
from pathlib import Path
from itertools import combinations

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0, HA as h_val, LN_Q
from experimental_constants import M_E_MEV, Q_TRITIUM_MEV, Q_NEUTRON_MEV

z = 1.0 / (q0**0.5 + q0**(-0.5))


# ══════════════════════════════════════════════════════════════
#  KOSTKA NUMBER AND SUPPORT
# ══════════════════════════════════════════════════════════════

def kostka_2row(k, m, n_u, n_d):
    """Kostka number K_{(k,m),(n_u,n_d)} for 2-row partition.

    K = 1 iff we can fill a SSYT of shape (k,m) with n_u 1's and n_d 2's.
    Forced: first m columns have 1 in row 1 and 2 in row 2.
    Remaining k-m boxes in row 1: (n_u - m) 1's then (k - n_u) 2's.
    """
    if k + m != n_u + n_d:
        return 0
    if n_u < m:  # not enough 1's for the forced positions
        return 0
    if k < n_u:  # not enough room in row 1 for all 1's
        return 0
    return 1


def character_support(n, n_u, n_d):
    """Find the 2-row partitions in the support of weight (n_u, n_d).

    Returns: list of (k, m) with K_{(k,m),(n_u,n_d)} = 1.
    """
    assert n_u + n_d == n
    support = []
    for k in range(n, (n-1)//2, -1):
        m = n - k
        if kostka_2row(k, m, n_u, n_d) == 1:
            if m == 0:
                support.append((n,))
            else:
                support.append((k, m))
    return support


def hook_length_dim(partition):
    """Dimension of irrep via hook-length formula."""
    n = sum(partition)
    hooks = []
    for r in range(len(partition)):
        for c in range(partition[r]):
            arm = partition[r] - c - 1
            leg = sum(1 for rr in range(r+1, len(partition)) if partition[rr] > c)
            hooks.append(arm + leg + 1)
    dim = math.factorial(n)
    for hook in hooks:
        dim //= hook
    return dim


# ══════════════════════════════════════════════════════════════
#  YOUNG TABLEAUX AND WEIGHT VECTORS
# ══════════════════════════════════════════════════════════════

def standard_young_tableaux(partition):
    """Generate all standard Young tableaux for a partition."""
    n = sum(partition)
    rows = len(partition)

    def fill(tableau, remaining, row_lengths):
        if not remaining:
            yield [row[:] for row in tableau]
            return
        val = n - len(remaining) + 1
        for r in range(rows):
            if row_lengths[r] < partition[r]:
                if r > 0 and row_lengths[r] >= row_lengths[r-1]:
                    continue
                tableau[r].append(val)
                new_lengths = row_lengths[:]
                new_lengths[r] += 1
                yield from fill(tableau, remaining[1:], new_lengths)
                tableau[r].pop()

    initial = [[] for _ in range(rows)]
    yield from fill(initial, list(range(1, n+1)), [0]*rows)


def content(tableau, val):
    for r, row in enumerate(tableau):
        for c, v in enumerate(row):
            if v == val:
                return c - r
    raise ValueError(f"{val} not in tableau")


def axial_distance(tableau, k):
    return content(tableau, k+1) - content(tableau, k)


def swap_in_tableau(tableau, k):
    new_tab = [row[:] for row in tableau]
    pos_k = pos_k1 = None
    for r, row in enumerate(new_tab):
        for c, v in enumerate(row):
            if v == k: pos_k = (r, c)
            if v == k+1: pos_k1 = (r, c)
    if pos_k is None or pos_k1 is None:
        return None
    new_tab[pos_k[0]][pos_k[1]] = k+1
    new_tab[pos_k1[0]][pos_k1[1]] = k
    for r, row in enumerate(new_tab):
        for c in range(len(row)-1):
            if row[c] >= row[c+1]: return None
        if r > 0:
            for c in range(min(len(new_tab[r]), len(new_tab[r-1]))):
                if new_tab[r][c] <= new_tab[r-1][c]: return None
    return new_tab


def tableau_weight(tableau, n):
    """Weight of a standard tableau: how many values are in row 1 vs row 2.

    For a semistandard tableau of content (n_u, n_d), the values 1..n_u
    go in positions that form a specific weight.

    For standard Young tableaux, the weight is given by which values
    are in which row. Row 1 values → counted as u, row 2 values → d.
    """
    row1_vals = set(tableau[0])
    row2_vals = set(tableau[1]) if len(tableau) > 1 else set()
    return len(row1_vals), len(row2_vals)  # (n_in_row1, n_in_row2)


def find_weight_vector(tableaux, n_u, n_d):
    """Find the weight vector |w_λ⟩ in the weight-(n_u,n_d) subspace.

    The weight vector corresponds to the semistandard Young tableau
    with content (n_u, n_d). In the standard basis, this projects
    onto all standard tableaux that are "compatible" with the weight.

    For a 2-row partition with weight (n_u, n_d):
    - The unique SSYT has 1's in specific positions of row 1 and row 2
    - The standard tableaux that contribute are those where the
      "1-positions" (row 1 up to column n_u) match the weight pattern

    Actually, the weight vector in the Gelfand-Tsetlin basis IS
    a specific standard tableau. For 2-row partitions with 2 letters:

    The weight vector for weight (n_u, n_d) in irrep (k, m) is:
      SSYT: row 1 = [1,1,...,1,2,2,...,2] with n_u-m 1's then k-n_u+m 2's
            row 2 = [1,1,...,1,2,...,2] wait this doesn't work for SYT...

    Actually, the weight vector in the seminormal basis is obtained by
    applying Jucys-Murphy element analysis. For practical purposes:
    - Each standard tableau T determines a weight (|T row1|, |T row2|)
    - The weight vector is the projection onto tableaux with matching weight
    """
    dim = len(tableaux)
    n = n_u + n_d

    # Find which tableaux have the right "descent structure" matching (n_u, n_d)
    # In the weight decomposition, a standard tableau T has weight μ where
    # μ_i = number of values in row i.
    # For 2 rows: weight = (|row 1|, |row 2|) = (k, m) which is the partition
    # shape, not the quark content.
    #
    # The CONTENT weight (not to be confused with "content" c-r) comes from
    # the semistandard tableaux construction. For standard tableaux, we need
    # the projection onto the weight-(n_u,n_d) subspace via raising/lowering
    # operators.
    #
    # Simplified approach: the weight vector is the sum over all standard
    # tableaux T such that the "reading word" of T is compatible with the
    # content (n_u, n_d). For 2-row partitions this is determined by the
    # descent set.

    # For practical computation: compute the Jucys-Murphy decomposition
    # to find the weight vector. But this is complex.
    #
    # SIMPLER: since the weight space is 1-dimensional (K=1), we can use
    # the Garside element's action on ANY vector in the weight space.
    # The weight space is spanned by |w⟩ = projection of the tensor product
    # state |u^{n_u} d^{n_d}⟩ onto the irrep λ.
    #
    # In the seminormal basis, this projection is:
    # |w_λ⟩ = Σ_T c_T |T⟩
    # where c_T is determined by the content of T.
    #
    # For our purposes, just use the first matching tableau as an approximation
    # (since the weight space is 1D, the diagonal element is the same for
    # any normalized vector in that space).

    # Return the index of a "typical" weight vector
    # For now, return all tableaux indices with their weights
    weight_info = []
    for i, T in enumerate(tableaux):
        wt = tableau_weight(T, n)
        weight_info.append((i, wt))

    return weight_info


# ══════════════════════════════════════════════════════════════
#  SEMINORMAL GENERATOR MATRIX (same as before)
# ══════════════════════════════════════════════════════════════

def seminormal_matrix(tableaux, tab_to_idx, gen_idx):
    dim = len(tableaux)
    k = gen_idx + 1
    mat = np.zeros((dim, dim))
    for i, T in enumerate(tableaux):
        d = axial_distance(T, k)
        if d == 0:
            raise ValueError(f"d=0")
        if abs(d) == 1:
            mat[i, i] = q0 if d == 1 else -qi0
        else:
            qd = q0**d
            qdi = q0**(-d)
            diag = h_val / (qd - qdi)
            mat[i, i] = diag
            T_sw = swap_in_tableau(T, k)
            if T_sw is not None:
                key = tuple(tuple(row) for row in T_sw)
                if key in tab_to_idx:
                    j = tab_to_idx[key]
                    off_sq = 1.0 - diag**2
                    mat[i, j] = math.sqrt(abs(off_sq)) * (1 if off_sq >= 0 else -1)
    return mat


def typed_d(fi, fj):
    if fi == 'u' and fj == 'u': return 0.0
    if fi == 'd' and fj == 'd': return -h_val
    return -h_val / 2


# ══════════════════════════════════════════════════════════════
#  MAIN: SUPPORT ANALYSIS
# ══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print("CHARACTER SUPPORT ANALYSIS FOR PER-IRREP Q-VALUES")
    print(f"q₀ = {q0:.10f}, h = {h_val:.10f}")
    print("=" * 80)

    test_cases = [
        ('n (udd)',    3, 1, 2, 'udd'),
        ('p (uud)',    3, 2, 1, 'uud'),
        ('³H (4u5d)',  9, 4, 5, None),
        ('³He (5u4d)', 9, 5, 4, None),
        ('⁶He (8u10d)', 18, 8, 10, None),
        ('⁶Li (9u9d)',  18, 9, 9, None),
    ]

    for name, n, n_u, n_d, quarks in test_cases:
        print(f"\n  {name}: n={n}, weight=({n_u},{n_d})")
        all_2row = []
        for k in range(n, (n-1)//2, -1):
            m = n - k
            part = (n,) if m == 0 else (k, m)
            all_2row.append(part)

        support = character_support(n, n_u, n_d)
        non_support = [p for p in all_2row if p not in support]

        print(f"    Total 2-row partitions: {len(all_2row)}")
        print(f"    In support (K=1): {len(support)}")
        print(f"    Zero (K=0): {len(non_support)}")

        for p in all_2row:
            dim = hook_length_dim(p)
            K = 1 if p in support else 0
            status = "✓ K=1" if K == 1 else "✗ K=0 SKIP"
            print(f"      λ={str(p):>10s}: dim={dim:>6d}, {status}")

        if non_support:
            print(f"    SAVINGS: skip {len(non_support)} irreps "
                  f"(dims: {', '.join(str(hook_length_dim(p)) for p in non_support)})")

    # ══════════════════════════════════════════════════════════════
    #  COMPUTE FULL GARSIDE IN SUPPORTED IRREPS FOR SMALL CASES
    # ══════════════════════════════════════════════════════════════

    print("\n" + "=" * 80)
    print("  FULL GARSIDE TRACE vs DIAGONAL ELEMENT IN SUPPORTED IRREPS")
    print("=" * 80)

    # For n→p (3 quarks), compute both trace and diagonal elements
    for quarks_name, quarks in [('udd (neutron)', list('udd')),
                                  ('uud (proton)', list('uud'))]:
        n = len(quarks)
        n_u = quarks.count('u')
        n_d = quarks.count('d')
        support = character_support(n, n_u, n_d)

        print(f"\n  {quarks_name}: n={n}, ({n_u}u,{n_d}d)")

        for part in support:
            tableaux = list(standard_young_tableaux(part))
            dim = len(tableaux)
            tab_to_idx = {tuple(tuple(row) for row in T): i
                          for i, T in enumerate(tableaux)}

            # Precompute generators
            gen_mats = {}
            for k in range(n - 1):
                gen_mats[k] = seminormal_matrix(tableaux, tab_to_idx, k)

            # Build Garside product
            result = np.eye(dim)
            for L in range(1, n):
                for k in range(L - 1, -1, -1):
                    d_coeff = typed_d(quarks[k], quarks[L])
                    crossing = gen_mats[k] + d_coeff * np.eye(dim)
                    result = result @ crossing

            tr_full = np.trace(result).real

            # Diagonal elements
            diag = np.diag(result).real
            print(f"    λ={str(part):>6s} (dim={dim}):")
            print(f"      tr(ρ(Δ)) = {tr_full:+.6f}")
            for i, T in enumerate(tableaux):
                wt = tableau_weight(T, n)
                print(f"      ⟨T_{i}|Δ|T_{i}⟩ = {diag[i]:+.6f}  "
                      f"(wt=({wt[0]},{wt[1]}), T={T})")

    # ══════════════════════════════════════════════════════════════
    #  KEY INSIGHT: MATRIX ELEMENT vs TRACE
    # ══════════════════════════════════════════════════════════════

    print("\n" + "=" * 80)
    print("  KEY INSIGHT: MATRIX ELEMENT vs FULL TRACE")
    print("=" * 80)
    print("""
  For a nucleus with quark state |v⟩ ∈ (ℂ²)^⊗n, the PHYSICAL quantity is
  the MATRIX ELEMENT ⟨v|ρ(Δ)|v⟩, not the TRACE tr(ρ_λ(Δ)).

  The trace sums over ALL basis states. The matrix element picks out the
  component relevant to the specific quark configuration.

  Computational savings:
    tr(ρ_λ(Δ)):    O(n_crossings × dim²)     [full matrix product]
    ⟨v|ρ_λ(Δ)|v⟩:  O(n_crossings × dim)      [vector action only]

  For ⁶He λ=(11,7) with dim=13260:
    Full matrix:  ~2.7×10¹⁰ operations
    Vector action: ~2×10⁶ operations
    Speedup: 13260×

  But we need the right vector |v⟩ for each quark ordering.
  This requires the Gelfand-Tsetlin basis construction.

  The vector |v_λ⟩ is the projection of the quark tensor product
  state |f_1 ⊗ f_2 ⊗ ... ⊗ f_n⟩ onto the irrep λ. By Schur-Weyl
  duality, this projection is unique (up to phase) when the Kostka
  number K_{λ,μ} = 1 (1-dimensional weight space).
""")
