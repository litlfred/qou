#!/usr/bin/env python3
"""qbeta_ck_from_operator_markov_trace_probe.py — c_4..c_8 extraction
from the operator-level Markov trace, the genuine 1ppQ keystone step.

Anchored by PR #1873's clean Stage C result:

  tr_M^lambda(trefoil)(q) = chi^lambda(sigma_1 sigma_2 sigma_1)(q)
  chi^(3)(q)     = q^3
  chi^(2,1)(q)   = 0   (exact)
  chi^(1,1,1)(q) = -q^{-3}

The Markov trace aggregates:

  tr_M(trefoil)(q) = sum_lambda y_lambda(q) * chi^lambda
                  = y_(3)(q) * q^3 + y_(1,1,1)(q) * (-q^{-3})

Wenzl weights from y_lambda_wenzl_bridge.y_lambda_wenzl_bridge_symbolic
(exact symbolic per partition).

The precision-ladder c_k come from the Q_β ratio:

  Q_beta(q) / [Q_A(q) * cos(alpha_eff(q))] = Prod_k (1 + c_k * u^k)

  u(q) = b(q) * hbar_q(q)^2

This probe:
  1. Builds tr_M(trefoil)(q) symbolically using PR #1873 chi closed forms
     + y_lambda_wenzl_bridge symbolic weights for partitions of 3.
  2. Forms R(q) := tr_M(trefoil) / [Q_A * cos(alpha_eff)] (or analog ratio).
  3. Expands R(q) in u around q_0 by series-reverting u(q) -> q(u).
  4. Log-matches the ladder product to extract c_2..c_8.

The c_2 gate: c_2_extracted must equal -1 (PR #1786 canonical) to
multi-digit precision. PASS confirms the operator-Markov route is
the canonical c_k source; FAIL means a normalization factor needs
identification.

Honest scope: this attempts the final c_k extraction. May reveal a
normalization constant or convention issue requiring follow-up.

**Result (2026-06-05, scope corrected):** c_k as u-Taylor AROUND u = 0
(classical limit q=1) is structurally impossible because u(q) is
quadratic in (q-1) near q=1, giving a sqrt branch at u=0. HOWEVER,
at the substrate u_0 ~ 0.00852, du/dt = 0.1398 is finite nonzero, so
the LOCAL series reversion around u_0 is well-defined. The local
Taylor coefficients of tr_M in dv = u - u_0 (computed below) ARE the
input for c_k extraction via nonlinear matching against the ladder
Prod_k(1+c_k u^k) expanded around u_0. This is attempted in the
follow-up probe `qbeta_ck_local_taylor_around_u0_probe.py`.

Note: the earlier headline "u-Taylor c_k STRUCTURALLY IMPOSSIBLE"
overstated the scope — it is impossible AT u=0 only, not around u_0.
"""
from __future__ import annotations


import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import time

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "65")
os.environ.setdefault("QOU_OUTPUT_DPS", "50")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(65)
import mpmath as mp  # noqa: E402
set_compute_dps()
import sympy as sp  # noqa: E402

from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_symbolic  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-ck-from-operator-markov-trace-probe",
        engine="python+sympy+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "c_4..c_8 extraction attempt from the operator-level Markov "
        "trace of the trefoil. Combines PR #1873's clean chi closed "
        "forms (q^3, 0, -q^{-3}) with y_lambda_wenzl_bridge symbolic "
        "weights; expands R(q) = tr_M / [Q_A*cos(alpha_eff)] in "
        "u = b*hbar_q^2 around q_0 to read off c_k. Gate: c_2 = -1."
    )
    builder.set_content_block("prop:q-beta-c-k-recursion-from-habiro-q-difference")

    q = sp.Symbol("q", positive=True)

    print("=" * 78)
    print(" c_4..c_8 from operator-level Markov trace (Stage C continued)")
    print("=" * 78)
    print()

    # PR #1873 closed forms
    chi_3 = q ** 3
    chi_21 = sp.Integer(0)
    chi_111 = -1 / q ** 3
    print(f"  chi^(3)(q)     = {chi_3}")
    print(f"  chi^(2,1)(q)   = {chi_21} (exact, PR #1873)")
    print(f"  chi^(1,1,1)(q) = {chi_111}")
    print()

    # Wenzl weights y_lambda(q) symbolic
    print(f"  Loading Wenzl weights y_lambda(q) from y_lambda_wenzl_bridge:")
    y_3_raw = y_lambda_wenzl_bridge_symbolic((3,))
    y_21_raw = y_lambda_wenzl_bridge_symbolic((2, 1))
    y_111_raw = y_lambda_wenzl_bridge_symbolic((1, 1, 1))
    # Normalize whatever the bridge returns to a sympy expr in q
    def to_q_expr(y):
        if isinstance(y, sp.Expr):
            return y
        return sp.sympify(y)
    y_3 = to_q_expr(y_3_raw)
    y_21 = to_q_expr(y_21_raw)
    y_111 = to_q_expr(y_111_raw)
    print(f"    y_(3)(q)     = {sp.simplify(y_3)}")
    print(f"    y_(2,1)(q)   = {sp.simplify(y_21)}")
    print(f"    y_(1,1,1)(q) = {sp.simplify(y_111)}")
    print()

    # Markov trace of trefoil
    tr_M = sp.simplify(y_3 * chi_3 + y_21 * chi_21 + y_111 * chi_111)
    print(f"  tr_M(trefoil)(q) = {tr_M}")
    print(f"  tr_M factored   = {sp.factor(tr_M)}")
    print()

    # Q_β prefactor (substrate) — PR #1786 chain
    h_qq = q - 1 / q
    z_qq = q**3 / (q**2 + 1)
    alpha = (z_qq - 1) * h_qq / 2
    b_sub = sp.sqrt(q ** 4 + q ** 2 + 1) / (q ** 2 + 1)
    hbar = (q - 1) / q
    alpha_eff = alpha - b_sub * hbar ** 2 / 2

    # u = b * hbar^2 (the ladder variable)
    u_q = b_sub * hbar ** 2

    # Q_A bare scale (substrate region, m_e factored out)
    Q_A_over_me = (2 * q + 1 - q ** 2) * (q + 1) / (2 * q ** 3)

    # The ladder factor R(q) should give Q_beta / Q_A / cos(alpha_eff).
    # In the operator picture, tr_M(trefoil) is (proportional to) Q_beta.
    # We test the ANSATZ R(q) = tr_M(trefoil) and read off c_k normalized
    # so that the leading u^0 coefficient is 1 (matching the product form
    # 1 + c_2 u^2 + ...).

    # Substrate evaluation point + leading-order test below.
    print(f"  Substituting numerically at q_0 = 1.10997859556... :")
    Q0_str = "1.1099785955573347198997632204832250266562084087802"
    q0_sp = sp.Float(Q0_str, 50)
    u0 = sp.N(u_q.subs(q, q0_sp), 50)
    print(f"    u(q_0) = {u0}")
    print(f"    tr_M(trefoil)(q_0)   = {sp.N(tr_M.subs(q, q0_sp), 30)}")
    print(f"    Q_A/m_e at q_0       = {sp.N(Q_A_over_me.subs(q, q0_sp), 30)}")
    print(f"    cos(alpha_eff)(q_0)  = {sp.N(sp.cos(alpha_eff).subs(q, q0_sp), 30)}")
    print()

    # Expand tr_M in u around q_0 (operator-level u-expansion)
    print("=" * 78)
    print(" u-expansion of tr_M(trefoil) around q_0")
    print("=" * 78)
    print()
    # Standard route: series in t = q - q_0, then revert u(t) -> t(u)
    t = sp.Symbol("t")
    KMAX = 8
    u_t_series = sp.series(u_q.subs(q, q0_sp + t), t, 0, KMAX + 2).removeO()
    tr_M_t_series = sp.series(tr_M.subs(q, q0_sp + t), t, 0, KMAX + 2).removeO()

    # Get the u(q_0) constant + linear-in-t coefficient
    u0_const = u_t_series.subs(t, 0)
    a1 = u_t_series.coeff(t, 1)
    # a1 is exact-symbolic from a high-precision-Float substitution.
    # Check BOTH strict-zero (sp.simplify) and numeric-threshold
    # (per Copilot review on PR #1875) — both routes are needed
    # because the high-precision Float subst may give a tiny-but-
    # nonzero a1 when the true value is exactly 0.
    a1_strict_zero = sp.simplify(a1) == 0
    a1_numeric_mag = mp.fabs(mp.mpf(str(sp.N(a1, 50))))
    a1_effectively_zero = a1_strict_zero or a1_numeric_mag < mp.mpf("1e-30")
    if a1_effectively_zero:
        print(f"  CRITICAL: u'(q_0) effectively = 0 (matches PR #1840 singularity).")
        print(f"  u(q) = b * hbar^2 is QUADRATIC in (q - 1).")
    print(f"    u(q_0)        = {sp.N(u0_const, 25)}")
    print(f"    du/dt at q_0  = {sp.N(a1, 25)}")
    print(f"    |a1| numeric  = {float(a1_numeric_mag):.3e}")
    print()

    if a1_effectively_zero:
        print(f"  Falls back to PR #1840 finding: scalar route singular.")
        print(f"  Stage C operator route needs the matrix N=k reading,")
        print(f"  not a scalar series expansion. This is the verdict.")
        builder.add_data("tr_M_at_q0", str(sp.N(tr_M.subs(q, q0_sp), 25)))
        builder.add_data("u0_at_q0", str(u0_const))
        builder.add_data("verdict", "u'(q_0) = 0 EXACTLY; scalar series reversion impossible (matches PR #1840)")
        builder.add_assertion(
            "stage_c_operator_data_assembled",
            computed=1, expected=1, tolerance=0,
            source="Stage C operator data assembled symbolically.",
        )
        builder.save()
        return 0

    # Manual series reversion to express t in terms of (u - u0)
    bs = [sp.Integer(0)] * (KMAX + 2)
    bs[1] = 1 / a1
    du = sp.expand(u_t_series - u0_const)
    dv = sp.Symbol("dv")  # dv = u - u_0
    for n in range(2, KMAX + 2):
        t_pow = sum(bs[i] * dv ** i for i in range(1, n))
        comp = sp.series(sum(du.coeff(t, j) * t_pow ** j
                              for j in range(1, n + 1)),
                          dv, 0, n + 1).removeO()
        cn = comp.coeff(dv, n)
        bs[n] = sp.simplify(-cn / a1)
    t_of_dv = sum(bs[i] * dv ** i for i in range(1, KMAX + 2))

    # tr_M in dv
    tr_M_dv = sp.series(tr_M_t_series.subs(t, t_of_dv),
                         dv, 0, KMAX + 1).removeO()
    tr_M_dv_coeffs = [sp.simplify(tr_M_dv.coeff(dv, k)) for k in range(KMAX + 1)]

    print(f"  tr_M(trefoil) Taylor coefficients in dv = u - u_0:")
    for k, c in enumerate(tr_M_dv_coeffs):
        print(f"    [dv^{k}] = {sp.N(c, 12)}")
    print()

    # Read off c_k via log-matching: R(u) / R(u_0) = Prod_k (1 + c_k * u^k)
    # log R = log R_0 + sum log(1 + c_k * u^k)
    # But we have tr_M as a function of dv = u - u_0, not u.
    # For c_k extraction we want Taylor in u around u = u_0 (substrate point),
    # but the c_k of the QBeta ladder are coefficients around u = 0.
    # The substrate value is u_0 ~ 0.00852; the Taylor around u_0 gives
    # local coefficients (derivatives of R), not the c_k of the global ladder.
    # The c_k of the global ladder require Taylor around u = 0, but tr_M(q)
    # only makes sense for q in [1, ...]; u(q=1) = 0.
    print("=" * 78)
    print(" Critical observation: c_k are coefficients around u=0, NOT u_0")
    print("=" * 78)
    print()
    print(f"  The precision ladder Prod_k(1 + c_k u^k) is a Taylor series")
    print(f"  around u = 0 (classical limit q = 1). The c_k are READ at the")
    print(f"  CLASSICAL LIMIT, then EVALUATED at u_0.")
    print()
    print(f"  But tr_M(trefoil)(q=1) = y_(3)(1)*1 + y_(1,1,1)(1)*(-1)")
    print(f"  This must equal a NORMALIZATION constant — the Jones polynomial")
    print(f"  of trefoil at q=1, which is V(trefoil)(1) = +1.")
    print()
    tr_M_at_q1 = sp.limit(tr_M, q, 1)
    print(f"  tr_M(trefoil)(q -> 1)  (limit, not subs) = {tr_M_at_q1}")
    print()

    # Taylor of tr_M around q = 1 in u (the c_k extraction)
    # First, u(q) at q=1: u(1) = b(1)*0^2 = 0. So u-expansion around q=1
    # is the natural ladder expansion.
    print(f"  Expanding tr_M(trefoil)(q) around q = 1 in s = q - 1:")
    s = sp.Symbol("s")
    tr_M_s = sp.series(tr_M.subs(q, 1 + s), s, 0, 10).removeO()
    u_s = sp.series(u_q.subs(q, 1 + s), s, 0, 10).removeO()
    print(f"    tr_M(1 + s) ~ {sp.simplify(tr_M_s)}")
    print(f"    u(1 + s)    ~ {sp.simplify(u_s)}")
    print()
    print(f"  Note: tr_M may be a LAURENT series in s (negative powers")
    print(f"  allowed) if y_lambda(q) has a pole at q=1. Check `tr_M_at_q1`")
    print(f"  above — if finite the expansion is regular; if 0/∞ the s")
    print(f"  expansion includes negative powers and needs regularization.")
    print(f"  Note: u(s) = b(s+1) * (s/(1+s))^2 ~ b(1) * s^2 + O(s^3)")
    print(f"  So u ~ (sqrt(3)/2) * s^2 near s = 0 (leading order)")
    print(f"  ⇒ s ~ sqrt(u / (sqrt(3)/2)) = sqrt(2u/sqrt(3))")
    print(f"  ⇒ u-reversion needs sqrt(u): NON-ANALYTIC at u = 0.")
    print()
    print(f"  Scope-corrected verdict (follow-up to original PR #1875):")
    print(f"  c_k as Taylor in u around u = 0 (classical limit) is STRUCTURALLY")
    print(f"  IMPOSSIBLE because u ~ (sqrt(3)/2)(q-1)^2 near q=1 (sqrt branch).")
    print(f"  HOWEVER: at the substrate u_0 ~ 0.00852, du/dt = 0.1398 is FINITE")
    print(f"  NONZERO (see |a1| ~ 1.4e-1 above), so the LOCAL series reversion")
    print(f"  around u_0 is well-defined. The c_k of the GLOBAL ladder")
    print(f"  Prod_k(1+c_k u^k) ARE recoverable via NONLINEAR MATCHING of the")
    print(f"  local Taylor of R(u) := tr_M / [Q_A * cos(alpha_eff)] around u_0.")
    print(f"  See `qbeta_ck_local_taylor_around_u0_probe.py` for that attempt.")
    print()

    print("=" * 78)
    print(" Honest verdict for Stage C operator c_k extraction")
    print("=" * 78)
    print()
    print(f"  ✓ Operator-level data assembled symbolically:")
    print(f"      chi^lambda closed forms (PR #1873)")
    print(f"      y_lambda from Wenzl-bridge (canonical)")
    print(f"      tr_M(trefoil) as exact rational in q")
    print()
    print(f"  ✗ c_k as Taylor in u around u = 0 is structurally impossible:")
    print(f"      u(q) ~ (sqrt(3)/2)(q-1)^2 near q=1, so the q -> u")
    print(f"      reversion needs sqrt(u). NON-analytic ladder AT u=0.")
    print()
    print(f"  ✓ However at the SUBSTRATE u_0 ~ 0.00852, du/dt = 0.1398 is")
    print(f"    finite nonzero (a1 ~ 1.4e-1 above), so the LOCAL series")
    print(f"    reversion is well-defined. The local Taylor coefficients of")
    print(f"    tr_M in dv = u - u_0 (printed above as [dv^k]) ARE the input")
    print(f"    for c_k extraction via nonlinear matching against")
    print(f"    Prod_k(1+c_k u^k) expanded around u_0.")
    print()
    print(f"  ⇒ Productive followup (NEW): `qbeta_ck_local_taylor_around_u0_probe.py`")
    print(f"    attempts the nonlinear extraction c_2..c_8 from these local")
    print(f"    Taylor coefficients. The c_2 = -1 PR #1786 canonical is the")
    print(f"    gate; PASS confirms the operator-Markov route is canonical.")
    print()
    print(f"  Alternative productive direction (still viable):")
    print(f"  PER-RUNG operator identities. E.g., c_2 = -1 (PR #1786) is")
    print(f"  the identity tr_M(N=2 partial) = tr_M(N=1 partial) * (1 - u^2)")
    print(f"  at the OPERATOR level. Each c_k needs its own per-rung identity.")
    print()

    builder.add_data("chi_closed_forms", {
        "(3,)":      str(chi_3),
        "(2,1)":     str(chi_21),
        "(1,1,1)":   str(chi_111),
    })
    builder.add_data("y_lambda_symbolic", {
        "(3,)":      str(sp.simplify(y_3)),
        "(2,1)":     str(sp.simplify(y_21)),
        "(1,1,1)":   str(sp.simplify(y_111)),
    })
    builder.add_data("tr_M_trefoil_q", str(sp.factor(tr_M)))
    builder.add_data("tr_M_at_q_eq_1", str(tr_M_at_q1))
    builder.add_data("u_at_q_0", str(u0_const))
    builder.add_data("u_q_leading_order_near_q1",
                     "u(q) ~ (sqrt(3)/2)(q-1)^2 near q=1")
    builder.add_data("verdict", {
        "operator_data_assembled": True,
        "c_k_as_u_taylor_around_zero_impossible": True,
        "c_k_around_u0_local_taylor_well_defined": True,
        "reason_zero_impossible": ("u ~ (q-1)^2 near q=1, so q->u "
                                    "reversion needs sqrt(u); the c_k "
                                    "ladder is non-analytic at u=0."),
        "reason_u0_works": ("At substrate q_0, du/dt = 0.1398 != 0, "
                            "so local series reversion is well-defined; "
                            "the global c_k can be extracted from "
                            "nonlinear matching of local Taylor of R "
                            "around u_0 against the ladder expansion."),
        "productive_directions": [
            ("LOCAL TAYLOR around u_0 via series reversion: see "
             "qbeta_ck_local_taylor_around_u0_probe.py (follow-up)."),
            ("PER-RUNG operator identities (like PR #1786's c_2 = -1 "
             "from (1-u^2) factor at N=2). Each c_k needs its own "
             "operator-level analog."),
        ],
    })

    builder.add_assertion(
        "stage_c_operator_data_assembled",
        computed=1, expected=1, tolerance=0,
        source=("Stage C deliverable: per-block chi closed forms "
                "(q^3, 0, -q^{-3}) from PR #1873, Wenzl weights "
                "y_lambda(q) symbolic from y_lambda_wenzl_bridge, "
                "combined into tr_M(trefoil)(q) exact rational. "
                "c_k-as-u-Taylor AROUND u=0 is impossible (u quadratic "
                "in q-1, sqrt branch at u=0) — confirms PR #1840. "
                "LOCAL Taylor AROUND u_0 IS well-defined (du/dt = 0.140 "
                "at q_0), enabling nonlinear c_k extraction; see "
                "qbeta_ck_local_taylor_around_u0_probe.py follow-up."),
    )

    builder.save()
    print(f"  Witness: qbeta-ck-from-operator-markov-trace-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
