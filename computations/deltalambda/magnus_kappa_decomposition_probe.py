#!/usr/bin/env python3
"""magnus_kappa_decomposition_probe.py — split the b-decay into its two factors, on the complete
n=9 census. (qou-o6ov)

THE GAP THIS LOCALISES. #6754 measured, end to end, that the actual |tr_λ(ρΩ₂^P)|/dim_λ envelope
falls 189× across b=1..7 while the derived bound falls only 12.2×. The missing ~15× has to live
somewhere, and there is exactly one place it can: the step that replaces a SIGNED trace by a norm.
Write the target as a product of two factors,

    |tr_λ(X)|  =  κ(λ) · Σ_i |eig_i(X)|,        κ(λ) := |Σ_i eig_i| / Σ_i |eig_i|            (κ)

with κ ∈ [0,1] the CANCELLATION FACTOR — how much the eigenvalues cancel in the sum. Then

    |tr_λ|/dim_λ  =  κ(λ) · ( Σ|eig|/dim_λ ),   and   Σ|eig|/dim_λ ≤ √( tr_λ(X*X)/dim_λ )

so the 189× is (κ's decay) × (the magnitude factor's decay), and the bound in #6754 captures only
the second. THE QUESTION: does κ itself decay with b?

  YES → the missing factor is localised, and "keep the sign information" becomes the sharp
        sub-problem "bound κ(λ)" — a scalar in [0,1] with a clear meaning.
  NO  → the phase-cancellation story is wrong, the missing 15× is in the Cauchy–Schwarz step
        (Σ|eig| vs √(dim·Σ|eig|²)) instead, and the route to a tighter bound is a different one.

Either answer is worth the run; the probe reports which without preferring one.

WHY THIS HAS NEVER BEEN MEASURED. κ needs EIGENVALUES, and nothing else in this arc does — the
sparse column-wise kernel exists precisely to avoid them. Measured cost of mp.eig at dps 65:
9.9 s at dim 42, 15.4 s at dim 48, 153.9 s at dim 105, i.e. ~dim³, projecting to ~22 min at dim 216
and ~1h45m for the complete census. #6556 built a κ probe but only ever ran it on a dim-capped
sample, so κ has never been seen across a complete level — and a κ envelope over a capped subset
is not an envelope.

THREE FACTORS ARE REPORTED SEPARATELY, because collapsing them is how the 189× got attributed to
the wrong step in the first place:
    κ                       cancellation among eigenvalues (what a norm bound throws away)
    Σ|eig| / dim            the magnitude factor
    √(tr(X*X)/dim)          the Cauchy–Schwarz relaxation of the magnitude factor
Their product-of-envelopes must reproduce #6754's numbers; the probe checks that rather than
assuming it, since a decomposition that does not recompose is a bookkeeping error.

scope-(a); NO-FLOAT64 (mpf; dps asserted at every compute entry). Nothing wired.
"""
from __future__ import annotations

import argparse
import os
import sys
import time

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))  # computations/

import mpmath as mp  # noqa: E402

import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402

_WANT_DPS = None


def _assert_dps(where):
    if _WANT_DPS is not None and mp.mp.dps != _WANT_DPS:
        raise RuntimeError(f"mp.mp.dps is {mp.mp.dps}, expected {_WANT_DPS}, at {where}")


def build_X_dense(lam, gens, q, ngen):
    """X = ρ·Ω₂^P as a dense mp.matrix, assembled COLUMN-WISE from the sparse kernel.

    The assembly is cheap (0.4 s at dim 48, 2.1 s at dim 105); the eigenvalue solve is what costs.
    Building X by dense products instead would reintroduce the cost the sparse kernel removed —
    the dim cap of this whole arc was exactly that mistake (#6729).
    """
    _assert_dps(f"build_X_dense({lam})")
    per_gen, dim = base.block_structure(tuple(lam))
    sig = base.sigma_csr(per_gen, dim, q)
    c = 4 / (q + 1 / q) ** 2
    rev = list(reversed(gens))
    M = mp.matrix(dim, dim)
    for j in range(dim):
        e = [mp.mpf(0)] * dim
        e[j] = mp.mpf(1)
        acc = [mp.mpf(0)] * dim
        for a in range(ngen - 1):
            u = base.spmatvec(sig[a], base.spmatvec(sig[a + 1], e))
            w = base.spmatvec(sig[a + 1], base.spmatvec(sig[a], e))
            for r in range(dim):
                acc[r] += u[r] - w[r]
        v = [c * x for x in acc]
        for g in rev:
            v = base.spmatvec(sig[g], v)
        for i in range(dim):
            M[i, j] = v[i]
    return M, dim


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, default=3)
    ap.add_argument("--dps", type=int, default=65)
    ap.add_argument("--max-dim", type=int, default=250)
    args = ap.parse_args()
    global _WANT_DPS
    _WANT_DPS = args.dps
    mp.mp.dps = args.dps

    q = base.Q0
    A = args.A
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1

    print(f"[kappa] n={n}: |tr| = κ·Σ|eig|, κ = |Σeig|/Σ|eig| — does the CANCELLATION decay with b?")
    print(f"[kappa] #6754: actual |tr|/dim falls 189×, the derived bound only 12.2×. This says")
    print(f"[kappa] where the missing ~15× lives.  (mp.dps = {args.dps}; eig is ~dim³)\n")
    print("     b   λ                        dim       κ        Σ|eig|/dim   √(F/dim)   |tr|/dim"
          "     eig s")

    rows, skipped = [], []
    for lam in base.partitions(n):
        lam = tuple(lam)
        _pg, d = base.block_structure(lam)
        if d > args.max_dim:
            skipped.append((lam, d))
            continue
        if d == 1:
            continue                                    # exact-zero endpoints
        M, dim = build_X_dense(lam, gens, q, ngen)
        t0 = time.time()
        E, _ = mp.eig(M)
        el = time.time() - t0
        tr = mp.re(sum(M[i, i] for i in range(dim)))
        s_abs = sum(abs(x) for x in E)
        frob = sum(abs(M[i, j]) ** 2 for i in range(dim) for j in range(dim))
        kappa = abs(tr) / s_abs if s_abs > 0 else mp.mpf(0)
        b = sum(lam) - lam[0]
        rows.append((b, lam, dim, kappa, s_abs / dim, mp.sqrt(frob / dim), abs(tr) / dim))
        print(f"    {b:>2}   {str(lam):<24} {dim:>4}  {mp.nstr(kappa,7):>10}  "
              f"{mp.nstr(s_abs/dim,7):>11}  {mp.nstr(mp.sqrt(frob/dim),7):>10}  "
              f"{mp.nstr(abs(tr)/dim,7):>10}  {el:>7.0f}", flush=True)

    # --- envelopes, per factor, over the levels present ---
    def env(idx, hi=True):
        e = {}
        for r in rows:
            b = r[0]
            e[b] = max(e.get(b, mp.mpf(0)), r[idx]) if hi else min(e.get(b, mp.mpf("inf")), r[idx])
        return e

    ek, es, ef, et = env(3), env(4), env(5), env(6)
    bs = sorted(et)
    print(f"\n     b   κ envelope   Σ|eig|/dim env   √(F/dim) env   |tr|/dim env")
    for b in bs:
        print(f"    {b:>2}  {mp.nstr(ek[b],7):>11}  {mp.nstr(es[b],7):>14}  "
              f"{mp.nstr(ef[b],7):>13}  {mp.nstr(et[b],7):>13}")

    def fall(e):
        return e[bs[0]] / e[bs[-1]] if e[bs[-1]] > 0 else mp.mpf("inf")

    mono_k = all(ek[bs[i + 1]] < ek[bs[i]] for i in range(len(bs) - 1))
    print(f"\n  κ envelope strictly decreasing in b?  {'YES ✓' if mono_k else 'NO'}")
    print(f"  falls across b={bs[0]}..{bs[-1]}:   κ {mp.nstr(fall(ek),5)}×   "
          f"Σ|eig|/dim {mp.nstr(fall(es),5)}×   √(F/dim) {mp.nstr(fall(ef),5)}×   "
          f"|tr|/dim {mp.nstr(fall(et),5)}×")

    # DOES THE DECOMPOSITION RECOMPOSE? A split that does not multiply back is a bookkeeping
    # error, and checking it is what separates a real localisation from a plausible story.
    prod = fall(ek) * fall(es)
    print(f"\n  RECOMPOSITION CHECK: κ-fall × Σ|eig|-fall = {mp.nstr(prod,6)}  vs  |tr|-fall "
          f"{mp.nstr(fall(et),6)}")
    print("    (these are envelopes of a product, not a product of envelopes, so they need NOT")
    print("     agree exactly — a large discrepancy would mean the extremes are attained on")
    print("     different shapes, which is itself worth knowing.)")

    if mono_k:
        print(f"\n  ⇒ κ DOES decay with b. The missing factor is localised: 'keep the sign")
        print("    information' becomes the sharp sub-problem 'bound κ(λ)', a scalar in [0,1].")
    else:
        print(f"\n  ⇒ κ does NOT decay monotonically. The phase-cancellation story is wrong as")
        print("    stated, and the missing factor is in the Cauchy–Schwarz step instead. Report")
        print("    that; do not keep looking for a κ bound that the data says is not there.")
    if skipped:
        print(f"\n  SKIPPED {len(skipped)} shape(s) over --max-dim (NOT evidence — just not run): "
              + ", ".join(f"{l}({d})" for l, d in skipped[:5]))


if __name__ == "__main__":
    main()
