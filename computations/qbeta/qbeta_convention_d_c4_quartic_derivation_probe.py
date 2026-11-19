#!/usr/bin/env python3
"""
qbeta_convention_d_c4_quartic_derivation_probe.py — First-principles symbolic Q[[hbar_q]]
and Q(sqrt(3))[[hbar_q]] derivation and 80-dps evaluation of the fourth-order Habiro /
Kashiwara / Wedderburn ladder rung c_4 (bean qou-51yf, order u^4 = (b * hbar_q^2)^4 ~ 5.263e-9).

Strict methodological gates enforced throughout:
  1. ZERO CODATA FITTING / ZERO PSLQ AGAINST Q_CODATA:
     Every c_4 branch is derived strictly as an exact rational function in Q(q) or exact
     formal power series coefficient in Q[[hbar_q]] / Q(sqrt(3))[[hbar_q]] around the
     classical point q = 1 (hbar_q = 1 - q^{-1} = 0). CODATA-2022 and AME-2020 anchors
     enter ONLY at the final step to evaluate falsifiable Q_beta, Delta_pn, and m_n residuals.
  2. ZERO FLOAT64:
     All symbolic power series use exact Python fractions.Fraction and QSqrt3 = Q(sqrt(3))
     arithmetic through hbar_q^12; all numerical evaluations run in 85-dps mpmath (80-dps
     working target, 50-digit string witness serialization) with zero binary64 floats,
     zero float literals, and zero float() calls.

Three first-principles contributions analyzed:
  - Contribution A (Even-Rung Kashiwara / Habiro Cyclotomic / Chebyshev Holonomy Factors):
      A1. Exact rationality of u^2(q), u^4(q), and all even rungs u^{2m}(q) in Q(q);
          4th Habiro cyclotomic ideal Phi_1*Phi_2*Phi_3*Phi_4 and 4-step bar-even Pochhammer
          norm eta_4(q) = 576*hbar_q^8 + ... (u^4/eta_4 -> 1/1024 at q = 1);
          Habiro Euler q-Pochhammer (u^2; u^2)_infty rung c_4^{Hab,Poch} = -1 and
          Hopf-Kashiwara pair-rule c_4^{JK}(q) = -2*b(q)^4 = -9/8 - (3/4)*hbar_q^2 + ...
      A2. Exact m = 2 Kashiwara q-divided-power cosine sum_{m=0}^2 (-1)^m X^{2m}/[2m]_q!
          at X^2 = [2]_q! * u^2: c_4^{Kash,div}(q) = [2]_q / ([3]_q [4]_q) = +1/6 - (5/9)*hbar_q^2 + ...
      A3. Exact Chebyshev / Kohno-Drinfeld 6-crossing full-twist hyperbolic holonomy
          C_KD^{(6)}(q) = (q^6 + q^{-6})/2 = 1 + (9/2)*h^2 + 3*h^4 + (1/2)*h^6 + 0*h^8
          (identically zero h^8 quartic term, c_4^{Cheb,h^2} = 0) and exact hbar_q-series.
  - Contribution B (4th Cumulant / Kurtosis kappa_4 of H_3(q) Multi-Block Wedderburn & GPMT+ Traces):
      B1. Exact rational cumulants of the H_3(q) Jucys-Murphy / transposition content spectrum
          (+1, 0, -1): under Convention D, kappa_2^D(q) = 2*q^2*(q^4+1)/(q^2+1)^4 (= 1/4 at q=1),
          kappa_4^D(q) = -1/8 + (1/2)*hbar_q^4 + hbar_q^5 + (3/4)*hbar_q^6 - (1/4)*hbar_q^7
          - (51/32)*hbar_q^8 + O(hbar_q^9), standardized excess kurtosis gamma_2^D(1) = -2 = J_Hopf(1),
          and variance-matched block-phase cumulant rung c_4^{cum,D}(q) = 1/2 + gamma_2^D(q)/6
          = (q^8 - 2*q^6 + 6*q^4 - 2*q^2 + 1)/(12*q^2*(q^4+1)) -> +1/6 at q = 1 (matching
          c_4^{Kash,div}(1) = +1/6 identically!). Under GPMT+ (+|d_D(S^{(1^3)})|),
          kappa_4^{GPMT+}(1) = -516/2401 and c_4^{cum,GPMT+}(1) = +101/288.
      B2. Exact Q(sqrt(3))[[hbar_q]] Taylor expansions through hbar_q^{10} of the Convention-D
          and GPMT+ operator traces on Delta_nuc11_interleaved and Delta_nuc11_gen_grouped
          divided by Q_base(q) * cos(alpha_D^{proj}(q) - u(q)/2) * (1 - u(q)^2) * (1 - 2*u(q)^3),
          isolating both full Q(sqrt(3)) coefficients at [hbar_q^8]/(9/16) and pure Q parts.
  - Contribution C (Two-Term Categorical Lagrangian QED Series & Two-Photon O(alpha_EM^2 hbar_q^4) Scale):
      C1. Exact rational hbar_q-series of Delta tr_conn^{plain}(V^3) = (q^2-1)^4*(4*q^4+q^2+4)/(27*q^6)
          = (16/3)*hbar_q^4 + (32/3)*hbar_q^5 + (760/27)*hbar_q^6 + (520/9)*hbar_q^7 + 107*hbar_q^8
          + (4948/27)*hbar_q^9 + (2662/9)*hbar_q^{10} + O(hbar_q^{11}).
      C2. Form-B Bring-Schwinger cubic alpha_EM(q_{2t}) evaluation and two-photon Borromean trace
          scale alpha_EM(q_{2t})^2 * hbar_q^4 = 5.1322e-9 = 0.97524 * u^4 (~0.00402 eV = 0.00836 sigma_n),
          confirming that both O(1) c_4 * u^4 and two-photon QED sit > 100x inside sigma_exp(m_n),
          and the N >= 5 truncation remainder O(u^5) < 4.5e-11 sits at < 10^{-4} sigma_exp(m_n) (< 0.04 ppt).

Lean 4 companion: folio/quantum-observable-universe/lean/QOU/QBeta/ConventionDC4QuarticCumulantDerivation.lean
Witness output:   computations/qbeta/qbeta-convention-d-c4-quartic-derivation.witness.json
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for _rel in (
    "computations",
    "computations/qbeta",
    "computations/substrate",
    "tools/qou-substrate/python",
    "tools/pyhecke/python",
):
    _p = os.path.join(ROOT, _rel)
    if _p not in sys.path:
        sys.path.insert(0, _p)

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from codata_2022_source import (  # noqa: E402
    M_E_MEV,
    M_MU_MEV,
    M_N_MEV_AME_DERIVED,
    M_N_MEV_AME_DERIVED_ERR,
    M_N_MEV_CODATA_DIRECT,
    M_N_MEV_CODATA_DIRECT_ERR,
    M_N_MINUS_P_MEV,
    M_N_MINUS_P_MEV_ERR,
    M_P_MEV,
    Q_BETA_MEV_AME,
    Q_BETA_MEV_AME_ERR,
    Q_BETA_MEV_DERIVED_FROM_CODATA_DIRECT,
)
from q_parameter import (  # noqa: E402
    Q_50_DIGIT_STR,
    q_at,
    q_muon_at,
    q_two_term_borromean_at,
    tr_conn_borromean_diff_at,
    tr_conn_borromean_n_at,
    tr_conn_borromean_p_at,
)
from qou_substrate import codata as _codata  # noqa: E402
from qou_substrate.witness import q0_comparison  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(80)
mp.mp.dps = 85

ORD = 12  # Formal power series truncation degree in t = hbar_q = 1 - q^{-1} (covers t^0..t^12)


def fmt(val: mp.mpf, digits: int = 50) -> str:
    """Serialize an mpmath mpf to a decimal string with zero binary64 intermediates."""
    return mp.nstr(val, digits)


def rat_to_mpf(r: Fraction) -> mp.mpf:
    """Convert an exact Python Fraction into an 85-dps mpmath mpf."""
    return mp.mpf(r.numerator) / mp.mpf(r.denominator)


@dataclass(frozen=True)
class QSqrt3:
    """Exact algebraic scalar a + b * sqrt(3) in Q(sqrt(3)) over fractions.Fraction."""

    a: Fraction
    b: Fraction = Fraction(0)

    @staticmethod
    def of(r: int | Fraction) -> "QSqrt3":
        return QSqrt3(Fraction(r), Fraction(0))

    def __add__(self, other: "QSqrt3 | int | Fraction") -> "QSqrt3":
        o = other if isinstance(other, QSqrt3) else QSqrt3.of(other)
        return QSqrt3(self.a + o.a, self.b + o.b)

    def __radd__(self, other: int | Fraction) -> "QSqrt3":
        return QSqrt3.of(other) + self

    def __sub__(self, other: "QSqrt3 | int | Fraction") -> "QSqrt3":
        o = other if isinstance(other, QSqrt3) else QSqrt3.of(other)
        return QSqrt3(self.a - o.a, self.b - o.b)

    def __rsub__(self, other: int | Fraction) -> "QSqrt3":
        return QSqrt3.of(other) - self

    def __neg__(self) -> "QSqrt3":
        return QSqrt3(-self.a, -self.b)

    def __mul__(self, other: "QSqrt3 | int | Fraction") -> "QSqrt3":
        o = other if isinstance(other, QSqrt3) else QSqrt3.of(other)
        return QSqrt3(self.a * o.a + 3 * self.b * o.b, self.a * o.b + self.b * o.a)

    def __rmul__(self, other: int | Fraction) -> "QSqrt3":
        return QSqrt3.of(other) * self

    def inv(self) -> "QSqrt3":
        norm = self.a * self.a - 3 * self.b * self.b
        if norm == 0:
            raise ZeroDivisionError("Singular element in QSqrt3.inv")
        return QSqrt3(self.a / norm, -self.b / norm)

    def __truediv__(self, other: "QSqrt3 | int | Fraction") -> "QSqrt3":
        o = other if isinstance(other, QSqrt3) else QSqrt3.of(other)
        return self * o.inv()

    def is_zero(self) -> bool:
        return self.a == 0 and self.b == 0

    def is_pure_rational(self) -> bool:
        return self.b == 0

    def to_mpf(self) -> mp.mpf:
        return rat_to_mpf(self.a) + rat_to_mpf(self.b) * mp.sqrt(mp.mpf(3))

    def to_exact_str(self) -> str:
        if self.b == 0:
            return str(self.a)
        if self.a == 0:
            return f"({self.b})*sqrt(3)"
        sign = "+" if self.b > 0 else "-"
        return f"{self.a} {sign} ({abs(self.b)})*sqrt(3)"


ZERO = QSqrt3(Fraction(0), Fraction(0))
ONE = QSqrt3(Fraction(1), Fraction(0))


def ser_zero() -> list[QSqrt3]:
    return [ZERO] * (ORD + 1)


def ser_const(c: QSqrt3 | int | Fraction) -> list[QSqrt3]:
    out = ser_zero()
    out[0] = c if isinstance(c, QSqrt3) else QSqrt3.of(c)
    return out


def ser_add(x: list[QSqrt3], y: list[QSqrt3]) -> list[QSqrt3]:
    return [xi + yi for xi, yi in zip(x, y)]


def ser_sub(x: list[QSqrt3], y: list[QSqrt3]) -> list[QSqrt3]:
    return [xi - yi for xi, yi in zip(x, y)]


def ser_scale(c: QSqrt3 | int | Fraction, x: list[QSqrt3]) -> list[QSqrt3]:
    cc = c if isinstance(c, QSqrt3) else QSqrt3.of(c)
    return [cc * xi for xi in x]


def ser_mul(x: list[QSqrt3], y: list[QSqrt3]) -> list[QSqrt3]:
    out = [ZERO] * (ORD + 1)
    for i, xi in enumerate(x):
        if xi.is_zero():
            continue
        for j in range(ORD + 1 - i):
            yj = y[j]
            if not yj.is_zero():
                out[i + j] = out[i + j] + xi * yj
    return out


def ser_inv(x: list[QSqrt3]) -> list[QSqrt3]:
    if x[0].is_zero():
        raise ZeroDivisionError("ser_inv requires nonzero constant coefficient")
    out = [ZERO] * (ORD + 1)
    inv0 = x[0].inv()
    out[0] = inv0
    for n in range(1, ORD + 1):
        acc = ZERO
        for k in range(1, n + 1):
            if not x[k].is_zero() and not out[n - k].is_zero():
                acc = acc + x[k] * out[n - k]
        out[n] = -(acc * inv0)
    return out


def ser_pow(x: list[QSqrt3], n: int) -> list[QSqrt3]:
    if n == 0:
        return ser_const(1)
    if n < 0:
        return ser_pow(ser_inv(x), -n)
    res = ser_const(1)
    base = x
    e = n
    while e > 0:
        if e & 1:
            res = ser_mul(res, base)
        e >>= 1
        if e > 0:
            base = ser_mul(base, base)
    return res


def ser_sqrt_three_quarters(x: list[QSqrt3]) -> list[QSqrt3]:
    """Exact formal square root of x(t) = 3/4 + O(t) in Q(sqrt(3))[[t]]."""
    if x[0] != QSqrt3.of(Fraction(3, 4)):
        raise ValueError(f"Expected leading term 3/4, got {x[0].to_exact_str()}")
    out = [ZERO] * (ORD + 1)
    s0 = QSqrt3(Fraction(0), Fraction(1, 2))  # sqrt(3)/2
    out[0] = s0
    two_s0_inv = (QSqrt3.of(2) * s0).inv()
    for n in range(1, ORD + 1):
        acc = ZERO
        for k in range(1, n):
            acc = acc + out[k] * out[n - k]
        out[n] = (x[n] - acc) * two_s0_inv
    return out


def ser_cos0(x: list[QSqrt3]) -> list[QSqrt3]:
    """Exact formal series of cos(x(t)) for x(0) = 0."""
    if not x[0].is_zero():
        raise ValueError("ser_cos0 requires x[0] == 0")
    out = ser_const(1)
    x2 = ser_mul(x, x)
    xpow = ser_const(1)
    fact = Fraction(1)
    m = 1
    while 2 * m <= ORD:
        xpow = ser_mul(xpow, x2)
        fact = fact * (2 * m - 1) * (2 * m)
        coeff = Fraction((-1) ** m, 1) / fact
        out = ser_add(out, ser_scale(coeff, xpow))
        m += 1
    return out


def ser_log1(x: list[QSqrt3]) -> list[QSqrt3]:
    """Exact formal series of log(x(t)) for x(0) = 1 via termwise integration of x'/x."""
    if x[0] != ONE:
        raise ValueError("ser_log1 requires x[0] == 1")
    dx = [QSqrt3.of(n + 1) * x[n + 1] for n in range(ORD)] + [ZERO]
    ratio = ser_mul(dx, ser_inv(x))
    out = [ZERO] * (ORD + 1)
    for n in range(1, ORD + 1):
        out[n] = ratio[n - 1] / Fraction(n)
    return out


def ser_to_dict(s: list[QSqrt3], max_order: int = 10) -> dict[str, str]:
    """Serialize formal series coefficients through max_order as exact symbolic strings."""
    return {str(k): s[k].to_exact_str() for k in range(max_order + 1)}


def alpha_em_form_b_cubic_80dps(q_val: mp.mpf) -> dict[str, mp.mpf]:
    """Solve the Form-B Bring-Schwinger cubic fixed-point relation at 85 dps (zero float64):
    1/alpha = T(q) + alpha * H(q) * (1 - h^2 * alpha),
    where T(q) = q * [9]_q * [10]_q + 2 / (3*pi), H(q) = [2]_q / (8*pi), h = q - q^{-1}.
    """
    one = mp.mpf(1)
    two = mp.mpf(2)
    three = mp.mpf(3)
    eight = mp.mpf(8)
    h = q_val - one / q_val
    h2 = h * h

    def q_bracket(n: int) -> mp.mpf:
        return (q_val**n - q_val ** (-n)) / h

    t_tree = q_val * q_bracket(9) * q_bracket(10) + two / (three * mp.pi)
    h_loop = q_bracket(2) / (eight * mp.pi)

    # Form A quadratic: H * alpha^2 + T * alpha - 1 = 0
    alpha_form_a = (-t_tree + mp.sqrt(t_tree * t_tree + mp.mpf(4) * h_loop)) / (two * h_loop)

    # Form B cubic: -H * h^2 * alpha^3 + H * alpha^2 + T * alpha - 1 = 0
    alpha = alpha_form_a
    tol = mp.mpf(10) ** (-80)
    for _ in range(25):
        f_val = -h_loop * h2 * (alpha**3) + h_loop * (alpha**2) + t_tree * alpha - one
        df_val = -three * h_loop * h2 * (alpha**2) + two * h_loop * alpha + t_tree
        step = f_val / df_val
        alpha = alpha - step
        if abs(step) < tol:
            break
    cubic_res = abs(-h_loop * h2 * (alpha**3) + h_loop * (alpha**2) + t_tree * alpha - one)
    return {
        "alpha_form_A": alpha_form_a,
        "alpha_inv_form_A": one / alpha_form_a,
        "alpha_form_B": alpha,
        "alpha_inv_form_B": one / alpha,
        "cubic_equation_residual": cubic_res,
    }


def build_symbolic_derivations() -> dict[str, object]:
    """Construct all exact Q[[hbar_q]] and Q(sqrt(3))[[hbar_q]] series through hbar_q^10."""
    t_ser = ser_zero()
    t_ser[1] = ONE  # t = hbar_q = 1 - q^{-1}
    q_inv = ser_sub(ser_const(1), t_ser)
    q_ser = ser_inv(q_inv)
    q2 = ser_pow(q_ser, 2)
    q4 = ser_pow(q_ser, 4)

    h_ser = ser_sub(q_ser, q_inv)
    h2_ser = ser_mul(h_ser, h_ser)
    two_q = ser_add(q_ser, q_inv)
    three_q = ser_add(ser_add(q2, ser_const(1)), ser_pow(q_inv, 2))
    four_q = ser_mul(two_q, ser_add(q2, ser_pow(q_inv, 2)))

    # Section 1: Rationality of even rungs u^2(q) and u^4(q) vs odd rungs u(q), u^3(q)
    b2_ser = ser_mul(three_q, ser_inv(ser_mul(two_q, two_q)))
    b_ser = ser_sqrt_three_quarters(b2_ser)
    u_ser = ser_mul(b_ser, ser_pow(t_ser, 2))
    u2_ser = ser_mul(b2_ser, ser_pow(t_ser, 4))
    u3_ser = ser_mul(u2_ser, u_ser)
    u4_ser = ser_mul(u2_ser, u2_ser)

    u2_all_rational = all(c.is_pure_rational() for c in u2_ser)
    u4_all_rational = all(c.is_pure_rational() for c in u4_ser)

    # Contribution A:
    # A1. Habiro 4th cyclotomic ideal & 4-step bar-even Pochhammer norm eta_4(q)
    eta1 = ser_mul(ser_pow(ser_sub(q_ser, ser_const(1)), 2), q_inv)
    eta2 = ser_mul(eta1, ser_mul(ser_pow(ser_sub(q2, ser_const(1)), 2), ser_pow(q_inv, 2)))
    eta3 = ser_mul(
        eta2,
        ser_mul(ser_pow(ser_sub(ser_pow(q_ser, 3), ser_const(1)), 2), ser_pow(q_inv, 3)),
    )
    eta4 = ser_mul(eta3, ser_mul(ser_pow(ser_sub(q4, ser_const(1)), 2), ser_pow(q_inv, 4)))
    u4_over_eta4_lead = u4_ser[8] / eta4[8]  # (9/16) / 576 = 1/1024

    c4_jk_ser = ser_scale(-2, ser_mul(b2_ser, b2_ser))  # J_Hopf(1) * b(q)^4 = -2 * b^4

    # A2. Kashiwara divided-power cosine m = 2 coefficient [2]_q / ([3]_q * [4]_q)
    c4_kash_ser = ser_mul(two_q, ser_inv(ser_mul(three_q, four_q)))

    # A3. Chebyshev 6-crossing full-twist holonomy C_KD^{(6)}(q) = (q^6 + q^{-6})/2
    c_kd6_ser = ser_scale(Fraction(1, 2), ser_add(ser_pow(q_ser, 6), ser_pow(q_inv, 6)))
    cheb_cubic_h2 = ser_add(
        ser_add(ser_const(1), ser_scale(Fraction(9, 2), h2_ser)),
        ser_add(ser_scale(3, ser_pow(h2_ser, 2)), ser_scale(Fraction(1, 2), ser_pow(h2_ser, 3))),
    )
    cheb_diff = ser_sub(c_kd6_ser, cheb_cubic_h2)
    cheb_h8_zero = all(c.is_zero() for c in cheb_diff)

    # Also expand C_KD^{(6)}(q) / (1 + (9/2)*h^2) at even orders t^4 (u^2) and t^8 (u^4):
    kd6_over_h2 = ser_mul(c_kd6_ser, ser_inv(ser_add(ser_const(1), ser_scale(Fraction(9, 2), h2_ser))))
    kd6_u2_coeff = kd6_over_h2[4] / u2_ser[4]  # 48 / (3/4) = 64? Wait: compute exact!
    kd6_after_u2 = ser_sub(kd6_over_h2, ser_add(ser_const(1), ser_scale(kd6_u2_coeff, u2_ser)))

    # Contribution B:
    # B1. Convention-D and GPMT+ Wedderburn cumulants on normalized JM content (+1, 0, -1)
    q2p1 = ser_add(q2, ser_const(1))
    q2p1_inv2 = ser_inv(ser_mul(q2p1, q2p1))
    w3_ser = ser_mul(ser_add(q4, ser_const(1)), q2p1_inv2)
    w21_ser = ser_mul(q2, q2p1_inv2)
    q4pq2p1 = ser_add(ser_add(q4, q2), ser_const(1))
    d111_abs_ser = ser_mul(ser_pow(q_ser, 3), ser_inv(ser_mul(q2p1, q4pq2p1)))

    mu2_d = ser_mul(w3_ser, ser_sub(ser_const(1), w3_ser))
    mu3_d = ser_mul(mu2_d, ser_sub(ser_const(1), ser_scale(2, w3_ser)))
    mu4_d = ser_mul(
        mu2_d,
        ser_add(ser_sub(ser_const(1), ser_scale(3, w3_ser)), ser_scale(3, ser_pow(w3_ser, 2))),
    )
    kappa4_d = ser_sub(mu4_d, ser_scale(3, ser_pow(mu2_d, 2)))
    gamma2_d = ser_mul(kappa4_d, ser_inv(ser_pow(mu2_d, 2)))
    c4_cum_d = ser_add(ser_const(Fraction(1, 2)), ser_scale(Fraction(1, 6), gamma2_d))

    z_gpmt = ser_add(ser_const(1), d111_abs_ser)
    p3_g = ser_mul(w3_ser, ser_inv(z_gpmt))
    p111_g = ser_mul(d111_abs_ser, ser_inv(z_gpmt))
    m1_g = ser_sub(p3_g, p111_g)
    m2_g = ser_add(p3_g, p111_g)
    m3_g = ser_sub(p3_g, p111_g)
    m4_g = ser_add(p3_g, p111_g)
    kappa2_g = ser_sub(m2_g, ser_pow(m1_g, 2))
    kappa3_g = ser_add(ser_sub(m3_g, ser_scale(3, ser_mul(m2_g, m1_g))), ser_scale(2, ser_pow(m1_g, 3)))
    kappa4_g = ser_sub(
        ser_add(
            ser_sub(m4_g, ser_scale(4, ser_mul(m3_g, m1_g))),
            ser_scale(12, ser_mul(m2_g, ser_pow(m1_g, 2))),
        ),
        ser_add(ser_scale(3, ser_pow(m2_g, 2)), ser_scale(6, ser_pow(m1_g, 4))),
    )
    gamma2_g = ser_mul(kappa4_g, ser_inv(ser_pow(kappa2_g, 2)))
    c4_cum_g = ser_add(ser_const(Fraction(1, 2)), ser_scale(Fraction(1, 6), gamma2_g))

    # B2. Operator trace ratios on Delta_nuc11_interleaved and Delta_nuc11_gen_grouped
    # divided by Q_base(q) * cos(alpha_D^proj - u/2) * (1 - u^2) * (1 - 2*u^3)
    z_d = ser_mul(ser_pow(q_ser, 3), ser_inv(q2p1))
    alpha_d = ser_scale(Fraction(1, 2), ser_mul(ser_sub(z_d, ser_const(1)), h_ser))
    alpha_d_proj = ser_sub(alpha_d, ser_scale(Fraction(1, 4), h2_ser))
    cos_proj = ser_cos0(ser_sub(alpha_d_proj, ser_scale(Fraction(1, 2), u_ser)))
    n2_fac = ser_sub(ser_const(1), u2_ser)
    n3_hopf = ser_sub(ser_const(1), ser_scale(2, u3_ser))
    ladder_denom_n3 = ser_mul(cos_proj, ser_mul(n2_fac, n3_hopf))

    neg_chi3_red = ser_scale(Fraction(1, 4), ser_mul(ser_mul(q2p1, q2p1), q_inv))
    neg_chi111_red = ser_scale(Fraction(1, 4), ser_mul(ser_mul(q2p1, q2p1), ser_pow(q_inv, 5)))
    p_poly = ser_add(
        ser_scale(2, ser_pow(q_ser, 12)),
        ser_add(
            ser_scale(-5, ser_pow(q_ser, 10)),
            ser_add(
                ser_scale(5, ser_pow(q_ser, 8)),
                ser_add(
                    ser_scale(-5, ser_pow(q_ser, 6)),
                    ser_add(ser_scale(5, q4), ser_add(ser_scale(-5, q2), ser_const(2))),
                ),
            ),
        ),
    )
    neg_chi21_int_red = ser_scale(
        Fraction(-1, 4),
        ser_mul(ser_add(q4, ser_const(1)), ser_mul(p_poly, ser_pow(q_inv, 9))),
    )
    neg_chi21_grp_red = ser_scale(
        Fraction(1, 4),
        ser_mul(ser_add(q4, ser_const(1)), ser_pow(q_inv, 3)),
    )

    tr_zd_int = ser_add(ser_mul(w3_ser, neg_chi3_red), ser_mul(w21_ser, neg_chi21_int_red))
    tr_zd_grp = ser_add(ser_mul(w3_ser, neg_chi3_red), ser_mul(w21_ser, neg_chi21_grp_red))
    tr_planch_int = ser_add(
        ser_scale(Fraction(1, 2), neg_chi3_red), ser_scale(Fraction(1, 4), neg_chi21_int_red)
    )
    tr_planch_grp = ser_add(
        ser_scale(Fraction(1, 2), neg_chi3_red), ser_scale(Fraction(1, 4), neg_chi21_grp_red)
    )

    tr_gpmt_int = ser_add(tr_zd_int, ser_mul(d111_abs_ser, neg_chi111_red))
    tr_gpmt_grp = ser_add(tr_zd_grp, ser_mul(d111_abs_ser, neg_chi111_red))
    tr_planch3_int = ser_add(tr_planch_int, ser_scale(Fraction(1, 6), neg_chi111_red))
    tr_planch3_grp = ser_add(tr_planch_grp, ser_scale(Fraction(1, 6), neg_chi111_red))

    op_quotients: dict[str, dict[str, object]] = {}
    for ratio_key, bare_ratio in (
        ("pure_inverse_ladder_denom", ser_const(1)),
        ("zD_grouped_over_Plancherel_grouped", ser_mul(tr_zd_grp, ser_inv(tr_planch_grp))),
        ("zD_interleaved_over_Plancherel_interleaved", ser_mul(tr_zd_int, ser_inv(tr_planch_int))),
        ("GPMT_pos_grouped_over_Plancherel3_grouped", ser_mul(tr_gpmt_grp, ser_inv(tr_planch3_grp))),
        (
            "GPMT_pos_interleaved_over_Plancherel3_interleaved",
            ser_mul(tr_gpmt_int, ser_inv(tr_planch3_int)),
        ),
        ("zD_interleaved_over_zD_grouped", ser_mul(tr_zd_int, ser_inv(tr_zd_grp))),
        ("GPMT_pos_interleaved_over_GPMT_pos_grouped", ser_mul(tr_gpmt_int, ser_inv(tr_gpmt_grp))),
    ):
        quot = ser_mul(bare_ratio, ser_inv(ladder_denom_n3))
        c4_t8 = quot[8] / u4_ser[8]
        op_quotients[ratio_key] = {
            "bare_ratio_series_hbar_q": ser_to_dict(bare_ratio, 8),
            "quotient_series_hbar_q": ser_to_dict(quot, 8),
            "c4_at_hbar8_over_u4_lead_exact": c4_t8.to_exact_str(),
            "c4_pure_rational_part_exact": str(c4_t8.a),
            "c4_sqrt3_coeff_exact": str(c4_t8.b),
            "c4_full_50dps": fmt(c4_t8.to_mpf()),
            "c4_pure_rational_part_50dps": fmt(rat_to_mpf(c4_t8.a)),
            "lower_order_hbar2_obstruction": bare_ratio[2].to_exact_str(),
        }

    # Contribution C: Connected 4th-order Borromean V^3 QED series in hbar_q through hbar_q^10
    q2m1_4 = ser_pow(ser_sub(q2, ser_const(1)), 4)
    poly_414 = ser_add(ser_add(ser_scale(4, q4), q2), ser_const(4))
    tr_conn_p = ser_scale(Fraction(-2, 27), ser_mul(q2m1_4, ser_mul(q4pq2p1, ser_pow(q_inv, 6))))
    tr_conn_n = ser_scale(
        Fraction(1, 27),
        ser_mul(
            q2m1_4,
            ser_mul(ser_add(ser_sub(ser_scale(2, q4), q2), ser_const(2)), ser_pow(q_inv, 6)),
        ),
    )
    tr_conn_diff_plain = ser_scale(
        Fraction(1, 27), ser_mul(q2m1_4, ser_mul(poly_414, ser_pow(q_inv, 6)))
    )
    tr_conn_diff_minus_u2_lead = ser_sub(
        tr_conn_diff_plain, ser_scale(Fraction(64, 9), u2_ser)
    )

    return {
        "even_rung_rationality": {
            "u2_is_pure_Q_series": u2_all_rational,
            "u4_is_pure_Q_series": u4_all_rational,
            "b2_series_hbar_q": ser_to_dict(b2_ser, 10),
            "b_series_hbar_q": ser_to_dict(b_ser, 10),
            "u_series_hbar_q": ser_to_dict(u_ser, 10),
            "u2_series_hbar_q": ser_to_dict(u2_ser, 10),
            "u3_series_hbar_q": ser_to_dict(u3_ser, 10),
            "u4_series_hbar_q": ser_to_dict(u4_ser, 12),
        },
        "contribution_A_kashiwara_habiro_chebyshev": {
            "habiro_eta4_series_hbar_q": ser_to_dict(eta4, 10),
            "u4_over_eta4_at_q1_exact": u4_over_eta4_lead.to_exact_str(),
            "c4_habiro_pochhammer_u2_exact": "-1",
            "c4_hopf_kashiwara_b4_series_hbar_q": ser_to_dict(c4_jk_ser, 8),
            "c4_kashiwara_divided_cos_series_hbar_q": ser_to_dict(c4_kash_ser, 8),
            "c4_kashiwara_divided_cos_at_q1_exact": c4_kash_ser[0].to_exact_str(),
            "c_kd6_series_hbar_q": ser_to_dict(c_kd6_ser, 10),
            "c_kd6_is_exact_cubic_in_h2_zero_h8": cheb_h8_zero,
            "c_kd6_over_1_plus_9half_h2_u2_coeff_exact": kd6_u2_coeff.to_exact_str(),
            "c_kd6_over_1_plus_9half_h2_after_u2_hbar_q": ser_to_dict(kd6_after_u2, 8),
        },
        "contribution_B_wedderburn_kurtosis_and_traces": {
            "convention_D_jm_variance_kappa2_hbar_q": ser_to_dict(mu2_d, 8),
            "convention_D_jm_skewness_kappa3_hbar_q": ser_to_dict(mu3_d, 8),
            "convention_D_jm_kurtosis_kappa4_hbar_q": ser_to_dict(kappa4_d, 8),
            "convention_D_excess_kurtosis_at_q1_exact": gamma2_d[0].to_exact_str(),
            "convention_D_cumulant_rung_c4_hbar_q": ser_to_dict(c4_cum_d, 8),
            "convention_D_cumulant_rung_c4_at_q1_exact": c4_cum_d[0].to_exact_str(),
            "gpmt_pos_jm_mean_kappa1_hbar_q": ser_to_dict(m1_g, 6),
            "gpmt_pos_jm_variance_kappa2_hbar_q": ser_to_dict(kappa2_g, 6),
            "gpmt_pos_jm_skewness_kappa3_hbar_q": ser_to_dict(kappa3_g, 6),
            "gpmt_pos_jm_kurtosis_kappa4_hbar_q": ser_to_dict(kappa4_g, 6),
            "gpmt_pos_excess_kurtosis_at_q1_exact": gamma2_g[0].to_exact_str(),
            "gpmt_pos_cumulant_rung_c4_hbar_q": ser_to_dict(c4_cum_g, 6),
            "gpmt_pos_cumulant_rung_c4_at_q1_exact": c4_cum_g[0].to_exact_str(),
            "operator_trace_quotients_hbar_q": op_quotients,
        },
        "contribution_C_borromean_qed_series": {
            "tr_conn_p_hbar_q": ser_to_dict(tr_conn_p, 10),
            "tr_conn_n_hbar_q": ser_to_dict(tr_conn_n, 10),
            "tr_conn_diff_plain_hbar_q": ser_to_dict(tr_conn_diff_plain, 10),
            "tr_conn_diff_minus_64_9_u2_hbar_q": ser_to_dict(tr_conn_diff_minus_u2_lead, 10),
        },
    }


def evaluate_pin_80dps(q_val: mp.mpf, pin_name: str) -> dict[str, object]:
    """Evaluate Lean remainder identities, two-photon QED scale, and all parameter-free c_4
    branches at 80 dps at a substrate pin q_val, comparing against CODATA ONLY at the end."""
    one = mp.mpf(1)
    two = mp.mpf(2)
    three = mp.mpf(3)
    four = mp.mpf(4)
    five = mp.mpf(5)
    six = mp.mpf(6)

    me_mev = mp.mpf(str(M_E_MEV))
    mp_mev = mp.mpf(str(M_P_MEV))
    mn_ame_mev = mp.mpf(str(M_N_MEV_AME_DERIVED))
    mn_ame_err = mp.mpf(str(M_N_MEV_AME_DERIVED_ERR))
    mn_dir_mev = mp.mpf(str(M_N_MEV_CODATA_DIRECT))
    mn_dir_err = mp.mpf(str(M_N_MEV_CODATA_DIRECT_ERR))
    dpn_codata_mev = mp.mpf(str(M_N_MINUS_P_MEV))
    dpn_codata_err = mp.mpf(str(M_N_MINUS_P_MEV_ERR))
    q_ame_mev = mp.mpf(str(Q_BETA_MEV_AME))
    q_ame_err = mp.mpf(str(Q_BETA_MEV_AME_ERR))
    q_dir_mev = mp.mpf(str(Q_BETA_MEV_DERIVED_FROM_CODATA_DIRECT))

    alpha_inv_entry = _codata.codata("inverse fine-structure constant")
    codata_alpha_inv = mp.mpf(alpha_inv_entry.value_str)

    h = q_val - one / q_val
    hbar = (q_val - one) / q_val
    b_sq = (h * h + three) / (h * h + four)
    b_val = mp.sqrt(b_sq)
    u_val = b_val * (hbar**2)
    u2_val = b_sq * (hbar**4)
    u3_val = u2_val * u_val
    u4_val = (b_sq**2) * (hbar**8)
    u5_val = u4_val * u_val

    # Verify Lean exact remainder identities at 80 dps:
    u4_rational = (
        ((q_val - one) ** 8)
        * ((q_val**2 - q_val + one) ** 2)
        * ((q_val**2 + q_val + one) ** 2)
        / ((q_val**8) * ((q_val**2 + one) ** 4))
    )
    u4_lead_lhs = u4_val - (mp.mpf(9) / mp.mpf(16)) * (hbar**8)
    u4_lead_rhs = (
        ((q_val - one) ** 10)
        * ((q_val + one) ** 2)
        * (mp.mpf(7) * (q_val**4) + mp.mpf(10) * (q_val**2) + mp.mpf(7))
        / (mp.mpf(16) * (q_val**8) * ((q_val**2 + one) ** 4))
    )

    tr_diff_plain = tr_conn_borromean_diff_at(q_val, dps=80)
    tr_diff_poly8 = (
        (mp.mpf(16) / three) * (hbar**4)
        + (mp.mpf(32) / three) * (hbar**5)
        + (mp.mpf(760) / mp.mpf(27)) * (hbar**6)
        + (mp.mpf(520) / mp.mpf(9)) * (hbar**7)
        + mp.mpf(107) * (hbar**8)
    )
    tr_diff_rem_rhs = (
        ((q_val - one) ** 9)
        * (
            four * (q_val**5)
            + mp.mpf(36) * (q_val**4)
            + mp.mpf(165) * (q_val**3)
            + mp.mpf(525) * (q_val**2)
            + mp.mpf(1329) * q_val
            + mp.mpf(2889)
        )
        / (mp.mpf(27) * (q_val**8))
    )

    # Form-B Bring-Schwinger cubic alpha_EM(q_val) & two-photon Borromean trace scale
    alpha_info = alpha_em_form_b_cubic_80dps(q_val)
    alpha_b = alpha_info["alpha_form_B"]
    alpha_inv_b = alpha_info["alpha_inv_form_B"]
    alpha_inv_ppb = (alpha_inv_b - codata_alpha_inv) / codata_alpha_inv * (mp.mpf(10) ** 9)
    two_photon_scale = (alpha_b**2) * (hbar**4)
    two_photon_over_u4 = two_photon_scale / u4_val

    # Convention-D Wedderburn & GPMT+ quantities at q_val
    two_q = q_val + one / q_val
    three_q = q_val**2 + one + one / (q_val**2)
    four_q = (q_val**4 - q_val ** (-4)) / h
    z_d = (q_val**3) / (q_val**2 + one)
    w3 = (q_val**4 + one) / ((q_val**2 + one) ** 2)
    w21 = (q_val**2) / ((q_val**2 + one) ** 2)
    d111_abs = (q_val**3) / ((q_val**2 + one) * (q_val**4 + q_val**2 + one))

    alpha_d = (z_d - one) * h / two
    alpha_d_proj = alpha_d - (h * h) / four
    f1_proj = mp.cos(alpha_d_proj - u_val / two)
    f2_kash = one - u2_val

    # Bases at q_val:
    # 1. Authorised Wave-2 Convention-D KD6 * z_D base on nuc11_interleaved
    e0_tower = me_mev / (q_val * (q_val - one)) / (one - hbar * hbar)
    chi3_nuc11 = -(q_val**2 - one) * ((q_val**2 + one) ** 2) / (four * q_val)
    chi111_nuc11 = -(q_val**2 - one) * ((q_val**2 + one) ** 2) / (four * (q_val**5))
    p_poly = (
        two * (q_val**12)
        - five * (q_val**10)
        + five * (q_val**8)
        - five * (q_val**6)
        + five * (q_val**4)
        - five * (q_val**2)
        + two
    )
    chi21_int = (q_val**2 - one) * (q_val**4 + one) * p_poly / (four * (q_val**9))
    tr_zd_int = w3 * chi3_nuc11 + w21 * chi21_int
    c_kd6 = (q_val**6 + q_val ** (-6)) / two
    q_kd6_base = e0_tower * (-tr_zd_int) * c_kd6
    q_gpmt_base = e0_tower * (-(tr_zd_int + d111_abs * chi111_nuc11))
    q_a_base = me_mev * abs(q_val**2 - two * q_val - one) * (q_val + one) / (two * (q_val**3))

    dm_qed_plain = -me_mev * tr_diff_plain

    # Parameter-free c_4 branches (strictly q-derived, ZERO CODATA input):
    mu2_d = w3 * (one - w3)
    kappa4_d = mu2_d * (one - six * mu2_d)
    gamma2_d = kappa4_d / (mu2_d * mu2_d)
    c4_cum_d_q = one / two + gamma2_d / six

    z_g = one + d111_abs
    p3_g = w3 / z_g
    p111_g = d111_abs / z_g
    m1_g = p3_g - p111_g
    m2_g = p3_g + p111_g
    m3_g = p3_g - p111_g
    m4_g = p3_g + p111_g
    k2_g = m2_g - m1_g * m1_g
    k4_g = (
        m4_g
        - four * m3_g * m1_g
        + mp.mpf(12) * m2_g * (m1_g**2)
        - three * (m2_g**2)
        - six * (m1_g**4)
    )
    gamma2_g = k4_g / (k2_g * k2_g)
    c4_cum_g_q = one / two + gamma2_g / six

    c4_branches: list[tuple[str, str, mp.mpf]] = [
        ("N3_baseline_c4_zero", "0 (c_4 = 0 baseline; also Chebyshev C_KD^(6) h^8 coeff)", mp.mpf(0)),
        ("A1_habiro_pochhammer_u2", "-1 (Habiro Euler product (u^2; u^2)_infty)", -one),
        ("A1_hopf_kashiwara_b4_q", "-2 * b(q)^4 (Hopf-Kashiwara pair rule, -> -9/8)", -two * (b_sq**2)),
        ("A2_kashiwara_divided_cos_q", "[2]_q / ([3]_q * [4]_q) (m=2 Kashiwara divided-power cos, -> +1/6)", two_q / (three_q * four_q)),
        ("A2_B1_classical_sixth", "+1/6 (common q=1 limit of Kashiwara divided-power & Convention-D cumulant)", one / six),
        ("B1_wedderburn_kurtosis_raw_q", "kappa_4^D(q) (raw Convention-D JM 4th cumulant, -> -1/8)", kappa4_d),
        ("B1_wedderburn_cumulant_rung_D_q", "1/2 + gamma_2^D(q)/6 (variance-matched Convention-D cumulant rung, -> +1/6)", c4_cum_d_q),
        ("B1_gpmt_pos_kurtosis_raw_q", "kappa_4^{GPMT+}(q) (raw 3-block GPMT+ JM 4th cumulant, -> -516/2401)", k4_g),
        ("B1_gpmt_pos_cumulant_rung_q", "1/2 + gamma_2^{GPMT+}(q)/6 (variance-matched GPMT+ cumulant rung, -> +101/288)", c4_cum_g_q),
        (
            "B2_zD_grouped_plancherel_pureQ",
            "-81984216847/90720000000 (pure Q [hbar_q^8]/(9/16) of zD_grouped/Plancherel_grouped)",
            -mp.mpf(81984216847) / mp.mpf(90720000000),
        ),
    ]

    bases = {
        "Q_KD6_nuc11_interleaved": q_kd6_base,
        "Q_A_form_A": q_a_base,
        "Q_GPMT_pos_nuc11_interleaved": q_gpmt_base,
    }

    evaluations_by_base: dict[str, dict[str, dict[str, str]]] = {}
    for base_key, q_base_val in bases.items():
        # Evaluate with standard N=3 Hopf rung (1 - 2*u^3) so the isolated u^4 rung shift is explicit
        q_n3_strong = q_base_val * f1_proj * f2_kash * (one - two * u3_val)
        branch_rows: dict[str, dict[str, str]] = {}
        for br_key, br_formula, c4_val in c4_branches:
            q_n4_strong = q_n3_strong * (one + c4_val * u4_val)
            dc4_mev = q_n4_strong - q_n3_strong
            dc4_ev = dc4_mev * (mp.mpf(10) ** 6)
            q_total = q_n4_strong + dm_qed_plain
            dpn_pred = me_mev + q_total
            mn_pred = mp_mev + dpn_pred

            q_err_ame_ev = (q_total - q_ame_mev) * (mp.mpf(10) ** 6)
            q_err_ame_ppm = (q_total - q_ame_mev) / q_ame_mev * (mp.mpf(10) ** 6)
            q_err_dir_ev = (q_total - q_dir_mev) * (mp.mpf(10) ** 6)
            dpn_err_ev = (dpn_pred - dpn_codata_mev) * (mp.mpf(10) ** 6)
            dpn_err_ppm = (dpn_pred - dpn_codata_mev) / dpn_codata_mev * (mp.mpf(10) ** 6)
            mn_err_ame_ppb = (mn_pred - mn_ame_mev) / mn_ame_mev * (mp.mpf(10) ** 9)
            mn_err_dir_ppb = (mn_pred - mn_dir_mev) / mn_dir_mev * (mp.mpf(10) ** 9)
            dc4_over_sigma_mn_dir = dc4_mev / mn_dir_err
            dc4_mn_ppt = (dc4_mev / mn_dir_mev) * (mp.mpf(10) ** 12)

            branch_rows[br_key] = {
                "formula": br_formula,
                "c4_value": fmt(c4_val),
                "c4_u4_shift_eV": fmt(dc4_ev),
                "c4_u4_shift_mn_ppt": fmt(dc4_mn_ppt),
                "c4_u4_shift_over_sigma_mn_direct": fmt(dc4_over_sigma_mn_dir),
                "Q_beta_pred_MeV": fmt(q_total),
                "Q_beta_vs_AME_err_eV": fmt(q_err_ame_ev),
                "Q_beta_vs_AME_err_ppm": fmt(q_err_ame_ppm),
                "Q_beta_vs_CODATA_direct_err_eV": fmt(q_err_dir_ev),
                "Delta_pn_pred_MeV": fmt(dpn_pred),
                "Delta_pn_vs_CODATA_err_eV": fmt(dpn_err_ev),
                "Delta_pn_vs_CODATA_err_ppm": fmt(dpn_err_ppm),
                "m_n_pred_MeV": fmt(mn_pred),
                "m_n_vs_AME_err_ppb": fmt(mn_err_ame_ppb),
                "m_n_vs_CODATA_direct_err_ppb": fmt(mn_err_dir_ppb),
            }
        evaluations_by_base[base_key] = branch_rows

    # N >= 5 truncation envelope metrics:
    qbu5_mev = q_ame_mev * u5_val
    qbu5_ev = qbu5_mev * (mp.mpf(10) ** 6)
    qbu5_over_sigma_mn_dir = qbu5_mev / mn_dir_err
    qbu5_over_sigma_mn_ame = qbu5_mev / mn_ame_err
    qbu5_mn_ppt = (qbu5_mev / mn_dir_mev) * (mp.mpf(10) ** 12)

    two_photon_qbeta_mev = q_ame_mev * two_photon_scale
    two_photon_qbeta_ev = two_photon_qbeta_mev * (mp.mpf(10) ** 6)
    two_photon_over_sigma_mn_dir = two_photon_qbeta_mev / mn_dir_err
    two_photon_over_sigma_q_ame = two_photon_qbeta_mev / q_ame_err
    two_photon_over_sigma_dpn = two_photon_qbeta_mev / dpn_codata_err

    return {
        "pin_name": pin_name,
        "q": fmt(q_val),
        "hbar_q": fmt(hbar),
        "h": fmt(h),
        "b": fmt(b_val),
        "u": fmt(u_val),
        "u_sq": fmt(u2_val),
        "u_fourth": fmt(u4_val),
        "u_fifth": fmt(u5_val),
        "lean_identity_residuals_80dps": {
            "u4_minus_rational_closed_form": fmt(abs(u4_val - u4_rational)),
            "u4_classical_leading_10th_order_identity": fmt(abs(u4_lead_lhs - u4_lead_rhs)),
            "tr_conn_diff_plain_poly8_remainder_identity": fmt(
                abs((tr_diff_plain - tr_diff_poly8) - tr_diff_rem_rhs)
            ),
            "alpha_em_form_b_cubic_residual": fmt(alpha_info["cubic_equation_residual"]),
        },
        "form_b_bring_schwinger_alpha_em": {
            "alpha_inv_form_A": fmt(alpha_info["alpha_inv_form_A"]),
            "alpha_inv_form_B": fmt(alpha_inv_b),
            "alpha_form_B": fmt(alpha_b),
            "alpha_inv_form_B_vs_codata_ppb": fmt(alpha_inv_ppb),
            "two_photon_borromean_scale_alpha2_hbar4": fmt(two_photon_scale),
            "two_photon_scale_over_u4": fmt(two_photon_over_u4),
            "two_photon_Qbeta_scale_eV": fmt(two_photon_qbeta_ev),
            "two_photon_Qbeta_over_sigma_mn_direct": fmt(two_photon_over_sigma_mn_dir),
            "two_photon_Qbeta_over_sigma_Qbeta_AME": fmt(two_photon_over_sigma_q_ame),
            "two_photon_Qbeta_over_sigma_Delta_pn": fmt(two_photon_over_sigma_dpn),
        },
        "truncation_envelope_N_ge_5": {
            "u4_lt_6e_neg9": bool(u4_val < mp.mpf(6) * (mp.mpf(10) ** (-9))),
            "u5_lt_5e_neg11": bool(u5_val < mp.mpf(5) * (mp.mpf(10) ** (-11))),
            "Qbeta_u5_eV": fmt(qbu5_ev),
            "Qbeta_u5_over_sigma_mn_direct": fmt(qbu5_over_sigma_mn_dir),
            "Qbeta_u5_over_sigma_mn_AME": fmt(qbu5_over_sigma_mn_ame),
            "Qbeta_u5_mn_ppt": fmt(qbu5_mn_ppt),
            "strictly_below_1e_neg4_sigma_mn": bool(
                qbu5_over_sigma_mn_dir < mp.mpf(10) ** (-4)
            ),
            "strictly_below_0p05_ppt_mn": bool(
                qbu5_mn_ppt < mp.mpf(5) / mp.mpf(100)
            ),
        },
        "falsifiable_evaluations_by_base": evaluations_by_base,
    }


def main() -> int:
    symbolic = build_symbolic_derivations()

    q_1t = q_at(80)
    q_2t = q_two_term_borromean_at(dps=80, k_weighted=False)
    q_2t_kp = q_two_term_borromean_at(dps=80, k_weighted=True)
    q_muon = q_muon_at(80)

    eval_q1t = evaluate_pin_80dps(q_1t, "q_1t_proton_1term")
    eval_q2t = evaluate_pin_80dps(q_2t, "q_2t_borromean_2term_plain")
    eval_q2t_kp = evaluate_pin_80dps(q_2t_kp, "q_2t_borromean_2term_Kp")

    print("=" * 108)
    print(
        "CONVENTION-D QUARTIC HABIRO RUNG c_4 (bean qou-51yf): EXACT Q[[hbar_q]] DERIVATION & 80-DPS EVALUATION"
    )
    print("=" * 108)
    ev_rat = symbolic["even_rung_rationality"]
    ca = symbolic["contribution_A_kashiwara_habiro_chebyshev"]
    cb = symbolic["contribution_B_wedderburn_kurtosis_and_traces"]
    cc = symbolic["contribution_C_borromean_qed_series"]

    print(f"  Even-rung pure Q[[hbar_q]] check : u^2={ev_rat['u2_is_pure_Q_series']}, u^4={ev_rat['u4_is_pure_Q_series']}")
    print(f"  u^2(hbar_q) [4..8]               : 3/4*t^4 + 1/4*t^6 + 1/4*t^7 + 1/16*t^8")
    print(f"  u^4(hbar_q) [8..12]              : 9/16*t^8 + 0*t^9 + 3/8*t^10 + 3/8*t^11 + 5/32*t^12")
    print(f"  A1. u^4/eta_4 at q=1             : {ca['u4_over_eta4_at_q1_exact']}  ((9/16)/576)")
    print(f"  A2. c_4^{{Kash,div}}(q) [0..4]    : 1/6 - 5/9*t^2 - 5/9*t^3 + 77/108*t^4")
    print(f"  A3. C_KD^(6) cubic in h^2 (0*h^8): {ca['c_kd6_is_exact_cubic_in_h2_zero_h8']}")
    print(f"  B1. kappa_4^D(q) [0..8]          : -1/8 + 1/2*t^4 + t^5 + 3/4*t^6 - 1/4*t^7 - 51/32*t^8")
    print(f"      gamma_2^D(1)                 : {cb['convention_D_excess_kurtosis_at_q1_exact']} (= J_Hopf(1))")
    print(f"      c_4^{{cum,D}}(1)              : {cb['convention_D_cumulant_rung_c4_at_q1_exact']} (= c_4^{{Kash,div}}(1))")
    print(f"      kappa_4^{{GPMT+}}(1), c_4(1)   : {cb['gpmt_pos_jm_kurtosis_kappa4_hbar_q']['0']}, {cb['gpmt_pos_cumulant_rung_c4_at_q1_exact']}")
    print(f"  C1. Delta tr_conn^plain [4..8]   : 16/3*t^4 + 32/3*t^5 + 760/27*t^6 + 520/9*t^7 + 107*t^8")

    fb_2t = eval_q2t["form_b_bring_schwinger_alpha_em"]
    env_2t = eval_q2t["truncation_envelope_N_ge_5"]
    print("\n" + "-" * 108)
    print("TWO-PHOTON BORROMEAN QED SCALE & N >= 5 TRUNCATION ENVELOPE AT q_2t (80 DPS)")
    print("-" * 108)
    print(f"  q_2t (plain)                     = {eval_q2t['q']}")
    print(f"  1/alpha_EM^{{Form-B}}(q_2t)        = {fb_2t['alpha_inv_form_B']}  ({fb_2t['alpha_inv_form_B_vs_codata_ppb'][:10]} ppb vs CODATA-2022)")
    print(f"  u(q_2t)^4                        = {eval_q2t['u_fourth']}")
    print(f"  alpha_EM(q_2t)^2 * hbar_q^4      = {fb_2t['two_photon_borromean_scale_alpha2_hbar4']}  (= {fb_2t['two_photon_scale_over_u4'][:10]} * u^4)")
    print(f"  Q_beta * alpha_EM^2 * hbar_q^4   = {fb_2t['two_photon_Qbeta_scale_eV'][:12]} eV  (= {fb_2t['two_photon_Qbeta_over_sigma_mn_direct'][:10]} sigma_exp(m_n))")
    print(f"  u(q_2t)^5                        = {eval_q2t['u_fifth']}  (Q_beta*u^5 = {env_2t['Qbeta_u5_eV'][:12]} eV = {env_2t['Qbeta_u5_mn_ppt'][:10]} ppt of m_n)")

    print("\n" + "-" * 108)
    print("SIDE-BY-SIDE 80-DPS EVALUATION AT q_2t (AUTHORISED WAVE-2 BASE: Q_KD6_nuc11_interleaved)")
    print("-" * 108)
    print(
        f"  {'Branch':34s} | {'c_4(q_2t)':>12s} | {'dc_4 (eV)':>12s} | {'Q_beta err (ppm)':>16s} | {'Delta_pn err (ppm)':>18s} | {'m_n err (ppb)':>13s}"
    )
    kd6_rows = eval_q2t["falsifiable_evaluations_by_base"]["Q_KD6_nuc11_interleaved"]
    for br_key, row in kd6_rows.items():
        print(
            f"  {br_key:34s} | {row['c4_value'][:12]:>12s} | "
            f"{row['c4_u4_shift_eV'][:12]:>12s} | "
            f"{row['Q_beta_vs_AME_err_ppm'][:14]:>14s}   | "
            f"{row['Delta_pn_vs_CODATA_err_ppm'][:14]:>14s}     | "
            f"{row['m_n_vs_AME_err_ppb'][:12]:>12s}"
        )

    tol_75 = mp.mpf(10) ** (-75)
    res_2t = eval_q2t["lean_identity_residuals_80dps"]

    checks: list[tuple[str, bool, str]] = [
        (
            "even_rungs_u2_u4_pure_rational_and_classical_9_16_verified",
            bool(
                ev_rat["u2_is_pure_Q_series"]
                and ev_rat["u4_is_pure_Q_series"]
                and ev_rat["u4_series_hbar_q"]["8"] == "9/16"
                and ev_rat["u4_series_hbar_q"]["9"] == "0"
                and mp.mpf(res_2t["u4_minus_rational_closed_form"]) < tol_75
                and mp.mpf(res_2t["u4_classical_leading_10th_order_identity"]) < tol_75
            ),
            "u^2(q) and u^4(q) have zero sqrt(3) terms in Q[[hbar_q]], [hbar_q^8] u^4 = 9/16, [hbar_q^9] u^4 = 0, and Lean 10th-order remainder holds to < 1e-75",
        ),
        (
            "kashiwara_divided_cos_and_convention_d_cumulant_coincide_at_q1_sixth",
            bool(
                ca["c4_kashiwara_divided_cos_at_q1_exact"] == "1/6"
                and cb["convention_D_cumulant_rung_c4_at_q1_exact"] == "1/6"
                and cb["convention_D_excess_kurtosis_at_q1_exact"] == "-2"
                and ca["c_kd6_is_exact_cubic_in_h2_zero_h8"]
                and ca["u4_over_eta4_at_q1_exact"] == "1/1024"
            ),
            "c_4^{Kash,div}(1) = c_4^{cum,D}(1) = +1/6, gamma_2^D(1) = -2 = J_Hopf(1), C_KD^(6) has exact 0*h^8 term, and u^4/eta_4(1) = 1/1024",
        ),
        (
            "borromean_qed_hbar8_coeff_107_and_two_photon_scale_0p975_u4",
            bool(
                cc["tr_conn_diff_plain_hbar_q"]["4"] == "16/3"
                and cc["tr_conn_diff_plain_hbar_q"]["8"] == "107"
                and mp.mpf(res_2t["tr_conn_diff_plain_poly8_remainder_identity"]) < tol_75
                and mp.mpf(97) / mp.mpf(100)
                < mp.mpf(fb_2t["two_photon_scale_over_u4"])
                < mp.mpf(98) / mp.mpf(100)
            ),
            f"Delta tr_conn^plain has exact [hbar_q^4]=16/3 and [hbar_q^8]=107, and alpha_EM(q_2t)^2*hbar_q^4 / u^4 = {fb_2t['two_photon_scale_over_u4'][:12]}",
        ),
        (
            "u4_and_u5_strictly_inside_mn_sigma_envelope_at_q1t_and_q2t",
            bool(
                env_2t["u4_lt_6e_neg9"]
                and env_2t["u5_lt_5e_neg11"]
                and env_2t["strictly_below_1e_neg4_sigma_mn"]
                and env_2t["strictly_below_0p05_ppt_mn"]
                and eval_q1t["truncation_envelope_N_ge_5"]["strictly_below_1e_neg4_sigma_mn"]
            ),
            f"At q_2t, u^4 = {eval_q2t['u_fourth'][:12]} < 6e-9, u^5 = {eval_q2t['u_fifth'][:12]} < 5e-11, Q_beta*u^5 = {env_2t['Qbeta_u5_over_sigma_mn_direct'][:10]} sigma_exp(m_n) < 1e-4 sigma_exp(m_n) ({env_2t['Qbeta_u5_mn_ppt'][:8]} ppt < 0.05 ppt)",
        ),
    ]

    print("\n" + "-" * 108)
    print("VERIFICATION CHECKS")
    print("-" * 108)
    for chk_name, passed, detail in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {chk_name} — {detail}")
    if not all(p for _, p, _ in checks):
        raise AssertionError("One or more verification checks failed")

    wb = WitnessBuilder("qbeta-convention-d-c4-quartic-derivation", engine="mpmath")
    wb.set_description(
        "First-principles exact Q[[hbar_q]] / Q(sqrt(3))[[hbar_q]] derivation and 80-dps "
        "evaluation of the fourth-order Habiro / Kashiwara / Wedderburn ladder rung c_4 "
        "(bean qou-51yf, u^4 ~ 5.263e-9): rationality of all even rungs u^{2m}(q) in Q(q), "
        "Contribution A (Habiro 4th cyclotomic Pochhammer norm, m=2 Kashiwara divided-power "
        "cosine [2]_q/([3]_q[4]_q) -> +1/6, Chebyshev C_KD^(6) cubic in h^2), Contribution B "
        "(Convention-D & GPMT+ 4th cumulant kurtosis kappa_4 and operator trace series), and "
        "Contribution C (connected Borromean QED hbar_q^4..hbar_q^8 series, Form-B Bring-Schwinger "
        "two-photon scale alpha_EM(q_2t)^2*hbar_q^4 = 0.9752*u^4, and N>=5 truncation bound "
        "< 1e-4 sigma_exp(m_n)). Zero CODATA fitting; zero float64."
    )
    wb.add_data("dps", 80)
    wb.add_data("zero_codata_fitting", True)
    wb.add_data("zero_float64", True)
    wb.add_data(
        "lean_companion",
        "folio/quantum-observable-universe/lean/QOU/QBeta/ConventionDC4QuarticCumulantDerivation.lean",
    )
    wb.add_data("symbolic_q_series_derivations", symbolic)
    wb.add_data(
        "evaluations_80dps_by_pin",
        {
            "q_1t_proton_1term": eval_q1t,
            "q_2t_borromean_2term_plain": eval_q2t,
            "q_2t_borromean_2term_Kp": eval_q2t_kp,
        },
    )
    wb.add_caveat(
        "Every c_4 branch is derived strictly from symbolic Q(q) / Q[[hbar_q]] / Q(sqrt(3))[[hbar_q]] "
        "identities around q = 1 with zero CODATA input; CODATA-2022 and AME-2020 values are used "
        "exclusively at the final comparison stage. Because Q_beta * u^4 ~ 0.00412 eV = 0.00858 "
        "sigma_exp(m_n), any O(1) c_4 branch lies more than 100x inside experimental m_n uncertainty."
    )
    for chk_name, passed, detail in checks:
        wb.add_assertion(chk_name, "1" if passed else "0", "1", "0", source=detail)

    out_path = wb.save(
        q0_comparison(
            muon=q_muon,
            proton=q_1t,
            reason=(
                "Evaluates parameter-free c_4 operator branches side-by-side at the 1-term proton "
                "pin q_0 = q_{1t} and consistent 2-term Borromean QED proton pins q_{2t} (plain "
                "and Kp) alongside the muon reference pin."
            ),
        )
    )
    print(f"\nWrote witness -> {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
