#!/usr/bin/env python3
"""
Pursue Markov-weight resolutions 1 and 2 in parallel.

Resolution 1 — Jones-Ocneanu convention everywhere:
  z_JO = 1/(q^{1/2} + q^{-1/2}) = 0.4993
  tr_M defined by the Markov property tr_M(σ_n·x) = z_JO · tr_M(x)
  Plancherel-style weights become z-dependent (not d_q²/[n]_q!)

Resolution 2 — Plancherel convention everywhere:
  tr_canonical(x) = Σ_λ (d_q²/[n]_q!) · χ_λ(x)
  The "z" that satisfies tr(σ_n·x) = z·tr(x) is
    z_Planck = H_A / [2]_q ≈ 0.1045  (NOT 0.4993)
  Use this z_Planck in the V̂^std = z·a + b transfer recurrence.

For each convention, compute:
  • V̂_0 and V̂_1 for proton (uud) and neutron (udd)
  • Tower mass m_p = T1 + T2 + T3 + T4
  • Apply the same geometric-series correction α = [2]_q · ℏ_q²

Report side by side which convention lands closer to CODATA m_p,
m_n, and nuclear binding B(D).

Output: markov-convention-parallel.witness.json
"""
from __future__ import annotations

import math
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

from hecke_core import (
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
    h as H_A_VAL, q0 as Q_NUM, qi as QI_NUM,
    W_SYM, W_STD, W_ALT,
)
from q_parameter import Q as Q0
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from witness_base import WitnessBuilder


def Phi_q(v, max_iter=2000, tol=1e-16):
    if abs(v) >= float(Q0):
        return float('inf')
    prod = 1.0
    qi_v = float(QI_NUM)
    coef = qi_v
    for k in range(1, max_iter + 1):
        term = 1.0 - coef * v
        if abs(term) < 1e-300:
            return float('inf')
        prod /= term
        if abs(coef * v) < tol:
            break
        coef *= qi_v
    return prod


def vertex_volume_with_z(chain, z_val: float) -> float:
    """Per-gen V̂^full = w_sym·sp + w_std·(z·a+b) + w_alt·ap

    Matches hecke_core.vertex_volume but with CONFIGURABLE z.
    """
    q = float(Q_NUM)
    qi = float(QI_NUM)
    h = float(H_A_VAL)
    a, b = 0.0, 1.0
    sp, ap = 1.0, 1.0
    for (c, d) in chain:
        a, b = a * c * h + a * d + b * c, a * c + b * d
        sp *= c * q + d
        ap *= -c * qi + d
    V_std = z_val * a + b
    return float(W_SYM) * sp + float(W_STD) * V_std + float(W_ALT) * ap


def tower_mass(V0, V1, z_for_pair) -> dict:
    absV0, absV1 = abs(V0), abs(V1)
    prod = abs(V0 * V1)
    T1 = prod
    T2 = Phi_q(absV0)
    T3 = Phi_q(absV1)
    T4 = z_for_pair ** 2 * Phi_q(prod)
    return {"T1": T1, "T2": T2, "T3": T3, "T4": T4,
            "m_Hecke": T1 + T2 + T3 + T4}


def main():
    w = WitnessBuilder("markov-convention-parallel",
                        engine="tower-with-configurable-z")
    w.set_description(
        "Parallel evaluation of Markov-weight conventions 1 and 2 on "
        "the mass-endomorphism-tower for proton/neutron."
    )

    q = float(Q_NUM)
    qi = float(QI_NUM)
    h = float(H_A_VAL)
    hbar_q_sq = ((q - 1) / q) ** 2
    two_q = q + 1 / q

    # Two z values.  z_Planck is the trace ratio tr_Planck(T_1)/tr_Planck(1)
    # under Plancherel weights w_λ = d_q²/[n]_q!; verified
    # numerically in markov_weight_verification.py to equal H_A/2,
    # not H_A/[2]_q.
    z_JO = 1.0 / (math.sqrt(q) + 1.0 / math.sqrt(q))        # 0.4993
    z_Planck = h / 2.0                                      # 0.1045

    print("=" * 100)
    print("MARKOV-CONVENTION PARALLEL EVALUATION")
    print("=" * 100)
    print(f"  q_0 = {q:.10f},  [2]_q = {two_q:.6f},  H_A = {h:.6f}")
    print(f"  z_JO (Jones-Ocneanu)     = 1/(q^½+q^-½)  = {z_JO:.10f}")
    print(f"  z_Planck (canonical)     = H_A / 2       = {z_Planck:.10f}")
    print(f"  ratio z_JO / z_Planck    = {z_JO/z_Planck:.4f} "
          f"≈ 2/H_A/[2]_q ratio of conventions")
    print()

    # Compute V̂_i for proton/neutron under each convention
    print("─" * 100)
    print("V̂_i^full per generator under each z:")
    print("─" * 100)
    print(f"  {'chain':<10} {'z_JO V̂':>14} {'z_Planck V̂':>16}")
    Vp0_JO = vertex_volume_with_z(_PROTON_G0, z_JO)
    Vp1_JO = vertex_volume_with_z(_PROTON_G1, z_JO)
    Vn0_JO = vertex_volume_with_z(_NEUTRON_G0, z_JO)
    Vn1_JO = vertex_volume_with_z(_NEUTRON_G1, z_JO)
    Vp0_P = vertex_volume_with_z(_PROTON_G0, z_Planck)
    Vp1_P = vertex_volume_with_z(_PROTON_G1, z_Planck)
    Vn0_P = vertex_volume_with_z(_NEUTRON_G0, z_Planck)
    Vn1_P = vertex_volume_with_z(_NEUTRON_G1, z_Planck)
    Ve_JO = vertex_volume_with_z([(1.0, 0.0)] * 3, z_JO)
    Ve_P = vertex_volume_with_z([(1.0, 0.0)] * 3, z_Planck)
    print(f"  {'e':<10} {Ve_JO:>+14.6f} {Ve_P:>+16.6f}")
    print(f"  {'p g0':<10} {Vp0_JO:>+14.6f} {Vp0_P:>+16.6f}")
    print(f"  {'p g1':<10} {Vp1_JO:>+14.6f} {Vp1_P:>+16.6f}")
    print(f"  {'n g0':<10} {Vn0_JO:>+14.6f} {Vn0_P:>+16.6f}")
    print(f"  {'n g1':<10} {Vn1_JO:>+14.6f} {Vn1_P:>+16.6f}")
    print()

    # Tower masses under each convention
    print("─" * 100)
    print("Tower mass predictions (m_e Hecke used as MeV reference):")
    print("─" * 100)
    # Electron (1 gen): m_e = |V_e| + Φ_q(|V_e|)
    m_e_JO = abs(Ve_JO) + Phi_q(abs(Ve_JO))
    m_e_P = abs(Ve_P) + Phi_q(abs(Ve_P))
    p_tower_JO = tower_mass(Vp0_JO, Vp1_JO, z_JO)
    p_tower_P = tower_mass(Vp0_P, Vp1_P, z_Planck)
    n_tower_JO = tower_mass(Vn0_JO, Vn1_JO, z_JO)
    n_tower_P = tower_mass(Vn0_P, Vn1_P, z_Planck)

    def to_MeV(m_H, m_e_H):
        return (m_H / m_e_H) * M_E_MEV

    m_p_JO = to_MeV(p_tower_JO["m_Hecke"], m_e_JO)
    m_p_P = to_MeV(p_tower_P["m_Hecke"], m_e_P)
    m_n_JO = to_MeV(n_tower_JO["m_Hecke"], m_e_JO)
    m_n_P = to_MeV(n_tower_P["m_Hecke"], m_e_P)

    print(f"  {'quantity':<16} {'z_JO':>18} {'z_Planck':>18} {'CODATA':>14}")
    print(f"  {'m_e (Hecke)':<16} {m_e_JO:>18.4f} {m_e_P:>18.4f} "
          f"{'(reference)':>14}")
    print(f"  {'m_p (MeV)':<16} {m_p_JO:>18.4f} {m_p_P:>18.4f} {M_P_MEV:>14.4f}")
    print(f"  {'m_n (MeV)':<16} {m_n_JO:>18.4f} {m_n_P:>18.4f} {M_N_MEV:>14.4f}")
    print(f"  {'m_p err %':<16} {(m_p_JO-M_P_MEV)/M_P_MEV*100:>+17.3f}% "
          f"{(m_p_P-M_P_MEV)/M_P_MEV*100:>+17.3f}%")
    print(f"  {'m_n err %':<16} {(m_n_JO-M_N_MEV)/M_N_MEV*100:>+17.3f}% "
          f"{(m_n_P-M_N_MEV)/M_N_MEV*100:>+17.3f}%")
    print()

    # Apply geometric-series correction α = [2]_q · ℏ_q² (same for both)
    print("─" * 100)
    print("With [2]_q · ℏ_q² geometric-series correction:")
    print("─" * 100)
    correction = 1.0 / (1.0 + two_q * hbar_q_sq)
    m_p_JO_c = m_p_JO * correction
    m_p_P_c = m_p_P * correction
    m_n_JO_c = m_n_JO * correction
    m_n_P_c = m_n_P * correction
    print(f"  Correction factor 1/(1+[2]_q·ℏ_q²) = {correction:.6f}")
    print(f"  {'quantity':<16} {'z_JO':>18} {'z_Planck':>18} {'CODATA':>14}")
    print(f"  {'m_p (MeV)':<16} {m_p_JO_c:>18.4f} {m_p_P_c:>18.4f} "
          f"{M_P_MEV:>14.4f}")
    print(f"  {'m_n (MeV)':<16} {m_n_JO_c:>18.4f} {m_n_P_c:>18.4f} "
          f"{M_N_MEV:>14.4f}")
    print(f"  {'m_p err %':<16} {(m_p_JO_c-M_P_MEV)/M_P_MEV*100:>+17.3f}% "
          f"{(m_p_P_c-M_P_MEV)/M_P_MEV*100:>+17.3f}%")
    print(f"  {'m_n err %':<16} {(m_n_JO_c-M_N_MEV)/M_N_MEV*100:>+17.3f}% "
          f"{(m_n_P_c-M_N_MEV)/M_N_MEV*100:>+17.3f}%")
    print()

    # Mass ratios (calibration-free)
    print("─" * 100)
    print("Calibration-free ratios (z-independent of m_e scale):")
    print("─" * 100)
    r_pe_JO = p_tower_JO["m_Hecke"] / m_e_JO
    r_pe_P = p_tower_P["m_Hecke"] / m_e_P
    r_ne_JO = n_tower_JO["m_Hecke"] / m_e_JO
    r_ne_P = n_tower_P["m_Hecke"] / m_e_P
    print(f"  {'ratio':<16} {'z_JO':>18} {'z_Planck':>18} {'CODATA':>14}")
    print(f"  {'m_p / m_e':<16} {r_pe_JO:>18.3f} {r_pe_P:>18.3f} "
          f"{M_P_MEV/M_E_MEV:>14.3f}")
    print(f"  {'m_n / m_e':<16} {r_ne_JO:>18.3f} {r_ne_P:>18.3f} "
          f"{M_N_MEV/M_E_MEV:>14.3f}")
    print(f"  {'m_n / m_p':<16} {r_ne_JO/r_pe_JO:>18.6f} {r_ne_P/r_pe_P:>18.6f} "
          f"{M_N_MEV/M_P_MEV:>14.6f}")
    print()

    # Verdict
    print("=" * 100)
    print("VERDICT")
    print("=" * 100)
    print(f"  z_JO (corrected) gives:")
    print(f"    m_p = {m_p_JO_c:.4f} MeV  err = {(m_p_JO_c-M_P_MEV)/M_P_MEV*100:+.3f}%")
    print(f"    m_n = {m_n_JO_c:.4f} MeV  err = {(m_n_JO_c-M_N_MEV)/M_N_MEV*100:+.3f}%")
    print()
    print(f"  z_Planck (corrected) gives:")
    print(f"    m_p = {m_p_P_c:.4f} MeV  err = {(m_p_P_c-M_P_MEV)/M_P_MEV*100:+.3f}%")
    print(f"    m_n = {m_n_P_c:.4f} MeV  err = {(m_n_P_c-M_N_MEV)/M_N_MEV*100:+.3f}%")
    print()
    if abs(m_p_JO_c - M_P_MEV) < abs(m_p_P_c - M_P_MEV):
        print("  Conclusion: z_JO (Jones-Ocneanu) is closer to CODATA for m_p.")
    else:
        print("  Conclusion: z_Planck (canonical) is closer to CODATA for m_p.")

    w.add_data("params", {
        "q_0": q, "H_A": h, "two_q": two_q, "hbar_q_sq": hbar_q_sq,
        "z_JO": z_JO, "z_Planck": z_Planck,
    })
    w.add_data("level_0", {
        "z_JO": {
            "V_e": Ve_JO, "V0_p": Vp0_JO, "V1_p": Vp1_JO,
            "V0_n": Vn0_JO, "V1_n": Vn1_JO,
            "m_e_Hecke": m_e_JO,
            "m_p_MeV": m_p_JO, "m_n_MeV": m_n_JO,
            "m_p_err_pct": (m_p_JO-M_P_MEV)/M_P_MEV*100,
            "m_n_err_pct": (m_n_JO-M_N_MEV)/M_N_MEV*100,
        },
        "z_Planck": {
            "V_e": Ve_P, "V0_p": Vp0_P, "V1_p": Vp1_P,
            "V0_n": Vn0_P, "V1_n": Vn1_P,
            "m_e_Hecke": m_e_P,
            "m_p_MeV": m_p_P, "m_n_MeV": m_n_P,
            "m_p_err_pct": (m_p_P-M_P_MEV)/M_P_MEV*100,
            "m_n_err_pct": (m_n_P-M_N_MEV)/M_N_MEV*100,
        },
    })
    w.add_data("corrected_geometric_series", {
        "correction_factor": correction,
        "z_JO": {
            "m_p_MeV": m_p_JO_c, "m_n_MeV": m_n_JO_c,
            "m_p_err_pct": (m_p_JO_c-M_P_MEV)/M_P_MEV*100,
            "m_n_err_pct": (m_n_JO_c-M_N_MEV)/M_N_MEV*100,
        },
        "z_Planck": {
            "m_p_MeV": m_p_P_c, "m_n_MeV": m_n_P_c,
            "m_p_err_pct": (m_p_P_c-M_P_MEV)/M_P_MEV*100,
            "m_n_err_pct": (m_n_P_c-M_N_MEV)/M_N_MEV*100,
        },
    })
    w.save()


if __name__ == "__main__":
    main()
