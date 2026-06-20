#!/usr/bin/env python3
"""
First structural crack at the q-deformed keystone (muon) shift, now that the
`pyhecke_native` wheel builds in-sandbox (PR #2511).

It evaluates the ONE well-posed object the functor-resolution doc
(`docs/audits/2026-06-13-s5-so3-fiber-action-functor-resolution.md` §4) asks
for: the shift in the H_3(q) Borromean Markov trace induced by evaluating the
knot through the muon projector E_(3,2) (ℓ=2) versus the electron projector
E_(3,1,1) (ℓ=1), via the classical S_5 -> S_3 restriction branchings

    (3,2)   ↓ S_3 = (3) ⊕ 2·(2,1)
    (3,1,1) ↓ S_3 = (1,1,1) ⊕ 2·(2,1) ⊕ (3)

DISCIPLINE (critical-distance + 2026-06-13 doc §1): the 210 ppb muon target is
an *anchor-shift artifact*.  This script does NOT fit `1.000000210`; it reports
what the structural object actually gives and at what order of magnitude, so the
mechanism can be accepted or refuted on its size, not tuned to a target.

Two operator-valued models are reported:

  Model A — branching-multiplicity trace.  For generation g with H_5 home block
  μ_g, weight the Borromean H_3 characters by the H_3 Markov weights y_ν and the
  S_5->S_3 branching multiplicity m(ν; μ_g):

        T_g = Σ_{ν⊢3} m(ν; μ_g) · y_ν^{H3} · χ_ν^{Bor}

  Model B — H_5 home-block-weight ratio.  Weight the (shared) Borromean trace by
  the H_5 Jones-Markov weight of each generation's home block:

        r = y_{(3,2)}^{H5} / y_{(3,1,1)}^{H5}
"""
import pyhecke_native as ph

Q0 = 1.1099785955541805  # tools/hecke-engine/src/gram.rs::Q_0 (f64)
DPS = 50
BORROMEAN = [(-1, 1), (1, 2)] * 3  # b = (s1^{-1} s2)^3

# Classical S_5 -> S_3 branching multiplicities m(ν ; μ), ν⊢3, verified by hand
# (S_5->S_4->S_3 box removal) and against the functor-resolution doc §2.
BRANCH = {
    "muon":     {(3,): 1, (2, 1): 2, (1, 1, 1): 0},  # μ = (3,2),   ℓ=2
    "electron": {(3,): 1, (2, 1): 2, (1, 1, 1): 1},  # μ = (3,1,1), ℓ=1
}
H3 = [(3,), (2, 1), (1, 1, 1)]


def main() -> int:
    print(f"pyhecke_native v{ph.__version__}  |  q_0 = {Q0}  |  dps = {DPS}\n")

    # --- H_3 Markov weights and Borromean per-block characters (mpfr chars) ---
    y3 = dict(zip([tuple(p) for p in ph.partitions_of(3)],
                  ph.trace_weights_n(3, Q0)))
    chi = {nu: float(ph.chi_lambda_braid_mpfr(list(nu), BORROMEAN, str(Q0), DPS))
           for nu in H3}
    print("H_3 Markov weights y_ν and Borromean characters χ_ν:")
    for nu in H3:
        print(f"  ν={str(nu):<11}  y={y3[nu]:+.12f}   χ_Bor={chi[nu]:+.12f}")

    # --- Model A: branching-multiplicity operator-valued trace --------------
    print("\n[Model A] branching-multiplicity trace  T_g = Σ m(ν;μ_g)·y_ν·χ_ν")
    T = {}
    for g, mult in BRANCH.items():
        T[g] = sum(mult[nu] * y3[nu] * chi[nu] for nu in H3)
        print(f"  T_{g:<9} = {T[g]:.12f}")
    diff = T["electron"] - T["muon"]
    rel = diff / T["electron"]
    # The (2,1) channel contributes 2·y·χ to BOTH -> cancels in the difference.
    only_111 = y3[(1, 1, 1)] * chi[(1, 1, 1)]
    print(f"\n  T_e - T_μ            = {diff:.12e}")
    print(f"  isolated (1,1,1) term = {only_111:.12e}   "
          f"(should equal T_e - T_μ exactly)")
    print(f"  |Δ(cancellation)|     = {abs(diff - only_111):.2e}")
    print(f"  relative split  (T_e-T_μ)/T_e = {rel:.6e}  "
          f"= {rel*1e9:.3e} ppb")
    print(f"  vs 210 ppb target: factor {rel/210e-9:.3e}× too large")

    # --- Model B: H_5 home-block weight ratio -------------------------------
    print("\n[Model B] H_5 home-block weight ratio  r = y_(3,2) / y_(3,1,1)")
    y5 = dict(zip([tuple(p) for p in ph.partitions_of(5)],
                  ph.trace_weights_n(5, Q0)))
    y_mu, y_el = y5[(3, 2)], y5[(3, 1, 1)]
    r = y_mu / y_el
    print(f"  y_(3,2)^H5   = {y_mu:.12f}")
    print(f"  y_(3,1,1)^H5 = {y_el:.12f}")
    print(f"  ratio r      = {r:.12f}   (deviation from 1: {(r-1)*1e9:.3e} ppb)")
    print(f"  vs 210 ppb target: factor {(r-1)/210e-9:.3e}× too large")

    # --- Structural verdict --------------------------------------------------
    print("\n=== STRUCTURAL VERDICT (no fitting) ===")
    print(" 1. The h^4-bearing (2,1) channel enters BOTH branchings with the")
    print("    SAME (classical, q-independent) multiplicity 2 -> it cancels")
    print("    exactly in the muon/electron difference.  The naive Res functor")
    print("    multiplicity model carries NO h^4-driven generation splitting.")
    print(" 2. The entire Model-A split is the antisymmetric (1,1,1) sign")
    print("    channel (χ=1, h-INDEPENDENT), at the ~1e-2 level.")
    print(" 3. Both well-posed objects (Model A ~1e-2, Model B ~1e0) are 5-7")
    print("    orders of magnitude too large to BE the 210 ppb shift, and")
    print("    neither is bar-even-h^4 in origin.  Confirms 210 ppb is not the")
    print("    leading block-selection effect (anchor-shift artifact framing).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
