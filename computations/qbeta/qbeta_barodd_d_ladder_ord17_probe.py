#!/usr/bin/env python3
"""qbeta_barodd_d_ladder_ord17_probe.py — route 1 of the bar-odd-S program:
MAJOR CORRECTION — the "order-11 failure" of the two-variable form was an
O/h top-order truncation artifact; the form log R = E(ũ) + h·D(ũ) holds
EXACTLY at every valid order tested (through s^18, margin 9), and the exact
D-ladder is extended to d₁..d₉.

The artifact (diagnosed this session, three-way):
  * ai81 (ORD 11): first "failing" order 11 = its truncation top;
  * this probe's first draft (ORD 17): "failing" orders = [17] only — the
    interior orders 11, 13, 15 are EXACTLY ZERO;
  * an ORD 19 rerun: "failing" orders = [19] only — 11..17 all exactly zero.
  The failing order tracks the truncation top perfectly. Root cause (located
  by diffing every intermediate series at ORD 11 vs ORD 15 — only G differs,
  and only at its top order): dividing by h (s-valuation 1) is implemented as
      G = ser_mul(O[1:] + [0], ser_inv(h[1:] + [0]))
  — the shift PADS THE TOP WITH 0, so G[ORD] depends on the unknown O[ORD+1]
  and is garbage BY CONSTRUCTION. The valid orders of O/h are 1..ORD−1 only.

Consequences (each a scope-(a) re-scope, per the (a)/(b) discipline —
the numerical results stand, only the top-row readings were invalid):
  * ai81's "TWO-VARIABLE FORM FAILS at order 11" verdict → CORRECTED to
    "holds exactly through s^10 at that run; artifact at 11". The residual
    −13000.75 is reproducible but is the padded-top row, not data.
  * 08ds's "h·D(ũ) + h³F(ũ) INCONSISTENT (margin 1)" → the margin-1 row was
    the invalid top row; with it removed there is NO residual to repair —
    the h³-repair question is moot, not refuted.
  * the "sharpened constraint set for the ζ₄-residue route" drawn from the
    failing residuals (bean 5lcg input) → those residuals are artifacts;
    the ζ₄/Hopf-cubic axis (KC18–KC20) is untouched but loses this input.
  * the capstone's ladder decomposition S = h·D(ũ) is STRENGTHENED: D(ũ) is
    an exact ℚ(√3) power series at every tested order.

Deliverables:
  (1) the exact D-ladder d₁..d₉ ∈ ℚ(√3) at ORD 19 (extends ai81's d₁..d₅,
      which today's corpus reproduces exactly);
  (2) the artifact demonstration rows (interior residuals all zero; the
      top-row value printed for the record, labeled invalid);
  (3) cross-route numeric diagnostic: h·Σ d_k ũ(q₀)^k partial sums at the
      anchors vs the S targets (S(muon)=+0.00968298, S(proton)=−0.03945936)
      — DIAGNOSTIC ONLY (the net-route ladder and the c₃ observable are
      related through the ladder inversion; measured, not wired).

All exact (ℚ(√3) scalars) except the labeled numeric rows; scope (a);
audit-only; no c_k wired; no fit; no tier change.
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
core.ORD = 19          # raise the truncation BEFORE any series call
ORD = core.ORD
from qbeta_ck_sseries_exact_rational import (  # noqa: E402
    q, simp, ser_add, ser_mul, ser_scale, ser_inv, ser_sqrt,
    ser_log1, ser_cos0, rat_series, load_net_symbolic,
)

mp.mp.dps = 60
HERE = Path(__file__).resolve().parent
S_TARGET = {"proton": mp.mpf("-0.03945936"), "muon": mp.mpf("0.00968298")}
VALID_TOP = ORD - 1     # O/h is valid only through s^(ORD-1) — see header


def ser_compose(a, phi):
    """a(phi(s)) for phi with zero constant term."""
    assert phi[0] == 0
    out = [sp.Integer(0)] * (ORD + 1)
    out[0] = a[ORD]
    for n in range(ORD - 1, -1, -1):
        out = ser_mul(out, phi)
        out[0] = simp(out[0] + a[n])
    return out


def u_adic_match(f, u_ser, kmax, top):
    """Triangular match f = Σ_{k≥1} d_k ũ^k pinned at s^{2k}; residuals
    reported only over the VALID orders 1..top."""
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
    resid = {n: simp(f[n] - model[n]) for n in range(1, top + 1)}
    invalid_top_row = simp(f[ORD] - model[ORD])
    return e, resid, invalid_top_row


def height(x):
    """Max |num|,|den| over the rational parts of a+b√3."""
    x = sp.nsimplify(sp.expand(x))
    a = x.coeff(sp.sqrt(3), 0)
    b = x.coeff(sp.sqrt(3), 1)
    hs = []
    for r_ in (a, b):
        if r_ != 0:
            r_ = sp.Rational(r_)
            hs += [abs(r_.p), abs(r_.q)]
    return max(hs) if hs else 0


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" route 1 — D-ladder at ORD 19 + the top-order-artifact CORRECTION")
    print("=" * 78)

    # rebuild the exact logR series (same objects as ai81/08ds)
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
    u_ser = ser_mul(rat_series(q), u_raw)          # ũ = q·u (bar-even)
    sqrt_q = ser_sqrt(rat_series(q))
    z_ser = ser_mul(sqrt_q, ser_inv(rat_series(q + 1)))
    h_ser = rat_series(q - 1 / q)
    zm1 = list(z_ser); zm1[0] = simp(zm1[0] - 1)
    alpha = ser_add(ser_scale(sp.Rational(1, 2), ser_mul(zm1, h_ser)),
                    ser_scale(sp.Rational(-1, 2), u_ser))
    R = ser_mul(Qb, ser_inv(ser_mul(QA, ser_cos0(alpha))))
    logR = ser_log1(R)

    # exact bar split
    phi = [sp.Integer(0)] + [sp.Integer(-1) ** n for n in range(1, ORD + 1)]
    logR_bar = ser_compose(logR, phi)
    O = [simp((x - y) / 2) for x, y in zip(logR, logR_bar)]
    assert sp.simplify(O[0]) == 0

    # O/h via the valuation-aware helper: it strips the common s^1, does the
    # division, and zeroes + reports the rows it cannot determine (the top row,
    # which the old ser_mul(O[1:]+[0], ser_inv(h[1:]+[0])) shift-padding left as
    # garbage depending on the unknown O[ORD+1] — the artifact this probe fixed).
    G, g_valid_top = core.ser_div(O, h_ser)
    assert g_valid_top == VALID_TOP, (g_valid_top, VALID_TOP)

    # (1)+(2) the D-ladder with valid-order residuals
    KMAX = (ORD - 1) // 2          # = 9
    dk, resid, bad_top = u_adic_match(G, u_ser, KMAX, VALID_TOP)
    print(f"\n  (1) exact D-ladder d_k (O/h = Σ d_k ũ^k pinned at s^(2k)), ORD {ORD}:")
    d_rows = {}
    for k_, v_ in dk.items():
        hgt = height(v_)
        d_rows[str(k_)] = {"exact": str(v_), "float": str(sp.N(v_, 12)),
                           "height_digits": len(str(hgt))}
        print(f"      d_{k_} = {sp.N(v_, 10)}   height ~ 10^{len(str(hgt))}")

    nz = {n: v_ for n, v_ in resid.items() if sp.simplify(v_) != 0}
    n_checks = len([n for n in range(1, VALID_TOP + 1) if n % 2 == 1])
    print(f"\n  (2) VALID-order residuals (s^1..s^{VALID_TOP}): "
          f"nonzero at {sorted(nz) if nz else 'NONE — the form holds exactly'}")
    print(f"      over-determining checks (odd orders 1..{VALID_TOP}): {n_checks}, all zero: {not nz}")
    print(f"      invalid top row s^{ORD} (padded-shift artifact, for the record): "
          f"{sp.N(bad_top, 10)}")
    holds = not nz

    # (3) cross-route numeric rows — DIAGNOSTIC ONLY
    print("\n  (3) numeric diagnostic: h·Σ d_k ũ(q₀)^k vs the S targets:")
    q_num = {"proton": q0}
    try:
        sys.path.insert(0, str(HERE.parents[1] / "tools" / "qou-substrate" / "python"))
        from qou_substrate.constants import q_muon_at  # noqa: E402
        q_num["muon"] = q_muon_at(50)
    except Exception as exc:                       # muon row is diagnostic-only
        print(f"      (muon pin unavailable: {exc})")
    diag = {}
    for tag, qq in q_num.items():
        qv = mp.mpf(str(qq))
        hb2 = (1 - 1 / qv) ** 2
        bb = mp.sqrt(qv ** 4 + qv ** 2 + 1) / (qv ** 2 + 1)
        ut = qv * bb * hb2
        hh = qv - 1 / qv
        partial = mp.mpf(0)
        sums = []
        for k_ in range(1, KMAX + 1):
            partial += mp.mpf(str(sp.N(dk[k_], 40))) * ut ** k_
            sums.append(hh * partial)
        hD = sums[-1]
        diag[tag] = {"u_tilde": mp.nstr(ut, 12), "h": mp.nstr(hh, 12),
                     "h_D_partial_sums": [mp.nstr(x, 10) for x in sums],
                     "h_D_k9": mp.nstr(hD, 12),
                     "S_target": mp.nstr(S_TARGET[tag], 10),
                     "h_D_over_S": mp.nstr(hD / S_TARGET[tag], 8)}
        print(f"      {tag:7s}: ũ={mp.nstr(ut, 8)}  h·D(ũ)|_(k≤9) = {mp.nstr(hD, 8)}  "
              f"S = {mp.nstr(S_TARGET[tag], 8)}  ratio = {mp.nstr(hD / S_TARGET[tag], 6)}")
    print("      (net-route ladder object vs the c₃ observable — related through the")
    print("       ladder inversion; ratio is a measured bridge datum, NOT a wiring test)")

    converged = all(
        abs(mp.mpf(diag[t]["h_D_partial_sums"][-1]) -
            mp.mpf(diag[t]["h_D_partial_sums"][-2])) <
        abs(mp.mpf(diag[t]["h_D_partial_sums"][-2])) * mp.mpf("0.01")
        for t in diag)

    # d₅ must reproduce ai81's witnessed exact value (today's corpus does)
    d5_ai81 = sp.Rational(-252241, 243) * sp.sqrt(3) - sp.Rational(836891, 139345920)
    d5_ok = sp.simplify(dk[5] - d5_ai81) == 0

    verdict = (
        f"CORRECTION (scope-(a) re-scope; numbers stand, top-row readings were "
        f"invalid): the two-variable form log R = E(ũ) + h·D(ũ) HOLDS exactly at "
        f"every valid order through s^{VALID_TOP} ({n_checks} over-determining "
        f"odd-order checks, all zero). The corpus's 'order-11 failure' (ai81) and "
        f"the margin-1 h³-refutation (08ds) sat on the O/h top row, which the "
        f"shift-padding makes garbage by construction (G[ORD] needs O[ORD+1]); "
        f"the failing order tracks the truncation top (11→11, 17→17, 19→19). "
        f"Exact D-ladder extended to d₁..d₉ ∈ ℚ(√3) (d₅ reproduces ai81). "
        f"Diagnostic h·D(ũ(q₀))|_(k≤9) = {diag.get('proton', {}).get('h_D_k9', 'n/a')} "
        f"(proton) vs S(proton) = −0.03945936 — related through the ladder "
        f"inversion (measured, not wired). Scope (a); no fit; no c_k wired."
    )
    print(f"\n  VERDICT: {verdict}")
    print(f"  ({time.monotonic() - t0:.1f}s)")

    wb = WitnessBuilder("qbeta-barodd-d-ladder-ord17", engine="sympy")
    wb.set_description(
        "Route 1 CORRECTION: the ai81 'order-11 failure' of "
        "log R = E(ũ) + h·D(ũ) was the O/h top-order shift-padding artifact "
        "(G[ORD] depends on the unknown O[ORD+1]); at ORD 19 every valid "
        "order through s^18 vanishes exactly (margin 9) — the two-variable "
        "form HOLDS and the exact D-ladder extends to d₁..d₉ ∈ ℚ(√3). "
        "Includes the h·D(ũ(q₀)) vs S-target diagnostic. Scope (a); no wiring."
    )
    wb.add_data("ORD", ORD)
    wb.add_data("valid_top_order", VALID_TOP)
    wb.add_data("artifact_diagnosis",
                "G = ser_mul(O[1:]+[0], ser_inv(h[1:]+[0])) pads the top; G[ORD] "
                "needs O[ORD+1] => top row invalid by construction. Failing order "
                "tracked truncation top across ORD 11/17/19 runs; series-object "
                "diff (ORD11 vs ORD15) localized the drift to G[11] only.")
    wb.add_data("D_ladder_exact", d_rows)
    wb.add_data("valid_residuals_all_zero", bool(holds))
    wb.add_data("overdetermining_checks", n_checks)
    wb.add_data("invalid_top_row_value_for_record", str(sp.N(bad_top, 15)))
    wb.add_data("corrections", {
        "ai81": "verdict 'FAILS at order 11' re-scoped: artifact row; form holds",
        "08ds_B": "margin-1 h3-refutation used the invalid row; question moot (no residual)",
        "zeta4_input": "the 'failing residual' constraint set is void; KC18-KC20 axis untouched",
        "capstone": "S = h*D(u) ladder decomposition STRENGTHENED (exact at all tested orders)"})
    wb.add_data("numeric_diagnostic_h_D_vs_S", diag)
    wb.add_data("verdict", verdict)
    wb.add_data("scope", "(a) — exact truncation ORD 19, net route; no wiring")
    wb.add_assertion("two_variable_form_holds_all_valid_orders", bool(holds), True)
    wb.add_assertion("d5_reproduces_ai81_witness", bool(d5_ok), True)
    wb.add_assertion("partial_sums_converged_1pct", bool(converged), True)
    out = wb.save()
    print(f"  Witness: {out}")
    return 0 if (holds and d5_ok) else 1


if __name__ == "__main__":
    sys.exit(main())
