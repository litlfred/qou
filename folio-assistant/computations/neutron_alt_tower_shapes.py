#!/usr/bin/env python3
"""
Item 1: neutron direct derivation — alternative tower shapes.

The standard mass-endomorphism-tower formula

    m = |V̂_0 V̂_1| + Φ_q(|V̂_0|) + Φ_q(|V̂_1|) + z² Φ_q(|V̂_0 V̂_1|)

gives m_p = 955 MeV (+1.83% vs CODATA) but m_n = 419 MeV (-55.4%)
because V̂_0(neutron) = 0.854 is structurally further from the Φ_q
pole than V̂_0(proton) = 0.989.  The asymmetry comes from the 2 ud-
halves in neutron's g0 chain vs 1 in proton's.

This script tests several candidate "neutron-corrected" tower shapes:

  (A) SWAP V̂_0 and V̂_1 for neutron: use V̂_1 (closer to pole) as the
      "dominant" generator.  If the tower is GENERATOR-LABEL-SYMMETRIC
      under the Hecke algebra, this should give identical masses.
      Testing whether the asymmetry is a labeling artifact.

  (B) SYMMETRISE: m_n_sym = (m_n + m_n_swapped) / 2.  If the true
      neutron mass is the symmetric average, this captures it.

  (C) SAVED-POLE: replace V̂_0 → V̂_0 · (1 + α · ud_count) where
      α is fitted such that V̂_0^n_corrected = V̂_0^p.  The ud_count
      is 1 for proton g0 and 2 for neutron g0 — so the correction
      brings neutron's V̂_0 to proton's value.  Not physically
      motivated but tests whether the tower CAN fit the neutron.

  (D) EXPLICIT ADDITIONAL TERM: add a z^4 · Φ_q(V̂_0²) term specifically
      for neutron (to account for the 2 ud-halves in g0).  If motivated
      by Hecke braid relations, this would be a derivation.

Output: neutron-alt-tower-shapes.witness.json
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
    h as H_A_VAL, q0 as Q_NUM, qi as QI_NUM, z as Z_MARKOV,
    vertex_volume,
)
from q_parameter import Q as Q0
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from witness_base import WitnessBuilder


def Phi_q(v, q, max_iter=2000, tol=1e-16):
    if abs(v) >= abs(q):
        return float('inf')
    qi = 1.0 / q
    prod = 1.0
    coef = qi
    for k in range(1, max_iter + 1):
        term = 1.0 - coef * v
        if abs(term) < 1e-300:
            return float('inf')
        prod /= term
        if abs(coef * v) < tol:
            break
        coef *= qi
    return prod


def tower_std(V0, V1, z, q):
    """Standard m = |V_0 V_1| + Φ(|V_0|) + Φ(|V_1|) + z² Φ(|V_0V_1|)."""
    absV0, absV1 = abs(V0), abs(V1)
    prod = abs(V0 * V1)
    return prod + Phi_q(absV0, q) + Phi_q(absV1, q) + z ** 2 * Phi_q(prod, q)


def tower_saturated(V0, V1, z, q):
    """Shape (D): add z^4 · Φ_q(V_0 · V_0) term for V_0-pole saturation."""
    base = tower_std(V0, V1, z, q)
    absV0 = abs(V0)
    return base + z ** 4 * Phi_q(absV0 ** 2, q)


def main():
    w = WitnessBuilder("neutron-alt-tower-shapes",
                        engine="alt-tower-shapes")
    w.set_description(
        "Test 4 alternative tower shapes against the neutron CODATA value "
        "to see if any closes the -56% gap with a physically-motivated "
        "extra term."
    )

    q = float(Q_NUM)
    z_val = float(Z_MARKOV)
    hbar_q_sq = ((q - 1) / q) ** 2

    # Level-0 V̂
    Ve = vertex_volume([(1.0, 0.0)] * 3)
    Vp0 = vertex_volume(_PROTON_G0)
    Vp1 = vertex_volume(_PROTON_G1)
    Vn0 = vertex_volume(_NEUTRON_G0)
    Vn1 = vertex_volume(_NEUTRON_G1)

    m_e = abs(Ve) + Phi_q(abs(Ve), q)

    def MeV(m_H):
        return (m_H / m_e) * M_E_MEV

    def err(mev, codata):
        return (mev - codata) / codata * 100

    print("=" * 100)
    print("NEUTRON ALTERNATIVE TOWER SHAPES")
    print("=" * 100)
    print(f"  V̂ (proton):  V_0 = {Vp0:+.6f}  V_1 = {Vp1:+.6f}")
    print(f"  V̂ (neutron): V_0 = {Vn0:+.6f}  V_1 = {Vn1:+.6f}")
    print(f"  q = {q:.6f}  z = {z_val:.6f}")
    print()

    # PROTON reference (standard)
    m_p_std = MeV(tower_std(Vp0, Vp1, z_val, q))
    print(f"  m_p (standard tower) = {m_p_std:.4f} MeV  err = {err(m_p_std, M_P_MEV):+.3f}%")
    print()

    # (A) SWAP V_0 ↔ V_1 for neutron
    m_n_std = MeV(tower_std(Vn0, Vn1, z_val, q))
    m_n_swap = MeV(tower_std(Vn1, Vn0, z_val, q))
    print(f"  (A) SWAP V_0↔V_1 for neutron:")
    print(f"      m_n (standard, V_0=0.854, V_1=0.976) = {m_n_std:.4f} MeV  "
          f"err = {err(m_n_std, M_N_MEV):+.3f}%")
    print(f"      m_n (swapped,  V_0=0.976, V_1=0.854) = {m_n_swap:.4f} MeV  "
          f"err = {err(m_n_swap, M_N_MEV):+.3f}%")
    swap_helps = abs(err(m_n_swap, M_N_MEV)) < abs(err(m_n_std, M_N_MEV))
    print(f"      → swap {'HELPS' if swap_helps else 'no help'}")
    print()

    # (B) Symmetrise
    m_n_sym = 0.5 * (m_n_std + m_n_swap)
    print(f"  (B) SYMMETRISED: (std + swap)/2 = {m_n_sym:.4f} MeV  "
          f"err = {err(m_n_sym, M_N_MEV):+.3f}%")
    print()

    # (C) Saved-pole: correct V_0 to match proton's V_0
    ratio_V0 = Vp0 / Vn0
    Vn0_corrected = Vn0 * ratio_V0  # = Vp0
    m_n_poleC = MeV(tower_std(Vn0_corrected, Vn1, z_val, q))
    print(f"  (C) V_0 → V_0 × (V_0^p / V_0^n) = {Vn0_corrected:+.6f}:")
    print(f"      m_n corrected = {m_n_poleC:.4f} MeV  "
          f"err = {err(m_n_poleC, M_N_MEV):+.3f}%")
    print(f"      [factor needed: {ratio_V0:.4f}; not physically derived]")
    print()

    # (D) Saturated tower with z^4 Φ(V_0²) term
    m_p_sat = MeV(tower_saturated(Vp0, Vp1, z_val, q))
    m_n_sat = MeV(tower_saturated(Vn0, Vn1, z_val, q))
    print(f"  (D) ADDITIONAL z^4 Φ_q(V_0²) term (motivated by 2 ud-halves):")
    print(f"      m_p_sat = {m_p_sat:.4f} MeV  err = {err(m_p_sat, M_P_MEV):+.3f}%")
    print(f"      m_n_sat = {m_n_sat:.4f} MeV  err = {err(m_n_sat, M_N_MEV):+.3f}%")
    print(f"      → {'Bigger proton overshoot' if abs(err(m_p_sat, M_P_MEV)) > abs(err(m_p_std, M_P_MEV)) else 'Proton unchanged'}")
    print(f"        {'Neutron closer' if abs(err(m_n_sat, M_N_MEV)) < abs(err(m_n_std, M_N_MEV)) else 'Neutron NOT closer'}")
    print()

    # (E) n-specific: ONLY add z^4 term for neutron, not proton
    m_n_D_only = MeV(tower_std(Vn0, Vn1, z_val, q)
                       + z_val ** 4 * Phi_q(abs(Vn0) ** 2, q))
    print(f"  (E) z^4 Φ(V_0²) term FOR NEUTRON ONLY:")
    print(f"      m_n = {m_n_D_only:.4f} MeV  err = {err(m_n_D_only, M_N_MEV):+.3f}%")
    print()

    # (F) Find the additional term c that closes the gap exactly
    m_n_target = M_N_MEV
    m_n_std_Hecke = tower_std(Vn0, Vn1, z_val, q)
    m_n_target_Hecke = (m_n_target / M_E_MEV) * m_e
    delta_needed = m_n_target_Hecke - m_n_std_Hecke
    delta_ratio_to_V0sq_Phi = delta_needed / Phi_q(abs(Vn0)**2, q)
    print(f"  (F) Required additive correction to match neutron CODATA:")
    print(f"      Δ m_n (Hecke) = {delta_needed:+.4f}")
    print(f"      Δ / Φ_q(V_0²) = {delta_ratio_to_V0sq_Phi:.6f}")
    print(f"         coefficient if term were c·Φ_q(V_0²)")
    print(f"         (z^4 = {z_val**4:.6f}, so c/z^4 = {delta_ratio_to_V0sq_Phi/z_val**4:.4f})")
    print()

    w.add_data("params", {"q": q, "z": z_val, "hbar_q_sq": hbar_q_sq})
    w.add_data("level_0_V_hat", {
        "Ve": Ve, "Vp0": Vp0, "Vp1": Vp1, "Vn0": Vn0, "Vn1": Vn1,
    })
    w.add_data("shapes", {
        "A_standard_n": {"m_n_MeV": m_n_std, "err_pct": err(m_n_std, M_N_MEV)},
        "A_swap_n":     {"m_n_MeV": m_n_swap, "err_pct": err(m_n_swap, M_N_MEV)},
        "B_symmetric":  {"m_n_MeV": m_n_sym, "err_pct": err(m_n_sym, M_N_MEV)},
        "C_V0_corrected": {"m_n_MeV": m_n_poleC, "err_pct": err(m_n_poleC, M_N_MEV),
                             "factor": ratio_V0},
        "D_saturated_both": {"m_p_MeV": m_p_sat, "m_n_MeV": m_n_sat,
                               "m_p_err_pct": err(m_p_sat, M_P_MEV),
                               "m_n_err_pct": err(m_n_sat, M_N_MEV)},
        "E_saturated_neutron_only": {
            "m_n_MeV": m_n_D_only,
            "m_n_err_pct": err(m_n_D_only, M_N_MEV)},
        "F_required_delta": {
            "delta_Hecke": delta_needed,
            "coefficient_if_Phi_V0sq": delta_ratio_to_V0sq_Phi,
            "coeff_over_z4": delta_ratio_to_V0sq_Phi / z_val**4,
        },
    })

    # Proton reference
    w.add_data("proton_reference", {
        "m_p_std_MeV": m_p_std, "err_pct": err(m_p_std, M_P_MEV),
    })
    w.save()


if __name__ == "__main__":
    main()
