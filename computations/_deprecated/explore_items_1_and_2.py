#!/usr/bin/env python3
"""
Items 1 & 2 of the 1-ppb exploration:

  (1) Level-2 brane-tower V̂^(2) = q²·∂²V̂/∂q² — does an ℏ_q⁴ correction
      at level 2 close the proton or neutron residual?

  (2) Alternative neutron topological structures — test whether the
      −55% direct-tower gap for neutron closes under modified braid
      words for udd, e.g.:
        (a) isospin-swap conjugate:  σ_0⁻¹ σ_1 σ_0 on g0 instead of σ_1
        (b) ud-purified: replace each (1,-h/2) with two (1,-h/4)
            [equal splitting of ud channel]
        (c) W-insertion: add an extra (1, -h/2) to g0 modelling
            a W-exchange in the confined-state tower
        (d) squared-chain: append (1,0) ⋅ (1,0) to g0 (second gluon
            coupling) — mirrors proton's extra structure
"""
from __future__ import annotations

import sys
import math
import warnings
from pathlib import Path
from itertools import product

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

from hecke_core import (
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
    h as H_A_VAL, q0 as Q_NUM, z as Z_MARKOV,
    W_SYM, W_STD, W_ALT,
)
from q_parameter import Q as Q0
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from level1_vhat_brane_tower import (
    Phi_q, vertex_volume_at_q, q_derivative_of_V, tower
)
from witness_base import WitnessBuilder


def q_second_derivative_of_V(chain, q: float, h_step: float = 1e-5) -> float:
    """∂²V̂/∂q² via central second-order finite difference."""
    v_plus = vertex_volume_at_q(chain, q + h_step)
    v_zero = vertex_volume_at_q(chain, q)
    v_minus = vertex_volume_at_q(chain, q - h_step)
    return (v_plus - 2 * v_zero + v_minus) / (h_step ** 2)


def shift_chain_d(chain, d_replace):
    """Return a new chain where each (c, d) entry has its d replaced
    via d_replace(d).  Used to build alternative neutron structures."""
    return [(c, d_replace(d)) for (c, d) in chain]


def explore_item1_level2():
    """Level-2 V̂^(2) = q²·∂²V̂/∂q² — check if jet-level-2 closes residuals."""
    print("=" * 100)
    print("ITEM 1: LEVEL-2 BRANE TOWER  V̂^(2) = q²·∂²V̂/∂q²")
    print("=" * 100)
    q = float(Q_NUM)
    hbar_q_sq = ((q - 1) / q) ** 2
    hbar_q_4 = hbar_q_sq ** 2
    z_val = float(Z_MARKOV)
    print(f"  q₀     = {q:.10f}")
    print(f"  ℏ_q²   = {hbar_q_sq:.10f}")
    print(f"  ℏ_q⁴   = {hbar_q_4:.12f}")
    print()

    # Level-0, 1, 2 for each chain
    chains = [
        ("e",    [(1.0, 0.0)] * 3),
        ("p g0", _PROTON_G0),
        ("p g1", _PROTON_G1),
        ("n g0", _NEUTRON_G0),
        ("n g1", _NEUTRON_G1),
    ]
    print(f"  {'chain':<8} {'V̂^(0)':>14} {'q·V̂^(1)':>14} "
          f"{'q²·V̂^(2)':>14} {'ℏ_q²·L1':>14} {'ℏ_q⁴·L2':>14}")
    data = {}
    for name, ch in chains:
        V0 = vertex_volume_at_q(ch, q)
        V1 = q * q_derivative_of_V(ch, q)
        V2 = q * q * q_second_derivative_of_V(ch, q)
        data[name] = (V0, V1, V2)
        print(f"  {name:<8} {V0:>+14.6f} {V1:>+14.6f} {V2:>+14.6f} "
              f"{hbar_q_sq*V1:>+14.6e} {hbar_q_4*V2:>+14.6e}")
    print()

    # Apply level-2 shift: V̂_eff = V̂^(0) + ℏ_q²·V̂^(1) + ℏ_q⁴·V̂^(2)
    def eff(name):
        V0, V1, V2 = data[name]
        return V0 + hbar_q_sq * V1 + hbar_q_4 * V2

    Ve_L2  = eff("e")
    Vp0_L2 = eff("p g0"); Vp1_L2 = eff("p g1")
    Vn0_L2 = eff("n g0"); Vn1_L2 = eff("n g1")

    m_e_L0 = abs(data["e"][0]) + Phi_q(abs(data["e"][0]), q)
    m_p_L0 = (tower(data["p g0"][0], data["p g1"][0], z_val, q) / m_e_L0) * M_E_MEV
    m_n_L0 = (tower(data["n g0"][0], data["n g1"][0], z_val, q) / m_e_L0) * M_E_MEV

    m_e_L2 = abs(Ve_L2) + Phi_q(abs(Ve_L2), q)
    m_p_L2 = (tower(Vp0_L2, Vp1_L2, z_val, q) / m_e_L2) * M_E_MEV
    m_n_L2 = (tower(Vn0_L2, Vn1_L2, z_val, q) / m_e_L2) * M_E_MEV

    print("  " + "─" * 90)
    print(f"  {'':<14} {'m (MeV)':>12} {'CODATA':>12} {'err':>10}")
    print(f"  {'m_p L0':<14} {m_p_L0:>12.4f} {M_P_MEV:>12.4f} "
          f"{(m_p_L0-M_P_MEV)/M_P_MEV*100:>+9.4f}%")
    print(f"  {'m_p L0+1+2':<14} {m_p_L2:>12.4f} {M_P_MEV:>12.4f} "
          f"{(m_p_L2-M_P_MEV)/M_P_MEV*100:>+9.4f}%")
    print(f"  {'m_n L0':<14} {m_n_L0:>12.4f} {M_N_MEV:>12.4f} "
          f"{(m_n_L0-M_N_MEV)/M_N_MEV*100:>+9.4f}%")
    print(f"  {'m_n L0+1+2':<14} {m_n_L2:>12.4f} {M_N_MEV:>12.4f} "
          f"{(m_n_L2-M_N_MEV)/M_N_MEV*100:>+9.4f}%")
    return {
        "per_chain": data,
        "m_p_L0_MeV": m_p_L0, "m_p_L0_1_2_MeV": m_p_L2,
        "m_n_L0_MeV": m_n_L0, "m_n_L0_1_2_MeV": m_n_L2,
        "m_p_err_L0": (m_p_L0-M_P_MEV)/M_P_MEV*100,
        "m_p_err_L2": (m_p_L2-M_P_MEV)/M_P_MEV*100,
        "m_n_err_L0": (m_n_L0-M_N_MEV)/M_N_MEV*100,
        "m_n_err_L2": (m_n_L2-M_N_MEV)/M_N_MEV*100,
    }


def explore_item2_neutron_alts():
    """Test alternative neutron topological structures."""
    print("\n" + "=" * 100)
    print("ITEM 2: ALTERNATIVE NEUTRON BRAID STRUCTURES")
    print("=" * 100)
    q = float(Q_NUM)
    z_val = float(Z_MARKOV)
    h = float(H_A_VAL)
    print(f"  baseline neutron g0: {_NEUTRON_G0}")
    print(f"  baseline neutron g1: {_NEUTRON_G1}")
    print()

    # Baseline
    Vn0_base = vertex_volume_at_q(_NEUTRON_G0, q)
    Vn1_base = vertex_volume_at_q(_NEUTRON_G1, q)
    Vp0 = vertex_volume_at_q(_PROTON_G0, q)
    Vp1 = vertex_volume_at_q(_PROTON_G1, q)
    m_e_0 = abs(vertex_volume_at_q([(1.0, 0.0)] * 3, q)) + Phi_q(
            abs(vertex_volume_at_q([(1.0, 0.0)] * 3, q)), q)
    m_p_0 = (tower(Vp0, Vp1, z_val, q) / m_e_0) * M_E_MEV
    m_n_base = (tower(Vn0_base, Vn1_base, z_val, q) / m_e_0) * M_E_MEV

    print(f"  baseline V̂_0^p = {Vp0:+.6f}  V̂_0^n = {Vn0_base:+.6f}")
    print(f"  baseline V̂_1^p = {Vp1:+.6f}  V̂_1^n = {Vn1_base:+.6f}")
    print(f"  baseline m_p = {m_p_0:.3f} MeV  err {(m_p_0-M_P_MEV)/M_P_MEV*100:+.3f}%")
    print(f"  baseline m_n = {m_n_base:.3f} MeV  err {(m_n_base-M_N_MEV)/M_N_MEV*100:+.3f}%")
    print()

    # Alternatives
    # (a) ud-purified: neutron g0 has two ud pairs (1,-h/2); replace each
    #     with two subdivided halves (1,-h/4) × 2 — same net structure
    #     but with extended chain
    ud_purified_g0 = []
    for (c, d) in _NEUTRON_G0:
        if abs(d + h / 2) < 1e-9:
            ud_purified_g0.append((c, -h / 4))
            ud_purified_g0.append((c, -h / 4))
        else:
            ud_purified_g0.append((c, d))

    # (b) W-insertion: add an extra (1, -h/2) to g0 (hypothetical
    #     W-exchange contribution)
    w_insert_g0 = list(_NEUTRON_G0) + [(1, -h / 2)]

    # (c) proton-like d→u swap: use proton chains directly (null test:
    #     should reproduce proton mass, not neutron)
    proton_like_g0 = list(_PROTON_G0)
    proton_like_g1 = list(_PROTON_G1)

    # (d) squared-chain: append extra (1,0) (second gluon self-coupling)
    squared_g0 = list(_NEUTRON_G0) + [(1, 0)]

    # (e) strong dd replacement: replace each (1, -h) with (1, -h/2)
    #     (weakening the dd channel — test sensitivity)
    weak_dd_g1 = [(c, -h/2 if abs(d + h) < 1e-9 else d) for (c, d) in _NEUTRON_G1]

    # (f) hybrid g0^p + g1^n: use proton's g0 but neutron's g1 (tests
    #     which generator carries the factor-2 gap)
    hybrid_g0p_g1n_g0 = list(_PROTON_G0)
    hybrid_g0p_g1n_g1 = list(_NEUTRON_G1)

    # (g) hybrid g0^n + g1^p: opposite to (f)
    hybrid_g0n_g1p_g0 = list(_NEUTRON_G0)
    hybrid_g0n_g1p_g1 = list(_PROTON_G1)

    # (h) isospin-swap conjugate approximation: σ_0⁻¹ σ_1 σ_0 in
    #     braid-group terms contributes an additional (1, -h) · (1,0)
    #     · (1, 0) pair.  Test by adding (1, -h) to g0.
    iso_swap_g0 = list(_NEUTRON_G0) + [(1, -h)]

    alternatives = [
        ("baseline",        _NEUTRON_G0,        _NEUTRON_G1),
        ("(a) ud-purified", ud_purified_g0,     _NEUTRON_G1),
        ("(b) W-insertion", w_insert_g0,        _NEUTRON_G1),
        ("(c) proton-like", proton_like_g0,     proton_like_g1),
        ("(d) squared",     squared_g0,         _NEUTRON_G1),
        ("(e) weak dd",     _NEUTRON_G0,        weak_dd_g1),
        ("(f) g0^p+g1^n",   hybrid_g0p_g1n_g0,  hybrid_g0p_g1n_g1),
        ("(g) g0^n+g1^p",   hybrid_g0n_g1p_g0,  hybrid_g0n_g1p_g1),
        ("(h) iso-swap",    iso_swap_g0,        _NEUTRON_G1),
    ]

    print(f"  {'variant':<22} {'V̂_0':>12} {'V̂_1':>12} {'m_n (MeV)':>12} "
          f"{'err vs CODATA':>16}")
    results = []
    for name, g0, g1 in alternatives:
        V0 = vertex_volume_at_q(g0, q)
        V1 = vertex_volume_at_q(g1, q)
        m_n = (tower(V0, V1, z_val, q) / m_e_0) * M_E_MEV
        err_pct = (m_n - M_N_MEV) / M_N_MEV * 100
        print(f"  {name:<22} {V0:>+12.6f} {V1:>+12.6f} {m_n:>12.4f} "
              f"{err_pct:>+15.3f}%")
        results.append({"variant": name, "V0": V0, "V1": V1,
                         "m_n_MeV": m_n, "err_pct": err_pct})
    return {"m_p_baseline_MeV": m_p_0, "m_n_baseline_MeV": m_n_base,
            "m_n_baseline_err_pct": (m_n_base-M_N_MEV)/M_N_MEV*100,
            "alternatives": results}


def main():
    w = WitnessBuilder("explore-1ppb-items-1-and-2",
                        engine="brane-tower-probe + alt-neutron")
    w.set_description(
        "Two-part exploration: (1) level-2 brane-tower V̂^(2) for "
        "proton/neutron residuals; (2) alternative neutron braid "
        "structures — test whether any captures the factor-2 gap."
    )
    item1 = explore_item1_level2()
    item2 = explore_item2_neutron_alts()

    print("\n" + "=" * 100)
    print("VERDICT")
    print("=" * 100)
    print(f"  Item 1 (level-2 tower):")
    print(f"    proton: L0 {item1['m_p_err_L0']:+.3f}%  →  L0+1+2 "
          f"{item1['m_p_err_L2']:+.3f}%   "
          f"(shift: {item1['m_p_err_L2']-item1['m_p_err_L0']:+.4f}%)")
    print(f"    neutron: L0 {item1['m_n_err_L0']:+.3f}%  →  L0+1+2 "
          f"{item1['m_n_err_L2']:+.3f}%   "
          f"(shift: {item1['m_n_err_L2']-item1['m_n_err_L0']:+.4f}%)")
    print()
    print(f"  Item 2 (alternative neutron braids):")
    alts = item2["alternatives"]
    best = min(alts, key=lambda r: abs(r["err_pct"]))
    print(f"    best variant: {best['variant']}  err = {best['err_pct']:+.3f}%")
    print(f"    baseline:     err = {item2['m_n_baseline_err_pct']:+.3f}%")
    under_10 = [a for a in alts if abs(a['err_pct']) < 10]
    if len(under_10) > 1:
        print(f"    {len(under_10)} variants under 10% error")
    else:
        print(f"    no variant achieves < 10% error — factor-2 gap is "
              f"structural, not captured by simple braid modifications")

    w.add_data("item_1_level_2", {
        "m_p_err_L0": item1["m_p_err_L0"],
        "m_p_err_L2": item1["m_p_err_L2"],
        "m_n_err_L0": item1["m_n_err_L0"],
        "m_n_err_L2": item1["m_n_err_L2"],
        "m_p_L0_MeV": item1["m_p_L0_MeV"],
        "m_p_L0_1_2_MeV": item1["m_p_L0_1_2_MeV"],
        "m_n_L0_MeV": item1["m_n_L0_MeV"],
        "m_n_L0_1_2_MeV": item1["m_n_L0_1_2_MeV"],
    })
    w.add_data("item_2_alternatives", item2)
    w.save()


if __name__ == "__main__":
    main()
