#!/usr/bin/env python3
"""magnus_hook_exterior_power_probe.py — are the hook irreps the EXTERIOR POWERS of the
reduced Burau (reflection) rep? (qou-o6ov)

If YES, the whole hook column of the tr-decay reduces to the (n−1)-dim reduced-Burau matrix —
the Alexander determinant. The cleanest verifiable core is the exterior-power / elementary-
symmetric identity for the PLAIN character (no Ω₂ insertion):

    tr_{(k,1^{n-k})}(ρ)  ==  e_{n-k}( eigenvalues of ρ in the reflection rep (n-1,1) )

because hook (k,1^{n-k}) = Λ^{n-k}(V), V = reflection rep, and
tr_{Λ^j V}(Λ^j(g)) = e_j(eig g) = [t^j] det(1 + t·g|_V).

This probe builds ρ in the reflection rep (dim n-1), gets its eigenvalues, forms
e_j = [t^j] ∏(1+t μ_i), and compares to the directly-computed hook character tr_{hook}(ρ).
A match (possibly up to a q-power twist, reported) establishes hooks = q-exterior-powers of
Burau — reducing the hook column to an (n-1)-dim object. scope-(a); NO-FLOAT64 (mpf).
No fit, no witness, nothing wired.
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


def word_dense(shape, gens):
    """ρ = ∏σ_{g_i} as a dense mp.matrix in the seminormal irrep `shape`; also return dim."""
    per_gen, dim = base.block_structure(shape)
    sig = base.sigma_csr(per_gen, dim, base.Q0)
    sd = [base._dense_from_csr(sig[g], dim) for g in range(max(gens) + 1)]
    M = sd[gens[0]]
    for g in gens[1:]:
        M = M * sd[g]
    return M, dim


def word_trace(shape, gens):
    M, dim = word_dense(shape, gens)
    return sum(M[i, i] for i in range(dim)), dim


def elem_sym_from_eigs(eigs):
    """e_j for j=0..len via ∏(1+t μ_i) coefficient extraction (exact mpf convolution)."""
    poly = [mp.mpf(1)]  # coefficients, poly[j] = e_j
    for mu in eigs:
        new = poly[:] + [mp.mpf(0)]
        for j in range(len(poly)):
            new[j + 1] += poly[j] * mu
        poly = new
    return poly  # poly[j] = e_j(eigs)


def hook(n, k):
    return (n,) if k == n else tuple([k] + [1] * (n - k))


def analyze(A):
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    # reflection rep (n-1,1): eigenvalues of ρ
    refl = tuple([n - 1, 1])
    Mrefl, dv = word_dense(refl, gens)
    E, _ = mp.eig(Mrefl)              # eigenvalues (complex mpf)
    e = elem_sym_from_eigs(E)          # e[j] = e_j(eig ρ^V),  j=0..n-1
    L = len(gens)
    qL = base.Q0 ** L
    print(f"[extpow] A={A} (n={n}); reflection rep dim n-1={dv}, L={L}, q^L={mp.nstr(qL,6)}")
    print(f"[extpow] testing  tr_(k,1^(n-k))(ρ) == q^(L(1-j)) · e_j(eig ρ^V),  j=n-k\n")
    print("   k   j=n-k   tr_hook(ρ)          q^(L(1-j))·e_j        |Δ_rel|")
    worst = mp.mpf(0)
    for k in range(1, n + 1):
        lam = hook(n, k)
        trh, dim = word_trace(lam, gens)
        j = n - k
        pred = qL ** (1 - j) * e[j]
        # both real to full precision; drop imaginary noise from eig
        pred = mp.re(pred); trh_r = mp.re(trh)
        rel = abs(trh_r - pred) / (abs(trh_r) + mp.mpf(10) ** -80)
        worst = max(worst, rel if not mp.isnan(rel) else mp.mpf(0))
        print(f"  {k:>2}   {j:>3}   {mp.nstr(trh_r,10):>18}   {mp.nstr(pred,10):>18}   {mp.nstr(rel,3):>8}")
    ok = worst < mp.mpf(10) ** -20
    print(f"\n  worst relative |tr_hook − q^(L(1-j))·e_j| = {mp.nstr(worst,4)}  "
          f"{'✓ EXACT ⇒ hooks = q-exterior-powers of the reduced Burau; the whole hook' if ok else '✗ no match'}")
    if ok:
        print("  column is governed by the (n-1)-dim reduced-Burau spectrum (Alexander determinant).")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, default=3)
    args = ap.parse_args()
    analyze(A=args.A)


if __name__ == "__main__":
    main()
