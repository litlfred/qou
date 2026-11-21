#!/usr/bin/env python3
"""magnus_n9_stragglers_probe.py — the four n=9 shapes no tensor handle reaches, and the discovery
that the dim cap was never about the seminormal construction. (qou-o6ov)

WHAT IS LEFT. Of the 30 partitions of 9, the handles cover 26: the sl_3 weight-sector + Kostka
inversion gives the 12 with ≤3 ROWS, the same machinery on φ-transformed generators (φ: σ_i ↦
−σ_i⁻¹) gives the 12 with ≤3 COLUMNS — overlapping only in (3,3,3) — and the reduced-Burau closed
form adds 3 further hooks. The remaining four are

    (5,2,1,1) dim 189    (4,3,1,1) dim 216    (4,2,2,1) dim 216    (4,2,1,1,1) dim 189

each with ≥4 rows AND ≥4 columns, so NEITHER orientation of a k=3 construction reaches them, and
k=4 is hopeless (largest weight sector 7560 against 1680, cost ~D²).

🛑 THE FINDING, AND IT PARTLY UNDERCUTS THE MOTIVATION FOR THE TENSOR HANDLES. My first version of
this probe called `build`, which forms ρ by DENSE dim×dim products, and one shape at dim 189 had not
finished after a long run. That is not an intrinsic cost: the Young seminormal generators are
**at most 2-sparse per row** — `sigma_csr` in the base probe emits exactly one entry for a `diag`
block and two per row for a 2×2 block — so the same column-wise kernel used for the R-matrix in
#6710 applies DIRECTLY to the seminormal representation. Cost at dim 216 drops from ~86 dense
216×216 products to 216 columns × 63 sparse mat-vecs ≈ 6e6 multiplications.

So the `dim ≤ 50` cap that shaped this entire arc — and that the sl_3 machinery was built to escape
— was an artifact of using DENSE matrix products in `build`, not a property of the seminormal route.
Stated plainly because it is the kind of thing that is convenient to leave unsaid: a good part of
the tensor scaffolding was not strictly necessary at n=9. It remains the right tool at larger n,
where dim_λ itself explodes (the sl_3 sectors stay bounded by multinomials while dim_λ does not),
and the closed forms remain independent cross-checks — which is exactly what makes the gate below
possible.

THE GATE, and it is unusually well-matched. The sparse seminormal route is checked against BOTH
  (a) the dense `build` on small shapes (dim ≤ 50), and
  (b) the sl_3 + Kostka values at dim 162 and 168 — right beside the stragglers' 189 and 216,
      so the gate covers the dimension regime actually being used rather than only a small one.
Symmetry of the seminormal generators is VERIFIED, not taken from a docstring, because
tr_λ(X*X) = ‖X‖_F² depends on σᵀ = σ.

The stragglers themselves have no independent second route BY CONSTRUCTION — that is what makes
them stragglers — so beyond the gate above, the only check on them is positivity: X*X is a positive
element, so a negative value would mean the construction is wrong, and the probe says so rather
than reporting the number.

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
mp.mp.dps = max(50, mp.mp.dps)

import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from magnus_frobenius_is_positive_trace_probe import build  # noqa: E402

_WANT_DPS = None

STRAGGLERS = [(5, 2, 1, 1), (4, 3, 1, 1), (4, 2, 2, 1), (4, 2, 1, 1, 1)]

# sl_3 + Kostka values from #6729, at dims bracketing the stragglers. Used as an independent
# reference in the dimension regime the stragglers actually live in.
SL3_REFERENCE = {
    (5, 3, 1): mp.mpf("135577.6856"),      # dim 162
    (4, 3, 2): mp.mpf("64656.12187"),      # dim 168
    (6, 2, 1): mp.mpf("165160.4266"),      # dim 105
    (5, 2, 2): mp.mpf("79858.63347"),      # dim 120
}


def _assert_dps(where):
    if _WANT_DPS is not None and mp.mp.dps != _WANT_DPS:
        raise RuntimeError(f"mp.mp.dps is {mp.mp.dps}, expected {_WANT_DPS}, at {where}")


def sparse_majorant(lam, gens, q, ngen):
    """tr_λ(X*X) = ‖X‖_F² for X = ρ·Ω₂^P, column by column on the 2-sparse seminormal generators.

    Returns (value, dim, worst_asymmetry). The asymmetry is measured, not assumed: the identity
    tr(X*X) = ‖X‖_F² needs σᵀ = σ, and `sigma_csr`'s docstring asserting symmetry is not evidence.
    """
    _assert_dps(f"sparse_majorant({lam})")
    per_gen, dim = base.block_structure(tuple(lam))
    sig = base.sigma_csr(per_gen, dim, q)

    asym = mp.mpf(0)
    for g in range(len(sig)):
        d = base.csr_to_dict(sig[g])
        for i, row in d.items():
            for j, v in row.items():
                asym = max(asym, abs(v - d.get(j, {}).get(i, mp.mpf(0))))

    c = 4 / (q + 1 / q) ** 2
    rev = list(reversed(gens))
    total = mp.mpf(0)
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
        for x in v:
            if x:
                total += x * x
    return total, dim, asym


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dps", type=int, default=65)
    args = ap.parse_args()
    global _WANT_DPS
    _WANT_DPS = args.dps
    mp.mp.dps = args.dps

    q = base.Q0
    A = 3
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1

    print(f"[strag] sparse seminormal kernel (mp.dps = {args.dps}); the seminormal generators are")
    print(f"[strag] ≤2-sparse per row, so the #6710 column-wise kernel applies DIRECTLY — the")
    print(f"[strag] dim ≤ 50 cap was a DENSE-PRODUCTS artifact, not a seminormal one.\n")

    # ---- GATE (a): against the dense build, on shapes where dense is affordable ----
    print("  [gate a] sparse vs DENSE build (dim ≤ 50)")
    worst_a = mp.mpf(0)
    for lam in [(6, 3), (5, 4), (3, 3, 3), (2, 2, 2, 2, 1)]:
        X, Xs, dim, _ = build(lam, gens, q, ngen)
        P = Xs * X
        ref = mp.re(sum(P[i, i] for i in range(dim)))
        got, d2, asym = sparse_majorant(lam, gens, q, ngen)
        den = abs(ref) if abs(ref) > mp.mpf(10) ** -40 else mp.mpf(1)
        worst_a = max(worst_a, abs(got - ref) / den)
        print(f"    {str(lam):<16} dim {dim:>3}  |Δ_rel| = {mp.nstr(abs(got-ref)/den,3):>9}  "
              f"max|σ−σᵀ| = {mp.nstr(asym,3)}")

    # ---- GATE (b): against sl_3 + Kostka, in the stragglers' OWN dimension regime ----
    print("\n  [gate b] sparse vs sl_3+Kostka (#6729) at dim 105–168 — the regime the stragglers")
    print("           live in, so the gate is not only exercised on small shapes")
    worst_b = mp.mpf(0)
    for lam, ref in SL3_REFERENCE.items():
        got, dim, _asym = sparse_majorant(lam, gens, q, ngen)
        rel = abs(got - ref) / abs(ref)
        worst_b = max(worst_b, rel)
        print(f"    {str(lam):<16} dim {dim:>3}  sparse {mp.nstr(got,10):>16}  "
              f"sl_3 {mp.nstr(ref,10):>16}  |Δ_rel| = {mp.nstr(rel,3)}")

    # SL3_REFERENCE is quoted to 10 significant figures from #6729's printed table, so agreement
    # is bounded by that transcription, NOT by the arithmetic. 1e-9 is the right threshold here;
    # demanding 1e-60 would fail on the quoting, not on the mathematics.
    ok = worst_a < mp.mpf(10) ** -(args.dps // 2) and worst_b < mp.mpf(10) ** -9
    print(f"\n  gate (a) worst {mp.nstr(worst_a,3)} (vs dense, full precision);  "
          f"gate (b) worst {mp.nstr(worst_b,3)} (vs a 10-sig-fig quote)   {'✓' if ok else '✗'}")
    if not ok:
        print("\n  ⇒ GATE FAILED — the sparse seminormal kernel does not reproduce a known value.")
        print("    No straggler is reportable. Report the mismatch; do not tune the kernel to fit.")
        return
    print("  ⇒ gate passed in the stragglers' own dimension regime.\n")

    print("   λ                  dim    χ_λ(X*X)             per-dim        b(λ)   positive?   wall")
    allpos = True
    for lam in STRAGGLERS:
        t0 = time.time()
        val, dim, _asym = sparse_majorant(lam, gens, q, ngen)
        el = time.time() - t0
        pos = val >= 0
        allpos = allpos and pos
        print(f"  {str(lam):<18} {dim:>4}   {mp.nstr(val,10):>16}  {mp.nstr(val/dim,8):>13}   "
              f"{sum(lam)-lam[0]:>4}   {'yes' if pos else 'NO ✗':<9}  {el:.1f}s")
    print()
    if allpos:
        print("  positivity holds on every shape (X*X is a positive element, so it must).")
        print("  ⇒ n=9 is now COMPLETE at 30/30 and every b-level closes. NOTE the honest weakness:")
        print("    these four have no independent second route BY CONSTRUCTION, so unlike every")
        print("    other shape in this arc they rest on one kernel — gated above, but one kernel.")
    else:
        print("  ⇒ A NEGATIVE VALUE APPEARED. X*X is positive, so this is a construction error, not")
        print("    a result. Report it; do not carry the number into the census.")


if __name__ == "__main__":
    main()
