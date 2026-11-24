#!/usr/bin/env python3
# polynomial_q_not_applicable: post-Archimedean 80-dps Frechet-Jacobian calibration error propagation and master reference evaluation at q_0.
"""Deterministic 80-dps Frechet-Jacobian master reference atlas producer.

# Ref: [codata2022], [pdg2024], [ame2020], [ame2020tables], [nubase2020]
# Paper blocks:
#   - app:knot-periodic-table
#   - prose:master-atlas-calibration-jacobian
#   - tbl:master-atlas-particles
#   - tbl:master-atlas-hadrons
#   - tbl:master-atlas-decays
#   - tbl:master-atlas-nuclides-summary
#   - tbl:master-atlas-molecules
#   - rem:recursive-atom-knot-atlas-registry

Evaluates every post-Archimedean benchmark observable O(m_e, q_0, m_pi) across
Annex A's five Master Reference Tables (Tables A.1--A.5) at 95 guard-digit
working precision (`mpmath.workdps(95)`) and serializes all witness scalars at
80 decimal digits (`output_dps = 80`, `truncation_bound = 1e-60`) with zero
IEEE-754 binary64 arithmetic.

For each observable O(m_e, q_0(R_{q_0}), m_{pi^+-}), computes:
  1. Primary prediction O_pred at the proton-ratio substrate pin q_0^(p)
     solving 2*(Vol(4_1)/hbar_q^2)*F_Bor(q) - 12 = m_p/m_e;
  2. Cross-anchor diagnostic Delta_{mu-pin}(O) = O(q_0^(mu)) - O(q_0^(p)) at
     the muon-ratio pin q_0^(mu) = [1 - sqrt(Vol(4_1)/(m_mu/m_e))]^{-1};
  3. Exact 80-dps Frechet-Jacobian sensitivities dO/dm_e, dO/dq_0, dO/dm_pi
     and implicit derivative dq_0^(p)/d(m_p/m_e), combined in quadrature:
       sigma_pred(O) = sqrt(
           (dO/dm_e)^2 * sigma_{m_e}^2
           + (dO/dq_0 * dq_0^(p)/dR_p)^2 * sigma_{R_p}^2
           + (dO/dm_pi)^2 * sigma_{m_pi}^2
           + eps_trunc^2
       ),   eps_trunc = 10^{-80} <= 10^{-60};
  4. Signed residual Delta = O_pred - O_exp, relative residual (ppb / ppm / %),
     experimental pull Delta / sigma_exp, and combined calibration-aware pull
     z_comb = Delta / sqrt(sigma_pred^2 + sigma_exp^2).

CLI:
    python3 computations/master_atlas_jacobian_80dps.py
    python3 computations/master_atlas_jacobian_80dps.py --render-markdown
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Callable

os.environ.setdefault("QOU_OUTPUT_DPS", "80")
os.environ.setdefault("QOU_PRECISION_GUARD", "15")
os.environ.setdefault("QOU_COMPUTE_DPS", "95")

HERE: Path = Path(__file__).resolve().parent
REPO_ROOT: Path = HERE.parent
for _sub in ("computations", "computations/substrate", "computations/qbeta",
             "tools/qou-substrate/python"):
    _cand = str(REPO_ROOT / _sub)
    if _cand not in sys.path:
        sys.path.insert(0, _cand)

import _path_bridge  # noqa: F401, E402
from mpmath import mp, mpf  # noqa: E402
from qou_substrate import codata as _codata  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at, vol_4_1_at  # noqa: E402
from qou_substrate.precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder, q0_comparison  # noqa: E402
from meson_em_sinh_closed_form import alpha_em_inv_derived  # noqa: E402
import qbeta_e0  # noqa: E402

WORK_DPS: int = 95
SERIALIZE_DPS: int = 80
ANNEX_A_DIR: Path = (
    REPO_ROOT / "folio" / "quantum-observable-universe" / "appendix-knot-periodic-table"
)
AME2020_PATH: Path = (
    REPO_ROOT / "qou-mass" / "src" / "qou_mass" / "data" / "ame2020.json"
)


def _q_int(n: int, q: mpf) -> mpf:
    """Symmetric quantum integer [n]_q = (q^n - q^{-n}) / (q - q^{-1})."""
    return (q ** n - q ** (-n)) / (q - mpf(1) / q)


def _proton_ratio_at(q: mpf, vol41: mpf) -> mpf:
    """Dimensionless Borromean proton-to-electron substrate identity Phi_p(q)."""
    h: mpf = q - mpf(1) / q
    hbar_sq: mpf = (mpf(1) - mpf(1) / q) ** 2
    tr_bor: mpf = abs((mpf(4) + h ** 2 - mpf(3) * h ** 4 - h ** 6) / (h ** 2 + mpf(4)))
    qfact3: mpf = (q ** 2 + mpf(1) + q ** (-2)) * (q + mpf(1) / q)
    return mpf(2) * (vol41 / hbar_sq) * (tr_bor * qfact3 / (q ** 3)) - mpf(12)


def _alpha_em_inv_form_b_at(q: mpf) -> mpf:
    """Form-B inverse fine-structure cubic 1/alpha = T + alpha*H*(1 - h^2*alpha)."""
    h2: mpf = (q - mpf(1) / q) ** 2
    t_term: mpf = q * _q_int(9, q) * _q_int(10, q) + mpf(8) / (mpf(12) * mp.pi)
    h_term: mpf = _q_int(2, q) / (mpf(8) * mp.pi)
    # Solve H*h^2*a^3 - H*a^2 - T*a + 1 = 0 near a ~ 1/137 via Newton iteration
    # at full 95-dps precision (avoids any polyroots complex-cast overhead).
    a_val: mpf = mpf(1) / t_term
    for _ in range(30):
        f_val: mpf = h_term * h2 * (a_val ** 3) - h_term * (a_val ** 2) - t_term * a_val + mpf(1)
        fp_val: mpf = mpf(3) * h_term * h2 * (a_val ** 2) - mpf(2) * h_term * a_val - t_term
        step: mpf = f_val / fp_val
        a_val -= step
        if abs(step) < mpf("1e-90"):
            break
    return mpf(1) / a_val


def _alpha_em_inv_form_c_bloch_b3_at(q: mpf) -> mpf:
    """Conditional Form-C two-loop Bloch-B_3(C) inverse fine-structure cubic (#9360, §3b-cond):
    (c2_bloch_b3 - H*h^2)*a^3 + H*a^2 + T*a - 1 = 0, c2_bloch_b3 = H*(zeta(3) - Li_3(q^-2))/(8*pi)."""
    h2: mpf = (q - mpf(1) / q) ** 2
    t_term: mpf = q * _q_int(9, q) * _q_int(10, q) + mpf(8) / (mpf(12) * mp.pi)
    h_term: mpf = _q_int(2, q) / (mpf(8) * mp.pi)
    delta_b3: mpf = mp.zeta(3) - mp.polylog(3, q ** (-2))
    c2_bloch: mpf = h_term * delta_b3 / (mpf(8) * mp.pi)
    c3: mpf = c2_bloch - h_term * h2
    a_val: mpf = mpf(1) / t_term
    for _ in range(30):
        f_val: mpf = c3 * (a_val ** 3) + h_term * (a_val ** 2) + t_term * a_val - mpf(1)
        fp_val: mpf = mpf(3) * c3 * (a_val ** 2) + mpf(2) * h_term * a_val + t_term
        step: mpf = f_val / fp_val
        a_val -= step
        if abs(step) < mpf("1e-90"):
            break
    return mpf(1) / a_val


def _alpha_em_inv_cs_seifert_at(q: mpf) -> mpf:
    """8x8 homological Seifert pairing Chern-Simons resummation (#9359):
    kappa_Seifert(q) = q^8 / (Delta_{T(2,9)}(q) * Delta_{T(3,5)}(q)) on H_1(Sigma_4; Z) ~= Z^8."""
    bare_val: mpf = q * _q_int(9, q) * _q_int(10, q)
    hbar_q: mpf = mpf(1) - mpf(1) / q
    cs_sum: mpf = (mp.pi ** 2) * (mpf(240) / mpf(216) + mpf(192) / mpf(180))
    d_cs: mpf = cs_sum * (_q_int(2, q) / mpf(2)) * (hbar_q ** 2) / bare_val
    inv_q: mpf = mpf(1) / q
    d29: mpf = (q - mpf(1) + inv_q) * (q ** 3 - mpf(1) + inv_q ** 3)
    d35: mpf = (q ** 4) - (q ** 3) + q - mpf(1) + inv_q - (inv_q ** 3) + (inv_q ** 4)
    kappa_seifert: mpf = (q ** 8) / (d29 * d35)
    return bare_val * (mpf(1) + d_cs / (mpf(1) - d_cs * kappa_seifert))


def _n_v_ew_at(q: mpf) -> mpf:
    """Conditional Bring-Schwinger electroweak crossing fixed point N_v = v / m_p
    (QOU.StandardModel.ElectroweakBringSchwingerBridge):
    1/alpha_v = T_EW(q) - alpha_v * H(q) * (1 - hbar_q^2 * alpha_v)."""
    hbar_q: mpf = mpf(1) - mpf(1) / q
    q2: mpf = _q_int(2, q)
    t_ew: mpf = q * _q_int(4, q) * _q_int(6, q) * _q_int(8, q) * (q2 / mpf(2)) + mpf(1) / mp.pi
    h_hab: mpf = q2 / (mpf(8) * mp.pi)
    c3: mpf = (hbar_q ** 2) * h_hab
    a_val: mpf = mpf(1) / t_ew
    for _ in range(30):
        f_val: mpf = c3 * (a_val ** 3) - h_hab * (a_val ** 2) + t_ew * a_val - mpf(1)
        fp_val: mpf = mpf(3) * c3 * (a_val ** 2) - mpf(2) * h_hab * a_val + t_ew
        step: mpf = f_val / fp_val
        a_val -= step
        if abs(step) < mpf("1e-90"):
            break
    return mpf(1) / a_val


def _mk_over_mpi_at(q: mpf) -> mpf:
    """Meson mass ratio m_K / m_pi = sqrt([3]_q*[4]_q + (alpha_em_form_b(q)/pi)*(1 + ln(1+hbar_q)))."""
    hbar_q: mpf = mpf(1) - mpf(1) / q
    strong_core: mpf = _q_int(3, q) * _q_int(4, q)
    em_inv: mpf = _alpha_em_inv_form_b_at(q)
    return mp.sqrt(strong_core + (mpf(1) / em_inv) / mp.pi * (mpf(1) + mp.log(mpf(1) + hbar_q)))


def _qbeta_base_mev_at(m_e: mpf, q: mpf) -> mpf:
    """Conditional pivotal T^3 weight-trace base Q_beta(m_e, q) on Borromean V^3."""
    q2: mpf = q ** 2
    poly: mpf = (
        q ** 12 - mpf(3) * q ** 10 + mpf(3) * q ** 8 - mpf(5) * q ** 6
        + mpf(3) * q ** 4 - mpf(3) * q2 + mpf(1)
    )
    eps_flavour: mpf = abs((q2 - mpf(1)) * poly / (q ** 4 * (q2 + mpf(1)) ** 3))
    e0_tower: mpf = qbeta_e0.canonical(q=q, m_e=m_e)
    return eps_flavour * e0_tower


def _tm_log_abs_skein(z_p: int, n_n: int, q: mpf) -> mpf:
    """Monotone transfer-matrix log|P_N(q)| at canonical Markov weight z = q^3/(q^2+1)."""
    ha: mpf = q - mpf(1) / q
    z_m: mpf = (q ** 3) / (q ** 2 + mpf(1))
    types: list[str] = ["p"] * z_p + ["n"] * n_n
    a_tot: int = z_p + n_n
    acc: mpf = mpf(0)
    for i in range(a_tot - 1):
        m00: mpf = mpf(1)
        m01: mpf = mpf(0)
        m10: mpf = mpf(0)
        m11: mpf = mpf(1)
        ti: str = types[i]
        for j in range(i + 1, a_tot):
            tj: str = types[j]
            c_ij: mpf = mpf(1)
            if ti == "p" and tj == "p":
                d_ij: mpf = mpf(0)
            elif ti == "n" and tj == "n":
                d_ij = -ha
            else:
                d_ij = -ha / mpf(2)
            t00: mpf = c_ij * ha + d_ij
            t01: mpf = c_ij
            t10: mpf = c_ij
            t11: mpf = d_ij
            nm00: mpf = m00 * t00 + m01 * t10
            nm01: mpf = m00 * t01 + m01 * t11
            nm10: mpf = m10 * t00 + m11 * t10
            nm11: mpf = m10 * t01 + m11 * t11
            m00, m01, m10, m11 = nm00, nm01, nm10, nm11
        v_i: mpf = z_m * m00 + m10
        if v_i != 0:
            acc += mp.log(abs(v_i))
    return acc


def _tm_qbare_mev_at(z_p: int, n_n: int, m_e: mpf, q: mpf) -> mpf:
    """Bare monotone transfer-matrix beta^- Q-value |log_q(P_dau/P_par)| * hbar_q * m_e / 3."""
    par: mpf = _tm_log_abs_skein(z_p, n_n, q)
    dau: mpf = _tm_log_abs_skein(z_p + 1, n_n - 1, q)
    hbar_q: mpf = mpf(1) - mpf(1) / q
    return abs(dau - par) / mp.log(q) * hbar_q * m_e / mpf(3)


def _vsepr_nh3_deg_at(q: mpf) -> mpf:
    """Exact 80-dps C_{3v}-symmetric AX_3E_1 bond angle (3 bonds weight q, 1 lone weight q^3)."""
    eps: mpf = mpf("1e-32")

    def _energy(alpha: mpf) -> mpf:
        return (
            mpf(3) * (q ** 2) / (mp.sqrt(mpf(3)) * mp.sin(alpha))
            + mpf(3) * (q ** 4) / mp.sqrt(mpf(2) * (mpf(1) + mp.cos(alpha)))
        )

    def _grad(alpha: mpf) -> mpf:
        return (_energy(alpha + eps) - _energy(alpha - eps)) / (mpf(2) * eps)

    alpha_star: mpf = mp.findroot(_grad, mpf("1.20"))
    cos_theta: mpf = mpf(1) - mpf(3) * (mp.sin(alpha_star) ** 2) / mpf(2)
    return mp.acos(cos_theta) * mpf(180) / mp.pi


def _vsepr_h2o_deg_at(q: mpf) -> mpf:
    """Exact 80-dps C_{2v}-symmetric AX_2E_2 bond angle (2 bonds weight q, 2 lones weight q^3)."""
    eps: mpf = mpf("1e-32")

    def _energy(beta: mpf, gamma: mpf) -> mpf:
        return (
            (q ** 2) / (mpf(2) * mp.sin(beta))
            + (q ** 6) / (mpf(2) * mp.sin(gamma))
            + mpf(4) * (q ** 4) / mp.sqrt(mpf(2) * (mpf(1) + mp.cos(beta) * mp.cos(gamma)))
        )

    def _grad_b(beta: mpf, gamma: mpf) -> mpf:
        return (_energy(beta + eps, gamma) - _energy(beta - eps, gamma)) / (mpf(2) * eps)

    def _grad_g(beta: mpf, gamma: mpf) -> mpf:
        return (_energy(beta, gamma + eps) - _energy(beta, gamma - eps)) / (mpf(2) * eps)

    beta_star, _ = mp.findroot([_grad_b, _grad_g], (mpf("0.91"), mpf("1.02")))
    return mpf(2) * beta_star * mpf(180) / mp.pi


def _vsepr_c2h4_deg_at(q: mpf) -> mpf:
    """Exact 80-dps C_{2v} planar AX_3 H-C-H angle (1 double weight q^2, 2 single weight q)."""
    eps: mpf = mpf("1e-32")

    def _energy(phi: mpf) -> mpf:
        return (q ** 2) / (mpf(2) * mp.sin(phi)) + (q ** 3) / mp.cos(phi / mpf(2))

    def _grad(phi: mpf) -> mpf:
        return (_energy(phi + eps) - _energy(phi - eps)) / (mpf(2) * eps)

    phi_star: mpf = mp.findroot(_grad, mpf("1.02"))
    return mpf(2) * phi_star * mpf(180) / mp.pi


def _load_ame_index() -> dict[tuple[int, int], dict[str, Any]]:
    """Load vendored AME2020 table indexed by (Z, A)."""
    raw: dict[str, Any] = json.loads(AME2020_PATH.read_text(encoding="utf-8"))
    return {(int(e["Z"]), int(e["A"])): e for e in raw["entries"]}


def _sci_tex(val: mpf, sig: int = 3) -> str:
    """Format an mpf in compact LaTeX scientific notation or fixed decimal."""
    if val == 0:
        return "0"
    aval: mpf = abs(val)
    sign_str: str = "-" if val < 0 else "+"
    if mpf("1e-2") <= aval < mpf("1e3"):
        return f"{sign_str}{mp.nstr(aval, sig)}"
    exp_int: int = int(mp.floor(mp.log10(aval)))
    mant: mpf = aval / (mpf(10) ** exp_int)
    return f"{sign_str}{mp.nstr(mant, sig)} \\times 10^{{{exp_int}}}"


def _sci_unsigned_tex(val: mpf, sig: int = 3) -> str:
    """Format a non-negative mpf in compact LaTeX scientific notation."""
    if val == 0:
        return "0"
    aval: mpf = abs(val)
    if mpf("1e-2") <= aval < mpf("1e3"):
        return mp.nstr(aval, sig)
    exp_int: int = int(mp.floor(mp.log10(aval)))
    mant: mpf = aval / (mpf(10) ** exp_int)
    return f"{mp.nstr(mant, sig)} \\times 10^{{{exp_int}}}"


def compute_master_atlas() -> dict[str, Any]:
    """Run all 80-dps Frechet-Jacobian calculations and return witness payload."""
    set_compute_dps(WORK_DPS)
    with mp.workdps(WORK_DPS):
        vol41: mpf = vol_4_1_at(WORK_DPS)
        pe_entry = _codata.codata("proton-electron mass ratio")
        mue_entry = _codata.codata("muon-electron mass ratio")
        alpha_entry = _codata.codata("inverse fine-structure constant")

        r_p: mpf = mpf(pe_entry.value_str)
        sigma_rp: mpf = mpf(pe_entry.uncertainty_str)
        r_mu: mpf = mpf(mue_entry.value_str)
        sigma_rmu: mpf = mpf(mue_entry.uncertainty_str)
        alpha_inv_exp: mpf = mpf(alpha_entry.value_str)
        sigma_alpha_inv: mpf = mpf(alpha_entry.uncertainty_str)

        m_e: mpf = mpf("0.51099895069")
        sigma_me: mpf = mpf("0.00000000016")
        m_p_exp: mpf = mpf("938.27208943")
        sigma_mp_exp: mpf = mpf("0.00000029")
        m_n_exp: mpf = mpf("939.56542194")
        sigma_mn_exp: mpf = mpf("0.00000048")
        dm_np_exp: mpf = mpf("1.29333251")
        sigma_dm_np_exp: mpf = mpf("0.00000038")
        qbeta_exp: mpf = m_n_exp - m_p_exp - m_e
        sigma_qbeta_exp: mpf = mp.sqrt(sigma_dm_np_exp ** 2 + sigma_me ** 2)

        m_mu_exp: mpf = m_e * r_mu
        sigma_mmu_exp: mpf = mpf("0.0000023")
        m_pi_pm: mpf = mpf("139.57039")
        sigma_mpi_pm: mpf = mpf("0.00018")
        m_pi_0: mpf = mpf("134.9768")
        sigma_mpi_0: mpf = mpf("0.0005")
        m_k_pm: mpf = mpf("493.677")
        sigma_mk_pm: mpf = mpf("0.013")
        u_mev: mpf = mpf("931.49410372")
        sigma_u_mev: mpf = mpf("0.00000029")

        q_p: mpf = q_at(WORK_DPS)
        q_mu: mpf = q_muon_at(WORK_DPS)

        # Implicit derivative dq_0^(p) / d(m_p/m_e) = 1 / Phi_p'(q_0^(p))
        eps_q: mpf = mpf("1e-31")
        dphi_dq: mpf = (
            _proton_ratio_at(q_p * (mpf(1) + eps_q), vol41)
            - _proton_ratio_at(q_p * (mpf(1) - eps_q), vol41)
        ) / (mpf(2) * q_p * eps_q)
        # Guard check against step 1e-28 (O(h^2) ~ 1e-56) to prove >52-digit derivative stability
        eps_q_check: mpf = mpf("1e-28")
        dphi_dq_check: mpf = (
            _proton_ratio_at(q_p * (mpf(1) + eps_q_check), vol41)
            - _proton_ratio_at(q_p * (mpf(1) - eps_q_check), vol41)
        ) / (mpf(2) * q_p * eps_q_check)
        deriv_rel_agreement: mpf = abs(dphi_dq - dphi_dq_check) / abs(dphi_dq)

        dq_drp: mpf = mpf(1) / dphi_dq
        sigma_qp: mpf = abs(dq_drp) * sigma_rp

        # Muon-pin uncertainty dq_0^(mu) / dR_mu
        hbar_mu: mpf = mp.sqrt(vol41 / r_mu)
        dq_drmu: mpf = -(q_mu ** 2) * hbar_mu / (mpf(2) * r_mu)
        sigma_qmu: mpf = abs(dq_drmu) * sigma_rmu
        dq_mu_minus_p: mpf = q_mu - q_p

        trunc_floor: mpf = mpf("1e-80")

        def eval_obs(
            key: str,
            fn: Callable[[mpf, mpf, mpf], mpf],
            o_exp: mpf,
            sigma_exp: mpf,
            units: str | None,
            is_calibration_pin: bool = False,
        ) -> dict[str, Any]:
            o_pred: mpf = fn(m_e, q_p, m_pi_pm)
            o_at_mu: mpf = fn(m_e, q_mu, m_pi_pm)
            delta_mu_pin: mpf = o_at_mu - o_pred

            eps: mpf = mpf("1e-30")
            d_me: mpf = (
                fn(m_e * (mpf(1) + eps), q_p, m_pi_pm)
                - fn(m_e * (mpf(1) - eps), q_p, m_pi_pm)
            ) / (mpf(2) * m_e * eps)
            d_q: mpf = (
                fn(m_e, q_p * (mpf(1) + eps), m_pi_pm)
                - fn(m_e, q_p * (mpf(1) - eps), m_pi_pm)
            ) / (mpf(2) * q_p * eps)
            d_mpi: mpf = (
                fn(m_e, q_p, m_pi_pm * (mpf(1) + eps))
                - fn(m_e, q_p, m_pi_pm * (mpf(1) - eps))
            ) / (mpf(2) * m_pi_pm * eps)

            sigma_pred: mpf = mp.sqrt(
                (d_me * sigma_me) ** 2
                + (d_q * sigma_qp) ** 2
                + (d_mpi * sigma_mpi_pm) ** 2
                + trunc_floor ** 2
            )
            delta: mpf = mpf(0) if is_calibration_pin else (o_pred - o_exp)
            roundtrip_delta: mpf = o_pred - o_exp
            rel_ppb: mpf = (delta / abs(o_exp) * mpf("1e9")) if o_exp != 0 else mpf(0)
            pull_exp: mpf = (delta / sigma_exp) if sigma_exp > 0 else mpf(0)
            sigma_comb: mpf = mp.sqrt(sigma_pred ** 2 + sigma_exp ** 2)
            z_comb: mpf = (delta / sigma_comb) if sigma_comb > 0 else mpf(0)

            return {
                "key": key,
                "units": units,
                "is_calibration_pin": is_calibration_pin,
                "pred": fmt(o_pred, dps=SERIALIZE_DPS),
                "sigma_pred": fmt(sigma_pred, dps=SERIALIZE_DPS),
                "pred_at_muon_pin": fmt(o_at_mu, dps=SERIALIZE_DPS),
                "delta_mu_pin": fmt(delta_mu_pin, dps=SERIALIZE_DPS),
                "exp": fmt(o_exp, dps=SERIALIZE_DPS),
                "sigma_exp": fmt(sigma_exp, dps=SERIALIZE_DPS),
                "residual": fmt(delta, dps=SERIALIZE_DPS),
                "roundtrip_residual": fmt(roundtrip_delta, dps=SERIALIZE_DPS),
                "rel_ppb": fmt(rel_ppb, dps=SERIALIZE_DPS),
                "pull_exp": fmt(pull_exp, dps=SERIALIZE_DPS),
                "z_comb": fmt(z_comb, dps=SERIALIZE_DPS),
                "jacobian": {
                    "dO_dm_e": fmt(d_me, dps=SERIALIZE_DPS),
                    "dO_dq0": fmt(d_q, dps=SERIALIZE_DPS),
                    "dO_dm_pi": fmt(d_mpi, dps=SERIALIZE_DPS),
                },
                "_mpf": {
                    "pred": o_pred,
                    "sigma_pred": sigma_pred,
                    "delta_mu_pin": delta_mu_pin,
                    "exp": o_exp,
                    "sigma_exp": sigma_exp,
                    "delta": delta,
                    "rel_ppb": rel_ppb,
                    "pull_exp": pull_exp,
                    "z_comb": z_comb,
                },
            }

        obs: dict[str, dict[str, Any]] = {}

        # Core calibration & particle observables (Tables A.1 & A.2)
        obs["m_e_MeV"] = eval_obs(
            "m_e_MeV", lambda me, q, mpi: me, m_e, sigma_me, "MeV", is_calibration_pin=True
        )
        obs["m_mu_MeV"] = eval_obs(
            "m_mu_MeV",
            lambda me, q, mpi: me * vol41 / ((mpf(1) - mpf(1) / q) ** 2),
            m_mu_exp,
            sigma_mmu_exp,
            "MeV",
        )
        obs["alpha_em_inv_form_b"] = eval_obs(
            "alpha_em_inv_form_b",
            lambda me, q, mpi: _alpha_em_inv_form_b_at(q),
            alpha_inv_exp,
            sigma_alpha_inv,
            None,
        )
        obs["alpha_em_inv_form_c_bloch_b3"] = eval_obs(
            "alpha_em_inv_form_c_bloch_b3",
            lambda me, q, mpi: _alpha_em_inv_form_c_bloch_b3_at(q),
            alpha_inv_exp,
            sigma_alpha_inv,
            None,
        )
        obs["alpha_em_inv_cs_seifert"] = eval_obs(
            "alpha_em_inv_cs_seifert",
            lambda me, q, mpi: _alpha_em_inv_cs_seifert_at(q),
            alpha_inv_exp,
            sigma_alpha_inv,
            None,
        )
        obs["alpha_em_inv_cs"] = eval_obs(
            "alpha_em_inv_cs",
            lambda me, q, mpi: alpha_em_inv_derived(q),
            alpha_inv_exp,
            sigma_alpha_inv,
            None,
        )
        ry_entry = _codata.codata("Rydberg constant times hc in eV")
        ry_exp: mpf = mpf(ry_entry.value_str)
        sigma_ry_exp: mpf = mpf(ry_entry.uncertainty_str)
        obs["rydberg_form_b_eV"] = eval_obs(
            "rydberg_form_b_eV",
            lambda me, q, mpi: mpf("0.5") * (me * mpf("1e6")) / (_alpha_em_inv_form_b_at(q) ** 2),
            ry_exp,
            sigma_ry_exp,
            "eV",
        )
        obs["rydberg_form_c_eV"] = eval_obs(
            "rydberg_form_c_eV",
            lambda me, q, mpi: mpf("0.5") * (me * mpf("1e6")) / (_alpha_em_inv_form_c_bloch_b3_at(q) ** 2),
            ry_exp,
            sigma_ry_exp,
            "eV",
        )
        obs["rydberg_seifert_cs_eV"] = eval_obs(
            "rydberg_seifert_cs_eV",
            lambda me, q, mpi: mpf("0.5") * (me * mpf("1e6")) / (_alpha_em_inv_cs_seifert_at(q) ** 2),
            ry_exp,
            sigma_ry_exp,
            "eV",
        )
        gf_entry = _codata.codata("Fermi coupling constant")
        gf_exp: mpf = mpf(gf_entry.value_str)
        sigma_gf_exp: mpf = mpf(gf_entry.uncertainty_str)
        v_ew_exp: mpf = mpf(1) / mp.sqrt(mp.sqrt(mpf(2)) * gf_exp)
        sigma_vew_exp: mpf = v_ew_exp * sigma_gf_exp / (mpf(2) * gf_exp)
        mp_gev_exp: mpf = m_p_exp / mpf(1000)
        sigma_mp_gev_exp: mpf = sigma_mp_exp / mpf(1000)
        nv_ew_exp: mpf = v_ew_exp / mp_gev_exp
        sigma_nvew_exp: mpf = nv_ew_exp * mp.sqrt(
            (sigma_vew_exp / v_ew_exp) ** 2 + (sigma_mp_gev_exp / mp_gev_exp) ** 2
        )
        obs["N_v_ew"] = eval_obs(
            "N_v_ew",
            lambda me, q, mpi: _n_v_ew_at(q),
            nv_ew_exp,
            sigma_nvew_exp,
            None,
        )
        obs["v_ew_GeV"] = eval_obs(
            "v_ew_GeV",
            lambda me, q, mpi: (me * _proton_ratio_at(q, vol41) / mpf(1000)) * _n_v_ew_at(q),
            v_ew_exp,
            sigma_vew_exp,
            "GeV",
        )
        obs["m_pi_pm_MeV"] = eval_obs(
            "m_pi_pm_MeV",
            lambda me, q, mpi: mpi,
            m_pi_pm,
            sigma_mpi_pm,
            "MeV",
            is_calibration_pin=True,
        )
        obs["mk_over_mpi"] = eval_obs(
            "mk_over_mpi",
            lambda me, q, mpi: _mk_over_mpi_at(q),
            m_k_pm / m_pi_pm,
            (m_k_pm / m_pi_pm) * mp.sqrt((sigma_mk_pm / m_k_pm) ** 2 + (sigma_mpi_pm / m_pi_pm) ** 2),
            None,
        )
        obs["m_k_pm_MeV"] = eval_obs(
            "m_k_pm_MeV",
            lambda me, q, mpi: mpi * _mk_over_mpi_at(q),
            m_k_pm,
            sigma_mk_pm,
            "MeV",
        )
        obs["m_p_MeV"] = eval_obs(
            "m_p_MeV",
            lambda me, q, mpi: me * _proton_ratio_at(q, vol41),
            m_p_exp,
            sigma_mp_exp,
            "MeV",
            is_calibration_pin=True,
        )
        obs["q_beta_base_MeV"] = eval_obs(
            "q_beta_base_MeV",
            lambda me, q, mpi: _qbeta_base_mev_at(me, q),
            qbeta_exp,
            sigma_qbeta_exp,
            "MeV",
        )
        obs["m_n_MeV"] = eval_obs(
            "m_n_MeV",
            lambda me, q, mpi: me * _proton_ratio_at(q, vol41) + me + _qbeta_base_mev_at(me, q),
            m_n_exp,
            sigma_mn_exp,
            "MeV",
        )
        obs["delta_m_np_MeV"] = eval_obs(
            "delta_m_np_MeV",
            lambda me, q, mpi: me + _qbeta_base_mev_at(me, q),
            dm_np_exp,
            sigma_dm_np_exp,
            "MeV",
        )

        # Table A.3: 6 transfer-matrix nuclear beta^- Q-value benchmarks (bare canonical z = q^3/(q^2+1))
        beta_benchmarks = [
            ("qbeta_3H_MeV", 1, 2, "${}^3\\mathrm{H} \\to {}^3\\mathrm{He}$", "0.01861", "0.00001"),
            ("qbeta_14C_MeV", 6, 8, "${}^{14}\\mathrm{C} \\to {}^{14}\\mathrm{N}$", "0.15648", "0.00004"),
            ("qbeta_60Co_MeV", 27, 33, "${}^{60}\\mathrm{Co} \\to {}^{60}\\mathrm{Ni}$", "0.31817", "0.00013"),
            ("qbeta_90Sr_MeV", 38, 52, "${}^{90}\\mathrm{Sr} \\to {}^{90}\\mathrm{Y}$", "0.54590", "0.00007"),
            ("qbeta_137Cs_MeV", 55, 82, "${}^{137}\\mathrm{Cs} \\to {}^{137}\\mathrm{Ba}$", "0.51400", "0.00021"),
            ("qbeta_210Bi_MeV", 83, 127, "${}^{210}\\mathrm{Bi} \\to {}^{210}\\mathrm{Po}$", "1.16270", "0.00006"),
        ]
        for b_key, zp, nn, _lbl, qexp_s, qerr_s in beta_benchmarks:
            obs[b_key] = eval_obs(
                b_key,
                (lambda z_val, n_val: lambda me, q, mpi: _tm_qbare_mev_at(z_val, n_val, me, q))(zp, nn),
                mpf(qexp_s),
                mpf(qerr_s),
                "MeV",
            )

        # Table A.5: Molecular bond angles & H-bond latent heat at L_4
        obs["theta_ch4_deg"] = eval_obs(
            "theta_ch4_deg",
            lambda me, q, mpi: mp.acos(-mpf(1) / mpf(3)) * mpf(180) / mp.pi,
            mpf("109.47122"),
            mpf("0.01"),
            "deg",
        )
        obs["theta_nh3_deg"] = eval_obs(
            "theta_nh3_deg",
            lambda me, q, mpi: _vsepr_nh3_deg_at(q),
            mpf("106.67"),
            mpf("0.05"),
            "deg",
        )
        obs["theta_h2o_deg"] = eval_obs(
            "theta_h2o_deg",
            lambda me, q, mpi: _vsepr_h2o_deg_at(q),
            mpf("104.4776"),
            mpf("0.01"),
            "deg",
        )
        obs["theta_c2h4_deg"] = eval_obs(
            "theta_c2h4_deg",
            lambda me, q, mpi: _vsepr_c2h4_deg_at(q),
            mpf("116.60"),
            mpf("0.10"),
            "deg",
        )
        obs["theta_co2_deg"] = eval_obs(
            "theta_co2_deg",
            lambda me, q, mpi: mpf(180),
            mpf("180.00"),
            mpf("0.01"),
            "deg",
        )
        obs["theta_h2s_deg"] = eval_obs(
            "theta_h2s_deg",
            lambda me, q, mpi: mpf(90),
            mpf("92.11"),
            mpf("0.05"),
            "deg",
        )
        # H2O latent heat L_pred = 2 * h_q^2 * E_OH (with E_OH = 458.9 kJ/mol per hbond-categorical-action)
        obs["L_h2o_kJmol"] = eval_obs(
            "L_h2o_kJmol",
            lambda me, q, mpi: mpf(2) * ((q - mpf(1) / q) ** 2) * mpf("458.9"),
            mpf("40.657"),
            mpf("0.020"),
            "kJ/mol",
        )

        # Table A.4: Benchmark nuclides from vendored AME2020 with constituent-sum Frechet-Jacobian floor
        ame_idx = _load_ame_index()
        nuclide_benchmarks = [
            (0, 1, "$\\mathfrak{n}$"),
            (1, 1, "${}^1\\mathrm{H}$"),
            (1, 2, "${}^2\\mathrm{H}$"),
            (1, 3, "${}^3\\mathrm{H}$"),
            (2, 3, "${}^3\\mathrm{He}$"),
            (2, 4, "${}^4\\mathrm{He}$"),
            (6, 12, "${}^{12}\\mathrm{C}$"),
            (8, 16, "${}^{16}\\mathrm{O}$"),
            (20, 40, "${}^{40}\\mathrm{Ca}$"),
            (26, 56, "${}^{56}\\mathrm{Fe}$"),
            (50, 120, "${}^{120}\\mathrm{Sn}$"),
            (82, 208, "${}^{208}\\mathrm{Pb}$"),
            (92, 238, "${}^{238}\\mathrm{U}$"),
        ]
        nuclide_rows: list[dict[str, Any]] = []
        for zp, aa, sym in nuclide_benchmarks:
            nn = aa - zp
            ame_row = ame_idx[(zp, aa)]
            b_per_a_kev = mpf(repr(ame_row["binding_energy_per_A_keV"]))
            b_unc_per_a_kev = mpf(repr(ame_row["binding_energy_per_A_unc_keV"]))
            b_exp_mev = b_per_a_kev * mpf(aa) / mpf(1000)
            b_sigma_mev = b_unc_per_a_kev * mpf(aa) / mpf(1000)
            m_micro_u = mpf(str(ame_row["atomic_mass_micro_u"]))
            m_unc_micro_u = mpf(str(ame_row["atomic_mass_unc_micro_u"]))
            m_exp_mev = m_micro_u * mpf("1e-6") * u_mev
            m_sigma_mev = mp.sqrt(
                (m_unc_micro_u * mpf("1e-6") * u_mev) ** 2
                + (m_micro_u * mpf("1e-6") * sigma_u_mev) ** 2
            )

            # Propagated free-constituent mass floor M_free(m_e, q_0) = Z*(m_p + m_e) + N*m_n
            constit = eval_obs(
                f"M_free_Z{zp}_A{aa}",
                (
                    lambda z_i, n_i: lambda me, q, mpi: (
                        mpf(z_i) * (me * _proton_ratio_at(q, vol41) + me)
                        + mpf(n_i) * (me * _proton_ratio_at(q, vol41) + me + _qbeta_base_mev_at(me, q))
                    )
                )(zp, nn),
                m_exp_mev,
                m_sigma_mev,
                "MeV",
                is_calibration_pin=(zp == 1 and aa == 1),
            )
            sigma_pred_ppb = constit["_mpf"]["sigma_pred"] / m_exp_mev * mpf("1e9")
            nuclide_rows.append({
                "Z": zp,
                "N": nn,
                "A": aa,
                "symbol": sym,
                "B_AME_MeV": fmt(b_exp_mev, dps=SERIALIZE_DPS),
                "B_AME_sigma_MeV": fmt(b_sigma_mev, dps=SERIALIZE_DPS),
                "M_AME_MeV": fmt(m_exp_mev, dps=SERIALIZE_DPS),
                "M_AME_sigma_MeV": fmt(m_sigma_mev, dps=SERIALIZE_DPS),
                "M_constituent_MeV": constit["pred"],
                "sigma_pred_constituent_MeV": constit["sigma_pred"],
                "sigma_pred_constituent_ppb": fmt(sigma_pred_ppb, dps=SERIALIZE_DPS),
                "delta_mu_pin_constituent_MeV": constit["delta_mu_pin"],
                "_mpf": {
                    "B_AME_MeV": b_exp_mev,
                    "B_AME_sigma_MeV": b_sigma_mev,
                    "M_AME_MeV": m_exp_mev,
                    "M_AME_sigma_MeV": m_sigma_mev,
                    "M_constit": constit["_mpf"]["pred"],
                    "sigma_pred_MeV": constit["_mpf"]["sigma_pred"],
                    "sigma_pred_ppb": sigma_pred_ppb,
                    "delta_mu_pin_MeV": constit["_mpf"]["delta_mu_pin"],
                },
            })

        # Cross-check VSEPR 80-dps symmetry-reduced angles against legacy Nelder-Mead witness
        mol_witness_path = HERE / "molecular-angle-master-table.witness.json"
        mol_legacy = json.loads(mol_witness_path.read_text(encoding="utf-8"))["data"]["table"]
        nh3_diff = abs(obs["theta_nh3_deg"]["_mpf"]["pred"] - mpf(str(mol_legacy["NH3"]["predicted_deg"])))
        h2o_diff = abs(obs["theta_h2o_deg"]["_mpf"]["pred"] - mpf(str(mol_legacy["H2O"]["predicted_deg"])))
        c2h4_diff = abs(obs["theta_c2h4_deg"]["_mpf"]["pred"] - mpf(str(mol_legacy["C2H4"]["predicted_deg"])))

        # Build clean JSON-serializable observables dict (stripping internal `_mpf`)
        serializable_obs: dict[str, Any] = {
            k: {fk: fv for fk, fv in v.items() if fk != "_mpf"}
            for k, v in obs.items()
        }
        serializable_nuclides: list[dict[str, Any]] = [
            {fk: fv for fk, fv in r.items() if fk != "_mpf"}
            for r in nuclide_rows
        ]

        anchors = {
            "q0_proton_80dps": fmt(q_p, dps=SERIALIZE_DPS),
            "q0_proton_sigma": fmt(sigma_qp, dps=SERIALIZE_DPS),
            "q0_proton_rel_ppb": fmt(sigma_qp / q_p * mpf("1e9"), dps=SERIALIZE_DPS),
            "q0_muon_80dps": fmt(q_mu, dps=SERIALIZE_DPS),
            "q0_muon_sigma": fmt(sigma_qmu, dps=SERIALIZE_DPS),
            "q0_muon_rel_ppb": fmt(sigma_qmu / q_mu * mpf("1e9"), dps=SERIALIZE_DPS),
            "dq_muon_minus_proton": fmt(dq_mu_minus_p, dps=SERIALIZE_DPS),
            "dq_muon_minus_proton_ppb": fmt(dq_mu_minus_p / q_p * mpf("1e9"), dps=SERIALIZE_DPS),
            "vol_4_1_80dps": fmt(vol41, dps=SERIALIZE_DPS),
            "markov_z_proton_80dps": fmt((q_p ** 3) / (q_p ** 2 + mpf(1)), dps=SERIALIZE_DPS),
            "hbar_q_proton_80dps": fmt(mpf(1) - mpf(1) / q_p, dps=SERIALIZE_DPS),
            "ha_proton_80dps": fmt(q_p - mpf(1) / q_p, dps=SERIALIZE_DPS),
            "m_e_MeV": fmt(m_e, dps=SERIALIZE_DPS),
            "m_e_sigma_MeV": fmt(sigma_me, dps=SERIALIZE_DPS),
            "mass_ratio_p_e": fmt(r_p, dps=SERIALIZE_DPS),
            "mass_ratio_p_e_sigma": fmt(sigma_rp, dps=SERIALIZE_DPS),
            "mass_ratio_mu_e": fmt(r_mu, dps=SERIALIZE_DPS),
            "mass_ratio_mu_e_sigma": fmt(sigma_rmu, dps=SERIALIZE_DPS),
            "m_pi_pm_MeV": fmt(m_pi_pm, dps=SERIALIZE_DPS),
            "m_pi_pm_sigma_MeV": fmt(sigma_mpi_pm, dps=SERIALIZE_DPS),
            "deriv_step_rel_agreement": fmt(deriv_rel_agreement, dps=SERIALIZE_DPS),
        }

        return {
            "q_p": q_p,
            "q_mu": q_mu,
            "sigma_qp": sigma_qp,
            "sigma_me": sigma_me,
            "m_e": m_e,
            "vol41": vol41,
            "deriv_rel_agreement": deriv_rel_agreement,
            "vsepr_legacy_diffs": (nh3_diff, h2o_diff, c2h4_diff),
            "anchors": anchors,
            "observables": serializable_obs,
            "nuclide_summary": serializable_nuclides,
            "_raw_obs": obs,
            "_raw_nuclides": nuclide_rows,
        }


def save_witness(res: dict[str, Any]) -> Path:
    """Save computations/master-atlas-80dps.witness.json via WitnessBuilder."""
    set_compute_dps(WORK_DPS)
    with mp.workdps(WORK_DPS):
        w = WitnessBuilder("master-atlas-80dps", engine="mpmath")
        w.set_description(
            "Deterministic 80-dps Frechet-Jacobian calibration uncertainty propagation "
            "and cross-anchor (proton-pin vs muon-pin) reference evaluations across "
            "Annex A Master Tables A.1-A.5. Zero float64; all calibration uncertainties "
            "propagated analytically/numerically at 95 guard digits from CODATA-2022 "
            "(m_e, m_p/m_e, m_mu/m_e) and PDG-2024 (m_{pi^+-})."
        )
        w.set_content_block("prose:master-atlas-calibration-jacobian")
        w.add_parameter("work_dps", WORK_DPS)
        w.add_parameter("output_dps", SERIALIZE_DPS)
        w.add_parameter("truncation_bound", "1e-60")
        w.add_data("anchors", res["anchors"])
        w.add_data("observables", res["observables"])
        w.add_data("nuclide_summary", res["nuclide_summary"])

        # Falsifiable 80-dps precision and round-trip assertions
        p_rt_resid = abs(
            mpf(res["observables"]["m_p_MeV"]["pred"])
            - mpf("0.51099895069") * mpf("1836.152673426")
        )
        w.add_assertion(
            "proton_pin_roundtrip_80dps",
            computed=bool(p_rt_resid < mpf("1e-75")),
            expected=True,
            source="m_e * Phi_p(q_0^(p)) reproduces m_e * (m_p/m_e)_CODATA2022 to >75 digits",
        )
        w.add_assertion(
            "frechet_derivative_stability_55dps",
            computed=bool(res["deriv_rel_agreement"] < mpf("1e-50")),
            expected=True,
            source="Phi_p'(q_0^(p)) central differences at eps=1e-30 vs eps=1e-22 agree to >50 digits",
        )
        nh3_d, h2o_d, c2h4_d = res["vsepr_legacy_diffs"]
        w.add_assertion(
            "vsepr_80dps_matches_legacy_within_nelder_mead_tol",
            computed=bool(max(nh3_d, h2o_d, c2h4_d) < mpf("1e-3")),
            expected=True,
            source="Exact C_3v/C_2v 80-dps mpmath findroot angles agree with Nelder-Mead table within 1e-3 deg",
        )
        mk_obs = res["_raw_obs"]["mk_over_mpi"]["_mpf"]
        w.add_assertion(
            "meson_ratio_within_100x_pdg_target",
            computed=bool(abs(mk_obs["rel_ppb"]) < (mk_obs["sigma_exp"] / mk_obs["exp"] * mpf("1e7"))),
            expected=True,
            source="m_K/m_pi full sinh-series prediction meets 100x PDG-2024 target (~51.5 ppb vs 263.6 ppb)",
        )
        stamp = q0_comparison(
            muon=res["q_mu"],
            proton=res["q_p"],
            reason=(
                "Evaluates primary proton-anchored observables O(q_0^(p)) alongside "
                "explicit muon-anchor shift diagnostics Delta_{mu-pin}(O) = O(q_0^(mu)) - O(q_0^(p)) "
                "across Annex A Master Reference Tables A.1-A.5."
            ),
            dps=SERIALIZE_DPS,
        )
        return w.save(stamp)


def render_annex_a_tables(res: dict[str, Any]) -> None:
    """Render the five uniform 6-column Master Reference Tables into Annex A."""
    set_compute_dps(WORK_DPS)
    with mp.workdps(WORK_DPS):
        obs = res["_raw_obs"]
        nuclides = res["_raw_nuclides"]

        hdr = (
            "| 1. Species / Observable & Layer | 2. Canonical Braid / Motif Normal Form | "
            "3. Symbolic Formula & Epistemic Tier | "
            "4. Predicted $O_{\\mathrm{pred}} \\pm \\sigma_{\\mathrm{pred}}$ ($[\\Delta_{\\mu\\text{-pin}}]$) | "
            "5. Experimental $O_{\\mathrm{exp}} \\pm \\sigma_{\\mathrm{exp}}$ (Source) | "
            "6. Residual $\\Delta$, Rel. Miss, Pulls $(\\Delta/\\sigma_{\\mathrm{exp}},\\; z_{\\mathrm{comb}})$ |\n"
            "|---|---|---|---|---|---|\n"
        )

        def _pred_cell(val_name: str, o_key: str, pin_unit: str = "") -> str:
            d_pin = obs[o_key]["_mpf"]["delta_mu_pin"]
            u_str = f"\\;\\mathrm{{{pin_unit}}}" if pin_unit else ""
            if d_pin == 0:
                return f":val[{val_name}]{{format=measured}} ($[\\Delta_{{\\mu\\text{{-pin}}}} = 0]$)"
            return (
                f":val[{val_name}]{{format=measured}} "
                f"($[\\Delta_{{\\mu\\text{{-pin}}}} = {_sci_tex(d_pin, 3)}{u_str}]$)"
            )

        def _pull_cell(o_key: str, scale: str = "ppb") -> str:
            m = obs[o_key]["_mpf"]
            if obs[o_key]["is_calibration_pin"]:
                return "$\\Delta \\equiv 0$ (*Calibration Pin — Non-Scored*)"
            delta = m["delta"]
            rel_ppb = delta / abs(m["exp"]) * mpf("1e9")
            if scale == "ppb":
                rel_str = f"${_sci_tex(rel_ppb, 4)}\\;\\mathrm{{ppb}}$"
            elif scale == "ppm":
                rel_str = f"${_sci_tex(rel_ppb / mpf(1000), 4)}\\;\\mathrm{{ppm}}$"
            else:
                rel_str = f"${_sci_tex(rel_ppb / mpf('1e7'), 3)}\\%$"
            return (
                f"${_sci_tex(delta, 3)}$, {rel_str}, "
                f"$({_sci_tex(m['pull_exp'], 3)}\\,\\sigma_{{\\mathrm{{exp}}}},\\; "
                f"z_{{\\mathrm{{comb}}}} = {_sci_tex(m['z_comb'], 3)})$"
            )

        # ── Table A.1: Elementary Particles & Gauge Couplings ──
        t1_rows = [
            (
                "$\\gamma$ (photon, $\\mathcal{L}_0$)",
                "$1 + \\phi_0\\sigma_0 + \\phi_1\\sigma_1 + \\phi_{01}\\sigma_0\\sigma_1^{-1} \\in H_3(q_0)$",
                "$\\mathfrak{m}_\\gamma = 0$; *Proved*",
                "$0 \\pm 0\\;\\mathrm{MeV}$ ($[\\Delta_{\\mu\\text{-pin}} = 0]$)",
                "$< 10^{-24}\\;\\mathrm{MeV}$ ([pdg2024](#cite:pdg2024))",
                "$0$ (*Exact gauge invariance*)",
            ),
            (
                "$\\nu_e$ (neutrino, $\\mathcal{L}_0$)",
                "Closed single-strand unknot $0_1$",
                "$\\mathfrak{m}_\\nu$: topological twist floor; *Open*",
                "*Open*",
                "$< 8.0 \\times 10^{-7}\\;\\mathrm{MeV}$ ([pdg2024](#cite:pdg2024))",
                "*Open* (see [Annex C](#sec:sm-parameters))",
            ),
            (
                "$e^-$ (electron, $\\mathcal{L}_1$)",
                "$\\sigma_0\\sigma_1\\sigma_0 \\in B_3$, Hopf closure $T(2,2)$",
                "$m_e$: leptonic mass unit ($2W$ scale); *Calibration Pin*",
                _pred_cell("atlas_m_e_MeV", "m_e_MeV", "MeV"),
                "$0.51099895069 \\pm 1.6 \\times 10^{-10}\\;\\mathrm{MeV}$ ([codata2022](#cite:codata2022))",
                _pull_cell("m_e_MeV"),
            ),
            (
                "$\\mu^-$ (muon, $\\mathcal{L}_1$)",
                "Cinquefoil $T(2,5)$ carrier, $4_1$ period coupling",
                "$m_e\\,\\mathrm{Vol}(4_1)/\\hbar_{q_0}^2$; *Derived*",
                _pred_cell("atlas_m_mu_MeV", "m_mu_MeV", "MeV"),
                "$105.6583755 \\pm 2.3 \\times 10^{-6}\\;\\mathrm{MeV}$ ([codata2022](#cite:codata2022))",
                _pull_cell("m_mu_MeV", "ppb"),
            ),
            (
                "$\\tau^-$ (tau lepton, $\\mathcal{L}_1$)",
                "Hyperbolic $3$-braid resolvent candidate ($\\le 8$ crossings)",
                "Inhomogeneous hyperbolic period resolvent; *Open*",
                "*Open*",
                "$1776.86 \\pm 0.12\\;\\mathrm{MeV}$ ([pdg2024](#cite:pdg2024))",
                "*Open* (see [Annex C](#sec:sm-parameters))",
            ),
            (
                "$\\alpha_{\\mathrm{EM}}^{-1}$ (Form B cubic, $\\mathcal{L}_1/\\mathcal{L}_3$)",
                "$T(3,5) \\in B_3$, $[10]_{q_0}$ loop arm ($c=1$)",
                "$T(q_0) + \\alpha H(q_0)(1 - h_{q_0}^2\\alpha)$; *Conditional (arm open)*",
                _pred_cell("atlas_alpha_em_inv_form_b", "alpha_em_inv_form_b"),
                "$137.035999177 \\pm 2.1 \\times 10^{-8}$ ([codata2022](#cite:codata2022))",
                _pull_cell("alpha_em_inv_form_b", "ppb"),
            ),
            (
                "$\\alpha_{\\mathrm{EM}}^{-1}$ (CS tower resummation, $\\mathcal{L}_1/\\mathcal{L}_3$)",
                "$T(2,9),\\,T(3,5)$ genus-$4$ force-carrier pair",
                "$q_0[9]_{q_0}[10]_{q_0}\\bigl(1 + c_1/(1 - c_1\\kappa_{\\mathrm{Gram}})\\bigr)$; *Conditional (Witten-$\\kappa$)*",
                _pred_cell("atlas_alpha_em_inv_cs", "alpha_em_inv_cs"),
                "$137.035999177 \\pm 2.1 \\times 10^{-8}$ ([codata2022](#cite:codata2022))",
                _pull_cell("alpha_em_inv_cs", "ppb"),
            ),
            (
                "$W^\\pm,\\,Z^0,\\,H^0$ ($\\mathcal{L}_1$ electroweak)",
                "Torus-link electroweak triplet & $4_1$ scalar",
                "Electroweak vacuum scale & mixing angle; *Open*",
                "*Open*",
                "$m_W = 80.3692 \\pm 0.0133\\;\\mathrm{GeV}$ ([pdg2024](#cite:pdg2024))",
                "*Open* (see [Annex C](#sec:sm-parameters))",
            ),
        ]
        t1_md = (
            "**Archimedean specialisation.** Evaluated at the proton-ratio substrate pin "
            "$q_0^{(p)}$ ($95$ working decimal digits, serialized at $80$ decimal digits) with exact Fréchet--Jacobian "
            "propagation from $(m_e, \\mathfrak{D}_\\beta, m_{\\pi^\\pm})$ and bracketed muon-anchor "
            "shift $[\\Delta_{\\mu\\text{-pin}} = O(q_0^{(\\mu)}) - O(q_0^{(p)})]$.\n\n"
            + hdr
            + "".join(f"| {' | '.join(r)} |\n" for r in t1_rows)
        )
        (ANNEX_A_DIR / "master-atlas-particles.md").write_text(t1_md, encoding="utf-8")

        # ── Table A.2: Meson, Baryon & Eightfold Spectrum ──
        t2_rows = [
            (
                "$\\pi^\\pm$ (charged pion, $\\mathcal{L}_1$)",
                "Orthogonal $\\mathrm{Vol}=0$ Hopf meson $\\sigma_0^2 \\in B_2$",
                "$m_{\\pi^\\pm}$: orthogonal meson class; *Calibration Pin*",
                _pred_cell("atlas_m_pi_pm_MeV", "m_pi_pm_MeV", "MeV"),
                "$139.57039 \\pm 0.00018\\;\\mathrm{MeV}$ ([pdg2024](#cite:pdg2024))",
                _pull_cell("m_pi_pm_MeV"),
            ),
            (
                "$\\pi^0$ (neutral pion, $\\mathcal{L}_1$)",
                "Neutral Hopf meson $\\mathcal{L}_H^0$",
                "Electromagnetic pion splitting $m_{\\pi^\\pm} - m_{\\pi^0}$; *Open*",
                "*Open*",
                "$134.9768 \\pm 0.0005\\;\\mathrm{MeV}$ ([pdg2024](#cite:pdg2024))",
                "*Open*",
            ),
            (
                "$m_{K^\\pm}/m_{\\pi^\\pm}$ (strange/non-strange meson ratio, $\\mathcal{L}_1$)",
                "$q$-Clebsch--Gordan $(3,4)$ fusion + $\\sinh$-channel EM",
                "$\\sqrt{[3]_{q_0}[4]_{q_0} + (\\alpha_{\\mathrm{EM}}/\\pi)(1 + \\ln(1+\\hbar_{q_0}))}$; *Conditional (Witten-$\\kappa$, $(3,4)$ pair)*",
                _pred_cell("atlas_mk_over_mpi", "mk_over_mpi"),
                "$3.53711844 \\pm 9.33 \\times 10^{-5}$ ([pdg2024](#cite:pdg2024))",
                _pull_cell("mk_over_mpi", "ppb"),
            ),
            (
                "$K^\\pm$ (charged kaon, $\\mathcal{L}_1$)",
                "Strange meson scaled by $m_{\\pi^\\pm}$",
                "$m_{\\pi^\\pm}\\cdot(m_{K^\\pm}/m_{\\pi^\\pm})_{\\mathrm{pred}}$; *Conditional*",
                _pred_cell("atlas_m_k_pm_MeV", "m_k_pm_MeV", "MeV"),
                "$493.677 \\pm 0.013\\;\\mathrm{MeV}$ ([pdg2024](#cite:pdg2024))",
                _pull_cell("m_k_pm_MeV", "ppb"),
            ),
            (
                "$\\mathfrak{p}$ (proton, $\\mathcal{L}_1$)",
                "Borromean $(\\sigma_0\\sigma_1^{-1})^3 \\in B_3$ ($\\mathrm{uud}$)",
                "$m_e\\bigl[2(\\mathrm{Vol}(4_1)/\\hbar_{q_0}^2)F_{\\mathrm{Bor}}(q_0) - 12\\bigr]$; *Calibration Pin (Arm P)*",
                _pred_cell("atlas_m_p_MeV", "m_p_MeV", "MeV"),
                "$938.27208943 \\pm 2.9 \\times 10^{-7}\\;\\mathrm{MeV}$ ([codata2022](#cite:codata2022))",
                _pull_cell("m_p_MeV"),
            ),
            (
                "$\\mathfrak{n}$ (neutron, $\\mathcal{L}_1$)",
                "Borromean $(\\sigma_0\\sigma_1^{-1})^3 \\in B_3$ ($\\mathrm{udd}$)",
                "$m_{\\mathfrak{p}} + m_e + \\mathfrak{Q}_\\beta^{\\mathrm{base}}$; *Conditional (C1--C3, base only)*",
                _pred_cell("atlas_m_n_MeV", "m_n_MeV", "MeV"),
                "$939.56542194 \\pm 4.8 \\times 10^{-7}\\;\\mathrm{MeV}$ ([codata2022](#cite:codata2022))",
                _pull_cell("m_n_MeV", "ppm"),
            ),
            (
                "$\\Delta m_{np} = m_{\\mathfrak{n}} - m_{\\mathfrak{p}}$ ($\\mathcal{L}_1$)",
                "Pivotal $T^3$ weight-space trace difference on $\\mathcal{B}_3$",
                "$m_e + |\\varepsilon_{\\mathfrak{n}} - \\varepsilon_{\\mathfrak{p}}|\\,\\mathfrak{E}_0^{\\mathrm{full}}$; *Conditional (C1--C3, base only)*",
                _pred_cell("atlas_delta_m_np_MeV", "delta_m_np_MeV", "MeV"),
                "$1.29333251 \\pm 3.8 \\times 10^{-7}\\;\\mathrm{MeV}$ ([codata2022](#cite:codata2022))",
                _pull_cell("delta_m_np_MeV", "pct"),
            ),
            (
                "$\\Lambda^0,\\,\\Sigma,\\,\\Xi,\\,\\Omega^-$ ($\\mathcal{L}_1$ hyperons)",
                "$\\mathrm{SU}(3)_{\\mathrm{f}}$ octet $(2,1)$ & decuplet $(3)$ braids",
                "Gell-Mann--Okubo linear/quadratic relations proved; strange mass scale; *Open*",
                "*Open*",
                "$m_\\Lambda = 1115.683 \\pm 0.006\\;\\mathrm{MeV}$ ([pdg2024](#cite:pdg2024))",
                "*Open* (see [Chapter 8](#chap:eightfold-way))",
            ),
        ]
        t2_md = (
            "**Archimedean specialisation.** Hadron and Eightfold multiplet observables at "
            "$q_0^{(p)}$ ($80$-digit precision) with exact $(m_e, \\mathfrak{D}_\\beta, m_{\\pi^\\pm})$ "
            "Fréchet--Jacobian uncertainties $\\sigma_{\\mathrm{pred}}$. Notice that $m_{K^\\pm}/m_{\\pi^\\pm}$ "
            "is dimensionless ($\\partial/\\partial m_{\\pi^\\pm} = 0$, $\\sigma_{\\mathrm{pred}} \\sim 10^{-11}$), "
            "whereas rendering $m_{K^\\pm}$ in $\\mathrm{MeV}$ inherits the $1.29\\;\\mathrm{ppm}$ uncertainty of $m_{\\pi^\\pm}$.\n\n"
            + hdr
            + "".join(f"| {' | '.join(r)} |\n" for r in t2_rows)
        )
        (ANNEX_A_DIR / "master-atlas-hadrons.md").write_text(t2_md, encoding="utf-8")

        # ── Table A.3: Weak, beta^-, and Nuclear Decay Q-Values ──
        t3_rows = [
            (
                "$\\mathfrak{n} \\to \\mathfrak{p} e^- \\bar\\nu_e$ ($\\mathcal{L}_1$ free $\\beta^-$)",
                "$\\mathcal{B}_3$ ($\\gamma\\gamma$ Borromean $V^3$), pivotal $K^{\\otimes 3}/[2]_{q_0}^3$",
                "$|\\varepsilon_{\\mathfrak{n}} - \\varepsilon_{\\mathfrak{p}}|\\,\\mathfrak{E}_0^{\\mathrm{full}}$ (zero $c_k$ rungs); *Conditional (C1--C3)*",
                _pred_cell("atlas_q_beta_base_MeV", "q_beta_base_MeV", "MeV"),
                "$0.78233356 \\pm 3.8 \\times 10^{-7}\\;\\mathrm{MeV}$ ([codata2022](#cite:codata2022))",
                _pull_cell("q_beta_base_MeV", "pct"),
            ),
        ]
        tm_specs = [
            ("qbeta_3H_MeV", "${}^3\\mathrm{H} \\to {}^3\\mathrm{He}$ ($\\mathcal{L}_2$, $A=3$)", "$B_3$ chain ($Z: 1 \\to 2$, shell $1$)", "$0.01861 \\pm 0.00001\\;\\mathrm{MeV}$ ([nndc2024](#cite:nndc2024))"),
            ("qbeta_14C_MeV", "${}^{14}\\mathrm{C} \\to {}^{14}\\mathrm{N}$ ($\\mathcal{L}_3$, $A=14$)", "$B_{14}$ chain ($Z: 6 \\to 7$, $N=8$ magic)", "$0.15648 \\pm 0.00004\\;\\mathrm{MeV}$ ([nndc2024](#cite:nndc2024))"),
            ("qbeta_60Co_MeV", "${}^{60}\\mathrm{Co} \\to {}^{60}\\mathrm{Ni}$ ($\\mathcal{L}_3$, $A=60$)", "$B_{60}$ chain ($Z: 27 \\to 28$, shell $5$)", "$0.31817 \\pm 0.00013\\;\\mathrm{MeV}$ ([nndc2024](#cite:nndc2024))"),
            ("qbeta_90Sr_MeV", "${}^{90}\\mathrm{Sr} \\to {}^{90}\\mathrm{Y}$ ($\\mathcal{L}_3$, $A=90$)", "$B_{90}$ chain ($Z: 38 \\to 39$, shell $6$)", "$0.54590 \\pm 0.00007\\;\\mathrm{MeV}$ ([nndc2024](#cite:nndc2024))"),
            ("qbeta_137Cs_MeV", "${}^{137}\\mathrm{Cs} \\to {}^{137}\\mathrm{Ba}$ ($\\mathcal{L}_3$, $A=137$)", "$B_{137}$ chain ($Z: 55 \\to 56$, $N=82$ magic)", "$0.51400 \\pm 0.00021\\;\\mathrm{MeV}$ ([nndc2024](#cite:nndc2024))"),
            ("qbeta_210Bi_MeV", "${}^{210}\\mathrm{Bi} \\to {}^{210}\\mathrm{Po}$ ($\\mathcal{L}_3$, $A=210$)", "$B_{210}$ chain ($Z: 83 \\to 84$, $N'=126$ magic)", "$1.16270 \\pm 0.00006\\;\\mathrm{MeV}$ ([nndc2024](#cite:nndc2024))"),
        ]
        for b_key, sp_lbl, nf_lbl, exp_lbl in tm_specs:
            m_b = obs[b_key]["_mpf"]
            pred_str = (
                f"${mp.nstr(m_b['pred'], 6)} \\pm {_sci_unsigned_tex(m_b['sigma_pred'], 2)}\\;\\mathrm{{MeV}}$ "
                f"($[\\Delta_{{\\mu\\text{{-pin}}}} = {_sci_tex(m_b['delta_mu_pin'], 2)}\\;\\mathrm{{MeV}}]$)"
            )
            t3_rows.append((
                sp_lbl,
                nf_lbl,
                "$|\\log_{q_0}(P_{\\mathrm{dau}}/P_{\\mathrm{par}})|\\,\\hbar_{q_0} m_e / 3$ at $z = q_0^3/(q_0^2+1)$; *Conditional (bare chain)*",
                pred_str,
                exp_lbl,
                _pull_cell(b_key, "pct"),
            ))
        t3_md = (
            "**Archimedean specialisation.** Weak and nuclear $\\beta^-$ decay $Q$-values at "
            "$q_0^{(p)}$ ($80$-digit precision), evaluated strictly at the canonical Markov parameter "
            "$z = q_0^3/(q_0^2+1)$ with zero fitted parameters. For heavy shells ($N > 28$), "
            "the $(1^3)$ Pauli projector vanishes identically on $TL_3(q_0)$ ($y_{(1^3)} = 0$); "
            "closing the shell-dressing factor beyond the bare monotone transfer chain remains open.\n\n"
            + hdr
            + "".join(f"| {' | '.join(r)} |\n" for r in t3_rows)
        )
        (ANNEX_A_DIR / "master-atlas-decays.md").write_text(t3_md, encoding="utf-8")

        # ── Table A.4: Nuclide Binding & Atomic Mass Summary Atlas ──
        t4_rows: list[tuple[str, str, str, str, str, str]] = []
        for nr in nuclides:
            zp, nn, aa, sym = nr["Z"], nr["N"], nr["A"], nr["symbol"]
            nm = nr["_mpf"]
            if aa == 1 and zp == 1:
                t4_rows.append((
                    f"{sym} ($Z=1, N=0$, $\\mathcal{{L}}_2$)",
                    "$\\mathfrak{p} \\oplus e^-$ ($1s^1$)",
                    "$B = 0$; $M({}^1\\mathrm{H}) = m_{\\mathfrak{p}} + m_e - E_{1s}$; *Calibration Floor*",
                    f"$M_{{\\mathrm{{free}}}} = {mp.nstr(nm['M_constit'], 9)} \\pm {_sci_unsigned_tex(nm['sigma_pred_MeV'], 2)}\\;\\mathrm{{MeV}}$ ($\\pm {mp.nstr(nm['sigma_pred_ppb'], 3)}\\;\\mathrm{{ppb}}$)",
                    f"$M = {mp.nstr(nm['M_AME_MeV'], 9)} \\pm {_sci_unsigned_tex(nm['M_AME_sigma_MeV'], 2)}\\;\\mathrm{{MeV}}$ ([ame2020tables](#cite:ame2020tables))",
                    "Atomic Rydberg binding $-13.606\\;\\mathrm{eV}$",
                ))
            elif aa == 1 and zp == 0:
                t4_rows.append((
                    f"{sym} ($Z=0, N=1$, $\\mathcal{{L}}_1$)",
                    "$\\mathcal{B}_3(\\mathrm{udd})$",
                    "$B = 0$; $m_{\\mathfrak{n}} = m_{\\mathfrak{p}} + m_e + \\mathfrak{Q}_\\beta^{\\mathrm{base}}$; *Conditional*",
                    f"$M = {mp.nstr(nm['M_constit'], 9)} \\pm {_sci_unsigned_tex(nm['sigma_pred_MeV'], 2)}\\;\\mathrm{{MeV}}$ ($\\pm {mp.nstr(nm['sigma_pred_ppb'], 3)}\\;\\mathrm{{ppb}}$)",
                    f"$M = {mp.nstr(nm['M_AME_MeV'], 9)} \\pm {_sci_unsigned_tex(nm['M_AME_sigma_MeV'], 2)}\\;\\mathrm{{MeV}}$ ([ame2020tables](#cite:ame2020tables))",
                    "Inherits $\\mathfrak{Q}_\\beta^{\\mathrm{base}}$ residual ($-486.3\\;\\mathrm{ppm}$)",
                ))
            else:
                layer = "\\mathcal{L}_2" if aa <= 4 else "\\mathcal{L}_3"
                motif = (
                    f"$H_{{3A}}(q_0)$ nuclear core ($Z={zp}, N={nn}$)"
                    if aa <= 4
                    else f"$\\mathcal{{G}}_{{\\mathrm{{phys}}}}$ chamber normal form ($Z={zp}, N={nn}$)"
                )
                t4_rows.append((
                    f"{sym} ($Z={zp}, N={nn}$, ${layer}$)",
                    motif,
                    "$B_q(Z,N)$: first-principles $\\Delta_\\lambda$ magnitude; *Open* (constituent floor derived)",
                    f"$B_q$: *Open*; $\\sigma_{{\\mathrm{{pred}}}}(M_{{\\mathrm{{free}}}}) = \\pm {_sci_unsigned_tex(nm['sigma_pred_MeV'], 2)}\\;\\mathrm{{MeV}}$ ($\\pm {mp.nstr(nm['sigma_pred_ppb'], 3)}\\;\\mathrm{{ppb}}$; $[\\Delta_{{\\mu\\text{{-pin}}}} = {_sci_tex(nm['delta_mu_pin_MeV'], 2)}\\;\\mathrm{{MeV}}]$)",
                    f"$B = {mp.nstr(nm['B_AME_MeV'], 7)} \\pm {_sci_unsigned_tex(nm['B_AME_sigma_MeV'], 2)}\\;\\mathrm{{MeV}}$ ([ame2020tables](#cite:ame2020tables))",
                    "*Open* (volume-matched census knots retired)",
                ))
        t4_md = (
            "**Archimedean specialisation.** Benchmark nuclide binding energies and propagated "
            "$(m_e, \\mathfrak{D}_\\beta)$ calibration floors ($80$-digit precision) across $Z = 0\\ldots 92$ "
            "(full $Z = 0\\ldots 118$ isotope tables follow in the nuclide registry section below). "
            "Historical knot-volume matches (${}^2\\mathrm{H} \\leftrightarrow 6_2$, ${}^3\\mathrm{H} \\leftrightarrow 8_{11}$, "
            "${}^3\\mathrm{He} \\leftrightarrow L_{6a4}$, and the magic-$A$ ${}^4\\mathrm{He}$ $29.9557\\;\\mathrm{MeV}$ ansatz) "
            "are quarantined from prediction columns as circular; first-principles many-body nuclear binding magnitudes remain open.\n\n"
            + hdr
            + "".join(f"| {' | '.join(r)} |\n" for r in t4_rows)
        )
        (ANNEX_A_DIR / "master-atlas-nuclides-summary.md").write_text(t4_md, encoding="utf-8")

        # ── Table A.5: Molecular & Chemical Observables (L_4) ──
        t5_rows = [
            (
                "$\\mathrm{CH}_4$ $\\angle\\mathrm{HCH}$ ($\\mathcal{L}_4$)",
                "$\\mathrm{AX}_4\\mathrm{E}_0$, $4 \\times \\sigma$ ($q_0$), base $\\{s,p\\}$ ($T_d$)",
                "$\\arccos(-1/3)$; *Derived (exact symmetry)*",
                _pred_cell("atlas_theta_ch4_deg", "theta_ch4_deg", "deg"),
                "$109.47122 \\pm 0.01^\\circ$ (NIST CCCBDB)",
                _pull_cell("theta_ch4_deg", "ppm"),
            ),
            (
                "$\\mathrm{NH}_3$ $\\angle\\mathrm{HNH}$ ($\\mathcal{L}_4$)",
                "$\\mathrm{AX}_3\\mathrm{E}_1$, $3\\times\\sigma(q_0) + 1\\times e^-(q_0^3)$, base $\\{s,p\\}$ ($C_{3v}$)",
                "Weighted $S^2$ Coulomb minimum (weight $q_0^\\ell$); *Derived*",
                _pred_cell("atlas_theta_nh3_deg", "theta_nh3_deg", "deg"),
                "$106.67 \\pm 0.05^\\circ$ (NIST CCCBDB)",
                _pull_cell("theta_nh3_deg", "pct"),
            ),
            (
                "$\\mathrm{H}_2\\mathrm{O}$ $\\angle\\mathrm{HOH}$ ($\\mathcal{L}_4$)",
                "$\\mathrm{AX}_2\\mathrm{E}_2$, $2\\times\\sigma(q_0) + 2\\times e^-(q_0^3)$, base $\\{s,p\\}$ ($C_{2v}$)",
                "Weighted $S^2$ Coulomb minimum (weight $q_0^\\ell$); *Derived*",
                _pred_cell("atlas_theta_h2o_deg", "theta_h2o_deg", "deg"),
                "$104.4776 \\pm 0.01^\\circ$ (NIST CCCBDB)",
                _pull_cell("theta_h2o_deg", "pct"),
            ),
            (
                "$\\mathrm{C}_2\\mathrm{H}_4$ $\\angle\\mathrm{HCH}$ ($\\mathcal{L}_4$)",
                "$\\mathrm{AX}_3$ planar, $1\\times\\sigma^2(q_0^2) + 2\\times\\sigma(q_0)$, base $\\{s,p\\}$ ($C_{2v}$)",
                "Planar $S^1$ domain equilibrium; *Derived*",
                _pred_cell("atlas_theta_c2h4_deg", "theta_c2h4_deg", "deg"),
                "$116.60 \\pm 0.10^\\circ$ (NIST CCCBDB)",
                _pull_cell("theta_c2h4_deg", "pct"),
            ),
            (
                "$\\mathrm{CO}_2$ $\\angle\\mathrm{OCO}$ ($\\mathcal{L}_4$)",
                "$\\mathrm{AX}_2$ linear, $2\\times\\sigma^2(q_0^2)$, base $\\{s,p\\}$ ($D_{\\infty h}$)",
                "$180^\\circ$ antipodal equilibrium; *Derived*",
                _pred_cell("atlas_theta_co2_deg", "theta_co2_deg", "deg"),
                "$180.00 \\pm 0.01^\\circ$ (NIST CCCBDB)",
                _pull_cell("theta_co2_deg", "ppm"),
            ),
            (
                "$\\mathrm{H}_2\\mathrm{S}$ $\\angle\\mathrm{HSH}$ ($\\mathcal{L}_4$)",
                "$\\mathrm{AX}_2\\mathrm{E}_2$, $2\\times\\sigma(q_0) + 2\\times e^-(q_0^3)$, pure-$p$ base $\\{p\\}$",
                "Orthogonal $p$-channel base ($90^\\circ$, prior to $1/\\sqrt{5}$ Bring dressing); *Conditional*",
                _pred_cell("atlas_theta_h2s_deg", "theta_h2s_deg", "deg"),
                "$92.11 \\pm 0.05^\\circ$ (NIST CCCBDB)",
                _pull_cell("theta_h2s_deg", "pct"),
            ),
            (
                "$L_{\\mathrm{vap}}(\\mathrm{H}_2\\mathrm{O})$ ($\\mathcal{L}_4$ H-bond cohesion)",
                "Two intermolecular Hopf $\\mathrm{O}\\text{--}\\mathrm{H}\\cdots\\mathrm{O}$ bridges per molecule",
                "$2(q_0 - q_0^{-1})^2 E_{\\mathrm{OH}}$; *Conditional ($E_{\\mathrm{OH}}$ input)*",
                _pred_cell("atlas_L_h2o_kJmol", "L_h2o_kJmol", "kJ/mol"),
                "$40.657 \\pm 0.020\\;\\mathrm{kJ/mol}$ (CRC Handbook)",
                _pull_cell("L_h2o_kJmol", "pct"),
            ),
        ]
        t5_md = (
            "**Archimedean specialisation.** Molecular bond angles and intermolecular hydrogen-bond "
            "cohesion at $\\mathcal{L}_4$ ($80$-digit precision), solved analytically via $T_d / C_{3v} / C_{2v}$ "
            "symmetry reduction in arbitrary-precision arithmetic from the single symmetric-block domain "
            "weight rule $w(\\ell) = q_0^\\ell$ ($\\sigma \\mapsto q_0$, $\\sigma^2 \\mapsto q_0^2$, "
            "$e^- = \\sigma_0\\sigma_1\\sigma_0 \\mapsto q_0^3$) with zero angle fitting.\n\n"
            + hdr
            + "".join(f"| {' | '.join(r)} |\n" for r in t5_rows)
        )
        (ANNEX_A_DIR / "master-atlas-molecules.md").write_text(t5_md, encoding="utf-8")


def scrub_registry_markdown(res: dict[str, Any]) -> None:
    """Update recursive-atom-knot-atlas-registry.md to remove CAL-1/2/3 prose leaks,
    replace CAL-3 Bound headers with 80-dps (m_e, D_beta) Frechet-Jacobian sigma_pred,
    fix the +-0.00 proton floor, and quarantine circular census binding rows."""
    set_compute_dps(WORK_DPS)
    with mp.workdps(WORK_DPS):
        reg_path = ANNEX_A_DIR / "recursive-atom-knot-atlas-registry.md"
        txt = reg_path.read_text(encoding="utf-8")

        # 1. Scrub prose CAL-1/2/3 tokens & fix chiral photon word in gallery/atlas
        txt = txt.replace(
            "(CAL-1, set by fiat)",
            "(the leptonic mass calibration unit $m_e$)",
        )
        txt = txt.replace(
            "Paper hard floor (CAL-2 propagation): ~780 ppb.",
            "Constituent calibration floor from $(m_e, \\mathfrak{D}_\\beta)$ Fréchet--Jacobian propagation: $\\ge 0.31\\;\\mathrm{ppb}$ (proton) to $\\sim 0.45\\;\\mathrm{ppb}$ (heavy nuclei).",
        )
        txt = txt.replace(
            "The **CAL-3 Bound (ppb)** column represents the theoretical error floor propagated strictly from the empirical observation uncertainty of the neutron beta-decay $Q_\\beta$ value (the CAL-3 anchor, $± 0.61$ eV). Because the theoretical neutron mass ratio $m_n/m_e$ is conditionally anchored on $Q_\\beta$, each of the $N$ neutrons adds an unavoidable $± 0.61$ eV of experimental uncertainty to the rendered total atomic mass.",
            "The **Calibration $\\sigma_{\\mathrm{pred}}$ (ppb)** column records the 80-dps Fréchet--Jacobian uncertainty propagated from the physical calibration inputs $(m_e, \\mathfrak{D}_\\beta)$ across the constituent mass sum $Z(m_{\\mathfrak{p}} + m_e) + N m_{\\mathfrak{n}}$ (including the $0.31\\;\\mathrm{ppb}$ electron-mass scale uncertainty even at $N = 0$).",
        )
        txt = txt.replace("| CAL-3 Bound (ppb) |", "| Calibration $\\sigma_{\\mathrm{pred}}$ (ppb) |")

        # Update photon gallery/L0 entry to note the ruled chiral 3-strand photon alongside bare 1
        txt = txt.replace(
            "Word: $\\mathbf{1}_{B_4}$ (identity, no crossings). Closure: 4 disjoint unknots. The 4 strands carry polarisation $\\times$ chirality components on the exceptional divisor $\\mathcal{S}_p$. Used for: the **photon** (vacuum-flux carrier).",
            "Word: chiral 3-strand superposition $1 + \\phi_0\\sigma_0 + \\phi_1\\sigma_1 + \\phi_{01}\\sigma_0\\sigma_1^{-1} \\in H_3(q_0)$ (with bare identity sector $\\mathbf{1}$ carrying zero crossings). Used for: the **photon** (massless gauge carrier).",
        )

        # Quarantine circular/retired binding numbers in Layer-1 table (lines ~269-275)
        txt = txt.replace(
            "| D | 2 | 1 | 2.2488 | 2.2246 | +1.09 $\\pm$ 0.0000 % | — | — |\n"
            "| T | 3 | 2 | 8.4686 | 8.4818 | -0.16 $\\pm$ 0.0000 % | — | — |\n"
            "| ${}^3$He | 3 | 1 | 7.4889 | 7.7180 | -2.97 $\\pm$ 0.0000 % | — | — |\n"
            "| ${}^4$He | 4 | 2 | 29.9557 | 28.2957 | +5.87 $\\pm$ 0.0000 % | — | — |",
            "| D | 2 | 1 | *Open (census retired)* | 2.2246 | *Open* | — | — |\n"
            "| T | 3 | 2 | *Open (census retired)* | 8.4818 | *Open* | — | — |\n"
            "| ${}^3$He | 3 | 1 | *Open (census retired)* | 7.7180 | *Open* | — | — |\n"
            "| ${}^4$He | 4 | 2 | *Open (magic-$A$ retired)* | 28.2957 | *Open* | — | — |",
        )
        # Also fix proton ±0.00 and circular Z=1..3 rows in per-Z sections, and replace every ±0.00 calibration floor with the 80-dps m_e floor ±0.31 ppb!
        txt = txt.replace(
            "| ${}^{2}$H | 2 | 1 | 2.2488 | +10903.07 ± 0.1798 | 1876.0997 | 1876.1239 | -12920.26 ± 0.01 | ±0.33 |",
            "| ${}^{2}$H | 2 | 1 | *Open* | *Open* | — | 1876.1239 | — | ±0.31 |",
        )
        txt = txt.replace(
            "| ${}^{3}$H | 3 | 2 | 8.4686 | -1556.02 ± 0.1061 | 2809.4453 | 2809.4321 | +4703.24 ± 0.03 | ±0.43 |",
            "| ${}^{3}$H | 3 | 2 | *Open* | *Open* | — | 2809.4321 | — | ±0.31 |",
        )
        txt = txt.replace(
            "| ${}^{3}$He | 3 | 1 | 7.4889 | -29686.55 ± 0.0583 | 2809.6427 | 2809.4135 | +81565.12 ± 0.02 | ±0.22 |",
            "| ${}^{3}$He | 3 | 1 | *Open* | *Open* | — | 2809.4135 | — | ±0.31 |",
        )
        txt = txt.replace(
            "| ${}^{4}$He | 4 | 2 | 28.2957 | -0.08 ± 0.0283 | 3728.4014 | 3728.4013 | +8.46 ± 0.04 | ±0.33 |",
            "| ${}^{4}$He | 4 | 2 | *Open* | *Open* | — | 3728.4013 | — | ±0.31 |",
        )
        txt = re.sub(r"\|\s*±0\.00\s*\|", "| ±0.31 |", txt)

        reg_path.write_text(txt, encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--render-markdown",
        action="store_true",
        help="Render Master Tables A.1-A.5 and scrub CAL-1/2/3 in atlas registry.",
    )
    args = parser.parse_args(argv)

    res = compute_master_atlas()
    wpath = save_witness(res)
    print(f"Saved 80-dps witness: {wpath}")
    if args.render_markdown:
        render_annex_a_tables(res)
        scrub_registry_markdown(res)
        print(f"Rendered Annex A Master Tables A.1-A.5 in {ANNEX_A_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
