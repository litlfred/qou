#!/usr/bin/env python3
"""From-scratch Hoefsmit seminormal matrix construction for H_n(q).

For partition λ ⊢ n, irrep V_λ has dimension d_λ (= number of SYTs of
shape λ). The Hoefsmit / seminormal basis is indexed by SYTs T_1, ...,
T_{d_λ}.

For each generator σ_i (i = 1, ..., n-1), the seminormal matrix
σ_i^λ ∈ Mat_{d_λ}(ℚ(q)) is determined by the SYT axial distances:

  Let a(T, i) := axial distance from box-(i+1) to box-i in T,
                = (col(i+1) - col(i)) - (row(i+1) - row(i)).

  Case (i, i+1 in same row of T): σ_i T = q · T (i.e. diag = q)
  Case (i, i+1 in same column of T): σ_i T = -q⁻¹ · T (diag = -q⁻¹)
  Case (different row, different column):
    σ_i T = α(T,i) · T + β(T,i) · s_i T
    where s_i T is T with i and i+1 swapped (still an SYT iff |a| ≥ 2),
    α(T, i) = (q - q⁻¹) / (1 - q^{-2 a(T,i)})
    β(T, i)·β(s_i T, i) determined by σ_i² = (q-q⁻¹) σ_i + 1.

NO dependencies on existing folio-assistant infrastructure.
"""
from __future__ import annotations
import sympy as sp
from typing import List, Tuple

q = sp.Symbol('q', positive=True, real=True)


def partitions_of(n: int) -> List[Tuple[int, ...]]:
    """Generate all partitions of n in dominance order (largest part first)."""
    if n == 0:
        return [()]
    out = []
    def gen(remaining, max_part, current):
        if remaining == 0:
            out.append(tuple(current))
            return
        for p in range(min(remaining, max_part), 0, -1):
            gen(remaining - p, p, current + [p])
    gen(n, n, [])
    return out


def syts_of_shape(lam: Tuple[int, ...]) -> List[List[List[int]]]:
    """Generate all standard Young tableaux of shape λ.

    SYT = filling of λ-shape with 1..n, increasing along rows and columns.
    Returns list of tableaux as list-of-rows.
    """
    n = sum(lam)
    if n == 0:
        return [[]]
    # Recursive: place n in the last possible cell (a corner of λ)
    out = []
    def gen(shape, used, fill_idx):
        if fill_idx == n + 1:
            # Convert filling dict to row-list
            rows = [[None]*r for r in lam]
            for (r, c), v in used.items():
                rows[r][c] = v
            out.append(rows)
            return
        # Find all cells (r, c) where (r-1, c) and (r, c-1) are filled (or boundary)
        for r in range(len(lam)):
            for c in range(lam[r]):
                if (r, c) in used:
                    continue
                if r > 0 and (r-1, c) not in used:
                    continue
                if c > 0 and (r, c-1) not in used:
                    continue
                used[(r, c)] = fill_idx
                gen(shape, used, fill_idx + 1)
                del used[(r, c)]
    gen(lam, {}, 1)
    return out


def position_of(syt, val) -> Tuple[int, int]:
    """Return (row, col) of value `val` in SYT (0-indexed)."""
    for r, row in enumerate(syt):
        for c, v in enumerate(row):
            if v == val:
                return (r, c)
    raise ValueError(f"{val} not in SYT")


def swap_i_iplus1(syt, i):
    """Swap entries i and i+1 in the SYT; return new SYT (or None if invalid)."""
    pos_i = position_of(syt, i)
    pos_ip1 = position_of(syt, i + 1)
    new_syt = [row[:] for row in syt]
    new_syt[pos_i[0]][pos_i[1]] = i + 1
    new_syt[pos_ip1[0]][pos_ip1[1]] = i
    # Verify still an SYT (rows + cols increasing)
    for r, row in enumerate(new_syt):
        for c in range(len(row) - 1):
            if row[c] >= row[c+1]:
                return None
    for c in range(max(len(row) for row in new_syt)):
        for r in range(len(new_syt) - 1):
            if c < len(new_syt[r]) and c < len(new_syt[r+1]):
                if new_syt[r][c] >= new_syt[r+1][c]:
                    return None
    return new_syt


def axial_distance(syt, i):
    """a(T, i) = (col(i+1) - col(i)) - (row(i+1) - row(i)) in T."""
    r_i, c_i = position_of(syt, i)
    r_ip1, c_ip1 = position_of(syt, i + 1)
    return (c_ip1 - c_i) - (r_ip1 - r_i)


def hoefsmit_sigma_matrix(lam: Tuple[int, ...], i: int) -> sp.Matrix:
    """Build the Hoefsmit seminormal matrix for σ_i in irrep λ ⊢ n.

    For each pair (T, s_i T) of swap-related SYTs:
      diag(T) = α(T, i) = (q - q⁻¹) / (1 - q^{-2 a(T, i)})
      off-diagonal: b·c = d_T · d_{sT} + 1   (from σ_i² = h σ_i + 1)
      Symmetric choice b = c = √(d_T · d_{sT} + 1).
    """
    syts = syts_of_shape(lam)
    d = len(syts)
    M = sp.zeros(d, d)
    for j, T in enumerate(syts):
        a = axial_distance(T, i)
        if a == 1:
            # i, i+1 in same row → diag = q
            M[j, j] = q
        elif a == -1:
            # i, i+1 in same column → diag = -1/q
            M[j, j] = -1/q
        else:
            # |a| ≥ 2: split between T and s_i T
            alpha = (q - 1/q) / (1 - q**(-2*a))
            M[j, j] = alpha
            sT = swap_i_iplus1(T, i)
            if sT is not None:
                # find sT in syts
                k = next((kk for kk, T2 in enumerate(syts) if T2 == sT), None)
                if k is not None:
                    a_sT = axial_distance(sT, i)
                    alpha_sT = (q - 1/q) / (1 - q**(-2*a_sT))
                    # Correct formula: bc = d_T · d_{sT} + 1
                    # (derived from σ_i² = (q-q⁻¹)σ_i + 1)
                    off_prod = sp.simplify(alpha * alpha_sT + 1)
                    # Symmetric choice b = c = sqrt(off_prod)
                    M[j, k] = sp.sqrt(off_prod)
    return M


def chi_lambda_braid(lam: Tuple[int, ...], braid_word: list) -> sp.Expr:
    """χ_λ(T_w) = trace of the seminormal matrix product over braid_word.

    braid_word: list of signed integers; positive i means σ_i, negative -i
                means σ_i⁻¹ = σ_i - h.
    """
    n = sum(lam)
    if n == 0:
        return sp.Integer(1)
    # Cache σ_i^λ matrices
    n_gens = max(abs(g) for g in braid_word) if braid_word else 1
    sigmas = {i: hoefsmit_sigma_matrix(lam, i) for i in range(1, n_gens + 1)}
    h_val = q - 1/q
    d = sigmas[1].shape[0]
    M = sp.eye(d)
    for g in braid_word:
        if g > 0:
            M = M @ sigmas[g]
        else:
            M = M @ (sigmas[-g] - h_val * sp.eye(d))
    return sp.simplify(M.trace())


def chi_lambda_braid_numeric(lam: Tuple[int, ...], braid_word: list,
                              q_value) -> float:
    """Numerical χ_λ(T_w) at q = q_value.

    Substitutes q→q_value INTO the Hoefsmit matrices before multiplying.
    Much faster than the symbolic chi_lambda_braid for n ≥ 5.
    """
    import numpy as np
    n = sum(lam)
    if n == 0:
        return 1.0
    n_gens = max(abs(g) for g in braid_word) if braid_word else 1
    h_val = float((q - 1/q).subs(q, q_value).evalf(30))
    d = len(syts_of_shape(lam))
    sigmas_num = {}
    for i in range(1, n_gens + 1):
        S = hoefsmit_sigma_matrix(lam, i)
        sigmas_num[i] = np.array([
            [float(S[r, c].subs(q, q_value).evalf(30))
             for c in range(d)]
            for r in range(d)
        ])
    I = np.eye(d)
    M = np.eye(d)
    for g in braid_word:
        if g > 0:
            M = M @ sigmas_num[g]
        else:
            M = M @ (sigmas_num[-g] - h_val * I)
    return float(M.trace())


# ─── Verification: H_3 standard rep matches the closed form in
# wedderburn_markov.py ─────────────────────────────────────────────────
if __name__ == "__main__":
    print("Verification: Hoefsmit matrices for H_3 (2,1) standard rep")
    print()
    lam = (2, 1)
    s1 = hoefsmit_sigma_matrix(lam, 1)
    s2 = hoefsmit_sigma_matrix(lam, 2)
    print(f"σ_1 in λ={lam}:")
    sp.pretty_print(sp.simplify(s1))
    print()
    print(f"σ_2 in λ={lam}:")
    sp.pretty_print(sp.simplify(s2))
    print()
    print(f"Verify σ_1² = h σ_1 + 1:")
    h_val = q - 1/q
    lhs = sp.simplify(s1 @ s1)
    rhs = sp.simplify(h_val * s1 + sp.eye(2))
    print(f"  σ_1² - (h σ_1 + 1) = ")
    sp.pretty_print(sp.simplify(lhs - rhs))
    print()
    print(f"Verify braid σ_1 σ_2 σ_1 = σ_2 σ_1 σ_2:")
    lhs = sp.simplify(s1 @ s2 @ s1)
    rhs = sp.simplify(s2 @ s1 @ s2)
    print(f"  diff = ")
    sp.pretty_print(sp.simplify(lhs - rhs))
    print()
    print(f"All H_3 partitions:")
    for p in partitions_of(3):
        d = len(syts_of_shape(p))
        print(f"  λ={p}: dim = {d}")
    print()
    print(f"All H_5 partitions:")
    for p in partitions_of(5):
        d = len(syts_of_shape(p))
        print(f"  λ={p}: dim = {d}")
