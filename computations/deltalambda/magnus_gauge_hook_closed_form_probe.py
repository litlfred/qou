#!/usr/bin/env python3
"""magnus_gauge_hook_closed_form_probe.py — the hook column of the GAUGE-INVARIANT curvature Ω₂^P
has a reduced-Burau closed form, all orders (qou-o6ov).

#6445 established that the projector curvature Ω₂^P = (4/[2]_q²)·Σ_a[σ_a,σ_{a+1}] is a genuine
Hecke-algebra ELEMENT (not a rep-specific log-derivative like the germ), so — unlike the germ,
whose exterior-power reduction was the whole point of #6430 and was germ-naturality-limited — the
#6430 hook handle applies to Ω₂^P DIRECTLY.

CLOSED FORM (derived). On a hook (k,1^{n-k}) = Λ^{j}(V), j = n−k, V = reflection rep (n-1,1):
Λ^j is a tensor functor, so Λ^j(A)·Λ^j(B) = Λ^j(AB) and tr_{Λ^j V}(Λ^j M) = e_j(eig M|_V).
With ρ acting as Λ^j(W), W = ρ^V (reduced Burau of the word), and Ω₂^P built from the σ's:

    tr_{(k,1^{n-k})}(ρ·Ω₂^P)
      = (4/[2]_q²) · q^{(L+2)(1−j)} · Σ_a [ e_j(eig( W·σ^V_a·σ^V_{a+1} )) − e_j(eig( W·σ^V_{a+1}·σ^V_a )) ]

with j = n−k and L = |ρ| the word length. The q^{(L+2)(1−j)} is #6430's exact word-length twist
(tr_hook(word) = q^{len·(1−j)}·e_j(eig word^V)) at len = L+2, since each ρσ_aσ_{a+1} is a word two
generators longer than ρ; it is common to both commutator terms and factors out. (A first pass
omitted it and matched ONLY at j=0,1 and the endpoints — j=1 has twist 1, and the endpoints
vanish regardless — so the interior failure was the missing twist, not a wrong reduction.)

A closed form in the (n-1)-dim reduced Burau — NO seminormal germ, valid for ALL orders. It makes
the manifest endpoint-zero explicit: j=0 ⇒ e_0≡1 ⇒ each bracket 0 (trivial); j=n−1 ⇒ e_{n-1}=det,
and det(Wσ_aσ_{a+1})=det(Wσ_{a+1}σ_a) ⇒ each bracket 0 (sign).

This probe VERIFIES the closed form against the direct seminormal projector-curvature trace
(the #6445 `projector_curvature_trace`) on every hook at A=2 (n=6), exact mpf. A match to ~1e-130
establishes the hook column of the gauge-invariant curvature = a reduced-Burau elementary-symmetric
formula, extending #6430 from the plain character to the curvature. scope-(a); NO-FLOAT64 (mpf).
No fit, no witness, nothing wired.
"""
from __future__ import annotations

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))  # computations/

import mpmath as mp  # noqa: E402

mp.mp.dps = 140  # pin explicitly (do not rely on an imported side effect)

import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from magnus_hook_exterior_power_probe import elem_sym_from_eigs  # noqa: E402
from magnus_gauge_invariant_curvature_probe import projector_curvature_trace  # noqa: E402


def reflection_generators(n, ngen, q):
    """Dense reduced-Burau (reflection rep V=(n-1,1)) matrices σ^V_g for g=0..ngen-1, + dim."""
    per_gen, dim = base.block_structure((n - 1, 1))
    sig = base.sigma_csr(per_gen, dim, q)
    return [base._dense_from_csr(sig[g], dim) for g in range(ngen)], dim


def hook_closed_form(k, n, W, sV, ngen, q, L):
    """(4/[2]²)·q^{(L+2)(1−j)}·Σ_a [e_j(eig(W σ_a σ_{a+1})) − e_j(eig(W σ_{a+1} σ_a))], j = n−k.

    Each term ρσ_aσ_{a+1} is a WORD of length L+2, so #6430's exact hook identity
    tr_(k,1^{n-k})(word) = q^{len(word)·(1−j)}·e_j(eig word^V) applies with len = L+2; the twist
    is common to both terms of the commutator, so it factors out of the whole sum."""
    j = n - k
    two_q = q + 1 / q
    coef = 4 / two_q ** 2
    twist = q ** ((L + 2) * (1 - j))            # #6430 word-length twist, len(ρσσ) = L+2
    total = mp.mpf(0)
    for a in range(ngen - 1):
        E_ab, _ = mp.eig(W * sV[a] * sV[a + 1])       # mp.eig → (eigenvalues, eigenvectors)
        E_ba, _ = mp.eig(W * sV[a + 1] * sV[a])
        e_ab = elem_sym_from_eigs(list(E_ab))
        e_ba = elem_sym_from_eigs(list(E_ba))
        total += e_ab[j] - e_ba[j]
    return coef * twist * total


def main():
    A = 2
    q = base.Q0
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1

    sV, dimV = reflection_generators(n, ngen, q)
    W = sV[gens[0]]
    for g in gens[1:]:
        W = W * sV[g]

    print(f"[gauge-hook] Ω₂^P hook column via reduced Burau (dim {dimV}); A={A}, n={n}, |word|={len(gens)}")
    print(f"[gauge-hook] tr_(k,1^(n-k))(ρΩ₂^P) =?= (4/[2]²)Σ_a[e_j(eig Wσ_aσ_(a+1)) − e_j(eig Wσ_(a+1)σ_a)], j=n−k\n")
    print("   k  hook             j    direct tr(ρΩ₂^P)       closed form (Burau)      |Δ_rel|")
    worst = mp.mpf(0)
    for k in range(n, 0, -1):
        hook = tuple([k] + [1] * (n - k))
        direct, _ = projector_curvature_trace(hook, gens, q)
        cf = hook_closed_form(k, n, W, sV, ngen, q, len(gens))
        direct_r, cf_r = mp.re(direct), mp.re(cf)
        absd = abs(direct_r - cf_r)
        # At the two endpoints the direct trace is EXACTLY 0 (scalar σ ⇒ zero commutator), so a
        # relative error over a 1e-80 regulariser inflates dps-floor eig noise (~1e-140) into a
        # spurious ~1e-60 "miss". Score those by ABSOLUTE error; interiors by relative error.
        if abs(direct_r) < mp.mpf(10) ** -120:
            err = absd                       # absolute, endpoint (exactly-zero) case
            tag = "abs"
        else:
            err = absd / abs(direct_r)       # relative, interior case
            tag = "rel"
        worst = max(worst, err)
        print(f"  {k:>2}  {str(hook):<15}  {n-k:>1}   {mp.nstr(direct_r,12):>18}   "
              f"{mp.nstr(cf_r,12):>18}   {mp.nstr(err,3)} ({tag})")
    print()
    if worst < mp.mpf(10) ** -100:
        print(f"  ✓ CLOSED FORM VERIFIED on every hook (worst |Δ_rel| = {mp.nstr(worst,3)} < 1e-100).")
        print("    The hook column of the GAUGE-INVARIANT curvature Ω₂^P reduces to an elementary-")
        print("    symmetric formula in the (n-1)-dim reduced Burau — all orders, no seminormal germ.")
        print("    Extends #6430 (plain character) to the curvature; endpoint-zero is manifest")
        print("    (j=0 ⇒ e_0≡1; j=n−1 ⇒ e_{n-1}=det, both brackets vanish).")
    else:
        print(f"  ✗ mismatch (worst |Δ_rel| = {mp.nstr(worst,3)}) — closed form does NOT hold; re-derive.")


if __name__ == "__main__":
    main()
