#!/usr/bin/env python3
"""dirac_callan_gross_and_dis_cross_section_probe.py — 80-dps Chiral Weyl-Dirac
Clifford Algebra, Spin-1/2 vs Spin-0 Callan-Gross DIS Contractions, 1-Loop QCD
Longitudinal F_L Mellin Moments from Borromean Proton Structure, & Worldline
Schwinger DIS UV Suppression Probe (Zero Fitting, Zero Float64).

Companion to Lean 4 formalization:
  `folio/quantum-observable-universe/lean/QOU/StandardModel/DiracWeylCliffordCallanGrossAndDISCrossSection.lean`
  (`namespace QOU.StandardModel.DiracWeylCliffordCallanGrossAndDISCrossSection`).

PURPOSE & STRICT ANTI-FITTING DISCIPLINE
----------------------------------------
Evaluates at 80 decimal places (95 working guard digits, zero float64 intermediates,
zero `math` or `numpy` imports, zero `float(...)` or `complex(...)` calls, zero fitted
parameters, zero experimental-proximity gated assertions) four linked components of
deep-inelastic lepton-hadron scattering (DIS) in the Quantum Observable Universe:

1. **Part 1 — Chiral Weyl Spinor Clifford Algebra & 4x4 Dirac Trace Identities**:
   - Verifies the exact bridge `spinorMatVec(p) = sum_{mu=0}^3 p_mu sigma^mu` between
     `WorldlineSchwingerFunctorAndSpinorMinkowski` (`Herm_2(C) ~= R^{1,3}`) and the
     chiral Pauli 4-vectors `sigma^mu = (I_2, sigma_vec)`, `sigmaBar^mu = (I_2, -sigma_vec)`.
   - Verifies all 16 Weyl Clifford anticommutators
     `sigma^mu sigmaBar^nu + sigma^nu sigmaBar^mu = 2 eta^{mu nu} I_2` and
     `sigmaBar^mu sigma^nu + sigmaBar^nu sigma^mu = 2 eta^{mu nu} I_2`.
   - Constructs the 4x4 chiral Weyl-Dirac matrices `gamma^mu` and chirality grading
     `gamma_5 = i gamma^0 gamma^1 gamma^2 gamma^3 = diag(-I_2, I_2)` on `C^2_L (+) C^2_R`,
     verifying `{gamma^mu, gamma^nu} = 2 eta^{mu nu} I_4`, `gamma_5^2 = I_4`,
     `{gamma_5, gamma^mu} = 0`, `Tr(gamma_5) = 0`, all 16 two-gamma traces
     `Tr(gamma^mu gamma^nu) = 4 eta^{mu nu}`, all `4^4 = 256` four-gamma traces
     `Tr(gamma^mu gamma^nu gamma^rho gamma^sigma) = 4(eta^{mu nu} eta^{rho sigma} - eta^{mu rho} eta^{nu sigma} + eta^{mu sigma} eta^{nu rho})`,
     all `4^4 = 256` chiral Levi-Civita traces `Tr(gamma_5 gamma^mu gamma^nu gamma^rho gamma^sigma) = -4 i eps^{mu nu rho sigma}`,
     and the Feynman-slash tensor identity `Tr(gamma^mu k_slash gamma^nu k'_slash) = 4(k^mu k'^nu + k'^mu k^nu - (k . k') eta^{mu nu})`.

2. **Part 2 — Spin-1/2 `1 + (1 - y)^2` vs Spin-0 `2(1 - y)` Partonic Contraction &
   Callan-Gross Relation `F_2 = 2 x F_1`**:
   - Evaluates by explicit 4x4 Dirac matrix trace contraction across massless `2 -> 2`
     `e(k) + q(p) -> e(k') + q(p')` centre-of-mass kinematics (`s_hat + t_hat + u_hat = 0`,
     `y = -t_hat / s_hat in [0, 1]`):
       * Spin-1/2 parton: `(1/4) L_{mu nu} W_{1/2}^{mu nu} = 2(s_hat^2 + u_hat^2) = 2 s_hat^2 (1 + (1 - y)^2)`,
       * Spin-0 scalar parton: `(1/2) L_{mu nu} W_0^{mu nu} = -4 s_hat u_hat = 2 s_hat^2 * 2(1 - y)`,
     confirming exact forward (`y = 0`) Rutherford universality (`2` vs `2`) alongside
     backward (`y = 1`) transverse-helicity survival (`1` for spin-1/2 vs `0` for spin-0).
   - Verifies the exact Callan-Gross angular decomposition
     `(1 - y) F_2 + y^2 x F_1 = ((1 + (1 - y)^2)/2) F_2 - (y^2 / 2) F_L` with
     `F_L(x) = F_2(x) - 2 x F_1(x)` (`F_L = 0 <=> F_2 = 2 x F_1`).

3. **Part 3 — 1-Loop QCD Longitudinal `F_L` Mellin Moments (`n = 2, 3, 4`) Evolved
   from QOU Borromean Proton Structure**:
   - Cross-verifies by 95-dps Tanh-Sinh quadrature (`mp.quad`) on `[0, 1]` against exact
     rational FTC formulas the Zee-Wilczek-Treiman / Altarelli-Martinelli 1-loop QCD
     longitudinal Mellin kernel moments (`n = 2, 3, 4`):
       * Quark coefficients in `alpha_s / (2 pi)`: `(8/9, 2/3, 8/15)`
         (equivalently `(16/9, 4/3, 16/15)` in `alpha_s / (4 pi)`),
       * Gluon coefficients per `sum_f e_f^2` in `alpha_s / (2 pi)`: `(1/3, 1/5, 2/15)`
         (equivalently `(2/3, 2/5, 4/15)` in `alpha_s / (4 pi)`).
   - Evolves QOU's Borromean proton `[u, u, d] in H_3(q)` Mellin moments (`n = 2, 3, 4`)
     via the full 2x2 1-loop QCD singlet + non-singlet anomalous-dimension matrix
     `Gamma_n^{(0)}(n_f)` from `mu_0 = m_p` across `m_c = 1.27 GeV` and `m_b = 4.18 GeV`
     to `Q^2 in {4, 20, 100, M_Z^2} GeV^2` side-by-side across `{q_0, q_2t, q_muon}`,
     initial valence fractions `{1/[2]_q, z_D}`, Jucys-Murphy strand branches, and
     2-loop `alpha_s(Q^2)` scale interpretations without post-hoc branch selection.

4. **Part 4 — Worldline Schwinger `1 - exp(-2 Q^2 / E_{Pl}^2)` DIS UV Suppression Bounds
   Across JLab, HERA, LHC, and Trans-Planckian Regimes**:
   - Evaluates the squared massless Schwinger photon propagator factor
     `G_SW(Q^2, 0, T_min)^2 / (1/Q^2)^2 = exp(-2 Q^2 T_min)` and cancellation-free
     fractional cross-section deviation `1 - exp(-2 Q^2 T_min) = -expm1(-2 Q^2 T_min)`
     at `T_min = 1 / E_{Pl}^2` across JLab (`Q^2 = 4 GeV^2`), HERA (`Q^2 = 20 GeV^2` and
     ceiling `10^4 GeV^2`, `< 1.35e-34`), LHC (`Q^2 = 10^8 GeV^2`, `< 1.35e-30`),
     ultra-high-`Q^2` (`10^9 GeV^2`, `< 1.35e-29 < 3.4e-29`), and trans-Planckian scales.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ["QOU_OUTPUT_DPS"] = "80"
os.environ["QOU_COMPUTE_DPS"] = "95"
os.environ["QOU_PRECISION_GUARD"] = "15"

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

from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_P_MEV_VALIDATION,
    M_PI_PM_MEV_VALIDATION,
)
from q_parameter import q_at, q_muon_at, q_two_term_borromean_at  # noqa: E402
from witness_base import WitnessBuilder, q0_comparison  # noqa: E402


# ── Section 0: High-Precision Matrix, Tensor, & Quantum-Integer Helpers ──────
def q_int(n: int, q: mp.mpf) -> mp.mpf:
    """Balanced quantum integer [n]_q = (q^n - q^{-n}) / (q - q^{-1})."""
    return (q ** n - q ** (-n)) / (q - mp.mpf(1) / q)


def mat_zeros(n: int) -> list[list[mp.mpc]]:
    """Construct an n x n zero matrix over mp.mpc."""
    z = mp.mpc(0, 0)
    return [[z for _ in range(n)] for _ in range(n)]


def mat_eye(n: int) -> list[list[mp.mpc]]:
    """Construct an n x n identity matrix over mp.mpc."""
    z = mp.mpc(0, 0)
    one = mp.mpc(1, 0)
    return [[one if r == c else z for c in range(n)] for r in range(n)]


def mat_add(a: list[list[mp.mpc]], b: list[list[mp.mpc]]) -> list[list[mp.mpc]]:
    """Matrix addition over mp.mpc."""
    n = len(a)
    return [[a[r][c] + b[r][c] for c in range(n)] for r in range(n)]


def mat_sub(a: list[list[mp.mpc]], b: list[list[mp.mpc]]) -> list[list[mp.mpc]]:
    """Matrix subtraction over mp.mpc."""
    n = len(a)
    return [[a[r][c] - b[r][c] for c in range(n)] for r in range(n)]


def mat_scale(s: mp.mpc, a: list[list[mp.mpc]]) -> list[list[mp.mpc]]:
    """Scalar-matrix product over mp.mpc."""
    n = len(a)
    return [[s * a[r][c] for c in range(n)] for r in range(n)]


def mat_mul(a: list[list[mp.mpc]], b: list[list[mp.mpc]]) -> list[list[mp.mpc]]:
    """Square matrix multiplication over mp.mpc."""
    n = len(a)
    out = mat_zeros(n)
    for r in range(n):
        for k in range(n):
            ark = a[r][k]
            if ark == 0:
                continue
            for c in range(n):
                out[r][c] += ark * b[k][c]
    return out


def mat_trace(a: list[list[mp.mpc]]) -> mp.mpc:
    """Matrix trace sum_i A_{ii}."""
    n = len(a)
    acc = mp.mpc(0, 0)
    for i in range(n):
        acc += a[i][i]
    return acc


def mat_max_abs(a: list[list[mp.mpc]]) -> mp.mpf:
    """Maximum entrywise modulus max_{r, c} |A_{rc}|."""
    best = mp.mpf(0)
    for row in a:
        for val in row:
            av = abs(val)
            if av > best:
                best = av
    return best


def minkowski_eta(mu: int, nu: int) -> mp.mpf:
    """Minkowski metric tensor eta^{mu nu} = diag(+1, -1, -1, -1)."""
    if mu != nu:
        return mp.mpf(0)
    return mp.mpf(1) if mu == 0 else mp.mpf(-1)


def minkowski_dot(u: list[mp.mpf], v: list[mp.mpf]) -> mp.mpf:
    """Minkowski inner product u_0 v_0 - u_1 v_1 - u_2 v_2 - u_3 v_3."""
    return u[0] * v[0] - u[1] * v[1] - u[2] * v[2] - u[3] * v[3]


def levi_civita_4d(mu: int, nu: int, rho: int, sigma: int) -> int:
    """Totally antisymmetric 4D Levi-Civita tensor with eps^{0123} = +1."""
    idx = [mu, nu, rho, sigma]
    if len(set(idx)) < 4:
        return 0
    inv = 0
    for i in range(4):
        for j in range(i + 1, 4):
            if idx[i] > idx[j]:
                inv += 1
    return 1 if (inv % 2 == 0) else -1


def build_weyl_and_dirac_matrices() -> tuple[
    list[list[list[mp.mpc]]],
    list[list[list[mp.mpc]]],
    list[list[list[mp.mpc]]],
    list[list[mp.mpc]],
]:
    """Build chiral 2x2 sigma^mu, sigmaBar^mu and 4x4 Weyl-Dirac gamma^mu, gamma_5."""
    z = mp.mpc(0, 0)
    one = mp.mpc(1, 0)
    neg_one = mp.mpc(-1, 0)
    im = mp.mpc(0, 1)
    neg_im = mp.mpc(0, -1)

    s0 = [[one, z], [z, one]]
    s1 = [[z, one], [one, z]]
    s2 = [[z, neg_im], [im, z]]
    s3 = [[one, z], [z, neg_one]]

    sigma_vec = [s0, s1, s2, s3]
    sigma_bar_vec = [
        s0,
        mat_scale(neg_one, s1),
        mat_scale(neg_one, s2),
        mat_scale(neg_one, s3),
    ]

    gammas: list[list[list[mp.mpc]]] = []
    for mu in range(4):
        g = mat_zeros(4)
        for r in range(2):
            for c in range(2):
                g[r][2 + c] = sigma_vec[mu][r][c]
                g[2 + r][c] = sigma_bar_vec[mu][r][c]
        gammas.append(g)

    gamma5 = mat_zeros(4)
    gamma5[0][0] = neg_one
    gamma5[1][1] = neg_one
    gamma5[2][2] = one
    gamma5[3][3] = one

    return sigma_vec, sigma_bar_vec, gammas, gamma5


def dirac_slash(k: list[mp.mpf], gammas: list[list[list[mp.mpc]]]) -> list[list[mp.mpc]]:
    """Contravariant Feynman slash k_slash = sum_alpha eta_{alpha alpha} k^alpha gamma^alpha."""
    out = mat_zeros(4)
    for alpha in range(4):
        coeff = mp.mpc(minkowski_eta(alpha, alpha) * k[alpha], 0)
        out = mat_add(out, mat_scale(coeff, gammas[alpha]))
    return out


# ── Section 1: Chiral Weyl-Dirac Clifford & 256-Component Trace Verification ─
def compute_part1_clifford_and_traces() -> dict[str, object]:
    """Verify at 95 working dps all Weyl/Dirac Clifford identities and 256-component traces."""
    with mp.workdps(95):
        sigma_vec, sigma_bar_vec, gammas, gamma5 = build_weyl_and_dirac_matrices()
        eye2 = mat_eye(2)
        eye4 = mat_eye(4)

        # 1. Bridge spinorMatVec(p) == sum_mu p_mu sigma^mu
        p_test = [
            mp.sqrt(mp.mpf(19)),
            mp.pi / mp.mpf(3),
            -mp.sqrt(mp.mpf(5)) / mp.mpf(2),
            mp.log(mp.mpf(7)),
        ]
        spinor_mat_direct = [
            [
                mp.mpc(p_test[0] + p_test[3], 0),
                mp.mpc(p_test[1], -p_test[2]),
            ],
            [
                mp.mpc(p_test[1], p_test[2]),
                mp.mpc(p_test[0] - p_test[3], 0),
            ],
        ]
        spinor_mat_sum = mat_zeros(2)
        for mu in range(4):
            spinor_mat_sum = mat_add(
                spinor_mat_sum, mat_scale(mp.mpc(p_test[mu], 0), sigma_vec[mu])
            )
        spinor_bridge_res = mat_max_abs(mat_sub(spinor_mat_direct, spinor_mat_sum))

        # 2. Weyl 2x2 Clifford anticommutators (all 16 pairs)
        max_weyl_clifford_res = mp.mpf(0)
        for mu in range(4):
            for nu in range(4):
                rhs = mat_scale(mp.mpc(mp.mpf(2) * minkowski_eta(mu, nu), 0), eye2)
                lhs1 = mat_add(
                    mat_mul(sigma_vec[mu], sigma_bar_vec[nu]),
                    mat_mul(sigma_vec[nu], sigma_bar_vec[mu]),
                )
                lhs2 = mat_add(
                    mat_mul(sigma_bar_vec[mu], sigma_vec[nu]),
                    mat_mul(sigma_bar_vec[nu], sigma_vec[mu]),
                )
                max_weyl_clifford_res = max(
                    max_weyl_clifford_res,
                    mat_max_abs(mat_sub(lhs1, rhs)),
                    mat_max_abs(mat_sub(lhs2, rhs)),
                )

        # 3. 4x4 Dirac Clifford anticommutators & gamma_5 identities
        max_dirac_clifford_res = mp.mpf(0)
        max_gamma5_anticomm_res = mp.mpf(0)
        max_two_gamma_trace_res = mp.mpf(0)
        for mu in range(4):
            ac5 = mat_add(mat_mul(gamma5, gammas[mu]), mat_mul(gammas[mu], gamma5))
            max_gamma5_anticomm_res = max(max_gamma5_anticomm_res, mat_max_abs(ac5))
            for nu in range(4):
                rhs4 = mat_scale(mp.mpc(mp.mpf(2) * minkowski_eta(mu, nu), 0), eye4)
                ac = mat_add(mat_mul(gammas[mu], gammas[nu]), mat_mul(gammas[nu], gammas[mu]))
                max_dirac_clifford_res = max(
                    max_dirac_clifford_res, mat_max_abs(mat_sub(ac, rhs4))
                )
                tr2 = mat_trace(mat_mul(gammas[mu], gammas[nu]))
                max_two_gamma_trace_res = max(
                    max_two_gamma_trace_res,
                    abs(tr2 - mp.mpc(mp.mpf(4) * minkowski_eta(mu, nu), 0)),
                )

        gamma5_sq_res = mat_max_abs(mat_sub(mat_mul(gamma5, gamma5), eye4))
        prod_0123 = mat_mul(mat_mul(mat_mul(gammas[0], gammas[1]), gammas[2]), gammas[3])
        gamma5_prod_res = mat_max_abs(
            mat_sub(mat_scale(mp.mpc(0, 1), prod_0123), gamma5)
        )
        tr_gamma5_res = abs(mat_trace(gamma5))

        # 4. All 4^4 = 256 four-gamma traces and chiral gamma_5 four-gamma traces
        max_four_gamma_trace_res = mp.mpf(0)
        max_chiral_levi_civita_trace_res = mp.mpf(0)
        nonzero_four_gamma_count = 0
        nonzero_levi_civita_count = 0
        for mu in range(4):
            for nu in range(4):
                g_mn = mat_mul(gammas[mu], gammas[nu])
                for rho in range(4):
                    g_mnr = mat_mul(g_mn, gammas[rho])
                    for sigma in range(4):
                        g_mnrs = mat_mul(g_mnr, gammas[sigma])
                        tr4 = mat_trace(g_mnrs)
                        expected_tr4 = mp.mpf(4) * (
                            minkowski_eta(mu, nu) * minkowski_eta(rho, sigma)
                            - minkowski_eta(mu, rho) * minkowski_eta(nu, sigma)
                            + minkowski_eta(mu, sigma) * minkowski_eta(nu, rho)
                        )
                        if expected_tr4 != mp.mpf(0):
                            nonzero_four_gamma_count += 1
                        max_four_gamma_trace_res = max(
                            max_four_gamma_trace_res,
                            abs(tr4 - mp.mpc(expected_tr4, 0)),
                        )

                        tr5 = mat_trace(mat_mul(gamma5, g_mnrs))
                        eps_val = levi_civita_4d(mu, nu, rho, sigma)
                        if eps_val != 0:
                            nonzero_levi_civita_count += 1
                        # For gamma_5 = +i gamma^0 gamma^1 gamma^2 gamma^3,
                        # gamma^0 gamma^1 gamma^2 gamma^3 = -i gamma_5 => Tr(gamma_5 g^0 g^1 g^2 g^3) = -4 i.
                        expected_tr5 = mp.mpc(0, -4 * eps_val)
                        max_chiral_levi_civita_trace_res = max(
                            max_chiral_levi_civita_trace_res,
                            abs(tr5 - expected_tr5),
                        )

        # 5. Feynman slash trace Tr(gamma^mu k_slash gamma^nu k'_slash) = L^{mu nu}(k, k')
        k_vec = [mp.sqrt(mp.mpf(17)), mp.mpf(2), -mp.mpf(3) / mp.mpf(2), mp.sqrt(mp.mpf(43)) / mp.mpf(2)]
        kp_vec = [mp.sqrt(mp.mpf(29)), -mp.mpf(5) / mp.mpf(3), mp.mpf(4) / mp.mpf(3), mp.mpf(7) / mp.mpf(5)]
        k_sl = dirac_slash(k_vec, gammas)
        kp_sl = dirac_slash(kp_vec, gammas)
        k_dot_kp = minkowski_dot(k_vec, kp_vec)
        max_slash_trace_res = mp.mpf(0)
        for mu in range(4):
            for nu in range(4):
                prod_mat = mat_mul(mat_mul(mat_mul(gammas[mu], k_sl), gammas[nu]), kp_sl)
                tr_val = mat_trace(prod_mat)
                tensor_val = mp.mpf(4) * (
                    k_vec[mu] * kp_vec[nu]
                    + kp_vec[mu] * k_vec[nu]
                    - k_dot_kp * minkowski_eta(mu, nu)
                )
                max_slash_trace_res = max(
                    max_slash_trace_res, abs(tr_val - mp.mpc(tensor_val, 0))
                )

        worst_res = max(
            spinor_bridge_res,
            max_weyl_clifford_res,
            max_dirac_clifford_res,
            max_gamma5_anticomm_res,
            gamma5_sq_res,
            gamma5_prod_res,
            tr_gamma5_res,
            max_two_gamma_trace_res,
            max_four_gamma_trace_res,
            max_chiral_levi_civita_trace_res,
            max_slash_trace_res,
        )

        return {
            "four_gamma_components_checked": 256,
            "nonzero_four_gamma_components": nonzero_four_gamma_count,
            "nonzero_chiral_levi_civita_components": nonzero_levi_civita_count,
            "spinor_mat_bridge_residual": fmt(spinor_bridge_res),
            "max_weyl_clifford_residual": fmt(max_weyl_clifford_res),
            "max_dirac_clifford_residual": fmt(max_dirac_clifford_res),
            "gamma5_sq_residual": fmt(gamma5_sq_res),
            "gamma5_four_product_residual": fmt(gamma5_prod_res),
            "max_gamma5_anticommutator_residual": fmt(max_gamma5_anticomm_res),
            "trace_gamma5_residual": fmt(tr_gamma5_res),
            "max_two_gamma_trace_residual": fmt(max_two_gamma_trace_res),
            "max_four_gamma_trace_256_residual": fmt(max_four_gamma_trace_res),
            "max_chiral_levi_civita_256_residual": fmt(max_chiral_levi_civita_trace_res),
            "max_feynman_slash_trace_residual": fmt(max_slash_trace_res),
            "_raw_worst_residual": worst_res,
        }


# ── Section 2: Spin-1/2 vs Spin-0 DIS Contraction & Callan-Gross Relation ────
def compute_part2_spin_half_vs_spin_zero_callan_gross() -> dict[str, object]:
    """Verify 80-dps spin-1/2 1+(1-y)^2 vs spin-0 2(1-y) contractions and Callan-Gross."""
    with mp.workdps(95):
        _s, _sb, gammas, _g5 = build_weyl_and_dirac_matrices()
        e_cm = mp.sqrt(mp.mpf(37))  # s_hat = 4 E_cm^2 = 148 GeV^2
        s_hat = mp.mpf(4) * (e_cm ** 2)

        y_grid = [
            ("y_0_forward", mp.mpf(0)),
            ("y_1_over_10", mp.mpf(1) / mp.mpf(10)),
            ("y_1_over_4", mp.mpf(1) / mp.mpf(4)),
            ("y_1_over_2", mp.mpf(1) / mp.mpf(2)),
            ("y_3_over_4", mp.mpf(3) / mp.mpf(4)),
            ("y_9_over_10", mp.mpf(9) / mp.mpf(10)),
            ("y_1_backward", mp.mpf(1)),
        ]

        angular_scan: dict[str, object] = {}
        max_spin_half_res = mp.mpf(0)
        max_spin_zero_res = mp.mpf(0)
        max_mandelstam_res = mp.mpf(0)

        for label, y_val in y_grid:
            # Massless CM kinematics: cos(theta*) = 1 - 2 y, sin(theta*) = 2 sqrt(y (1 - y))
            cos_th = mp.mpf(1) - mp.mpf(2) * y_val
            sin_th = mp.mpf(2) * mp.sqrt(max(y_val * (mp.mpf(1) - y_val), mp.mpf(0)))

            k_in = [e_cm, mp.mpf(0), mp.mpf(0), e_cm]
            p_in = [e_cm, mp.mpf(0), mp.mpf(0), -e_cm]
            k_out = [e_cm, e_cm * sin_th, mp.mpf(0), e_cm * cos_th]
            p_out = [e_cm, -e_cm * sin_th, mp.mpf(0), -e_cm * cos_th]

            t_hat = -mp.mpf(2) * minkowski_dot(k_in, k_out)
            u_hat = -mp.mpf(2) * minkowski_dot(k_in, p_out)
            max_mandelstam_res = max(
                max_mandelstam_res,
                abs(s_hat + t_hat + u_hat),
                abs(y_val - (-t_hat / s_hat)),
                abs(minkowski_dot(k_in, k_in)),
                abs(minkowski_dot(p_in, p_in)),
                abs(minkowski_dot(k_out, k_out)),
                abs(minkowski_dot(p_out, p_out)),
            )

            k_sl = dirac_slash(k_in, gammas)
            ko_sl = dirac_slash(k_out, gammas)
            p_sl = dirac_slash(p_in, gammas)
            po_sl = dirac_slash(p_out, gammas)

            # Direct 4x4 matrix trace evaluation of L^{mu nu} and W_{1/2}^{mu nu}
            l_ten = [[mp.mpf(0) for _ in range(4)] for _ in range(4)]
            w_half = [[mp.mpf(0) for _ in range(4)] for _ in range(4)]
            w_zero = [[mp.mpf(0) for _ in range(4)] for _ in range(4)]
            for mu in range(4):
                for nu in range(4):
                    tr_l = mat_trace(mat_mul(mat_mul(mat_mul(gammas[mu], k_sl), gammas[nu]), ko_sl))
                    tr_w = mat_trace(mat_mul(mat_mul(mat_mul(gammas[mu], p_sl), gammas[nu]), po_sl))
                    l_ten[mu][nu] = tr_l.real
                    w_half[mu][nu] = tr_w.real
                    w_zero[mu][nu] = (p_in[mu] + p_out[mu]) * (p_in[nu] + p_out[nu])

            contract_half = mp.mpf(0)
            contract_zero = mp.mpf(0)
            for mu in range(4):
                eta_m = minkowski_eta(mu, mu)
                for nu in range(4):
                    eta_n = minkowski_eta(nu, nu)
                    contract_half += eta_m * eta_n * l_ten[mu][nu] * w_half[mu][nu]
                    contract_zero += eta_m * eta_n * l_ten[mu][nu] * w_zero[mu][nu]

            spin_avg_half = contract_half / mp.mpf(4)
            spin_avg_zero = contract_zero / mp.mpf(2)

            norm_half = spin_avg_half / (mp.mpf(2) * (s_hat ** 2))
            norm_zero = spin_avg_zero / (mp.mpf(2) * (s_hat ** 2))

            analytic_half = mp.mpf(1) + (mp.mpf(1) - y_val) ** 2
            analytic_zero = mp.mpf(2) * (mp.mpf(1) - y_val)

            max_spin_half_res = max(
                max_spin_half_res,
                abs(spin_avg_half - mp.mpf(2) * (s_hat ** 2 + u_hat ** 2)),
                abs(norm_half - analytic_half),
            )
            max_spin_zero_res = max(
                max_spin_zero_res,
                abs(spin_avg_zero - (-mp.mpf(4) * s_hat * u_hat)),
                abs(norm_zero - analytic_zero),
            )

            angular_scan[label] = {
                "y": fmt(y_val),
                "spin_half_normalized_trace": fmt(norm_half),
                "spin_half_1_plus_1_minus_y_sq": fmt(analytic_half),
                "spin_zero_normalized_trace": fmt(norm_zero),
                "spin_zero_2_times_1_minus_y": fmt(analytic_zero),
                "spin_half_minus_spin_zero_y_sq_excess": fmt(norm_half - norm_zero),
            }

        # Callan-Gross decomposition identity check across generic (x, y, F_1, F_2)
        x_t = mp.mpf(3) / mp.mpf(11)
        f2_t = mp.sqrt(mp.mpf(2)) / mp.mpf(3)
        f1_cg = f2_t / (mp.mpf(2) * x_t)  # Callan-Gross F_2 = 2 x F_1 => F_L = 0
        f1_gen = f1_cg - mp.mpf(1) / mp.mpf(17)
        fl_cg = f2_t - mp.mpf(2) * x_t * f1_cg
        fl_gen = f2_t - mp.mpf(2) * x_t * f1_gen

        max_cg_decomp_res = mp.mpf(0)
        for _lbl, y_val in y_grid:
            for f1_v, fl_v in ((f1_cg, fl_cg), (f1_gen, fl_gen), (mp.mpf(0), f2_t)):
                lhs = (mp.mpf(1) - y_val) * f2_t + (y_val ** 2) * x_t * f1_v
                rhs = ((mp.mpf(1) + (mp.mpf(1) - y_val) ** 2) / mp.mpf(2)) * f2_t - (
                    (y_val ** 2) / mp.mpf(2)
                ) * fl_v
                max_cg_decomp_res = max(max_cg_decomp_res, abs(lhs - rhs))

        backward_spin_half = mp.mpf(1) + (mp.mpf(1) - mp.mpf(1)) ** 2
        backward_spin_zero = mp.mpf(2) * (mp.mpf(1) - mp.mpf(1))

        return {
            "s_hat_test_gev2": fmt(s_hat),
            "forward_y0_spin_half_weight": fmt(mp.mpf(2)),
            "forward_y0_spin_zero_weight": fmt(mp.mpf(2)),
            "backward_y1_spin_half_transverse_helicity_weight": fmt(backward_spin_half),
            "backward_y1_spin_zero_weight": fmt(backward_spin_zero),
            "callan_gross_exact_fl_residual": fmt(abs(fl_cg)),
            "max_mandelstam_kinematic_residual": fmt(max_mandelstam_res),
            "max_spin_half_trace_vs_1_plus_1_minus_y_sq_residual": fmt(max_spin_half_res),
            "max_spin_zero_trace_vs_2_times_1_minus_y_residual": fmt(max_spin_zero_res),
            "max_callan_gross_decomposition_residual": fmt(max_cg_decomp_res),
            "angular_inelasticity_scan": angular_scan,
            "_raw_worst_residual": max(
                max_mandelstam_res, max_spin_half_res, max_spin_zero_res, max_cg_decomp_res, abs(fl_cg)
            ),
            "_raw_backward_spin_half": backward_spin_half,
            "_raw_backward_spin_zero": backward_spin_zero,
        }


# ── Section 3: 1-Loop QCD Longitudinal F_L Mellin Moments (n = 2, 3, 4) ──────
def b0_qcd(nf: int) -> mp.mpf:
    """1-loop SU(3)_c beta coefficient b_0(n_f) = 11 - (2/3) n_f."""
    return mp.mpf(11) - mp.mpf(2 * nf) / mp.mpf(3)


def b1_qcd(nf: int) -> mp.mpf:
    """2-loop SU(3)_c beta coefficient b_1(n_f) = 102 - (38/3) n_f."""
    return mp.mpf(102) - mp.mpf(38 * nf) / mp.mpf(3)


def rg_f_2loop(alpha_s: mp.mpf, nf: int) -> mp.mpf:
    """Exact 2-loop RG invariant F(alpha_s; n_f) = ln(Q^2 / Lambda^2)."""
    with mp.workdps(95):
        b0 = b0_qcd(nf)
        b1 = b1_qcd(nf)
        c = b1 / (b0 ** 2)
        u = (mp.mpf(4) * mp.pi) / (b0 * alpha_s)
        return u - c * mp.log(u + c)


def solve_alpha_s_2loop(target_f: mp.mpf, nf: int) -> mp.mpf:
    """Solve F(alpha_s; n_f) = target_f by 95-dps Newton iteration."""
    with mp.workdps(95):
        b0 = b0_qcd(nf)
        b1 = b1_qcd(nf)
        c = b1 / (b0 ** 2)
        u = max(target_f + c * mp.log(max(target_f, mp.mpf(2))), mp.mpf(1))
        for _ in range(45):
            f_val = u - c * mp.log(u + c) - target_f
            df_val = mp.mpf(1) - c / (u + c)
            du = f_val / df_val
            u -= du
            if abs(du) < mp.mpf("1e-90"):
                break
        return (mp.mpf(4) * mp.pi) / (b0 * u)


def build_alpha_s_profile_from_lambda3(lam3_gev: mp.mpf) -> dict[str, mp.mpf]:
    """Build continuously threshold-matched 2-loop alpha_s profile across m_c=1.27, m_b=4.18 GeV."""
    with mp.workdps(95):
        m_c = mp.mpf("1.27")
        m_b = mp.mpf("4.18")
        f3_mc = mp.mpf(2) * mp.log(m_c / lam3_gev)
        as_mc = solve_alpha_s_2loop(f3_mc, 3)
        f4_mc = rg_f_2loop(as_mc, 4)
        lam4 = m_c * mp.exp(-f4_mc / mp.mpf(2))
        f4_mb = f4_mc + mp.mpf(2) * mp.log(m_b / m_c)
        as_mb = solve_alpha_s_2loop(f4_mb, 4)
        f5_mb = rg_f_2loop(as_mb, 5)
        lam5 = m_b * mp.exp(-f5_mb / mp.mpf(2))
        return {
            "lam3": lam3_gev,
            "lam4": lam4,
            "lam5": lam5,
            "f3_mc": f3_mc,
            "f4_mc": f4_mc,
            "f4_mb": f4_mb,
            "f5_mb": f5_mb,
            "as_mc": as_mc,
            "as_mb": as_mb,
        }


def build_alpha_s_profile_from_lambda5(lam5_gev: mp.mpf) -> dict[str, mp.mpf]:
    """Match downward from Lambda^{(5)} across m_b=4.18 and m_c=1.27 GeV to Lambda^{(3)}."""
    with mp.workdps(95):
        m_c = mp.mpf("1.27")
        m_b = mp.mpf("4.18")
        f5_mb = mp.mpf(2) * mp.log(m_b / lam5_gev)
        as_mb = solve_alpha_s_2loop(f5_mb, 5)
        f4_mb = rg_f_2loop(as_mb, 4)
        f4_mc = f4_mb + mp.mpf(2) * mp.log(m_c / m_b)
        as_mc = solve_alpha_s_2loop(f4_mc, 4)
        f3_mc = rg_f_2loop(as_mc, 3)
        lam3 = m_c * mp.exp(-f3_mc / mp.mpf(2))
        return build_alpha_s_profile_from_lambda3(lam3)


def eval_alpha_s_2loop_at_q(prof: dict[str, mp.mpf], q_gev: mp.mpf) -> tuple[mp.mpf, int]:
    """Evaluate 2-loop alpha_s(Q) and active flavour count n_f at scale Q (in GeV)."""
    with mp.workdps(95):
        m_c = mp.mpf("1.27")
        m_b = mp.mpf("4.18")
        if q_gev <= m_c:
            fq = mp.mpf(2) * mp.log(q_gev / prof["lam3"])
            return solve_alpha_s_2loop(fq, 3), 3
        if q_gev <= m_b:
            fq = prof["f4_mc"] + mp.mpf(2) * mp.log(q_gev / m_c)
            return solve_alpha_s_2loop(fq, 4), 4
        fq = prof["f5_mb"] + mp.mpf(2) * mp.log(q_gev / m_b)
        return solve_alpha_s_2loop(fq, 5), 5


def gamma_ns_1loop(n: int) -> mp.mpf:
    """Exact 1-loop QCD non-singlet Mellin anomalous dimension gamma_n^{NS} (C_F = 4/3)."""
    with mp.workdps(95):
        hn = sum(mp.mpf(1) / mp.mpf(k) for k in range(1, n + 1))
        return (mp.mpf(4) / mp.mpf(3)) * (
            mp.mpf(4) * hn - mp.mpf(3) - mp.mpf(2) / mp.mpf(n * (n + 1))
        )


def singlet_anomalous_matrix_1loop(n: int, nf: int) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    """Exact 1-loop QCD singlet 2x2 Mellin anomalous-dimension matrix Gamma_n^{(0)}(n_f)
    for n >= 2 (Gross & Wilczek 1974; Georgi & Politzer 1974; Altarelli & Parisi 1977):
      gamma_qq(n)      = gamma_n^{NS} = (4/3)(4 H_n - 3 - 2/(n(n+1))),
      gamma_qg(n, n_f) = -2 n_f (n^2 + n + 2) / (n (n+1) (n+2)),
      gamma_gq(n)      = -(8/3) (n^2 + n + 2) / ((n-1) n (n+1)),
      gamma_gg(n, n_f) = 12 [H_n - 1/(n(n-1)) - 1/((n+1)(n+2))] - 11 + (2/3) n_f.
    """
    with mp.workdps(95):
        hn = sum(mp.mpf(1) / mp.mpf(k) for k in range(1, n + 1))
        num_poly = mp.mpf(n * n + n + 2)
        g_qq = gamma_ns_1loop(n)
        g_qg = -mp.mpf(2 * nf) * num_poly / mp.mpf(n * (n + 1) * (n + 2))
        g_gq = -(mp.mpf(8) / mp.mpf(3)) * num_poly / mp.mpf((n - 1) * n * (n + 1))
        g_gg = (
            mp.mpf(12)
            * (
                hn
                - mp.mpf(1) / mp.mpf(n * (n - 1))
                - mp.mpf(1) / mp.mpf((n + 1) * (n + 2))
            )
            - mp.mpf(11)
            + mp.mpf(2 * nf) / mp.mpf(3)
        )
        return g_qq, g_qg, g_gq, g_gg


def sum_quark_charges_sq(nf: int) -> mp.mpf:
    """Sum of squared quark electric charges sum_{f=1}^{n_f} e_f^2 for active flavours
    (u, d, s -> 2/3; +c -> 10/9; +b -> 11/9)."""
    charges_sq = [
        mp.mpf(4) / mp.mpf(9),  # u
        mp.mpf(1) / mp.mpf(9),  # d
        mp.mpf(1) / mp.mpf(9),  # s
        mp.mpf(4) / mp.mpf(9),  # c
        mp.mpf(1) / mp.mpf(9),  # b
    ]
    return sum(charges_sq[:nf])


def evolve_singlet_and_flavour_interval(
    flav_moments: dict[int, dict[str, mp.mpf]],
    as_low: mp.mpf,
    as_high: mp.mpf,
    nf: int,
) -> dict[int, dict[str, mp.mpf]]:
    """Evolve individual quark+antiquark flavour moments q_f^+ = q_f + qbar_f (f in {u,d,s,c,b})
    and gluon moments g for n in {2, 3, 4} across an active-n_f threshold interval [mu_low, mu_high]
    using exact 2x2 spectral projector diagonalization of Gamma_n^{(0)}(n_f).
    """
    with mp.workdps(95):
        b0 = b0_qcd(nf)
        ratio = as_high / as_low
        active_flavs = ["u", "d", "s", "c", "b"][:nf]
        inactive_flavs = ["u", "d", "s", "c", "b"][nf:]

        out: dict[int, dict[str, mp.mpf]] = {}
        for n in (2, 3, 4):
            cur = flav_moments[n]
            g_ns = gamma_ns_1loop(n)
            fac_ns = ratio ** (g_ns / (mp.mpf(2) * b0))

            sigma_old = sum(cur[f] for f in active_flavs)
            gluon_old = cur["g"]

            g_qq, g_qg, g_gq, g_gg = singlet_anomalous_matrix_1loop(n, nf)
            tr_g = g_qq + g_gg
            diff_g = g_qq - g_gg
            disc = mp.sqrt(diff_g * diff_g + mp.mpf(4) * g_qg * g_gq)
            lam_minus = (tr_g - disc) / mp.mpf(2)
            lam_plus = (tr_g + disc) / mp.mpf(2)

            e_minus = ratio ** (lam_minus / (mp.mpf(2) * b0))
            e_plus = ratio ** (lam_plus / (mp.mpf(2) * b0))

            # Matrix exponential E = e_- P_- + e_+ P_+ where P_- = (Gamma - lam_+ I)/(lam_- - lam_+)
            denom = lam_minus - lam_plus
            p_mm_00 = (g_qq - lam_plus) / denom
            p_mm_01 = g_qg / denom
            p_mm_10 = g_gq / denom
            p_mm_11 = (g_gg - lam_plus) / denom

            e_00 = e_minus * p_mm_00 + e_plus * (mp.mpf(1) - p_mm_00)
            e_01 = e_minus * p_mm_01 + e_plus * (-p_mm_01)
            e_10 = e_minus * p_mm_10 + e_plus * (-p_mm_10)
            e_11 = e_minus * p_mm_11 + e_plus * (mp.mpf(1) - p_mm_11)

            sigma_new = e_00 * sigma_old + e_01 * gluon_old
            gluon_new = e_10 * sigma_old + e_11 * gluon_old

            # Each active flavour q_f^+ = sigma / n_f + (q_f^+ - sigma / n_f), where the
            # traceless non-singlet difference evolves multiplicatively by fac_ns:
            avg_old = sigma_old / mp.mpf(nf)
            avg_new = sigma_new / mp.mpf(nf)
            next_n: dict[str, mp.mpf] = {"g": gluon_new}
            for f in active_flavs:
                next_n[f] = avg_new + (cur[f] - avg_old) * fac_ns
            for f in inactive_flavs:
                next_n[f] = mp.mpf(0)
            out[n] = next_n

        return out


def build_borromean_initial_partons(
    q_val: mp.mpf,
    m2_val_init: mp.mpf,
    strand_mode: str,
    gluon_higher_mode: str,
) -> dict[int, dict[str, mp.mpf]]:
    """Construct initial Borromean proton parton Mellin moments at mu_0 = m_p for n in {2, 3, 4}."""
    with mp.workdps(95):
        w_tot = mp.mpf(1) + (q_val ** 2) + (q_val ** 4)
        x1 = m2_val_init / w_tot
        x2 = m2_val_init * (q_val ** 2) / w_tot
        x3 = m2_val_init * (q_val ** 4) / w_tot

        m2_g = mp.mpf(1) - m2_val_init
        out: dict[int, dict[str, mp.mpf]] = {}
        for n in (2, 3, 4):
            p = n - 1
            uv_pal = (x1 ** p) + (x3 ** p)
            dv_pal = x2 ** p
            uv_ord = (x2 ** p) + (x3 ** p)
            dv_ord = x1 ** p

            if strand_mode == "palindromic_d_middle":
                uv_n, dv_n = uv_pal, dv_pal
            elif strand_mode == "ordered_d_first":
                uv_n, dv_n = uv_ord, dv_ord
            elif strand_mode == "symmetrized_midpoint":
                if n == 2:
                    r_pal = (mp.mpf(1) + (q_val ** 4)) / (q_val ** 2)
                    r_ord = (q_val ** 2) * (mp.mpf(1) + (q_val ** 2))
                    r_mid = (r_pal + r_ord) / mp.mpf(2)
                    dv_n = m2_val_init / (mp.mpf(1) + r_mid)
                    uv_n = m2_val_init * r_mid / (mp.mpf(1) + r_mid)
                else:
                    uv_n = (uv_pal + uv_ord) / mp.mpf(2)
                    dv_n = (dv_pal + dv_ord) / mp.mpf(2)
            else:
                raise ValueError(f"Unknown strand_mode: {strand_mode}")

            if n == 2:
                g_n = m2_g
            elif gluon_higher_mode == "three_tube_flux_sharing":
                # Symmetric sharing of M_2(g, mu_0) across the 3 Borromean colour-flux tubes:
                g_n = mp.mpf(3) * ((m2_g / mp.mpf(3)) ** p)
            elif gluon_higher_mode == "pure_radiative_gluon":
                g_n = mp.mpf(0)
            else:
                raise ValueError(f"Unknown gluon_higher_mode: {gluon_higher_mode}")

            out[n] = {
                "u": uv_n,
                "d": dv_n,
                "s": mp.mpf(0),
                "c": mp.mpf(0),
                "b": mp.mpf(0),
                "g": g_n,
            }
        return out


def evaluate_fl_moments_at_scale(
    partons: dict[int, dict[str, mp.mpf]], alpha_s: mp.mpf, nf: int
) -> dict[str, object]:
    """Evaluate electromagnetic M_n(Sigma_em), M_n(g), 1-loop M_n(F_L), and R_n = M_n(F_L)/(M_n(Sigma_em)-M_n(F_L))."""
    with mp.workdps(95):
        e_sq_map = {
            "u": mp.mpf(4) / mp.mpf(9),
            "d": mp.mpf(1) / mp.mpf(9),
            "s": mp.mpf(1) / mp.mpf(9),
            "c": mp.mpf(4) / mp.mpf(9),
            "b": mp.mpf(1) / mp.mpf(9),
        }
        sum_e2 = sum_quark_charges_sq(nf)
        pref_2pi = alpha_s / (mp.mpf(2) * mp.pi)
        pref_4pi = alpha_s / (mp.mpf(4) * mp.pi)

        moments_out: dict[str, object] = {}
        raw_fl: dict[int, mp.mpf] = {}
        raw_r: dict[int, mp.mpf] = {}
        max_dual_norm_res = mp.mpf(0)

        for n in (2, 3, 4):
            cur = partons[n]
            m_sigma_em = sum(e_sq_map[f] * cur[f] for f in ("u", "d", "s", "c", "b")[:nf])
            m_sigma_plain = sum(cur[f] for f in ("u", "d", "s", "c", "b")[:nf])
            m_g = cur["g"]

            c_q_2pi = mp.mpf(8) / mp.mpf(3 * (n + 1))
            c_g_2pi = mp.mpf(4) / mp.mpf((n + 1) * (n + 2))
            m_fl_2pi = pref_2pi * (c_q_2pi * m_sigma_em + sum_e2 * c_g_2pi * m_g)

            c_q_4pi = mp.mpf(16) / mp.mpf(3 * (n + 1))
            c_g_4pi = mp.mpf(8) * sum_e2 / mp.mpf((n + 1) * (n + 2))
            m_fl_4pi = pref_4pi * (c_q_4pi * m_sigma_em + c_g_4pi * m_g)
            max_dual_norm_res = max(max_dual_norm_res, abs(m_fl_2pi - m_fl_4pi))

            r_ratio = m_fl_2pi / (m_sigma_em - m_fl_2pi)
            raw_fl[n] = m_fl_2pi
            raw_r[n] = r_ratio

            moments_out[f"n_{n}"] = {
                "M_n_Sigma_em": fmt(m_sigma_em),
                "M_n_Sigma_flavour_singlet": fmt(m_sigma_plain),
                "M_n_gluon": fmt(m_g),
                "M_n_F_L_1loop": fmt(m_fl_2pi),
                "M_n_F_L_quark_channel": fmt(pref_2pi * c_q_2pi * m_sigma_em),
                "M_n_F_L_gluon_channel": fmt(pref_2pi * sum_e2 * c_g_2pi * m_g),
                "longitudinal_to_transverse_ratio_R_n": fmt(r_ratio),
            }

        return {
            "moments": moments_out,
            "_raw_fl": raw_fl,
            "_raw_r": raw_r,
            "_raw_dual_norm_res": max_dual_norm_res,
            "_raw_m2_total": sum(partons[2][f] for f in ("u", "d", "s", "c", "b")[:nf]) + partons[2]["g"],
        }


def compute_part3_fl_mellin_moments() -> dict[str, object]:
    """Verify Altarelli-Martinelli kernel integrals at 80+ dps and evolve Borromean F_L moments."""
    with mp.workdps(95):
        # 1. Direct 95-dps quadrature vs exact FTC rational coefficients for n in {2, 3, 4}
        kernel_benchmarks: dict[str, object] = {}
        max_quad_kernel_res = mp.mpf(0)
        for n in (2, 3, 4):
            q_exact_2pi = mp.mpf(8) / mp.mpf(3 * (n + 1))
            g_exact_2pi = mp.mpf(4) / mp.mpf((n + 1) * (n + 2))
            q_quad = mp.quad(
                lambda z, n_exp=n: (mp.mpf(8) / mp.mpf(3)) * (z ** n_exp),
                [mp.mpf(0), mp.mpf(1)],
            )
            g_quad = mp.quad(
                lambda z, n_exp=n: mp.mpf(4) * (z ** n_exp) * (mp.mpf(1) - z),
                [mp.mpf(0), mp.mpf(1)],
            )
            max_quad_kernel_res = max(
                max_quad_kernel_res,
                abs(q_quad - q_exact_2pi),
                abs(g_quad - g_exact_2pi),
            )
            kernel_benchmarks[f"n_{n}"] = {
                "quark_coeff_alpha_s_over_2pi": fmt(q_exact_2pi),
                "quark_coeff_alpha_s_over_4pi": fmt(mp.mpf(2) * q_exact_2pi),
                "quark_quadrature_residual": fmt(abs(q_quad - q_exact_2pi)),
                "gluon_coeff_per_sum_e2_alpha_s_over_2pi": fmt(g_exact_2pi),
                "gluon_coeff_per_sum_e2_alpha_s_over_4pi": fmt(mp.mpf(2) * g_exact_2pi),
                "gluon_quadrature_residual": fmt(abs(g_quad - g_exact_2pi)),
            }

        # Verify momentum conservation sum rule on Gamma_2^{(0)}(n_f):
        max_mom_anom_res = mp.mpf(0)
        for nf in (3, 4, 5):
            g_qq, g_qg, g_gq, g_gg = singlet_anomalous_matrix_1loop(2, nf)
            max_mom_anom_res = max(max_mom_anom_res, abs(g_qq + g_gq), abs(g_qg + g_gg))

        # 2. Alpha_s profiles: QOU (3/2) m_pi as Lambda^{(5)} and as Lambda^{(3)}, plus PDG reference
        m_p_gev = M_P_MEV_VALIDATION / mp.mpf(1000)
        m_pi_gev = M_PI_PM_MEV_VALIDATION / mp.mpf(1000)
        m_c_gev = mp.mpf("1.27")
        m_b_gev = mp.mpf("4.18")
        m_z_gev = mp.mpf("91.1876")

        lam_3half_mpi = (mp.mpf(3) / mp.mpf(2)) * m_pi_gev
        as_mz_pdg = mp.mpf("0.1180")
        lam5_pdg = m_z_gev * mp.exp(-rg_f_2loop(as_mz_pdg, 5) / mp.mpf(2))

        alpha_profiles = {
            "qou_3half_mpi_as_lambda5": build_alpha_s_profile_from_lambda5(lam_3half_mpi),
            "qou_3half_mpi_as_lambda3": build_alpha_s_profile_from_lambda3(lam_3half_mpi),
            "pdg_2024_alpha_s_mz_0p1180": build_alpha_s_profile_from_lambda5(lam5_pdg),
        }

        pins = {
            "q_0_one_term_proton": q_at(95),
            "q_2t_two_term_borromean_proton": q_two_term_borromean_at(95),
            "q_muon_ideal_cal2": q_muon_at(95),
        }

        q2_scales = [
            ("Q2_4_GeV2", mp.mpf(2)),
            ("Q2_20_GeV2_HERA_FL", mp.sqrt(mp.mpf(20))),
            ("Q2_100_GeV2", mp.mpf(10)),
            ("Q2_MZ2_LHC", m_z_gev),
        ]

        branch_census: dict[str, object] = {}
        max_dual_norm_res = mp.mpf(0)
        max_momentum_sum_res = mp.mpf(0)
        monotonic_r_ok = True
        strict_positive_fl_ok = True

        for pin_name, q_val in pins.items():
            val_inits = {
                "inv_q2_int": mp.mpf(1) / q_int(2, q_val),
                "z_D_markov": (q_val ** 3) / ((q_val ** 2) + mp.mpf(1)),
            }
            pin_out: dict[str, object] = {"q_value": fmt(q_val), "branches": {}}

            for val_label, m2_val in val_inits.items():
                for strand_mode in ("palindromic_d_middle", "ordered_d_first", "symmetrized_midpoint"):
                    for gluon_mode in ("three_tube_flux_sharing", "pure_radiative_gluon"):
                        # Keep full 3x3x2x3 cross-section at q_0 and canonical representative
                        # across q_2t and q_muon so witness stays compact yet complete across all pins:
                        if pin_name != "q_0_one_term_proton" and not (
                            strand_mode == "symmetrized_midpoint"
                            and gluon_mode == "three_tube_flux_sharing"
                        ):
                            continue

                        bkey = f"{val_label}__{strand_mode}__{gluon_mode}"
                        init_partons = build_borromean_initial_partons(
                            q_val, m2_val, strand_mode, gluon_mode
                        )
                        prof_tables: dict[str, object] = {}

                        for prof_name, prof in alpha_profiles.items():
                            as_mp, _ = eval_alpha_s_2loop_at_q(prof, m_p_gev)
                            as_mc = prof["as_mc"]
                            as_mb = prof["as_mb"]

                            at_mc = evolve_singlet_and_flavour_interval(
                                init_partons, as_mp, as_mc, 3
                            )
                            at_mb = evolve_singlet_and_flavour_interval(
                                at_mc, as_mc, as_mb, 4
                            )

                            scale_evals: dict[str, object] = {}
                            r_seq_by_n: dict[int, list[mp.mpf]] = {2: [], 3: [], 4: []}

                            for q2_name, q_gev in q2_scales:
                                as_q, nf_q = eval_alpha_s_2loop_at_q(prof, q_gev)
                                if nf_q == 4:
                                    partons_q = evolve_singlet_and_flavour_interval(
                                        at_mc, as_mc, as_q, 4
                                    )
                                else:
                                    partons_q = evolve_singlet_and_flavour_interval(
                                        at_mb, as_mb, as_q, 5
                                    )

                                ev_fl = evaluate_fl_moments_at_scale(partons_q, as_q, nf_q)
                                max_dual_norm_res = max(
                                    max_dual_norm_res, ev_fl["_raw_dual_norm_res"]
                                )
                                max_momentum_sum_res = max(
                                    max_momentum_sum_res, abs(ev_fl["_raw_m2_total"] - mp.mpf(1))
                                )

                                for n in (2, 3, 4):
                                    if ev_fl["_raw_fl"][n] <= mp.mpf(0):
                                        strict_positive_fl_ok = False
                                    r_seq_by_n[n].append(ev_fl["_raw_r"][n])

                                scale_evals[q2_name] = {
                                    "Q2_GeV2": fmt(q_gev ** 2),
                                    "active_nf": nf_q,
                                    "alpha_s_2loop": fmt(as_q),
                                    "moments": ev_fl["moments"],
                                }

                            # Verify UV asymptotic Callan-Gross softening between Q^2=4 and Q^2=20 GeV^2
                            # (same active n_f=4) and between Q^2=100 and Q^2=M_Z^2 (same active n_f=5):
                            for n in (2, 3, 4):
                                seq = r_seq_by_n[n]
                                if not (seq[1] < seq[0] and seq[3] < seq[2]):
                                    monotonic_r_ok = False

                            prof_tables[prof_name] = scale_evals

                        pin_out["branches"][bkey] = prof_tables

            branch_census[pin_name] = pin_out

        return {
            "altarelli_martinelli_kernel_benchmarks": kernel_benchmarks,
            "max_kernel_quadrature_residual": fmt(max_quad_kernel_res),
            "max_singlet_n2_momentum_anomalous_sum_residual": fmt(max_mom_anom_res),
            "max_2pi_vs_4pi_normalization_residual": fmt(max_dual_norm_res),
            "max_evolved_m2_momentum_sum_rule_residual": fmt(max_momentum_sum_res),
            "all_fl_moments_strictly_positive": strict_positive_fl_ok,
            "uv_callan_gross_ratio_monotonic_within_nf_plateaus": monotonic_r_ok,
            "borromean_fl_evolution_census": branch_census,
            "_raw_kernel_res": max_quad_kernel_res,
            "_raw_mom_res": max(max_mom_anom_res, max_momentum_sum_res, max_dual_norm_res),
            "_raw_pos_and_mono": strict_positive_fl_ok and monotonic_r_ok,
        }


# ── Section 4: Worldline Schwinger DIS UV Suppression Across HERA & LHC ──────
def compute_part4_worldline_dis_uv_bounds() -> dict[str, object]:
    """Evaluate 1 - exp(-2 Q^2 T_min) across JLab, HERA, LHC, and trans-Planckian Q^2."""
    with mp.workdps(95):
        e_pl_codata_gev = mp.mpf("1.220890e19")
        e_pl_lean_floor_gev = mp.mpf("1.22e19")
        m_e_gev = M_E_MEV / mp.mpf(1000)

        collider_benchmarks = [
            ("JLab_Q2_4_GeV2", mp.mpf(4), None),
            ("HERA_FL_Q2_20_GeV2", mp.mpf(20), None),
            ("HERA_ceiling_Q2_1e4_GeV2", mp.mpf(10) ** 4, mp.mpf("1.35e-34")),
            ("LHC_ceiling_Q2_1e8_GeV2", mp.mpf(10) ** 8, mp.mpf("1.35e-30")),
            ("UltraHigh_Q2_1e9_GeV2", mp.mpf(10) ** 9, mp.mpf("1.35e-29")),
        ]

        def eval_table_for_e_pl(e_pl_gev: mp.mpf) -> tuple[dict[str, object], bool, mp.mpf]:
            tmin = mp.mpf(1) / (e_pl_gev ** 2)
            rows: dict[str, object] = {}
            bounds_ok = True
            max_prop_sq_res = mp.mpf(0)

            for name, q2_val, ceiling in collider_benchmarks:
                x_arg = mp.mpf(2) * q2_val * tmin
                factor = mp.exp(-x_arg)
                # Cancellation-free evaluation of 1 - exp(-2 Q^2 T_min):
                frac_dev = -mp.expm1(-x_arg)

                g_sw = mp.exp(-q2_val * tmin) / q2_val
                g_cont = mp.mpf(1) / q2_val
                prop_sq_res = abs((g_sw ** 2) / (g_cont ** 2) - factor)
                max_prop_sq_res = max(max_prop_sq_res, prop_sq_res)

                if not (mp.mpf(0) < frac_dev <= x_arg and mp.mpf(0) < factor < mp.mpf(1)):
                    bounds_ok = False
                if ceiling is not None and not (frac_dev < ceiling):
                    bounds_ok = False

                row: dict[str, object] = {
                    "Q2_GeV2": fmt(q2_val),
                    "worldline_damping_factor_exp_neg_2Q2_Tmin": fmt(factor),
                    "fractional_deviation_1_minus_exp": fmt(frac_dev),
                    "linear_envelope_2Q2_Tmin": fmt(x_arg),
                    "envelope_slack_2Q2_Tmin_minus_dev": fmt(x_arg - frac_dev),
                }
                if ceiling is not None:
                    row["lean_certified_upper_bound"] = fmt(ceiling)
                    row["margin_below_lean_bound"] = fmt(ceiling - frac_dev)
                rows[name] = row

            return rows, bounds_ok, max_prop_sq_res

        codata_rows, codata_ok, res_codata = eval_table_for_e_pl(e_pl_codata_gev)
        lean_rows, lean_ok, res_lean = eval_table_for_e_pl(e_pl_lean_floor_gev)

        # Symbolic substrate UV scale M_P^{sym}(q) = (q - 1)^2 / q^{3/2} in electron mass units:
        pins = {
            "q_0_one_term_proton": q_at(95),
            "q_2t_two_term_borromean_proton": q_two_term_borromean_at(95),
            "q_muon_ideal_cal2": q_muon_at(95),
        }
        substrate_symbolic_scales: dict[str, object] = {}
        for pin_name, q_val in pins.items():
            mp_sym_over_me = ((q_val - mp.mpf(1)) ** 2) / (q_val ** (mp.mpf(3) / mp.mpf(2)))
            e_star_sym_gev = m_e_gev * mp_sym_over_me
            tmin_sym = mp.mpf(1) / (e_star_sym_gev ** 2)
            dev_hera = -mp.expm1(-mp.mpf(2) * (mp.mpf(10) ** 4) * tmin_sym)
            dev_lhc = -mp.expm1(-mp.mpf(2) * (mp.mpf(10) ** 8) * tmin_sym)
            substrate_symbolic_scales[pin_name] = {
                "M_P_sym_over_m_e": fmt(mp_sym_over_me),
                "E_star_sym_GeV": fmt(e_star_sym_gev),
                "HERA_Q2_1e4_fractional_deviation": fmt(dev_hera),
                "LHC_Q2_1e8_fractional_deviation": fmt(dev_lhc),
            }

        # Trans-Planckian ghost-free UV damping check (Q^2 / E_Pl^2 in {1/10, 1, 10})
        trans_planckian: dict[str, object] = {}
        trans_ok = True
        for label, ratio_q2 in (
            ("Q2_0p1_EPl2", mp.mpf(1) / mp.mpf(10)),
            ("Q2_1_EPl2", mp.mpf(1)),
            ("Q2_10_EPl2", mp.mpf(10)),
        ):
            fac = mp.exp(-mp.mpf(2) * ratio_q2)
            dev = -mp.expm1(-mp.mpf(2) * ratio_q2)
            if not (mp.mpf(0) < fac < mp.mpf(1) and mp.mpf(0) < dev < mp.mpf(1)):
                trans_ok = False
            trans_planckian[label] = {
                "Q2_over_E_Pl_sq": fmt(ratio_q2),
                "worldline_cross_section_factor": fmt(fac),
                "fractional_uv_suppression": fmt(dev),
            }

        return {
            "E_Pl_CODATA_GeV": fmt(e_pl_codata_gev),
            "E_Pl_Lean_floor_GeV": fmt(e_pl_lean_floor_gev),
            "codata_planck_collider_evaluations": codata_rows,
            "lean_floor_planck_collider_evaluations": lean_rows,
            "substrate_symbolic_planck_evaluations": substrate_symbolic_scales,
            "trans_planckian_ghost_free_damping": trans_planckian,
            "max_propagator_square_identity_residual": fmt(max(res_codata, res_lean)),
            "all_hera_lhc_bounds_satisfied": codata_ok and lean_ok and trans_ok,
            "_raw_prop_sq_res": max(res_codata, res_lean),
            "_raw_bounds_ok": codata_ok and lean_ok and trans_ok,
        }


# ── Section 5: Witness Assembly & Main Entrypoint ────────────────────────────
def main() -> int:
    with mp.workdps(95):
        part1 = compute_part1_clifford_and_traces()
        part2 = compute_part2_spin_half_vs_spin_zero_callan_gross()
        part3 = compute_part3_fl_mellin_moments()
        part4 = compute_part4_worldline_dis_uv_bounds()

        wb = WitnessBuilder(
            "dirac-callan-gross-and-dis-cross-section",
            engine="mpmath",
        )
        wb.set_description(
            "80-dps verification of chiral Weyl-Dirac Clifford algebra and 256-component "
            "4-gamma traces, spin-1/2 1+(1-y)^2 vs spin-0 2(1-y) DIS contractions and "
            "Callan-Gross relation F_2 = 2x F_1, 1-loop QCD longitudinal F_L Mellin moments "
            "(n = 2, 3, 4) evolved from QOU Borromean proton moments, and worldline "
            "1 - exp(-2 Q^2 / E_Pl^2) UV bounds across HERA and LHC."
        )

        # Assertion 1: Chiral Weyl-Dirac Clifford algebra & all 256 4-gamma traces exact to >88 dps
        wb.add_assertion(
            name="chiral_weyl_dirac_clifford_and_256_four_gamma_traces_88dps",
            computed=fmt(part1["_raw_worst_residual"]),
            expected="0",
            tolerance="1e-88",
            source="DiracWeylCliffordCallanGrossAndDISCrossSection.lean §1 (sigmaVec_sigmaBarVec_clifford, trace_diracGamma_two_and_four)",
        )

        # Assertion 2: Spin-1/2 1+(1-y)^2 vs spin-0 2(1-y) contraction & backward y=1 discrimination
        spin_disc_ok = (
            part2["_raw_worst_residual"] < mp.mpf("1e-88")
            and part2["_raw_backward_spin_half"] == mp.mpf(1)
            and part2["_raw_backward_spin_zero"] == mp.mpf(0)
        )
        wb.add_assertion(
            name="spin_half_1_plus_1_minus_y_sq_vs_spin_zero_2_times_1_minus_y_and_callan_gross_exact",
            computed="1" if spin_disc_ok else "0",
            expected="1",
            tolerance="0",
            source="DiracWeylCliffordCallanGrossAndDISCrossSection.lean §2 (partonic_spinHalf_vs_spinZero_and_callan_gross)",
        )

        # Assertion 3: Altarelli-Martinelli 1-loop F_L Mellin kernel quadrature (n=2,3,4) exact to >85 dps
        wb.add_assertion(
            name="altarelli_martinelli_1loop_fl_kernel_quadrature_n2_n3_n4_85dps",
            computed=fmt(part3["_raw_kernel_res"]),
            expected="0",
            tolerance="1e-85",
            source="Altarelli & Martinelli (1978, Phys. Lett. B 76, 89) & DiracWeylCliffordCallanGrossAndDISCrossSection.lean §2",
        )

        # Assertion 4: Evolved Borromean proton F_L Mellin moments (n=2,3,4) positivity, momentum sum rule, & UV softening
        fl_evol_ok = (
            part3["_raw_mom_res"] < mp.mpf("1e-85") and bool(part3["_raw_pos_and_mono"])
        )
        wb.add_assertion(
            name="borromean_proton_evolved_fl_mellin_moments_positivity_and_uv_softening",
            computed="1" if fl_evol_ok else "0",
            expected="1",
            tolerance="0",
            source="1-loop singlet/non-singlet DGLAP evolution of QOU Borromean [u,u,d] moments across Q^2 in {4, 20, 100, M_Z^2} GeV^2",
        )

        # Assertion 5: Worldline Schwinger DIS UV bounds 1 - exp(-2 Q^2 / E_Pl^2) across HERA & LHC
        uv_ok = (
            part4["_raw_prop_sq_res"] < mp.mpf("1e-88") and bool(part4["_raw_bounds_ok"])
        )
        wb.add_assertion(
            name="worldline_schwinger_dis_uv_hera_and_lhc_planck_bounds_certified",
            computed="1" if uv_ok else "0",
            expected="1",
            tolerance="0",
            source="DiracWeylCliffordCallanGrossAndDISCrossSection.lean §3 (dis_worldline_hera_lhc_planck_bounds)",
        )

        clean_part1 = {k: v for k, v in part1.items() if not k.startswith("_")}
        clean_part2 = {k: v for k, v in part2.items() if not k.startswith("_")}
        clean_part3 = {k: v for k, v in part3.items() if not k.startswith("_")}
        clean_part4 = {k: v for k, v in part4.items() if not k.startswith("_")}

        wb.add_data(
            "lean_companion_module",
            "folio/quantum-observable-universe/lean/QOU/StandardModel/"
            "DiracWeylCliffordCallanGrossAndDISCrossSection.lean",
        )
        wb.add_data("part1_chiral_weyl_dirac_clifford_and_traces", clean_part1)
        wb.add_data("part2_spin_half_vs_spin_zero_and_callan_gross", clean_part2)
        wb.add_data("part3_one_loop_qcd_fl_mellin_moments_from_borromean_proton", clean_part3)
        wb.add_data("part4_worldline_schwinger_dis_uv_bounds", clean_part4)

        q0_proton = q_at(95)
        q0_muon = q_muon_at(95)
        out_path = wb.save(
            q0_comparison(
                muon=q0_muon,
                proton=q0_proton,
                reason=(
                    "Evaluates q-independent chiral Weyl-Dirac Clifford traces, Callan-Gross "
                    "partonic contractions, and Planck worldline UV bounds alongside 1-loop QCD "
                    "longitudinal F_L Mellin moments evolved from QOU Borromean proton moments "
                    "side-by-side across {q_0, q_2t, q_muon}."
                ),
                dps=80,
            )
        )

        hera_dev = clean_part4["codata_planck_collider_evaluations"]["HERA_ceiling_Q2_1e4_GeV2"][
            "fractional_deviation_1_minus_exp"
        ]
        lhc_dev = clean_part4["codata_planck_collider_evaluations"]["LHC_ceiling_Q2_1e8_GeV2"][
            "fractional_deviation_1_minus_exp"
        ]
        print(f"Wrote witness: {out_path}")
        print(f"  4-gamma 256-trace max residual : {clean_part1['max_four_gamma_trace_256_residual']}")
        print(f"  F_L kernel quadrature residual : {clean_part3['max_kernel_quadrature_residual']}")
        print(f"  HERA Q^2=10^4 worldline dev    : {hera_dev[:28]}... (< 1.35e-34)")
        print(f"  LHC  Q^2=10^8 worldline dev    : {lhc_dev[:28]}... (< 1.35e-30)")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
