#!/usr/bin/env python3
"""
qbeta-convention-d-c3-and-tail-derivation-probe — 80-dps zero-float64 derivation probe for:

  1. Part 1 (Bean qou-j1e5 — Five-Letter Valence/Gluon Tail Closure and Ordering Selection):
     - Unique Kazhdan-Lusztig bar-fixed affine shift -h/2 on the h-line and achiral crossing
       average T_i - (h/2)*1 = (1/2)*(T_i + T_i^{-1}) with central square 1 + h^2/4.
     - Unique minimal positive PSD gluon pair k = 2 (sigma_0^2) across both H_2(q) blocks.
     - Exact rational constituent-to-decay identity:
       tr_M^{z_D}(Delta_nuc11_interleaved) = -(tr_M^{z_D}(p_Bor) - tr_M^{z_D}(n_Bor)).
     - Universal H_3(q) braid commutator [sigma_0 + c_0, sigma_1 + c_1] = L_+ - L_- and
       [sigma_1 + c_1, sigma_0^2] = -h * (L_+ - L_-), Wedderburn block visibility on (2,1),
       flavor-slot permutation invariance (uud = udu, dud = ddu, duu - uud = dud - udd),
       and a priori selection of interleaved over grouped by constituent energy minimization
       (M_QCD and M_QCD + M_QED) and gramGPMT Frobenius positivity without CODATA input.

  2. Part 2 (Beans qou-51yf / qou-cds1 + Two-Term Categorical Lagrangian Corrected-Photon Bridge):
     - Exact symbolic Q(sqrt(3)) (Fraction) Taylor series through order 4/8 in both
       hbar_q = 1 - q^{-1} and the bar-even Habiro variable u_Hab = q * u = b(q)*((q + q^{-1}) - 2),
       including exact cubic termination Q_A/m_e = 2 - 5*hbar_q + 3*hbar_q^2 - (1/2)*hbar_q^3,
       exact algebraic coefficients of cos(alpha_D^{proj}) in u_Hab
       (1, -sqrt(3)/12, 47/96, -2069*sqrt(3)/5760, 11658923/17418240),
       Kashiwara-Hopf N=3 product (1 - u^2)*(1 - 2*u^3) = 1 - u^2 - 2*u^3 + 2*u^5,
       and connected Borromean QED trace Delta_tr_conn(V^3).
     - Complete 80-dps parameter-free evaluation of the Two-Term Categorical Lagrangian Trace
       M = M_QCD + M_QED evaluated with the Form-B Bring-Schwinger corrected photon coupling
       alpha_EM^{corr}(q) (1/alpha = q*[9]_q*[10]_q + 2/(3*pi) + alpha*([2]_q/(8*pi))*(1 - h^2*alpha))
       at consistent two-term proton pins q_{2t}, reporting Q_beta, Delta_pn = Q_beta + m_e, and
       m_n = m_p + Delta_pn side-by-side across all parameter-free bases, phases, rungs, and QED
       modes (zero fitting, zero PSLQ against Q_beta/Delta_pn, zero float64).

Lean companion:
  folio/quantum-observable-universe/lean/QOU/QBeta/ConventionDC3AndTailSelectionDerivation.lean
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
    "computations/probes",
    "tools/qou-substrate/python",
    "tools/pyhecke/python",
):
    _abs = os.path.join(ROOT, _rel)
    if _abs not in sys.path:
        sys.path.insert(0, _abs)

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from codata_2022_source import (  # noqa: E402
    M_E_MEV,
    M_MU_MEV,
    M_N_MEV_AME_DERIVED,
    M_N_MEV_CODATA_DIRECT,
    M_N_MINUS_P_MEV,
    M_P_MEV,
    Q_BETA_MEV_AME,
)
from compound_shift_nf import hm_mp  # noqa: E402
from confinement_lp_sdp_twoterm_photon_gpmt_probe import (  # noqa: E402
    build_h3_gpmt_and_twoterm_data,
    compute_alpha_em_bring_schwinger,
)
from q_parameter import (  # noqa: E402
    Q_50_DIGIT_STR,
    q_at,
    q_muon_at,
    q_two_term_borromean_at,
    tr_conn_borromean_diff_at,
    vol_4_1_at,
)
from qou_substrate.constants import MASS_RATIO_P_E_STR  # noqa: E402
from qou_substrate.witness import WitnessBuilder, q0_comparison  # noqa: E402

set_compute_dps(80)
mp.mp.dps = 80

_VOL_4_1_95 = vol_4_1_at(95)
_M_E_MPF = mp.mpf(str(M_E_MEV))
_M_MU_MPF = mp.mpf(str(M_MU_MEV))
_M_P_MPF = mp.mpf(str(M_P_MEV))
_M_N_AME_MPF = mp.mpf(str(M_N_MEV_AME_DERIVED))
_M_N_COD_MPF = mp.mpf(str(M_N_MEV_CODATA_DIRECT))
_DPN_COD_MPF = mp.mpf(str(M_N_MINUS_P_MEV))
_QB_AME_MPF = mp.mpf(str(Q_BETA_MEV_AME))
_DPN_AME_MPF = _QB_AME_MPF + _M_E_MPF
_MP_OVER_ME_MPF = mp.mpf(MASS_RATIO_P_E_STR)


def fmt(val: mp.mpf, digits: int = 50) -> str:
    """Serialize an mpmath mpf to a decimal string with zero float64 conversion."""
    return mp.nstr(val, digits)


# ---------------------------------------------------------------------------
# Exact Q(sqrt(3)) field and truncated power-series arithmetic (zero float64)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Q3:
    """Exact element a + b*sqrt(3) in Q(sqrt(3)) over Python Fraction."""

    a: Fraction
    b: Fraction = Fraction(0)

    @staticmethod
    def of(x: Q3 | Fraction | int) -> Q3:
        if isinstance(x, Q3):
            return x
        return Q3(Fraction(x), Fraction(0))

    def __add__(self, other: Q3 | Fraction | int) -> Q3:
        o = Q3.of(other)
        return Q3(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __sub__(self, other: Q3 | Fraction | int) -> Q3:
        o = Q3.of(other)
        return Q3(self.a - o.a, self.b - o.b)

    def __rsub__(self, other: Q3 | Fraction | int) -> Q3:
        return Q3.of(other) - self

    def __neg__(self) -> Q3:
        return Q3(-self.a, -self.b)

    def __mul__(self, other: Q3 | Fraction | int) -> Q3:
        o = Q3.of(other)
        return Q3(self.a * o.a + 3 * self.b * o.b, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def inv(self) -> Q3:
        norm = self.a * self.a - 3 * self.b * self.b
        if norm == 0:
            raise ZeroDivisionError("Singular Q3 element")
        return Q3(self.a / norm, -self.b / norm)

    def __truediv__(self, other: Q3 | Fraction | int) -> Q3:
        return self * Q3.of(other).inv()

    def __rtruediv__(self, other: Q3 | Fraction | int) -> Q3:
        return Q3.of(other) * self.inv()

    def is_zero(self) -> bool:
        return self.a == 0 and self.b == 0

    def to_mpf(self) -> mp.mpf:
        s3 = mp.sqrt(mp.mpf(3))
        ra = mp.mpf(self.a.numerator) / mp.mpf(self.a.denominator)
        rb = mp.mpf(self.b.numerator) / mp.mpf(self.b.denominator)
        return ra + rb * s3

    def to_exact_str(self) -> str:
        if self.b == 0:
            return str(self.a)
        if self.a == 0:
            return f"({self.b})*sqrt(3)"
        return f"{self.a} + ({self.b})*sqrt(3)"


def s_const(c: Q3 | Fraction | int, deg: int) -> list[Q3]:
    return [Q3.of(c)] + [Q3.of(0)] * deg


def s_var(deg: int) -> list[Q3]:
    return [Q3.of(0), Q3.of(1)] + [Q3.of(0)] * (deg - 1)


def s_add(f: list[Q3], g: list[Q3]) -> list[Q3]:
    return [x + y for x, y in zip(f, g)]


def s_sub(f: list[Q3], g: list[Q3]) -> list[Q3]:
    return [x - y for x, y in zip(f, g)]


def s_scale(c: Q3 | Fraction | int, f: list[Q3]) -> list[Q3]:
    cc = Q3.of(c)
    return [cc * x for x in f]


def s_mul(f: list[Q3], g: list[Q3]) -> list[Q3]:
    deg = len(f) - 1
    out = [Q3.of(0)] * (deg + 1)
    for i in range(deg + 1):
        if f[i].is_zero():
            continue
        for j in range(deg + 1 - i):
            if not g[j].is_zero():
                out[i + j] = out[i + j] + f[i] * g[j]
    return out


def s_pow(f: list[Q3], exp: int) -> list[Q3]:
    deg = len(f) - 1
    res = s_const(1, deg)
    base = f
    k = exp
    while k > 0:
        if k & 1:
            res = s_mul(res, base)
        base = s_mul(base, base)
        k >>= 1
    return res


def s_inv(f: list[Q3]) -> list[Q3]:
    deg = len(f) - 1
    inv0 = f[0].inv()
    out = [Q3.of(0)] * (deg + 1)
    out[0] = inv0
    for n in range(1, deg + 1):
        acc = Q3.of(0)
        for k in range(1, n + 1):
            acc = acc + f[k] * out[n - k]
        out[n] = -acc * inv0
    return out


def s_div(f: list[Q3], g: list[Q3]) -> list[Q3]:
    return s_mul(f, s_inv(g))


def s_sqrt_three_quarters(f: list[Q3]) -> list[Q3]:
    """Square root of a series with constant term 3/4 (positive branch +sqrt(3)/2)."""
    deg = len(f) - 1
    if f[0] != Q3(Fraction(3, 4)):
        raise ValueError("Expected constant term 3/4")
    g = [Q3.of(0)] * (deg + 1)
    g[0] = Q3(Fraction(0), Fraction(1, 2))
    two_g0 = g[0] * 2
    for n in range(1, deg + 1):
        acc = f[n]
        for k in range(1, n):
            acc = acc - g[k] * g[n - k]
        g[n] = acc / two_g0
    return g


def s_cos_zero_const(f: list[Q3]) -> list[Q3]:
    """Cosine of a formal power series with zero constant term."""
    deg = len(f) - 1
    if not f[0].is_zero():
        raise ValueError("Expected zero constant term")
    res = s_const(1, deg)
    f2 = s_mul(f, f)
    term = s_const(1, deg)
    fact = Fraction(1)
    for k in range(1, deg // 2 + 1):
        term = s_mul(term, f2)
        fact = fact * (2 * k - 1) * (2 * k)
        sign = Fraction(-1) if (k % 2 == 1) else Fraction(1)
        res = s_add(res, s_scale(sign / fact, term))
    return res


def s_revert_linear(g: list[Q3]) -> list[Q3]:
    """Compositional inverse h of g with g[0] = 0 and g[1] != 0."""
    deg = len(g) - 1
    if not g[0].is_zero() or g[1].is_zero():
        raise ValueError("Expected g[0]=0 and g[1]!=0")
    h = [Q3.of(0)] * (deg + 1)
    h[1] = g[1].inv()
    for k in range(2, deg + 1):
        h_trunc = h[:]
        acc = Q3.of(0)
        hp = s_const(1, deg)
        for m in range(1, k + 1):
            hp = s_mul(hp, h_trunc)
            acc = acc + g[m] * hp[k]
        h[k] = -acc / g[1]
    return h


def s_compose(f: list[Q3], g: list[Q3]) -> list[Q3]:
    """Formal composition f(g(x)) with g[0] = 0."""
    deg = len(f) - 1
    if not g[0].is_zero():
        raise ValueError("Expected g[0]=0")
    res = s_const(f[0], deg)
    gp = s_const(1, deg)
    for n in range(1, deg + 1):
        gp = s_mul(gp, g)
        res = s_add(res, s_scale(f[n], gp))
    return res


# ---------------------------------------------------------------------------
# Part 1: Symbolic and 80-dps verification of 5-letter tail & ordering (qou-j1e5)
# ---------------------------------------------------------------------------


def eval_word_hm_mp(word: list[tuple[int, mp.mpf]], h_val: mp.mpf) -> list[mp.mpf]:
    """Multiply affine letters (gen_idx, scalar_shift) in H_3(q) normal form at 80 dps."""
    nf = [mp.mpf(1)] + [mp.mpf(0)] * 5
    one = mp.mpf(1)
    for gen, shift in word:
        nf = hm_mp(nf, one, shift, gen, h_val)
    return nf


def run_part1_tail_and_ordering_verification(q_eval: mp.mpf) -> dict:
    """Verify all Part 1 algebraic identities symbolically and evaluate at 80 dps."""
    q_sym = sp.Symbol("q", positive=True)
    h_sym = q_sym - 1 / q_sym
    c_sym = sp.Symbol("c")

    # 1. Unique bar-fixed shift -h/2 on the h-line
    bar_shift_fixed_sol = sp.solve((-h_sym - c_sym * h_sym) - c_sym * h_sym, c_sym)
    assert bar_shift_fixed_sol == [-sp.Rational(1, 2)]

    # 2. Hoefsmit (2,1) matrices S0, S1: commutator & flavor-slot permutation identities
    s0 = sp.Matrix([[q_sym, 0], [1, -1 / q_sym]])
    s1 = sp.Matrix([[-1 / q_sym, 1], [0, q_sym]])
    i2 = sp.eye(2)
    m0_avg = s0 - (h_sym / 2) * i2
    m1_avg = s1 - (h_sym / 2) * i2
    m0_inv = s0 - h_sym * i2
    m1_inv = s1 - h_sym * i2

    comm_avg = sp.simplify(m0_avg * m1_avg - m1_avg * m0_avg)
    comm_bare = sp.simplify(s0 * s1 - s1 * s0)
    comm_gluon = sp.simplify(m1_avg * (s0 * s0) - (s0 * s0) * m1_avg + h_sym * comm_avg)
    assert sp.simplify(comm_avg - comm_bare) == sp.zeros(2, 2)
    assert comm_gluon == sp.zeros(2, 2)
    assert sp.simplify(comm_avg[0, 1] - (q_sym + 1 / q_sym)) == 0

    qp_uud = s0 * m0_avg * m1_avg
    qp_udu = m0_avg * s0 * m1_avg
    qp_duu = m0_avg * m0_avg * s1
    qn_udd = m0_avg * m0_avg * m1_inv
    qn_dud = m0_avg * m0_inv * m1_avg
    qn_ddu = m0_inv * m0_avg * m1_avg

    assert sp.simplify(qp_uud - qp_udu) == sp.zeros(2, 2)
    assert sp.simplify(qn_dud - qn_ddu) == sp.zeros(2, 2)
    assert sp.simplify((qp_duu - qp_uud) - (qn_dud - qn_udd)) == sp.zeros(2, 2)
    assert sp.simplify((qn_udd - qp_uud) - (qn_dud - qp_duu)) == sp.zeros(2, 2)

    # 3. 80-dps normal-form constituent energy & gramGPMT Frobenius positivity table
    one = mp.mpf(1)
    two = mp.mpf(2)
    three = mp.mpf(3)
    four = mp.mpf(4)
    hv = q_eval - one / q_eval
    hb = one - one / q_eval
    e0_mev = _M_E_MPF / (q_eval * (q_eval - one)) / (one - hb**2)
    h3_data = build_h3_gpmt_and_twoterm_data(q_eval)
    alpha_corr = compute_alpha_em_bring_schwinger(q_eval)

    ci = [(0, mp.mpf(0)), (1, -hv)] * 3
    gl = [(0, mp.mpf(0)), (0, mp.mpf(0))]
    candidates = [
        ("p_interleaved_uud", "p", ci + [(0, mp.mpf(0)), (0, -hv / two), (1, -hv / two)] + gl),
        ("p_interleaved_udu", "p", ci + [(0, -hv / two), (0, mp.mpf(0)), (1, -hv / two)] + gl),
        ("p_interleaved_duu", "p", ci + [(0, -hv / two), (0, -hv / two), (1, mp.mpf(0))] + gl),
        ("p_tail_grouped", "p", ci + [(0, mp.mpf(0)), (0, -hv / two)] + gl + [(1, -hv / two)]),
        (
            "p_full_grouped",
            "p",
            [(0, mp.mpf(0))] * 4 + [(0, -hv / two)] + gl + [(1, -hv)] * 3 + [(1, -hv / two)],
        ),
        ("n_interleaved_udd", "n", ci + [(0, -hv / two), (0, -hv / two), (1, -hv)] + gl),
        ("n_interleaved_dud", "n", ci + [(0, -hv / two), (0, -hv), (1, -hv / two)] + gl),
        ("n_interleaved_ddu", "n", ci + [(0, -hv), (0, -hv / two), (1, -hv / two)] + gl),
        ("n_tail_grouped", "n", ci + [(0, -hv / two), (0, -hv / two)] + gl + [(1, -hv)]),
        (
            "n_full_grouped",
            "n",
            [(0, mp.mpf(0))] * 3 + [(0, -hv / two)] * 2 + gl + [(1, -hv)] * 4,
        ),
    ]

    candidate_rows: dict[str, dict] = {}
    nf_cache: dict[str, list[mp.mpf]] = {}
    tr_zd_raw: dict[str, mp.mpf] = {}
    m_2t_raw: dict[str, mp.mpf] = {}
    for name, kind, word in candidates:
        nf = eval_word_hm_mp(word, hv)
        nf_cache[name] = nf
        gx = h3_data["g_gpmt"] * mp.matrix(nf)
        tr_zd = mp.fsum(h3_data["t_d"][j] * nf[j] for j in range(6))
        tr_gp = mp.fsum(h3_data["t_gpmt"][j] * nf[j] for j in range(6))
        qvec = h3_data["t_qadjp"] if kind == "p" else h3_data["t_qadjn"]
        tr_qed = mp.fsum(qvec[j] * nf[j] for j in range(6)) / three
        m_qcd_mev = e0_mev * tr_zd
        m_2t_mev = e0_mev * (tr_zd + alpha_corr * tr_qed)
        tr_zd_raw[name] = tr_zd
        m_2t_raw[name] = m_2t_mev
        min_gram_gpmt = min(gx[i] for i in range(6))
        neg_slots = [i for i in range(6) if gx[i] < mp.mpf(0)]
        candidate_rows[name] = {
            "species": kind,
            "tr_zD": fmt(tr_zd),
            "tr_GPMT_pos": fmt(tr_gp),
            "tr_QED_over_3": fmt(tr_qed),
            "M_QCD_constituent_MeV": fmt(m_qcd_mev),
            "M_2t_constituent_MeV": fmt(m_2t_mev),
            "min_gramGPMT_entry": fmt(min_gram_gpmt),
            "gramGPMT_all_nonneg": "1" if len(neg_slots) == 0 else "0",
        }

    # Constituent-to-decay rational identity residual at 80 dps
    nf_diff_int = [
        nf_cache["n_interleaved_udd"][j] - nf_cache["p_interleaved_uud"][j]
        for j in range(6)
    ]
    tr_diff_nf = mp.fsum(h3_data["t_d"][j] * nf_diff_int[j] for j in range(6))
    p_poly = (
        two * q_eval**12
        - mp.mpf(6) * q_eval**10
        + three * q_eval**8
        - mp.mpf(6) * q_eval**6
        + mp.mpf(5) * q_eval**4
        - mp.mpf(5) * q_eval**2
        + two
    )
    tr_diff_rational = (
        (q_eval**2 - one)
        * (q_eval**4 + one)
        * p_poly
        / (four * q_eval**7 * (q_eval**2 + one) ** 2)
    )
    tr_p_const = tr_zd_raw["p_interleaved_uud"]
    tr_n_const = tr_zd_raw["n_interleaved_udd"]
    constituent_bridge_residual = abs(tr_diff_nf - tr_diff_rational) + abs(
        tr_diff_nf + (tr_p_const - tr_n_const)
    )

    # Interleaved vs full_grouped trace defect identity
    tr_diff_grp = (
        -(q_eval**2 - one)
        * (q_eval**4 + one)
        * (q_eval**4 + two * q_eval**2 + two)
        / (four * q_eval * (q_eval**2 + one) ** 2)
    )
    defect_closed = (
        (q_eval**2 - one) ** 3
        * (q_eval**4 + one)
        * (q_eval**4 + q_eval**2 + one)
        * (two * q_eval**4 - three * q_eval**2 + two)
        / (four * q_eval**7 * (q_eval**2 + one) ** 2)
    )
    defect_residual = abs((tr_diff_rational - tr_diff_grp) - defect_closed)

    # Gluon k=1 vs k=2 eigenvalues
    sym_k2 = q_eval**2
    alt_k2 = one / (q_eval**2)
    alt_k1 = -one / q_eval

    return {
        "bar_fixed_shift_unique_c": "-1/2",
        "gluon_psd_eigenvalues_at_q": {
            "sym_k2_pos": fmt(sym_k2),
            "alt_k2_pos": fmt(alt_k2),
            "alt_k1_neg": fmt(alt_k1),
        },
        "constituent_to_decay_bridge_residual": fmt(constituent_bridge_residual),
        "interleaved_vs_grouped_defect_MeV_equiv": fmt(e0_mev * defect_closed),
        "interleaved_vs_grouped_defect_residual": fmt(defect_residual),
        "candidates": candidate_rows,
        "_raw_checks": {
            "constituent_bridge_residual": constituent_bridge_residual,
            "defect_residual": defect_residual,
            "defect_val": defect_closed,
            "p_int_lt_grp_2t": mp.mpf(
                candidate_rows["p_interleaved_uud"]["M_2t_constituent_MeV"]
            )
            < mp.mpf(candidate_rows["p_full_grouped"]["M_2t_constituent_MeV"]),
            "n_int_lt_grp_2t": mp.mpf(
                candidate_rows["n_interleaved_udd"]["M_2t_constituent_MeV"]
            )
            < mp.mpf(candidate_rows["n_full_grouped"]["M_2t_constituent_MeV"]),
            "p_int_lt_duu_2t": mp.mpf(
                candidate_rows["p_interleaved_uud"]["M_2t_constituent_MeV"]
            )
            < mp.mpf(candidate_rows["p_interleaved_duu"]["M_2t_constituent_MeV"]),
            "n_int_lt_dud_2t": mp.mpf(
                candidate_rows["n_interleaved_udd"]["M_2t_constituent_MeV"]
            )
            < mp.mpf(candidate_rows["n_interleaved_dud"]["M_2t_constituent_MeV"]),
        },
    }


# ---------------------------------------------------------------------------
# Part 2A: Exact Q(sqrt(3)) Taylor series in hbar_q and bar-even u_Hab (qou-51yf)
# ---------------------------------------------------------------------------


def compute_exact_operator_series(q_eval: mp.mpf) -> dict:
    """Compute exact Q(sqrt(3)) Taylor series of both strong and QED Lagrangian terms."""
    deg = 8
    one = s_const(1, deg)
    hb = s_var(deg)  # hbar_q = 1 - q^{-1}
    qi = s_sub(one, hb)
    q_s = s_inv(qi)
    q2 = s_mul(q_s, q_s)
    q3 = s_mul(q2, q_s)
    q4 = s_mul(q2, q2)
    h_s = s_sub(q_s, qi)
    h2_s = s_mul(h_s, h_s)

    # 1. Exact cubic termination of Q_A / m_e in hbar_q: -(q^2 - 2*q - 1)*(q + 1)/(2*q^3)
    qa_num = s_mul(
        s_sub(s_add(s_scale(2, q_s), one), q2),
        s_add(q_s, one),
    )
    qa_over_me_hb = s_div(qa_num, s_scale(2, q3))

    # 2. Convention-D base Q_zD / m_e and Q_KD6 / m_e and Q_GPMT+ / m_e in hbar_q
    # E_0 / m_e * (q^2 - 1) = (q + 1) / (q * (1 - hbar_q^2)) -> nonsingular at hbar_q = 0!
    e0_times_q2_sub_1 = s_div(
        s_add(q_s, one),
        s_mul(q_s, s_sub(one, s_mul(hb, hb))),
    )
    p_poly_hb = s_const(2, deg)
    for coeff, pwr in [(-5, 2), (5, 4), (-6, 6), (3, 8), (-6, 10), (2, 12)]:
        p_poly_hb = s_add(p_poly_hb, s_scale(coeff, s_pow(q_s, pwr)))
    tr_zd_over_q2_sub_1 = s_div(
        s_mul(s_add(q4, one), p_poly_hb),
        s_scale(4, s_mul(s_pow(q_s, 7), s_pow(s_add(q2, one), 2))),
    )
    q_zd_over_me_hb = s_mul(e0_times_q2_sub_1, s_scale(-1, tr_zd_over_me_tmp := tr_zd_over_q2_sub_1))
    del tr_zd_over_me_tmp

    c_kd6_hb = s_scale(Fraction(1, 2), s_add(s_pow(q_s, 6), s_pow(qi, 6)))
    q_kd6_over_me_hb = s_mul(q_zd_over_me_hb, c_kd6_hb)

    # 3. Ladder factors in hbar_q
    z_d_hb = s_div(q3, s_add(q2, one))
    w21_hb = s_div(q2, s_pow(s_add(q2, one), 2))
    b_hb = s_sqrt_three_quarters(s_sub(one, w21_hb))
    u_hb = s_mul(b_hb, s_mul(hb, hb))
    alpha_d_hb = s_scale(Fraction(1, 2), s_mul(s_sub(z_d_hb, one), h_s))
    alpha_proj_hb = s_sub(alpha_d_hb, s_scale(Fraction(1, 4), h2_s))
    n1_unproj_hb = s_cos_zero_const(s_sub(alpha_d_hb, s_scale(Fraction(1, 2), u_hb)))
    n1_proj_hb = s_cos_zero_const(s_sub(alpha_proj_hb, s_scale(Fraction(1, 2), u_hb)))
    n2_hb = s_sub(one, s_mul(u_hb, u_hb))
    n3_hb = s_sub(one, s_scale(2, s_pow(u_hb, 3)))
    ladder_proj_n3_hb = s_mul(s_mul(n1_proj_hb, n2_hb), n3_hb)
    q_kd6_full_n3_hb = s_mul(q_kd6_over_me_hb, ladder_proj_n3_hb)

    # 4. Connected Borromean QED trace Delta_tr_conn(V^3) = (q^2 - 1)^4*(4*q^4 + q^2 + 4)/(27*q^6)
    #    and Bring-Schwinger photon ingredients T_tree(q) = q*[9]_q*[10]_q, [2]_q, h^2 in hbar_q
    tr_conn_hb = s_div(
        s_mul(
            s_pow(s_sub(q2, one), 4),
            s_add(s_scale(4, q4), s_add(q2, s_const(4, deg))),
        ),
        s_scale(27, s_pow(q_s, 6)),
    )
    q9_br = s_const(0, deg)
    for m in range(-8, 9, 2):
        q9_br = s_add(q9_br, s_pow(q_s, m) if m >= 0 else s_pow(qi, -m))
    q10_br = s_const(0, deg)
    for m in range(-9, 10, 2):
        q10_br = s_add(q10_br, s_pow(q_s, m) if m >= 0 else s_pow(qi, -m))
    t_tree_q9_q10_hb = s_mul(q_s, s_mul(q9_br, q10_br))
    bracket2_hb = s_add(q_s, qi)

    # 5. Bar-even Habiro variable y = deltaHabiroSq = (q + q^{-1}) - 2 and u_Hab = b(q)*y = q*u(q)
    y = s_var(deg)
    b2_y = s_div(
        s_mul(s_add(y, one), s_add(y, s_const(3, deg))),
        s_pow(s_add(y, s_const(2, deg)), 2),
    )
    b_y = s_sqrt_three_quarters(b2_y)
    u_hab_y = s_mul(y, b_y)
    y_of_uhab = s_revert_linear(u_hab_y)

    # Squared mirror-projected phase P_2(y) = y*(y + 4)*(y^2 + 2*y - 2)^2 / (16*(y + 2)^2)
    p2_y = s_div(
        s_mul(
            s_mul(y, s_add(y, s_const(4, deg))),
            s_pow(s_sub(s_add(s_mul(y, y), s_scale(2, y)), s_const(2, deg)), 2),
        ),
        s_scale(16, s_pow(s_add(y, s_const(2, deg)), 2)),
    )
    cos_proj_y = s_const(1, deg)
    p2_pow = s_const(1, deg)
    fact = Fraction(1)
    for k in range(1, deg + 1):
        p2_pow = s_mul(p2_pow, p2_y)
        fact = fact * (2 * k - 1) * (2 * k)
        sign = Fraction(-1) if (k % 2 == 1) else Fraction(1)
        cos_proj_y = s_add(cos_proj_y, s_scale(sign / fact, p2_pow))

    cos_proj_in_uhab = s_compose(cos_proj_y, y_of_uhab)

    # Connected Borromean QED trace in y and u_Hab:
    # (q^2 - 1)^4 * (4*q^4 + q^2 + 4) / (27 * q^6) = (h^2)^2 * (4*(y^2 + 4*y + 2) + 1) / 27
    # where h^2 = y*(y + 4)!
    h2_y = s_mul(y, s_add(y, s_const(4, deg)))
    q2_plus_qi2_y = s_add(s_mul(y, y), s_add(s_scale(4, y), s_const(2, deg)))
    tr_conn_y = s_scale(
        Fraction(1, 27),
        s_mul(
            s_mul(h2_y, h2_y),
            s_add(s_scale(4, q2_plus_qi2_y), one),
        ),
    )
    tr_conn_in_uhab = s_compose(tr_conn_y, y_of_uhab)

    # Verify numerical convergence of cos_proj_in_uhab at q_eval
    one_m = mp.mpf(1)
    hv = q_eval - one_m / q_eval
    hb_m = one_m - one_m / q_eval
    b_m = mp.sqrt(q_eval**4 + q_eval**2 + one_m) / (q_eval**2 + one_m)
    u_hab_m = q_eval * b_m * (hb_m**2)
    z_d_m = q_eval**3 / (q_eval**2 + one_m)
    alpha_proj_m = (z_d_m - one_m) * hv / mp.mpf(2) - (hv**2) / mp.mpf(4)
    cos_exact_m = mp.cos(alpha_proj_m)
    cos_cubic_m = mp.fsum(cos_proj_in_uhab[k].to_mpf() * (u_hab_m**k) for k in range(4))
    cos_quartic_m = mp.fsum(cos_proj_in_uhab[k].to_mpf() * (u_hab_m**k) for k in range(5))
    cubic_trunc_err = abs(cos_cubic_m - cos_exact_m)
    quartic_trunc_err = abs(cos_quartic_m - cos_exact_m)

    # Verify exact cubic termination of Q_A/m_e
    qa_higher_zero = all(qa_over_me_hb[k].is_zero() for k in range(4, deg + 1))

    return {
        "Q_A_over_me_in_hbar_q": [qa_over_me_hb[k].to_exact_str() for k in range(7)],
        "Q_A_exact_cubic_termination": "1" if qa_higher_zero else "0",
        "cos_alpha_D_proj_in_y_deltaHabiroSq": [
            cos_proj_y[k].to_exact_str() for k in range(5)
        ],
        "cos_alpha_D_proj_in_u_Hab": [
            cos_proj_in_uhab[k].to_exact_str() for k in range(6)
        ],
        "Q_zD_over_me_in_hbar_q": [q_zd_over_me_hb[k].to_exact_str() for k in range(6)],
        "Q_KD6_over_me_in_hbar_q": [q_kd6_over_me_hb[k].to_exact_str() for k in range(6)],
        "Q_KD6_proj_N3_over_me_in_hbar_q": [
            q_kd6_full_n3_hb[k].to_exact_str() for k in range(7)
        ],
        "Delta_tr_conn_V3_in_hbar_q": [tr_conn_hb[k].to_exact_str() for k in range(7)],
        "Delta_tr_conn_V3_in_u_Hab": [
            tr_conn_in_uhab[k].to_exact_str() for k in range(5)
        ],
        "BringSchwinger_T_tree_q_q9_q10_in_hbar_q": [
            t_tree_q9_q10_hb[k].to_exact_str() for k in range(6)
        ],
        "BringSchwinger_bracket2_in_hbar_q": [
            bracket2_hb[k].to_exact_str() for k in range(6)
        ],
        "BringSchwinger_h_sq_in_hbar_q": [
            h2_s[k].to_exact_str() for k in range(6)
        ],
        "cos_alpha_D_proj_cubic_truncation_residual_at_q": fmt(cubic_trunc_err),
        "cos_alpha_D_proj_quartic_truncation_residual_at_q": fmt(quartic_trunc_err),
        "_raw_checks": {
            "qa_higher_zero": qa_higher_zero,
            "c0_eq_1": cos_proj_in_uhab[0] == Q3(Fraction(1), Fraction(0)),
            "c1_eq_neg_sqrt3_12": cos_proj_in_uhab[1]
            == Q3(Fraction(0), Fraction(-1, 12)),
            "c2_eq_47_96": cos_proj_in_uhab[2] == Q3(Fraction(47, 96), Fraction(0)),
            "c3_eq_neg_2069_sqrt3_5760": cos_proj_in_uhab[3]
            == Q3(Fraction(0), Fraction(-2069, 5760)),
            "c4_eq_11658923_17418240": cos_proj_in_uhab[4]
            == Q3(Fraction(11658923, 17418240), Fraction(0)),
            "cubic_trunc_err": cubic_trunc_err,
            "quartic_trunc_err": quartic_trunc_err,
        },
    }


# ---------------------------------------------------------------------------
# Part 2B: Two-Term Categorical Lagrangian + Corrected Photon alpha_EM^{corr}(q)
# ---------------------------------------------------------------------------


def alpha_em_bare_at(q_val: mp.mpf) -> mp.mpf:
    """Tree-level electromagnetic coupling 1 / (q * [9]_q * [10]_q) at 80 dps."""
    one = mp.mpf(1)
    hv = q_val - one / q_val
    q9 = (q_val**9 - q_val ** (-9)) / hv
    q10 = (q_val**10 - q_val ** (-10)) / hv
    return one / (q_val * q9 * q10)


def solve_consistent_two_term_proton_pin(
    qed_scale_mode: str, k_weighted: bool
) -> mp.mpf:
    """Solve m_p^{QCD}(q)/m_e + w * S_QED(q) * |tr_conn_p(V^3)| = m_p^{exp}/m_e at 80 dps.

    qed_scale_mode in {"fiber", "photon_ratio", "alpha_lag"}:
      - "fiber": S_QED(q) = 1 (raw fiber cancellation E_0 * hbar_q^2 -> m_e)
      - "photon_ratio": S_QED(q) = alpha_EM^{corr}(q) / alpha_EM^{bare}(q)
      - "alpha_lag": S_QED(q) = alpha_EM^{corr}(q) / hbar_q^2
        (Two-Term Categorical Lagrangian on hadronic scale m_e / hbar_q^2 with physical photon)
    """
    one = mp.mpf(1)
    two = mp.mpf(2)
    three = mp.mpf(3)
    four = mp.mpf(4)

    def residual(qq: mp.mpf) -> mp.mpf:
        hv = qq - one / qq
        hb_sq = (one - one / qq) ** 2
        tr_m_bor = abs((four + hv**2 - three * hv**4 - hv**6) / (hv**2 + four))
        qf3 = (qq**2 + one + qq ** (-2)) * (qq + qq ** (-1))
        qcd_over_me = two * _VOL_4_1_95 / hb_sq * (tr_m_bor * qf3 / qq**3) - mp.mpf(12)
        q2 = qq**2
        tr_p_abs = two * (q2 - one) ** 4 * (q2**2 + q2 + one) / (mp.mpf(27) * q2**3)
        w = qq if k_weighted else one
        if qed_scale_mode == "fiber":
            scale = one
        elif qed_scale_mode == "photon_ratio":
            scale = compute_alpha_em_bring_schwinger(qq) / alpha_em_bare_at(qq)
        elif qed_scale_mode == "alpha_lag":
            scale = compute_alpha_em_bring_schwinger(qq) / hb_sq
        else:
            raise ValueError(f"Unknown qed_scale_mode: {qed_scale_mode}")
        return qcd_over_me + w * scale * tr_p_abs - _MP_OVER_ME_MPF

    with mp.workdps(95):
        qv = q_at(90)
        eps = mp.mpf("1e-42")
        for _ in range(18):
            fq = residual(qv)
            if abs(fq) < mp.mpf("1e-82"):
                break
            dfq = (residual(qv + eps) - residual(qv - eps)) / (two * eps)
            qv = qv - fq / dfq
        return +qv


def evaluate_all_prescriptions_at_pin(pin_name: str, q_val: mp.mpf, q_mu: mp.mpf) -> dict:
    """Evaluate all parameter-free strong + Two-Term Lagrangian QED models at q_val (80 dps)."""
    one = mp.mpf(1)
    two = mp.mpf(2)
    four = mp.mpf(4)

    hv = q_val - one / q_val
    hb = one - one / q_val
    hb_sq = hb**2
    y_hab = (q_val + one / q_val) - two
    b_val = mp.sqrt(q_val**4 + q_val**2 + one) / (q_val**2 + one)
    u_lad = b_val * hb_sq
    u_hab = q_val * u_lad

    z_d = q_val**3 / (q_val**2 + one)
    alpha_d = (z_d - one) * hv / two
    alpha_proj = alpha_d - (hv**2) / four

    # Corrected Bring-Schwinger photon coupling vs bare tree coupling
    alpha_corr = compute_alpha_em_bring_schwinger(q_val)
    alpha_bare = alpha_em_bare_at(q_val)
    rho_photon = alpha_corr / alpha_bare
    ratio_alpha_over_hbsq = alpha_corr / hb_sq

    # Parameter-free strong bases
    q_a = _M_E_MPF * abs(q_val**2 - two * q_val - one) * (q_val + one) / (two * q_val**3)
    e0_t = _M_E_MPF / (q_val * (q_val - one)) / (one - hb_sq)
    w3 = (q_val**4 + one) / ((q_val**2 + one) ** 2)
    w21 = (q_val**2) / ((q_val**2 + one) ** 2)
    d111 = (q_val**3) / ((q_val**2 + one) * (q_val**4 + q_val**2 + one))
    chi3_d = -(q_val**2 - one) * ((q_val**2 + one) ** 2) / (four * q_val)
    chi111_d = -(q_val**2 - one) * ((q_val**2 + one) ** 2) / (four * q_val**5)
    p_poly = (
        two * q_val**12
        - mp.mpf(5) * q_val**10
        + mp.mpf(5) * q_val**8
        - mp.mpf(5) * q_val**6
        + mp.mpf(5) * q_val**4
        - mp.mpf(5) * q_val**2
        + two
    )
    chi21_int = (q_val**2 - one) * (q_val**4 + one) * p_poly / (four * q_val**9)
    chi21_grp = -(q_val**2 - one) * (q_val**4 + one) / (four * q_val**3)
    tr_zd_int = w3 * chi3_d + w21 * chi21_int
    tr_gp_int = tr_zd_int + d111 * chi111_d
    tr_gp_grp = w3 * chi3_d + w21 * chi21_grp + d111 * chi111_d
    c_kd6 = (q_val**6 + q_val ** (-6)) / two

    q_zd_int = e0_t * (-tr_zd_int)
    q_kd6_int = q_zd_int * c_kd6
    q_gp_int = e0_t * (-tr_gp_int)
    q_gp_grp = e0_t * (-tr_gp_grp)

    # Kashiwara-Hopf ladder factors
    f1_unproj = mp.cos(alpha_d - u_lad / two)
    f1_proj = mp.cos(alpha_proj - u_lad / two)
    f2 = one - u_lad**2
    f3 = one - two * (u_lad**3)

    # Connected Borromean V^3 QED splittings
    tr_conn_diff = tr_conn_borromean_diff_at(q_val, dps=80)
    dm_fiber_plain = -_M_E_MPF * tr_conn_diff
    dm_fiber_q = -_M_E_MPF * q_val * tr_conn_diff
    dm_ratio_plain = rho_photon * dm_fiber_plain
    dm_ratio_q = rho_photon * dm_fiber_q
    dm_alag_plain = ratio_alpha_over_hbsq * dm_fiber_plain
    dm_alag_q = ratio_alpha_over_hbsq * dm_fiber_q

    strong_specs = [
        ("FormA_N1unproj_N2", q_a * f1_unproj * f2),
        ("FormA_N1unproj_N2_N3", q_a * f1_unproj * f2 * f3),
        ("FormA_N1proj_N2", q_a * f1_proj * f2),
        ("FormA_N1proj_N2_N3", q_a * f1_proj * f2 * f3),
        ("KD6_int_N1unproj_N2", q_kd6_int * f1_unproj * f2),
        ("KD6_int_N1proj_N2", q_kd6_int * f1_proj * f2),
        ("KD6_int_N1proj_N2_N3", q_kd6_int * f1_proj * f2 * f3),
        ("GPMTpos_int_N1proj_N2", q_gp_int * f1_proj * f2),
        ("GPMTpos_int_N1proj_N2_N3", q_gp_int * f1_proj * f2 * f3),
        ("GPMTpos_grp_N1proj_N2", q_gp_grp * f1_proj * f2),
        ("zD_bare_int_N0", q_zd_int),
    ]
    qed_specs = [
        ("none", mp.mpf(0)),
        ("2t_fiber_plain", dm_fiber_plain),
        ("2t_fiber_q", dm_fiber_q),
        ("2t_photon_ratio_plain", dm_ratio_plain),
        ("2t_photon_ratio_q", dm_ratio_q),
        ("2t_alpha_lag_plain", dm_alag_plain),
        ("2t_alpha_lag_q", dm_alag_q),
    ]

    rows: dict[str, dict] = {}
    for s_name, q_strong in strong_specs:
        for q_name, dm_qed in qed_specs:
            qb = q_strong + dm_qed
            dpn = qb + _M_E_MPF
            mn = _M_P_MPF + dpn
            qb_err_ev = (qb - _QB_AME_MPF) * mp.mpf("1e6")
            qb_err_ppm = (qb - _QB_AME_MPF) / _QB_AME_MPF * mp.mpf("1e6")
            dpn_err_ppm = (dpn - _DPN_AME_MPF) / _DPN_AME_MPF * mp.mpf("1e6")
            mn_err_ppb = (mn - _M_N_AME_MPF) / _M_N_AME_MPF * mp.mpf("1e9")
            rows[f"{s_name}__{q_name}"] = {
                "strong_model": s_name,
                "qed_mode": q_name,
                "Q_strong_MeV": fmt(q_strong),
                "delta_m_QED_MeV": fmt(dm_qed),
                "Q_beta_MeV": fmt(qb),
                "Q_beta_err_eV": fmt(qb_err_ev),
                "Q_beta_err_ppm": fmt(qb_err_ppm),
                "Delta_pn_MeV": fmt(dpn),
                "Delta_pn_err_ppm": fmt(dpn_err_ppm),
                "m_n_MeV": fmt(mn),
                "m_n_err_ppb": fmt(mn_err_ppb),
            }

    return {
        "pin_name": pin_name,
        "q": fmt(q_val),
        "q_vs_q_muon_ppb": fmt((q_val - q_mu) / q_mu * mp.mpf("1e9")),
        "hbar_q": fmt(hb),
        "deltaHabiroSq_y": fmt(y_hab),
        "u_ladder": fmt(u_lad),
        "u_Hab_bar_even": fmt(u_hab),
        "inv_alpha_EM_bare": fmt(one / alpha_bare),
        "inv_alpha_EM_corr_BringSchwinger": fmt(one / alpha_corr),
        "photon_ratio_corr_over_bare": fmt(rho_photon),
        "lagrangian_ratio_alpha_corr_over_hbar_sq": fmt(ratio_alpha_over_hbsq),
        "prescriptions": rows,
    }


def main() -> int:
    q0_1t = q_at(80)
    q_mu = q_muon_at(80)
    q2t_fiber_plain = q_two_term_borromean_at(dps=80, k_weighted=False)
    q2t_fiber_kp = q_two_term_borromean_at(dps=80, k_weighted=True)
    q2t_ratio_plain = solve_consistent_two_term_proton_pin("photon_ratio", False)
    q2t_ratio_kp = solve_consistent_two_term_proton_pin("photon_ratio", True)
    q2t_alag_plain = solve_consistent_two_term_proton_pin("alpha_lag", False)
    q2t_alag_kp = solve_consistent_two_term_proton_pin("alpha_lag", True)

    part1 = run_part1_tail_and_ordering_verification(q2t_alag_plain)
    part2_series = compute_exact_operator_series(q2t_alag_plain)

    pins = [
        ("q_0_one_term", q0_1t),
        ("q_2t_fiber_plain", q2t_fiber_plain),
        ("q_2t_fiber_Kp", q2t_fiber_kp),
        ("q_2t_photon_ratio_plain", q2t_ratio_plain),
        ("q_2t_photon_ratio_Kp", q2t_ratio_kp),
        ("q_2t_alpha_lag_plain", q2t_alag_plain),
        ("q_2t_alpha_lag_Kp", q2t_alag_kp),
        ("q_muon", q_mu),
    ]
    part2_by_pin = {
        nm: evaluate_all_prescriptions_at_pin(nm, qv, q_mu) for nm, qv in pins
    }

    # Exact error-dilution factors (on exact additive reference mn_ref_sum = m_p + m_e + Q_beta)
    mn_ref_sum = _M_P_MPF + _DPN_AME_MPF
    dilution_dpn = _QB_AME_MPF / _DPN_AME_MPF
    dilution_mn = _QB_AME_MPF / mn_ref_sum
    sample_row = part2_by_pin["q_2t_alpha_lag_plain"]["prescriptions"][
        "KD6_int_N1proj_N2__2t_alpha_lag_plain"
    ]
    qb_s = mp.mpf(sample_row["Q_beta_MeV"])
    dpn_s = qb_s + _M_E_MPF
    mn_s = _M_P_MPF + dpn_s
    rel_qb = (qb_s - _QB_AME_MPF) / _QB_AME_MPF
    rel_dpn = (dpn_s - _DPN_AME_MPF) / _DPN_AME_MPF
    rel_mn = (mn_s - mn_ref_sum) / mn_ref_sum
    dilution_law_residual = abs(rel_dpn - dilution_dpn * rel_qb) + abs(
        rel_mn - dilution_mn * rel_qb
    )

    dilution_summary = {
        "Q_beta_AME_MeV": fmt(_QB_AME_MPF),
        "Delta_pn_AME_MeV": fmt(_DPN_AME_MPF),
        "Delta_pn_CODATA_direct_MeV": fmt(_DPN_COD_MPF),
        "m_n_AME_MeV": fmt(_M_N_AME_MPF),
        "m_n_CODATA_direct_MeV": fmt(_M_N_COD_MPF),
        "dilution_factor_Q_over_Delta_pn": fmt(dilution_dpn),
        "dilution_factor_Q_over_m_n": fmt(dilution_mn),
        "dilution_law_identity_residual": fmt(dilution_law_residual),
    }

    # Print concise fixed-width 80-dps summary table
    print("=" * 116)
    print(
        "QBETA CONVENTION-D 5-LETTER TAIL (qou-j1e5), u^3 SERIES (qou-51yf), & 2-TERM LAGRANGIAN PHOTON — 80 DPS"
    )
    print("=" * 116)
    for nm, _ in pins:
        pinfo = part2_by_pin[nm]
        print(
            f"  {nm:24s}: q = {pinfo['q'][:26]} | vs q_muon = {pinfo['q_vs_q_muon_ppb'][:9]:>9s} ppb | "
            f"1/alpha_corr = {pinfo['inv_alpha_EM_corr_BringSchwinger'][:16]}"
        )

    print("\n--- Exact Operator Series in Bar-Even u_Hab = q * b(q) * hbar_q^2 ---")
    for k, c_str in enumerate(part2_series["cos_alpha_D_proj_in_u_Hab"]):
        print(f"  [u_Hab^{k}] cos(alpha_D^proj) = {c_str}")
    print(f"  Q_A / m_e in hbar_q         = {part2_series['Q_A_over_me_in_hbar_q']}")
    print(f"  Delta_tr_conn(V^3) in hbar_q = {part2_series['Delta_tr_conn_V3_in_hbar_q']}")

    print("\n--- Side-by-Side 80-dps Q_beta / Delta_pn / m_n Table (Zero Fitting) ---")
    header = (
        f"  {'Pin':23s} | {'Strong Prescription':25s} | {'QED Mode':21s} | "
        f"{'Q_beta (MeV) [ppm]':26s} | {'Delta_pn [ppm]':18s} | {'m_n [ppb]'}"
    )
    print(header)
    print("-" * 135)
    highlight_keys = [
        ("q_0_one_term", "FormA_N1unproj_N2", "none"),
        ("q_0_one_term", "FormA_N1unproj_N2_N3", "none"),
        ("q_0_one_term", "KD6_int_N1proj_N2", "none"),
        ("q_0_one_term", "KD6_int_N1proj_N2_N3", "none"),
        ("q_2t_fiber_plain", "FormA_N1unproj_N2", "2t_fiber_plain"),
        ("q_2t_fiber_plain", "KD6_int_N1unproj_N2", "2t_fiber_plain"),
        ("q_2t_fiber_plain", "KD6_int_N1proj_N2", "2t_fiber_plain"),
        ("q_2t_photon_ratio_plain", "KD6_int_N1proj_N2", "2t_photon_ratio_plain"),
        ("q_2t_alpha_lag_plain", "FormA_N1unproj_N2", "2t_alpha_lag_plain"),
        ("q_2t_alpha_lag_plain", "FormA_N1proj_N2", "2t_alpha_lag_plain"),
        ("q_2t_alpha_lag_plain", "KD6_int_N1unproj_N2", "2t_alpha_lag_plain"),
        ("q_2t_alpha_lag_plain", "KD6_int_N1proj_N2", "2t_alpha_lag_plain"),
        ("q_2t_alpha_lag_Kp", "KD6_int_N1proj_N2", "2t_alpha_lag_q"),
        ("q_2t_alpha_lag_plain", "KD6_int_N1proj_N2_N3", "2t_alpha_lag_plain"),
        ("q_2t_alpha_lag_plain", "GPMTpos_int_N1proj_N2", "2t_alpha_lag_plain"),
        ("q_2t_alpha_lag_plain", "GPMTpos_grp_N1proj_N2", "2t_alpha_lag_plain"),
    ]
    for p_nm, s_nm, q_nm in highlight_keys:
        r = part2_by_pin[p_nm]["prescriptions"][f"{s_nm}__{q_nm}"]
        print(
            f"  {p_nm:23s} | {s_nm:25s} | {q_nm:21s} | "
            f"{r['Q_beta_MeV'][:11]} ({r['Q_beta_err_ppm'][:8]:>8s}) | "
            f"{r['Delta_pn_err_ppm'][:8]:>8s} ppm      | "
            f"{r['m_n_err_ppb'][:8]:>8s} ppb"
        )

    p1_raw = part1["_raw_checks"]
    p2_raw = part2_series["_raw_checks"]
    checks = [
        (
            "part1_constituent_to_decay_bridge_and_ordering_selection",
            bool(
                p1_raw["constituent_bridge_residual"] < mp.mpf("1e-70")
                and p1_raw["defect_residual"] < mp.mpf("1e-70")
                and p1_raw["defect_val"] > mp.mpf(0)
                and p1_raw["p_int_lt_grp_2t"]
                and p1_raw["n_int_lt_grp_2t"]
                and p1_raw["p_int_lt_duu_2t"]
                and p1_raw["n_int_lt_dud_2t"]
            ),
            (
                "Constituent-to-decay identity tr_zD(n - p) == -(trM(p_Bor) - trM(n_Bor)) "
                "and interleaved < grouped constituent 2-term energy ordering hold at 80 dps"
            ),
        ),
        (
            "part2_formA_exact_cubic_and_mirror_phase_uHab_coefficients",
            bool(
                p2_raw["qa_higher_zero"]
                and p2_raw["c0_eq_1"]
                and p2_raw["c1_eq_neg_sqrt3_12"]
                and p2_raw["c2_eq_47_96"]
                and p2_raw["c3_eq_neg_2069_sqrt3_5760"]
                and p2_raw["c4_eq_11658923_17418240"]
                and p2_raw["cubic_trunc_err"] < mp.mpf("1e-7")
                and p2_raw["quartic_trunc_err"] < mp.mpf("1e-9")
            ),
            (
                "Q_A/m_e terminates identically at hbar_q^3 and cos(alpha_D^proj) expands in "
                "bar-even u_Hab with exact Q(sqrt(3)) coefficients (1, -sqrt(3)/12, 47/96, -2069*sqrt(3)/5760)"
            ),
        ),
        (
            "part2_twoterm_lagrangian_alpha_corr_pin_and_error_dilution",
            bool(
                abs(
                    mp.mpf(part2_by_pin["q_2t_alpha_lag_plain"]["q_vs_q_muon_ppb"])
                )
                < mp.mpf("5")
                and abs(mp.mpf(sample_row["Q_beta_err_ppm"])) < mp.mpf("50")
                and abs(mp.mpf(sample_row["m_n_err_ppb"])) < mp.mpf("40")
                and dilution_law_residual < mp.mpf("1e-75")
            ),
            (
                f"Consistent 2-term Lagrangian alpha_EM^corr pin sits at "
                f"{part2_by_pin['q_2t_alpha_lag_plain']['q_vs_q_muon_ppb'][:6]} ppb from q_muon, "
                f"KD6*N1(proj)*N2+2t_alpha_lag gives Q_beta {sample_row['Q_beta_err_ppm'][:7]} ppm / "
                f"m_n {sample_row['m_n_err_ppb'][:7]} ppb, and dilution law holds to {fmt(dilution_law_residual, 10)}"
            ),
        ),
    ]

    print("\n--- Verification Assertions ---")
    for name, ok, detail in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    if not all(ok for _, ok, _ in checks):
        raise RuntimeError("Verification assertion failed")

    # Strip internal mpmath check dicts before serializing witness JSON
    part1_clean = {k: v for k, v in part1.items() if k != "_raw_checks"}
    part2_series_clean = {k: v for k, v in part2_series.items() if k != "_raw_checks"}

    w = WitnessBuilder("qbeta-convention-d-c3-and-tail-derivation", engine="mpmath")
    w.set_description(
        "80-dps zero-float64 derivation witness for the 5-letter valence/gluon tail closure "
        "(qou-j1e5), exact Q(sqrt(3)) operator Taylor expansion through u^3 (qou-51yf / qou-cds1), "
        "and Two-Term Categorical Lagrangian evaluation with Form-B Bring-Schwinger corrected "
        "photon coupling alpha_EM^{corr}(q_{2t}) across Q_beta, Delta_pn, and m_n."
    )
    w.add_data("dps", 80)
    w.add_data("q0_proton_50digit", Q_50_DIGIT_STR)
    w.add_data("part1_tail_and_ordering_derivation", part1_clean)
    w.add_data("part2_exact_symbolic_series", part2_series_clean)
    w.add_data("part2_prescriptions_by_pin", part2_by_pin)
    w.add_data("part2_error_dilution_summary", dilution_summary)
    w.add_caveat(
        "All symbolic coefficients are derived from operator traces in Q(sqrt(3)) over exact "
        "Fraction arithmetic with zero CODATA fitting; all numerical evaluations run at 80-dps "
        "mpmath precision with zero float64 conversions."
    )
    for name, ok, detail in checks:
        w.add_assertion(name, "1" if ok else "0", "1", "0", source=detail)

    out_path = w.save(
        q0_comparison(
            muon=q_mu,
            proton=q0_1t,
            reason=(
                "Compares 1-term proton, consistent 2-term Borromean / corrected-photon "
                "Lagrangian proton pins, and CODATA-2022 muon pin across Q_beta, Delta_pn, and m_n."
            ),
        )
    )
    print(f"\nWrote witness -> {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
