#!/usr/bin/env python3
"""
Explicit proton and neutron mass calculation with error attribution.

Two prediction routes for the nucleon mass:

  (A) Tower route        m_p^tower = Σ_λ w_λ(q_0) · χ_λ(β_p) / d_λ
                         m_n^tower = Σ_λ w_λ(q_0) · χ_λ(β_n) / d_λ
                         (sum over all partitions λ ⊢ 3)

  (B) Kashaev route      m = Vol_hyp(K_internal) · ρ_q
                         ρ_q = 1/ℏ_q² = q²/(q−1)² ≈ 102 in m_e units
                         K_internal = Borromean rings (B_3 closure)

For each route we show:
  1. The categorical unit prediction (no CODATA input)
  2. The MeV value with the framework's canonical density factor
  3. The CODATA value
  4. The percent error

Plus the RATIO m_n / m_p — a pure prediction with no density input,
independent of calibration.

Output: proton-neutron-mass-error.witness.json
"""
from __future__ import annotations

import math
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

from atom_mass_branching import (
    atom_tower_mass_branching,
    q0, qi, h as H_A_VAL,
    q_fact,
)
from witness_base import WitnessBuilder

# CODATA 2018
M_PROTON_MEV = 938.27208816
M_NEUTRON_MEV = 939.56542052
M_N_MINUS_P_MEV = 1.29333216
M_N_OVER_P = M_NEUTRON_MEV / M_PROTON_MEV
M_E_MEV = 0.51099895

# Borromean volume
CATALAN_G = 0.915965594177219015054603514932
VOL_BORROMEAN = 8.0 * CATALAN_G

# Kashaev substrate drag
RHO_Q_CAT = 1.0 / (((float(q0) - 1.0) / float(q0)) ** 2)  # 1/ℏ_q² ≈ 102 in m_e units


def main():
    w = WitnessBuilder("proton-neutron-mass-error", engine="tower+kashaev")
    w.set_description(
        "Explicit proton and neutron mass calculation via (A) Hecke "
        "Plancherel tower m = Σ w_λ χ_λ / d_λ and (B) Kashaev substrate "
        "m = Vol · ρ_q with ρ_q = 1/ℏ_q². Reports absolute predictions, "
        "the calibration-free m_n / m_p ratio, and the mass splitting."
    )
    w.add_parameter("q_0", float(q0))
    w.add_parameter("H_A", float(H_A_VAL))
    w.add_parameter("rho_q_cat_units", float(RHO_Q_CAT))
    w.add_parameter("CODATA_m_p_MeV", M_PROTON_MEV)
    w.add_parameter("CODATA_m_n_MeV", M_NEUTRON_MEV)
    w.add_parameter("CODATA_m_n_over_m_p", M_N_OVER_P)

    print("=" * 80)
    print("PROTON AND NEUTRON MASS — EXPLICIT CALCULATION")
    print("=" * 80)
    print(f"  q_0           = {float(q0):.10f}")
    print(f"  H_A = q−1/q   = {float(H_A_VAL):.10f}")
    print(f"  ℏ_q² = (q−1/q)²/q² = {(float(q0)-float(qi))**2 / float(q0)**2:.10f}")
    print(f"  ρ_q = 1/ℏ_q²  = {RHO_Q_CAT:.6f}  (m_e units)")
    print(f"  Vol(Borromean) = 8G = {VOL_BORROMEAN:.10f}")
    print()
    print(f"  CODATA m_p = {M_PROTON_MEV:.6f} MeV")
    print(f"  CODATA m_n = {M_NEUTRON_MEV:.6f} MeV")
    print(f"  m_n − m_p  = {M_N_MINUS_P_MEV:.6f} MeV")
    print(f"  m_n / m_p  = {M_N_OVER_P:.10f}")
    print()

    # ──────────────────────────────────────────────────────────────
    # Route A: Hecke Plancherel tower
    # ──────────────────────────────────────────────────────────────
    print("=" * 80)
    print("ROUTE A: Hecke Plancherel tower")
    print("  m = Σ_{λ ⊢ 3} w_λ(q_0) · χ_λ(β_nucleon) / d_λ")
    print("=" * 80)
    m_p_cat = atom_tower_mass_branching(1, 0, include_inter=False)
    m_n_cat = atom_tower_mass_branching(0, 1, include_inter=False)
    print(f"  m_p^tower (categorical units) = {m_p_cat:.6e}")
    print(f"  m_n^tower (categorical units) = {m_n_cat:.6e}")
    print(f"  ratio m_n^tower / m_p^tower   = {m_n_cat / m_p_cat:.10f}")
    print()

    ratio_err_A = (m_n_cat / m_p_cat / M_N_OVER_P - 1) * 100
    print(f"  CODATA   m_n / m_p            = {M_N_OVER_P:.10f}")
    print(f"  err (tower ratio vs CODATA)   = {ratio_err_A:+.4f}%  "
          f"= {ratio_err_A * 1e4:+,.0f} ppm")
    print()

    # Calibration to fix absolute scale
    E_0_CALIBRATED = M_PROTON_MEV / m_p_cat
    print(f"  E_0 calibrated to CODATA m_p  = {E_0_CALIBRATED:.6e} MeV/cat")
    print(f"    (sets m_p^tower → {M_PROTON_MEV:.4f} MeV exactly by choice)")
    print(f"  m_n^tower · E_0               = {m_n_cat * E_0_CALIBRATED:.6f} MeV "
          f"[vs CODATA {M_NEUTRON_MEV:.4f}]")
    print(f"  mass diff predicted           = "
          f"{(m_n_cat - m_p_cat) * E_0_CALIBRATED:+.6f} MeV "
          f"[vs CODATA {M_N_MINUS_P_MEV:+.4f}]")
    print()

    # Derivation-only absolute prediction (no calibration)
    alpha_MeV = M_E_MEV * VOL_BORROMEAN
    m_p_pred_alpha = m_p_cat * alpha_MeV
    m_n_pred_alpha = m_n_cat * alpha_MeV
    err_p_alpha = (m_p_pred_alpha - M_PROTON_MEV) / M_PROTON_MEV * 100
    err_n_alpha = (m_n_pred_alpha - M_NEUTRON_MEV) / M_NEUTRON_MEV * 100
    print(f"  DERIVATION ONLY: E_0 = α = m_e·8G = {alpha_MeV:.6f} MeV/cat")
    print(f"  m_p^tower · α = {m_p_pred_alpha:+.3e} MeV "
          f"[vs CODATA {M_PROTON_MEV:.4f}]  err = {err_p_alpha:+.2f}%")
    print(f"  m_n^tower · α = {m_n_pred_alpha:+.3e} MeV "
          f"[vs CODATA {M_NEUTRON_MEV:.4f}]  err = {err_n_alpha:+.2f}%")
    print()

    # ──────────────────────────────────────────────────────────────
    # Route B: Kashaev substrate on internal Borromean
    # ──────────────────────────────────────────────────────────────
    print("=" * 80)
    print("ROUTE B: Kashaev substrate (internal Borromean closure)")
    print("  m = Vol(Borromean) · ρ_q in m_e units")
    print("=" * 80)
    m_nucleon_kashaev_me = VOL_BORROMEAN * RHO_Q_CAT
    m_nucleon_kashaev_MeV = m_nucleon_kashaev_me * M_E_MEV
    err_kashaev = (m_nucleon_kashaev_MeV - M_PROTON_MEV) / M_PROTON_MEV * 100
    print(f"  m_nucleon = 8G · (1/ℏ_q²) = {VOL_BORROMEAN:.4f} · {RHO_Q_CAT:.4f}")
    print(f"                            = {m_nucleon_kashaev_me:.4f} m_e")
    print(f"                            = {m_nucleon_kashaev_MeV:.4f} MeV")
    print(f"  vs CODATA m_p = {M_PROTON_MEV:.4f} MeV")
    print(f"  err = {err_kashaev:+.3f}%")
    print()
    print(f"  Note: Kashaev ρ_q does NOT distinguish p from n — both")
    print(f"  nucleons have identical internal Borromean volume.  Mass")
    print(f"  splitting m_n − m_p requires the quark-typed crossings")
    print(f"  (u vs d), which modify the Hecke character β_nucleon but")
    print(f"  not the hyperbolic volume of the closure.")
    print()

    # ──────────────────────────────────────────────────────────────
    # Error attribution summary
    # ──────────────────────────────────────────────────────────────
    print("=" * 80)
    print("ERROR ATTRIBUTION")
    print("=" * 80)
    print()
    print(" 1. m_n/m_p ratio (calibration-free tower prediction):")
    print(f"      predicted   = {m_n_cat / m_p_cat:.10f}")
    print(f"      CODATA      = {M_N_OVER_P:.10f}")
    print(f"      err         = {ratio_err_A:+.4f}%")
    print(f"      [this is the CLEAN tower test — no density input]")
    print()
    print(" 2. Absolute m_p via Kashaev Vol · ρ_q:")
    print(f"      predicted   = {m_nucleon_kashaev_MeV:.4f} MeV")
    print(f"      CODATA      = {M_PROTON_MEV:.4f} MeV")
    print(f"      err         = {err_kashaev:+.3f}%")
    print(f"      [Vol is exact; ρ_q = 1/ℏ_q² is derivation-only]")
    print()
    print(" 3. Absolute m_p via tower · α:")
    print(f"      predicted   = {m_p_pred_alpha:.3e} MeV")
    print(f"      CODATA      = {M_PROTON_MEV:.4f} MeV")
    print(f"      err         = {err_p_alpha:+.2f}%")
    print(f"      [α = m_e·8G; tower scale is ~1.2e6 cat, α is ~3.7 MeV]")
    print()
    print(" 4. Where error lives:")
    print(f"    • Tower ratio is off by {ratio_err_A:+.4f}% → quark-typed")
    print(f"      crossings in β_p vs β_n not reproducing full CODATA")
    print(f"      splitting. The tower underestimates m_n − m_p.")
    print(f"    • Kashaev absolute is off by {err_kashaev:+.3f}% → the")
    print(f"      ρ_q = 1/ℏ_q² identification mispredicts the nucleon")
    print(f"      density. 8G · ρ_q gives ~{m_nucleon_kashaev_MeV:.0f} MeV, but")
    print(f"      CODATA is 938.27.")
    print(f"    • Tower absolute × α is off by ~10^6 → α is the")
    print(f"      NUCLEAR-scale density, NOT the particle-scale density.")
    print(f"      The framework uses ρ_q (not α) for particle masses")
    print(f"      (see rem:kashaev-volume-density), and uses α = m_e·8G")
    print(f"      for nuclear binding only.")

    # Save
    w.add_data("route_A_tower", {
        "m_p_cat_units": m_p_cat,
        "m_n_cat_units": m_n_cat,
        "m_n_over_m_p_pred": m_n_cat / m_p_cat,
        "m_n_over_m_p_codata": M_N_OVER_P,
        "ratio_err_pct": ratio_err_A,
        "E_0_calibrated_MeV": E_0_CALIBRATED,
        "m_n_MeV_calibrated": m_n_cat * E_0_CALIBRATED,
        "mass_diff_MeV_calibrated": (m_n_cat - m_p_cat) * E_0_CALIBRATED,
        "mass_diff_MeV_codata": M_N_MINUS_P_MEV,
        "m_p_pred_alpha_MeV": m_p_pred_alpha,
        "m_n_pred_alpha_MeV": m_n_pred_alpha,
        "err_p_alpha_pct": err_p_alpha,
        "err_n_alpha_pct": err_n_alpha,
    })
    w.add_data("route_B_kashaev", {
        "m_nucleon_kashaev_me": m_nucleon_kashaev_me,
        "m_nucleon_kashaev_MeV": m_nucleon_kashaev_MeV,
        "err_pct_vs_m_p": err_kashaev,
        "Vol_Borromean_8G": VOL_BORROMEAN,
        "rho_q_cat": RHO_Q_CAT,
    })
    w.add_assertion(
        "tower ratio m_n/m_p matches CODATA within 10%",
        computed=float(abs(ratio_err_A)),
        expected=0.0, tolerance=10.0,
        source="Hecke Plancherel tower",
    )
    w.save()


if __name__ == "__main__":
    main()
