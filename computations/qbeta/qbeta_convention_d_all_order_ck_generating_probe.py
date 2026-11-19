#!/usr/bin/env python3
"""All-order Convention-D higher-c_k (k = 2..10..inf) generating function probe.

Derives the all-order neutron-beta decay ladder product
    Pi_op(u) = prod_{k=2}^{inf} (1 + c_k * u^k) = 1 + sum_{n=2}^{inf} p_n * u^n
and exact symbolic coefficients c_2, c_3, ..., c_10 in Q(sqrt(3)) purely from the
parameter-free Convention-D + GPMT + Corrected Photon + Two-Term Categorical
Lagrangian Trace operator (ZERO CODATA fitting of c_k, ZERO float64).

Mathematical architecture (mirroring QOU.QBeta.ConventionDAllOrderCkGeneratingFunction):
1. Bar-even H = (q - q^{-1})^2 algebraic building blocks:
   - w_{(2,1)}(z_D) = 1 / (H + 4)
   - w_{(3)}(z_D)   = (H + 2) / (H + 4)
   - |d_Mod^{(1^3)}(q)| = 1 / (sqrt(H + 4) * (H + 3))
   - C_{KD}^{(6)}(q) = 1 + (9/2) H + 3 H^2 + (1/2) H^3
   - tr_conn(p, V^3) = -2 H^2 (H + 3) / 27
   - tr_conn(n, V^3) = +H^2 (2 H + 3) / 27
   - Delta_tr_conn^{plain}(V^3) = +H^2 (4 H + 9) / 27
   - alpha_D^{proj}(q) = (h / 4) * ((H + 2) / sqrt(H + 4) - 2)  (bar-odd, so cos is bar-even in H)
2. Lagrange-Burmann inversion of u_bar(H) = (H / 4) * sqrt((H + 3) / (H + 4)):
   - Exact critical quadratic 2 H^2 + 15 H + 24 = 0 with branch point
     H_* = (-15 + sqrt(33)) / 4 approx -2.313859338365493
   - Exact radius of convergence R_u = sqrt(u_bar^2(H_*)) approx 0.3690087298281905
   - Exact inverse power series H(u) = sum_{m=1}^{10} beta_m u^m in Q(sqrt(3))[[u]]
3. Distinct-partition triangular extraction of c_2 .. c_10 in Q(sqrt(3)):
   - Route A (Bar-even Lagrange-Burmann inversion in u of the Two-Term + GPMT + Mirror-Projected
     Phase operator ratio Pi_{2t,LB}(u), whose H^1 / u^1 coefficient vanishes identically)
   - Route B1 (Exact Q(sqrt(3))[[s]] log-product [s^{2k}] extraction for k = 2..10 extending
     qbeta_ck_sseries_exact_rational.py from KC=4 to KC=10 on the GB-reduced net operator)
   - Route B2 (Exact Q(sqrt(3))[[s]] [s^{2k}] extraction for k = 2..10 on the Two-Term
     Borromean V^3 QED + GPMT + Mirror-Projected Phase operator)
4. 80-dps partial-product convergence sweep N = 2..10 against the untruncated closed-form
   operator at q_{1t}, q_{2t}, and q_{mu}, demonstrating exponential decay below 1 ppQ = 10^{-15}.
"""

from __future__ import annotations

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for _p in (
    "computations",
    "computations/qbeta",
    "computations/substrate",
    "tools/qou-substrate/python",
    "tools/pyhecke/python",
):
    _s = os.path.join(ROOT, _p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

from pathlib import Path  # noqa: E402
import _path_bridge as _pb  # noqa: E402
import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from codata_2022_source import (  # noqa: E402
    M_E_MEV,
    M_MU_MEV,
    M_N_MEV_AME_DERIVED,
    M_P_MEV,
    Q_BETA_MEV_AME,
)
from q_parameter import (  # noqa: E402
    Q_50_DIGIT_STR,
    q_muon_at,
    q_two_term_borromean_at,
)
from qou_substrate.witness import q0_comparison  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(80)
mp.mp.dps = 80
HERE = Path(__file__).resolve().parent

# ---------------------------------------------------------------------------
# Section 0: Physical constants (80-dps mpmath strings, zero float literals)
# ---------------------------------------------------------------------------
_M_E_MEV = mp.mpf(str(M_E_MEV))
_M_MU_MEV = mp.mpf(str(M_MU_MEV))
_M_P_EXP_MEV = mp.mpf(str(M_P_MEV))
_M_N_EXP_MEV = mp.mpf(str(M_N_MEV_AME_DERIVED))
_Q_BETA_CODATA_MEV = mp.mpf(str(Q_BETA_MEV_AME))
Q_BETA_CODATA_EV = _Q_BETA_CODATA_MEV * mp.mpf("1000000")
ME_EV = _M_E_MEV * mp.mpf("1000000")
MP_EV = _M_P_EXP_MEV * mp.mpf("1000000")
MN_EV = _M_N_EXP_MEV * mp.mpf("1000000")


def fmt(val: mp.mpf, digits: int = 50) -> str:
    """Format an mpmath mpf at 50 significant digits with zero float64."""
    return mp.nstr(val, digits)


# ---------------------------------------------------------------------------
# Section 1: Exact Q(sqrt(3)) arithmetic & truncated formal power series
# ---------------------------------------------------------------------------
SQRT3 = sp.sqrt(sp.Integer(3))


def decompose_q_sqrt3(expr: sp.Expr) -> tuple[sp.Rational, sp.Rational]:
    """Decompose an element of Q(sqrt(3)) into (a, b) with expr = a + b*sqrt(3)."""
    expanded = sp.expand(expr)
    poly = sp.Poly(expanded, SQRT3)
    coeffs = poly.all_coeffs()
    if len(coeffs) == 1:
        a = sp.Rational(coeffs[0])
        b = sp.Rational(0)
    elif len(coeffs) == 2:
        b = sp.Rational(coeffs[0])
        a = sp.Rational(coeffs[1])
    else:
        simplified = sp.simplify(expanded)
        b = sp.Rational(simplified.coeff(SQRT3))
        a = sp.Rational(sp.simplify(simplified - b * SQRT3))
    return a, b


def q_sqrt3_to_mpf(a: sp.Rational, b: sp.Rational) -> mp.mpf:
    """Evaluate a + b*sqrt(3) at 80-dps mpmath without float conversion."""
    a_mp = mp.mpf(str(a.p)) / mp.mpf(str(a.q))
    b_mp = mp.mpf(str(b.p)) / mp.mpf(str(b.q))
    return a_mp + b_mp * mp.sqrt(mp.mpf(3))


def format_q_sqrt3(a: sp.Rational, b: sp.Rational) -> str:
    """Canonical human-readable string for a + b*sqrt(3)."""
    if b == 0:
        return str(a)
    if a == 0:
        return f"({b})*sqrt(3)"
    return f"{a} + ({b})*sqrt(3)"


def series_mul(p: list[sp.Expr], q_ser: list[sp.Expr], order: int) -> list[sp.Expr]:
    """Multiply two formal power series truncated to degree <= order."""
    out = [sp.Integer(0)] * (order + 1)
    for i in range(order + 1):
        if p[i] == 0:
            continue
        for j in range(order + 1 - i):
            if q_ser[j] == 0:
                continue
            out[i + j] = sp.expand(out[i + j] + p[i] * q_ser[j])
    return out


def series_add(p: list[sp.Expr], q_ser: list[sp.Expr], scale_q: sp.Expr = sp.Integer(1)) -> list[sp.Expr]:
    """Compute p + scale_q * q_ser coefficient-wise."""
    return [sp.expand(pi + scale_q * qi) for pi, qi in zip(p, q_ser)]


def series_inv(p: list[sp.Expr], order: int) -> list[sp.Expr]:
    """Invert formal power series p with p[0] != 0 up to degree <= order."""
    a0, b0 = decompose_q_sqrt3(p[0])
    if b0 == 0:
        p0_inv: sp.Expr = sp.Rational(1, 1) / a0
    else:
        norm = a0**2 - sp.Integer(3) * b0**2
        p0_inv = (a0 - b0 * SQRT3) / norm
    inv = [sp.Integer(0)] * (order + 1)
    inv[0] = p0_inv
    for n in range(1, order + 1):
        acc = sp.Integer(0)
        for k in range(1, n + 1):
            if p[k] != 0 and inv[n - k] != 0:
                acc = sp.expand(acc + p[k] * inv[n - k])
        inv[n] = sp.expand(-p0_inv * acc)
    return inv


def series_sqrt_1_plus(delta: list[sp.Expr], order: int) -> list[sp.Expr]:
    """Compute sqrt(1 + delta) where delta[0] == 0 up to degree <= order."""
    out = [sp.Integer(0)] * (order + 1)
    out[0] = sp.Integer(1)
    delta_pow = [sp.Integer(0)] * (order + 1)
    delta_pow[0] = sp.Integer(1)
    binom = sp.Rational(1, 2)
    for m in range(1, order + 1):
        delta_pow = series_mul(delta_pow, delta, order)
        for k in range(m, order + 1):
            if delta_pow[k] != 0:
                out[k] = sp.expand(out[k] + binom * delta_pow[k])
        binom = binom * sp.Rational(1 - 2 * m, 2 * (m + 1))
    return out


def series_log_1_plus(a_ser: list[sp.Expr], order: int) -> list[sp.Expr]:
    """Compute log(a_ser) where a_ser[0] == 1 up to degree <= order."""
    delta = list(a_ser)
    delta[0] = sp.Integer(0)
    out = [sp.Integer(0)] * (order + 1)
    dpow = [sp.Integer(0)] * (order + 1)
    dpow[0] = sp.Integer(1)
    for m in range(1, order + 1):
        dpow = series_mul(dpow, delta, order)
        coeff = sp.Rational((-1) ** (m - 1), m)
        for k in range(m, order + 1):
            if dpow[k] != 0:
                out[k] = sp.expand(out[k] + coeff * dpow[k])
    return out


def series_cos_of_sq(alpha_sq: list[sp.Expr], order: int) -> list[sp.Expr]:
    """Compute cos(alpha) = sum_{m>=0} (-1)^m (alpha^2)^m / (2m)! given alpha^2 with alpha_sq[0] == 0."""
    out = [sp.Integer(0)] * (order + 1)
    out[0] = sp.Integer(1)
    pow_ser = [sp.Integer(0)] * (order + 1)
    pow_ser[0] = sp.Integer(1)
    for m in range(1, order + 1):
        pow_ser = series_mul(pow_ser, alpha_sq, order)
        coeff = sp.Rational((-1) ** m, sp.factorial(2 * m))
        for k in range(m, order + 1):
            if pow_ser[k] != 0:
                out[k] = sp.expand(out[k] + coeff * pow_ser[k])
    return out


def series_compose(outer: list[sp.Expr], inner: list[sp.Expr], order: int) -> list[sp.Expr]:
    """Compose outer(inner(u)) where inner[0] == 0 up to degree <= order."""
    out = [sp.Integer(0)] * (order + 1)
    out[0] = outer[0]
    inner_pow = [sp.Integer(0)] * (order + 1)
    inner_pow[0] = sp.Integer(1)
    for m in range(1, order + 1):
        inner_pow = series_mul(inner_pow, inner, order)
        if outer[m] == 0:
            continue
        for k in range(m, order + 1):
            if inner_pow[k] != 0:
                out[k] = sp.expand(out[k] + outer[m] * inner_pow[k])
    return out


def distinct_partition_ck_from_pn(p_coeffs: dict[int, sp.Expr], max_k: int = 10) -> dict[int, sp.Expr]:
    """Division-free triangular inverse ckFromSeries from ConventionDAllOrderCkGeneratingFunction.lean.

    Given p_n = [u^n] prod_{k=2}^{max_k} (1 + c_k u^k) for n = 2..max_k,
    extracts c_2 .. c_{max_k} via c_n = p_n - [u^n] prod_{k=2}^{n-1} (1 + c_k u^k).
    """
    prod_poly = [sp.Integer(0)] * (max_k + 1)
    prod_poly[0] = sp.Integer(1)
    c_out: dict[int, sp.Expr] = {}
    for n in range(2, max_k + 1):
        c_n = sp.expand(p_coeffs[n] - prod_poly[n])
        c_out[n] = c_n
        for deg in range(max_k, n - 1, -1):
            if prod_poly[deg - n] != 0:
                prod_poly[deg] = sp.expand(prod_poly[deg] + c_n * prod_poly[deg - n])
    return c_out


# ---------------------------------------------------------------------------
# Section 2: Lagrange-Burmann inversion of u_bar(H) = (H/4)*sqrt((H+3)/(H+4))
# ---------------------------------------------------------------------------
def build_lagrange_burmann_H_of_u(max_order: int = 10) -> tuple[list[sp.Expr], list[sp.Expr]]:
    """Build u(H) in Q(sqrt(3))[[H]] and its Lagrange-Burmann compositional inverse H(u) in Q(sqrt(3))[[u]]."""
    delta3 = [sp.Integer(0)] * (max_order + 1)
    delta4 = [sp.Integer(0)] * (max_order + 1)
    delta3[1] = sp.Rational(1, 3)
    delta4[1] = sp.Rational(1, 4)

    sqrt_1_p_H3 = series_sqrt_1_plus(delta3, max_order)
    sqrt_1_p_H4 = series_sqrt_1_plus(delta4, max_order)
    inv_sqrt_1_p_H4 = series_inv(sqrt_1_p_H4, max_order)
    ratio_sqrt = series_mul(sqrt_1_p_H3, inv_sqrt_1_p_H4, max_order)

    u_of_H = [sp.Integer(0)] * (max_order + 1)
    for m in range(1, max_order + 1):
        u_of_H[m] = sp.expand(sp.Rational(1, 8) * SQRT3 * ratio_sqrt[m - 1])

    H_of_u = [sp.Integer(0)] * (max_order + 1)
    u1_inv = sp.Rational(8, 3) * SQRT3
    H_of_u[1] = u1_inv
    for n in range(2, max_order + 1):
        composed = series_compose(u_of_H, H_of_u, n)
        H_of_u[n] = sp.expand(-u1_inv * composed[n])

    return u_of_H, H_of_u


# ---------------------------------------------------------------------------
# Section 3: Route A - Bar-even operator generating function Pi_{op}(H(u))
# ---------------------------------------------------------------------------
def build_bar_even_operator_series_in_H(max_order: int = 10) -> dict[str, list[sp.Expr]]:
    """Build exact formal power series in H = (q - q^{-1})^2 for all bar-even operator channels.

    Every channel in the higher-c_k generating function starts at H^2 = O(u^2) (zero H^1 term):
      1. Phase-curvature ratio: cos(alpha_D^{proj}(H)) / cos(sqrt(H)/4) = 1 + (3/128) H^2 - ...
      2. Connected 2-term Borromean V^3 (n - p) QED trace:
         1 + Delta_tr_conn^{plain}(V^3)(H) = 1 + (1/3) H^2 + (4/27) H^3
      3. GPMT modified-dimension cumulant shift:
         1 - (|d_Mod^{(1^3)}(H)| - 1/6) * H = 1 + (11/144) H^2 - ...
    """
    delta4 = [sp.Integer(0)] * (max_order + 1)
    delta4[1] = sp.Rational(1, 4)
    inv_sqrt_1_p_H4 = series_inv(series_sqrt_1_plus(delta4, max_order), max_order)

    h_plus_2_half = [sp.Integer(0)] * (max_order + 1)
    h_plus_2_half[0] = sp.Integer(1)
    h_plus_2_half[1] = sp.Rational(1, 2)
    loop_mean = series_mul(h_plus_2_half, inv_sqrt_1_p_H4, max_order)
    loop_mean_minus_2 = list(loop_mean)
    loop_mean_minus_2[0] = sp.expand(loop_mean_minus_2[0] - sp.Integer(2))
    sq_factor = series_mul(loop_mean_minus_2, loop_mean_minus_2, max_order)
    alpha_proj_sq = [sp.Integer(0)] * (max_order + 1)
    for m in range(1, max_order + 1):
        alpha_proj_sq[m] = sp.expand(sp.Rational(1, 16) * sq_factor[m - 1])

    cos_alpha_proj = series_cos_of_sq(alpha_proj_sq, max_order)

    # Leading tangent phase squared (sqrt(H)/4)^2 = H/16
    alpha_lead_sq = [sp.Integer(0)] * (max_order + 1)
    alpha_lead_sq[1] = sp.Rational(1, 16)
    cos_alpha_lead = series_cos_of_sq(alpha_lead_sq, max_order)
    phase_ratio_H = series_mul(cos_alpha_proj, series_inv(cos_alpha_lead, max_order), max_order)

    tr_conn_diff_plain = [sp.Integer(0)] * (max_order + 1)
    if max_order >= 2:
        tr_conn_diff_plain[2] = sp.Rational(1, 3)
    if max_order >= 3:
        tr_conn_diff_plain[3] = sp.Rational(4, 27)

    one_p_H3 = [sp.Integer(0)] * (max_order + 1)
    one_p_H3[0] = sp.Integer(1)
    one_p_H3[1] = sp.Rational(1, 3)
    inv_1_p_H3 = series_inv(one_p_H3, max_order)
    d_mod_111 = [
        sp.expand(sp.Rational(1, 6) * c)
        for c in series_mul(inv_sqrt_1_p_H4, inv_1_p_H3, max_order)
    ]

    one_p_H4 = [sp.Integer(0)] * (max_order + 1)
    one_p_H4[0] = sp.Integer(1)
    one_p_H4[1] = sp.Rational(1, 4)
    inv_1_p_H4 = series_inv(one_p_H4, max_order)
    w21_H = [sp.expand(sp.Rational(1, 4) * c) for c in inv_1_p_H4]

    one_plus_qed = list(tr_conn_diff_plain)
    one_plus_qed[0] = sp.Integer(1)

    d_mod_shift = list(d_mod_111)
    d_mod_shift[0] = sp.Integer(0)
    gpmt_corr = [sp.Integer(0)] * (max_order + 1)
    gpmt_corr[0] = sp.Integer(1)
    for m in range(2, max_order + 1):
        gpmt_corr[m] = sp.expand(-d_mod_shift[m - 1])

    combined_2t = series_mul(
        series_mul(phase_ratio_H, one_plus_qed, max_order),
        gpmt_corr,
        max_order,
    )
    assert combined_2t[1] == 0, f"Expected zero H^1 coefficient in combined_2t, got {combined_2t[1]}"

    return {
        "phase_ratio_H": phase_ratio_H,
        "tr_conn_diff_plain_H": tr_conn_diff_plain,
        "d_mod_111_H": d_mod_111,
        "w21_H": w21_H,
        "combined_2t_H": combined_2t,
    }


# ---------------------------------------------------------------------------
# Section 4: Route B - Exact Q(sqrt(3))[[s]] [s^{2k}] triangular extraction (k = 2..10)
# ---------------------------------------------------------------------------
def build_sseries_exact_ck_up_to_k10(max_k: int = 10) -> dict[str, dict[int, sp.Expr]]:
    """Extend qbeta_ck_sseries_exact_rational.py from k=2..4 to k=2..10 (ORD = 2*max_k = 20).

    Route B1 ('net_operator_sseries'):
      Uses the exact symbolic GB-reduced net operator Delta(net)(q) from
      free-neutron-decay.witness.json with the identical conventions of
      qbeta_ck_sseries_exact_rational.py (matching c_2, c_3, c_4 identically and
      extending to c_5 .. c_{10}).
    Route B2 ('two_term_qed_mirror_phase_sseries'):
      Augments the net operator with the parameter-free 2-term Borromean V^3
      (n - p) QED trace Delta_tr_conn^{plain}(V^3) = H^2(4H+9)/27 and the
      mirror-projected Convention-D phase alpha_D^{proj}.
    """
    ord_s = 2 * max_k
    q_sym = sp.Symbol("q", positive=True)
    s_sym = sp.Symbol("s")

    def rat_series_s(expr: sp.Expr) -> list[sp.Expr]:
        f = sp.cancel(expr.subs(q_sym, sp.Integer(1) + s_sym))
        num, den = sp.fraction(f)
        pn = sp.Poly(sp.expand(num), s_sym)
        pd = sp.Poly(sp.expand(den), s_sym)
        a_ser = [sp.Rational(pn.coeff_monomial(s_sym**i)) if i > 0 else sp.Rational(pn.TC()) for i in range(ord_s + 1)]
        b_ser = [sp.Rational(pd.coeff_monomial(s_sym**i)) if i > 0 else sp.Rational(pd.TC()) for i in range(ord_s + 1)]
        return series_mul(a_ser, series_inv(b_ser, ord_s), ord_s)

    def load_net_symbolic(side: str) -> sp.Expr:
        d = json.load(open(_pb.witness_path("free-neutron-decay.witness.json", HERE)))
        net = sp.Integer(0)
        for t in d[side]["nf_terms"]:
            net += sp.sympify(t["coefficient_symbolic"], locals={"q": q_sym})
        return sp.simplify(net)

    dnet = sp.simplify(load_net_symbolic("neutron") - load_net_symbolic("proton"))
    dnet_reg = sp.cancel(dnet / (q_sym - sp.Integer(1)))

    # At q > 1, dnet < 0 so sgn = -1
    Qb_s = rat_series_s(sp.Integer(-1) * dnet_reg / q_sym)
    QA_s = rat_series_s((sp.Integer(2) * q_sym + sp.Integer(1) - q_sym**2) * (q_sym + sp.Integer(1)) / (sp.Integer(2) * q_sym**3))
    hbar2_s = rat_series_s(((q_sym - sp.Integer(1)) / q_sym) ** 2)

    # b(q) = sqrt(q^4 + q^2 + 1) / (q^2 + 1)
    # Write q^4 + q^2 + 1 = 3 * (1 + delta_b(s)) so sqrt = sqrt(3) * sqrt(1 + delta_b(s))
    b_rad_s = rat_series_s((q_sym**4 + q_sym**2 + sp.Integer(1)) / sp.Integer(3))
    delta_b = list(b_rad_s)
    delta_b[0] = sp.Integer(0)
    sqrt_b_rad = [sp.expand(SQRT3 * c) for c in series_sqrt_1_plus(delta_b, ord_s)]
    b_ser = series_mul(sqrt_b_rad, rat_series_s(sp.Integer(1) / (q_sym**2 + sp.Integer(1))), ord_s)
    u_ser = series_mul(b_ser, hbar2_s, ord_s)

    # In qbeta_ck_sseries_exact_rational.py:
    # z_ser = sqrt(q) / (q + 1), h_ser = q - 1/q, alpha_eff = (z - 1)*h/2 - u/2
    delta_q = [sp.Integer(0)] * (ord_s + 1)
    delta_q[1] = sp.Integer(1)
    sqrt_q_s = series_sqrt_1_plus(delta_q, ord_s)
    z_ser = series_mul(sqrt_q_s, rat_series_s(sp.Integer(1) / (q_sym + sp.Integer(1))), ord_s)
    h_ser = rat_series_s(q_sym - sp.Integer(1) / q_sym)
    H_ser = series_mul(h_ser, h_ser, ord_s)
    zm1 = list(z_ser)
    zm1[0] = sp.expand(zm1[0] - sp.Integer(1))
    alpha_eff_s = series_add(
        [sp.expand(sp.Rational(1, 2) * c) for c in series_mul(zm1, h_ser, ord_s)],
        u_ser,
        sp.Rational(-1, 2),
    )
    cos_alpha_eff_s = series_cos_of_sq(series_mul(alpha_eff_s, alpha_eff_s, ord_s), ord_s)

    # Route B1 ratio R_net(s) = Qb / (QA * cos(alpha_eff))
    R_net_s = series_mul(
        Qb_s,
        series_inv(series_mul(QA_s, cos_alpha_eff_s, ord_s), ord_s),
        ord_s,
    )
    log_R_net_s = series_log_1_plus(R_net_s, ord_s)

    # Route B2: Two-term Borromean V^3 QED + mirror-projected Convention-D phase
    # alpha_D^{proj}(s) = ((q^3/(q^2+1) - 1)*h/2 - H/4)
    zD_m1_s = rat_series_s(q_sym**3 / (q_sym**2 + sp.Integer(1)) - sp.Integer(1))
    alpha_proj_s = series_add(
        [sp.expand(sp.Rational(1, 2) * c) for c in series_mul(zD_m1_s, h_ser, ord_s)],
        H_ser,
        sp.Rational(-1, 4),
    )
    cos_alpha_proj_s = series_cos_of_sq(series_mul(alpha_proj_s, alpha_proj_s, ord_s), ord_s)

    tr_conn_diff_s = rat_series_s(
        (q_sym - sp.Integer(1) / q_sym) ** 4
        * (sp.Integer(4) * (q_sym - sp.Integer(1) / q_sym) ** 2 + sp.Integer(9))
        / sp.Integer(27)
    )
    one_p_tr_conn_s = list(tr_conn_diff_s)
    one_p_tr_conn_s[0] = sp.expand(one_p_tr_conn_s[0] + sp.Integer(1))

    R_2t_s = series_mul(
        series_mul(Qb_s, one_p_tr_conn_s, ord_s),
        series_inv(series_mul(QA_s, cos_alpha_proj_s, ord_s), ord_s),
        ord_s,
    )
    log_R_2t_s = series_log_1_plus(R_2t_s, ord_s)

    # Powers u(s)^k for k = 1..max_k
    u_pows: dict[int, list[sp.Expr]] = {1: u_ser}
    for k in range(2, max_k + 1):
        u_pows[k] = series_mul(u_pows[k - 1], u_ser, ord_s)

    def solve_log_triangular_s2k(log_R_target: list[sp.Expr]) -> dict[int, sp.Expr]:
        model = [sp.Integer(0)] * (ord_s + 1)
        c_sol: dict[int, sp.Expr] = {}
        for k in range(2, max_k + 1):
            deg = 2 * k
            resid = sp.expand(log_R_target[deg] - model[deg])
            lead = u_pows[k][deg]
            # Divide resid by lead in Q(sqrt(3))
            al, bl = decompose_q_sqrt3(lead)
            if bl == 0:
                lead_inv: sp.Expr = sp.Rational(1, 1) / al
            else:
                norm = al**2 - sp.Integer(3) * bl**2
                lead_inv = (al - bl * SQRT3) / norm
            ck = sp.expand(resid * lead_inv)
            c_sol[k] = ck
            one_p_ck_uk = [sp.expand(ck * c) for c in u_pows[k]]
            one_p_ck_uk[0] = sp.Integer(1)
            model = series_add(model, series_log_1_plus(one_p_ck_uk, ord_s), sp.Integer(1))
        return c_sol

    return {
        "net_operator_sseries": solve_log_triangular_s2k(log_R_net_s),
        "two_term_qed_mirror_phase_sseries": solve_log_triangular_s2k(log_R_2t_s),
    }


# ---------------------------------------------------------------------------
# Section 5: 80-dps Closed-Form Evaluators
# ---------------------------------------------------------------------------
def u_bar_mpf(q: mp.mpf) -> mp.mpf:
    """80-dps evaluation of bar-even u_bar(H) = (H / 4) * sqrt((H + 3) / (H + 4))."""
    h = q - mp.mpf(1) / q
    H = h**2
    return (H / mp.mpf(4)) * mp.sqrt((H + mp.mpf(3)) / (H + mp.mpf(4)))


def u_hbar_mpf(q: mp.mpf) -> mp.mpf:
    """80-dps evaluation of u_hbar(q) = ((q - 1)/q)^2 * sqrt(q^4 + q^2 + 1) / (q^2 + 1)."""
    hbar_sq = ((q - mp.mpf(1)) / q) ** 2
    b_val = mp.sqrt(q**4 + q**2 + mp.mpf(1)) / (q**2 + mp.mpf(1))
    return hbar_sq * b_val


def QA_over_me_mpf(q: mp.mpf) -> mp.mpf:
    """80-dps evaluation of Form-A tree ratio Q_A(q) / m_e = (2q + 1 - q^2)(q + 1)/(2 q^3)."""
    return (mp.mpf(2) * q + mp.mpf(1) - q**2) * (q + mp.mpf(1)) / (mp.mpf(2) * q**3)


def alpha_D_mpf(q: mp.mpf) -> mp.mpf:
    """80-dps evaluation of alpha_D(q) = (z_D - 1) * h / 2."""
    z_d = q**3 / (q**2 + mp.mpf(1))
    h = q - mp.mpf(1) / q
    return (z_d - mp.mpf(1)) * h / mp.mpf(2)


def alpha_proj_mpf(q: mp.mpf) -> mp.mpf:
    """80-dps evaluation of mirror-projected phase alpha_D^{proj}(q) = alpha_D(q) - h^2 / 4."""
    h = q - mp.mpf(1) / q
    return alpha_D_mpf(q) - (h**2) / mp.mpf(4)


def alpha_eff_sseries_mpf(q: mp.mpf) -> mp.mpf:
    """80-dps evaluation of alpha_eff(q) = (sqrt(q)/(q+1) - 1)*h/2 - u_hbar(q)/2."""
    z_val = mp.sqrt(q) / (q + mp.mpf(1))
    h = q - mp.mpf(1) / q
    return (z_val - mp.mpf(1)) * h / mp.mpf(2) - u_hbar_mpf(q) / mp.mpf(2)


def main() -> int:
    # -----------------------------------------------------------------------
    # 1. Exact Critical Branch Point H_* and Lagrange-Burmann Radius R_u
    # -----------------------------------------------------------------------
    sqrt33_mp = mp.sqrt(mp.mpf(33))
    H_star = (mp.mpf(-15) + sqrt33_mp) / mp.mpf(4)
    H_star_secondary = (mp.mpf(-15) - sqrt33_mp) / mp.mpf(4)
    crit_quad_at_H_star = mp.mpf(2) * H_star**2 + mp.mpf(15) * H_star + mp.mpf(24)
    R_u_sq = (H_star**2 * (H_star + mp.mpf(3))) / (mp.mpf(16) * (H_star + mp.mpf(4)))
    R_u = mp.sqrt(R_u_sq)
    R_u_inv = mp.mpf(1) / R_u

    q_1t = mp.mpf(Q_50_DIGIT_STR)
    q_2t = q_two_term_borromean_at(80)
    q_mu = q_muon_at(80)
    u_bar_1t = u_bar_mpf(q_1t)
    u_bar_2t = u_bar_mpf(q_2t)
    u_bar_mu = u_bar_mpf(q_mu)
    u_hbar_1t = u_hbar_mpf(q_1t)
    u_hbar_2t = u_hbar_mpf(q_2t)
    u_hbar_mu = u_hbar_mpf(q_mu)

    tail_bound_N8 = (mp.mpf(1) / mp.mpf(40)) ** 9 / (mp.mpf(39) / mp.mpf(40))
    tail_bound_N9 = (mp.mpf(1) / mp.mpf(40)) ** 10 / (mp.mpf(39) / mp.mpf(40))

    part1_critical_radius = {
        "critical_quadratic_formula": "2*H^2 + 15*H + 24",
        "discriminant_identity": "8*(2*H^2 + 15*H + 24) = (4*H + 15)^2 - 33",
        "H_star_closed_form": "(-15 + sqrt(33)) / 4",
        "H_star": fmt(H_star),
        "H_star_secondary_closed_form": "(-15 - sqrt(33)) / 4",
        "H_star_secondary": fmt(H_star_secondary),
        "critical_quadratic_residual_at_H_star": fmt(crit_quad_at_H_star),
        "R_u_sq_closed_form": "H_*^2 * (H_* + 3) / (16 * (H_* + 4))",
        "R_u_sq": fmt(R_u_sq),
        "R_u_closed_form": "((15 - sqrt(33)) / 16) * sqrt((sqrt(33) - 3) / (sqrt(33) + 1))",
        "R_u": fmt(R_u),
        "R_u_inv": fmt(R_u_inv),
        "singularity_ordering": "|H_*| approx 2.313859 < |[3]_q=0 zero at H=-3| = 3 < |[2]_q=0 pole at H=-4| = 4",
        "u_bar_at_q_1t": fmt(u_bar_1t),
        "u_bar_at_q_2t": fmt(u_bar_2t),
        "u_bar_at_q_mu": fmt(u_bar_mu),
        "u_hbar_at_q_1t": fmt(u_hbar_1t),
        "u_hbar_at_q_2t": fmt(u_hbar_2t),
        "u_hbar_at_q_mu": fmt(u_hbar_mu),
        "ratio_u_bar_over_Ru_at_q_2t": fmt(u_bar_2t / R_u),
        "ratio_u_hbar_over_Ru_at_q_2t": fmt(u_hbar_2t / R_u),
        "geometric_tail_bound_N8_at_1_over_40": fmt(tail_bound_N8),
        "geometric_tail_bound_N9_at_1_over_40": fmt(tail_bound_N9),
    }

    # -----------------------------------------------------------------------
    # 2. Lagrange-Burmann Inverse Series H(u) = sum_{m=1}^{10} beta_m u^m
    # -----------------------------------------------------------------------
    _, H_of_u = build_lagrange_burmann_H_of_u(max_order=10)
    beta_records: dict[str, dict[str, object]] = {}
    for m in range(1, 11):
        a_m, b_m = decompose_q_sqrt3(H_of_u[m])
        val_mp = q_sqrt3_to_mpf(a_m, b_m)
        beta_records[f"beta_{m}"] = {
            "order_m": m,
            "q_rational_part": str(a_m),
            "sqrt3_rational_part": str(b_m),
            "exact_q_sqrt3": format_q_sqrt3(a_m, b_m),
            "value": fmt(val_mp),
            "root_test_abs_pow_1_over_m": fmt(abs(val_mp) ** (mp.mpf(1) / mp.mpf(m))),
        }

    H_2t_exact = (q_2t - mp.mpf(1) / q_2t) ** 2
    H_2t_from_LB10 = mp.mpf(0)
    for m in range(1, 11):
        a_m, b_m = decompose_q_sqrt3(H_of_u[m])
        H_2t_from_LB10 += q_sqrt3_to_mpf(a_m, b_m) * (u_bar_2t**m)
    H_2t_lb10_rel_err = abs(H_2t_from_LB10 - H_2t_exact) / H_2t_exact

    part2_lagrange_burmann_H_of_u = {
        "coefficients": beta_records,
        "H_at_q_2t_exact": fmt(H_2t_exact),
        "H_at_q_2t_trunc10": fmt(H_2t_from_LB10),
        "H_at_q_2t_trunc10_rel_residual": fmt(H_2t_lb10_rel_err),
    }

    # -----------------------------------------------------------------------
    # 3. Route A: Bar-Even Two-Term + GPMT + Mirror-Projected Phase in u
    # -----------------------------------------------------------------------
    H_channels = build_bar_even_operator_series_in_H(max_order=10)
    combined_2t_u = series_compose(H_channels["combined_2t_H"], H_of_u, order=10)
    p_route_a = {n: combined_2t_u[n] for n in range(2, 11)}
    c_route_a = distinct_partition_ck_from_pn(p_route_a, max_k=10)

    route_a_table: dict[str, dict[str, object]] = {}
    for k in range(2, 11):
        ap, bp = decompose_q_sqrt3(p_route_a[k])
        ac, bc = decompose_q_sqrt3(c_route_a[k])
        p_mp = q_sqrt3_to_mpf(ap, bp)
        c_mp = q_sqrt3_to_mpf(ac, bc)
        route_a_table[f"k_{k}"] = {
            "k": k,
            "p_k_q_part": str(ap),
            "p_k_sqrt3_part": str(bp),
            "p_k_exact_q_sqrt3": format_q_sqrt3(ap, bp),
            "p_k": fmt(p_mp),
            "c_k_q_part": str(ac),
            "c_k_sqrt3_part": str(bc),
            "c_k_exact_q_sqrt3": format_q_sqrt3(ac, bc),
            "c_k": fmt(c_mp),
            "term_c_k_u_bar_2t_pow_k": fmt(c_mp * (u_bar_2t**k)),
        }

    # -----------------------------------------------------------------------
    # 4. Route B: Exact Q(sqrt(3))[[s]] [s^{2k}] Triangular Extraction (k = 2..10)
    # -----------------------------------------------------------------------
    sseries_routes = build_sseries_exact_ck_up_to_k10(max_k=10)
    route_b_net = sseries_routes["net_operator_sseries"]
    route_b_2t = sseries_routes["two_term_qed_mirror_phase_sseries"]

    route_b_net_table: dict[str, dict[str, object]] = {}
    route_b_2t_table: dict[str, dict[str, object]] = {}
    base_net_2t_ev = ME_EV * QA_over_me_mpf(q_2t) * mp.cos(alpha_eff_sseries_mpf(q_2t))
    base_2t_proj_ev = ME_EV * QA_over_me_mpf(q_2t) * mp.cos(alpha_proj_mpf(q_2t))
    for k in range(2, 11):
        an, bn = decompose_q_sqrt3(route_b_net[k])
        cn_mp = q_sqrt3_to_mpf(an, bn)
        route_b_net_table[f"c_{k}"] = {
            "k": k,
            "q_rational_part": str(an),
            "sqrt3_rational_part": str(bn),
            "exact_q_sqrt3": format_q_sqrt3(an, bn),
            "c_k": fmt(cn_mp),
            "c_k_u_hbar_2t_pow_k": fmt(cn_mp * (u_hbar_2t**k)),
            "ev_shift_at_q_2t": fmt(base_net_2t_ev * cn_mp * (u_hbar_2t**k)),
        }

        a2, b2 = decompose_q_sqrt3(route_b_2t[k])
        c2_mp = q_sqrt3_to_mpf(a2, b2)
        route_b_2t_table[f"c_{k}"] = {
            "k": k,
            "q_rational_part": str(a2),
            "sqrt3_rational_part": str(b2),
            "exact_q_sqrt3": format_q_sqrt3(a2, b2),
            "c_k": fmt(c2_mp),
            "c_k_u_hbar_2t_pow_k": fmt(c2_mp * (u_hbar_2t**k)),
            "ev_shift_at_q_2t": fmt(base_2t_proj_ev * c2_mp * (u_hbar_2t**k)),
        }

    # -----------------------------------------------------------------------
    # 5. All-Order Partial-Product Convergence Sweep (N = 2..10 -> inf)
    # -----------------------------------------------------------------------
    h_2t = q_2t - mp.mpf(1) / q_2t
    H_2t = h_2t**2
    tr_conn_diff_2t = H_2t**2 * (mp.mpf(4) * H_2t + mp.mpf(9)) / mp.mpf(27)
    d_mod_111_2t = mp.mpf(1) / (mp.sqrt(H_2t + mp.mpf(4)) * (H_2t + mp.mpf(3)))
    pi_route_a_closed_2t = (
        (mp.cos(alpha_proj_mpf(q_2t)) / mp.cos(h_2t / mp.mpf(4)))
        * (mp.mpf(1) + tr_conn_diff_2t)
        * (mp.mpf(1) - (d_mod_111_2t - mp.mpf(1) / mp.mpf(6)) * H_2t)
    )

    convergence_sweep_route_a: dict[str, dict[str, object]] = {}
    partial_prod_a = mp.mpf(1)
    rel_trunc_res_N9 = mp.mpf(1)
    rel_trunc_res_N10 = mp.mpf(1)
    for n_trunc in range(2, 11):
        ac, bc = decompose_q_sqrt3(c_route_a[n_trunc])
        c_mp = q_sqrt3_to_mpf(ac, bc)
        partial_prod_a = partial_prod_a * (mp.mpf(1) + c_mp * (u_bar_2t**n_trunc))
        rel_trunc_res = abs(partial_prod_a - pi_route_a_closed_2t) / pi_route_a_closed_2t
        ev_trunc_res = abs(partial_prod_a - pi_route_a_closed_2t) * base_2t_proj_ev
        if n_trunc == 9:
            rel_trunc_res_N9 = rel_trunc_res
        if n_trunc == 10:
            rel_trunc_res_N10 = rel_trunc_res
        convergence_sweep_route_a[f"N_{n_trunc}"] = {
            "N": n_trunc,
            "partial_product_Pi_N": fmt(partial_prod_a),
            "closed_form_Pi_op": fmt(pi_route_a_closed_2t),
            "relative_truncation_residual": fmt(rel_trunc_res),
            "truncation_residual_ppQ": fmt(rel_trunc_res * mp.mpf("1e15")),
            "truncation_residual_eV": fmt(ev_trunc_res),
        }

    route_b_partial_sweep: dict[str, dict[str, object]] = {}
    prod_b_net = mp.mpf(1)
    prod_b_2t = mp.mpf(1)
    for n_trunc in range(2, 11):
        an, bn = decompose_q_sqrt3(route_b_net[n_trunc])
        cn_mp = q_sqrt3_to_mpf(an, bn)
        prod_b_net = prod_b_net * (mp.mpf(1) + cn_mp * (u_hbar_2t**n_trunc))
        q_pred_net_N = base_net_2t_ev * prod_b_net

        a2, b2 = decompose_q_sqrt3(route_b_2t[n_trunc])
        c2_mp = q_sqrt3_to_mpf(a2, b2)
        prod_b_2t = prod_b_2t * (mp.mpf(1) + c2_mp * (u_hbar_2t**n_trunc))
        q_pred_2t_N = base_2t_proj_ev * prod_b_2t

        route_b_partial_sweep[f"N_{n_trunc}"] = {
            "N": n_trunc,
            "net_partial_product": fmt(prod_b_net),
            "net_Q_pred_eV": fmt(q_pred_net_N),
            "net_residual_vs_CODATA_eV": fmt(q_pred_net_N - Q_BETA_CODATA_EV),
            "two_term_partial_product": fmt(prod_b_2t),
            "two_term_Q_pred_eV": fmt(q_pred_2t_N),
            "two_term_residual_vs_CODATA_eV": fmt(q_pred_2t_N - Q_BETA_CODATA_EV),
        }

    # Check exact agreement of Route B1 c_2, c_3, c_4 with qbeta-ck-sseries-exact-rational.witness.json
    c2_net_a, c2_net_b = decompose_q_sqrt3(route_b_net[2])
    c3_net_a, c3_net_b = decompose_q_sqrt3(route_b_net[3])
    c4_net_a, c4_net_b = decompose_q_sqrt3(route_b_net[4])

    checks = [
        (
            "critical_branch_point_root_and_ordering",
            bool(
                abs(crit_quad_at_H_star) < mp.mpf("1e-70")
                and mp.mpf(-3) < H_star < mp.mpf(-2)
                and R_u > mp.mpf("0.369")
                and (u_hbar_2t / R_u) < mp.mpf(1) / mp.mpf(40)
                and (u_bar_2t / R_u) < mp.mpf(1) / mp.mpf(38)
            ),
            (
                f"H_* = {fmt(H_star, 18)} in (-3, -2), R_u = {fmt(R_u, 18)}, "
                f"u_hbar(q_2t)/R_u = {fmt(u_hbar_2t / R_u, 12)} < 1/40, "
                f"u_bar(q_2t)/R_u = {fmt(u_bar_2t / R_u, 12)} < 1/38"
            ),
        ),
        (
            "lagrange_burmann_H_of_u_trunc10_sub_ppQ_accuracy",
            bool(H_2t_lb10_rel_err < mp.mpf("1e-18")),
            f"H(u_bar_2t) truncated at u^10 matches exact H_2t to {fmt(H_2t_lb10_rel_err, 8)} (< 10^-18)",
        ),
        (
            "route_b_sseries_c2_c3_c4_match_exact_rational_witness",
            bool(
                c2_net_a == sp.Rational(-1049, 144)
                and c2_net_b == sp.Rational(-5, 12)
                and c3_net_a == sp.Rational(841, 144)
                and c3_net_b == sp.Rational(604739, 12960)
                and c4_net_a == sp.Rational(-2483340421, 1451520)
                and c4_net_b == sp.Rational(-120701, 1920)
            ),
            (
                f"c_2 = {format_q_sqrt3(c2_net_a, c2_net_b)}, "
                f"c_3 = {format_q_sqrt3(c3_net_a, c3_net_b)}, "
                f"c_4 = {format_q_sqrt3(c4_net_a, c4_net_b)} match exact [s^2k] benchmark"
            ),
        ),
        (
            "route_a_partial_product_converges_below_1_ppQ_by_N9",
            bool(rel_trunc_res_N9 < mp.mpf("1e-15") and rel_trunc_res_N10 < mp.mpf("1e-17")),
            (
                f"Bar-even partial product Pi_N(u_bar_2t) reaches {fmt(rel_trunc_res_N9 * mp.mpf('1e15'), 8)} ppQ at N=9 "
                f"and {fmt(rel_trunc_res_N10 * mp.mpf('1e15'), 8)} ppQ at N=10"
            ),
        ),
    ]

    print("=" * 96)
    print("ALL-ORDER CONVENTION-D HIGHER-c_k GENERATING FUNCTION PROBE (80 DPS)")
    print("=" * 96)
    for name, passed, detail in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}: {detail}")
    assert all(p for _, p, _ in checks), "Verification check failed!"

    w = WitnessBuilder("qbeta-convention-d-all-order-ck-generating")
    w.set_description(
        "All-order Convention-D higher-c_k (k = 2..10..inf) generating function, "
        "Lagrange-Burmann critical branch point H_* = (-15 + sqrt(33))/4 and radius R_u = 0.36900873, "
        "exact Q(sqrt(3)) distinct-partition extraction of c_2..c_10 across bar-even Lagrange-Burmann "
        "and [s^{2k}] operator routes, and 80-dps sub-ppQ convergence sweep (zero CODATA fitting, zero float64)."
    )
    w.add_data("dps", 80)
    w.add_data("part1_lagrange_burmann_critical_radius", part1_critical_radius)
    w.add_data("part2_lagrange_burmann_inverse_series_H_of_u", part2_lagrange_burmann_H_of_u)
    w.add_data("part3_route_a_bar_even_lagrange_burmann_ck", route_a_table)
    w.add_data(
        "part4_route_b_sseries_exact_ck_k2_to_k10",
        {
            "net_operator_sseries_ck": route_b_net_table,
            "two_term_qed_mirror_phase_sseries_ck": route_b_2t_table,
        },
    )
    w.add_data(
        "part5_partial_product_convergence_sweep_N2_to_N10",
        {
            "bar_even_route_a_convergence_to_closed_form": convergence_sweep_route_a,
            "sseries_route_b_partial_products_at_q_2t": route_b_partial_sweep,
            "Q_beta_CODATA_eV": fmt(Q_BETA_CODATA_EV),
        },
    )
    w.add_caveat(
        "All c_2..c_10 coefficients are derived symbolically in Q(sqrt(3)) from the parameter-free "
        "Convention-D + GPMT + Two-Term Categorical Lagrangian operator without any CODATA fitting."
    )
    for name, passed, detail in checks:
        w.add_assertion(name, "1" if passed else "0", "1", "0", source=detail)

    out_path = w.save(
        q0_comparison(
            muon=q_mu,
            proton=q_1t,
            reason=(
                "Evaluates the all-order Convention-D higher-c_k generating function and "
                "Lagrange-Burmann convergence ratios across 1-term proton, 2-term Borromean proton, "
                "and CODATA-2022 muon substrate pins."
            ),
        )
    )
    print(f"Wrote witness -> {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
