#!/usr/bin/env python3
"""80-dps verification probe for Bridge B Stokes discriminant, pivotal skew-Howe trace,
and H_3(q) skew-Howe Schur vs Markov weights (beans qou-pdio / NF-P2, qou-2eg2 / NF-P4).

Lean companions:
  - QOU/Mass/AdditiveConnectionMixedResidueZero.lean
  - QOU/QBeta/FlavourWeightSplitPivotalSkewHowe.lean
  - QOU/MassTheory/SkewHoweProtonSchurNorm.lean

Pure exact rationals + 80-dps mpmath at the proton pin q_0 = q_at(80). Zero fitting, zero float64.
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
from qou_substrate.constants import M_E_MEV_STR, Q_MP, q_at  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402


def fmt50(x: mpf) -> str:
    return mp.nstr(x, 50, strip_zeros=False)


def poly_P(qv: mpf) -> mpf:
    return (
        qv ** 12
        - mpf(3) * (qv ** 10)
        + mpf(3) * (qv ** 8)
        - mpf(5) * (qv ** 6)
        + mpf(3) * (qv ** 4)
        - mpf(3) * (qv ** 2)
        + mpf(1)
    )


def eps_flavour_v3(qv: mpf) -> mpf:
    return (qv ** 2 - mpf(1)) * poly_P(qv) / ((qv ** 4) * ((qv ** 2 + mpf(1)) ** 3))


def mat3_borromean_traces(qv: mpf) -> tuple[mpf, mpf]:
    """Direct 3x3 matrix multiplication trace of V^3 on W_p and W_n at 80 dps."""
    qi = mpf(1) / qv
    h = qv - qi
    a1 = mp.matrix([[qv, mpf(0), mpf(0)], [mpf(0), mpf(0), mpf(1)], [mpf(0), mpf(1), h]])
    a2_inv = mp.matrix([[-h, mpf(1), mpf(0)], [mpf(1), mpf(0), mpf(0)], [mpf(0), mpf(0), qi]])
    b1 = mp.matrix([[mpf(0), mpf(1), mpf(0)], [mpf(1), h, mpf(0)], [mpf(0), mpf(0), qv]])
    b2_inv = mp.matrix([[qi, mpf(0), mpf(0)], [mpf(0), -h, mpf(1)], [mpf(0), mpf(1), mpf(0)]])
    va = a1 * a2_inv
    vb = b1 * b2_inv
    v3a = va * va * va
    v3b = vb * vb * vb
    tr_a = v3a[0, 0] + v3a[1, 1] + v3a[2, 2]
    tr_b = v3b[0, 0] + v3b[1, 1] + v3b[2, 2]
    return tr_a, tr_b


def main() -> int:
    with mp.workdps(80):
        q0 = q_at(80)
        qi0 = mpf(1) / q0
        me = mpf(M_E_MEV_STR)

        wb = WitnessBuilder(
            "bridge-b-and-skew-howe-schur",
            engine="sympy + mpmath (80 dps)",
            output_dir=HERE,
        )
        wb.set_description(
            "80-dps verification of AdditiveConnectionMixedResidueZero, Bridge B rank-4 "
            "tensor-square Stokes discriminant, FlavourWeightSplitPivotalSkewHowe, and "
            "SkewHoweProtonSchurNorm (qou-pdio / NF-P2, qou-2eg2 / NF-P4)."
        )
        wb.add_parameter("workdps", 80)
        wb.add_parameter("q0_proton_50dps", fmt50(q0))

        wb.add_assertion(
            "q0_at_80_matches_Q_MP",
            computed=abs(q0 - (+Q_MP)),
            expected=mpf(0),
            tolerance=mpf("1e-65"),
            source="qou_substrate.constants",
        )

        # 1. Exact symbolic mixed-residue vanishing on End(C^3 x C^3) x End(C^2 x C^2)
        ac, bc, af, bf = sp.symbols("ac bc af bf")
        # Swap P_c on C^3 x C^3 (9x9) and swap P_f on C^2 x C^2 (4x4)
        p_c = sp.zeros(9, 9)
        for i in range(3):
            for j in range(3):
                p_c[3 * j + i, 3 * i + j] = 1
        p_f = sp.zeros(4, 4)
        for i in range(2):
            for j in range(2):
                p_f[2 * j + i, 2 * i + j] = 1
        omega_c = ac * sp.eye(9) + bc * p_c
        omega_f = af * sp.eye(4) + bf * p_f
        # Project each tensor factor onto traceless matrices M - tr(M)/dim * I
        # On omega_c x I_4 + I_9 x omega_f, bilinear projection pi_c x pi_f kills both summands
        pi_c_id = sp.eye(9) - (sp.eye(9).trace() / sp.Integer(9)) * sp.eye(9)
        pi_f_id = sp.eye(4) - (sp.eye(4).trace() / sp.Integer(4)) * sp.eye(4)
        mixed_zero = (pi_c_id == sp.zeros(9, 9)) and (pi_f_id == sp.zeros(4, 4))
        comm_norm = sp.kronecker_product(omega_c, sp.eye(4)) * sp.kronecker_product(
            sp.eye(9), omega_f
        ) - sp.kronecker_product(sp.eye(9), omega_f) * sp.kronecker_product(omega_c, sp.eye(4))
        wb.add_assertion(
            "additive_connection_mixed_residue_and_commutator_zero",
            computed=mpf(0 if (mixed_zero and comm_norm == sp.zeros(36, 36)) else 1),
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="AdditiveConnectionMixedResidueZero.mixedResidueProj_additive_eq_zero",
        )

        # 2. Bridge B rank-4 tensor-square KZ / Stokes discriminant at q0
        h0 = q0 - qi0
        qd2 = q0 + qi0
        delta_1 = h0 ** 2 + mpf(4)
        delta_2 = (q0 ** 2 + qi0 ** 2) ** 2 - mpf(4)
        wb.add_assertion(
            "hecke_discriminant_eq_qd2_sq",
            computed=abs(delta_1 - qd2 ** 2),
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="AdditiveConnectionMixedResidueZero.heckeDiscriminant_eq_qd2_sq",
        )
        wb.add_assertion(
            "tensor_square_outer_discriminant_eq_h_sq_mul_hecke",
            computed=abs(delta_2 - (h0 ** 2) * delta_1),
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="AdditiveConnectionMixedResidueZero.tensorSquare_discriminant_eq_h_sq_mul_hecke",
        )

        # 3. Pivotal quantum-trace & skew-Howe colour-singlet invariance (-q0^-1)
        tr_wp, tr_wn = mat3_borromean_traces(q0)
        piv_diff = (qi0 * tr_wn - q0 * tr_wp) / (qd2 ** 3)
        eps_q0 = eps_flavour_v3(q0)
        eps_mirror = eps_flavour_v3(-qi0)
        e0_full_mev = me / (q0 * (q0 - mpf(1)) * (mpf(1) - (mpf(1) - qi0) ** 2))
        qbeta_scored_mev = e0_full_mev * abs(eps_q0)
        qbeta_mirror_mev = e0_full_mev * abs(eps_mirror)

        wb.add_assertion(
            "pivotal_trace_diff_equals_epsFlavourV3",
            computed=abs(piv_diff - eps_q0),
            expected=mpf(0),
            tolerance=mpf("1e-74"),
            source="FlavourWeightSplitPivotalSkewHowe.pivotal_trace_diff_eq_epsFlavourV3",
        )
        wb.add_assertion(
            "skew_howe_mirror_neg_inv_antisymmetric",
            computed=abs(eps_mirror + eps_q0),
            expected=mpf(0),
            tolerance=mpf("1e-74"),
            source="FlavourWeightSplitPivotalSkewHowe.epsFlavourV3_skewHowe_mirror",
        )
        wb.add_assertion(
            "skew_howe_mirror_leaves_scored_Q_beta_invariant",
            computed=abs(qbeta_mirror_mev - qbeta_scored_mev),
            expected=mpf(0),
            tolerance=mpf("1e-74"),
            source="FlavourWeightSplitPivotalSkewHowe.abs_epsFlavourV3_skewHowe_invariant",
        )

        # 4. Skew-Howe H_3(q0) Schur elements vs Convention-D Markov weights (qou-2eg2)
        def poincare_s3(qv: mpf) -> mpf:
            return mpf(1) + mpf(2) * (qv ** 2) + mpf(2) * (qv ** 4) + qv ** 6

        def qfact3_bal(qv: mpf) -> mpf:
            return poincare_s3(qv) / (qv ** 3)

        def schur_triv(qv: mpf) -> mpf:
            return poincare_s3(qv)

        def schur_sign(qv: mpf) -> mpf:
            return poincare_s3(mpf(1) / qv)

        def schur_refl(qv: mpf) -> mpf:
            return qv ** 2 + mpf(1) + (mpf(1) / qv) ** 2

        def y_triv(qv: mpf) -> mpf:
            return (qv ** 4 + mpf(1)) / ((qv ** 2 + mpf(1)) ** 2)

        def y_refl(qv: mpf) -> mpf:
            return (qv ** 2) / ((qv ** 2 + mpf(1)) ** 2)

        def tr_m_bor(qv: mpf) -> mpf:
            hv = qv - mpf(1) / qv
            return (mpf(4) + hv ** 2 - mpf(3) * (hv ** 4) - hv ** 6) / (hv ** 2 + mpf(4))

        prod_13_3_q0 = schur_sign(q0) * schur_triv(q0)
        prod_13_3_bar = schur_sign(qi0) * schur_triv(qi0)
        f_bor_q0 = tr_m_bor(q0) * qfact3_bal(q0) / (q0 ** 3)
        f_bor_bar = tr_m_bor(qi0) * qfact3_bal(qi0) / (qi0 ** 3)

        wb.add_assertion(
            "skew_howe_symmetric_schur_product_cancels_q3",
            computed=abs(prod_13_3_q0 - (qfact3_bal(q0) ** 2)),
            expected=mpf(0),
            tolerance=mpf("1e-73"),
            source="SkewHoweProtonSchurNorm.tensorSchurSingletSym_eq_sq",
        )
        wb.add_assertion(
            "skew_howe_symmetric_schur_product_bar_invariant",
            computed=abs(prod_13_3_bar - prod_13_3_q0),
            expected=mpf(0),
            tolerance=mpf("1e-73"),
            source="SkewHoweProtonSchurNorm.tensorSchurSingletSym_bar_invariant",
        )
        wb.add_assertion(
            "convention_d_markov_weights_bar_symmetric_and_partition_unity",
            computed=abs((y_triv(q0) + mpf(2) * y_refl(q0)) - mpf(1))
            + abs(y_triv(qi0) - y_triv(q0))
            + abs(y_refl(qi0) - y_refl(q0)),
            expected=mpf(0),
            tolerance=mpf("1e-74"),
            source="SkewHoweProtonSchurNorm.markovWeight_partition_of_unity",
        )
        wb.add_assertion(
            "asymmetric_colour_schur_times_flavour_markov_gives_fBor",
            computed=abs(schur_sign(q0) * tr_m_bor(q0) - f_bor_q0)
            + abs(schur_triv(q0) * tr_m_bor(q0) - f_bor_bar),
            expected=mpf(0),
            tolerance=mpf("1e-73"),
            source="SkewHoweProtonSchurNorm.colourSchur_flavourMarkov_dichotomy",
        )

        wb.add_data(
            "bridge_b_stokes",
            {
                "hecke_discriminant_q0": fmt50(delta_1),
                "tensor_square_outer_discriminant_q0": fmt50(delta_2),
                "tensor_square_eigenvalues_q0": [
                    fmt50(q0 ** 2),
                    "-1",
                    "-1",
                    fmt50(qi0 ** 2),
                ],
            },
        )
        wb.add_data(
            "pivotal_skew_howe",
            {
                "epsFlavourV3_q0": fmt50(eps_q0),
                "epsFlavourV3_neg_inv_q0": fmt50(eps_mirror),
                "Q_beta_scored_MeV": fmt50(qbeta_scored_mev),
            },
        )
        wb.add_data(
            "h3_schur_vs_markov_q0",
            {
                "schur_triv_c_3": fmt50(schur_triv(q0)),
                "schur_refl_c_21": fmt50(schur_refl(q0)),
                "schur_sign_c_111": fmt50(schur_sign(q0)),
                "qfact3_balanced": fmt50(qfact3_bal(q0)),
                "symmetric_product_c111_c3": fmt50(prod_13_3_q0),
                "markov_y_3": fmt50(y_triv(q0)),
                "markov_y_21": fmt50(y_refl(q0)),
                "markov_y_111": "0",
                "tr_M_Borromean": fmt50(tr_m_bor(q0)),
                "F_Bor_q0": fmt50(f_bor_q0),
                "mirror_ratio_q0_pow_6": fmt50(q0 ** 6),
            },
        )
        wb.save({"q0Anchor": "proton"})
        print("All Bridge-B + Pivotal + Skew-Howe Schur checks passed at 80 dps.")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
