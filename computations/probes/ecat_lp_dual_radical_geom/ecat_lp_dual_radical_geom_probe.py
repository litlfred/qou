#!/usr/bin/env python3
"""80-dps evaluation of solver-free `ECatLPDualRadical` shadow prices and dual
feasibility across the pre-registered 6D `H_3(q_0)` normal-form geometric costs.

Bean `qou-udad` (`critical`). Pre-registered in `PREREGISTRATION.md` (commit
`3004225fb9c`) BEFORE running any numerical evaluation.

Formal backing:
  - `folio/quantum-observable-universe/lean/QOU/QBeta/ECatLPDualRadical.lean`
    (`dual_price_determined_by_radical`, `dual_price_ne_zero_of_cost_not_orthogonal`)
  - `folio/quantum-observable-universe/lean/QOU/Nuclear/ECatRadicalShadowPriceEvaluation.lean`
    (`inner_one_radicalVec3`, `inner_ecatPairCyclicCost_radicalVec3`,
     `inner_ecatPairOpenCost_radicalVec3`, `inner_thomaeJacksonCrossing_radicalVec3`,
     `inner_thomaeJacksonGeom_radicalVec3`, `residual_orthogonal_to_radical`,
     `dual_equality_shift_along_radical`, `ecatPairCyclic_shadowPrice_closed_form`,
     `thomaeJacksonCrossing_shadowPrice_closed_form`)

Precision discipline:
  - `mpmath` at `workdps = 80` (`OUT_DPS = 50` serialized),
  - `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`),
  - exact `sympy.Rational` verification at `q = 11/10` and `q = 7/5`,
  - zero `float64` imports, literals, or casts, zero post-hoc parameter fitting.
"""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[3]
if str(_ROOT / "tools" / "qou-substrate" / "python") not in sys.path:
    sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))
if str(_ROOT / "computations") not in sys.path:
    sys.path.insert(0, str(_ROOT / "computations"))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

WORK_DPS = 80
OUT_DPS = 50
set_compute_dps(WORK_DPS)

# Standard 6-element Coxeter normal-form basis of H_3(q):
#   b = (1, sigma_0, sigma_1, sigma_0 sigma_1, sigma_1 sigma_0, sigma_0 sigma_1 sigma_0)
NF_WORDS: list[tuple[int, ...]] = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
NF_LABELS: list[str] = ["1", "sigma_0", "sigma_1", "sigma_0*sigma_1", "sigma_1*sigma_0", "sigma_0*sigma_1*sigma_0"]
POS_V_INDICES = (0, 3, 4)  # (-1/q)^len > 0 for q > 0
NEG_V_INDICES = (1, 2, 5)  # (-1/q)^len < 0 for q > 0


def hm_nf_mp(nf: list[mp.mpf], c: mp.mpf, d: mp.mpf, gen: int, h_val: mp.mpf) -> list[mp.mpf]:
    """Right-multiply a 6D H_3(q) NF vector by `c * sigma_gen + d * 1` in pure mpmath."""
    zero = mp.mpf(0)
    out = [zero] * 6
    if gen == 0:
        rules = (
            (0, ((1, c), (0, d))),
            (1, ((1, c * h_val), (0, c), (1, d))),
            (2, ((3, c), (2, d))),
            (3, ((3, c * h_val), (2, c), (3, d))),
            (4, ((5, c), (4, d))),
            (5, ((5, c * h_val), (4, c), (5, d))),
        )
    else:
        rules = (
            (0, ((2, c), (0, d))),
            (1, ((4, c), (1, d))),
            (2, ((2, c * h_val), (0, c), (2, d))),
            (3, ((5, c), (3, d))),
            (4, ((4, c * h_val), (1, c), (4, d))),
            (5, ((5, c * h_val), (3, c), (5, d))),
        )
    for src_idx, targets in rules:
        val = nf[src_idx]
        if val == zero:
            continue
        for dst_idx, coeff in targets:
            out[dst_idx] += val * coeff
    return out


def word_to_nf_mp(word: tuple[int, ...], h_val: mp.mpf) -> list[mp.mpf]:
    """Convert positive generator word (0/1 indices) to its 6D H_3(q) NF vector."""
    one = mp.mpf(1)
    zero = mp.mpf(0)
    nf = [one, zero, zero, zero, zero, zero]
    for gen in word:
        nf = hm_nf_mp(nf, one, zero, gen, h_val)
    return nf


def build_convention_d_gram_mp(q: mp.mpf) -> tuple[mp.matrix, list[mp.mpf], list[mp.mpf]]:
    """Build exact 80-dps Convention-D Markov trace weights, 6x6 Gram G_D, and radical v."""
    one = mp.mpf(1)
    h_val = q - one / q
    z_d = (q ** 3) / (q * q + one)
    tr_weights = [
        one,
        z_d,
        z_d,
        z_d * z_d,
        z_d * z_d,
        h_val * z_d * z_d + z_d,
    ]
    g_mat = mp.matrix(6, 6)
    for i, wi in enumerate(NF_WORDS):
        nfi = word_to_nf_mp(wi, h_val)
        for j, wj in enumerate(NF_WORDS):
            prod_nf = list(nfi)
            for gen in wj:
                prod_nf = hm_nf_mp(prod_nf, one, mp.mpf(0), gen, h_val)
            g_mat[i, j] = mp.fsum(prod_nf[k] * tr_weights[k] for k in range(6))
    rad_v = [(-one / q) ** len(w) for w in NF_WORDS]
    return g_mat, tr_weights, rad_v


def wedderburn_characters_basis_mp(q: mp.mpf) -> dict[str, list[mp.mpf]]:
    """Characters chi_lambda(b_i) on the 6 NF basis elements of H_3(q) for lambda in {(3),(2,1),(1^3)}."""
    one = mp.mpf(1)
    zero = mp.mpf(0)
    neg_q_inv = -one / q
    # 2D standard representation rho_{(2,1)}:
    # rho(sigma_0) = [[q, 1], [0, -1/q]], rho(sigma_1) = [[-1/q, 0], [1, q]]
    r0 = mp.matrix([[q, one], [zero, neg_q_inv]])
    r1 = mp.matrix([[neg_q_inv, zero], [one, q]])
    eye2 = mp.eye(2)

    chi_3: list[mp.mpf] = []
    chi_21: list[mp.mpf] = []
    chi_111: list[mp.mpf] = []
    for w in NF_WORDS:
        chi_3.append(q ** len(w))
        chi_111.append(neg_q_inv ** len(w))
        m = eye2.copy()
        for gen in w:
            m = m * (r0 if gen == 0 else r1)
        chi_21.append(m[0, 0] + m[1, 1])
    return {"(3)": chi_3, "(2,1)": chi_21, "(1^3)": chi_111}


def build_candidate_costs_mp(q: mp.mpf, tr_weights: list[mp.mpf]) -> dict[str, list[mp.mpf]]:
    """Construct all 8 pre-registered zero-parameter 6D cost vectors on H_3(q)."""
    one = mp.mpf(1)
    zero = mp.mpf(0)
    h_val = q - one / q

    def tr_word(w: tuple[int, ...]) -> mp.mpf:
        nf = word_to_nf_mp(w, h_val)
        return mp.fsum(nf[k] * tr_weights[k] for k in range(6))

    # C0: Hecke Markov trace control t_i = tr_M(b_i)
    c0_hecke = list(tr_weights)

    # C1a & C1b: ECatProbeAssertions separation-dependent ordered-letter pair kernel
    # on each basis word w_i (cyclic arc separation vs open-word separation)
    c1a_pair_cyc: list[mp.mpf] = []
    c1b_pair_open: list[mp.mpf] = []
    for w in NF_WORDS:
        ell = len(w)
        acc_cyc = zero
        acc_open = zero
        for a in range(ell):
            for b in range(a + 1, ell):
                tr_ab = tr_word((w[a], w[b]))
                d_open = mp.mpf(b - a)
                d_cyc = mp.mpf(min(b - a, ell - (b - a)))
                acc_cyc += tr_ab / (d_cyc * d_cyc)
                acc_open += tr_ab / (d_open * d_open)
        c1a_pair_cyc.append(acc_cyc)
        c1b_pair_open.append(acc_open)

    # C2a: Backward q^{-2} Thomae-Jackson proper-time step cost per crossing q^{-2} * len(w_i)
    q_inv_sq = one / (q * q)
    c2a_tj_crossing = [q_inv_sq * mp.mpf(len(w)) for w in NF_WORDS]

    # C2b: Cumulative backward Thomae-Jackson geometric lattice cost q^{-2} * ((q^2)^{len(w_i)} - 1)
    q_sq = q * q
    c2b_tj_geom = [q_inv_sq * ((q_sq ** len(w)) - one) for w in NF_WORDS]

    # Full twist Delta_3^2 = (sigma_0 sigma_1 sigma_0)^2 in B_3
    full_twist_word = (0, 1, 0, 0, 1, 0)
    nf_full_twist = word_to_nf_mp(full_twist_word, h_val)

    # C3a: Markov-traced full-twist pairing tr_M(Delta_3^2 * b_i) (expected structural collapse)
    c3a_ft_markov: list[mp.mpf] = []
    for w in NF_WORDS:
        prod_nf = list(nf_full_twist)
        for gen in w:
            prod_nf = hm_nf_mp(prod_nf, one, zero, gen, h_val)
        c3a_ft_markov.append(mp.fsum(prod_nf[k] * tr_weights[k] for k in range(6)))

    # C3b: Unweighted regular/Wedderburn central Casimir shift
    # (1/6) * sum_lambda dim(lambda) * (c_lambda(q) - 1) * chi_lambda(b_i)
    chars = wedderburn_characters_basis_mp(q)
    c_sym = (q ** 6) - one
    c_std = zero  # q^{2*0} - 1 = 0 on (2,1)
    c_alt = (q ** (-6)) - one
    six = mp.mpf(6)
    c3b_ft_casimir = [
        (one * c_sym * chars["(3)"][i] + mp.mpf(2) * c_std * chars["(2,1)"][i] + one * c_alt * chars["(1^3)"][i]) / six
        for i in range(6)
    ]

    # C3c: Normal-form 6-vector nf(Delta_3^2) in H_3(q)
    c3c_ft_nf = list(nf_full_twist)

    return {
        "C0_hecke_trace_control": c0_hecke,
        "C1a_ecat_pair_kernel_cyclic": c1a_pair_cyc,
        "C1b_ecat_pair_kernel_open": c1b_pair_open,
        "C2a_thomae_jackson_bwd_crossing": c2a_tj_crossing,
        "C2b_thomae_jackson_bwd_geom_lattice": c2b_tj_geom,
        "C3a_full_twist_markov_trace_control": c3a_ft_markov,
        "C3b_full_twist_wedderburn_casimir": c3b_ft_casimir,
        "C3c_full_twist_nf_vector": c3c_ft_nf,
    }


def solve_quotient_and_dual_interval_mp(
    g_mat: mp.matrix,
    rad_v: list[mp.mpf],
    t_vec: list[mp.mpf],
    one_dot_v: mp.mpf,
    e0_mev: mp.mpf,
    eosc_mev: mp.mpf,
) -> dict[str, object]:
    """Compute <t,v>, y_0, MeV conversions, quotient solve y_min, and 1D cone interval."""
    vv = mp.fsum(rad_v[i] * rad_v[i] for i in range(6))
    a_mat = mp.matrix(6, 6)
    for i in range(6):
        for j in range(6):
            a_mat[i, j] = g_mat[i, j] + rad_v[i] * rad_v[j] / vv

    t_dot_v = mp.fsum(t_vec[i] * rad_v[i] for i in range(6))
    y0 = t_dot_v / one_dot_v
    rhs = [t_vec[i] - y0 for i in range(6)]
    rhs_rad_pairing = mp.fsum(rhs[i] * rad_v[i] for i in range(6))

    y_min_col = mp.lu_solve(a_mat, mp.matrix(rhs))
    y_min = [y_min_col[i, 0] for i in range(6)]
    y_min_dot_v = mp.fsum(y_min[i] * rad_v[i] for i in range(6))

    # Dual linear equality residual || y0 * 1 + G_D y_min - t ||_inf
    dual_eq_res = max(
        abs(y0 + mp.fsum(g_mat[i, j] * y_min[j] for j in range(6)) - t_vec[i])
        for i in range(6)
    )

    # 1D affine line y(alpha) = y_min + alpha * v >= 0:
    #   for i in POS_V_INDICES (v_i > 0): alpha >= -y_min[i] / v_i
    #   for j in NEG_V_INDICES (v_j < 0): alpha <= -y_min[j] / v_j
    alpha_lo = max(-y_min[i] / rad_v[i] for i in POS_V_INDICES)
    alpha_hi = min(-y_min[j] / rad_v[j] for j in NEG_V_INDICES)
    cone_margin = alpha_hi - alpha_lo
    dual_cone_feasible = alpha_lo <= alpha_hi

    # Also check opposite-sign cost (-t), where y_neg(alpha) = -y_min + alpha * v >= 0:
    neg_alpha_lo = max(y_min[i] / rad_v[i] for i in POS_V_INDICES)
    neg_alpha_hi = min(y_min[j] / rad_v[j] for j in NEG_V_INDICES)
    neg_cost_dual_feasible = neg_alpha_lo <= neg_alpha_hi

    witness_y_star = None
    witness_dual_eq_res = None
    witness_min_entry = None
    if dual_cone_feasible:
        alpha_mid = (alpha_lo + alpha_hi) / mp.mpf(2)
        y_star = [y_min[i] + alpha_mid * rad_v[i] for i in range(6)]
        witness_y_star = [fmt(val, dps=30) for val in y_star]
        witness_dual_eq_res = fmt(
            max(
                abs(y0 + mp.fsum(g_mat[i, j] * y_star[j] for j in range(6)) - t_vec[i])
                for i in range(6)
            ),
            dps=20,
        )
        witness_min_entry = fmt(min(y_star), dps=20)

    return {
        "raw": {
            "t_dot_v": t_dot_v,
            "y0": y0,
            "rhs_rad_pairing": rhs_rad_pairing,
            "y_min_dot_v": y_min_dot_v,
            "dual_eq_res": dual_eq_res,
            "alpha_lo": alpha_lo,
            "alpha_hi": alpha_hi,
            "cone_margin": cone_margin,
            "dual_cone_feasible": dual_cone_feasible,
            "neg_cost_dual_feasible": neg_cost_dual_feasible,
        },
        "serialized": {
            "t_vector": [fmt(val, dps=30) for val in t_vec],
            "t_dot_v": fmt(t_dot_v, dps=OUT_DPS),
            "y0_dimensionless": fmt(y0, dps=OUT_DPS),
            "y0_times_E0_MeV": fmt(y0 * e0_mev, dps=OUT_DPS),
            "y0_times_Eosc_MeV": fmt(y0 * eosc_mev, dps=OUT_DPS),
            "abs_y0_times_E0_MeV": fmt(abs(y0) * e0_mev, dps=OUT_DPS),
            "abs_y0_times_Eosc_MeV": fmt(abs(y0) * eosc_mev, dps=OUT_DPS),
            "residual_orthogonality_abs": fmt(abs(rhs_rad_pairing), dps=20),
            "dual_linear_equality_max_residual": fmt(dual_eq_res, dps=20),
            "y_min_quotient": [fmt(val, dps=30) for val in y_min],
            "alpha_lo": fmt(alpha_lo, dps=30),
            "alpha_hi": fmt(alpha_hi, dps=30),
            "cone_interval_margin_alpha_hi_minus_lo": fmt(cone_margin, dps=30),
            "dual_cone_feasible_y_ge_0": dual_cone_feasible,
            "negated_cost_dual_cone_feasible_y_ge_0": neg_cost_dual_feasible,
            "feasible_y_star_midpoint": witness_y_star,
            "feasible_y_star_dual_residual": witness_dual_eq_res,
            "feasible_y_star_min_entry": witness_min_entry,
        },
    }


def verify_exact_sympy_identities() -> dict[str, str]:
    """Exact Q(q) symbolic verification at rational q in {11/10, 7/5}."""
    results: dict[str, str] = {}
    for label, p_num, p_den in (("11_over_10", 11, 10), ("7_over_5", 7, 5)):
        q_rat = sp.Rational(p_num, p_den)
        z_rat = q_rat ** 3 / (q_rat ** 2 + 1)
        h_rat = q_rat - sp.Rational(1, 1) / q_rat
        v_rat = [(-sp.Rational(1, 1) / q_rat) ** len(w) for w in NF_WORDS]
        one_dot_v_sum = sum(v_rat)
        one_dot_v_formula = (q_rat - 1) * (q_rat ** 2 - q_rat + 1) / (q_rat ** 3)
        assert sp.simplify(one_dot_v_sum - one_dot_v_formula) == 0

        # C1a cyclic pair kernel exact rational check vs Lean theorem
        t_c1a = [
            sp.Integer(0),
            sp.Integer(0),
            sp.Integer(0),
            z_rat ** 2,
            z_rat ** 2,
            2 * z_rat ** 2 + h_rat * z_rat + 1,
        ]
        tv_c1a = sum(t_c1a[i] * v_rat[i] for i in range(6))
        tv_c1a_lean = (2 * q_rat ** 7 - 3 * q_rat ** 6 - q_rat ** 4 - q_rat ** 2 - 1) / (
            q_rat ** 3 * (q_rat ** 2 + 1) ** 2
        )
        assert sp.simplify(tv_c1a - tv_c1a_lean) == 0
        y0_c1a_rat = sp.simplify(tv_c1a / one_dot_v_sum)
        results[f"one_dot_v_at_{label}"] = str(one_dot_v_sum)
        results[f"y0_ecat_pair_cyclic_at_{label}"] = str(y0_c1a_rat)
    return results


def main() -> int:
    with mp.workdps(WORK_DPS):
        q0 = q_at(dps=WORK_DPS)
        one = mp.mpf(1)
        m_e_mev = codata("electron mass energy equivalent in mev").value
        hbar_q = one - one / q0
        e0_mev = m_e_mev / (q0 * (q0 - one))
        eosc_mev = m_e_mev / ((q0 - one) ** 2)

        g_mat, tr_weights, rad_v = build_convention_d_gram_mp(q0)
        rad_poly = [(-q0 ** 3) * rad_v[i] for i in range(6)]

        # 1. Radical annihilates G_D and <1, v_{(1^3)}> matches Lean closed form
        gv_max = max(
            abs(mp.fsum(g_mat[i, j] * rad_v[j] for j in range(6)))
            for i in range(6)
        )
        one_dot_v = mp.fsum(rad_v)
        one_dot_v_lean = (q0 - one) * (q0 * q0 - q0 + one) / (q0 ** 3)
        one_dot_v_poly = mp.fsum(rad_poly)
        one_dot_v_poly_lean = -(q0 - one) * (q0 * q0 - q0 + one)

        one_dot_v_diff = abs(one_dot_v - one_dot_v_lean)
        one_dot_v_poly_diff = abs(one_dot_v_poly - one_dot_v_poly_lean)

        # 2. Evaluate all 8 pre-registered candidate cost vectors
        candidates = build_candidate_costs_mp(q0, tr_weights)
        evals: dict[str, dict[str, object]] = {}
        for name, t_vec in candidates.items():
            evals[name] = solve_quotient_and_dual_interval_mp(
                g_mat=g_mat,
                rad_v=rad_v,
                t_vec=t_vec,
                one_dot_v=one_dot_v,
                e0_mev=e0_mev,
                eosc_mev=eosc_mev,
            )

        # 3. Cross-check closed-form Lean theorems from ECatRadicalShadowPriceEvaluation.lean
        lean_tv_c1a = (
            mp.mpf(2) * q0 ** 7 - mp.mpf(3) * q0 ** 6 - q0 ** 4 - q0 ** 2 - one
        ) / ((q0 ** 3) * ((q0 * q0 + one) ** 2))
        lean_y0_c1a = (
            mp.mpf(2) * q0 ** 7 - mp.mpf(3) * q0 ** 6 - q0 ** 4 - q0 ** 2 - one
        ) / ((q0 - one) * (q0 * q0 - q0 + one) * ((q0 * q0 + one) ** 2))

        lean_tv_c1b = (
            mp.mpf(8) * q0 ** 7 - mp.mpf(9) * q0 ** 6 - q0 ** 4 - q0 ** 2 - one
        ) / (mp.mpf(4) * (q0 ** 3) * ((q0 * q0 + one) ** 2))

        w_bwd = one / (q0 * q0)
        lean_tv_c2a = -w_bwd * (mp.mpf(2) * q0 * q0 - mp.mpf(4) * q0 + mp.mpf(3)) / (q0 ** 3)
        lean_y0_c2a = -w_bwd * (mp.mpf(2) * q0 * q0 - mp.mpf(4) * q0 + mp.mpf(3)) / (
            (q0 - one) * (q0 * q0 - q0 + one)
        )

        lean_tv_c2b = -(q0 - one) * (
            q0 ** 5 - q0 ** 4 + q0 ** 3 + q0 ** 2 - q0 + one
        ) / (q0 ** 5)

        lean_tv_c3c = q0 ** (-6)  # sign-rep value (-1/q0)^writhe(Delta_3^2), writhe = +6

        c0_tv_err = abs(evals["C0_hecke_trace_control"]["raw"]["t_dot_v"])
        c1a_tv_err = abs(evals["C1a_ecat_pair_kernel_cyclic"]["raw"]["t_dot_v"] - lean_tv_c1a)
        c1a_y0_err = abs(evals["C1a_ecat_pair_kernel_cyclic"]["raw"]["y0"] - lean_y0_c1a)
        c1b_tv_err = abs(evals["C1b_ecat_pair_kernel_open"]["raw"]["t_dot_v"] - lean_tv_c1b)
        c2a_tv_err = abs(evals["C2a_thomae_jackson_bwd_crossing"]["raw"]["t_dot_v"] - lean_tv_c2a)
        c2a_y0_err = abs(evals["C2a_thomae_jackson_bwd_crossing"]["raw"]["y0"] - lean_y0_c2a)
        c2b_tv_err = abs(evals["C2b_thomae_jackson_bwd_geom_lattice"]["raw"]["t_dot_v"] - lean_tv_c2b)
        c3a_tv_err = abs(evals["C3a_full_twist_markov_trace_control"]["raw"]["t_dot_v"])
        c3c_tv_err = abs(evals["C3c_full_twist_nf_vector"]["raw"]["t_dot_v"] - lean_tv_c3c)

        max_dual_eq_res = max(v["raw"]["dual_eq_res"] for v in evals.values())
        max_orth_res = max(abs(v["raw"]["rhs_rad_pairing"]) for v in evals.values())

        sympy_checks = verify_exact_sympy_identities()

        tol = mp.mpf("1e-70")
        assert gv_max < tol
        assert one_dot_v_diff < tol
        assert one_dot_v_poly_diff < tol
        assert c0_tv_err < tol
        assert c1a_tv_err < tol and c1a_y0_err < tol
        assert c1b_tv_err < tol
        assert c2a_tv_err < tol and c2a_y0_err < tol
        assert c2b_tv_err < tol
        assert c3a_tv_err < tol
        assert c3c_tv_err < tol
        assert max_dual_eq_res < tol
        assert max_orth_res < tol

        print("=== qou-udad: 6D H_3(q0) ECatLPDualRadical Shadow-Price Evaluation (80 dps) ===")
        print(f"  q0 (proton pin)          = {fmt(q0, dps=30)}")
        print(f"  E0(q0) [MeV]             = {fmt(e0_mev, dps=20)}")
        print(f"  E_osc(q0) = m_e c_q^2    = {fmt(eosc_mev, dps=20)}")
        print(f"  <1, v_(1^3)>             = {fmt(one_dot_v, dps=30)}")
        print(f"  <1, v_poly>              = {fmt(one_dot_v_poly, dps=30)}")
        print(f"  ||G_D v_(1^3)||_inf      = {fmt(gv_max, dps=12)}")
        print()
        header = (
            f"  {'candidate':<38} {'<t, v_(1^3)>':>18} {'y0 (dimless)':>18} "
            f"{'y0*E0 [MeV]':>15} {'y0*Eosc [MeV]':>15} {'y>=0?':>7} {'-t y>=0?':>9}"
        )
        print(header)
        print("  " + "-" * (len(header) - 2))
        for name, res in evals.items():
            r = res["raw"]
            print(
                f"  {name:<38} {mp.nstr(r['t_dot_v'], 10):>18} "
                f"{mp.nstr(r['y0'], 10):>18} "
                f"{mp.nstr(r['y0'] * e0_mev, 8):>15} "
                f"{mp.nstr(r['y0'] * eosc_mev, 8):>15} "
                f"{str(r['dual_cone_feasible']):>7} "
                f"{str(r['neg_cost_dual_feasible']):>9}"
            )

        wb = WitnessBuilder(Path(__file__).stem, engine="mpmath+sympy")
        wb.set_description(
            "80-dps (50-dps serialized) evaluation of solver-free ECatLPDualRadical "
            "shadow prices y_0 = <t_geom, v_(1^3)> / <1, v_(1^3)>, energy-unit "
            "conversions via E_0(q_0) and Compton E_osc(q_0) = m_e/(q_0 - 1)^2, and "
            "exact 1D dual cone feasibility intervals [alpha_lo, alpha_hi] across the "
            "8 pre-registered natural 6D H_3(q_0) normal-form cost vectors (Bean qou-udad)."
        )
        wb.add_parameter("q0", fmt(q0, dps=OUT_DPS))
        wb.add_parameter("q0_pin", "proton (qou_substrate.constants.q_at)")
        wb.add_parameter("work_dps", WORK_DPS)
        wb.add_parameter("output_dps", OUT_DPS)
        wb.add_parameter("E0_MeV", fmt(e0_mev, dps=OUT_DPS))
        wb.add_parameter("E_osc_MeV", fmt(eosc_mev, dps=OUT_DPS))
        wb.add_parameter("hbar_q", fmt(hbar_q, dps=OUT_DPS))

        wb.add_data(
            "radical_normalisation",
            {
                "basis_words": [list(w) for w in NF_WORDS],
                "basis_labels": NF_LABELS,
                "radical_v_1cubed": [fmt(val, dps=OUT_DPS) for val in rad_v],
                "radical_poly": [fmt(val, dps=OUT_DPS) for val in rad_poly],
                "one_dot_v_1cubed": fmt(one_dot_v, dps=OUT_DPS),
                "one_dot_v_poly": fmt(one_dot_v_poly, dps=OUT_DPS),
                "gram_radical_max_residual": fmt(gv_max, dps=20),
            },
        )
        wb.add_data(
            "candidates",
            {name: res["serialized"] for name, res in evals.items()},
        )
        wb.add_data("exact_sympy_rational_checks", sympy_checks)
        wb.add_data(
            "lean_module",
            "folio/quantum-observable-universe/lean/QOU/Nuclear/ECatRadicalShadowPriceEvaluation.lean",
        )

        wb.add_assertion(
            "inner_one_radicalVec3_matches_lean_closed_form",
            fmt(one_dot_v_diff, dps=15),
            "0",
            "1e-70",
            source="QOU.Nuclear.ECatRadicalShadowPriceEvaluation.inner_one_radicalVec3",
        )
        wb.add_assertion(
            "hecke_and_markov_fulltwist_costs_collapse_to_zero",
            fmt(max(c0_tv_err, c3a_tv_err), dps=15),
            "0",
            "1e-70",
            source="inner_heckeTraceCost_radicalVec3_eq_zero & convention-D y_(1^3)=0",
        )
        wb.add_assertion(
            "ecat_pair_cyclic_shadow_price_matches_lean_closed_form",
            fmt(max(c1a_tv_err, c1a_y0_err), dps=15),
            "0",
            "1e-70",
            source="QOU.Nuclear.ECatRadicalShadowPriceEvaluation.ecatPairCyclic_shadowPrice_closed_form",
        )
        wb.add_assertion(
            "thomae_jackson_crossing_shadow_price_matches_lean_closed_form",
            fmt(max(c2a_tv_err, c2a_y0_err), dps=15),
            "0",
            "1e-70",
            source="QOU.Nuclear.ECatRadicalShadowPriceEvaluation.thomaeJacksonCrossing_shadowPrice_closed_form",
        )
        wb.add_assertion(
            "all_candidates_satisfy_linear_dual_equality_on_quotient",
            fmt(max(max_dual_eq_res, max_orth_res), dps=15),
            "0",
            "1e-70",
            source="residual_orthogonal_to_radical & (G_D + P_v)^{-1} exact quotient solve",
        )

        wb.add_caveat(
            "Nonzero <t_geom, v_(1^3)> clears ECatLPDualRadical's linear escape bar "
            "and pins y_0 = <t_geom, v_(1^3)> / <1, v_(1^3)> uniquely, while dual "
            "cone non-negativity (y_min + alpha * v_(1^3) >= 0) is an independent "
            "1D interval condition [alpha_lo, alpha_hi] reported explicitly per cost."
        )

        out = wb.save({"q0Anchor": "proton", "q0Value": fmt(q0, dps=OUT_DPS)})
        print(f"\nwitness -> {out}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
