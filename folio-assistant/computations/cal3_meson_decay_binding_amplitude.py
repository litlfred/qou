#!/usr/bin/env python3
"""
CAL-3 as meson decay: compute the Hoefsmit binding amplitude b
and its relationship to m_π.

The Frobenius bridge says V_(2,1) ↓ H₂ = V_(2) ⊕ V_(1,1).
The pion decay π → μ + ν is the de-entanglement: the off-diagonal
Hoefsmit element b goes from non-zero (bound meson) to zero
(free lepton pair).

The binding amplitude b = √(a_ρ · a_{-ρ} + 1) where
  a_ρ = h/(1 - q^{-2ρ})

For the (2,1) block at H₃, ρ = ±2 (the axial distance between
the two SYT of shape (2,1)).

This script:
1. Computes b(q₀) exactly
2. Relates b to m_π through the mass formula
3. Tests whether m_π ∝ b² (binding energy ~ amplitude squared)
4. Computes the "de-entanglement energy" in MeV
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402


def main():
    set_compute_dps()
    mp.mp.dps = 50
    q = mp.mpf(Q_50_DIGIT_STR)
    h = q - 1/q
    m_e = mp.mpf(M_E_MEV)
    m_pi = mp.mpf("139.57039")
    m_K = mp.mpf("493.677")

    print("=" * 70)
    print("  CAL-3 as meson decay: Hoefsmit binding amplitude")
    print("=" * 70)
    print()

    # ── 1. The Hoefsmit off-diagonal element b ──────────────────
    # For (2,1) at H₃, the axial distance ρ = 2
    # (between the two SYT: [1,2|3] and [1,3|2])
    rho = 2

    a_rho = h / (1 - q**(-2*rho))
    a_neg_rho = h / (1 - q**(2*rho))
    b_sq = a_rho * a_neg_rho + 1
    b = mp.sqrt(b_sq)

    print(f"  1. Hoefsmit off-diagonal amplitude (ρ = {rho})")
    print(f"     a_ρ = h/(1-q⁻⁴) = {mp.nstr(a_rho, 15)}")
    print(f"     a₋ρ = h/(1-q⁴) = {mp.nstr(a_neg_rho, 15)}")
    print(f"     b² = a_ρ·a₋ρ + 1 = {mp.nstr(b_sq, 15)}")
    print(f"     b = √(b²) = {mp.nstr(b, 15)}")
    print()

    # ── 2. The Hoefsmit matrix structure ────────────────────────
    print(f"  2. The (2,1) Hoefsmit matrix for σ₂ at H₃")
    print(f"     [a_ρ    b  ]   [{mp.nstr(a_rho, 8):>12s}  {mp.nstr(b, 8):>12s}]")
    print(f"     [b    a₋ρ ]   [{mp.nstr(b, 8):>12s}  {mp.nstr(a_neg_rho, 8):>12s}]")
    print()
    print(f"     Eigenvalues: q = {mp.nstr(q, 10)}, -q⁻¹ = {mp.nstr(-1/q, 10)}")
    print(f"     (These are the lepton-channel eigenvalues V_(2) and V_(1,1))")
    print()

    # ── 3. b as binding strength ────────────────────────────────
    print(f"  3. Binding interpretation")
    print(f"     b = 0: matrix is diagonal → V_(2) and V_(1,1) decouple → leptons")
    print(f"     b ≠ 0: off-diagonal mixing → entangled → meson")
    print(f"     b(q₀) = {mp.nstr(b, 12)} (non-zero → mesons exist)")
    print()

    # What is b in terms of h?
    # b² = h²/((1-q⁻⁴)(1-q⁴)) + 1
    # (1-q⁻⁴)(1-q⁴) = 1 - q⁴ - q⁻⁴ + 1 = 2 - (q⁴+q⁻⁴)
    # q⁴+q⁻⁴ = (q²+q⁻²)² - 2 = (h²+2)² - 2 = h⁴ + 4h² + 2
    # So denominator = 2 - h⁴ - 4h² - 2 = -(h⁴+4h²) = -h²(h²+4)
    # b² = h²/(-h²(h²+4)) + 1 = -1/(h²+4) + 1 = (h²+3)/(h²+4)

    b_sq_formula = (h**2 + 3) / (h**2 + 4)
    print(f"     b² = (h²+3)/(h²+4) = {mp.nstr(b_sq_formula, 15)}")
    print(f"     Matches: {mp.nstr(abs(b_sq - b_sq_formula), 5)}")
    print()

    # Recognize: h²+4 = [2]_q² and h²+3 = [3]_q
    q2_sq = (q + 1/q)**2
    q3_q = q**2 + 1 + q**(-2)
    print(f"     b² = [3]_q / [2]_q²")
    print(f"     [3]_q = {mp.nstr(q3_q, 12)}")
    print(f"     [2]_q² = {mp.nstr(q2_sq, 12)}")
    print(f"     [3]_q/[2]_q² = {mp.nstr(q3_q/q2_sq, 12)}")
    print(f"     Matches b²: {mp.nstr(abs(b_sq - q3_q/q2_sq), 5)}")
    print()

    # ── 4. Relate b to m_π ──────────────────────────────────────
    print(f"  4. Binding amplitude vs pion mass")
    print()

    # b² = [3]_q / [2]_q² ≈ 0.7530
    # b ≈ 0.8678

    # What is m_π in terms of b?
    # Try: m_π = m_e · f(b, q)
    ratio_pi = m_pi / m_e
    print(f"     m_π/m_e = {mp.nstr(ratio_pi, 12)}")
    print(f"     b = {mp.nstr(b, 12)}")
    print(f"     b² = {mp.nstr(b_sq, 12)}")
    print()

    # Test various combinations
    candidates = [
        ("m_π/m_e / b²", ratio_pi / b_sq),
        ("m_π/m_e / b", ratio_pi / b),
        ("m_π/m_e · b²", ratio_pi * b_sq),
        ("m_π/m_e / (1-b²)", ratio_pi / (1 - b_sq)),
        ("m_π/m_e · (1-b²)", ratio_pi * (1 - b_sq)),
    ]

    print(f"     Structural ratios:")
    for name, val in candidates:
        print(f"       {name:>25s} = {mp.nstr(val, 12)}")

    # 1 - b² = 1 - [3]_q/[2]_q² = ([2]_q² - [3]_q)/[2]_q² = 1/[2]_q²
    one_minus_bsq = 1 - b_sq
    inv_q2sq = 1 / q2_sq
    print()
    print(f"     KEY: 1 - b² = 1/[2]_q²")
    print(f"       1 - b² = {mp.nstr(one_minus_bsq, 12)}")
    print(f"       1/[2]_q² = {mp.nstr(inv_q2sq, 12)}")
    print(f"       Match: {mp.nstr(abs(one_minus_bsq - inv_q2sq), 5)}")
    print()

    # So b² = 1 - 1/[2]_q² = ([2]_q² - 1)/[2]_q²
    # And m_π/m_e · (1-b²) = m_π/m_e / [2]_q²
    # = m_π / (m_e · [2]_q²)
    m_pi_over_me_q2sq = ratio_pi * inv_q2sq
    print(f"     m_π / (m_e · [2]_q²) = {mp.nstr(m_pi_over_me_q2sq, 12)}")
    print(f"     = m_π · (1-b²) / m_e")
    print()

    # What structural constant is m_π/(m_e·[2]_q²) close to?
    vol41 = mp.mpf("2.0298832128193072500424051085490405718833786150606")
    catG = mp.mpf("0.915965594177219015054603514932384110774149374281672")

    print(f"     m_π / (m_e·[2]_q²) = {mp.nstr(m_pi_over_me_q2sq, 10)}")
    print(f"     vs Vol(4₁)/ℏ² = {mp.nstr(vol41/(((q-1)/q)**2), 10)} (= m_μ/m_e)")
    print(f"     vs [3]_q! = {mp.nstr(q3_q*(q+1/q), 10)}")
    print(f"     ratio to m_μ/m_e: {mp.nstr(m_pi_over_me_q2sq / (vol41/((q-1)/q)**2), 8)}")
    print()

    # ── 5. The de-entanglement energy ───────────────────────────
    print(f"  5. De-entanglement energy (pion decay π → μ + ν)")
    print()
    print(f"     The binding amplitude b² = [3]_q/[2]_q² ≈ {mp.nstr(b_sq, 6)}")
    print(f"     The de-coupling fraction (1-b²) = 1/[2]_q² ≈ {mp.nstr(one_minus_bsq, 6)}")
    print()
    print(f"     The pion decay releases the binding energy:")
    print(f"     E_bind = m_π · (1 - b²) = m_π / [2]_q²")
    E_bind = m_pi * one_minus_bsq
    print(f"           = {mp.nstr(E_bind, 10)} MeV")
    print(f"     vs m_e = {mp.nstr(m_e, 10)} MeV")
    print(f"     ratio E_bind/m_e = {mp.nstr(E_bind/m_e, 10)}")
    print()

    # The remaining energy goes to the muon + neutrino:
    # m_π = m_μ + E_ν + E_bind (roughly)
    m_mu = mp.mpf("105.6583755")
    E_remaining = m_pi - E_bind
    print(f"     m_π - E_bind = {mp.nstr(E_remaining, 10)} MeV")
    print(f"     vs m_μ = {mp.nstr(m_mu, 10)} MeV")
    print(f"     ratio: {mp.nstr(E_remaining/m_mu, 8)}")

    w = WitnessBuilder("cal3-meson-decay-binding-amplitude", engine="mpmath")
    w.set_description(
        "Computes the Hoefsmit binding amplitude b for the (2,1) block "
        "and its relationship to m_π. Key identity: b² = [3]_q/[2]_q², "
        "so 1-b² = 1/[2]_q². The pion decay energy fraction is 1/[2]_q²."
    )
    w.set_content_block("prop:frobenius-lepton-meson-bridge")
    w.add_data("b_squared", str(mp.nstr(b_sq, 20)))
    w.add_data("b_squared_identity", "b² = [3]_q / [2]_q²")
    w.add_data("one_minus_b_squared", "1/[2]_q²")
    w.add_data("de_entanglement_energy_MeV", str(mp.nstr(E_bind, 15)))
    w.add_assertion("b_sq_identity", computed=1 if abs(float(b_sq - q3_q/q2_sq)) < 1e-30 else 0,
                     expected=1, tolerance=0,
                     source="b² = [3]_q/[2]_q² verified to machine precision")
    print(f"\n  Witness: {w.save()}")


if __name__ == "__main__":
    main()
