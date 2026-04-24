#!/usr/bin/env python3
"""
Derive absolute proton mass from the mass-endomorphism-tower formula.

Source: content/quantum-observable-universe/braids-and-knots/
        mass-endomorphism-tower.md §"Application to the proton-electron
        mass ratio".

The paper's explicit formula:

  𝔪(W) = |Π_i V̂_i^full|  +  Σ_i Φ_q(|V̂_i^full|)
         +  z² · Σ_{|i-j|=1} Φ_q(|V̂_i^full · V̂_j^full|)

where:
  • V̂_i^full = w_sym·λ_i^sym + w_std·V_i^std + w_alt·λ_i^alt
    is the additive Wedderburn volume per generator
    (from hecke_core.atom_per_generator_volumes).
  • Φ_q(z) = Π_{k=1}^∞ (1 - q^{-k} z)^{-1} is the non-perturbative
    quantum dilogarithm.
  • z = Markov weight.

For the electron, a single trefoil σ_1^3 on 2 strands with 1 generator:
  𝔪_e = |V̂_e| + Φ_q(|V̂_e|)

For the proton, B_3·uud with gluon on 3 strands with 2 generators:
  𝔪_p = |V̂_0 V̂_1| + Φ_q(|V̂_0|) + Φ_q(|V̂_1|)
        + z² · Φ_q(|V̂_0 V̂_1|)

The paper claims 𝔪_p/𝔪_e ≈ 1870 (CODATA: 1836.15, 1.8% error).

Uses only q_0 (derived from m_μ/m_e) and the braid construction.
No AME-fit, no calibration to m_p.

Output: proton-mass-tower-derivation.witness.json
"""
from __future__ import annotations

import math
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

from hecke_core import (
    atom_per_generator_volumes,
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
    h as H_A_VAL, q0 as Q_NUM, qi as QI_NUM, z as Z_MARKOV,
    W_SYM, W_STD, W_ALT, vertex_volume,
)
from q_parameter import Q as Q0
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from witness_base import WitnessBuilder


def Phi_q(z: float, *, max_iter: int = 2000, tol: float = 1e-16) -> float:
    """Non-perturbative quantum dilogarithm
    Φ_q(z) = Π_{k=1}^∞ (1 - q^{-k} z)^{-1}.  Converges when |z| < q.

    Index convention: k starts at 1, so coef = qi^k at step k.
    """
    if abs(z) >= float(Q0):
        return float('inf')
    prod = 1.0
    qi_val = float(QI_NUM)
    coef = qi_val  # qi^1 at k=1
    for k in range(1, max_iter + 1):
        term = 1.0 - coef * z
        if abs(term) < 1e-300:
            return float('inf')
        prod /= term
        if abs(coef * z) < tol:
            break
        coef *= qi_val
    return prod


def electron_V_hat() -> float:
    """Electron = trefoil σ_1^3 on 2 strands, 1 generator.
    V̂_e = w_sym·q^3 + w_std·V_std(σ^3) + w_alt·(-q^-1)^3"""
    # trefoil = [(1, 0)] * 3  (three positive crossings)
    chain = [(1.0, 0.0)] * 3
    return vertex_volume(chain)


def nucleon_V_hat(g0_chain, g1_chain) -> tuple[float, float]:
    """Per-generator additive Wedderburn volumes for one nucleon."""
    V0 = vertex_volume(g0_chain)
    V1 = vertex_volume(g1_chain)
    return V0, V1


def mass_tower_electron(V_e: float) -> dict:
    """m_e = |V_e| + Φ_q(|V_e|) — flat tower for 1-generator word."""
    absV = abs(V_e)
    phi = Phi_q(absV)
    m = absV + phi
    return {
        "V_hat": V_e, "abs_V": absV,
        "term_abs_V": absV,
        "term_Phi_q_V": phi,
        "m_Hecke_units": m,
    }


def phi_q_trace(z: float, max_iter: int = 250) -> list[dict]:
    """Return per-k breakdown of Phi_q(z) accumulation for debugging."""
    qi_val = float(QI_NUM)
    coef = qi_val
    prod = 1.0
    rows = []
    for k in range(1, max_iter + 1):
        term = 1.0 - coef * z
        factor = 1.0 / term
        prod *= factor
        if k <= 10 or k % 50 == 0 or (abs(coef * z) < 1e-10 and k <= 250):
            rows.append({
                "k": k, "qi_k": coef, "qi_k_z": coef * z,
                "one_minus_qi_k_z": term, "factor": factor,
                "running_prod": prod,
            })
        if abs(coef * z) < 1e-16:
            break
        coef *= qi_val
    return rows


def mass_tower_nucleon(V0: float, V1: float, z: float) -> dict:
    """m_nucleon = |V_0 V_1| + Φ_q(|V_0|) + Φ_q(|V_1|)
                   + z² · Φ_q(|V_0 V_1|)."""
    absV0, absV1 = abs(V0), abs(V1)
    prod_V = abs(V0 * V1)
    phi0 = Phi_q(absV0)
    phi1 = Phi_q(absV1)
    phi_prod = Phi_q(prod_V)
    z_sq_phi = z * z * phi_prod
    m = prod_V + phi0 + phi1 + z_sq_phi
    return {
        "V_hat_0": V0, "V_hat_1": V1,
        "abs_V0": absV0, "abs_V1": absV1, "abs_prod": prod_V,
        "term_abs_prod": prod_V,
        "term_Phi_q_V0": phi0,
        "term_Phi_q_V1": phi1,
        "term_z2_Phi_q_V0V1": z_sq_phi,
        "z_squared": z * z,
        "Phi_q(|V0 V1|)": phi_prod,
        "m_Hecke_units": m,
    }


def main():
    w = WitnessBuilder("proton-mass-tower-derivation",
                        engine="mass-endomorphism-tower")
    w.set_description(
        "Absolute proton mass via mass-endomorphism-tower formula "
        "(content/quantum-observable-universe/braids-and-knots/"
        "mass-endomorphism-tower.md §application to p-e ratio). "
        "m_p/m_e ≈ 1870 from framework; CODATA 1836.15."
    )
    w.add_parameter("q_0", float(Q0))
    w.add_parameter("H_A", float(H_A_VAL))
    w.add_parameter("z_markov", float(Z_MARKOV))
    w.add_parameter("w_sym", float(W_SYM))
    w.add_parameter("w_std", float(W_STD))
    w.add_parameter("w_alt", float(W_ALT))

    print("=" * 90)
    print("PROTON MASS ABSOLUTE via MASS-ENDOMORPHISM-TOWER")
    print("=" * 90)
    print(f"  q_0 = {float(Q0):.10f}   ℏ_q² = {((float(Q0)-float(QI_NUM))/float(Q0))**2:.10f}")
    print(f"  z (Markov) = {float(Z_MARKOV):.10f}")
    print(f"  Wedderburn weights: w_sym = {float(W_SYM):.4f}, "
          f"w_std = {float(W_STD):.4f}, w_alt = {float(W_ALT):.4f}")
    print()

    # Electron
    print("─" * 90)
    print("ELECTRON (trefoil σ_1^3 on 2 strands, 1 generator)")
    print("─" * 90)
    V_e = electron_V_hat()
    e_data = mass_tower_electron(V_e)
    print(f"  V̂_e = {V_e:+.6f}")
    print(f"  |V̂_e| = {e_data['abs_V']:.6f}")
    print(f"  Φ_q(|V̂_e|) = {e_data['term_Phi_q_V']:.6f}")
    print(f"  m_e (Hecke units) = |V̂_e| + Φ_q(|V̂_e|) = {e_data['m_Hecke_units']:.6f}")
    print()

    # Proton
    print("─" * 90)
    print("PROTON (B_3 × uud + gluon on 3 strands, 2 generators)")
    print("─" * 90)
    Vp0, Vp1 = nucleon_V_hat(_PROTON_G0, _PROTON_G1)
    p_data = mass_tower_nucleon(Vp0, Vp1, float(Z_MARKOV))
    print(f"  V̂_0^full (gen 0) = {Vp0:+.6f}")
    print(f"  V̂_1^full (gen 1) = {Vp1:+.6f}")
    print(f"  |V̂_0|           = {p_data['abs_V0']:.6f}")
    print(f"  |V̂_1|           = {p_data['abs_V1']:.6f}")
    print(f"  |V̂_0 · V̂_1|    = {p_data['abs_prod']:.6f}")
    print()
    print(f"  TOWER CONTRIBUTIONS (m_p = T1 + T2 + T3 + T4):")
    print(f"    T1 = |V̂_0 V̂_1|            = {p_data['term_abs_prod']:>14.6f}")
    print(f"    T2 = Φ_q(|V̂_0|)           = {p_data['term_Phi_q_V0']:>14.6f}")
    print(f"    T3 = Φ_q(|V̂_1|)           = {p_data['term_Phi_q_V1']:>14.6f}")
    print(f"    T4 = z² · Φ_q(|V̂_0 V̂_1|) = {p_data['term_z2_Phi_q_V0V1']:>14.6f}  "
          f"(z² = {p_data['z_squared']:.4f}, Φ_q(|V₀V₁|) = {p_data['Phi_q(|V0 V1|)']:.2f})")
    print(f"  m_p (Hecke) = {p_data['m_Hecke_units']:>14.6f}")
    print()

    # Neutron
    print("─" * 90)
    print("NEUTRON (B_3 × udd + gluon on 3 strands, 2 generators)")
    print("─" * 90)
    Vn0, Vn1 = nucleon_V_hat(_NEUTRON_G0, _NEUTRON_G1)
    n_data = mass_tower_nucleon(Vn0, Vn1, float(Z_MARKOV))
    print(f"  V̂_0^full (gen 0) = {Vn0:+.6f}")
    print(f"  V̂_1^full (gen 1) = {Vn1:+.6f}")
    print()
    print(f"  TOWER CONTRIBUTIONS (m_n = T1 + T2 + T3 + T4):")
    print(f"    T1 = |V̂_0 V̂_1|            = {n_data['term_abs_prod']:>14.6f}")
    print(f"    T2 = Φ_q(|V̂_0|)           = {n_data['term_Phi_q_V0']:>14.6f}")
    print(f"    T3 = Φ_q(|V̂_1|)           = {n_data['term_Phi_q_V1']:>14.6f}")
    print(f"    T4 = z² · Φ_q(|V̂_0 V̂_1|) = {n_data['term_z2_Phi_q_V0V1']:>14.6f}")
    print(f"  m_n (Hecke) = {n_data['m_Hecke_units']:>14.6f}")
    print()

    # Ratios
    print("=" * 90)
    print("PREDICTED MASS RATIOS (no calibration, no CODATA input)")
    print("=" * 90)
    ratio_p_e = p_data["m_Hecke_units"] / e_data["m_Hecke_units"]
    ratio_n_e = n_data["m_Hecke_units"] / e_data["m_Hecke_units"]
    ratio_n_p = n_data["m_Hecke_units"] / p_data["m_Hecke_units"]
    codata_p_e = M_P_MEV / M_E_MEV
    codata_n_e = M_N_MEV / M_E_MEV
    codata_n_p = M_N_MEV / M_P_MEV

    def fmt_err(pred, obs):
        return (pred - obs) / obs * 100

    print(f"  m_p/m_e pred = {ratio_p_e:.3f}   CODATA = {codata_p_e:.3f}   "
          f"err = {fmt_err(ratio_p_e, codata_p_e):+.3f}%")
    print(f"  m_n/m_e pred = {ratio_n_e:.3f}   CODATA = {codata_n_e:.3f}   "
          f"err = {fmt_err(ratio_n_e, codata_n_e):+.3f}%")
    print(f"  m_n/m_p pred = {ratio_n_p:.6f}  CODATA = {codata_n_p:.6f}  "
          f"err = {fmt_err(ratio_n_p, codata_n_p):+.3f}%")

    # Absolute masses using m_e as calibration
    m_p_MeV = ratio_p_e * M_E_MEV
    m_n_MeV = ratio_n_e * M_E_MEV
    print()
    print(f"  Using m_e = {M_E_MEV} MeV as the ONLY absolute scale input:")
    print(f"  m_p pred = {m_p_MeV:.4f} MeV  CODATA = {M_P_MEV:.4f} MeV  "
          f"err = {fmt_err(m_p_MeV, M_P_MEV):+.3f}%")
    print(f"  m_n pred = {m_n_MeV:.4f} MeV  CODATA = {M_N_MEV:.4f} MeV  "
          f"err = {fmt_err(m_n_MeV, M_N_MEV):+.3f}%")
    print(f"  m_n - m_p = {m_n_MeV - m_p_MeV:+.4f} MeV  CODATA = "
          f"{M_N_MEV - M_P_MEV:+.4f} MeV")

    # Save
    w.add_data("electron", e_data)
    w.add_data("proton", p_data)
    w.add_data("neutron", n_data)
    w.add_data("ratios", {
        "m_p_over_m_e_pred": ratio_p_e,
        "m_p_over_m_e_codata": codata_p_e,
        "m_p_over_m_e_err_pct": fmt_err(ratio_p_e, codata_p_e),
        "m_n_over_m_e_pred": ratio_n_e,
        "m_n_over_m_e_codata": codata_n_e,
        "m_n_over_m_e_err_pct": fmt_err(ratio_n_e, codata_n_e),
        "m_n_over_m_p_pred": ratio_n_p,
        "m_n_over_m_p_codata": codata_n_p,
        "m_n_over_m_p_err_pct": fmt_err(ratio_n_p, codata_n_p),
    })
    w.add_data("absolute_masses_MeV", {
        "m_p_pred": m_p_MeV,
        "m_p_codata": M_P_MEV,
        "m_p_err_pct": fmt_err(m_p_MeV, M_P_MEV),
        "m_n_pred": m_n_MeV,
        "m_n_codata": M_N_MEV,
        "m_n_err_pct": fmt_err(m_n_MeV, M_N_MEV),
        "mass_diff_pred_MeV": m_n_MeV - m_p_MeV,
        "mass_diff_codata_MeV": M_N_MEV - M_P_MEV,
    })

    w.add_assertion(
        "m_p/m_e within 5% of CODATA",
        computed=float(abs(fmt_err(ratio_p_e, codata_p_e))),
        expected=0.0, tolerance=5.0,
        source="mass-endomorphism-tower formula",
    )
    w.save()


if __name__ == "__main__":
    main()
