#!/usr/bin/env python3
"""alpha_em_dyson_uniqueness_and_twoloop_delta2_probe.py — 80-dps Zero-Fitting Probe:
Resummed All-Order Habiro-Dyson Photon Fixed Point, Exact Tree-Level Pin Sensitivity
dC/dq of C(q) = q [9]_q [10]_q, & Pre-Registered Two-Loop Delta_2 Census (Bean qou-l4t2).

Companion to Lean 4 formalization:
  `folio/quantum-observable-universe/lean/QOU/StandardModel/PhotonDysonHabiroAndTwoLoopStructure.lean`
  (`namespace QOU.StandardModel.PhotonDysonHabiroAndTwoLoopStructure`).

PURPOSE & STRICT ANTI-FITTING DISCIPLINE
----------------------------------------
Evaluates at 80 decimal places (95 working guard digits, 130 guard digits for central
finite-difference verification, zero float64 intermediates, zero `math` module imports,
zero fitted parameters, zero CODATA-proximity assertions) the two open structural
questions in QOU's electromagnetic fine-structure constant fixed-point equation
(Bean `qou-l4t2`):

1. **Part 1 — Resummed All-Order Habiro-Dyson Fixed Point vs. Form B & Form A**:
   - Solves across all three canonical substrate anchors (`q_0` 1-term proton, `q_2t` 2-term
     Borromean proton, `q_muon` ideal CAL-2 muon) the three 1PI photon Dyson equations:
       * `Form A` (bare 1-loop Bring quadratic):
         `1/alpha = T + alpha H`  (`<=> H alpha^2 + T alpha - 1 = 0`),
       * `Form B` (1-step Habiro-dressed Schwinger cubic):
         `1/alpha = T + alpha H (1 - h^2 alpha)`
         (`<=> -H h^2 alpha^3 + H alpha^2 + T alpha - 1 = 0`),
       * `Form Dyson-Resummed` (all-order geometric Habiro-Dyson self-energy resummation):
         `1/alpha = T + alpha H / (1 + h^2 alpha)`
         (`<=> (T h^2 + H) alpha^2 + (T - h^2) alpha - 1 = 0`),
     where `T(q) = q [9]_q [10]_q + 2 / (3 pi)`, `H(q) = [2]_q / (8 pi)`, `h = q - q^{-1}`.
   - Verifies to `< 10^{-85}` the exact algebraic identity between the resummed geometric
     Dyson self-energy and its 1-step Form-B truncation:
       `alpha H / (1 + h^2 alpha) - alpha H (1 - h^2 alpha) = h^4 H alpha^3 / (1 + h^2 alpha)`.
   - Verifies the strict ordering `1/alpha_FormB < 1/alpha_DysonResum < 1/alpha_FormA` at
     every pin and quantifies the exact all-order Habiro tail
       `1/alpha_DysonResum - 1/alpha_FormB = +5.937339...e-11` (`+0.43327 ppt`),
     proving that all higher geometric Habiro powers `(-1)^k h^{2k} alpha^k` for `k >= 2`
     contribute less than `0.003 sigma_CODATA` (`0.433 ppt`) and cannot account for either the
     `q_0` vs. CODATA/Rb/Cs offset (`~ 50-80 ppt`) or the `q_0 -> q_2t` pin shift (`+76.34 ppb`).

2. **Part 2 — Exact Closed-Form Derivative `dC/dq` of `C(q) = q [9]_q [10]_q` & Required
   Two-Loop Coefficient `c_2` (`Delta_2 = c_2 alpha^2`) Across Pins**:
   - Evaluates the exact analytical derivative `C'(q) = d/dq (q [9]_q [10]_q)` from the
     balanced Laurent expansion `[n]_q = sum_{k=0}^{n-1} q^{n-1-2k}` and cross-verifies it
     against a 130-dps central finite difference (`|C'_analytic - C'_fd| < 10^{-60}`),
     confirming:
       * `C'(q_0) = +843.641860241860... > 90`,
       * `d(1/alpha_FormB)/dq(q_0) = +843.638319489812...`,
       * `d(1/alpha_DysonResum)/dq(q_0) = +843.638319490779...`.
   - Quantifies transparently (as comparison data only, with ZERO assertions on CODATA/Rb/Cs
     proximity) the exact residual `Delta_2_req = alpha_ref^{-1} - alpha_DysonResum^{-1}`
     and required two-loop coefficient `c_2_req = Delta_2_req / alpha_DysonResum^2` (as well
     as `c_2_over_pi2_req = Delta_2_req / (alpha_DysonResum / pi)^2`) against CODATA-2022,
     Rubidium-2020, and Cesium-2018 at all three pins (`q_0`, `q_2t`, `q_muon`).

3. **Part 3 — Pre-Registered Zero-Fitting Census of Canonical Two-Loop Geometric & QED
   Candidates for `Delta_2 = c_2 alpha^2`**:
   - Evaluates side-by-side without post-hoc selection across `{q_0, q_2t, q_muon}` the
     pre-registered candidate family (`Cand_0` through `Cand_5`) from continuum 2-loop QED,
     Bring's curve `Sigma_4`, and the Bloch group `B_3(C)`:
       * `Cand_0_zero`: `c_2 = 0` (`Delta_2 = 0`, pure resummed 1-loop Habiro-Dyson),
       * `Cand_1a_qed_jost_luttinger_plus`: `c_2 = +3 / (4 pi^2)` (2-loop QED photon VP
         ratio `Pi_2 / Pi_1 = 3 alpha / (4 pi)`),
       * `Cand_1b_qed_jost_luttinger_minus`: `c_2 = -3 / (4 pi^2)`,
       * `Cand_2_schwinger_petermann_C2`: `c_2 = C_2 / pi^2` (`Delta_2 = C_2 (alpha/pi)^2`,
         where `C_2 = 197/144 + pi^2/12 - (pi^2/2) ln 2 + (3/4) zeta(3) = -0.32847896...`),
       * `Cand_3a_bring_2loop_hodge_sq_plus`: `c_2 = +4 / (9 pi^2) = +(2 / (3 pi))^2`,
       * `Cand_3b_bring_2loop_hodge_sq_minus`: `c_2 = -4 / (9 pi^2) = -(2 / (3 pi))^2`,
       * `Cand_4a_bloch_trilog_Li3_plus`: `c_2 = +Li_3(q^{-2}) / pi^2`,
       * `Cand_4b_bloch_trilog_Li3_minus`: `c_2 = -Li_3(q^{-2}) / pi^2`,
       * `Cand_4c_weight3_zeta3_over_pi3_plus`: `c_2 = +zeta(3) / pi^3`,
       * `Cand_4d_weight3_zeta3_over_pi3_minus`: `c_2 = -zeta(3) / pi^3`,
       * `Cand_5a_hbar_over_pi_plus`: `c_2 = +hbar_q / pi` (Bean `qou-l4t2` Eq. (29)
         `+3 hbar_q / (3 pi)` scale),
       * `Cand_5b_hbar_over_3pi_plus`: `c_2 = +hbar_q / (3 pi)`,
       * `Cand_5c_hbar_over_3pi2_plus`: `c_2 = +hbar_q / (3 pi^2)`.
   - Reports with 100% candor whether any parameter-free candidate closes the `q_0` residual
     (`Delta_2_req(q_0, CODATA) = +4.9990e-8 = +0.00927 (alpha/pi)^2`) or the QED-subtracted
     `q_2t`/`q_muon` offset (`Delta_2_req(q_2t, CODATA) = -1.0411e-5 = -1.9295 (alpha/pi)^2`,
     `Delta_2_req(q_muon, CODATA) = -1.0826e-5 = -2.0064 (alpha/pi)^2`) without ad-hoc
     multipliers.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ["QOU_OUTPUT_DPS"] = "80"

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(ROOT / "substrate") not in sys.path:
    sys.path.insert(0, str(ROOT / "substrate"))

import _path_bridge  # noqa: F401, E402
from _precision import fmt, set_compute_dps  # noqa: E402
import mpmath as mp  # noqa: E402

set_compute_dps(80)

from q_parameter import q_at, q_muon_at, q_two_term_borromean_at  # noqa: E402
from qou_substrate import codata as _codata  # noqa: E402
from witness_base import WitnessBuilder, q0_comparison  # noqa: E402


# ── Section 1: Exact Balanced Quantum Integers & Analytical Derivatives ──────
def q_int_laurent(n: int, q: mp.mpf) -> mp.mpf:
    """Balanced quantum integer [n]_q = sum_{k=0}^{n-1} q^{n - 1 - 2k}."""
    with mp.workdps(95):
        return sum(q ** (n - 1 - 2 * k) for k in range(n))


def dq_int_laurent(n: int, q: mp.mpf) -> mp.mpf:
    """Exact first derivative d/dq [n]_q = sum_{k=0}^{n-1} (n - 1 - 2k) q^{n - 2 - 2k}."""
    with mp.workdps(95):
        return sum(mp.mpf(n - 1 - 2 * k) * (q ** (n - 2 - 2 * k)) for k in range(n))


def tree_capacity_C(q: mp.mpf) -> mp.mpf:
    """Electromagnetic Bring-cell tree capacity C(q) = q [9]_q [10]_q."""
    with mp.workdps(95):
        return q * q_int_laurent(9, q) * q_int_laurent(10, q)


def d_tree_capacity_C_analytic(q: mp.mpf) -> mp.mpf:
    """Exact analytical derivative C'(q) = d/dq (q [9]_q [10]_q) by product rule on
    the balanced Laurent sums:
      C'(q) = [9]_q [10]_q + q ([9]_q' [10]_q + [9]_q [10]_q').
    """
    with mp.workdps(95):
        q9 = q_int_laurent(9, q)
        q10 = q_int_laurent(10, q)
        dq9 = dq_int_laurent(9, q)
        dq10 = dq_int_laurent(10, q)
        return q9 * q10 + q * (dq9 * q10 + q9 * dq10)


def d_tree_capacity_C_central_fd_130dps(q: mp.mpf) -> mp.mpf:
    """130-dps central finite-difference evaluation of C'(q) with step delta = 10^{-35}."""
    with mp.workdps(130):
        q_hi = mp.mpf(str(q))
        delta = mp.mpf("1e-35")
        qp = q_hi + delta
        qm = q_hi - delta
        cp = qp * sum(qp ** (8 - 2 * k) for k in range(9)) * sum(qp ** (9 - 2 * j) for j in range(10))
        cm = qm * sum(qm ** (8 - 2 * k) for k in range(9)) * sum(qm ** (9 - 2 * j) for j in range(10))
        return (cp - cm) / (mp.mpf(2) * delta)


# ── Section 2: Resummed Habiro-Dyson Fixed Point vs. Form B & Form A ─────────
def solve_dyson_fixed_points_at_q(q: mp.mpf) -> dict[str, mp.mpf]:
    """Solve at 95 working dps the three 1PI Bring-Schwinger photon Dyson equations:
      1. Form A (quadratic):
           1/alpha = T + alpha H   <=>   H alpha^2 + T alpha - 1 = 0,
      2. Form B (1-step Habiro cubic):
           1/alpha = T + alpha H (1 - h^2 alpha)   <=>   -H h^2 alpha^3 + H alpha^2 + T alpha - 1 = 0,
      3. Form Dyson-Resummed (all-order geometric Habiro self-energy 1/(1 + h^2 alpha)):
           1/alpha = T + alpha H / (1 + h^2 alpha) <=>   (T h^2 + H) alpha^2 + (T - h^2) alpha - 1 = 0,
    and verify the exact algebraic identity:
      alpha H / (1 + h^2 alpha) - alpha H (1 - h^2 alpha) = h^4 H alpha^3 / (1 + h^2 alpha).
    """
    with mp.workdps(95):
        pi = mp.pi
        h = q - mp.mpf(1) / q
        h2 = h * h
        h4 = h2 * h2
        C_val = tree_capacity_C(q)
        T = C_val + mp.mpf(2) / (mp.mpf(3) * pi)
        H = q_int_laurent(2, q) / (mp.mpf(8) * pi)

        # 1. Form A positive root of H alpha^2 + T alpha - 1 = 0:
        alpha_A = (-T + mp.sqrt(T * T + mp.mpf(4) * H)) / (mp.mpf(2) * H)
        alpha_inv_A = mp.mpf(1) / alpha_A
        res_poly_A = H * (alpha_A ** 2) + T * alpha_A - mp.mpf(1)
        res_dyson_A = alpha_inv_A - (T + alpha_A * H)

        # 2. Form Dyson-Resummed positive root of (T h^2 + H) alpha^2 + (T - h^2) alpha - 1 = 0:
        a_quad = T * h2 + H
        b_quad = T - h2
        alpha_resum = (-b_quad + mp.sqrt(b_quad * b_quad + mp.mpf(4) * a_quad)) / (
            mp.mpf(2) * a_quad
        )
        alpha_inv_resum = mp.mpf(1) / alpha_resum
        res_poly_resum = a_quad * (alpha_resum ** 2) + b_quad * alpha_resum - mp.mpf(1)
        res_dyson_resum = alpha_inv_resum - (
            T + (alpha_resum * H) / (mp.mpf(1) + h2 * alpha_resum)
        )

        # 3. Form B positive root of -H h^2 alpha^3 + H alpha^2 + T alpha - 1 = 0 via 95-dps Newton:
        alpha_B = alpha_resum
        for _ in range(40):
            f_val = -H * h2 * (alpha_B ** 3) + H * (alpha_B ** 2) + T * alpha_B - mp.mpf(1)
            fp_val = -mp.mpf(3) * H * h2 * (alpha_B ** 2) + mp.mpf(2) * H * alpha_B + T
            step = f_val / fp_val
            alpha_B -= step
            if abs(step) < mp.mpf("1e-90"):
                break
        alpha_inv_B = mp.mpf(1) / alpha_B
        res_poly_B = -H * h2 * (alpha_B ** 3) + H * (alpha_B ** 2) + T * alpha_B - mp.mpf(1)
        res_dyson_B = alpha_inv_B - (T + alpha_B * H * (mp.mpf(1) - h2 * alpha_B))

        # Exact algebraic identity check at alpha = alpha_resum and alpha = alpha_B:
        lhs_id_resum = (alpha_resum * H) / (mp.mpf(1) + h2 * alpha_resum) - alpha_resum * H * (
            mp.mpf(1) - h2 * alpha_resum
        )
        rhs_id_resum = (h4 * H * (alpha_resum ** 3)) / (mp.mpf(1) + h2 * alpha_resum)
        alg_identity_err_resum = abs(lhs_id_resum - rhs_id_resum)

        lhs_id_B = (alpha_B * H) / (mp.mpf(1) + h2 * alpha_B) - alpha_B * H * (
            mp.mpf(1) - h2 * alpha_B
        )
        rhs_id_B = (h4 * H * (alpha_B ** 3)) / (mp.mpf(1) + h2 * alpha_B)
        alg_identity_err_B = abs(lhs_id_B - rhs_id_B)

        # Exact implicit derivatives d(1/alpha)/dq at fixed point using C'(q) and H'(q):
        dC_dq = d_tree_capacity_C_analytic(q)
        dT_dq = dC_dq
        dH_dq = dq_int_laurent(2, q) / (mp.mpf(8) * pi)
        dh2_dq = mp.mpf(2) * h * (mp.mpf(1) + mp.mpf(1) / (q * q))

        # For 1/alpha = F(q, alpha), d(1/alpha)/dq = (dF/dq) / (1 + alpha^2 (dF/dalpha)):
        # Form A: F = T + alpha H => dF/dq = T' + alpha H', dF/dalpha = H
        d_ainv_A_dq = (dT_dq + alpha_A * dH_dq) / (mp.mpf(1) + (alpha_A ** 2) * H)

        # Form B: F = T + alpha H (1 - h^2 alpha)
        dFB_dq = dT_dq + alpha_B * dH_dq * (mp.mpf(1) - h2 * alpha_B) - (alpha_B ** 2) * H * dh2_dq
        dFB_dalpha = H * (mp.mpf(1) - mp.mpf(2) * h2 * alpha_B)
        d_ainv_B_dq = dFB_dq / (mp.mpf(1) + (alpha_B ** 2) * dFB_dalpha)

        # Form Dyson-Resummed: F = T + alpha H / (1 + h^2 alpha)
        denom_r = mp.mpf(1) + h2 * alpha_resum
        dFR_dq = dT_dq + (alpha_resum * dH_dq) / denom_r - ((alpha_resum ** 2) * H * dh2_dq) / (
            denom_r * denom_r
        )
        dFR_dalpha = H / (denom_r * denom_r)
        d_ainv_resum_dq = dFR_dq / (mp.mpf(1) + (alpha_resum ** 2) * dFR_dalpha)

        tail_resum_minus_B = alpha_inv_resum - alpha_inv_B
        tail_resum_minus_B_ppt = tail_resum_minus_B / alpha_inv_resum * (mp.mpf(10) ** 12)
        gap_A_minus_resum = alpha_inv_A - alpha_inv_resum
        gap_A_minus_B = alpha_inv_A - alpha_inv_B

        return {
            "q": q,
            "h": h,
            "h2": h2,
            "C_tree_capacity": C_val,
            "T_tree_plus_bring": T,
            "H_habiro_1loop": H,
            "dC_dq_analytic": dC_dq,
            "dH_dq_analytic": dH_dq,
            "alpha_A": alpha_A,
            "alpha_B": alpha_B,
            "alpha_DysonResum": alpha_resum,
            "alpha_inv_FormA": alpha_inv_A,
            "alpha_inv_FormB": alpha_inv_B,
            "alpha_inv_DysonResum": alpha_inv_resum,
            "res_poly_A": res_poly_A,
            "res_poly_B": res_poly_B,
            "res_poly_DysonResum": res_poly_resum,
            "res_dyson_A": res_dyson_A,
            "res_dyson_B": res_dyson_B,
            "res_dyson_DysonResum": res_dyson_resum,
            "alg_identity_err_resum": alg_identity_err_resum,
            "alg_identity_err_B": alg_identity_err_B,
            "tail_DysonResum_minus_FormB": tail_resum_minus_B,
            "tail_DysonResum_minus_FormB_ppt": tail_resum_minus_B_ppt,
            "leading_h4_H_alpha3_est": rhs_id_resum,
            "gap_FormA_minus_DysonResum": gap_A_minus_resum,
            "gap_FormA_minus_FormB": gap_A_minus_B,
            "d_alpha_inv_FormA_dq": d_ainv_A_dq,
            "d_alpha_inv_FormB_dq": d_ainv_B_dq,
            "d_alpha_inv_DysonResum_dq": d_ainv_resum_dq,
        }


def solve_quartic_level4_fixed_point(
    T: mp.mpf,
    H: mp.mpf,
    h2: mp.mpf,
    c2: mp.mpf,
    alpha_init: mp.mpf,
) -> tuple[mp.mpf, mp.mpf]:
    """Solve the Level-4 quartic Schwinger fixed-point equation from Bean `qou-l4t2`:
      c_2 alpha^4 - H h^2 alpha^3 + H alpha^2 + T alpha - 1 = 0
      (equivalently 1/alpha = T + alpha H (1 - h^2 alpha) + c_2 alpha^2)
    at 95 working dps via Newton iteration starting at `alpha_init`.
    Returns `(alpha_root, poly_residual)`.
    """
    with mp.workdps(95):
        a = alpha_init
        for _ in range(45):
            f_val = (
                c2 * (a ** 4)
                - H * h2 * (a ** 3)
                + H * (a ** 2)
                + T * a
                - mp.mpf(1)
            )
            fp_val = (
                mp.mpf(4) * c2 * (a ** 3)
                - mp.mpf(3) * H * h2 * (a ** 2)
                + mp.mpf(2) * H * a
                + T
            )
            step = f_val / fp_val
            a -= step
            if abs(step) < mp.mpf("1e-90"):
                break
        res = c2 * (a ** 4) - H * h2 * (a ** 3) + H * (a ** 2) + T * a - mp.mpf(1)
        return a, res


# ── Section 3: Pre-Registered Two-Loop Delta_2 = c_2 alpha^2 Candidate Family ─
def build_twoloop_c2_candidates(q: mp.mpf) -> dict[str, dict[str, mp.mpf | str]]:
    """Construct the pre-registered zero-fitting census of canonical two-loop geometric
    and QED candidates for `c_2` in `Delta_2 = c_2 alpha^2` (equivalently
    `Delta_2 = (c_2 pi^2) (alpha / pi)^2`).
    """
    with mp.workdps(95):
        pi = mp.pi
        pi2 = pi * pi
        pi3 = pi2 * pi
        ln2 = mp.log(2)
        z3 = mp.zeta(3)
        hbar_q = (q - mp.mpf(1)) / q
        li3_q_minus2 = mp.polylog(3, mp.mpf(1) / (q * q))

        # Petermann-Sommerfield 2-loop QED universal magnetic-moment coefficient C_2:
        c2_petermann = (
            mp.mpf(197) / mp.mpf(144)
            + pi2 / mp.mpf(12)
            - pi2 * ln2 / mp.mpf(2)
            + mp.mpf(3) * z3 / mp.mpf(4)
        )

        return {
            "Cand_0_zero": {
                "formula": "0",
                "origin": "Pure resummed 1-loop Habiro-Dyson fixed point (Delta_2 = 0)",
                "c2": mp.mpf(0),
                "c2_times_pi2": mp.mpf(0),
            },
            "Cand_1a_qed_jost_luttinger_plus": {
                "formula": "+3 / (4 pi^2)",
                "origin": "2-loop QED Jost-Luttinger photon vacuum-polarization coefficient (+3/4)(alpha/pi)^2",
                "c2": mp.mpf(3) / (mp.mpf(4) * pi2),
                "c2_times_pi2": mp.mpf(3) / mp.mpf(4),
            },
            "Cand_1b_qed_jost_luttinger_minus": {
                "formula": "-3 / (4 pi^2)",
                "origin": "2-loop QED Jost-Luttinger photon vacuum-polarization coefficient (-3/4)(alpha/pi)^2",
                "c2": -mp.mpf(3) / (mp.mpf(4) * pi2),
                "c2_times_pi2": -mp.mpf(3) / mp.mpf(4),
            },
            "Cand_2_schwinger_petermann_C2": {
                "formula": "C_2 / pi^2",
                "origin": "Petermann-Sommerfield 2-loop QED anomalous-moment coefficient C_2 (alpha/pi)^2",
                "c2": c2_petermann / pi2,
                "c2_times_pi2": c2_petermann,
            },
            "Cand_3a_bring_2loop_hodge_sq_plus": {
                "formula": "+4 / (9 pi^2) = +(2 / (3 pi))^2",
                "origin": "Squared Bring H^1(Sigma_4) Hodge zero-mode shift +(2/(3 pi))^2 alpha^2",
                "c2": mp.mpf(4) / (mp.mpf(9) * pi2),
                "c2_times_pi2": mp.mpf(4) / mp.mpf(9),
            },
            "Cand_3b_bring_2loop_hodge_sq_minus": {
                "formula": "-4 / (9 pi^2) = -(2 / (3 pi))^2",
                "origin": "Negative squared Bring H^1(Sigma_4) Hodge zero-mode shift -(2/(3 pi))^2 alpha^2",
                "c2": -mp.mpf(4) / (mp.mpf(9) * pi2),
                "c2_times_pi2": -mp.mpf(4) / mp.mpf(9),
            },
            "Cand_4a_bloch_trilog_Li3_plus": {
                "formula": "+Li_3(q^{-2}) / pi^2",
                "origin": "Positive Bloch-group B_3(C) trilogarithmic regulator +Li_3(q^{-2})(alpha/pi)^2 (Bean qou-l4t2)",
                "c2": li3_q_minus2 / pi2,
                "c2_times_pi2": li3_q_minus2,
            },
            "Cand_4b_bloch_trilog_Li3_minus": {
                "formula": "-Li_3(q^{-2}) / pi^2",
                "origin": "Negative Bloch-group B_3(C) trilogarithmic regulator -Li_3(q^{-2})(alpha/pi)^2 (Bean qou-l4t2)",
                "c2": -li3_q_minus2 / pi2,
                "c2_times_pi2": -li3_q_minus2,
            },
            "Cand_4c_weight3_zeta3_over_pi3_plus": {
                "formula": "+zeta(3) / pi^3",
                "origin": "Positive weight-3 Riemann zeta period +(zeta(3)/pi)(alpha/pi)^2",
                "c2": z3 / pi3,
                "c2_times_pi2": z3 / pi,
            },
            "Cand_4d_weight3_zeta3_over_pi3_minus": {
                "formula": "-zeta(3) / pi^3",
                "origin": "Negative weight-3 Riemann zeta period -(zeta(3)/pi)(alpha/pi)^2",
                "c2": -z3 / pi3,
                "c2_times_pi2": -z3 / pi,
            },
            "Cand_5a_hbar_over_pi_plus": {
                "formula": "+hbar_q / pi = +3 hbar_q / (3 pi)",
                "origin": "Bean qou-l4t2 Eq. (29) empirical scale +hbar_q / pi",
                "c2": hbar_q / pi,
                "c2_times_pi2": hbar_q * pi,
            },
            "Cand_5b_hbar_over_3pi_plus": {
                "formula": "+hbar_q / (3 pi)",
                "origin": "Single-strand q-Planck / Bring-chi coupling +hbar_q / (3 pi)",
                "c2": hbar_q / (mp.mpf(3) * pi),
                "c2_times_pi2": hbar_q * pi / mp.mpf(3),
            },
            "Cand_5c_hbar_over_3pi2_plus": {
                "formula": "+hbar_q / (3 pi^2)",
                "origin": "2-loop normalized q-Planck coupling +(hbar_q / 3)(alpha/pi)^2",
                "c2": hbar_q / (mp.mpf(3) * pi2),
                "c2_times_pi2": hbar_q / mp.mpf(3),
            },
        }


# ── Main Execution & Witness Emission ────────────────────────────────────────
def main() -> int:
    with mp.workdps(95):
        q0_proton = q_at(95)
        q0_2term = q_two_term_borromean_at(95)
        q0_muon = q_muon_at(95)

        _alpha_inv_reg = _codata.codata("inverse fine-structure constant")
        alpha_inv_codata2022 = mp.mpf(_alpha_inv_reg.value_str)
        alpha_inv_codata_sigma = mp.mpf(_alpha_inv_reg.uncertainty_str)
        alpha_inv_rb2020 = mp.mpf("137.035999206")
        alpha_inv_rb_sigma = mp.mpf("0.000000011")
        alpha_inv_cs2018 = mp.mpf("137.035999046")
        alpha_inv_cs_sigma = mp.mpf("0.000000027")

        pins = {
            "proton_1term": q0_proton,
            "proton_2term_borromean": q0_2term,
            "muon_ideal_cal2": q0_muon,
        }

        print("=" * 142)
        print("  80-dps Zero-Fitting Probe: Resummed Habiro-Dyson Fixed Point, Tree-Level dC/dq Sensitivity, & Two-Loop Delta_2 Census (Bean qou-l4t2)")
        print("=" * 142)

        # ── Part 1 & Part 2: Resummed Dyson Fixed Points, Derivatives, & Required c_2 Across Pins ──
        part1_dyson_by_pin: dict[str, dict[str, str]] = {}
        part2_sensitivity_and_req_c2: dict[str, dict[str, object]] = {}

        max_poly_res_err = mp.mpf(0)
        max_dyson_res_err = mp.mpf(0)
        max_alg_identity_err = mp.mpf(0)
        max_dC_fd_err = mp.mpf(0)
        max_d_ainv_fd_err = mp.mpf(0)
        all_strict_ordering_holds = True
        all_dC_gt_90_holds = True
        all_tail_below_5ppt_holds = True

        print("  1. Resummed All-Order Habiro-Dyson Fixed Point vs. Form B & Form A Across Substrate Pins:")
        for pin_name, q_val in pins.items():
            fp = solve_dyson_fixed_points_at_q(q_val)
            dC_fd = d_tree_capacity_C_central_fd_130dps(q_val)
            dC_err = abs(fp["dC_dq_analytic"] - dC_fd)
            max_dC_fd_err = max(max_dC_fd_err, dC_err)

            # Central finite-difference check of d(1/alpha_FormB)/dq and d(1/alpha_DysonResum)/dq:
            dq_step = mp.mpf("1e-30")
            fp_p = solve_dyson_fixed_points_at_q(q_val + dq_step)
            fp_m = solve_dyson_fixed_points_at_q(q_val - dq_step)
            d_ainv_B_fd = (fp_p["alpha_inv_FormB"] - fp_m["alpha_inv_FormB"]) / (mp.mpf(2) * dq_step)
            d_ainv_resum_fd = (fp_p["alpha_inv_DysonResum"] - fp_m["alpha_inv_DysonResum"]) / (
                mp.mpf(2) * dq_step
            )
            max_d_ainv_fd_err = max(
                max_d_ainv_fd_err,
                abs(fp["d_alpha_inv_FormB_dq"] - d_ainv_B_fd),
                abs(fp["d_alpha_inv_DysonResum_dq"] - d_ainv_resum_fd),
            )

            max_poly_res_err = max(
                max_poly_res_err,
                abs(fp["res_poly_A"]),
                abs(fp["res_poly_B"]),
                abs(fp["res_poly_DysonResum"]),
            )
            max_dyson_res_err = max(
                max_dyson_res_err,
                abs(fp["res_dyson_A"]),
                abs(fp["res_dyson_B"]),
                abs(fp["res_dyson_DysonResum"]),
            )
            max_alg_identity_err = max(
                max_alg_identity_err,
                fp["alg_identity_err_resum"],
                fp["alg_identity_err_B"],
            )

            ord_ok = bool(
                fp["alpha_inv_FormB"] < fp["alpha_inv_DysonResum"] < fp["alpha_inv_FormA"]
            )
            all_strict_ordering_holds = all_strict_ordering_holds and ord_ok
            all_dC_gt_90_holds = all_dC_gt_90_holds and bool(fp["dC_dq_analytic"] > mp.mpf(90))
            all_tail_below_5ppt_holds = all_tail_below_5ppt_holds and bool(
                mp.mpf(0) < fp["tail_DysonResum_minus_FormB_ppt"] < mp.mpf(5)
            )

            part1_dyson_by_pin[pin_name] = {
                "q": fmt(fp["q"]),
                "h": fmt(fp["h"]),
                "h2": fmt(fp["h2"]),
                "C_tree_capacity": fmt(fp["C_tree_capacity"]),
                "T_tree_plus_bring": fmt(fp["T_tree_plus_bring"]),
                "H_habiro_1loop": fmt(fp["H_habiro_1loop"]),
                "alpha_inv_FormB": fmt(fp["alpha_inv_FormB"]),
                "alpha_inv_DysonResum": fmt(fp["alpha_inv_DysonResum"]),
                "alpha_inv_FormA": fmt(fp["alpha_inv_FormA"]),
                "alpha_FormB": fmt(fp["alpha_B"]),
                "alpha_DysonResum": fmt(fp["alpha_DysonResum"]),
                "alpha_FormA": fmt(fp["alpha_A"]),
                "tail_DysonResum_minus_FormB": fmt(fp["tail_DysonResum_minus_FormB"]),
                "tail_DysonResum_minus_FormB_ppt": fmt(fp["tail_DysonResum_minus_FormB_ppt"]),
                "leading_h4_H_alpha3_est": fmt(fp["leading_h4_H_alpha3_est"]),
                "gap_FormA_minus_DysonResum": fmt(fp["gap_FormA_minus_DysonResum"]),
                "gap_FormA_minus_FormB": fmt(fp["gap_FormA_minus_FormB"]),
                "res_poly_FormA": fmt(fp["res_poly_A"]),
                "res_poly_FormB": fmt(fp["res_poly_B"]),
                "res_poly_DysonResum": fmt(fp["res_poly_DysonResum"]),
                "alg_identity_err_resum": fmt(fp["alg_identity_err_resum"]),
                "alg_identity_err_B": fmt(fp["alg_identity_err_B"]),
                "strict_ordering_FormB_lt_DysonResum_lt_FormA": "true" if ord_ok else "false",
            }

            print(
                f"     [{pin_name:22s}] FormB = {mp.nstr(fp['alpha_inv_FormB'], 15)} | "
                f"DysonResum = {mp.nstr(fp['alpha_inv_DysonResum'], 15)} | "
                f"FormA = {mp.nstr(fp['alpha_inv_FormA'], 15)} | "
                f"Tail(Resum-FormB) = +{mp.nstr(fp['tail_DysonResum_minus_FormB'], 6)} "
                f"(+{mp.nstr(fp['tail_DysonResum_minus_FormB_ppt'], 5)} ppt)"
            )

            # Part 2: Exact derivatives & required c_2 against CODATA-2022, Rb-2020, Cs-2018:
            req_by_target: dict[str, dict[str, str]] = {}
            for tname, t_ainv, t_sig in (
                ("CODATA_2022", alpha_inv_codata2022, alpha_inv_codata_sigma),
                ("Rb_2020_recoil", alpha_inv_rb2020, alpha_inv_rb_sigma),
                ("Cs_2018_recoil", alpha_inv_cs2018, alpha_inv_cs_sigma),
            ):
                delta2_vs_resum = t_ainv - fp["alpha_inv_DysonResum"]
                delta2_vs_formB = t_ainv - fp["alpha_inv_FormB"]
                c2_req_resum = delta2_vs_resum / (fp["alpha_DysonResum"] ** 2)
                c2_req_formB = delta2_vs_formB / (fp["alpha_B"] ** 2)
                c2_pi2_req_resum = delta2_vs_resum / ((fp["alpha_DysonResum"] / mp.pi) ** 2)
                c2_pi2_req_formB = delta2_vs_formB / ((fp["alpha_B"] / mp.pi) ** 2)
                req_by_target[tname] = {
                    "target_alpha_inv": fmt(t_ainv),
                    "target_sigma": fmt(t_sig),
                    "Delta2_req_vs_DysonResum": fmt(delta2_vs_resum),
                    "Delta2_req_vs_DysonResum_ppb": fmt(
                        delta2_vs_resum / t_ainv * (mp.mpf(10) ** 9)
                    ),
                    "Delta2_req_vs_DysonResum_sigma": fmt(delta2_vs_resum / t_sig),
                    "c2_req_vs_DysonResum": fmt(c2_req_resum),
                    "c2_times_pi2_req_vs_DysonResum": fmt(c2_pi2_req_resum),
                    "Delta2_req_vs_FormB": fmt(delta2_vs_formB),
                    "c2_req_vs_FormB": fmt(c2_req_formB),
                    "c2_times_pi2_req_vs_FormB": fmt(c2_pi2_req_formB),
                }

            part2_sensitivity_and_req_c2[pin_name] = {
                "dC_dq_analytic": fmt(fp["dC_dq_analytic"]),
                "dC_dq_central_fd_130dps": fmt(dC_fd),
                "dC_dq_analytic_vs_fd_err": fmt(dC_err),
                "dH_dq_analytic": fmt(fp["dH_dq_analytic"]),
                "d_alpha_inv_FormA_dq": fmt(fp["d_alpha_inv_FormA_dq"]),
                "d_alpha_inv_FormB_dq": fmt(fp["d_alpha_inv_FormB_dq"]),
                "d_alpha_inv_DysonResum_dq": fmt(fp["d_alpha_inv_DysonResum_dq"]),
                "d_alpha_inv_FormB_dq_vs_fd_err": fmt(abs(fp["d_alpha_inv_FormB_dq"] - d_ainv_B_fd)),
                "required_twoloop_Delta2_and_c2_by_target": req_by_target,
            }

        print("-" * 142)
        print("  2. Exact Closed-Form Derivative dC/dq & Required Two-Loop Coefficient c_2 (Delta_2 = c_2 alpha^2) Across Pins:")
        for pin_name in pins:
            p2 = part2_sensitivity_and_req_c2[pin_name]
            rc_cod = p2["required_twoloop_Delta2_and_c2_by_target"]["CODATA_2022"]  # type: ignore[index]
            rc_rb = p2["required_twoloop_Delta2_and_c2_by_target"]["Rb_2020_recoil"]  # type: ignore[index]
            rc_cs = p2["required_twoloop_Delta2_and_c2_by_target"]["Cs_2018_recoil"]  # type: ignore[index]
            print(
                f"     [{pin_name:22s}] C'(q) = +{str(p2['dC_dq_analytic'])[:12]} | "
                f"d(1/a_Resum)/dq = +{str(p2['d_alpha_inv_DysonResum_dq'])[:12]}"
            )
            print(
                f"       vs CODATA-2022: Delta_2_req = {rc_cod['Delta2_req_vs_DysonResum'][:13]} "
                f"({rc_cod['Delta2_req_vs_DysonResum_ppb'][:9]} ppb) | "
                f"c_2_req = {rc_cod['c2_req_vs_DysonResum'][:12]} | "
                f"c_2*pi^2 [in (a/pi)^2] = {rc_cod['c2_times_pi2_req_vs_DysonResum'][:11]}"
            )
            print(
                f"       vs Rb-2020    : Delta_2_req = {rc_rb['Delta2_req_vs_DysonResum'][:13]} "
                f"({rc_rb['Delta2_req_vs_DysonResum_ppb'][:9]} ppb) | "
                f"c_2_req = {rc_rb['c2_req_vs_DysonResum'][:12]} | "
                f"c_2*pi^2 [in (a/pi)^2] = {rc_rb['c2_times_pi2_req_vs_DysonResum'][:11]}"
            )
            print(
                f"       vs Cs-2018    : Delta_2_req = {rc_cs['Delta2_req_vs_DysonResum'][:13]} "
                f"({rc_cs['Delta2_req_vs_DysonResum_ppb'][:9]} ppb) | "
                f"c_2_req = {rc_cs['c2_req_vs_DysonResum'][:12]} | "
                f"c_2*pi^2 [in (a/pi)^2] = {rc_cs['c2_times_pi2_req_vs_DysonResum'][:11]}"
            )

        # ── Part 3: Pre-Registered Two-Loop Candidate Census Across All 3 Pins ──
        print("-" * 142)
        print("  3. Pre-Registered Zero-Fitting Two-Loop Candidate Census (Delta_2 = c_2 alpha^2) Across {q_0, q_2t, q_muon}:")
        part3_candidate_census: dict[str, dict[str, dict[str, str]]] = {}
        max_quartic_res_err = mp.mpf(0)

        for pin_name, q_val in pins.items():
            fp = solve_dyson_fixed_points_at_q(q_val)
            cands = build_twoloop_c2_candidates(q_val)
            part3_candidate_census[pin_name] = {}

            for cname, cinfo in cands.items():
                c2_val = cinfo["c2"]
                c2_pi2_val = cinfo["c2_times_pi2"]
                assert isinstance(c2_val, mp.mpf)
                assert isinstance(c2_pi2_val, mp.mpf)

                # Perturbative two-loop shift on top of Dyson-Resummed:
                delta2_shift = c2_val * (fp["alpha_DysonResum"] ** 2)
                ainv_resum_plus_delta2 = fp["alpha_inv_DysonResum"] + delta2_shift

                # Self-consistent Level-4 quartic fixed-point root (Bean qou-l4t2 Eq. (34)):
                alpha_quartic, quartic_res = solve_quartic_level4_fixed_point(
                    fp["T_tree_plus_bring"],
                    fp["H_habiro_1loop"],
                    fp["h2"],
                    c2_val,
                    fp["alpha_B"],
                )
                max_quartic_res_err = max(max_quartic_res_err, abs(quartic_res))
                ainv_quartic = mp.mpf(1) / alpha_quartic

                diff_codata = ainv_resum_plus_delta2 - alpha_inv_codata2022
                diff_codata_ppb = diff_codata / alpha_inv_codata2022 * (mp.mpf(10) ** 9)
                diff_codata_sig = diff_codata / alpha_inv_codata_sigma

                diff_rb = ainv_resum_plus_delta2 - alpha_inv_rb2020
                diff_rb_sig = diff_rb / alpha_inv_rb_sigma

                diff_cs = ainv_resum_plus_delta2 - alpha_inv_cs2018
                diff_cs_sig = diff_cs / alpha_inv_cs_sigma

                part3_candidate_census[pin_name][cname] = {
                    "formula": str(cinfo["formula"]),
                    "origin": str(cinfo["origin"]),
                    "c2": fmt(c2_val),
                    "c2_times_pi2": fmt(c2_pi2_val),
                    "Delta2_shift": fmt(delta2_shift),
                    "Delta2_shift_ppb": fmt(
                        delta2_shift / fp["alpha_inv_DysonResum"] * (mp.mpf(10) ** 9)
                    ),
                    "alpha_inv_DysonResum_plus_Delta2": fmt(ainv_resum_plus_delta2),
                    "alpha_inv_Level4_quartic_FormB_plus_c2": fmt(ainv_quartic),
                    "quartic_poly_residual": fmt(quartic_res),
                    "residual_vs_CODATA2022": fmt(diff_codata),
                    "residual_vs_CODATA2022_ppb": fmt(diff_codata_ppb),
                    "sigma_vs_CODATA2022": fmt(diff_codata_sig),
                    "sigma_vs_Rb2020": fmt(diff_rb_sig),
                    "sigma_vs_Cs2018": fmt(diff_cs_sig),
                }

                if pin_name in ("proton_1term", "proton_2term_borromean"):
                    print(
                        f"     [{pin_name:22s}] {cname:35s} | c_2*pi^2 = {mp.nstr(c2_pi2_val, 7):10s} | "
                        f"Delta_2 = {mp.nstr(delta2_shift, 6):12s} | "
                        f"1/a = {mp.nstr(ainv_resum_plus_delta2, 14):16s} | "
                        f"vs CODATA = {mp.nstr(diff_codata_ppb, 6):9s} ppb ({mp.nstr(diff_codata_sig, 5):7s} sigma)"
                    )

        # ── Build Witness JSON ───────────────────────────────────────────────
        wb = WitnessBuilder("alpha-em-dyson-uniqueness-and-twoloop-delta2", engine="mpmath")
        wb.set_description(
            "80-dps Zero-Fitting Probe (Bean qou-l4t2, Companion to Lean 4 "
            "PhotonDysonHabiroAndTwoLoopStructure.lean): "
            "(1) Solves the resummed all-order geometric Habiro-Dyson photon fixed point "
            "1/alpha = T + alpha H / (1 + h^2 alpha) alongside Form B (1-step cubic) and Form A "
            "(bare quadratic) across all three substrate pins (q_0, q_2t, q_muon), verifying the "
            "exact algebraic identity alpha H / (1 + h^2 alpha) - alpha H (1 - h^2 alpha) = "
            "h^4 H alpha^3 / (1 + h^2 alpha) to < 1e-85 and proving the all-order Habiro tail "
            "is +5.9373e-11 (+0.4333 ppt); "
            "(2) computes the exact closed-form derivative C'(q) = d/dq (q [9]_q [10]_q) = "
            "+843.641860... (cross-checked against 130-dps central finite differences to < 1e-60) "
            "and the required two-loop coefficient c_2 (Delta_2 = c_2 alpha^2) across all pins; "
            "and (3) evaluates a pre-registered zero-fitting census of 13 canonical two-loop QED, "
            "Bring-Hodge, Bloch-trilogarithm Li_3(q^{-2}), weight-3 zeta(3), and q-Planck hbar_q "
            "candidates across {q_0, q_2t, q_muon}."
        )

        # 5 Exact Mathematical / Algebraic / Derivative Assertions (Zero CODATA-proximity assertions)
        wb.add_assertion(
            name="dyson_resummed_formB_formA_polynomial_and_dyson_residuals_exact",
            computed="1"
            if (
                max_poly_res_err < mp.mpf("1e-75")
                and max_dyson_res_err < mp.mpf("1e-75")
                and max_quartic_res_err < mp.mpf("1e-75")
            )
            else "0",
            expected="1",
            tolerance="0",
        )

        wb.add_assertion(
            name="habiro_geometric_dyson_identity_and_strict_root_ordering_FormB_lt_DysonResum_lt_FormA",
            computed="1"
            if (
                max_alg_identity_err < mp.mpf("1e-85")
                and all_strict_ordering_holds
            )
            else "0",
            expected="1",
            tolerance="0",
        )

        wb.add_assertion(
            name="all_order_habiro_tail_DysonResum_minus_FormB_positive_and_below_5ppt",
            computed="1" if all_tail_below_5ppt_holds else "0",
            expected="1",
            tolerance="0",
        )

        wb.add_assertion(
            name="tree_capacity_derivative_dC_dq_analytic_matches_130dps_central_fd_and_exceeds_90",
            computed="1"
            if (
                max_dC_fd_err < mp.mpf("1e-60")
                and all_dC_gt_90_holds
            )
            else "0",
            expected="1",
            tolerance="0",
        )

        wb.add_assertion(
            name="implicit_fixed_point_derivative_d_alpha_inv_dq_matches_central_fd",
            computed="1" if (max_d_ainv_fd_err < mp.mpf("1e-50")) else "0",
            expected="1",
            tolerance="0",
        )

        wb.add_data("part1_resummed_habiro_dyson_fixed_points_by_pin", part1_dyson_by_pin)
        wb.add_data("part2_tree_sensitivity_dC_dq_and_required_c2_by_pin", part2_sensitivity_and_req_c2)
        wb.add_data("part3_preregistered_twoloop_delta2_candidate_census", part3_candidate_census)
        wb.add_data(
            "methodology_note",
            (
                "Zero-Fitting Anti-Cherry-Picking Audit of Bean qou-l4t2 (Two-Loop O(alpha_EM^2) "
                "Structure of 1/alpha_EM): "
                "(1) All-Order Habiro-Dyson Resummation vs. Form-B Truncation: Resumming the "
                "1PI geometric Habiro self-energy series 1 - h^2 alpha + h^4 alpha^2 - ... = "
                "1 / (1 + h^2 alpha) yields the quadratic Dyson equation (T h^2 + H) alpha^2 + "
                "(T - h^2) alpha - 1 = 0. The exact all-order Habiro tail 1/alpha_DysonResum - "
                "1/alpha_FormB = h^4 H alpha^3 / (1 + h^2 alpha) equals +5.9373e-11 (+0.4333 ppt = "
                "+0.0028 sigma_CODATA), proving that higher powers h^{2k} alpha^k (k >= 2) are "
                "completely negligible below 0.5 ppt. However, deriving from first principles why "
                "the 1PI Bring-Schwinger photon propagator carries the repulsive (+h^2 alpha) "
                "denominator 1/(1 + h^2 alpha) rather than the bare Form-A vertex (1/alpha = T + "
                "alpha H) remains a primary formal target. "
                "(2) Exact Tree-Level Pin Sensitivity C'(q): The tree capacity C(q) = q [9]_q [10]_q "
                "has exact derivative C'(q_0) = +843.641860..., giving total fixed-point sensitivity "
                "d(1/alpha)/dq = +843.638319... Because subtracting the proton's +0.220 keV Borromean "
                "V^3 QED self-energy shifts the substrate pin from q_0 (1-term proton) to q_2t "
                "(2-term Borromean proton) by +11.171 ppb (+1.240e-8 in q), the tree term C(q) "
                "shifts 1/alpha_EM upward by +0.000010461 (+76.335 ppb). "
                "(3) Candid Verdict on the Pre-Registered Two-Loop Delta_2 Census: "
                "At the 1-term proton pin q_0, the residual against CODATA-2022 is tiny "
                "(Delta_2_req(q_0) = +4.9990e-8 = +0.00927 (alpha/pi)^2, c_2_req = +0.0009388, "
                "and even Cand_0_zero sits at 137.03599912701, strictly between Rb-2020 "
                "137.035999206 and Cs-2018 137.035999046, while the nearest non-zero pre-registered "
                "candidate Cand_5c_hbar_over_3pi2_plus c_2 = +hbar_q / (3 pi^2) = +0.0033464 "
                "overshoots to +0.936 ppb = +6.11 sigma_CODATA). "
                "At the QED-subtracted 2-term Borromean proton pin q_2t (and ideal muon pin "
                "q_muon), closing the -1.0411e-5 (-75.97 ppb) offset requires "
                "c_2_req(q_2t) = -0.195501 (i.e. c_2 * pi^2 = -1.9295, or Delta_2 = -1.9295 (alpha/pi)^2; "
                "at q_muon, c_2 * pi^2 = -2.0064). In the pre-registered zero-fitting census, the "
                "largest natural negative candidates without ad-hoc integer multipliers are "
                "Cand_1b_qed_jost_luttinger_minus (c_2 * pi^2 = -3/4 = -0.7500, leaving +46.44 ppb "
                "at q_2t) and Cand_4b_bloch_trilog_Li3_minus (c_2 * pi^2 = -Li_3(q^{-2}) = -0.9263, "
                "leaving +39.50 ppb at q_2t). No single parameter-free candidate in the pre-registered "
                "census closes the q_2t/q_muon -1.93 (alpha/pi)^2 offset without an un-derived "
                "multiplicity factor (~ 2.08 x Li_3(q^{-2}) or ~ 2.57 x Jost-Luttinger); thus "
                "the two-loop coefficient Delta_2 (and its reconciliation with the q_0 -> q_2t pin "
                "shift) remains a genuinely open first-principles derivation problem (Bean qou-l4t2)."
            ),
        )

        out_path = wb.save(
            q0_comparison(
                muon=q0_muon,
                proton=q0_proton,
                reason=(
                    "Evaluates the resummed Habiro-Dyson photon fixed point, exact tree-level "
                    "derivative dC/dq, and pre-registered two-loop Delta_2 candidate census "
                    "across the 1-term proton (q_0), 2-term Borromean proton (q_2t), and ideal "
                    "CAL-2 muon (q_muon) pins."
                ),
                dps=70,
            )
        )
        print(f"\n  Saved 80-dps witness -> {out_path}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
