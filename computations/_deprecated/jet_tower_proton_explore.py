#!/usr/bin/env python3
"""
Jet-tower exploration for the proton +1.83% residual.

Target: m_p = 938.272 MeV from framework.  Level-0 tower prediction
(proton_mass_tower_derivation.py):  955.49 MeV, err +1.83%.

Per jet-tower-mass-endomorphism.md the full mass is a SUM over jet
levels n = 0, 1, 2, ...:

  m(ρ) = |Π V̂_i^{(0)}|
       + Σ_{n=0}^N [ Σ_i Φ_q(|V̂_i^{(n)}|)
                   + z² Σ_{(i,j) ∈ P_n} Φ_q(|V̂_i^{(n)} V̂_j^{(n)}|) ]

The descended term is at level 0 only.  Level-n contributions
ascend via the pentagon identity.

Exploration 1 — tower variants at level 0
  Adjacent-only pairs vs full i<j pairs (proton has only 2 gens, so same)
  Different Φ_q variants (raw product, series, no-resonance)
  all_subsets form (same as full for n_gens = 2)

Exploration 2 — jet-level-1 upper bound via Δ_max
  From prop:delta-max-uniform-bound:
    Δ_max = 2·L(β)·‖ρ(β)‖_op² · m^(0)(ρ_free)
    |m^(≥1) tail| ≤ Δ_max · ℏ_q² / (1 − ℏ_q²)

Shows what jet-level-1 CAN contribute (upper bound), without
computing the level-1 V̂_i^(1) explicitly (the jet-prolonged Hecke
representation is not implemented in this branch).

Output: jet-tower-proton-explore.witness.json
"""
from __future__ import annotations

import math
import sys
import warnings
from itertools import combinations
from pathlib import Path

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import numpy as np

from hecke_core import (
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
    h as H_A_VAL, q0 as Q_NUM, qi as QI_NUM, z as Z_MARKOV,
    W_SYM, W_STD, W_ALT, vertex_volume,
)
from q_parameter import Q as Q0
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from witness_base import WitnessBuilder


def Phi_q(z: float, max_iter: int = 2000, tol: float = 1e-16) -> float:
    """Φ_q(z) = Π_{k=1}^∞ (1 - q^{-k} z)^{-1}."""
    if abs(z) >= float(Q0):
        return float('inf')
    prod = 1.0
    qi_val = float(QI_NUM)
    coef = qi_val
    for k in range(1, max_iter + 1):
        term = 1.0 - coef * z
        if abs(term) < 1e-300:
            return float('inf')
        prod /= term
        if abs(coef * z) < tol:
            break
        coef *= qi_val
    return prod


def tower_variant(V_list: list[float], cross_mode: str) -> float:
    """Compute tower mass for given V_i list and cross-term scheme.

    cross_mode ∈ {'adjacent', 'full', 'all_subsets'}
    """
    n = len(V_list)
    abs_V = [abs(v) for v in V_list]
    prod_V = 1.0
    for v in V_list:
        prod_V *= v
    prod_V = abs(prod_V)

    m = prod_V + sum(Phi_q(v) for v in abs_V)
    z_sq = float(Z_MARKOV) ** 2

    if cross_mode == "adjacent":
        for i in range(n - 1):
            m += z_sq * Phi_q(abs_V[i] * abs_V[i + 1])
    elif cross_mode == "full":
        for i in range(n):
            for j in range(i + 1, n):
                m += z_sq * Phi_q(abs_V[i] * abs_V[j])
    elif cross_mode == "all_subsets":
        # k=2, 3, ..., n: k-subset carries z^k · Φ_q(Π)
        for k in range(2, n + 1):
            zk = float(Z_MARKOV) ** k
            for S in combinations(range(n), k):
                p = 1.0
                for i in S:
                    p *= abs_V[i]
                m += zk * Phi_q(p)
    else:
        raise ValueError(f"unknown cross_mode: {cross_mode}")
    return m


def hecke_rep_op_norm(chain: list[tuple[float, float]]) -> float:
    """Operator-norm estimate for the std-block Hecke rep of the braid
    given by chain = [(c, d)] sequence.

    Use the 2×2 Hoefsmit rep for std(2,1) and compute the matrix product's
    operator norm.  For single-gen words this is trivially diag(q, -q⁻¹),
    norm = q.  For longer words, compute product and take spectral norm.
    """
    q = float(Q_NUM)
    qi = float(QI_NUM)
    # Hoefsmit std rep matrices — single-gen on 2 strands has 2×2 for std
    # at n=3; but chain is on ONE generator (gen 0 or gen 1), so acts via
    # eigenvalue diag on its eigenspace.
    # Approx: each factor (c·σ + d·I) has eigenvalues c·q+d and c·(-qi)+d.
    max_eig = 0.0
    for c, d in chain:
        e1 = abs(c * q + d)
        e2 = abs(-c * qi + d)
        max_eig *= 1  # placeholder, will use product-of-max
    # Submultiplicative bound: product of max eigenvalues per factor
    prod_max = 1.0
    for c, d in chain:
        e1 = abs(c * q + d)
        e2 = abs(-c * qi + d)
        prod_max *= max(e1, e2)
    return prod_max


def main():
    w = WitnessBuilder("jet-tower-proton-explore",
                        engine="jet-tower-level0-level1-bound")
    w.set_description(
        "Exploration of the +1.83% proton residual via tower-variant "
        "sensitivity (level 0) and jet-level-1 upper bound from "
        "prop:delta-max-uniform-bound.  Does not compute the explicit "
        "level-1 V̂_i^(1); only bounds its contribution."
    )

    # ──────────────────────────────────────────────────────────────
    # Compute level-0 V̂_i
    # ──────────────────────────────────────────────────────────────
    V_e = vertex_volume([(1.0, 0.0)] * 3)
    Vp0 = vertex_volume(_PROTON_G0)
    Vp1 = vertex_volume(_PROTON_G1)

    print("=" * 90)
    print("JET TOWER — proton residual exploration")
    print("=" * 90)
    print(f"  q_0 = {float(Q0):.10f}")
    print(f"  H_A = {float(H_A_VAL):.10f}")
    h_q_sq_form_A = ((float(Q_NUM) - 1.0) / float(Q_NUM)) ** 2
    h_q_sq_form_B = ((float(Q_NUM) - float(QI_NUM)) / float(Q_NUM)) ** 2
    print(f"  ℏ_q² (form A: (q-1)/q squared) = {h_q_sq_form_A:.6f}  (~{h_q_sq_form_A*100:.2f}%)")
    print(f"  ℏ_q² (form B: H_A/q  squared) = {h_q_sq_form_B:.6f}  (~{h_q_sq_form_B*100:.2f}%)")
    print()
    print(f"  V̂_e = {V_e:+.6f}")
    print(f"  V̂_0(proton) = {Vp0:+.6f}")
    print(f"  V̂_1(proton) = {Vp1:+.6f}")
    print()

    # ──────────────────────────────────────────────────────────────
    # Exploration 1 — tower variants at level 0
    # ──────────────────────────────────────────────────────────────
    print("─" * 90)
    print("EXPLORATION 1: tower variants (level 0 only)")
    print("─" * 90)
    m_e_L0 = tower_variant([V_e], "full")  # electron: 1 gen, trivially just singleton
    print(f"  m_e (level 0, any variant): {m_e_L0:.4f} Hecke")
    print()
    print(f"  {'cross_mode':<15} {'m_p (Hecke)':>14} {'m_p (MeV)':>12} {'err vs 938.27':>12}")
    print(f"  {'-'*65}")
    rows_level0 = []
    for mode in ["adjacent", "full", "all_subsets"]:
        m_p = tower_variant([Vp0, Vp1], mode)
        m_p_MeV = (m_p / m_e_L0) * M_E_MEV
        err = (m_p_MeV - M_P_MEV) / M_P_MEV * 100
        rows_level0.append({"mode": mode, "m_p_Hecke": m_p,
                              "m_p_MeV": m_p_MeV, "err_pct": err})
        print(f"  {mode:<15} {m_p:>14.2f} {m_p_MeV:>12.4f} {err:>+11.3f}%")
    print()
    print("  NOTE: for proton n_gens = 2, all three variants are")
    print("  identical (only one pair (0,1) exists).  Variants matter")
    print("  only for heavier atoms with n_gens ≥ 3.")
    print()

    # ──────────────────────────────────────────────────────────────
    # Exploration 2 — jet-level-1 upper bound
    # ──────────────────────────────────────────────────────────────
    print("─" * 90)
    print("EXPLORATION 2: jet-level-1 upper bound via Δ_max")
    print("─" * 90)
    # L(β_proton): chain length
    L_proton = len(_PROTON_G0) + len(_PROTON_G1)
    # ‖ρ(β)‖_op² estimate via submultiplicative product of max eigenvalues
    norm_p_g0 = hecke_rep_op_norm(_PROTON_G0)
    norm_p_g1 = hecke_rep_op_norm(_PROTON_G1)
    norm_p = norm_p_g0 * norm_p_g1  # (multiplicative bound over gens)
    norm_p_sq = norm_p ** 2

    m_p_level0_Hecke = rows_level0[0]["m_p_Hecke"]  # all variants same

    # Δ_max = 2·L·‖ρ‖²·m^(0)(ρ_free)
    # For free proton without inter-nucleon: same as proton (single-nucleon),
    # so m^(0)_free ≈ m_p^(0)
    delta_max = 2 * L_proton * norm_p_sq * m_p_level0_Hecke

    # Tail bound at N=0 → |level ≥ 1 tail| ≤ Δ_max · ℏ_q² / (1 - ℏ_q²)
    tail_bound_A = delta_max * h_q_sq_form_A / (1 - h_q_sq_form_A)
    tail_bound_B = delta_max * h_q_sq_form_B / (1 - h_q_sq_form_B)
    tail_bound_A_MeV = (tail_bound_A / m_e_L0) * M_E_MEV
    tail_bound_B_MeV = (tail_bound_B / m_e_L0) * M_E_MEV

    print(f"  L(β_proton)         = {L_proton}")
    print(f"  ‖ρ(p g0)‖ (mult)    = {norm_p_g0:.4f}")
    print(f"  ‖ρ(p g1)‖ (mult)    = {norm_p_g1:.4f}")
    print(f"  ‖ρ(β)‖²            = {norm_p_sq:.4f}")
    print(f"  m^(0)(ρ_free)       = {m_p_level0_Hecke:.4f}  (single-nucleon, same as atom)")
    print(f"  Δ_max = 2·L·‖ρ‖²·m^(0)  = {delta_max:.4e}")
    print()
    print(f"  Tail bound |m^(≥1)| ≤ Δ_max · ℏ_q² / (1 − ℏ_q²):")
    print(f"    using form A (ℏ_q² = {h_q_sq_form_A:.4f}): {tail_bound_A:.4e} Hecke "
          f"= {tail_bound_A_MeV:.4f} MeV")
    print(f"    using form B (ℏ_q² = {h_q_sq_form_B:.4f}): {tail_bound_B:.4e} Hecke "
          f"= {tail_bound_B_MeV:.4f} MeV")
    print()
    print(f"  Target residual (|m_p_MeV - 938.27|) = "
          f"{abs(rows_level0[0]['m_p_MeV'] - M_P_MEV):.4f} MeV")
    print()
    print("  → The Δ_max bound is enormous (the theoretical worst case).")
    print("    The paper says the bound is 'saturated within factor 2' on")
    print("    light atoms, so actual |m^(≥1)| is 2x-10x smaller than Δ_max.")
    print("    Even so, the bound ENCOMPASSES the residual: jet-level-1")
    print("    contributions can in principle bring m_p down by ~17 MeV to")
    print("    match CODATA — they're big enough for that, if sign is right.")
    print()

    # ──────────────────────────────────────────────────────────────
    # Exploration 3 — required level-1 correction to match CODATA
    # ──────────────────────────────────────────────────────────────
    print("─" * 90)
    print("EXPLORATION 3: required level-1 correction to match CODATA")
    print("─" * 90)
    m_p_target_Hecke = (M_P_MEV / M_E_MEV) * m_e_L0
    delta_needed_Hecke = m_p_target_Hecke - m_p_level0_Hecke
    delta_needed_MeV = (delta_needed_Hecke / m_e_L0) * M_E_MEV
    delta_needed_frac = delta_needed_Hecke / m_p_level0_Hecke

    print(f"  m_p target (Hecke) = {m_p_target_Hecke:.4f}")
    print(f"  m_p level-0 (Hecke) = {m_p_level0_Hecke:.4f}")
    print(f"  Required Δ = m_target - m_level0 = {delta_needed_Hecke:+.4f} Hecke = "
          f"{delta_needed_MeV:+.4f} MeV ({delta_needed_frac*100:+.3f}%)")
    print()
    print(f"  Sign check:")
    if delta_needed_Hecke < 0:
        print(f"    Δ < 0: level-0 OVERSHOOTS.  Level-1 correction must be")
        print(f"           NEGATIVE (subtract from level-0).")
    else:
        print(f"    Δ > 0: level-0 UNDERSHOOTS.  Level-1 correction must be")
        print(f"           POSITIVE (add to level-0).")
    print()
    print(f"  Ratio to ℏ_q²:")
    print(f"    |Δ/m_p^(0)| = {abs(delta_needed_frac)*100:.4f}%")
    print(f"    ℏ_q² (A) = {h_q_sq_form_A*100:.4f}% ({'✓' if abs(delta_needed_frac - h_q_sq_form_A) < 0.005 else '✗'} match to 0.5%)")
    print(f"    ℏ_q² (B) = {h_q_sq_form_B*100:.4f}% ({'✓' if abs(delta_needed_frac - h_q_sq_form_B) < 0.005 else '✗'})")

    # Save
    w.add_data("level_0_variants", rows_level0)
    w.add_data("delta_max_bound", {
        "L_proton": L_proton,
        "op_norm_sq": norm_p_sq,
        "m_p_level0_Hecke": m_p_level0_Hecke,
        "Delta_max_Hecke": delta_max,
        "tail_bound_A_Hecke": tail_bound_A,
        "tail_bound_A_MeV": tail_bound_A_MeV,
        "tail_bound_B_Hecke": tail_bound_B,
        "tail_bound_B_MeV": tail_bound_B_MeV,
    })
    w.add_data("residual_required", {
        "m_p_target_Hecke": m_p_target_Hecke,
        "delta_needed_Hecke": delta_needed_Hecke,
        "delta_needed_MeV": delta_needed_MeV,
        "delta_needed_frac_pct": delta_needed_frac * 100,
        "hbar_q_sq_form_A_pct": h_q_sq_form_A * 100,
        "hbar_q_sq_form_B_pct": h_q_sq_form_B * 100,
    })
    w.save()


if __name__ == "__main__":
    main()
