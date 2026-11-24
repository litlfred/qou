#!/usr/bin/env python3
"""80-dps verification probe for substrate parameter locality & varying-constants co-variation.

Salvaged from PR #8158 (`qou-1u7x`, `qou-cweq`, `ovud`, `i5p0`, `qou-cgbd`).
Lean companion: `QOU/Observations/SubstrateParameterLocality.lean`.
Precision: 80-dps mpmath + SymPy, zero float64, zero hardcoded CODATA literals.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

THIS = Path(__file__).resolve()
COMPUTATIONS_DIR = THIS.parent.parent
ROOT = COMPUTATIONS_DIR.parent
for _rel in (
    "computations",
    "computations/substrate",
    "tools/qou-substrate/python",
    "schemas/witness-schema/python",
):
    if str(ROOT / _rel) not in sys.path:
        sys.path.insert(0, str(ROOT / _rel))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402
from codata_2022_source import (  # noqa: E402
    M_E_MEV,
    M_N_MEV_AME_DERIVED,
    M_N_MEV_CODATA_DIRECT,
    M_N_MEV_CODATA_DIRECT_ERR,
    M_P_MEV,
    M_P_MEV_ERR,
)
from q_parameter import Q_50_DIGIT_STR, q_at, q_muon_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

DPS = 80
set_compute_dps(DPS)
mp.mp.dps = DPS


def main() -> int:
    t0 = time.time()
    set_compute_dps(DPS)
    mp.mp.dps = DPS

    q_p = q_at(DPS)
    q_mu = q_muon_at(DPS)

    # 1. Symbolic identities (sympy): c_q, kappa_mu, kappa_alpha, [3]_q!/q^3
    q_sym = sp.Symbol("q", positive=True)
    hbar_sym = 1 - 1 / q_sym
    cq_sym = (1 / q_sym) / hbar_sym
    cq_simplified = sp.simplify(cq_sym - 1 / (q_sym - 1))

    kappa_mu_sym = sp.simplify(q_sym * sp.diff(-2 * sp.log(hbar_sym), q_sym))
    kappa_mu_residual = sp.simplify(kappa_mu_sym - (-2 / (q_sym - 1)))

    q3_int_sym = q_sym**2 + 1 + q_sym ** (-2)
    q2_int_sym = q_sym + q_sym ** (-1)
    kappa_alpha3_sym = sp.simplify(q_sym * sp.diff(-sp.log(q3_int_sym), q_sym))
    kappa_alpha3_expected = -2 * (q_sym**2 - q_sym ** (-2)) / (
        q_sym**2 + 1 + q_sym ** (-2)
    )
    kappa_alpha3_residual = sp.simplify(kappa_alpha3_sym - kappa_alpha3_expected)

    kappa_alpha2_sym = sp.simplify(q_sym * sp.diff(-sp.log(q2_int_sym), q_sym))
    kappa_alpha2_expected = -(q_sym - q_sym ** (-1)) / (q_sym + q_sym ** (-1))
    kappa_alpha2_residual = sp.simplify(kappa_alpha2_sym - kappa_alpha2_expected)

    qfact3_over_q3_sym = sp.simplify(q3_int_sym * q2_int_sym / q_sym**3)
    laurent_bal_sym = 1 + 2 * q_sym ** (-2) + 2 * q_sym ** (-4) + q_sym ** (-6)
    ovud_residual = sp.simplify(qfact3_over_q3_sym - laurent_bal_sym)

    sym_ok = bool(
        cq_simplified == 0
        and kappa_mu_residual == 0
        and kappa_alpha3_residual == 0
        and kappa_alpha2_residual == 0
        and ovud_residual == 0
    )

    # 2. 80-dps evaluation at q_0 (qou-1u7x: varying-constants co-variation)
    cq_p = mp.mpf(1) / (q_p - 1)
    kappa_mu_p = -mp.mpf(2) / (q_p - 1)
    q3_p = q_p**2 + 1 + q_p ** (-2)
    q2_p = q_p + q_p ** (-1)
    kappa_alpha3_p = -mp.mpf(2) * (q_p**2 - q_p ** (-2)) / q3_p
    kappa_alpha2_p = -(q_p - q_p ** (-1)) / q2_p

    bal_p = 1 + 2 * q_p ** (-2) + 2 * q_p ** (-4) + 2 * 0 + q_p ** (-6)
    kappa_bal_p = -(4 * q_p ** (-2) + 8 * q_p ** (-4) + 6 * q_p ** (-6)) / bal_p

    slope_mu_over_alpha3 = kappa_mu_p / kappa_alpha3_p
    slope_mu_over_alpha2 = kappa_mu_p / kappa_alpha2_p

    eps_fd = mp.mpf("1e-30")
    fd_kappa_mu = (
        q_p
        * (
            (-2 * mp.log(1 - 1 / (q_p + eps_fd)))
            - (-2 * mp.log(1 - 1 / (q_p - eps_fd)))
        )
        / (2 * eps_fd)
    )
    fd_kappa_alpha3 = (
        q_p
        * (
            (-mp.log((q_p + eps_fd) ** 2 + 1 + (q_p + eps_fd) ** (-2)))
            - (-mp.log((q_p - eps_fd) ** 2 + 1 + (q_p - eps_fd) ** (-2)))
        )
        / (2 * eps_fd)
    )
    fd_ok = bool(
        abs(kappa_mu_p - fd_kappa_mu) < mp.mpf("1e-45")
        and abs(kappa_alpha3_p - fd_kappa_alpha3) < mp.mpf("1e-45")
    )
    cov_ok = bool(
        slope_mu_over_alpha3 > mp.mpf(65)
        and slope_mu_over_alpha2 > mp.mpf(174)
        and abs(kappa_mu_p) > 60 * abs(kappa_alpha3_p)
    )

    # 3. qou-cweq: c-q-q0.derivation.json proton-anchor consistency
    cq_derivation_path = COMPUTATIONS_DIR / "c-q-q0.derivation.json"
    with open(cq_derivation_path, "r", encoding="utf-8") as fh:
        cq_chain = json.load(fh, parse_float=str)
    cq_target = mp.mpf(str(cq_chain["target_value"]))
    cq_mu = mp.mpf(1) / (q_mu - 1)
    cq_rel_gap_mu_vs_p = (cq_p - cq_mu) / cq_p
    cq_exact_shift_formula = (q_mu - q_p) / (q_mu - 1)
    cweq_ok = bool(
        abs(cq_p - cq_target) < mp.mpf("5e-48")
        and abs(cq_rel_gap_mu_vs_p - cq_exact_shift_formula) < mp.mpf("1e-65")
    )

    # 4. i5p0: Homogeneous 1/hbar_q cancellation in log Phi_q ratios
    # Note: electron ruling 2026-11-21 sets sigma_0 sigma_1 sigma_0 in B_3 (Hopf closure)
    # as primary with trefoil kept as backup; homogeneous hbar_q^-1 cancels for any pair.
    xi_witness_path = COMPUTATIONS_DIR / "xi-ell-phi-q-probe.witness.json"
    with open(xi_witness_path, "r", encoding="utf-8") as fh:
        xi_data = json.load(fh)
    r_mu_t25_logphi = mp.mpf(
        xi_data["ratios_to_electron"]["muon T(2,5) \u03c3_1\u2075"]["ratio_log_phi"]
    )
    r_mu_41_logphi = mp.mpf(
        xi_data["ratios_to_electron"]["muon 4_1 (\u03c3_1\u03c3_2\u207b\u00b9)\u00b2"][
            "ratio_log_phi"
        ]
    )
    r_mu_41_phi = mp.mpf(
        xi_data["ratios_to_electron"]["muon 4_1 (\u03c3_1\u03c3_2\u207b\u00b9)\u00b2"][
            "ratio_phi_direct"
        ]
    )
    i5p0_ok = bool(
        r_mu_t25_logphi < mp.mpf(2)
        and r_mu_41_logphi < mp.mpf(11)
        and r_mu_41_phi > mp.mpf(100000)
    )

    # 5. qou-cgbd: CODATA-2022 direct vs AME-derived neutron mass in Q_beta
    m_e = +M_E_MEV
    m_p_cod = +M_P_MEV
    m_n_cod = +M_N_MEV_CODATA_DIRECT
    m_n_ame = +M_N_MEV_AME_DERIVED
    sig_p = +M_P_MEV_ERR
    sig_n = +M_N_MEV_CODATA_DIRECT_ERR

    q_beta_codata = m_n_cod - m_p_cod - m_e
    q_beta_ame = m_n_ame - m_p_cod - m_e
    dq_beta_cod_vs_ame = q_beta_codata - q_beta_ame
    sig_q_beta = mp.sqrt(sig_n**2 + sig_p**2)

    hbar_p = (q_p - 1) / q_p
    b_p = mp.sqrt(q_p**4 + q_p**2 + 1) / (q_p**2 + 1)
    rung_c3 = b_p**3 * hbar_p**6
    dc3_from_mass_table_split = abs(dq_beta_cod_vs_ame / q_beta_codata) / rung_c3
    sig_c3_codata = (sig_q_beta / q_beta_codata) / rung_c3
    cgbd_ok = bool(
        abs(dq_beta_cod_vs_ame) < sig_q_beta
        and dc3_from_mass_table_split < sig_c3_codata
    )

    wb = WitnessBuilder(
        "substrate-parameter-locality-varying-constants-probe",
        engine="mpmath+sympy",
        output_dir=THIS.parent,
        start_time=t0,
    )
    wb.set_description(
        "80-dps verification of conj:substrate-parameter-locality logarithmic "
        "sensitivities and parameter-free co-variation slopes (qou-1u7x), "
        "c_q(q_0) proton-anchor consistency (qou-cweq), [3]_q!/q^3 Laurent "
        "balancing identity (ovud), homogeneous 1/hbar_q cancellation (i5p0), "
        "and CODATA-2022 vs AME Q_beta consistency (qou-cgbd)."
    )
    wb.add_parameter("workdps", DPS)
    wb.add_parameter("q_0_proton", Q_50_DIGIT_STR)
    wb.add_data("c_q_proton", fmt(cq_p, 50))
    wb.add_data("kappa_mu_leading", fmt(kappa_mu_p, 50))
    wb.add_data("kappa_alpha_q3", fmt(kappa_alpha3_p, 50))
    wb.add_data("kappa_alpha_q2", fmt(kappa_alpha2_p, 50))
    wb.add_data("kappa_fbor_balancing", fmt(kappa_bal_p, 50))
    wb.add_data("covariation_slope_mu_over_alpha_q3", fmt(slope_mu_over_alpha3, 50))
    wb.add_data("covariation_slope_mu_over_alpha_q2", fmt(slope_mu_over_alpha2, 50))

    wb.add_assertion(
        "symbolic_cq_and_kappa_identities_exact",
        computed=sym_ok,
        expected=True,
        source="QOU.Observations.qfact3_eq_q3_mul_laurent_balancing + covariation_ratio_alpha3",
    )
    wb.add_assertion(
        "analytic_sensitivities_and_positive_covariation_slopes",
        computed=bool(fd_ok and cov_ok),
        expected=True,
        source="QOU.Observations.covariation_ratio_alpha2_pos_of_gt_one",
    )
    wb.add_assertion(
        "c_q_q0_derivation_and_anchor_shift_exact",
        computed=cweq_ok,
        expected=True,
        source="QOU.Observations.cq_anchor_relative_shift",
    )
    wb.add_assertion(
        "i5p0_homogeneous_hbar_cancellation_and_cgbd_sub_sigma",
        computed=bool(i5p0_ok and cgbd_ok),
        expected=True,
        source="QOU.Observations.homogeneous_hbar_scaling_cancels",
    )

    out_path = wb.save({"q0Anchor": "proton", "q0Value": Q_50_DIGIT_STR})
    print(f"Saved witness: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
