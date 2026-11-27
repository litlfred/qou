#!/usr/bin/env python3
"""Pre-registered 80-dps evaluation of the canonical Fefferman-Lee 4D Lorentzian CR
circle-bundle metric g_theta (signature (3,1)), full Cartan moving-frame Riemann/Ricci/
Einstein/Weyl curvature across S^3, Heisenberg H^1, and Bring UT(Sigma_4), and the
Bisognano-Wichmann + Jacobson-Raychaudhuri (2*pi)/(8*pi) = 1/4 modular horizon law across
both QOU substrate gravitational normalizations (Arm N1: G_q*(hbar_q/c_q)^2 = 1 vs
Arm N2: hbar_q*G_q/c_q^3 = q_0).

Closing Open Gap 4 (Option 4A), stacked on `claude/reeb-length-time-bh-lcq-20261123`
(PR #9240, Issue #9239, Bean `qou-slfm`), paired with Lean 4 formalization
`folio/quantum-observable-universe/lean/QOU/GravitySpacetime/FeffermanLorentzianHorizonEntropy.lean`.
Pre-registered in `PREREGISTRATION.md` (commit `edf9f174ae4decbb7a8f702d554ab3fcf8f592b6`)
BEFORE writing or running this script.

Precision & anti-fit discipline (STRICT):
  - `mpmath` at `workdps = 80` (`OUT_DPS = 70` serialized into witness),
  - `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`),
  - ZERO `float64` imports, literals, or casts anywhere in the script or witness,
  - `selectedCandidate = "none"` (side-by-side reporting of Arm N1 vs Arm N2 and
    curvature diagnostics with zero parameter tuning).

Reproduce:
    python3 -u computations/probes/gap4_fefferman_lorentzian_bh_quarter/gap4_fefferman_lorentzian_bh_quarter_probe.py
"""

from __future__ import annotations

import os as _os
import sys as _sys
from itertools import permutations as _permutations
from pathlib import Path as _Path

_os.environ.setdefault("QOU_COMPUTE_DPS", "80")
_os.environ.setdefault("QOU_OUTPUT_DPS", "70")

_ROOT = _Path(__file__).resolve().parents[3]
if str(_ROOT / "tools" / "qou-substrate" / "python") not in _sys.path:
    _sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))
if str(_ROOT / "computations") not in _sys.path:
    _sys.path.insert(0, str(_ROOT / "computations"))

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp  # noqa: E402

from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

WORK_DPS = 80
OUT_DPS = 70
PREREG_COMMIT = "edf9f174ae4decbb7a8f702d554ab3fcf8f592b6"


def det4_leibniz(mat: list[list[mp.mpf]]) -> mp.mpf:
    """Exact 4x4 Leibniz determinant over mpmath.mpf without float conversions."""
    total = mp.mpf(0)
    idx = (0, 1, 2, 3)
    for perm in _permutations(idx):
        inv_count = 0
        for i in range(4):
            for j in range(i + 1, 4):
                if perm[i] > perm[j]:
                    inv_count += 1
        sign = -mp.mpf(1) if (inv_count % 2 == 1) else mp.mpf(1)
        prod = mp.mpf(1)
        for r in range(4):
            prod *= mat[r][perm[r]]
        total += sign * prod
    return total


def mat4_mul(a: list[list[mp.mpf]], b: list[list[mp.mpf]]) -> list[list[mp.mpf]]:
    """4x4 matrix product over mpmath.mpf."""
    return [
        [sum(a[i][k] * b[k][j] for k in range(4)) for j in range(4)]
        for i in range(4)
    ]


def mat4_transpose(a: list[list[mp.mpf]]) -> list[list[mp.mpf]]:
    """4x4 matrix transpose."""
    return [[a[j][i] for j in range(4)] for i in range(4)]


def quad_form4(mat: list[list[mp.mpf]], u: list[mp.mpf], v: list[mp.mpf]) -> mp.mpf:
    """Bilinear evaluation sum_{i,j} u_i mat_{ij} v_j."""
    return sum(u[i] * mat[i][j] * v[j] for i in range(4) for j in range(4))


def fefferman_gram(c_r: mp.mpf, ell1: mp.mpf, ell2: mp.mpf) -> list[list[mp.mpf]]:
    """4x4 Gram matrix of g_theta in adapted basis (R_theta, partial_sigma, X_1, X_2)."""
    z = mp.mpf(0)
    one = mp.mpf(1)
    two = mp.mpf(2)
    return [
        [two * c_r, one, z, z],
        [one, z, z, z],
        [z, z, ell1, z],
        [z, z, z, ell2],
    ]


def sylvester_basis4(c_r: mp.mpf) -> list[list[mp.mpf]]:
    """Unimodular SL_4 basis P(c_R) satisfying P^T G_Feff P = diag(-1, 1, ell1, ell2)."""
    z = mp.mpf(0)
    one = mp.mpf(1)
    half = one / mp.mpf(2)
    return [
        [half, half, z, z],
        [-(half * c_r + one), -(half * c_r - one), z, z],
        [z, z, one, z],
        [z, z, z, one],
    ]


def cartan_fefferman_curvature(
    r_w: mp.mpf, lam0: mp.mpf, c_r: mp.mpf
) -> dict[str, object]:
    """Compute exact 80-dps Cartan moving-frame Levi-Civita connection, Riemann, Ricci,
    scalar, Einstein, and Weyl tensors of g = 2 E^0 E^1 + (E^2)^2 + (E^3)^2 on C(M^3)
    for a constant-Webster-curvature Sasakian CR 3-manifold M^3 (Webster scalar R_W).

    Coframe on C(M^3):
      E^0 = theta,   E^1 = lam0*(dgamma - phi) + c_R*theta,   (E^2, E^3) unitary CR coframe
      d(E^0) = E^2 ^ E^3
      d(E^1) = (lam0 * R_W + c_R) * (E^2 ^ E^3)
      d(E^2) = Psi ^ E^3,   d(E^3) = -Psi ^ E^2   with Psi = -(1/lam0)*E^1 + (c_R/lam0)*E^0.
    """
    z = mp.mpf(0)
    one = mp.mpf(1)
    two = mp.mpf(2)
    six = mp.mpf(6)

    g = [
        [z, one, z, z],
        [one, z, z, z],
        [z, z, one, z],
        [z, z, z, one],
    ]
    # Since g^2 = I_4, g^{-1} = g identically:
    ginv = g

    c_struct = [[[z for _ in range(4)] for _ in range(4)] for _ in range(4)]

    def add_wedge(a: int, b: int, c: int, val: mp.mpf) -> None:
        c_struct[a][b][c] += val
        c_struct[a][c][b] -= val

    add_wedge(0, 2, 3, one)
    add_wedge(1, 2, 3, lam0 * r_w + c_r)
    add_wedge(2, 1, 3, -one / lam0)
    add_wedge(2, 0, 3, c_r / lam0)
    add_wedge(3, 1, 2, one / lam0)
    add_wedge(3, 0, 2, -c_r / lam0)

    c_low = [
        [
            [sum(g[a][d] * c_struct[d][b][c] for d in range(4)) for c in range(4)]
            for b in range(4)
        ]
        for a in range(4)
    ]

    # Koszul formula for [E_b, E_c] = -C^a_{bc} E_a:
    gamma_low = [
        [
            [(-c_low[a][c][b] + c_low[c][b][a] - c_low[b][a][c]) / two for b in range(4)]
            for c in range(4)
        ]
        for a in range(4)
    ]
    gamma = [
        [
            [sum(ginv[a][d] * gamma_low[d][c][b] for d in range(4)) for b in range(4)]
            for c in range(4)
        ]
        for a in range(4)
    ]

    max_torsion_or_metric_res = z
    for a in range(4):
        for b in range(4):
            for c in range(4):
                tor = abs((gamma[a][c][b] - gamma[a][b][c]) + c_struct[a][c][b])
                met = abs(gamma_low[a][c][b] + gamma_low[b][c][a])
                max_torsion_or_metric_res = max(max_torsion_or_metric_res, tor, met)

    riem = [
        [[[z for _ in range(4)] for _ in range(4)] for _ in range(4)]
        for _ in range(4)
    ]
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    val = sum(
                        gamma[a][c][e] * gamma[e][d][b] - gamma[a][d][e] * gamma[e][c][b]
                        for e in range(4)
                    )
                    val += sum(c_struct[e][c][d] * gamma[a][e][b] for e in range(4))
                    riem[a][b][c][d] = val

    ric = [
        [sum(riem[a][b][a][d] for a in range(4)) for d in range(4)]
        for b in range(4)
    ]
    scal = sum(ginv[b][d] * ric[b][d] for b in range(4) for d in range(4))
    ein = [
        [ric[b][d] - (scal / two) * g[b][d] for d in range(4)]
        for b in range(4)
    ]

    riem_low = [
        [
            [
                [sum(g[a][e] * riem[e][b][c][d] for e in range(4)) for d in range(4)]
                for c in range(4)
            ]
            for b in range(4)
        ]
        for a in range(4)
    ]

    max_weyl_abs = z
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    s_part = (
                        g[a][c] * ric[b][d]
                        - g[a][d] * ric[b][c]
                        - g[b][c] * ric[a][d]
                        + g[b][d] * ric[a][c]
                    ) / two
                    scal_part = scal * (g[a][c] * g[b][d] - g[a][d] * g[b][c]) / six
                    w_abcd = riem_low[a][b][c][d] - s_part + scal_part
                    max_weyl_abs = max(max_weyl_abs, abs(w_abcd))

    return {
        "g": g,
        "ric": ric,
        "scal": scal,
        "ein": ein,
        "max_torsion_or_metric_res": max_torsion_or_metric_res,
        "max_weyl_abs": max_weyl_abs,
    }


def main() -> int:
    set_compute_dps(WORK_DPS)
    with mp.workdps(WORK_DPS):
        q0 = q_at(WORK_DPS)
        z = mp.mpf(0)
        one = mp.mpf(1)
        two = mp.mpf(2)
        three = mp.mpf(3)
        four = mp.mpf(4)
        six = mp.mpf(6)
        eight = mp.mpf(8)
        quarter = one / four
        pi_mp = mp.pi

        # Substrate Layer-I / gravitational quantities at q_0 (proton pin)
        q0_inv = one / q0
        hbar_q0 = one - q0_inv
        t_p_q0 = one / hbar_q0
        ell_p_circuit = hbar_q0 * t_p_q0
        c_q0 = one / (q0 - one)
        s_cell_q0 = ((q0 - one) ** 2) / (q0 ** 3)
        g_q0 = (c_q0 ** 3) * hbar_q0 / s_cell_q0

        ell_grav_sq_n1 = g_q0 * ((hbar_q0 / c_q0) ** 2)  # = 1
        ell_grav_sq_n2 = hbar_q0 * g_q0 / (c_q0 ** 3)    # = q_0

        # =====================================================================
        # Battery F1: Algebraic (3,1) Signature, SL_4 Congruence & Eigenvalues
        # =====================================================================
        signature_models: list[tuple[str, mp.mpf, mp.mpf, mp.mpf, str]] = [
            (
                "M0_heisenberg_flat",
                z,
                one,
                one,
                "Webster-flat CR Heisenberg H^1 (R_W = 0, c_R = 0, ell_1 = ell_2 = 1)",
            ),
            (
                "M1_cr_three_sphere_S3",
                two,
                one,
                one,
                "Round CR 3-sphere S^3 subset C^2 (R_W = +2, c_R = +1/3, ell_1 = ell_2 = 1)",
            ),
            (
                "M2_bring_ut_sigma4",
                -two,
                one,
                one,
                "Hyperbolic / Bring contact link UT(Sigma_4) (R_W = -2, c_R = -1/3, chi = -6)",
            ),
            (
                "M3_substrate_anisotropic_q0",
                -two * (q0_inv ** 2),
                q0_inv ** 2,
                q0_inv ** 2,
                "D_nabla q_0^-1 horizontal rescaled CR metric (R_W = -2 q_0^-2, ell_1 = ell_2 = q_0^-2)",
            ),
        ]

        f1_rows: dict[str, dict[str, str]] = {}
        max_f1_res = z
        all_3_1_signs_ok = True

        for key, r_w_val, ell1, ell2, desc in signature_models:
            c_r_val = r_w_val / six
            g_mat = fefferman_gram(c_r_val, ell1, ell2)
            p_mat = sylvester_basis4(c_r_val)
            det_g = det4_leibniz(g_mat)
            det_p = det4_leibniz(p_mat)
            det_g_expected = -(ell1 * ell2)

            cong = mat4_mul(mat4_mul(mat4_transpose(p_mat), g_mat), p_mat)
            diag_target = [
                [-one, z, z, z],
                [z, one, z, z],
                [z, z, ell1, z],
                [z, z, z, ell2],
            ]
            cong_res = max(
                abs(cong[i][j] - diag_target[i][j]) for i in range(4) for j in range(4)
            )

            # Exact eigenvalues of upper-left 2x2 block [[2 c_R, 1], [1, 0]]:
            lam_minus = c_r_val - mp.sqrt((c_r_val ** 2) + one)
            lam_plus = c_r_val + mp.sqrt((c_r_val ** 2) + one)
            eig_prod_res = abs((lam_minus * lam_plus) + one)
            eig_sum_res = abs((lam_minus + lam_plus) - two * c_r_val)

            if not (lam_minus < z and lam_plus > z and ell1 > z and ell2 > z and det_g < z):
                all_3_1_signs_ok = False

            # Null vectors: fibreVec = [0, 1, 0, 0], reebVec = [1, 0, 0, 0], k_+ = [1, -c_R, 0, 0]
            v_fib = [z, one, z, z]
            v_reeb = [one, z, z, z]
            v_kplus = [one, -c_r_val, z, z]
            null_res = max(
                abs(quad_form4(g_mat, v_fib, v_fib)),
                abs(quad_form4(g_mat, v_reeb, v_fib) - one),
                abs(quad_form4(g_mat, v_reeb, v_reeb) - two * c_r_val),
                abs(quad_form4(g_mat, v_kplus, v_kplus)),
                abs(quad_form4(g_mat, v_kplus, v_fib) - one),
            )

            max_f1_res = max(
                max_f1_res,
                abs(det_g - det_g_expected),
                abs(det_p - one),
                cong_res,
                eig_prod_res,
                eig_sum_res,
                null_res,
            )

            f1_rows[key] = {
                "description": desc,
                "R_W": fmt(r_w_val, dps=OUT_DPS),
                "c_R_lee_shift": fmt(c_r_val, dps=OUT_DPS),
                "det_fefferman_gram": fmt(det_g, dps=OUT_DPS),
                "det_sylvester_P": fmt(det_p, dps=OUT_DPS),
                "sylvester_congruence_max_res": fmt(cong_res, dps=OUT_DPS),
                "eigenvalue_timelike_neg": fmt(lam_minus, dps=OUT_DPS),
                "eigenvalue_spacelike_1": fmt(lam_plus, dps=OUT_DPS),
                "eigenvalue_spacelike_2": fmt(ell1, dps=OUT_DPS),
                "eigenvalue_spacelike_3": fmt(ell2, dps=OUT_DPS),
            }

        reeb_lock_res = abs(ell_p_circuit - one)
        max_f1_res = max(max_f1_res, reeb_lock_res)

        # Bring surface topological Gauss-Bonnet invariants (g_Bring = 4):
        genus_bring = 4
        chi_bring = 2 - 2 * genus_bring  # -6
        hyperbolic_area_bring = mp.mpf(-chi_bring) * two * pi_mp  # 12 * pi

        # =====================================================================
        # Battery F2: Sparling-Graham-Lee Cartan Curvature, Weyl=0, & Ricci_kk
        # =====================================================================
        lam0_canonical = one / three
        f2_rows: dict[str, dict[str, str]] = {}
        max_f2_weyl_and_decomp_res = z
        min_unshifted_weyl_norm_nonzero_rw = mp.mpf("1e9")
        all_null_cone_nonneg = True
        all_fibre_ricci_half = True

        # 6 exact 4D null rays k = [k0, k1, k2, k3] satisfying 2*k0*k1 + k2^2 + k3^2 = 0:
        null_rays: list[list[mp.mpf]] = [
            [z, one, z, z],                                      # S^1 fibre generator K = partial_sigma
            [one, z, z, z],                                      # Lifted Reeb null generator E_0
            [one, -(one / two), one, z],                         # Tilted horizontal ray 1
            [one, -(mp.mpf(5) / two), one, two],                 # Tilted horizontal ray 2
            [mp.mpf(3), -(mp.mpf(13) / six), two, three],        # General 4-component null ray
            [q0, -one / (two * q0), one, z],                     # Substrate-tilted null ray at q_0
        ]

        for key, r_w_val, _ell1, _ell2, _desc in signature_models:
            c_r_lee = r_w_val / six
            curv = cartan_fefferman_curvature(r_w_val, lam0_canonical, c_r_lee)
            g0 = curv["g"]
            ric = curv["ric"]
            scal = curv["scal"]
            ein = curv["ein"]
            tor_met_res = curv["max_torsion_or_metric_res"]
            weyl_max = curv["max_weyl_abs"]

            # Contrast: omit Lee's R_W/6 shift (set c_R = 0) and check Weyl tensor!
            curv_unshifted = cartan_fefferman_curvature(r_w_val, lam0_canonical, z)
            weyl_unshifted = curv_unshifted["max_weyl_abs"]
            if abs(r_w_val) > mp.mpf("1e-30"):
                min_unshifted_weyl_norm_nonzero_rw = min(
                    min_unshifted_weyl_norm_nonzero_rw, weyl_unshifted
                )

            # Check Sparling-Graham R_{ab} K^a K^b = 1/2 along fibre K = [0, 1, 0, 0]
            v_fib = [z, one, z, z]
            ric_kk_fib = quad_form4(ric, v_fib, v_fib)
            if abs(ric_kk_fib - (one / two)) > mp.mpf("1e-74"):
                all_fibre_ricci_half = False

            # Check rank-1 wave decomposition: G_{ab} + (R_W/4) g_{ab} = (1/2) xi_a xi_b
            xi = [-r_w_val / two, one, z, z]
            rank1_res = max(
                abs(
                    (ein[a][b] + (r_w_val / four) * g0[a][b])
                    - (one / two) * xi[a] * xi[b]
                )
                for a in range(4)
                for b in range(4)
            )
            scal_res = abs(scal - (three * r_w_val / two))

            # Check null-cone Raychaudhuri identity across all 6 null rays
            max_null_ray_res = z
            for k_vec in null_rays:
                null_check = abs(
                    two * k_vec[0] * k_vec[1] + (k_vec[2] ** 2) + (k_vec[3] ** 2)
                )
                ric_kk = quad_form4(ric, k_vec, k_vec)
                ein_kk = quad_form4(ein, k_vec, k_vec)
                expected_kk = (one / two) * ((k_vec[1] - (r_w_val / two) * k_vec[0]) ** 2)
                max_null_ray_res = max(
                    max_null_ray_res,
                    null_check,
                    abs(ric_kk - expected_kk),
                    abs(ein_kk - expected_kk),
                )
                if ric_kk < -mp.mpf("1e-75"):
                    all_null_cone_nonneg = False

            max_f2_weyl_and_decomp_res = max(
                max_f2_weyl_and_decomp_res,
                tor_met_res,
                weyl_max,
                rank1_res,
                scal_res,
                max_null_ray_res,
            )

            f2_rows[key] = {
                "R_W": fmt(r_w_val, dps=OUT_DPS),
                "scalar_curvature_3RW_over_2": fmt(scal, dps=OUT_DPS),
                "Ric_00_reeb_null": fmt(ric[0][0], dps=OUT_DPS),
                "Ric_01_mixed": fmt(ric[0][1], dps=OUT_DPS),
                "Ric_11_fibre_killing": fmt(ric[1][1], dps=OUT_DPS),
                "Ric_22_levi_horiz": fmt(ric[2][2], dps=OUT_DPS),
                "weyl_linf_with_lee_lock": fmt(weyl_max, dps=OUT_DPS),
                "weyl_linf_without_lee_shift_cR0": fmt(weyl_unshifted, dps=30),
                "einstein_rank1_wave_decomp_max_res": fmt(rank1_res, dps=OUT_DPS),
                "null_cone_raychaudhuri_max_res": fmt(max_null_ray_res, dps=OUT_DPS),
            }

        # =====================================================================
        # Battery F3: Modular-Raychaudhuri (2*pi)/(8*pi) = 1/4 & Dual Arms N1/N2
        # =====================================================================
        # Test invariance across multiple (kappa, dA) horizon variations
        test_pairs = [
            (one, one),
            (mp.mpf(7) / mp.mpf(3), mp.mpf(19) / mp.mpf(5)),
            (q0, pi_mp),
        ]
        max_f3_modular_res = z
        for kappa_val, da_val in test_pairs:
            accel_val = c_q0 * kappa_val
            # Arm N1: G_eff such that hbar_q * G_eff / c_q^3 = ell_grav_sq_n1 = 1
            # (i.e. native def:gravitational-constant Planck area = 1)
            g_eff_n1 = (c_q0 ** 3) * ell_grav_sq_n1 / hbar_q0  # = q_0^-1 * G_q0
            tu_accel = (hbar_q0 * accel_val) / (two * pi_mp * c_q0)
            tu_surf = (hbar_q0 * kappa_val) / (two * pi_mp)
            dq_n1_accel = ((c_q0 ** 2) * accel_val / (eight * pi_mp * g_eff_n1)) * da_val
            dq_n1_surf = ((c_q0 ** 3) * kappa_val / (eight * pi_mp * g_eff_n1)) * da_val
            ds_over_da_n1 = (dq_n1_accel / tu_accel) / da_val

            # Arm N2: Direct substitution of native G_q0 (where hbar_q0 * G_q0 / c_q0^3 = q_0)
            dq_n2_accel = ((c_q0 ** 2) * accel_val / (eight * pi_mp * g_q0)) * da_val
            dq_n2_surf = ((c_q0 ** 3) * kappa_val / (eight * pi_mp * g_q0)) * da_val
            ds_over_da_n2 = (dq_n2_accel / tu_accel) / da_val

            max_f3_modular_res = max(
                max_f3_modular_res,
                abs(tu_accel - tu_surf),
                abs(dq_n1_accel - dq_n1_surf),
                abs(dq_n2_accel - dq_n2_surf),
                abs(ds_over_da_n1 - quarter),
                abs(ds_over_da_n2 - (one / (four * q0))),
            )

        density_arm_n1 = one / (four * ell_grav_sq_n1)     # = 1/4 = 0.25
        density_arm_n2 = one / (four * ell_grav_sq_n2)     # = 1/(4*q_0) = 0.22522957...
        arm_n2_over_n1 = density_arm_n2 / density_arm_n1   # = q_0^-1 = hbar_q0 * c_q0
        arm_n2_rel_diff_vs_quarter = (density_arm_n2 - quarter) / quarter  # = -hbar_q0

        dual_split_identity_res = max(
            abs(density_arm_n1 - quarter),
            abs(density_arm_n2 - (one / (four * q0))),
            abs(arm_n2_over_n1 - (hbar_q0 * c_q0)),
            abs(arm_n2_over_n1 - q0_inv),
            abs(arm_n2_rel_diff_vs_quarter + hbar_q0),
        )
        max_f3_modular_res = max(max_f3_modular_res, dual_split_identity_res)

        # Corresponding puncture area ratios in unit Reeb-circuit cells (ell_P(q_0)^2 = 1):
        s_cat = mp.log(two)
        q2_q0 = q0 + q0_inv
        s_tl_q2 = mp.log(q2_q0)
        p_plus = (q0 ** 2) / (one + q0 ** 2)
        p_minus = one / (one + q0 ** 2)
        s_haar = -(p_plus * mp.log(p_plus) + p_minus * mp.log(p_minus))

        a0_n1_cat = four * s_cat
        a0_n1_tl = four * s_tl_q2
        a0_n1_haar = four * s_haar

        a0_n2_sub_cat = four * q0 * s_cat
        a0_n2_sub_tl = four * q0 * s_tl_q2
        a0_n2_sub_haar = four * q0 * s_haar

        # =====================================================================
        # Build 80-dps Witness JSON
        # =====================================================================
        wb = WitnessBuilder(
            "gap4-fefferman-lorentzian-bh-quarter",
            engine="mpmath",
            output_dir=_Path(__file__).resolve().parent,
        )
        wb.set_description(
            "Pre-registered 80-dps (70-dps serialized) evaluation of the canonical Fefferman-Lee "
            "4D Lorentzian CR circle-bundle metric g_theta (signature (3,1), SL_4 Sylvester "
            "congruence, null pairing), full Cartan moving-frame Riemann/Ricci/Einstein/Weyl "
            "curvature on S^3, Heisenberg H^1, and Bring UT(Sigma_4) (confirming Weyl = 0 under "
            "Lee's c_R = R_W/6 lock, Sparling-Graham vacuum obstruction Ric(K,K) = 1/2, and "
            "rank-1 null-energy positivity Ric(k,k) >= 0), and the (2*pi)/(8*pi) = 1/4 modular "
            "horizon law across both QOU gravitational normalizations (Arm N1: 1/4 = 0.25 vs "
            "Arm N2: 1/(4*q_0) = 0.22522957..., shift -hbar_{q_0} = -9.908%)."
        )
        wb.set_content_block("cr-structure-lorentzian-lift")
        wb.add_parameter("q0", fmt(q0, dps=OUT_DPS))
        wb.add_parameter("q0_pin", "proton (qou_substrate.constants.q_at)")
        wb.add_parameter("work_dps", WORK_DPS)
        wb.add_parameter("output_dps", OUT_DPS)
        wb.add_parameter("preregistration_commit", PREREG_COMMIT)
        wb.add_parameter("selectedCandidate", "none")

        wb.add_data(
            "battery_f1_fefferman_lorentzian_signature",
            {
                "normalised_reeb_circuit_ell_P": fmt(ell_p_circuit, dps=OUT_DPS),
                "bring_surface_genus": genus_bring,
                "bring_surface_euler_characteristic": chi_bring,
                "bring_surface_hyperbolic_area_12pi": fmt(hyperbolic_area_bring, dps=OUT_DPS),
                "models": f1_rows,
                "max_algebraic_signature_residual": fmt(max_f1_res, dps=OUT_DPS),
            },
        )

        wb.add_data(
            "battery_f2_sparling_graham_lee_curvature",
            {
                "canonical_lee_lambda0": fmt(lam0_canonical, dps=OUT_DPS),
                "models": f2_rows,
                "min_unshifted_weyl_norm_for_nonzero_RW": fmt(
                    min_unshifted_weyl_norm_nonzero_rw, dps=30
                ),
                "max_weyl_and_rank1_decomposition_residual": fmt(
                    max_f2_weyl_and_decomp_res, dps=OUT_DPS
                ),
            },
        )

        wb.add_data(
            "battery_f3_modular_raychaudhuri_dual_normalizations",
            {
                "arm_N1_native_planck_ell_grav_sq": fmt(ell_grav_sq_n1, dps=OUT_DPS),
                "arm_N1_entropy_density_dS_over_dA_sub": fmt(density_arm_n1, dps=OUT_DPS),
                "arm_N1_rel_diff_vs_quarter": fmt(
                    (density_arm_n1 - quarter) / quarter, dps=OUT_DPS
                ),
                "arm_N1_required_a0_catalan_4ln2": fmt(a0_n1_cat, dps=OUT_DPS),
                "arm_N1_required_a0_tl_4ln_q2": fmt(a0_n1_tl, dps=OUT_DPS),
                "arm_N1_required_a0_haar_4s_haar": fmt(a0_n1_haar, dps=OUT_DPS),
                "arm_N2_relativistic_ell_grav_sq_hbar_G_over_c3": fmt(
                    ell_grav_sq_n2, dps=OUT_DPS
                ),
                "arm_N2_entropy_density_per_relativistic_cell": fmt(quarter, dps=OUT_DPS),
                "arm_N2_entropy_density_per_unit_reeb_cell_1_over_4q0": fmt(
                    density_arm_n2, dps=OUT_DPS
                ),
                "arm_N2_over_arm_N1_ratio_hbar_q0_mul_c_q0": fmt(
                    arm_n2_over_n1, dps=OUT_DPS
                ),
                "arm_N2_rel_diff_vs_quarter_minus_hbar_q0": fmt(
                    arm_n2_rel_diff_vs_quarter, dps=OUT_DPS
                ),
                "arm_N2_sub_required_a0_catalan_4q0_ln2": fmt(a0_n2_sub_cat, dps=OUT_DPS),
                "arm_N2_sub_required_a0_tl_4q0_ln_q2": fmt(a0_n2_sub_tl, dps=OUT_DPS),
                "arm_N2_sub_required_a0_haar_4q0_s_haar": fmt(a0_n2_sub_haar, dps=OUT_DPS),
                "max_modular_cancellation_and_dual_split_residual": fmt(
                    max_f3_modular_res, dps=OUT_DPS
                ),
            },
        )

        wb.add_assertion(
            "f1_fefferman_lorentzian_3_1_signature_congruence_and_null_pairing_exact",
            computed=fmt(max_f1_res, dps=OUT_DPS) if all_3_1_signs_ok else "1",
            expected="0",
            tolerance="1e-74",
            source="FeffermanLorentzianHorizonEntropy §1: det G_Feff = -ell_1 ell_2 < 0, "
                   "SL_4 congruence P^T G_Feff P = diag(-1, 1, ell_1, ell_2), eigenvalues (3+, 1-), "
                   "and nullity g(partial_sigma, partial_sigma) = g(k_+, k_+) = 0 across M0..M3.",
        )
        wb.add_assertion(
            "f2_lee_conformal_flatness_weyl_zero_and_rank1_einstein_wave_exact",
            computed=fmt(max_f2_weyl_and_decomp_res, dps=OUT_DPS),
            expected="0",
            tolerance="1e-74",
            source="FeffermanLorentzianHorizonEntropy §2: Cartan moving-frame Weyl W_{abcd} = 0 "
                   "at Lee lock c_R = R_W/6, Einstein + (R_W/4) g = (1/2) xi (x) xi, and null-cone "
                   "Ric(k,k) = (1/2)(k_1 - (R_W/2) k_0)^2 across S^3, H^1, and Bring UT(Sigma_4).",
        )
        wb.add_assertion(
            "f2_sparling_graham_vacuum_obstruction_and_unshifted_weyl_nonzero",
            computed="1"
            if (
                all_fibre_ricci_half
                and all_null_cone_nonneg
                and min_unshifted_weyl_norm_nonzero_rw > mp.mpf("0.15")
            )
            else "0",
            expected="1",
            source="Sparling-Graham vacuum obstruction: Ric(K,K) = 1/2 != 0 along null Killing "
                   "fibre K = partial_sigma (ruling out vacuum Ric = Lambda g), and omitting Lee's "
                   "c_R = R_W/6 shift yields nonzero Weyl curvature (> 0.15 on S^3, UT(Sigma_4), M3).",
        )
        wb.add_assertion(
            "f3_modular_raychaudhuri_quarter_cancellation_and_dual_q0_split_exact",
            computed=fmt(max_f3_modular_res, dps=OUT_DPS),
            expected="0",
            tolerance="1e-74",
            source="FeffermanLorentzianHorizonEntropy §3: (dQ/T_U)/dA = 1/(4 ell_grav^2) with "
                   "Arm N1 = 1/4 = 0.25 exact and Arm N2 = 1/(4 q_0) = 0.22522957..., relative "
                   "shift -(1 - q_0^-1) = -hbar_{q_0} = -9.90817160%.",
        )

        wb.add_caveat(
            "Fefferman's canonical CR circle-bundle metric g_theta constructs an explicit, "
            "zero-parameter 4D Lorentzian (3,1) metric lift on C(M^3) -> M^3 with conformally "
            "flat geometry (W_{abcd} = 0 on S^3, H^1, and Bring UT(Sigma_4)) and universal "
            "null-focusing sign Ric(k,k) = (1/2)(k_1 - (R_W/2) k_0)^2 >= 0, closing the "
            "kinematical Lorentzian-lift gap in cr-structure-lorentzian-lift.md. Two dynamical/"
            "normalization items remain open in Rule-13a class FeffermanDynamicalEinsteinHorizonConjecture: "
            "(1) g_theta has intrinsic twist curvature Ric(K,K) = 1/2 (not vacuum Ricci-flat), so "
            "Jacobson's dynamical perturbation law delta R_{kk} = (8*pi*G/c^4) delta T_{kk} still "
            "requires an induced-Einstein / spectral-action derivation from QOU's q-Yang-Mills-Levi "
            "action; and (2) QOU's two substrate Planck normalizations give exact 1/4 = 0.25 under "
            "Arm N1 (G_q(hbar_q/c_q)^2 = 1) vs 1/(4*q_0) = 0.22522957... (-9.9082% = -hbar_{q_0}) "
            "per unit Reeb-circuit area cell under Arm N2 (hbar_q*G_q/c_q^3 = q_0)."
        )

        out_path = wb.save({"q0Anchor": "proton", "workdps": WORK_DPS})

        print("=== 80-dps Gap 4: Fefferman 4D Lorentzian Metric & Modular 1/4 Horizon Probe ===")
        print(f"q_0 (proton, 80 dps)                 = {fmt(q0, dps=50)}")
        print(f"ell_P(q_0) = hbar_q0 * t_P(q_0)      = {fmt(ell_p_circuit, dps=50)}")
        print("\n--- Battery F1 & F2: Signature (3,1) & Sparling-Graham-Lee Curvature ---")
        for k in f1_rows:
            r1 = f1_rows[k]
            r2 = f2_rows[k]
            print(
                f"  {k:<30} det(G)={r1['det_fefferman_gram'][:14]}  "
                f"eigs=({r1['eigenvalue_timelike_neg'][:10]}, {r1['eigenvalue_spacelike_1'][:9]}, "
                f"{r1['eigenvalue_spacelike_2'][:8]}, {r1['eigenvalue_spacelike_3'][:8]})  "
                f"Ric_11={r2['Ric_11_fibre_killing'][:6]}  |Weyl|={r2['weyl_linf_with_lee_lock'][:8]}"
            )
        print("\n--- Battery F3: Modular-Raychaudhuri (2*pi)/(8*pi) Dual Gravitational Arms ---")
        print(f"  Arm N1 [G_q*(hbar_q/c_q)^2 = 1]     dS/dA_sub = {fmt(density_arm_n1, dps=50)} (rel diff 0)")
        print(f"  Arm N2 [hbar_q*G_q/c_q^3 = q_0]     dS/dA_sub = {fmt(density_arm_n2, dps=50)}")
        print(f"  Arm N2 / Arm N1 (= hbar_q0 * c_q0)  = {fmt(arm_n2_over_n1, dps=50)}")
        print(f"  Arm N2 rel diff vs 1/4 (= -hbar_q0) = {fmt(arm_n2_rel_diff_vs_quarter, dps=50)}")
        print(f"  Arm N1 a0* (Cat / TL / Haar)        = {fmt(a0_n1_cat, dps=16)} / {fmt(a0_n1_tl, dps=16)} / {fmt(a0_n1_haar, dps=16)}")
        print(f"  Arm N2 a0* in Reeb cells (4*q0*s)   = {fmt(a0_n2_sub_cat, dps=16)} / {fmt(a0_n2_sub_tl, dps=16)} / {fmt(a0_n2_sub_haar, dps=16)}")
        print(f"\nWitness written to: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
