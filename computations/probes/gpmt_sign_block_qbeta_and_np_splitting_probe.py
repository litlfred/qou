#!/usr/bin/env python3
"""gpmt_sign_block_qbeta_and_np_splitting_probe.py — 80-dps First-Principles
GPMT (1,1,1) Sign-Block + Two-Term QED Nucleon Splitting & Q_beta Audit (Lane R3).

Companion to Lean 4 formalization:
  `folio/quantum-observable-universe/lean/QOU/QBeta/GPMTSignBlockAndTwoTermNucleonSplitting.lean`
  (`namespace QOU.QBeta.GPMTSignBlockAndTwoTermNucleonSplitting`).

STRICT ANTI-FITTING & PRECISION DISCIPLINE
------------------------------------------
1. ZERO fitting to CODATA/AME2020 Q_beta or Delta m_{np}; ZERO post-hoc integer
   multipliers; ZERO assertions gated on proximity to experimental values.
2. ZERO binary64 (`float64`) arithmetic, ZERO `math` or `numpy` imports, ZERO raw
   JSON floats in the emitted witness (`witness_raw_float64_audit` = 0).
3. Evaluates all exact H_3(q) Specht/Hoefsmit block traces, both GPMT sign-block
   combinations (`tr_{z_D} +- d_mod(1,1,1) * chi_{(1,1,1)}`), the Convention-D
   generating function `G_D(u; q)`, and the Two-Term Borromean V^3 QED splitting
   at 80 decimal places across `q_0`, `q_2t`, and `q_muon`.
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
    M_N_MEV_AME_DERIVED,
    M_P_MEV,
    Q_BETA_MEV_AME,
    Q_BETA_MEV_AME_ERR,
)
from qou_substrate.constants import (  # noqa: E402
    q_at,
    q_muon_at,
    q_two_term_borromean_at,
)
from qou_substrate.witness import (  # noqa: E402
    WitnessBuilder,
    q0_comparison,
)


# ── Exact H_3(q) Normal-Form Algebra over 80-dps mpmath ──────────────────────
# Canonical basis slot order matching Lean `QOU.Machinery.H3`:
#   [0: 1 (gamma), 1: sigma_0, 2: sigma_1, 3: L_- = sigma_1*sigma_0,
#    4: L_+ = sigma_0*sigma_1, 5: e^- = sigma_0*sigma_1*sigma_0]
NF_BASIS_LABELS: tuple[str, ...] = (
    "1",
    "sigma_0",
    "sigma_1",
    "sigma_1*sigma_0 (L_-)",
    "sigma_0*sigma_1 (L_+)",
    "sigma_0*sigma_1*sigma_0 (e^-)",
)


def _nf_identity() -> list[mp.mpf]:
    z = mp.mpf(0)
    return [mp.mpf(1), z, z, z, z, z]


def _nf_right_step(v: list[mp.mpf], gen: int, s_scalar: mp.mpf, b_gen: mp.mpf, h: mp.mpf) -> list[mp.mpf]:
    """Right-multiply 6-vector `v` by `s_scalar * 1 + b_gen * sigma_{gen}` (`gen in {0, 1}`),
    matching Lean `QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace.nfStep`."""
    x0, x1, x2, x3, x4, x5 = v
    if gen == 0:
        return [
            s_scalar * x0 + b_gen * x1,
            s_scalar * x1 + b_gen * (x0 + h * x1),
            s_scalar * x2 + b_gen * x3,
            s_scalar * x3 + b_gen * (x2 + h * x3),
            s_scalar * x4 + b_gen * x5,
            s_scalar * x5 + b_gen * (x4 + h * x5),
        ]
    if gen == 1:
        return [
            s_scalar * x0 + b_gen * x2,
            s_scalar * x1 + b_gen * x4,
            s_scalar * x2 + b_gen * (x0 + h * x2),
            s_scalar * x3 + b_gen * x5,
            s_scalar * x4 + b_gen * (x1 + h * x4),
            s_scalar * x5 + b_gen * (x3 + h * x5),
        ]
    raise ValueError(f"Invalid H_3 generator index: {gen}")


def _nf_sub(u: list[mp.mpf], v: list[mp.mpf]) -> list[mp.mpf]:
    return [a - b for a, b in zip(u, v)]


# ── Explicit 2x2 Hoefsmit/Specht Representation of H_3(q) on (2,1) ───────────
def _specht21_generators(q: mp.mpf) -> tuple[mp.matrix, mp.matrix]:
    """Return the exact 2x2 Hoefsmit seminormal matrices `(S0, S1)` of `(2,1)` from
    Lean `QOU.Machinery.HeckeH3BlockRep.S0` and `S1`."""
    one = mp.mpf(1)
    zero = mp.mpf(0)
    q2_1 = q ** 2 + one
    s0 = mp.matrix([[q, zero], [zero, -one / q]])
    s1 = mp.matrix(
        [
            [-one / (q * q2_1), one],
            [(q ** 4 + q ** 2 + one) / (q2_1 ** 2), (q ** 3) / q2_1],
        ]
    )
    return s0, s1


def _block21_of_nf(q: mp.mpf, v: list[mp.mpf]) -> mp.matrix:
    """Evaluate `blockOf q v` in M_2(R) on a 6-element H_3(q) normal-form vector `v`."""
    s0, s1 = _specht21_generators(q)
    i2 = mp.eye(2)
    s1_s0 = s1 * s0
    s0_s1 = s0 * s1
    s0_s1_s0 = s0_s1 * s0
    return (
        v[0] * i2
        + v[1] * s0
        + v[2] * s1
        + v[3] * s1_s0
        + v[4] * s0_s1
        + v[5] * s0_s1_s0
    )


def _mat2_max_abs(m: mp.matrix) -> mp.mpf:
    return max(abs(m[i, j]) for i in range(2) for j in range(2))


def _mat2_trace(m: mp.matrix) -> mp.mpf:
    return m[0, 0] + m[1, 1]


def _mat2_det(m: mp.matrix) -> mp.mpf:
    return m[0, 0] * m[1, 1] - m[0, 1] * m[1, 0]


def _specht_characters_and_matrix_check(q: mp.mpf, v: list[mp.mpf]) -> dict[str, mp.mpf]:
    """Compute `(chi_3, chi_21, chi_111)` both from basis characters and from the
    explicit 2x2 Hoefsmit matrix `blockOf q v`, recording the exact matrix residual."""
    one = mp.mpf(1)
    qi = one / q
    h = q - qi
    c0, c1, c2, c_lm, c_lp, c_w0 = v

    chi3 = c0 + q * (c1 + c2) + (q ** 2) * (c_lm + c_lp) + (q ** 3) * c_w0
    chi21_basis = mp.mpf(2) * c0 + h * (c1 + c2) - (c_lm + c_lp)
    chi111 = c0 - qi * (c1 + c2) + (qi ** 2) * (c_lm + c_lp) - (qi ** 3) * c_w0

    m21 = _block21_of_nf(q, v)
    chi21_mat = _mat2_trace(m21)
    det21_mat = _mat2_det(m21)
    return {
        "chi_3": chi3,
        "chi_21": chi21_mat,
        "chi_21_basis_vs_matrix_gap": abs(chi21_basis - chi21_mat),
        "chi_111": chi111,
        "det_21": det21_mat,
        "entry01_21": m21[0, 1],
        "max_abs_entry_21": _mat2_max_abs(m21),
    }


# ── Exact Rational Series for Convention-D Generating Function G_D(u; q) ─────
# Elements of Q(sqrt(3)) represented as exact pairs (a, b) -> a + b * sqrt(3).
QSqrt3 = tuple[Fraction, Fraction]


def _qs3(a: int | Fraction, b: int | Fraction = 0) -> QSqrt3:
    return (Fraction(a), Fraction(b))


def _qs3_add(x: QSqrt3, y: QSqrt3) -> QSqrt3:
    return (x[0] + y[0], x[1] + y[1])


def _qs3_sub(x: QSqrt3, y: QSqrt3) -> QSqrt3:
    return (x[0] - y[0], x[1] - y[1])


def _qs3_mul(x: QSqrt3, y: QSqrt3) -> QSqrt3:
    return (x[0] * y[0] + Fraction(3) * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def _qs3_inv(x: QSqrt3) -> QSqrt3:
    norm = x[0] * x[0] - Fraction(3) * x[1] * x[1]
    return (x[0] / norm, -x[1] / norm)


def _ser_mul(p: list[QSqrt3], r: list[QSqrt3], order: int) -> list[QSqrt3]:
    z = _qs3(0)
    out = [z] * (order + 1)
    for i in range(order + 1):
        if p[i] == z:
            continue
        for j in range(order + 1 - i):
            if r[j] == z:
                continue
            out[i + j] = _qs3_add(out[i + j], _qs3_mul(p[i], r[j]))
    return out


def _ser_inv(p: list[QSqrt3], order: int) -> list[QSqrt3]:
    z = _qs3(0)
    p0_inv = _qs3_inv(p[0])
    out = [z] * (order + 1)
    out[0] = p0_inv
    for n in range(1, order + 1):
        acc = z
        for k in range(1, n + 1):
            if p[k] != z and out[n - k] != z:
                acc = _qs3_add(acc, _qs3_mul(p[k], out[n - k]))
        out[n] = _qs3_mul(_qs3(-1), _qs3_mul(p0_inv, acc))
    return out


def _ser_sqrt_1_plus(delta: list[QSqrt3], order: int) -> list[QSqrt3]:
    z = _qs3(0)
    out = [z] * (order + 1)
    out[0] = _qs3(1)
    dpow = [z] * (order + 1)
    dpow[0] = _qs3(1)
    binom = Fraction(1, 2)
    for m in range(1, order + 1):
        dpow = _ser_mul(dpow, delta, order)
        b_qs = _qs3(binom)
        for k in range(m, order + 1):
            if dpow[k] != z:
                out[k] = _qs3_add(out[k], _qs3_mul(b_qs, dpow[k]))
        binom = binom * Fraction(1 - 2 * m, 2 * (m + 1))
    return out


def _ser_cos_of_sq(alpha_sq: list[QSqrt3], order: int) -> list[QSqrt3]:
    z = _qs3(0)
    out = [z] * (order + 1)
    out[0] = _qs3(1)
    pser = [z] * (order + 1)
    pser[0] = _qs3(1)
    fact_2m = 1
    for m in range(1, order + 1):
        fact_2m *= (2 * m - 1) * (2 * m)
        pser = _ser_mul(pser, alpha_sq, order)
        c_qs = _qs3(Fraction((-1) ** m, fact_2m))
        for k in range(m, order + 1):
            if pser[k] != z:
                out[k] = _qs3_add(out[k], _qs3_mul(c_qs, pser[k]))
    return out


def _ser_compose(outer: list[QSqrt3], inner: list[QSqrt3], order: int) -> list[QSqrt3]:
    z = _qs3(0)
    out = [z] * (order + 1)
    out[0] = outer[0]
    ipow = [z] * (order + 1)
    ipow[0] = _qs3(1)
    for m in range(1, order + 1):
        ipow = _ser_mul(ipow, inner, order)
        if outer[m] == z:
            continue
        for k in range(m, order + 1):
            if ipow[k] != z:
                out[k] = _qs3_add(out[k], _qs3_mul(outer[m], ipow[k]))
    return out


def _build_gd_ck_coefficients(max_k: int = 10) -> dict[int, QSqrt3]:
    """Compute exact `c_2 .. c_{max_k}` in Q(sqrt(3)) from the bar-even Lagrange-Burmann
    generating function of `ConventionDAllOrderCkGeneratingFunction.lean` (zero sympy/float)."""
    z = _qs3(0)
    delta3 = [z] * (max_k + 1)
    delta4 = [z] * (max_k + 1)
    delta3[1] = _qs3(Fraction(1, 3))
    delta4[1] = _qs3(Fraction(1, 4))

    sqrt_1_p_h3 = _ser_sqrt_1_plus(delta3, max_k)
    sqrt_1_p_h4 = _ser_sqrt_1_plus(delta4, max_k)
    inv_sqrt_1_p_h4 = _ser_inv(sqrt_1_p_h4, max_k)
    ratio_sqrt = _ser_mul(sqrt_1_p_h3, inv_sqrt_1_p_h4, max_k)

    u_of_h = [z] * (max_k + 1)
    c_u = _qs3(0, Fraction(1, 8))
    for m in range(1, max_k + 1):
        u_of_h[m] = _qs3_mul(c_u, ratio_sqrt[m - 1])

    h_of_u = [z] * (max_k + 1)
    u1_inv = _qs3(0, Fraction(8, 3))
    h_of_u[1] = u1_inv
    for n in range(2, max_k + 1):
        comp = _ser_compose(u_of_h, h_of_u, n)
        h_of_u[n] = _qs3_mul(_qs3(-1), _qs3_mul(u1_inv, comp[n]))

    # Bar-even operator ratio Pi_{2t,LB}(H) in Q[[H]]
    h_plus_2_half = [z] * (max_k + 1)
    h_plus_2_half[0] = _qs3(1)
    h_plus_2_half[1] = _qs3(Fraction(1, 2))
    loop_mean = _ser_mul(h_plus_2_half, inv_sqrt_1_p_h4, max_k)
    lm_minus_2 = list(loop_mean)
    lm_minus_2[0] = _qs3_sub(lm_minus_2[0], _qs3(2))
    sq_fac = _ser_mul(lm_minus_2, lm_minus_2, max_k)
    alpha_proj_sq = [z] * (max_k + 1)
    for m in range(1, max_k + 1):
        alpha_proj_sq[m] = _qs3_mul(_qs3(Fraction(1, 16)), sq_fac[m - 1])
    cos_alpha_proj = _ser_cos_of_sq(alpha_proj_sq, max_k)

    alpha_lead_sq = [z] * (max_k + 1)
    alpha_lead_sq[1] = _qs3(Fraction(1, 16))
    cos_alpha_lead = _ser_cos_of_sq(alpha_lead_sq, max_k)
    phase_ratio_h = _ser_mul(cos_alpha_proj, _ser_inv(cos_alpha_lead, max_k), max_k)

    one_plus_qed = [z] * (max_k + 1)
    one_plus_qed[0] = _qs3(1)
    if max_k >= 2:
        one_plus_qed[2] = _qs3(Fraction(1, 3))
    if max_k >= 3:
        one_plus_qed[3] = _qs3(Fraction(4, 27))

    one_p_h3 = [z] * (max_k + 1)
    one_p_h3[0] = _qs3(1)
    one_p_h3[1] = _qs3(Fraction(1, 3))
    d_mod_111_h = [
        _qs3_mul(_qs3(Fraction(1, 6)), c)
        for c in _ser_mul(inv_sqrt_1_p_h4, _ser_inv(one_p_h3, max_k), max_k)
    ]
    gpmt_corr = [z] * (max_k + 1)
    gpmt_corr[0] = _qs3(1)
    for m in range(2, max_k + 1):
        gpmt_corr[m] = _qs3_mul(_qs3(-1), d_mod_111_h[m - 1])

    combined_h = _ser_mul(_ser_mul(phase_ratio_h, one_plus_qed, max_k), gpmt_corr, max_k)
    pi_of_u = _ser_compose(combined_h, h_of_u, max_k)

    # Distinct-partition triangular extraction `ckFromSeries`
    prod_poly = [z] * (max_k + 1)
    prod_poly[0] = _qs3(1)
    c_out: dict[int, QSqrt3] = {}
    for n in range(2, max_k + 1):
        c_n = _qs3_sub(pi_of_u[n], prod_poly[n])
        c_out[n] = c_n
        for deg in range(max_k, n - 1, -1):
            if prod_poly[deg - n] != z:
                prod_poly[deg] = _qs3_add(prod_poly[deg], _qs3_mul(c_n, prod_poly[deg - n]))
    return c_out


def _eval_qs3_mpf(val: QSqrt3) -> mp.mpf:
    a, b = val
    a_mp = mp.mpf(a.numerator) / mp.mpf(a.denominator)
    b_mp = mp.mpf(b.numerator) / mp.mpf(b.denominator)
    return a_mp + b_mp * mp.sqrt(mp.mpf(3))


# ── Nucleon Normal-Form Candidate Constructors (Zero External Sympy Drift) ───
def _build_b3_core(h: mp.mpf) -> list[mp.mpf]:
    """6-crossing Borromean core `(sigma_0 * sigma_1^{-1})^3` in H_3(q)."""
    one, zero = mp.mpf(1), mp.mpf(0)
    nf = _nf_identity()
    for _ in range(3):
        nf = _nf_right_step(nf, 0, zero, one, h)
        nf = _nf_right_step(nf, 1, -h, one, h)
    return nf


def _build_nuc9(kind: str, h: mp.mpf) -> list[mp.mpf]:
    """9-crossing typed Borromean nucleon (`B_3 * typed_quark_triple`)."""
    one, zero = mp.mpf(1), mp.mpf(0)
    half_neg_h = -h / mp.mpf(2)
    nf = _build_b3_core(h)
    if kind == "p":
        nf = _nf_right_step(nf, 0, zero, one, h)
        nf = _nf_right_step(nf, 0, half_neg_h, one, h)
        nf = _nf_right_step(nf, 1, half_neg_h, one, h)
    elif kind == "n":
        nf = _nf_right_step(nf, 0, half_neg_h, one, h)
        nf = _nf_right_step(nf, 0, half_neg_h, one, h)
        nf = _nf_right_step(nf, 1, -h, one, h)
    else:
        raise ValueError(kind)
    return nf


def _apply_two_crossing_stabilizer(nf: list[mp.mpf], stab: str, h: mp.mpf) -> list[mp.mpf]:
    one, zero = mp.mpf(1), mp.mpf(0)
    if stab == "none_9x":
        return list(nf)
    if stab == "sigma0_sq":
        return _nf_right_step(_nf_right_step(nf, 0, zero, one, h), 0, zero, one, h)
    if stab == "V":
        return _nf_right_step(_nf_right_step(nf, 0, zero, one, h), 1, -h, one, h)
    if stab == "V_inv":
        return _nf_right_step(_nf_right_step(nf, 1, zero, one, h), 0, -h, one, h)
    if stab == "L_plus":
        return _nf_right_step(_nf_right_step(nf, 0, zero, one, h), 1, zero, one, h)
    if stab == "L_minus":
        return _nf_right_step(_nf_right_step(nf, 1, zero, one, h), 0, zero, one, h)
    raise ValueError(stab)


def _build_nuc11_gen_grouped(kind: str, h: mp.mpf) -> list[mp.mpf]:
    """11-crossing generator-grouped nucleon word (`nucleon_gen_chains`)."""
    one, zero = mp.mpf(1), mp.mpf(0)
    half = mp.mpf(1) / mp.mpf(2)
    if kind == "p":
        g0 = [zero, zero, zero, zero, -half * h, zero, zero]
        g1 = [-h, -h, -h, -half * h]
    elif kind == "n":
        g0 = [zero, zero, zero, -half * h, -half * h, zero, zero]
        g1 = [-h, -h, -h, -h]
    else:
        raise ValueError(kind)
    nf = _nf_identity()
    for s_val in g0:
        nf = _nf_right_step(nf, 0, s_val, one, h)
    for s_val in g1:
        nf = _nf_right_step(nf, 1, s_val, one, h)
    return nf


# ── Evaluate Complete Diagnostics at a Given 80-dps Substrate Pin ────────────
def _evaluate_at_pin(
    q: mp.mpf,
    pin_label: str,
    ck_qs3: dict[int, QSqrt3],
    me: mp.mpf,
    mp_exp: mp.mpf,
    mn_exp: mp.mpf,
    qbeta_exp: mp.mpf,
    qbeta_sigma: mp.mpf,
) -> dict[str, object]:
    with mp.workdps(95):
        one = mp.mpf(1)
        zero = mp.mpf(0)
        qi = one / q
        h = q - qi
        h_sq = h ** 2
        hbar_q = (q - one) / q

        e0_order0 = me / (q * (q - one))
        e0_tower = me / (q * (q - one) * (one - hbar_q ** 2))
        e0_tower_closed = me * q / ((q - one) * (mp.mpf(2) * q - one))
        e0_tower_closed_gap = abs(e0_tower - e0_tower_closed)

        z_d = (q ** 3) / (q ** 2 + one)
        w3_d = (q ** 4 + one) / ((q ** 2 + one) ** 2)
        w21_d = (q ** 2) / ((q ** 2 + one) ** 2)
        d_mod_111 = -(q ** 3) / ((q ** 2 + one) * (q ** 4 + q ** 2 + one))
        d_mod_111_abs = -d_mod_111

        # 1. Explicit 2x2 Hoefsmit/Specht verification on H_3(q)
        s0, s1 = _specht21_generators(q)
        i2 = mp.eye(2)
        hecke_s0_gap = _mat2_max_abs(s0 * s0 - h * s0 - i2)
        hecke_s1_gap = _mat2_max_abs(s1 * s1 - h * s1 - i2)
        braid_gap = _mat2_max_abs(s0 * s1 * s0 - s1 * s0 * s1)

        # Single-wrap proton, neutron, and Delta = n - p
        p_sw = _nf_right_step(
            [zero, one, zero, zero, zero, zero], 1, -h / mp.mpf(2), one, h
        )
        n_sw = _nf_right_step(
            [-h / mp.mpf(2), one, zero, zero, zero, zero], 1, -h, one, h
        )
        delta_sw = _nf_sub(n_sw, p_sw)
        delta_sw_expected = [h_sq / mp.mpf(2), -h / mp.mpf(2), -h / mp.mpf(2), zero, zero, zero]
        delta_sw_nf_gap = max(abs(a - b) for a, b in zip(delta_sw, delta_sw_expected))

        sp_delta = _specht_characters_and_matrix_check(q, delta_sw)
        m21_delta = _block21_of_nf(q, delta_sw)
        m21_delta_sq_gap = _mat2_max_abs(m21_delta * m21_delta - (h_sq / mp.mpf(4)) * i2)
        m21_delta_det_gap = abs(sp_delta["det_21"] - (-h_sq / mp.mpf(4)))
        m21_delta_entry01_gap = abs(sp_delta["entry01_21"] - (-h / mp.mpf(2)))

        # Lean §1-§2 closed-form checks on single-wrap Delta
        chi3_delta_closed = -(q ** 2 - qi ** 2) / mp.mpf(2)
        chi111_delta_closed = (q ** 2 - qi ** 2) / mp.mpf(2)
        tr_zd_delta_def = w3_d * sp_delta["chi_3"] + w21_d * sp_delta["chi_21"]
        tr_zd_delta_closed = -h * (q ** 4 + one) / (mp.mpf(2) * q * (q ** 2 + one))
        tau_gpmt_delta_def = d_mod_111_abs * sp_delta["chi_111"]
        tau_gpmt_delta_closed1 = (
            (q ** 3) * (q ** 2 - qi ** 2)
            / (mp.mpf(2) * (q ** 2 + one) * (q ** 4 + q ** 2 + one))
        )
        tau_gpmt_delta_closed2 = q * (q ** 2 - one) / (mp.mpf(2) * (q ** 4 + q ** 2 + one))

        tr_signed_delta_def = tr_zd_delta_def + d_mod_111 * sp_delta["chi_111"]
        tr_signed_delta_closed = (
            -(q ** 2 - one)
            * (q ** 8 + q ** 6 + q ** 5 + mp.mpf(2) * (q ** 4) + q ** 3 + q ** 2 + one)
            / (mp.mpf(2) * (q ** 2) * (q ** 2 + one) * (q ** 4 + q ** 2 + one))
        )
        tr_pos_delta_def = tr_zd_delta_def + d_mod_111_abs * sp_delta["chi_111"]
        tr_pos_delta_closed = (
            -(q ** 2 - one)
            * (q ** 8 + q ** 6 - q ** 5 + mp.mpf(2) * (q ** 4) - q ** 3 + q ** 2 + one)
            / (mp.mpf(2) * (q ** 2) * (q ** 2 + one) * (q ** 4 + q ** 2 + one))
        )

        # 2. Convention-D generating function G_D(u; q) & phase factors
        u_bar = (h_sq / mp.mpf(4)) * mp.sqrt((h_sq + mp.mpf(3)) / (h_sq + mp.mpf(4)))
        u_hbar = (hbar_q ** 2) * mp.sqrt(q ** 4 + q ** 2 + one) / (q ** 2 + one)
        alpha_d = (z_d - one) * h / mp.mpf(2)
        rung_n1n2 = mp.cos(alpha_d - u_hbar / mp.mpf(2)) * (one - u_hbar ** 2)

        gd_bar = one
        gd_hbar = one
        for k_idx, ck_val in sorted(ck_qs3.items()):
            ck_mp = _eval_qs3_mpf(ck_val)
            gd_bar *= one + ck_mp * (u_bar ** k_idx)
            gd_hbar *= one + ck_mp * (u_hbar ** k_idx)

        # 3. Two-Term Connected Borromean V^3 QED Splitting (Lean §4)
        #   - Per-period cyclic average -(m_e / 3) * Delta_tr_conn (`borromeanConnectedDeltaMQED`, -0.1106 keV)
        #   - Unaveraged 3-period sum  -m_e * Delta_tr_conn (`two_term_qed_isotope_and_nucleon_compute.py`, -0.3317 keV)
        q2 = q ** 2
        tr_conn_p = -mp.mpf(2) * ((q2 - one) ** 4) * (q ** 4 + q2 + one) / (mp.mpf(27) * (q ** 6))
        tr_conn_n = ((q2 - one) ** 4) * (mp.mpf(2) * (q ** 4) - q2 + mp.mpf(2)) / (mp.mpf(27) * (q ** 6))
        delta_tr_conn_3period = tr_conn_n - tr_conn_p
        # Note: in `NucleonWeightSpaceTwoTerm.trace_QAdj_connected_diff_borromeanV3`, the denominator is `9 * q^6`
        # (three times `delta_tr_conn_3period`), so `-(m_e / 3) * trace_QAdj_connected_diff = -m_e * delta_tr_conn_3period`!
        trace_qadj_diff_lean = (
            ((q2 - one) ** 4) * (mp.mpf(4) * (q ** 4) + q2 + mp.mpf(4)) / (mp.mpf(9) * (q ** 6))
        )
        dm_qed_bor_lean_mev = -(me / mp.mpf(3)) * trace_qadj_diff_lean
        dm_qed_bor_direct_mev = -me * delta_tr_conn_3period
        dm_qed_identity_gap = abs(dm_qed_bor_lean_mev - dm_qed_bor_direct_mev)

        mp_qed_bor_lean_mev = -(me / mp.mpf(3)) * (
            -mp.mpf(2) * ((q2 - one) ** 4) * (q ** 4 + q2 + one) / (mp.mpf(9) * (q ** 6))
        )
        mn_qed_bor_lean_mev = -(me / mp.mpf(3)) * (
            ((q2 - one) ** 4) * (mp.mpf(2) * (q ** 4) - q2 + mp.mpf(2)) / (mp.mpf(9) * (q ** 6))
        )
        dm_qed_split_sum_gap = abs(
            (mn_qed_bor_lean_mev - mp_qed_bor_lean_mev) - dm_qed_bor_lean_mev
        )

        # 4. Evaluate helper for any H_3(q) difference element `v_diff`
        dm_np_exp = mn_exp - mp_exp

        def _eval_element_table(label: str, desc: str, v_diff: list[mp.mpf]) -> dict[str, object]:
            sp = _specht_characters_and_matrix_check(q, v_diff)
            c3, c21, c111 = sp["chi_3"], sp["chi_21"], sp["chi_111"]
            tr_zd = w3_d * c3 + w21_d * c21
            tau_111 = d_mod_111_abs * c111
            tr_gpmt_pos = tr_zd + tau_111
            tr_gpmt_signed = tr_zd - tau_111

            variants: dict[str, object] = {}
            for fn_name, tr_val in (
                ("bare_zD", tr_zd),
                ("GPMT_pos_add_abs_dMod_chi111", tr_gpmt_pos),
                ("GPMT_signed_add_dMod_chi111", tr_gpmt_signed),
            ):
                qb_tower_1t = abs(tr_val) * e0_tower
                qb_tower_2t = qb_tower_1t + dm_qed_bor_lean_mev
                qb_tower_gd_2t = qb_tower_1t * gd_bar + dm_qed_bor_lean_mev
                qb_tower_rung_2t = qb_tower_1t * rung_n1n2 + dm_qed_bor_lean_mev
                qb_order0_1t = abs(tr_val) * e0_order0
                dm_np_2t = me + qb_tower_2t
                dm_np_gd_2t = me + qb_tower_gd_2t

                variants[fn_name] = {
                    "trace_value": fmt(tr_val),
                    "abs_trace_value": fmt(abs(tr_val)),
                    "Q_beta_E0_order0_1term_MeV": fmt(qb_order0_1t),
                    "Q_beta_E0_tower_1term_MeV": fmt(qb_tower_1t),
                    "Q_beta_E0_tower_1term_err_pct": fmt((qb_tower_1t - qbeta_exp) / qbeta_exp * mp.mpf(100)),
                    "Q_beta_E0_tower_2term_QED_MeV": fmt(qb_tower_2t),
                    "Q_beta_E0_tower_2term_QED_err_pct": fmt((qb_tower_2t - qbeta_exp) / qbeta_exp * mp.mpf(100)),
                    "Q_beta_E0_tower_2term_QED_err_sigma": fmt((qb_tower_2t - qbeta_exp) / qbeta_sigma),
                    "Q_beta_with_GD_uBar_and_2term_QED_MeV": fmt(qb_tower_gd_2t),
                    "Q_beta_with_GD_uBar_and_2term_QED_err_pct": fmt(
                        (qb_tower_gd_2t - qbeta_exp) / qbeta_exp * mp.mpf(100)
                    ),
                    "Q_beta_with_N1N2_rung_and_2term_QED_MeV": fmt(qb_tower_rung_2t),
                    "Delta_m_np_2term_QED_MeV": fmt(dm_np_2t),
                    "Delta_m_np_2term_QED_err_pct": fmt((dm_np_2t - dm_np_exp) / dm_np_exp * mp.mpf(100)),
                    "Delta_m_np_with_GD_and_2term_QED_MeV": fmt(dm_np_gd_2t),
                }

            return {
                "candidate": label,
                "description": desc,
                "nf_vector": [fmt(x) for x in v_diff],
                "specht_blocks": {
                    "chi_3": fmt(c3),
                    "chi_21_matrix_trace": fmt(c21),
                    "chi_21_basis_vs_matrix_gap": fmt(sp["chi_21_basis_vs_matrix_gap"]),
                    "chi_111": fmt(c111),
                    "tau_GPMT_111_abs_dMod_mul_chi111": fmt(tau_111),
                    "chi3_and_chi111_same_sign": bool(c3 * c111 > zero),
                },
                "functionals": variants,
                "_raw_sp": sp,
                "_raw_tr_zd": tr_zd,
                "_raw_tau_111": tau_111,
                "_raw_tr_pos": tr_gpmt_pos,
                "_raw_tr_signed": tr_gpmt_signed,
            }

        # Build all candidates transparently (ZERO cherry-picking!)
        cand_single_wrap = _eval_element_table(
            "single_wrap_Delta",
            "Single-wrap (n - p) normal-form difference Delta = (h^2/2)*1 - (h/2)*(sigma_0 + sigma_1)",
            delta_sw,
        )

        # 11-crossing reselected `nuc11_interleaved` (`sigma_0^2` stabilizer, `two-term-qed-isotope-and-nucleon-compute`)
        p9 = _build_nuc9("p", h)
        n9 = _build_nuc9("n", h)
        cand_nuc9 = _eval_element_table(
            "nuc9_bare_borromean_quarks",
            "9-crossing typed Borromean nucleon difference (no 2-crossing gluon stabilizer)",
            _nf_sub(n9, p9),
        )

        diff_nuc11_int = _nf_sub(
            _apply_two_crossing_stabilizer(n9, "sigma0_sq", h),
            _apply_two_crossing_stabilizer(p9, "sigma0_sq", h),
        )
        cand_nuc11_int = _eval_element_table(
            "nuc11_interleaved_sigma0_sq",
            "11-crossing interleaved nucleon difference (`nucleonDiffCoord`, `0.6515 MeV` 2-term baseline)",
            diff_nuc11_int,
        )

        # Verify Lean §3 closed-form theorems on `nuc11_interleaved` (`nucleonDiffCoord`)
        chi3_nuc11_closed = -(q2 - one) * ((q2 + one) ** 2) / (mp.mpf(4) * q)
        chi21_nuc11_closed = (
            (q2 - one)
            * (q ** 4 + one)
            * (
                mp.mpf(2) * (q ** 12)
                - mp.mpf(5) * (q ** 10)
                + mp.mpf(5) * (q ** 8)
                - mp.mpf(5) * (q ** 6)
                + mp.mpf(5) * (q ** 4)
                - mp.mpf(5) * q2
                + mp.mpf(2)
            )
            / (mp.mpf(4) * (q ** 9))
        )
        chi111_nuc11_closed = -(q2 - one) * ((q2 + one) ** 2) / (mp.mpf(4) * (q ** 5))
        tau_nuc11_closed = -(q2 - one) * (q2 + one) / (mp.mpf(4) * q2 * (q ** 4 + q2 + one))

        nuc11_lean_gaps = {
            "chi3_closed_gap": abs(cand_nuc11_int["_raw_sp"]["chi_3"] - chi3_nuc11_closed),
            "chi21_closed_gap": abs(cand_nuc11_int["_raw_sp"]["chi_21"] - chi21_nuc11_closed),
            "chi111_closed_gap": abs(cand_nuc11_int["_raw_sp"]["chi_111"] - chi111_nuc11_closed),
            "tauGPMT111_closed_gap": abs(cand_nuc11_int["_raw_tau_111"] - tau_nuc11_closed),
            "boost_identity_gap": abs(
                abs(cand_nuc11_int["_raw_tr_pos"])
                - (abs(cand_nuc11_int["_raw_tr_zd"]) + abs(tau_nuc11_closed))
            ),
        }

        # Complete `{V, V^{-1}, L_+, L_-}` 2-crossing stabilizer sweep + per-nucleon min |tr_{z_D}| audit
        four_letter_2cross = ("V", "V_inv", "L_plus", "L_minus")
        per_nucleon_traces: dict[str, dict[str, str]] = {"proton": {}, "neutron": {}}
        best_p = None
        best_n = None
        for st in four_letter_2cross:
            vp = _apply_two_crossing_stabilizer(p9, st, h)
            vn = _apply_two_crossing_stabilizer(n9, st, h)
            spp = _specht_characters_and_matrix_check(q, vp)
            spn = _specht_characters_and_matrix_check(q, vn)
            tr_p = w3_d * spp["chi_3"] + w21_d * spp["chi_21"]
            tr_n = w3_d * spn["chi_3"] + w21_d * spn["chi_21"]
            per_nucleon_traces["proton"][st] = fmt(tr_p)
            per_nucleon_traces["neutron"][st] = fmt(tr_n)
            if best_p is None or abs(tr_p) < best_p[0]:
                best_p = (abs(tr_p), st)
            if best_n is None or abs(tr_n) < best_n[0]:
                best_n = (abs(tr_n), st)

        cand_v = _eval_element_table(
            "reselected_2cross_V",
            "11-crossing difference with 2-crossing Borromean step V = sigma_0 * sigma_1^{-1}",
            _nf_sub(
                _apply_two_crossing_stabilizer(n9, "V", h),
                _apply_two_crossing_stabilizer(p9, "V", h),
            ),
        )
        cand_vinv = _eval_element_table(
            "reselected_2cross_V_inv",
            "11-crossing difference with V^{-1} = sigma_1 * sigma_0^{-1} (unique min |tr_{z_D}| winner over {V, V^{-1}, L_+, L_-})",
            _nf_sub(
                _apply_two_crossing_stabilizer(n9, "V_inv", h),
                _apply_two_crossing_stabilizer(p9, "V_inv", h),
            ),
        )
        cand_lplus = _eval_element_table(
            "reselected_2cross_L_plus",
            "11-crossing difference with positive Hopf stabilizer L_+ = sigma_0 * sigma_1",
            _nf_sub(
                _apply_two_crossing_stabilizer(n9, "L_plus", h),
                _apply_two_crossing_stabilizer(p9, "L_plus", h),
            ),
        )
        cand_lminus = _eval_element_table(
            "reselected_2cross_L_minus",
            "11-crossing difference with Hopf stabilizer L_- = sigma_1 * sigma_0 (`categorical-proton/neutron-properties`)",
            _nf_sub(
                _apply_two_crossing_stabilizer(n9, "L_minus", h),
                _apply_two_crossing_stabilizer(p9, "L_minus", h),
            ),
        )
        cand_gen_grouped = _eval_element_table(
            "nuc11_gen_grouped",
            "11-crossing generator-grouped nucleon difference (`nucleon_gen_chains`)",
            _nf_sub(_build_nuc11_gen_grouped("n", h), _build_nuc11_gen_grouped("p", h)),
        )

        all_cands_raw = [
            cand_single_wrap,
            cand_nuc9,
            cand_nuc11_int,
            cand_gen_grouped,
            cand_v,
            cand_vinv,
            cand_lplus,
            cand_lminus,
        ]
        max_basis_vs_mat_gap = max(c["_raw_sp"]["chi_21_basis_vs_matrix_gap"] for c in all_cands_raw)

        # Strip `_raw_*` keys for clean JSON serialization
        all_cands_clean = [
            {k: val for k, val in c.items() if not k.startswith("_raw_")}
            for c in all_cands_raw
        ]

        max_lean_delta_gap = max(
            delta_sw_nf_gap,
            abs(sp_delta["chi_3"] - chi3_delta_closed),
            abs(sp_delta["chi_21"]),
            abs(sp_delta["chi_111"] - chi111_delta_closed),
            m21_delta_sq_gap,
            m21_delta_det_gap,
            m21_delta_entry01_gap,
            abs(tr_zd_delta_def - tr_zd_delta_closed),
            abs(tau_gpmt_delta_def - tau_gpmt_delta_closed1),
            abs(tau_gpmt_delta_def - tau_gpmt_delta_closed2),
            abs(tr_signed_delta_def - tr_signed_delta_closed),
            abs(tr_pos_delta_def - tr_pos_delta_closed),
            e0_tower_closed_gap,
            dm_qed_identity_gap,
            dm_qed_split_sum_gap,
        )
        max_lean_nuc11_gap = max(nuc11_lean_gaps.values())

        return {
            "pin_label": pin_label,
            "q": fmt(q),
            "h": fmt(h),
            "hbar_q": fmt(hbar_q),
            "z_D": fmt(z_d),
            "w3_zD": fmt(w3_d),
            "w21_zD": fmt(w21_d),
            "dMod111": fmt(d_mod_111),
            "dMod111_abs": fmt(d_mod_111_abs),
            "E0_order0_MeV": fmt(e0_order0),
            "E0_tower_MeV": fmt(e0_tower),
            "generating_function_factors": {
                "u_bar": fmt(u_bar),
                "u_hbar": fmt(u_hbar),
                "G_D_uBar_k2_to_10": fmt(gd_bar),
                "G_D_uHbar_k2_to_10": fmt(gd_hbar),
                "N1N2_phase_rung": fmt(rung_n1n2),
            },
            "two_term_borromean_qed": {
                "M_QED_proton_Bor_MeV": fmt(mp_qed_bor_lean_mev),
                "M_QED_neutron_Bor_conn_MeV": fmt(mn_qed_bor_lean_mev),
                "Delta_M_QED_Bor_conn_MeV": fmt(dm_qed_bor_lean_mev),
                "Delta_M_QED_Bor_conn_keV": fmt(dm_qed_bor_lean_mev * mp.mpf(1000)),
            },
            "hoefsmit_2x2_specht_verification": {
                "S0_hecke_residual": fmt(hecke_s0_gap),
                "S1_hecke_residual": fmt(hecke_s1_gap),
                "S0_S1_braid_residual": fmt(braid_gap),
                "Delta_trace_on_21": fmt(sp_delta["chi_21"]),
                "Delta_entry01_on_21": fmt(sp_delta["entry01_21"]),
                "Delta_det_on_21": fmt(sp_delta["det_21"]),
                "Delta_sq_minus_quarter_hSq_I2_max_abs": fmt(m21_delta_sq_gap),
                "max_basis_vs_matrix_trace_gap_all_candidates": fmt(max_basis_vs_mat_gap),
            },
            "reselection_over_V_Vinv_Lplus_Lminus": {
                "per_nucleon_tr_zD": per_nucleon_traces,
                "min_abs_tr_zD_winner_proton": best_p[1] if best_p else "",
                "min_abs_tr_zD_winner_neutron": best_n[1] if best_n else "",
            },
            "candidates": all_cands_clean,
            "_raw_checks": {
                "hecke_braid_max": max(hecke_s0_gap, hecke_s1_gap, braid_gap, max_basis_vs_mat_gap),
                "delta_tr21_abs": abs(sp_delta["chi_21"]),
                "delta_m21_nonzero": abs(sp_delta["entry01_21"]) > mp.mpf("0.05"),
                "max_lean_delta_gap": max_lean_delta_gap,
                "max_lean_nuc11_gap": max_lean_nuc11_gap,
                "ordering_delta_ok": (
                    mp.mpf(0) < abs(tr_pos_delta_def) < abs(tr_zd_delta_def) < abs(tr_signed_delta_def)
                ),
                "qed_signs_ok": (
                    mp_qed_bor_lean_mev > mp.mpf(0)
                    and mn_qed_bor_lean_mev < mp.mpf(0)
                    and dm_qed_bor_lean_mev < mp.mpf(0)
                ),
            },
        }


def main() -> int:
    set_compute_dps(80)
    with mp.workdps(95):
        q0 = q_at(95)
        q2t = q_two_term_borromean_at(95, k_weighted=False)
        q_mu = q_muon_at(95)

        me = mp.mpf(str(M_E_MEV))
        mp_exp = mp.mpf(str(M_P_MEV))
        mn_exp = mp.mpf(str(M_N_MEV_AME_DERIVED))
        qbeta_exp = mp.mpf(str(Q_BETA_MEV_AME))
        qbeta_sig = mp.mpf(str(Q_BETA_MEV_AME_ERR))

        ck_qs3 = _build_gd_ck_coefficients(max_k=10)

        res_q0 = _evaluate_at_pin(
            q0, "q0_proton_1term", ck_qs3, me, mp_exp, mn_exp, qbeta_exp, qbeta_sig
        )
        res_q2t = _evaluate_at_pin(
            q2t, "q2t_two_term_borromean", ck_qs3, me, mp_exp, mn_exp, qbeta_exp, qbeta_sig
        )
        res_qmu = _evaluate_at_pin(
            q_mu, "q_muon_codata2022", ck_qs3, me, mp_exp, mn_exp, qbeta_exp, qbeta_sig
        )

        all_pins = (res_q0, res_q2t, res_qmu)
        raw_checks = [r["_raw_checks"] for r in all_pins]
        clean_q0 = {k: v for k, v in res_q0.items() if not k.startswith("_raw_")}
        clean_q2t = {k: v for k, v in res_q2t.items() if not k.startswith("_raw_")}
        clean_qmu = {k: v for k, v in res_qmu.items() if not k.startswith("_raw_")}

        wb = WitnessBuilder(
            "gpmt-sign-block-qbeta-and-np-splitting",
            engine="mpmath-80dps",
            output_dir=HERE,
        )
        wb.set_description(
            "80-dps parameter-free evaluation of the H_3(q) Wedderburn-Specht decomposition "
            "((3), 2x2 Hoefsmit (2,1), and (1,1,1) sign block), Geer-Patureau-Mirand-Turaev "
            "(GPMT) modified-trace sign-block completions (both +- signs), Convention-D "
            "all-order generating function G_D(u; q), and Two-Term Borromean V^3 QED nucleon "
            "mass splitting across single-wrap Delta and 11-crossing reselected nucleon "
            "differences at q_0, q_2t, and q_muon (Lane R3)."
        )

        wb.add_parameter("precision_dps", 80)
        wb.add_parameter("q0_proton_1term", fmt(q0))
        wb.add_parameter("q2t_two_term_borromean", fmt(q2t))
        wb.add_parameter("q0_muon_codata2022", fmt(q_mu))
        wb.add_parameter("m_e_CODATA2022_MeV", fmt(me))
        wb.add_parameter("Q_beta_AME2020_validation_only_MeV", fmt(qbeta_exp))
        wb.add_parameter("Delta_m_np_CODATA2022_validation_only_MeV", fmt(mn_exp - mp_exp))
        wb.add_parameter("zero_fitting", True)
        wb.add_parameter("zero_post_hoc_integer_multipliers", True)
        wb.add_parameter(
            "lean_companion",
            "folio/quantum-observable-universe/lean/QOU/QBeta/GPMTSignBlockAndTwoTermNucleonSplitting.lean",
        )

        wb.add_data(
            "gd_ck_exact_q_sqrt3_coefficients",
            {
                f"c_{k}": {
                    "rational_part": f"{val[0].numerator}/{val[0].denominator}",
                    "sqrt3_coeff": f"{val[1].numerator}/{val[1].denominator}",
                    "value_80dps": fmt(_eval_qs3_mpf(val)),
                }
                for k, val in sorted(ck_qs3.items())
            },
        )
        wb.add_data("at_q0_proton_1term", clean_q0)
        wb.add_data("at_q2t_two_term_borromean", clean_q2t)
        wb.add_data("at_q_muon_codata2022", clean_qmu)

        # Purely algebraic / structural assertions mirroring Lean theorems across all 3 pins
        # (ZERO assertions gated on proximity to CODATA Q_beta or Delta m_{np}!)
        wb.add_assertion(
            name="hoefsmit_2x2_hecke_braid_and_basis_trace_identities_80dps",
            computed=fmt(max(rc["hecke_braid_max"] for rc in raw_checks)),
            expected="0",
            tolerance="1e-80",
            source="HeckeH3BlockRep.S0_hecke, S1_hecke, S0_S1_braid across q_0, q_2t, q_muon",
        )
        wb.add_assertion(
            name="single_wrap_delta_21_block_trace_vanishes_identically_80dps",
            computed=fmt(max(rc["delta_tr21_abs"] for rc in raw_checks)),
            expected="0",
            tolerance="1e-80",
            source="blockOf_deltaSNF_trace_eq_zero : (blockOf q (deltaSNF (q - q⁻¹))).trace = 0",
        )
        wb.add_assertion(
            name="lean_single_wrap_gpmt_and_two_term_closed_forms_80dps",
            computed=fmt(max(rc["max_lean_delta_gap"] for rc in raw_checks)),
            expected="0",
            tolerance="1e-80",
            source="GPMTSignBlockAndTwoTermNucleonSplitting.lean §1, §2, §4 closed forms at q_0, q_2t, q_muon",
        )
        wb.add_assertion(
            name="lean_11crossing_specht_and_gpmt_boost_identities_80dps",
            computed=fmt(max(rc["max_lean_nuc11_gap"] for rc in raw_checks)),
            expected="0",
            tolerance="1e-78",
            source="chi21_nucleonDiffCoord_closed_form & abs_trM_gpmtPos_nucleonDiffCoord_boost at q_0, q_2t, q_muon",
        )
        wb.add_assertion(
            name="delta_gpmt_sign_ordering_and_borromean_qed_signs_exact",
            computed=(
                "1"
                if all(
                    rc["delta_m21_nonzero"] and rc["ordering_delta_ok"] and rc["qed_signs_ok"]
                    for rc in raw_checks
                )
                else "0"
            ),
            expected="1",
            tolerance="0",
            source="abs_trM_gpmt_ordering_on_deltaSNF & borromeanQED_signs_and_qbeta_lowering across q_0, q_2t, q_muon",
        )

        wb.add_caveat(
            "Both relative signs (`tr_{z_D} +- d_mod(1,1,1) * chi_{(1,1,1)}`) and all 2-crossing "
            "stabilizer candidates (`sigma_0^2` interleaved, `sigma_0^2` generator-grouped, "
            "`V = sigma_0*sigma_1^{-1}`, `V^{-1} = sigma_1*sigma_0^{-1}`, `L_+ = sigma_0*sigma_1`, "
            "`L_- = sigma_1*sigma_0`, plus bare 9-crossing `nuc9` and single-wrap `Delta`) are "
            "reported side-by-side without post-hoc selection. Because `chi_{(1,1,1)}(Delta) = "
            "-chi_{(3)}(Delta) > 0` on single-wrap `Delta` while `chi_{(1,1,1)} < 0` and "
            "`chi_{(3)} < 0` share the same sign on odd-length 9- and 11-crossing nucleon words, "
            "`tr_{z_D} + |d_mod(1,1,1)| * chi_{(1,1,1)}` reduces `|tr|` on single-wrap `Delta` "
            "(`0.4491 -> 0.3039 MeV`, whereas signed `+d_mod*chi_{(1,1,1)}` gives `0.5943 MeV`) "
            "and constructively boosts `|tr|` on all 9- and 11-crossing nucleon words "
            "(`0.6519 -> 0.7703 MeV` on `nuc11_interleaved`, `0.6680 -> 0.7865 MeV` on "
            "`nuc11_gen_grouped`, `0.6822 -> 0.8007 MeV` on `L_-`)."
        )
        wb.add_caveat(
            "In `NucleonWeightSpaceTwoTerm.trace_QAdj_connected_diff_borromeanV3`, the 3x3 "
            "adjacent-pair trace difference sums across all 3 periods of `V^3` (`denominator 9*q^6`), "
            "so `borromeanConnectedDeltaMQED = -(m_e / 3) * trace_QAdj_connected_diff_borromeanV3` "
            "equals `-m_e * (q^2 - 1)^4 (4 q^4 + q^2 + 4) / (27 q^6) = -0.331696 keV` identically, "
            "matching `two_term_qed_isotope_and_nucleon_compute.py` (`dm_qed_plain`)."
        )

        stamp = q0_comparison(
            muon=q_mu,
            proton=q0,
            reason=(
                "Lane R3 probe evaluates H_3(q) Specht block traces, GPMT (1,1,1) sign-block "
                "completions, G_D(u; q), and Two-Term Borromean V^3 QED nucleon mass splitting "
                "side-by-side across the 1-term proton pin q_0, consistent 2-term Borromean "
                "proton pin q_2t, and live CODATA-2022 muon pin q_muon."
            ),
        )
        saved_path = wb.save(stamp)
        saved_doc = json.loads(saved_path.read_text(encoding="utf-8"))

        import witness_raw_float64_audit as _f64_audit

        n_raw_floats = _f64_audit.count_raw_floats(saved_doc)
        if n_raw_floats != 0:
            raise RuntimeError(f"Emitted witness contains {n_raw_floats} raw float64 values!")

        print("=" * 126)
        print(
            "  Lane R3: 80-dps GPMT (1,1,1) Sign-Block + Two-Term QED Q_beta & Delta m_np Audit (@ q_2t)"
        )
        print("=" * 126)
        print(
            f"  q_0 = {mp.nstr(q0, 22)} | q_2t = {mp.nstr(q2t, 22)} | "
            f"E0^(inf) = {mp.nstr(mp.mpf(clean_q2t['E0_tower_MeV']), 10)} MeV | "
            f"Delta M_QED = {mp.nstr(mp.mpf(clean_q2t['two_term_borromean_qed']['Delta_M_QED_Bor_conn_keV']), 8)} keV"
        )
        print("-" * 126)
        hdr = (
            f"{'Candidate':<28} | {'chi_(3)':>10} {'chi_(2,1)':>11} {'chi_(1^3)':>10} | "
            f"{'Bare 2t':>9} {'GPMT+ 2t':>9} {'GPMT+GD+2t':>10} {'GPMT- 2t':>9} | {'GPMT+ err%':>10}"
        )
        print(hdr)
        print("-" * len(hdr))
        for c in clean_q2t["candidates"]:
            sb = c["specht_blocks"]
            fn_b = c["functionals"]["bare_zD"]
            fn_p = c["functionals"]["GPMT_pos_add_abs_dMod_chi111"]
            fn_s = c["functionals"]["GPMT_signed_add_dMod_chi111"]
            print(
                f"{c['candidate']:<28} | "
                f"{mp.nstr(mp.mpf(sb['chi_3']), 6):>10} "
                f"{mp.nstr(mp.mpf(sb['chi_21_matrix_trace']), 6):>11} "
                f"{mp.nstr(mp.mpf(sb['chi_111']), 6):>10} | "
                f"{mp.nstr(mp.mpf(fn_b['Q_beta_E0_tower_2term_QED_MeV']), 6):>9} "
                f"{mp.nstr(mp.mpf(fn_p['Q_beta_E0_tower_2term_QED_MeV']), 6):>9} "
                f"{mp.nstr(mp.mpf(fn_p['Q_beta_with_GD_uBar_and_2term_QED_MeV']), 6):>10} "
                f"{mp.nstr(mp.mpf(fn_s['Q_beta_E0_tower_2term_QED_MeV']), 6):>9} | "
                f"{mp.nstr(mp.mpf(fn_p['Q_beta_E0_tower_2term_QED_err_pct']), 5):>9}%"
            )
        print("=" * 126)
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
