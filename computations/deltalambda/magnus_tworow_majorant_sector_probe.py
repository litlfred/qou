#!/usr/bin/env python3
"""magnus_tworow_majorant_sector_probe.py — the two-row majorant via R-matrix sectors, and why
POSITIVITY is what unblocks it (qou-o6ov).

THE OBSTACLE #6525 LEFT. Two-row irreps are carried exactly by up-spin sectors of the 2-dim
R-matrix: for every Hecke algebra element g,
    tr_(n-k,k)(g) = tr_W_k(g) - tr_W_(k-1)(g),        dim = C(n,k) - C(n,k-1)
with W_k the k-up-spin sector of (ℂ²)^⊗n. #6525 noted that this DIFFERENCE structure blocks a
bound: a per-sector triangle inequality gives |tr_W_k| + |tr_W_(k-1)|, which does not decay in k
because the W_(k-1) term carries the previous sector back in.

WHY THE MAJORANT ESCAPES IT. That obstacle is about the SIGNED trace. The majorant
tr_λ(X* X) = ‖M_λ‖_F² (X = ρ·Ω₂^P) is POSITIVE for every λ, so every term in
tr_W_k(X*X) = Σ_{k'≤k} tr_(n-k',k')(X*X) is non-negative, and the subtracted sector can simply be
DROPPED:

    0 ≤ tr_(n-k,k)(X* X) = tr_W_k(X*X) - tr_W_(k-1)(X*X) ≤ tr_W_k(X* X)              (S)

No triangle inequality, no cancellation to fight — positivity does the work. This is the concrete
payoff of having moved from the signed quantity to the positive majorant (#6556): a bound the
signed trace could not have.

AND IT IS CHEAP. Ř is symmetric (verified below, not assumed), so the sector matrices are too and
tr_W_k(X*X) = ‖X|_W_k‖_F² — a sum of squared entries on a C(n,k)-dim block built from the fixed
4×4 Ř. No eigenvalues, no seminormal construction.

CHECKS (A=2,3; exact mpf, dps 140):
  (1) Ř symmetric, and the sector identity tr_λ(X*X) = tr_W_k - tr_W_(k-1) exact;
  (2) the bound (S) holds, and its slack;
  (3) does tr_W_k(X*X)/dim_λ decay with k = b(λ)?  ← the deciding column. If it does NOT, (S) is a
      valid bound that is useless for the decay theorem, and this probe says so rather than
      presenting a non-decaying bound as progress.
scope-(a); NO-FLOAT64. Nothing wired.
"""
from __future__ import annotations

import argparse
import math
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))  # computations/

import mpmath as mp  # noqa: E402

mp.mp.dps = 140  # pin explicitly (do not rely on an imported side effect)

import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from magnus_frobenius_is_positive_trace_probe import build  # noqa: E402
from magnus_two_row_weight_sector_probe import sector_basis, sector_R  # noqa: E402


def sector_majorant(n, k, gens, q):
    """tr_W_k(X* X) = ‖X|_W_k‖_F², X = ρ·Ω₂^P, all from the fixed 4×4 Ř. Returns (value, dimW, asym)."""
    states, index = sector_basis(n, k)
    D = len(states)
    ngen = max(gens) + 1
    R = [sector_R(n, k, i, q, states, index) for i in range(ngen)]
    asym = max(max(abs(R[g][i, j] - R[g][j, i]) for i in range(D) for j in range(D))
               for g in range(ngen)) if D > 1 else mp.mpf(0)
    rho = R[gens[0]]
    for g in gens[1:]:
        rho = rho * R[g]
    O = mp.zeros(D, D)
    for a in range(ngen - 1):
        O = O + (R[a] * R[a + 1] - R[a + 1] * R[a])
    X = rho * ((4 / (q + 1 / q) ** 2) * O)
    frob2 = sum(abs(X[i, j]) ** 2 for i in range(D) for j in range(D))
    return frob2, D, asym


def analyze(A):
    q = base.Q0
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1
    print(f"[tworow-maj] A={A} (n={n}); (S)  0 ≤ tr_(n-k,k)(X*X) = tr_W_k − tr_W_(k−1) ≤ tr_W_k")
    print(f"[tworow-maj] sectors built from the fixed 4×4 Ř; tr_W_k(X*X) = ‖X|_W_k‖_F² (no eigenvalues)\n")
    print("   k  λ=(n-k,k)   dim_λ   tr_λ(X*X)      sector diff     |Δ_rel|    bound tr_W_k    "
          "bound/dim_λ   slack")
    prev = mp.mpf(0)
    worst_id = mp.mpf(0)
    worst_asym = mp.mpf(0)
    rows = []
    all_hold = True
    for k in range(0, n // 2 + 1):
        lam = (n - k, k) if k > 0 else (n,)
        _pg, dim_lam = base.block_structure(lam)
        X, Xstar, dimS, _a = build(lam, gens, q, ngen)
        P = Xstar * X
        direct = mp.re(sum(P[i, i] for i in range(dimS)))
        sec, dW, asym = sector_majorant(n, k, gens, q)
        worst_asym = max(worst_asym, asym)
        diff = mp.re(sec) - mp.re(prev)
        prev = sec
        den = abs(direct) if abs(direct) > mp.mpf(10) ** -100 else mp.mpf(1)
        rel = abs(direct - diff) / den
        worst_id = max(worst_id, rel)
        holds = direct <= mp.re(sec) * (1 + mp.mpf(10) ** -60)
        all_hold = all_hold and holds
        slack = (mp.re(sec) / direct) if direct > mp.mpf(10) ** -100 else mp.mpf("inf")
        rows.append((k, dim_lam, mp.re(sec)))
        print(f"  {k:>2}  {str(lam):<10}  {dim_lam:>5}  {mp.nstr(direct,8):>12}  {mp.nstr(diff,8):>13}  "
              f"{mp.nstr(rel,3):>9}  {mp.nstr(mp.re(sec),8):>13}  {mp.nstr(mp.re(sec)/dim_lam,7):>11}  "
              f"{mp.nstr(slack,4):>7}")

    print()
    sym = worst_asym < mp.mpf(10) ** -100
    idok = worst_id < mp.mpf(10) ** -100
    print(f"  (1) Ř sector matrices symmetric?  {'YES ✓' if sym else 'NO'}  "
          f"(max|R−Rᵀ| = {mp.nstr(worst_asym,3)});  sector identity exact?  "
          f"{'YES ✓' if idok else 'NO ✗'}  (worst {mp.nstr(worst_id,3)})")
    print(f"  (2) bound (S) holds for every k?  {'YES ✓' if all_hold else 'NO ✗'}")
    inner = [(k, d, s) for k, d, s in rows if s > 0 and k > 0]
    mono = all(inner[i + 1][2] / inner[i + 1][1] < inner[i][2] / inner[i][1]
               for i in range(len(inner) - 1))
    print(f"  (3) bound/dim_λ strictly decreasing in k for k ≥ 1?  {'YES ✓' if mono else 'NO'}")
    if all_hold and mono:
        print("\n  ⇒ TWO-ROW COLUMN BOUNDED. Positivity of the majorant lets the subtracted sector be")
        print("    dropped outright — the difference structure that blocked #6525's signed trace is")
        print("    not an obstacle here. The bound is a single sector Frobenius norm on a C(n,k)-dim")
        print("    block of the fixed 4×4 Ř, and it decays per dimension in k = b(λ).")
    elif all_hold:
        print("\n  ⇒ (S) holds but its per-dim form is NOT monotone — a valid bound that is USELESS")
        print("    for the decay theorem. Dropping tr_W_(k-1) is evidently too lossy at large k;")
        print("    the difference would have to be kept. Reporting this, not presenting it as progress.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, nargs="+", default=[2, 3])
    args = ap.parse_args()
    for A in args.A:
        analyze(A)
        print()


if __name__ == "__main__":
    main()
