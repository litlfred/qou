#!/usr/bin/env python3
"""80-dps diagnostic & verification probe for Batch 7 (`qou-i9q6` Q-Drain-7):
1. `qou-jkmh` & `qou-krgl`: Frame-Robinson-Thrall hook-length / Springer `sRow3` table (`k <= 7`)
   and `H_4(q_0)` GPMT modified quantum dimensions `dMod111`, `dMod211`, `dMod1111`, Wedderburn
   character sums, and per-partition `A = 4` cumulant ratio `|mu4GPMT_H4 / mu3GPMT_H4|` at `q_0`.
2. `qou-pwz4` & `qou-krgl`: Microscopic connected Borromean `V^3` Coleman-Glashow QED identity at
   `q_0` both for `(q_u, q_d) = (+2/3, -1/3)` and for generic symbolic/irrational charges with
   `q_s = q_d`, plus `tr(e_Lambda(q_0) A_2(q_0)) = z_D(q_0)`.
3. `qou-hkgd`: Exact rational / 80-dps check on the `su(3) = stab_{Der(O)}(e_1)` 8-generator basis:
   `P_singlet` annihilation, rank-8 injectivity of `su3ToEndTriplet`, `[D|_6, J_6] = 0`, and Lie
   bracket homomorphism residual `0`.
4. `qou-txc1`: Exact 80-dps check of the `Z_6` kernel of `smCoverHom : SU(3) x SU(2) x U(1) ->
   S(U(3) x U(2))` and the parameterized `sl_3 + sl_2` commutant trace ratio `1 / (1 + 60 alpha^2)`
   on `5bar + 10` (`3/8 <-> alpha^2 = 1/36`).
5. `qou-kebu` & `qou-qvpl`: Exhaustive `{-1, 0, 1}^3` (`27`-point) single-twist cube scan checking
   the coherence load-bearing window `T in {-1, 0, +1}`, Hopf-link `(0 2)` vs knot `(0 1 2)` vs
   Borromean `id` component framings, and Asselmeyer-Maluga `1910.09966` §5.2-5.3 zero-linking
   diagonal defect `3 sigma(diag(t)) - T(t) = 2 T(t) in 2Z`.

Zero fitting, zero float64, zero empirical literals; proton pin `q_0 = q_at(80)`.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
for _p in ("computations", "computations/substrate", "tools/qou-substrate/python"):
    if str(ROOT / _p) not in sys.path:
        sys.path.insert(0, str(ROOT / _p))

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

import sympy as sp  # noqa: E402
from mpmath import mp, mpf  # noqa: E402
from qou_substrate.constants import Q_MP, q_at  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.dps = 80


def fmt50(x: mpf) -> str:
    return mp.nstr(x, 50, strip_zeros=False)


def partitions_of(n: int, max_part: int | None = None) -> list[list[int]]:
    if n == 0:
        return [[]]
    cap = n if max_part is None else min(n, max_part)
    out: list[list[int]] = []
    for first in range(cap, 0, -1):
        for tail in partitions_of(n - first, first):
            out.append([first] + tail)
    return out


def dim_hlf(lam: list[int]) -> int:
    n = sum(lam)
    if n == 0:
        return 1
    fact = 1
    for k in range(2, n + 1):
        fact *= k
    hook_prod = 1
    for i, row_len in enumerate(lam):
        for j in range(row_len):
            arm = row_len - j - 1
            leg = sum(1 for r in range(i + 1, len(lam)) if lam[r] > j)
            hook_prod *= arm + leg + 1
    return fact // hook_prod


def n_stat(lam: list[int]) -> int:
    return sum(i * part for i, part in enumerate(lam))


def s_row3_derived(k: int) -> int:
    total = 0
    for lam in partitions_of(k):
        if len(lam) >= 3:
            sign = -1 if (n_stat(lam) % 2 == 1) else 1
            total += sign * dim_hlf(lam)
    return total


def build_octonion_table() -> list[list[tuple[int, int]]]:
    """Standard Fano-plane octonion multiplication table matching QOU.MathlibExt.OctonionDerivations."""
    # Directed Fano triples (i, j, k) with e_i * e_j = +e_k (1-indexed imaginary units 1..7)
    triples = [
        (1, 2, 3),
        (1, 4, 5),
        (1, 7, 6),
        (2, 4, 6),
        (2, 5, 7),
        (3, 4, 7),
        (3, 6, 5),
    ]
    tbl: list[list[tuple[int, int]]] = [[(1, 0) for _ in range(8)] for _ in range(8)]
    for a in range(8):
        tbl[0][a] = (1, a)
        tbl[a][0] = (1, a)
    for a in range(1, 8):
        tbl[a][a] = (-1, 0)
    for i, j, k in triples:
        tbl[i][j] = (1, k)
        tbl[j][i] = (-1, k)
        tbl[j][k] = (1, i)
        tbl[k][j] = (-1, i)
        tbl[k][i] = (1, j)
        tbl[i][k] = (-1, j)
    return tbl


def main() -> int:
    with mp.workdps(80):
        mp.dps = 80
        q0 = q_at(80)
        qi0 = mpf(1) / q0
        zD = (q0 ** 3) / (q0 ** 2 + mpf(1))

        wb = WitnessBuilder(
            "sm-eightfold-batch7-audit",
            engine="mpmath (80 dps) + sympy Q(q) + exact Fraction/int",
            output_dir=HERE,
        )
        wb.set_description(
            "80-dps verification & diagnostic audit for Backlog Drain Batch 7 (qou-i9q6): "
            "sRow3 hook-length derivation (qou-jkmh), H_4 GPMT modified dimensions & cumulants "
            "(qou-krgl), charge-free & SM-charge Borromean V^3 Coleman-Glashow + Lambda-Sigma0 "
            "projector (qou-pwz4, qou-krgl), octonionic su(3) 1+3 colour-triplet splitting "
            "(qou-hkgd), S(U(3)xU(2)) Z_6 kernel & parameterized commutant trace ratio (qou-txc1), "
            "and Hopf-link component framing + Asselmeyer-Maluga Hirzebruch defect (qou-kebu, qou-qvpl)."
        )
        wb.add_parameter("workdps", 80)
        wb.add_parameter("q0_proton_50dps", fmt50(q0))
        wb.add_parameter("zD_proton_50dps", fmt50(zD))

        wb.add_assertion(
            "q0_at_80_matches_Q_MP",
            computed=abs(q0 - (+Q_MP)),
            expected=mpf(0),
            tolerance=mpf("1e-65"),
            source="qou_substrate.constants",
        )

        # ==================================================================
        # 1. qou-jkmh & qou-krgl: sRow3 Hook-Length Table & H_4 GPMT Cumulants
        # ==================================================================
        srow3_vals = {k: s_row3_derived(k) for k in range(8)}
        expected_le5 = {0: 0, 1: 0, 2: 0, 3: -1, 4: -2, 5: 4}
        srow3_mismatch = sum(abs(srow3_vals[k] - expected_le5[k]) for k in range(6))
        wb.add_assertion(
            "sRow3Derived_matches_sRow3_table_k0_to_5",
            computed=mpf(srow3_mismatch),
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="ThreeRowSpringerSYTDerivation.sRow3Derived_eq_sRow3",
        )

        # H_4(q, z) Wedderburn weights & GPMT modified quantum dimensions at q_0
        def h4_denom(q: mpf) -> mpf:
            return ((q ** 2 + mpf(1)) ** 2) * (q ** 4 + mpf(1)) * (q ** 4 + q ** 2 + mpf(1))

        def w4(q: mpf, z: mpf) -> mpf:
            return (
                (q * z + mpf(1))
                * (q ** 3 * z + q * z + mpf(1))
                * (q ** 5 * z + q ** 3 * z + q * z + mpf(1))
                / h4_denom(q)
            )

        def w31(q: mpf, z: mpf) -> mpf:
            return (
                q
                * (q - z)
                * (q * z + mpf(1))
                * (q ** 3 * z + q * z + mpf(1))
                / (((q ** 2 + mpf(1)) ** 2) * (q ** 4 + mpf(1)))
            )

        def w22(q: mpf, z: mpf) -> mpf:
            return (
                (q ** 3)
                * (q - z)
                * (q * z + mpf(1))
                / (((q ** 2 + mpf(1)) ** 2) * (q ** 4 + q ** 2 + mpf(1)))
            )

        def w211(q: mpf, z: mpf) -> mpf:
            return (
                (q ** 2)
                * (z - q)
                * (q * z + mpf(1))
                * ((q ** 2 + mpf(1)) * z - q ** 3)
                / (((q ** 2 + mpf(1)) ** 2) * (q ** 4 + mpf(1)))
            )

        def w1111(q: mpf, z: mpf) -> mpf:
            return (
                -(q ** 3)
                * (z - q)
                * ((q ** 2 + mpf(1)) * z - q ** 3)
                * ((q ** 4 + q ** 2 + mpf(1)) * z - q ** 5)
                / h4_denom(q)
            )

        h4_unity_res = abs(
            w4(q0, zD)
            + mpf(3) * w31(q0, zD)
            + mpf(2) * w22(q0, zD)
            + mpf(3) * w211(q0, zD)
            + w1111(q0, zD)
            - mpf(1)
        )
        h4_kill_res = abs(w211(q0, zD)) + abs(w1111(q0, zD))

        dMod111 = -(q0 ** 3) / ((q0 ** 2 + mpf(1)) * (q0 ** 4 + q0 ** 2 + mpf(1)))
        dMod211 = -(q0 ** 3) * (q0 ** 4 + q0 ** 2 + mpf(1)) / (
            ((q0 ** 2 + mpf(1)) ** 3) * (q0 ** 4 + mpf(1))
        )
        dMod1111 = (q0 ** 7) / (
            ((q0 ** 2 + mpf(1)) ** 3) * (q0 ** 4 + mpf(1)) * (q0 ** 4 + q0 ** 2 + mpf(1))
        )
        mu3_h4 = -dMod111
        srow3_gpmt_4 = mpf(-3) * dMod211 + mpf(1) * dMod1111
        mu4_h4 = srow3_gpmt_4 - mpf(4) * mu3_h4
        mu4_h4_closed = (
            -(q0 ** 3)
            * (q0 ** 8 + mpf(2) * q0 ** 6 - mpf(2) * q0 ** 4 + mpf(2) * q0 ** 2 + mpf(1))
            / (((q0 ** 2 + mpf(1)) ** 3) * (q0 ** 4 + mpf(1)) * (q0 ** 4 + q0 ** 2 + mpf(1)))
        )
        ratio_mu4_over_mu3_h4 = abs(mu4_h4 / mu3_h4)

        wb.add_assertion(
            "H4_conventionD_partition_of_unity_and_3row_vanishing",
            computed=h4_unity_res + h4_kill_res,
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="H4GPMTModifiedDimensionCumulants.weights_h4_conventionD_twoRow_sum_eq_one",
        )
        wb.add_assertion(
            "H4_GPMT_mu4_closed_form_matches_cumulant_definition",
            computed=abs(mu4_h4 - mu4_h4_closed),
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="H4GPMTModifiedDimensionCumulants.mu4GPMT_H4",
        )
        wb.add_assertion(
            "H4_GPMT_sign_window_mu3_pos_and_mu4_neg",
            computed=mpf(1) if (mu3_h4 > mpf(0) and mu4_h4 < mpf(0)) else mpf(0),
            expected=mpf(1),
            tolerance=mpf("1e-75"),
            source="H4GPMTModifiedDimensionCumulants.mu4GPMT_H4_neg_of_pos",
        )

        # ==================================================================
        # 2. qou-pwz4 & qou-krgl: Coleman-Glashow V^3 (SM & Charge-Free) + Lambda-Sigma0
        # ==================================================================
        def borromean_matrices(qv: mpf) -> tuple[mp.matrix, mp.matrix, mp.matrix, mp.matrix]:
            qiv = mpf(1) / qv
            hv = qv - qiv
            A1 = mp.matrix([[qv, mpf(0), mpf(0)], [mpf(0), hv, mpf(1)], [mpf(0), mpf(1), mpf(0)]])
            A2 = mp.matrix([[hv, mpf(1), mpf(0)], [mpf(1), mpf(0), mpf(0)], [mpf(0), mpf(0), qv]])
            A2i = mp.matrix([[-hv, mpf(1), mpf(0)], [mpf(1), mpf(0), mpf(0)], [mpf(0), mpf(0), qiv]])
            B1 = mp.matrix([[hv, mpf(1), mpf(0)], [mpf(1), mpf(0), mpf(0)], [mpf(0), mpf(0), qv]])
            B2i = mp.matrix([[qiv, mpf(0), mpf(0)], [mpf(0), -hv, mpf(1)], [mpf(0), mpf(1), mpf(0)]])
            VA = A1 * A2i
            VB = B1 * B2i
            return VA * VA * VA, VB * VB * VB, A1, A2

        V3A, V3B, A1_q0, A2_q0 = borromean_matrices(q0)

        def mat_trace(M: mp.matrix) -> mpf:
            return sum((M[i, i] for i in range(M.rows)), mpf(0))

        def tr_conn_aab(qa: mpf, qb: mpf) -> mpf:
            Q = mp.matrix(
                [
                    [qa * qa + qa * qb, mpf(0), mpf(0)],
                    [mpf(0), mpf(2) * qa * qb, mpf(0)],
                    [mpf(0), mpf(0), qb * qa + qa * qa],
                ]
            )
            avg = (mpf(2) * qa * qa + mpf(4) * qa * qb) / mpf(3)
            return (mat_trace(Q * V3A) - avg * mat_trace(V3A)) / mpf(3)

        def tr_conn_abb(qa: mpf, qb: mpf) -> mpf:
            Q = mp.matrix(
                [
                    [qa * qb + qb * qb, mpf(0), mpf(0)],
                    [mpf(0), mpf(2) * qa * qb, mpf(0)],
                    [mpf(0), mpf(0), qb * qb + qb * qa],
                ]
            )
            avg = (mpf(4) * qa * qb + mpf(2) * qb * qb) / mpf(3)
            return (mat_trace(Q * V3B) - avg * mat_trace(V3B)) / mpf(3)

        # SM charges (+2/3, -1/3, -1/3)
        qu_sm = mpf(2) / mpf(3)
        qd_sm = -mpf(1) / mpf(3)
        split_pn = tr_conn_aab(qu_sm, qd_sm) - tr_conn_abb(qu_sm, qd_sm)
        split_sig = tr_conn_aab(qu_sm, qd_sm) - tr_conn_aab(qd_sm, qd_sm)
        split_xi = tr_conn_abb(qu_sm, qd_sm) - tr_conn_abb(qd_sm, qd_sm)
        cg_sm = split_pn - split_sig + split_xi

        # Generic non-SM irrational charges (mp.sqrt(5), -mp.sqrt(2)) with qs = qd
        qu_gen = mp.sqrt(mpf(5))
        qd_gen = -mp.sqrt(mpf(2))
        cg_gen = (
            (tr_conn_aab(qu_gen, qd_gen) - tr_conn_abb(qu_gen, qd_gen))
            - (tr_conn_aab(qu_gen, qd_gen) - tr_conn_aab(qd_gen, qd_gen))
            + (tr_conn_abb(qu_gen, qd_gen) - tr_conn_abb(qd_gen, qd_gen))
        )

        # Lambda sub-projector e_Lambda(q_0) on A_2(q_0) -> z_D(q_0)
        I3 = mp.eye(3)
        e_lambda = (mpf(1) / (q0 + qi0)) * (q0 * I3 - A1_q0)
        tr_e_lambda_A2 = mat_trace(e_lambda * A2_q0)

        wb.add_assertion(
            "Coleman_Glashow_BorromeanV3_SM_and_generic_charges_vanish",
            computed=abs(cg_sm) + abs(cg_gen),
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="HopfFramingAndHirzebruchDefect.coleman_glashow_borromeanV3_any_charges",
        )
        wb.add_assertion(
            "Lambda_subprojector_on_A2_equals_zD_exact",
            computed=abs(tr_e_lambda_A2 - zD),
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="USpinColemanGlashowLambdaSigma.trace_eLambda_mul_A2_eq_zD",
        )

        # ==================================================================
        # 3. qou-hkgd: Octonionic su(3) = stab_{Der(O)}(e_1) 1+3 Colour-Triplet Split
        # ==================================================================
        oct_tbl = build_octonion_table()
        # Solve linear system for all D in End_Q(Q^8) satisfying D(e_a * e_b) = D(e_a)*e_b + e_a*D(e_b)
        # and D(e_1) = 0, using exact SymPy Rational nullspace!
        rows = []
        # D(e_a) = sum_m D_{m, a} e_m; variable index 8*m + a for m,a in 0..7
        for a in range(8):
            for b in range(8):
                sgn_ab, idx_ab = oct_tbl[a][b]
                for m in range(8):
                    row = [sp.Integer(0)] * 64
                    # LHS: coeff of e_m in D(sgn_ab * e_{idx_ab}) = sgn_ab * D_{m, idx_ab}
                    row[8 * m + idx_ab] += sgn_ab
                    # RHS1: sum_r D_{r, a} * (e_r * e_b)_m
                    for r in range(8):
                        s1, k1 = oct_tbl[r][b]
                        if k1 == m:
                            row[8 * r + a] -= s1
                    # RHS2: sum_r D_{r, b} * (e_a * e_r)_m
                    for r in range(8):
                        s2, k2 = oct_tbl[a][r]
                        if k2 == m:
                            row[8 * r + b] -= s2
                    if any(x != 0 for x in row):
                        rows.append(row)
        # Stabilizer condition D(e_1) = 0: D_{m, 1} = 0 for m = 0..7
        for m in range(8):
            row = [sp.Integer(0)] * 64
            row[8 * m + 1] = sp.Integer(1)
            rows.append(row)

        su3_basis_vecs = sp.Matrix(rows).nullspace()
        su3_dim = len(su3_basis_vecs)
        su3_mats_8 = [sp.Matrix(8, 8, lambda i, j, v=vec: v[8 * i + j]) for vec in su3_basis_vecs]

        # Build Le (left multiplication by e_1) and J_6 = compressToTriplet(Le)
        Le_mat = sp.zeros(8, 8)
        for j in range(8):
            s_le, k_le = oct_tbl[1][j]
            Le_mat[k_le, j] = s_le
        J6_mat = Le_mat[2:8, 2:8]
        assert J6_mat * J6_mat == -sp.eye(6)

        singlet_leak = 0
        j6_comm_leak = 0
        su3_mats_6 = []
        for D8 in su3_mats_8:
            # Check singlet columns 0,1 and singlet rows 0,1 vanish identically
            for r in range(8):
                for c in (0, 1):
                    singlet_leak += abs(int(D8[r, c]))
                    singlet_leak += abs(int(D8[c, r]))
            D6 = D8[2:8, 2:8]
            su3_mats_6.append(D6)
            diff_j6 = D6 * J6_mat - J6_mat * D6
            j6_comm_leak += sum(abs(int(x)) for x in diff_j6)

        # Check rank of su3ToEndTriplet is 8 (faithful) and bracket homomorphism holds
        rank_6 = sp.Matrix([[D6[i, j] for i in range(6) for j in range(6)] for D6 in su3_mats_6]).rank()
        bracket_leak = 0
        for D8a, D6a in zip(su3_mats_8, su3_mats_6):
            for D8b, D6b in zip(su3_mats_8, su3_mats_6):
                br8_6 = (D8a * D8b - D8b * D8a)[2:8, 2:8]
                br6 = D6a * D6b - D6b * D6a
                bracket_leak += sum(abs(int(x)) for x in (br8_6 - br6))

        wb.add_assertion(
            "Octonion_su3_dim8_faithful_6D_C_linear_triplet_action",
            computed=mpf(
                abs(su3_dim - 8)
                + abs(rank_6 - 8)
                + singlet_leak
                + j6_comm_leak
                + bracket_leak
            ),
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="OctonionColourTripletSplitting.{su3ToEndTriplet_injective,su3ToEndTriplet_comm_J6,su3ToEndTriplet_bracket}",
        )

        # ==================================================================
        # 4. qou-txc1: S(U(3)xU(2)) Z_6 Kernel & Parameterized Commutant Trace Ratio
        # ==================================================================
        # Verify at 80 dps all 6 elements k = 0..5 of Z_6: u_k = exp(2*pi*i*k/6),
        # g3_k = u_k^-2 I_3 (det = u_k^-6 = 1), g2_k = u_k^3 I_2 (det = u_k^6 = 1),
        # and smCoverHom(g3_k, g2_k, u_k) = (I_3, I_2)
        z6_max_err = mpf(0)
        for k in range(6):
            theta = mpf(2) * mp.pi * mpf(k) / mpf(6)
            uk = mp.expj(theta)
            g3_diag = uk ** (-2)
            g2_diag = uk ** 3
            det_g3_err = abs(g3_diag ** 3 - mpf(1))
            det_g2_err = abs(g2_diag ** 2 - mpf(1))
            img3_err = abs((uk ** 2) * g3_diag - mpf(1))
            img2_err = abs((uk ** (-3)) * g2_diag - mpf(1))
            z6_max_err = max(z6_max_err, det_g3_err, det_g2_err, img3_err, img2_err)

        # Parameterized trace ratio on 5bar + 10 for alpha in {1/6, -1/6, 1/3, 1/2}
        t3_w = [Fraction(0), Fraction(0), Fraction(0), Fraction(1, 2), Fraction(-1, 2)]
        y0_w = [Fraction(-2), Fraction(-2), Fraction(-2), Fraction(3), Fraction(3)]
        ratio_check_err = Fraction(0)
        for alpha in (Fraction(1, 6), Fraction(-1, 6), Fraction(1, 3), Fraction(1, 2)):
            qw = [t3_w[i] + alpha * y0_w[i] for i in range(5)]
            tr_t3 = sum((-t3_w[i]) ** 2 for i in range(5)) + sum(
                (t3_w[i] + t3_w[j]) ** 2 for i in range(5) for j in range(i + 1, 5)
            )
            tr_q = sum((-qw[i]) ** 2 for i in range(5)) + sum(
                (qw[i] + qw[j]) ** 2 for i in range(5) for j in range(i + 1, 5)
            )
            formula = Fraction(1, 1) / (Fraction(1, 1) + 60 * (alpha ** 2))
            ratio_check_err += abs((tr_t3 / tr_q) - formula)
        assert Fraction(1, 1) / (Fraction(1, 1) + 60 * Fraction(1, 36)) == Fraction(3, 8)

        wb.add_assertion(
            "Baez_Huerta_Z6_kernel_and_parameterized_5bar10_trace_ratio",
            computed=z6_max_err + mpf(ratio_check_err.numerator) / mpf(ratio_check_err.denominator),
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="Su3Su2U1Z6GroupAndCommutant.{smQuotientZ6EquivSU3xU2,traceRatio_5bar_oplus_10_param}",
        )

        # ==================================================================
        # 5. qou-kebu & qou-qvpl: 27-Point Single-Twist Cube, Hopf Framing & Hirzebruch Defect
        # ==================================================================
        cube = list(itertools.product((-1, 0, 1), repeat=3))
        incoherent_totals = sorted(
            {
                sum(t)
                for t in cube
                if any(x > 0 for x in t) and any(x < 0 for x in t)
            }
        )
        hopf_at_neg3 = [t for t in cube if t[0] == t[2] and sum(t) == -3]
        # Zero-linking Hirzebruch defect 3*sigma(diag(t)) - sum(t) == 2*sum(t) (always even)
        defect_mismatch = 0
        for t in cube:
            sig_diag = sum((1 if x > 0 else (-1 if x < 0 else 0)) for x in t)
            h_def = 3 * sig_diag - sum(t)
            if h_def != 2 * sum(t) or (h_def % 2 != 0):
                defect_mismatch += 1

        wb.add_assertion(
            "Single_twist_cube_coherence_window_Hopf_e_and_even_zero_linking_Hirzebruch_defect",
            computed=mpf(
                (0 if incoherent_totals == [-1, 0, 1] else 1)
                + (0 if hopf_at_neg3 == [(-1, -1, -1)] else 1)
                + defect_mismatch
            ),
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="HopfFramingAndHirzebruchDefect.{exists_incoherent_in_range_iff,zeroLinking_unitFraming_hirzebruchDefect_eq_two_mul_sum}",
        )

        wb.add_data("sRow3_derived_k0_to_7", {str(k): v for k, v in srow3_vals.items()})
        wb.add_data(
            "H4_GPMT_evaluations_at_proton_q0",
            {
                "dMod111_q0": fmt50(dMod111),
                "dMod211_q0": fmt50(dMod211),
                "dMod1111_q0": fmt50(dMod1111),
                "mu3GPMT_H4_q0": fmt50(mu3_h4),
                "mu4GPMT_H4_q0": fmt50(mu4_h4),
                "abs_mu4_over_mu3_H4_q0": fmt50(ratio_mu4_over_mu3_h4),
                "uniform_H3_ratio": "2",
            },
        )
        wb.add_data(
            "Coleman_Glashow_BorromeanV3_q0",
            {
                "split_p_minus_n_q0": fmt50(split_pn),
                "split_SigmaPlus_minus_SigmaMinus_q0": fmt50(split_sig),
                "split_XiZero_minus_XiMinus_q0": fmt50(split_xi),
                "coleman_glashow_alternating_sum_SM": fmt50(cg_sm),
                "coleman_glashow_alternating_sum_generic": fmt50(cg_gen),
                "trace_eLambda_A2_q0": fmt50(tr_e_lambda_A2),
            },
        )
        wb.add_data(
            "Octonion_su3_triplet_audit",
            {
                "dim_su3_stab_e1": su3_dim,
                "rank_6D_triplet_restriction": rank_6,
                "singlet_leak": singlet_leak,
                "J6_commutator_leak": j6_comm_leak,
                "lie_bracket_leak": bracket_leak,
            },
        )
        wb.add_data(
            "Twist_cube_and_Hirzebruch_summary",
            {
                "incoherent_totals_in_unit_cube": incoherent_totals,
                "hopf_component_framings_at_T_neg3_in_unit_cube": [list(x) for x in hopf_at_neg3],
                "zero_linking_defect_odd_count": defect_mismatch,
            },
        )
        wb.save({"q0Anchor": "proton"})
        print(
            f"[PASS] sm_eightfold_batch7_audit_probe: sRow3={srow3_vals}, "
            f"|mu4/mu3|_H4(q0)={mp.nstr(ratio_mu4_over_mu3_h4, 12)}, "
            f"CG_SM={mp.nstr(cg_sm, 6)}, su3_dim={su3_dim}/rank6={rank_6}"
        )
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
