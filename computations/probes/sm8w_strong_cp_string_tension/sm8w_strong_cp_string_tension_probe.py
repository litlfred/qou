#!/usr/bin/env python3
"""Pre-registered 80-dps probe for Standard Model Package 5 (`qou-tcpx` / `Q-Gap-11`):
Strong-CP `theta_bar_QCD = 0` Colour-Singlet Writhe & Hermitian Determinant Cancellation,
and `SU(3)_c` Markov-Trace / Casimir Wilson String Tension Candidates.

EXPLORATORY shape-probe & exact algebraic witness corresponding to:
- Pre-registration: `computations/probes/sm8w_strong_cp_string_tension/PREREGISTRATION.md`
- Lean 4 module: `folio/quantum-observable-universe/lean/QOU/StandardModel/StrongCPWritheCancellationAndStringTension.lean`

STRICT PRECISION & ANTI-FIT DISCIPLINE:
- `mpmath` at `workdps = 80` (`OUT_DPS = 50` serialized decimal strings).
- ZERO `float64` imports (`math`, `numpy`, `cmath`, `scipy`, `statistics` banned),
  ZERO `float(...)` or `complex(...)` calls, ZERO binary64 literals.
- `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`), `CAL-1` `m_e`, `CAL-3` `m_{pi+-}`.
- Empirical bounds (`PDG-2024` `|theta_bar_QCD| < 1e-10`, `|d_n| < 1.8e-26 e*cm`,
  lattice/Regge `sqrt(sigma) in [420, 440] MeV`) enter strictly as downstream comparison
  targets; all hits and misses are reported verbatim with `selected = "none"` (Rule 14).
"""

from __future__ import annotations

import pathlib
import sys
from fractions import Fraction

_ROOT = pathlib.Path(__file__).resolve().parents[3]
for _rel in ("tools/qou-substrate/python", "computations"):
    _p = str(_ROOT / _rel)
    if _p not in sys.path:
        sys.path.insert(0, _p)

from mpmath import mp, mpc, mpf, workdps  # noqa: E402
from qou_substrate.codata import value_str  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

WORK_DPS = 80
OUT_DPS = 50
mp.dps = WORK_DPS
set_compute_dps(WORK_DPS)


# =============================================================================
# 3x3 Arbitrary-Precision Complex Matrix Helpers (Pure mpmath, Zero float64)
# =============================================================================

Mat3 = list[list[mpc]]


def mat3_zero() -> Mat3:
    z = mpc(0, 0)
    return [[z, z, z], [z, z, z], [z, z, z]]


def mat3_eye() -> Mat3:
    z = mpc(0, 0)
    one = mpc(1, 0)
    return [[one, z, z], [z, one, z], [z, z, one]]


def mat3_diag(d0: mpf, d1: mpf, d2: mpf) -> Mat3:
    z = mpc(0, 0)
    return [[mpc(d0, 0), z, z], [z, mpc(d1, 0), z], [z, z, mpc(d2, 0)]]


def mat3_add(a: Mat3, b: Mat3) -> Mat3:
    return [[a[i][j] + b[i][j] for j in range(3)] for i in range(3)]


def mat3_sub(a: Mat3, b: Mat3) -> Mat3:
    return [[a[i][j] - b[i][j] for j in range(3)] for i in range(3)]


def mat3_scale(c: mpc, a: Mat3) -> Mat3:
    return [[c * a[i][j] for j in range(3)] for i in range(3)]


def mat3_dagger(a: Mat3) -> Mat3:
    return [[mp.conj(a[j][i]) for j in range(3)] for i in range(3)]


def mat3_mul(a: Mat3, b: Mat3) -> Mat3:
    out = mat3_zero()
    for i in range(3):
        for j in range(3):
            acc = mpc(0, 0)
            for k in range(3):
                acc += a[i][k] * b[k][j]
            out[i][j] = acc
    return out


def mat3_comm(a: Mat3, b: Mat3) -> Mat3:
    return mat3_sub(mat3_mul(a, b), mat3_mul(b, a))


def mat3_trace(a: Mat3) -> mpc:
    return a[0][0] + a[1][1] + a[2][2]


def mat3_det(a: Mat3) -> mpc:
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def mat3_max_abs(a: Mat3) -> mpf:
    best = mpf(0)
    for i in range(3):
        for j in range(3):
            val = abs(a[i][j])
            if val > best:
                best = val
    return best


def mat3_inv(a: Mat3) -> Mat3:
    """Exact cofactor / adjugate inverse of a 3x3 mpc matrix at full working precision."""
    d = mat3_det(a)
    cof = mat3_zero()
    for i in range(3):
        i1 = (i + 1) % 3
        i2 = (i + 2) % 3
        for j in range(3):
            j1 = (j + 1) % 3
            j2 = (j + 2) % 3
            # Cofactor transposed -> adjugate entry (j, i)
            cof[j][i] = (a[i1][j1] * a[i2][j2] - a[i1][j2] * a[i2][j1]) / d
    return cof


def build_chau_keung_ckm(s12: mpf, s23: mpf, s13: mpf, delta: mpf) -> Mat3:
    """Standard Chau-Keung 3x3 unitary CKM matrix from sines and CP phase delta."""
    one = mpf(1)
    c12 = mp.sqrt(one - s12 * s12)
    c23 = mp.sqrt(one - s23 * s23)
    c13 = mp.sqrt(one - s13 * s13)
    ep = mp.exp(mpc(0, 1) * delta)
    em = mp.exp(mpc(0, -1) * delta)
    return [
        [mpc(c12 * c13, 0), mpc(s12 * c13, 0), mpc(s13, 0) * em],
        [
            mpc(-s12 * c23, 0) - mpc(c12 * s23 * s13, 0) * ep,
            mpc(c12 * c23, 0) - mpc(s12 * s23 * s13, 0) * ep,
            mpc(s23 * c13, 0),
        ],
        [
            mpc(s12 * s23, 0) - mpc(c12 * c23 * s13, 0) * ep,
            mpc(-c12 * s23, 0) - mpc(s12 * c23 * s13, 0) * ep,
            mpc(c23 * c13, 0),
        ],
    ]


def cayley_unitary_from_hermitian(h_mat: Mat3) -> Mat3:
    """Exact Cayley transform U = (I - i H)(I + i H)^{-1}, unitary to full working dps."""
    eye = mat3_eye()
    ih = mat3_scale(mpc(0, 1), h_mat)
    num = mat3_sub(eye, ih)
    den_inv = mat3_inv(mat3_add(eye, ih))
    return mat3_mul(num, den_inv)


# =============================================================================
# Braid Writhe, Levi-Civita Singlet & SU(3)_c Casimir Exact Helpers
# =============================================================================

def levi_civita_3(i: int, j: int, k: int) -> int:
    triple = (i, j, k)
    if triple in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
        return 1
    if triple in ((0, 2, 1), (2, 1, 0), (1, 0, 2)):
        return -1
    return 0


def q_int_bal(q: mpf, n: int) -> mpf:
    one = mpf(1)
    qinv = one / q
    if q == one:
        return mpf(n)
    return (q ** n - qinv ** n) / (q - qinv)


def markov_z3(q: mpf) -> mpf:
    one = mpf(1)
    return (q ** 3) / (q ** 2 + one + one / (q ** 2))


def markov_z3_sym(q: mpf) -> mpf:
    one = mpf(1)
    return one / (q ** 2 + one + one / (q ** 2))


def markov_z3_neg(q: mpf) -> mpf:
    one = mpf(1)
    return (one / (q ** 3)) / (q ** 2 + one + one / (q ** 2))


def vol_4_1_80dps() -> mpf:
    """Hyperbolic figure-eight volume Vol(4_1) = 2 * Cl_2(pi/3) = 2 * Im Li_2(e^{i pi/3})."""
    z = mp.exp(mpc(0, 1) * (mp.pi / mpf(3)))
    return mpf(2) * mp.polylog(2, z).imag


def proton_electron_ratio_qou(q: mpf) -> mpf:
    """Canonical QOU Borromean proton-electron ratio 2*(Vol(4_1)/hbar_q^2)*F_Bor(q) - 12."""
    one = mpf(1)
    hbar_q = one - one / q
    h = q - one / q
    tr_m_bor = (mpf(4) + h ** 2 - mpf(3) * (h ** 4) - h ** 6) / (h ** 2 + mpf(4))
    q3_fact = (q + one / q) * (q ** 2 + one + one / (q ** 2))
    f_bor = abs(tr_m_bor) * q3_fact / (q ** 3)
    return mpf(2) * (vol_4_1_80dps() / (hbar_q ** 2)) * f_bor - mpf(12)


def main() -> int:
    with workdps(WORK_DPS):
        one = mpf(1)
        tol_exact = mpf("1e-78")
        tol_rel = mpf("1e-70")

        # ── Substrate & Calibration Constants (CAL-1, proton q_0, CAL-3) ──
        q0 = q_at(WORK_DPS)
        h0 = q0 - one / q0
        q2_0 = q_int_bal(q0, 2)
        q3_0 = q_int_bal(q0, 3)

        m_e_mev_str = value_str("electron mass energy equivalent in MeV")
        m_e_mev = mpf(m_e_mev_str)
        mp_me_codata = mpf(value_str("proton-electron mass ratio"))
        r_p_codata_fm = mpf(value_str("proton rms charge radius")) * mpf("1e15")
        # Exact 80-dps SI-2019 hbar*c [MeV*fm] = (h * c * 10^9) / (2 * pi * e)
        h_si = mpf(value_str("Planck constant"))
        c_si = mpf(value_str("speed of light in vacuum"))
        e_si = mpf(value_str("elementary charge"))
        hbar_c_mev_fm = (h_si * c_si * mpf("1e9")) / (mpf(2) * mp.pi * e_si)
        alpha_em_inv = mpf(value_str("inverse fine-structure constant"))
        alpha_em = one / alpha_em_inv
        g_f_gev_inv2 = mpf(value_str("Fermi coupling constant"))
        sin2_tw = mpf(value_str("weak mixing angle"))

        mp_me_qou = proton_electron_ratio_qou(q0)
        m_p_qou_mev = m_e_mev * mp_me_qou
        mp_anchor_err = abs(mp_me_qou - mp_me_codata)

        # CAL-3 charged pion mass (MeV)
        m_pi_mev_str = "139.57039"
        m_pi_mev = mpf(m_pi_mev_str)

        # =====================================================================
        # ARM A1: Topological Writhe Cancellation & [1^3] Singlet Invariance
        # =====================================================================
        fig8_word = [(0, True), (1, False), (0, True), (1, False)]
        bor_word = [(0, True), (1, False)] * 3
        t29_word = [(0, True)] * 9
        t29_mirror = [(idx, not pos) for (idx, pos) in t29_word]

        def writhe(word: list[tuple[int, bool]]) -> int:
            return sum(1 if pos else -1 for (_, pos) in word)

        def perm_sign_3(word: list[tuple[int, bool]]) -> int:
            p = [0, 1, 2]
            for idx, _ in word:
                p[idx], p[idx + 1] = p[idx + 1], p[idx]
            inv = 0
            for a in range(3):
                for b in range(a + 1, 3):
                    if p[a] > p[b]:
                        inv += 1
            return -1 if (inv % 2 == 1) else 1

        w_fig8 = writhe(fig8_word)
        w_bor = writhe(bor_word)
        w_t29 = writhe(t29_word)
        w_t29_mir = writhe(t29_mirror)
        w_t29_pair = writhe(t29_word + t29_mirror)

        # Single T(2,9) framing asymmetry vs mirror-paired exact cancellation at q_0
        single_t29_cp_asym = abs(q0 ** w_t29 - q0 ** (-w_t29))
        paired_t29_phase_err = abs(q0 ** w_t29_pair - one)

        # Exact 27x27 rational Levi-Civita projector P_{(1^3)} = (1/6) |eps><eps|
        eps_vec = [
            Fraction(levi_civita_3(i, j, k), 1)
            for i in range(3)
            for j in range(3)
            for k in range(3)
        ]
        eps_norm_sq = sum(v * v for v in eps_vec)
        proj_sing = [
            [eps_vec[a] * eps_vec[b] / Fraction(6, 1) for b in range(27)]
            for a in range(27)
        ]
        proj_tr = sum(proj_sing[a][a] for a in range(27))
        proj_idem_ok = all(
            sum(proj_sing[a][c] * proj_sing[c][b] for c in range(27)) == proj_sing[a][b]
            for a in range(27)
            for b in range(27)
        )

        # Non-trivial SL_3(Z) test matrix g with det(g) = 1 and traceless A in sl_3(Z)
        g_sl3 = [[1, 2, -1], [0, 1, 3], [2, 5, 4]]  # det = 1*(4-15) - 2*(0-6) - 1*(0-2) = -11 + 12 + 2 = 3? Wait: fix entry (2,2)!
        # Let's use unipotent product L * U with guaranteed det = 1:
        # L = [[1,0,0],[2,1,0],[-1,3,1]], U = [[1,2,-1],[0,1,2],[0,0,1]] -> det(L*U) = 1
        g_sl3 = [
            [1, 2, -1],
            [2, 5, 0],
            [-1, 1, 8],
        ]
        det_g_sl3 = (
            g_sl3[0][0] * (g_sl3[1][1] * g_sl3[2][2] - g_sl3[1][2] * g_sl3[2][1])
            - g_sl3[0][1] * (g_sl3[1][0] * g_sl3[2][2] - g_sl3[1][2] * g_sl3[2][0])
            + g_sl3[0][2] * (g_sl3[1][0] * g_sl3[2][1] - g_sl3[1][1] * g_sl3[2][0])
        )
        sl3_singlet_ok = (det_g_sl3 == 1) and all(
            sum(
                g_sl3[i][a] * g_sl3[j][b] * g_sl3[k][c] * levi_civita_3(a, b, c)
                for a in range(3)
                for b in range(3)
                for c in range(3)
            )
            == levi_civita_3(i, j, k)
            for i in range(3)
            for j in range(3)
            for k in range(3)
        )

        a_sl3 = [[2, -3, 1], [4, -5, 2], [-1, 2, 3]]  # tr = 2 - 5 + 3 = 0
        su3_lie_singlet_ok = (a_sl3[0][0] + a_sl3[1][1] + a_sl3[2][2] == 0) and all(
            sum(
                a_sl3[i][a] * levi_civita_3(a, j, k)
                + a_sl3[j][a] * levi_civita_3(i, a, k)
                + a_sl3[k][a] * levi_civita_3(i, j, a)
                for a in range(3)
            )
            == 0
            for i in range(3)
            for j in range(3)
            for k in range(3)
        )

        # Balanced [1^3] parity check across odd and even 3-strand words
        test_words_b3 = [
            fig8_word,
            bor_word,
            t29_word,
            [(0, True), (1, True), (0, False)],
            [(1, False), (0, True), (1, True), (0, True), (1, False)],
        ]
        balanced_parity_ok = all(
            ((-1 if (writhe(w) % 2 != 0) else 1) * perm_sign_3(w)) == 1
            for w in test_words_b3
        )

        # =====================================================================
        # ARM A2: 3x3 Hermitian Quark Mass Matrices with J_CP ~ 2.6e-5 & theta=0
        # =====================================================================
        # Zero-parameter substrate braiding test angles (PREREGISTRATION §2.A2)
        s12_sub = h0
        s23_sub = h0 ** 2
        s13_sub = (h0 ** 3) / q2_0
        delta_sub = mp.pi / mpf(3)

        v_sub = build_chau_keung_ckm(s12_sub, s23_sub, s13_sub, delta_sub)
        v_unitarity_err = mat3_max_abs(
            mat3_sub(mat3_mul(mat3_dagger(v_sub), v_sub), mat3_eye())
        )
        j_cp_plaquette = (
            v_sub[0][1] * v_sub[1][2] * mp.conj(v_sub[0][2]) * mp.conj(v_sub[1][1])
        ).imag
        c12_sub = mp.sqrt(one - s12_sub ** 2)
        c23_sub = mp.sqrt(one - s23_sub ** 2)
        c13_sub = mp.sqrt(one - s13_sub ** 2)
        j_cp_formula = (
            c12_sub
            * s12_sub
            * c23_sub
            * s23_sub
            * (c13_sub ** 2)
            * s13_sub
            * mp.sin(delta_sub)
        )
        j_cp_formula_err = abs(j_cp_plaquette - j_cp_formula)

        # Positive Yukawa eigenvalues & dense complex Cayley basis rotation U_0
        u_eigs = [h0 ** 6, h0 ** 3, one]
        d_eigs = [h0 ** 5, (h0 ** 3) / q3_0, h0]
        d_u_diag = mat3_diag(u_eigs[0], u_eigs[1], u_eigs[2])
        d_d_diag = mat3_diag(d_eigs[0], d_eigs[1], d_eigs[2])

        h_rot = [
            [mpc(0, 0), mpc(mpf("1") / mpf("3"), mpf("1") / mpf("5")), mpc(mpf("-1") / mpf("7"), mpf("2") / mpf("9"))],
            [mpc(mpf("1") / mpf("3"), mpf("-1") / mpf("5")), mpc(0, 0), mpc(mpf("1") / mpf("4"), mpf("-1") / mpf("6"))],
            [mpc(mpf("-1") / mpf("7"), mpf("-2") / mpf("9")), mpc(mpf("1") / mpf("4"), mpf("1") / mpf("6")), mpc(0, 0)],
        ]
        u0 = cayley_unitary_from_hermitian(h_rot)
        u0_dag = mat3_dagger(u0)
        u0_unitarity_err = mat3_max_abs(mat3_sub(mat3_mul(u0_dag, u0), mat3_eye()))

        m_u_sub = mat3_mul(mat3_mul(u0_dag, d_u_diag), u0)
        m_d_in_u_basis = mat3_mul(mat3_mul(v_sub, d_d_diag), mat3_dagger(v_sub))
        m_d_sub = mat3_mul(mat3_mul(u0_dag, m_d_in_u_basis), u0)

        herm_err_u = mat3_max_abs(mat3_sub(m_u_sub, mat3_dagger(m_u_sub)))
        herm_err_d = mat3_max_abs(mat3_sub(m_d_sub, mat3_dagger(m_d_sub)))
        max_offdiag_im_u = max(
            abs(m_u_sub[i][j].imag) for i in range(3) for j in range(3) if i != j
        )
        max_offdiag_im_d = max(
            abs(m_d_sub[i][j].imag) for i in range(3) for j in range(3) if i != j
        )

        prod_ud = mat3_mul(m_u_sub, m_d_sub)
        # Note: M_u * M_d itself is non-Hermitian because [M_u, M_d] != 0
        non_herm_prod_ud = mat3_max_abs(mat3_sub(prod_ud, mat3_dagger(prod_ud)))
        det_prod_ud = mat3_det(prod_ud)
        det_prod_expected_re = (
            u_eigs[0] * u_eigs[1] * u_eigs[2] * d_eigs[0] * d_eigs[1] * d_eigs[2]
        )
        im_det_ud = abs(det_prod_ud.imag)
        re_det_ud_rel_err = abs(det_prod_ud.real - det_prod_expected_re) / det_prod_expected_re
        theta_tree_rad = abs(mp.arg(det_prod_ud))

        # Basis-invariant Jarlskog commutator Tr([M_u^2, M_d^2]^3) in rotated basis
        m_u_sq = mat3_mul(m_u_sub, m_u_sub)
        m_d_sq = mat3_mul(m_d_sub, m_d_sub)
        comm_sq = mat3_comm(m_u_sq, m_d_sq)
        comm_cube = mat3_mul(mat3_mul(comm_sq, comm_sq), comm_sq)
        tr_comm_cube = mat3_trace(comm_cube)

        vand_u_sq = (
            (u_eigs[0] ** 2 - u_eigs[1] ** 2)
            * (u_eigs[1] ** 2 - u_eigs[2] ** 2)
            * (u_eigs[2] ** 2 - u_eigs[0] ** 2)
        )
        vand_d_sq = (
            (d_eigs[0] ** 2 - d_eigs[1] ** 2)
            * (d_eigs[1] ** 2 - d_eigs[2] ** 2)
            * (d_eigs[2] ** 2 - d_eigs[0] ** 2)
        )
        # By Jarlskog's identity: Im Tr([M_u^2, M_d^2]^3) = 6 * vand_u_sq * vand_d_sq * J_CP
        im_tr_expected = mpf(6) * vand_u_sq * vand_d_sq * j_cp_plaquette
        jarlskog_comm_rel_err = abs(tr_comm_cube.imag - im_tr_expected) / abs(im_tr_expected)

        # Cross-check exact integer Lean witness (witnessMu, witnessMd)
        w_mu = mat3_diag(mpf(1), mpf(2), mpf(3))
        w_md = [
            [mpc(4, 0), mpc(1, 0), mpc(0, 1)],
            [mpc(1, 0), mpc(4, 0), mpc(1, 0)],
            [mpc(0, -1), mpc(1, 0), mpc(4, 0)],
        ]
        w_det_prod = mat3_det(mat3_mul(w_mu, w_md))
        w_comm = mat3_comm(mat3_mul(w_mu, w_mu), mat3_mul(w_md, w_md))
        w_tr_cube = mat3_trace(mat3_mul(mat3_mul(w_comm, w_comm), w_comm))

        # =====================================================================
        # ARM A3: 1-Loop Chiral Dressing Reality & 3-Loop Ellis-Gaillard Bound
        # =====================================================================
        eps_1loop = alpha_em / (mpf(4) * mp.pi * sin2_tw)
        sigma_l_1loop = mat3_scale(mpc(eps_1loop, 0), m_d_sq)
        h_l_factor = mat3_add(mat3_eye(), sigma_l_1loop)
        m_u_1loop = mat3_mul(h_l_factor, m_u_sub)
        m_u_1loop_non_herm = mat3_max_abs(mat3_sub(m_u_1loop, mat3_dagger(m_u_1loop)))
        det_1loop_prod = mat3_det(mat3_mul(m_u_1loop, m_d_sub))
        im_det_1loop = abs(det_1loop_prod.imag)

        # Ellis-Gaillard 3-loop electroweak + QCD estimate (PDG comparison constants ONLY)
        alpha_s_mz_ref = mpf("0.1180")
        m_c_gev_ref = mpf("1.273")
        m_s_gev_ref = mpf("0.0935")
        m_w_gev_ref = mpf("80.3692")
        j_cp_pdg_ref = mpf("3.08e-5")

        delta_theta_ew_eg_sub = (
            (alpha_s_mz_ref / mp.pi)
            * ((alpha_em / (mpf(4) * mp.pi * sin2_tw)) ** 2)
            * ((m_c_gev_ref ** 2) * (m_s_gev_ref ** 2) / (m_w_gev_ref ** 4))
            * j_cp_plaquette
            * mp.log((m_w_gev_ref ** 2) / (m_c_gev_ref ** 2))
        )
        delta_theta_ew_env = (
            ((alpha_em / mp.pi) ** 2)
            * (g_f_gev_inv2 ** 2)
            * (m_c_gev_ref ** 2)
            * (m_s_gev_ref ** 2)
            * j_cp_pdg_ref
        )
        # Neutron EDM proportionality |d_n| ~ 2.4e-16 * |theta_bar| e*cm (Pospelov-Ritz)
        dn_coeff_ecm = mpf("2.4e-16")
        dn_ew_eg_ecm = dn_coeff_ecm * abs(delta_theta_ew_eg_sub)
        dn_ew_env_ecm = dn_coeff_ecm * abs(delta_theta_ew_env)
        pdg_theta_bound = mpf("1e-10")
        pdg_dn_bound_ecm = mpf("1.8e-26")

        # =====================================================================
        # ARM B: SU(3)_c Casimir Scaling & Zero-Parameter String Tension sqrt(sigma)
        # =====================================================================
        c2_singlet = Fraction(0, 1)
        c2_fund = Fraction(4, 3)
        c2_sextet = Fraction(10, 3)
        c2_adj = Fraction(3, 1)
        c2_decuplet = Fraction(6, 1)
        casimir_ratio_adj_fund = c2_adj / c2_fund  # 9/4
        baryon_pair_factor = Fraction(c2_singlet - 3 * c2_fund, 6)  # -2/3
        meson_singlet_factor = Fraction(c2_singlet - 2 * c2_fund, 2)  # -4/3

        z3_q0 = markov_z3(q0)
        z3_sym_q0 = markov_z3_sym(q0)
        z3_neg_q0 = markov_z3_neg(q0)

        sigma_hat_pos = -mp.log(z3_q0)
        sigma_hat_sym = -mp.log(z3_sym_q0)  # = ln([3]_{q_0})
        sigma_hat_neg = -mp.log(z3_neg_q0)

        # Creutz ratio perimeter-cancellation check across (R, T) in {(1,1), (2,3), (4,5)}
        c0_test = mpf("1.7320508075688772")
        p_perim_test = mpf("0.8319472615")

        def wilson_rect(r_len: int, t_len: int) -> mpf:
            return (
                c0_test
                * (p_perim_test ** (2 * (r_len + t_len)))
                * (z3_q0 ** (r_len * t_len))
            )

        creutz_max_err = max(
            abs(
                (wilson_rect(r_l + 1, t_l + 1) * wilson_rect(r_l, t_l))
                / (wilson_rect(r_l + 1, t_l) * wilson_rect(r_l, t_l + 1))
                - z3_q0
            )
            for (r_l, t_l) in ((1, 1), (2, 3), (4, 5))
        )

        # Logarithmic q-slopes d ln(sqrt(sigma_hat)) / d ln q at q_0 via central finite diff
        dq = mpf("1e-20")

        def dln_sqrt_sigma_dlnq(step_fn) -> mpf:
            f_plus = mp.sqrt(-mp.log(step_fn(q0 + dq)))
            f_minus = mp.sqrt(-mp.log(step_fn(q0 - dq)))
            f_mid = mp.sqrt(-mp.log(step_fn(q0)))
            return (q0 / f_mid) * ((f_plus - f_minus) / (mpf(2) * dq))

        qslope_pos = dln_sqrt_sigma_dlnq(markov_z3)
        qslope_sym = dln_sqrt_sigma_dlnq(markov_z3_sym)

        # Lattice / Regge comparison band (strictly external comparison!)
        lat_low_mev = mpf("420")
        lat_high_mev = mpf("440")
        lat_mid_mev = mpf("430")
        regge_alpha_prime_gev_inv2 = mpf("0.88")
        sqrt_sigma_regge_mev = mpf("1000") / mp.sqrt(
            mpf(2) * mp.pi * regge_alpha_prime_gev_inv2
        )

        # Pre-registered candidate table (PREREGISTRATION §3)
        candidates_spec = [
            ("S1_pi_bare", sigma_hat_pos, m_pi_mev, qslope_pos, False, "a = lambda_pi = 1/m_pi (CAL-3)"),
            ("S2_pi_nc3", sigma_hat_pos, mpf(3) * m_pi_mev, qslope_pos, False, "a = lambda_pi / 3 (N_c=3 pion subcell)"),
            ("S3_pi_nc3_sym", sigma_hat_sym, mpf(3) * m_pi_mev, qslope_sym, False, "a = lambda_pi / 3 with bar-sym [3]_q^-1"),
            ("S4_mp_compton", sigma_hat_pos, m_p_qou_mev, qslope_pos, False, "a = lambda_p = 1/m_p(q_0)"),
            ("S5a_rp_full", sigma_hat_pos, m_p_qou_mev / mpf(4), qslope_pos, False, "a = r_{p,QOU} = 4/m_p(q_0)"),
            ("S5b_rp_half", sigma_hat_pos, m_p_qou_mev / mpf(2), qslope_pos, False, "a = r_{p,QOU}/2 = 2/m_p(q_0)"),
            ("S6_rp_half_sym", sigma_hat_sym, m_p_qou_mev / mpf(2), qslope_sym, False, "a = r_{p,QOU}/2 with bar-sym [3]_q^-1"),
            (
                "S7_diag_codata_rp_half",
                sigma_hat_pos,
                (mpf(2) * hbar_c_mev_fm) / r_p_codata_fm,
                qslope_pos,
                True,
                "Diagnostic only: a = r_{p,CODATA}/2",
            ),
        ]

        candidates_out: dict[str, dict[str, object]] = {}
        in_band_ids: list[str] = []
        near_15pct_ids: list[str] = []
        miss_ids: list[str] = []

        for cid, shat, inv_a_mev, qslope, is_diag, note in candidates_spec:
            sqrt_sig_3 = inv_a_mev * mp.sqrt(shat)
            sqrt_sig_8 = (mpf(3) / mpf(2)) * sqrt_sig_3
            a_fm = hbar_c_mev_fm / inv_a_mev
            sig_gev2 = (sqrt_sig_3 / mpf(1000)) ** 2
            alpha_prime_cand = one / (mpf(2) * mp.pi * sig_gev2)
            rel_vs_430 = (sqrt_sig_3 - lat_mid_mev) / lat_mid_mev
            pct_vs_430 = mpf(100) * rel_vs_430

            if lat_low_mev <= sqrt_sig_3 <= lat_high_mev:
                verdict = "IN_BAND"
                if not is_diag:
                    in_band_ids.append(cid)
            elif abs(rel_vs_430) <= mpf("0.15"):
                verdict = "NEAR_15PCT"
                if not is_diag:
                    near_15pct_ids.append(cid)
            else:
                verdict = "MISS"
                if not is_diag:
                    miss_ids.append(cid)

            candidates_out[cid] = {
                "isDiagnosticOnly": bool(is_diag),
                "spacingNote": note,
                "aCalFm": fmt(a_fm, dps=OUT_DPS),
                "invACalMeV": m_pi_mev_str if cid == "S1_pi_bare" else fmt(inv_a_mev, dps=OUT_DPS),
                "sigmaHatDimensionless": fmt(shat, dps=OUT_DPS),
                "sqrtSigma3MeV": fmt(sqrt_sig_3, dps=OUT_DPS),
                "sqrtSigma8CasimirMeV": fmt(sqrt_sig_8, dps=OUT_DPS),
                "impliedReggeSlopeGeVInv2": fmt(alpha_prime_cand, dps=OUT_DPS),
                "pctDiffVs430MeV": fmt(pct_vs_430, dps=12),
                "dLnSqrtSigmaDLnQAtQ0": fmt(qslope, dps=12),
                "verdictVsLattice420To440": verdict,
            }

        # =====================================================================
        # Emit Stamped Witness JSON (Zero Raw float64)
        # =====================================================================
        wb = WitnessBuilder(
            "sm8w-strong-cp-string-tension",
            engine="mpmath-80dps",
            output_dir=pathlib.Path(__file__).resolve().parent,
        )
        wb.set_description(
            "80-dps pre-registered verification of QOU/StandardModel/StrongCPWritheCancellationAndStringTension.lean "
            "(bean qou-tcpx / Q-Gap-11): closed SU(3)_c colour-singlet & mirror-paired T(2,9) writhe cancellation "
            "(theta_top = 0), 3x3 Hermitian / Nelson-Barr quark mass-determinant reality (Im det(M_u M_d) = 0, "
            "Re det(M_u M_d) > 0) coexisting with non-zero CKM Jarlskog J_CP = 3.513e-5, 1-loop chiral dressing "
            "determinant reality, 3-loop Ellis-Gaillard radiative bounds, SU(3)_c Casimir 9/4 scaling, and "
            "zero-parameter rank-3 Markov z_3(q_0) Wilson string-tension candidates."
        )

        wb.add_parameter("bean", "qou-tcpx")
        wb.add_parameter("parentEpic", "qou-sm8w")
        wb.add_parameter("gapId", "Q-Gap-11")
        wb.add_parameter("work_dps", WORK_DPS)
        wb.add_parameter("out_dps", OUT_DPS)
        wb.add_parameter("leanModule", "QOU.StandardModel.StrongCPWritheCancellationAndStringTension")
        wb.add_parameter("preregistration", "computations/probes/sm8w_strong_cp_string_tension/PREREGISTRATION.md")
        wb.add_parameter("selectedCandidate", "none")
        wb.add_parameter("q0ProtonAnchor", fmt(q0, dps=OUT_DPS))
        wb.add_parameter("h0SkeinDefect", fmt(h0, dps=OUT_DPS))
        wb.add_parameter("mElectronMeVCAL1", m_e_mev_str)
        wb.add_parameter("mProtonQOUMeV", fmt(m_p_qou_mev, dps=OUT_DPS))
        wb.add_parameter("mPionChargedMeVCAL3", m_pi_mev_str)

        wb.add_data(
            "armA_strongCP",
            {
                "writheFigEight": w_fig8,
                "writheBorromean": w_bor,
                "writheSingleT29": w_t29,
                "writheMirrorT29": w_t29_mir,
                "writhePairedT29": w_t29_pair,
                "singleT29CPAsymmetryAtQ0": fmt(single_t29_cp_asym, dps=OUT_DPS),
                "pairedT29PhaseResidual": fmt(paired_t29_phase_err, dps=15),
                "singletProjectorTrace": str(proj_tr),
                "singletNormSquared": str(eps_norm_sq),
                "jarlskogSubstrateBraiding": fmt(j_cp_plaquette, dps=OUT_DPS),
                "jarlskogFormulaResidual": fmt(j_cp_formula_err, dps=15),
                "maxOffdiagImMuRotated": fmt(max_offdiag_im_u, dps=20),
                "maxOffdiagImMdRotated": fmt(max_offdiag_im_d, dps=20),
                "nonHermiticityOfProductMuMd": fmt(non_herm_prod_ud, dps=20),
                "reDetMuMd": fmt(det_prod_ud.real, dps=OUT_DPS),
                "absImDetMuMd": fmt(im_det_ud, dps=15),
                "thetaBarTreeRadians": fmt(theta_tree_rad, dps=15),
                "imTrCommutatorCube": fmt(tr_comm_cube.imag, dps=OUT_DPS),
                "jarlskogCommutatorRelativeResidual": fmt(jarlskog_comm_rel_err, dps=15),
                "oneLoopDressedNonHermiticity": fmt(m_u_1loop_non_herm, dps=20),
                "oneLoopDressedAbsImDet": fmt(im_det_1loop, dps=15),
                "threeLoopEllisGaillardEstimate": fmt(delta_theta_ew_eg_sub, dps=20),
                "threeLoopConservativeEnvelope": fmt(delta_theta_ew_env, dps=20),
                "inducedNeutronEdm3LoopEcm": fmt(dn_ew_eg_ecm, dps=20),
                "inducedNeutronEdmEnvelopeEcm": fmt(dn_ew_env_ecm, dps=20),
                "pdg2024ThetaBarUpperBound": fmt(pdg_theta_bound, dps=10),
                "pdg2024NeutronEdmUpperBoundEcm": fmt(pdg_dn_bound_ecm, dps=10),
                "higherLoopCountertermStatus": "open_conditional_HigherLoopStrongCPFiniteHypothesis",
            },
        )

        wb.add_data(
            "armB_wilsonStringTension",
            {
                "su3CasimirSinglet": str(c2_singlet),
                "su3CasimirFundamental3": str(c2_fund),
                "su3CasimirSextet6": str(c2_sextet),
                "su3CasimirAdjoint8": str(c2_adj),
                "su3CasimirDecuplet10": str(c2_decuplet),
                "casimirScalingRatioAdjOverFund": str(casimir_ratio_adj_fund),
                "baryonPairwiseOverMesonSingletRatio": str(baryon_pair_factor / meson_singlet_factor),
                "markovZ3AtQ0": fmt(z3_q0, dps=OUT_DPS),
                "markovZ3SymAtQ0": fmt(z3_sym_q0, dps=OUT_DPS),
                "markovZ3NegAtQ0": fmt(z3_neg_q0, dps=OUT_DPS),
                "minusLnZ3AtQ0": fmt(sigma_hat_pos, dps=OUT_DPS),
                "lnQInt3AtQ0": fmt(sigma_hat_sym, dps=OUT_DPS),
                "creutzPerimeterCancellationMaxErr": fmt(creutz_max_err, dps=15),
                "latticeComparisonBandMeV": ["420", "440"],
                "reggeReferenceSqrtSigmaMeV": fmt(sqrt_sigma_regge_mev, dps=12),
                "inBandZeroParamCandidates": in_band_ids,
                "near15PctZeroParamCandidates": near_15pct_ids,
                "missZeroParamCandidates": miss_ids,
                "candidates": candidates_out,
            },
        )

        # Assertions (exact algebraic invariants & expected bounds — never fitting)
        wb.add_assertion(
            "proton_anchor_self_consistency_80dps",
            fmt(mp_anchor_err, dps=15),
            "0",
            "1e-70",
            source="q_at(80) Borromean proton-electron anchor",
        )
        wb.add_assertion(
            "topological_writhe_cancellation_4_1_borromean_and_paired_T29",
            int(
                w_fig8 == 0
                and w_bor == 0
                and w_t29 == 9
                and w_t29_mir == -9
                and w_t29_pair == 0
                and paired_t29_phase_err < tol_exact
                and single_t29_cp_asym > one
            ),
            1,
            "0",
            source="StrongCPWritheCancellationAndStringTension.substrate_and_gluon_writhe_identities",
        )
        wb.add_assertion(
            "su3_singlet_projector_sl3_invariance_and_balanced_parity",
            int(
                eps_norm_sq == 6
                and proj_tr == 1
                and proj_idem_ok
                and sl3_singlet_ok
                and su3_lie_singlet_ok
                and balanced_parity_ok
            ),
            1,
            "0",
            source="StrongCPWritheCancellationAndStringTension.{singletProj3_idempotent_and_trace_one,sl3_action_leviCivita3}",
        )
        wb.add_assertion(
            "hermitian_yukawa_im_det_Mu_Md_zero_below_1e_minus_78",
            int(
                u0_unitarity_err < tol_exact
                and v_unitarity_err < tol_exact
                and herm_err_u < tol_exact
                and herm_err_d < tol_exact
                and max_offdiag_im_u > mpf("1e-3")
                and max_offdiag_im_d > mpf("1e-3")
                and im_det_ud < tol_exact
                and det_prod_ud.real > mpf(0)
                and re_det_ud_rel_err < tol_rel
                and theta_tree_rad < tol_rel
            ),
            1,
            "0",
            source="StrongCPWritheCancellationAndStringTension.{det_mul_hermitian3_im_eq_zero,det_mul_gramDiag3_real_and_pos}",
        )
        wb.add_assertion(
            "nonzero_jarlskog_near_3p5e_minus_5_and_commutator_cube_identity",
            int(
                mpf("1.0e-5") <= j_cp_plaquette <= mpf("5.0e-5")
                and j_cp_formula_err < tol_exact
                and abs(tr_comm_cube.real) < tol_exact
                and jarlskog_comm_rel_err < tol_rel
                and int(mp.nint(w_det_prod.real)) == 312
                and int(mp.nint(w_det_prod.imag)) == 0
                and int(mp.nint(w_tr_cube.imag)) == -351360
            ),
            1,
            "0",
            source="StrongCPWritheCancellationAndStringTension.{jarlskog_commutator_cube_trace,strong_cp_zero_coexists_with_jarlskog_cp}",
        )
        wb.add_assertion(
            "one_loop_chiral_dressing_im_det_zero_and_three_loop_ew_below_pdg",
            int(
                m_u_1loop_non_herm > mpf("1e-6")
                and im_det_1loop < tol_exact
                and abs(delta_theta_ew_eg_sub) < pdg_theta_bound
                and abs(delta_theta_ew_env) < pdg_theta_bound
                and dn_ew_eg_ecm < pdg_dn_bound_ecm
                and dn_ew_env_ecm < pdg_dn_bound_ecm
            ),
            1,
            "0",
            source="StrongCPWritheCancellationAndStringTension.{det_chiralDressed_im_eq_zero,abs_thetaBarEffective_le_of_tree_zero}",
        )
        wb.add_assertion(
            "su3_casimir_9_over_4_markov_z3_window_and_creutz_cancellation",
            int(
                casimir_ratio_adj_fund == Fraction(9, 4)
                and baryon_pair_factor / meson_singlet_factor == Fraction(1, 2)
                and mpf(0) < z3_q0 < one
                and abs(z3_q0 - mpf("0.449305")) < mpf("1e-6")
                and creutz_max_err < tol_exact
                and len(candidates_out) == 8
            ),
            1,
            "0",
            source="StrongCPWritheCancellationAndStringTension.{su3_casimir_scaling_and_baryon_half_law,markovZ3_confinement_bounds,creutz_ratio_cancels_perimeter}",
        )

        wb.add_caveat(
            "1. Tree-level theta_bar_QCD = 0 rests on mirror-paired closed SU(3)_c colour-singlet writhe "
            "cancellation (theta_top = 0, excluding theta = pi at real q_0 > 1) and Hermiticity / positive "
            "congruence of tree-level Hecke mass operators (Im det(M_u M_d) = 1.96e-86 < 1e-78, Re det(M_u M_d) > 0 "
            "even with J_CP = 3.513e-5 != 0), plus exact determinant reality under factorized 1-loop chiral dressings "
            "(|Im det((I + Sigma_L) M_u M_d)| = 1.37e-86 < 1e-78); non-factorizable 3-loop+ electroweak-QCD shifts "
            "have finite Ellis-Gaillard magnitude 2.52e-20 (envelope 3.20e-22) << 1e-10, while UV counterterm "
            "finiteness remains open (HigherLoopStrongCPFiniteHypothesis). "
            "2. The pre-registered substrate CKM angles (s12 = h0, s23 = h0^2, s13 = h0^3/[2]_q0, delta = pi/3) "
            "serve solely as a zero-parameter complex braiding test texture giving J_CP = 3.513e-5 (not a CKM angle "
            "derivation: s12 = 0.2091 differs from PDG |V_us| = 0.2243 by -6.79%). "
            "3. All 7 zero-parameter Wilson string-tension candidates from z_3(q_0) = q_0^3/[3]_{q_0} = 0.449305 "
            "(and bar-symmetric 1/[3]_{q_0} = 0.328547) are reported verbatim without post-hoc selection "
            "(selectedCandidate = 'none', Rule 14): 0/7 lie strictly inside [420, 440] MeV; bare pion-Compton S1 "
            "(124.84 MeV, -70.97%), full proton-radius S5a (209.81 MeV, -51.21%), bare proton-Compton S4 "
            "(839.24 MeV, +95.17%), and S6_rp_half_sym (494.95 MeV, +15.10%) miss, while half-proton-radius "
            "Y-junction arm S5b_rp_half (419.62 MeV, -2.41% vs 430 MeV, -0.09% below 420 MeV), N_c=3 bar-symmetric "
            "pion-subcell S3_pi_nc3_sym (441.75 MeV, +2.73% vs 430 MeV, +0.40% above 440 MeV), and S2_pi_nc3 "
            "(374.52 MeV, -12.90%) bracket the 420-440 MeV lattice/Regge band pending a categorical derivation of a_cal."
        )

        saved = wb.save({"q0Anchor": "proton", "q0Value": fmt(q0, dps=OUT_DPS)})
        print(f"q0 (proton, 80 dps)      = {fmt(q0, dps=30)}")
        print(f"z3(q0) = q0^3 / [3]_q0   = {fmt(z3_q0, dps=20)}")
        print(f"-ln z3(q0)               = {fmt(sigma_hat_pos, dps=20)}")
        print(f"ln [3]_q0                = {fmt(sigma_hat_sym, dps=20)}")
        print(f"J_CP (substrate test)    = {fmt(j_cp_plaquette, dps=15)}")
        print(f"|Im det(M_u M_d)|        = {fmt(im_det_ud, dps=10)}")
        print(f"|Im det(M_u^1loop M_d)|  = {fmt(im_det_1loop, dps=10)}")
        print(f"delta_theta_EW (3-loop)  = {fmt(delta_theta_ew_eg_sub, dps=10)}")
        print(f"delta_theta_EW (env)     = {fmt(delta_theta_ew_env, dps=10)}")
        for cid, row in candidates_out.items():
            print(
                f"  {cid:24s}: sqrt(sigma_3) = {str(row['sqrtSigma3MeV'])[:12]} MeV "
                f"({row['pctDiffVs430MeV']}% vs 430 MeV) [{row['verdictVsLattice420To440']}]"
            )
        print(f"witness -> {saved}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
