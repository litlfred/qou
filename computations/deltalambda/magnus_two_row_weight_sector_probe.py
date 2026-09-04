#!/usr/bin/env python3
"""magnus_two_row_weight_sector_probe.py — the two-row column of the gauge-invariant curvature from
the WEIGHT SECTORS of the 2-dim R-matrix (qou-o6ov).

#6432: two-row CHARACTERS reduce exactly to the 2-dim U_q(sl₂) R-matrix via Schur–Weyl,
    (ℂ²)^⊗n = ⊕_{k=0}^{⌊n/2⌋} V_{n−2k} ⊗ (n−k,k),
but only as the WEIGHTED SUM Σ_k (n−2k+1)·tr_{(n−k,k)}. #6445: Ω₂^P = (4/[2]²)Σ_a[σ_a,σ_{a+1}] is a
genuine Hecke element, so its traces are characters — the R-matrix carries it (the germ it did not).

THE HANDLE. The R-matrix Ř is WEIGHT-PRESERVING: it never changes the number of up-spins, so every
Hecke element acts block-diagonally on the up-spin sectors W_k (k up-spins, dim C(n,k)). By
Schur–Weyl the sl₂ irrep V_{n−2k'} contributes exactly one weight vector to W_k iff k' ≤ k
(for k ≤ n/2), so
    tr_{W_k}(g) = Σ_{k'≤k} tr_{(n−k',k')}(g)   ⇒   tr_{(n−k,k)}(g) = tr_{W_k}(g) − tr_{W_{k−1}}(g)
for EVERY Hecke element g, with dim (n−k,k) = C(n,k) − C(n,k−1) (the two-row hook-length formula).
This is the two-row analogue of the hooks' reduced-Burau reduction: each two-row irrep trace comes
from two blocks of size C(n,k) built directly from the fixed 4×4 Ř — no seminormal machinery, and
the building block is n-independent.

THIS PROBE (A=2,3; exact mpf; dps 140):
  (a) PLAIN: tr_{(n−k,k)}^{seminormal}(ρ) == tr_{W_k}(ρ) − tr_{W_{k−1}}(ρ)   [expect ~1e-140]
  (b) CURVATURE: the same with ρ·Ω₂^P inserted (Ω₂^P built from Ř on each sector)  [expect match:
      Ω₂^P is an algebra element; the GERM would fail here exactly as it failed in #6432]
  (c) the two-row decay column |tr_{(n−k,k)}(ρΩ₂^P)|/dim vs b(λ) = k, from the sectors.
The sectors are built sparsely from bitstrings; the largest block at A=3 is C(9,4) = 126.
scope-(a); NO-FLOAT64 (mpf). No fit, no witness, nothing wired.
"""
from __future__ import annotations

import argparse
import math
import os
import sys
from itertools import combinations

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))  # computations/

import mpmath as mp  # noqa: E402

mp.mp.dps = 140  # pin explicitly (do not rely on an imported side effect)

import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from magnus_hook_exterior_power_probe import word_trace  # noqa: E402
from magnus_gauge_invariant_curvature_probe import projector_curvature_trace  # noqa: E402


def sector_basis(n, k):
    """All n-bit states with exactly k up-spins (bit (n-1-j) = strand j, strand 0 = MSB, matching
    the Kronecker convention of magnus_two_row_rmatrix_probe.embed). Returns (states, index)."""
    states = []
    for ups in combinations(range(n), k):
        s = 0
        for j in ups:
            s |= 1 << (n - 1 - j)
        states.append(s)
    states.sort()
    return states, {s: i for i, s in enumerate(states)}


def sector_R(n, k, i, q, states, index):
    """Ř acting on strands (i, i+1), restricted to the k-up-spin sector, as a dense mp.matrix
    M[out, in]. Ř in the pair basis (00,01,10,11) = (strand i, strand i+1):
        00 → q·00,  11 → q·11,  01 → (q−q⁻¹)·01 + 10,  10 → 01
    (the r_matrix of magnus_two_row_rmatrix_probe, column = input)."""
    qi = 1 / q
    D = len(states)
    M = mp.zeros(D, D)
    bi, bj = n - 1 - i, n - 2 - i          # bit positions of strand i and strand i+1
    for col, s in enumerate(states):
        a = (s >> bi) & 1                    # strand i
        b = (s >> bj) & 1                    # strand i+1
        if a == b:
            M[col, col] += q                 # 00 or 11: eigenvalue q, stays in place
        elif a == 0 and b == 1:              # 01 → (q−q⁻¹)·01 + 10
            M[col, col] += q - qi
            t = s ^ (1 << bi) ^ (1 << bj)    # swap → 10
            M[index[t], col] += 1
        else:                                # 10 → 01
            t = s ^ (1 << bi) ^ (1 << bj)
            M[index[t], col] += 1
    return M


def sector_traces(n, k, gens, q):
    """(tr_{W_k}(ρ), tr_{W_k}(ρ·Ω₂^P), dim W_k) with ρ = ∏Ř_{gens}, Ω₂^P = (4/[2]²)Σ_a[Ř_a,Ř_{a+1}]."""
    states, index = sector_basis(n, k)
    D = len(states)
    ngen = max(gens) + 1
    R = [sector_R(n, k, i, q, states, index) for i in range(ngen)]
    rho = R[gens[0]]
    for g in gens[1:]:
        rho = rho * R[g]
    two_q = q + 1 / q
    O = mp.zeros(D, D)
    for a in range(ngen - 1):
        O = O + (R[a] * R[a + 1] - R[a + 1] * R[a])
    O = (4 / two_q ** 2) * O
    M = rho * O
    return sum(rho[i, i] for i in range(D)), sum(M[i, i] for i in range(D)), D


def analyze(A):
    q = base.Q0
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    print(f"[sector] A={A} (n={n}); |word|={len(gens)}, ngen={max(gens)+1}")
    print(f"[sector] tr_(n-k,k)(g) =?= tr_W_k(g) − tr_W_(k-1)(g),  W_k = k-up-spin sector of (ℂ²)^⊗n\n")
    print("   k  λ=(n-k,k)   dim(sem)  C(n,k)-C(n,k-1)   |Δ_rel| PLAIN     |Δ_rel| ρΩ₂^P     |tr(ρΩ₂^P)|/dim")
    prev_plain, prev_curv = mp.mpf(0), mp.mpf(0)
    worst_plain, worst_curv = mp.mpf(0), mp.mpf(0)
    for k in range(0, n // 2 + 1):
        lam = (n - k, k) if k > 0 else (n,)
        _pg, dim_sem = base.block_structure(lam)
        sp, sc, D = sector_traces(n, k, gens, q)
        two_plain = mp.re(sp) - mp.re(prev_plain)
        two_curv = mp.re(sc) - mp.re(prev_curv)
        prev_plain, prev_curv = sp, sc
        dim_formula = math.comb(n, k) - (math.comb(n, k - 1) if k > 0 else 0)
        trp, _ = word_trace(lam, gens)
        trc, _ = projector_curvature_trace(lam, gens, q)
        trp, trc = mp.re(trp), mp.re(trc)
        relp = abs(trp - two_plain) / (abs(trp) + mp.mpf(10) ** -80)
        # curvature vanishes exactly on (n,) (1-dim: scalars commute) — use absolute error there
        relc = abs(trc - two_curv) if abs(trc) < mp.mpf(10) ** -100 else abs(trc - two_curv) / abs(trc)
        worst_plain = max(worst_plain, relp); worst_curv = max(worst_curv, relc)
        print(f"  {k:>2}  {str(lam):<10}  {dim_sem:>6}   {dim_formula:>8}         {mp.nstr(relp,3):>9}      "
              f"{mp.nstr(relc,3):>9}      {mp.nstr(abs(trc)/dim_sem,6)}")
    print()
    okp = worst_plain < mp.mpf(10) ** -100
    okc = worst_curv < mp.mpf(10) ** -100
    print(f"  (a) PLAIN two-row characters = sector differences?   {'YES ✓' if okp else 'NO ✗'}  (worst {mp.nstr(worst_plain,3)})")
    print(f"  (b) CURVATURE two-row traces = sector differences?   {'YES ✓' if okc else 'NO ✗'}  (worst {mp.nstr(worst_curv,3)})")
    if okp and okc:
        print("  ⇒ the two-row column of the gauge-invariant curvature is carried EXACTLY by the up-spin")
        print("    sectors of the 2-dim R-matrix: tr_(n-k,k)(ρΩ₂^P) = tr_W_k − tr_W_(k-1), blocks of size")
        print("    C(n,k) built from the fixed 4×4 Ř. This is the two-row analogue of the hooks'")
        print("    reduced-Burau handle (#6464) — it exists because Ω₂^P is an algebra element (#6445).")
    elif okp:
        print("  ⇒ plain matches but the curvature does not — Ω₂^P is NOT being carried; re-check the")
        print("    sector construction of the commutators (the germ would fail here; Ω₂^P must not).")
    else:
        print("  ⇒ plain mismatch: sector labelling / pair-ordering convention differs from seminormal;")
        print("    the identification needs the conjugate sector or a q ↔ q⁻¹ flip before (b) is meaningful.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, nargs="+", default=[2, 3])
    args = ap.parse_args()
    for A in args.A:
        analyze(A)
        print()


if __name__ == "__main__":
    main()
