#!/usr/bin/env python3
"""EXPLORATORY shape-probe (pre-registered 80-dps verification, bean qou-8fw2):
Framed (V_2, W_3^*) 3-strand hyperbolic meson gluon-clasp invariants, zero-parameter
H_3(q_0) S^{(2,1)} diquark spin-isospin projector split (Lambda vs Sigma^0), and
O((q_0 - q_0^{-1})^2) 2nd-order rational quantum Casimir Gell-Mann-Okubo evaluation.

Pre-registration: PREREGISTRATION.md (committed in 3c6d1b9dc71 prior to evaluation).
Lean companions:
  - QOU/Eightfold/HyperbolicMesonClaspAndDiquarkSplit.lean
  - QOU/Eightfold/USpinColemanGlashowLambdaSigma.lean
  - QOU/Eightfold/GellMannOkuboSecondOrder.lean

Zero fitting (CAL-1/2/3 only), zero float64; proton pin q_0 = q_at(80).
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
for _p in ("computations", "computations/substrate", "tools/qou-substrate/python"):
    if str(ROOT / _p) not in sys.path:
        sys.path.insert(0, str(ROOT / _p))

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

import sympy as sp  # noqa: E402
from mpmath import mp, mpf  # noqa: E402

mp.dps = 80

from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_K_0_MEV_VALIDATION,
    M_K_PM_MEV_VALIDATION,
    M_N_MEV_VALIDATION,
    M_P_MEV_VALIDATION,
    M_PI_0_MEV_VALIDATION,
    M_PI_PM_MEV_VALIDATION,
)
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.constants import Q_MP, q_at  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402


def fmt50(x: mpf) -> str:
    return mp.nstr(x, 50)


def mat2_mul(
    a: tuple[tuple[mpf, mpf], tuple[mpf, mpf]],
    b: tuple[tuple[mpf, mpf], tuple[mpf, mpf]],
) -> tuple[tuple[mpf, mpf], tuple[mpf, mpf]]:
    return (
        (a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]),
        (a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]),
    )


def mat2_pow(
    a: tuple[tuple[mpf, mpf], tuple[mpf, mpf]], n: int
) -> tuple[tuple[mpf, mpf], tuple[mpf, mpf]]:
    res = ((mpf(1), mpf(0)), (mpf(0), mpf(1)))
    base = a
    k = n
    while k > 0:
        if k & 1:
            res = mat2_mul(res, base)
        base = mat2_mul(base, base)
        k >>= 1
    return res


def mat2_det(a: tuple[tuple[mpf, mpf], tuple[mpf, mpf]]) -> mpf:
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def mat2_tr(a: tuple[tuple[mpf, mpf], tuple[mpf, mpf]]) -> mpf:
    return a[0][0] + a[1][1]


def mat2_sub_norm(
    a: tuple[tuple[mpf, mpf], tuple[mpf, mpf]],
    b: tuple[tuple[mpf, mpf], tuple[mpf, mpf]],
) -> mpf:
    return (
        abs(a[0][0] - b[0][0])
        + abs(a[0][1] - b[0][1])
        + abs(a[1][0] - b[1][0])
        + abs(a[1][1] - b[1][1])
    )


def mat3_mul(
    a: list[list[mpf]], b: list[list[mpf]]
) -> list[list[mpf]]:
    return [
        [sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)]
        for i in range(3)
    ]


def mat3_pow(a: list[list[mpf]], n: int) -> list[list[mpf]]:
    res = [
        [mpf(1) if i == j else mpf(0) for j in range(3)]
        for i in range(3)
    ]
    base = a
    k = n
    while k > 0:
        if k & 1:
            res = mat3_mul(res, base)
        base = mat3_mul(base, base)
        k >>= 1
    return res


def mat3_tr(a: list[list[mpf]]) -> mpf:
    return a[0][0] + a[1][1] + a[2][2]


def mat3_sub_norm(a: list[list[mpf]], b: list[list[mpf]]) -> mpf:
    return sum(abs(a[i][j] - b[i][j]) for i in range(3) for j in range(3))


def main() -> int:
    with mp.workdps(80):
        q0 = q_at(80)
        qi0 = mpf(1) / q0
        h0 = q0 - qi0

        def q_int(n: int) -> mpf:
            return (q0 ** n - qi0 ** n) / h0

        q2 = q_int(2)
        q3 = q_int(3)
        q4 = q_int(4)
        q5 = q_int(5)

        wb = WitnessBuilder(
            "sm8w-eightfold-clasp-diquark-gmo",
            engine="mpmath (80 dps) + sympy Q(q)",
            output_dir=HERE,
        )
        wb.set_description(
            "Pre-registered 80-dps evaluation of (1) split-bundle F = V_2 (+) W_3^* "
            "(z_3 = q^3/[3]_q) quantum W_3^{x3} = 10 + 8 + 8 + 1 decomposition and 3-strand "
            "hyperbolic meson gluon-clasp invariants separating Dbar^0 from K^0; "
            "(2) zero-parameter H_3(q_0) S^{(2,1)} diquark spin-isospin projector split "
            "(Lambda vs Sigma^0) and microscopic Borromean V^3 Coleman-Glashow cancellation; "
            "(3) O((q_0 - q_0^{-1})^2) 2nd-order rational quantum Casimir Gell-Mann-Okubo "
            "ratio vs PDG-2024 hadron masses (beans qou-8fw2, qou-8fl1, qou-3ttt, qou-qpj9, "
            "qou-pwz4, qou-c9uj, qou-3oi0)."
        )
        wb.add_parameter("workdps", 80)
        wb.add_parameter("q0_proton_50dps", fmt50(q0))
        wb.add_parameter("h0_50dps", fmt50(h0))
        wb.add_parameter("preregistration_commit", "3c6d1b9dc71")

        wb.add_assertion(
            "q0_at_80_matches_Q_MP",
            computed=abs(q0 - (+Q_MP)),
            expected=mpf(0),
            tolerance=mpf("1e-65"),
            source="qou_substrate.constants",
        )

        # ======================================================================
        # P1. Split-Bundle F = V_2 (+) W_3^*, Quantum W_3^{x3}, & 3-Strand Clasp
        # ======================================================================
        z2 = (q0 ** 3) / (q0 ** 2 + mpf(1))
        z3 = (q0 ** 3) / q3
        z3_rat = (q0 ** 5) / (q0 ** 4 + q0 ** 2 + mpf(1))
        z2_sub_z3_closed = (q0 ** 3) / (
            (q0 ** 2 + mpf(1)) * (q0 ** 4 + q0 ** 2 + mpf(1))
        )

        wb.add_assertion(
            "P1_z3_equals_q5_over_q4_q2_1",
            computed=abs(z3 - z3_rat),
            expected=mpf(0),
            tolerance=mpf("1e-77"),
            source="HyperbolicMesonClaspAndDiquarkSplit.zRank3_eq_rational",
        )
        wb.add_assertion(
            "P1_z2_sub_z3_closed_form_exact",
            computed=abs((z2 - z3) - z2_sub_z3_closed),
            expected=mpf(0),
            tolerance=mpf("1e-77"),
            source="HyperbolicMesonClaspAndDiquarkSplit.zRank2_sub_zRank3",
        )
        wb.add_assertion(
            "P1_z2_strictly_exceeds_z3",
            computed=mpf(1) if (z2 - z3) > mpf(0) else mpf(0),
            expected=mpf(1),
            tolerance=mpf("1e-78"),
            source="HyperbolicMesonClaspAndDiquarkSplit.zRank2_sub_zRank3",
        )

        dim_q_10 = (q0 ** 2 + qi0 ** 2) * q5
        dim_q_8 = q2 * q4
        dim_q_1 = mpf(1)
        w3_sym = dim_q_10 / (q3 ** 3)
        w3_mix = dim_q_8 / (q3 ** 3)
        w3_alt = dim_q_1 / (q3 ** 3)
        w2_sym = (q0 ** 4 + mpf(1)) / ((q0 ** 2 + mpf(1)) ** 2)
        w2_mix = (q0 ** 2) / ((q0 ** 2 + mpf(1)) ** 2)

        wb.add_assertion(
            "P1_quantum_cube_3x3x3_equals_qBracket3_cubed",
            computed=abs((dim_q_10 + mpf(2) * dim_q_8 + dim_q_1) - (q3 ** 3)),
            expected=mpf(0),
            tolerance=mpf("1e-76"),
            source="HyperbolicMesonClaspAndDiquarkSplit.quantum_cube_3x3x3_and_decuplet_10",
        )
        wb.add_assertion(
            "P1_rank3_ocneanu_weights_sum_to_one",
            computed=abs((w3_sym + mpf(2) * w3_mix + w3_alt) - mpf(1)),
            expected=mpf(0),
            tolerance=mpf("1e-77"),
            source="HyperbolicMesonClaspAndDiquarkSplit.quantum_cube_3x3x3_and_decuplet_10",
        )

        # Split-bundle Killing traces & Weinberg 3/8 + framed strand charges
        tr_t3_sq = (mpf(1) / mpf(2)) ** 2 + (-mpf(1) / mpf(2)) ** 2
        tr_half_yf_sq = mpf(2) * ((mpf(1) / mpf(2)) ** 2) + mpf(3) * (
            (-mpf(1) / mpf(3)) ** 2
        )
        weinberg_split_bundle = tr_t3_sq / (tr_t3_sq + tr_half_yf_sq)
        wb.add_assertion(
            "P1_split_bundle_killing_weinberg_3_over_8",
            computed=abs(weinberg_split_bundle - (mpf(3) / mpf(8))),
            expected=mpf(0),
            tolerance=mpf("1e-78"),
            source="HyperbolicMesonClaspAndDiquarkSplit.splitBundle_killing_traces",
        )

        def framed_charge(s2: int, tau3: int) -> mpf:
            return mpf(s2) / mpf(2) + mpf(tau3) / mpf(6)

        q_u = framed_charge(+1, +1)
        q_d = framed_charge(-1, +1)
        q_dbar = framed_charge(+1, -1)
        q_ubar = framed_charge(-1, -1)
        wb.add_assertion(
            "P1_framed_antiUp_down_separation_one_third",
            computed=abs((q_d - q_ubar) - (mpf(1) / mpf(3)))
            + abs(q_u - mpf(2) / mpf(3))
            + abs(q_d + mpf(1) / mpf(3))
            + abs(q_dbar - mpf(1) / mpf(3))
            + abs(q_ubar + mpf(2) / mpf(3)),
            expected=mpf(0),
            tolerance=mpf("1e-78"),
            source="HyperbolicMesonClaspAndDiquarkSplit.antiUp_down_same_weakSign_yet_distinct_charge",
        )

        # 2x2 S^{(2,1)} Hecke representation (matching BorromeanFlavourPivotalUnification)
        s1_21 = ((-qi0, -mpf(1)), (mpf(0), q0))
        s2_21 = ((q0, mpf(0)), (-mpf(1), -qi0))
        s2_inv_21 = ((qi0, mpf(0)), (-mpf(1), -q0))
        v_21 = mat2_mul(s1_21, s2_inv_21)

        generations = (3, 5, 7)
        clasp_grid: dict[tuple[int, int], dict[str, object]] = {}
        clasp_table_rows = []
        max_det_err = mpf(0)
        max_abs_tr21 = mpf(0)
        min_sl2_tr = 999

        for n1 in generations:
            for n2 in generations:
                c_mat = mat2_mul(
                    mat2_mul(mat2_pow(s1_21, n1), mat2_pow(s2_inv_21, n2)), v_21
                )
                det_c = mat2_det(c_mat)
                tr_c = mat2_tr(c_mat)
                max_det_err = max(max_det_err, abs(det_c - mpf(1)))
                max_abs_tr21 = max(max_abs_tr21, abs(tr_c))

                sl2_tr = 2 * n1 * n2 + n1 + n2 + 3
                min_sl2_tr = min(min_sl2_tr, sl2_tr)
                sl2_tr_mp = mpf(sl2_tr)
                lambda_pa = (sl2_tr_mp + mp.sqrt(sl2_tr_mp ** 2 - mpf(4))) / mpf(2)

                tr_sym = (q0 ** n1) * (qi0 ** n2)
                tr_alt = ((-qi0) ** n1) * ((-q0) ** n2)
                tr_m2 = w2_sym * tr_sym + w2_mix * tr_c
                tr_m3 = w3_sym * tr_sym + w3_mix * tr_c + w3_alt * tr_alt

                clasp_grid[(n1, n2)] = {
                    "tr21": tr_c,
                    "tr_m2": tr_m2,
                    "tr_m3": tr_m3,
                    "sl2_tr": sl2_tr,
                    "lambda_pa": lambda_pa,
                }
                clasp_table_rows.append(
                    {
                        "n1": n1,
                        "n2": n2,
                        "sl2_monodromy_trace": sl2_tr,
                        "pseudo_anosov_dilatation": fmt50(lambda_pa),
                        "det_rho21": fmt50(det_c),
                        "tr_rho21_q0": fmt50(tr_c),
                        "tr_markov_rank2_z2": fmt50(tr_m2),
                        "tr_markov_rank3_z3": fmt50(tr_m3),
                    }
                )

        wb.add_assertion(
            "P1_clasp_det_rho21_equals_1_all_9_pairs",
            computed=max_det_err,
            expected=mpf(0),
            tolerance=mpf("1e-76"),
            source="HyperbolicMesonClaspAndDiquarkSplit.claspMarkovTrace_separates_Dbar0_K0",
        )
        wb.add_assertion(
            "P1_clasp_sl2_monodromy_hyperbolic_ge_27_and_real_hecke_elliptic_diagnostic",
            computed=mpf(1)
            if (min_sl2_tr == 27 and max_abs_tr21 < mpf(2))
            else mpf(0),
            expected=mpf(1),
            tolerance=mpf("1e-78"),
            source="HyperbolicMesonClaspAndDiquarkSplit.claspSL2_hyperbolic_all_generations",
        )

        # Ordered-pair asymmetry checks on (5,3) vs (3,5) [Dbar^0 vs K^0], (7,3) vs (3,7), (7,5) vs (5,7)
        asymmetry_rows = []
        max_tr21_sym_err = mpf(0)
        max_m2_formula_err = mpf(0)
        max_m3_formula_err = mpf(0)
        all_distinct_nonzero = True
        for n1, n2, label in (
            (5, 3, "Dbar0_5_3_vs_K0_3_5"),
            (7, 3, "B_7_3_vs_3_7"),
            (7, 5, "Bs_Bc_7_5_vs_5_7"),
        ):
            a = clasp_grid[(n1, n2)]
            b = clasp_grid[(n2, n1)]
            d_tr21 = abs(a["tr21"] - b["tr21"])  # type: ignore[operator]
            d_m2 = a["tr_m2"] - b["tr_m2"]  # type: ignore[operator]
            d_m3 = a["tr_m3"] - b["tr_m3"]  # type: ignore[operator]
            dn = n1 - n2
            # Note: (-q^-1)^n1 (-q)^n2 has sign (-1)^(n1+n2) = +1 for odd n1, n2
            f_m2 = w2_sym * (q0 ** dn - qi0 ** dn)
            f_m3 = (w3_sym - w3_alt) * (q0 ** dn - qi0 ** dn)
            max_tr21_sym_err = max(max_tr21_sym_err, d_tr21)
            max_m2_formula_err = max(max_m2_formula_err, abs(d_m2 - f_m2))
            max_m3_formula_err = max(max_m3_formula_err, abs(d_m3 - f_m3))
            if abs(d_m2) <= mpf("1e-10") or abs(d_m3) <= mpf("1e-10"):
                all_distinct_nonzero = False
            asymmetry_rows.append(
                {
                    "pair": label,
                    "abs_diff_tr_rho21": fmt50(d_tr21),
                    "diff_markov_z2": fmt50(d_m2),
                    "diff_markov_z2_closed_form": fmt50(f_m2),
                    "diff_markov_z3": fmt50(d_m3),
                    "diff_markov_z3_closed_form": fmt50(f_m3),
                }
            )

        wb.add_assertion(
            "P1_clasp_rho21_trace_symmetric_under_swap",
            computed=max_tr21_sym_err,
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="HyperbolicMesonClaspAndDiquarkSplit.claspMarkovTrace_separates_Dbar0_K0",
        )
        wb.add_assertion(
            "P1_clasp_markov_z2_asymmetry_matches_closed_form",
            computed=max_m2_formula_err,
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="HyperbolicMesonClaspAndDiquarkSplit.claspMarkovTrace_separates_Dbar0_K0",
        )
        wb.add_assertion(
            "P1_clasp_markov_z3_asymmetry_matches_closed_form",
            computed=max_m3_formula_err,
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="HyperbolicMesonClaspAndDiquarkSplit.claspMarkovTrace_separates_Dbar0_K0",
        )

        # Five dictionary mesons (pion, kaon, etaPhi, Dmeson, K0) injectivity check
        meson_clasp_invariants = {
            "pion": ((3, 3), -4, 4),
            "kaon": ((3, 5), -4, -2),
            "etaPhi": ((5, 5), 2, -2),
            "Dmeson": ((5, 3), -4, 4),
            "K0": ((3, 5), 2, -2),
        }
        unique_meson_count = len(set(meson_clasp_invariants.values()))
        wb.add_assertion(
            "P1_all_five_dictionary_mesons_pairwise_distinct_and_Dbar0_ne_K0",
            computed=mpf(1)
            if (unique_meson_count == 5 and all_distinct_nonzero)
            else mpf(0),
            expected=mpf(1),
            tolerance=mpf("1e-78"),
            source="HyperbolicMesonClaspAndDiquarkSplit.framedMesonClaspDatum_injective",
        )

        # ======================================================================
        # P2. Zero-Parameter H_3(q_0) S^{(2,1)} Diquark Projector Split
        # ======================================================================
        inv_q2 = mpf(1) / q2
        p_lam = ((mpf(1), inv_q2), (mpf(0), mpf(0)))
        p_sig = ((mpf(0), -inv_q2), (mpf(0), mpf(1)))
        id2 = ((mpf(1), mpf(0)), (mpf(0), mpf(1)))
        z2_zero = ((mpf(0), mpf(0)), (mpf(0), mpf(0)))

        idem_err_2d = (
            mat2_sub_norm(
                (
                    (p_lam[0][0] + p_sig[0][0], p_lam[0][1] + p_sig[0][1]),
                    (p_lam[1][0] + p_sig[1][0], p_lam[1][1] + p_sig[1][1]),
                ),
                id2,
            )
            + mat2_sub_norm(mat2_mul(p_lam, p_lam), p_lam)
            + mat2_sub_norm(mat2_mul(p_sig, p_sig), p_sig)
            + mat2_sub_norm(mat2_mul(p_lam, p_sig), z2_zero)
            + mat2_sub_norm(mat2_mul(p_sig, p_lam), z2_zero)
            + abs(mat2_tr(p_lam) - mpf(1))
            + abs(mat2_tr(p_sig) - mpf(1))
        )
        wb.add_assertion(
            "P2_2D_diquark_projectors_complete_orthogonal_idempotents",
            computed=idem_err_2d,
            expected=mpf(0),
            tolerance=mpf("1e-77"),
            source="HyperbolicMesonClaspAndDiquarkSplit.projDiquark_complete_orthogonal_idempotents",
        )

        # 3D baryon weight-space matrices A_1, A_2, A_2^{-1} & projectors eLambda, eSigma0
        # Exact match to QOU.BraidsAndKnots.NucleonWeightSpaceTraces / NucleonWeightSpaceTwoTerm
        a1_w = [
            [q0, mpf(0), mpf(0)],
            [mpf(0), mpf(0), mpf(1)],
            [mpf(0), mpf(1), h0],
        ]
        a2_w = [
            [mpf(0), mpf(1), mpf(0)],
            [mpf(1), h0, mpf(0)],
            [mpf(0), mpf(0), q0],
        ]
        a2_inv_w = [
            [-h0, mpf(1), mpf(0)],
            [mpf(1), mpf(0), mpf(0)],
            [mpf(0), mpf(0), qi0],
        ]
        v_w = mat3_mul(a1_w, a2_inv_w)
        v3_w = mat3_pow(v_w, 3)

        id3_w = [[mpf(1) if i == j else mpf(0) for j in range(3)] for i in range(3)]
        c_sym = mpf(1) / q3
        e_sym_w = [
            [(qi0 ** 2) * c_sym, qi0 * c_sym, c_sym],
            [qi0 * c_sym, c_sym, q0 * c_sym],
            [c_sym, q0 * c_sym, (q0 ** 2) * c_sym],
        ]
        e21p_w = [
            [id3_w[i][j] - e_sym_w[i][j] for j in range(3)] for i in range(3)
        ]
        e_lam_w = [
            [(q0 * id3_w[i][j] - a1_w[i][j]) / q2 for j in range(3)]
            for i in range(3)
        ]
        e_sig_w = [
            [e21p_w[i][j] - e_lam_w[i][j] for j in range(3)] for i in range(3)
        ]
        sum_3d = [
            [e_lam_w[i][j] + e_sig_w[i][j] + e_sym_w[i][j] for j in range(3)]
            for i in range(3)
        ]

        v3_21 = mat2_pow(v_21, 3)
        cross_rep_err = (
            mat3_sub_norm(sum_3d, id3_w)
            + abs(mat2_tr(mat2_mul(p_lam, s1_21)) - mat3_tr(mat3_mul(e_lam_w, a1_w)))
            + abs(mat2_tr(mat2_mul(p_sig, s1_21)) - mat3_tr(mat3_mul(e_sig_w, a1_w)))
            + abs(mat2_tr(mat2_mul(p_lam, s2_21)) - mat3_tr(mat3_mul(e_lam_w, a2_w)))
            + abs(mat2_tr(mat2_mul(p_sig, s2_21)) - mat3_tr(mat3_mul(e_sig_w, a2_w)))
            + abs(mat2_tr(mat2_mul(p_lam, v_21)) - mat3_tr(mat3_mul(e_lam_w, v_w)))
            + abs(mat2_tr(mat2_mul(p_sig, v_21)) - mat3_tr(mat3_mul(e_sig_w, v_w)))
            + abs(mat2_tr(mat2_mul(p_lam, v3_21)) - mat3_tr(mat3_mul(e_lam_w, v3_w)))
            + abs(mat2_tr(mat2_mul(p_sig, v3_21)) - mat3_tr(mat3_mul(e_sig_w, v3_w)))
        )
        wb.add_assertion(
            "P2_2D_and_3D_diquark_projectors_agree_on_sigma1_sigma2_V_V3",
            computed=cross_rep_err,
            expected=mpf(0),
            tolerance=mpf("1e-76"),
            source="HyperbolicMesonClaspAndDiquarkSplit.jm2_jm3_comm_and_diquark_split",
        )

        # Jucys-Murphy twists J_2, J_3 and closed-form V, V^3 diquark splits
        jm2 = mat2_pow(s1_21, 2)
        jm3 = mat2_mul(mat2_mul(s2_21, jm2), s2_21)
        jm_comm_err = mat2_sub_norm(mat2_mul(jm2, jm3), mat2_mul(jm3, jm2))
        tr_sig_s1 = mat2_tr(mat2_mul(p_sig, s1_21))
        tr_lam_s1 = mat2_tr(mat2_mul(p_lam, s1_21))
        tr_sig_jm2 = mat2_tr(mat2_mul(p_sig, jm2))
        tr_lam_jm2 = mat2_tr(mat2_mul(p_lam, jm2))
        tr_sig_v = mat2_tr(mat2_mul(p_sig, v_21))
        tr_lam_v = mat2_tr(mat2_mul(p_lam, v_21))
        tr_sig_v3 = mat2_tr(mat2_mul(p_sig, v3_21))
        tr_lam_v3 = mat2_tr(mat2_mul(p_lam, v3_21))

        v3_split_form1 = (h0 ** 3) * q3 * q4 / (q2 ** 2)
        v3_split_form2 = (h0 ** 3) * (q0 ** 2 + qi0 ** 2) * q3 / q2

        wb.add_assertion(
            "P2_jucys_murphy_comm_and_jm2_eigenvalues_exact",
            computed=jm_comm_err
            + abs((tr_sig_s1 - tr_lam_s1) - q2)
            + abs(tr_sig_jm2 - (q0 ** 2))
            + abs(tr_lam_jm2 - (qi0 ** 2))
            + abs((tr_sig_jm2 - tr_lam_jm2) - h0 * q2),
            expected=mpf(0),
            tolerance=mpf("1e-76"),
            source="HyperbolicMesonClaspAndDiquarkSplit.jm2_jm3_comm_and_diquark_split",
        )
        wb.add_assertion(
            "P2_borromean_V_ratio_q6_and_V3_diquark_split_closed_form",
            computed=abs(abs(tr_sig_v) / abs(tr_lam_v) - (q0 ** 6))
            + abs((abs(tr_sig_v) - abs(tr_lam_v)) - (h0 * q3 / q2))
            + abs((tr_lam_v3 - tr_sig_v3) - v3_split_form1)
            + abs(v3_split_form1 - v3_split_form2),
            expected=mpf(0),
            tolerance=mpf("1e-76"),
            source="HyperbolicMesonClaspAndDiquarkSplit.trace_projDiquark_V_and_V3_split",
        )

        # Microscopic Borromean V^3 Coleman-Glashow QED cancellation check
        qu = mpf(2) / mpf(3)
        qd = -mpf(1) / mpf(3)
        qs = -mpf(1) / mpf(3)

        def pair_charge_sum(c1: mpf, c2: mpf, c3: mpf) -> mpf:
            return c1 * c2 + c1 * c3 + c2 * c3

        tr_w_v3 = mat3_tr(v3_w)
        alpha_qed = mpf(codata("fine-structure constant").value_str)
        em_p = alpha_qed * pair_charge_sum(qu, qu, qd) * tr_w_v3
        em_n = alpha_qed * pair_charge_sum(qu, qd, qd) * tr_w_v3
        em_sp = alpha_qed * pair_charge_sum(qu, qu, qs) * tr_w_v3
        em_sm = alpha_qed * pair_charge_sum(qd, qd, qs) * tr_w_v3
        em_x0 = alpha_qed * pair_charge_sum(qu, qs, qs) * tr_w_v3
        em_xm = alpha_qed * pair_charge_sum(qd, qs, qs) * tr_w_v3
        cg_borromean_em = (em_p - em_n) - (em_sp - em_sm) + (em_x0 - em_xm)

        wb.add_assertion(
            "P2_microscopic_borromean_V3_coleman_glashow_zero",
            computed=abs(cg_borromean_em),
            expected=mpf(0),
            tolerance=mpf("1e-78"),
            source="USpinColemanGlashowLambdaSigma.borromean_coulomb_coleman_glashow_zero",
        )

        # Validation-only PDG-2024 / CODATA-2022 comparison benchmarks (NEVER upstream inputs)
        m_e_str = codata("electron mass energy equivalent in MeV").value_str
        m_p_str = codata("proton mass energy equivalent in MeV").value_str
        m_n_str = codata("neutron mass energy equivalent in MeV").value_str
        m_e_mp = mpf(m_e_str)
        m_p_mp = mpf(m_p_str)
        m_n_mp = mpf(m_n_str)

        # Cross-check registry validation constants
        wb.add_assertion(
            "codata_registry_nucleon_and_electron_consistency",
            computed=abs(m_e_mp - (+M_E_MEV))
            + abs(m_p_mp - (+M_P_MEV_VALIDATION))
            + abs(m_n_mp - (+M_N_MEV_VALIDATION)),
            expected=mpf(0),
            tolerance=mpf("1e-45"),
            source="codata_constants",
        )

        m_pi_pm_str = "139.57039"
        m_pi_0_str = "134.9768"
        m_k_pm_str = "493.677"
        m_k_0_str = "497.611"
        m_eta_str = "547.862"
        m_lambda_str = "1115.683"
        m_sigma0_str = "1192.642"
        m_sigma_p_str = "1189.37"
        m_sigma_m_str = "1197.449"
        m_xi0_str = "1314.86"
        m_xim_str = "1321.71"

        m_pi_pm = mpf(m_pi_pm_str)  # noqa: P31 (PDG-2024 validation comparator)
        m_pi_0 = mpf(m_pi_0_str)  # noqa: P31 (PDG-2024 validation comparator)
        m_k_pm = mpf(m_k_pm_str)  # noqa: P31 (PDG-2024 validation comparator)
        m_k_0 = mpf(m_k_0_str)  # noqa: P31 (PDG-2024 validation comparator)
        m_eta = mpf(m_eta_str)  # noqa: P31 (PDG-2024 validation comparator)
        m_lambda = mpf(m_lambda_str)  # noqa: P31 (PDG-2024 validation comparator)
        m_sigma0 = mpf(m_sigma0_str)  # noqa: P31 (PDG-2024 validation comparator)
        m_sigma_p = mpf(m_sigma_p_str)  # noqa: P31 (PDG-2024 validation comparator)
        m_sigma_m = mpf(m_sigma_m_str)  # noqa: P31 (PDG-2024 validation comparator)
        m_xi0 = mpf(m_xi0_str)  # noqa: P31 (PDG-2024 validation comparator)
        m_xim = mpf(m_xim_str)  # noqa: P31 (PDG-2024 validation comparator)

        wb.add_assertion(
            "codata_registry_meson_validation_consistency",
            computed=abs(m_pi_pm - (+M_PI_PM_MEV_VALIDATION))
            + abs(m_pi_0 - (+M_PI_0_MEV_VALIDATION))
            + abs(m_k_pm - (+M_K_PM_MEV_VALIDATION))
            + abs(m_k_0 - (+M_K_0_MEV_VALIDATION)),
            expected=mpf(0),
            tolerance=mpf("1e-45"),
            source="codata_constants",
        )

        exp_sigma0_over_lambda = m_sigma0 / m_lambda
        exp_delta_sigma0_lambda = m_sigma0 - m_lambda
        diquark_ratio_candidates = [
            ("q0_single_crossing_eigenvalue", q0),
            ("q0_sq_JM_half_twist", q0 ** 2),
            ("q0_fourth_JM2_ratio", q0 ** 4),
            ("one_plus_half_JM2_diff", mpf(1) + h0 * q2 / mpf(2)),
            ("one_plus_borromean_V3_diquark_split", mpf(1) + v3_split_form1),
            ("abs_tr_P_Lambda_V3_over_abs_tr_P_Sigma0_V3", abs(tr_lam_v3) / abs(tr_sig_v3)),
        ]
        diquark_comparison_rows = []
        for cname, cval in diquark_ratio_candidates:
            implied_split_mev = (cval - mpf(1)) * m_lambda
            rel_err_ratio = (cval - exp_sigma0_over_lambda) / exp_sigma0_over_lambda
            rel_err_split = (
                implied_split_mev - exp_delta_sigma0_lambda
            ) / exp_delta_sigma0_lambda
            diquark_comparison_rows.append(
                {
                    "candidate": cname,
                    "zero_param_ratio": fmt50(cval),
                    "pdg_m_Sigma0_over_m_Lambda": fmt50(exp_sigma0_over_lambda),
                    "rel_diff_on_mass_ratio": fmt50(rel_err_ratio),
                    "implied_splitting_MeV_from_m_Lambda": fmt50(implied_split_mev),
                    "rel_diff_on_76p959_MeV_splitting": fmt50(rel_err_split),
                }
            )

        # ======================================================================
        # P3. O((q_0 - q_0^{-1})^2) 2nd-Order Rational Quantum Casimir GMO Law
        # ======================================================================
        d_q_i1 = q2
        d_q_i0 = mpf(0)
        d_q_doublet = q2 / (q2 + mpf(2))

        ratio_qcasimir_1 = -(((q0 - mpf(1)) / (q0 + mpf(1))) ** 2)
        ratio_qcasimir_2 = -(h0 ** 2) / ((q2 + mpf(2)) ** 2)

        def q_octet_gmo_ratio(a_val: mpf, b_val: mpf, c_val: mpf) -> mpf:
            m_kp = a_val + b_val * mpf(1) + c_val * d_q_doublet
            m_kb = a_val + b_val * (-mpf(1)) + c_val * d_q_doublet
            m_00 = a_val + c_val * d_q_i0
            m_10 = a_val + c_val * d_q_i1
            gmo_num = mpf(2) * (m_kp + m_kb) - mpf(3) * m_00 - m_10
            return gmo_num / (m_10 - m_00)

        max_gmo_ratio_err = abs(ratio_qcasimir_1 - ratio_qcasimir_2)
        for a_t, b_t, c_t in (
            (mpf("100"), mpf("-37"), mpf("13")),
            (mpf("512.25"), mpf("89.5"), mpf("-7.125")),
            (mpf("1150"), mpf("-190"), mpf("38.5")),
        ):
            max_gmo_ratio_err = max(
                max_gmo_ratio_err, abs(q_octet_gmo_ratio(a_t, b_t, c_t) - ratio_qcasimir_1)
            )

        wb.add_assertion(
            "P3_quantum_casimir_gmo_universal_ratio_exact",
            computed=max_gmo_ratio_err,
            expected=mpf(0),
            tolerance=mpf("1e-77"),
            source="HyperbolicMesonClaspAndDiquarkSplit.qCasimir_gmo_second_order_and_universal_ratio",
        )

        # SymPy symbolic verification of Q(q) exact identities
        q_sym = sp.Symbol("q", positive=True)
        qi_sym = 1 / q_sym
        q2_sym = q_sym + qi_sym
        d_half_sym = q2_sym / (q2_sym + 2)
        gmo_sym = sp.simplify((4 * d_half_sym - q2_sym) / q2_sym)
        assert sp.simplify(gmo_sym + ((q_sym - 1) / (q_sym + 1)) ** 2) == 0

        # Empirical PDG-2024 meson (m^2, isospin-averaged and neutral) & baryon (linear m) GMO residuals
        m_pi_avg_sq = (mpf(2) * (m_pi_pm ** 2) + (m_pi_0 ** 2)) / mpf(3)
        m_k_avg_sq = ((m_k_pm ** 2) + (m_k_0 ** 2)) / mpf(2)
        m_eta_sq = m_eta ** 2

        meson_gmo_lhs_minus_rhs_avg = mpf(4) * m_k_avg_sq - mpf(3) * m_eta_sq - m_pi_avg_sq
        meson_rel_dev_over_4mK2_avg = meson_gmo_lhs_minus_rhs_avg / (mpf(4) * m_k_avg_sq)
        meson_norm_ratio_avg = meson_gmo_lhs_minus_rhs_avg / (m_pi_avg_sq - m_eta_sq)

        meson_gmo_lhs_minus_rhs_neutral = (
            mpf(4) * (m_k_0 ** 2) - mpf(3) * m_eta_sq - (m_pi_0 ** 2)
        )
        meson_rel_dev_over_4mK02 = meson_gmo_lhs_minus_rhs_neutral / (
            mpf(4) * (m_k_0 ** 2)
        )
        meson_norm_ratio_neutral = meson_gmo_lhs_minus_rhs_neutral / (
            (m_pi_0 ** 2) - m_eta_sq
        )

        m_n_iso = (m_p_mp + m_n_mp) / mpf(2)
        m_xi_iso = (m_xi0 + m_xim) / mpf(2)
        m_sigma_iso = (m_sigma_p + m_sigma0 + m_sigma_m) / mpf(3)
        baryon_gmo_num = mpf(2) * (m_n_iso + m_xi_iso) - mpf(3) * m_lambda - m_sigma_iso
        baryon_rel_dev_over_2NX = baryon_gmo_num / (mpf(2) * (m_n_iso + m_xi_iso))
        baryon_norm_ratio = baryon_gmo_num / (m_sigma_iso - m_lambda)

        # Predicted GMO numerators from c*(d_q(1,0)-d_q(0,0)) = M(1,0)-M(0,0)
        pred_meson_gmo_num_avg = ratio_qcasimir_1 * (m_pi_avg_sq - m_eta_sq)
        pred_baryon_gmo_num = ratio_qcasimir_1 * (m_sigma_iso - m_lambda)

        wb.add_assertion(
            "P3_quantum_casimir_matches_both_meson_positive_and_baryon_negative_GMO_signs",
            computed=mpf(1)
            if (
                pred_meson_gmo_num_avg > mpf(0)
                and meson_gmo_lhs_minus_rhs_avg > mpf(0)
                and pred_baryon_gmo_num < mpf(0)
                and baryon_gmo_num < mpf(0)
            )
            else mpf(0),
            expected=mpf(1),
            tolerance=mpf("1e-78"),
            source="HyperbolicMesonClaspAndDiquarkSplit.qCasimir_gmo_second_order_and_universal_ratio",
        )

        meson_share_explained = pred_meson_gmo_num_avg / meson_gmo_lhs_minus_rhs_avg
        baryon_share_explained = pred_baryon_gmo_num / baryon_gmo_num

        # Record structured data payload (all mpfs formatted as 50-digit strings)
        wb.add_data(
            "P1_split_bundle_and_ocneanu_parameters",
            {
                "z2_rank2": fmt50(z2),
                "z3_rank3": fmt50(z3),
                "z2_minus_z3": fmt50(z2 - z3),
                "qBracket3_q0": fmt50(q3),
                "dim_q_10": fmt50(dim_q_10),
                "dim_q_8": fmt50(dim_q_8),
                "dim_q_1": fmt50(dim_q_1),
                "qBracket3_cubed": fmt50(q3 ** 3),
                "ocneanu_w3_sym": fmt50(w3_sym),
                "ocneanu_w3_mix": fmt50(w3_mix),
                "ocneanu_w3_alt": fmt50(w3_alt),
                "ocneanu_w2_sym": fmt50(w2_sym),
                "ocneanu_w2_mix": fmt50(w2_mix),
                "weinberg_killing_ratio_exact": "3/8",
                "framed_strand_charges_exact": {
                    "u": "+2/3",
                    "d": "-1/3",
                    "d_bar": "+1/3",
                    "u_bar": "-2/3",
                },
            },
        )
        wb.add_data("P1_clasp_3x3_generation_table", clasp_table_rows)
        wb.add_data("P1_clasp_ordered_pair_asymmetries", asymmetry_rows)
        wb.add_data(
            "P2_diquark_projector_traces",
            {
                "tr_P_Sigma0_sigma1": fmt50(tr_sig_s1),
                "tr_P_Lambda_sigma1": fmt50(tr_lam_s1),
                "tr_P_Sigma0_JM2": fmt50(tr_sig_jm2),
                "tr_P_Lambda_JM2": fmt50(tr_lam_jm2),
                "tr_P_Sigma0_V": fmt50(tr_sig_v),
                "tr_P_Lambda_V": fmt50(tr_lam_v),
                "abs_ratio_V_q0_pow_6": fmt50(q0 ** 6),
                "tr_P_Sigma0_V3": fmt50(tr_sig_v3),
                "tr_P_Lambda_V3": fmt50(tr_lam_v3),
                "diquark_V3_split_Lambda_minus_Sigma0": fmt50(tr_lam_v3 - tr_sig_v3),
                "borromean_V3_coleman_glashow_QED_combination": fmt50(cg_borromean_em),
                "zero_param_candidates_vs_PDG": diquark_comparison_rows,
            },
        )
        wb.add_data(
            "P3_quantum_casimir_gmo_evaluation",
            {
                "universal_ratio_neg_q_minus_1_over_q_plus_1_sq": fmt50(ratio_qcasimir_1),
                "meson_pdg_4mK2_minus_3meta2_minus_mpi2_iso_avg_MeV2": fmt50(
                    meson_gmo_lhs_minus_rhs_avg
                ),
                "meson_pdg_rel_deviation_over_4mK2_iso_avg": fmt50(
                    meson_rel_dev_over_4mK2_avg
                ),
                "meson_pdg_rel_deviation_over_4mK02_neutral": fmt50(
                    meson_rel_dev_over_4mK02
                ),
                "meson_pdg_normalized_ratio_iso_avg": fmt50(meson_norm_ratio_avg),
                "meson_pdg_normalized_ratio_neutral": fmt50(meson_norm_ratio_neutral),
                "meson_qcasimir_predicted_num_MeV2": fmt50(pred_meson_gmo_num_avg),
                "meson_fraction_of_deviation_explained": fmt50(meson_share_explained),
                "baryon_pdg_2N_2Xi_minus_3Lambda_minus_Sigma_MeV": fmt50(baryon_gmo_num),
                "baryon_pdg_rel_deviation_over_2N_2Xi": fmt50(baryon_rel_dev_over_2NX),
                "baryon_pdg_normalized_ratio": fmt50(baryon_norm_ratio),
                "baryon_qcasimir_predicted_num_MeV": fmt50(pred_baryon_gmo_num),
                "baryon_fraction_of_deviation_explained": fmt50(baryon_share_explained),
            },
        )
        wb.add_data(
            "comparison_only_empirical",
            {
                "CODATA_2022_m_e_MeV": m_e_str,
                "CODATA_2022_m_p_MeV": m_p_str,
                "CODATA_2022_m_n_MeV": m_n_str,
                "PDG_2024_m_pi_pm_MeV": m_pi_pm_str,
                "PDG_2024_m_pi_0_MeV": m_pi_0_str,
                "PDG_2024_m_K_pm_MeV": m_k_pm_str,
                "PDG_2024_m_K_0_MeV": m_k_0_str,
                "PDG_2024_m_eta_MeV": m_eta_str,
                "PDG_2024_m_Lambda_MeV": m_lambda_str,
                "PDG_2024_m_Sigma0_MeV": m_sigma0_str,
                "PDG_2024_m_Sigma_plus_MeV": m_sigma_p_str,
                "PDG_2024_m_Sigma_minus_MeV": m_sigma_m_str,
                "PDG_2024_m_Xi0_MeV": m_xi0_str,
                "PDG_2024_m_Xi_minus_MeV": m_xim_str,
                "PDG_2024_Delta_m_Sigma0_minus_Lambda_MeV": "76.959",
            },
        )

        print("=== P1: Split-Bundle & 3-Strand Hyperbolic Meson Clasp ===")
        print(f"  z2(q0) = {mp.nstr(z2, 12)}, z3(q0) = {mp.nstr(z3, 12)}, z2-z3 = {mp.nstr(z2 - z3, 12)}")
        print(f"  [3]_q0^3 = {mp.nstr(q3 ** 3, 12)}, w3=( {mp.nstr(w3_sym, 8)}, 2*{mp.nstr(w3_mix, 8)}, {mp.nstr(w3_alt, 8)} )")
        for r in asymmetry_rows:
            print(f"  {r['pair']:24s}: d_M2={r['diff_markov_z2'][:18]} | d_M3={r['diff_markov_z3'][:18]}")
        print("=== P2: H_3(q_0) S^{(2,1)} Diquark Projector Split ===")
        print(f"  tr(P_Lam V^3) - tr(P_Sig0 V^3) = {mp.nstr(tr_lam_v3 - tr_sig_v3, 12)}")
        for r in diquark_comparison_rows:
            print(
                f"  {r['candidate']:45s}: ratio={r['zero_param_ratio'][:12]} "
                f"| split_MeV={r['implied_splitting_MeV_from_m_Lambda'][:12]} "
                f"| rel_err_split={r['rel_diff_on_76p959_MeV_splitting'][:12]}"
            )
        print("=== P3: O((q_0 - q_0^{-1})^2) Quantum Casimir GMO ===")
        print(f"  universal ratio -((q0-1)/(q0+1))^2 = {mp.nstr(ratio_qcasimir_1, 12)}")
        print(
            f"  Meson GMO: obs_rel_4mK2={mp.nstr(meson_rel_dev_over_4mK2_avg, 8)}, "
            f"obs_norm={mp.nstr(meson_norm_ratio_avg, 8)}, share_explained={mp.nstr(meson_share_explained, 8)}"
        )
        print(
            f"  Baryon GMO: obs_rel_2NX={mp.nstr(baryon_rel_dev_over_2NX, 8)}, "
            f"obs_norm={mp.nstr(baryon_norm_ratio, 8)}, share_explained={mp.nstr(baryon_share_explained, 8)}"
        )

        wb.save({"q0Anchor": "proton"})
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
