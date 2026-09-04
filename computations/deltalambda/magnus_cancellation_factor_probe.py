#!/usr/bin/env python3
"""magnus_cancellation_factor_probe.py — QUANTIFY the cancellation: |Σ eig| / Σ|eig| per irrep
(qou-o6ov).

#6548 settled the MECHANISM: the b(λ)-decay of tr_λ(ρ·Ω₂^P) is cancellation, not size — at
identical dimension (conjugate pairs) the high-b partner has ~25% LARGER commutators and a
4x–290x SMALLER trace. This probe measures HOW MUCH cancellation, in the one quantity a spectral
bound must control.

THE MEASURE. Let M_λ = ρ_λ(ρ)·ρ_λ(Ω₂^P), so tr_λ(ρΩ₂^P) = Σ_i eig_i(M_λ). Define

    cancellation factor   κ(λ) := |Σ_i eig_i| / Σ_i |eig_i|   ∈ [0, 1]

κ = 1 iff every eigenvalue has the same phase (no cancellation: the trace is as big as its parts
allow). κ → 0 is total cancellation. Σ|eig| is the natural "no-cancellation comparator" FOR A
TRACE — it is what |tr| would be if nothing cancelled. (Note Σ|eig| is not the nuclear norm for a
non-normal M; it is nonetheless the right comparator here, because the trace is exactly Σ eig and
the question is purely one of phase alignment among those eigenvalues.)

WHAT THIS DISTINGUISHES, and why it is not a restatement of #6548:
  #6548 compared |tr| against a NORM OF THE INPUT (‖[ρ,σ_a]‖) and found the norm does not fall.
  κ compares |tr| against the SPECTRUM OF THE OUTPUT operator. So:
    - Σ|eig| roughly flat in b, κ falling  ⇒ the decay is entirely phase cancellation among the
      eigenvalues of M_λ; any bound that passes through |·| on those eigenvalues (Σ|eig|,
      spectral radius × dim, …) CANNOT decay, and a general-λ bound must track signed/phase
      structure — a much sharper constraint than #6548.
    - Σ|eig| itself falling with b ⇒ the decay is (partly) in the output spectrum after all, and
      an absolute-value spectral bound on M_λ is viable even though one on ‖[ρ,σ_a]‖ is not.
  These are genuinely different outcomes; #6548 does not predict which.

Reports κ, Σ|eig|/dim, |tr|/dim per λ, plus the conjugate-pair κ ratio (the dimension-controlled
comparison, dim λ = dim λ' exactly). scope-(a); NO-FLOAT64 (mpf, dps 140). Nothing wired.
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


def curvature_operator(lam, gens, q, ngen):
    """M_λ = ρ_λ(ρ)·ρ_λ(Ω₂^P), with Ω₂^P = (4/[2]²)Σ_a[σ_a,σ_(a+1)]. Returns (M, dim)."""
    sig, dim = sigma_dense(lam, q, ngen)
    rho = sig[gens[0]]
    for g in gens[1:]:
        rho = rho * sig[g]
    O = mp.zeros(dim, dim)
    for a in range(ngen - 1):
        O = O + (sig[a] * sig[a + 1] - sig[a + 1] * sig[a])
    return rho * ((4 / (q + 1 / q) ** 2) * O), dim


def kappa(lam, gens, q, ngen):
    """(κ, Σ|eig|, |tr|, dim) — κ = |Σ eig| / Σ|eig| ∈ [0,1]."""
    M, dim = curvature_operator(lam, gens, q, ngen)
    E, _ = mp.eig(M)
    s_abs = sum(abs(e) for e in E)
    s_sum = abs(sum(E))
    k = (s_sum / s_abs) if s_abs > mp.mpf(10) ** -100 else mp.mpf(0)
    return k, s_abs, s_sum, dim


def analyze(A, max_dim):
    q = base.Q0
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1
    print(f"[kappa] A={A} (n={n}); κ(λ) = |Σ eig(M_λ)| / Σ|eig(M_λ)|,  M_λ = ρ_λ(ρ)·ρ_λ(Ω₂^P); dim ≤ {max_dim}")
    print(f"[kappa] κ=1 ⇒ no cancellation.  κ→0 ⇒ total cancellation.\n")
    print("   λ                  b   dim    Σ|eig|/dim      |tr|/dim        κ")
    data = {}
    for lam in base.partitions(n):
        lam = tuple(lam)
        _pg, d = base.block_structure(lam)
        if d > max_dim:
            continue
        k, s_abs, s_sum, dim = kappa(lam, gens, q, ngen)
        b = sum(lam) - lam[0]
        data[lam] = (b, dim, s_abs, s_sum, k)
        print(f"  {str(lam):<18} {b:>1}  {dim:>4}   {mp.nstr(s_abs/dim,7):>12}  "
              f"{mp.nstr(s_sum/dim,7):>12}  {mp.nstr(k,6):>9}")

    # Is Σ|eig|/dim flat-ish in b while κ falls? Group by b.
    print("\n   b    mean Σ|eig|/dim    mean κ      (shapes)")
    byb = {}
    for lam, (b, dim, s_abs, s_sum, k) in data.items():
        byb.setdefault(b, []).append((s_abs / dim, k))
    for b in sorted(byb):
        rows = byb[b]
        m_abs = sum(r[0] for r in rows) / len(rows)
        m_k = sum(r[1] for r in rows) / len(rows)
        print(f"  {b:>2}    {mp.nstr(m_abs,7):>12}    {mp.nstr(m_k,6):>8}      {len(rows)}")

    # dimension-controlled: conjugate pairs
    print("\n   conjugate pairs (dim λ = dim λ' EXACTLY) — κ and Σ|eig| at equal dimension")
    print("   low-b λ            b   high-b λ'          b'   dim   κ(low)     κ(high)   κ ratio   Σ|eig| ratio")
    seen, pairs = set(), []
    for lam in list(data):
        cj = conjugate(lam)
        if lam == cj or lam in seen or cj in seen or cj not in data:
            seen.add(lam)
            continue
        seen.add(lam); seen.add(cj)
        b1, b2 = data[lam][0], data[cj][0]
        lo, hi = (lam, cj) if b1 < b2 else (cj, lam)
        (blo, dlo, alo, _slo, klo) = data[lo]
        (bhi, dhi, ahi, _shi, khi) = data[hi]
        assert dlo == dhi, "conjugate dims differ — control broken"
        if klo == 0 or alo == 0:
            continue
        pairs.append((klo, khi, ahi / alo))
        print(f"  {str(lo):<18} {blo:>1}   {str(hi):<18} {bhi:>1}  {dlo:>4}   "
              f"{mp.nstr(klo,5):>8}  {mp.nstr(khi,5):>8}  {mp.nstr(khi/klo,4):>8}   {mp.nstr(ahi/alo,4):>8}")

    print()
    if pairs:
        n_k_down = sum(1 for klo, khi, _ in pairs if khi < klo)
        n_abs_up = sum(1 for _, _, ar in pairs if ar >= 1)
        print(f"  pairs: {len(pairs)};  κ falls at higher b in {n_k_down}/{len(pairs)};  "
              f"Σ|eig| non-decreasing in {n_abs_up}/{len(pairs)}")
        if n_k_down == len(pairs) and n_abs_up == len(pairs):
            print("  ⇒ PHASE CANCELLATION, sharply: at equal dimension the high-b partner has a")
            print("    LARGER total |eigenvalue| mass and a SMALLER κ. So no bound passing through")
            print("    |eig| of M_λ (Σ|eig|, spectral radius × dim) can decay — a general-λ bound")
            print("    must track the PHASES, which is stronger than #6548's exclusion of ‖[ρ,σ_a]‖.")
        elif n_k_down == len(pairs):
            print("  ⇒ κ falls at higher b in every pair, but Σ|eig| also falls somewhere: part of")
            print("    the decay IS in the output spectrum, so an absolute-value spectral bound on")
            print("    M_λ stays viable even though the input-norm route (#6548) is excluded.")
        else:
            print("  ⇒ κ does NOT fall uniformly — report this: the cancellation reading does not")
            print("    survive the dimension-controlled test in this form.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, nargs="+", default=[2, 3])
    ap.add_argument("--max-dim", type=int, default=50,
                    help="skip irreps above this dim (eig is O(dim³)); skipped shapes are NOT evidence")
    args = ap.parse_args()
    for A in args.A:
        analyze(A, args.max_dim)
        print()


if __name__ == "__main__":
    main()
