#!/usr/bin/env python3
"""magnus_frobenius_is_positive_trace_probe.py — is the surviving majorant ‖M_λ‖_F itself a TRACE
of an algebra element? (qou-o6ov)

WHERE THIS SITS. The majorant ladder (magnus_majorant_ladder_probe.py) showed the b-decay survives
all the way to √dim·‖M_λ‖_F, M_λ = ρ_λ(ρ)·ρ_λ(Ω₂^P) — so a general-λ theorem can target the
FROBENIUS norm rather than the eigenvalues. This probe asks whether that target is not merely
elementary but STRUCTURALLY the same kind of object the arc already has handles for.

THE CLAIM. ‖M‖_F² = tr(Mᵀ M) always (trivially). The content is whether Mᵀ is again the image of an
ALGEBRA element. The Hecke algebra carries the word-reversal anti-involution
    * : σ_{i1}···σ_{ik} ↦ σ_{ik}···σ_{i1}   (an anti-automorphism, fixing each generator).
IF the seminormal generator matrices are symmetric, ρ_λ(σ_i)ᵀ = ρ_λ(σ_i), then for any word X,
    ρ_λ(X)ᵀ = ρ_λ(σ_{ik})ᵀ···ρ_λ(σ_{i1})ᵀ = ρ_λ(σ_{ik}···σ_{i1}) = ρ_λ(X*),
hence  ‖ρ_λ(X)‖_F² = tr_λ(X* X)  — a trace of a genuine algebra element, and a POSITIVE one
(it is Σσ_i² > 0, so NO cancellation can occur in it).

WHY THAT WOULD MATTER. The arc's two reductions — hooks to the reduced Burau (#6464) and two-rows
to R-matrix weight sectors (#6525) — apply to ANY algebra element, because they are character
identities. They could NOT be applied to the germ (#6432/#6434, rep-specific) but they DO apply to
Ω₂^P (#6445). If ‖M_λ‖_F² = tr_λ(X*X) with X = ρ·Ω₂^P, then the general-λ decay bound reduces to a
POSITIVE trace reachable by exactly those handles — the bound becomes the same kind of object as
the quantity it bounds, one rung down and with no cancellation to fight.

THIS PROBE CHECKS, exactly (mpf, dps 140):
  (1) are the seminormal ρ_λ(σ_i) symmetric?  (the hypothesis — reported per λ, not assumed)
  (2) does ‖M_λ‖_F² equal tr_λ(ρ_λ(X*)·ρ_λ(X)) with X* built by REVERSING the generator word
      of X = ρ·Ω₂^P?  Note Ω₂^P is a sum of commutators, so X* is assembled term by term:
      (ρ·[σ_a,σ_{a+1}])* = [σ_a,σ_{a+1}]*·ρ* = (σ_{a+1}σ_a − σ_aσ_{a+1})·ρ* = −[σ_a,σ_{a+1}]·ρ*.
  (3) is tr_λ(X*X) positive and decaying in b on conjugate pairs (dim λ = dim λ' EXACTLY)?
A failure of (1) is not a failure of the arc — it would mean the anti-involution is implemented by
a different similarity, and (2) reports that directly rather than assuming it.

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
from magnus_curvature_commutator_identity_probe import sigma_dense  # noqa: E402
from magnus_conjugate_pair_cancellation_probe import conjugate  # noqa: E402


def asymmetry(M, dim):
    """max |M - Mᵀ| — 0 iff symmetric."""
    return max(abs(M[i, j] - M[j, i]) for i in range(dim) for j in range(dim))


def build(lam, gens, q, ngen):
    """Return (X, Xstar, dim, max generator asymmetry).

    X      = ρ · Ω₂^P                       as a matrix
    Xstar  = the image of the ALGEBRA element X*, built by reversing every word:
             X* = Σ_a (ρ·[σ_a,σ_{a+1}])* = Σ_a −[σ_a,σ_{a+1}]·ρ*,  ρ* = reversed braid word.
    """
    sig, dim = sigma_dense(lam, q, ngen)
    gen_asym = max(asymmetry(sig[g], dim) for g in range(ngen))

    rho = sig[gens[0]]
    for g in gens[1:]:
        rho = rho * sig[g]
    rho_star = sig[gens[-1]]
    for g in reversed(gens[:-1]):
        rho_star = rho_star * sig[g]

    c = 4 / (q + 1 / q) ** 2
    O = mp.zeros(dim, dim)
    for a in range(ngen - 1):
        O = O + (sig[a] * sig[a + 1] - sig[a + 1] * sig[a])
    X = rho * (c * O)
    # X* = Σ_a −[σ_a,σ_(a+1)]·ρ*  (word reversal is an ANTI-automorphism: reverses products)
    Xstar = (-c) * (O * rho_star)
    return X, Xstar, dim, gen_asym


def analyze(A, max_dim):
    q = base.Q0
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1
    print(f"[frob] A={A} (n={n}); is ‖M_λ‖_F² = tr_λ(X* X),  X = ρ·Ω₂^P,  X* = word reversal?  dim ≤ {max_dim}")
    print(f"[frob] hypothesis tested, NOT assumed: ρ_λ(σ_i) symmetric ⇒ ρ_λ(X)ᵀ = ρ_λ(X*)\n")
    print("   λ                  b   dim   gen asym    ‖M‖_F²        tr(X*X)      |Δ_rel|    positive?")
    cache = {}
    worst = mp.mpf(0)
    worst_asym = mp.mpf(0)
    for lam in base.partitions(n):
        lam = tuple(lam)
        _pg, d = base.block_structure(lam)
        if d > max_dim:
            continue
        X, Xstar, dim, gen_asym = build(lam, gens, q, ngen)
        frob2 = sum(abs(X[i, j]) ** 2 for i in range(dim) for j in range(dim))
        P = Xstar * X
        tr_star = mp.re(sum(P[i, i] for i in range(dim)))
        den = abs(frob2) if abs(frob2) > mp.mpf(10) ** -100 else mp.mpf(1)
        rel = abs(frob2 - tr_star) / den
        worst = max(worst, rel); worst_asym = max(worst_asym, gen_asym)
        b = sum(lam) - lam[0]
        cache[lam] = (b, dim, frob2)
        print(f"  {str(lam):<18} {b:>1}  {dim:>4}  {mp.nstr(gen_asym,3):>9}  {mp.nstr(frob2,8):>12}  "
              f"{mp.nstr(tr_star,8):>12}  {mp.nstr(rel,3):>9}   {'yes' if tr_star >= 0 else 'NO'}")

    print()
    sym = worst_asym < mp.mpf(10) ** -100
    ok = worst < mp.mpf(10) ** -100
    print(f"  (1) seminormal generators symmetric?   {'YES ✓' if sym else 'NO'}  "
          f"(max |σ − σᵀ| = {mp.nstr(worst_asym,3)})")
    print(f"  (2) ‖M_λ‖_F² == tr_λ(X* X) for every λ? {'YES ✓' if ok else 'NO ✗'}  "
          f"(worst |Δ_rel| = {mp.nstr(worst,3)})")

    # (3) does the positive trace decay in b, at controlled dimension?
    print("\n   conjugate pairs — does the POSITIVE trace tr(X*X) = ‖M‖_F² decay at equal dim?")
    print("   low-b λ            b   high-b λ'          b'  dim   ‖M‖_F²(low)   ‖M‖_F²(high)   ratio")
    seen, rs = set(), []
    for lam in list(cache):
        cj = conjugate(lam)
        if lam == cj or lam in seen or cj in seen or cj not in cache:
            seen.add(lam)
            continue
        seen.add(lam); seen.add(cj)
        lo, hi = (lam, cj) if cache[lam][0] < cache[cj][0] else (cj, lam)
        blo, dlo, flo = cache[lo]; bhi, dhi, fhi = cache[hi]
        assert dlo == dhi, "conjugate dims differ — control broken"
        if flo == 0:
            continue
        rs.append(fhi / flo)
        print(f"  {str(lo):<18} {blo:>1}   {str(hi):<18} {bhi:>1} {dlo:>4}   {mp.nstr(flo,7):>12}  "
              f"{mp.nstr(fhi,7):>12}  {mp.nstr(fhi/flo,4):>8}")
    if rs:
        nd = sum(1 for r in rs if r < 1)
        print(f"\n  (3) decays at higher b in {nd}/{len(rs)} pairs (max ratio {mp.nstr(max(rs),4)})")
        if sym and ok and nd == len(rs):
            print("\n  ⇒ CLOSED: the surviving majorant is ‖M_λ‖_F² = tr_λ(X* X) — a trace of a genuine")
            print("    algebra element, POSITIVE (so no cancellation to fight), and decaying in b.")
            print("    The arc's existing handles apply to it verbatim: the reduced-Burau hook")
            print("    reduction (#6464) and the R-matrix weight sectors (#6525) are character")
            print("    identities, valid for ANY algebra element — and X*X is one.")


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
