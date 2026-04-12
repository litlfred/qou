#!/usr/bin/env python3
"""
Per-irrep Garside computation via Young's seminormal form.

Instead of building the full NF in H_n(q) (which grows exponentially),
compute Δ_A's matrix in each irrep separately.

For irrep λ ⊢ n with dimension d_λ:
  - Each generator σ_i acts as a d_λ × d_λ matrix (Young's seminormal form)
  - The typed crossing C(f_i, f_j; σ_k) = σ_k + d(f_i, f_j) acts as
    ρ_λ(σ_k) + d(f_i, f_j) × I_{d_λ}
  - The Garside element Δ_A = product of all crossings acts as
    product of these matrices

The Pauli data is extracted from the matrix traces:
  tr_alt = Σ_λ (-1)^{|λ'|} × tr(ρ_λ(Δ_A))  (weighted by sign character)
  net = Σ_λ d_λ × tr(ρ_λ(Δ_A)) / |S_n|
  tr_M = Σ_λ (z^n / s_λ) × tr(ρ_λ(Δ_A))

Actually simpler: just compute tr(ρ_λ(Δ_A)) for each λ.
The full Pauli function combines these.

Usage:
    python3 irrep-garside.py
"""
import sys
import numpy as np
from pathlib import Path
from itertools import combinations
import time

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0, HA as h

z = 1.0 / (q0**0.5 + q0**(-0.5))


# ══════════════════════════════════════════════════════════════
#  YOUNG'S SEMINORMAL FORM FOR H_n(q)
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
                # Check: val must be larger than all in this row (automatic by construction)
                # and larger than the element above (if exists)
                if r > 0 and row_lengths[r] >= row_lengths[r-1]:
                    continue
                # Also: columns must be increasing downward
                # The element at position (r, row_lengths[r]) must be > element at (r-1, row_lengths[r])
                # But since we fill left-to-right, top-to-bottom, this is satisfied if
                # we only place in row r when row_lengths[r] < row_lengths[r-1] (for r > 0)
                # Actually the condition above handles this.

                tableau[r].append(val)
                new_remaining = remaining[1:]
                new_lengths = row_lengths[:]
                new_lengths[r] += 1
                yield from fill(tableau, new_remaining, new_lengths)
                tableau[r].pop()

    initial = [[] for _ in range(rows)]
    yield from fill(initial, list(range(1, n+1)), [0]*rows)


def content(tableau, val):
    """Content of box containing val: column - row (0-indexed)."""
    for r, row in enumerate(tableau):
        for c, v in enumerate(row):
            if v == val:
                return c - r
    raise ValueError(f"{val} not in tableau")


def axial_distance(tableau, k):
    """Axial distance for transposition (k, k+1) in tableau T.
    d = content(T, k+1) - content(T, k)."""
    return content(tableau, k+1) - content(tableau, k)


def swap_in_tableau(tableau, k):
    """Return tableau with k and k+1 swapped, or None if not standard."""
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
    # Check if still standard
    for r, row in enumerate(new_tab):
        for c in range(len(row)-1):
            if row[c] >= row[c+1]: return None
        if r > 0:
            for c in range(min(len(new_tab[r]), len(new_tab[r-1]))):
                if new_tab[r][c] <= new_tab[r-1][c]: return None
    return new_tab


def young_seminormal_matrix(partition, gen_idx, q_val):
    """Matrix of σ_{gen_idx} in the seminormal form for partition λ.

    gen_idx is 0-based: σ_0 transposes positions 1 and 2.

    In Young's seminormal form, σ_i acts on basis {T_1, ..., T_d}
    (standard Young tableaux) as:
      σ_i |T⟩ = (q^{1/d_T(i)} - q^{-1/d_T(i)})^{-1} × (
          (q - q^{-1}) / (q^{d_T(i)} - q^{-d_T(i)}) |T⟩ + stuff × |T'⟩
      )
    where d_T(i) = content(T, i+2) - content(T, i+1) is the axial distance.

    Simplified: for the Hecke algebra with σ² = (q-q⁻¹)σ + 1,
    the seminormal matrix of σ_i has:
      diagonal entry (T,T): [d]_q⁻¹ × (q - q⁻¹)
      off-diagonal (T,T'): coefficient involving q^{±1/d}

    Actually, the standard result for H_n(q) seminormal form:
    σ_k acts on standard tableaux via the transposition (k+1, k+2):

      σ_k |T⟩ = (q^d - q^{-d})⁻¹ × (q - q⁻¹) |T⟩  if k+1, k+2 NOT in same row/col
              + sqrt(1 - ((q-q⁻¹)/(q^d - q^{-d}))²) |T'⟩

    where d = axial_distance(T, k+1) and T' is T with k+1, k+2 swapped.

    For |d| = 1 (same row or column): σ_k |T⟩ = q |T⟩ (same row) or -q⁻¹ |T⟩ (same column).
    """
    n = sum(partition)
    tableaux = list(standard_young_tableaux(partition))
    dim = len(tableaux)
    tab_to_idx = {}
    for i, t in enumerate(tableaux):
        key = tuple(tuple(row) for row in t)
        tab_to_idx[key] = i

    k = gen_idx + 1  # k+1 and k+2 are the transposed values (1-indexed)
    mat = np.zeros((dim, dim), dtype=complex)

    qq = q_val
    qi = 1.0 / qq
    ha = qq - qi

    for i, T in enumerate(tableaux):
        d = axial_distance(T, k)  # content(k+1) - content(k)

        if d == 0:
            raise ValueError(f"d=0 for tableau {T}, k={k}")

        if abs(d) == 1:
            # k and k+1 in same row (d=1) or same column (d=-1)
            if d == 1:
                mat[i, i] = qq  # same row → eigenvalue q
            else:
                mat[i, i] = -qi  # same column → eigenvalue -q⁻¹
        else:
            # General case
            qd = qq**d
            qdi = qq**(-d)
            denom = qd - qdi
            diag = ha / denom  # (q - q⁻¹) / (q^d - q^{-d})

            mat[i, i] = diag

            # Off-diagonal: T' = swap k, k+1 in T
            T_swapped = swap_in_tableau(T, k)
            if T_swapped is not None:
                key = tuple(tuple(row) for row in T_swapped)
                if key in tab_to_idx:
                    j = tab_to_idx[key]
                    # Off-diagonal coefficient
                    off_diag = np.sqrt(complex(1.0 - diag**2))
                    mat[i, j] = off_diag

    return mat, tableaux


def typed_d(fi, fj):
    """Crossing coefficient for quark flavors."""
    if fi == 'u' and fj == 'u': return 0.0
    elif fi == 'd' and fj == 'd': return -h
    else: return -h/2


# ══════════════════════════════════════════════════════════════
#  GARSIDE ELEMENT Δ_A IN EACH IRREP
# ══════════════════════════════════════════════════════════════

def garside_irrep(partition, quark_ordering, q_val):
    """Compute Δ_A in irrep λ as a d_λ × d_λ matrix.

    The Garside staircase (right-to-left sweep) builds Δ_A as
    product of typed crossings. Each crossing acts as:
      ρ_λ(σ_k) + d(f_i, f_j) × I

    Returns the matrix and its trace.
    """
    n = sum(partition)
    assert n == len(quark_ordering)

    # Get seminormal matrices for each generator
    gen_matrices = {}
    for k in range(n - 1):
        mat, tableaux = young_seminormal_matrix(partition, k, q_val)
        gen_matrices[k] = mat

    dim = gen_matrices[0].shape[0]
    result = np.eye(dim, dtype=complex)

    # Garside staircase: right-to-left sweep
    for level in range(n - 1):
        for sweep in range(level, -1, -1):
            d_coeff = typed_d(quark_ordering[sweep], quark_ordering[level + 1])
            crossing_mat = gen_matrices[sweep] + d_coeff * np.eye(dim)
            result = result @ crossing_mat

    return result, np.trace(result)


# ══════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print("PER-IRREP GARSIDE COMPUTATION")
    print(f"q₀ = {q0:.15f}")
    print("="*70)

    # Test on proton (n=3, partitions of 3)
    partitions_3 = [(3,), (2,1), (1,1,1)]

    print("\n=== Proton B₃ (uud, n=3) ===")
    quark_p = ['u', 'u', 'd']

    total_tr = 0.0
    for part in partitions_3:
        try:
            mat, tr = garside_irrep(part, quark_p, q0)
            dim = mat.shape[0]
            print(f"  λ={part}: dim={dim}, tr(Δ₃) = {tr:.8f}")
            total_tr += tr
        except Exception as e:
            print(f"  λ={part}: ERROR: {e}")

    print(f"  Σ tr = {total_tr:.8f}")

    print("\n=== Neutron B₃ (udd, n=3) ===")
    quark_n = ['u', 'd', 'd']

    total_tr = 0.0
    for part in partitions_3:
        try:
            mat, tr = garside_irrep(part, quark_n, q0)
            dim = mat.shape[0]
            print(f"  λ={part}: dim={dim}, tr(Δ₃) = {tr:.8f}")
            total_tr += tr
        except Exception as e:
            print(f"  λ={part}: ERROR: {e}")

    print(f"  Σ tr = {total_tr:.8f}")

    # Compare with full NF Pauli data
    # Proton: tr_alt = -0.9108, net = 0.7800 (from witness)
    # The Wedderburn trace should reconstruct these.
    print("\n=== Verification vs full NF ===")
    print("  Proton full NF: tr_alt=-0.9108, net=0.7800, F=1.168")
    print("  Neutron full NF: tr_alt=-1.1221, net=0.5905, F=1.900")
