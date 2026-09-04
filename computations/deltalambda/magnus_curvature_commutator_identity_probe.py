#!/usr/bin/env python3
"""magnus_curvature_commutator_identity_probe.py — the curvature trace IS a commutator-with-ρ sum,
in EVERY irrep (qou-o6ov).

DERIVATION (exact, from trace cyclicity alone — no Burau, no R-matrix, no seminormal machinery):
    tr_λ(ρ·[σ_a, σ_{a+1}]) = tr_λ(ρσ_aσ_{a+1}) − tr_λ(ρσ_{a+1}σ_a)
                            = tr_λ(ρσ_aσ_{a+1}) − tr_λ(σ_aρσ_{a+1})        [cyclicity]
                            = tr_λ([ρ, σ_a]·σ_{a+1}).
Summing over a and restoring the prefactor of Ω₂^P = (4/[2]_q²)Σ_a[σ_a,σ_{a+1}]:

    tr_λ(ρ·Ω₂^P) = (4/[2]_q²) · Σ_a tr_λ( [ρ, σ_a] · σ_{a+1} )        (★)

WHY THIS MATTERS. Every prior handle in this arc was FAMILY-SPECIFIC — hooks via the reduced Burau
(#6464), two-rows via R-matrix weight sectors (#6525). (★) holds for EVERY λ ⊢ n, and it lands on
[ρ, σ_a] — the arc's ORIGINAL single-window object (‖[ρ,A_a]‖_F). It says the curvature trace is
governed entirely by how the atom braid word FAILS TO COMMUTE with each generator: if ρ commuted
with every σ_a, the whole decay object would vanish identically in every irrep.

THIS PROBE (A=2,3; exact mpf; dps 140), over ALL λ ⊢ n:
  (1) verify (★) to the dps floor — direct tr_λ(ρΩ₂^P) vs the commutator form;
  (2) the SUB-IDENTITY per a: tr_λ(ρ[σ_a,σ_{a+1}]) == tr_λ([ρ,σ_a]σ_{a+1}) termwise;
  (3) MECHANISM: does the commutator itself carry the b(λ)-decay? Report the Frobenius-style
      weight Σ_a ‖[ρ,σ_a]‖ / (dim·‖ρ‖) alongside |tr(ρΩ₂^P)|/dim, to see whether the decay is
      already present in ‖[ρ,σ_a]‖ (a norm statement, family-independent) or only after tracing
      against σ_{a+1} (a cancellation statement).
scope-(a); NO-FLOAT64 (mpf). No fit, no witness, nothing wired.
"""
from __future__ import annotations

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))  # computations/

import mpmath as mp  # noqa: E402

mp.mp.dps = 140  # pin explicitly (do not rely on an imported side effect)

import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from magnus_gauge_invariant_curvature_probe import projector_curvature_trace  # noqa: E402


def sigma_dense(shape, q, ngen):
    per_gen, dim = base.block_structure(shape)
    sig = base.sigma_csr(per_gen, dim, q)
    return [base._dense_from_csr(sig[g], dim) for g in range(ngen)], dim


def frob(M, dim):
    s = mp.mpf(0)
    for i in range(dim):
        for j in range(dim):
            s += abs(M[i, j]) ** 2
    return mp.sqrt(s)


def analyze(A, max_dim=None):
    q = base.Q0
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1
    two_q = q + 1 / q
    coef = 4 / two_q ** 2

    print(f"[comm] A={A} (n={n}); |word|={len(gens)}, ngen={ngen}"
          + (f"; SKIPPING dim > {max_dim} (cost: O(dim³) mpf matmul)" if max_dim else ""))
    print(f"[comm] (★) tr_λ(ρ·Ω₂^P) =?= (4/[2]²)·Σ_a tr_λ([ρ,σ_a]·σ_(a+1))   — ALL λ ⊢ n\n")
    print("   λ                b   dim   |tr(ρΩ₂^P)|/dim   |Δ_rel| (★)   termwise worst   Σ‖[ρ,σ_a]‖/(dim‖ρ‖)")
    worst_star, worst_term = mp.mpf(0), mp.mpf(0)
    skipped = []
    for lam in base.partitions(n):
        _pg, _dim_peek = base.block_structure(lam)
        if max_dim is not None and _dim_peek > max_dim:
            skipped.append((lam, _dim_peek))
            continue
        sig, dim = sigma_dense(lam, q, ngen)
        rho = sig[gens[0]]
        for g in gens[1:]:
            rho = rho * sig[g]
        # direct
        direct, _ = projector_curvature_trace(lam, gens, q)
        direct = mp.re(direct)
        # commutator form + termwise check
        tot = mp.mpf(0)
        tw = mp.mpf(0)
        comm_norm = mp.mpf(0)
        for a in range(ngen - 1):
            C = rho * sig[a] - sig[a] * rho           # [ρ, σ_a]
            M = C * sig[a + 1]
            t_comm = sum(M[i, i] for i in range(dim))
            # sub-identity: tr(ρ[σ_a,σ_{a+1}]) == tr([ρ,σ_a]σ_{a+1})
            K = rho * (sig[a] * sig[a + 1] - sig[a + 1] * sig[a])
            t_direct = sum(K[i, i] for i in range(dim))
            den = abs(t_direct) if abs(t_direct) > mp.mpf(10) ** -100 else mp.mpf(1)
            tw = max(tw, abs(t_comm - t_direct) / den)
            tot += t_comm
        for a in range(ngen):
            comm_norm += frob(rho * sig[a] - sig[a] * rho, dim)
        star = coef * mp.re(tot)
        den = abs(direct) if abs(direct) > mp.mpf(10) ** -100 else mp.mpf(1)
        rel = abs(direct - star) / den
        worst_star = max(worst_star, rel); worst_term = max(worst_term, tw)
        b = sum(lam) - lam[0]
        rnorm = frob(rho, dim)
        print(f"  {str(lam):<16} {b:>1}  {dim:>4}   {mp.nstr(abs(direct)/dim,7):>13}   "
              f"{mp.nstr(rel,3):>10}   {mp.nstr(tw,3):>12}   {mp.nstr(comm_norm/(dim*rnorm),6)}")

    print()
    if skipped:
        print(f"  SKIPPED {len(skipped)} shape(s) over the dim cap (NOT evidence — just not run): "
              + ", ".join(f"{lam}(dim {d})" for lam, d in skipped) + "\n")
    ok1 = worst_star < mp.mpf(10) ** -100
    ok2 = worst_term < mp.mpf(10) ** -100
    print(f"  (1) (★) holds for every λ?        {'YES ✓' if ok1 else 'NO ✗'}  (worst |Δ_rel| = {mp.nstr(worst_star,3)})")
    print(f"  (2) termwise sub-identity holds?  {'YES ✓' if ok2 else 'NO ✗'}  (worst = {mp.nstr(worst_term,3)})")
    if ok1 and ok2:
        print("  ⇒ the curvature trace IS a commutator-with-ρ sum, in EVERY irrep — from trace")
        print("    cyclicity alone. Unlike the hook (Burau) and two-row (R-matrix sector) handles,")
        print("    this is family-independent, and it lands on the arc's original single-window")
        print("    object [ρ, σ_a]: if ρ commuted with every generator the decay object would")
        print("    vanish identically. Column (3) says whether the b-decay is already in the NORM.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, nargs="+", default=[2, 3])
    ap.add_argument("--max-dim", type=int, default=None,
                    help="skip irreps with dim above this (cost is O(dim³) mpf matmul); "
                         "skipped shapes are reported, and are NOT evidence either way")
    args = ap.parse_args()
    for A in args.A:
        analyze(A, max_dim=args.max_dim)
        print()


if __name__ == "__main__":
    main()
