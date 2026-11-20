#!/usr/bin/env python3
"""qbeta_even_channel_bar_split_probe.py — bean ai81: the even-channel
ladder variable, from the exact residual table.

The 9fnm measurement (qbeta_ck_sseries_exact_rational.py, audit
2026-07-03-9fnm-c3even-exact-rational-measurement.md) found the net-route
ladder log R is NOT of the form sum_k log(1 + c_k u^k) — exact residuals at
s^2 (9/8) and all odd orders survive every rung assignment.  Per
conj:binding-qbeta-complex-volume the natural candidates for the missing
structure are a COMPANION BAR-ODD VARIABLE or the zeta4-residue constraint.
This probe tests the companion-variable hypothesis EXACTLY (formalize-first
— structure before any scan):

    Bar involution on s = q-1:  sigma(s) = 1/q - 1 = -s/(1+s).
    Split log R = E + O with E = (logR + logR o sigma)/2 (bar-EVEN part)
    and O = (logR - logR o sigma)/2 (bar-ODD part) — EXACT series
    composition, no numerics.

    HYPOTHESIS (two-variable form):  log R = E(u) + h * D(u), where
    u = b*hbar_q^2 is the bar-even ladder variable and h = q - 1/q is the
    canonical bar-odd companion (h o sigma = -h).  Equivalent tests:
      (a) E lies in Q(sqrt3)[[u]]      (triangular u-adic match, exact
          residuals at every order up to ORD);
      (b) O / h lies in Q(sqrt3)[[u]]  (same test; O/h is bar-even).

If both close, the even channel IS a u-ladder after removing an exact
h-odd component — log R = E(u~) + h*D(u~), u~ = q*u bar-even — and the honest bar-even rungs
are read from E alone (reported, tiered).  If either fails, the exact
failing order + residual is the sharpened constraint for the next
candidate (zeta4-residue route).  All scope (a); audit-only; no wiring.

CORRECTION (2026-07-12, follow-up to the merged three-routes PR #3691).
The original ai81 run reported O/h "failing at order 11".  That was an
O/h top-order shift-padding ARTIFACT, not data: dividing O by h (both
s-valuation 1) via the old ser_mul(O[1:]+[0], ser_inv(h[1:]+[0])) idiom
pads the top with 0, so G[ORD] silently depends on the unknown O[ORD+1]
and is garbage by construction — and the failing order tracked the
truncation top exactly (see qbeta_barodd_d_ladder_ord17_probe.py, which
runs the same object at ORD 19 with all 9 over-determining orders zero).
This probe now divides through the valuation-aware core.ser_div, which
zeroes and reports the invalid top row, and scans failing orders only
over the valid range s^1..s^(ORD-1).  The two-variable form HOLDS.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401
sys.path.insert(0, str(Path(__file__).resolve().parent))
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

import json  # noqa: E402
import sympy as sp  # noqa: E402
import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from qbeta_ck_sseries_exact_rational import (  # noqa: E402
    q, ORD, simp, ser_add, ser_mul, ser_scale, ser_inv, ser_sqrt, ser_div,
    ser_log1, ser_cos0, rat_series, load_net_symbolic,
)

mp.mp.dps = 60
HERE = Path(__file__).resolve().parent


def ser_compose(a, phi):
    """a(phi(s)) for phi with zero constant term — Horner on truncated series."""
    assert phi[0] == 0
    out = [sp.Integer(0)] * (ORD + 1)
    out[0] = a[ORD]
    for n in range(ORD - 1, -1, -1):
        out = ser_mul(out, phi)
        out[0] = simp(out[0] + a[n])
    return out


def u_adic_match(f, u_ser, kmax):
    """Triangular match f = sum_{k>=1} e_k u^k at s^{2k}; return (e, residuals)."""
    e = {}
    model = [sp.Integer(0)] * (ORD + 1)
    upow = [None, list(u_ser)]
    for k in range(2, kmax + 1):
        upow.append(ser_mul(upow[k - 1], u_ser))
    for k in range(1, kmax + 1):
        lead = upow[k][2 * k]
        ek = simp((f[2 * k] - model[2 * k]) / lead)
        e[k] = ek
        model = ser_add(model, ser_scale(ek, upow[k]))
    resid = {n: simp(f[n] - model[n]) for n in range(1, ORD + 1)}
    return e, resid


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" ai81 — bar-split of log R: is log R = E(u~) + h*D(u~), u~ = q*u bar-even?  (exact)")
    print("=" * 78)

    # rebuild the exact logR series (same objects as 9fnm)
    dnet = sp.simplify(load_net_symbolic("neutron") - load_net_symbolic("proton"))
    dnet_reg = sp.cancel(dnet / (q - 1))
    # q₀ from q_parameter (proton pin, AGENTS.md 2026-08-07 directive).
    # Was a direct read of q-pinning-50-digit.witness.json, which is the
    # MUON anchor’s definition and bypasses the manifest entirely.
    q0 = Q_MP
    sgn = int(mp.sign(sp.lambdify(q, dnet, "mpmath")(q0)))
    Qb = rat_series(sp.Integer(sgn) * dnet_reg / q)
    QA = rat_series((2 * q + 1 - q**2) * (q + 1) / (2 * q**3))
    hbar2 = rat_series(((q - 1) / q) ** 2)
    b_ser = ser_mul(ser_sqrt(rat_series(q**4 + q**2 + 1)),
                    ser_inv(rat_series(q**2 + 1)))
    u_raw = ser_mul(b_ser, hbar2)
    # FINDING (exact): u = b*hbar^2 is NOT bar-even — hbar(1/q) = -q*hbar(q),
    # so u o sigma = q^2 * u.  The genuinely bar-even ladder variable is
    # u~ = q*u = q*b*hbar^2 (agrees with u at leading order s^2).
    u_ser = ser_mul(rat_series(q), u_raw)
    sqrt_q = ser_sqrt(rat_series(q))
    z_ser = ser_mul(sqrt_q, ser_inv(rat_series(q + 1)))
    h_ser = rat_series(q - 1 / q)
    zm1 = list(z_ser); zm1[0] = simp(zm1[0] - 1)
    alpha = ser_add(ser_scale(sp.Rational(1, 2), ser_mul(zm1, h_ser)),
                    ser_scale(sp.Rational(-1, 2), u_ser))
    R = ser_mul(Qb, ser_inv(ser_mul(QA, ser_cos0(alpha))))
    logR = ser_log1(R)

    # bar involution sigma(s) = -s/(1+s):  coefficients (-1)^n for n >= 1
    phi = [sp.Integer(0)] + [sp.Integer(-1) ** n for n in range(1, ORD + 1)]

    # sanity: u~ bar-even, h bar-odd, and the u-weight finding — EXACT
    u_bar = ser_compose(u_ser, phi)
    h_bar = ser_compose(h_ser, phi)
    uraw_bar = ser_compose(u_raw, phi)
    q2_uraw = ser_mul(rat_series(q**2), u_raw)
    u_even_ok = all(sp.simplify(x - y) == 0 for x, y in zip(u_bar, u_ser))
    h_odd_ok = all(sp.simplify(x + y) == 0 for x, y in zip(h_bar, h_ser))
    u_weight_ok = all(sp.simplify(x - y) == 0 for x, y in zip(uraw_bar, q2_uraw))
    print(f"  [finding] u o sigma == q^2 * u (u has bar-weight 2)?  {u_weight_ok}")
    print(f"  [sanity] u~ = q*u o sigma == u~ (bar-even)?  {u_even_ok}")
    print(f"  [sanity] h o sigma == -h (bar-odd)?  {h_odd_ok}")
    assert u_even_ok and h_odd_ok and u_weight_ok

    # exact bar split of logR
    logR_bar = ser_compose(logR, phi)
    E = [simp((x + y) / 2) for x, y in zip(logR, logR_bar)]
    O = [simp((x - y) / 2) for x, y in zip(logR, logR_bar)]
    print(f"  E (bar-even part) low orders: s^1:{E[1]}  s^2:{sp.N(E[2],8)}  s^3:{sp.N(E[3],8)}")
    print(f"  O (bar-odd part)  low orders: s^1:{O[1]}  s^2:{sp.N(O[2],8)}  s^3:{sp.N(O[3],8)}")

    # (a) E in Q(sqrt3)[[u]] ?
    KMAX = (ORD - 1) // 2
    eE, residE = u_adic_match(E, u_ser, KMAX)
    firstE = next((n for n in range(1, ORD + 1) if sp.simplify(residE[n]) != 0), None)
    print(f"\n  (a) E = sum e_k u^k: coefficients e_k = "
          f"{ {k: str(sp.N(v_, 10)) for k, v_ in eE.items()} }")
    print(f"      first nonzero residual order: {firstE}"
          + (f"  value {sp.N(residE[firstE], 12)}" if firstE else "  — E IS a u-series ✓"))

    # (b) O/h in Q(sqrt3)[[u]] ?  (h has s-valuation 1)
    assert h_ser[0] == 0 and h_ser[1] != 0
    assert sp.simplify(O[0]) == 0
    # Valuation-aware division: ser_div strips the common s^1, divides, and
    # zeroes + reports the invalid top row (the old shift-padding made G[ORD]
    # depend on the unknown O[ORD+1] — the "order-11 artifact"; see the header
    # correction).  Scan failing orders only over the valid range s^1..s^valid.
    G, g_valid_top = ser_div(O, h_ser)             # O/h, bar-even
    eG, residG = u_adic_match(G, u_ser, KMAX)
    firstG = next((n for n in range(1, g_valid_top + 1)
                   if sp.simplify(residG[n]) != 0), None)
    print(f"\n  (b) O/h = sum d_k u^k: coefficients d_k = "
          f"{ {k: str(sp.N(v_, 10)) for k, v_ in eG.items()} }")
    print(f"      first nonzero residual order (valid s^1..s^{g_valid_top}): {firstG}"
          + (f"  value {sp.N(residG[firstG], 12)}" if firstG
             else f"  — O/h IS a u-series through s^{g_valid_top} ✓"))

    two_var_form = (firstE is None) and (firstG is None)
    verdict = (
        ("TWO-VARIABLE FORM HOLDS (to s^" + str(ORD) + ", exact): "
         "log R = E(u~) + h*D(u~), with u~ = q*u the bar-even variable (u itself has bar-weight 2) and h = q - 1/q the companion "
         "bar-odd variable — the even channel IS a u-series after exact "
         "removal of the h-odd component; the honest bar-even ladder data "
         "are the e_k (E) with the d_k (D) as the odd-companion series. "
         "Scope (a): established to truncation order, on the net route.")
        if two_var_form else
        (f"TWO-VARIABLE FORM FAILS exactly at order "
         f"{{'E': {firstE}, 'O/h': {firstG}}} — the h-companion hypothesis "
         "as-is does not absorb the residual; the failing exact residuals "
         "sharpen the constraint for the next candidate (zeta4-residue "
         "route). Scope (a).")
    )
    print(f"\n  VERDICT: {verdict}")
    elapsed = time.monotonic() - t0
    print(f"  ({elapsed:.1f}s)")

    wb = WitnessBuilder("qbeta-even-channel-bar-split", engine="sympy")
    wb.set_description(
        "ai81: exact bar-involution split of the net-route log R "
        "(sigma: s -> -s/(1+s)); tests the two-variable hypothesis "
        "log R = E(u~) + h*D(u~), u~ = q*u bar-even (h = q - 1/q companion bar-odd variable) "
        "by exact u-adic matching of the bar-even part and of (bar-odd)/h."
    )
    wb.add_data("sigma", "s -> -s/(1+s) (q -> 1/q)")
    wb.add_data("u_weight_finding", "u o sigma = q^2 u exactly; bar-even variable is u~ = q*u")
    wb.add_data("u_tilde_bar_even_exact", bool(u_even_ok))
    wb.add_data("h_bar_odd_exact", bool(h_odd_ok))
    wb.add_data("E_u_coefficients_exact", {str(k): str(v_) for k, v_ in eE.items()})
    wb.add_data("E_first_nonzero_residual_order", firstE)
    wb.add_data("E_residuals_nonzero",
                {str(n): str(sp.N(v_, 15)) for n, v_ in residE.items()
                 if sp.simplify(v_) != 0})
    wb.add_data("D_u_coefficients_exact", {str(k): str(v_) for k, v_ in eG.items()})
    wb.add_data("OoverH_first_nonzero_residual_order", firstG)
    wb.add_data("OoverH_valid_top_order", g_valid_top)
    wb.add_data("OoverH_residuals_nonzero",
                {str(n): str(sp.N(v_, 15)) for n, v_ in residG.items()
                 if n <= g_valid_top and sp.simplify(v_) != 0})
    wb.add_data("two_variable_form_holds_to_ORD", bool(two_var_form))
    wb.add_data("verdict", verdict)
    wb.add_data("scope", "(a) — truncation order ORD, net route; no wiring")
    wb.add_assertion("bar_involution_sanity", bool(u_even_ok and h_odd_ok), True)
    out = wb.save()
    print(f"  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
