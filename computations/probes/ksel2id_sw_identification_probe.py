#!/usr/bin/env python3
"""ksel2id_sw_identification_probe.py — KSel-2-ID (bean qou-0ms0): is the
balanced binding-kernel moment family the classical Stieltjes–Wigert /
q-Laguerre indeterminate family, up to explicit rescaling?

AUDIT-ONLY — scope-(a), NO FIT, nothing wired. Every scored check is an
exact symbolic identity (sympy) or a numeric cross-check of a displayed
identity at stated tolerance (mpmath), at p = 5/6 and both q0 pins.

TARGET. The KSel-2 audit (2026-08-01-ksel2-gns-favard-canonicity.md)
derived the canonical Jacobi operator J(q) of the balanced moments
  m_k = q^{-k(k-1)/4} [k]_q!          (one-sided [k]_q, q > 1)
and located the kernel convention in its self-adjoint-extension circle.
Working hypothesis tested here: this indeterminate family IS (up to
explicit change of variable) the classical Stieltjes–Wigert (SW) /
q-Laguerre family (Stieltjes 1894 log-normal example; [wigert-lit via
christiansen2003sw]; q-Laguerre [moak1981]).

NOTATION. p = 1/q in (0,1); ptilde = sqrt(p); qtilde = sqrt(q);
L = ln(qtilde) = (ln q)/2. (p;p)_k = prod_{j<=k} (1-p^j).

SECTIONS (S1-S5):

  S1  Base-p rewrite (sympy exact, k <= 12):
        [k]_q!  = p^{-k(k-1)/2} (p;p)_k / (1-p)^k
        m_k     = ptilde^{-k(k-1)/2} (p;p)_k / (1-p)^k
      i.e. the balanced family = [Gaussian factor at base qtilde] x
      [q-Pochhammer factor at base q].
  S2  SW-proper reference (sympy exact): the log-normal LN(mu,s2) has
      moments E[s^k] = exp(k*mu + k^2*s2/2) — log-QUADRATIC in k; the
      class of log-quadratic moment sequences is CLOSED under every
      affine-in-log map s -> c*s^a (pushforward LN -> LN(ln c + a*mu,
      a^2*s2)). The classical SW weight w_g(x) = (g/sqrt(pi))
      exp(-g^2 ln^2 x) is LN(1/(4g^2)... exactly LN(mu=1/(2g^2)*0 + ...)
      — verified as the normalized moment sequence t^{-k(k+2)/2},
      t = e^{-1/(2g^2)} (Stieltjes 1894 example).
  S3  Obstruction (exact): Delta^2 ln m_k = L + ln((1-p^{k+2})/
      (1-p^{k+1})); the second term is > 0 and strictly decreasing to 0
      (exact at rational p), so Delta^2 is NOT constant => m_k is NOT
      log-quadratic => NO affine-in-log map
      matches the balanced family to SW-proper — scope-(b) exclusion
      with cited invariant (log-quadraticity is affine-in-log
      invariant). NEAR quantification: the deviation from quadratic is
      O(p^k) but at the q0 pins (p ~ 0.901) it is O(1) at accessible
      orders (residual vs the unique quadratic through k=0,1,2 tabled;
      -0.29 nats at k=3, -25.6 at k=12). Verdict: NO-MATCH to SW-proper.
  S4  SW is an exact FACTOR (the identification that does hold):
        m_k = G_k * J_k,
        G_k = exp(L*k^2/2 - L*k/2) = LN(-L/2, L) moments
            = the classical SW weight with t = e^{-L} = 1/qtilde
              (whose x-measure is LN(+L, L)), pushed forward by
              s -> s * qtilde^{-3/2} (exact parameter match,
              symbolic),
        J_k = (p;p)_k/(1-p)^k = moments of the Jackson factor
              mu_J = (p;p)_oo sum_m [p^m/(p;p)_m] delta_{p^m/(1-p)}
              (numeric via Euler's q-exponential sum, tol 1e-30,
              p = 5/6 + both pins) — compactly supported in
              (0, 1/(1-p)] hence DETERMINATE.
      So: balanced = SW(base qtilde) (*) Jackson — the indeterminacy
      core of the binding kernel family IS Stieltjes' 1894 log-normal
      example at base qtilde = sqrt(q); the ksel3 "one Gaussian"
      (sigma^2 = L, mu = -L/2) is exactly this SW factor.
  S5  q-Laguerre (generalized SW) identification — EXACT for the
      one-sided convention:
      (a) functional equation of the alpha=0 q-Laguerre weight
          w(x) = 1/(-x;p)_oo:  w(p x) = (1+x) w(x)  =>  moment
          recurrence nu_{k+1} = p^{-(k+1)} (1-p^{k+1}) nu_k (exact;
          numeric quadrature cross-check at p = 5/6 + both pins)
      (b) => normalized q-Laguerre moments rho_k = p^{-k(k+1)/2}(p;p)_k
      (c) EXACT map (symbolic, k <= 12):
            [k]_q! = rho_k * (p/(1-p))^k
          i.e. the ONE-SIDED normalizer family is exactly the
          q-Laguerre alpha=0 ([moak1981]) family under the pure
          scaling s -> (p/(1-p)) s — affine-in-log with a = 1.
      (d) balanced bridge (symbolic): m_k = p^{k(k-1)/4} [k]_q!, and
          p^{k(k-1)/4} = 1/G_k' with G_k' = LN(-L/2, L) moments, so
            m_k * G_k' = [k]_q!  (exactly one extra SW-Gaussian
          convolution carries balanced -> one-sided -> q-Laguerre).
          NOT affine-in-log (S3 obstruction applies to the residual
          quadratic factor); the balanced member is the bar-symmetric
          "half-dressed" point between Jackson and q-Laguerre.

VERDICTS (emitted in witness): sw_proper NO-MATCH (exact obstruction);
sw_factor EXACT; q_laguerre_one_sided EXACT (map s -> (p/(1-p)) s);
q_laguerre_balanced exact one-Gaussian bridge, not affine-in-log.

Exit 0 iff all assertions pass. Witness:
ksel2id-sw-identification.witness.json (audit-only).
Audit doc: docs/audits/2026-08-01-ksel2id-friedrichs-sw-identification.md.
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02). Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _bridge

import json  # noqa: E402

import sympy as sp  # noqa: E402
from mpmath import mp, mpf, exp as mexp, quad as mquad, qp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

TOL_30 = mpf("1e-30")   # Euler / Jackson moment identity
TOL_Q = mpf("1e-20")    # quadrature cross-checks (dps 40 working)
N_SYM = 12              # symbolic identity depth

_MUON_WITNESS = _Path(__file__).resolve().parent.parent / \
    "q-pinning-50-digit.witness.json"
Q0_MUON_STR = record_upstream(_MUON_WITNESS, _UPSTREAM_RECORDS)["q0Value"]
# tools/qou-substrate/python/qou_substrate/constants.py::Q_50_DIGIT_STR
Q0_PROTON_STR = "1.1099785827513808075916690956107688798744991218736"

_p, _pt, _c, _a, _mu, _s2, _k, _x, _g = sp.symbols(
    "p pt c a mu s2 k x g", positive=True)


def qint_q(qv, k: int):
    """One-sided [k]_q = 1 + q + ... + q^{k-1}."""
    return sum(qv ** i for i in range(k))


def qfact_q(qv, m: int):
    r_ = qv ** 0
    for j in range(1, m + 1):
        r_ = r_ * qint_q(qv, j)
    return r_


def qpoch(pv, k: int):
    """(p;p)_k = prod_{j=1..k} (1 - p^j)."""
    r_ = pv ** 0
    for j in range(1, k + 1):
        r_ = r_ * (1 - pv ** j)
    return r_


# ------------------------------------------------------ S1 base-p rewrite

def block_s1_base_p(wb: WitnessBuilder):
    q = 1 / _pt ** 2          # p = pt^2, q = 1/p — pt = sqrt(p) exact
    p = _pt ** 2
    for k in range(N_SYM + 1):
        one_sided = qfact_q(q, k)
        rhs_os = p ** sp.Rational(-k * (k - 1), 2) * qpoch(p, k) \
            / (1 - p) ** k
        assert sp.simplify(one_sided - rhs_os) == 0, (k, "one-sided")
        balanced = q ** sp.Rational(-k * (k - 1), 4) * qfact_q(q, k)
        rhs_bal = _pt ** (-(k * (k - 1)) // 2) * qpoch(p, k) / (1 - p) ** k
        assert sp.simplify(balanced - rhs_bal) == 0, (k, "balanced")
    wb.add_assertion(
        "s1_base_p_rewrite_exact", computed="0", expected="0", tolerance=0,
        source="sympy exact (k <= 12, p = pt^2 so ptilde = sqrt(p) is "
               "polynomial): [k]_q! = p^(-k(k-1)/2)(p;p)_k/(1-p)^k and "
               "m_k = q^(-k(k-1)/4)[k]_q! "
               "= ptilde^(-k(k-1)/2)(p;p)_k/(1-p)^k — the balanced "
               "family = [Gaussian factor at base qtilde] x "
               "[q-Pochhammer factor at base q]")
    wb.add_data("s1_base_p", {
        "one_sided": "[k]_q! = p^(-k(k-1)/2) (p;p)_k / (1-p)^k",
        "balanced": "m_k = ptilde^(-k(k-1)/2)(p;p)_k/(1-p)^k = "
                    "e^(L k(k-1)/2) (p;p)_k/(1-p)^k, L = ln qtilde",
        "reading": "Gaussian (log-quadratic) part at base qtilde = "
                   "sqrt(q); Pochhammer part at base q — MIXED bases: "
                   "the balanced convention is the half-step "
                   "(bar-symmetric) point",
    })


# --------------------------------------------- S2 SW-proper reference class

def block_s2_sw_reference(wb: WitnessBuilder):
    t = sp.symbols("t", positive=True)
    # log-normal moments: E[s^k] = exp(k mu + k^2 s2 / 2) (Gaussian integral)
    integrand = sp.exp(_k * t) * sp.exp(-(t - _mu) ** 2 / (2 * _s2)) \
        / sp.sqrt(2 * sp.pi * _s2)
    mom = sp.simplify(sp.integrate(integrand, (t, -sp.oo, sp.oo)))
    target = sp.exp(_k * _mu + _k ** 2 * _s2 / 2)
    assert sp.simplify(mom - target) == 0, mom
    # affine-in-log closure: s -> c s^a gives moments c^k E[s^{ak}] =
    # exp(k(ln c + a mu) + k^2 (a^2 s2)/2) — still log-quadratic
    pushed = sp.simplify(_c ** _k * target.subs(_k, _a * _k))
    closed = sp.exp(_k * (sp.log(_c) + _a * _mu) +
                    _k ** 2 * (_a ** 2 * _s2) / 2)
    assert sp.simplify(pushed / closed - 1) == 0
    # classical SW weight (Stieltjes 1894): w_g(x) = (g/sqrt(pi))
    # exp(-g^2 ln^2 x) on (0,oo): x-moments = exp((k+1)^2/(4 g^2));
    # normalized: t_sw^{-k(k+2)/2} with t_sw = exp(-1/(2 g^2))
    wmom = sp.simplify(sp.integrate(
        sp.exp((_k + 1) * t) * (_g / sp.sqrt(sp.pi)) *
        sp.exp(-_g ** 2 * t ** 2),
        (t, -sp.oo, sp.oo)).rewrite(sp.erf))   # erfc -> 1 - erf
    assert sp.simplify(wmom - sp.exp((_k + 1) ** 2 / (4 * _g ** 2))) == 0
    norm = sp.simplify(wmom / wmom.subs(_k, 0))
    tsw = sp.exp(-1 / (2 * _g ** 2))
    assert sp.simplify(norm - tsw ** (-_k * (_k + 2) / 2)) == 0
    wb.add_assertion(
        "s2_sw_lognormal_affine_closure_exact", computed="0",
        expected="0", tolerance=0,
        source="sympy exact: LN(mu,s2) moments exp(k mu + k^2 s2/2) "
               "(log-QUADRATIC in k); affine-in-log pushforward "
               "s -> c s^a keeps log-quadraticity (LN -> LN(ln c + "
               "a mu, a^2 s2)); classical SW weight (g/sqrt(pi))"
               "exp(-g^2 ln^2 x) has normalized moments "
               "t_sw^(-k(k+2)/2), t_sw = e^(-1/(2g^2)) — the "
               "Stieltjes 1894 log-normal example")


# ------------------------------------------------------- S3 obstruction

def block_s3_obstruction(wb: WitnessBuilder):
    # Delta^2 ln m_k = L + ln((1-p^{k+2})/(1-p^{k+1})): exact and strictly
    # increasing in k at rational p (=> NOT constant => not log-quadratic).
    pv = sp.Rational(9, 10)
    # ln of a strictly increasing >0 argument: compare arguments exactly
    args = [(1 - pv ** (k + 2)) / (1 - pv ** (k + 1)) for k in range(11)]
    assert all(args[i + 1] < args[i] for i in range(10)), "monotone dec"
    assert all(a > 1 for a in args), "above 1 (deviation positive)"
    # symbolic: Delta ln m_k = ln(m_{k+1}/m_k); built from S1 rewrite
    p = _pt ** 2
    q = 1 / p
    for k in range(0, 8):
        mk = _pt ** (-(k * (k - 1)) // 2) * qpoch(p, k) / (1 - p) ** k
        mk1 = _pt ** (-((k + 1) * k) // 2) * qpoch(p, k + 1) \
            / (1 - p) ** (k + 1)
        mk2 = _pt ** (-((k + 2) * (k + 1)) // 2) * qpoch(p, k + 2) \
            / (1 - p) ** (k + 2)
        # second ratio r2 = (m_{k+2} m_k)/(m_{k+1}^2) =
        #   qtilde * (1-p^{k+2})/(1-p^{k+1})   [qtilde = 1/pt^2... in p:
        #   ptilde^{-2} = 1/p^... ]  — verify exactly:
        r2 = sp.simplify(mk2 * mk / mk1 ** 2)
        # qtilde = q^{1/2} = pt^{-1}
        target = _pt ** (-1) * (1 - p ** (k + 2)) / (1 - p ** (k + 1))
        assert sp.simplify(r2 - target) == 0, (k, r2)
    # residual vs the unique log-quadratic through k = 0,1,2 at the pins
    set_compute_dps(60)
    resid_tbl = {}
    for tag, qs in (("muon", Q0_MUON_STR), ("proton", Q0_PROTON_STR)):
        q0 = mpf(qs)
        lm = []
        for k in range(13):
            f = mpf(1)
            for j in range(1, k + 1):
                f *= sum(q0 ** i for i in range(j))
            lm.append(mp.log(q0 ** (-mpf(k * (k - 1)) / 4) * f))
        # quadratic through 0,1,2: Q(k) = lm0 + k(lm1-lm0) +
        #   k(k-1)/2 (lm2-2lm1+lm0)
        Qf = lambda k: lm[0] + k * (lm[1] - lm[0]) + \
            mpf(k * (k - 1)) / 2 * (lm[2] - 2 * lm[1] + lm[0])  # noqa: E731
        res = [lm[k] - Qf(k) for k in range(13)]
        assert abs(res[12]) > mpf("0.5"), res[12]
        resid_tbl[tag] = {str(k): mp.nstr(res[k], 6)
                          for k in (3, 6, 9, 12)}
    wb.add_assertion(
        "s3_sw_proper_no_match_exact_obstruction", computed="0",
        expected="0", tolerance=0,
        source="exact: Delta^2 ln m_k = ln qtilde + ln((1-p^(k+2))/"
               "(1-p^(k+1))) — the second factor is > 1 and strictly "
               "decreasing to 1 (exact at p = 9/10; symbolic identity "
               "for the second ratio verified k <= 7) => ln m_k is NOT "
               "quadratic in k; log-quadraticity is invariant under "
               "every affine-in-log map (S2) => NO map s -> c s^a "
               "carries the balanced family to ANY SW-proper "
               "(log-normal) moment family. Scope-(b) exclusion with "
               "cited invariant. Deviation from quadratic at the pins "
               "is O(1) at accessible orders (residual -0.29 nats at "
               "k = 3, -25.6 nats at k = 12), asymptotic Delta^2 decay "
               "rate p^k.")
    wb.add_data("s3_obstruction", {
        "delta2_identity": "m_{k+2} m_k / m_{k+1}^2 = qtilde * "
                           "(1-p^(k+2))/(1-p^(k+1)) — exact symbolic",
        "verdict_sw_proper": "NO-MATCH (exact): the q-Pochhammer factor "
                             "cannot be produced by any affine-in-log "
                             "rescaling of a log-normal",
        "residual_vs_quadratic_nats": resid_tbl,
        "near_rate": "deviation of Delta^2 from constant ~ p^(k+1)(1-p) "
                     "-> 0: the family is SW-proper only asymptotically",
    })


# --------------------------------------------- S4 SW factor + Jackson

def block_s4_sw_factor(wb: WitnessBuilder):
    # symbolic parameter match: G_k = exp(L k^2/2 - L k/2) is LN(-L/2, L);
    # classical SW weight with t_sw = e^{-L} (g^2 = 1/(2L)) pushed by
    # s -> c s with c = e^{-L/2}: moments c^k t_sw^{-k(k+2)/2} =
    # e^{-Lk/2} e^{L k(k+2)/2} = e^{L k^2/2 + L k/2}... match to LN(+?):
    Lsym = sp.symbols("Lsym", positive=True)
    Gk = sp.exp(Lsym * _k ** 2 / 2 - Lsym * _k / 2)
    ln_mom = sp.exp(_k * (-Lsym / 2) + _k ** 2 * Lsym / 2)
    assert sp.simplify(Gk - ln_mom) == 0
    tsw = sp.exp(-Lsym)
    # normalized SW-weight x-moments are LN(+L, L): t_sw^{-k(k+2)/2} =
    # e^{L k^2/2 + L k}; pushforward s -> c s with c = e^{-3L/2} lands
    # on G_k = LN(-L/2, L) moments:
    pushed = (sp.exp(-3 * Lsym / 2)) ** _k * tsw ** (-_k * (_k + 2) / 2)
    assert sp.simplify(sp.expand(sp.log(pushed) - sp.log(Gk))) == 0
    # Jackson factor moments via Euler's identity, numeric at 3 points
    set_compute_dps(60)
    worst = mpf(0)
    for qs in ("1.2", Q0_MUON_STR, Q0_PROTON_STR):
        q0 = mpf(qs)
        pn = 1 / q0
        ppinf = qp(pn, pn)                      # (p;p)_oo
        M = 900                                  # p^900 ~ 1e-42 at pins
        for k in range(0, 9):
            # sum_m w_m (p^m/(1-p))^k, w_m = (p;p)_oo p^m/(p;p)_m
            s = mpf(0)
            poch = mpf(1)
            for m in range(M):
                if m > 0:
                    poch *= (1 - pn ** m)
                s += pn ** m / poch * pn ** (m * k)
            s *= ppinf / (1 - pn) ** k
            target = mpf(1)
            for j in range(1, k + 1):
                target *= (1 - pn ** j)
            target /= (1 - pn) ** k
            worst = max(worst, abs(s / target - 1))
    assert worst < TOL_30, worst
    wb.add_assertion(
        "s4_sw_exact_factor_decomposition", computed="0", expected="0",
        tolerance=float(TOL_30),
        source="symbolic: m_k = G_k J_k with G_k = LN(-L/2, L) moments "
               "= the classical SW weight at t_sw = e^(-L) = 1/qtilde "
               "pushed by s -> s qtilde^(-3/2) (exact); numeric: the "
               "Jackson atomic measure (p;p)_oo sum p^m/(p;p)_m "
               "delta_{p^m/(1-p)} has moments (p;p)_k/(1-p)^k via "
               "Euler's q-exponential (rel < 1e-30 at q = 1.2 + both "
               "pins, k <= 8) — support in (0, 1/(1-p)] compact => "
               "determinate. Balanced = SW(base qtilde) (*) Jackson: "
               "the indeterminacy core IS Stieltjes' 1894 example.")
    wb.add_data("s4_sw_factor", {
        "decomposition": "m_k = G_k * J_k exactly; G_k = SW/log-normal "
                         "(sigma^2 = L = ln qtilde, mu = -L/2 — the "
                         "ksel3 'one Gaussian'); J_k = Jackson, "
                         "determinate (compact support)",
        "sw_parameters": "t_sw = 1/qtilde; scaling c = qtilde^(-3/2), "
                         "a = 1",
        "jackson_worst_rel": mp.nstr(worst, 4),
        "reading": "the u-translate/extension indeterminacy of the "
                   "balanced kernel family is carried ENTIRELY by the "
                   "classical SW factor (christiansen2003sw, berg1995 "
                   "frame); the Jackson dressing is determinate",
    })


# ------------------------------------------------------ S5 q-Laguerre

def block_s5_q_laguerre(wb: WitnessBuilder):
    # (a) functional equation w(p x) = (1+x) w(x) for w = 1/(-x;p)_oo:
    #     symbolic on the truncated product, exact in the infinite limit
    #     via (-x;p)_oo = (1+x)(-px;p)_oo:
    Nprod = 14
    prod_full = sp.prod([1 + _x * _p ** n for n in range(Nprod)])
    prod_shift = sp.prod([1 + _x * _p ** (n + 1) for n in range(Nprod - 1)])
    assert sp.expand(prod_full - (1 + _x) * prod_shift) == 0
    # => nu_k = p^{k+1}(nu_k + nu_{k+1})  =>
    #    nu_{k+1} = p^{-(k+1)}(1-p^{k+1}) nu_k
    # => rho_k = nu_k/nu_0 = p^{-k(k+1)/2}(p;p)_k  (finite product, exact)
    for k in range(N_SYM + 1):
        prod_ratio = sp.prod(
            [_p ** (-(j + 1)) * (1 - _p ** (j + 1)) for j in range(k)])
        closed = _p ** sp.Rational(-k * (k + 1), 2) * qpoch(_p, k)
        assert sp.simplify(prod_ratio - closed) == 0, k
    # numeric quadrature cross-check of the recurrence at 3 points
    set_compute_dps()
    worst_q = mpf(0)
    pts = [mpf(5) / 6, 1 / mpf(Q0_MUON_STR), 1 / mpf(Q0_PROTON_STR)]
    quad_tbl = {}
    for pi, pn in enumerate(pts):
        def nu(k):
            f = lambda t: mexp((k + 1) * t) / qp(-mexp(t), pn)  # noqa: E731
            return mquad(f, [-50, -10, 0, 3, 8, 20, 50])
        prev = nu(0)
        worst_here = mpf(0)
        for k in range(0, 6):
            cur = nu(k + 1)
            target = pn ** (-(k + 1)) * (1 - pn ** (k + 1))
            worst_here = max(worst_here, abs((cur / prev) / target - 1))
            prev = cur
        quad_tbl[["p_5_6", "p_inv_q0_muon", "p_inv_q0_proton"][pi]] = \
            mp.nstr(worst_here, 4)
        worst_q = max(worst_q, worst_here)
    assert worst_q < TOL_Q, worst_q
    # (c) EXACT map: [k]_q! = rho_k (p/(1-p))^k   (symbolic, k <= 12)
    p = _pt ** 2
    q = 1 / p
    for k in range(N_SYM + 1):
        rho = p ** sp.Rational(-k * (k + 1), 2) * qpoch(p, k)
        assert sp.simplify(qfact_q(q, k) - rho * (p / (1 - p)) ** k) == 0, k
    # (d) balanced bridge: m_k * G'_k = [k]_q! with G'_k = LN(-L/2,L)
    #     moments = p^{-k(k-1)/4}: symbolic trivial
    for k in range(N_SYM + 1):
        bal = q ** sp.Rational(-k * (k - 1), 4) * qfact_q(q, k)
        assert sp.simplify(
            bal * q ** sp.Rational(k * (k - 1), 4) - qfact_q(q, k)) == 0
    set_compute_dps(60)
    wb.add_assertion(
        "s5_q_laguerre_one_sided_exact_identification", computed="0",
        expected="0", tolerance=float(TOL_Q),
        source="exact: the alpha=0 q-Laguerre weight 1/(-x;p)_oo "
               "satisfies w(px) = (1+x)w(x) => nu_{k+1} = "
               "p^(-(k+1))(1-p^(k+1)) nu_k (quadrature cross-check rel "
               "< 1e-20 at p = 5/6 + both pins, k <= 6) => rho_k = "
               "p^(-k(k+1)/2)(p;p)_k; symbolic k <= 12: [k]_q! = "
               "rho_k (p/(1-p))^k — the ONE-SIDED normalizer family "
               "IS the q-Laguerre (Moak) family under the exact "
               "scaling s -> (p/(1-p)) s; balanced = one-sided "
               "deconvolved by exactly one SW Gaussian LN(-L/2, L)")
    wb.add_data("s5_q_laguerre", {
        "moment_recurrence": "nu_{k+1}/nu_k = p^(-(k+1))(1-p^(k+1)) — "
                             "derived from w(px) = (1+x)w(x), exact",
        "closed_form": "rho_k = p^(-k(k+1)/2) (p;p)_k (normalized "
                       "alpha=0 q-Laguerre moments, [moak1981])",
        "exact_map_one_sided": "[k]_q! = rho_k (p/(1-p))^k — "
                               "pushforward under s -> (p/(1-p)) s",
        "balanced_bridge": "m_k = p^(k(k-1)/4) [k]_q!: exactly one "
                           "SW-Gaussian factor (LN(-L/2, L)) between "
                           "balanced and one-sided/q-Laguerre; NOT "
                           "affine-in-log (S3 obstruction)",
        "quadrature_worst_rel": quad_tbl,
        "verdicts": {
            "sw_proper": "NO-MATCH (exact obstruction, S3)",
            "sw_factor": "EXACT (S4): balanced = SW(1/qtilde) (*) "
                         "Jackson",
            "q_laguerre_one_sided": "EXACT: s -> (p/(1-p)) s",
            "q_laguerre_balanced": "one-Gaussian bridge exact; no "
                                   "affine-in-log identification",
        },
    })


# ------------------------------------------------------------------ main

def main() -> int:
    set_compute_dps(60)
    wb = WitnessBuilder("ksel2id-sw-identification", engine="sympy+mpmath")
    wb.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    wb.set_description(
        "KSel-2-ID (bean qou-0ms0; audit-only, scope-(a), NO FIT, "
        "nothing wired): literature identification of the balanced "
        "binding-kernel moment family m_k = q^(-k(k-1)/4)[k]_q! against "
        "the classical Stieltjes-Wigert / q-Laguerre indeterminate "
        "families. S1: exact base-p rewrite (Gaussian factor at base "
        "qtilde x Pochhammer factor at base q). S2-S3: SW-proper "
        "(log-normal) moment sequences are log-quadratic, a property "
        "invariant under every affine-in-log map s -> c s^a; the "
        "balanced family is exactly NOT log-quadratic (Delta^2 ln m_k "
        "= ln qtilde + ln((1-p^(k+2))/(1-p^(k+1))), strictly "
        "increasing) => NO-MATCH to SW-proper, scope-(b) with cited "
        "invariant. S4: the SW structure IS present as an exact tensor "
        "factor: balanced = SW(t = 1/qtilde, scaled) (*) Jackson "
        "(determinate, compact support) — the indeterminacy core is "
        "Stieltjes' 1894 log-normal example at base sqrt(q), = the "
        "ksel3 Gaussian. S5: the ONE-SIDED normalizer [k]_q! is "
        "EXACTLY the alpha=0 q-Laguerre (Moak/generalized-SW) moment "
        "family under s -> (p/(1-p)) s (weight functional equation "
        "derivation + quadrature cross-check); the balanced member "
        "sits exactly one SW-Gaussian convolution away — the "
        "bar-symmetric half-dressed point. Nothing here proves or "
        "refutes any conjecture.")
    wb.set_audit_only(
        "docs/audits/2026-08-01-ksel2id-friedrichs-sw-identification.md")

    block_s1_base_p(wb)
    print("S1: base-p rewrite exact (k <= 12).")
    block_s2_sw_reference(wb)
    print("S2: LN moments + affine-in-log closure + classical SW weight "
          "— exact.")
    block_s3_obstruction(wb)
    print("S3: SW-proper NO-MATCH — exact log-quadraticity obstruction; "
          "residuals tabled at both pins.")
    block_s4_sw_factor(wb)
    print("S4: balanced = SW(1/qtilde) (*) Jackson — exact factor "
          "decomposition; Jackson moments < 1e-30.")
    block_s5_q_laguerre(wb)
    print("S5: one-sided = q-Laguerre alpha=0 under s -> (p/(1-p))s — "
          "EXACT; balanced one SW-Gaussian away.")

    wb.add_data("q0_pins", {
        "muon": Q0_MUON_STR, "proton": Q0_PROTON_STR,
        "source": "computations/q-pinning-50-digit.witness.json (muon); "
                  "qou_substrate.constants.Q_50_DIGIT_STR (proton)"})
    wb.save()
    print("\nwitness saved; all assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
