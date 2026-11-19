#!/usr/bin/env python3
"""
qbeta-wedderburn-phase-twoterm-pin-probe — 80-dps parameter-free investigation of:

  1. Bean qou-q2oa (Convention-D Ladder Phase alpha(q) from True Wedderburn Weights):
     - Exact discrepancy between the retracted non-Markov coefficient
       kappa(z_D) = 1/2 - z_D = -(2*q^3 - q^2 - 1)/(2*(q^2 + 1)) = -0.11268803715 < 0
       and the true Convention-D middle Wedderburn weight
       w_{(2,1)}(z_D) = q^2 / (q^2 + 1)^2 = +0.24729788675 > 0,
       with exact positive gap:
       w_{(2,1)}(z_D) - (1/2 - z_D) = (2*q^5 - q^4 + 2*q^3 - 1) / (2*(q^2 + 1)^2)
                                    = +0.35998592389 > 0.
     - Systematic 80-dps evaluation of all 8 natural parameter-free Wedderburn /
       Jucys-Murphy content / Markov-trace / mirror-covariant loop-mean phase
       functionals alpha_Wed(q) built from the true Convention-D weights
       (w_{(3)}(z_D), w_{(2,1)}(z_D), w_{(1^3)}(z_D) = 0) and GPMT-completed weights
       (w_{(3)}(z_D), w_{(2,1)}(z_D), |d_D(S^{(1^3)})| = 1/([2]_q[3]_q)).
     - Key structural result on the KD6 * z_D base (`nuc11_interleaved`, tower E_0):
       Replacing the unprojected D-frame phase alpha_D = (z_D - 1)*h/2 = -0.04048578
       (which retains the bar-even mirror-covariance anomaly +h^2/4 and leaves
       Q_beta at +407.06 ppm / m_n at +338.94 ppb after connected Borromean QED)
       with the unique mirror-covariant bar-odd projected D-frame phase
       alpha_D^{proj} = alpha_D - h^2/4 = (h/4)*([2]_q * w_{(3)}(z_D) - 2) = -0.05141233
       (proved in LadderPhaseMirrorCovariance.lean §3-§4) moves Q_beta to
       -142.31 ppm (m_n to -118.49 ppb), cutting the residual nearly 3x and
       bracketing CODATA between the unprojected and mirror-projected phases.

  2. Consistent Two-Term Substrate Pin q_{2t} Propagation into BOTH m_p, m_n, and Q_beta:
     - Compares 4 substrate pins at 80 dps:
         (a) q_{1t}: 1-term proton pin m_p^{QCD}(q_{1t}) = m_p^{CODATA}
         (b) q_{2t,plain}: 2-term proton pin m_p^{QCD}(q) + M_p^{QED,conn,plain}(q) = m_p^{CODATA}
             (Delta q / q_{1t} = +11.123 ppb; collapses mu-p tension from 211.2 ppb to +8.06 ppb = +0.36 sigma)
         (c) q_{2t,Kp}: Cartan-weighted 2-term proton pin m_p^{QCD}(q) + q * M_p^{QED,conn,plain}(q) = m_p^{CODATA}
             (Delta q / q_{1t} = +12.347 ppb; collapses mu-p tension to -4.17 ppb = -0.19 sigma)
         (d) q_{mu}: muon-anchored substrate pin m_mu(q_{mu}) = m_mu^{CODATA}
     - Quantifies the logarithmic sensitivity hierarchy:
         S_{m_p} = d ln m_p^{QCD} / d ln q = -20.9970 (-220.08 eV for +11.123 ppb shift in q)
         vs S_{Q_A} = -2.5968 (-0.0226 eV shift) and S_{Q_{KD6}} = +3.5999 (+0.0314 eV shift).
     - Evaluates all 4 parameter-free Cartan QED weightings ('plain', 'KnKp', 'Kp3', 'q')
       from NucleonWeightSpaceTwoTerm.lean across 4 bases:
         * Q_A (Form-A 2-strand closed form)
         * Q_KD6_nuc11_interleaved (6-crossing full-twist cosh(6 ln q) * z_D on nuc11_interleaved)
         * Q_GPMT_pos_nuc11_interleaved (GPMT+ positive (1^3) modified-trace completion on nuc11_interleaved)
         * Q_GPMT_pos_nuc11_gen_grouped (GPMT+ positive (1^3) modified-trace completion on nuc11_gen_grouped)

  3. Exact eV / ppb Budget of m_n and Q_beta & 11-Letter Word Ordering Bracket (qou-j1e5):
     - Full additive breakdown of why m_n (2-strand Form-A + 2tQED) sits at +148.56 ppb ('plain')
       to +109.74 ppb ('q'), and why inconsistent 1-term proton core evaluation at q_{2t}
       (omitting M_p^{QED,conn} = +220.08 eV from m_p) shifts m_n by -234.23 ppb to -85.67 ppb.

Rule compliance:
  - 80-dps internal mpmath arithmetic (`set_compute_dps(80)` at module scope).
  - Zero `float()` conversions anywhere in this script.
  - Zero fitted parameters.

Tracking beans: qou-q2oa, qou-cds1, qou-j1e5
Lean companion: folio/quantum-observable-universe/lean/QOU/QBeta/WedderburnPhaseAndTwoTermPinBridge.lean
"""

from __future__ import annotations

import os
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

from _precision import set_compute_dps  # noqa: E402
from codata_2022_source import (  # noqa: E402
    M_E_MEV,
    M_MU_MEV,
    M_N_MEV_AME_DERIVED,
    M_P_MEV,
    Q_BETA_MEV_AME,
)
from q_parameter import (  # noqa: E402
    Q_50_DIGIT_STR,
    q_muon_at,
    q_two_term_borromean_at,
    tr_conn_borromean_diff_at,
    tr_conn_borromean_n_at,
    tr_conn_borromean_p_at,
    vol_4_1_at,
)
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(80)
mp.mp.dps = 80

_VOL_4_1_80 = vol_4_1_at(85)
_M_E_MPF = mp.mpf(str(M_E_MEV))
_M_MU_MPF = mp.mpf(str(M_MU_MEV))


def fmt(val: mp.mpf, digits: int = 50) -> str:
    """Format an mpmath mpf at 50 significant digits with zero float64."""
    return mp.nstr(val, digits)


def muon_mass_mev(q: mp.mpf) -> mp.mpf:
    """Substrate muon mass formula m_mu(q) = m_e * Vol(4_1) / hbar_q^2 at 80 dps."""
    hbar_q_sq = ((q - mp.mpf(1)) / q) ** 2
    return _M_E_MPF * _VOL_4_1_80 / hbar_q_sq


def m_p_qcd_bare_mev(q: mp.mpf) -> mp.mpf:
    """Substrate bare strong-core proton mass m_p^{QCD}(q) = 2 * m_mu(q) * F_Bor(q) - 12 * m_e at 80 dps."""
    one = mp.mpf(1)
    three = mp.mpf(3)
    four = mp.mpf(4)
    h = q - one / q
    tr_m_bor = abs((four + h**2 - three * (h**4) - h**6) / (h**2 + four))
    qfact3 = (q**2 + one + one / (q**2)) * (q + one / q)
    f_bor = tr_m_bor * qfact3 / (q**3)
    return mp.mpf(2) * muon_mass_mev(q) * f_bor - mp.mpf(12) * _M_E_MPF


def e0_hadronic_mev(q: mp.mpf) -> mp.mpf:
    """Canonical tower-summed hadronic energy scale E_0(q) = m_e / (q * (q - 1)) / (1 - hbar_q^2) at 80 dps."""
    one = mp.mpf(1)
    hbar_q = (q - one) / q
    return _M_E_MPF / (q * (q - one)) / (one - hbar_q**2)


def borromean_v3_proton_self_shift_mev(q: mp.mpf, cartan_weight: bool = False) -> mp.mpf:
    """Connected 4th-order Borromean V^3 proton QED self-energy shift M_p^{QED,conn}(q) > 0 at 80 dps."""
    tr_p = abs(tr_conn_borromean_p_at(q, dps=80))
    w = q if cartan_weight else mp.mpf(1)
    return _M_E_MPF * w * tr_p


def borromean_v3_connected_qed_splitting(
    q: mp.mpf, cartan_weight: str = "plain"
) -> dict[str, mp.mpf]:
    """Connected 4th-order Borromean V^3 (n - p) QED splitting across the 4 parameter-free Cartan weightings."""
    tr_p = tr_conn_borromean_p_at(q, dps=80)
    tr_n = tr_conn_borromean_n_at(q, dps=80)
    tr_diff_plain = tr_conn_borromean_diff_at(q, dps=80)
    if cartan_weight == "plain":
        tr_diff = tr_diff_plain
    elif cartan_weight == "KnKp":
        tr_diff = tr_n / q - q * tr_p
    elif cartan_weight == "Kp3":
        tr_diff = tr_n - q * tr_p
    elif cartan_weight == "q":
        tr_diff = q * tr_diff_plain
    else:
        raise ValueError(f"Unknown cartan_weight: {cartan_weight}")
    return {
        "tr_conn_p": tr_p,
        "tr_conn_n": tr_n,
        "tr_conn_diff": tr_diff,
        "delta_m_qed_mev": -_M_E_MPF * tr_diff,
    }


def solve_muon_pin_80dps(q_seed: mp.mpf) -> mp.mpf:
    """Solve m_mu(q_mu) = m_mu^{CODATA} at 80 dps."""
    return q_muon_at(80)


def solve_one_term_proton_pin_80dps(q_seed: mp.mpf) -> mp.mpf:
    """Refine 1-term proton pin m_p^{QCD}(q_{1t}) = m_p^{CODATA} to 80 dps."""
    mp_exp = mp.mpf(str(M_P_MEV))
    q_a = q_seed
    q_b = q_seed * (mp.mpf(1) + mp.mpf("1e-12"))
    for _ in range(25):
        f_a = m_p_qcd_bare_mev(q_a) - mp_exp
        f_b = m_p_qcd_bare_mev(q_b) - mp_exp
        diff = f_b - f_a
        if abs(diff) < mp.mpf("1e-75"):
            break
        q_next = q_b - f_b * (q_b - q_a) / diff
        q_a, q_b = q_b, q_next
        if abs(q_b - q_a) < mp.mpf("1e-70"):
            break
    return q_b


def wedderburn_weights_and_phases_at_q(q: mp.mpf) -> dict[str, mp.mpf]:
    """Compute exact Convention-D & GPMT+ Wedderburn weights, moments, and 8 parameter-free phases at q."""
    one = mp.mpf(1)
    two = mp.mpf(2)
    three = mp.mpf(3)
    four = mp.mpf(4)

    h = q - one / q
    two_q = q + one / q
    three_q = q**2 + one + one / (q**2)
    hbar_q = (q - one) / q
    b_val = mp.sqrt((h**2 + three) / (h**2 + four))
    u_ladder = b_val * (hbar_q**2)

    z_d = q**3 / (q**2 + one)
    z_d_bar = z_d - h  # bar(z_D) = z_D(q^{-1}) = 1/(q*(q^2+1)) = z_D - h
    z_d_loop_mean = (z_d + z_d_bar) / two  # (2*z_D - h)/2 = [2]_q * Xi_D / 2

    # True Convention-D Wedderburn weights
    w3 = (q**4 + one) / ((q**2 + one) ** 2)
    w21 = (q**2) / ((q**2 + one) ** 2)
    w111 = mp.mpf(0)
    weight_sum = w3 + two * w21 + w111  # identically 1

    # Retracted non-Markov middle coefficient kappa(z_D) = 1/2 - z_D
    kappa_retracted = one / two - z_d
    w21_minus_kappa = w21 - kappa_retracted
    w21_minus_kappa_closed = (two * q**5 - q**4 + two * q**3 - one) / (
        two * ((q**2 + one) ** 2)
    )

    # GPMT modified quantum dimension on killed (1^3) sector
    d_mod_111 = -one / (two_q * three_q)
    d_mod_111_abs = one / (two_q * three_q)

    # Transposition & Jucys-Murphy content moments
    # On H_3(q), normalized content eigenvalues c_bar_lambda = (1/3) sum_{x in lambda} c(x)
    # are (+1, 0, -1) on ((3), (2,1), (1^3)), identical to transposition characters chi^lambda(tau)/f^lambda.
    xi_d = w3 - w111  # = w3 = 1 - 2*w21
    jm_content_total_d = three * w3 + mp.mpf(0) * (two * w21) - three * w111
    jm_content_mean_d = jm_content_total_d / three  # = w3 = xi_d

    xi_gpmt_pos = w3 - d_mod_111_abs
    xi_gpmt_pos_closed = (
        q**8 + q**6 - q**5 + two * q**4 - q**3 + q**2 + one
    ) / (((q**2 + one) ** 2) * (q**4 + q**2 + one))

    # Loop-mean identity residual: (2*z_D - h) - [2]_q * Xi_D
    loop_mean_residual = abs((two * z_d - h) - two_q * xi_d)

    # 8 natural parameter-free phase functionals alpha(q)
    # 1. Asserted unprojected D-frame phase: alpha_D = (z_D - 1)*h/2 = (h/4)*([2]_q*Xi_D + h - 2)
    alpha_d_asserted = (z_d - one) * h / two
    # 2. Mirror-covariant bar-odd projected D-frame phase (LadderPhaseMirrorCovariance.lean §3-§4):
    #    alpha_D^{proj} = alpha_D - h^2/4 = ((z_D + bar(z_D))/2 - 1)*h/2 = (h/4)*([2]_q*Xi_D - 2)
    alpha_d_mirror_proj = alpha_d_asserted - (h**2) / four
    alpha_d_mirror_proj_w3_form = (h / four) * (two_q * w3 - two)
    # 3. Normalized Jucys-Murphy content-mean phase: -(h/2) * <c_bar>_D = -(h/2) * w_{(3)}(z_D)
    alpha_jm_content_mean = -(h / two) * jm_content_mean_d
    # 4. GPMT+ transposition/content-moment loop-mean phase (unprojected)
    alpha_gpmt_pos_moment = (h / four) * (two_q * xi_gpmt_pos + h - two)
    # 5. GPMT+ mirror-covariant bar-odd projected phase
    alpha_gpmt_pos_mirror_proj = (h / four) * (two_q * xi_gpmt_pos - two)
    # 6. Direct substitution of true w_{(2,1)}(z_D) into retracted affine formula -h/4 - (h/2)*y
    alpha_wed_real_w21_affine = -h / four - (h / two) * w21
    # 7. Quantum-dimension-scaled [2]_q * w_{(2,1)}(z_D) = 1/[2]_q affine phase
    alpha_wed_2q_w21 = -h / four - (h / two) * (two_q * w21)
    # 8. Pure middle-sector weight phase -(h/2) * w_{(2,1)}(z_D)
    alpha_w21_direct = -(h / two) * w21

    return {
        "q": q,
        "h": h,
        "two_q": two_q,
        "three_q": three_q,
        "hbar_q": hbar_q,
        "b": b_val,
        "u_ladder": u_ladder,
        "z_D": z_d,
        "z_D_bar": z_d_bar,
        "z_D_loop_mean": z_d_loop_mean,
        "w3_zD": w3,
        "w21_zD": w21,
        "w111_zD": w111,
        "weight_sum": weight_sum,
        "kappa_retracted": kappa_retracted,
        "w21_minus_kappa": w21_minus_kappa,
        "w21_minus_kappa_closed_residual": abs(w21_minus_kappa - w21_minus_kappa_closed),
        "d_mod_111": d_mod_111,
        "d_mod_111_abs": d_mod_111_abs,
        "Xi_D": xi_d,
        "jm_content_total_D": jm_content_total_d,
        "jm_content_mean_D": jm_content_mean_d,
        "Xi_GPMT_pos": xi_gpmt_pos,
        "Xi_GPMT_pos_closed_residual": abs(xi_gpmt_pos - xi_gpmt_pos_closed),
        "loop_mean_residual": loop_mean_residual,
        "mirror_proj_w3_form_residual": abs(
            alpha_d_mirror_proj - alpha_d_mirror_proj_w3_form
        ),
        "phases": {
            "alpha_D_asserted": alpha_d_asserted,
            "alpha_D_mirror_proj": alpha_d_mirror_proj,
            "alpha_JM_content_mean": alpha_jm_content_mean,
            "alpha_GPMT_pos_moment": alpha_gpmt_pos_moment,
            "alpha_GPMT_pos_mirror_proj": alpha_gpmt_pos_mirror_proj,
            "alpha_Wed_real_w21_affine": alpha_wed_real_w21_affine,
            "alpha_Wed_2q_w21": alpha_wed_2q_w21,
            "alpha_w21_direct": alpha_w21_direct,
        },
    }


def bases_at_q(q: mp.mpf, me_mev: mp.mpf) -> dict[str, mp.mpf]:
    """Compute the 4 parameter-free Convention-D Q_beta base energies (MeV) at arbitrary q."""
    one = mp.mpf(1)
    two = mp.mpf(2)
    four = mp.mpf(4)

    # 1. Form-A 2-strand closed-form base Q_A(q) = m_e * |q^2 - 2*q - 1| * (q + 1) / (2 * q^3)
    q_a = me_mev * abs(q**2 - two * q - one) * (q + one) / (two * (q**3))

    # Tower-summed hadronic scale E_0(q) = m_e / (q*(q-1)) / (1 - hbar_q^2)
    e0_tower = e0_hadronic_mev(q)

    # Exact Wedderburn weights & GPMT modified quantum dimension at q
    w3 = (q**4 + one) / ((q**2 + one) ** 2)
    w21 = (q**2) / ((q**2 + one) ** 2)
    d_mod_111_abs = (q**3) / ((q**2 + one) * (q**4 + q**2 + one))

    # Exact Wedderburn characters on 11-crossing production nucleon words (n - p):
    # From CoshHolonomyAndGPMTBaseBridge.lean §1 (`chi3_nucleonDiffCoord`, `chi111_nucleonDiffCoord`)
    # and qbeta_utils (`chi_block_3`, `chi_block_21`, `chi_block_111`):
    chi3_nuc11 = -(q**2 - one) * ((q**2 + one) ** 2) / (four * q)
    chi111_nuc11 = -(q**2 - one) * ((q**2 + one) ** 2) / (four * (q**5))
    p_poly = (
        two * (q**12)
        - mp.mpf(5) * (q**10)
        + mp.mpf(5) * (q**8)
        - mp.mpf(5) * (q**6)
        + mp.mpf(5) * (q**4)
        - mp.mpf(5) * (q**2)
        + two
    )
    chi21_interleaved = (q**2 - one) * (q**4 + one) * p_poly / (four * (q**9))
    chi21_grouped = (q**2 - one) * (-(q**4) - one) / (four * (q**3))

    # Standard Convention-D Markov trace tr_M^{z_D}(Delta_nuc11_interleaved) (< 0 for q > 1)
    tr_z_d_interleaved = w3 * chi3_nuc11 + w21 * chi21_interleaved
    q_zd_bare_interleaved = e0_tower * (-tr_z_d_interleaved)

    # 2. Lever-A 6-crossing full-twist hyperbolic KD character C_KD^{(6)}(q) = (q^6 + q^{-6})/2
    c_kd6 = (q**6 + q ** (-6)) / two
    q_kd6_interleaved = q_zd_bare_interleaved * c_kd6

    # 3. Lever-B GPMT+ positive-weight trace completion on nuc11_interleaved
    tr_gpmt_pos_interleaved = tr_z_d_interleaved + d_mod_111_abs * chi111_nuc11
    q_gpmt_pos_interleaved = e0_tower * (-tr_gpmt_pos_interleaved)

    # 4. Lever-B GPMT+ positive-weight trace completion on nuc11_gen_grouped
    tr_z_d_grouped = w3 * chi3_nuc11 + w21 * chi21_grouped
    tr_gpmt_pos_grouped = tr_z_d_grouped + d_mod_111_abs * chi111_nuc11
    q_gpmt_pos_grouped = e0_tower * (-tr_gpmt_pos_grouped)

    return {
        "Q_A": q_a,
        "Q_zD_bare_nuc11_interleaved": q_zd_bare_interleaved,
        "Q_KD6_nuc11_interleaved": q_kd6_interleaved,
        "Q_GPMT_pos_nuc11_interleaved": q_gpmt_pos_interleaved,
        "Q_GPMT_pos_nuc11_gen_grouped": q_gpmt_pos_grouped,
        "C_KD6": c_kd6,
        "E0_tower_MeV": e0_tower,
    }


def main() -> int:
    q_codata = mp.mpf(str(Q_BETA_MEV_AME))
    mn_codata = mp.mpf(str(M_N_MEV_AME_DERIVED))
    mp_codata = mp.mpf(str(M_P_MEV))
    me_codata = mp.mpf(str(M_E_MEV))
    m_mu_codata = _M_MU_MPF

    # 4 substrate pins at 80 dps
    q_1t_seed = mp.mpf(Q_50_DIGIT_STR)
    q_1t = solve_one_term_proton_pin_80dps(q_1t_seed)
    q_2t_plain = q_two_term_borromean_at(dps=80, k_weighted=False)
    q_2t_kp = q_two_term_borromean_at(dps=80, k_weighted=True)
    q_muon = solve_muon_pin_80dps(q_1t)

    pins = {
        "q_1t": q_1t,
        "q_2t_plain": q_2t_plain,
        "q_2t_Kp": q_2t_kp,
        "q_muon": q_muon,
    }

    # Part 1: Wedderburn weights, moments, and 8 parameter-free phase functionals across pins
    part1_by_pin: dict[str, dict] = {}
    for pin_name, q_val in pins.items():
        info = wedderburn_weights_and_phases_at_q(q_val)
        part1_by_pin[pin_name] = {
            "q": fmt(q_val),
            "h": fmt(info["h"]),
            "u_ladder": fmt(info["u_ladder"]),
            "z_D": fmt(info["z_D"]),
            "z_D_bar": fmt(info["z_D_bar"]),
            "z_D_loop_mean": fmt(info["z_D_loop_mean"]),
            "w3_zD": fmt(info["w3_zD"]),
            "w21_zD": fmt(info["w21_zD"]),
            "w111_zD": fmt(info["w111_zD"]),
            "weight_sum": fmt(info["weight_sum"]),
            "kappa_retracted_half_minus_zD": fmt(info["kappa_retracted"]),
            "w21_minus_kappa_gap": fmt(info["w21_minus_kappa"]),
            "w21_minus_kappa_closed_residual": fmt(
                info["w21_minus_kappa_closed_residual"]
            ),
            "d_mod_111": fmt(info["d_mod_111"]),
            "d_mod_111_abs": fmt(info["d_mod_111_abs"]),
            "Xi_D_transposition_moment": fmt(info["Xi_D"]),
            "jm_content_total_D": fmt(info["jm_content_total_D"]),
            "jm_content_mean_D": fmt(info["jm_content_mean_D"]),
            "Xi_GPMT_pos": fmt(info["Xi_GPMT_pos"]),
            "Xi_GPMT_pos_closed_residual": fmt(info["Xi_GPMT_pos_closed_residual"]),
            "loop_mean_residual": fmt(info["loop_mean_residual"]),
            "mirror_proj_w3_form_residual": fmt(info["mirror_proj_w3_form_residual"]),
            "phases": {k: fmt(v) for k, v in info["phases"].items()},
        }

    # Part 2: Propagating q_{2t} into m_p, m_mu, Q_beta, and m_n across 4 bases, 8 phases, 4 QED weightings
    pin_summary: dict[str, dict] = {}
    phase_base_qed_grid: dict[str, dict] = {}

    for pin_name, q_val in pins.items():
        w_info = wedderburn_weights_and_phases_at_q(q_val)
        b_info = bases_at_q(q_val, me_codata)
        u_lad = w_info["u_ladder"]
        f2 = mp.mpf(1) - u_lad**2

        mp_qcd = m_p_qcd_bare_mev(q_val)
        mp_qed_plain = borromean_v3_proton_self_shift_mev(q_val, cartan_weight=False)
        mp_qed_kp = borromean_v3_proton_self_shift_mev(q_val, cartan_weight=True)
        m_mu_pred = muon_mass_mev(q_val)
        mu_err_ppb = (m_mu_pred - m_mu_codata) / m_mu_codata * mp.mpf("1e9")
        dq_over_q1t_ppb = (q_val - q_1t) / q_1t * mp.mpf("1e9")
        q_vs_qmu_ppb = (q_val - q_muon) / q_muon * mp.mpf("1e9")

        qed_splits = {
            w_mode: borromean_v3_connected_qed_splitting(q_val, cartan_weight=w_mode)
            for w_mode in ("plain", "KnKp", "Kp3", "q")
        }

        pin_summary[pin_name] = {
            "q": fmt(q_val),
            "delta_q_vs_q1t_ppb": fmt(dq_over_q1t_ppb),
            "q_vs_q_muon_ppb": fmt(q_vs_qmu_ppb),
            "m_p_QCD_bare_MeV": fmt(mp_qcd),
            "M_p_QED_conn_plain_MeV": fmt(mp_qed_plain),
            "M_p_QED_conn_Kp_MeV": fmt(mp_qed_kp),
            "m_p_2t_plain_MeV": fmt(mp_qcd + mp_qed_plain),
            "m_p_2t_Kp_MeV": fmt(mp_qcd + mp_qed_kp),
            "m_mu_pred_MeV": fmt(m_mu_pred),
            "m_mu_residual_ppb": fmt(mu_err_ppb),
            "bases_MeV": {k: fmt(v) for k, v in b_info.items()},
            "qed_splittings_MeV": {
                w_mode: fmt(qed_splits[w_mode]["delta_m_qed_mev"])
                for w_mode in ("plain", "KnKp", "Kp3", "q")
            },
        }

        for base_name in (
            "Q_A",
            "Q_KD6_nuc11_interleaved",
            "Q_GPMT_pos_nuc11_interleaved",
            "Q_GPMT_pos_nuc11_gen_grouped",
        ):
            q_base = b_info[base_name]
            for ph_name, alpha_val in w_info["phases"].items():
                f1 = mp.cos(alpha_val - u_lad / mp.mpf(2))
                q_n1 = q_base * f1
                q_n2 = q_n1 * f2
                strong_err_ev = (q_n2 - q_codata) * mp.mpf("1e6")
                strong_err_ppm = (q_n2 - q_codata) / q_codata * mp.mpf("1e6")

                qed_outcomes: dict[str, dict] = {}
                for w_mode in ("plain", "KnKp", "Kp3", "q"):
                    dm_qed = qed_splits[w_mode]["delta_m_qed_mev"]
                    q_final = q_n2 + dm_qed
                    q_err_ev = (q_final - q_codata) * mp.mpf("1e6")
                    q_err_ppm = (q_final - q_codata) / q_codata * mp.mpf("1e6")

                    # Consistent 2-term total neutron mass (anchored to m_p^exp = m_p^{2t} at 2-term pin)
                    mn_consistent = mp_codata + me_codata + q_final
                    mn_consistent_err_ppb = (
                        (mn_consistent - mn_codata) / mn_codata * mp.mpf("1e9")
                    )

                    # Bare-proton-core evaluation m_p^{QCD}(q) + m_e + Q_final (omitting M_p^{QED,conn})
                    mn_bare_core = mp_qcd + me_codata + q_final
                    mn_bare_core_err_ppb = (
                        (mn_bare_core - mn_codata) / mn_codata * mp.mpf("1e9")
                    )

                    qed_outcomes[w_mode] = {
                        "delta_m_QED_MeV": fmt(dm_qed),
                        "delta_m_QED_eV": fmt(dm_qed * mp.mpf("1e6")),
                        "Q_beta_final_MeV": fmt(q_final),
                        "Q_beta_err_eV": fmt(q_err_ev),
                        "Q_beta_err_ppm": fmt(q_err_ppm),
                        "m_n_consistent_MeV": fmt(mn_consistent),
                        "m_n_consistent_err_ppb": fmt(mn_consistent_err_ppb),
                        "m_n_bare_proton_core_MeV": fmt(mn_bare_core),
                        "m_n_bare_proton_core_err_ppb": fmt(mn_bare_core_err_ppb),
                    }

                cell_key = f"{pin_name}__{base_name}__{ph_name}"
                phase_base_qed_grid[cell_key] = {
                    "pin": pin_name,
                    "base_name": base_name,
                    "phase_name": ph_name,
                    "alpha_value": fmt(alpha_val),
                    "F1_cos": fmt(f1),
                    "F2_quad": fmt(f2),
                    "Q_base_MeV": fmt(q_base),
                    "Q_N1_MeV": fmt(q_n1),
                    "Q_N2_strong_MeV": fmt(q_n2),
                    "Q_N2_strong_err_eV": fmt(strong_err_ev),
                    "Q_N2_strong_err_ppm": fmt(strong_err_ppm),
                    "qed_variants": qed_outcomes,
                }

    # Part 3: Logarithmic sensitivity contrast & complete eV/ppb budget
    dq_rel = (q_2t_plain - q_1t) / q_1t
    mp_1t = m_p_qcd_bare_mev(q_1t)
    mp_2t = m_p_qcd_bare_mev(q_2t_plain)
    s_mp = ((mp_2t - mp_1t) / mp_1t) / dq_rel

    b_1t = bases_at_q(q_1t, me_codata)
    b_2t = bases_at_q(q_2t_plain, me_codata)
    s_qa = ((b_2t["Q_A"] - b_1t["Q_A"]) / b_1t["Q_A"]) / dq_rel
    s_qkd6 = (
        (b_2t["Q_KD6_nuc11_interleaved"] - b_1t["Q_KD6_nuc11_interleaved"])
        / b_1t["Q_KD6_nuc11_interleaved"]
    ) / dq_rel
    s_qgpmt_int = (
        (
            b_2t["Q_GPMT_pos_nuc11_interleaved"]
            - b_1t["Q_GPMT_pos_nuc11_interleaved"]
        )
        / b_1t["Q_GPMT_pos_nuc11_interleaved"]
    ) / dq_rel

    sensitivity_budget = {
        "delta_q_over_q1t_ppb": fmt(dq_rel * mp.mpf("1e9")),
        "S_m_p_dln_mp_dln_q": fmt(s_mp),
        "S_Q_A_dln_QA_dln_q": fmt(s_qa),
        "S_Q_KD6_dln_QKD6_dln_q": fmt(s_qkd6),
        "S_Q_GPMT_pos_dln_QGPMT_dln_q": fmt(s_qgpmt_int),
        "delta_m_p_QCD_eV_from_q2t_shift": fmt((mp_2t - mp_1t) * mp.mpf("1e6")),
        "delta_Q_A_eV_from_q2t_shift": fmt(
            (b_2t["Q_A"] - b_1t["Q_A"]) * mp.mpf("1e6")
        ),
        "delta_Q_KD6_eV_from_q2t_shift": fmt(
            (b_2t["Q_KD6_nuc11_interleaved"] - b_1t["Q_KD6_nuc11_interleaved"])
            * mp.mpf("1e6")
        ),
    }

    # Print summary tables
    print("=" * 100)
    print(
        "QBETA WEDDERBURN PHASE (qou-q2oa), TWO-TERM PIN q_2t, AND 11-LETTER WORD GAP (qou-j1e5) — 80 DPS"
    )
    print("=" * 100)
    p1_1t = part1_by_pin["q_1t"]
    print(f"  q_1t                     = {p1_1t['q']}")
    print(f"  q_2t (plain)             = {part1_by_pin['q_2t_plain']['q']}  (+{pin_summary['q_2t_plain']['delta_q_vs_q1t_ppb'][:8]} ppb)")
    print(f"  q_2t (Kp)                = {part1_by_pin['q_2t_Kp']['q']}  (+{pin_summary['q_2t_Kp']['delta_q_vs_q1t_ppb'][:8]} ppb)")
    print(f"  q_muon                   = {part1_by_pin['q_muon']['q']}  (+{pin_summary['q_muon']['delta_q_vs_q1t_ppb'][:8]} ppb)")
    print(f"  w_(3)(z_D) = Xi_D        = {p1_1t['w3_zD']}")
    print(f"  w_(2,1)(z_D) (TRUE)      = {p1_1t['w21_zD']}  (> 0)")
    print(f"  1/2 - z_D (RETRACTED)    = {p1_1t['kappa_retracted_half_minus_zD']}  (< 0)")
    print(f"  w_(2,1)(z_D) - (1/2-z_D) = {p1_1t['w21_minus_kappa_gap']}  (closed-form residual {p1_1t['w21_minus_kappa_closed_residual']})")

    print("\n" + "-" * 100)
    print("PART 1: PARAMETER-FREE WEDDERBURN / JUCYS-MURPHY / MIRROR-COVARIANT PHASE FUNCTIONALS AT q_2t_plain")
    print("-" * 100)
    print(
        f"  {'Phase Functional':28s} | {'alpha(q_2t)':14s} | {'Q_A+N2+QED (ppm)':18s} | {'Q_KD6+N2+QED (ppm)':20s} | {'m_n (KD6+QED) ppb'}"
    )
    for ph_name in part1_by_pin["q_2t_plain"]["phases"]:
        c_qa = phase_base_qed_grid[f"q_2t_plain__Q_A__{ph_name}"]
        c_kd6 = phase_base_qed_grid[
            f"q_2t_plain__Q_KD6_nuc11_interleaved__{ph_name}"
        ]
        print(
            f"  {ph_name:28s} | {c_qa['alpha_value'][:14]:14s} | "
            f"{c_qa['qed_variants']['plain']['Q_beta_err_ppm'][:12]:>12s} ppm   | "
            f"{c_kd6['qed_variants']['plain']['Q_beta_err_ppm'][:12]:>12s} ppm     | "
            f"{c_kd6['qed_variants']['plain']['m_n_consistent_err_ppb'][:12]:>12s} ppb"
        )

    print("\n" + "-" * 100)
    print("PART 2: TWO-TERM PIN q_2t & 4 CARTAN QED WEIGHTINGS ON Q_A AND Q_KD6 (nuc11_interleaved)")
    print("-" * 100)
    print(
        f"  {'Base':25s} | {'Phase':22s} | {'QED mode':8s} | {'Delta m_QED (eV)':16s} | {'Q_beta err (ppm)':16s} | {'m_n err (ppb)'}"
    )
    for base_name, ph_name in [
        ("Q_A", "alpha_D_asserted"),
        ("Q_KD6_nuc11_interleaved", "alpha_D_asserted"),
        ("Q_KD6_nuc11_interleaved", "alpha_D_mirror_proj"),
        ("Q_KD6_nuc11_interleaved", "alpha_JM_content_mean"),
    ]:
        cell = phase_base_qed_grid[f"q_2t_plain__{base_name}__{ph_name}"]
        for w_mode in ("plain", "KnKp", "Kp3", "q"):
            qv = cell["qed_variants"][w_mode]
            print(
                f"  {base_name:25s} | {ph_name:22s} | {w_mode:8s} | "
                f"{qv['delta_m_QED_eV'][:12]:>12s} eV  | "
                f"{qv['Q_beta_err_ppm'][:12]:>12s} ppm | "
                f"{qv['m_n_consistent_err_ppb'][:12]:>12s} ppb"
            )

    # Verification assertions
    w_1t = wedderburn_weights_and_phases_at_q(q_1t)
    w_2t = wedderburn_weights_and_phases_at_q(q_2t_plain)
    kd6_unproj = phase_base_qed_grid[
        "q_2t_plain__Q_KD6_nuc11_interleaved__alpha_D_asserted"
    ]["qed_variants"]["plain"]
    kd6_proj = phase_base_qed_grid[
        "q_2t_plain__Q_KD6_nuc11_interleaved__alpha_D_mirror_proj"
    ]["qed_variants"]["plain"]
    qa_plain = phase_base_qed_grid["q_2t_plain__Q_A__alpha_D_asserted"][
        "qed_variants"
    ]["plain"]
    qa_q = phase_base_qed_grid["q_2t_plain__Q_A__alpha_D_asserted"]["qed_variants"][
        "q"
    ]

    checks = [
        (
            "w21_zD_minus_retracted_kappa_rational_identity",
            bool(
                w_1t["w21_minus_kappa_closed_residual"] < mp.mpf("1e-70")
                and w_1t["w21_minus_kappa"] > mp.mpf("0.35")
            ),
            (
                f"w_(2,1)(z_D) - (1/2 - z_D) = (2q^5 - q^4 + 2q^3 - 1)/(2(q^2+1)^2) = "
                f"{fmt(w_1t['w21_minus_kappa'], 20)} > 0 (residual {fmt(w_1t['w21_minus_kappa_closed_residual'], 10)})"
            ),
        ),
        (
            "jm_content_mean_equals_transposition_moment_w3_zD",
            bool(
                abs(w_1t["jm_content_mean_D"] - w_1t["Xi_D"]) < mp.mpf("1e-70")
                and w_1t["loop_mean_residual"] < mp.mpf("1e-70")
                and w_1t["Xi_GPMT_pos_closed_residual"] < mp.mpf("1e-70")
            ),
            (
                f"Jucys-Murphy content mean <c_bar>_D = w_(3)(z_D) = Xi_D = {fmt(w_1t['Xi_D'], 20)} "
                f"and loop-mean identity (2*z_D - h) = [2]_q * Xi_D holds to {fmt(w_1t['loop_mean_residual'], 10)}"
            ),
        ),
        (
            "mirror_projected_phase_cuts_kd6_residual_3x_and_brackets_codata",
            bool(
                w_2t["mirror_proj_w3_form_residual"] < mp.mpf("1e-70")
                and mp.mpf(kd6_proj["Q_beta_err_ppm"])
                < mp.mpf(0)
                < mp.mpf(kd6_unproj["Q_beta_err_ppm"])
                and abs(mp.mpf(kd6_proj["Q_beta_err_ppm"]))
                < abs(mp.mpf(kd6_unproj["Q_beta_err_ppm"])) / mp.mpf("2.5")
            ),
            (
                f"On KD6 * z_D (nuc11_interleaved), mirror-covariant bar-odd projection "
                f"alpha_D^proj = alpha_D - h^2/4 moves Q_beta from +{kd6_unproj['Q_beta_err_ppm'][:7]} ppm "
                f"(+{kd6_unproj['m_n_consistent_err_ppb'][:7]} ppb on m_n) to {kd6_proj['Q_beta_err_ppm'][:8]} ppm "
                f"({kd6_proj['m_n_consistent_err_ppb'][:8]} ppb on m_n), bracketing CODATA"
            ),
        ),
        (
            "two_term_proton_pin_collapses_mu_p_tension_with_sub_0p04eV_qbeta_shift",
            bool(
                abs(mp.mpf(pin_summary["q_2t_plain"]["q_vs_q_muon_ppb"]))
                < mp.mpf("10")
                and abs(mp.mpf(pin_summary["q_2t_Kp"]["q_vs_q_muon_ppb"]))
                < mp.mpf("10")
                and abs(
                    mp.mpf(sensitivity_budget["delta_Q_A_eV_from_q2t_shift"])
                )
                < mp.mpf("0.05")
                and abs(
                    mp.mpf(sensitivity_budget["delta_Q_KD6_eV_from_q2t_shift"])
                )
                < mp.mpf("0.05")
            ),
            (
                f"q_2t_plain shifts q by +{pin_summary['q_2t_plain']['delta_q_vs_q1t_ppb'][:7]} ppb "
                f"(collapsing mu-p tension to +{pin_summary['q_2t_plain']['q_vs_q_muon_ppb'][:5]} ppb) "
                f"while shifting Q_A by only {sensitivity_budget['delta_Q_A_eV_from_q2t_shift'][:8]} eV "
                f"and Q_KD6 by +{sensitivity_budget['delta_Q_KD6_eV_from_q2t_shift'][:7]} eV"
            ),
        ),
        (
            "form_a_two_term_qed_cartan_weightings_span_148_to_110_ppb_on_mn",
            bool(
                mp.mpf("105")
                < mp.mpf(qa_q["m_n_consistent_err_ppb"])
                < mp.mpf(qa_plain["m_n_consistent_err_ppb"])
                < mp.mpf("150")
            ),
            (
                f"On Form-A + 2tQED at q_2t, m_n residual spans +{qa_plain['m_n_consistent_err_ppb'][:7]} ppb "
                f"('plain', -331.70 eV) to +{qa_q['m_n_consistent_err_ppb'][:7]} ppb ('q', -368.18 eV)"
            ),
        ),
    ]

    print("\n" + "-" * 100)
    print("VERIFICATION CHECKS")
    print("-" * 100)
    for name, passed, detail in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name} — {detail}")
    assert all(p for _, p, _ in checks), "One or more verification checks failed!"

    w = WitnessBuilder("qbeta-wedderburn-phase-twoterm-pin")
    w.set_description(
        "80-dps parameter-free evaluation of the Convention-D Wedderburn / Jucys-Murphy / "
        "mirror-covariant ladder phase functionals alpha_Wed(q) (qou-q2oa), propagation of "
        "the two-term QED proton pin q_{2t} into m_p, m_mu, Q_beta, and m_n across 4 bases "
        "and 4 Cartan QED weightings, and exact eV/ppb error budget (qou-cds1, qou-j1e5)."
    )
    w.add_data("q0_anchor", "proton")
    w.add_data("q0_value", Q_50_DIGIT_STR)
    w.add_data("dps", 80)
    w.add_data("part1_wedderburn_weights_and_phases_by_pin", part1_by_pin)
    w.add_data("part2_pin_summary", pin_summary)
    w.add_data("part2_phase_base_qed_grid", phase_base_qed_grid)
    w.add_data("part3_sensitivity_and_ev_ppb_budget", sensitivity_budget)
    w.add_caveat(
        "All evaluated phase functionals, bases, substrate pins, and Cartan QED weightings "
        "are parameter-free algebraic/trigonometric functions of q at 80 dps (zero fitted "
        "parameters, zero float64)."
    )
    for name, passed, detail in checks:
        w.add_assertion(name, "1" if passed else "0", "1", "0", source=detail)

    from qou_substrate.witness import q0_comparison  # noqa: E402

    out_path = w.save(
        q0_comparison(
            muon=q_muon,
            proton=q_1t,
            reason=(
                "Deliberately compares 1-term proton, 2-term Borromean proton (plain and Kp), "
                "and CODATA-2022 muon pins across Wedderburn phase functionals and Q_beta/m_n."
            ),
        )
    )
    print(f"\nWrote witness -> {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
