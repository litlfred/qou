#!/usr/bin/env python3
"""magnus_extreme_rep_endpoint_probe.py — the b-decay TERMINATES at an exact zero (qou-o6ov).

CONTEXT. The whole arc (#6311→#6372) studies the decay of tr(ρ_λ ⁅A_a,A_{a+1}⁆) as b(λ)=n−λ_1
grows. Every probe skipped dim≤1 partitions, so it never looked at the ENDPOINT. But the two
extreme partitions are 1-dimensional:
  * λ=(n)   → the TRIVIAL rep,  dim 1,  b=0        (each σ_i = q scalar)
  * λ=(1ⁿ)  → the SIGN rep,     dim 1,  b=n−1 (MAXIMAL b)  (each σ_i = −q⁻¹ scalar)
In ANY 1-dim rep the algebra is commutative, so ⁅A_a,A_{a+1}⁆ = 0 (an instance of the
sorry-free Lean lemma QOU.MassTheory.commutator_eq_zero_of_commute), hence tr(ρ_λ Ω₂) = 0
EXACTLY. So the b→max decay does not approach a mysterious asymptote — it terminates at a
PROVABLE zero at the fully-antisymmetric endpoint.

WHY THIS MATTERS. Under Schur–Weyl duality the b-grading of Hecke H_n(q) irreps is dual to a
U_q(gl_N) rep grading; the sign rep λ=(1ⁿ) is the fully-antisymmetric/determinant sector,
which is exactly the Alexander-polynomial sector of the loop expansion (Melvin–Morton–Rozansky).
So the decay endpoint sits in the semiclassical/Alexander corner — a concrete anchor for the
Garoufalidis–Le zeta reformulation (#6372), and the reason the trace must vanish there.

This probe confirms the endpoint numerically for the QOU atoms and reports the near-endpoint
approach (the smallest genuinely-multidim reps at high b). scope-(a); NO-FLOAT64 (mpf,
dps=140). No fit, no witness, nothing wired.
"""
from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import mpmath as mp  # noqa: E402
import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402


def omega2_trace(shape, gens):
    """tr(ρ_λ · Ω₂) with Ω₂ = Σ_{|g−h|=1} ⁅A_g,A_h⁆, matrix-free-ish via row-dicts.
    Returns (trace, dim)."""
    per_gen, dim = base.block_structure(shape)
    ngen = max(gens) + 1
    sig = base.sigma_csr(per_gen, dim, base.Q0)
    germ_rows, hcheck = base.germ_csr(per_gen, dim, base.Q0, base.EPS)
    assert hcheck < mp.mpf(10) ** -55
    ad = {g: base.csr_to_dict(germ_rows[g]) for g in range(ngen)}
    sd = {g: base.csr_to_dict(sig[g]) for g in range(ngen)}
    # ρ = ∏ σ_{g_i}
    rho = sd[gens[0]]
    for g in gens[1:]:
        rho = base.spmatmul(rho, sd[g])
    # Ω₂ = Σ adjacent commutators
    O = {}
    for a in range(ngen - 1):
        C = base.commutator(ad[a], ad[a + 1])
        for i, row in C.items():
            orow = O.setdefault(i, {})
            for j, v in row.items():
                orow[j] = orow.get(j, mp.mpf(0)) + v
    # tr(ρ·O)
    tr = mp.mpf(0)
    for i, arow in rho.items():
        for k, av in arow.items():
            brow = O.get(k)
            if brow and i in brow:
                tr += av * brow[i]
    return tr, dim


def analyze(A):
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    print(f"[endpoint] A={A} (n={n})")

    # the two 1-dim extreme reps
    trivial = tuple([n])          # λ=(n),  b=0
    sign = tuple([1] * n)         # λ=(1ⁿ), b=n−1 (max)
    for name, shape in [("trivial λ=(n)    b=0   ", trivial), (f"sign    λ=(1^{n}) b={n-1} (MAX)", sign)]:
        tr, dim = omega2_trace(shape, gens)
        ok = "EXACT ZERO ✓" if abs(tr) < mp.mpf(10) ** -100 else f"NONZERO ✗ ({mp.nstr(tr,4)})"
        print(f"  {name}: dim={dim}  tr(ρ_λ Ω₂) = {mp.nstr(tr,3):>10}   {ok}")

    # near-endpoint approach: the highest-b partitions that are NOT 1-dim (smallest dim at high b)
    print("  near-endpoint approach (high-b, low-dim reps):")
    recs = []
    for shape in base.partitions(n):
        _pg, dim = base.block_structure(shape)
        if dim <= 1:
            continue
        b = n - shape[0]
        recs.append((b, dim, shape))
    # show the 4 highest-b multidim reps
    for b, dim, shape in sorted(recs, key=lambda r: (-r[0], r[1]))[:4]:
        tr, _ = omega2_trace(shape, gens)
        print(f"    λ={shape!s:<20} b={b:>2} dim={dim:>4}  |tr(ρ_λ Ω₂)|/dim = "
              f"{mp.nstr(abs(tr)/dim,4)}")

    print("  ⇒ the decay terminates at tr=0 EXACTLY at the sign rep (b=n−1, dim 1);")
    print("    structural reason: ⁅A_a,A_{a+1}⁆=0 in any 1-dim (commutative) rep.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, default=3)
    args = ap.parse_args()
    analyze(A=args.A)


if __name__ == "__main__":
    main()
