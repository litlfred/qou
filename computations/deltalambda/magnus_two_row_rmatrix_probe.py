#!/usr/bin/env python3
"""magnus_two_row_rmatrix_probe.py — does the 2-dim U_q(sl₂) R-matrix reach the two-row column?
(qou-o6ov)

magnus_two_row_reduction_probe.py showed two-rows do NOT reduce to the (n-1)-dim reduced Burau
ρ^V (hooks were special: single-column Schur functors are irreducible over S_n). The
Schur-Weyl-natural home for two-row CHARACTERS is the 2-dim U_q(sl₂) fundamental: the braid
group acts on (ℂ²)^⊗n via the R-matrix, and
    (ℂ²)^⊗n = ⊕_{k=0}^{⌊n/2⌋} (sl₂ irrep, dim n-2k+1) ⊗ (Hecke two-row irrep (n-k,k)),
so  tr_{(ℂ²)^⊗n}(g) = Σ_k (n-2k+1) · tr_{(n-k,k)}(g).

THE SUBTLETY THIS TESTS. The germ A_i = q ∂_q σ_i · σ_i⁻¹ is REPRESENTATION-SPECIFIC (a
log-derivative of the rep matrix, not an abstract algebra element), so the R-matrix germ need
NOT reproduce the seminormal two-row germ traces — it does iff the seminormal↔R-matrix
intertwiner on each two-row block is q-independent. Decisive empirical test (exact mpf):
    Σ_k (n-2k+1) · tr_{(n-k,k)}^{seminormal}(ρ·Ω₂)   ==?==   tr_{(ℂ²)^⊗n}(ρ·Ω₂)^{R-matrix}
A match ⇒ the 2-dim R-matrix IS the two-row handle (germ preserved); a mismatch ⇒ the germ is
realization-dependent and the 2-dim reduction does not carry the decay object.

Both sides use the germ built by the SAME finite-difference recipe (base.EPS). dim 2^n: A=2 → 64
(fast), A=3 → 512 (slower). scope-(a); NO-FLOAT64 (mpf). No fit, no witness, nothing wired.
"""
from __future__ import annotations

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))  # computations/

import mpmath as mp  # noqa: E402
import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from magnus_extreme_rep_endpoint_probe import omega2_trace  # noqa: E402


def r_matrix(q):
    """Hecke R-matrix Ř on ℂ²⊗ℂ² (basis 11,12,21,22), eigenvalues q (×3), −q⁻¹ (×1)."""
    qi = 1 / q
    return mp.matrix([
        [q, 0, 0, 0],
        [0, q - qi, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, q],
    ])


def germ_4x4(q, eps):
    """A = q·(∂Ř)·Ř⁻¹ by central finite difference (same recipe as base.germ_csr)."""
    Rp, Rm = r_matrix(q + eps), r_matrix(q - eps)
    dR = (Rp - Rm) / (2 * eps)
    return q * dR * (r_matrix(q) ** -1)


def embed(op4, i, n):
    """Embed a 4×4 operator on strands (i,i+1) into (ℂ²)^⊗n as a 2^n×2^n dense matrix."""
    left = 1 << i                # 2^i
    right = 1 << (n - i - 2)      # 2^(n-i-2)
    Il = mp.eye(left)
    Ir = mp.eye(right)
    # Kronecker: Il ⊗ op4 ⊗ Ir
    return mp.matrix(_kron(_kron(_mat_list(Il), _mat_list(op4)), _mat_list(Ir)))


def _mat_list(M):
    return [[M[i, j] for j in range(M.cols)] for i in range(M.rows)]


def _kron(A, B):
    ra, ca = len(A), len(A[0])
    rb, cb = len(B), len(B[0])
    out = [[mp.mpf(0)] * (ca * cb) for _ in range(ra * rb)]
    for i in range(ra):
        for j in range(ca):
            aij = A[i][j]
            if aij == 0:
                continue
            for p in range(rb):
                for r in range(cb):
                    out[i * rb + p][j * cb + r] = aij * B[p][r]
    return out


def tensor_side(A):
    """Return (tr_(ℂ²)^⊗n(ρ)  [plain],  tr_(ℂ²)^⊗n(ρΩ₂), n)."""
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    q = base.Q0
    R4 = r_matrix(q)
    g4 = germ_4x4(q, base.EPS)
    ngen = max(gens) + 1
    sig = [embed(R4, i, n) for i in range(ngen)]
    A_ = [embed(g4, i, n) for i in range(ngen)]
    rho = sig[gens[0]]
    for gi in gens[1:]:
        rho = rho * sig[gi]
    D = 1 << n
    tr_plain = sum(rho[i, i] for i in range(D))
    O = mp.zeros(D, D)
    for a in range(ngen - 1):
        O = O + (A_[a] * A_[a + 1] - A_[a + 1] * A_[a])
    M = rho * O
    return tr_plain, sum(M[i, i] for i in range(D)), n


def seminormal_weighted_sum(A):
    """Return (Σ mult·tr(ρΩ₂), Σ mult·tr(ρ) [plain], rows)."""
    from magnus_hook_exterior_power_probe import word_trace  # noqa: E402
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    total = mp.mpf(0)
    total_plain = mp.mpf(0)
    rows = []
    for k in range(0, n // 2 + 1):
        lam = (n - k, k) if k > 0 else (n,)
        _pg, dim = base.block_structure(lam)
        tr, _ = omega2_trace(lam, gens)
        trp, _ = word_trace(lam, gens)
        mult = n - 2 * k + 1  # dim of the sl₂ irrep paired with (n-k,k)
        total += mult * tr
        total_plain += mult * mp.re(trp)
        rows.append((k, lam, dim, mult, tr))
    return total, total_plain, rows


def analyze(A):
    print(f"[rmat] A={A} (n={3*A}); Σ_k (n-2k+1)·tr_(n-k,k)  vs  tr_(ℂ²)^⊗n  (plain AND ρΩ₂)")
    lhs, lhs_plain, rows = seminormal_weighted_sum(A)
    for k, lam, dim, mult, tr in rows:
        print(f"     k={k}  λ={str(lam):<10} dim={dim:>4}  mult(sl₂)={mult:>2}  "
              f"tr(ρΩ₂)={mp.nstr(tr,8)}")
    rhs_plain, rhs, n = tensor_side(A)
    D = 1 << n
    # PLAIN character check (must match exactly — the character is realization-independent)
    relp = abs(lhs_plain - rhs_plain) / (abs(lhs_plain) + mp.mpf(10) ** -80)
    print(f"\n   PLAIN:  Σ mult·tr(ρ) = {mp.nstr(lhs_plain,12)}   "
          f"tr_(ℂ²)^⊗{n}(ρ) = {mp.nstr(rhs_plain,12)}   |Δ_rel|={mp.nstr(relp,3)} "
          f"{'✓' if relp < mp.mpf(10)**-20 else '✗ (R-matrix convention mismatch!)'}")
    # germ-inserted check
    rel = abs(lhs - rhs) / (abs(lhs) + mp.mpf(10) ** -80)
    print(f"   ρΩ₂:    Σ mult·tr(ρΩ₂) = {mp.nstr(lhs,12)}   "
          f"tr_(ℂ²)^⊗{n}(ρΩ₂) = {mp.nstr(rhs,12)}   |Δ_rel|={mp.nstr(rel,3)}")
    print()
    if relp < mp.mpf(10) ** -20 and rel < mp.mpf(10) ** -20:
        print("  ⇒ BOTH match: the 2-dim R-matrix carries the two-row column AND its germ — the")
        print("    two-row handle is the 2-dim sl₂ fundamental (germ preserved).")
    elif relp < mp.mpf(10) ** -20:
        print("  ⇒ PLAIN matches but ρΩ₂ does NOT: the character reduces to the 2-dim R-matrix,")
        print("    but the GERM is realization-dependent — the 2-dim reduction does not carry the")
        print("    decay object. Two-rows need a germ-aware handle, not the bare R-matrix.")
    else:
        print("  ⇒ PLAIN mismatches ⇒ R-matrix convention/framing differs from seminormal;")
        print("    the germ comparison is inconclusive until the plain character matches.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, default=2)
    args = ap.parse_args()
    analyze(A=args.A)


if __name__ == "__main__":
    main()
