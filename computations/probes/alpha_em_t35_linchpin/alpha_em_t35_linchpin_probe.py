#!/usr/bin/env python3
"""Pre-registered 80-dps probe for Q-Gap-1 (beans qou-15sj, qou-ha6c, qou-itdn, qou-006b).

EXPLORATORY shape-probe & exact algebraic witness corresponding to:
- Pre-registration: `computations/probes/alpha_em_t35_linchpin/PREREGISTRATION.md`
- Lean 4 module: `folio/quantum-observable-universe/lean/QOU/StandardModel/AlphaEmT35Linchpin.lean`

Evaluates at `mpmath.workdps(80)` (`q0Anchor = "proton"`, zero float64):
1. Part A: Exact T(3,5) symmetrized Alexander (t = q^2 and t = q^4), 3-strand reduced
   Burau determinant, standard Jones (N = 2), and U_q(sl_3) HOMFLY-PT (N = 3) invariants
   at q_0 (plus exact rational points q in {2, 3/2} and q = 1 selectivity) vs q [9]_q [10]_q.
2. Part B: All 15 pre-registered zero-parameter candidate closed forms for the weight-3
   archimedean two-loop photon self-energy Delta_2 against CODATA-2022 implied Delta_2^emp,
   reporting exact residuals, sigma distances, and q-locality slopes with zero post-hoc selection.
3. Part C: Hadron charge-line coupling t = exp(-alpha_EM(q_0)/2) (2 ln t = -alpha_EM(q_0)),
   alternating Taylor jet enclosure for 1 - t^2, two-term weak-vertex form factor
   W(q_0) = t_1 + c_em t_2 across the three zero-parameter c_em normalizations, and
   Gatermann-Parrilo / Verstichel-van Aggelen semidefinite positivity bounds on E(Q)^conn.
"""

from __future__ import annotations

import pathlib
import sys
from fractions import Fraction

_ROOT = pathlib.Path(__file__).resolve().parents[3]
for _p in (
    _ROOT / "tools" / "qou-substrate" / "python",
    _ROOT / "computations",
):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import mpmath as mp  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.constants import VOL_FIGURE_EIGHT_50_STR, q_at  # noqa: E402
from qou_substrate.precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

WORK_DPS = 80
OUT_DPS = 50
set_compute_dps(WORK_DPS)


def igcd(a: int, b: int) -> int:
    """Pure-integer Euclidean greatest common divisor (zero `math` module import)."""
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def q_int_bal(q: mp.mpf, n: int) -> mp.mpf:
    """Balanced quantum integer `[n]_q = (q^n - q^{-n}) / (q - q^{-1})`."""
    one = mp.mpf(1)
    qinv = one / q
    if q == one:
        return mp.mpf(n)
    return (q ** n - qinv ** n) / (q - qinv)


def delta_t35_laurent(q: mp.mpf) -> mp.mpf:
    """Symmetrized Alexander Laurent polynomial of T(3,5) at `t = q^2`."""
    one = mp.mpf(1)
    qinv = one / q
    return (
        q ** 8
        - q ** 6
        + q ** 2
        - one
        + qinv ** 2
        - qinv ** 6
        + qinv ** 8
    )


def delta_t35_quotient(q: mp.mpf) -> mp.mpf:
    """Torus-knot Alexander rational quotient at `t = q^2`."""
    one = mp.mpf(1)
    qinv = one / q
    num = (q - qinv) * (q ** 15 - qinv ** 15)
    den = (q ** 3 - qinv ** 3) * (q ** 5 - qinv ** 5)
    return num / den


def delta_t35_skein_laurent(q: mp.mpf) -> mp.mpf:
    """Symmetrized Alexander Laurent polynomial of T(3,5) at `t = q^4`."""
    one = mp.mpf(1)
    qinv = one / q
    return (
        q ** 16
        - q ** 12
        + q ** 4
        - one
        + qinv ** 4
        - qinv ** 12
        + qinv ** 16
    )


def delta_t35_skein_quotient(q: mp.mpf) -> mp.mpf:
    """Skein Alexander rational quotient `(q^2 - q^{-2})(q^30 - q^{-30}) / ((q^6 - q^{-6})(q^10 - q^{-10}))`."""
    one = mp.mpf(1)
    qinv = one / q
    num = (q ** 2 - qinv ** 2) * (q ** 30 - qinv ** 30)
    den = (q ** 6 - qinv ** 6) * (q ** 10 - qinv ** 10)
    return num / den


def jones_t35(t: mp.mpf) -> mp.mpf:
    """Standard Jones polynomial `V_{T(3,5)}(t) = t^4 + t^6 - t^10`."""
    return t ** 4 + t ** 6 - t ** 10


def weak_vertex_trace_conv_d(q: mp.mpf) -> mp.mpf:
    """Convention-D Markov trace `W(q) = q^2 (q^12 + q^8 - 1) / (q^2 + 1)^2`."""
    one = mp.mpf(1)
    return (q ** 2) * (q ** 12 + q ** 8 - one) / ((q ** 2 + one) ** 2)


def homfly_sl3_t35_schur(q: mp.mpf) -> mp.mpf:
    """Framed `U_q(sl_3)` HOMFLY-PT evaluation `P_{T(3,5)}^{(N=3)}(q)` from 3-irrep Schur dimensions."""
    one = mp.mpf(1)
    qinv = one / q
    d_3 = q_int_bal(q, 4) * q_int_bal(q, 5) / q_int_bal(q, 2)
    d_21 = q_int_bal(q, 2) * q_int_bal(q, 4)
    d_111 = one
    unframed = (d_3 * (q ** 10) - d_21 + d_111 * (qinv ** 10)) / q_int_bal(q, 3)
    return (q ** (-30)) * unframed


def homfly_sl3_t35_laurent(q: mp.mpf) -> mp.mpf:
    """Closed-form 6-term Laurent polynomial for `P_{T(3,5)}^{(N=3)}(q)`."""
    one = mp.mpf(1)
    qinv = one / q
    unframed = (
        q ** 14
        + q ** 10
        + q ** 8
        - mp.mpf(2)
        - qinv ** 6
        + qinv ** 8
    )
    return (q ** (-30)) * unframed


def solve_alpha_inv_with_c2(
    q_val: mp.mpf,
    c2_add: mp.mpf,
    include_h2_form_b: bool = True,
) -> mp.mpf:
    """Solve `1/alpha = q[9]_q[10]_q + 2/(3*pi) + alpha*H*(1 - h^2*alpha) + c2_add*alpha^2` at 85 dps."""
    with mp.workdps(85):
        q = mp.mpf(q_val)
        c2 = mp.mpf(c2_add)
        one = mp.mpf(1)
        h = q - one / q
        h2 = h * h if include_h2_form_b else mp.mpf(0)
        two_q = q + one / q
        q9 = q_int_bal(q, 9)
        q10 = q_int_bal(q, 10)
        t_term = q * q9 * q10 + mp.mpf(2) / (mp.mpf(3) * mp.pi)
        h_term = two_q / (mp.mpf(8) * mp.pi)
        # Equation: (-h_term * h2 + c2?? Wait: 1/a = t_term + a*h_term - a^2*h_term*h2 + c2*a^2)
        # Multiply by `a`: `(c2 - h_term * h2) * a^3 + h_term * a^2 + t_term * a - 1 = 0`.
        quad_disc = t_term * t_term + mp.mpf(4) * h_term
        a = (-t_term + mp.sqrt(quad_disc)) / (mp.mpf(2) * h_term)
        cubic_coeff = c2 - h_term * h2
        for _ in range(45):
            fa = cubic_coeff * (a ** 3) + h_term * (a ** 2) + t_term * a - one
            dfa = (
                mp.mpf(3) * cubic_coeff * (a ** 2)
                + mp.mpf(2) * h_term * a
                + t_term
            )
            da = fa / dfa
            a -= da
            if abs(da) < mp.mpf(10) ** (-82):
                break
        return one / a


def kappa_weak_vertex(q: mp.mpf, charges: tuple[mp.mpf, mp.mpf, mp.mpf]) -> mp.mpf:
    """Connected coefficient `kappa(q, Q) = sum_b Q_b (q^{2b}/(1 + q^2 + q^4) - 1/3)`."""
    one = mp.mpf(1)
    three = mp.mpf(3)
    nrm = one + q ** 2 + q ** 4
    q0_c, q1_c, q2_c = charges
    return (
        q0_c * (one / nrm - one / three)
        + q1_c * ((q ** 2) / nrm - one / three)
        + q2_c * ((q ** 4) / nrm - one / three)
    )


def t_two_weak_vertex(
    q: mp.mpf,
    qp: tuple[mp.mpf, mp.mpf, mp.mpf],
    qm: tuple[mp.mpf, mp.mpf, mp.mpf],
) -> mp.mpf:
    """Connected second-term `t_2(q, Q_+, Q_-)` from `WeakVertexTwoTerm.tTwo_eq`."""
    one = mp.mpf(1)
    two = mp.mpf(2)
    kp = kappa_weak_vertex(q, qp)
    km = kappa_weak_vertex(q, qm)
    qd2 = q + one / q
    return (q * kp + (one / q) * km) * (two * (q ** 10) + one) / (two * (qd2 ** 3))


def p3_variance(q: mp.mpf, charges: tuple[mp.mpf, mp.mpf, mp.mpf]) -> tuple[mp.mpf, mp.mpf]:
    """Compute both `Var_{P_3}(Q)` and `-(1/2) Tr([diag(Q), P_3]^2)` independently."""
    one = mp.mpf(1)
    two = mp.mpf(2)
    nrm = one + q ** 2 + q ** 4
    weights = [one / nrm, (q ** 2) / nrm, (q ** 4) / nrm]
    mean_q = sum(charges[i] * weights[i] for i in range(3))
    mean_q2 = sum((charges[i] ** 2) * weights[i] for i in range(3))
    var_p3 = mean_q2 - mean_q ** 2

    # Explicit 3x3 Hilbert-Schmidt sum `(1/2) sum_{i,j} ((Q_i - Q_j) P3_{i,j})^2`
    v = [one, q, q ** 2]
    hs_sum = mp.mpf(0)
    for i in range(3):
        for j in range(3):
            p3_ij = v[i] * v[j] / nrm
            comm_ij = (charges[i] - charges[j]) * p3_ij
            hs_sum += (comm_ij ** 2) / two
    return var_p3, hs_sum


def main() -> int:
    with mp.workdps(WORK_DPS):
        one = mp.mpf(1)
        two = mp.mpf(2)
        three = mp.mpf(3)
        four = mp.mpf(4)
        eight = mp.mpf(8)
        nine = mp.mpf(9)
        twelve = mp.mpf(12)

        q0 = q_at(WORK_DPS)
        q0_inv = one / q0
        h0 = q0 - q0_inv
        hbar0 = one - q0_inv
        vol_41 = two * mp.clsin(2, mp.pi / three)
        vol_41_ref = mp.mpf(VOL_FIGURE_EIGHT_50_STR)
        zeta3 = mp.zeta(3)

        # Experimental CODATA-2022 comparison datum ONLY (never enters substrate formulas)
        codata_alpha_inv_entry = codata("inverse fine-structure constant")
        alpha_inv_codata2022 = mp.mpf(codata_alpha_inv_entry.value_str)
        sigma_alpha_inv_codata2022 = mp.mpf(codata_alpha_inv_entry.uncertainty_str)
        # Historical CODATA-2018 central value recorded solely to explain -0.313 vs -0.365 ppb note
        alpha_inv_codata2018_hist = mp.mpf("137.035999084")

        wb = WitnessBuilder(
            "alpha-em-t35-linchpin",
            engine="mpmath-80dps",
            output_dir=pathlib.Path(__file__).resolve().parent,
        )
        wb.set_description(
            "80-dps pre-registered verification of QOU/StandardModel/AlphaEmT35Linchpin.lean "
            "(beans qou-15sj, qou-ha6c, qou-itdn, qou-006b): exact T(3,5) Alexander, Burau, "
            "Jones, and U_q(sl_3) HOMFLY-PT invariants vs q[9]_q[10]_q; zero-parameter weight-3 "
            "two-loop Delta_2 candidate tests against CODATA-2022; hadron charge-line coupling "
            "2 ln t = -alpha_EM(q_0); and Gatermann-Parrilo / Verstichel-van Aggelen positivity "
            "bounds on E(Q)^conn."
        )
        wb.add_parameter("work_dps", WORK_DPS)
        wb.add_parameter("out_dps", OUT_DPS)
        wb.add_parameter("q0_proton", fmt(q0, dps=OUT_DPS))

        # ── PART A: T(3,5) Invariants & [10]_q Linchpin ───────────────────────
        genus4_hits: list[tuple[int, int]] = []
        for p in range(2, 31):
            for r in range(p + 1, 31):
                if igcd(p, r) == 1 and (p - 1) * (r - 1) == 8:
                    genus4_hits.append((p, r))

        # Exact rational verification at q = 2 and q = 3/2
        rational_checks: dict[str, str] = {}
        for q_frac in (Fraction(2, 1), Fraction(3, 2)):
            qi = Fraction(1, 1) / q_frac
            alex_laur = (
                q_frac ** 8 - q_frac ** 6 + q_frac ** 2 - 1 + qi ** 2 - qi ** 6 + qi ** 8
            )
            alex_quot = (
                (q_frac - qi)
                * (q_frac ** 15 - qi ** 15)
                / ((q_frac ** 3 - qi ** 3) * (q_frac ** 5 - qi ** 5))
            )
            assert alex_laur == alex_quot
            rational_checks[f"delta_T35_q={q_frac}"] = str(alex_laur)

        # 80-dps evaluations at q_0
        q9_0 = q_int_bal(q0, 9)
        q10_0 = q_int_bal(q0, 10)
        q2_0 = q_int_bal(q0, 2)
        q3_0 = q_int_bal(q0, 3)
        tree_bare_0 = q0 * q9_0 * q10_0
        cg_sum_0 = sum(q_int_bal(q0, 2 * k) for k in range(1, 10))
        cg_diff = abs(q9_0 * q10_0 - cg_sum_0)

        alex_q2_laur_0 = delta_t35_laurent(q0)
        alex_q2_quot_0 = delta_t35_quotient(q0)
        alex_q2_diff = abs(alex_q2_laur_0 - alex_q2_quot_0)

        alex_q4_laur_0 = delta_t35_skein_laurent(q0)
        alex_q4_quot_0 = delta_t35_skein_quotient(q0)
        alex_q4_diff = abs(alex_q4_laur_0 - alex_q4_quot_0)

        cyclotomic_q10_q2_lhs = ((q0 ** 10 - q0_inv ** 10) * (q0 + q0_inv)) / (q0 - q0_inv)
        cyclotomic_q10_q2_rhs = q10_0 * q2_0
        cyclotomic_diff = abs(cyclotomic_q10_q2_lhs - cyclotomic_q10_q2_rhs)

        burau_poly_0 = one + q0 ** 10 + q0 ** 20
        burau_quot_0 = (one - q0 ** 30) / (one - q0 ** 10)
        burau_diff = abs(burau_poly_0 - burau_quot_0)

        jones_pos_0 = jones_t35(q0 ** 2)
        jones_mir_0 = jones_t35(q0_inv ** 2)
        w_conv_d_0 = weak_vertex_trace_conv_d(q0)
        jones_markov_num_diff = abs(
            (q0 ** 2) * (q0 ** 12 + q0 ** 8 - one) - (q0 ** 22) * jones_mir_0
        )

        homfly_sl3_schur_0 = homfly_sl3_t35_schur(q0)
        homfly_sl3_laur_0 = homfly_sl3_t35_laurent(q0)
        homfly_sl3_diff = abs(homfly_sl3_schur_0 - homfly_sl3_laur_0)

        # Classical q = 1 selectivity (qou-itdn)
        v_at_1_c1 = (-2) ** (1 - 1)
        v_at_1_c2 = (-2) ** (2 - 1)
        v_at_1_c3 = (-2) ** (3 - 1)
        t_tree_at_1 = mp.exp(-one / mp.mpf(180))

        wb.add_data(
            "part_a_t35_invariants_and_linchpin",
            {
                "diophantine_genus4_coprime_knots": [f"T({p},{r})" for p, r in genus4_hits],
                "exact_rational_checks": rational_checks,
                "q9_q0": fmt(q9_0, dps=OUT_DPS),
                "q10_q0": fmt(q10_0, dps=OUT_DPS),
                "tree_q_q9_q10_q0": fmt(tree_bare_0, dps=OUT_DPS),
                "clebsch_gordan_abs_diff": fmt(cg_diff, dps=15),
                "delta_T35_at_q0_sq": fmt(alex_q2_laur_0, dps=OUT_DPS),
                "delta_T35_at_q0_fourth": fmt(alex_q4_laur_0, dps=OUT_DPS),
                "burau_det_1_plus_q10_plus_q20": fmt(burau_poly_0, dps=OUT_DPS),
                "jones_T35_q0_sq": fmt(jones_pos_0, dps=OUT_DPS),
                "jones_T35_q0_inv_sq": fmt(jones_mir_0, dps=OUT_DPS),
                "weak_vertex_convD_W_q0": fmt(w_conv_d_0, dps=OUT_DPS),
                "homfly_sl3_T35_q0": fmt(homfly_sl3_laur_0, dps=OUT_DPS),
                "q1_selectivity": {
                    "V_knot_c1_at_q1": v_at_1_c1,
                    "V_hopf_c2_at_q1": v_at_1_c2,
                    "V_borromean_c3_at_q1": v_at_1_c3,
                    "tree_alpha_inv_at_q1": 90,
                    "hadron_line_t_tree_at_q1": fmt(t_tree_at_1, dps=30),
                },
            },
        )

        # ── PART B: Pre-Registered Weight-3 Two-Loop Delta_2 Candidate Test ───
        alpha_inv_form_b = solve_alpha_inv_with_c2(q0, mp.mpf(0), include_h2_form_b=True)
        alpha_form_b = one / alpha_inv_form_b
        alpha_inv_form_a = solve_alpha_inv_with_c2(q0, mp.mpf(0), include_h2_form_b=False)
        alpha_form_a = one / alpha_inv_form_a

        delta2_emp_2022 = alpha_inv_codata2022 - alpha_inv_form_b
        resid_form_b_2022_ppb = (
            (alpha_inv_form_b - alpha_inv_codata2022) / alpha_inv_codata2022 * mp.mpf(10) ** 9
        )
        resid_form_b_2018_ppb = (
            (alpha_inv_form_b - alpha_inv_codata2018_hist)
            / alpha_inv_codata2018_hist
            * mp.mpf(10) ** 9
        )
        c2_plus_emp_2022 = delta2_emp_2022 / (alpha_form_b ** 2)
        c2_minus_emp_2022 = -c2_plus_emp_2022
        sigma_rel_ppb = sigma_alpha_inv_codata2022 / alpha_inv_codata2022 * mp.mpf(10) ** 9

        # Define the 14 symmetric magnitude functions |c_2|(q) + C4b replacement function
        def cand_c1a(_q: mp.mpf) -> mp.mpf:
            return mp.zeta(3) / (mp.pi ** 3)

        def cand_c1b(_q: mp.mpf) -> mp.mpf:
            return mp.zeta(3) / (eight * (mp.pi ** 3))

        def cand_c1c(_q: mp.mpf) -> mp.mpf:
            return mp.zeta(3) / ((eight * mp.pi) ** 2)

        def cand_c1d(_q: mp.mpf) -> mp.mpf:
            return one / (four * (mp.pi ** 2))

        def cand_c1e(_q: mp.mpf) -> mp.mpf:
            return three * mp.zeta(3) / (four * (mp.pi ** 2))

        def cand_c2a(_q: mp.mpf) -> mp.mpf:
            v41 = two * mp.clsin(2, mp.pi / three)
            return v41 / (mp.pi ** 2)

        def cand_c2b(_q: mp.mpf) -> mp.mpf:
            v41 = two * mp.clsin(2, mp.pi / three)
            return v41 / (two * (mp.pi ** 2))

        def cand_c2c(_q: mp.mpf) -> mp.mpf:
            v41 = two * mp.clsin(2, mp.pi / three)
            return v41 / ((eight * mp.pi) ** 2)

        def cand_c2d(_q: mp.mpf) -> mp.mpf:
            v41 = two * mp.clsin(2, mp.pi / three)
            return v41 / ((twelve * mp.pi) ** 2)

        def cand_c3a(q: mp.mpf) -> mp.mpf:
            hq = q - one / q
            return (hq ** 2) * mp.zeta(3)

        def cand_c3b(q: mp.mpf) -> mp.mpf:
            hq = q - one / q
            return (hq ** 2) * mp.zeta(3) / (eight * mp.pi)

        def cand_c3c(q: mp.mpf) -> mp.mpf:
            hb = one - one / q
            return (hb ** 2) * mp.zeta(3) / (mp.pi ** 2)

        def cand_c3d(q: mp.mpf) -> mp.mpf:
            return q_int_bal(q, 3) * mp.zeta(3) / ((eight * mp.pi) ** 2)

        def cand_c4a(q: mp.mpf) -> mp.mpf:
            return q_int_bal(q, 3) / ((eight * mp.pi) ** 2)

        symmetric_candidates = [
            ("C1a_schwinger_broadhurst_zeta3_pi3", cand_c1a),
            ("C1b_bring_b1_zeta3_8pi3", cand_c1b),
            ("C1c_bring_jacobian_zeta3_64pi2", cand_c1c),
            ("C1d_jost_luttinger_1_4pi2", cand_c1d),
            ("C1e_petermann_sommerfield_3zeta3_4pi2", cand_c1e),
            ("C2a_bloch_wigner_vol41_pi2", cand_c2a),
            ("C2b_single_tetra_D41_pi2", cand_c2b),
            ("C2c_bring_jacobian_vol41_64pi2", cand_c2c),
            ("C2d_bring_area_vol41_144pi2", cand_c2d),
            ("C3a_habiro_h0sq_zeta3", cand_c3a),
            ("C3b_habiro_h0sq_zeta3_8pi", cand_c3b),
            ("C3c_habiro_hbar0sq_zeta3_pi2", cand_c3c),
            ("C3d_theta_weight3_q3_zeta3_64pi2", cand_c3d),
            ("C4a_penrose_theta_q3_64pi2_on_formB", cand_c4a),
        ]

        dq_win = mp.mpf("0.05")
        dq_tiny = mp.mpf(10) ** (-25)
        candidate_rows: list[dict[str, object]] = []
        passes_1sigma: list[str] = []
        passes_2sigma: list[str] = []

        for cid, cfn in symmetric_candidates:
            mag0 = cfn(q0)
            for sgn_label, sgn_val in (("plus", one), ("minus", -one)):
                ainv_0 = solve_alpha_inv_with_c2(q0, sgn_val * mag0, include_h2_form_b=True)
                ainv_hi = solve_alpha_inv_with_c2(
                    q0 + dq_tiny,
                    sgn_val * cfn(q0 + dq_tiny),
                    include_h2_form_b=True,
                )
                ainv_lo = solve_alpha_inv_with_c2(
                    q0 - dq_tiny,
                    sgn_val * cfn(q0 - dq_tiny),
                    include_h2_form_b=True,
                )
                dln_inv_dln_q = (
                    (mp.log(ainv_hi) - mp.log(ainv_lo)) / (two * dq_tiny) * q0
                )
                # Window residual slope across [q0 - 0.05, q0 + 0.05] in ppm/q
                ainv_w_hi = solve_alpha_inv_with_c2(
                    q0 + dq_win,
                    sgn_val * cfn(q0 + dq_win),
                    include_h2_form_b=True,
                )
                ainv_w_lo = solve_alpha_inv_with_c2(
                    q0 - dq_win,
                    sgn_val * cfn(q0 - dq_win),
                    include_h2_form_b=True,
                )
                slope_ppm_per_q = (
                    ((ainv_w_hi - ainv_w_lo) / alpha_inv_codata2022)
                    * (mp.mpf(10) ** 6)
                    / (two * dq_win)
                )
                abs_err = abs(ainv_0 - alpha_inv_codata2022)
                resid_ppb = (
                    (ainv_0 - alpha_inv_codata2022) / alpha_inv_codata2022 * (mp.mpf(10) ** 9)
                )
                n_sigma = abs_err / sigma_alpha_inv_codata2022
                tag = f"{cid}_{sgn_label}"
                if n_sigma <= one:
                    verdict = "PASS_1SIGMA"
                    passes_1sigma.append(tag)
                    passes_2sigma.append(tag)
                elif n_sigma <= two:
                    verdict = "CONSISTENT_2SIGMA"
                    passes_2sigma.append(tag)
                else:
                    verdict = "MISS_OUTSIDE_2SIGMA"
                candidate_rows.append(
                    {
                        "id": tag,
                        "c2_signed_at_q0": fmt(sgn_val * mag0, dps=20),
                        "alpha_inv_q0": fmt(ainv_0, dps=25),
                        "residual_vs_codata2022_ppb": fmt(resid_ppb, dps=12),
                        "abs_sigma": fmt(n_sigma, dps=10),
                        "d_ln_alpha_inv_d_ln_q": fmt(dln_inv_dln_q, dps=12),
                        "window_slope_ppm_per_q": fmt(slope_ppm_per_q, dps=10),
                        "verdict": verdict,
                    }
                )

        # Evaluate C4b: Penrose theta-graph `-[3]_q/(8*pi)^2` on Form A (replacing `-h^2 H`)
        c4b_c2_on_form_a_0 = -cand_c4a(q0)
        c4b_delta_vs_form_b_0 = c4b_c2_on_form_a_0 + (h0 ** 2) * (q2_0 / (eight * mp.pi))
        ainv_c4b_0 = solve_alpha_inv_with_c2(q0, c4b_c2_on_form_a_0, include_h2_form_b=False)
        ainv_c4b_hi = solve_alpha_inv_with_c2(
            q0 + dq_tiny, -cand_c4a(q0 + dq_tiny), include_h2_form_b=False
        )
        ainv_c4b_lo = solve_alpha_inv_with_c2(
            q0 - dq_tiny, -cand_c4a(q0 - dq_tiny), include_h2_form_b=False
        )
        dln_c4b = (mp.log(ainv_c4b_hi) - mp.log(ainv_c4b_lo)) / (two * dq_tiny) * q0
        resid_c4b_ppb = (
            (ainv_c4b_0 - alpha_inv_codata2022) / alpha_inv_codata2022 * (mp.mpf(10) ** 9)
        )
        nsigma_c4b = abs(ainv_c4b_0 - alpha_inv_codata2022) / sigma_alpha_inv_codata2022
        if nsigma_c4b <= one:
            verdict_c4b = "PASS_1SIGMA"
            passes_1sigma.append("C4b_penrose_theta_replace_formB_h0sq")
            passes_2sigma.append("C4b_penrose_theta_replace_formB_h0sq")
        elif nsigma_c4b <= two:
            verdict_c4b = "CONSISTENT_2SIGMA"
            passes_2sigma.append("C4b_penrose_theta_replace_formB_h0sq")
        else:
            verdict_c4b = "MISS_OUTSIDE_2SIGMA"
        candidate_rows.append(
            {
                "id": "C4b_penrose_theta_replace_formB_h0sq",
                "c2_on_formA_at_q0": fmt(c4b_c2_on_form_a_0, dps=20),
                "effective_delta_c2_vs_formB_at_q0": fmt(c4b_delta_vs_form_b_0, dps=20),
                "alpha_inv_q0": fmt(ainv_c4b_0, dps=25),
                "residual_vs_codata2022_ppb": fmt(resid_c4b_ppb, dps=12),
                "abs_sigma": fmt(nsigma_c4b, dps=10),
                "d_ln_alpha_inv_d_ln_q": fmt(dln_c4b, dps=12),
                "verdict": verdict_c4b,
            }
        )

        wb.add_data(
            "part_b_two_loop_delta2_candidates",
            {
                "alpha_inv_formB_q0": fmt(alpha_inv_form_b, dps=OUT_DPS),
                "alpha_inv_formA_q0": fmt(alpha_inv_form_a, dps=OUT_DPS),
                "alpha_inv_codata2022": fmt(alpha_inv_codata2022, dps=20),
                "sigma_alpha_inv_codata2022": fmt(sigma_alpha_inv_codata2022, dps=10),
                "sigma_rel_ppb": fmt(sigma_rel_ppb, dps=10),
                "formB_residual_vs_codata2022_ppb": fmt(resid_form_b_2022_ppb, dps=12),
                "formB_residual_vs_codata2018_hist_ppb": fmt(resid_form_b_2018_ppb, dps=12),
                "delta2_emp_codata2022": fmt(delta2_emp_2022, dps=20),
                "c2_plus_emp_codata2022": fmt(c2_plus_emp_2022, dps=20),
                "c2_minus_emp_codata2022": fmt(c2_minus_emp_2022, dps=20),
                "passes_1sigma": passes_1sigma,
                "passes_2sigma": passes_2sigma,
                "candidates": candidate_rows,
            },
        )

        # ── PART C: Hadron Charge-Line 2 ln t = -alpha_EM(q_0), c_em & E(Q)^conn Positivity ──
        t_hadron_0 = mp.exp(-alpha_form_b / two)
        two_log_t_0 = two * mp.log(t_hadron_0)
        log_bridge_err = abs(two_log_t_0 - (-alpha_form_b))

        one_minus_t_sq = one - (t_hadron_0 ** 2)
        jet2_lower = alpha_form_b - (alpha_form_b ** 2) / two
        jet3_upper = jet2_lower + (alpha_form_b ** 3) / mp.mpf(6)
        jet_lower_slack = one_minus_t_sq - jet2_lower
        jet_upper_slack = jet3_upper - one_minus_t_sq

        # Three zero-parameter c_em normalizations
        c_em_n1_mon = alpha_form_b
        c_em_n2_jet = one_minus_t_sq
        c_em_n3_lag = alpha_form_b / hbar0

        # Weak-vertex two-term evaluations
        qp_unif = (-one / nine, -one / nine, -one / nine)
        qm_unif = (-one / nine, -one / nine, -one / nine)
        t2_uniform_0 = t_two_weak_vertex(q0, qp_unif, qm_unif)

        qp_lep0 = (-two / nine, -two / nine, -eight / nine)
        qm_lep0 = (one / nine, -mp.mpf(5) / nine, -mp.mpf(5) / nine)
        t2_lep0_0 = t_two_weak_vertex(q0, qp_lep0, qm_lep0)
        t2_lep0_closed = (
            -two
            * (q0 ** 2)
            * (q0 ** 2 - one)
            * (two * (q0 ** 10) + one)
            / (nine * ((q0 ** 2 + one) ** 3))
        )
        t2_lep0_diff = abs(t2_lep0_0 - t2_lep0_closed)

        w_two_term_n1 = w_conv_d_0 + c_em_n1_mon * t2_lep0_0
        w_two_term_n2 = w_conv_d_0 + c_em_n2_jet * t2_lep0_0
        w_two_term_n3 = w_conv_d_0 + c_em_n3_lag * t2_lep0_0

        # Gatermann-Parrilo / Verstichel-van Aggelen positivity diagnostics on W_{+1} and W_{-1}
        kp_lep0 = kappa_weak_vertex(q0, qp_lep0)
        km_lep0 = kappa_weak_vertex(q0, qm_lep0)
        var_p3_plus, hs_plus = p3_variance(q0, qp_lep0)
        var_p3_minus, hs_minus = p3_variance(q0, qm_lep0)
        hs_var_diff_plus = abs(var_p3_plus - hs_plus)
        hs_var_diff_minus = abs(var_p3_minus - hs_minus)

        # Cauchy-Schwarz check `kappa(Q)^2 <= (sum_b (d_b - 1/3)^2) * (sum_b (Q_b - Q_bar)^2)`
        nrm0 = one + q0 ** 2 + q0 ** 4
        d_vec = [one / nrm0, (q0 ** 2) / nrm0, (q0 ** 4) / nrm0]
        d_dev_sq = sum((d_b - one / three) ** 2 for d_b in d_vec)
        qp_bar = sum(qp_lep0) / three
        qm_bar = sum(qm_lep0) / three
        qp_dev_sq = sum((qb - qp_bar) ** 2 for qb in qp_lep0)
        qm_dev_sq = sum((qb - qm_bar) ** 2 for qb in qm_lep0)
        cs_slack_plus = d_dev_sq * qp_dev_sq - (kp_lep0 ** 2)
        cs_slack_minus = d_dev_sq * qm_dev_sq - (km_lep0 ** 2)

        psd_checks: dict[str, dict[str, str | bool]] = {}
        for cname, cval in (
            ("N1_monodromy_alpha", c_em_n1_mon),
            ("N2_chordal_jet_1_minus_t2", c_em_n2_jet),
            ("N3_lagrangian_alpha_over_hbarq", c_em_n3_lag),
        ):
            ck_p = cval * kp_lep0
            ck_m = cval * km_lep0
            eig_p_3 = one + ck_p
            eig_p_21 = one - ck_p / two
            eig_m_3 = one + ck_m
            eig_m_21 = one - ck_m / two
            psd_ok = bool(
                (-one <= ck_p <= two)
                and (-one <= ck_m <= two)
                and (eig_p_3 >= 0)
                and (eig_p_21 >= 0)
                and (eig_m_3 >= 0)
                and (eig_m_21 >= 0)
            )
            psd_checks[cname] = {
                "c_em": fmt(cval, dps=25),
                "c_em_mul_kappa_plus": fmt(ck_p, dps=20),
                "c_em_mul_kappa_minus": fmt(ck_m, dps=20),
                "dressed_eig_Wplus_3": fmt(eig_p_3, dps=20),
                "dressed_eig_Wplus_21": fmt(eig_p_21, dps=20),
                "dressed_eig_Wminus_3": fmt(eig_m_3, dps=20),
                "dressed_eig_Wminus_21": fmt(eig_m_21, dps=20),
                "gatermann_parrilo_psd_holds": psd_ok,
            }

        wb.add_data(
            "part_c_hadron_line_and_two_term_positivity",
            {
                "t_hadron_q0": fmt(t_hadron_0, dps=OUT_DPS),
                "two_ln_t_q0": fmt(two_log_t_0, dps=OUT_DPS),
                "one_minus_t_sq_q0": fmt(one_minus_t_sq, dps=OUT_DPS),
                "jet2_lower_alpha_minus_half_alpha2": fmt(jet2_lower, dps=OUT_DPS),
                "jet3_upper_alpha_minus_half_alpha2_plus_sixth_alpha3": fmt(
                    jet3_upper, dps=OUT_DPS
                ),
                "jet_lower_slack": fmt(jet_lower_slack, dps=20),
                "jet_upper_slack": fmt(jet_upper_slack, dps=20),
                "weak_vertex_t1_q0": fmt(w_conv_d_0, dps=OUT_DPS),
                "weak_vertex_t2_uniform_q0": fmt(t2_uniform_0, dps=20),
                "weak_vertex_t2_lepton_first_q0": fmt(t2_lep0_0, dps=OUT_DPS),
                "W_two_term_N1_monodromy": fmt(w_two_term_n1, dps=OUT_DPS),
                "W_two_term_N2_chordal_jet": fmt(w_two_term_n2, dps=OUT_DPS),
                "W_two_term_N3_lagrangian_reeb": fmt(w_two_term_n3, dps=OUT_DPS),
                "kappa_Wplus_lepton_first": fmt(kp_lep0, dps=30),
                "kappa_Wminus_lepton_first": fmt(km_lep0, dps=30),
                "var_P3_Wplus": fmt(var_p3_plus, dps=30),
                "var_P3_Wminus": fmt(var_p3_minus, dps=30),
                "cauchy_schwarz_slack_Wplus": fmt(cs_slack_plus, dps=20),
                "cauchy_schwarz_slack_Wminus": fmt(cs_slack_minus, dps=20),
                "gatermann_parrilo_psd_checks": psd_checks,
            },
        )

        # ── ASSERTIONS (strictly algebraic & honest pre-registered outcomes) ──
        wb.add_assertion(
            "diophantine_genus4_uniqueness_T29_T35",
            len(genus4_hits),
            2,
            "0",
            source="AlphaEmT35Linchpin.genus_four_coprime_torus_knot_iff",
        )
        wb.add_assertion(
            "delta_T35_q0_sq_quotient_eq_laurent",
            fmt(alex_q2_diff, dps=15),
            "0",
            "1e-70",
            source="AlphaEmT35Linchpin.deltaT35_at_q_sq",
        )
        wb.add_assertion(
            "delta_T35_q0_fourth_quotient_eq_laurent",
            fmt(alex_q4_diff, dps=15),
            "0",
            "1e-70",
            source="AlphaEmT35Linchpin.deltaT35_at_q_fourth",
        )
        wb.add_assertion(
            "burau_det_T35_identity_at_q0",
            fmt(burau_diff, dps=15),
            "0",
            "1e-65",
            source="AlphaEmT35Linchpin.burau_det_T35_from_hecke",
        )
        wb.add_assertion(
            "cyclotomic_q10_q2_identity_at_q0",
            fmt(cyclotomic_diff, dps=15),
            "0",
            "1e-70",
            source="AlphaEmT35Linchpin.qIntBal_9_10_laurent_and_cyclotomic",
        )
        wb.add_assertion(
            "clebsch_gordan_q9_mul_q10_at_q0",
            fmt(cg_diff, dps=15),
            "0",
            "1e-70",
            source="AlphaEmT35Linchpin.qIntBal_nine_mul_ten_clebsch_gordan",
        )
        wb.add_assertion(
            "homfly_sl3_T35_schur_eq_laurent_at_q0",
            fmt(homfly_sl3_diff, dps=15),
            "0",
            "1e-70",
            source="AlphaEmT35Linchpin.homflySl3_T35_exact",
        )
        wb.add_assertion(
            "jones_markov_numerator_identity_at_q0",
            fmt(jones_markov_num_diff, dps=15),
            "0",
            "1e-65",
            source="WeakVertexT35.weakVertexTrace_numerator_eq_jones",
        )
        wb.add_assertion(
            "vol_4_1_clausen_matches_substrate_50str",
            fmt(abs(vol_41 - vol_41_ref), dps=15),
            "0",
            "1e-48",
            source="Vol(4_1) = 2 * Cl_2(pi/3)",
        )
        wb.add_assertion(
            "hadron_line_two_ln_t_eq_neg_alpha_B",
            fmt(log_bridge_err, dps=15),
            "0",
            "1e-75",
            source="AlphaEmT35Linchpin.two_log_hadronLineParam_eq_neg_alpha",
        )
        wb.add_assertion(
            "hadron_line_jet_bounds_hold_strictly",
            int(jet_lower_slack > 0 and jet_upper_slack > 0),
            1,
            "0",
            source="AlphaEmT35Linchpin.hadronLine_jet_bounds",
        )
        wb.add_assertion(
            "weak_vertex_t2_uniform_charges_vanish",
            fmt(abs(t2_uniform_0), dps=15),
            "0",
            "1e-75",
            source="WeakVertexTwoTerm.twoTerm_eq_of_uniform",
        )
        wb.add_assertion(
            "weak_vertex_t2_lepton_first_closed_form",
            fmt(t2_lep0_diff, dps=15),
            "0",
            "1e-75",
            source="WeakVertexTwoTerm.tTwo_lepton_first",
        )
        wb.add_assertion(
            "inner_deriv_hilbert_schmidt_eq_P3_variance",
            fmt(max(hs_var_diff_plus, hs_var_diff_minus), dps=15),
            "0",
            "1e-75",
            source="AlphaEmT35Linchpin.innerDeriv_P3_hilbert_schmidt_variance",
        )
        wb.add_assertion(
            "gatermann_parrilo_dressed_kernel_psd_all_normalizations",
            int(
                all(
                    bool(v["gatermann_parrilo_psd_holds"])
                    for v in psd_checks.values()
                )
                and cs_slack_plus >= 0
                and cs_slack_minus >= 0
            ),
            1,
            "0",
            source="AlphaEmT35Linchpin.dressedKernel_posSemidef_iff",
        )
        wb.add_assertion(
            "codata2022_implied_abs_c2_near_9p40e_minus_4",
            fmt(abs(c2_minus_emp_2022), dps=8),
            "0.0009399",
            "2e-6",
            source="CODATA-2022 implied |Delta_2^emp / alpha_B^2| diagnostic",
        )

        wb.add_caveat(
            "1. In H_3(q), standard N=2 Jones and N=3 sl_3 HOMFLY-PT quantum-dimension traces of "
            "T(3,5) yield 3-term and 6-term Laurent polynomials and do NOT collapse to (q - q^-1)[10]_q; "
            "the clean binomial q^10 - q^-10 arises uniquely from the partition-conjugation antisymmetric "
            "(w_3, w_21, w_111) = (1, 0, -1) top-channel difference and from the 5-fold strand-period "
            "denominator of the symmetrized Alexander / 3-strand reduced Burau invariant. "
            "2. All 15 pre-registered zero-parameter two-loop Delta_2 candidates (29 signed variants) "
            "are reported verbatim without post-hoc selection: 27/29 miss outside 2*sigma_CODATA, while "
            "C3c (+hbar_q^2*zeta(3)/pi^2, +0.0994 ppb, 0.65 sigma) and C2d (+Vol(4_1)/(12*pi)^2, +0.1898 ppb, "
            "1.24 sigma) lie within 1 sigma and 2 sigma respectively; because 2*sigma_CODATA/alpha^2 spans "
            "~7.89e-4 around c_2^(+,emp) = +9.40e-4 and every candidate shares the steep tree q-slope "
            "(~6.43e6 ppm/q across q_0 +- 0.05), neither C3c nor C2d is promoted to production (Rule 14). "
            "3. On WeakVertexTwoTerm, strand charge assignments (e.g. C-lep) and covariance-group choices "
            "enter as explicit hypotheses per owner rulings (#8743, #8838)."
        )

        out = wb.save({"q0Anchor": "proton", "q0Value": fmt(q0, dps=OUT_DPS)})
        print(f"alpha_inv_FormB(q0)      = {fmt(alpha_inv_form_b, dps=20)}")
        print(f"alpha_inv_CODATA2022     = {fmt(alpha_inv_codata2022, dps=20)}")
        print(f"FormB resid (2022) [ppb] = {fmt(resid_form_b_2022_ppb, dps=10)}")
        print(f"FormB resid (2018) [ppb] = {fmt(resid_form_b_2018_ppb, dps=10)}")
        print(f"c2_plus_emp (2022)       = {fmt(c2_plus_emp_2022, dps=12)}")
        print(f"c2_minus_emp (2022)      = {fmt(c2_minus_emp_2022, dps=12)}")
        print(f"1-sigma passes           = {passes_1sigma}")
        print(f"2-sigma consistent       = {passes_2sigma}")
        print(f"witness -> {out}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
