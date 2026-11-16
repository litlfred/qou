#!/usr/bin/env python3
"""Substrate parameter locality & varying-constants co-variation signature probe.

Addresses Round 48 calibration & brane-tower beans under parent `qou-2002`:
  - `qou-1u7x` (`conj:substrate-parameter-locality`): `q_0` is an observed-local
    calibration parameter (pinned by CAL-2 / proton mass), not derived from a
    parameter-free equation. Any slow spatial or cosmological variation
    `delta ln q_0(x)` induces strictly locked logarithmic drifts
    `delta ln O_i = kappa_i(q_0) * delta ln q_0` across all QOU observables,
    yielding parameter-free co-variation slopes `kappa_i(q_0) / kappa_j(q_0)`
    testable against Webb et al. quasar `Delta alpha / alpha` and `H_2 / NH_3`
    proton-to-electron `Delta mu / mu` bounds.
  - `qou-cweq`: Verifies `c-q-q0.derivation.json` proton-anchor consistency
    (`c_q(q_0) = 1 / (q_0 - 1) = 9.092679456150245...`) and quantifies the
    11.54 ppb proton-vs-muon anchor shift amplified by `q_0 / (q_0 - 1) = 10.093`
    to `1.1645e-7` in `c_q`.
  - `ovud`: Verifies the exact Laurent identity
    `[3]_q! / q^3 = 1 + 2 q^{-2} + 2 q^{-4} + q^{-6}` in `F_Bor(q)` and computes
    its exact logarithmic derivative `d ln([3]_q!/q^3) / d ln q` at `q_0`.
  - `i5p0`: Verifies that in the `xi_ell(q)` Path A compact-dilog tower
    (`log Phi_q(z) = Li_2(z) / hbar_q + O(1)`), the `1 / hbar_q` enhancement is
    homogeneous across numerators and denominators and therefore cancels in the
    lepton ratio `m(mu) / m(e)`, proving `206.77` requires an asymmetric `hbar_q`
    grading between `4_1` and `T(2,3)`.
  - `qou-cgbd`: Quantifies the CODATA-2022 direct vs AME-derived neutron mass
    difference (`1.5e-7 MeV`, `191.7 ppb` of `Q_beta`) and its `0.310` (`0.268 sigma`)
    shift on extracted `c_3` versus `sigma(c_3) = 1.157`.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTATIONS_DIR = HERE.parent
SUBSTRATE_DIR = COMPUTATIONS_DIR / "substrate"
for _p in (str(COMPUTATIONS_DIR), str(SUBSTRATE_DIR)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 60

# Canonical 50-digit anchors (AGENTS.md §q_0 anchor convention)
Q0_PROTON_STR = "1.1099785827513808075916690956107688798744991218736"
Q0_MUON_STR = "1.1099785955573347096588450177928228443400143284304"

# Experimental constants (CODATA-2022 direct vs AME-derived, bean qou-cgbd)
M_E_MEV_STR = "0.51099895069"
M_P_CODATA_MEV_STR = "938.27208943"
M_P_CODATA_ERR_MEV_STR = "0.00000029"
M_N_CODATA_MEV_STR = "939.56542194"
M_N_CODATA_ERR_MEV_STR = "0.00000048"
M_N_AME_MEV_STR = "939.56542179"


def fmt(x: mp.mpf, digits: int = 50) -> str:
    return mp.nstr(x, digits)


def main() -> int:
    wb = WitnessBuilder(
        "substrate-parameter-locality-varying-constants-probe",
        engine="mpmath+sympy",
    )
    wb.set_description(
        "50-dps verification of conj:substrate-parameter-locality varying-constants "
        "logarithmic sensitivities kappa_i = d ln O_i / d ln q_0 and parameter-free "
        "co-variation slopes (qou-1u7x), c_q(q_0) proton-anchor consistency (qou-cweq), "
        "[3]_q!/q^3 exact Laurent balancing sensitivity (ovud), homogeneous 1/hbar_q "
        "cancellation in log Phi_q lepton ratios (i5p0), and CODATA-2022 vs AME "
        "Q_beta / c_3 consistency (qou-cgbd)."
    )

    q_p = mp.mpf(Q0_PROTON_STR)
    q_mu = mp.mpf(Q0_MUON_STR)
    wb.add_parameter("q_0_proton", Q0_PROTON_STR)
    wb.add_parameter("q_0_muon", Q0_MUON_STR)

    assertions: list[tuple[str, bool, str]] = []

    def check(name: str, passed: bool, detail: str) -> None:
        assertions.append((name, bool(passed), detail))
        status = "PASS" if passed else "FAIL"
        print(f"  [{status}] {name}: {detail}")

    # =========================================================================
    # 1. Symbolic identities (sympy): c_q, kappa_mu, kappa_alpha, [3]_q!/q^3
    # =========================================================================
    q_sym = sp.Symbol("q", positive=True)
    hbar_sym = 1 - 1 / q_sym
    cq_sym = (1 / q_sym) / hbar_sym
    cq_simplified = sp.simplify(cq_sym - 1 / (q_sym - 1))

    # Leading mass-ratio scaling R_mu(q) = Vol(4_1) / hbar_q^2
    # d ln(hbar_q^-2) / d ln q = q * d/dq (-2 ln(1 - 1/q)) = -2 / (q - 1) = -2 c_q
    kappa_mu_sym = sp.simplify(q_sym * sp.diff(-2 * sp.log(hbar_sym), q_sym))
    kappa_mu_residual = sp.simplify(kappa_mu_sym - (-2 / (q_sym - 1)))

    # Fine-structure [3]_q = q^2 + 1 + q^-2 and [2]_q = q + q^-1
    q3_int_sym = q_sym**2 + 1 + q_sym ** (-2)
    q2_int_sym = q_sym + q_sym ** (-1)
    kappa_alpha3_sym = sp.simplify(q_sym * sp.diff(-sp.log(q3_int_sym), q_sym))
    kappa_alpha3_expected = -2 * (q_sym**2 - q_sym ** (-2)) / (q_sym**2 + 1 + q_sym ** (-2))
    kappa_alpha3_residual = sp.simplify(kappa_alpha3_sym - kappa_alpha3_expected)

    kappa_alpha2_sym = sp.simplify(q_sym * sp.diff(-sp.log(q2_int_sym), q_sym))
    kappa_alpha2_expected = -(q_sym - q_sym ** (-1)) / (q_sym + q_sym ** (-1))
    kappa_alpha2_residual = sp.simplify(kappa_alpha2_sym - kappa_alpha2_expected)

    # Exact [3]_q! / q^3 = 1 + 2 q^-2 + 2 q^-4 + q^-6 (bean ovud)
    q1_int_sym = sp.Integer(1)
    qfact3_over_q3_sym = sp.simplify(q3_int_sym * q2_int_sym * q1_int_sym / q_sym**3)
    laurent_bal_sym = 1 + 2 * q_sym ** (-2) + 2 * q_sym ** (-4) + q_sym ** (-6)
    ovud_residual = sp.simplify(qfact3_over_q3_sym - laurent_bal_sym)

    check(
        "symbolic_cq_and_kappa_identities_exact",
        cq_simplified == 0
        and kappa_mu_residual == 0
        and kappa_alpha3_residual == 0
        and kappa_alpha2_residual == 0
        and ovud_residual == 0,
        f"c_q={sp.simplify(cq_sym)}, kappa_mu={kappa_mu_sym}, ovud_res={ovud_residual}",
    )

    # =========================================================================
    # 2. Numerical evaluation at q_0 (qou-1u7x: varying-constants co-variation)
    # =========================================================================
    cq_p = mp.mpf(1) / (q_p - 1)
    kappa_mu_p = -mp.mpf(2) / (q_p - 1)  # = -2 * c_q(q_0)
    q3_p = q_p**2 + 1 + q_p ** (-2)
    q2_p = q_p + q_p ** (-1)
    kappa_alpha3_p = -mp.mpf(2) * (q_p**2 - q_p ** (-2)) / q3_p
    kappa_alpha2_p = -(q_p - q_p ** (-1)) / q2_p

    # Balancing factor [3]_q!/q^3 = 1 + 2 q^-2 + 2 q^-4 + q^-6 logarithmic derivative
    bal_p = 1 + 2 * q_p ** (-2) + 2 * q_p ** (-4) + q_p ** (-6)
    kappa_bal_p = -(4 * q_p ** (-2) + 8 * q_p ** (-4) + 6 * q_p ** (-6)) / bal_p

    # Co-variation slopes R_{mu/alpha} = (Delta mu / mu) / (Delta alpha / alpha)
    slope_mu_over_alpha3 = kappa_mu_p / kappa_alpha3_p
    slope_mu_over_alpha2 = kappa_mu_p / kappa_alpha2_p

    # Verify numerical derivatives match central finite differences at 50 dps
    eps_fd = mp.mpf("1e-25")
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

    check(
        "analytic_sensitivities_match_finite_difference_to_34dps",
        abs(kappa_mu_p - fd_kappa_mu) < mp.mpf("1e-34")
        and abs(kappa_alpha3_p - fd_kappa_alpha3) < mp.mpf("1e-34"),
        f"|dkappa_mu|={fmt(abs(kappa_mu_p - fd_kappa_mu), 10)}, "
        f"|dkappa_alpha3|={fmt(abs(kappa_alpha3_p - fd_kappa_alpha3), 10)}",
    )

    check(
        "covariation_slope_positive_and_mass_dominates_alpha",
        slope_mu_over_alpha3 > mp.mpf(65)
        and slope_mu_over_alpha2 > mp.mpf(174)
        and abs(kappa_mu_p) > 60 * abs(kappa_alpha3_p),
        f"kappa_mu={fmt(kappa_mu_p, 12)}, kappa_alpha3={fmt(kappa_alpha3_p, 12)}, "
        f"R_mu_alpha3=+{fmt(slope_mu_over_alpha3, 12)}, R_mu_alpha2=+{fmt(slope_mu_over_alpha2, 12)}",
    )

    # Quasar / molecular H_2 bound: |Delta mu / mu| < 1e-7 => |delta q_0 / q_0| < 5.50e-9
    quasar_dmu_over_mu_bound = mp.mpf("1e-7")
    max_dq_over_q = quasar_dmu_over_mu_bound / abs(kappa_mu_p)
    implied_dalpha3_over_alpha = abs(kappa_alpha3_p) * max_dq_over_q

    # =========================================================================
    # 3. `qou-cweq`: c-q-q0.derivation.json proton-anchor consistency
    # =========================================================================
    cq_derivation_path = COMPUTATIONS_DIR / "c-q-q0.derivation.json"
    with open(cq_derivation_path, "r", encoding="utf-8") as fh:
        cq_chain = json.load(fh, parse_float=str)
    cq_target_str = str(cq_chain["target_value"])
    cq_target = mp.mpf(cq_target_str)
    cq_mu = mp.mpf(1) / (q_mu - 1)
    anchor_rel_gap = (q_mu - q_p) / q_p
    cq_rel_gap_mu_vs_p = abs(cq_mu - cq_p) / cq_p
    cq_exact_shift_formula = (q_mu - q_p) / (q_mu - 1)

    check(
        "c_q_q0_derivation_matches_proton_pin_to_48dps",
        abs(cq_p - cq_target) < mp.mpf("1e-48")
        and abs(cq_rel_gap_mu_vs_p - cq_exact_shift_formula) < mp.mpf("1e-48"),
        f"|c_q(q_p) - target|={fmt(abs(cq_p - cq_target), 10)}, "
        f"muon-vs-proton rel shift={fmt(cq_rel_gap_mu_vs_p, 10)}",
    )

    # =========================================================================
    # 4. `i5p0`: Homogeneous 1/hbar_q cancellation in log Phi_q lepton ratios
    # =========================================================================
    xi_witness_path = COMPUTATIONS_DIR / "xi-ell-phi-q-probe.witness.json"
    with open(xi_witness_path, "r", encoding="utf-8") as fh:
        xi_data = json.load(fh)
    r_mu_t25_li2q = mp.mpf(xi_data["ratios_to_electron"]["muon T(2,5) \u03c3_1\u2075"]["ratio_li2q_sym"])
    r_mu_t25_logphi = mp.mpf(xi_data["ratios_to_electron"]["muon T(2,5) \u03c3_1\u2075"]["ratio_log_phi"])
    r_mu_41_li2q = mp.mpf(xi_data["ratios_to_electron"]["muon 4_1 (\u03c3_1\u03c3_2\u207b\u00b9)\u00b2"]["ratio_li2q_sym"])
    r_mu_41_logphi = mp.mpf(xi_data["ratios_to_electron"]["muon 4_1 (\u03c3_1\u03c3_2\u207b\u00b9)\u00b2"]["ratio_log_phi"])
    r_mu_41_phi = mp.mpf(xi_data["ratios_to_electron"]["muon 4_1 (\u03c3_1\u03c3_2\u207b\u00b9)\u00b2"]["ratio_phi_direct"])

    check(
        "i5p0_log_phi_q_ratio_cancels_1_over_hbar_q_enhancement",
        r_mu_t25_logphi < mp.mpf(2)
        and r_mu_41_logphi < mp.mpf(11)
        and r_mu_41_phi > mp.mpf(100000),
        f"T(2,5)/T(2,3) logPhi={fmt(r_mu_t25_logphi, 6)} (Li2q={fmt(r_mu_t25_li2q, 6)}), "
        f"4_1/T(2,3) logPhi={fmt(r_mu_41_logphi, 6)} (Phi_direct={fmt(r_mu_41_phi, 8)}) vs CODATA 206.77",
    )

    # =========================================================================
    # 5. `qou-cgbd`: CODATA-2022 direct vs AME-derived neutron mass in Q_beta
    # =========================================================================
    m_e = mp.mpf(M_E_MEV_STR)
    m_p_cod = mp.mpf(M_P_CODATA_MEV_STR)
    m_n_cod = mp.mpf(M_N_CODATA_MEV_STR)
    m_n_ame = mp.mpf(M_N_AME_MEV_STR)
    sig_p = mp.mpf(M_P_CODATA_ERR_MEV_STR)
    sig_n = mp.mpf(M_N_CODATA_ERR_MEV_STR)

    q_beta_codata = m_n_cod - m_p_cod - m_e
    q_beta_ame = m_n_ame - m_p_cod - m_e
    dq_beta_cod_vs_ame = q_beta_codata - q_beta_ame
    sig_q_beta = mp.sqrt(sig_n**2 + sig_p**2)

    hbar_p = (q_p - 1) / q_p
    b_p = mp.sqrt(q_p**4 + q_p**2 + 1) / (q_p**2 + 1)
    rung_c3 = b_p**3 * hbar_p**6
    dc3_from_mass_table_split = (dq_beta_cod_vs_ame / q_beta_codata) / rung_c3
    sig_c3_codata = (sig_q_beta / q_beta_codata) / rung_c3

    check(
        "cgbd_codata_vs_ame_split_is_sub_sigma_and_quantified",
        abs(dq_beta_cod_vs_ame - mp.mpf("1.5e-7")) < mp.mpf("1e-16")
        and dc3_from_mass_table_split < sig_c3_codata,
        f"dQ_beta={fmt(dq_beta_cod_vs_ame, 10)} MeV, "
        f"dc_3={fmt(dc3_from_mass_table_split, 6)} vs sigma(c_3)={fmt(sig_c3_codata, 6)} "
        f"({fmt(dc3_from_mass_table_split / sig_c3_codata, 4)} sigma)",
    )

    for name, passed, _detail in assertions:
        wb.add_assertion(
            name,
            computed="1" if passed else "0",
            expected="1",
            tolerance="0",
        )

    wb.add_data("c_q_proton_50dps", fmt(cq_p))
    wb.add_data("c_q_muon_50dps", fmt(cq_mu))
    wb.add_data("kappa_mu_leading_50dps", fmt(kappa_mu_p))
    wb.add_data("kappa_alpha_q3_50dps", fmt(kappa_alpha3_p))
    wb.add_data("kappa_alpha_q2_50dps", fmt(kappa_alpha2_p))
    wb.add_data("kappa_fbor_balancing_50dps", fmt(kappa_bal_p))
    wb.add_data("covariation_slope_mu_over_alpha_q3_50dps", fmt(slope_mu_over_alpha3))
    wb.add_data("covariation_slope_mu_over_alpha_q2_50dps", fmt(slope_mu_over_alpha2))
    wb.add_data("quasar_dmu_1e7_max_dq_over_q", fmt(max_dq_over_q, 20))
    wb.add_data("quasar_dmu_1e7_implied_dalpha3_over_alpha", fmt(implied_dalpha3_over_alpha, 20))
    wb.add_data("cweq_anchor_rel_gap_muon_vs_proton", fmt(anchor_rel_gap, 20))
    wb.add_data("cweq_cq_rel_gap_muon_vs_proton", fmt(cq_rel_gap_mu_vs_p, 20))
    wb.add_data("i5p0_muon_t25_over_e_logphi", fmt(r_mu_t25_logphi, 20))
    wb.add_data("i5p0_muon_41_over_e_logphi", fmt(r_mu_41_logphi, 20))
    wb.add_data("i5p0_muon_41_over_e_phi_direct", fmt(r_mu_41_phi, 20))
    wb.add_data("cgbd_Q_beta_codata_2022_MeV", fmt(q_beta_codata, 20))
    wb.add_data("cgbd_Q_beta_ame_derived_MeV", fmt(q_beta_ame, 20))
    wb.add_data("cgbd_dQ_beta_MeV", fmt(dq_beta_cod_vs_ame, 20))
    wb.add_data("cgbd_dc3_split", fmt(dc3_from_mass_table_split, 20))
    wb.add_data("cgbd_sigma_c3_codata", fmt(sig_c3_codata, 20))

    out_path = wb.save()
    print(f"\nSaved witness: {out_path}")
    return 0 if all(p for _, p, _ in assertions) else 1


if __name__ == "__main__":
    raise SystemExit(main())
