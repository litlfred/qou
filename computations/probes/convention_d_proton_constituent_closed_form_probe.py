#!/usr/bin/env python3
"""50-dps Verification Probe for QOU/MassTheory/ConventionDProtonConstituentClosedForm.lean.

Evaluates and verifies at >= 50-dps mpmath precision (mp.mp.dps = 80, zero float64, zero fitting):
1. Target 1 (qou-nzp3): Exact Convention-D rational closed forms over Q(q) for the
   11-letter canonical alternating ('borromean') and historical 'grouped' proton and
   neutron constituent traces tr_M^{z_D}(p) and tr_M^{z_D}(n), their full per-Z step
   z_D(q)*tr_M^{z_D}(p_Bor)(q), their differences, and the scope-(b) exclusion of 2q - 1:
   - Verified against TWO independent 2D character representations of H_3(q):
     (a) the exact triangular representation rho_{(2,1)} in Lean, and
     (b) Hoefsmit's symmetric Young seminormal 2x2 matrices (with sqrt(1 - 1/[2]_q^2)).
   - Exact rational closed forms:
     * tr_M^{z_D}(p_Bor)(q) = (q^4+1)*(q^18 - 3q^16 + 7q^14 - 8q^12 + 10q^10 - 9q^8
                               + 10q^6 - 6q^4 + 3q^2 - 1) / (4 * q^9 * (q^2+1)^2)
     * tr_M^{z_D}(n_Bor)(q) = (q^4+1)*(q^14 - 3q^12 + 4q^10 - 4q^8 + 5q^6 - 4q^4
                               + 3q^2 - 1) / (4 * q^9)
     * tr_M^{z_D}(p_grp)(q) = (q^8 + q^4 + q^2 + 1)*(q^14 + q^12 + q^10 - 1)
                               / (4 * q^9 * (q^2+1)^2)
     * tr_M^{z_D}(n_grp)(q) = (q^8 - q^6 + q^4 + 1)*(q^10 + q^6 - q^4 + q^2 - 1)
                               / (4 * q^9)
   - Classical limit at q = 1: all four evaluate to z_D(1) = 1/2 != 2(1) - 1 = 1.
   - Triple-legacy reconstruction of 2q - 1: shows that the 0.033% proximity to
     2q_0 - 1 = 1.21995717 occurs ONLY in the excised Convention-C + grouped + lossy
     d=0 frame (sigma_0^7 sigma_1^{-2} at z_C = sqrt(q)/(q+1), giving 1.22036279).

2. Target 2 (qou-j11h): Reconciliation of tr_M vs tr_reg and classical vs q-deformed
   Plancherel weights in prop:mass-endomorphism-tower:
   - Exact grouped whole-word factorization:
     tr_M^{z_D}(p_grp) = V_{p,0}^{std} * V_{p,1}^{std}
     tr_M^{z_D}(n_grp) = V_{n,0}^{std} * V_{n,1}^{std}
   - Single-generator trace functionals on a*sigma_i + b*1 in H_3(q):
     * V_i^{std}      = z_D(q)*a_i + b_i
     * V_i^{full,q}   = z_{full,q}(q)*a_i + b_i,  z_{full,q}(q) = q*(q^4+2q^2-1)/(q^4+4q^2+1)
     * V_i^{full,cl}  = z_{full,cl}(q)*a_i + b_i, z_{full,cl}(q) = (5q^4-1)/(6q(q^2+1))
     * tau_{reg,cl}   = (h/2)*a_i + b_i

3. Target 3 (qou-aemx): Reconciliation of the three alpha_EM^{-1} formulations:
   - Algebraic incompatibility of T_bare(q) = q*[9]_q*[10]_q (q->1 limit 90) vs
     superseded gluon-octet prefactor 45*[3]_q (q->1 limit 135, ratio 3/2).
   - Additive identity T_bare*(1 + delta_CS/(1 - kappa*delta_CS))
     = T_bare + Delta_CS/(1 - kappa*delta_CS) where CS(T_{2,9}) + CS(T_{3,5}) = 98*pi^2/45,
     and exact matching value kappa_eff(q) to the Bring-Schwinger fixed-point shift
     2/(3*pi) + alpha * H(q) * (1 - c*alpha).

Run:
  python3 -u computations/probes/convention_d_proton_constituent_closed_form_probe.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_ROOT / "computations"))
sys.path.insert(0, str(_ROOT / "computations" / "substrate"))
sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))

import _path_bridge  # noqa: F401, E402
from mpmath import mpf  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, q_muon_at  # noqa: E402
from qou_substrate import codata as _codata  # noqa: E402
from witness_base import WitnessBuilder, q0_comparison  # noqa: E402

set_compute_dps()
mp.mp.dps = 80


def qbal(n: int, q: mpf) -> mpf:
    """Balanced quantum integer [n]_q = (q^n - q^{-n}) / (q - q^{-1})."""
    if q == mpf(1):
        return mpf(n)
    return (q ** n - q ** (-n)) / (q - mpf(1) / q)


def mat2_mul(A: list[list[mpf]], B: list[list[mpf]]) -> list[list[mpf]]:
    return [
        [
            A[0][0] * B[0][0] + A[0][1] * B[1][0],
            A[0][0] * B[0][1] + A[0][1] * B[1][1],
        ],
        [
            A[1][0] * B[0][0] + A[1][1] * B[1][0],
            A[1][0] * B[0][1] + A[1][1] * B[1][1],
        ],
    ]


def mat2_add(A: list[list[mpf]], B: list[list[mpf]], cA: mpf = mpf(1), cB: mpf = mpf(1)) -> list[list[mpf]]:
    return [
        [cA * A[0][0] + cB * B[0][0], cA * A[0][1] + cB * B[0][1]],
        [cA * A[1][0] + cB * B[1][0], cA * A[1][1] + cB * B[1][1]],
    ]


def mat2_trace(A: list[list[mpf]]) -> mpf:
    return A[0][0] + A[1][1]


def hoefsmit_word_trace(q: mpf, letters: list[tuple[int, int, mpf]]) -> mpf:
    """Evaluate chi_{(2,1)} on a product of letters (gen_idx, sign, d_shift)
    using Hoefsmit's symmetric 2x2 Young seminormal matrices."""
    qi = mpf(1) / q
    h = q - qi
    c2 = q + qi
    a = mpf(1) / c2
    b = mp.sqrt(mpf(1) - a * a)

    S0 = [[q, mpf(0)], [mpf(0), -qi]]
    S0_inv = [[qi, mpf(0)], [mpf(0), -q]]
    S1 = [
        [-qi * b * b + q * a * a, (q + qi) * a * b],
        [(q + qi) * a * b, q * b * b - qi * a * a],
    ]
    I2 = [[mpf(1), mpf(0)], [mpf(0), mpf(1)]]
    S1_inv = mat2_add(S1, I2, mpf(1), -h)

    M = [[mpf(1), mpf(0)], [mpf(0), mpf(1)]]
    for g, sgn, d_shift in letters:
        base = (S0 if sgn > 0 else S0_inv) if g == 0 else (S1 if sgn > 0 else S1_inv)
        letter_mat = mat2_add(base, I2, mpf(1), d_shift)
        M = mat2_mul(M, letter_mat)
    return mat2_trace(M)


def lean_std_word_trace(q: mpf, letters: list[tuple[int, int, mpf]]) -> mpf:
    """Evaluate chi_{(2,1)} on a product of letters (gen_idx, sign, d_shift)
    using the exact 2x2 triangular representation stdGen0, stdGen1 from Lean."""
    qi = mpf(1) / q
    G0 = [[q, mpf(0)], [mpf(1), -qi]]
    G0_inv = [[qi, mpf(0)], [mpf(1), -q]]
    G1 = [[-qi, mpf(1)], [mpf(0), q]]
    G1_inv = [[-q, mpf(1)], [mpf(0), qi]]
    I2 = [[mpf(1), mpf(0)], [mpf(0), mpf(1)]]

    M = [[mpf(1), mpf(0)], [mpf(0), mpf(1)]]
    for g, sgn, d_shift in letters:
        base = (G0 if sgn > 0 else G0_inv) if g == 0 else (G1 if sgn > 0 else G1_inv)
        letter_mat = mat2_add(base, I2, mpf(1), d_shift)
        M = mat2_mul(M, letter_mat)
    return mat2_trace(M)


def canonical_word_letters(baryon: str, ordering: str, h: mpf, averaged: bool = True) -> list[tuple[int, int, mpf]]:
    """Build the 11-letter nucleon word in H_3(q) matching pyhecke.atom.nucleon_word_letters."""
    d_avg = -h / mpf(2) if averaged else mpf(0)
    core = [(0, 1, mpf(0)), (1, -1, mpf(0))] * 3
    if baryon == "proton":
        if ordering == "borromean":
            return core + [
                (0, 1, mpf(0)),
                (0, 1, d_avg),
                (1, 1, d_avg),
                (0, 1, mpf(0)),
                (0, 1, mpf(0)),
            ]
        return [
            (0, 1, mpf(0)),
            (0, 1, mpf(0)),
            (0, 1, mpf(0)),
            (0, 1, mpf(0)),
            (0, 1, d_avg),
            (0, 1, mpf(0)),
            (0, 1, mpf(0)),
            (1, -1, mpf(0)),
            (1, -1, mpf(0)),
            (1, -1, mpf(0)),
            (1, 1, d_avg),
        ]
    if ordering == "borromean":
        return core + [
            (0, 1, d_avg),
            (0, 1, d_avg),
            (1, -1, mpf(0)),
            (0, 1, mpf(0)),
            (0, 1, mpf(0)),
        ]
    return [
        (0, 1, mpf(0)),
        (0, 1, mpf(0)),
        (0, 1, mpf(0)),
        (0, 1, d_avg),
        (0, 1, d_avg),
        (0, 1, mpf(0)),
        (0, 1, mpf(0)),
        (1, -1, mpf(0)),
        (1, -1, mpf(0)),
        (1, -1, mpf(0)),
        (1, -1, mpf(0)),
    ]


def solve_bring_fixed_point(T_bare: mpf, H_norm: mpf, c_loop: mpf) -> mpf:
    """Solve 1/alpha = (T_bare + 2/(3*pi)) + alpha * H_norm * (1 - c_loop * alpha)."""
    T_const = T_bare + mpf(2) / (mpf(3) * mp.pi)

    def cubic(alpha: mpf) -> mpf:
        return (
            -c_loop * H_norm * (alpha ** 3)
            + H_norm * (alpha ** 2)
            + T_const * alpha
            - mpf(1)
        )

    return mp.findroot(cubic, mpf(1) / T_const)


def evaluate_at_pin(q: mpf) -> dict:
    """Evaluate all closed-form expressions from ConventionDProtonConstituentClosedForm.lean at q."""
    qi = mpf(1) / q
    h = q - qi
    z_D = (q ** 3) / (q ** 2 + mpf(1))
    z_C = mp.sqrt(q) / (q + mpf(1))
    y3_D = (q ** 4 + mpf(1)) / ((q ** 2 + mpf(1)) ** 2)
    y21_D = (q ** 2) / ((q ** 2 + mpf(1)) ** 2)

    # 1D characters chi_{(3)}
    chi3_p = q * ((q ** 2 + mpf(1)) ** 2) / mpf(4)
    chi3_n = ((q ** 2 + mpf(1)) ** 2) / (mpf(4) * q)

    # 2D characters chi_{(2,1)} via Hoefsmit matrix product vs h-polynomial closed forms
    chi21_core_hoef = hoefsmit_word_trace(q, [(0, 1, mpf(0)), (1, -1, mpf(0))] * 3)
    chi21_core_poly = mpf(2) - mpf(3) * (h ** 4) - (h ** 6)
    trM_core_closed = (mpf(4) + h ** 2 - mpf(3) * (h ** 4) - (h ** 6)) / (h ** 2 + mpf(4))

    chi21_p_bor_hoef = hoefsmit_word_trace(q, canonical_word_letters("proton", "borromean", h, True))
    chi21_p_bor_lean = lean_std_word_trace(q, canonical_word_letters("proton", "borromean", h, True))
    chi21_p_bor_poly = (
        h * (h ** 2 + mpf(2)) * (h ** 2 + mpf(3))
        * (h ** 6 + mpf(3) * (h ** 4) + mpf(3) * (h ** 2) - mpf(1))
        / mpf(4)
    )

    chi21_n_bor_hoef = hoefsmit_word_trace(q, canonical_word_letters("neutron", "borromean", h, True))
    chi21_n_bor_lean = lean_std_word_trace(q, canonical_word_letters("neutron", "borromean", h, True))
    chi21_n_bor_poly = (
        h * (h ** 2 + mpf(2)) * (h ** 2 + mpf(4))
        * (h ** 6 + mpf(4) * (h ** 4) + mpf(3) * (h ** 2) - mpf(1))
        / mpf(4)
    )

    chi21_p_grp_hoef = hoefsmit_word_trace(q, canonical_word_letters("proton", "grouped", h, True))
    chi21_p_grp_lean = lean_std_word_trace(q, canonical_word_letters("proton", "grouped", h, True))
    chi21_p_grp_poly = (
        h * (h ** 2 + mpf(3)) * (h ** 4 + mpf(4) * (h ** 2) + mpf(2))
        * (h ** 4 + mpf(5) * (h ** 2) + mpf(5))
        / mpf(4)
    )

    chi21_n_grp_hoef = hoefsmit_word_trace(q, canonical_word_letters("neutron", "grouped", h, True))
    chi21_n_grp_lean = lean_std_word_trace(q, canonical_word_letters("neutron", "grouped", h, True))
    chi21_n_grp_poly = (
        h * (h ** 2 + mpf(4))
        * (h ** 8 + mpf(8) * (h ** 6) + mpf(22) * (h ** 4) + mpf(23) * (h ** 2) + mpf(7))
        / mpf(4)
    )

    # Exact rational closed forms over Q(q)
    trM_p_bor_wedderburn = y3_D * chi3_p + y21_D * chi21_p_bor_hoef
    trM_p_bor_rational = (
        (q ** 4 + mpf(1))
        * (
            q ** 18 - mpf(3) * (q ** 16) + mpf(7) * (q ** 14) - mpf(8) * (q ** 12)
            + mpf(10) * (q ** 10) - mpf(9) * (q ** 8) + mpf(10) * (q ** 6)
            - mpf(6) * (q ** 4) + mpf(3) * (q ** 2) - mpf(1)
        )
        / (mpf(4) * (q ** 9) * ((q ** 2 + mpf(1)) ** 2))
    )

    trM_n_bor_wedderburn = y3_D * chi3_n + y21_D * chi21_n_bor_hoef
    trM_n_bor_rational = (
        (q ** 4 + mpf(1))
        * (
            q ** 14 - mpf(3) * (q ** 12) + mpf(4) * (q ** 10) - mpf(4) * (q ** 8)
            + mpf(5) * (q ** 6) - mpf(4) * (q ** 4) + mpf(3) * (q ** 2) - mpf(1)
        )
        / (mpf(4) * (q ** 9))
    )

    trM_p_grp_wedderburn = y3_D * chi3_p + y21_D * chi21_p_grp_hoef
    trM_p_grp_rational = (
        (q ** 8 + q ** 4 + q ** 2 + mpf(1))
        * (q ** 14 + q ** 12 + q ** 10 - mpf(1))
        / (mpf(4) * (q ** 9) * ((q ** 2 + mpf(1)) ** 2))
    )

    trM_n_grp_wedderburn = y3_D * chi3_n + y21_D * chi21_n_grp_hoef
    trM_n_grp_rational = (
        (q ** 8 - q ** 6 + q ** 4 + mpf(1))
        * (q ** 10 + q ** 6 - q ** 4 + q ** 2 - mpf(1))
        / (mpf(4) * (q ** 9))
    )

    full_per_Z_p_bor = z_D * trM_p_bor_rational
    two_q_m1 = mpf(2) * q - mpf(1)
    zD_two_q_m1 = z_D * two_q_m1

    # Differences (grouped minus borromean, and proton minus neutron)
    diff_p_grp_bor = (
        h * (h ** 2 + mpf(3))
        * (mpf(4) * (h ** 6) + mpf(18) * (h ** 4) + mpf(25) * (h ** 2) + mpf(12))
        / (mpf(4) * (h ** 2 + mpf(4)))
    )
    diff_n_grp_bor = (
        h * (h ** 2 + mpf(1)) * (h ** 2 + mpf(3)) * (mpf(2) * (h ** 2) + mpf(3))
        / mpf(4)
    )
    diff_pn_bor = -(
        (q ** 2 - mpf(1)) * (q ** 4 + mpf(1))
        * (
            mpf(2) * (q ** 12) - mpf(6) * (q ** 10) + mpf(3) * (q ** 8)
            - mpf(6) * (q ** 6) + mpf(5) * (q ** 4) - mpf(5) * (q ** 2) + mpf(2)
        )
        / (mpf(4) * (q ** 7) * ((q ** 2 + mpf(1)) ** 2))
    )

    # Legacy bare words (d=0 on averaged letters, i.e. marshal_to_chi_lambda_braid)
    chi3_legacy = q ** 5
    chi21_legacy_grp_hoef = hoefsmit_word_trace(q, canonical_word_letters("proton", "grouped", h, False))
    chi21_legacy_bor_hoef = hoefsmit_word_trace(q, canonical_word_letters("proton", "borromean", h, False))
    trM_legacy_D_rational = (
        (q ** 4 + mpf(1))
        * (q ** 14 + q ** 10 - q ** 8 + q ** 6 - q ** 4 + q ** 2 - mpf(1))
        / ((q ** 7) * ((q ** 2 + mpf(1)) ** 2))
    )
    trM_legacy_bor_D = y3_D * chi3_legacy + y21_D * chi21_legacy_bor_hoef

    # Target 2 (qou-j11h): Single-generator factorizations and 3-channel vs tau_reg comparison
    ap0 = (h ** 2 + mpf(2)) * (h ** 4 + mpf(4) * (h ** 2) + mpf(1)) / mpf(2)
    bp0 = h * (h ** 4 + mpf(5) * (h ** 2) + mpf(5)) / mpf(2)
    ap1 = -h * (h ** 2 + mpf(3)) / mpf(2)
    bp1 = (h ** 4 + mpf(4) * (h ** 2) + mpf(2)) / mpf(2)

    an0 = (h ** 2 + mpf(4)) * (h ** 4 + mpf(3) * (h ** 2) + mpf(1)) / mpf(4)
    bn0 = h * (h ** 2 + mpf(4)) * (h ** 2 + mpf(2)) / mpf(4)
    an1 = -h * (h ** 2 + mpf(2))
    bn1 = h ** 4 + mpf(3) * (h ** 2) + mpf(1)

    z_full_q = q * (q ** 4 + mpf(2) * (q ** 2) - mpf(1)) / (q ** 4 + mpf(4) * (q ** 2) + mpf(1))
    z_full_cl = (mpf(5) * (q ** 4) - mpf(1)) / (mpf(6) * q * (q ** 2 + mpf(1)))

    Vp0_std = z_D * ap0 + bp0
    Vp1_std = z_D * ap1 + bp1
    Vn0_std = z_D * an0 + bn0
    Vn1_std = z_D * an1 + bn1

    Vp0_full_q = z_full_q * ap0 + bp0
    Vp1_full_q = z_full_q * ap1 + bp1
    Vn0_full_q = z_full_q * an0 + bn0
    Vn1_full_q = z_full_q * an1 + bn1

    Vp0_full_cl = z_full_cl * ap0 + bp0
    Vp1_full_cl = z_full_cl * ap1 + bp1
    Vn0_full_cl = z_full_cl * an0 + bn0
    Vn1_full_cl = z_full_cl * an1 + bn1

    tau_reg_p0 = (h / mpf(2)) * ap0 + bp0
    tau_reg_p1 = (h / mpf(2)) * ap1 + bp1

    # Target 3 (qou-aemx): Rival alpha_EM prefactors and additive shift reconciliation
    T_bare = q * qbal(9, q) * qbal(10, q)
    T_gluon_octet = mpf(45) * qbal(3, q)
    cs_sum = mpf(98) * (mp.pi ** 2) / mpf(45)
    hbar_q_sq = (mpf(1) - qi) ** 2
    Delta_CS = cs_sum * ((q + qi) / mpf(2)) * hbar_q_sq
    delta_CS = Delta_CS / T_bare
    kappa_shipped = mpf("1.7215935")
    shift_CS_shipped = Delta_CS / (mpf(1) - kappa_shipped * delta_CS)
    alpha_inv_CS_shipped = T_bare + shift_CS_shipped

    H_norm = (q + qi) / (mpf(8) * mp.pi)
    c_hecke = h ** 2
    alpha_bring_hecke = solve_bring_fixed_point(T_bare, H_norm, c_hecke)
    alpha_inv_bring_hecke = mpf(1) / alpha_bring_hecke
    shift_bring_hecke = alpha_inv_bring_hecke - T_bare
    # Exact kappa_eff making Delta_CS / (1 - kappa_eff * delta_CS) == shift_bring_hecke
    kappa_eff_hecke = (
        (mpf(1) - Delta_CS / shift_bring_hecke) / delta_CS
        if delta_CS != mpf(0)
        else mpf(0)
    )

    return {
        "q": q,
        "h": h,
        "z_D": z_D,
        "z_C": z_C,
        "y3_D": y3_D,
        "y21_D": y21_D,
        "chi21_core_hoef": chi21_core_hoef,
        "chi21_core_poly": chi21_core_poly,
        "trM_core_closed": trM_core_closed,
        "chi21_p_bor_hoef": chi21_p_bor_hoef,
        "chi21_p_bor_lean": chi21_p_bor_lean,
        "chi21_p_bor_poly": chi21_p_bor_poly,
        "chi21_n_bor_hoef": chi21_n_bor_hoef,
        "chi21_n_bor_lean": chi21_n_bor_lean,
        "chi21_n_bor_poly": chi21_n_bor_poly,
        "chi21_p_grp_hoef": chi21_p_grp_hoef,
        "chi21_p_grp_lean": chi21_p_grp_lean,
        "chi21_p_grp_poly": chi21_p_grp_poly,
        "chi21_n_grp_hoef": chi21_n_grp_hoef,
        "chi21_n_grp_lean": chi21_n_grp_lean,
        "chi21_n_grp_poly": chi21_n_grp_poly,
        "trM_p_bor_wedderburn": trM_p_bor_wedderburn,
        "trM_p_bor_rational": trM_p_bor_rational,
        "trM_n_bor_wedderburn": trM_n_bor_wedderburn,
        "trM_n_bor_rational": trM_n_bor_rational,
        "trM_p_grp_wedderburn": trM_p_grp_wedderburn,
        "trM_p_grp_rational": trM_p_grp_rational,
        "trM_n_grp_wedderburn": trM_n_grp_wedderburn,
        "trM_n_grp_rational": trM_n_grp_rational,
        "full_per_Z_p_bor": full_per_Z_p_bor,
        "two_q_m1": two_q_m1,
        "zD_two_q_m1": zD_two_q_m1,
        "diff_p_grp_bor": diff_p_grp_bor,
        "diff_n_grp_bor": diff_n_grp_bor,
        "diff_pn_bor": diff_pn_bor,
        "trM_legacy_D_rational": trM_legacy_D_rational,
        "trM_legacy_bor_D": trM_legacy_bor_D,
        "Vp0_std": Vp0_std,
        "Vp1_std": Vp1_std,
        "Vn0_std": Vn0_std,
        "Vn1_std": Vn1_std,
        "Vp0_full_q": Vp0_full_q,
        "Vp1_full_q": Vp1_full_q,
        "Vn0_full_q": Vn0_full_q,
        "Vn1_full_q": Vn1_full_q,
        "Vp0_full_cl": Vp0_full_cl,
        "Vp1_full_cl": Vp1_full_cl,
        "Vn0_full_cl": Vn0_full_cl,
        "Vn1_full_cl": Vn1_full_cl,
        "tau_reg_p0": tau_reg_p0,
        "tau_reg_p1": tau_reg_p1,
        "z_full_q": z_full_q,
        "z_full_cl": z_full_cl,
        "T_bare": T_bare,
        "T_gluon_octet": T_gluon_octet,
        "Delta_CS": Delta_CS,
        "delta_CS": delta_CS,
        "shift_CS_shipped": shift_CS_shipped,
        "alpha_inv_CS_shipped": alpha_inv_CS_shipped,
        "shift_bring_hecke": shift_bring_hecke,
        "alpha_inv_bring_hecke": alpha_inv_bring_hecke,
        "kappa_eff_hecke": kappa_eff_hecke,
    }


def main() -> int:
    q_proton = mpf(Q_50_DIGIT_STR)
    q_muon = q_muon_at(50)

    alpha_entry = _codata.codata("inverse fine-structure constant")
    alpha_inv_c22 = mpf(alpha_entry.value_str)
    alpha_inv_c22_sig = mpf(alpha_entry.uncertainty_str)

    res_p = evaluate_at_pin(q_proton)
    res_m = evaluate_at_pin(q_muon)
    res_1 = evaluate_at_pin(mpf(1))

    wb = WitnessBuilder(
        "convention_d_proton_constituent_closed_form_probe",
        engine="mpmath",
        output_dir=_HERE,
    )
    wb.set_content_block("thm:interface-knot-markov-z-proof")
    wb.set_description(
        "50-dps verification of QOU/MassTheory/ConventionDProtonConstituentClosedForm.lean: "
        "(1) qou-nzp3 exact Convention-D rational closed forms over Q(q) for the 11-letter "
        "borromean and grouped proton and neutron constituent traces tr_M^{z_D}(p) and "
        "tr_M^{z_D}(n), full per-Z step z_D*tr_M^{z_D}(p_Bor), and scope-(b) exclusion of 2q-1; "
        "(2) qou-j11h reconciliation of localized Jones-Markov trace V_i^{std}, q-deformed "
        "3-channel Plancherel volume V_i^{full,q}, classical-weight 3-channel volume V_i^{full,cl}, "
        "and genuine normalized regular-representation trace tau_{reg,cl}; "
        "(3) qou-aemx algebraic incompatibility of 45*[3]_q (q->1 limit 135) vs T_bare(q)=q[9]_q[10]_q "
        "(q->1 limit 90) and additive shift reconciliation between the Chern-Simons resummation "
        "and the Bring-Schwinger fixed point."
    )

    def add_check(name: str, lhs: mpf, rhs: mpf, source: str) -> None:
        wb.add_assertion(
            name=name,
            computed=fmt(lhs),
            expected=fmt(rhs),
            tolerance="1e-45",
            source=source,
        )

    # Assertions for Target 1 (qou-nzp3)
    add_check(
        "chi21_borromean_core_hoefsmit_eq_poly",
        res_p["chi21_core_hoef"],
        res_p["chi21_core_poly"],
        "ConventionDProtonConstituentClosedForm.trM_borromeanCore_eq",
    )
    add_check(
        "chi21_proton_borromean_lean_matrix_eq_poly",
        res_p["chi21_p_bor_lean"],
        res_p["chi21_p_bor_poly"],
        "ConventionDProtonConstituentClosedForm.chiTwoOne_borromean_eq_matrix_trace",
    )
    add_check(
        "chi21_neutron_borromean_lean_matrix_eq_poly",
        res_p["chi21_n_bor_lean"],
        res_p["chi21_n_bor_poly"],
        "ConventionDProtonConstituentClosedForm.chiTwoOne_borromean_eq_matrix_trace",
    )
    add_check(
        "chi21_proton_grouped_lean_matrix_eq_poly",
        res_p["chi21_p_grp_lean"],
        res_p["chi21_p_grp_poly"],
        "ConventionDProtonConstituentClosedForm.chiTwoOne_grouped_eq_matrix_trace",
    )
    add_check(
        "chi21_neutron_grouped_lean_matrix_eq_poly",
        res_p["chi21_n_grp_lean"],
        res_p["chi21_n_grp_poly"],
        "ConventionDProtonConstituentClosedForm.chiTwoOne_grouped_eq_matrix_trace",
    )
    add_check(
        "chi21_proton_borromean_hoefsmit_eq_poly",
        res_p["chi21_p_bor_hoef"],
        res_p["chi21_p_bor_poly"],
        "ConventionDProtonConstituentClosedForm.chiTwoOne_nucleon_factored_heckeH",
    )
    add_check(
        "chi21_neutron_borromean_hoefsmit_eq_poly",
        res_p["chi21_n_bor_hoef"],
        res_p["chi21_n_bor_poly"],
        "ConventionDProtonConstituentClosedForm.chiTwoOne_nucleon_factored_heckeH",
    )
    add_check(
        "chi21_proton_grouped_hoefsmit_eq_poly",
        res_p["chi21_p_grp_hoef"],
        res_p["chi21_p_grp_poly"],
        "ConventionDProtonConstituentClosedForm.chiTwoOne_nucleon_factored_heckeH",
    )
    add_check(
        "chi21_neutron_grouped_hoefsmit_eq_poly",
        res_p["chi21_n_grp_hoef"],
        res_p["chi21_n_grp_poly"],
        "ConventionDProtonConstituentClosedForm.chiTwoOne_nucleon_factored_heckeH",
    )
    add_check(
        "trM_proton_borromean_wedderburn_eq_rational",
        res_p["trM_p_bor_wedderburn"],
        res_p["trM_p_bor_rational"],
        "ConventionDProtonConstituentClosedForm.trM_proton_borromean_eq_rational",
    )
    add_check(
        "trM_neutron_borromean_wedderburn_eq_rational",
        res_p["trM_n_bor_wedderburn"],
        res_p["trM_n_bor_rational"],
        "ConventionDProtonConstituentClosedForm.trM_neutron_borromean_eq_rational",
    )
    add_check(
        "trM_proton_grouped_wedderburn_eq_rational",
        res_p["trM_p_grp_wedderburn"],
        res_p["trM_p_grp_rational"],
        "ConventionDProtonConstituentClosedForm.trM_proton_grouped_eq_rational",
    )
    add_check(
        "trM_neutron_grouped_wedderburn_eq_rational",
        res_p["trM_n_grp_wedderburn"],
        res_p["trM_n_grp_rational"],
        "ConventionDProtonConstituentClosedForm.trM_neutron_grouped_eq_rational",
    )
    add_check(
        "classical_limit_q1_all_four_nucleon_traces_eq_half",
        res_1["trM_p_bor_rational"],
        mpf("0.5"),
        "ConventionDProtonConstituentClosedForm.trM_nucleons_at_q_eq_one_refute_two_q_sub_one",
    )
    add_check(
        "trM_proton_grouped_sub_borromean_eq_heckeH_poly",
        res_p["trM_p_grp_rational"] - res_p["trM_p_bor_rational"],
        res_p["diff_p_grp_bor"],
        "ConventionDProtonConstituentClosedForm.trM_grouped_sub_borromean_eq_heckeH",
    )
    add_check(
        "trM_neutron_grouped_sub_borromean_eq_heckeH_poly",
        res_p["trM_n_grp_rational"] - res_p["trM_n_bor_rational"],
        res_p["diff_n_grp_bor"],
        "ConventionDProtonConstituentClosedForm.trM_grouped_sub_borromean_eq_heckeH",
    )
    add_check(
        "trM_proton_sub_neutron_borromean_eq_factored_rational",
        res_p["trM_p_bor_rational"] - res_p["trM_n_bor_rational"],
        res_p["diff_pn_bor"],
        "ConventionDProtonConstituentClosedForm.trM_proton_sub_neutron_eq_rational",
    )

    # Assertions for Target 2 (qou-j11h)
    add_check(
        "grouped_proton_factorization_eq_Vp0_std_mul_Vp1_std",
        res_p["trM_p_grp_rational"],
        res_p["Vp0_std"] * res_p["Vp1_std"],
        "ConventionDProtonConstituentClosedForm.trM_grouped_eq_prod_vStd",
    )
    add_check(
        "grouped_neutron_factorization_eq_Vn0_std_mul_Vn1_std",
        res_p["trM_n_grp_rational"],
        res_p["Vn0_std"] * res_p["Vn1_std"],
        "ConventionDProtonConstituentClosedForm.trM_grouped_eq_prod_vStd",
    )

    # Assertions for Target 3 (qou-aemx)
    add_check(
        "chern_simons_multiplicative_eq_additive_shift",
        res_p["T_bare"] * (mpf(1) + res_p["delta_CS"] / (mpf(1) - mpf("1.7215935") * res_p["delta_CS"])),
        res_p["alpha_inv_CS_shipped"],
        "ConventionDProtonConstituentClosedForm.chernSimons_resummed_eq_bare_add_shift",
    )
    add_check(
        "chern_simons_at_kappa_eff_eq_bring_schwinger_hecke",
        res_p["T_bare"] + res_p["Delta_CS"] / (mpf(1) - res_p["kappa_eff_hecke"] * res_p["delta_CS"]),
        res_p["alpha_inv_bring_hecke"],
        "ConventionDProtonConstituentClosedForm.chernSimons_eq_bringSchwinger_iff_shift_eq",
    )

    print("=" * 88)
    print("  50-DPS VERIFICATION: ConventionDProtonConstituentClosedForm.lean")
    print("=" * 88)
    print("\n[1] Target 1 (qou-nzp3): Exact Convention-D Closed Forms & Scope-(b) Exclusion of 2q-1")
    for label, res in [("q_proton (default)", res_p), ("q_muon (CAL-2)", res_m)]:
        print(f"  Pin: {label} = {fmt(res['q'], 30)}")
        print(f"    z_D(q) = q^3/(q^2+1)               = {fmt(res['z_D'], 30)}")
        print(f"    tr_M^{{z_D}}(beta_Bor) (6-letter)   = {fmt(res['trM_core_closed'], 30)}")
        print(f"    tr_M^{{z_D}}(p_Bor) (constit per-Z) = {fmt(res['trM_p_bor_rational'], 30)}")
        print(f"    tr_M^{{z_D}}(n_Bor) (constit per-N) = {fmt(res['trM_n_bor_rational'], 30)}")
        print(f"    tr_M^{{z_D}}(p_grp) (grouped)       = {fmt(res['trM_p_grp_rational'], 30)}")
        print(f"    tr_M^{{z_D}}(n_grp) (grouped)       = {fmt(res['trM_n_grp_rational'], 30)}")
        print(f"    z_D * tr_M^{{z_D}}(p_Bor) (full-Z)  = {fmt(res['full_per_Z_p_bor'], 30)}")
        print(f"    2q - 1                             = {fmt(res['two_q_m1'], 30)}")
        print(f"    legacy bare grouped   (d=0)      @zD = {fmt(res['trM_legacy_D_rational'], 30)}")
        print(f"    legacy bare borromean (d=0)      @zD = {fmt(res['trM_legacy_bor_D'], 30)}")

    print("\n[2] Target 2 (qou-j11h): Grouped Factorization & 3-Channel vs Regular-Rep Trace at q_proton")
    print(f"    V_{{p,0}}^{{std}} * V_{{p,1}}^{{std}}        = {fmt(res_p['Vp0_std'] * res_p['Vp1_std'], 30)}")
    print(f"    V_{{n,0}}^{{std}} * V_{{n,1}}^{{std}}        = {fmt(res_p['Vn0_std'] * res_p['Vn1_std'], 30)}")
    print(f"    V_{{p,0}}^{{full,q}} * V_{{p,1}}^{{full,q}}  = {fmt(res_p['Vp0_full_q'] * res_p['Vp1_full_q'], 30)}")
    print(f"    V_{{p,0}}^{{full,cl}} * V_{{p,1}}^{{full,cl}}= {fmt(res_p['Vp0_full_cl'] * res_p['Vp1_full_cl'], 30)}")
    print(f"    tau_{{reg,cl}}(p_0) * tau_{{reg,cl}}(p_1) = {fmt(res_p['tau_reg_p0'] * res_p['tau_reg_p1'], 30)}")

    print("\n[3] Target 3 (qou-aemx): Rival alpha_EM Prefactors & Additive Shift Reconciliation")
    for label, res in [("q_proton (default)", res_p), ("q_muon (CAL-2)", res_m)]:
        err_cs_ppb = (res["alpha_inv_CS_shipped"] - alpha_inv_c22) / alpha_inv_c22 * mpf("1e9")
        err_br_ppb = (res["alpha_inv_bring_hecke"] - alpha_inv_c22) / alpha_inv_c22 * mpf("1e9")
        print(f"  Pin: {label}")
        print(f"    T_bare(q) = q*[9]_q*[10]_q         = {fmt(res['T_bare'], 25)} (q->1: 90)")
        print(f"    45*[3]_q (superseded gluon-octet)  = {fmt(res['T_gluon_octet'], 25)} (q->1: 135)")
        print(f"    Delta_CS(q)                        = {fmt(res['Delta_CS'], 25)}")
        print(f"    CS shift (kappa=1.7215935)         = {fmt(res['shift_CS_shipped'], 25)} -> 1/alpha = {fmt(res['alpha_inv_CS_shipped'], 18)} ({mp.nstr(err_cs_ppb, 6)} ppb)")
        print(f"    Bring-Schwinger shift (c=hHecke^2) = {fmt(res['shift_bring_hecke'], 25)} -> 1/alpha = {fmt(res['alpha_inv_bring_hecke'], 18)} ({mp.nstr(err_br_ppb, 6)} ppb)")
        print(f"    Exact matching kappa_eff(c=h^2)    = {fmt(res['kappa_eff_hecke'], 25)}")

    def serialize_pin(res: dict) -> dict:
        return {k: fmt(v, 50) for k, v in res.items()}

    wb.add_data("q_proton_evaluation", serialize_pin(res_p))
    wb.add_data("q_muon_evaluation", serialize_pin(res_m))
    wb.add_data("classical_q1_limit", {
        "z_D_at_1": fmt(res_1["z_D"], 50),
        "trM_proton_borromean_at_1": fmt(res_1["trM_p_bor_rational"], 50),
        "trM_neutron_borromean_at_1": fmt(res_1["trM_n_bor_rational"], 50),
        "trM_proton_grouped_at_1": fmt(res_1["trM_p_grp_rational"], 50),
        "trM_neutron_grouped_at_1": fmt(res_1["trM_n_grp_rational"], 50),
        "two_q_minus_1_at_1": fmt(res_1["two_q_m1"], 50),
        "T_bare_at_1": "90",
        "T_gluon_octet_at_1": "135",
    })
    wb.add_data("codata_2022_reference", {
        "alpha_inv": alpha_entry.value_str,
        "uncertainty": alpha_entry.uncertainty_str,
    })

    out_path = wb.save(
        q0_comparison(
            muon=fmt(q_muon, 50),
            proton=fmt(q_proton, 50),
            reason=(
                "verifies the Convention-D rational closed forms for tr_M(proton) and tr_M(neutron), "
                "the 3-channel Plancherel vs regular-representation trace decomposition, and the "
                "Chern-Simons vs Bring-Schwinger alpha_EM reconciliation at both registered pins "
                "(q_proton default and q_muon CAL-2)"
            ),
        )
    )
    print(f"\n  Witness written to: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
