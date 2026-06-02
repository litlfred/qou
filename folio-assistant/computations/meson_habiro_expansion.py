#!/usr/bin/env python3
"""
meson_habiro_expansion.py — compute the Habiro expansion of the
meson braid M₊ = (σ₁σ₂)²σ₂σ₁ and use duality to derive the
meson tower correction.

TWO APPROACHES:
1. Direct Habiro expansion of tr_M(M₊) in the q-Pochhammer basis
2. Duality: M₋ = bar(M₊) maps near-antiparallel to near-identity,
   then apply the baryon spectral ladder to the dual

The meson mass ratio correction R = m_K/m_π / base should emerge
from the Habiro coefficients if it has algebraic origin.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

from mpmath import mp, mpf, fabs, sqrt, matrix, acos, pi as mppi

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_PI_PM_MEV_VALIDATION, M_K_PM_MEV_VALIDATION  # noqa: E402


def hoefsmit_V21(q_val):
    """Build σ₁, σ₂ on V_{(2,1)} at generic q."""
    qi = 1 / q_val
    h = q_val - qi
    sigma1 = matrix([[q_val, 0], [0, -qi]])
    a2 = -qi / (1 + q_val ** 2)
    d2 = q_val ** 3 / (1 + q_val ** 2)
    b2 = sqrt((h ** 2 + 3) / (h ** 2 + 4))
    sigma2 = matrix([[a2, b2], [b2, d2]])
    return sigma1, sigma2


def meson_braid_trace(q_val):
    """tr(M₊) on V_{(2,1)} where M₊ = (σ₁σ₂)²σ₂σ₁."""
    s1, s2 = hoefsmit_V21(q_val)
    s12 = s1 * s2
    M = s12 * s12 * s2 * s1
    return M[0, 0] + M[1, 1]


def meson_dual_trace(q_val):
    """tr(M₊^{bar}) = tr(M₊(q⁻¹)) — bar involution sends q→q⁻¹."""
    return meson_braid_trace(1 / q_val)


def full_markov_trace_H3(n, q_val):
    """Full H₃ Markov trace of σ₁ⁿ."""
    qi = 1 / q_val
    h = q_val - qi
    qf3 = (q_val ** 3 - qi ** 3) / h * (q_val ** 2 - qi ** 2) / h
    y3 = q_val ** 3 / qf3
    y21 = 1 / qf3
    y111 = qi ** 3 / qf3
    return y3 * q_val ** n + y21 * (q_val ** n + (-qi) ** n) / 2 + y111 * (-qi) ** n


def main():
    set_compute_dps()
    wb = WitnessBuilder("meson-habiro-expansion", engine="mpmath")

    q0 = mpf(Q_50_DIGIT_STR)
    h = q0 - 1 / q0
    hbar = (q0 - 1) / q0
    b = sqrt((h ** 2 + 3) / (h ** 2 + 4))
    u = b * hbar ** 2

    target = M_K_PM_MEV_VALIDATION / M_PI_PM_MEV_VALIDATION
    chi5 = q0 ** 5 - q0 ** (-5)
    seifert_sq = (mpf(9) / 5) ** 2
    base = chi5 * seifert_sq
    R_exact = target / base

    print("=" * 70)
    print("MESON HABIRO EXPANSION + DUALITY PROOF ATTEMPT")
    print("=" * 70)
    print()

    # === 1. Meson braid trace at q₀ and q₀⁻¹ (duality) ===
    tr_M_q0 = meson_braid_trace(q0)
    tr_M_qi = meson_braid_trace(1 / q0)  # bar-dual

    print(f"Meson braid M₊ = (σ₁σ₂)²σ₂σ₁ on V_(2,1):")
    print(f"  tr(M₊; q₀) = {float(tr_M_q0):.10f}  (near-antiparallel)")
    print(f"  tr(M₊; q₀⁻¹) = {float(tr_M_qi):.10f}  (bar-dual)")
    print()

    # === 2. Duality spectral approach ===
    # The PRODUCT M₊(q₀) · M₊(q₀⁻¹) should give a near-identity
    # operator (bar × original ≈ identity for real q)
    s1, s2 = hoefsmit_V21(q0)
    I2 = matrix([[1, 0], [0, 1]])
    s12 = s1 * s2
    M_plus = s12 * s12 * s2 * s1

    # Hecke inverse: σ⁻¹ = σ - h·I
    s1_inv = s1 - h * I2
    s2_inv = s2 - h * I2
    # M₋ = σ₁⁻¹σ₂⁻¹(σ₂σ₁)⁻² = inverse meson braid
    s2_inv_s1_inv = s2_inv * s1_inv
    M_minus = s1_inv * s2_inv * s2_inv_s1_inv * s2_inv_s1_inv

    tr_M_minus = M_minus[0, 0] + M_minus[1, 1]
    det_M_minus = M_minus[0, 0] * M_minus[1, 1] - M_minus[0, 1] * M_minus[1, 0]

    # Product M₊·M₋ should = I (if M₋ is the true inverse)
    product = M_plus * M_minus
    tr_product = product[0, 0] + product[1, 1]

    print(f"Inverse meson M₋ on V_(2,1):")
    print(f"  tr(M₋) = {float(tr_M_minus):.10f}")
    print(f"  det(M₋) = {float(det_M_minus):.10f}")
    print(f"  tr(M₊·M₋) = {float(tr_product):.10f} (should be 2 if M₋=M₊⁻¹)")
    print()

    # === 3. Spectral ladder on the DUAL ===
    # The dual meson braid: negate and check if near-identity
    # Or: use M₊² (square of meson braid) — eigenvalues squared
    M_sq = M_plus * M_plus
    tr_sq = M_sq[0, 0] + M_sq[1, 1]
    det_sq = M_sq[0, 0] * M_sq[1, 1] - M_sq[0, 1] * M_sq[1, 0]
    print(f"Meson squared M₊²:")
    print(f"  tr(M₊²) = {float(tr_sq):.10f}")
    print(f"  det(M₊²) = {float(det_sq):.10f}")

    # M₊² has eigenvalues λ², where λ are eigenvalues of M₊
    # If M₊ eigenvalues are e^{±iθ}, then M₊² has e^{±2iθ}
    # tr(M₊) = 2cos(θ) = -1.044 → cos(θ) = -0.522 → θ ≈ 2.12
    # tr(M₊²) = 2cos(2θ) = 2(2cos²θ-1) = 2(2×0.272-1) = 2(-0.455) = -0.910
    # That matches!
    print(f"  Expected: 2(2cos²θ-1) = {float(2*(2*(tr_M_q0/2)**2-1)):.10f}")
    print()

    # === 4. KEY IDEA: The mass ratio involves σ₁ⁿ (quark braids), ===
    # not the meson braid. Compute the H₃ FULL trace ratio with     ===
    # the Habiro q-Pochhammer expansion of the TRACE RATIO.          ===

    print("=== QUARK TRACE RATIO HABIRO EXPANSION ===")
    print()

    # Define f(q) = tr_M^{H₃}(σ₁⁵; q) / tr_M^{H₃}(σ₁³; q)
    # and expand f(q₀)/f_base in the eigenvalue parameter u
    tr5 = full_markov_trace_H3(5, q0)
    tr3 = full_markov_trace_H3(3, q0)
    markov_ratio = fabs(tr5) / fabs(tr3)  # 1.461

    # The base formula uses chi_21 only. What's the ratio of
    # FULL trace to (2,1)-character-only?
    # R_block = full_ratio × (9/5)² / base
    R_block = markov_ratio * seifert_sq / base
    print(f"Full Markov ratio |tr₅/tr₃| = {float(markov_ratio):.15f}")
    print(f"Full × (9/5)² = {float(markov_ratio * seifert_sq):.10f}")
    print(f"R_block = full×(9/5)²/base = {float(R_block):.15f}")
    print()

    # The actual mass ratio uses a DIFFERENT decomposition:
    # m_K/m_π = χ₂₁(σ₁⁵) × (Seifert ratio)^n_q
    # where n_q = 2 for meson.
    # The correction is: what Seifert exponent gives the exact PDG value?

    from mpmath import log
    # If m_K/m_π = χ₂₁(σ₁⁵) × (9/5)^x, what is x?
    x_exact = float(log(target / chi5) / log(mpf(9) / 5))
    print(f"Exact Seifert exponent: (9/5)^x with x = {x_exact:.10f}")
    print(f"x - 2 = {x_exact - 2:.10e}")
    print(f"x = 2 + {x_exact - 2:.6e}")
    print()

    # The deviation δx = x - 2 from the integer exponent:
    delta_x = x_exact - 2
    # Can δx be expressed in terms of u?
    print(f"δx / u = {delta_x / float(u):.6f}")
    print(f"δx / u² = {delta_x / float(u ** 2):.6f}")
    print(f"δx / h² = {delta_x / float(h ** 2):.6f}")
    print(f"δx / ℏ² = {delta_x / float(hbar ** 2):.6f}")
    print()

    # Check: does δx = c × h² for some rational c?
    c_h2 = delta_x / float(h ** 2)
    print(f"If δx = c·h²: c = {c_h2:.10f}")
    print(f"  c ≈ 1/600 = {1/600:.10f}")
    print(f"  c ≈ 1/(4·[3]_q!) = {1/(4*float((q0**3-q0**(-3))/h*(q0**2-q0**(-2))/h)):.10f}")
    print()

    # === 5. ALTERNATIVE: R as a function of the full Wedderburn sum ===
    # R_exact = 1.000290. Is this the ratio of two different Wedderburn sums?
    # Sum_full(5)/Sum_full(3) vs chi_21(5)/chi_21(3)

    # Define correction C = (R_exact - 1)
    C = float(R_exact - 1)
    print(f"=== CORRECTION C = R-1 = {C:.15e} ===")
    print()

    # Test: C = (sym+antisym contribution to tr₅) / base
    qi_val = 1 / q0
    qf3 = (q0 ** 3 - qi_val ** 3) / h * (q0 ** 2 - qi_val ** 2) / h
    y3 = q0 ** 3 / qf3
    y111 = qi_val ** 3 / qf3

    sym5 = float(y3 * q0 ** 5)
    antisym5 = float(y111 * (-qi_val) ** 5)
    sym3 = float(y3 * q0 ** 3)
    antisym3 = float(y111 * (-qi_val) ** 3)

    # The (3)+(1,1,1) block ratio minus the (2,1)-only ratio
    # full_ratio = (std + sym + antisym)/(std3 + sym3 + antisym3)
    # base_ratio = chi5/chi3 (normalized differently)
    # This comparison is hard because normalizations differ.

    # Instead: is C proportional to the ANTISYMMETRIC block contribution?
    print(f"Antisymmetric block at n=5: y₁₁₁·(-q⁻⁵) = {antisym5:.10e}")
    print(f"Antisymmetric block at n=3: y₁₁₁·(-q⁻³) = {antisym3:.10e}")
    print(f"C / |antisym5| = {C / abs(antisym5):.10f}")
    print(f"C / (sym5 + antisym5) = {C / (sym5 + antisym5):.10e}")
    print()

    # Test: C = y₃ × h² × something?
    print(f"y₃ = {float(y3):.10f}")
    print(f"y₁₁₁ = {float(y111):.10f}")
    print(f"C / y₃ = {C / float(y3):.10e}")
    print(f"C / y₁₁₁ = {C / float(y111):.10e}")
    print(f"C / (y₃·h²) = {C / float(y3 * h ** 2):.10f}")
    print(f"C / (y₁₁₁·h²) = {C / float(y111 * h ** 2):.10f}")

    wb.set_description(
        "Meson Habiro expansion + duality analysis. "
        f"Seifert exponent x = {x_exact:.6f} (deviation δx = {delta_x:.6e} from 2). "
        "Correction C = R-1 analyzed via Wedderburn block decomposition."
    )
    wb.add_data("seifert_exponent", {"x": x_exact, "delta_x": delta_x})
    wb.add_data("correction", {"C": C, "four_u_sq": float(4 * u ** 2)})
    wb.add_assertion("R_near_1", computed=float(fabs(R_exact - 1)), expected=0,
                     tolerance=0.001, source="R = target/base ≈ 1")
    wb.save()


if __name__ == "__main__":
    main()
