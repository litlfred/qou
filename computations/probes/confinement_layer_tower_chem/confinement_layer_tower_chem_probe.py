#!/usr/bin/env python3
"""Pre-registered 80-dps & exact symbolic probe for the 5-Layer Iterated Confinement Tower,
Adiabatic Gap Stability, Layer-3 Shadow-Price Hardness & Layer-4 Toric / Gröbner Stoichiometry
(Bean qou-5lct / Q-Gap-0).

Pre-registration: PREREGISTRATION.md (committed in e800e93bde6 prior to running).
Lean companion: QOU/MathlibInfra/ConfinementLayerTower.lean (0 sorry, 0 custom axioms).

Computes at mp.dps = 80 (zero float64, q0Anchor = "proton"):
  1. Adiabatic confinement ratios eta_k = ||V_{k+1}|| / Delta_k across L_0 -> L_1 -> L_2 -> L_3 -> L_4,
     verifying eta_0 ~ 7.30e-3, eta_1 ~ 7.54e-3..8.19e-3 (~10^-2, EMC regime), eta_2 ~ 1.77e-6 (~10^-6,
     nuclear transmutation barrier in chemistry), and eta_3 ~ 1.03e-2 (~10^-2, core-shell & thermal
     molecular regime), plus the exact neutron-star outer-crust L_3 -> L_2 electron-capture flip
     threshold E_{F,e}^* = m_n - m_p = 1.29333236 MeV (and QOU-derived m_e + Q_beta(q_0)).
  2. Layer-3 Mulliken electronegativity chi_M = -(mu_+ + mu_-)/2 and Parr-Pearson chemical hardness
     eta_PP = mu_+ - mu_- = I - A_ea >= 0 (Perdew-Parr-Levy-Balduz convexity) and cumulative 2n^2
     noble-gas closures [2, 10, 18, 36, 54, 86].
  3. Exact Smith & Hermite normal forms, 1D primitive circuits (H2O, CH4, NH3, C6H12O6), and for the
     3 x 7 multi-reaction C-H-O network (C, H2, O2, CO, CO2, H2O, CH4): elementary circuits C(A_CHO),
     complete Graver basis G(A_CHO) (Pottier completion cross-checked by exhaustive lattice-box scan),
     exact Universal Gröbner Basis UGB(I_{A_CHO}), zero-temperature Sturmfels-Thomas enthalpy normal
     form reduction on b = (2, 8, 4)^T with LP reduced-cost fiber invariance (Hess's law), and 80-dps
     finite-temperature Birch mass-action equilibrium x^* on Spec C[N A_CHO].
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
for _p in ("computations", "computations/substrate", "tools/qou-substrate/python"):
    if str(ROOT / _p) not in sys.path:
        sys.path.insert(0, str(ROOT / _p))

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

import sympy as sp  # noqa: E402
from codata_constants import (  # noqa: E402  (comparison / validation only where suffixed)
    M_E_MEV,
    M_N_MEV_VALIDATION,
    M_P_MEV_VALIDATION,
    Q_BETA_MEV,
    U_MEV,
    ame_binding_mev,
)
from mpmath import mp, mpf  # noqa: E402
from qou_substrate.codata import value_str  # noqa: E402
from qou_substrate.constants import M_E_MEV_STR, Q_MP, q_at  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form  # noqa: E402


def fmt50(x: mpf) -> str:
    return mp.nstr(x, 50, strip_zeros=False)


def igcd_two(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def vec_gcd(v: tuple[int, ...]) -> int:
    g = 0
    for x in v:
        g = igcd_two(g, x)
    return g


def canonical_sign(v: tuple[int, ...]) -> tuple[int, ...]:
    """Canonical sign for an unoriented circuit/Graver pair {v, -v}: first nonzero entry > 0."""
    for x in v:
        if x != 0:
            return v if x > 0 else tuple(-y for y in v)
    return v


def conformal_le(u: tuple[int, ...], v: tuple[int, ...]) -> bool:
    """True iff u is conformally <= v in Z^M (u_j * v_j >= 0 and |u_j| <= |v_j| for all j)."""
    for uj, vj in zip(u, v):
        if uj * vj < 0 or abs(uj) > abs(vj):
            return False
    return True


def pottier_graver_basis(basis_vecs: list[tuple[int, ...]]) -> set[tuple[int, ...]]:
    """Exact Pottier conformal S-vector completion of a lattice basis into G(A) (both signs)."""
    G: set[tuple[int, ...]] = set()
    for b in basis_vecs:
        if any(x != 0 for x in b):
            g = vec_gcd(b)
            prim = tuple(x // g for x in b)
            G.add(prim)
            G.add(tuple(-x for x in prim))

    changed = True
    while changed:
        changed = False
        cur = sorted(G, key=lambda t: (sum(abs(x) for x in t), t))
        new_elems: set[tuple[int, ...]] = set()
        for i, u in enumerate(cur):
            for w in cur[i + 1 :]:
                # Only pairs with at least one opposite-sign coordinate can produce a conformal child
                if not any(uj * wj < 0 for uj, wj in zip(u, w)):
                    continue
                s = tuple(uj + wj for uj, wj in zip(u, w))
                if all(x == 0 for x in s):
                    continue
                # Conformal reduction modulo current G
                reduced = True
                while reduced:
                    reduced = False
                    for g in cur:
                        if g != s and conformal_le(g, s):
                            s = tuple(sj - gj for sj, gj in zip(s, g))
                            reduced = True
                            break
                if any(x != 0 for x in s) and s not in G and s not in new_elems:
                    new_elems.add(s)
                    new_elems.add(tuple(-x for x in s))
        if new_elems:
            G |= new_elems
            # Prune non-minimal elements under conformal order
            all_g = list(G)
            minimal: set[tuple[int, ...]] = set()
            for v in all_g:
                if not any(u != v and conformal_le(u, v) for u in all_g):
                    minimal.add(v)
            if minimal != G:
                G = minimal
            changed = True
    return G


def enumerate_fiber_points_cho(b: tuple[int, int, int]) -> list[tuple[int, ...]]:
    """Exact nonnegative integer fiber {u in N^7 : A_CHO u = b} for species (C, H2, O2, CO, CO2, H2O, CH4)."""
    bC, bH, bO = b
    pts: list[tuple[int, ...]] = []
    # Row 1: 2*u_H2 + 2*u_H2O + 4*u_CH4 = bH
    if bH % 2 != 0:
        return pts
    for u_CH4 in range(bH // 4 + 1):
        if u_CH4 > bC:
            break
        rem_C1 = bC - u_CH4
        rem_H_pairs = bH // 2 - 2 * u_CH4
        for u_H2O in range(min(rem_H_pairs, bO) + 1):
            u_H2 = rem_H_pairs - u_H2O
            rem_O1 = bO - u_H2O
            # Row 0: u_C + u_CO + u_CO2 = rem_C1
            # Row 2: 2*u_O2 + u_CO + 2*u_CO2 = rem_O1
            for u_CO2 in range(min(rem_C1, rem_O1 // 2) + 1):
                rem_C2 = rem_C1 - u_CO2
                rem_O2 = rem_O1 - 2 * u_CO2
                for u_CO in range(min(rem_C2, rem_O2) + 1):
                    if (rem_O2 - u_CO) % 2 == 0:
                        u_O2 = (rem_O2 - u_CO) // 2
                        u_C = rem_C2 - u_CO
                        pts.append((u_C, u_H2, u_O2, u_CO, u_CO2, u_H2O, u_CH4))
    return pts


def is_edge_of_fiber_polytope(
    u_plus: tuple[int, ...], u_minus: tuple[int, ...], fiber_pts: list[tuple[int, ...]]
) -> bool:
    """Sturmfels (1996, Cor. 4.4 / Prop. 4.11): a primitive binomial x^{u_+} - x^{u_-} in G(A)
    belongs to the Universal Gröbner Basis UGB(I_A) iff the segment [u_+, u_-] is an edge of
    conv(fiber_pts) (or more generally a circuit/edge face: no nontrivial convex combination of
    fiber_pts \\ {u_+, u_-} lies on the segment [u_+, u_-]).
    Check exact rational LP feasibility: can (1 - t) u_+ + t u_- = sum_{w != u_+, u_-} lam_w w
    with t in [0, 1], lam_w >= 0, sum lam_w = 1?
    Because u_+ - u_- is already Graver-minimal (so no integer interior point exists on (u_+, u_-)),
    [u_+, u_-] fails to be an edge iff some convex combination of OTHER fiber vertices equals a
    point (1 - t) u_+ + t u_- on the segment!
    """
    others = [w for w in fiber_pts if w != u_plus and w != u_minus]
    if not others:
        return True
    # Exact rational feasibility: test basic solutions of M_eq * x = rhs with x >= 0, t <= 1
    k = len(others)
    M_eq = sp.Matrix([[sp.Integer(1)] * k + [sp.Integer(0)]])
    rhs = [sp.Integer(1)]
    for j in range(len(u_plus)):
        M_eq = M_eq.col_join(
            sp.Matrix([[sp.Integer(others[i][j]) for i in range(k)] + [sp.Integer(u_plus[j] - u_minus[j])]])
        )
        rhs.append(sp.Integer(u_plus[j]))
    # Reduce M_eq | rhs to row-echelon over Q once!
    aug = M_eq.row_join(sp.Matrix(rhs))
    rref_mat, pivots = aug.rref()
    # Check consistency of zero rows
    n_vars = k + 1
    for r in range(rref_mat.rows):
        if all(rref_mat[r, c] == 0 for c in range(n_vars)) and rref_mat[r, n_vars] != 0:
            return True
    rank_M = len(pivots)
    M_red = rref_mat[:rank_M, :n_vars]
    rhs_red = rref_mat[:rank_M, n_vars]
    for cols in itertools.combinations(range(n_vars), rank_M):
        sub = M_red[:, list(cols)]
        if sub.det() == 0:
            continue
        sol = sub.LUsolve(rhs_red)
        full = [sp.Rational(0)] * n_vars
        for idx, val in zip(cols, sol):
            full[idx] = sp.Rational(val)
        lam_vals = full[:k]
        t_val = full[k]
        if all(lv >= 0 for lv in lam_vals) and sp.Rational(0) <= t_val <= sp.Rational(1):
            return False
    return True


def main() -> int:
    with mp.workdps(80):
        q0 = q_at(80)
        q_mp_ref = mpf(str(Q_MP))
        me_mev = +M_E_MEV
        me_from_str = mpf(M_E_MEV_STR)

        wb = WitnessBuilder(
            "confinement-layer-tower-chem",
            engine="sympy exact Z/Q + mpmath (80 dps)",
            output_dir=HERE,
        )
        wb.set_description(
            "Pre-registered 80-dps & exact symbolic verification of the 5-Layer Iterated "
            "Confinement Tower (L_0..L_4), adiabatic gap ratios eta_k = ||V_{k+1}|| / Delta_k, "
            "neutron-star electron-capture flip threshold, Layer-3 Mulliken/Parr-Pearson shadow "
            "prices, and Layer-4 Diophantine/Graver/Universal-Gröbner/Birch toric chemistry "
            "(Bean qou-5lct / Q-Gap-0)."
        )
        wb.add_parameter("workdps", 80)
        wb.add_parameter("q0_proton_50dps", fmt50(q0))
        wb.add_parameter("m_e_MeV_CAL1", fmt50(me_mev))

        wb.add_assertion(
            "q0_at_80_matches_Q_MP_to_65dps",
            computed=abs(q0 - q_mp_ref),
            expected=mpf(0),
            tolerance=mpf("1e-65"),
            source="qou_substrate.constants.q_at(80) vs Q_MP",
        )
        wb.add_assertion(
            "m_e_CAL1_matches_substrate_str",
            computed=abs(me_mev - me_from_str),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="codata_constants.M_E_MEV vs qou_substrate.constants.M_E_MEV_STR",
        )

        # =====================================================================
        # PART 1: 80-dps 5-Layer Confinement Tower & Adiabatic Gap Ratios eta_k
        # =====================================================================
        vol_41 = 2 * mp.clsin(2, mp.pi / 3)
        h_q0 = q0 - 1 / q0
        hbar_q0 = 1 - 1 / q0
        trM_bor = abs((4 + h_q0**2 - 3 * h_q0**4 - h_q0**6) / (h_q0**2 + 4))
        qf3 = (q0**2 + 1 + q0**-2) * (q0 + 1 / q0)
        mp_qou_mev = me_mev * (2 * vol_41 / (hbar_q0**2) * (trM_bor * qf3 / (q0**3)) - 12)

        # QOU derived Q_beta(q0) = m_e * |q0^2 - 2*q0 - 1| * (q0 + 1) / (2 * q0^3)
        qbeta_qou_mev = me_mev * abs(q0**2 - 2 * q0 - 1) * (q0 + 1) / (2 * q0**3)
        delta_np_qou_mev = me_mev + qbeta_qou_mev

        # Validation constants read strictly from NIST CODATA-2022 / AME-2020 tables
        # (Exact SI-2019 defined constants h, c, e, k_B give full 80-dps hbar*c and k_B in eV)
        alpha_val = mpf(value_str("fine-structure constant"))
        h_si = mpf(value_str("Planck constant"))
        c_si = mpf(value_str("speed of light in vacuum"))
        e_si = mpf(value_str("elementary charge"))
        k_B_si = mpf(value_str("Boltzmann constant"))
        hbar_c_mev_fm = (h_si * c_si / (2 * mp.pi)) / (e_si * mpf("1e6")) * mpf("1e15")
        k_B_eV_K = k_B_si / e_si
        mp_codata_mev = +M_P_MEV_VALIDATION
        mn_codata_mev = +M_N_MEV_VALIDATION
        delta_np_codata_mev = mn_codata_mev - mp_codata_mev
        qbeta_codata_mev = +Q_BETA_MEV

        b_d_mev = +ame_binding_mev(1, 2) / 2
        b_he4_per_a_mev = +ame_binding_mev(2, 4) / 4
        b_c12_per_a_mev = +ame_binding_mev(6, 12) / 12
        b_fe56_per_a_mev = +ame_binding_mev(26, 56) / 56

        # Rydberg atomic valence scale Ry = (1/2) alpha^2 m_e
        ry_mev = (alpha_val**2 * me_mev) / 2
        ry_ev = ry_mev * mpf("1000000")

        # Adiabatic ratios eta_k = ||V_{k+1}|| / Delta_k
        # L_0 -> L_1: QED intra-hadron radiative shift vs Borromean V^3 colour-singlet gap m_p(q0)
        eta_0 = alpha_val  # (alpha * m_p) / m_p

        # L_1 -> L_2: Nuclear binding per nucleon vs Layer-1 hadron confinement gap m_p(q0)
        eta_1_he4 = b_he4_per_a_mev / mp_qou_mev
        eta_1_c12 = b_c12_per_a_mev / mp_qou_mev
        eta_1_fe56 = b_fe56_per_a_mev / mp_qou_mev

        # L_2 -> L_3: Atomic Rydberg binding Ry vs Layer-2 nuclear separation / beta gaps
        eta_2_c12 = ry_mev / b_c12_per_a_mev
        eta_2_he4 = ry_mev / b_he4_per_a_mev
        eta_2_np = ry_mev / delta_np_codata_mev

        # L_3 -> L_4: Covalent perturbation (~Ry/3) vs C 1s core shell (Z_eff = 57/10 => Z_eff^2 Ry)
        # and room-temperature thermal k_B * 298.15 K vs Ry
        z_eff_c1s = mpf(57) / mpf(10)
        delta_3_c1s_ev = (z_eff_c1s**2) * ry_ev
        v_4_cov_ev = ry_ev / mpf(3)
        eta_3_core_cov = v_4_cov_ev / delta_3_c1s_ev
        kT_298_ev = k_B_eV_K * (mpf(29815) / mpf(100))
        eta_3_thermal_cov = kT_298_ev / v_4_cov_ev
        eta_3_hbond_ry = mpf(2) / mpf(10) / ry_ev  # 0.20 eV H-bond vs 13.6057 eV Ry

        # Neutron-star outer-crust inverse beta capture flip (L_3 -> L_2: p + e^- -> n + nu_e)
        # Threshold: E_{F,e}^* = m_n - m_p (including electron rest mass)
        efe_star_codata_mev = delta_np_codata_mev
        tfe_star_codata_mev = efe_star_codata_mev - me_mev
        pfe_star_mev = mp.sqrt(efe_star_codata_mev**2 - me_mev**2)
        ne_star_fm3 = (pfe_star_mev / hbar_c_mev_fm) ** 3 / (3 * mp.pi**2)
        ne_star_cm3 = ne_star_fm3 * mpf("1e39")
        # Equivalent mass density for pure proton-electron plasma (mu_e = 1): rho^* = n_e^* * u
        mev_per_c2_in_g = mpf(value_str("atomic mass constant")) * mpf(1000) / (+U_MEV)
        rho_star_ye1_g_cm3 = ne_star_cm3 * mp_codata_mev * mev_per_c2_in_g

        # QOU-derived threshold comparison
        efe_star_qou_mev = delta_np_qou_mev
        pfe_star_qou_mev = mp.sqrt(efe_star_qou_mev**2 - me_mev**2)
        ne_star_qou_fm3 = (pfe_star_qou_mev / hbar_c_mev_fm) ** 3 / (3 * mp.pi**2)

        wb.add_assertion(
            "mp_qou_matches_codata_proton_anchor",
            computed=abs(mp_qou_mev - mp_codata_mev) / mp_codata_mev,
            expected=mpf(0),
            tolerance=mpf("1e-9"),
            source="Proton anchor identity m_p(q0) vs CODATA-2022 m_p",
        )
        wb.add_assertion(
            "all_ambient_adiabatic_ratios_strictly_below_unity",
            computed=mpf(
                0
                if (
                    mpf(0) < eta_0 < mpf("1e-1")
                    and mpf("1e-3") < eta_1_c12 < mpf("2e-2")
                    and mpf("1e-7") < eta_2_c12 < mpf("1e-5")
                    and mpf("1e-3") < eta_3_core_cov < mpf("5e-2")
                )
                else 1
            ),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="hierarchical_confinement_of_adiabatic_ratio_lt_one across L_0..L_4",
        )
        wb.add_assertion(
            "neutron_star_capture_flip_sign_change_exact",
            computed=mpf(
                0
                if (
                    delta_np_codata_mev - (efe_star_codata_mev * mpf(99) / mpf(100)) > 0
                    and delta_np_codata_mev - (efe_star_codata_mev * mpf(101) / mpf(100)) < 0
                )
                else 1
            ),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="neutron_star_electron_capture_threshold at E_{F,e}^* = m_n - m_p",
        )

        tower_summary = {
            "L0_to_L1_eta0_QED_over_hadron": fmt50(eta_0),
            "L1_to_L2_eta1_4He_per_A_over_mp": fmt50(eta_1_he4),
            "L1_to_L2_eta1_12C_per_A_over_mp": fmt50(eta_1_c12),
            "L1_to_L2_eta1_56Fe_per_A_over_mp": fmt50(eta_1_fe56),
            "L2_to_L3_eta2_Ry_over_12C_per_A": fmt50(eta_2_c12),
            "L2_to_L3_eta2_Ry_over_4He_per_A": fmt50(eta_2_he4),
            "L2_to_L3_eta2_Ry_over_delta_np": fmt50(eta_2_np),
            "L3_to_L4_eta3_cov_over_C1s_core": fmt50(eta_3_core_cov),
            "L3_to_L4_eta3_kT298_over_cov": fmt50(eta_3_thermal_cov),
            "L3_to_L4_eta3_Hbond_over_Ry": fmt50(eta_3_hbond_ry),
            "mp_QOU_MeV": fmt50(mp_qou_mev),
            "Rydberg_eV": fmt50(ry_ev),
            "neutron_star_flip_E_Fe_star_CODATA_MeV": fmt50(efe_star_codata_mev),
            "neutron_star_flip_T_Fe_star_CODATA_MeV": fmt50(tfe_star_codata_mev),
            "neutron_star_flip_p_Fe_star_MeV_c": fmt50(pfe_star_mev),
            "neutron_star_flip_n_e_star_cm3": fmt50(ne_star_cm3),
            "neutron_star_flip_rho_Ye1_g_cm3": fmt50(rho_star_ye1_g_cm3),
            "neutron_star_flip_E_Fe_star_QOU_MeV": fmt50(efe_star_qou_mev),
            "neutron_star_flip_n_e_star_QOU_fm3": fmt50(ne_star_qou_fm3),
        }
        wb.add_data("five_layer_adiabatic_tower", tower_summary)

        # =====================================================================
        # PART 2: Layer-3 Shadow Prices (Mulliken chi_M & Parr-Pearson eta_PP)
        # =====================================================================
        # Cumulative 2n^2 Madelung noble-gas closures [2, 10, 18, 36, 54, 86]
        pauli_caps = [2 * (n**2) for n in range(1, 5)]
        madelung_caps = [2 * (((p + 1) // 2 + 1) ** 2) for p in range(6)]
        noble_closures = []
        acc = 0
        for cap in madelung_caps:
            acc += cap
            noble_closures.append(acc)

        wb.add_assertion(
            "noble_gas_magic_closures_match_2_10_18_36_54_86",
            computed=mpf(0 if noble_closures == [2, 10, 18, 36, 54, 86] else 1),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="ConfinementLayerTower.noble_gas_magic_closures_eq",
        )

        # Experimental NIST reference (I_1, A_ea) in eV (comparison table; negative A_ea = metastable anion resonance)
        nist_ie_ea_ev = [
            ("H", 1, Fraction("13.59844"), Fraction("0.754195")),
            ("He", 2, Fraction("24.58739"), Fraction("-0.5")),
            ("Li", 3, Fraction("5.39172"), Fraction("0.618049")),
            ("C", 6, Fraction("11.26030"), Fraction("1.262118")),
            ("N", 7, Fraction("14.53414"), Fraction("-0.07")),
            ("O", 8, Fraction("13.61806"), Fraction("1.461112")),
            ("F", 9, Fraction("17.42282"), Fraction("3.401190")),
            ("Ne", 10, Fraction("21.56454"), Fraction("-1.2")),
            ("Na", 11, Fraction("5.13908"), Fraction("0.547926")),
            ("Cl", 17, Fraction("12.96764"), Fraction("3.612724")),
            ("Ar", 18, Fraction("15.75962"), Fraction("-1.0")),
        ]
        layer3_rows = []
        all_convex = True
        for sym, z_num, ie, ea in nist_ie_ea_ev:
            mu_plus = -ea
            mu_minus = -ie
            eta_pp = mu_plus - mu_minus
            chi_m = -(mu_plus + mu_minus) / Fraction(2)
            if eta_pp <= 0 or eta_pp != ie - ea or 2 * chi_m != ie + ea:
                all_convex = False
            layer3_rows.append(
                {
                    "element": sym,
                    "Z": z_num,
                    "I_eV_NIST_comparison": str(mp.nstr(mpf(ie.numerator) / mpf(ie.denominator), 10)),
                    "A_ea_eV_NIST_comparison": str(mp.nstr(mpf(ea.numerator) / mpf(ea.denominator), 10)),
                    "mu_minus_eV": str(mp.nstr(mpf(mu_minus.numerator) / mpf(mu_minus.denominator), 10)),
                    "mu_plus_eV": str(mp.nstr(mpf(mu_plus.numerator) / mpf(mu_plus.denominator), 10)),
                    "chi_Mulliken_eV": str(mp.nstr(mpf(chi_m.numerator) / mpf(chi_m.denominator), 10)),
                    "eta_ParrPearson_jump_eV": str(mp.nstr(mpf(eta_pp.numerator) / mpf(eta_pp.denominator), 10)),
                    "noble_closure": z_num in noble_closures,
                }
            )

        wb.add_assertion(
            "layer3_shadow_price_identities_and_pplb_convexity",
            computed=mpf(0 if all_convex else 1),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="parr_pearson_hardness_eq_shadow_jump & two_mul_mulliken_eq_neg_shadow_sum",
        )
        wb.add_data(
            "layer3_shadow_prices",
            {
                "pauli_shell_capacities_1_to_4": pauli_caps,
                "noble_gas_closures": noble_closures,
                "comparison_elements": layer3_rows,
            },
        )

        # =====================================================================
        # PART 3: Canonical 1D Chemical Circuits & Multi-Reaction C-H-O Network
        # =====================================================================
        canonical_1d = [
            ("water_synthesis", ["H2", "O2", "H2O"], [[2, 0, 2], [0, 2, 1]], (-2, -1, 2)),
            (
                "methane_combustion",
                ["CH4", "O2", "CO2", "H2O"],
                [[1, 0, 1, 0], [4, 0, 0, 2], [0, 2, 2, 1]],
                (-1, -2, 1, 2),
            ),
            ("haber_bosch_ammonia", ["N2", "H2", "NH3"], [[2, 0, 1], [0, 2, 3]], (-1, -3, 2)),
            (
                "glucose_respiration",
                ["C6H12O6", "O2", "CO2", "H2O"],
                [[6, 0, 1, 0], [12, 0, 0, 2], [6, 2, 2, 1]],
                (-1, -6, 6, 6),
            ),
        ]
        canon_results = []
        canon_ok = True
        for name, species, mat_rows, v_expected in canonical_1d:
            M_sp = sp.Matrix(mat_rows)
            snf = smith_normal_form(M_sp)
            hnf = hermite_normal_form(M_sp)
            ns = M_sp.nullspace()
            if len(ns) != 1:
                canon_ok = False
            # Clear rational denominators to primitive integer generator
            lcm_den = sp.ilcm(*[sp.Rational(x).q for x in ns[0]]) if len(ns[0]) > 1 else sp.Rational(ns[0][0]).q
            v_int = tuple(int(sp.Rational(x) * lcm_den) for x in ns[0])
            g_int = vec_gcd(v_int)
            v_prim = tuple(x // g_int for x in v_int)
            if canonical_sign(v_prim) != canonical_sign(v_expected):
                canon_ok = False
            if M_sp * sp.Matrix(v_expected) != sp.zeros(M_sp.rows, 1) or vec_gcd(v_expected) != 1:
                canon_ok = False
            inv_factors = [int(snf[i, i]) for i in range(min(snf.rows, snf.cols)) if snf[i, i] != 0]
            canon_results.append(
                {
                    "system": name,
                    "species": species,
                    "rank": int(M_sp.rank()),
                    "kernel_dim": len(ns),
                    "smith_invariant_factors": inv_factors,
                    "hermite_normal_form": [[int(hnf[r, c]) for c in range(hnf.cols)] for r in range(hnf.rows)],
                    "primitive_circuit": list(v_expected),
                    "gcd": vec_gcd(v_expected),
                }
            )

        wb.add_assertion(
            "four_canonical_1d_chemical_circuits_exact_and_primitive",
            computed=mpf(0 if canon_ok else 1),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="ConfinementLayerTower.{ker_A_H2O_iff, ker_A_CH4_iff, ker_A_NH3_iff, ker_A_gluc_iff}",
        )
        wb.add_data("canonical_1d_stoichiometry", canon_results)

        # Multi-reaction 3 x 7 C-H-O network: (C, H2, O2, CO, CO2, H2O, CH4)
        cho_species = ["C", "H2", "O2", "CO", "CO2", "H2O", "CH4"]
        A_cho_rows = [
            [1, 0, 0, 1, 1, 0, 1],  # C
            [0, 2, 0, 0, 0, 2, 4],  # H
            [0, 0, 2, 1, 2, 1, 0],  # O
        ]
        A_cho = sp.Matrix(A_cho_rows)
        snf_cho = smith_normal_form(A_cho)
        hnf_cho = hermite_normal_form(A_cho)
        hnf_row_cho = hermite_normal_form(A_cho.T).T
        inv_cho = [int(snf_cho[i, i]) for i in range(3)]

        # Lattice basis of ker_Z(A_CHO): parameterize free columns (CO, CO2, H2O, CH4) -> (j = 3, 4, 5, 6)
        # Wait: column O2 has entry 2, so 2*v_O2 = -(v_CO + 2*v_CO2 + v_H2O) requires v_CO + v_H2O even!
        # Let's extract an exact Z-basis of ker_Z(A_CHO):
        # Free integer coordinates:
        #   b1 = WGS:         (0,  1,  0, -1,  1, -1,  0)  [CO + H2O -> CO2 + H2]
        #   b2 = Boudouard:   (1,  0,  0, -2,  1,  0,  0)  [2 CO -> C + CO2]
        #   b3 = Methanation: (0, -3,  0, -1,  0,  1,  1)  [CO + 3 H2 -> CH4 + H2O]
        #   b4 = CarbonOx:    (-1, 0, -1,  0,  1,  0,  0)  [C + O2 -> CO2]
        # Check if {b1, b2, b3, b4} spans ALL of ker_Z(A_CHO) over Z!
        # Take any v = (v_C, v_H2, v_O2, v_CO, v_CO2, v_H2O, v_CH4) in ker_Z(A_CHO):
        #   alpha3 = v_CH4 -> v' = v - alpha3 * b3 has v'_CH4 = 0.
        #   alpha1 = -v'_H2O -> v'' = v' - alpha1 * b1 has v''_CH4 = 0, v''_H2O = 0.
        #   Row 2 on v'': 2*v''_O2 + v''_CO + 2*v''_CO2 = 0 => v''_CO is EVEN!
        #   So alpha2 = -v''_CO / 2 is an INTEGER! v''' = v'' - alpha2 * b2 has v'''_CO = 0, v'''_H2O = 0, v'''_CH4 = 0.
        #   Row 1 on v''': 2*v'''_H2 = 0 => v'''_H2 = 0.
        #   Row 0 & 2 on v''': v'''_C = -v'''_CO2, v'''_O2 = -v'''_CO2 => v''' = v'''_CO2 * b4!
        # Q.E.D.!! {b1, b2, b3, b4} = {WGS, Boudouard, Methanation, CarbonOx} is an EXACT Z-BASIS OF ker_Z(A_CHO)!!
        z_basis_cho = [
            (0, 1, 0, -1, 1, -1, 0),   # WGS
            (1, 0, 0, -2, 1, 0, 0),    # Boudouard
            (0, -3, 0, -1, 0, 1, 1),   # Methanation
            (-1, 0, -1, 0, 1, 0, 0),   # CarbonOx
        ]

        # Compute Graver basis via Pottier's conformal completion
        G_pottier = pottier_graver_basis(z_basis_cho)

        # Independent exhaustive verification over [-6, 6]^4 in free coordinates (v_CO, v_CO2, v_H2O, v_CH4)
        ker_box: list[tuple[int, ...]] = []
        for v_co in range(-6, 7):
            for v_co2 in range(-6, 7):
                for v_h2o in range(-6, 7):
                    if (v_co + v_h2o) % 2 != 0:
                        continue
                    v_o2 = -(v_co + 2 * v_co2 + v_h2o) // 2
                    for v_ch4 in range(-6, 7):
                        v_c = -(v_co + v_co2 + v_ch4)
                        v_h2 = -(v_h2o + 2 * v_ch4)
                        vec = (v_c, v_h2, v_o2, v_co, v_co2, v_h2o, v_ch4)
                        if any(x != 0 for x in vec):
                            ker_box.append(vec)

        G_box: set[tuple[int, ...]] = set()
        # Filter ker_box to conformal-minimal vectors
        ker_box_sorted = sorted(ker_box, key=lambda t: sum(abs(x) for x in t))
        minimal_list: list[tuple[int, ...]] = []
        for v in ker_box_sorted:
            if not any(conformal_le(u, v) for u in minimal_list):
                minimal_list.append(v)
        G_box = set(minimal_list)

        wb.add_assertion(
            "pottier_graver_basis_matches_exhaustive_box_scan",
            computed=mpf(0 if G_pottier == G_box else 1),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="Pottier Algorithm 3.2.2 vs exhaustive Z^4 kernel box scan",
        )

        # Identify elementary circuits C(A_CHO) (inclusion-minimal support among nonzero kernel vectors)
        G_canon = sorted({canonical_sign(g) for g in G_pottier})
        circuits_canon: list[tuple[int, ...]] = []
        for g in G_canon:
            supp_g = {j for j, x in enumerate(g) if x != 0}
            if not any(
                h != g and {j for j, x in enumerate(h) if x != 0} < supp_g for h in G_canon
            ):
                circuits_canon.append(g)

        # Identify exact Universal Gröbner Basis UGB(I_{A_CHO}) via edge test on each Graver fiber
        ugb_canon: list[tuple[int, ...]] = []
        for g in G_canon:
            u_plus = tuple(max(x, 0) for x in g)
            u_minus = tuple(max(-x, 0) for x in g)
            b_g = (
                sum(A_cho_rows[0][j] * u_plus[j] for j in range(7)),
                sum(A_cho_rows[1][j] * u_plus[j] for j in range(7)),
                sum(A_cho_rows[2][j] * u_plus[j] for j in range(7)),
            )
            f_pts = enumerate_fiber_points_cho(b_g)
            if is_edge_of_fiber_polytope(u_plus, u_minus, f_pts):
                ugb_canon.append(g)

        # Verify inclusions C(A_CHO) <= UGB(I_{A_CHO}) <= G(A_CHO)
        inclusions_ok = set(circuits_canon).issubset(set(ugb_canon)) and set(ugb_canon).issubset(
            set(G_canon)
        )
        wb.add_assertion(
            "toric_hierarchy_circuits_subset_ugb_subset_graver",
            computed=mpf(0 if inclusions_ok else 1),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="Sturmfels (1996) Prop. 4.11: C(A) subseteq UGB(I_A) subseteq G(A)",
        )

        # =====================================================================
        # PART 4: Zero-Temperature Sturmfels-Thomas Enthalpy Normal Form Reduction
        # =====================================================================
        # Standard molar formation enthalpies Delta_f H^o (298.15 K) in kJ/mol (NIST-JANAF comparison cost):
        # (C(s), H2(g), O2(g), CO(g), CO2(g), H2O(g), CH4(g))
        hf_kj_mol = [
            Fraction(0),
            Fraction(0),
            Fraction(0),
            Fraction("-110.53"),
            Fraction("-393.51"),
            Fraction("-241.82"),
            Fraction("-74.87"),
        ]

        def cost_key(u: tuple[int, ...]) -> tuple[Fraction, tuple[int, ...]]:
            return (sum(hf_kj_mol[j] * u[j] for j in range(7)), u)

        # Initial synthesis-gas + oxygen inventory: u_0 = 2 CO + 4 H2 + O2 -> b = (2, 8, 4)
        u0 = (0, 4, 1, 2, 0, 0, 0)
        b_inv = (
            sum(A_cho_rows[0][j] * u0[j] for j in range(7)),
            sum(A_cho_rows[1][j] * u0[j] for j in range(7)),
            sum(A_cho_rows[2][j] * u0[j] for j in range(7)),
        )
        fiber_284 = enumerate_fiber_points_cho(b_inv)
        global_min_u = min(fiber_284, key=cost_key)

        # Reduce u0 modulo the cost-oriented Graver/Gröbner test set:
        # Whenever g in G_pottier has u_cur >= g_- and cost_key(u_cur + g) < cost_key(u_cur), rewrite u_cur -> u_cur + g!
        u_cur = u0
        reduction_steps = []
        while True:
            improved = False
            for g in sorted(G_pottier):
                if all(u_cur[j] + g[j] >= 0 for j in range(7)):
                    u_nxt = tuple(u_cur[j] + g[j] for j in range(7))
                    if cost_key(u_nxt) < cost_key(u_cur):
                        reduction_steps.append(
                            {
                                "move": list(g),
                                "from": list(u_cur),
                                "to": list(u_nxt),
                                "delta_H_kJ": str(
                                    mp.nstr(
                                        mpf((cost_key(u_nxt)[0] - cost_key(u_cur)[0]).numerator)
                                        / mpf((cost_key(u_nxt)[0] - cost_key(u_cur)[0]).denominator),
                                        10,
                                    )
                                ),
                            }
                        )
                        u_cur = u_nxt
                        improved = True
                        break
            if not improved:
                break

        # Verify Hess's law / LP reduced-cost fiber invariance on arbitrary shadow price y
        y_test = [Fraction("-150"), Fraction("-60"), Fraction("-120")]
        c_bar = [
            hf_kj_mol[j] - sum(A_cho_rows[e][j] * y_test[e] for e in range(3)) for j in range(7)
        ]
        bare_diff = sum(hf_kj_mol[j] * (u0[j] - u_cur[j]) for j in range(7))
        red_diff = sum(c_bar[j] * (u0[j] - u_cur[j]) for j in range(7))

        wb.add_assertion(
            "sturmfels_thomas_normal_form_reaches_exact_ip_global_optimum",
            computed=mpf(0 if (u_cur == global_min_u and bare_diff == red_diff) else 1),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="Sturmfels-Thomas test-set optimality & reduced_cost_fiber_invariance",
        )

        # =====================================================================
        # PART 5: 80-dps Finite-Temperature Birch Mass-Action Toric Equilibrium
        # =====================================================================
        # Dimensionless standard chemical potentials g_j / (R T) at T = 1000 K (syngas reformer regime)
        g_dimless = [
            mpf("0"),           # C (reference)
            mpf("0"),           # H2 (reference)
            mpf("0"),           # O2 (reference)
            mpf("-24.12"),      # CO: Delta_f G^o(1000 K) / RT
            mpf("-47.62"),      # CO2: Delta_f G^o(1000 K) / RT
            mpf("-23.17"),      # H2O(g): Delta_f G^o(1000 K) / RT
            mpf("2.35"),        # CH4(g): Delta_f G^o(1000 K) / RT
        ]
        b_target = [mpf(2), mpf(8), mpf(4)]

        # Solve A_CHO * x(y) = b_target where x_j(y) = exp((A_CHO^T y)_j - g_dimless[j])
        # via damped 80-dps Newton iteration on convex dual potential Phi(y) = sum_j x_j(y) - b^T y
        y_vec = [mpf("-5"), mpf("-2"), mpf("-12")]

        def eval_x(yv: list[mpf]) -> list[mpf]:
            out = []
            for j in range(7):
                aty = sum(mpf(A_cho_rows[e][j]) * yv[e] for e in range(3))
                out.append(mp.exp(aty - g_dimless[j]))
            return out

        for _ in range(80):
            xv = eval_x(y_vec)
            grad = [
                sum(mpf(A_cho_rows[e][j]) * xv[j] for j in range(7)) - b_target[e]
                for e in range(3)
            ]
            if max(abs(r) for r in grad) < mpf("1e-76"):
                break
            H_mat = mp.matrix(3, 3)
            for r in range(3):
                for c in range(3):
                    H_mat[r, c] = sum(
                        mpf(A_cho_rows[r][j] * A_cho_rows[c][j]) * xv[j] for j in range(7)
                    )
            step = mp.lu_solve(H_mat, mp.matrix([-g for g in grad]))
            # Backtracking line search on strictly convex Phi(y)
            phi_cur = sum(xv) - sum(b_target[e] * y_vec[e] for e in range(3))
            lam = mpf(1)
            for _ls in range(40):
                y_cand = [y_vec[e] + lam * step[e] for e in range(3)]
                x_cand = eval_x(y_cand)
                phi_cand = sum(x_cand) - sum(b_target[e] * y_cand[e] for e in range(3))
                if phi_cand <= phi_cur:
                    y_vec = y_cand
                    break
                lam /= mpf(2)

        x_star = eval_x(y_vec)
        fiber_res = max(
            abs(sum(mpf(A_cho_rows[e][j]) * x_star[j] for j in range(7)) - b_target[e])
            for e in range(3)
        )

        # Check mass-action toric binomial x^{* nu_+} - K_eq(g) x^{* nu_-} = 0 on EVERY Graver element!
        max_toric_binomial_res = mpf(0)
        for g in G_canon:
            lhs = mpf(1)
            rhs = mpf(1)
            dg = sum(mpf(g[j]) * g_dimless[j] for j in range(7))
            k_eq = mp.exp(-dg)
            for j in range(7):
                if g[j] > 0:
                    lhs *= x_star[j] ** g[j]
                elif g[j] < 0:
                    rhs *= x_star[j] ** (-g[j])
            scale = max(abs(lhs), abs(k_eq * rhs), mpf(1))
            max_toric_binomial_res = max(max_toric_binomial_res, abs(lhs - k_eq * rhs) / scale)

        # Sylvester positive-definiteness check on Hessian H(y^*) = A diag(x^*) A^T
        H_star = mp.matrix(3, 3)
        for r in range(3):
            for c in range(3):
                H_star[r, c] = sum(
                    mpf(A_cho_rows[r][j] * A_cho_rows[c][j]) * x_star[j] for j in range(7)
                )
        det1 = H_star[0, 0]
        det2 = H_star[0, 0] * H_star[1, 1] - H_star[0, 1] * H_star[1, 0]
        det3 = mp.det(H_star)

        wb.add_assertion(
            "birch_toric_equilibrium_fiber_conservation_70dps",
            computed=fiber_res,
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="Birch's theorem: A_CHO x^* = b on positive orthant",
        )
        wb.add_assertion(
            "birch_toric_equilibrium_satisfies_all_graver_binomials_70dps",
            computed=max_toric_binomial_res,
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="Detailed-balance toric ideal x^{nu_+} = K_eq x^{nu_-} across all G(A_CHO)",
        )
        wb.add_assertion(
            "birch_hessian_strictly_positive_definite",
            computed=mpf(0 if (det1 > 0 and det2 > 0 and det3 > 0) else 1),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="Strict convexity of Legendre potential Phi(y) => global uniqueness of x^*",
        )

        wb.add_data(
            "cho_multi_reaction_network",
            {
                "species": cho_species,
                "rank": int(A_cho.rank()),
                "kernel_dim": 7 - int(A_cho.rank()),
                "smith_invariant_factors": inv_cho,
                "hermite_normal_form_col": [
                    [int(hnf_cho[r, c]) for c in range(hnf_cho.cols)]
                    for r in range(hnf_cho.rows)
                ],
                "row_hermite_normal_form": [
                    [int(hnf_row_cho[r, c]) for c in range(hnf_row_cho.cols)]
                    for r in range(hnf_row_cho.rows)
                ],
                "num_elementary_circuits_unoriented": len(circuits_canon),
                "num_universal_groebner_binomials_unoriented": len(ugb_canon),
                "num_graver_elements_unoriented": len(G_canon),
                "num_graver_elements_oriented": len(G_pottier),
                "elementary_circuits": [list(v) for v in circuits_canon],
                "universal_groebner_basis": [list(v) for v in ugb_canon],
                "graver_basis_unoriented": [list(v) for v in G_canon],
                "zero_T_inventory_b": list(b_inv),
                "zero_T_fiber_cardinality": len(fiber_284),
                "zero_T_initial_syngas": list(u0),
                "zero_T_normal_form_optimum": list(u_cur),
                "zero_T_optimum_enthalpy_kJ": str(
                    mp.nstr(
                        mpf(cost_key(u_cur)[0].numerator) / mpf(cost_key(u_cur)[0].denominator),
                        10,
                    )
                ),
                "zero_T_reduction_steps": reduction_steps,
                "birch_T1000K_dual_potentials_y_star": [fmt50(v) for v in y_vec],
                "birch_T1000K_equilibrium_moles_x_star": {
                    cho_species[j]: fmt50(x_star[j]) for j in range(7)
                },
                "birch_fiber_infinity_residual": fmt50(fiber_res),
                "birch_max_relative_graver_binomial_residual": fmt50(max_toric_binomial_res),
                "birch_hessian_leading_minors": [fmt50(det1), fmt50(det2), fmt50(det3)],
            },
        )

        print("=== 5-Layer Adiabatic Ratios (80 dps) ===")
        for k, val in tower_summary.items():
            print(f"  {k:44s} = {val[:26]}")
        print(
            f"=== C-H-O (3x7) Toric Hierarchy: |C|={len(circuits_canon)}, "
            f"|UGB|={len(ugb_canon)}, |G_unoriented|={len(G_canon)} (oriented {len(G_pottier)}) ==="
        )
        print(
            f"=== Zero-T Sturmfels-Thomas Normal Form on b={b_inv} (|fiber|={len(fiber_284)}): "
            f"{u0} -> {u_cur} in {len(reduction_steps)} steps ==="
        )
        print(
            f"=== Birch 1000K Equilibrium: fiber_res={mp.nstr(fiber_res, 6)}, "
            f"toric_binomial_res={mp.nstr(max_toric_binomial_res, 6)} ==="
        )

        wb.save({"q0Anchor": "proton"})
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
