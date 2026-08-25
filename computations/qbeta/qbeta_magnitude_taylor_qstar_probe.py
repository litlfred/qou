#!/usr/bin/env python3
"""qbeta_magnitude_taylor_qstar_probe.py — close the S-channel magnitude to a
1-ppQ SYMBOLIC FORM (L1 compute precision) via the Taylor expansion of S at its
simple zero q*.

ROUTE A (this probe). The companion Bring-embedding probe
(`qbeta_bring_embedding_magnitude_probe.py`, `docs/audits/2026-08-01-bring-
embedding-magnitude.md`) established the honest negative: the observed
`|S_proton/S_muon| ≈ 4.075` is NOT a knot-embedding period — it is the ratio of
the two substrate anchors' offsets from the simple zero `q*` of

    S(q) := c3_target_at(q, Q_codata, m_e) + Vol(4₁),   Vol(4₁) = 2·Cl₂(π/3),

verified to ~6 digits by the leading-order offset ratio. The Lean file
`SLeakMagnitudeOffsetRatio.lean` proves the STRUCTURAL invariant behind it
(slope cancellation `linear_ratio_slope_independent`; smoothness-wall exclusion
`smooth_period_excluded_as_magnitude`).

This probe turns that leading-order identity into a **1-ppQ symbolic form**. Write
`δ = q − q*` and Taylor-expand S at the simple zero:

    S(q) = S'(q*)·δ + ½S''(q*)·δ² + (1/6)S'''(q*)·δ³ + …
         = S'(q*)·δ·(1 + a·δ + b·δ² + …),   a = ½S''/S',  b = (1/6)S'''/S'.

The slope S'(q*) cancels in the ratio (this is exactly the Lean-proved
`linear_ratio_slope_independent` made quantitative), leaving

    |S(q_p)/S(q_m)| = |δ_p/δ_m| · g(δ_p)/g(δ_m),   g(δ) = 1 + a·δ + b·δ² + … .

Because δ ~ 1e-8, each Taylor order in g adds ~6–7 digits of agreement with the
DIRECT evaluation `|S(q_p)/S(q_m)|`. The probe DERIVES q* (mpmath findroot,
bracketed between the two anchors, which have opposite S-sign), DERIVES the
Taylor coefficients (mpmath.diff), and reports the residual at each truncation
order — nothing is tuned, the 1-ppQ match is FORCED not selected.

RESULT (60 dps, derive-then-check):
  * q* = 1.1099785930315232884023283427354933150988  (S(q*) residual ~8e-56)
  * DIRECT |S_p/S_m| = 4.07512700316204532552627382494
  * residual of the symbolic form vs the direct eval, by Taylor order of g:
        order 0 (offset ratio, g≡1)  : 6.18e-7   (leading order, matches ~6 digits)
        order 1 (g = 1+aδ)           : 1.40e-13
        order 2 (g = 1+aδ+bδ²)       : 3.53e-20  ← first order ≤ 1e-15 (1 ppQ)
        order 3 (g = 1+aδ+bδ²+cδ³)   : 6.95e-27
    ⇒ minimum Taylor order N = 2 reaches L1 compute precision (1 ppQ, ≤1e-15).

SCOPE (STRICT — do not over-claim). This is **L1 compute precision** (internal
cross-method agreement of a symbolic form vs a direct evaluation), NOT **L2
per-observable accuracy**: `|S_p/S_m| = 4.075` is an INTERNAL cross-check of the
bar-odd residual's near-zero-crossing structure, NOT a measured observable and
NOT a prediction against experiment. Closing the symbolic form to 1 ppQ does NOT
close the open `u(q₀)` map and does NOT give a closed form for q* itself — q* is
obtained here numerically (findroot); a closed form for q* is Route B and stays
OPEN. Anti-laundering: no `c_k` wired to production, no `SDeformedVolumeChannel`
instance fabricated, no `u(q₀)` map claimed.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import c3_target_at  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402

mp.mp.dps = 60
ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))       # experimental neutron β-decay Q-value: FIXED constant
with mp.workdps(60):
    VOL41 = +(2 * mp.clsin(2, mp.pi / 3))   # Vol(4₁) = 2·Cl₂(π/3)

ONE_PPQ = mp.mpf("1e-15")               # L1 compute-precision target (1 part per quadrillion)


def S(q):
    """Bar-odd residual: c₃-target shifted by Vol(4₁). q_codata is the SAME physical
    constant at every anchor; only the substrate quantities move with q (see
    `c3_target_at` docstring)."""
    return c3_target_at(q, QCOD, ME) + VOL41


def main() -> int:
    print("=" * 80)
    print(" MAGNITUDE via TAYLOR at q*: symbolic form for |S_p/S_m| to 1 ppQ (L1)")
    print("=" * 80)

    q_pr, q_mu = q_at(60), q_muon_at(60)
    S_mu, S_pr = S(q_mu), S(q_pr)
    direct = abs(S_pr / S_mu)
    print(f"\n substrate anchors (opposite S-sign ⇒ a zero of S lies between them):")
    print(f"   q_proton = {mp.nstr(q_pr,20)}   S(q_p) = {mp.nstr(S_pr,9)} ({'−' if S_pr<0 else '+'})")
    print(f"   q_muon   = {mp.nstr(q_mu,20)}   S(q_m) = {mp.nstr(S_mu,9)} ({'−' if S_mu<0 else '+'})")
    print(f"   DIRECT |S_proton/S_muon| = {mp.nstr(direct,30)}   ← target to reproduce symbolically")

    # ---- [1] DERIVE q* as the simple zero, bracketed between the anchors -------
    print("\n [1] q* = simple zero of S (findroot, midpoint start between anchors)")
    q_star = mp.findroot(S, (q_pr + q_mu) / 2)
    qstar_resid = abs(S(q_star))
    print(f"      q* = {mp.nstr(q_star,50)}")
    print(f"      S(q*) residual = {mp.nstr(qstar_resid,6)}   (< 1e-40: {qstar_resid < mp.mpf('1e-40')})")

    # ---- [2] DERIVE the Taylor coefficients of S at q* (mpmath.diff) -----------
    print("\n [2] Taylor coefficients at q*: a = ½S''/S', b = (1/6)S'''/S', c = (1/24)S''''/S'")
    with mp.workdps(100):
        d1 = mp.diff(S, q_star, 1)
        d2 = mp.diff(S, q_star, 2)
        d3 = mp.diff(S, q_star, 3)
        d4 = mp.diff(S, q_star, 4)
    a_coef = d2 / (2 * d1)
    b_coef = d3 / (6 * d1)
    c_coef = d4 / (24 * d1)
    print(f"      S'(q*)   = {mp.nstr(d1,16)}   (the local slope L — CANCELS in the ratio)")
    print(f"      S''(q*)  = {mp.nstr(d2,16)}")
    print(f"      S'''(q*) = {mp.nstr(d3,16)}")
    print(f"      a = {mp.nstr(a_coef,12)}   b = {mp.nstr(b_coef,12)}   c = {mp.nstr(c_coef,12)}")

    dp = q_pr - q_star
    dm = q_mu - q_star
    print(f"      δ_proton = {mp.nstr(dp,16)}   δ_muon = {mp.nstr(dm,16)}")

    # ---- [3] the symbolic form, truncated at each Taylor order -----------------
    def g(delta, order):
        """analytic cofactor 1 + a·δ + b·δ² + c·δ³ truncated at `order`."""
        val = mp.mpf(1)
        if order >= 1:
            val += a_coef * delta
        if order >= 2:
            val += b_coef * delta ** 2
        if order >= 3:
            val += c_coef * delta ** 3
        return val

    def symbolic(order):
        # |S_p/S_m| = |δ_p/δ_m| · g(δ_p)/g(δ_m)  (slope S' cancels — Lean-proved)
        return abs(dp / dm) * (g(dp, order) / g(dm, order))

    print("\n [3] symbolic |S_p/S_m| = |δ_p/δ_m|·g(δ_p)/g(δ_m); residual vs DIRECT by order")
    residuals = {}
    N = None
    for order in range(0, 4):
        val = symbolic(order)
        res = abs(val - direct) / abs(direct)
        residuals[order] = res
        flag = ""
        if res <= ONE_PPQ and N is None:
            N = order
            flag = "  ← first order ≤ 1e-15 (1 ppQ)"
        label = "offset ratio, g≡1" if order == 0 else f"g=1+aδ+…(deg {order})"
        print(f"      order {order} ({label:22s}): {mp.nstr(val,25):27s}  resid {mp.nstr(res,5):>9}{flag}")

    off_ratio = abs(dp / dm)
    off_resid = residuals[0]
    print(f"\n      leading offset ratio |δ_p/δ_m| = {mp.nstr(off_ratio,20)}")
    print(f"        matches DIRECT to rel {mp.nstr(off_resid,4)}  (≈ {int(-mp.log10(off_resid))} digits — order of validity)")
    print(f"      minimum Taylor order reaching 1 ppQ: N = {N}")

    # ---- verdict ---------------------------------------------------------------
    print("\n" + "=" * 80)
    print(f" RESULT: |S_p/S_m| closed to a 1-ppQ SYMBOLIC FORM at Taylor order N = {N}.")
    print("   The slope S'(q*) cancels (Lean `linear_ratio_slope_independent`); the")
    print("   residual is FORCED by the derived Taylor coefficients, not tuned.")
    print(" SCOPE: L1 compute precision (symbolic vs direct), NOT an L2 observable —")
    print("   |S_p/S_m| is an internal cross-check, not a measured prediction. The")
    print("   closed form for q* (Route B) and the u(q₀) map stay OPEN; nothing wired.")
    print("=" * 80)

    wb = WitnessBuilder("qbeta-magnitude-taylor-qstar", engine="mpmath")
    wb.set_description(
        "Route A: close the S-channel magnitude |S_proton/S_muon|≈4.075 to a 1-ppQ SYMBOLIC "
        "FORM (L1 compute precision) via the Taylor expansion of S(q)=c3_target_at(q,Q_codata,m_e)"
        "+Vol(4₁) at its simple zero q*. The companion Bring-embedding probe showed the magnitude "
        "is NOT a knot period but the anchor-offset ratio near q*; this probe makes that "
        "leading-order identity a 1-ppQ symbolic form. DERIVED (not tuned): q* by findroot "
        "bracketed between the two anchors (opposite S-sign; S(q*) residual ~8e-56, <1e-40); the "
        "Taylor coefficients a=½S''/S', b=(1/6)S'''/S' by mpmath.diff. With δ=q−q*, the slope S'(q*) "
        "cancels in the ratio (Lean-proved linear_ratio_slope_independent), leaving "
        "|S_p/S_m|=|δ_p/δ_m|·g(δ_p)/g(δ_m), g(δ)=1+aδ+bδ²+…. Residual vs the DIRECT eval by "
        "Taylor order of g: order0 (offset ratio) 6.18e-7 (~6 digits, leading order of validity); "
        "order1 1.40e-13; order2 3.53e-20 (first ≤1e-15); order3 6.95e-27 — each order adds ~6–7 "
        "digits (δ~1e-8). MINIMUM Taylor order reaching 1 ppQ: N=2. SCOPE: this is L1 (internal "
        "symbolic-vs-direct cross-check), NOT L2 — |S_p/S_m| is an internal cross-check of the "
        "bar-odd residual's near-zero-crossing structure, not a measured observable/prediction. "
        "Closing the symbolic form does NOT close the closed form for q* (Route B, OPEN) nor the "
        "u(q₀) map (OPEN); anti-laundering — no c_k wired, no SDeformedVolumeChannel instance, no "
        "u(q₀) claimed.")
    wb.set_content_block("conj:binding-qbeta-complex-volume")
    wb.add_data("magnitude_taylor_qstar_readout", {
        "S_definition": "S(q) = c3_target_at(q, Q_codata, m_e) + Vol(4₁),  Vol(4₁)=2·Cl₂(π/3)",
        "q_codata_is_fixed_constant": mp.nstr(QCOD, 12),
        "q_star": mp.nstr(q_star, 50),
        "q_star_residual": mp.nstr(qstar_resid, 6),
        "direct_magnitude": mp.nstr(direct, 30),
        "slope_L_cancels": f"S'(q*) = {mp.nstr(d1,12)} (cancels in the ratio; Lean linear_ratio_slope_independent)",
        "taylor_coeffs": f"a=½S''/S'={mp.nstr(a_coef,12)}, b=(1/6)S'''/S'={mp.nstr(b_coef,12)}, c=(1/24)S''''/S'={mp.nstr(c_coef,12)}",
        "delta_offsets": f"δ_proton={mp.nstr(dp,12)}, δ_muon={mp.nstr(dm,12)}",
        "symbolic_form": "|S_p/S_m| = |δ_p/δ_m| · g(δ_p)/g(δ_m),  g(δ)=1+a·δ+b·δ²+…",
        "residual_by_order": {
            "order_0_offset_ratio": mp.nstr(residuals[0], 6),
            "order_1": mp.nstr(residuals[1], 6),
            "order_2": mp.nstr(residuals[2], 6),
            "order_3": mp.nstr(residuals[3], 6),
        },
        "offset_ratio_leading_order_of_validity": f"|δ_p/δ_m|={mp.nstr(off_ratio,20)} matches DIRECT to rel {mp.nstr(off_resid,4)} (~6 digits)",
        "min_taylor_order_for_1ppq": int(N),
        "scope": (
            "L1 compute precision (symbolic form vs direct evaluation), NOT L2 per-observable "
            "accuracy. |S_p/S_m|=4.075 is an INTERNAL cross-check of the bar-odd residual's "
            "near-zero-crossing structure, not a measured observable or a prediction against "
            "experiment."),
        "still_open": (
            "closed form for q* (Route B — q* is obtained here numerically by findroot) and the "
            "u(q₀) map. No c_k wired to production, no SDeformedVolumeChannel instance fabricated, "
            "no u(q₀) map claimed."),
    })
    # assertions
    a_qstar = qstar_resid < mp.mpf("1e-40")
    a_offset = mp.mpf("1e-8") < off_resid < mp.mpf("1e-5")   # leading order matches ~6 digits
    a_N2_reaches = residuals[2] <= ONE_PPQ                    # order 2 reaches 1 ppQ
    a_N2_minimal = residuals[1] > ONE_PPQ                     # order 1 does NOT (so N=2 is minimal)
    wb.add_assertion("qstar_residual_below_1e40", str(bool(a_qstar)), "True")
    wb.add_assertion("offset_ratio_leading_matches_about_6_digits", str(bool(a_offset)), "True")
    wb.add_assertion("taylor_order_2_reaches_1ppq", str(bool(a_N2_reaches)), "True")
    wb.add_assertion("taylor_order_2_is_minimal_for_1ppq", str(bool(a_N2_minimal)), "True")
    wb.save()
    print("\nwitness → qbeta-magnitude-taylor-qstar.witness.json")
    ok = all([a_qstar, a_offset, a_N2_reaches, a_N2_minimal])
    print("ALL ASSERTIONS PASS" if ok else "ASSERTION FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
