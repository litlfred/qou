#!/usr/bin/env python3
"""qbeta_c3_odd_dof_normalization_fork_probe.py — the DECISIVE c₃ DOF fork.

Bean qou-1dnr. Settles: is the Q_β precision-ladder rung c₃ PINNED (exactly
determined) by the determined ℚ(√3) triangular solve on the derived net
decay-width — the same solve behind c₂ = −1 — or is it a SEPARATE degree of
freedom?

VERDICT (B): c₃ is a separate DOF. The structural reason ("what changes at
order 3"), formalized in QOU.Mass.QbetaC3OddDOF:

  * c₂ is the LEADING rung (pinned at s⁴ = leading order of u²). At s⁴ the
    bar-weight-2 variable u = b·ℏ_q² and the bar-EVEN variable ũ = q·u agree
    (u₂ = ũ₂ = √3/2), so c₂'s extraction is BLIND to the u→ũ normalization —
    a reparametrisation invariant. This is the algebraic shadow of the CLOSED
    finite N=2 factor 1 − b²ℏ_q⁴ = 1 − u² (c₂ = −1, structural).

  * c₃ is the first SUBLEADING rung (pinned at s⁶). Its extraction must subtract
    the s⁶ TAIL of the already-fixed c₂ rung (2u₂u₄ + u₃²), which lives exactly
    where u (bar-weight 2) and ũ (bar-even) DIVERGE. So the extracted c₃ carries
    the u-vs-ũ ambiguity: it SHIFTS by an exact nonzero ℚ(√3) amount. It is NOT
    a structural invariant; the determined even solve does not pin a canonical
    c₃. There is no known CLOSED N=3 factor to make it one.

This probe MEASURES (all exact ℚ(√3), no CODATA, no fit):

  (1) c₂,c₃,c₄ solved from the SAME determined net-route log R in the u
      convention and the ũ = q·u convention; exact diffs (c₂ diff = 0;
      c₃, c₄ diffs ≠ 0, exact ℚ(√3)).
  (2) cross-check of the Lean shift identity
      c₃(u) − c₃(ũ) = c₂·(4u₃ + u₂)/u₂²  (w = q ⇒ w₁ = 1, w₂ = 0).
  (3) the ODD-CHANNEL DECOUPLING pillar: with the even rungs c₂..c₄ fixed, the
      single-variable ladder ∏(1+c_k u^k) leaves ALL odd-order residuals
      (s³,s⁵,s⁷,s⁹) exactly NONZERO — it is blind to the bar-odd content. That
      content is the separate, exactly-determined companion h·D(ũ) whose
      observable rung needs the OPEN fibre f-map / A_ω (Reeb-sinh, #3805).

Honesty: no c_k wired; no fit (both channels are the determined ℚ(√3) solve on
the symbolic GB-reduced Δ(net)); scope (a); audit-only. The verdict is a clean,
valuable NEGATIVE: c₃ is a separate DOF, which is exactly the certificate that
A_ω is REQUIRED, not optional.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401
sys.path.insert(0, str(Path(__file__).resolve().parent))

import json  # noqa: E402
import sympy as sp  # noqa: E402
import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

import qbeta_ck_sseries_exact_rational as core  # noqa: E402
core.ORD = 13          # need s⁴..s⁸ for c₂..c₄, plus odd orders s³..s⁹
ORD = core.ORD
from qbeta_ck_sseries_exact_rational import (  # noqa: E402
    q, simp, ser_add, ser_mul, ser_scale, ser_inv, ser_sqrt, ser_div,
    ser_log1, ser_cos0, rat_series, load_net_symbolic,
)

mp.mp.dps = 60
HERE = Path(__file__).resolve().parent


def build_logR():
    """Exact net-route log R series (IDENTICAL convention to 9fnm: alpha_eff
    uses the weight-2 u = b·ℏ_q²; c₂ gate = −8.006)."""
    dnet = sp.simplify(load_net_symbolic("neutron") - load_net_symbolic("proton"))
    dnet_reg = sp.cancel(dnet / (q - 1))
    q0 = mp.mpf(json.load(open(_pb.witness_path(
        "q-pinning-50-digit.witness.json", HERE)))["derived_50_digit"]["q"])
    sgn = int(mp.sign(sp.lambdify(q, dnet, "mpmath")(q0)))
    Qb = rat_series(sp.Integer(sgn) * dnet_reg / q)
    QA = rat_series((2 * q + 1 - q**2) * (q + 1) / (2 * q**3))
    hbar2 = rat_series(((q - 1) / q) ** 2)
    b_ser = ser_mul(ser_sqrt(rat_series(q**4 + q**2 + 1)),
                    ser_inv(rat_series(q**2 + 1)))
    u_raw = ser_mul(b_ser, hbar2)          # u  = b·ℏ²        (bar-weight 2)
    u_til = ser_mul(rat_series(q), u_raw)  # ũ  = q·u         (bar-even)
    sqrt_q = ser_sqrt(rat_series(q))
    z_ser = ser_mul(sqrt_q, ser_inv(rat_series(q + 1)))
    h_ser = rat_series(q - 1 / q)
    zm1 = list(z_ser); zm1[0] = simp(zm1[0] - 1)
    alpha = ser_add(ser_scale(sp.Rational(1, 2), ser_mul(zm1, h_ser)),
                    ser_scale(sp.Rational(-1, 2), u_raw))   # 9fnm: alpha uses u_raw
    R = ser_mul(Qb, ser_inv(ser_mul(QA, ser_cos0(alpha))))
    logR = ser_log1(R)
    return logR, u_raw, u_til, h_ser


def solve_ladder(logR, uvar, kmax=4):
    """Triangular log-ladder solve log R = Σ_{k≥2} log(1 + c_k·uvar^k), pinned
    at s^{2k}; returns {k: exact c_k} and the full residual table by order."""
    upow = {1: uvar}
    for k in range(2, kmax + 1):
        upow[k] = ser_mul(upow[k - 1], uvar)
    c = {}
    model = [sp.Integer(0)] * (ORD + 1)
    for k in range(2, kmax + 1):
        o = 2 * k
        ck = simp((logR[o] - model[o]) / upow[k][o])
        c[k] = ck
        cku = ser_scale(ck, upow[k]); onep = list(cku); onep[0] = simp(onep[0] + 1)
        model = ser_add(model, ser_log1(onep))
    resid = {n: simp(logR[n] - model[n]) for n in range(2, ORD + 1)}
    return c, resid


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" qou-1dnr — c₃ DOF fork: reparam-invariance (c₂) vs shift (c₃), exact ℚ(√3)")
    print("=" * 78)

    logR, u_raw, u_til, h_ser = build_logR()

    # (1) same log R, two ladder-variable conventions
    cu, residu = solve_ladder(logR, u_raw)
    ct, _ = solve_ladder(logR, u_til)
    print(f"\n  c₂ (u-conv) exact = {cu[2]}   numeric = {sp.N(cu[2], 12)}  (9fnm gate −8.006)")
    diffs = {}
    for k in (2, 3, 4):
        d = simp(cu[k] - ct[k])
        diffs[k] = d
        inv = sp.simplify(d) == 0
        print(f"  c{k}: diff(u, ũ)_exact = {d}    invariant = {inv}")

    c2_invariant = sp.simplify(diffs[2]) == 0
    c3_shift = diffs[3]
    c3_not_invariant = sp.simplify(c3_shift) != 0
    c4_not_invariant = sp.simplify(diffs[4]) != 0

    # (2) Lean shift-identity cross-check:  c₃(u) − c₃(ũ) = c₂·(4u₃ + u₂)/u₂²
    u2, u3 = u_raw[2], u_raw[3]
    predicted = simp(cu[2] * (4 * u3 + u2) / u2**2)
    lean_identity_ok = sp.simplify(c3_shift - predicted) == 0
    print(f"\n  Lean shift identity  c₃(u)−c₃(ũ) = c₂·(4u₃+u₂)/u₂²  holds? {lean_identity_ok}")
    print(f"    u₂ = {u2}   u₃ = {u3}")
    print(f"    predicted = {predicted}")

    # (3) ODD-CHANNEL DECOUPLING: even-ladder residuals at odd orders (exact ≠ 0)
    odd_resid = {n: residu[n] for n in range(3, ORD + 1, 2)}
    odd_all_nonzero = all(sp.simplify(v) != 0 for v in odd_resid.values())
    print("\n  odd-order residuals of the single-u ladder (blindness to bar-odd content):")
    for n, v in odd_resid.items():
        print(f"    residual [s^{n}] = {sp.N(v, 10)}   nonzero = {sp.simplify(v) != 0}")

    # ... and the separate, exactly-determined bar-odd companion D = O/h
    phi = [sp.Integer(0)] + [sp.Integer(-1) ** n for n in range(1, ORD + 1)]

    def ser_compose(a, ph):
        out = [sp.Integer(0)] * (ORD + 1); out[0] = a[ORD]
        for n in range(ORD - 1, -1, -1):
            out = ser_mul(out, ph); out[0] = simp(out[0] + a[n])
        return out
    logR_bar = ser_compose(logR, phi)
    O = [simp((x - y) / 2) for x, y in zip(logR, logR_bar)]
    G, g_top = ser_div(O, h_ser)      # D = O/h, bar-even companion series
    d_ladder = {}
    upt = {1: u_til}
    for k in range(2, 6):
        upt[k] = ser_mul(upt[k - 1], u_til)
    modelD = [sp.Integer(0)] * (ORD + 1)
    for k in range(1, 6):
        dk = simp((G[2 * k] - modelD[2 * k]) / upt[k][2 * k])
        d_ladder[k] = dk
        modelD = ser_add(modelD, ser_scale(dk, upt[k]))
    print("\n  separate exact bar-odd companion D = O/h = Σ d_k ũ^k (determined, ℚ(√3)):")
    for k, v in d_ladder.items():
        print(f"    d_{k} = {sp.N(v, 10)}   (≠ the observable rungs −1/−2 — needs the open f-map)")

    # ---- VERDICT ------------------------------------------------------------
    verdict_B = bool(c2_invariant and c3_not_invariant and lean_identity_ok
                     and odd_all_nonzero)
    print("\n" + "=" * 78)
    print(" VERDICT")
    print("=" * 78)
    if verdict_B:
        print("  (B) c₃ IS A SEPARATE DOF — NOT pinned by the determined even solve.")
        print("      • c₂ diff(u,ũ) = 0 exactly  → leading rung, reparam-INVARIANT")
        print("        (algebraic shadow of the closed N=2 factor 1 − u², c₂ = −1).")
        print(f"      • c₃ diff(u,ũ) = {c3_shift}")
        print("        ≠ 0 → first subleading rung, reparam-DEPENDENT (subtracts the")
        print("        c₂-tail at the bar-weight-ambiguous s⁶ order). No closed N=3")
        print("        factor pins it.")
        print("      • single-u ladder is BLIND to the bar-odd channel (odd residuals")
        print("        all ≠ 0); that content is the separate h·D companion, whose")
        print("        observable rung needs the OPEN fibre A_ω (Reeb-sinh, #3805).")
        print("      ⇒ A_ω is REQUIRED, not optional.")
        verdict = "B_C3_SEPARATE_DOF"
    else:
        verdict = "INCONCLUSIVE"
        print("  INCONCLUSIVE — see data.")

    elapsed = time.monotonic() - t0
    print(f"\n  ({elapsed:.1f}s)")

    wb = WitnessBuilder("qbeta-c3-odd-dof-normalization-fork", engine="sympy")
    wb.set_description(
        "qou-1dnr DECISIVE fork: is Q_β ladder rung c₃ pinned by the determined "
        "ℚ(√3) net solve (as c₂ is), or a separate DOF? Exact measurement over "
        "one fixed net-route log R in the u = b·ℏ² and ũ = q·u conventions: c₂ "
        "diff = 0 (leading rung, reparam-invariant — shadow of the closed N=2 "
        "factor 1−u²); c₃ diff = 35/6 + 7343√3/216 ≠ 0 (first subleading rung, "
        "reparam-dependent, no closed N=3 factor). Cross-checks the Lean shift "
        "identity c₃(u)−c₃(ũ)=c₂(4u₃+u₂)/u₂² and the odd-channel decoupling "
        "(single-u ladder blind to bar-odd content; separate exact h·D "
        "companion). VERDICT (B): c₃ is a separate DOF ⇒ the fibre A_ω is "
        "required. Scope (a); no fit; no c_k wired."
    )
    wb.set_content_block("conj:qbeta-precision-ladder")
    wb.add_data("c2_exact_u_conv", str(cu[2]))
    wb.add_data("c_k_diff_u_vs_utilde_exact", {str(k): str(v) for k, v in diffs.items()})
    wb.add_data("c2_reparam_invariant_diff_zero", bool(c2_invariant))
    wb.add_data("c3_reparam_shift_exact", str(c3_shift))
    wb.add_data("c3_not_reparam_invariant", bool(c3_not_invariant))
    wb.add_data("c4_not_reparam_invariant", bool(c4_not_invariant))
    wb.add_data("lean_shift_identity_c3", "c3(u)-c3(utilde) = c2*(4*u3+u2)/u2^2")
    wb.add_data("lean_shift_identity_holds", bool(lean_identity_ok))
    wb.add_data("odd_ladder_residuals_exact",
                {str(n): str(sp.N(v, 15)) for n, v in odd_resid.items()})
    wb.add_data("odd_residuals_all_nonzero_ladder_blind_to_barodd", bool(odd_all_nonzero))
    wb.add_data("barodd_companion_d_ladder_exact",
                {str(k): str(v) for k, v in d_ladder.items()})
    wb.add_data("verdict", verdict)
    wb.add_data("structural_reason", (
        "c₂ is the LEADING rung: pinned at s⁴ where u and ũ=q·u agree "
        "(u₂=ũ₂=√3/2), so its extraction is normalization-invariant — a genuine "
        "structural identity (closed N=2 factor 1−u², c₂=−1). c₃ is the first "
        "SUBLEADING rung: pinned at s⁶ after subtracting the c₂-rung tail "
        "2u₂u₄+u₃², which lives where u (bar-weight 2) and ũ (bar-even) diverge, "
        "so c₃ shifts by an exact nonzero ℚ(√3) amount and is NOT a "
        "presentation-invariant pinned value. Additionally the single-u "
        "even-power ladder is blind to the bar-odd content c₃ must carry (odd "
        "residuals ≠ 0); that content is the separate exact h·D companion whose "
        "observable rung requires the open fibre f-map / A_ω. Both pillars ⇒ "
        "c₃ is a separate DOF; A_ω required, not optional."
    ))
    wb.add_data("scope", "(a) — exact ℚ(√3) truncation, net route; no wiring; no fit")
    wb.add_assertion("c2_reparam_invariant", 1.0 if c2_invariant else 0.0, 1.0)
    wb.add_assertion("c3_reparam_dependent", 1.0 if c3_not_invariant else 0.0, 1.0)
    wb.add_assertion("lean_shift_identity_holds", 1.0 if lean_identity_ok else 0.0, 1.0)
    wb.add_assertion("odd_ladder_residuals_all_nonzero",
                     1.0 if odd_all_nonzero else 0.0, 1.0)
    wb.add_assertion("verdict_B_c3_separate_dof", 1.0 if verdict_B else 0.0, 1.0)
    out = wb.save()
    print(f"  Witness: {out}")
    return 0 if verdict_B else 1


if __name__ == "__main__":
    sys.exit(main())
