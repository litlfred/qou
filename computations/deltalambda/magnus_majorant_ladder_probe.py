#!/usr/bin/env python3
"""magnus_majorant_ladder_probe.py — WHICH computable majorant of the curvature trace decays with
b(λ)? The ladder |tr| ≤ Σ|eig| ≤ Σσ ≤ √dim·‖M‖_F (qou-o6ov).

WHERE THIS SITS. #6548: the decay is not in the INPUT norm ‖[ρ,σ_a]‖ (which GROWS ~25% at high b),
so a term-by-term input bound cannot work. #6556: the decay factorizes as |tr| = κ·Σ|eig| and the
MAGNITUDE factor Σ|eig(M_λ)| dominates, M_λ = ρ_λ(ρ)·ρ_λ(Ω₂^P) — so an absolute-value spectral
bound on the assembled M_λ is viable.

BUT Σ|eig| IS NOT A BOUND — it is the quantity. A theorem needs a computable majorant that (a)
dominates |tr| and (b) still decays. The standard ladder, each step a classical inequality:

    |tr M| ≤ Σ_i |eig_i(M)|          (triangle inequality on the trace)
           ≤ Σ_i σ_i(M)              (Weyl: eigenvalue moduli are majorized by singular values)
           ≤ √dim · ‖M‖_F            (Cauchy–Schwarz on Σσ, since ‖M‖_F² = Σσ_i²)
    and separately  Σ_i|eig_i| ≤ dim · ϱ(M)   (ϱ = spectral radius)

Each rung is progressively cheaper to bound analytically and progressively weaker. THE QUESTION:
how far up the ladder does the b-decay survive? The answer says which object a general-λ theorem
should target — and ‖M‖_F is elementary (a sum of squared entries) where eigenvalues are not.

MEASURED on conjugate pairs (dim λ = dim λ' EXACTLY — the dimension confound removed by a theorem,
not by normalisation), reporting each rung's high-b/low-b ratio. A rung with ratio < 1 still
decays; the FIRST rung with ratio ≥ 1 is where the b-information is destroyed, and every rung above
it is useless for the theorem.

scope-(a); NO-FLOAT64 (mpf, dps 140). No fit, no witness, nothing wired.
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
from magnus_cancellation_factor_probe import curvature_operator  # noqa: E402
from magnus_conjugate_pair_cancellation_probe import conjugate  # noqa: E402


def rungs(lam, gens, q, ngen):
    """(|tr|, Σ|eig|, Σσ, √dim·‖M‖_F, dim·ϱ, dim) for M_λ — the majorant ladder, in order."""
    M, dim = curvature_operator(lam, gens, q, ngen)
    E, _ = mp.eig(M)
    tr = abs(sum(E))
    s_eig = sum(abs(e) for e in E)
    rho_spec = max(abs(e) for e in E)
    # singular values: σ² = eigenvalues of Mᴴ M (Hermitian PSD ⇒ real, non-negative)
    MH = M.transpose_conj() * M
    EH, _ = mp.eig(MH)
    sig = [mp.sqrt(max(mp.re(x), mp.mpf(0))) for x in EH]
    s_sing = sum(sig)
    frob = mp.sqrt(sum(abs(M[i, j]) ** 2 for i in range(dim) for j in range(dim)))
    return tr, s_eig, s_sing, mp.sqrt(dim) * frob, dim * rho_spec, dim


LABELS = ["|tr|", "Σ|eig|", "Σσ", "√dim·‖M‖_F", "dim·ϱ"]


def analyze(A, max_dim):
    q = base.Q0
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1
    print(f"[ladder] A={A} (n={n}); majorant ladder on conjugate pairs, dim ≤ {max_dim}")
    print(f"[ladder] |tr| ≤ Σ|eig| ≤ Σσ ≤ √dim·‖M‖_F ;  also Σ|eig| ≤ dim·ϱ.  "
          f"Ratio = high-b / low-b at EQUAL dim.")
    print(f"[ladder] ratio < 1 ⇒ that rung still decays.  First rung ≥ 1 ⇒ b-information destroyed there.\n")

    cache = {}
    for lam in base.partitions(n):
        lam = tuple(lam)
        _pg, d = base.block_structure(lam)
        if d > max_dim:
            continue
        cache[lam] = rungs(lam, gens, q, ngen)

    print("   low-b λ            b   high-b λ'          b'  dim " + "".join(f"{l:>14}" for l in LABELS))
    seen, ratios = set(), []
    for lam in list(cache):
        cj = conjugate(lam)
        if lam == cj or lam in seen or cj in seen or cj not in cache:
            seen.add(lam)
            continue
        seen.add(lam); seen.add(cj)
        b1 = sum(lam) - lam[0]; b2 = sum(cj) - cj[0]
        lo, hi = (lam, cj) if b1 < b2 else (cj, lam)
        vlo, vhi = cache[lo], cache[hi]
        assert vlo[5] == vhi[5], "conjugate dims differ — control broken"
        if any(v == 0 for v in vlo[:5]):
            continue                      # trivial/sign: all rungs 0, no ratio
        r = [vhi[i] / vlo[i] for i in range(5)]
        ratios.append(r)
        print(f"  {str(lo):<18} {sum(lo)-lo[0]:>1}   {str(hi):<18} {sum(hi)-hi[0]:>1} {vlo[5]:>4} "
              + "".join(f"{mp.nstr(x,4):>14}" for x in r))

    if not ratios:
        print("\n  no pairs under the dim cap — raise --max-dim")
        return
    print("\n   rung            pairs decaying (ratio < 1)     max ratio")
    first_bad = None
    for i, lab in enumerate(LABELS):
        dec = sum(1 for r in ratios if r[i] < 1)
        mx = max(r[i] for r in ratios)
        print(f"  {lab:<14}  {dec}/{len(ratios)}{'':>22}{mp.nstr(mx,4):>10}")
        if dec < len(ratios) and first_bad is None:
            first_bad = lab
    print()
    if first_bad is None:
        print("  ⇒ EVERY rung decays, up to √dim·‖M‖_F and dim·ϱ. The b-information survives all the")
        print("    way to the FROBENIUS norm of the assembled M_λ — an elementary quantity (a sum of")
        print("    squared entries, no eigenvalues). That is the object a general-λ theorem should")
        print("    bound: |tr_λ(ρΩ₂^P)| ≤ √dim·‖M_λ‖_F with the right-hand side decaying in b.")
    else:
        print(f"  ⇒ the ladder breaks at '{first_bad}': that rung does NOT decay on every pair, so it")
        print(f"    and everything above it are useless for a general-λ bound. The theorem must")
        print(f"    target a rung BELOW it — the last one that still carries the b-decay.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, nargs="+", default=[2, 3])
    ap.add_argument("--max-dim", type=int, default=50,
                    help="skip irreps above this dim (two eig solves + SVD, O(dim³) mpf); "
                         "skipped shapes are NOT evidence either way")
    args = ap.parse_args()
    for A in args.A:
        analyze(A, args.max_dim)
        print()


if __name__ == "__main__":
    main()
