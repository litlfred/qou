#!/usr/bin/env python3
"""qbeta_bar_split_ord17_probe.py — bean 08ds: raise truncation to s^17;
test E(u~) persistence and the h^3*F(u~) discriminant with honest DOF
accounting.

Follow-up to qbeta_even_channel_bar_split_probe.py (bean ai81), which at
ORD = 11 found: E (bar-even part of log R) IS exactly a u~-series (6
over-determining orders, all zero); O/h a u~-series through s^10, failing
only at s^11.  Two questions this probe answers at ORD = 17:

  (A) Does E stay exactly a u~-series through s^17?  (8 rungs vs 17
      constraint orders — over-determination margin 9: a STRONG test.)
  (B) Is the bar-odd sector of the form h*D(u~) + h^3*F(u~)?  Joint exact
      linear solve for (d_k, f_k) with the margin REPORTED — the
      (u~, h^2)-family adds ~2 unknowns per 2 orders, so this test is
      structurally marginal (margin stays O(1) at any order); a "fit"
      verdict here is honest only as consistency-at-margin-M, never as a
      derivation.  (Formalize-first note: asymptotically EVERY bar-even
      series is representable in Q(sqrt3)[[u~, h^2]] — representability
      is not the question; the constrained one-variable-F form is.)

All exact (Q(sqrt3) scalars); scope (a); audit-only; no wiring.

CORRECTION (2026-07-12, follow-up to the merged three-routes PR #3691).
Test (B)'s "margin-1" discriminant was built on the O/h top-order
shift-padding ARTIFACT: G[ORD] (from the old ser_mul(O[1:]+[0],
ser_inv(h[1:]+[0])) idiom) depends on the unknown O[ORD+1] and is garbage
by construction, yet the joint solve used it as one of its ORD constraints
— and it was precisely the single over-determining row (margin = ORD -
unknowns = 1).  This probe now divides through the valuation-aware
core.ser_div (which zeroes + reports the invalid top row) and solves over
the valid range s^1..s^(ORD-1) only.  With the artifact row removed the
(B) system is exactly determined (margin 0) — so ORD 17 has NO
discriminating power for the h^3*F form; the "margin-1 refutation" is moot,
not a refutation.  (A) — E(u~) persistence — is unaffected: E carries no
division, so E[ORD] is a genuine coefficient.  See
qbeta_barodd_d_ladder_ord17_probe.py for the ORD-19 confirmation.
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

import qbeta_ck_sseries_exact_rational as core  # noqa: E402
core.ORD = 17          # raise the truncation BEFORE any series call
ORD = core.ORD
from qbeta_ck_sseries_exact_rational import (  # noqa: E402
    q, simp, ser_add, ser_mul, ser_scale, ser_inv, ser_sqrt,
    ser_log1, ser_cos0, rat_series, load_net_symbolic,
)

mp.mp.dps = 60
HERE = Path(__file__).resolve().parent


def ser_compose(a, phi):
    assert phi[0] == 0
    out = [sp.Integer(0)] * (ORD + 1)
    out[0] = a[ORD]
    for n in range(ORD - 1, -1, -1):
        out = ser_mul(out, phi)
        out[0] = simp(out[0] + a[n])
    return out


def u_adic_match(f, u_ser, kmax):
    e = {}
    model = [sp.Integer(0)] * (ORD + 1)
    upow = [None, list(u_ser)]
    for k in range(2, kmax + 1):
        upow.append(ser_mul(upow[k - 1], u_ser))
    for k in range(1, kmax + 1):
        ek = simp((f[2 * k] - model[2 * k]) / upow[k][2 * k])
        e[k] = ek
        model = ser_add(model, ser_scale(ek, upow[k]))
    resid = {n: simp(f[n] - model[n]) for n in range(1, ORD + 1)}
    return e, resid, model


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(f" 08ds — ORD={ORD} bar-split: E(u~) persistence + h^3 discriminant")
    print("=" * 78)

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
    u_ser = ser_mul(rat_series(q), ser_mul(b_ser, hbar2))   # u~ = q*b*hbar^2
    sqrt_q = ser_sqrt(rat_series(q))
    z_ser = ser_mul(sqrt_q, ser_inv(rat_series(q + 1)))
    h_ser = rat_series(q - 1 / q)
    zm1 = list(z_ser); zm1[0] = simp(zm1[0] - 1)
    alpha = ser_add(ser_scale(sp.Rational(1, 2), ser_mul(zm1, h_ser)),
                    ser_scale(sp.Rational(-1, 2), u_ser))
    R = ser_mul(Qb, ser_inv(ser_mul(QA, ser_cos0(alpha))))
    logR = ser_log1(R)
    print(f"  series built ({time.monotonic()-t0:.0f}s)")

    phi = [sp.Integer(0)] + [sp.Integer(-1) ** n for n in range(1, ORD + 1)]
    logR_bar = ser_compose(logR, phi)
    E = [simp((x + y) / 2) for x, y in zip(logR, logR_bar)]
    O = [simp((x - y) / 2) for x, y in zip(logR, logR_bar)]

    # (A) E in Q(sqrt3)[[u~]] through s^17?
    KMAX = (ORD - 1) // 2
    eE, residE, _ = u_adic_match(E, u_ser, KMAX)
    firstE = next((n for n in range(1, ORD + 1) if sp.simplify(residE[n]) != 0), None)
    marginE = ORD - KMAX  # constraint orders beyond the fitted rungs
    print(f"\n  (A) E rungs e_1..e_{KMAX}: "
          f"{ {k: str(sp.N(x, 10)) for k, x in eE.items()} }")
    print(f"      first nonzero residual: {firstE} "
          f"(over-determination margin {marginE})"
          + ("" if firstE else "  — E IS a u~-series through s^17 ✓"))

    # (B) O/h = D(u~) + h^2*F(u~) — joint exact solve + DOF accounting.
    # Valuation-aware division zeroes + reports the invalid top row; the joint
    # solve below is restricted to the valid orders s^1..s^g_valid_top so it no
    # longer consumes the shift-padding artifact (which was the sole
    # over-determining constraint — see the header correction).
    assert sp.simplify(O[0]) == 0
    G, g_valid_top = core.ser_div(O, h_ser)    # O/h (bar-even)
    h2 = ser_mul(h_ser, h_ser)
    # basis: u~^k (k=1..KD) and h^2*u~^k (k=0..KF)
    KD = (ORD - 1) // 2
    KF = (ORD - 3) // 2
    basis = []
    labels = []
    upow = [ [sp.Integer(1)] + [sp.Integer(0)] * ORD ]
    for k in range(1, max(KD, KF) + 1):
        upow.append(ser_mul(upow[k - 1], u_ser))
    for k in range(1, KD + 1):
        basis.append(upow[k]); labels.append(f"d{k}")
    for k in range(0, KF + 1):
        basis.append(ser_mul(h2, upow[k])); labels.append(f"f{k}")
    syms = sp.symbols(f"c0:{len(basis)}")
    eqs = []
    for n in range(1, g_valid_top + 1):        # valid orders only (drop artifact top)
        eqs.append(sum(syms[i] * basis[i][n] for i in range(len(basis))) - G[n])
    sol = sp.linsolve(eqs, list(syms))
    n_constraints = g_valid_top  # orders 1..g_valid_top (artifact top row excluded)
    n_unknowns = len(basis)
    margin = n_constraints - n_unknowns
    solvable = bool(sol) and len(list(sol)) > 0
    free_params = 0
    coeffs = None
    if solvable:
        vec = list(sol)[0]
        free = sorted(set().union(*[t.free_symbols for t in vec], set()),
                      key=lambda x: x.name)
        free_params = len(free)
        subs0 = {g: 0 for g in free}
        coeffs = {labels[i]: simp(vec[i].subs(subs0)) for i in range(len(basis))}
    print(f"\n  (B) joint solve O/h = D(u~) + h^2 F(u~): "
          f"constraints {n_constraints}, unknowns {n_unknowns}, "
          f"margin {margin}, solvable {solvable}, free params {free_params}")
    if coeffs:
        print(f"      coefficients: { {k_: str(sp.N(x, 8)) for k_, x in coeffs.items()} }")

    two_form_verdict = (
        f"E(u~) holds through s^{ORD} with margin {marginE}"
        if firstE is None else
        f"E(u~) FAILS first at s^{firstE}"
    )
    eff_margin = margin - free_params
    b_verdict = (
        (f"h*D(u~) + h^3*F(u~): after removing the O/h shift-padding artifact "
         f"top row the joint solve is under-determined at ORD {ORD} "
         f"({free_params} free parameters, effective margin {eff_margin}) — so "
         "this order has NO discriminating power for the h^3*F form; the earlier "
         "'margin-1 refutation' rested entirely on the artifact row and is moot, "
         "not a refutation. A genuine (B) test needs ORD high enough that the "
         "valid orders over-determine (u~,h^2).")
        if solvable and eff_margin <= 0 else
        (f"h*D(u~) + h^3*F(u~) CONSISTENT at effective margin {eff_margin} "
         "(honest tier: consistency-at-margin, NOT a derivation)")
        if solvable else
        "h*D(u~) + h^3*F(u~) INCONSISTENT over the valid orders — exact "
        "refutation of the one-variable-F form at this order (scope (a))"
    )
    print(f"\n  VERDICT (A): {two_form_verdict}")
    print(f"  VERDICT (B): {b_verdict}")
    elapsed = time.monotonic() - t0
    print(f"  ({elapsed:.1f}s)")

    wb = WitnessBuilder("qbeta-bar-split-ord17", engine="sympy")
    wb.set_description(
        "08ds: ORD=17 bar-split of the net-route log R — E(u~) persistence "
        "test (margin 9) and the h*D(u~)+h^3*F(u~) discriminant as a joint "
        "exact linear solve with explicit DOF accounting."
    )
    wb.add_data("ORD", ORD)
    wb.add_data("E_rungs_exact", {str(k): str(x) for k, x in eE.items()})
    wb.add_data("E_first_nonzero_residual", firstE)
    wb.add_data("E_margin", marginE)
    wb.add_data("B_valid_top_order", g_valid_top)
    wb.add_data("B_constraints", n_constraints)
    wb.add_data("B_unknowns", n_unknowns)
    wb.add_data("B_margin", margin)
    wb.add_data("B_solvable", solvable)
    wb.add_data("B_free_params", free_params)
    wb.add_data("B_coefficients",
                {k_: str(x) for k_, x in (coeffs or {}).items()})
    wb.add_data("verdict_A", two_form_verdict)
    wb.add_data("verdict_B", b_verdict)
    wb.add_data("scope", "(a); consistency-at-margin tier for (B); no wiring")
    wb.add_assertion("E_u_series_through_ORD", firstE is None, True)
    out = wb.save()
    print(f"  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
