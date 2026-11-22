#!/usr/bin/env python3
"""The c_3 anchor swing is NOT exactly resolved: it carries +/- 0.0052 from the
muon pin, so a gate keyed on it needs a 10.5 % tolerance.

Bean `qou-cds1`, tranche S1.

*** MOST OF THIS FILE'S MECHANISM IS ALREADY THE CORPUS'S.  Recorded first: ***

  - `qbeta_c3_experimental_uncertainty_probe.py` has the 1/u^3 amplification
    (gain 1.618e6), sigma(c_3) = 1.16, and "-2 is inside 1 sigma".
  - `qbeta_c3_swing_gate_probe.py` has the COMMON-MODE CANCELLATION, derives it
    by perturbing Q_beta rather than asserting it, and already uses the swing as
    the PRIMARY RESOLVED FILTER on candidate u(q0) maps.

  I re-derived both because my corpus-grep covered `AGENTS.md docs/audits/
  content/` and skipped `computations/` -- path 3 of the checklist -- where ~55
  `qbeta_c3_*` probes live.

WHAT THIS FILE ADDS, and it bears on that live gate.

`qbeta_c3_swing_gate_probe` calls the swing **RESOLVED** because the CAL-3
(Q_beta) error is common-mode, and does not propagate the PIN uncertainty
(grepped: no MASS_RATIO_MU_E_ERR, no dq/dr, no pin sigma).  The pins are what
the difference is made of, and their error does not cancel:

    sigma(swing) from Q_beta   (common-mode, cancels)   +/- 8.33e-7
    sigma(swing) from muon pin (does NOT cancel)        +/- 5.21e-3   6255x larger
    total                                               +/- 5.21e-3

    swing        = -0.049482266
    significance = 9.4936 sigma

So the swing is significant but NOT exact -- a **10.5 %** bar.  A gate keyed on
it must allow that; a tighter tolerance rejects correct candidates.

The 9.4936 sigma independently reproduces the 9.5 sigma mu-p substrate tension
AGENTS.md documents, from the Q_beta side rather than the m_mu side.  That
cross-check is why the corrected number is trustworthy rather than a third error
-- there were two before it, in opposite directions:

  (1) propagating only Q_beta gives "59,400 sigma", wrong by four orders;
  (2) applying the 22.2 ppb directly to q gives "0.53 sigma", also wrong,
      because the ratio->q0 map COMPRESSES by ~18x (dq/dr = -2.95e-4).

THE CONSEQUENCE WORTH CARRYING:

    quantity      value          sigma        relative     limited by
    c_3           -2.0693        +/- 1.379      67 %       Q_beta^exp
    dc_3/dq        3838405.9     +/- 4.04e5     10.5 %     m_mu/m_e

"Improve the measurement" is TWO programmes.  Sharpening Q_beta (32x / 130x, per
`rem-qstar-decay-sector-q0`) buys the VALUE and almost nothing for the
derivative; sharpening m_mu/m_e buys the DERIVATIVE and nothing for the value.
The derivative's value is the corpus's three ways over (this is a fourth route,
agreeing to ~1e-6); the ERROR BAR is what was missing.

NOT CHASED: the swing-gate probe records `Delta_S = 0.0491423421`; this file
gets `0.049482266`, 0.7 % apart, from a different extraction path (its `S_leak`
carries a Vol(4_1) that cancels in the swing).  Flagged for that probe's owner;
it does not move the 10.5 % conclusion.

SCOPE (a).  Convention C.  NOT a claim that the swing gate is wrong -- its
cancellation derivation is sound and its use as primary filter stands.  Only
that its tolerance should be +/- 0.0052, not zero.

Exact mpmath at 50 dps; no float64; emits no witness.
"""
import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
import json
import pathlib
import sys

import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
mp.mp.dps = 50

from qou_substrate import constants as C  # noqa: E402
from qou_substrate.constants import (M_E_MEV, Q_NEUTRON_MEV,  # noqa: E402
                                     Q_NEUTRON_MEV_ERR, q_at)

ME = mp.mpf(str(M_E_MEV))
R = mp.mpf(str(Q_NEUTRON_MEV))
SR = mp.mpf(str(Q_NEUTRON_MEV_ERR))
MUON_WITNESS = HERE.parent / "q-pinning-50-digit.witness.json"


def QN2(q):
    """N=2 truncation, convention C — the frame the extraction was done in."""
    h = q - 1 / q
    hb = (q - 1) / q
    b = mp.sqrt(q**4 + q**2 + 1) / (q**2 + 1)
    z = mp.sqrt(q) / (q + 1)
    QA = abs(_qbeta_e0.order_zero_scaled(((q - 1 / q) / 2 * h - h) * ME, q))
    return QA * mp.cos((z - 1) * h / 2 - b * hb**2 / 2) * (1 - b**2 * hb**4)


def u3(q):
    hb = (q - 1) / q
    b = mp.sqrt(q**4 + q**2 + 1) / (q**2 + 1)
    return (b * hb**2) ** 3


def c3_of(q):
    return (R / QN2(q) - 1) / u3(q)


def main() -> int:
    checks = []

    q_p = q_at(50)
    q_m = mp.mpf(str(json.loads(MUON_WITNESS.read_text())
                     ["derived_50_digit"]["q"]))
    dq = q_p - q_m
    swing = c3_of(q_p) - c3_of(q_m)
    deriv = swing / dq

    # --- Q_beta contribution: common-mode, cancels ------------------------
    dp = 1 / (QN2(q_p) * u3(q_p))
    dm = 1 / (QN2(q_m) * u3(q_m))
    s_val_Q = dp * SR                 # sigma on ONE c_3 value
    s_swing_Q = abs(dp - dm) * SR     # sigma on the DIFFERENCE

    checks.append(("Q_beta error is common-mode: cancels by > 1e6 in the swing",
                   s_val_Q / s_swing_Q > mp.mpf("1e6")))

    # --- muon pin: does NOT cancel, and dominates -------------------------
    # m_mu/m_e = Vol(4_1)/hbar_q^2 with hbar = 1 - 1/q  =>  dq/dr analytic
    V = 2 * mp.clsin(2, mp.pi / 3)                      # Vol(4_1) = 2*Cl_2(pi/3)
    hb_m = (q_m - 1) / q_m
    dq_dr = -hb_m**3 * q_m**2 / (2 * V)
    s_q_mu = abs(dq_dr) * mp.mpf(str(C.MASS_RATIO_MU_E_ERR))
    s_swing_mu = abs(deriv) * s_q_mu

    # proton pin, for completeness: far tighter anchor
    s_q_p_rel = mp.mpf(str(C.MASS_RATIO_P_E_ERR)) / mp.mpf(str(C.MASS_RATIO_P_E))
    checks.append(("proton anchor is ~1276x tighter than muon in relative terms",
                   (mp.mpf(str(C.MASS_RATIO_MU_E_ERR))
                    / mp.mpf(str(C.MASS_RATIO_MU_E))) / s_q_p_rel > 1000))

    checks.append(("the muon pin dominates sigma(swing), by > 1000x",
                   s_swing_mu / s_swing_Q > 1000))

    s_swing = mp.sqrt(s_swing_Q**2 + s_swing_mu**2)
    sig = abs(swing) / s_swing

    # --- the documented cross-check ---------------------------------------
    checks.append(("swing significance reproduces the documented 9.5 sigma "
                   "mu-p substrate tension",
                   abs(sig - mp.mpf("9.5")) < mp.mpf("0.1")))

    # --- derivative value agrees with the corpus's three routes -----------
    checks.append(("dc_3/dq reproduces rem-qstar's 3838404.458 to < 1e-5 rel",
                   abs(deriv - mp.mpf("3838404.458")) / mp.mpf("3838404.458")
                   < mp.mpf("1e-5")))

    # --- value vs derivative precision ------------------------------------
    s_deriv = s_swing / abs(dq)
    rel_val = s_val_Q / abs(c3_of(q_p))
    rel_der = s_deriv / abs(deriv)

    checks.append(("the DERIVATIVE is better determined than the VALUE",
                   rel_der < rel_val))
    checks.append(("but only by ~6x, NOT the 4 orders a Q_beta-only pass gives",
                   3 < rel_val / rel_der < 12))

    print("What Q_beta can and cannot test about c_3.  mpmath, 50 dps. "
          "Convention C.\n")
    print(f"  q_proton = {mp.nstr(q_p, 15)}")
    print(f"  q_muon   = {mp.nstr(q_m, 15)}   ({mp.nstr(dq / q_p * 1e9, 5)} ppb apart)\n")
    print(f"  c_3(proton) = {mp.nstr(c3_of(q_p), 12)}")
    print(f"  c_3(muon)   = {mp.nstr(c3_of(q_m), 12)}")
    print(f"  swing       = {mp.nstr(swing, 10)}")
    print(f"  dc_3/dq     = {mp.nstr(deriv, 12)}\n")

    print(f"  {'contribution to sigma(swing)':34} {'value':>14}")
    print(f"    {'Q_beta  (common-mode, cancels)':32} {mp.nstr(s_swing_Q, 6):>14}")
    print(f"    {'muon pin (does NOT cancel)':32} {mp.nstr(s_swing_mu, 6):>14}")
    print(f"    {'total':32} {mp.nstr(s_swing, 6):>14}")
    print(f"    {'cancellation of Q_beta':32} {mp.nstr(s_val_Q / s_swing_Q, 6):>14}x\n")
    print(f"  swing significance = {mp.nstr(sig, 6)} sigma"
          f"   (documented mu-p tension: 9.5)\n")

    print(f"  {'quantity':12} {'value':>16} {'sigma':>14} {'relative':>12}")
    print(f"  {'c_3':12} {mp.nstr(c3_of(q_p), 8):>16} {mp.nstr(s_val_Q, 6):>14}"
          f" {mp.nstr(rel_val * 100, 4):>11} %")
    print(f"  {'dc_3/dq':12} {mp.nstr(deriv, 10):>16} {mp.nstr(s_deriv, 6):>14}"
          f" {mp.nstr(rel_der * 100, 4):>11} %")
    print(f"\n  derivative is {mp.nstr(rel_val / rel_der, 4)}x better determined "
          f"than the value")

    print("\n--- checks ---")
    ok = True
    for name, passed in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
        ok = ok and bool(passed)
    print(f"\n{sum(1 for _, p in checks if p)}/{len(checks)}")

    print("""
FINDING

  Q_beta CAN test something about c_3 -- the q-derivative, not the value -- and
  the limiting input is different for each:

    c_3 value     67 %      limited by Q_beta^exp
    dc_3/dq       10.5 %    limited by m_mu/m_e

  because the Q_beta error is common-mode between the two anchors and cancels
  1.65e6-fold in the difference, which promotes the muon anchor to dominant.

  So "improve the measurement" is TWO programmes, not one.  Sharpening Q_beta
  (the 32x / 130x in `rem-qstar-decay-sector-q0`) buys the value and almost
  nothing for the derivative; sharpening m_mu/m_e buys the derivative and
  nothing for the value.

  And the derivative test needs NO experimental improvement to run today: a
  candidate closed form c_3(q) must reproduce 3838405.9 +/- 4.0e5, a 10.5 %
  target, where the value test offers only 67 %.

  The 9.4936 sigma independently reproduces the documented 9.5 sigma mu-p
  substrate tension from the Q_beta side, which is a consistency check on the
  whole propagation rather than a new result.

SCOPE (a).  Convention C.  The derivative VALUE is the corpus's, three ways
over; what is added here is its ERROR BAR and the input-attribution.  No claim
that any candidate passes or fails the derivative test -- none is tested here.
""")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
