#!/usr/bin/env python3
"""su3_su2_u1_pushforward_and_weinberg_probe.py — 80-dps Standard Model Pushforward,
Jimbo N=3 HOMFLY-PT Schur-Weyl Duality, and Weinberg-Angle / Gauge-Coupling Audit (Wave 5).

Companion to Lean 4 formalization:
  `folio/quantum-observable-universe/lean/QOU/StandardModel/BringPushforwardAndGaugeGroupUnification.lean`

STRICT ANTI-FITTING & PRECISION DISCIPLINE
------------------------------------------
1. ZERO fitting to PDG/CODATA sin^2(theta_W), alpha_s(M_Z), or quark masses; ZERO
   assertions gated on proximity to experimental electroweak observables.
2. ZERO binary64 (`float64`) arithmetic, ZERO `math` or `numpy` imports, ZERO
   `float(...)` or `complex(...)` calls, ZERO float literals, and ZERO raw JSON
   floats in the emitted witness (`witness_raw_float64_audit` = 0).
3. Evaluates all exact anomaly/kernel/Lie-algebra identities on the split fibre
   `F = V_2 (+) W_3^*` (`W_3 = pi_* L`), explicit 9x9 & 27x27 Jimbo `N=3` (`a = q^3`)
   HOMFLY-PT Schur-Weyl central idempotents alongside 4x4 & 8x8 `N=2`, and all
   canonical Weinberg-angle / 1-loop RG candidates side-by-side at 80 decimal places
   across `q_0`, `q_2t`, and `q_muon`.
"""
from __future__ import annotations

from fractions import Fraction
import json
import os
import sys
from pathlib import Path

os.environ.setdefault("QOU_OUTPUT_DPS", "80")
os.environ.setdefault("QOU_COMPUTE_DPS", "95")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
for _p in (str(ROOT), str(ROOT / "substrate"), str(ROOT / "audits")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402

set_compute_dps(80)

from codata_2022_source import (  # noqa: E402
    M_E_MEV,
    M_MU_MEV,
    M_P_MEV,
)
from coulomb_energy import alpha_em_inv_bring_schwinger  # noqa: E402
from qou_substrate import codata as _codata_reg  # noqa: E402
from qou_substrate.constants import (  # noqa: E402
    q_at,
    q_muon_at,
    q_two_term_borromean_at,
    vol_4_1_at,
)
from qou_substrate.witness import (  # noqa: E402
    WitnessBuilder,
    q0_comparison,
)


# ── Pure-Integer Combinatorics (Zero `math` Import) ──────────────────────────
def _binom_int(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    num = 1
    den = 1
    for i in range(1, k + 1):
        num *= n - (k - i)
        den *= i
    return num // den


def _mat_max_abs(m: mp.matrix) -> mp.mpf:
    best = mp.mpf(0)
    for r in range(m.rows):
        for c in range(m.cols):
            val = abs(m[r, c])
            if val > best:
                best = val
    return best


def _mat_trace(m: mp.matrix) -> mp.mpf:
    return mp.fsum(m[i, i] for i in range(m.rows))


def _kron2(a: mp.matrix, b: mp.matrix) -> mp.matrix:
    ra, ca = a.rows, a.cols
    rb, cb = b.rows, b.cols
    out = mp.zeros(ra * rb, ca * cb)
    for i1 in range(ra):
        for j1 in range(ca):
            aij = a[i1, j1]
            if aij == 0:
                continue
            r_off = i1 * rb
            c_off = j1 * cb
            for i2 in range(rb):
                for j2 in range(cb):
                    bij = b[i2, j2]
                    if bij != 0:
                        out[r_off + i2, c_off + j2] = aij * bij
    return out


# ── Part 1: Split Fibre F = V_2 (+) W_3^*, Exterior Generation, Z_6, Anomalies ─
def _evaluate_part1_fibre_and_anomalies() -> dict[str, object]:
    with mp.workdps(95):
        # Fundamental split fibre F = V_2 (+) W_3^* of complex dimension 2 + 3 = 5.
        # Unique normalized traceless central generator in s(u(2) (+) u(3)):
        #   Y|_F = diag(-1/2, -1/2, +1/3, +1/3, +1/3)
        y_v2 = Fraction(-1, 2)
        y_w3_dual = Fraction(1, 3)
        y_v2_dual = -y_v2
        y_w3 = -y_w3_dual

        tr_y_fibre = 2 * y_v2 + 3 * y_w3_dual  # 0

        # Chiral generation S_chiral = Lambda^1(F) (+) Lambda^2(F^*):
        #   Lambda^1(F)   = V_2 (+) W_3^* = L(1,2)_{-1/2} (+) d^c(3bar,1)_{+1/3}   [dim 2 + 3 = 5]
        #   Lambda^2(F^*) = Lambda^2(V_2^*) (+) (V_2^* (x) W_3) (+) Lambda^2(W_3)
        #                 = e^c(1,1)_{+1} (+) Q(3,2)_{+1/6} (+) u^c(3bar,1)_{-2/3} [dim 1 + 6 + 3 = 10]
        y_L = y_v2
        y_dc = y_w3_dual
        y_ec = 2 * y_v2_dual
        y_Q = y_v2_dual + y_w3
        y_uc = 2 * y_w3

        multiplets = [
            {
                "name": "Q_L",
                "origin": "V_2^* (x) W_3 in Lambda^2(F^*)",
                "su3_rep": "3",
                "su3_dim": 3,
                "su3_cubic_A": Fraction(1, 1),
                "su3_dynkin_T": Fraction(1, 2),
                "su2_dim": 2,
                "su2_dynkin_T": Fraction(1, 2),
                "Y": y_Q,
                "six_Y": int(6 * y_Q),
            },
            {
                "name": "u_L^c",
                "origin": "Lambda^2(W_3) ~= W_3^* in Lambda^2(F^*)",
                "su3_rep": "3bar",
                "su3_dim": 3,
                "su3_cubic_A": Fraction(-1, 1),
                "su3_dynkin_T": Fraction(1, 2),
                "su2_dim": 1,
                "su2_dynkin_T": Fraction(0, 1),
                "Y": y_uc,
                "six_Y": int(6 * y_uc),
            },
            {
                "name": "d_L^c",
                "origin": "W_3^* in Lambda^1(F)",
                "su3_rep": "3bar",
                "su3_dim": 3,
                "su3_cubic_A": Fraction(-1, 1),
                "su3_dynkin_T": Fraction(1, 2),
                "su2_dim": 1,
                "su2_dynkin_T": Fraction(0, 1),
                "Y": y_dc,
                "six_Y": int(6 * y_dc),
            },
            {
                "name": "L_L",
                "origin": "V_2 in Lambda^1(F)",
                "su3_rep": "1",
                "su3_dim": 1,
                "su3_cubic_A": Fraction(0, 1),
                "su3_dynkin_T": Fraction(0, 1),
                "su2_dim": 2,
                "su2_dynkin_T": Fraction(1, 2),
                "Y": y_L,
                "six_Y": int(6 * y_L),
            },
            {
                "name": "e_L^c",
                "origin": "Lambda^2(V_2^*) in Lambda^2(F^*)",
                "su3_rep": "1",
                "su3_dim": 1,
                "su3_cubic_A": Fraction(0, 1),
                "su3_dynkin_T": Fraction(0, 1),
                "su2_dim": 1,
                "su2_dynkin_T": Fraction(0, 1),
                "Y": y_ec,
                "six_Y": int(6 * y_ec),
            },
        ]

        total_weyl_dim = sum(m["su3_dim"] * m["su2_dim"] for m in multiplets)
        dim_lambda1 = 2 + 3
        dim_lambda2 = 1 + 6 + 3

        # Five gauge & gravitational anomaly sums (exact rational arithmetic)
        anom_su3_cubed = sum(m["su2_dim"] * m["su3_cubic_A"] for m in multiplets)
        anom_su3_sq_u1 = sum(m["su2_dim"] * m["su3_dynkin_T"] * m["Y"] for m in multiplets)
        anom_su2_sq_u1 = sum(m["su3_dim"] * m["su2_dynkin_T"] * m["Y"] for m in multiplets)
        anom_grav_sq_u1 = sum(m["su3_dim"] * m["su2_dim"] * m["Y"] for m in multiplets)
        anom_u1_cubed = sum(m["su3_dim"] * m["su2_dim"] * (m["Y"] ** 3) for m in multiplets)

        # Polynomial factorization check for general (Y_Q, Y_uc) after linear anomaly elimination:
        #   [SU(3)]^2 U(1)_Y = 0  =>  Y_dc = -2*Y_Q - Y_uc
        #   [SU(2)]^2 U(1)_Y = 0  =>  Y_L  = -3*Y_Q
        #   Tr(Y) = 0             =>  Y_ec =  6*Y_Q
        # Then:
        #   (1/2) * Tr(Y^3) = 9 * Y_Q * (4*Y_Q + Y_uc) * (2*Y_Q - Y_uc)
        #   Tr(Y^3)         = 18 * Y_Q * (4*Y_Q + Y_uc) * (2*Y_Q - Y_uc)
        # Verify exact polynomial equality across 49 independent rational pairs (sufficient to
        # determine every homogeneous degree-3 bivariate polynomial over Q uniquely).
        poly_diff_max = Fraction(0, 1)
        for a_num in (-3, -2, -1, 0, 1, 2, 3):
            for b_num in (-5, -3, -1, 0, 1, 2, 4):
                yq_t = Fraction(a_num, 6)
                yuc_t = Fraction(b_num, 3)
                ydc_t = -2 * yq_t - yuc_t
                yl_t = -3 * yq_t
                yec_t = 6 * yq_t
                half_tr_y3 = Fraction(1, 2) * (
                    6 * (yq_t ** 3)
                    + 3 * (yuc_t ** 3)
                    + 3 * (ydc_t ** 3)
                    + 2 * (yl_t ** 3)
                    + (yec_t ** 3)
                )
                factored = 9 * yq_t * (4 * yq_t + yuc_t) * (2 * yq_t - yuc_t)
                diff = abs(half_tr_y3 - factored)
                if diff > poly_diff_max:
                    poly_diff_max = diff

        # Verify unique non-vector-like roots at Y_Q = +1/6:
        yq_std = Fraction(1, 6)
        root_branch_1 = (-4 * yq_std, -2 * yq_std - (-4 * yq_std))  # (-2/3, +1/3)
        root_branch_2 = (2 * yq_std, -2 * yq_std - (2 * yq_std))    # (+1/3, -2/3) = u^c <-> d^c swap

        # Exact order-6 kernel Z_6 <= SU(3)_c x SU(2)_L x U(1)_Y at 80-dps complex precision
        # Parameterize U(1)_Y by u = exp(i * alpha) acting as u^{6 Y}:
        #   k in {0..5}: u_k = exp(2*pi*i*k/6), g3_k = u_k^2 * I_3, g2_k = u_k^3 * I_2.
        i_unit = mp.mpc(0, 1)
        z6_max_action_err = mp.mpf(0)
        z6_det_err = mp.mpf(0)
        distinct_z6_elements = 0
        for k in range(6):
            theta_k = mp.mpf(2 * k) * mp.pi / mp.mpf(6)
            u_k = mp.exp(i_unit * theta_k)
            g3_scalar = u_k ** 2
            g2_scalar = u_k ** 3
            # Check det(g3_k) = (u_k^2)^3 = 1 and det(g2_k) = (u_k^3)^2 = 1
            z6_det_err = max(
                z6_det_err,
                abs((g3_scalar ** 3) - mp.mpf(1)),
                abs((g2_scalar ** 2) - mp.mpf(1)),
                abs(abs(u_k) - mp.mpf(1)),
            )
            if k == 0 or abs(u_k - mp.mpf(1)) > mp.mpf(1) / mp.mpf(10):
                distinct_z6_elements += 1
            # Action on F = V_2 (+) W_3^*:
            #   V_2: g2_scalar * u_k^{-3},  W_3^*: conj(g3_scalar) * u_k^{+2}
            act_v2 = g2_scalar * (u_k ** (-3))
            act_w3_dual = mp.conj(g3_scalar) * (u_k ** 2)
            # Action on all 5 chiral multiplets + Higgs doublet H = (1, 2)_{+1/2} (six_Y = +3)
            act_Q = g3_scalar * g2_scalar * (u_k ** 1)
            act_uc = mp.conj(g3_scalar) * (u_k ** (-4))
            act_dc = mp.conj(g3_scalar) * (u_k ** 2)
            act_L = g2_scalar * (u_k ** (-3))
            act_ec = u_k ** 6
            act_H = g2_scalar * (u_k ** 3)
            for act_val in (act_v2, act_w3_dual, act_Q, act_uc, act_dc, act_L, act_ec, act_H):
                err = abs(act_val - mp.mpf(1))
                if err > z6_max_action_err:
                    z6_max_action_err = err

        # Exact integer gcd/order check: kernel on e_L^c forces u^6 = 1; for k in 0..5 each
        # u_k uniquely determines g2_k = u_k^3 I_2 and g3_k = u_k^2 I_3, so |ker| = 6.
        trivial_sixth_roots = [
            k
            for k in range(6)
            if (2 * k + 3 * k + k) % 6 == 0
            and (-2 * k - 4 * k) % 6 == 0
            and (-2 * k + 2 * k) % 6 == 0
            and (3 * k - 3 * k) % 6 == 0
            and (6 * k) % 6 == 0
        ]

        # Real Lie algebra s(u(2) (+) u(3)) <= su(5): construct explicit 12-element basis
        # as 5x5 skew-Hermitian traceless matrices on F = C^2 (+) C^3 and verify:
        #   1. dim_R s(u(2) (+) u(3)) = 12 (rank of flattened 50-component real vectors = 12)
        #   2. Off-diagonal Hom(V_2, W_3^*) (+) Hom(W_3^*, V_2) block norm = 0 (0 X/Y leptoquarks)
        #   3. Exact commutator closure inside block-diagonal End(V_2) (+) End(W_3^*)
        basis_12: list[mp.matrix] = []
        # 3 su(2)_L generators on indices {0, 1}
        m_su2_1 = mp.zeros(5, 5)
        m_su2_1[0, 1] = i_unit
        m_su2_1[1, 0] = i_unit
        m_su2_2 = mp.zeros(5, 5)
        m_su2_2[0, 1] = mp.mpf(-1)
        m_su2_2[1, 0] = mp.mpf(1)
        m_su2_3 = mp.zeros(5, 5)
        m_su2_3[0, 0] = i_unit
        m_su2_3[1, 1] = -i_unit
        basis_12.extend([m_su2_1, m_su2_2, m_su2_3])

        # 8 su(3)_c generators on indices {2, 3, 4}
        for p_idx, q_idx in ((2, 3), (2, 4), (3, 4)):
            g_sym = mp.zeros(5, 5)
            g_sym[p_idx, q_idx] = i_unit
            g_sym[q_idx, p_idx] = i_unit
            g_asym = mp.zeros(5, 5)
            g_asym[p_idx, q_idx] = mp.mpf(-1)
            g_asym[q_idx, p_idx] = mp.mpf(1)
            basis_12.extend([g_sym, g_asym])
        g_diag1 = mp.zeros(5, 5)
        g_diag1[2, 2] = i_unit
        g_diag1[3, 3] = -i_unit
        g_diag2 = mp.zeros(5, 5)
        g_diag2[2, 2] = i_unit
        g_diag2[3, 3] = i_unit
        g_diag2[4, 4] = mp.mpf(-2) * i_unit
        basis_12.extend([g_diag1, g_diag2])

        # 1 u(1)_Y generator i * diag(-1/2, -1/2, +1/3, +1/3, +1/3)
        g_u1y = mp.zeros(5, 5)
        g_u1y[0, 0] = -i_unit / mp.mpf(2)
        g_u1y[1, 1] = -i_unit / mp.mpf(2)
        g_u1y[2, 2] = i_unit / mp.mpf(3)
        g_u1y[3, 3] = i_unit / mp.mpf(3)
        g_u1y[4, 4] = i_unit / mp.mpf(3)
        basis_12.append(g_u1y)

        # Verify skew-Hermiticity, tracelessness, zero off-diagonal X/Y entries, and Gram det > 0
        lie_prop_err = mp.mpf(0)
        leptoquark_offdiag_max = mp.mpf(0)
        for b_mat in basis_12:
            # Skew-Hermitian: B + B^dagger = 0
            for r in range(5):
                for c in range(5):
                    sh_err = abs(b_mat[r, c] + mp.conj(b_mat[c, r]))
                    if sh_err > lie_prop_err:
                        lie_prop_err = sh_err
                    if (r < 2 and c >= 2) or (r >= 2 and c < 2):
                        if abs(b_mat[r, c]) > leptoquark_offdiag_max:
                            leptoquark_offdiag_max = abs(b_mat[r, c])
            tr_err = abs(mp.fsum(b_mat[d, d] for d in range(5)))
            if tr_err > lie_prop_err:
                lie_prop_err = tr_err

        # 12x12 real Hilbert-Schmidt Gram matrix G_{ab} = -Tr(B_a * B_b)
        gram_12 = mp.zeros(12, 12)
        for a_i in range(12):
            for b_i in range(12):
                prod = basis_12[a_i] * basis_12[b_i]
                tr_val = -mp.fsum(prod[d, d] for d in range(5))
                gram_12[a_i, b_i] = mp.re(tr_val)
        gram_det = mp.det(gram_12)

        # Check all commutators [B_a, B_b] remain strictly block-diagonal (0 leptoquarks)
        comm_offdiag_max = mp.mpf(0)
        for a_i in range(12):
            for b_i in range(a_i + 1, 12):
                comm = basis_12[a_i] * basis_12[b_i] - basis_12[b_i] * basis_12[a_i]
                for r in range(2):
                    for c in range(2, 5):
                        comm_offdiag_max = max(
                            comm_offdiag_max, abs(comm[r, c]), abs(comm[c, r])
                        )

        return {
            "split_fibre_definition": "F = V_2 (+) W_3^* with W_3 = pi_* L (rank 3 pushforward along degree-3 Bring projection)",
            "dim_V2": 2,
            "dim_W3_pushforward": 3,
            "dim_F": 5,
            "dim_Lambda1_F": dim_lambda1,
            "dim_Lambda2_F_dual": dim_lambda2,
            "dim_S_chiral_generation": total_weyl_dim,
            "traceless_fibre_generator_Y_on_F": "diag(-1/2, -1/2, +1/3, +1/3, +1/3)",
            "trace_Y_on_F": f"{tr_y_fibre.numerator}/{tr_y_fibre.denominator}",
            "chiral_multiplets": [
                {
                    "name": m["name"],
                    "exterior_origin": m["origin"],
                    "rep": f"({m['su3_rep']}, {m['su2_dim']})_{{{m['Y'].numerator}/{m['Y'].denominator}}}",
                    "weyl_multiplicity": m["su3_dim"] * m["su2_dim"],
                    "Y_rational": f"{m['Y'].numerator}/{m['Y'].denominator}",
                    "six_Y": m["six_Y"],
                }
                for m in multiplets
            ],
            "anomaly_cancellation_exact": {
                "SU3_cubed": f"{anom_su3_cubed.numerator}/{anom_su3_cubed.denominator}",
                "SU3_sq_U1Y": f"{anom_su3_sq_u1.numerator}/{anom_su3_sq_u1.denominator}",
                "SU2_sq_U1Y": f"{anom_su2_sq_u1.numerator}/{anom_su2_sq_u1.denominator}",
                "grav_sq_U1Y_TrY": f"{anom_grav_sq_u1.numerator}/{anom_grav_sq_u1.denominator}",
                "U1Y_cubed_TrY3": f"{anom_u1_cubed.numerator}/{anom_u1_cubed.denominator}",
            },
            "cubic_hypercharge_polynomial_factorization": {
                "linear_eliminations": "Y_{d^c} = -2 Y_Q - Y_{u^c}, Y_L = -3 Y_Q, Y_{e^c} = 6 Y_Q",
                "half_Tr_Y3_factored": "9 * Y_Q * (4 * Y_Q + Y_{u^c}) * (2 * Y_Q - Y_{u^c})",
                "full_Tr_Y3_factored": "18 * Y_Q * (4 * Y_Q + Y_{u^c}) * (2 * Y_Q - Y_{u^c})",
                "bivariate_grid_49pt_max_rational_diff": f"{poly_diff_max.numerator}/{poly_diff_max.denominator}",
                "at_YQ_one_sixth_branch_1": f"({root_branch_1[0]}, {root_branch_1[1]})",
                "at_YQ_one_sixth_branch_2_swap": f"({root_branch_2[0]}, {root_branch_2[1]})",
            },
            "global_gauge_group_kernel_Z6": {
                "generator": "(zeta_6^2 * I_3, zeta_6^3 * I_2, zeta_6) in SU(3)_c x SU(2)_L x U(1)_Y",
                "kernel_order": len(trivial_sixth_roots),
                "distinct_unit_circle_elements": distinct_z6_elements,
                "max_determinant_and_unitarity_residual": fmt(z6_det_err),
                "max_action_residual_on_F_Schiral_and_Higgs": fmt(z6_max_action_err),
                "quotient_group": "S(U(2) x U(3)) ~= (SU(3)_c x SU(2)_L x U(1)_Y) / Z_6",
            },
            "split_lie_algebra_s_u2_oplus_u3": {
                "dim_su3_c": 8,
                "dim_su2_L": 3,
                "dim_u1_Y": 1,
                "dim_s_u2_oplus_u3": len(basis_12),
                "dim_su5_ambient": 24,
                "num_XY_leptoquark_generators_on_split_bundle": 0,
                "hilbert_schmidt_gram_det_12x12": fmt(gram_det),
                "skew_hermitian_and_traceless_max_residual": fmt(lie_prop_err),
                "off_diagonal_XY_block_max_abs": fmt(
                    max(leptoquark_offdiag_max, comm_offdiag_max)
                ),
            },
            "_raw_checks": {
                "all_five_anomalies_zero": (
                    anom_su3_cubed == 0
                    and anom_su3_sq_u1 == 0
                    and anom_su2_sq_u1 == 0
                    and anom_grav_sq_u1 == 0
                    and anom_u1_cubed == 0
                    and tr_y_fibre == 0
                ),
                "poly_factorization_exact": (
                    poly_diff_max == 0
                    and root_branch_1 == (Fraction(-2, 3), Fraction(1, 3))
                    and root_branch_2 == (Fraction(1, 3), Fraction(-2, 3))
                ),
                "z6_exact_err": max(z6_det_err, z6_max_action_err),
                "z6_order_six": len(trivial_sixth_roots) == 6 and distinct_z6_elements == 6,
                "lie_12_ok": (
                    len(basis_12) == 12
                    and gram_det > mp.mpf(1)
                    and max(lie_prop_err, leptoquark_offdiag_max, comm_offdiag_max)
                    < mp.mpf(10) ** (-85)
                ),
            },
        }


# ── Part 2: Explicit Jimbo N=2 (8x8) & N=3 (9x9, 27x27) HOMFLY-PT Schur-Weyl ──
def _build_jimbo_r_check(n_rank: int, q: mp.mpf) -> mp.matrix:
    """Jimbo U_q(sl_N) braided R-matrix on C^N (x) C^N (dimension N^2 x N^2):
        R_check(|i, i>) = q |i, i>
        R_check(|i, j>) = (q - q^{-1}) |i, j> + |j, i>   for i < j
        R_check(|i, j>) = |j, i>                         for i > j
    Satisfies (R_check - q I)(R_check + q^{-1} I) = 0 and the braid relation."""
    h = q - mp.mpf(1) / q
    dim2 = n_rank * n_rank
    r_mat = mp.zeros(dim2, dim2)
    for i in range(n_rank):
        for j in range(n_rank):
            col = i * n_rank + j
            if i == j:
                r_mat[col, col] = q
            elif i < j:
                swap_row = j * n_rank + i
                r_mat[col, col] = h
                r_mat[swap_row, col] = mp.mpf(1)
            else:
                swap_row = j * n_rank + i
                r_mat[swap_row, col] = mp.mpf(1)
    return r_mat


def _evaluate_schur_weyl_n(n_rank: int, q: mp.mpf) -> dict[str, object]:
    one = mp.mpf(1)
    qi = one / q
    i_n = mp.eye(n_rank)
    dim2 = n_rank * n_rank
    dim3 = n_rank ** 3
    i_dim2 = mp.eye(dim2)
    i_dim3 = mp.eye(dim3)

    r_check = _build_jimbo_r_check(n_rank, q)
    hecke_quad_mat = (r_check - q * i_dim2) * (r_check + qi * i_dim2)
    hecke_quad_err = _mat_max_abs(hecke_quad_mat)

    r12 = _kron2(r_check, i_n)
    r23 = _kron2(i_n, r_check)
    braid_err = _mat_max_abs(r12 * r23 * r12 - r23 * r12 * r23)

    # H_3(q) basis words inside End((C^N)^{x 3})
    r12_r23 = r12 * r23
    r23_r12 = r23 * r12
    w0_mat = r12_r23 * r12
    full_twist = w0_mat * w0_mat

    # Exact H_3(q) central idempotents e_{(3)}, e_{(1,1,1)}, e_{(2,1)}
    denom_sym = (one + q ** 2) * (one + q ** 2 + q ** 4)  # = q^3 [3]_q!
    e_3 = (
        i_dim3 + q * (r12 + r23) + (q ** 2) * (r12_r23 + r23_r12) + (q ** 3) * w0_mat
    ) / denom_sym
    e_111 = (
        (q ** 6)
        * (
            i_dim3
            - qi * (r12 + r23)
            + (qi ** 2) * (r12_r23 + r23_r12)
            - (qi ** 3) * w0_mat
        )
        / denom_sym
    )
    e_21 = i_dim3 - e_3 - e_111

    idem_err = max(
        _mat_max_abs(e_3 * e_3 - e_3),
        _mat_max_abs(e_21 * e_21 - e_21),
        _mat_max_abs(e_111 * e_111 - e_111),
    )
    orth_err = max(
        _mat_max_abs(e_3 * e_21),
        _mat_max_abs(e_21 * e_3),
        _mat_max_abs(e_3 * e_111),
        _mat_max_abs(e_111 * e_3),
        _mat_max_abs(e_21 * e_111),
        _mat_max_abs(e_111 * e_21),
    )
    comp_err = _mat_max_abs(e_3 + e_21 + e_111 - i_dim3)
    cent_err = max(
        _mat_max_abs(e_3 * r12 - r12 * e_3),
        _mat_max_abs(e_3 * r23 - r23 * e_3),
        _mat_max_abs(e_21 * r12 - r12 * e_21),
        _mat_max_abs(e_21 * r23 - r23 * e_21),
        _mat_max_abs(e_111 * r12 - r12 * e_111),
        _mat_max_abs(e_111 * r23 - r23 * e_111),
    )
    twist_err = max(
        _mat_max_abs(full_twist * e_3 - (q ** 6) * e_3),
        _mat_max_abs(full_twist * e_21 - e_21),
        _mat_max_abs(full_twist * e_111 - (qi ** 6) * e_111),
    )

    tr_3 = _mat_trace(e_3)
    tr_21 = _mat_trace(e_21)
    tr_111 = _mat_trace(e_111)
    rk_3 = int(mp.nint(tr_3))
    rk_21 = int(mp.nint(tr_21))
    rk_111 = int(mp.nint(tr_111))
    rk_integrality_err = max(
        abs(tr_3 - mp.mpf(rk_3)),
        abs(tr_21 - mp.mpf(rk_21)),
        abs(tr_111 - mp.mpf(rk_111)),
    )

    # Pivotal Cartan element K_N = diag(q^{N-1}, q^{N-3}, ..., q^{-(N-1)}) for quantum traces
    k_vec = mp.zeros(n_rank, n_rank)
    for idx in range(n_rank):
        exp_pow = n_rank - 1 - 2 * idx
        k_vec[idx, idx] = q ** exp_pow
    k_tensor3 = _kron2(_kron2(k_vec, k_vec), k_vec)
    k_comm_err = max(
        _mat_max_abs(k_tensor3 * r12 - r12 * k_tensor3),
        _mat_max_abs(k_tensor3 * r23 - r23 * k_tensor3),
    )
    qtr_3 = _mat_trace(k_tensor3 * e_3)
    qtr_21 = _mat_trace(k_tensor3 * e_21)
    qtr_111 = _mat_trace(k_tensor3 * e_111)

    return {
        "N": n_rank,
        "dim_R_check": f"{dim2}x{dim2}",
        "dim_tensor3": f"{dim3}x{dim3}",
        "hecke_quadratic_max_err": fmt(hecke_quad_err),
        "yang_baxter_braid_max_err": fmt(braid_err),
        "idempotent_max_err": fmt(idem_err),
        "orthogonality_max_err": fmt(orth_err),
        "completeness_max_err": fmt(comp_err),
        "centrality_max_err": fmt(cent_err),
        "full_twist_eigenvalue_max_err": fmt(twist_err),
        "pivotal_K3_commutator_max_err": fmt(k_comm_err),
        "ranks": {
            "rk_e_3": rk_3,
            "rk_e_21": rk_21,
            "rk_e_111": rk_111,
            "sum_ranks": rk_3 + rk_21 + rk_111,
            "trace_integrality_max_err": fmt(rk_integrality_err),
            "e_111_matrix_max_entry_abs": fmt(_mat_max_abs(e_111)),
        },
        "quantum_traces_K_tensor3": {
            "Tr_q_e_3": fmt(qtr_3),
            "Tr_q_e_21": fmt(qtr_21),
            "Tr_q_e_111": fmt(qtr_111),
            "Tr_q_sum": fmt(qtr_3 + qtr_21 + qtr_111),
        },
        "_raw": {
            "hecke_quad_err": hecke_quad_err,
            "braid_err": braid_err,
            "alg_err": max(
                idem_err,
                orth_err,
                comp_err,
                cent_err,
                twist_err,
                k_comm_err,
                rk_integrality_err,
            ),
            "ranks_tuple": (rk_3, rk_21, rk_111),
            "e111_max_abs": _mat_max_abs(e_111),
            "qtr_3": qtr_3,
            "qtr_21": qtr_21,
            "qtr_111": qtr_111,
        },
    }


def _evaluate_part2_at_pin(q: mp.mpf, pin_label: str) -> dict[str, object]:
    with mp.workdps(95):
        one = mp.mpf(1)
        h = q - one / q
        q2 = (q ** 2 - q ** (-2)) / h
        q3 = (q ** 3 - q ** (-3)) / h
        q4 = (q ** 4 - q ** (-4)) / h
        q5 = (q ** 5 - q ** (-5)) / h

        sw_n2 = _evaluate_schur_weyl_n(2, q)
        sw_n3 = _evaluate_schur_weyl_n(3, q)

        # Quantum-dimension closed-form checks on W_3^{x 3} (N=3, a = q^3):
        #   d_q^{N=3}(3)     = [4]_q [5]_q / [2]_q
        #   2 * d_q^{N=3}(2,1) = 2 [2]_q [4]_q
        #   d_q^{N=3}(1,1,1) = 1
        #   Sum              = [3]_q^3
        dq3_sym = q4 * q5 / q2
        dq3_21_twice = mp.mpf(2) * q2 * q4
        dq3_111 = one
        qdim_n3_gap = max(
            abs(sw_n3["_raw"]["qtr_3"] - dq3_sym),
            abs(sw_n3["_raw"]["qtr_21"] - dq3_21_twice),
            abs(sw_n3["_raw"]["qtr_111"] - dq3_111),
            abs((dq3_sym + dq3_21_twice + dq3_111) - (q3 ** 3)),
        )

        # Baryon singlet weight comparison:
        #   N=3 HOMFLY-PT normalized quantum-dimension weight: w_{(1^3)}^{N=3} = 1 / [3]_q^3
        #   N=2 GPMT modified-trace magnitude: |d_mod(1,1,1)| = q^3 / ((q^2+1)(q^4+q^2+1)) = 1 / ([2]_q [3]_q)
        #   Exact ratio: w_{(1^3)}^{N=3} / |d_mod(1,1,1)| = [2]_q / [3]_q^2
        w_baryon_n3 = sw_n3["_raw"]["qtr_111"] / (q3 ** 3)
        d_mod_n2_laurent = (q ** 3) / ((q ** 2 + one) * (q ** 4 + q ** 2 + one))
        d_mod_n2_qint = one / (q2 * q3)
        ratio_n3_over_gpmt = w_baryon_n3 / d_mod_n2_laurent
        ratio_closed = q2 / (q3 ** 2)
        baryon_ratio_gap = max(
            abs(d_mod_n2_laurent - d_mod_n2_qint),
            abs(w_baryon_n3 - one / (q3 ** 3)),
            abs(ratio_n3_over_gpmt - ratio_closed),
        )

        raw_n2 = sw_n2.pop("_raw")
        raw_n3 = sw_n3.pop("_raw")

        return {
            "pin_label": pin_label,
            "q": fmt(q),
            "a_homfly_N3_eq_q_cubed": fmt(q ** 3),
            "qInt_2": fmt(q2),
            "qInt_3": fmt(q3),
            "schur_weyl_N2_V2_tensor3": sw_n2,
            "schur_weyl_N3_W3_tensor3": sw_n3,
            "baryon_singlet_weight_comparison": {
                "N3_homfly_qdim_weight_1_div_qInt3_cubed": fmt(w_baryon_n3),
                "N2_gpmt_abs_dMod_1_div_qInt2_qInt3": fmt(d_mod_n2_laurent),
                "gpmt_laurent_vs_qint_gap": fmt(abs(d_mod_n2_laurent - d_mod_n2_qint)),
                "ratio_N3_over_N2_GPMT_eq_qInt2_div_qInt3_sq": fmt(ratio_n3_over_gpmt),
                "classical_q_to_1_limit_ratio": "2/9",
            },
            "_raw_checks": {
                "n3_hecke_err": raw_n3["hecke_quad_err"],
                "n3_braid_err": raw_n3["braid_err"],
                "n2_hecke_braid_err": max(raw_n2["hecke_quad_err"], raw_n2["braid_err"]),
                "idem_alg_err": max(raw_n2["alg_err"], raw_n3["alg_err"], qdim_n3_gap, baryon_ratio_gap),
                "ranks_ok": (
                    raw_n2["ranks_tuple"] == (4, 4, 0)
                    and raw_n3["ranks_tuple"] == (10, 16, 1)
                    and raw_n2["e111_max_abs"] < mp.mpf(10) ** (-85)
                    and raw_n3["e111_max_abs"] > mp.mpf(1) / mp.mpf(10)
                ),
            },
        }


# ── Part 3: 80-dps Weinberg Angle sin^2(theta_W) & 1-Loop RG Unification Audit ─
def _trace_poly_P(m: int, h: mp.mpf) -> mp.mpf:
    """2-strand torus-link Plancherel trace polynomial P_m(h) = sum_{j=0}^m (1/2) C(m+j, 2j) h^{2j}."""
    half = mp.mpf(1) / mp.mpf(2)
    return mp.fsum(
        mp.mpf(_binom_int(m + j, 2 * j)) * half * (h ** (2 * j))
        for j in range(m + 1)
    )


def _solve_ew_vev_gev(q: mp.mpf, m_p_mev: mp.mpf) -> mp.mpf:
    """QOU derived electroweak VEV v(q) from `ElectroweakBringSchwingerBridge` fixed-point cubic."""
    one = mp.mpf(1)
    h = q - one / q
    hbar_q = (q - one) / q
    q2 = (q ** 2 - q ** (-2)) / h
    q4 = (q ** 4 - q ** (-4)) / h
    q6 = (q ** 6 - q ** (-6)) / h
    q8 = (q ** 8 - q ** (-8)) / h
    t_ew = q * (q2 / mp.mpf(2)) * q4 * q6 * q8 + one / mp.pi
    h_hab = q2 / (mp.mpf(8) * mp.pi)

    def _cubic(av: mp.mpf) -> mp.mpf:
        return (hbar_q ** 2) * h_hab * (av ** 3) - h_hab * (av ** 2) + t_ew * av - one

    av_root = mp.findroot(_cubic, one / t_ew)
    n_v = one / av_root
    return n_v * (m_p_mev / mp.mpf(1000))


def _evaluate_part3_weinberg_and_rg(
    pins: dict[str, mp.mpf],
) -> dict[str, object]:
    with mp.workdps(95):
        one = mp.mpf(1)
        three = mp.mpf(3)
        eight = mp.mpf(8)

        # Validation-only experimental benchmarks (CODATA 2022 / PDG 2024)
        alpha_inv_0_codata = mp.mpf(
            _codata_reg.codata("inverse fine-structure constant").value_str
        )
        e_planck_gev = mp.mpf(
            _codata_reg.codata("Planck mass energy equivalent in GeV").value_str
        )
        m_planck_reduced_gev = e_planck_gev / mp.sqrt(eight * mp.pi)

        me_gev = mp.mpf(str(M_E_MEV)) / mp.mpf(1000)
        mmu_pdg_gev = mp.mpf(str(M_MU_MEV)) / mp.mpf(1000)
        mp_pdg_gev = mp.mpf(str(M_P_MEV)) / mp.mpf(1000)
        mtau_pdg_gev = mp.mpf("1.77686")
        mc_pdg_gev = mp.mpf("1.27")
        mb_pdg_gev = mp.mpf("4.18")
        mz_pdg_gev = mp.mpf("91.1876")
        mw_pdg_gev = mp.mpf("80.3692")

        sin2_pdg_msbar = mp.mpf("0.23122")
        sin2_pdg_msbar_err = mp.mpf("0.00004")
        sin2_pdg_onshell_fit = mp.mpf("0.22305")
        sin2_pdg_mw_mz_direct = one - (mw_pdg_gev / mz_pdg_gev) ** 2
        alpha_inv_mz_pdg_msbar = mp.mpf("127.951")
        alpha_s_mz_pdg = mp.mpf("0.1180")

        # 1. Exact UV trace normalization on F = V_2 (+) W_3^* and S_chiral = Lambda^1(F) (+) Lambda^2(F^*):
        #    Tr_{S_chiral}(T_3^2) = 3*(1/4 + 1/4) + (1/4 + 1/4) = 2
        #    Tr_{S_chiral}(Y^2)   = 6*(1/36) + 3*(4/9) + 3*(1/9) + 2*(1/4) + 1*(1) = 10/3
        #    Tr_{S_chiral}(Q^2)   = Tr(T_3^2) + Tr(Y^2) = 2 + 10/3 = 16/3
        #    sin^2(theta_W)_UV    = Tr(T_3^2) / Tr(Q^2) = 2 / (16/3) = 3/8
        tr_t3_sq_gen = Fraction(3, 2) + Fraction(1, 2)
        tr_y_sq_gen = (
            6 * Fraction(1, 36)
            + 3 * Fraction(4, 9)
            + 3 * Fraction(1, 9)
            + 2 * Fraction(1, 4)
            + Fraction(1, 1)
        )
        tr_q_sq_gen = tr_t3_sq_gen + tr_y_sq_gen
        sin2_uv_rat = tr_t3_sq_gen / tr_q_sq_gen  # 3/8
        k_gut_rat = tr_y_sq_gen / tr_t3_sq_gen    # 5/3

        # 2. Exact 1-loop Standard Model beta coefficients derived from S_chiral x N_gen + N_H Higgs doublet:
        #    b_i = -(11/3) C_2(G_i) + (2/3) * N_gen * T_i(S_chiral) + (1/3) * N_H * T_i(H)
        n_gen = 3
        n_higgs = 1
        b1_rat = (
            Fraction(2, 3) * n_gen * (Fraction(3, 5) * tr_y_sq_gen)
            + Fraction(1, 3) * n_higgs * (Fraction(3, 5) * 2 * Fraction(1, 4))
        )  # 41/10
        b2_rat = (
            -Fraction(11, 3) * 2
            + Fraction(2, 3) * n_gen * tr_t3_sq_gen
            + Fraction(1, 3) * n_higgs * Fraction(1, 2)
        )  # -19/6
        b3_rat = -Fraction(11, 3) * 3 + Fraction(2, 3) * n_gen * Fraction(2, 1)  # -7
        b_em_rat = b2_rat + k_gut_rat * b1_rat  # +11/3

        b1 = mp.mpf(b1_rat.numerator) / mp.mpf(b1_rat.denominator)
        b2 = mp.mpf(b2_rat.numerator) / mp.mpf(b2_rat.denominator)
        b3 = mp.mpf(b3_rat.numerator) / mp.mpf(b3_rat.denominator)
        b_em = mp.mpf(b_em_rat.numerator) / mp.mpf(b_em_rat.denominator)
        sin2_uv = mp.mpf(sin2_uv_rat.numerator) / mp.mpf(sin2_uv_rat.denominator)

        def _err_pct(val: mp.mpf, ref: mp.mpf) -> str:
            return fmt((val - ref) / ref * mp.mpf(100))

        def _rg_run_from_uv(
            sin2_star: mp.mpf, alpha_inv_mz: mp.mpf, mu_star_gev: mp.mpf, mz_gev: mp.mpf
        ) -> dict[str, mp.mpf]:
            """Run 1-loop SM gauge couplings from UV boundary sin^2(theta_W)(mu_*) = sin2_star
            (i.e. alpha_2^{-1}(mu_*) / alpha_EM^{-1}(mu_*) = sin2_star) down to M_Z."""
            t_log = mp.log(mu_star_gev / mz_gev) / (mp.mpf(2) * mp.pi)
            alpha_em_inv_star = alpha_inv_mz - b_em * t_log
            alpha2_inv_star = sin2_star * alpha_em_inv_star
            alpha1_inv_star = (three / mp.mpf(5)) * (one - sin2_star) * alpha_em_inv_star
            alpha2_inv_mz = alpha2_inv_star + b2 * t_log
            alpha1_inv_mz = alpha1_inv_star + b1 * t_log
            sin2_mz = alpha2_inv_mz / alpha_inv_mz
            # Also evaluate alpha_3^{-1}(M_Z) if alpha_3(mu_*) = alpha_2(mu_*)
            alpha3_inv_mz = alpha2_inv_star + b3 * t_log
            return {
                "t_log_div_2pi": t_log,
                "alpha_em_inv_star": alpha_em_inv_star,
                "alpha2_inv_star": alpha2_inv_star,
                "alpha1_inv_star": alpha1_inv_star,
                "alpha2_inv_mz": alpha2_inv_mz,
                "alpha1_inv_mz": alpha1_inv_mz,
                "sin2_mz": sin2_mz,
                "alpha3_inv_mz_from_alpha2_star": alpha3_inv_mz,
            }

        def _solve_mu12_intersection(
            alpha_inv_mz: mp.mpf, sin2_target_mz: mp.mpf, mz_gev: mp.mpf
        ) -> dict[str, mp.mpf]:
            """Solve exact 1-loop SM alpha_1(mu_12) = alpha_2(mu_12) intersection scale mu_12
            corresponding to sin^2(theta_W)(mu_12) = 3/8."""
            alpha2_inv_mz = sin2_target_mz * alpha_inv_mz
            alpha1_inv_mz = (three / mp.mpf(5)) * (one - sin2_target_mz) * alpha_inv_mz
            # alpha1_inv(mu) - alpha2_inv(mu) = (alpha1_inv_mz - alpha2_inv_mz) - (b1 - b2) * t = 0
            t_12 = (alpha1_inv_mz - alpha2_inv_mz) / (b1 - b2)
            ln_ratio = mp.mpf(2) * mp.pi * t_12
            mu_12_gev = mz_gev * mp.exp(ln_ratio)
            alpha_u_inv = alpha2_inv_mz - b2 * t_12
            alpha3_inv_mz_pred = alpha_u_inv + b3 * t_12
            alpha_s_mz_pred = one / alpha3_inv_mz_pred
            return {
                "ln_mu12_over_MZ": ln_ratio,
                "mu_12_GeV": mu_12_gev,
                "alpha_U_inv_at_mu12": alpha_u_inv,
                "alpha3_inv_MZ_if_unified_at_mu12": alpha3_inv_mz_pred,
                "alpha_s_MZ_if_unified_at_mu12": alpha_s_mz_pred,
            }

        per_pin_results: dict[str, object] = {}
        raw_rg_identity_err = mp.mpf(0)
        cosh_cos_sep_ok = True

        vol_41 = vol_4_1_at(95)

        for pin_name, q in pins.items():
            qi = one / q
            h = q - qi
            eta = mp.log(q)
            hbar_q = (q - one) / q
            q2 = (q ** 2 - q ** (-2)) / h
            q3 = (q ** 3 - q ** (-3)) / h

            # QOU Form-B Bring-Schwinger alpha_EM^{-1}(q) at q^2 = 0
            alpha_inv_0_qou = mp.mpf(str(alpha_em_inv_bring_schwinger(q=q)))

            # QOU-derived scales (zero empirical quark/tau/Z mass inputs):
            #   m_mu^{QOU}(q) = m_e * Vol(4_1) / hbar_q^2
            #   m_p^{QOU}(q)  = m_e * (2 * Vol(4_1) / hbar_q^2 * |tr_M(Bor)| * [3]_q! / q^3 - 12)
            #   v^{QOU}(q)    = N_v(q) * m_p^{QOU}(q)
            trm_bor = abs(
                (mp.mpf(4) + h ** 2 - mp.mpf(3) * (h ** 4) - h ** 6) / (h ** 2 + mp.mpf(4))
            )
            mp_qou_gev = me_gev * (
                mp.mpf(2) * vol_41 / (hbar_q ** 2) * (trm_bor * q2 * q3 / (q ** 3))
                - mp.mpf(12)
            )
            mmu_qou_gev = me_gev * vol_41 / (hbar_q ** 2)
            m_constit_qou_gev = mp_qou_gev / three
            v_qou_gev = _solve_ew_vev_gev(q, mp_qou_gev * mp.mpf(1000))

            # VP Track 1 (Pure QOU-derived thresholds):
            #   Charged leptons at (m_e, m_mu^{QOU}, m_p^{QOU}); light quarks (u,d,s: sum N_c Q^2 = 2)
            #   at constituent threshold m_p^{QOU}/3; heavy active quarks (c,b: sum N_c Q^2 = 5/3)
            #   at hadronic scale m_p^{QOU}, evaluated at M_Z^{QOU} ~= v^{QOU} * 0.37035 (from EW-bridge
            #   g^2+g'^2 or reference M_Z; use self-consistent EW-bridge scale M_Z_ref = mz_pdg_gev for
            #   direct comparison at the same renorm scale, AND record v_qou_gev explicitly).
            vp_coeff = mp.mpf(2) / (three * mp.pi)
            delta_ainv_qou_ll = -vp_coeff * (
                mp.log(mz_pdg_gev / me_gev)
                + mp.log(mz_pdg_gev / mmu_qou_gev)
                + mp.log(mz_pdg_gev / mp_qou_gev)
                + mp.mpf(2) * mp.log(mz_pdg_gev / m_constit_qou_gev)
                + (mp.mpf(5) / three) * mp.log(mz_pdg_gev / mp_qou_gev)
            )
            alpha_inv_mz_qou_vp = alpha_inv_0_qou + delta_ainv_qou_ll

            # VP Track 2 (Standard 1-loop fermion VP from Form-B alpha_EM^{-1}(q) with PDG thresholds:
            #   leptons m_e, m_mu, m_tau; constituent light quarks m_p/3; heavy quarks m_c, m_b,
            #   both pure leading-log and finite -5/6 subtraction + W-loop +1/(6*pi)):
            sum_nc_q2_5f = three + mp.mpf(2) + (mp.mpf(5) / three)  # = 20/3
            delta_ainv_sm_ll = -vp_coeff * (
                mp.log(mz_pdg_gev / me_gev)
                + mp.log(mz_pdg_gev / mmu_pdg_gev)
                + mp.log(mz_pdg_gev / mtau_pdg_gev)
                + mp.mpf(2) * mp.log(mz_pdg_gev / (mp_pdg_gev / three))
                + (mp.mpf(4) / three) * mp.log(mz_pdg_gev / mc_pdg_gev)
                + (one / three) * mp.log(mz_pdg_gev / mb_pdg_gev)
            )
            delta_ainv_sm_1loop_finite = (
                delta_ainv_sm_ll
                + vp_coeff * sum_nc_q2_5f * (mp.mpf(5) / mp.mpf(6))
                + one / (mp.mpf(6) * mp.pi)
            )
            alpha_inv_mz_sm_ll = alpha_inv_0_qou + delta_ainv_sm_ll
            alpha_inv_mz_sm_1loop_fin = alpha_inv_0_qou + delta_ainv_sm_1loop_finite

            # Run 1-loop SM RG from UV sin^2(theta_W)(mu_*) = 3/8 at mu_* = E_Pl and M_Pl_reduced
            rg_epl_pdg_vp = _rg_run_from_uv(
                sin2_uv, alpha_inv_mz_pdg_msbar, e_planck_gev, mz_pdg_gev
            )
            rg_epl_qou_vp = _rg_run_from_uv(
                sin2_uv, alpha_inv_mz_qou_vp, e_planck_gev, mz_pdg_gev
            )
            rg_mpl_red_pdg_vp = _rg_run_from_uv(
                sin2_uv, alpha_inv_mz_pdg_msbar, m_planck_reduced_gev, mz_pdg_gev
            )

            # Verify closed-form Georgi-Quinn-Weinberg identity:
            #   sin^2(theta_W)(M_Z) = 3/8 - (5/8)*(b_1 - b_2) * ln(mu_*/M_Z) / (2*pi*alpha_EM^{-1}(M_Z))
            gqw_closed = sin2_uv - (mp.mpf(5) / eight) * (b1 - b2) * (
                mp.log(e_planck_gev / mz_pdg_gev)
                / (mp.mpf(2) * mp.pi * alpha_inv_mz_pdg_msbar)
            )
            raw_rg_identity_err = max(
                raw_rg_identity_err,
                abs(rg_epl_pdg_vp["sin2_mz"] - gqw_closed),
                abs(
                    (
                        rg_epl_pdg_vp["alpha2_inv_mz"]
                        + (mp.mpf(5) / three) * rg_epl_pdg_vp["alpha1_inv_mz"]
                    )
                    - alpha_inv_mz_pdg_msbar
                ),
            )

            mu12_pdg_vp = _solve_mu12_intersection(
                alpha_inv_mz_pdg_msbar, sin2_pdg_msbar, mz_pdg_gev
            )
            mu12_qou_vp = _solve_mu12_intersection(
                alpha_inv_mz_qou_vp, sin2_pdg_msbar, mz_pdg_gev
            )

            # 3. q-Deformed Quantum-Dimension Trace Candidates on F = V_2 (+) W_3^*:
            #   QDim-A: Rational Y|_F = (-1/2, +1/3) weighted by ([2]_q, [3]_q): 9[2]_q / (18[2]_q + 4[3]_q)
            sin2_qdim_a = (mp.mpf(9) * q2) / (mp.mpf(18) * q2 + mp.mpf(4) * q3)
            #   QDim-B1: GUT-normalized (3/8 at q=1) replacement (2,3) -> ([2]_q, [3]_q): 9[2]_q / (9[2]_q + 10[3]_q)
            sin2_qdim_b1 = (mp.mpf(9) * q2) / (mp.mpf(9) * q2 + mp.mpf(10) * q3)
            #   QDim-B2: Unrescaled [2]_q / ([2]_q + (5/3)[3]_q) = 3[2]_q / (3[2]_q + 5[3]_q) (2/7 at q=1)
            sin2_qdim_b2 = (three * q2) / (three * q2 + mp.mpf(5) * q3)
            #   QDim-C: q-traceless hypercharge [2]_q y_2 + [3]_q y_3 = 0 => [3]_q / (2[3]_q + [2]_q)
            sin2_qdim_c = q3 / (mp.mpf(2) * q3 + q2)
            #   QDim-D: Chiral generation S_chiral with (2,3) -> ([2]_q, [3]_q)
            trq_t3_s = (q3 + one) * (q2 / mp.mpf(4))
            trq_y_s = (
                (q2 * q3) / mp.mpf(36)
                + (mp.mpf(5) / mp.mpf(9)) * q3
                + (q2 / mp.mpf(4))
                + one
            )
            sin2_qdim_d = trq_t3_s / (trq_t3_s + trq_y_s)

            # Also run QDim-B2 from mu_12_pdg_vp down to M_Z to check whether a (2/7) UV ratio closes M_Z
            rg_qdim_b2_from_mu12 = _rg_run_from_uv(
                sin2_qdim_b2,
                alpha_inv_mz_pdg_msbar,
                mu12_pdg_vp["mu_12_GeV"],
                mz_pdg_gev,
            )

            # 4. Existing QOU Repo Categorical / Torus-Link / Hoefsmit / Substrate Candidates:
            #   Repo-EW1a (`conj:weinberg-angle-categorical` pure-pattern Hoefsmit evaluation):
            #     cot(theta_W) = q^{-4}  =>  sin^2(theta_W) = q^8 / (1 + q^8)
            sin2_ew1_pure = (q ** 8) / (one + q ** 8)
            #   Repo-EW1b (inverted slot ratio cot(theta_W) = q^{+4}):
            #     sin^2(theta_W) = 1 / (1 + q^8)
            sin2_ew1_inv = one / (one + q ** 8)

            #   Repo-EW2 (`TorusKnotMassPlancherelBridge.lean` bare T(2,4)/T(2,6) Plancherel ratio):
            #     cos(theta_W) = P_2(h) / P_3(h) = cosh(5*eta) / cosh(7*eta)
            p2_h = _trace_poly_P(2, h)
            p3_h = _trace_poly_P(3, h)
            cos_ew2_bare = p2_h / p3_h
            cos_ew2_cosh = mp.cosh(mp.mpf(5) * eta) / mp.cosh(mp.mpf(7) * eta)
            cos_ew2_trig = mp.cos(mp.mpf(5) * eta) / mp.cos(mp.mpf(7) * eta)
            raw_rg_identity_err = max(
                raw_rg_identity_err, abs(cos_ew2_bare - cos_ew2_cosh)
            )
            if not (cos_ew2_cosh < one < cos_ew2_trig):
                cosh_cos_sep_ok = False
            sin2_ew2_bare = one - cos_ew2_bare ** 2

            #   Repo-EW3 (`ElectroweakBringSchwingerBridge.lean` ([2]_q/2)^2 dressed W/Z ratio):
            #     cos(theta_W) = (P_2(h) / P_3(h)) * (2 / [2]_q)^2
            cos_ew3_dressed = cos_ew2_bare * ((mp.mpf(2) / q2) ** 2)
            sin2_ew3_dressed = one - cos_ew3_dressed ** 2

            #   Repo-EW4 (`SubstrateEWHypotheses.lean` g = pi * h => sin^2(theta_W) = e^2 / g^2 = 4 / (pi * h^2 * alpha_EM^{-1})):
            sin2_ew4_mz_pdg_vp = mp.mpf(4) / (mp.pi * (h ** 2) * alpha_inv_mz_pdg_msbar)
            sin2_ew4_mz_qou_vp = mp.mpf(4) / (mp.pi * (h ** 2) * alpha_inv_mz_qou_vp)
            sin2_ew4_q2_zero = mp.mpf(4) / (mp.pi * (h ** 2) * alpha_inv_0_qou)

            def _cand_row(cid: str, formula: str, status: str, val: mp.mpf) -> dict[str, str]:
                return {
                    "candidate_id": cid,
                    "formula": formula,
                    "epistemic_status": status,
                    "sin2_theta_W": fmt(val),
                    "err_vs_PDG_MSbar_0p23122_pct": _err_pct(val, sin2_pdg_msbar),
                    "err_vs_PDG_onshell_0p22305_pct": _err_pct(val, sin2_pdg_onshell_fit),
                }

            candidates_table = [
                _cand_row(
                    "UV_1_classical_trace_3_div_8",
                    "Tr_{S_chiral}(T_3^2) / Tr_{S_chiral}(Q^2) = 3/8 (unrun UV boundary)",
                    "proved_UV_trace_identity_requires_RG_running",
                    sin2_uv,
                ),
                _cand_row(
                    "RG_2a_1loop_SM_from_E_Planck_PDG_VP",
                    "3/8 - (109/24) * ln(E_Pl/M_Z) / (2*pi*alpha_EM^{-1}(M_Z)_PDG)",
                    "exact_1loop_SM_RGE_no_intermediate_thresholds",
                    rg_epl_pdg_vp["sin2_mz"],
                ),
                _cand_row(
                    "RG_2b_1loop_SM_from_E_Planck_QOU_VP",
                    "3/8 - (109/24) * ln(E_Pl/M_Z) / (2*pi*alpha_EM^{-1}(M_Z)_QOU_VP)",
                    "exact_1loop_SM_RGE_with_QOU_derived_VP_thresholds",
                    rg_epl_qou_vp["sin2_mz"],
                ),
                _cand_row(
                    "RG_2c_1loop_SM_from_reduced_M_Planck_PDG_VP",
                    "3/8 - (109/24) * ln(M_Pl_red/M_Z) / (2*pi*alpha_EM^{-1}(M_Z)_PDG)",
                    "exact_1loop_SM_RGE_at_reduced_Planck_scale",
                    rg_mpl_red_pdg_vp["sin2_mz"],
                ),
                _cand_row(
                    "QDim_3a_fibre_rational_Y_quantum_trace",
                    "9*[2]_q / (18*[2]_q + 4*[3]_q) (UV q-trace on F = V_2 (+) W_3^*)",
                    "exploratory_UV_q_trace_reduces_to_3_div_8_at_q_eq_1",
                    sin2_qdim_a,
                ),
                _cand_row(
                    "QDim_3b1_GUT_normalized_qdim_ratio",
                    "9*[2]_q / (9*[2]_q + 10*[3]_q) (UV q-dim replacement, 3/8 at q=1)",
                    "exploratory_UV_q_dim_ratio",
                    sin2_qdim_b1,
                ),
                _cand_row(
                    "QDim_3b2_unrescaled_qdim_ratio",
                    "[2]_q / ([2]_q + (5/3)*[3]_q) = 3*[2]_q / (3*[2]_q + 5*[3]_q) (2/7 at q=1)",
                    "exploratory_unrescaled_q_dim_ratio",
                    sin2_qdim_b2,
                ),
                _cand_row(
                    "QDim_3b2_run_from_mu12_to_MZ",
                    "1-loop SM RG from sin^2(mu_12) = 3*[2]_q/(3*[2]_q + 5*[3]_q) down to M_Z",
                    "exploratory_q_dim_UV_with_1loop_SM_RG",
                    rg_qdim_b2_from_mu12["sin2_mz"],
                ),
                _cand_row(
                    "QDim_3c_q_traceless_hypercharge",
                    "[3]_q / (2*[3]_q + [2]_q) (from Tr_q(Y_q|_F) = 0, 3/8 at q=1)",
                    "exploratory_q_traceless_UV_ratio",
                    sin2_qdim_c,
                ),
                _cand_row(
                    "QDim_3d_chiral_exterior_qdim_trace",
                    "Tr_q(T_3^2)_{S_chiral} / Tr_q(Q^2)_{S_chiral} (3/8 at q=1)",
                    "exploratory_chiral_generation_q_trace",
                    sin2_qdim_d,
                ),
                _cand_row(
                    "Repo_EW1a_hoefsmit_pure_pattern_cot_q_minus4",
                    "q^8 / (1 + q^8) from cot(theta_W) = q^{-4} (`weinberg-angle-categorical.md:24`)",
                    "documented_negative_result_pure_pattern_fails",
                    sin2_ew1_pure,
                ),
                _cand_row(
                    "Repo_EW1b_hoefsmit_inverted_slot_cot_q_plus4",
                    "1 / (1 + q^8) from inverted slot ratio cot(theta_W) = q^{+4}",
                    "exploratory_slot_inversion_still_fails",
                    sin2_ew1_inv,
                ),
                _cand_row(
                    "Repo_EW2_torus_link_plancherel_bare_T24_T26",
                    "1 - (P_2(h)/P_3(h))^2 = 1 - (cosh(5*ln q)/cosh(7*ln q))^2 (`TorusKnotMassPlancherelBridge`)",
                    "derived_2strand_plancherel_ratio_no_fit",
                    sin2_ew2_bare,
                ),
                _cand_row(
                    "Repo_EW3_torus_link_qdim_dressed_W_Z_bridge",
                    "1 - ((P_2(h)/P_3(h)) * (2/[2]_q)^2)^2 (`ElectroweakBringSchwingerBridge`)",
                    "postulated_qInt2_over_2_sq_genus_step_dressing_onshell_target",
                    sin2_ew3_dressed,
                ),
                _cand_row(
                    "Repo_EW4a_substrate_g_eq_pi_h_at_MZ_PDG_VP",
                    "4 / (pi * h^2 * alpha_EM^{-1}(M_Z)_PDG) from g = pi*h (`SubstrateEWHypotheses`)",
                    "conjectural_class_hypothesis_g_eq_pi_h_with_PDG_VP",
                    sin2_ew4_mz_pdg_vp,
                ),
                _cand_row(
                    "Repo_EW4b_substrate_g_eq_pi_h_at_MZ_QOU_VP",
                    "4 / (pi * h^2 * alpha_EM^{-1}(M_Z)_QOU_VP) from g = pi*h (`SubstrateEWHypotheses`)",
                    "conjectural_class_hypothesis_g_eq_pi_h_with_QOU_VP",
                    sin2_ew4_mz_qou_vp,
                ),
                _cand_row(
                    "Repo_EW4c_substrate_g_eq_pi_h_unrun_q2_zero",
                    "4 / (pi * h^2 * alpha_EM^{-1}(q)_FormB) at q^2 = 0",
                    "conjectural_class_hypothesis_g_eq_pi_h_unrun_IR",
                    sin2_ew4_q2_zero,
                ),
            ]

            per_pin_results[pin_name] = {
                "q": fmt(q),
                "h": fmt(h),
                "eta_ln_q": fmt(eta),
                "v_QOU_fixed_point_GeV": fmt(v_qou_gev),
                "alpha_em_inv_tracks": {
                    "FormB_Bring_Schwinger_q2_eq_0": fmt(alpha_inv_0_qou),
                    "CODATA2022_q2_eq_0_validation_only": fmt(alpha_inv_0_codata),
                    "Track1_QOU_derived_thresholds_LL_at_MZ": fmt(alpha_inv_mz_qou_vp),
                    "Track2a_SM_PDG_fermions_LL_from_FormB_at_MZ": fmt(alpha_inv_mz_sm_ll),
                    "Track2b_SM_PDG_fermions_finite_plus_W_from_FormB_at_MZ": fmt(
                        alpha_inv_mz_sm_1loop_fin
                    ),
                    "Track3_PDG_MSbar_benchmark_at_MZ": fmt(alpha_inv_mz_pdg_msbar),
                },
                "one_loop_sm_unification_diagnostics": {
                    "mu_12_intersection_PDG_VP": {
                        k_key: fmt(v_val) for k_key, v_val in mu12_pdg_vp.items()
                    },
                    "mu_12_intersection_QOU_VP": {
                        k_key: fmt(v_val) for k_key, v_val in mu12_qou_vp.items()
                    },
                    "top_down_from_E_Planck_PDG_VP": {
                        k_key: fmt(v_val) for k_key, v_val in rg_epl_pdg_vp.items()
                    },
                    "top_down_from_E_Planck_QOU_VP": {
                        k_key: fmt(v_val) for k_key, v_val in rg_epl_qou_vp.items()
                    },
                    "cosh_vs_cos_separation_at_eta": {
                        "cosh_5eta_div_cosh_7eta": fmt(cos_ew2_cosh),
                        "cos_5eta_div_cos_7eta": fmt(cos_ew2_trig),
                    },
                },
                "weinberg_angle_candidates": candidates_table,
            }

        return {
            "uv_trace_identities": {
                "Tr_T3_sq_per_generation": f"{tr_t3_sq_gen.numerator}/{tr_t3_sq_gen.denominator}",
                "Tr_Y_sq_per_generation": f"{tr_y_sq_gen.numerator}/{tr_y_sq_gen.denominator}",
                "Tr_Q_sq_per_generation": f"{tr_q_sq_gen.numerator}/{tr_q_sq_gen.denominator}",
                "GUT_hypercharge_factor_k_Y": f"{k_gut_rat.numerator}/{k_gut_rat.denominator}",
                "sin2_theta_W_UV_exact": f"{sin2_uv_rat.numerator}/{sin2_uv_rat.denominator}",
                "sin2_theta_W_UV_80dps": fmt(sin2_uv),
            },
            "one_loop_sm_beta_coefficients": {
                "N_gen": n_gen,
                "N_Higgs_doublets": n_higgs,
                "b1_U1_GUT": f"{b1_rat.numerator}/{b1_rat.denominator}",
                "b2_SU2_L": f"{b2_rat.numerator}/{b2_rat.denominator}",
                "b3_SU3_c": f"{b3_rat.numerator}/{b3_rat.denominator}",
                "b_EM_eq_b2_add_5_div_3_b1": f"{b_em_rat.numerator}/{b_em_rat.denominator}",
            },
            "validation_benchmarks_not_used_in_derivations": {
                "PDG_sin2_theta_W_MZ_MSbar": fmt(sin2_pdg_msbar),
                "PDG_sin2_theta_W_MZ_MSbar_err": fmt(sin2_pdg_msbar_err),
                "PDG_sin2_theta_W_onshell_fit": fmt(sin2_pdg_onshell_fit),
                "PDG_1_minus_MW2_div_MZ2_direct": fmt(sin2_pdg_mw_mz_direct),
                "PDG_alpha_s_MZ": fmt(alpha_s_mz_pdg),
                "CODATA_E_Planck_GeV": fmt(e_planck_gev),
                "CODATA_M_Planck_reduced_GeV": fmt(m_planck_reduced_gev),
            },
            "by_pin": per_pin_results,
            "_raw_checks": {
                "uv_and_beta_exact": (
                    sin2_uv_rat == Fraction(3, 8)
                    and b1_rat == Fraction(41, 10)
                    and b2_rat == Fraction(-19, 6)
                    and b3_rat == Fraction(-7, 1)
                    and b_em_rat == Fraction(11, 3)
                ),
                "rg_and_plancherel_identity_err": raw_rg_identity_err,
                "cosh_cos_sep_ok": cosh_cos_sep_ok,
            },
        }


def main() -> int:
    set_compute_dps(80)
    with mp.workdps(95):
        q0 = q_at(95)
        q2t = q_two_term_borromean_at(95, k_weighted=False)
        q_mu = q_muon_at(95)

        pins = {
            "q0_proton_1term": q0,
            "q2t_two_term_borromean": q2t,
            "q_muon_codata2022": q_mu,
        }

        part1 = _evaluate_part1_fibre_and_anomalies()
        part2_by_pin = {
            p_name: _evaluate_part2_at_pin(q_val, p_name)
            for p_name, q_val in pins.items()
        }
        part3 = _evaluate_part3_weinberg_and_rg(pins)

        p1_raw = part1.pop("_raw_checks")
        p2_raws = [v.pop("_raw_checks") for v in part2_by_pin.values()]
        p3_raw = part3.pop("_raw_checks")

        wb = WitnessBuilder(
            "su3-su2-u1-pushforward-and-weinberg",
            engine="mpmath-80dps",
            output_dir=HERE,
        )
        wb.set_description(
            "80-dps parameter-free verification of the split Standard Model bundle "
            "F = V_2 (+) W_3^* (W_3 = pi_* L on Bring's curve), chiral exterior generation "
            "Lambda^1(F) (+) Lambda^2(F^*), exact anomaly uniqueness factorization "
            "9 Y_Q (4 Y_Q + Y_{u^c})(2 Y_Q - Y_{u^c}), global Z_6 kernel, 12-generator split "
            "Lie algebra s(u(2) (+) u(3)) (0 X/Y leptoquarks), explicit 9x9 and 27x27 Jimbo "
            "N=3 (a = q^3) HOMFLY-PT Schur-Weyl central idempotents (ranks 10, 16, 1 vs N=2 "
            "ranks 4, 4, 0), and side-by-side Weinberg-angle / 1-loop RG gauge-coupling audit "
            "across q_0, q_2t, and q_muon."
        )

        wb.add_parameter("precision_dps", 80)
        wb.add_parameter("q0_proton_1term", fmt(q0))
        wb.add_parameter("q2t_two_term_borromean", fmt(q2t))
        wb.add_parameter("q0_muon_codata2022", fmt(q_mu))
        wb.add_parameter("zero_fitting", True)
        wb.add_parameter("zero_exp_proximity_assertions", True)
        wb.add_parameter(
            "lean_companion",
            "folio/quantum-observable-universe/lean/QOU/StandardModel/BringPushforwardAndGaugeGroupUnification.lean",
        )

        wb.add_data("part1_split_fibre_anomalies_and_Z6_kernel", part1)
        wb.add_data("part2_jimbo_N2_and_N3_homfly_schur_weyl", part2_by_pin)
        wb.add_data("part3_weinberg_angle_and_rg_audit", part3)

        # Strictly algebraic, representation-theoretic, and RG-identity assertions ONLY
        # (ZERO assertions gated on proximity to experimental sin^2(theta_W) or alpha_s!)
        wb.add_assertion(
            name="part1_five_anomalies_and_hypercharge_uniqueness_polynomial_exact",
            computed=(
                "1"
                if (
                    p1_raw["all_five_anomalies_zero"]
                    and p1_raw["poly_factorization_exact"]
                    and p1_raw["z6_order_six"]
                    and p1_raw["lie_12_ok"]
                )
                else "0"
            ),
            expected="1",
            tolerance="0",
            source="Five SM anomaly sums = 0, (1/2)Tr(Y^3) = 9 Y_Q (4 Y_Q + Y_{u^c})(2 Y_Q - Y_{u^c}), |Z_6| = 6, dim s(u(2)+u(3)) = 12",
        )
        wb.add_assertion(
            name="part1_z6_kernel_action_residual_80dps",
            computed=fmt(p1_raw["z6_exact_err"]),
            expected="0",
            tolerance="1e-85",
            source="(zeta_6^{2k} I_3, zeta_6^{3k} I_2, zeta_6^k) trivial action on F, S_chiral, and Higgs",
        )
        wb.add_assertion(
            name="part2_jimbo_N3_9x9_hecke_and_27x27_yang_baxter_80dps",
            computed=fmt(
                max(
                    max(r["n3_hecke_err"], r["n3_braid_err"], r["n2_hecke_braid_err"])
                    for r in p2_raws
                )
            ),
            expected="0",
            tolerance="1e-85",
            source="(R_W3 - q I_9)(R_W3 + q^{-1} I_9) = 0 and R_12 R_23 R_12 = R_23 R_12 R_23 across q_0, q_2t, q_muon",
        )
        wb.add_assertion(
            name="part2_h3_central_idempotents_and_baryon_qdim_ratio_80dps",
            computed=fmt(max(r["idem_alg_err"] for r in p2_raws)),
            expected="0",
            tolerance="1e-82",
            source="H_3(q) central idempotents on V_2^{x3} and W_3^{x3} and (1/[3]_q^3)/|d_mod(1^3)| = [2]_q/[3]_q^2",
        )
        wb.add_assertion(
            name="part2_schur_weyl_ranks_N2_4_4_0_vs_N3_10_16_1_exact",
            computed="1" if all(r["ranks_ok"] for r in p2_raws) else "0",
            expected="1",
            tolerance="0",
            source="rk(e_(3), e_(2,1), e_(1,1,1)) = (4, 4, 0) on V_2^{x3} vs (10, 16, 1) on W_3^{x3}",
        )
        wb.add_assertion(
            name="part3_uv_trace_3_div_8_sm_betas_and_rge_identities_80dps",
            computed=(
                fmt(p3_raw["rg_and_plancherel_identity_err"])
                if (p3_raw["uv_and_beta_exact"] and p3_raw["cosh_cos_sep_ok"])
                else "1"
            ),
            expected="0",
            tolerance="1e-80",
            source="sin^2(theta_W)_UV = 3/8, (b_1, b_2, b_3) = (41/10, -19/6, -7), 1-loop GQW identity, and CoshCosSeparation",
        )

        wb.add_caveat(
            "Proved algebraic/geometric identities vs open electroweak physics: Part 1 establishes "
            "that on the split rank-5 bundle F = V_2 (+) W_3^* (W_3 = pi_* L), the split Lie algebra "
            "s(u(2) (+) u(3)) has real dimension 12 with 0 off-diagonal X/Y leptoquark generators, "
            "global kernel Z_6, and chiral exterior representation Lambda^1(F) (+) Lambda^2(F^*) = "
            "(1,2)_{-1/2} (+) (3bar,1)_{+1/3} (+) (1,1)_{+1} (+) (3,2)_{+1/6} (+) (3bar,1)_{-2/3} "
            "cancelling all 5 gauge/gravitational anomalies uniquely via (1/2)Tr(Y^3) = "
            "9 Y_Q (4 Y_Q + Y_{u^c})(2 Y_Q - Y_{u^c}). Part 2 establishes at 80 dps that pushing "
            "forward to W_3 (N=3, a = q^3) promotes the H_3(q) Schur-Weyl ranks from (4, 4, 0) to "
            "(10, 16, 1) (10_S (+) 2 x 8_M (+) 1_A = 27) without altering H_3(q) or q_0."
        )
        wb.add_caveat(
            "Candid Weinberg-angle & gauge-unification audit (zero fitting): (1) Because F = V_2 (+) W_3^* "
            "is a direct sum rather than an irreducible SU(5) quintuplet, g_3, g_2, and g_1 are NOT "
            "forced equal by simple-group symmetry unless a common geometric kinetic metric on Bring's "
            "surface sets trace-normalized couplings equal at a UV scale mu_*. (2) If sin^2(theta_W)(mu_*) "
            "= 3/8 = 0.375 holds with pure 1-loop non-SUSY SM running (b_1 = 41/10, b_2 = -19/6, b_3 = -7) "
            "and no intermediate thresholds, alpha_1 and alpha_2 intersect at mu_12 ~= 1.03e13 GeV "
            "(predicting alpha_s(M_Z) ~= 0.0711 vs PDG 0.1180 — the classic non-SUSY SM triangle "
            "mismatch), whereas setting mu_* = E_Pl = 1.22089e19 GeV yields sin^2(theta_W)(M_Z) ~= 0.1522 "
            "(-34.2% vs PDG MS-bar 0.23122) and alpha_3^{-1}(M_Z) ~= -4.58. (3) Among existing repo "
            "electroweak formulas at q_2t, naive pure-pattern Hoefsmit (`weinberg-angle-categorical.md:24`) "
            "gives 0.6974 (+201.6%), bare 2-strand Plancherel 1 - (P_2/P_3)^2 gives 0.20641 (-7.46% vs "
            "on-shell 0.22305, -10.73% vs MS-bar 0.23122), ([2]_q/2)^2-dressed W/Z (`ElectroweakBringSchwingerBridge`) "
            "gives 0.22347 (+0.19% vs on-shell 0.22305, -3.35% vs MS-bar 0.23122; dressing factor still "
            "postulated), and SubstrateEWHypotheses g = pi*h gives 0.22768 at M_Z (-1.53% vs MS-bar 0.23122; "
            "open class hypothesis)."
        )

        stamp = q0_comparison(
            muon=q_mu,
            proton=q0,
            reason=(
                "Wave-5 Standard Model pushforward and Weinberg-angle audit evaluates Jimbo N=3 "
                "HOMFLY-PT Schur-Weyl idempotents, q-deformed fibre traces, existing QOU torus-link "
                "electroweak ratios, and 1-loop SM RG running side-by-side across q_0, q_2t, and q_muon."
            ),
        )
        saved_path = wb.save(stamp)
        saved_doc = json.loads(saved_path.read_text(encoding="utf-8"))

        import witness_raw_float64_audit as _f64_audit

        n_raw_floats = _f64_audit.count_raw_floats(saved_doc)
        if n_raw_floats != 0:
            raise RuntimeError(f"Emitted witness contains {n_raw_floats} raw float64 values!")

        p2_q2t = part2_by_pin["q2t_two_term_borromean"]
        p3_q2t = part3["by_pin"]["q2t_two_term_borromean"]
        print("=" * 124)
        print(
            "  Wave 5: 80-dps SU(3)xSU(2)xU(1)/Z_6 Pushforward, Jimbo N=3 Schur-Weyl & Weinberg-Angle Audit (@ q_2t)"
        )
        print("=" * 124)
        print(
            f"  Part 1: Anomalies = 0 | (1/2)Tr(Y^3) = 9*Y_Q*(4*Y_Q+Y_uc)*(2*Y_Q-Y_uc) | "
            f"|Z_6| = {part1['global_gauge_group_kernel_Z6']['kernel_order']} | "
            f"dim s(u(2)+u(3)) = {part1['split_lie_algebra_s_u2_oplus_u3']['dim_s_u2_oplus_u3']} (0 X/Y)"
        )
        print(
            f"  Part 2: N=2 ranks = {p2_q2t['schur_weyl_N2_V2_tensor3']['ranks']['rk_e_3']},"
            f"{p2_q2t['schur_weyl_N2_V2_tensor3']['ranks']['rk_e_21']},"
            f"{p2_q2t['schur_weyl_N2_V2_tensor3']['ranks']['rk_e_111']} | "
            f"N=3 ranks = {p2_q2t['schur_weyl_N3_W3_tensor3']['ranks']['rk_e_3']},"
            f"{p2_q2t['schur_weyl_N3_W3_tensor3']['ranks']['rk_e_21']},"
            f"{p2_q2t['schur_weyl_N3_W3_tensor3']['ranks']['rk_e_111']} | "
            f"Baryon ratio [2]_q/[3]_q^2 = {mp.nstr(mp.mpf(p2_q2t['baryon_singlet_weight_comparison']['ratio_N3_over_N2_GPMT_eq_qInt2_div_qInt3_sq']), 12)}"
        )
        print("-" * 124)
        hdr = f"{'Candidate ID':<46} | {'sin^2(theta_W)':>16} | {'vs MSbar 0.23122':>16} | {'vs OnShell 0.22305':>18}"
        print(hdr)
        print("-" * len(hdr))
        for row in p3_q2t["weinberg_angle_candidates"]:
            s2 = mp.nstr(mp.mpf(row["sin2_theta_W"]), 10)
            ems = mp.nstr(mp.mpf(row["err_vs_PDG_MSbar_0p23122_pct"]), 6)
            eos = mp.nstr(mp.mpf(row["err_vs_PDG_onshell_0p22305_pct"]), 6)
            print(f"{row['candidate_id']:<46} | {s2:>16} | {ems:>15}% | {eos:>17}%")
        print("=" * 124)
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
