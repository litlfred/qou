#!/usr/bin/env python3
"""magnus_germ_underdetermination_probe.py — is the germ a canonical full-tower object? NO —
the differentiated-Hecke relation underdetermines it (qou-o6ov).

The germ A = q·(∂σ)·σ⁻¹ satisfies {σ, σ'} = h'σ + h·σ'  (h = q−q⁻¹, h' = 1+q⁻²), obtained by
differentiating the Hecke relation σ² = hσ + 1. In σ's eigenbasis (eigenvalues q, −q⁻¹) this
Sylvester equation reads, per matrix entry (i,j):
    (λ_i + λ_j − h)·σ'_{ij} = h'·λ_i·δ_{ij}.
DIAGONAL (i=j): 2λ_i − h = λ_i + q⁻¹ ≠ 0, so σ'_{ii} = h'λ_i/(2λ_i − h) is FIXED.
OFF-DIAGONAL (i≠j): λ_q + λ_₋ = q − q⁻¹ = h, so the coefficient VANISHES and σ'_{ij} is FREE.

⇒ the germ's σ-eigenbasis diagonal is constraint-fixed but its off-diagonal is representation-
dependent. So the germ is NOT a canonical full-tower object; different realizations (seminormal
vs R-matrix) fill the free off-diagonal differently — the exact mechanism behind the 6.5%
two-row R-matrix mismatch (#6432).

This probe VERIFIES: on a genuine 2×2 σ block, the seminormal germ and the 2-dim R-matrix germ
(1) have the SAME σ-eigenbasis DIAGONAL, matching the closed form h'λ/(2λ−h), but (2) DIFFER in
the off-diagonal. scope-(a); NO-FLOAT64 (mpf). No fit, no witness, nothing wired.
"""
from __future__ import annotations

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))

import mpmath as mp  # noqa: E402
import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from magnus_two_row_rmatrix_probe import r_matrix, germ_4x4  # noqa: E402


def in_eigenbasis(A2, sigma2):
    """Express the 2×2 germ A2 in the eigenbasis of the 2×2 σ block sigma2."""
    E, V = mp.eig(sigma2)                       # sigma2 = V diag(E) V⁻¹
    Vi = V ** -1
    return Vi * A2 * V, E


def seminormal_2x2_block():
    """Extract a GENUINE 2×2 seminormal σ block + its germ: σ_1 on (2,1) (σ_0 there is
    diagonal — a degenerate case that would falsely show a zero off-diagonal)."""
    shape = (2, 1)
    per_gen, dim = base.block_structure(shape)   # dim 2
    q = base.Q0
    sig = base.sigma_csr(per_gen, dim, q)
    germ_rows, hcheck = base.germ_csr(per_gen, dim, q, base.EPS)
    assert hcheck < mp.mpf(10) ** -55
    S = base._dense_from_csr(sig[1], dim)        # gen 1 = genuine 2×2 block
    A = base._dense_from_csr(germ_rows[1], dim)
    assert abs(S[0, 1]) + abs(S[1, 0]) > mp.mpf("0.1"), "not a genuine 2×2 block"
    return S, A


def main():
    q = base.Q0
    h = q - 1 / q
    hp = 1 + 1 / q ** 2
    print(f"[germ] q₀={mp.nstr(q,8)}, h=q−q⁻¹={mp.nstr(h,6)}, h'={mp.nstr(hp,6)}")
    print(f"[germ] constraint fixes DIAG (σ-eigenbasis): σ'_ii = h'λ/(2λ−h); OFF-DIAG is FREE\n")
    lam = [q, -1 / q]
    print("  closed-form diagonal germ entries A_ii = q·σ'_ii·λ_i⁻¹ = q·h'/(2λ_i−h):")
    diag_pred = []
    for i, lm in enumerate(lam):
        # A = q σ' σ⁻¹, in eigenbasis A_ii = q σ'_ii / λ_i = q·(h'λ_i/(2λ_i−h))/λ_i = q h'/(2λ_i−h)
        val = q * hp / (2 * lm - h)
        diag_pred.append(val)
        print(f"     λ_{i}={mp.nstr(lm,6):>10}:  A_ii(pred) = q·h'/(2λ−h) = {mp.nstr(val,8)}")

    # seminormal germ, in σ-eigenbasis
    Ssem, Asem = seminormal_2x2_block()
    Asem_eb, Esem = in_eigenbasis(Asem, Ssem)
    # R-matrix germ: extract the nontrivial 2×2 block (rows/cols 1,2 of Ř, basis 12,21)
    R4 = r_matrix(q); g4 = germ_4x4(q, base.EPS)
    Sr = mp.matrix([[R4[1, 1], R4[1, 2]], [R4[2, 1], R4[2, 2]]])
    Ar = mp.matrix([[g4[1, 1], g4[1, 2]], [g4[2, 1], g4[2, 2]]])
    Ar_eb, Er = in_eigenbasis(Ar, Sr)

    def diag_offdiag(M):
        d = [M[0, 0], M[1, 1]]
        o = mp.sqrt(abs(M[0, 1]) ** 2 + abs(M[1, 0]) ** 2)
        return d, o

    dsem, osem = diag_offdiag(Asem_eb)
    dr, orr = diag_offdiag(Ar_eb)
    print(f"\n  seminormal germ (σ-eigenbasis): diag={[mp.nstr(mp.re(x),6) for x in dsem]}  "
          f"offdiag_norm={mp.nstr(osem,4)}")
    print(f"  R-matrix    germ (σ-eigenbasis): diag={[mp.nstr(mp.re(x),6) for x in dr]}  "
          f"offdiag_norm={mp.nstr(orr,4)}")
    # sort diagonals to compare (eigenvalue order may differ)
    dsem_s = sorted([mp.re(x) for x in dsem]); dr_s = sorted([mp.re(x) for x in dr])
    dpred_s = sorted([mp.re(x) for x in diag_pred])
    diag_match = max(abs(dsem_s[i] - dpred_s[i]) for i in range(2)) < mp.mpf(10) ** -20 and \
                 max(abs(dr_s[i] - dpred_s[i]) for i in range(2)) < mp.mpf(10) ** -20
    offdiag_differ = abs(osem - orr) > mp.mpf("1e-6")
    print(f"\n  DIAGONALS match the closed form (both reps)?  {'YES ✓' if diag_match else 'NO'}")
    print(f"  OFF-DIAGONALS differ between reps?            {'YES ✓' if offdiag_differ else 'NO'}")
    if diag_match and offdiag_differ:
        print("\n  ⇒ CONFIRMED: the germ's σ-eigenbasis DIAGONAL is fixed by the differentiated-Hecke")
        print("    relation (identical across reps + matches h'λ/(2λ−h)); the OFF-DIAGONAL is FREE")
        print("    and rep-dependent. The germ is NOT a canonical full-tower object — the seminormal")
        print("    and R-matrix realizations are both valid germs differing only in the free part,")
        print("    which is the mechanism behind the two-row R-matrix mismatch (#6432).")


if __name__ == "__main__":
    main()
