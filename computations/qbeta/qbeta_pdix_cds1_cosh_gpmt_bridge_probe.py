#!/usr/bin/env python3
"""
qbeta-pdix-cds1-cosh-gpmt-bridge-probe — 50-dps evaluation of the two active
candidate mechanisms bridging the Convention D Q_beta ladder & base gap
(qou-pdix -> qou-cds1):

  Lever A (Re-opened KZ / Kohno-Drinfeld Hyperbolic cosh Holonomy on z_D):
    In NucleonIdempotentModifiedTrace.lean §2 (`chi3_fullTwistNF`,
    `chi111_fullTwistNF`), the 6-crossing 3-strand full-twist framing element
    Delta_3^2 = w_0^2 = (sigma_0 * sigma_1 * sigma_0)^2 (matching the 6-crossing
    Borromean core length of the nucleon) acts with exact eigenvalues q^{+6}
    on (3) and q^{-6} on (1^3). Its bar-even / mirror-symmetrized Kohno-Drinfeld
    hyperbolic character is:
      C_KD^{(6)}(q) = (q^6 + q^{-6}) / 2 = cosh(6 * ln q)
      C_KD^{(6)}(q) - 1 = (q^6 - 1)^2 / (2 * q^6) > 0.
    We evaluate the pre-registered parameter-free family C_KD^{(k)}(q) =
    (q^k + q^{-k}) / 2 = cosh(k * ln q) for k in {1, 2, 3, 6} on the ruled z_D
    base across the census candidates, together with the Convention-D N=1
    (cos(alpha_D - u/2)), N=2 (1 - u^2) ladder rungs and the two-term connected
    Borromean V^3 QED correction Delta_m_QED^conn = -0.331696 keV.

  Lever B (GPMT (1^3) Modified-Trace Completion of tr_M^{z_D} where w_{(1^3)}(z_D) = 0):
    In NucleonIdempotentModifiedTrace.lean §3-§5 (`w111_conventionD`, `dMod111`,
    `tMod111`), the standard Markov trace tr_M^{z_D} vanishes on the antisymmetric
    cubed-antifundamental sector (1^3) because w_{(1^3)}(z_D) = 0 at z_D = q^3/(q^2+1),
    while the Geer-Patureau-Mirand-Turaev (GPMT) modified trace restores (1^3) with
    modified quantum dimension d_D(S^{(1^3)}) = -1/([2]_q[3]_q) =
    -q^3/((q^2+1)(q^4+q^2+1)) and magnitude |d_D(S^{(1^3)})| = +1/([2]_q[3]_q) > 0.
    We evaluate the exact Wedderburn characters (chi_{(3)}, chi_{(2,1)}, chi_{(1^3)})
    and both GPMT completions:
      tr_M^{D,GPMT+}(v) = tr_M^{z_D}(v) - t_D^{(1^3)}(v)
                        = w_{(3)}(z_D)*chi_{(3)}(v) + w_{(2,1)}(z_D)*chi_{(2,1)}(v)
                          + (1/([2]_q[3]_q))*chi_{(1^3)}(v)
      tr_M^{D,GPMT-}(v) = tr_M^{z_D}(v) + t_D^{(1^3)}(v)
                        = w_{(3)}(z_D)*chi_{(3)}(v) + w_{(2,1)}(z_D)*chi_{(2,1)}(v)
                          - (1/([2]_q[3]_q))*chi_{(1^3)}(v)
    across all 4 census candidates (`delta_S`, `nuc9`, `nuc11_interleaved`,
    `nuc11_gen_grouped`) and both E_0 forms (`tower_summed` and `order_zero`),
    and measure the resulting effect on Q_beta, m_n, Delta_{pn}, the remaining
    ladder factor F_rem, and the LadderUniformBound C_min threshold.

Rule compliance:
  - 60-dps internal mpmath arithmetic (`set_compute_dps(60)` at module scope).
  - Zero `float()` conversions anywhere in this script.
  - Zero fitted parameters; all candidate expressions are parameter-free rational/
    hyperbolic functions of q_0 at the proton pin.

Tracking beans: qou-pdix, qou-cds1
Lean companion: folio/quantum-observable-universe/lean/QOU/QBeta/CoshHolonomyAndGPMTBaseBridge.lean
"""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for _p in (
    "computations",
    "computations/qbeta",
    "computations/substrate",
    "tools/qou-substrate/python",
    "tools/pyhecke/python",
):
    _s = os.path.join(ROOT, _p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from codata_2022_source import (  # noqa: E402
    M_E_MEV,
    M_N_MEV_AME_DERIVED,
    M_P_MEV,
    Q_BETA_MEV_AME,
)
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
import qbeta_e0  # noqa: E402
from qbeta_utils import (  # noqa: E402
    chi_block_3,
    chi_block_21,
    chi_block_111,
    d_mod_111_convention_D,
    substrate_ladder_quantities,
)
from qou_substrate.codata import codata as _codata  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(60)
mp.mp.dps = 60

# Load canonical census constructors from qbeta_delta_candidate_census_probe.py
_CEN = os.path.join(ROOT, "computations", "qbeta", "qbeta_delta_candidate_census_probe.py")
_spec = importlib.util.spec_from_file_location("_census", _CEN)
assert _spec is not None and _spec.loader is not None
_census = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_census)
set_compute_dps(60)
mp.mp.dps = 60

h_sym = _census.h
ZERO, ONE = _census.ZERO, _census.ONE
Q0_RAT = sp.Rational(Q_50_DIGIT_STR)
H0_RAT = Q0_RAT - 1 / Q0_RAT


def fmt(val: mp.mpf, digits: int = 50) -> str:
    """Format an mpmath mpf at 50 significant digits without float64."""
    return mp.nstr(val, digits)


def at_q0_mpf(expr) -> mp.mpf:
    """Exact h -> h(q_0) substitution, converted to 60-dps mpf with zero float64."""
    return mp.mpf(str(sp.N(sp.sympify(expr).subs(h_sym, H0_RAT), 65)))


def build_census_vectors() -> dict[str, dict[str, object]]:
    """Return the 4 canonical census difference elements in the 6-element H_3(q) basis.

    Note: `_census.BASIS = ["gamma", "sigma_0", "sigma_1", "L-", "L+", "e^-"]`.
    """
    _census._assert_slots()
    delta_s_sym = [h_sym**2 / 2, -h_sym / 2, -h_sym / 2, ZERO, ZERO, ZERO]
    nuc9_sym = _census.delta(_census.nuc9("n"), _census.nuc9("p"))
    nuc11_int_sym = _census.delta(_census.nuc11_interleaved("n"), _census.nuc11_interleaved("p"))
    nuc11_grp_sym = _census.delta(_census.nuc11_gen_grouped("n"), _census.nuc11_gen_grouped("p"))

    def _to_mpf_vec(sym_vec):
        return [at_q0_mpf(c) for c in sym_vec]

    return {
        "delta_S": {
            "vector": _to_mpf_vec(delta_s_sym),
            "crossing_length": 1,
            "description": "Single-crossing linear generator element Delta_S = (h^2/2)*1 - (h/2)*(sigma_0 + sigma_1)",
        },
        "nuc9": {
            "vector": _to_mpf_vec(nuc9_sym),
            "crossing_length": 9,
            "description": "9-crossing nucleon word difference build_nucleon_nf(n) - build_nucleon_nf(p)",
        },
        "nuc11_interleaved": {
            "vector": _to_mpf_vec(nuc11_int_sym),
            "crossing_length": 11,
            "description": "11-crossing interleaved nucleon word difference build_atom_nf_exact(n) - build_atom_nf_exact(p) (LIVE SCORED Form-B cell)",
        },
        "nuc11_gen_grouped": {
            "vector": _to_mpf_vec(nuc11_grp_sym),
            "crossing_length": 11,
            "description": "11-crossing generator-grouped nucleon word difference nucleon_gen_chains(n) - nucleon_gen_chains(p)",
        },
    }


def wedderburn_characters_from_census_vec(vec: list[mp.mpf], q0: mp.mpf) -> dict[str, mp.mpf]:
    """Compute exact Wedderburn sector characters (chi_3, chi_21, chi_111) on H_3(q).

    Slot order from `_census.BASIS`:
      vec[0] = 1 (gamma)
      vec[1] = sigma_0
      vec[2] = sigma_1
      vec[3] = L- = sigma_1 * sigma_0
      vec[4] = L+ = sigma_0 * sigma_1
      vec[5] = e^- = sigma_0 * sigma_1 * sigma_0

    Basis character values from `NucleonIdempotentModifiedTrace.lean` §2 (`chiM_eq_closed`):
      chi_{(3)}   = [1, q, q, q^2, q^2, q^3]
      chi_{(2,1)} = [2, h, h, -1,  -1,  0]      where h = q - q^{-1}
      chi_{(1^3)} = [1, -q^{-1}, -q^{-1}, q^{-2}, q^{-2}, -q^{-3}]
    """
    h0 = q0 - mp.mpf(1) / q0
    q_inv = mp.mpf(1) / q0

    c0, c1, c2, c_lm, c_lp, c_w0 = vec
    chi3 = c0 + q0 * (c1 + c2) + (q0**2) * (c_lm + c_lp) + (q0**3) * c_w0
    chi21 = mp.mpf(2) * c0 + h0 * (c1 + c2) - (c_lm + c_lp)
    chi111 = c0 - q_inv * (c1 + c2) + (q_inv**2) * (c_lm + c_lp) - (q_inv**3) * c_w0
    return {
        "chi_3": chi3,
        "chi_21": chi21,
        "chi_111": chi111,
    }


def convention_d_weights_mpf(q0: mp.mpf) -> dict[str, mp.mpf]:
    """Convention-D Markov weights at z_D = q^3/(q^2+1) and GPMT (1^3) modified dimension."""
    w3_zD = (q0**4 + mp.mpf(1)) / ((q0**2 + mp.mpf(1)) ** 2)
    w21_zD = (q0**2) / ((q0**2 + mp.mpf(1)) ** 2)
    w111_zD = mp.mpf(0)

    q_num_2 = q0 + mp.mpf(1) / q0
    q_num_3 = q0**2 + mp.mpf(1) + mp.mpf(1) / (q0**2)
    d_mod_111 = -mp.mpf(1) / (q_num_2 * q_num_3)
    d_mod_111_abs = -d_mod_111
    d_mod_111_rational = d_mod_111_convention_D(q0)
    return {
        "w3_zD": w3_zD,
        "w21_zD": w21_zD,
        "w111_zD": w111_zD,
        "q_num_2": q_num_2,
        "q_num_3": q_num_3,
        "d_mod_111": d_mod_111,
        "d_mod_111_abs": d_mod_111_abs,
        "d_mod_111_rational_residual": abs(d_mod_111 - d_mod_111_rational),
    }


def solve_c_min_uniform(u0: mp.mpf, f_rem: mp.mpf, k_max: int = 20) -> mp.mpf:
    """Compute the LadderUniformBound uniform coefficient threshold C_min(K) for F_rem > 1:
    C_min(K) = (F_rem - 1) / sum_{k=2}^K u0^(2k) = (F_rem - 1) * (1 - u0^2) / (u0^4 * (1 - u0^(2*(K-1)))).
    """
    if f_rem <= mp.mpf(1):
        return mp.mpf(0)
    tail_sum = sum(u0 ** (2 * k) for k in range(2, k_max + 1))
    return (f_rem - mp.mpf(1)) / tail_sum


def compute_two_term_borromean_qed_mev(q0: mp.mpf, me_codata: mp.mpf) -> dict[str, mp.mpf]:
    """Compute the connected fourth-order Borromean V^3 QED correction
    (`NucleonWeightSpaceTwoTerm.trace_QAdj_connected_diff_borromeanV3`):
      Delta_tr_QAdj^conn(V^3) = (q - 1)^4 * (q + 1)^4 * (4*q^4 + q^2 + 4) / (9 * q^6)
      Delta_m_QED^conn(V^3)   = -(m_e / 3) * Delta_tr_QAdj^conn(V^3).
    """
    delta_tr_conn = (
        ((q0 - mp.mpf(1)) ** 4)
        * ((q0 + mp.mpf(1)) ** 4)
        * (mp.mpf(4) * (q0**4) + (q0**2) + mp.mpf(4))
        / (mp.mpf(9) * (q0**6))
    )
    delta_m_qed_two_term = -(me_codata / mp.mpf(3)) * delta_tr_conn
    return {
        "delta_tr_QAdj_conn_borromeanV3": delta_tr_conn,
        "delta_m_qed_two_term_mev": delta_m_qed_two_term,
    }


def evaluate_lever_b_gpmt(
    q0: mp.mpf,
    u0: mp.mpf,
    e0_map: dict[str, mp.mpf],
    census: dict[str, dict[str, object]],
    gpmt_info: dict[str, mp.mpf],
    q_codata: mp.mpf,
    mn_codata: mp.mpf,
    mp_codata: mp.mpf,
    me_codata: mp.mpf,
) -> dict[str, object]:
    """Evaluate Lever B: GPMT (1^3) modified-trace completion across all 4 census candidates and 2 E0 forms."""
    w3_zD = gpmt_info["w3_zD"]
    w21_zD = gpmt_info["w21_zD"]
    d_mod_111 = gpmt_info["d_mod_111"]
    dpn_codata = mn_codata - mp_codata

    character_table: dict[str, object] = {}
    grid_cells: dict[str, object] = {}

    for cand_key, cand_meta in census.items():
        vec = cand_meta["vector"]
        decomp = wedderburn_characters_from_census_vec(vec, q0)
        chi3 = decomp["chi_3"]
        chi21 = decomp["chi_21"]
        chi111 = decomp["chi_111"]

        tr_zD = w3_zD * chi3 + w21_zD * chi21
        t_mod_111 = d_mod_111 * chi111
        # GPMT+ restores (1^3) with positive modified dimension magnitude |d_D(S^{(1^3)})| = -d_D(S^{(1^3)})
        tr_gpmt_pos = tr_zD - t_mod_111
        # GPMT- adds signed modified trace +t_D^{(1^3)} = d_D(S^{(1^3)}) * chi_{(1^3)}
        tr_gpmt_signed = tr_zD + t_mod_111

        boost_pos = tr_gpmt_pos / tr_zD
        boost_signed = tr_gpmt_signed / tr_zD

        character_table[cand_key] = {
            "crossing_length": cand_meta["crossing_length"],
            "description": cand_meta["description"],
            "chi_3": fmt(chi3),
            "chi_21": fmt(chi21),
            "chi_111": fmt(chi111),
            "chi_111_over_chi_3": fmt(chi111 / chi3),
            "t_mod_111": fmt(t_mod_111),
            "tr_M_zD": fmt(tr_zD),
            "tr_M_D_GPMT_pos": fmt(tr_gpmt_pos),
            "tr_M_D_GPMT_signed": fmt(tr_gpmt_signed),
            "boost_factor_GPMT_pos": fmt(boost_pos),
            "boost_factor_GPMT_signed": fmt(boost_signed),
            "chi3_chi111_same_sign": bool(chi3 * chi111 > 0),
        }

        for e0_key, e0_val in e0_map.items():
            for trace_label, tr_val in [
                ("zD_bare", tr_zD),
                ("zD_GPMT_pos", tr_gpmt_pos),
                ("zD_GPMT_signed", tr_gpmt_signed),
            ]:
                cell_id = f"{cand_key}__{e0_key}__{trace_label}"
                q_pred = -e0_val * tr_val
                rel_q = (q_pred - q_codata) / q_codata
                mn_pred = mp_codata + me_codata + q_pred
                mn_ppm = (mn_pred - mn_codata) / mn_codata * mp.mpf("1e6")
                dpn_pred = me_codata + q_pred
                dpn_rel = (dpn_pred - dpn_codata) / dpn_codata
                f_rem = q_codata / q_pred
                c_min = solve_c_min_uniform(u0, f_rem, k_max=20)

                grid_cells[cell_id] = {
                    "candidate": cand_key,
                    "e0_variant": e0_key,
                    "trace_variant": trace_label,
                    "E0_MeV": fmt(e0_val),
                    "trace_value": fmt(tr_val),
                    "Q_beta_MeV": fmt(q_pred),
                    "Q_beta_rel_err": fmt(rel_q),
                    "Q_beta_pct_err": fmt(rel_q * 100),
                    "m_n_MeV": fmt(mn_pred),
                    "m_n_ppm_err": fmt(mn_ppm),
                    "Delta_pn_MeV": fmt(dpn_pred),
                    "Delta_pn_pct_err": fmt(dpn_rel * 100),
                    "F_rem_to_CODATA": fmt(f_rem),
                    "in_elliptic_cosine_reach": bool(mp.mpf(0) < f_rem <= mp.mpf(1)),
                    "C_min_K20": fmt(c_min),
                }

    # Verify exact algebraic identities proved in CoshHolonomyAndGPMTBaseBridge.lean:
    d_delta_s = wedderburn_characters_from_census_vec(census["delta_S"]["vector"], q0)
    id_delta_s_anti = abs(d_delta_s["chi_111"] + d_delta_s["chi_3"])
    id_delta_s_21 = abs(d_delta_s["chi_21"])

    d_nuc9 = wedderburn_characters_from_census_vec(census["nuc9"]["vector"], q0)
    id_nuc9_eq = abs(d_nuc9["chi_111"] - d_nuc9["chi_3"])

    d_nuc11_int = wedderburn_characters_from_census_vec(census["nuc11_interleaved"]["vector"], q0)
    d_nuc11_grp = wedderburn_characters_from_census_vec(census["nuc11_gen_grouped"]["vector"], q0)
    id_nuc11_int_q4 = abs(d_nuc11_int["chi_111"] - (q0 ** (-4)) * d_nuc11_int["chi_3"])
    id_nuc11_grp_q4 = abs(d_nuc11_grp["chi_111"] - (q0 ** (-4)) * d_nuc11_grp["chi_3"])
    id_nuc11_same_extremal = abs(d_nuc11_int["chi_3"] - d_nuc11_grp["chi_3"]) + abs(
        d_nuc11_int["chi_111"] - d_nuc11_grp["chi_111"]
    )
    id_nuc11_closed_form = (
        abs(d_nuc11_int["chi_3"] - chi_block_3(q0))
        + abs(d_nuc11_int["chi_21"] - chi_block_21(q0, intra_order="borromean"))
        + abs(d_nuc11_grp["chi_21"] - chi_block_21(q0, intra_order="grouped"))
        + abs(d_nuc11_int["chi_111"] - chi_block_111(q0))
    )

    return {
        "character_table": character_table,
        "grid_cells": grid_cells,
        "exact_identity_residuals": {
            "delta_S_chi111_plus_chi3": fmt(id_delta_s_anti),
            "delta_S_chi21_zero": fmt(id_delta_s_21),
            "nuc9_chi111_minus_chi3": fmt(id_nuc9_eq),
            "nuc11_interleaved_chi111_minus_q_inv4_chi3": fmt(id_nuc11_int_q4),
            "nuc11_gen_grouped_chi111_minus_q_inv4_chi3": fmt(id_nuc11_grp_q4),
            "nuc11_extremal_characters_ordering_invariant": fmt(id_nuc11_same_extremal),
            "nuc11_all_blocks_match_qbeta_utils_closed_forms": fmt(id_nuc11_closed_form),
        },
    }


def evaluate_lever_a_cosh_holonomy(
    q0: mp.mpf,
    h0: mp.mpf,
    u0: mp.mpf,
    z_d: mp.mpf,
    e0_map: dict[str, mp.mpf],
    census: dict[str, dict[str, object]],
    gpmt_info: dict[str, mp.mpf],
    qed_info: dict[str, mp.mpf],
    q_codata: mp.mpf,
    mn_codata: mp.mpf,
    mp_codata: mp.mpf,
    me_codata: mp.mpf,
) -> dict[str, object]:
    """Evaluate Lever A: Parameter-free Kohno-Drinfeld hyperbolic cosh(k*ln q) holonomy factors on z_D."""
    w3_zD = gpmt_info["w3_zD"]
    w21_zD = gpmt_info["w21_zD"]
    dpn_codata = mn_codata - mp_codata
    delta_m_qed = qed_info["delta_m_qed_two_term_mev"]

    # Convention-D elliptic N=1 and N=2 rungs via canonical substrate_ladder_quantities(q0, convention="D"):
    lad_d = substrate_ladder_quantities(q0, convention="D")
    u_ladder = lad_d["u"]
    alpha_D = lad_d["alpha"]
    theta_D = alpha_D - u_ladder / mp.mpf(2)
    rung_N1_cos_D = mp.cos(theta_D)
    rung_N2_factor = mp.mpf(1) - u_ladder**2
    rung_N1_N2_D = rung_N1_cos_D * rung_N2_factor

    kd_definitions = [
        (0, "bare_zD", "No hyperbolic framing factor (1)"),
        (1, "KD_k1_single_wrap", "1-crossing Kohno-Drinfeld hyperbolic character (q + q^{-1})/2 = cosh(ln q)"),
        (2, "KD_k2_double_wrap", "2-crossing Kohno-Drinfeld hyperbolic character (q^2 + q^{-2})/2 = cosh(2 ln q)"),
        (3, "KD_k3_half_twist", "3-crossing half-twist Delta_3 hyperbolic character (q^3 + q^{-3})/2 = cosh(3 ln q)"),
        (
            6,
            "KD_k6_full_twist_framing",
            "6-crossing full-twist framing Delta_3^2 = (sigma_0*sigma_1*sigma_0)^2 character (q^6 + q^{-6})/2 = cosh(6 ln q)",
        ),
    ]

    kd_factors: dict[str, object] = {}
    for k, label, desc in kd_definitions:
        val_rat = (q0**k + q0 ** (-k)) / mp.mpf(2) if k > 0 else mp.mpf(1)
        val_cosh = mp.cosh(mp.mpf(k) * u0)
        diff_from_one = ((q0**k - mp.mpf(1)) ** 2) / (mp.mpf(2) * (q0**k)) if k > 0 else mp.mpf(0)
        kd_factors[label] = {
            "k": k,
            "description": desc,
            "C_KD_k": fmt(val_rat),
            "cosh_k_u0_minus_rational_residual": fmt(abs(val_cosh - val_rat)),
            "excess_over_one_identity_residual": fmt(abs((val_rat - mp.mpf(1)) - diff_from_one)),
        }

    decomp_int = wedderburn_characters_from_census_vec(census["nuc11_interleaved"]["vector"], q0)
    tr_zD_int = w3_zD * decomp_int["chi_3"] + w21_zD * decomp_int["chi_21"]

    live_cell_kd_table: dict[str, object] = {}
    for e0_key, e0_val in e0_map.items():
        q_base = -e0_val * tr_zD_int
        for k, label, _desc in kd_definitions:
            c_kd = (q0**k + q0 ** (-k)) / mp.mpf(2) if k > 0 else mp.mpf(1)
            q_kd = q_base * c_kd
            q_kd_n1 = q_kd * rung_N1_cos_D
            q_kd_n2 = q_kd * rung_N1_N2_D
            q_kd_n2_qed = q_kd_n2 + delta_m_qed

            f_rem_kd = q_codata / q_kd
            in_cos_reach = bool(mp.mpf(0) < f_rem_kd <= mp.mpf(1))
            theta_eff = mp.acos(f_rem_kd) if in_cos_reach else mp.mpf(0)
            c_min_kd = solve_c_min_uniform(u_ladder, f_rem_kd, k_max=20)

            mn_final = mp_codata + me_codata + q_kd_n2_qed
            mn_final_ppm = (mn_final - mn_codata) / mn_codata * mp.mpf("1e6")
            dpn_final = me_codata + q_kd_n2_qed
            dpn_final_ppm = (dpn_final - dpn_codata) / dpn_codata * mp.mpf("1e6")

            row_key = f"nuc11_interleaved__{e0_key}__{label}"
            live_cell_kd_table[row_key] = {
                "e0_variant": e0_key,
                "kd_variant": label,
                "k": k,
                "C_KD_k": fmt(c_kd),
                "Q_KD_base_MeV": fmt(q_kd),
                "Q_KD_base_pct_err": fmt((q_kd - q_codata) / q_codata * 100),
                "F_rem_after_KD": fmt(f_rem_kd),
                "in_elliptic_cosine_reach": in_cos_reach,
                "theta_eff_rad_if_reachable": fmt(theta_eff),
                "theta_eff_over_u0_if_reachable": fmt(theta_eff / u0),
                "C_min_K20_after_KD": fmt(c_min_kd),
                "Q_KD_N1_MeV": fmt(q_kd_n1),
                "Q_KD_N1_pct_err": fmt((q_kd_n1 - q_codata) / q_codata * 100),
                "Q_KD_N2_MeV": fmt(q_kd_n2),
                "Q_KD_N2_pct_err": fmt((q_kd_n2 - q_codata) / q_codata * 100),
                "Q_KD_N2_plus_QED_MeV": fmt(q_kd_n2_qed),
                "Q_KD_N2_plus_QED_pct_err": fmt((q_kd_n2_qed - q_codata) / q_codata * 100),
                "Q_KD_N2_plus_QED_ppm_err": fmt((q_kd_n2_qed - q_codata) / q_codata * mp.mpf("1e6")),
                "Q_KD_N2_plus_QED_eV_err": fmt((q_kd_n2_qed - q_codata) * mp.mpf("1e6")),
                "m_n_final_MeV": fmt(mn_final),
                "m_n_final_ppm_err": fmt(mn_final_ppm),
                "Delta_pn_final_MeV": fmt(dpn_final),
                "Delta_pn_final_ppm_err": fmt(dpn_final_ppm),
            }

    return {
        "convention_d_ladder_parameters": {
            "z_D": fmt(z_d),
            "alpha_D": fmt(alpha_D),
            "theta_D_minus_u0_over_2": fmt(theta_D),
            "rung_N1_cos_alphaD_minus_u0_over_2": fmt(rung_N1_cos_D),
            "rung_N2_one_minus_u0_sq": fmt(rung_N2_factor),
            "product_N1_N2_D": fmt(rung_N1_N2_D),
            "delta_m_QED_conn_two_term_MeV": fmt(delta_m_qed),
        },
        "kd_hyperbolic_factors": kd_factors,
        "live_cell_kd_table": live_cell_kd_table,
    }


def main() -> int:
    q0 = mp.mpf(Q_50_DIGIT_STR)
    h0 = q0 - mp.mpf(1) / q0
    u0 = mp.log(q0)
    z_d = (q0**3) / (q0**2 + mp.mpf(1))

    q_codata = mp.mpf(str(Q_BETA_MEV_AME))
    mn_codata = mp.mpf(str(M_N_MEV_AME_DERIVED))
    mp_codata = mp.mpf(str(M_P_MEV))
    me_codata = mp.mpf(str(M_E_MEV))

    e0_map = {
        "tower_summed": qbeta_e0.tower_summed(q0, me_codata),
        "order_zero": qbeta_e0.order_zero(q0, me_codata),
    }

    census = build_census_vectors()
    gpmt_info = convention_d_weights_mpf(q0)
    qed_info = compute_two_term_borromean_qed_mev(q0, me_codata)

    lad_d = substrate_ladder_quantities(q0, convention="D")
    u_ladder = lad_d["u"]

    lever_b = evaluate_lever_b_gpmt(
        q0, u_ladder, e0_map, census, gpmt_info, q_codata, mn_codata, mp_codata, me_codata
    )
    lever_a = evaluate_lever_a_cosh_holonomy(
        q0, h0, u0, z_d, e0_map, census, gpmt_info, qed_info, q_codata, mn_codata, mp_codata, me_codata
    )

    print("=" * 96)
    print("Q_BETA PDIX -> CDS1 BRIDGE PROBE: LEVER A (KD COSH FRAMING) & LEVER B (GPMT (1^3) TRACE)")
    print("=" * 96)
    print(f"Proton pin q_0            = {mp.nstr(q0, 35)}")
    print(f"Hecke h_0 = q_0 - q_0^-1  = {mp.nstr(h0, 35)}")
    print(f"u_0 = ln(q_0)             = {mp.nstr(u0, 35)}")
    print(f"Convention D z_D          = {mp.nstr(z_d, 35)}")
    print(f"w_(3)(z_D)                = {mp.nstr(gpmt_info['w3_zD'], 30)}")
    print(f"w_(2,1)(z_D)              = {mp.nstr(gpmt_info['w21_zD'], 30)}")
    print(f"w_(1^3)(z_D)              = {mp.nstr(gpmt_info['w111_zD'], 30)}")
    print(f"GPMT d_D(S^(1^3))         = {mp.nstr(gpmt_info['d_mod_111'], 30)}")
    print(f"GPMT |d_D(S^(1^3))|       = {mp.nstr(gpmt_info['d_mod_111_abs'], 30)}")
    print(f"E_0 (tower_summed)        = {mp.nstr(e0_map['tower_summed'], 25)} MeV")
    print(f"E_0 (order_zero)          = {mp.nstr(e0_map['order_zero'], 25)} MeV")
    print(f"Q_beta (CODATA/AME)       = {mp.nstr(q_codata, 20)} MeV")
    print(f"Delta_m_QED^conn (2-term) = {mp.nstr(qed_info['delta_m_qed_two_term_mev'], 20)} MeV")

    print("\n" + "-" * 96)
    print("PART 1 (LEVER B): WEDDERBURN CHARACTERS & GPMT (1^3) COMPLETION ACROSS CENSUS CANDIDATES")
    print("-" * 96)
    for cand_key, c_row in lever_b["character_table"].items():
        c3_s = mp.nstr(mp.mpf(c_row["chi_3"]), 10)
        c21_s = mp.nstr(mp.mpf(c_row["chi_21"]), 10)
        c111_s = mp.nstr(mp.mpf(c_row["chi_111"]), 10)
        print(
            f"  {cand_key:18s} (L={c_row['crossing_length']:2d}): "
            f"chi_3={c3_s:14s}  chi_21={c21_s:14s}  "
            f"chi_111={c111_s:14s}  same_sign(3,111)={c_row['chi3_chi111_same_sign']}"
        )

    print("\n  Lever B 50-dps Summary Table (tower_summed E_0):")
    print(
        f"  {'Candidate':18s} | {'Trace Variant':15s} | {'Q_beta (MeV)':15s} | {'Q_beta err':10s} | "
        f"{'m_n err (ppm)':13s} | {'F_rem':12s} | {'C_min(20)':10s} | {'cos reach'}"
    )
    for cand_key in ["delta_S", "nuc9", "nuc11_interleaved", "nuc11_gen_grouped"]:
        for tr_label in ["zD_bare", "zD_GPMT_pos", "zD_GPMT_signed"]:
            cell = lever_b["grid_cells"][f"{cand_key}__tower_summed__{tr_label}"]
            print(
                f"  {cand_key:18s} | {tr_label:15s} | {cell['Q_beta_MeV'][:15]:15s} | "
                f"{cell['Q_beta_pct_err'][:8]:>8s}% | {cell['m_n_ppm_err'][:11]:>11s} | "
                f"{cell['F_rem_to_CODATA'][:12]:12s} | {cell['C_min_K20'][:10]:10s} | "
                f"{str(cell['in_elliptic_cosine_reach']):5s}"
            )

    print("\n" + "-" * 96)
    print("PART 2 (LEVER A): KOHNO-DRINFELD HYPERBOLIC COSH(k*ln q) FRAMING ON LIVE CELL (nuc11_interleaved)")
    print("-" * 96)
    print(
        f"  {'E_0 form':12s} | {'KD Framing Variant':26s} | {'C_KD^(k)':12s} | "
        f"{'Q_KD base':12s} | {'F_rem':10s} | {'Q_KD+N2+QED':12s} | {'Q_beta err':10s} | {'m_n ppm'}"
    )
    for e0_key in ["tower_summed", "order_zero"]:
        for label in [
            "bare_zD",
            "KD_k1_single_wrap",
            "KD_k2_double_wrap",
            "KD_k3_half_twist",
            "KD_k6_full_twist_framing",
        ]:
            row = lever_a["live_cell_kd_table"][f"nuc11_interleaved__{e0_key}__{label}"]
            print(
                f"  {e0_key:12s} | {label:26s} | {row['C_KD_k'][:12]:12s} | "
                f"{row['Q_KD_base_MeV'][:12]:12s} | {row['F_rem_after_KD'][:10]:10s} | "
                f"{row['Q_KD_N2_plus_QED_MeV'][:12]:12s} | {row['Q_KD_N2_plus_QED_pct_err'][:8]:>8s}% | "
                f"{row['m_n_final_ppm_err'][:9]:>9s}"
            )

    # Verification checks
    res_ids = lever_b["exact_identity_residuals"]
    cell_int_gpmt = lever_b["grid_cells"]["nuc11_interleaved__tower_summed__zD_GPMT_pos"]
    cell_grp_gpmt = lever_b["grid_cells"]["nuc11_gen_grouped__tower_summed__zD_GPMT_pos"]
    kd6_live = lever_a["live_cell_kd_table"]["nuc11_interleaved__tower_summed__KD_k6_full_twist_framing"]

    checks = [
        (
            "gpmt_d_mod_111_rational_identity",
            bool(gpmt_info["d_mod_111_rational_residual"] < mp.mpf("1e-50")),
            f"d_D(S^(1^3)) = -1/([2]_q[3]_q) = -q^3/((q^2+1)(q^4+q^2+1)) residual = {fmt(gpmt_info['d_mod_111_rational_residual'])}",
        ),
        (
            "nuc11_chi111_equals_q_inv4_chi3",
            bool(
                mp.mpf(res_ids["nuc11_interleaved_chi111_minus_q_inv4_chi3"]) < mp.mpf("1e-50")
                and mp.mpf(res_ids["nuc11_gen_grouped_chi111_minus_q_inv4_chi3"]) < mp.mpf("1e-50")
            ),
            "chi_{(1^3)}(Delta_nuc11) = q^{-4} * chi_{(3)}(Delta_nuc11) < 0 on both 11-letter words",
        ),
        (
            "nuc11_blocks_match_qbeta_utils_closed_forms",
            bool(mp.mpf(res_ids["nuc11_all_blocks_match_qbeta_utils_closed_forms"]) < mp.mpf("1e-50")),
            "chi_{(3)}, chi_{(2,1)}, chi_{(1^3)} on census vectors match qbeta_utils closed forms to 50+ dps",
        ),
        (
            "delta_s_chi111_equals_neg_chi3",
            bool(
                mp.mpf(res_ids["delta_S_chi111_plus_chi3"]) < mp.mpf("1e-50")
                and mp.mpf(res_ids["delta_S_chi21_zero"]) < mp.mpf("1e-50")
            ),
            "chi_{(1^3)}(Delta_S) = -chi_{(3)}(Delta_S) > 0 and chi_{(2,1)}(Delta_S) = 0",
        ),
        (
            "lever_b_gpmt_pos_brackets_codata_on_11_crossing_words",
            bool(
                mp.mpf(cell_int_gpmt["Q_beta_MeV"]) < q_codata < mp.mpf(cell_grp_gpmt["Q_beta_MeV"])
                and bool(cell_grp_gpmt["in_elliptic_cosine_reach"])
            ),
            (
                f"GPMT+ moves nuc11_interleaved to {cell_int_gpmt['Q_beta_MeV'][:10]} MeV "
                f"({cell_int_gpmt['Q_beta_pct_err'][:7]}%) and nuc11_gen_grouped to "
                f"{cell_grp_gpmt['Q_beta_MeV'][:10]} MeV (+{cell_grp_gpmt['Q_beta_pct_err'][:6]}%), "
                "bracketing CODATA and restoring F_rem < 1 on nuc11_gen_grouped"
            ),
        ),
        (
            "lever_a_kd6_full_twist_restores_elliptic_cosine_reach_on_live_cell",
            bool(
                bool(kd6_live["in_elliptic_cosine_reach"])
                and abs(mp.mpf(kd6_live["Q_KD_N2_plus_QED_pct_err"])) < mp.mpf("0.05")
            ),
            (
                f"6-crossing full-twist KD character (q^6+q^-6)/2 = {kd6_live['C_KD_k'][:12]} moves live cell base "
                f"to {kd6_live['Q_KD_base_MeV'][:10]} MeV (+{kd6_live['Q_KD_base_pct_err'][:6]}%), "
                f"restoring F_rem = {kd6_live['F_rem_after_KD'][:10]} < 1; "
                f"with N=1, N=2 & 2-term Borromean QED gives Q_beta = {kd6_live['Q_KD_N2_plus_QED_MeV'][:10]} MeV "
                f"({kd6_live['Q_KD_N2_plus_QED_pct_err'][:7]}%, m_n residual {kd6_live['m_n_final_ppm_err'][:6]} ppm)"
            ),
        ),
    ]

    print("\n" + "-" * 96)
    print("VERIFICATION CHECKS")
    print("-" * 96)
    for name, passed, detail in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name} — {detail}")
    assert all(p for _, p, _ in checks), "One or more verification checks failed!"

    w = WitnessBuilder("qbeta-pdix-cds1-cosh-gpmt-bridge")
    w.set_description(
        "50-dps evaluation of the two active candidate mechanisms bridging the "
        "Convention D Q_beta ladder & base gap (qou-pdix -> qou-cds1): "
        "Lever A (Kohno-Drinfeld hyperbolic cosh(k*ln q) holonomy & 6-crossing "
        "full-twist framing (q^6+q^{-6})/2 on the ruled z_D base) and "
        "Lever B (GPMT (1^3) modified-trace completion of tr_M^{z_D} where w_{(1^3)}(z_D) = 0)."
    )
    w.add_data("q0_anchor", "proton")
    w.add_data("q0_value", Q_50_DIGIT_STR)
    w.add_data(
        "parameters",
        {
            "dps": 60,
            "q0": fmt(q0),
            "h0": fmt(h0),
            "u0": fmt(u0),
            "z_D": fmt(z_d),
            "w3_zD": fmt(gpmt_info["w3_zD"]),
            "w21_zD": fmt(gpmt_info["w21_zD"]),
            "w111_zD": fmt(gpmt_info["w111_zD"]),
            "d_mod_111": fmt(gpmt_info["d_mod_111"]),
            "d_mod_111_abs": fmt(gpmt_info["d_mod_111_abs"]),
            "E0_tower_summed_MeV": fmt(e0_map["tower_summed"]),
            "E0_order_zero_MeV": fmt(e0_map["order_zero"]),
            "Q_beta_CODATA_MeV": fmt(q_codata),
            "m_n_CODATA_MeV": fmt(mn_codata),
            "m_p_CODATA_MeV": fmt(mp_codata),
            "m_e_CODATA_MeV": fmt(me_codata),
            "delta_m_QED_conn_two_term_MeV": fmt(qed_info["delta_m_qed_two_term_mev"]),
        },
    )
    w.add_data("lever_b_gpmt_modified_trace", lever_b)
    w.add_data("lever_a_kd_cosh_holonomy", lever_a)
    w.add_caveat(
        "Scope-(a) diagnostic and bridge probe for qou-pdix -> qou-cds1. All evaluated "
        "expressions are parameter-free functions of q_0 at the proton pin (zero fitted "
        "parameters, zero float64)."
    )
    for name, passed, detail in checks:
        w.add_assertion(name, "1" if passed else "0", "1", "0", source=detail)

    try:
        from qou_substrate.witness import WitnessBuilder as WB2

        WB2.stamp_staleness_metadata(
            w,
            script_path=__file__,
            engine="python+sympy+mpmath",
            q0_anchor="proton",
            q0_value=Q_50_DIGIT_STR,
        )
    except Exception:
        pass

    out_path = w.save()
    print(f"\nWrote witness -> {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
