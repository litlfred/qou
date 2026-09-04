#!/usr/bin/env python3
"""magnus_sumabs_eig_bound_probe.py — a DERIVED bound for Σ|eig(M_λ)| itself (qou-o6ov).

THE TARGET. #6556 established that the b(λ)-decay of |tr_λ(ρΩ₂^P)| is carried by the magnitude
factor Σ|eig(M_λ)|, M_λ = ρ_λ(ρ)·ρ_λ(Ω₂^P). That quantity is what a general-λ theorem must control,
and until now it was only measured. This derives a bound for it.

THE DERIVATION — three steps, each a classical inequality, no new mathematics:

  (i)   Σ_i |eig_i(M)|  ≤  √(dim · Σ_i |eig_i(M)|²)          [Cauchy–Schwarz on the moduli vector]
  (ii)  Σ_i |eig_i(M)|² ≤  ‖M‖_F²                            [Schur's inequality]
  (iii) ‖M_λ‖_F²        =  tr_λ(X* X),   X = ρ·Ω₂^P          [the anti-involution identity, #6556]

Composing:

        Σ_i |eig_i(M_λ)|  ≤  √( dim_λ · tr_λ(X* X) )                       (B)

and since |tr_λ(ρΩ₂^P)| ≤ Σ|eig|, the same right-hand side bounds the quantity the arc is after.
(B) is fully derived. Its right-hand side is a POSITIVE trace of a Hecke algebra element, so the
arc's handles apply — and on the hook column it is explicit in the reduced Burau (#6556's derived
closed form), needing only (n−1)×(n−1) matrices.

NOTE ON STEP (i): it costs a factor up to √dim and is tight exactly when all |eig_i| are equal.
That is a real loss and this probe measures it rather than hiding it — the tightness column is
Σ|eig| / √(dim·tr(X*X)).

WHAT THIS PROBE CHECKS (A=2,3; exact mpf; dps 140):
  (1) (B) HOLDS for every λ — a violation would mean one of (i)-(iii) is misapplied;
  (2) its TIGHTNESS, per λ and per b — how much the Cauchy–Schwarz step gives away;
  (3) whether the BOUND ITSELF decays with b, per dimension and on conjugate pairs
      (dim λ = dim λ' EXACTLY). A bound that holds but does not decay is useless for the theorem;
      this is the decisive column.
scope-(a); NO-FLOAT64. No fit, no witness, nothing wired.
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
from magnus_frobenius_is_positive_trace_probe import build  # noqa: E402
from magnus_conjugate_pair_cancellation_probe import conjugate  # noqa: E402


def measure(lam, gens, q, ngen):
    """(|tr|, Σ|eig|, Σ|eig|², bound √(dim·tr(X*X)), tr(X*X), dim)."""
    X, Xstar, dim, _asym = build(lam, gens, q, ngen)
    E, _ = mp.eig(X)
    tr = abs(sum(E))
    s_abs = sum(abs(e) for e in E)
    s_sq = sum(abs(e) ** 2 for e in E)
    P = Xstar * X
    trXX = mp.re(sum(P[i, i] for i in range(dim)))
    bound = mp.sqrt(dim * trXX) if trXX > 0 else mp.mpf(0)
    return tr, s_abs, s_sq, bound, trXX, dim


def analyze(A, max_dim):
    q = base.Q0
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1
    print(f"[bound] A={A} (n={n});  (B)  Σ|eig(M_λ)| ≤ √(dim_λ · tr_λ(X*X)),  X = ρ·Ω₂^P;  dim ≤ {max_dim}")
    print(f"[bound] via Cauchy–Schwarz (i), Schur (ii), the anti-involution identity (iii)\n")
    print("   λ                  b   dim     Σ|eig|       bound (B)     tightness   Schur slack   bound/dim   holds?")
    cache, all_hold = {}, True
    for lam in base.partitions(n):
        lam = tuple(lam)
        _pg, d = base.block_structure(lam)
        if d > max_dim:
            continue
        tr, s_abs, s_sq, bound, trXX, dim = measure(lam, gens, q, ngen)
        holds = s_abs <= bound * (1 + mp.mpf(10) ** -60)
        all_hold = all_hold and holds
        tight = (s_abs / bound) if bound > 0 else mp.mpf(0)
        schur = (s_sq / trXX) if trXX > 0 else mp.mpf(0)   # ≤ 1 by Schur; 1 iff M normal
        cache[lam] = (sum(lam) - lam[0], dim, bound, s_abs)
        print(f"  {str(lam):<18} {sum(lam)-lam[0]:>1}  {dim:>4}  {mp.nstr(s_abs,7):>11}  {mp.nstr(bound,7):>13}  "
              f"{mp.nstr(tight,4):>10}  {mp.nstr(schur,4):>11}  {mp.nstr(bound/dim,6):>10}   "
              f"{'yes' if holds else 'NO'}")

    print(f"\n  (1) (B) holds for every λ?  {'YES ✓' if all_hold else 'NO ✗ — one of (i)-(iii) is misapplied'}")

    print("\n   b     mean bound/dim     mean tightness")
    byb = {}
    for lam, (b, dim, bound, s_abs) in cache.items():
        if bound > 0:
            byb.setdefault(b, []).append((bound / dim, s_abs / bound))
    for b in sorted(byb):
        rows = byb[b]
        print(f"  {b:>2}     {mp.nstr(sum(r[0] for r in rows)/len(rows),7):>12}     "
              f"{mp.nstr(sum(r[1] for r in rows)/len(rows),4):>10}")

    print("\n   conjugate pairs (dim λ = dim λ' EXACTLY) — does the BOUND decay at equal dim?")
    print("   low-b λ            b   high-b λ'          b'  dim   bound(low)     bound(high)   bound ratio  Σ|eig| ratio")
    seen, rs = set(), []
    for lam in list(cache):
        cj = conjugate(lam)
        if lam == cj or lam in seen or cj in seen or cj not in cache:
            seen.add(lam)
            continue
        seen.add(lam); seen.add(cj)
        lo, hi = (lam, cj) if cache[lam][0] < cache[cj][0] else (cj, lam)
        blo, dlo, Blo, alo = cache[lo]; bhi, dhi, Bhi, ahi = cache[hi]
        assert dlo == dhi, "conjugate dims differ — control broken"
        if Blo == 0 or alo == 0:
            continue
        rs.append(Bhi / Blo)
        print(f"  {str(lo):<18} {blo:>1}   {str(hi):<18} {bhi:>1} {dlo:>4}  {mp.nstr(Blo,7):>11}  "
              f"{mp.nstr(Bhi,7):>13}  {mp.nstr(Bhi/Blo,4):>11}  {mp.nstr(ahi/alo,4):>11}")
    if rs:
        nd = sum(1 for r in rs if r < 1)
        print(f"\n  (3) the BOUND decays at higher b in {nd}/{len(rs)} pairs (max ratio {mp.nstr(max(rs),4)})")
        if all_hold and nd == len(rs):
            print("\n  ⇒ (B) IS A USABLE BOUND: it holds for every λ and it DECAYS with b at controlled")
            print("    dimension. Its right-hand side is a positive trace of an algebra element, and on")
            print("    the hook column that trace has the derived reduced-Burau closed form — so the")
            print("    chain from Σ|eig(M_λ)| down to (n-1)×(n-1) matrices is complete there.")
        elif all_hold:
            print("\n  ⇒ (B) holds but does NOT decay on every pair — it is a valid bound and USELESS")
            print("    for the b-decay theorem. Report that; do not present a non-decaying bound as")
            print("    progress. The Cauchy–Schwarz step (i) is the likely culprit (costs up to √dim).")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, nargs="+", default=[2, 3])
    ap.add_argument("--max-dim", type=int, default=50)
    args = ap.parse_args()
    for A in args.A:
        analyze(A, args.max_dim)
        print()


if __name__ == "__main__":
    main()
