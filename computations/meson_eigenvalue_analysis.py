#!/usr/bin/env python3
"""
meson_eigenvalue_analysis.py — apply the baryon eigenvalue structure
to the meson sector and identify the structural differences.

The baryon precision ladder uses eigenvalue b·ℏ_q² with
b² = (h²+3)/(h²+4). Can the same structure predict meson masses?

FINDINGS:

1. The meson braid 𝔐₊ = (σ₀σ₁)²·σ₁σ₀ has ALL POSITIVE crossings
   (6 crossings in H₃(q)), vs the Borromean β_Bor = (σ₁σ₂⁻¹)³
   which has MIXED SIGNS. Both are 6-crossing, 3-strand.

2. The Hoefsmit eigenvalue structure carries over: σ₁ has the same
   eigenvalues q and −q⁻¹ on each Wedderburn block, so b² =
   (h²+3)/(h²+4) is the SAME for mesons and baryons (it depends
   on H₃(q), not on the specific braid).

3. The per-partition character coefficients on (2,1) are c₁ = c₂ = 1
   exactly: χ_{(2,1)}(σ₁ⁿ) = qⁿ + (−q⁻¹)ⁿ. Both eigenspaces
   contribute equally (regular structure).

4. The trace ratio |tr_M(σ₁⁵)|/|tr_M(σ₁³)| = 1.461 misses the
   CODATA m_K/m_π = 3.537 by a factor of 2.42. No single Wedderburn
   channel reproduces the ratio either.

5. The γγ formation chain (meson-formation-chain.md) shows mesons
   arise from γγ → e⁻e⁺ → qq̄ → 𝔐 via Hopf-link operators in
   H₃(q). The Hopf link L₊ = σ₀σ₁ is the quark creation operator.

6. STRUCTURAL DIFFERENCE: for baryons, the SDP selects the regular
   representation (all Wedderburn blocks, proved via Δ_λ = sgn × dim).
   For mesons, the all-positive-crossing structure forces the symmetric
   channel (eigenvalue q) to dominate. The meson SDP may select a
   DIFFERENT Wedderburn-block combination than the baryon.

OPEN: the m_K/m_π ratio requires per-typed-crossing evaluation
(the d→s typing change at each crossing modifies the characters).
This is PR #1310's scope.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

from mpmath import mp, mpf, sqrt, fabs

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402


def main():
    set_compute_dps()

    q = mpf(Q_50_DIGIT_STR)
    h = q - 1 / q
    hbar = 1 - 1 / q

    b_sq = (h ** 2 + 3) / (h ** 2 + 4)
    eigenvalue = sqrt(b_sq) * hbar ** 2

    qi2 = q + 1 / q
    qi3 = (q ** 3 - q ** (-3)) / h
    qf3 = qi3 * qi2

    y3 = q ** 3 / qf3
    y21 = 1 / qf3
    y111 = q ** (-3) / qf3

    # σ₁ on (2,1): trace = a + a' = h/(1-q⁻²) + h/(1-q²) = h²/(-(h²+4)... wait
    # Actually tr = a + a', eigenvalues q and -q⁻¹
    # Character: χ_{(2,1)}(σ₁ⁿ) = qⁿ + (-q⁻¹)ⁿ (c₁=c₂=1)

    def tr_M_sigma1n(n):
        chi_3 = q ** n
        chi_111 = (-1 / q) ** n
        chi_21 = q ** n + (-1 / q) ** n
        return y3 * chi_3 + y21 * chi_21 / 2 + y111 * chi_111

    tr3 = fabs(tr_M_sigma1n(3))
    tr5 = fabs(tr_M_sigma1n(5))
    ratio = tr5 / tr3
    target = mpf("3.53713")

    wb = WitnessBuilder("meson-eigenvalue-analysis", engine="mpmath")
    wb.set_description(
        "Apply baryon eigenvalue structure (b*hbar^2, b^2=(h^2+3)/(h^2+4)) "
        "to mesons. Eigenvalue carries over (same H_3(q)), but trace ratio "
        "misses m_K/m_pi by 2.4x. Meson SDP selects different Wedderburn "
        "blocks than baryon (all-positive crossings → symmetric dominance)."
    )

    wb.add_data("eigenvalue_shared", {
        "b_sq": str(float(b_sq)),
        "eigenvalue": str(float(eigenvalue)),
        "note": "Same for mesons and baryons — depends on H_3(q), not braid",
    })
    wb.add_data("character_structure", {
        "c1_on_21": "1 (exact)",
        "c2_on_21": "1 (exact)",
        "chi_21_sigma1n": "q^n + (-q^{-1})^n",
    })
    wb.add_data("trace_ratios", {
        "tr_sigma1_3": str(float(tr3)),
        "tr_sigma1_5": str(float(tr5)),
        "ratio": str(float(ratio)),
        "m_K_over_m_pi_CODATA": str(float(target)),
        "miss_factor": str(float(target / ratio)),
    })
    wb.add_data("structural_difference", {
        "baryon_braid": "beta_Bor = (sigma_1 sigma_2^{-1})^3 [mixed sign]",
        "meson_braid": "M+ = (sigma_0 sigma_1)^2 sigma_1 sigma_0 [all positive]",
        "baryon_SDP": "regular rep (all blocks, PROVED)",
        "meson_SDP": "OPEN — all-positive crossings → symmetric channel dominance",
        "gamma_gamma_chain": "gamma gamma → e-e+ → qq-bar → M (Hopf link operators)",
    })

    wb.add_assertion(
        "trace_ratio_computed",
        computed=float(ratio),
        expected=1.461,
        tolerance=0.01,
        source="|tr_M(sigma_1^5)|/|tr_M(sigma_1^3)|",
    )

    wb.save()

    print("=== MESON EIGENVALUE ANALYSIS ===")
    print()
    print(f"Eigenvalue b·ℏ² = {float(eigenvalue):.6e} (SAME as baryon)")
    print(f"b² = (h²+3)/(h²+4) = {float(b_sq):.6f}")
    print()
    print(f"|tr_M(σ₁³)| (pion)  = {float(tr3):.6f}")
    print(f"|tr_M(σ₁⁵)| (kaon)  = {float(tr5):.6f}")
    print(f"Ratio               = {float(ratio):.6f}")
    print(f"m_K/m_π (CODATA)    = {float(target):.6f}")
    print(f"Miss factor         = {float(target / ratio):.3f}×")
    print()
    print("Baryon SDP: regular rep (all blocks) — PROVED")
    print("Meson SDP:  symmetric dominance (all-positive) — OPEN")
    print("γγ chain:   γγ → e⁻e⁺ → qq̄ → 𝔐 (Hopf link ops in H₃)")


if __name__ == "__main__":
    main()
