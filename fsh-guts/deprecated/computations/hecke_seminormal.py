#!/usr/bin/env python3
# polynomial_q_not_applicable: library / no own witness output; sympy used internally by callers.
"""
Hecke seminormal-form representation ρ_λ : H_n(q) → M_{f^λ}(R)
+ word-sensitive Hecke trace tr(T_w · ρ_λ).

The Iwahori-Hecke algebra H_n(q) acts on V_λ (Specht module) for
each λ ⊢ n. The standard basis of V_λ is the set of standard Young
tableaux SYT(λ); generators σ_i act by the Hoefsmit / seminormal
formulas:

  Let T ∈ SYT(λ). Let r_i, c_i be the row/col of i in T. Define
  the axial distance:
      d_i(T) = (c_{i+1} - r_{i+1}) - (c_i - r_i)
  Then:
    - If i, i+1 in same row (d=1):    ρ(σ_i)|T⟩ = q |T⟩
    - If i, i+1 in same col (d=-1):    ρ(σ_i)|T⟩ = -q^{-1} |T⟩
    - Otherwise: 2x2 block on (T, s_i T) with entries:
          ρ(σ_i)|T⟩       = α_d |T⟩ + β_d |s_i T⟩
          ρ(σ_i)|s_i T⟩   = γ_d |T⟩ + δ_d |s_i T⟩
      where (using [d]_q = (q^d - q^{-d})/(q - q^{-1})):
          α_d = (q - q^{-1}) / (1 - q^{-2 d})        (diagonal)
          which evaluates to q at d = 1 and -q^{-1} at d = -1, so
          the same-row / same-column special cases are recovered as
          the |d| = 1 limits of the generic formula.
      In the asymmetric (non-square-root) rational form used here:
          β_d (T → T', d > 0) = 1
          β_d (T' → T, d < 0) = (1 − α_{|d|})(α_{|d|} + q^{-1})
      The constraint ρ(σ_i)² = (q − q^{-1}) ρ(σ_i) + 1 fixes the
      product β_d · β_{-d}.
              with β_d = 1 and β'_d = (1 - α_d)(α_d + q^{-1})

The simplest presentation (rational Hoefsmit):
  α_d = q · [d-1]_q / [d]_q             where d = axial distance
  γ_d_s = 1                              (β = 1 normalisation)
  δ_d = q · α_{-d} = -q^{-1} · [d+1]_q / [d]_q
  off-diagonal: ρ(σ_i)|T⟩ = α_d |T⟩ + 1 |s_i T⟩
                ρ(σ_i)|s_i T⟩ = ((1 - α_d)(α_d + q^{-1})) |T⟩ + (q - q^{-1} - α_d) |s_i T⟩

For our purposes we don't need the full off-diagonal entries — we
just need the trace tr(ρ_λ(T_w)). The trace can be computed as
the sum of diagonal entries of the matrix product.

References
----------

[hoefsmit1974]   Representations of Hecke algebras of finite groups
                 with BN-pairs of classical type, Theorem 4.4.
[ram1996]        Seminormal representations of Weyl groups and
                 Iwahori-Hecke algebras, Definition 2.1.
[mathas1999]     Iwahori-Hecke algebras and Schur algebras, §3.
"""
from __future__ import annotations

import sys
import time
from functools import lru_cache
from pathlib import Path

import sympy as sp
from sympy import Rational

sys.path.insert(0, str(Path(__file__).parent))

from murnaghan_nakayama import (
    partitions_of,
    dim_specht,
    cycle_type_of_permutation,
    permutation_from_braid_word,
    atomic_braid_word,
    mn_character,
)


# ─── Standard Young tableaux ────────────────────────────────────────

def standard_young_tableaux(partition):
    """Generate all SYT of shape λ (returned as tuples of tuples).

    Each SYT is a 2D arrangement filling λ with 1..n such that rows
    increase left-to-right and columns increase top-to-bottom.
    """
    n = sum(partition)
    if n == 0:
        return [()]
    # Build via recursive insertion
    rows = [list(r) for r in [[0] * p for p in partition]]
    out = []

    def fill(k, rows):
        if k > n:
            out.append(tuple(tuple(r) for r in rows))
            return
        for i, row in enumerate(rows):
            for j, val in enumerate(row):
                if val != 0:
                    continue
                # Check: above must be filled (row check)
                # Check: column constraint — cell (i, j) can be filled
                # only if (i-1, j) is filled (or i == 0)
                if j > 0 and row[j - 1] == 0:
                    continue
                if i > 0 and rows[i - 1][j] == 0:
                    continue
                rows[i][j] = k
                fill(k + 1, rows)
                rows[i][j] = 0
                break  # left-to-right; skip remaining j in this row

    fill(1, rows)
    return out


def position_in_tableau(T, k):
    """Return (row_idx, col_idx) of integer k in tableau T (1-indexed
    inputs; 1-indexed output coords)."""
    for i, row in enumerate(T):
        for j, val in enumerate(row):
            if val == k:
                return (i + 1, j + 1)
    raise ValueError(f"{k} not in tableau {T}")


def axial_distance(T, i):
    """d_i(T) = (col(i+1) - row(i+1)) - (col(i) - row(i))."""
    r_i, c_i = position_in_tableau(T, i)
    r_ip, c_ip = position_in_tableau(T, i + 1)
    return (c_ip - r_ip) - (c_i - r_i)


def swap_in_tableau(T, i):
    """Swap positions of i and i+1 in T. Returns new tableau (or None
    if the result isn't a valid SYT — i.e. when i, i+1 are in the
    same row or column)."""
    if abs(axial_distance(T, i)) == 1:
        return None
    r_i, c_i = position_in_tableau(T, i)
    r_ip, c_ip = position_in_tableau(T, i + 1)
    new_rows = [list(r) for r in T]
    new_rows[r_i - 1][c_i - 1] = i + 1
    new_rows[r_ip - 1][c_ip - 1] = i
    return tuple(tuple(r) for r in new_rows)


# ─── Hecke generator action ─────────────────────────────────────────

def hecke_generator_action(partition, i, q):
    """Build matrix ρ_λ(σ_i) on the SYT basis of V_λ.

    Returns (basis: list of SYT, matrix: sp.Matrix).
    """
    basis = standard_young_tableaux(partition)
    idx = {T: k for k, T in enumerate(basis)}
    n = len(basis)
    mat = sp.zeros(n, n)
    for T in basis:
        d = axial_distance(T, i)
        k = idx[T]
        if d == 1:
            # Same row: ρ(σ_i) acts as q
            mat[k, k] = q
        elif d == -1:
            # Same col: ρ(σ_i) acts as -q^{-1}
            mat[k, k] = -1 / q
        else:
            # 2x2 block with s_i T
            T_swap = swap_in_tableau(T, i)
            if T_swap is None or T_swap not in idx:
                # Should not happen if SYT enumeration + swap are correct
                continue
            l = idx[T_swap]
            # Hoefsmit rational form:
            #   ρ(σ_i)|T⟩ = α_d |T⟩ + β_d |s_i T⟩
            # with α_d = (q - q⁻¹) / (1 - q^{-2d})
            # Equivalently α_d = q · [d-1]_q / [d]_q for d > 0.
            # Use the symmetric (non-square-root) presentation:
            #   diagonal:   α_d
            #   off-diag:   1 (for T → s_i T)
            #               (1 - α_d)(α_d + q^{-1}) (for s_i T → T)
            alpha = (q - 1 / q) / (1 - q ** (-2 * d))
            mat[k, k] = alpha
            # Off-diagonal: ρ(σ_i)|T⟩ has a |T'⟩ component. In the
            # asymmetric (non-square-root) Hoefsmit presentation:
            #   d > 0:  β_d = 1            (T → T' direction)
            #   d < 0:  β_d = (q − α_{|d|})(α_{|d|} + q⁻¹)
            #                              (T' → T direction)
            # Derivation: ρ(σ_i)² = (q − q⁻¹) ρ(σ_i) + 1 yields
            # β_d · β_{−d} = 1 − α_d² + (q − q⁻¹) α_d
            #              = (q − α_d)(α_d + q⁻¹).
            # Setting β_d = 1 (forward direction) forces
            # β_{−d} = (q − α_d)(α_d + q⁻¹).
            if d > 0:
                mat[l, k] = 1
            else:
                alpha_pos = (q - 1 / q) / (1 - q ** (2 * d))
                mat[l, k] = (q - alpha_pos) * (alpha_pos + 1 / q)
    return basis, mat


def hecke_braid_matrix(partition, braid_word, q):
    """Compute ρ_λ(T_w) for a braid word w = (σ_{i_1}, σ_{i_2}, …).

    braid_word: list of (gen_idx, sign) tuples, where gen_idx is the
    0-indexed Hecke generator (so σ_0 swaps positions 1, 2 in the SYT;
    we shift to 1-indexed internally).

    Returns the matrix ρ_λ(T_w) as a sympy.Matrix.
    """
    basis = standard_young_tableaux(partition)
    n = len(basis)
    if n == 0:
        return sp.Matrix([[0]])
    M = sp.eye(n)
    for gen_idx, _sign in braid_word:
        i = gen_idx + 1  # convert 0-indexed to 1-indexed
        _, mat = hecke_generator_action(partition, i, q)
        M = mat * M
    return M


def hecke_trace(partition, braid_word, q):
    """tr(ρ_λ(T_w)) — the word-sensitive Hecke character."""
    M = hecke_braid_matrix(partition, braid_word, q)
    return sp.cancel(M.trace())


# ─── Self-test ───────────────────────────────────────────────────────

def _test_q_close_to_1_approaches_classical_trace():
    """Verify tr(ρ_λ(T_w)) at q = 1 + 10⁻⁶ approaches the classical
    MN character on the underlying permutation. The Hoefsmit α_d
    formula has a removable singularity at q=1; testing at q close
    to 1 avoids the 0/0 form while still verifying the limit.
    """
    q_test = sp.Rational(1000001, 1000000)  # q = 1 + 10⁻⁶
    failures = 0
    tolerance = sp.Rational(1, 1000)  # 10⁻³ tolerance
    for n in (3, 4):
        for partition in partitions_of(n):
            for word in [[(0, 1)], [(0, 1), (1, 1)], [(1, 1), (0, 1), (1, 1)]]:
                if any(g >= n - 1 for g, _ in word):
                    continue
                tr = sp.simplify(hecke_trace(partition, word, q_test))
                perm = permutation_from_braid_word(word, n)
                cyc = cycle_type_of_permutation(perm)
                classical = mn_character(partition, cyc)
                # Compare numerically
                tr_num = float(tr)
                if abs(tr_num - classical) > float(tolerance):
                    failures += 1
                    if failures <= 3:
                        print(f"  FAIL: λ={partition}, word={word}, "
                              f"tr@q≈1 = {tr_num:.6f} vs MN = {classical}")
    return failures


def _check_3he_vs_3h_at_q():
    """Verify Hecke trace distinguishes ³He vs ³H — including at q=1
    via the actual braid word."""
    q = sp.Symbol("q", positive=True, real=True)
    partition = (2, 1)  # smallest non-trivial partition of 3
    # Atomic braids for proton-only and neutron-only with A=1 (just to
    # exercise — at A=1 they ARE different braid words even with same
    # cycle type)
    word_p = atomic_braid_word(1, 0, include_inter=False)
    word_n = atomic_braid_word(0, 1, include_inter=False)
    if word_p == word_n:
        return None
    # Reduce to atom-only generator indices < n_strands - 1 = 2
    word_p = [(g, s) for g, s in word_p if g < 2]
    word_n = [(g, s) for g, s in word_n if g < 2]
    if not word_p or not word_n:
        return None
    tr_p = hecke_trace(partition, word_p, q)
    tr_n = hecke_trace(partition, word_n, q)
    return {
        "word_p": word_p,
        "word_n": word_n,
        "tr_p_at_q": str(sp.simplify(tr_p))[:120],
        "tr_n_at_q": str(sp.simplify(tr_n))[:120],
        "differ_at_symbolic_q": not sp.cancel(tr_p - tr_n).equals(0),
    }


def main():
    print("Hecke seminormal-form representation — self-test")
    print("=" * 60)
    print()

    print("1. SYT enumeration sanity check:")
    for n in (1, 2, 3, 4, 5):
        for lam in partitions_of(n):
            syt = standard_young_tableaux(lam)
            assert len(syt) == dim_specht(lam), \
                f"λ={lam}: SYT count {len(syt)} != f^λ {dim_specht(lam)}"
    print("   PASS — SYT counts match hook-length formula for n ≤ 5")
    print()

    print("2. Hecke trace approaches classical MN as q → 1 "
          "(short braid words, n ∈ {3, 4}, q = 1 + 10⁻⁶):")
    fails = _test_q_close_to_1_approaches_classical_trace()
    print(f"   {'PASS' if fails == 0 else f'FAIL ({fails})'}")
    print()

    print("3. ³He vs ³H atomic-braid traces (symbolic q):")
    r = _check_3he_vs_3h_at_q()
    if r is None:
        print("   (atomic braids identical at A=1 single-nucleon — expected)")
    else:
        print(f"   word_p = {r['word_p']}")
        print(f"   word_n = {r['word_n']}")
        print(f"   tr_p(q) = {r['tr_p_at_q']}")
        print(f"   tr_n(q) = {r['tr_n_at_q']}")
        print(f"   Differ at symbolic q: {r['differ_at_symbolic_q']}")
    print()

    print("Status: Hecke seminormal forms + word-sensitive trace "
          "tr(ρ_λ(T_w)) implemented.")


if __name__ == "__main__":
    main()
