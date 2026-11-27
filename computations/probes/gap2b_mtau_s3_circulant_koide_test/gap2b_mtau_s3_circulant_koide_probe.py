#!/usr/bin/env python3
"""EXPLORATORY shape-probe (pre-registered 80-dps test) for Open Gap 2 Backup (Option 2B, bean `qou-j96h`):
S_3-Equivariant / Z_3-Circulant Mass Matrix & Algebraic Koide Trace-to-Norm Test on Bring's 3-Generation Subspace `projGen3`.

Pre-registration committed & pushed BEFORE execution:
  - `computations/probes/gap2b_mtau_s3_circulant_koide_test/PREREGISTRATION.md`
Formal Lean 4 backing (`0 sorry`, `0` custom `axiom`s, generic `[CommRing R]` / `[Field F]`, §7c):
  - `folio/quantum-observable-universe/lean/QOU/StandardModel/S3CirculantKoideTraceIdentity.lean`

Precision & anti-fit discipline:
  - `mpmath.workdps(80)` (`OUT_DPS = 50` serialized),
  - `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`),
  - exact symbolic `sympy` verification of all circulant, Bring-metric, S_3-commutant,
    quadratic-resolvent, and H_3(q)/TL_3(q) identities,
  - zero `float64` imports, casts, or lossy literals (`scripts/probe-float64-guard.py` clean),
  - zero tuned angles, radii, or weights (`NO FITTING, EXCEPT CAL-1/2/3`).
"""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[3]
for _p in (
    _ROOT / "tools" / "qou-substrate" / "python",
    _ROOT / "schemas" / "witness-schema" / "python",
    _ROOT / "computations",
):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.constants import q_at, vol_4_1_at  # noqa: E402
from qou_substrate.precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

WORK_DPS = 80
OUT_DPS = 50
set_compute_dps(WORK_DPS)


# ---------------------------------------------------------------------------
# 1. Exact Symbolic Verification (`sympy` over Q) mirroring Lean 4 module
# ---------------------------------------------------------------------------
def run_symbolic_checks() -> dict[str, object]:
    a, b_re, b_im, u, v, x, q = sp.symbols("a b_re b_im u v x q", commutative=True)
    i_unit = sp.I

    c_shift = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    i3 = sp.eye(3)
    b_cx = b_re + i_unit * b_im
    b_bar = b_re - i_unit * b_im
    norm_b_sq = b_re**2 + b_im**2

    s_herm = a * i3 + b_cx * c_shift + b_bar * (c_shift**2)
    s_dag = sp.Matrix(3, 3, lambda r, c: s_herm[c, r].subs(i_unit, -i_unit))

    herm_diff = sp.simplify(s_dag - s_herm)
    tr_s = sp.simplify(s_herm.trace() - 3 * a)
    tr_s2 = sp.simplify((s_herm**2).trace() - 3 * (a**2 + 2 * norm_b_sq))
    tr_sdags = sp.simplify((s_dag * s_herm).trace() - 3 * (a**2 + 2 * norm_b_sq))
    koide_poly = sp.simplify(
        3 * (s_herm**2).trace() - 2 * s_herm.trace() ** 2 - 9 * (2 * norm_b_sq - a**2)
    )

    # Unbroken S_3 symmetric circulant S(a, b, b) doublet degeneracy
    b_sym = sp.Symbol("b_sym", commutative=True)
    m_s3 = a * i3 + b_sym * (c_shift + c_shift**2)
    min_poly_s3 = sp.simplify((m_s3 - (a + 2 * b_sym) * i3) * (m_s3 - (a - b_sym) * i3))

    # Bring projGen3 ambient F^5 metric stretch: ||projDem1(embed(lam))||_5^2 = 4 ||demProj3(lam)||_3^2
    l0, l1, l2 = sp.symbols("l0 l1 l2", commutative=True)
    lsum = l0 + l1 + l2
    dem3_norm_sq = 3 * (lsum / 3) ** 2
    dem5_vec = [lsum / 3, lsum / 3, lsum / 3, -lsum, sp.Integer(0)]
    dem5_norm_sq = sum(comp**2 for comp in dem5_vec)
    bring_stretch_diff = sp.simplify(dem5_norm_sq - 4 * dem3_norm_sq)

    # Quadratic Koide resolvent identity
    resolvent_poly = x**2 - 4 * (u + v) * x + (u**2 + v**2 - 4 * u * v)
    resolvent_id = sp.simplify(3 * (u**2 + v**2 + x**2) - 2 * (u + v + x) ** 2 - resolvent_poly)
    completed_sq_id = sp.simplify(
        resolvent_poly - ((x - 2 * (u + v)) ** 2 - 3 * (u**2 + 4 * u * v + v**2))
    )
    disc_id = sp.simplify(
        (-4 * (u + v)) ** 2 - 4 * (u**2 + v**2 - 4 * u * v) - 12 * (u**2 + 4 * u * v + v**2)
    )

    # H_3(q) chiral photon vertex stepPlus(q, q - q^-1) and TL_3(q) deficit
    h = q - 1 / q
    step_plus = sp.Matrix(
        [
            [-h * q, q, 0],
            [0, 0, q - h],
            [1, 0, h * q - h**2],
        ]
    )
    step_at_one_diff = sp.simplify(step_plus.subs(q, 1) - c_shift)
    step_trace_diff = sp.simplify(step_plus.trace() + h**2)

    y3 = 1 - 2 / (q + 1 / q) ** 2
    y21 = 1 / (q + 1 / q) ** 2
    q_tl3 = sp.simplify((y3 + 2 * y21) / (3 * y3))
    tl3_deficit_diff = sp.simplify(
        (sp.Rational(2, 3) - q_tl3) - h**2 / (3 * (q**2 + q ** (-2)))
    )

    all_ok = (
        herm_diff == sp.zeros(3, 3)
        and tr_s == 0
        and tr_s2 == 0
        and tr_sdags == 0
        and koide_poly == 0
        and min_poly_s3 == sp.zeros(3, 3)
        and bring_stretch_diff == 0
        and resolvent_id == 0
        and completed_sq_id == 0
        and disc_id == 0
        and step_at_one_diff == sp.zeros(3, 3)
        and step_trace_diff == 0
        and tl3_deficit_diff == 0
    )
    return {
        "all_symbolic_identities_verified": all_ok,
        "hermitian_circulant_koide_poly_zero": koide_poly == 0,
        "s3_symmetric_min_poly_zero": min_poly_s3 == sp.zeros(3, 3),
        "bring_ambient_f5_stretch_factor_4_exact": bring_stretch_diff == 0,
        "koide_quadratic_resolvent_exact": resolvent_id == 0 and completed_sq_id == 0,
        "step_plus_q1_is_cyclic_shift": step_at_one_diff == sp.zeros(3, 3),
        "tl3_finite_q_deficit_exact": tl3_deficit_diff == 0,
    }


# ---------------------------------------------------------------------------
# 2. 80-dps Koide Helpers (zero float64)
# ---------------------------------------------------------------------------
def koide_ratio_from_mass_ratios(r_mu_e: mp.mpf, r_tau_e: mp.mpf) -> mp.mpf:
    u = mp.mpf(1)
    v = mp.sqrt(r_mu_e)
    w = mp.sqrt(r_tau_e)
    return (u**2 + v**2 + w**2) / ((u + v + w) ** 2)


def koide_tau_from_mu_ratio(r_mu_e: mp.mpf) -> dict[str, mp.mpf]:
    """Positive root x_+ of x^2 - 4(1+v)x + (1 + v^2 - 4v) = 0, returning m_tau/m_e = x_+^2."""
    u = mp.mpf(1)
    v = mp.sqrt(r_mu_e)
    s = mp.sqrt(3 * (u**2 + 4 * u * v + v**2))
    x_plus = 2 * (u + v) + s
    x_minus = 2 * (u + v) - s
    r_tau_pred = x_plus**2
    q_check = koide_ratio_from_mass_ratios(r_mu_e, r_tau_pred)
    return {
        "sqrt_m_mu_over_m_e": v,
        "x_plus_sqrt_m_tau_over_m_e": x_plus,
        "x_minus_secondary_root": x_minus,
        "m_tau_over_m_e_pred": r_tau_pred,
        "koide_q_check": q_check,
    }


def koide_mass_ratios_from_theta(theta: mp.mpf) -> dict[str, mp.mpf]:
    """Standard positive-ordered Brannen-Koide parameterization (0 < theta < pi/12):
      lambda_e   / a = 1 + sqrt(2) cos(theta + 2 pi / 3)
      lambda_mu  / a = 1 + sqrt(2) cos(theta + 4 pi / 3)
      lambda_tau / a = 1 + sqrt(2) cos(theta)
    """
    rt2 = mp.sqrt(2)
    two_pi_3 = 2 * mp.pi / 3
    four_pi_3 = 4 * mp.pi / 3
    le = 1 + rt2 * mp.cos(theta + two_pi_3)
    lmu = 1 + rt2 * mp.cos(theta + four_pi_3)
    ltau = 1 + rt2 * mp.cos(theta)
    r_mu_e = (lmu / le) ** 2
    r_tau_e = (ltau / le) ** 2
    r_tau_mu = (ltau / lmu) ** 2
    q_val = (le**2 + lmu**2 + ltau**2) / ((le + lmu + ltau) ** 2)
    # Exact logarithmic sensitivities d ln(m_l / m_e) / d theta
    dle = -rt2 * mp.sin(theta + two_pi_3)
    dlmu = -rt2 * mp.sin(theta + four_pi_3)
    dltau = -rt2 * mp.sin(theta)
    dln_mu_e = 2 * (dlmu / lmu - dle / le)
    dln_tau_e = 2 * (dltau / ltau - dle / le)
    return {
        "lambda_e_over_a": le,
        "lambda_mu_over_a": lmu,
        "lambda_tau_over_a": ltau,
        "m_mu_over_m_e": r_mu_e,
        "m_tau_over_m_e": r_tau_e,
        "m_tau_over_m_mu": r_tau_mu,
        "koide_q": q_val,
        "dln_mmu_me_dtheta": dln_mu_e,
        "dln_mtau_me_dtheta": dln_tau_e,
    }


def solve_theta_from_mu_ratio(r_mu_e: mp.mpf) -> mp.mpf:
    """Solve (1 + sqrt(2) cos(theta + 4pi/3)) / (1 + sqrt(2) cos(theta + 2pi/3)) = sqrt(r_mu_e)
    on theta in (0, pi/12) at 80 dps."""
    target = mp.sqrt(r_mu_e)
    rt2 = mp.sqrt(2)
    two_pi_3 = 2 * mp.pi / 3
    four_pi_3 = 4 * mp.pi / 3

    def f(th: mp.mpf) -> mp.mpf:
        le = 1 + rt2 * mp.cos(th + two_pi_3)
        lmu = 1 + rt2 * mp.cos(th + four_pi_3)
        return lmu - target * le

    return mp.findroot(f, mp.mpf("2") / mp.mpf("9"))


def cubic_sym_eigenvalues_3x3(m: list[list[mp.mpf]]) -> list[mp.mpf]:
    """Exact 80-dps eigenvalues of a 3x3 real symmetric matrix via trigonometric Vieta formula."""
    tr = m[0][0] + m[1][1] + m[2][2]
    p1 = m[0][1] ** 2 + m[0][2] ** 2 + m[1][2] ** 2
    q_mean = tr / 3
    p2 = (
        (m[0][0] - q_mean) ** 2
        + (m[1][1] - q_mean) ** 2
        + (m[2][2] - q_mean) ** 2
        + 2 * p1
    )
    p = mp.sqrt(p2 / 6)
    if p == 0:
        return [q_mean, q_mean, q_mean]
    b = [
        [(m[i][j] - (q_mean if i == j else mp.mpf(0))) / p for j in range(3)]
        for i in range(3)
    ]
    det_b = (
        b[0][0] * (b[1][1] * b[2][2] - b[1][2] * b[2][1])
        - b[0][1] * (b[1][0] * b[2][2] - b[1][2] * b[2][0])
        + b[0][2] * (b[1][0] * b[2][1] - b[1][1] * b[2][0])
    )
    half_det = det_b / 2
    if half_det <= -1:
        phi = mp.pi / 3
    elif half_det >= 1:
        phi = mp.mpf(0)
    else:
        phi = mp.acos(half_det) / 3
    e_max = q_mean + 2 * p * mp.cos(phi)
    e_min = q_mean + 2 * p * mp.cos(phi + 2 * mp.pi / 3)
    e_mid = 3 * q_mean - e_max - e_min
    return sorted([e_min, e_mid, e_max])


# ---------------------------------------------------------------------------
# 3. Main Pre-Registered Execution
# ---------------------------------------------------------------------------
def main() -> int:
    with mp.workdps(WORK_DPS):
        sym_res = run_symbolic_checks()

        # Proton-anchored substrate constants at 80 dps
        q0 = q_at(WORK_DPS)
        vol41 = vol_4_1_at(WORK_DPS)
        hbar_q0 = 1 - 1 / q0
        h_q0 = q0 - 1 / q0
        two_q0 = q0 + 1 / q0
        three_q0 = q0**2 + 1 + 1 / (q0**2)
        four_q0 = (q0**4 - 1 / (q0**4)) / h_q0

        # Downstream experimental benchmarks (read-only from authoritative NIST CODATA-2022 + PDG-2024)
        mu_codata = codata("muon-electron mass ratio")
        tau_codata = codata("tau-electron mass ratio")
        me_codata = codata("electron mass energy equivalent in MeV")
        tau_mev_codata = codata("tau energy equivalent")

        r_mu_exp = mp.mpf(mu_codata.value_str)
        r_mu_err = mp.mpf(mu_codata.uncertainty_str)
        m_e_mev = mp.mpf(me_codata.value_str)
        m_e_mev_err = mp.mpf(me_codata.uncertainty_str)

        # 1. Primary CODATA-2022 dimensionless tau-electron mass ratio: 3477.23 +/- 0.23
        r_tau_codata = mp.mpf(tau_codata.value_str)
        r_tau_codata_err = mp.mpf(tau_codata.uncertainty_str)

        # 2. PDG pre-Belle-II MeV world average (in CODATA-2022): 1776.86 +/- 0.12 MeV / m_e = 3477.2283 +/- 0.2348
        #    (Fixes earlier 10x transcription bug that misread `(23)` in `3477.23(23)` as `+/- 0.023`.)
        m_tau_pdg_pre_mev = mp.mpf(tau_mev_codata.value_str)
        m_tau_pdg_pre_err_mev = mp.mpf(tau_mev_codata.uncertainty_str)
        r_tau_pdg_pre = m_tau_pdg_pre_mev / m_e_mev
        r_tau_pdg_pre_err = mp.sqrt(
            (m_tau_pdg_pre_err_mev / m_e_mev) ** 2
            + (r_tau_pdg_pre * m_e_mev_err / m_e_mev) ** 2
        )

        # 3. PDG-2024 post-Belle-II world average (Navas et al., Phys. Rev. D 110, 030001 (2024)):
        #    m_tau = 1776.93 +/- 0.09 MeV -> m_tau / m_e = 3477.3653 +/- 0.1761
        m_tau_pdg24_mev = mp.mpf("1776.93")
        m_tau_pdg24_err_mev = mp.mpf("0.09")
        r_tau_pdg24 = m_tau_pdg24_mev / m_e_mev
        r_tau_pdg24_err = mp.sqrt(
            (m_tau_pdg24_err_mev / m_e_mev) ** 2
            + (r_tau_pdg24 * m_e_mev_err / m_e_mev) ** 2
        )

        two_thirds = mp.mpf(2) / mp.mpf(3)

        # Empirical Koide Q and 80-dps uncertainty propagation across CODATA-2022 & PDG-2024
        q_exp_codata = koide_ratio_from_mass_ratios(r_mu_exp, r_tau_codata)
        q_exp_pdg_pre = koide_ratio_from_mass_ratios(r_mu_exp, r_tau_pdg_pre)
        q_exp_pdg24 = koide_ratio_from_mass_ratios(r_mu_exp, r_tau_pdg24)
        eps_step = mp.mpf(10) ** (-35)
        dq_dmu_cod = (
            koide_ratio_from_mass_ratios(r_mu_exp + eps_step, r_tau_codata)
            - koide_ratio_from_mass_ratios(r_mu_exp - eps_step, r_tau_codata)
        ) / (2 * eps_step)
        dq_dtau_cod = (
            koide_ratio_from_mass_ratios(r_mu_exp, r_tau_codata + eps_step)
            - koide_ratio_from_mass_ratios(r_mu_exp, r_tau_codata - eps_step)
        ) / (2 * eps_step)
        q_exp_codata_err = mp.sqrt(
            (dq_dmu_cod * r_mu_err) ** 2 + (dq_dtau_cod * r_tau_codata_err) ** 2
        )
        dq_dmu_p24 = (
            koide_ratio_from_mass_ratios(r_mu_exp + eps_step, r_tau_pdg24)
            - koide_ratio_from_mass_ratios(r_mu_exp - eps_step, r_tau_pdg24)
        ) / (2 * eps_step)
        dq_dtau_p24 = (
            koide_ratio_from_mass_ratios(r_mu_exp, r_tau_pdg24 + eps_step)
            - koide_ratio_from_mass_ratios(r_mu_exp, r_tau_pdg24 - eps_step)
        ) / (2 * eps_step)
        q_exp_pdg24_err = mp.sqrt(
            (dq_dmu_p24 * r_mu_err) ** 2 + (dq_dtau_p24 * r_tau_pdg24_err) ** 2
        )

        theta_exp = solve_theta_from_mu_ratio(r_mu_exp)
        theta_crit = mp.pi / 12
        exp_koide_spec = koide_mass_ratios_from_theta(theta_exp)

        # -------------------------------------------------------------------
        # Part A: Quadratic Resolvent Tests (R1, R2a, R2b)
        # -------------------------------------------------------------------
        r_mu_qou_bare = vol41 / (hbar_q0**2)
        y3_q0 = 1 - 2 / (two_q0**2)
        tau_e_q0 = (q0**3) * y3_q0
        tau_41_q0 = (h_q0**4 + 3 * h_q0**2 + 1) / (two_q0**2)
        r_mu_qou_9213 = tau_41_q0 / tau_e_q0 + r_mu_qou_bare

        resolvent_inputs = [
            ("R1_codata_cal1_cal2", r_mu_exp),
            ("R2a_qou_bare_vol41", r_mu_qou_bare),
            ("R2b_qou_inhomogeneous_9213", r_mu_qou_9213),
        ]
        part_a_results: dict[str, dict[str, str]] = {}
        for label, r_mu_in in resolvent_inputs:
            res = koide_tau_from_mu_ratio(r_mu_in)
            mtau_pred = res["m_tau_over_m_e_pred"]
            diff_codata = mtau_pred - r_tau_codata
            rel_codata = diff_codata / r_tau_codata
            pull_codata = diff_codata / r_tau_codata_err
            diff_pdg_pre = mtau_pred - r_tau_pdg_pre
            rel_pdg_pre = diff_pdg_pre / r_tau_pdg_pre
            pull_pdg_pre = diff_pdg_pre / r_tau_pdg_pre_err
            diff_pdg24 = mtau_pred - r_tau_pdg24
            rel_pdg24 = diff_pdg24 / r_tau_pdg24
            pull_pdg24 = diff_pdg24 / r_tau_pdg24_err
            part_a_results[label] = {
                "input_m_mu_over_m_e": fmt(r_mu_in, dps=OUT_DPS),
                "input_m_mu_rel_err_vs_codata": fmt((r_mu_in - r_mu_exp) / r_mu_exp, dps=20),
                "pred_m_tau_over_m_e": fmt(mtau_pred, dps=OUT_DPS),
                "diff_vs_codata_2022": fmt(diff_codata, dps=20),
                "rel_err_vs_codata_2022": fmt(rel_codata, dps=20),
                "rel_err_pct_vs_codata_2022": fmt(100 * rel_codata, dps=12),
                "sigma_pull_vs_codata_2022": fmt(pull_codata, dps=12),
                "diff_vs_pdg_pre_belle2": fmt(diff_pdg_pre, dps=20),
                "rel_err_vs_pdg_pre_belle2": fmt(rel_pdg_pre, dps=20),
                "sigma_pull_vs_pdg_pre_belle2": fmt(pull_pdg_pre, dps=12),
                "diff_vs_pdg_2024": fmt(diff_pdg24, dps=20),
                "rel_err_vs_pdg_2024": fmt(rel_pdg24, dps=20),
                "rel_err_pct_vs_pdg_2024": fmt(100 * rel_pdg24, dps=12),
                "sigma_pull_vs_pdg_2024": fmt(pull_pdg24, dps=12),
                "koide_q_identity_residual": fmt(abs(res["koide_q_check"] - two_thirds), dps=15),
            }

        # -------------------------------------------------------------------
        # Part B: Un-Tuned H_3(q_0) & Bring `projGen3` Operator Tests
        # -------------------------------------------------------------------
        y21_q0 = 1 / (two_q0**2)
        rho_tl3 = (2 * y21_q0) / y3_q0
        q_tl3_q0 = (y3_q0 + 2 * y21_q0) / (3 * y3_q0)
        q_tl3_closed = (two_q0**2) / (3 * (q0**2 + 1 / (q0**2)))
        tl3_deficit_exact = (h_q0**2) / (3 * (q0**2 + 1 / (q0**2)))
        tl3_deficit_identity_res = abs((two_thirds - q_tl3_q0) - tl3_deficit_exact)

        # Op_B5: Regular H_3(q_0) Wedderburn Hook / q-dimension weights on V_(3) + V_(2,1)
        # In H_3(q), standard q-Plancherel weights (normalized on S_3: w_(3) ~ 1/[3]_q!, w_(2,1) ~ [2]_q/[3]_q)
        # On 1D singlet + 2D doublet: w_sing_h3 = 1 / (two_q0 * three_q0), w_doub_h3 = 2 * two_q0 / (two_q0 * three_q0) = 2 / three_q0?
        # Check q -> 1: w_sing = 1/6, 2 * d_(2,1) * w_(2,1) = 4/6 (since dim V_(2,1) = 2, Plancherel dim^2 = 4): ratio = 4.
        # Also Schur-Weyl SU(2)_q quantum dimension ratio: 2 * [2]_q / [4]_q (identical to rho_tl3).
        rho_h3_plancherel = 2 * (two_q0**2)  # (dim V_21)^2 / (dim V_3)^2 q-deformed = 4 at q=1 -> [2]_q^2? Wait: Plancherel in H_3(q):
        # Exact H_3(q) Plancherel weights: P_(3)(q) = q^3 / [3]_q! or bar-invariant 1 / ([2]_q * [3]_q),
        # P_(2,1)(q) = 1 / [3]_q -> total 2D trace weight 2 / [3]_q, ratio w_doub / w_sing = 2 * [2]_q (= 4 at q=1).
        rho_h3_reg = 2 * two_q0
        q_h3_reg = (1 + rho_h3_reg) / 3

        # Op_B6: Ruled chiral photon vertex V(q_0) = stepPlus(q_0, h_q0) on M_{+1}
        v_mat = [
            [-h_q0 * q0, q0, mp.mpf(0)],
            [mp.mpf(0), mp.mpf(0), q0 - h_q0],
            [mp.mpf(1), mp.mpf(0), h_q0 * q0 - h_q0**2],
        ]
        v_herm = [
            [(v_mat[i][j] + v_mat[j][i]) / 2 for j in range(3)]
            for i in range(3)
        ]

        op_b6_variants: dict[str, dict[str, object]] = {}
        for k_name, kappa in [("kappa_1", mp.mpf(1)), ("kappa_inv_sqrt2", 1 / mp.sqrt(2))]:
            s_op = [
                [(mp.mpf(1) if i == j else mp.mpf(0)) + kappa * v_herm[i][j] for j in range(3)]
                for i in range(3)
            ]
            eigs = cubic_sym_eigenvalues_3x3(s_op)
            q_op = (eigs[0] ** 2 + eigs[1] ** 2 + eigs[2] ** 2) / ((eigs[0] + eigs[1] + eigs[2]) ** 2)
            op_b6_variants[k_name] = {
                "eigenvalues": [fmt(ev, dps=30) for ev in eigs],
                "all_positive": bool(eigs[0] > 0),
                "koide_q": fmt(q_op, dps=OUT_DPS),
                "diff_vs_two_thirds": fmt(q_op - two_thirds, dps=20),
                "m_mu_over_m_e_if_positive": fmt((eigs[1] / eigs[0]) ** 2, dps=20)
                if eigs[0] > 0
                else "non_positive_spectrum",
                "m_tau_over_m_e_if_positive": fmt((eigs[2] / eigs[0]) ** 2, dps=20)
                if eigs[0] > 0
                else "non_positive_spectrum",
            }

        part_b_operators = {
            "Op_B1_identity": {
                "rho_doublet_over_singlet": "0",
                "koide_q": fmt(mp.mpf(1) / mp.mpf(3), dps=OUT_DPS),
                "diff_vs_two_thirds": fmt(-mp.mpf(1) / mp.mpf(3), dps=20),
                "passes_equipartition": False,
            },
            "Op_B2_democratic_D3": {
                "rho_doublet_over_singlet": "2",
                "koide_q": "1",
                "diff_vs_two_thirds": fmt(mp.mpf(1) / mp.mpf(3), dps=20),
                "passes_equipartition": False,
            },
            "Op_B3_isotropic_Z3_plancherel_or_projGen3_dof": {
                "rho_doublet_over_singlet": "2",
                "koide_q": "1",
                "diff_vs_two_thirds": fmt(mp.mpf(1) / mp.mpf(3), dps=20),
                "passes_equipartition": False,
            },
            "Op_B4_TL3_convD_wedderburn_norm": {
                "y3_q0": fmt(y3_q0, dps=OUT_DPS),
                "two_y21_q0": fmt(2 * y21_q0, dps=OUT_DPS),
                "schur_weyl_check_2_twoq_over_fourq_diff": fmt(
                    abs(rho_tl3 - (2 * two_q0 / four_q0)), dps=15
                ),
                "rho_doublet_over_singlet": fmt(rho_tl3, dps=OUT_DPS),
                "koide_q_at_q1_exact": fmt(two_thirds, dps=OUT_DPS),
                "koide_q_at_q0": fmt(q_tl3_q0, dps=OUT_DPS),
                "diff_vs_two_thirds": fmt(q_tl3_q0 - two_thirds, dps=20),
                "rel_shift_pct_vs_two_thirds": fmt(100 * (q_tl3_q0 - two_thirds) / two_thirds, dps=12),
                "sigma_pull_vs_q_exp_codata_2022": fmt(
                    (q_tl3_q0 - q_exp_codata) / q_exp_codata_err, dps=12
                ),
                "sigma_pull_vs_q_exp_pdg_2024": fmt(
                    (q_tl3_q0 - q_exp_pdg24) / q_exp_pdg24_err, dps=12
                ),
                "deficit_closed_form_residual": fmt(tl3_deficit_identity_res, dps=15),
                "passes_equipartition": bool(
                    abs(q_tl3_q0 - q_exp_codata) <= 3 * q_exp_codata_err
                ),
            },
            "Op_B5_H3_regular_plancherel_qdim": {
                "rho_doublet_over_singlet": fmt(rho_h3_reg, dps=OUT_DPS),
                "koide_q_at_q0": fmt(q_h3_reg, dps=OUT_DPS),
                "diff_vs_two_thirds": fmt(q_h3_reg - two_thirds, dps=20),
                "passes_equipartition": False,
            },
            "Op_B6_chiral_photon_vertex_Mplus1": op_b6_variants,
        }

        # -------------------------------------------------------------------
        # Part C: Zero-Parameter Phase Candidates theta_1 .. theta_7 (Q = 2/3)
        # -------------------------------------------------------------------
        alpha_chiral = mp.acos(-(1 + h_q0**2) / 2)
        phase_candidates = [
            ("theta_1_two_hbar", 2 * hbar_q0, True),
            ("theta_2_two_ln_q0", 2 * mp.log(q0), True),
            ("theta_3_two_q0_minus_1", 2 * (q0 - 1), True),
            ("theta_4_hecke_h", h_q0, True),
            ("theta_5_rational_two_ninths", mp.mpf(2) / mp.mpf(9), False),
            ("theta_6_q_triality_casimir", 2 / (three_q0**2), True),
            ("theta_7_chiral_vertex_eigenphase_shift", alpha_chiral - 2 * mp.pi / 3, True),
        ]

        part_c_phases: dict[str, dict[str, object]] = {}
        any_q0_phase_under_1pct_both = False
        for name, th_val, is_q0_derived in phase_candidates:
            spec = koide_mass_ratios_from_theta(th_val)
            rmu = spec["m_mu_over_m_e"]
            rtau = spec["m_tau_over_m_e"]
            rtaumu = spec["m_tau_over_m_mu"]
            rel_mu = (rmu - r_mu_exp) / r_mu_exp
            rel_tau_cod = (rtau - r_tau_codata) / r_tau_codata
            rel_tau_p24 = (rtau - r_tau_pdg24) / r_tau_pdg24
            pull_mu = (rmu - r_mu_exp) / r_mu_err
            pull_tau_cod = (rtau - r_tau_codata) / r_tau_codata_err
            pull_tau_p24 = (rtau - r_tau_pdg24) / r_tau_pdg24_err
            under_1pct_both = bool(
                abs(rel_mu) < mp.mpf("0.01") and abs(rel_tau_cod) < mp.mpf("0.01")
            )
            if is_q0_derived and under_1pct_both:
                any_q0_phase_under_1pct_both = True
            part_c_phases[name] = {
                "is_q0_derived": is_q0_derived,
                "theta_rad": fmt(th_val, dps=OUT_DPS),
                "theta_minus_theta_exp": fmt(th_val - theta_exp, dps=20),
                "theta_rel_diff_vs_theta_exp_pct": fmt(
                    100 * (th_val - theta_exp) / theta_exp, dps=12
                ),
                "pred_m_mu_over_m_e": fmt(rmu, dps=OUT_DPS),
                "rel_err_m_mu_pct": fmt(100 * rel_mu, dps=12),
                "rel_err_m_mu_ppm": fmt((mp.mpf(10) ** 6) * rel_mu, dps=12),
                "sigma_pull_m_mu": fmt(pull_mu, dps=12),
                "pred_m_tau_over_m_e": fmt(rtau, dps=OUT_DPS),
                "rel_err_m_tau_pct_vs_codata_2022": fmt(100 * rel_tau_cod, dps=12),
                "rel_err_m_tau_ppm_vs_codata_2022": fmt((mp.mpf(10) ** 6) * rel_tau_cod, dps=12),
                "sigma_pull_m_tau_vs_codata_2022": fmt(pull_tau_cod, dps=12),
                "rel_err_m_tau_pct_vs_pdg_2024": fmt(100 * rel_tau_p24, dps=12),
                "rel_err_m_tau_ppm_vs_pdg_2024": fmt((mp.mpf(10) ** 6) * rel_tau_p24, dps=12),
                "sigma_pull_m_tau_vs_pdg_2024": fmt(pull_tau_p24, dps=12),
                "pred_m_tau_over_m_mu": fmt(rtaumu, dps=30),
                "koide_q_check": fmt(spec["koide_q"], dps=30),
                "passes_1pct_both_ratios": under_1pct_both,
            }

        any_operator_passes_equipartition = bool(
            part_b_operators["Op_B4_TL3_convD_wedderburn_norm"]["passes_equipartition"]
        )
        gate_g2b_passed = bool(any_operator_passes_equipartition and any_q0_phase_under_1pct_both)

        # Print concise 80-dps summary table to stdout
        print("=== Open Gap 2B (qou-j96h): S_3/Z_3 Circulant & Koide Trace-to-Norm Probe (80 dps) ===")
        print(f"q0 (proton)           = {fmt(q0, dps=OUT_DPS)}")
        print(f"hbar_q0 = 1 - q0^-1   = {fmt(hbar_q0, dps=OUT_DPS)}")
        print(f"h_q0    = q0 - q0^-1  = {fmt(h_q0, dps=OUT_DPS)}")
        print(f"Q_Koide^exp (CODATA)  = {fmt(q_exp_codata, dps=20)} +/- {fmt(q_exp_codata_err, dps=8)}")
        print(f"Q_Koide^exp (PDG-24)  = {fmt(q_exp_pdg24, dps=20)} +/- {fmt(q_exp_pdg24_err, dps=8)}")
        print(f"Q_Koide^exp - 2/3     = {fmt(q_exp_codata - two_thirds, dps=12)} (CODATA) | {fmt(q_exp_pdg24 - two_thirds, dps=12)} (PDG-24)")
        print(f"theta_exp (CODATA mu) = {fmt(theta_exp, dps=30)} rad (2/9 = {fmt(mp.mpf(2)/9, dps=30)})")
        print(f"d ln(m_mu/m_e)/dtheta = {fmt(exp_koide_spec['dln_mmu_me_dtheta'], dps=12)}")
        print(f"d ln(m_tau/m_e)/dtheta= {fmt(exp_koide_spec['dln_mtau_me_dtheta'], dps=12)}")
        print("\n--- Part A: Quadratic Resolvent m_tau/m_e Predictions (assuming exact Q = 2/3) ---")
        for k, v in part_a_results.items():
            print(
                f"  {k:28s}: m_mu/m_e={v['input_m_mu_over_m_e'][:14]} -> "
                f"m_tau/m_e={v['pred_m_tau_over_m_e'][:16]} "
                f"(CODATA: {v['sigma_pull_vs_codata_2022']}s, PDG-pre: {v['sigma_pull_vs_pdg_pre_belle2']}s, PDG-24: {v['sigma_pull_vs_pdg_2024']}s)"
            )
        print("\n--- Part B: Un-Tuned H_3(q0) / TL_3(q0) Operator Equipartition Tests ---")
        print(
            f"  Op_B4 TL_3(q0) Wedderburn: Q(1)=2/3 exact; Q(q0)={fmt(q_tl3_q0, dps=20)} "
            f"(diff={fmt(q_tl3_q0 - two_thirds, dps=12)}, {part_b_operators['Op_B4_TL3_convD_wedderburn_norm']['rel_shift_pct_vs_two_thirds']}%)"
        )
        for k_var, v_var in op_b6_variants.items():
            print(
                f"  Op_B6 Chiral Vertex ({k_var}): Q(q0)={v_var['koide_q'][:18]}, "
                f"diff={v_var['diff_vs_two_thirds']}"
            )
        print("\n--- Part C: Zero-Parameter Phase Tests (Q = 2/3) ---")
        for k, v in part_c_phases.items():
            print(
                f"  {k:38s}: theta={str(v['theta_rad'])[:12]} | "
                f"m_mu/m_e={str(v['pred_m_mu_over_m_e'])[:12]} ({v['rel_err_m_mu_pct']}%) | "
                f"m_tau/m_e={str(v['pred_m_tau_over_m_e'])[:12]} ({v['rel_err_m_tau_pct_vs_codata_2022']}%)"
            )
        print(f"\nGate G-2B Passed: {gate_g2b_passed}")

        # -------------------------------------------------------------------
        # Build & Save Schema-Validated Witness JSON
        # -------------------------------------------------------------------
        wb = WitnessBuilder(
            name="gap2b-mtau-s3-circulant-koide-probe",
            engine="mpmath",
            output_dir=Path(__file__).resolve().parent,
        )
        wb.set_description(
            "Pre-registered 80-dps algebraic and numerical test of S_3/Z_3 circulant square-root "
            "mass operators, Koide Q=2/3 singlet-doublet equipartition on Bring's 3-generation "
            "subspace projGen3, quadratic sqrt(m_tau) resolvent, and zero-parameter q_0 phase "
            "candidates (Open Gap 2 Backup / Option 2B, bean qou-j96h; CODATA-2022 & PDG-2024 uncertainties)."
        )
        wb.add_parameter("work_dps", WORK_DPS)
        wb.add_parameter("out_dps", OUT_DPS)
        wb.add_parameter("q0", fmt(q0, dps=OUT_DPS))
        wb.add_parameter("hbar_q0", fmt(hbar_q0, dps=OUT_DPS))
        wb.add_parameter("h_q0", fmt(h_q0, dps=OUT_DPS))
        wb.add_parameter("vol_4_1", fmt(vol41, dps=OUT_DPS))
        wb.add_parameter("preregistration", "computations/probes/gap2b_mtau_s3_circulant_koide_test/PREREGISTRATION.md")
        wb.add_parameter("lean_module", "folio/quantum-observable-universe/lean/QOU/StandardModel/S3CirculantKoideTraceIdentity.lean")

        wb.add_data("symbolic_verification", sym_res)
        wb.add_data(
            "empirical_benchmarks",
            {
                "m_e_mev_codata_2022": me_codata.value_str,
                "m_e_mev_uncert": me_codata.uncertainty_str,
                "m_mu_over_m_e_codata_2022": mu_codata.value_str,
                "m_mu_over_m_e_uncert": mu_codata.uncertainty_str,
                "m_tau_over_m_e_codata_2022": tau_codata.value_str,
                "m_tau_over_m_e_codata_uncert": tau_codata.uncertainty_str,
                "m_tau_mev_pdg_pre_belle2_codata_2022": tau_mev_codata.value_str,
                "m_tau_mev_pdg_pre_belle2_uncert": tau_mev_codata.uncertainty_str,
                "m_tau_over_m_e_pdg_pre_belle2": fmt(r_tau_pdg_pre, dps=OUT_DPS),
                "m_tau_over_m_e_pdg_pre_belle2_uncert": fmt(r_tau_pdg_pre_err, dps=20),
                "m_tau_mev_pdg_2024": "1776.93",
                "m_tau_mev_pdg_2024_uncert": "0.09",
                "m_tau_over_m_e_pdg_2024": fmt(r_tau_pdg24, dps=OUT_DPS),
                "m_tau_over_m_e_pdg_2024_uncert": fmt(r_tau_pdg24_err, dps=20),
                "koide_q_exp_codata_2022": fmt(q_exp_codata, dps=OUT_DPS),
                "koide_q_exp_codata_2022_uncert": fmt(q_exp_codata_err, dps=15),
                "koide_q_exp_codata_minus_two_thirds": fmt(q_exp_codata - two_thirds, dps=20),
                "koide_q_exp_pdg_pre_belle2": fmt(q_exp_pdg_pre, dps=OUT_DPS),
                "koide_q_exp_pdg_2024": fmt(q_exp_pdg24, dps=OUT_DPS),
                "koide_q_exp_pdg_2024_uncert": fmt(q_exp_pdg24_err, dps=15),
                "koide_q_exp_pdg_2024_minus_two_thirds": fmt(q_exp_pdg24 - two_thirds, dps=20),
                "theta_exp_rad": fmt(theta_exp, dps=OUT_DPS),
                "theta_chiral_zero_pi_over_12": fmt(theta_crit, dps=OUT_DPS),
                "theta_margin_to_electron_zero": fmt(theta_crit - theta_exp, dps=25),
                "dln_mmu_me_dtheta_at_exp": fmt(exp_koide_spec["dln_mmu_me_dtheta"], dps=20),
                "dln_mtau_me_dtheta_at_exp": fmt(exp_koide_spec["dln_mtau_me_dtheta"], dps=20),
            },
        )
        wb.add_data("part_a_quadratic_resolvent", part_a_results)
        wb.add_data("part_b_operator_equipartition", part_b_operators)
        wb.add_data("part_c_zero_parameter_phases", part_c_phases)
        wb.add_data(
            "gate_g2b_verdict",
            {
                "gate_g2b_passed": gate_g2b_passed,
                "any_untuned_q0_operator_passes_equipartition": any_operator_passes_equipartition,
                "any_q0_phase_passes_1pct_both_ratios": any_q0_phase_under_1pct_both,
                "selected_q0_operator": "none" if not gate_g2b_passed else "candidate_found",
                "disposition": "honest_falsification_of_untuned_q0_koide_closure_rule13a"
                if not gate_g2b_passed
                else "passed",
            },
        )

        # Assertions (using honest refutation/algebraic verification pattern per exploratory discipline)
        wb.add_assertion(
            "sympy_exact_circulant_koide_resolvent_and_tl3_identities",
            1 if sym_res["all_symbolic_identities_verified"] else 0,
            1,
            "0",
            source="S3CirculantKoideTraceIdentity.lean (§1-§5 exact ring/field identities)",
        )
        r1_rel_err = abs(
            (koide_tau_from_mu_ratio(r_mu_exp)["m_tau_over_m_e_pred"] - r_tau_codata) / r_tau_codata
        )
        wb.add_assertion(
            "classic_koide_cal1_cal2_resolvent_matches_mtau_within_100ppm",
            fmt(r1_rel_err, dps=15),
            "0",
            "1e-4",
            source="Koide 1983 (doi:10.1103/PhysRevD.28.252) quadratic resolvent on CODATA-2022 m_mu/m_e",
        )
        r2a_pull_codata = abs(
            (koide_tau_from_mu_ratio(r_mu_qou_bare)["m_tau_over_m_e_pred"] - r_tau_codata)
            / r_tau_codata_err
        )
        r2a_pull_pdg24 = abs(
            (koide_tau_from_mu_ratio(r_mu_qou_bare)["m_tau_over_m_e_pred"] - r_tau_pdg24)
            / r_tau_pdg24_err
        )
        wb.add_assertion(
            "qou_bare_vol41_koide_resolvent_within_1sigma_codata_and_pdg2024",
            1 if (r2a_pull_codata < 1 and r2a_pull_pdg24 < 1) else 0,
            1,
            "0",
            source="CODATA-2022 (3477.23 +/- 0.23, +0.923s) and PDG-2024 (1776.93 +/- 0.09 MeV -> 3477.3653 +/- 0.1761, +0.437s)",
        )
        wb.add_assertion(
            "tl3_finite_q0_deficit_identity_exact_80dps",
            fmt(tl3_deficit_identity_res, dps=15),
            "0",
            "1e-70",
            source="S3CirculantKoideTraceIdentity.tl3KoideNormRatio_closed_form_and_deficit",
        )
        wb.add_assertion(
            "tl3_strict_departure_below_two_thirds_at_q0",
            1 if (q_tl3_q0 < two_thirds and 2 * y21_q0 < y3_q0) else 0,
            1,
            "0",
            source="S3CirculantKoideTraceIdentity.tl3_strict_departure_from_two_thirds",
        )
        wb.add_assertion(
            "untuned_q0_operators_falsify_simultaneous_koide_gate_g2b",
            1 if (not gate_g2b_passed) else 0,
            1,
            "0",
            source="Pre-registered Gate G-2B honest refutation check (PREREGISTRATION.md §5)",
        )

        wb.add_caveat(
            "1. Unbroken S_3-equivariance on Bring's 3-generation space projGen3 forces b = c in "
            "S(a,b,c), leaving a degenerate 2D doublet (lambda_1 = lambda_2 = a - b); splitting all "
            "three charged leptons strictly requires chiral symmetry breaking S_3 -> Z_3 (b != c). "
            "2. While Temperley-Lieb Wedderburn trace weights (y_3, 2 y_21) achieve "
            "EXACT singlet-doublet equipartition (1/2 = 1/2, Q = 2/3) at the classical point q = 1, "
            "at finite q_0 = 1.10997858... they shift strictly below 2/3 by -(q_0 - q_0^-1)^2 / "
            "(3(q_0^2 + q_0^-2)) = -0.00712859 (-1.0693% relative, -1073 sigma vs CODATA-2022 "
            "Q_exp = 0.66666056(66) and -1402 sigma vs PDG-2024 Q_exp = 0.66666442(51)). "
            "3. Feeding QOU's parameter-free Vol(4_1)/hbar_{q_0}^2 into protected Q = 2/3 predicts "
            "m_tau/m_e = 3477.442306 (+61.06 ppm = +0.923 sigma vs CODATA-2022 3477.23 +/- 0.23, "
            "+61.55 ppm = +0.911 sigma vs PDG pre-Belle-II 1776.86 +/- 0.12 MeV / m_e = 3477.2283 +/- 0.2348, "
            "and +22.16 ppm = +0.437 sigma vs PDG-2024 1776.93 +/- 0.09 MeV / m_e = 3477.3653 +/- 0.1761). "
            "First-principles operator derivation of topological protection remains gated behind Rule-13a "
            "zero-instance class KoideTopologicalProtectionHypothesis / KoideCirculantEquipartitionHypothesis."
        )

        out = wb.save({"q0Anchor": "proton", "q0Value": fmt(q0, dps=OUT_DPS)})
        print(f"\nwitness -> {out}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
