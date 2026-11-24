#!/usr/bin/env python3
"""muon_fbor_poincare_and_worldline_loop_probe.py

80-dps zero-fitting diagnostic and working-assumption probe for the mu-p
substrate residual and the algebraic identities of
`QOU/BraidKnot/MuonFigureEightFBorPoincareIdentities.lean`
(beans `qou-1ozb`, `qou-6gf9`, `qou-24w9`, `qou-gbsa`).

Companion audit:
`docs/audits/2026-11-24-muon-41-fbor-poincare-worldline-adjudication.md`.

What this script verifies and records at 80 decimal digits (`mp.mp.dps = 80`,
zero `float64`, CODATA-2022 read exclusively from `qou_substrate.codata`,
cross-anchor `q0_comparison` at both `q_p` and `q_mu`):

  (a) Coupled-vs-Uncoupled Re-Pinning Theorem:
      Any universal multiplicative dressing `M_mu(q) -> M_mu(q) * (1 - delta)`
      shared by the proton's `Vol(4_1) / hbar_q^2` constituent and the free
      muon shifts `q_p` by `-10.12 ppb`, re-absorbing `~87.2%` (`~92%` against
      the `200 ppb` nominal scale) of `delta` back into `q_p`, leaving
      `m_mu / m_e` at `+184.12 ppb` while pulling Form-B `1 / alpha_EM` by
      `-69.19 ppb`. A genuine resolution of the mu-p offset must therefore
      distinguish the free open-worldline muon from the bound colour-singlet
      Borromean constituent.

  (b) Exclusion of Track 2 (`[murakami-h2011]` real-`u` `4_1` torsion
      `1 - sqrt(3 - 2 cosh u)`: `4.82e4 .. 5.46e6 ppb`), Track 4 (`4_1` and
      `Sigma(2,3,5)` instantons: `1.27 .. 6.08 ppb` and `1.90e8 ppb`), and all
      five canonical proton counterterms on `V_p^3`:
        1. static all-pairs `QPairP = 0` (`0 keV`);
        2. diagonal self-energy `QSelfP = I_3` (absorbed scalar `1`);
        3. unprojected adjacent-crossing EM trace
           `E_0(q_p)(1 - q_p^-1) tr((Q12p + Q23p) V_p^3) = -0.53588 keV`
           (opposite sign to the `+0.22881 keV` / `+0.22877 keV` proton shift
           needed to align `q_p` with `q_mu`, worsening `mu-p` to `+705.86 ppb`);
        4. `e_(2,1)`-projected adjacent-crossing EM trace (`-25.56 keV`,
           opposite sign and `112x` too large);
        5. non-covariant modulus-flipped two-term pin `+|tr_conn(p, V^3)|`
           (shifts `q_p` by `+11.17 ppb` and degrades Form-B `1 / alpha_EM` to
           `+75.97 ppb`).

  (c) Exact 4D Worldline QED 1-Loop Fermion Self-Energy Asymptotic:
      Direct 80-dps quadrature of the intrinsic-clock Schwinger proper-time
      integral (`s_1 >= u_l`, `s_2 >= u_l`) confirms to `< 1e-25`:
        delta m_l^WL(u_l) / m_l = (alpha_EM / (2 pi)) * [
            (3/2) * (ln(1 / u_l) - gamma_E) + (1 - (3/2) ln 2) + O(u_l ln u_l)
        ],
      with single-clock massless-subtracted finite part `+(5/4)(alpha_EM / pi)`
      and exact lepton-universal cancellation (`0`) at `u_e = u_mu`. Naive
      1-vertex and 2-vertex Hecke photon-projector `e_i^(-) = (q - sigma_i)/[2]_q`
      correlators on `4_1 = (sigma_1 sigma_2^-1)^2` carry `O(w^0)` and `O(w^1)`
      pieces (`(3 alpha_EM / (4 pi)) w = +18,983.6 ppb`, `~90x` too large).
      The two surviving bar-even working-assumption candidates —
        * 2-loop Bring-Schwinger: `-alpha_EM^2 H(q) h^2 = -186.22 ppb`
          (leaving `+24.99 ppb = +1.12 sigma`, or `+24.95 ppb = +1.15 sigma`
          relative to the historical `211.16 ppb` tension witness);
        * 1-loop double-commutator: `-(3 alpha_EM / (4 pi)) w^2 = -206.86 ppb`
          (leaving `+4.34 ppb = +0.20 sigma`, or `+4.30 ppb` against `211.16 ppb`)
      — are recorded strictly as UNWIRED WORKING-ASSUMPTION PROBES respecting
      the `~10.5%` (`10.3%` at `22 ppb / 211 ppb`) 1-digit CODATA entropy bound.

  (d) 80-dps cross-check of the three `[Field K]` algebraic theorem groups in
      `MuonFigureEightFBorPoincareIdentities.lean`:
        1. `chi_(2,1)(Delta_3) = 0`, `tr_M(4_1) = (q^5 + q^-5)/(q + q^-1)^3`,
           and ratio `2 q^3 / ((q^2 + 1)(q^4 + 1))` to bar-symmetrized 2-strand
           `T(2,5)`;
        2. `[3]_q! / q^3 = (1 + q^-2)(1 + q^-2 + q^-4) = P_{S_3}(q^-2)` from
           chiral horizontal-Dirac Hecke generator `T = q^-1 sigma`;
        3. asymmetric Seifert determinant / balanced Alexander identity
           connecting `(t^2 - t + 1)(t^6 - t^3 + 1) Phi_15(t)` at `t = q^-1`
           to `q^-8 Delta_{T(2,9)}(q) Delta_{T(3,5)}(q)`.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import _path_bridge  # noqa: E402, F401
from _precision import fmt, set_compute_dps  # noqa: E402

set_compute_dps(80)
mp.mp.dps = 80

from qou_substrate import codata as _codata  # noqa: E402
from qou_substrate.constants import (  # noqa: E402
    Q_MUON_50_DIGIT_STR,
    q_at,
    q_muon_at,
    q_proton_two_term_at,
    vol_4_1_at,
)
from witness_base import WitnessBuilder, q0_comparison  # noqa: E402

PPB = mp.mpf(10) ** 9


def qbal(n: int, q: mp.mpf) -> mp.mpf:
    """Balanced quantum integer [n]_q = (q^n - q^{-n}) / (q - q^{-1})."""
    return (q**n - q ** (-n)) / (q - mp.mpf(1) / q)


def hbar_q(q: mp.mpf) -> mp.mpf:
    """Substrate Planck deformation parameter 1 - q^{-1}."""
    return mp.mpf(1) - mp.mpf(1) / q


def w_gen(q: mp.mpf) -> mp.mpf:
    """Bar-even Habiro / [2]_q - 2 generator w(q) = q + q^{-1} - 2 = q * hbar_q^2."""
    return q + mp.mpf(1) / q - mp.mpf(2)


def f_bor(q: mp.mpf) -> mp.mpf:
    """Borromean proton factor |tr_M(beta_Bor)| * [3]_q! / q^3."""
    h = q - mp.mpf(1) / q
    tr_abs = mp.fabs((mp.mpf(4) + h**2 - mp.mpf(3) * h**4 - h**6) / (h**2 + mp.mpf(4)))
    return tr_abs * qbal(3, q) * qbal(2, q) / (q**3)


def m_mu_bare(q: mp.mpf, vol41: mp.mpf) -> mp.mpf:
    """Bare figure-eight muon-electron mass ratio Vol(4_1) / hbar_q^2."""
    return vol41 / (hbar_q(q) ** 2)


def m_p_one_term(q: mp.mpf, vol41: mp.mpf) -> mp.mpf:
    """One-term Borromean proton-electron mass ratio 2 * M_mu(q) * F_Bor(q) - 12."""
    return mp.mpf(2) * m_mu_bare(q, vol41) * f_bor(q) - mp.mpf(12)


def alpha_form_b_inv(q: mp.mpf) -> mp.mpf:
    """Form-B inverse fine-structure fixed point: 1/a = T + a * H * (1 - h^2 * a)."""
    h2 = (q - mp.mpf(1) / q) ** 2
    t_tree = q * qbal(9, q) * qbal(10, q) + mp.mpf(2) / (mp.mpf(3) * mp.pi)
    h_loop = qbal(2, q) / (mp.mpf(8) * mp.pi)
    a = mp.mpf(1) / t_tree
    tol = mp.mpf(10) ** (-75)
    for _ in range(200):
        a_next = mp.mpf(1) / (t_tree + a * h_loop * (mp.mpf(1) - h2 * a))
        if mp.fabs(a_next - a) < tol:
            a = a_next
            break
        a = a_next
    return mp.mpf(1) / a


def mat3(rows: list[list[mp.mpf]]) -> mp.matrix:
    return mp.matrix(rows)


def tr3(m: mp.matrix) -> mp.mpf:
    return m[0, 0] + m[1, 1] + m[2, 2]


def a1_mat(q: mp.mpf) -> mp.matrix:
    z = mp.mpf(0)
    o = mp.mpf(1)
    return mat3([[q, z, z], [z, z, o], [z, o, q - o / q]])


def a2_mat(q: mp.mpf) -> mp.matrix:
    z = mp.mpf(0)
    o = mp.mpf(1)
    return mat3([[z, o, z], [o, q - o / q, z], [z, z, q]])


def a2_inv_mat(q: mp.mpf) -> mp.matrix:
    z = mp.mpf(0)
    o = mp.mpf(1)
    return mat3([[o / q - q, o, z], [o, z, z], [z, z, o / q]])


def fep_mat(q: mp.mpf) -> mp.matrix:
    return mat3(
        [
            [q**2, q, mp.mpf(1)],
            [q, mp.mpf(1), mp.mpf(1) / q],
            [mp.mpf(1), mp.mpf(1) / q, mp.mpf(1) / (q**2)],
        ]
    )


def worldline_inner_kernel(s: mp.mpf, u: mp.mpf) -> mp.mpf:
    """Exact inner y-integral of (1 + y) exp(-s y^2) on [u/s, 1 - u/s] for s >= 2u."""
    a = u / s
    b = mp.mpf(1) - a
    rs = mp.sqrt(s)
    term_erf = (
        mp.mpf(1)
        / mp.mpf(2)
        * mp.sqrt(mp.pi / s)
        * (mp.erf(rs * b) - mp.erf(rs * a))
    )
    term_exp = (mp.exp(-s * (a**2)) - mp.exp(-s * (b**2))) / (mp.mpf(2) * s)
    return term_erf + term_exp


def worldline_self_energy_coeff_quad(u: mp.mpf) -> mp.mpf:
    """80-dps quadrature of int_u^inf ds_1 int_u^inf ds_2 (2 s_1 + s_2)/(s_1 + s_2)^3 exp(-s_1^2/(s_1+s_2))."""
    raw_pts = [
        mp.mpf(2) * u,
        mp.mpf(4) * u,
        mp.mpf(16) * u,
        mp.mpf(100) * u,
        mp.sqrt(u),
        mp.mpf("0.1"),
        mp.mpf(1),
        mp.mpf(10),
        mp.mpf(60),
    ]
    pts = sorted({p for p in raw_pts if p >= mp.mpf(2) * u}) + [mp.inf]
    return mp.quad(lambda s: worldline_inner_kernel(s, u) / s, pts)


def worldline_self_energy_coeff_symbolic(u: mp.mpf) -> mp.mpf:
    """Leading small-u asymptotic (3/2)(ln(1/u) - gamma_E) + (1 - (3/2) ln 2)."""
    return mp.mpf(3) / mp.mpf(2) * (mp.log(mp.mpf(1) / u) - mp.euler) + (
        mp.mpf(1) - mp.mpf(3) / mp.mpf(2) * mp.log(mp.mpf(2))
    )


def evaluate_pin_bundle(
    q: mp.mpf,
    vol41: mp.mpf,
    mmu_exp: mp.mpf,
    sigma_mu_ppb: mp.mpf,
    alpha_codata: mp.mpf,
) -> dict[str, str]:
    """Evaluate algebraic identities and unwired working-assumption candidates at a pin `q`."""
    h = q - mp.mpf(1) / q
    w = w_gen(q)
    h_loop = qbal(2, q) / (mp.mpf(8) * mp.pi)
    ainv_b = alpha_form_b_inv(q)
    alpha_b = mp.mpf(1) / ainv_b
    mmu_pred = m_mu_bare(q, vol41)
    bare_ppb = (mmu_pred - mmu_exp) / mmu_exp * PPB

    # Unwired working-assumption candidates (evaluated with both Form-B alpha(q) and CODATA alpha)
    cand_bs_b = -(alpha_b**2) * h_loop * (h**2)
    cand_dc_b = -(mp.mpf(3) * alpha_b / (mp.mpf(4) * mp.pi)) * (w**2)
    cand_bs_codata = -(alpha_codata**2) * h_loop * (h**2)
    cand_dc_codata = -(mp.mpf(3) * alpha_codata / (mp.mpf(4) * mp.pi)) * (w**2)
    ow1_scale_b = (mp.mpf(3) * alpha_b / (mp.mpf(4) * mp.pi)) * w

    resid_bs_ppb = (mmu_pred * (mp.mpf(1) + cand_bs_b) - mmu_exp) / mmu_exp * PPB
    resid_dc_ppb = (mmu_pred * (mp.mpf(1) + cand_dc_b) - mmu_exp) / mmu_exp * PPB

    # Stage B algebraic identities at pin q
    y3 = (q**4 + mp.mpf(1)) / ((q**2 + mp.mpf(1)) ** 2)
    y21 = (q**2) / ((q**2 + mp.mpf(1)) ** 2)
    delta3 = a1_mat(q) * a2_mat(q) * a1_mat(q)
    chi21_delta3 = tr3(delta3) - q**3
    w41 = (a1_mat(q) * a2_inv_mat(q)) * (a1_mat(q) * a2_inv_mat(q))
    chi21_41 = tr3(w41) - mp.mpf(1)
    trm_41_mat = y3 * mp.mpf(1) + y21 * chi21_41
    trm_41_closed = (q**5 + q ** (-5)) / ((q + mp.mpf(1) / q) ** 3)
    t25_bar = (
        (q**2 + q ** (-2))
        * (q**5 + q ** (-5))
        / (mp.mpf(2) * ((q + mp.mpf(1) / q) ** 2))
    )
    ratio_41_t25 = (mp.mpf(2) * (q**3)) / ((q**2 + mp.mpf(1)) * (q**4 + mp.mpf(1)))

    poincare_lhs = qbal(3, q) * qbal(2, q) / (q**3)
    poincare_rhs = (
        mp.mpf(1)
        + mp.mpf(2) * (q ** (-2))
        + mp.mpf(2) * (q ** (-4))
        + (q ** (-6))
    )

    t_inv = mp.mpf(1) / q
    seifert_lhs = (
        (t_inv**2 - t_inv + mp.mpf(1))
        * (t_inv**6 - t_inv**3 + mp.mpf(1))
        * (t_inv**8 - t_inv**7 + t_inv**5 - t_inv**4 + t_inv**3 - t_inv + mp.mpf(1))
    )
    delta_t29 = (
        (q ** (-4))
        * (q**18 - mp.mpf(1))
        * (q - mp.mpf(1))
        / ((q**2 - mp.mpf(1)) * (q**9 - mp.mpf(1)))
    )
    delta_t35 = (
        (q ** (-4))
        * (q**15 - mp.mpf(1))
        * (q - mp.mpf(1))
        / ((q**3 - mp.mpf(1)) * (q**5 - mp.mpf(1)))
    )
    seifert_rhs = (q ** (-8)) * delta_t29 * delta_t35
    kappa_seifert = (q**8) / (delta_t29 * delta_t35)

    return {
        "q": fmt(q),
        "hbar_q": fmt(hbar_q(q)),
        "w_bar_even": fmt(w),
        "alpha_formB_inv": fmt(ainv_b),
        "kappa_seifert": fmt(kappa_seifert),
        "m_mu_bare": fmt(mmu_pred),
        "bare_overshoot_ppb": fmt(bare_ppb),
        "ow1_naive_1loop_ppb": fmt(ow1_scale_b * PPB),
        "unwired_cand_bring_schwinger_2loop_ppb": fmt(cand_bs_b * PPB),
        "unwired_cand_bring_schwinger_2loop_codata_alpha_ppb": fmt(cand_bs_codata * PPB),
        "unwired_cand_bring_schwinger_post_resid_ppb": fmt(resid_bs_ppb),
        "unwired_cand_bring_schwinger_post_sigma": fmt(resid_bs_ppb / sigma_mu_ppb),
        "unwired_cand_double_comm_1loop_ppb": fmt(cand_dc_b * PPB),
        "unwired_cand_double_comm_1loop_codata_alpha_ppb": fmt(cand_dc_codata * PPB),
        "unwired_cand_double_comm_post_resid_ppb": fmt(resid_dc_ppb),
        "unwired_cand_double_comm_post_sigma": fmt(resid_dc_ppb / sigma_mu_ppb),
        "chi21_delta3_abs_err": fmt(mp.fabs(chi21_delta3)),
        "trm_41_matrix_minus_closed_abs_err": fmt(mp.fabs(trm_41_mat - trm_41_closed)),
        "ratio_41_to_t25_abs_err": fmt(mp.fabs(trm_41_mat / t25_bar - ratio_41_t25)),
        "poincare_s3_abs_err": fmt(mp.fabs(poincare_lhs - poincare_rhs)),
        "seifert_alexander_abs_err": fmt(mp.fabs(seifert_lhs - seifert_rhs)),
        "seifert_kappa_reciprocal_abs_err": fmt(mp.fabs(seifert_lhs * kappa_seifert - mp.mpf(1))),
    }


def main() -> int:
    # Authoritative CODATA-2022 constants read exclusively from qou_substrate.codata
    mp_entry = _codata.codata("proton-electron mass ratio")
    mmu_entry = _codata.codata("muon-electron mass ratio")
    ainv_entry = _codata.codata("inverse fine-structure constant")
    me_entry = _codata.codata("electron mass energy equivalent in MeV")

    mp_me = mp.mpf(mp_entry.value_str)
    mp_me_u = mp.mpf(mp_entry.uncertainty_str)
    mmu_me = mp.mpf(mmu_entry.value_str)
    mmu_me_u = mp.mpf(mmu_entry.uncertainty_str)
    ainv_exp = mp.mpf(ainv_entry.value_str)
    ainv_exp_u = mp.mpf(ainv_entry.uncertainty_str)
    me_kev = mp.mpf(me_entry.value_str) * mp.mpf(1000)

    alpha_codata = mp.mpf(1) / ainv_exp
    sigma_mu_ppb = mmu_me_u / mmu_me * PPB
    sigma_ainv_ppb = ainv_exp_u / ainv_exp * PPB

    vol41 = vol_4_1_at(80)
    q_p = q_at(80)
    q_mu = q_muon_at(80)
    q_mu_frozen = mp.mpf(Q_MUON_50_DIGIT_STR)
    q_p_two_term = q_proton_two_term_at(80)

    # Bare residual & CODATA entropy bound
    mmu_at_qp = m_mu_bare(q_p, vol41)
    bare_overshoot_ppb = (mmu_at_qp - mmu_me) / mmu_me * PPB
    delta_req = mp.mpf(1) - mmu_me / mmu_at_qp
    entropy_fraction = sigma_mu_ppb / (delta_req * PPB)
    sig_digits_on_residual = -mp.log10(entropy_fraction)

    # ------------------------------------------------------------------
    # (a) Coupled-vs-Uncoupled Re-Pinning Theorem (80 dps)
    # ------------------------------------------------------------------
    q_p_coupled = mp.findroot(
        lambda q: mp.mpf(2) * m_mu_bare(q, vol41) * (mp.mpf(1) - delta_req) * f_bor(q)
        - mp.mpf(12)
        - mp_me,
        q_p,
    )
    shift_qp_coupled_ppb = (q_p_coupled - q_p) / q_p * PPB
    mmu_coupled = m_mu_bare(q_p_coupled, vol41) * (mp.mpf(1) - delta_req)
    resid_coupled_ppb = (mmu_coupled - mmu_me) / mmu_me * PPB
    reabsorbed_exact = resid_coupled_ppb / bare_overshoot_ppb

    ainv_qp = alpha_form_b_inv(q_p)
    ainv_coupled = alpha_form_b_inv(q_p_coupled)
    shift_ainv_coupled_ppb = (ainv_coupled - ainv_qp) / ainv_qp * PPB

    sl_mu = q_p * mp.diff(lambda x: m_mu_bare(x, vol41), q_p) / mmu_at_qp
    sl_fbor = q_p * mp.diff(f_bor, q_p) / f_bor(q_p)
    reabsorbed_linear_theorem = sl_mu / (sl_mu + sl_fbor)

    # ------------------------------------------------------------------
    # (b) Exclusion of Track 2, Track 4, and all 5 proton counterterms
    # ------------------------------------------------------------------
    # Track 2: [murakami-h2011] real-u 4_1 Reidemeister torsion 1 - sqrt(3 - 2 cosh u)
    u_hbar_sq = hbar_q(q_p) ** 2
    u_w = w_gen(q_p)
    u_hbar = hbar_q(q_p)
    u_lnq = mp.log(q_p)
    u_q_minus_1 = q_p - mp.mpf(1)
    track2_torsion_ppb = {
        "u_eq_hbar_q_sq": fmt((mp.mpf(1) - mp.sqrt(mp.mpf(3) - mp.mpf(2) * mp.cosh(u_hbar_sq))) * PPB),
        "u_eq_w_bar_even": fmt((mp.mpf(1) - mp.sqrt(mp.mpf(3) - mp.mpf(2) * mp.cosh(u_w))) * PPB),
        "u_eq_hbar_q": fmt((mp.mpf(1) - mp.sqrt(mp.mpf(3) - mp.mpf(2) * mp.cosh(u_hbar))) * PPB),
        "u_eq_ln_q_p": fmt((mp.mpf(1) - mp.sqrt(mp.mpf(3) - mp.mpf(2) * mp.cosh(u_lnq))) * PPB),
        "u_eq_q_p_minus_1": fmt((mp.mpf(1) - mp.sqrt(mp.mpf(3) - mp.mpf(2) * mp.cosh(u_q_minus_1))) * PPB),
    }

    # Track 4: 4_1 hyperbolic & Sigma(2,3,5) Chern-Simons instantons
    inst_41_hbar_ppb = mp.exp(-vol41 / u_hbar) * PPB
    inst_41_lnq_ppb = mp.exp(-vol41 / u_lnq) * PPB
    inst_41_half_h_ppb = mp.exp(-mp.mpf(2) * vol41 / (q_p - mp.mpf(1) / q_p)) * PPB
    inst_41_with_2loop_prefactor_ppb = (
        mp.sqrt(mp.mpf(2) * mp.pi / u_hbar) * mp.exp(-vol41 / u_hbar) / mp.sqrt(mp.mpf(3)) * PPB
    )
    inst_sigma235_hbar_ppb = mp.exp(-(mp.pi**2) / (mp.mpf(60) * u_hbar)) * PPB
    inst_sigma235_lnq_ppb = mp.exp(-(mp.pi**2) / (mp.mpf(60) * u_lnq)) * PPB

    # 5 Canonical proton counterterms on Borromean V_p^3 = (A_1 A_2^-1)^3
    vp = a1_mat(q_p) * a2_inv_mat(q_p)
    vp3 = vp * vp * vp
    z = mp.mpf(0)
    q12p = mat3([[mp.mpf(4) / 9, z, z], [z, -mp.mpf(2) / 9, z], [z, z, -mp.mpf(2) / 9]])
    q23p = mat3([[-mp.mpf(2) / 9, z, z], [z, -mp.mpf(2) / 9, z], [z, z, mp.mpf(4) / 9]])
    q13p = mat3([[-mp.mpf(2) / 9, z, z], [z, mp.mpf(4) / 9, z], [z, z, -mp.mpf(2) / 9]])
    q_pair_p = q12p + q23p + q13p
    i3 = mat3([[mp.mpf(1), z, z], [z, mp.mpf(1), z], [z, z, mp.mpf(1)]])
    qint3_qp = q_p**2 + mp.mpf(1) + q_p ** (-2)
    e21p = i3 - (mp.mpf(1) / qint3_qp) * fep_mat(q_p)

    e0_me = mp.mpf(1) / (q_p * (q_p - mp.mpf(1)))
    e0_kev = me_kev * e0_me

    needed_proton_kev_live_mu = (mp_me - m_p_one_term(q_mu, vol41)) * me_kev
    needed_proton_kev_frozen_mu = (mp_me - m_p_one_term(q_mu_frozen, vol41)) * me_kev

    ct1_qpair_kev = e0_kev * hbar_q(q_p) * tr3(q_pair_p * vp3)
    ct2_qself_trace_ratio = tr3(i3 * vp3) / tr3(vp3)
    ct3_qadj_unproj_kev = e0_kev * hbar_q(q_p) * tr3((q12p + q23p) * vp3)
    ct4_qadj_e21_kev = e0_kev * hbar_q(q_p) * tr3(e21p * (q12p + q23p) * vp3)

    q_p_with_ct3 = mp.findroot(
        lambda q: m_p_one_term(q, vol41)
        + (mp.mpf(1) / (q * (q - mp.mpf(1))))
        * hbar_q(q)
        * tr3((q12p + q23p) * ((a1_mat(q) * a2_inv_mat(q)) ** 3))
        - mp_me,
        q_p,
    )
    mup_with_ct3_ppb = (m_mu_bare(q_p_with_ct3, vol41) - mmu_me) / mmu_me * PPB

    shift_qp_ct5_two_term_ppb = (q_p_two_term - q_p) / q_p * PPB
    ainv_two_term_resid_ppb = (alpha_form_b_inv(q_p_two_term) - ainv_exp) / ainv_exp * PPB

    # ------------------------------------------------------------------
    # (c) 4D Worldline QED 1-Loop Fermion Self-Energy & Hecke Projectors
    # ------------------------------------------------------------------
    u_probe = mp.mpf(10) ** (-30)
    wl_quad_30 = worldline_self_energy_coeff_quad(u_probe)
    wl_sym_30 = worldline_self_energy_coeff_symbolic(u_probe)
    wl_abs_diff_30 = mp.fabs(wl_quad_30 - wl_sym_30)

    # Single-clock massless-subtracted finite part:
    # (alpha / (2 pi)) * int_0^1 (1 + y) (-ln(y^2)) dy = (alpha / (2 pi)) * (5/2) = +(5/4) * (alpha / pi)
    wl_single_clock_finite_quad = mp.quad(
        lambda y: -(mp.mpf(1) + y) * mp.log(y**2), [mp.mpf(0), mp.mpf(1)]
    ) / mp.mpf(2)
    wl_single_clock_finite_exact = mp.mpf(5) / mp.mpf(4)

    # Intrinsic Compton clock u_e = u_mu cancellation in m_mu / m_e
    u_compton = mp.mpf(10) ** (-8)
    wl_ratio_cancel_diff = worldline_self_energy_coeff_quad(
        u_compton
    ) - worldline_self_energy_coeff_quad(u_compton)

    # Naive 1-vertex and 2-vertex Hecke photon-projector e_i^(-) = (q - sigma_i)/[2]_q on 4_1
    two_qp = qbal(2, q_p)
    e1_proj = (q_p * i3 - a1_mat(q_p)) / two_qp
    e2_proj = (q_p * i3 - a2_mat(q_p)) / two_qp
    a2i_qp = a2_inv_mat(q_p)
    w41_qp = (a1_mat(q_p) * a2i_qp) * (a1_mat(q_p) * a2i_qp)
    y3_qp = (q_p**4 + mp.mpf(1)) / ((q_p**2 + mp.mpf(1)) ** 2)
    y21_qp = (q_p**2) / ((q_p**2 + mp.mpf(1)) ** 2)
    trm_41_qp = y3_qp + y21_qp * (tr3(w41_qp) - mp.mpf(1))

    hecke_1v = y21_qp * tr3(e1_proj * w41_qp) / trm_41_qp
    hecke_2v_same = (
        y21_qp * tr3(e1_proj * a1_mat(q_p) * a2i_qp * e1_proj * a1_mat(q_p) * a2i_qp) / trm_41_qp
    )
    hecke_2v_cross = (
        y21_qp * tr3(e1_proj * a1_mat(q_p) * e2_proj * a2i_qp * a1_mat(q_p) * a2i_qp) / trm_41_qp
    )
    comm_e1_s2i = e1_proj * a2i_qp - a2i_qp * e1_proj
    hecke_comm_sq = y21_qp * tr3((comm_e1_s2i * comm_e1_s2i) * w41_qp) / trm_41_qp

    # Evaluate full pin bundles at BOTH q_p and q_mu
    bundle_qp = evaluate_pin_bundle(q_p, vol41, mmu_me, sigma_mu_ppb, alpha_codata)
    bundle_qmu = evaluate_pin_bundle(q_mu, vol41, mmu_me, sigma_mu_ppb, alpha_codata)

    # Exact rational q = 3/2 algebraic sanity check for Stage B [Field K] theorems
    q_rat = mp.mpf(3) / mp.mpf(2)
    bundle_qrat = evaluate_pin_bundle(q_rat, vol41, mmu_me, sigma_mu_ppb, alpha_codata)

    print("=" * 78)
    print(" 80-dps Muon 4_1 / F_Bor Poincare / Seifert / Worldline QED Probe")
    print("=" * 78)
    print(f"  q_p (proton pin)          = {mp.nstr(q_p, 35)}")
    print(f"  q_mu (live muon pin)      = {mp.nstr(q_mu, 35)}")
    print(f"  bare overshoot at q_p     = +{mp.nstr(bare_overshoot_ppb, 8)} ppb  "
          f"(CODATA sigma = {mp.nstr(sigma_mu_ppb, 6)} ppb, entropy = {mp.nstr(entropy_fraction * 100, 4)}%)")
    print(f"  coupled re-pin Delta q_p  = {mp.nstr(shift_qp_coupled_ppb, 8)} ppb")
    print(f"  coupled m_mu/m_e residual = +{mp.nstr(resid_coupled_ppb, 8)} ppb  "
          f"(re-absorbed = {mp.nstr(reabsorbed_exact * 100, 5)}%)")
    print(f"  coupled Form-B 1/alpha    = {mp.nstr(shift_ainv_coupled_ppb, 8)} ppb shift")
    print(f"  proton ct3 (Q12p+Q23p)    = {mp.nstr(ct3_qadj_unproj_kev, 8)} keV vs needed "
          f"+{mp.nstr(needed_proton_kev_live_mu, 7)} keV (+{mp.nstr(needed_proton_kev_frozen_mu, 7)} keV frozen) "
          f"-> +{mp.nstr(mup_with_ct3_ppb, 6)} ppb")
    print(f"  4D WL QED |quad - sym|    = {mp.nstr(wl_abs_diff_30, 8)} at u = 1e-30")
    print(f"  naive O(w^1) 1-loop scale = +{bundle_qp['ow1_naive_1loop_ppb'][:10]} ppb")
    print(f"  UNWIRED Bring-Schwinger   = {bundle_qp['unwired_cand_bring_schwinger_2loop_ppb'][:10]} ppb "
          f"(post: +{bundle_qp['unwired_cand_bring_schwinger_post_resid_ppb'][:8]} ppb)")
    print(f"  UNWIRED double-commutator = {bundle_qp['unwired_cand_double_comm_1loop_ppb'][:10]} ppb "
          f"(post: +{bundle_qp['unwired_cand_double_comm_post_resid_ppb'][:8]} ppb)")

    wb = WitnessBuilder("muon-fbor-poincare-and-worldline-loop", engine="mpmath")
    wb.set_description(
        "80-dps working-assumption probe and algebraic verification for "
        "MuonFigureEightFBorPoincareIdentities.lean (qou-1ozb, qou-6gf9, qou-24w9, qou-gbsa): "
        "coupled-vs-uncoupled re-pinning theorem, Track 2/4 and 5-counterterm proton exclusions, "
        "4D worldline QED 1-loop self-energy asymptotic, and unwired bar-even candidates at q_p and q_mu."
    )

    wb.add_data(
        "codata_2022_inputs",
        {
            "proton_electron_mass_ratio": mp_entry.value_str,
            "proton_electron_mass_ratio_uncertainty": mp_entry.uncertainty_str,
            "muon_electron_mass_ratio": mmu_entry.value_str,
            "muon_electron_mass_ratio_uncertainty": mmu_entry.uncertainty_str,
            "inverse_fine_structure_constant": ainv_entry.value_str,
            "inverse_fine_structure_constant_uncertainty": ainv_entry.uncertainty_str,
            "electron_mass_keV": fmt(me_kev),
            "sigma_mu_ppb": fmt(sigma_mu_ppb),
            "sigma_alpha_inv_ppb": fmt(sigma_ainv_ppb),
            "entropy_sigma_over_residual_fraction": fmt(entropy_fraction),
            "significant_digits_on_residual": fmt(sig_digits_on_residual),
        },
    )
    wb.add_data(
        "coupled_repinning_theorem",
        {
            "delta_required": fmt(delta_req),
            "q_p_coupled": fmt(q_p_coupled),
            "shift_q_p_ppb": fmt(shift_qp_coupled_ppb),
            "post_coupled_mmu_resid_ppb": fmt(resid_coupled_ppb),
            "reabsorbed_fraction_exact": fmt(reabsorbed_exact),
            "reabsorbed_fraction_linear_slope_ratio": fmt(reabsorbed_linear_theorem),
            "shift_alpha_formB_inv_ppb": fmt(shift_ainv_coupled_ppb),
        },
    )
    wb.add_data(
        "exclusions_track2_track4_and_proton_counterterms",
        {
            "track2_murakami_h2011_real_u_4_1_torsion_ppb": track2_torsion_ppb,
            "track4_instantons_ppb": {
                "figure_eight_exp_neg_vol_over_hbar_q": fmt(inst_41_hbar_ppb),
                "figure_eight_exp_neg_vol_over_ln_q": fmt(inst_41_lnq_ppb),
                "figure_eight_exp_neg_2vol_over_h_q": fmt(inst_41_half_h_ppb),
                "figure_eight_saddle_prefactor_hbar_q": fmt(inst_41_with_2loop_prefactor_ppb),
                "sigma_235_exp_neg_pi2_over_60_hbar_q": fmt(inst_sigma235_hbar_ppb),
                "sigma_235_exp_neg_pi2_over_60_ln_q": fmt(inst_sigma235_lnq_ppb),
            },
            "five_canonical_proton_counterterms": {
                "needed_proton_shift_live_q_mu_keV": fmt(needed_proton_kev_live_mu),
                "needed_proton_shift_frozen_q_mu_keV": fmt(needed_proton_kev_frozen_mu),
                "ct1_static_all_pairs_QPairP_keV": fmt(ct1_qpair_kev),
                "ct2_diagonal_self_energy_QSelfP_trace_ratio": fmt(ct2_qself_trace_ratio),
                "ct3_adjacent_crossing_unprojected_keV": fmt(ct3_qadj_unproj_kev),
                "ct3_induced_mu_p_residual_ppb": fmt(mup_with_ct3_ppb),
                "ct4_e21_projected_adjacent_crossing_keV": fmt(ct4_qadj_e21_kev),
                "ct5_modulus_flipped_two_term_q_p_shift_ppb": fmt(shift_qp_ct5_two_term_ppb),
                "ct5_modulus_flipped_formB_alpha_inv_resid_ppb": fmt(ainv_two_term_resid_ppb),
            },
        },
    )
    wb.add_data(
        "worldline_qed_1loop_and_hecke_correlators",
        {
            "u_probe": fmt(u_probe),
            "worldline_coeff_quad": fmt(wl_quad_30),
            "worldline_coeff_symbolic": fmt(wl_sym_30),
            "worldline_quad_minus_symbolic_abs": fmt(wl_abs_diff_30),
            "single_clock_subtracted_finite_alpha_over_pi_coeff": fmt(wl_single_clock_finite_quad),
            "compton_clock_ue_eq_umu_cancellation_diff": fmt(wl_ratio_cancel_diff),
            "hecke_photon_projector_4_1_correlators_at_q_p": {
                "one_vertex_e1": fmt(hecke_1v),
                "two_vertex_e1_sep": fmt(hecke_2v_same),
                "two_vertex_e1_e2": fmt(hecke_2v_cross),
                "commutator_sq_e1_s2inv": fmt(hecke_comm_sq),
            },
            "unwired_working_assumption_status": (
                "STRICTLY UNWIRED WORKING ASSUMPTION: zero production rewire of m_mu/m_e; "
                "CODATA-2022 m_mu/m_e uncertainty (22.25 ppb) is ~10.5% of the 211.21 ppb "
                "residual (~1 significant digit), so coefficients must be derived from a "
                "complete 4D->1D worldline-braid reduction prior to wiring."
            ),
        },
    )
    wb.add_data(
        "pin_comparison_bundles",
        {
            "proton_pin": bundle_qp,
            "muon_pin": bundle_qmu,
            "exact_rational_3_over_2_check": bundle_qrat,
        },
    )

    wb.add_assertion(
        name="coupled_repinning_shifts_q_p_neg_10p12_ppb",
        computed=fmt(shift_qp_coupled_ppb),
        expected="-10.12460327",
        tolerance=mp.mpf("1e-6"),
        source="Coupled Borromean re-pinning 2 M_mu(q)(1 - delta_*) F_Bor(q) - 12 = m_p/m_e",
    )
    wb.add_assertion(
        name="coupled_repinning_leaves_mmu_at_pos_184p12_ppb",
        computed=fmt(resid_coupled_ppb),
        expected="184.1195717",
        tolerance=mp.mpf("1e-5"),
        source="87.18% of universal muon dressing re-absorbed into q_p via Borromean constituent",
    )
    wb.add_assertion(
        name="coupled_repinning_pulls_formB_alpha_inv_neg_69p19_ppb",
        computed=fmt(shift_ainv_coupled_ppb),
        expected="-69.18536117",
        tolerance=mp.mpf("1e-5"),
        source="Form-B 1/alpha_EM evaluated at coupled vs uncoupled proton pin",
    )
    wb.add_assertion(
        name="proton_static_all_pairs_QPairP_vanishes_exactly",
        computed=fmt(ct1_qpair_kev),
        expected="0",
        tolerance=mp.mpf("1e-75"),
        source="NucleonWeightSpaceTwoTerm.QPairP = 0 on proton (2,1) weight space",
    )
    wb.add_assertion(
        name="proton_adjacent_em_trace_has_opposite_sign_neg_0p53588_keV",
        computed=fmt(ct3_qadj_unproj_kev),
        expected="-0.5358796853",
        tolerance=mp.mpf("1e-7"),
        source="E_0(q_p)(1 - q_p^-1) tr((Q12p + Q23p) V_p^3) vs needed +0.22881 keV (+705.86 ppb)",
    )
    wb.add_assertion(
        name="worldline_qed_1loop_asymptotic_quad_vs_symbolic_lt_1e25",
        computed=fmt(wl_abs_diff_30),
        expected="0",
        tolerance=mp.mpf("1e-25"),
        source="4D Euclidean worldline QED 1-loop self-energy at u = 1e-30 vs (3/2)(ln(1/u)-gamma_E)+(1-3/2 ln 2)",
    )
    wb.add_assertion(
        name="worldline_single_clock_finite_part_is_5_over_4_alpha_over_pi",
        computed=fmt(wl_single_clock_finite_quad),
        expected=fmt(wl_single_clock_finite_exact),
        tolerance=mp.mpf("1e-70"),
        source="(1/2) int_0^1 -(1+y) ln(y^2) dy = 5/4",
    )
    wb.add_assertion(
        name="lean_group1_trm_41_and_t25_ratio_exact_at_q_p",
        computed=bundle_qp["trm_41_matrix_minus_closed_abs_err"],
        expected="0",
        tolerance=mp.mpf("1e-75"),
        source="y_3 + y_21 chi_21(4_1) = (q^5 + q^-5)/(q + q^-1)^3",
    )
    wb.add_assertion(
        name="lean_group2_fbor_poincare_s3_identity_exact_at_q_p",
        computed=bundle_qp["poincare_s3_abs_err"],
        expected="0",
        tolerance=mp.mpf("1e-75"),
        source="[3]_q! / q^3 = 1 + 2 q^-2 + 2 q^-4 + q^-6 = P_{S_3}(q^-2)",
    )
    wb.add_assertion(
        name="lean_group3_seifert_balanced_alexander_exact_at_q_p",
        computed=bundle_qp["seifert_alexander_abs_err"],
        expected="0",
        tolerance=mp.mpf("1e-75"),
        source="(t^2-t+1)(t^6-t^3+1) Phi_15(t)|_{t=q^-1} = q^-8 Delta_{T(2,9)}(q) Delta_{T(3,5)}(q)",
    )
    wb.add_assertion(
        name="lean_group3_kappa_seifert_reciprocal_exact_at_q_p",
        computed=bundle_qp["seifert_kappa_reciprocal_abs_err"],
        expected="0",
        tolerance=mp.mpf("1e-75"),
        source="kappa_Seifert(q) = q^8 / (Delta_{T(2,9)}(q) Delta_{T(3,5)}(q)) = 1.905155328...",
    )

    out_path = wb.save(
        q0_comparison(
            muon=fmt(q_mu),
            proton=fmt(q_p),
            reason=(
                "evaluates coupled-vs-uncoupled Borromean re-pinning, proton counterterms, "
                "and unwired bar-even worldline loop candidates across both registered pins "
                "(q_p proton pin and q_mu live muon pin) to adjudicate the mu-p offset"
            ),
            dps=80,
        )
    )
    all_passed = all(a.passed for a in wb.assertions)
    print(f"\n  Witness written -> {out_path} (assertions={len(wb.assertions)}, allPassed={all_passed})")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
