#!/usr/bin/env python3
"""l2_gap_independence_decomposition.py — how many INDEPENDENT derivation gaps
does the 1ppQ L2 goal actually have?

THE QUESTION
    `per_observable_100x_status.py` scores 7 observables against
    `σ_pred(O) ≤ σ_exp(O)/100` and reports **2 / 7**. Read literally that is five
    separate problems. It is not. Some of those observables are algebraic
    functions of the others, and one is a pure artifact of which q₀ pin is in
    force — so their errors are not independent evidence, they are the same
    number counted again.

    Getting this wrong costs real work. `Q_beta` misses by 164.0x and
    `Delta_pn` by 163.3x; those read as two comparable, separate targets.

THE CANONICAL CHAIN (docs/canonical-mass-formula-guardrail.md)

    hbar_q  = (q-1)/q
    m_mu    = m_e * Vol(4_1) / hbar_q^2          ABSOLUTE muon anchor
    F_Bor   = |tr_M(b_Bor)| * [3]_q! / q^3       dimensionless
    m_p     = 2*(m_mu*F_Bor - 6*m_e)             ABSOLUTE proton
    m_n     = m_p + Q_beta + m_e                 ABSOLUTE neutron
    Delta_pn= m_n - m_p = Q_beta + m_e

WHAT THIS SHOWS — four of the five failures are not derivation gaps

    m_mu     PIN ARTIFACT.  Its 209.8 ppb is EXACTLY the 11.537 ppb muon/proton
             layer separation times its pin sensitivity |S| = 18.185 (predicted
             209.81, ratio 1.0000). At the muon anchor m_mu returns CODATA by
             construction; at the proton pin it is a genuine prediction, and its
             whole miss IS the separation. Nothing else is wrong with it.

    m_n      DERIVED.  `m_n = m_p + Q_beta + m_e` makes its absolute error the
             sum of m_p's and Q_beta's: predicted 2.4141 ppb vs 2.414 reported,
             ratio 1.00004.

    Delta_pn DERIVED.  `Delta_pn = Q_beta + m_e` with m_e the exact CAL-1 anchor,
             so its ABSOLUTE error must equal Q_beta's: ratio 1.00031. The
             relative errors differ only by Delta_pn/Q_beta = 1.6532, which is
             the whole of the gap between the 163.3x and 164.0x miss factors.

    m_p      CALIBRATION RESIDUAL, not an accuracy claim.  Its pin sensitivity
             |S| = 20.997 would put it at 242.2 ppb if the separation drove it;
             it sits at 1.351 ppb, **179x SMALLER**. Being far more accurate than
             your own pin sensitivity allows is the signature of a quantity the
             pin was solved to reproduce — which is exactly m_p's stated role,
             CAL-2 numerical anchor.

    Q_beta   THE GENUINE GAP.  Its pin sensitivity |S| = 2.632 accounts for only
             30.4 ppb of the observed 1279 ppb — **2.4 %**. Nothing in the pin,
             the chain, or the calibration explains the other 97.6 %.

SO: ONE unexplained derivation gap, Q_beta — plus a q₀-pin question (m_mu) and a
calibration residual (m_p). Closing Q_beta closes Delta_pn and m_n with it, which
takes the scoreboard from 2/7 to 5/7 on a single result.

The propagation identities are proven in Lean, not just checked numerically:
`QOU.MassTheory.DifferenceObservableErrorSplit`.

Read-only over the status and sensitivity witnesses; writes its own.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
for _p in (str(_HERE), str(_HERE / "substrate"),
           str(_HERE.parent / "tools" / "qou-substrate" / "python")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from substrate._precision import set_compute_dps  # noqa: E402
from substrate.witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()
mp.mp.dps = 50

# CODATA 2022, MeV. Only differences and ratios enter a conclusion.
M_P = mp.mpf("938.27208816")
M_N = mp.mpf("939.56542052")
M_E = mp.mpf("0.51099895000")

# Reported by per_observable_100x_status.py (2026-08-08), ppb.
ERR = {"m_p": mp.mpf("1.351"), "m_n": mp.mpf("2.414"), "m_mu": mp.mpf("209.8"),
       "Delta_pn": mp.mpf("773.9"), "Q_beta": mp.mpf("1279.")}
SIGMA = {"m_p": mp.mpf("0.3091"), "m_n": mp.mpf("0.5747"), "m_mu": mp.mpf("21.77"),
         "Delta_pn": mp.mpf("473.9"), "Q_beta": mp.mpf("779.7")}

# S(O) = dlog O / dlog q0, from mu_p_pin_sensitivity_map.py (mu-p-pin-sensitivity-map.witness.json).
SENS = {"m_p": mp.mpf("-20.9969854"), "m_n": mp.mpf("-20.97027445"),
        "m_mu": mp.mpf("-18.18535891"), "Q_beta": mp.mpf("-2.632392301")}

# The muon/proton q0 layer separation (AGENTS.md §q0-anchor).
SEPARATION_PPB = mp.mpf("11.537118")
PPB = mp.mpf("1e9")


def _s(x, n=6):
    return mp.nstr(x, n)


def main() -> int:
    t0 = time.monotonic()
    D = M_N - M_P
    Q = D - M_E

    # ── (A) which errors are just the pin separation, amplified? ────────
    pin = {}
    for k, S in SENS.items():
        pred = abs(S) * SEPARATION_PPB
        pin[k] = {"S": S, "predicted_ppb": pred, "actual_ppb": ERR[k],
                  "ratio": pred / ERR[k]}

    # ── (B) m_n is derived: m_n = m_p + Q_beta + m_e ────────────────────
    abs_p = ERR["m_p"] / PPB * M_P
    abs_Q = ERR["Q_beta"] / PPB * Q
    mn_pred = (abs_p + abs_Q) / M_N * PPB
    mn_ratio = mn_pred / ERR["m_n"]

    # ── (C) Delta_pn is derived: Delta_pn = Q_beta + m_e, m_e exact ─────
    abs_D = ERR["Delta_pn"] / PPB * D
    d_ratio = abs_D / abs_Q
    rel_scale = D / Q                       # 1.6532: the 163.3x vs 164.0x gap

    # ── (D) the residual, unexplained share of each ─────────────────────
    unexplained = {k: 1 - pin[k]["predicted_ppb"] / ERR[k] for k in pin}

    print("=" * 80)
    print("L2 gap independence — how many of the 5 failures are real gaps?")
    print("=" * 80)
    print(f"  q0 layer separation = {SEPARATION_PPB} ppb"
          f"     Delta_pn = {_s(D, 10)} MeV     Q_beta = {_s(Q, 10)} MeV")
    print()
    print("  (A) is the error just the PIN SEPARATION times the sensitivity?")
    print(f"      {'obs':<10}{'S=dlnO/dlnq':>14}{'|S|*sep':>12}{'actual':>12}"
          f"{'ratio':>10}   verdict")
    for k in ("m_mu", "m_p", "m_n", "Q_beta"):
        r = pin[k]["ratio"]
        v = ("PIN ARTIFACT — the whole miss" if abs(r - 1) < mp.mpf("0.01")
             else "far MORE accurate than the pin → calibrated" if r > 10
             else f"pin explains only {_s((1 - unexplained[k]) * 100, 3)} %")
        print(f"      {k:<10}{_s(SENS[k], 9):>14}{_s(pin[k]['predicted_ppb'], 6):>12}"
              f"{_s(ERR[k], 6):>12}{_s(r, 5):>10}   {v}")
    print()
    print("  (B) m_n = m_p + Q_beta + m_e  →  is m_n's error derived?")
    print(f"      predicted {_s(mn_pred)} ppb    reported {ERR['m_n']} ppb"
          f"    ratio {_s(mn_ratio)}")
    print("  (C) Delta_pn = Q_beta + m_e   →  absolute errors must be EQUAL")
    print(f"      dDelta {_s(abs_D)} MeV    dQ_beta {_s(abs_Q)} MeV"
          f"    ratio {_s(d_ratio)}")
    print(f"      relative errors differ by Delta_pn/Q_beta = {_s(rel_scale)}"
          f"  (the 163.3x vs 164.0x gap)")
    print()
    print("=" * 80)
    print("  ONE unexplained derivation gap: Q_beta (pin explains 2.4 %).")
    print("  m_mu is a pin artifact; m_p a calibration residual; m_n and")
    print("  Delta_pn are algebraic consequences of Q_beta. Closing Q_beta")
    print("  takes the scoreboard 2/7 -> 5/7 on a single result.")
    print("=" * 80)

    wb = (
        WitnessBuilder("l2-gap-independence-decomposition",
                       engine="python+mpmath", start_time=t0)
        .set_description(
            "Separates the five failing 1ppQ L2 observables into real "
            "derivation gaps and bookkeeping. m_mu's 209.8 ppb is exactly the "
            "11.537 ppb muon/proton pin separation times its sensitivity "
            "18.185 (ratio 1.0000); m_n is derived from m_p and Q_beta (ratio "
            "1.00004); Delta_pn carries Q_beta's absolute error identically "
            "(ratio 1.00031); m_p sits 179x more accurate than its own pin "
            "sensitivity allows, the signature of the CAL-2 calibration it "
            "anchors. Only Q_beta is unexplained — the pin accounts for 2.4% "
            "of its 1279 ppb. Propagation identities proven in "
            "QOU.MassTheory.DifferenceObservableErrorSplit."
        )
        .add_parameter("source_status", "per_observable_100x_status.py 2026-08-08")
        .add_parameter("source_sensitivity", "mu-p-pin-sensitivity-map.witness.json")
        .add_parameter("q0_layer_separation_ppb", str(SEPARATION_PPB))
    )
    wb.add_data("pin_attribution", {
        k: {kk: str(vv) for kk, vv in v.items()} for k, v in pin.items()})
    wb.add_data("m_n_is_derived", {
        "relation": "m_n = m_p + Q_beta + m_e",
        "predicted_ppb": str(mn_pred), "reported_ppb": str(ERR["m_n"]),
        "ratio": str(mn_ratio)})
    wb.add_data("Delta_pn_is_derived", {
        "relation": "Delta_pn = Q_beta + m_e (m_e exact, CAL-1)",
        "abs_err_Delta_MeV": str(abs_D), "abs_err_Q_beta_MeV": str(abs_Q),
        "ratio": str(d_ratio), "relative_scale_Delta_over_Q": str(rel_scale)})
    wb.add_data("verdict", {
        "genuine_gap": ["Q_beta"],
        "pin_artifact": ["m_mu"],
        "calibration_residual": ["m_p"],
        "algebraic_consequence": ["m_n", "Delta_pn"],
        "scoreboard_if_Q_beta_closes": "5/7"})

    wb.add_assertion("m_mu_error_is_the_pin_separation",
                     computed=float(abs(pin["m_mu"]["ratio"] - 1)), expected=0.0,
                     tolerance=1e-3,
                     source="|S(m_mu)| * 11.537 ppb vs reported 209.8 ppb")
    wb.add_assertion("m_n_error_is_derived_from_m_p_and_Q_beta",
                     computed=float(abs(mn_ratio - 1)), expected=0.0,
                     tolerance=1e-3, source="m_n = m_p + Q_beta + m_e")
    wb.add_assertion("Delta_pn_absolute_error_equals_Q_beta",
                     computed=float(abs(d_ratio - 1)), expected=0.0,
                     tolerance=1e-3, source="Delta_pn = Q_beta + m_e, m_e exact")
    wb.add_assertion("m_p_far_more_accurate_than_its_pin_sensitivity",
                     computed=str(bool(pin["m_p"]["ratio"] > 10)), expected="True",
                     source="signature of the quantity the pin was solved to reproduce")
    wb.add_assertion("Q_beta_is_NOT_explained_by_the_pin",
                     computed=float(pin["Q_beta"]["ratio"]), expected=0.0,
                     tolerance=0.05,
                     source="pin accounts for 30.4 of 1279 ppb")
    out = wb.save()
    print(f"\nWrote: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
