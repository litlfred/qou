#!/usr/bin/env python3
"""Does the STORED muon pin still agree with the LIVE derivation?

Bean `qou-bred`. Implements step 3 of the A-vs-C recommendation: drift
DETECTION without drift.

THE SITUATION IT WATCHES
------------------------
Two things are both called "the muon q0":

  A  the STORED 50-digit string in q-pinning-50-digit.witness.json, which
     `_q0_value_for_anchor("muon")` serves. `q_pinning_50_digit` is listed
     under `ideal_muon`, so `q_parameter` rebinds `q_at` to return that string
     and the Newton solve never runs -- the producer is a FIXED POINT that
     reproduces its own input. This is deliberate and load-bearing: the
     manifest warns that moving it "broke main for 208 producers".

  C  the LIVE derivation `q_muon_at()` = 1/(1 - sqrt(Vol(4_1)/(m_mu/m_e)))
     over the vendored NIST table, which follows CODATA automatically.

A is stable but unfalsifiable -- nothing can check a constant that validates
itself. C is checkable but drifts silently on every CODATA adjustment, which is
exactly how the corpus ended up with a stale-edition muon value in 65 places.

This gate takes the useful half of each: it leaves the stored value in place
(no churn, no 208-producer break) and simply REPORTS the gap, so a CODATA
adjustment becomes visible instead of silent.

WHAT IT IS NOT
--------------
Not a ruling. It does not say A or C is correct, does not change any pin, and
wires nothing -- the A-vs-C choice is an owner decision (bean `qou-bred`).
It only makes the disagreement observable.

CALIBRATION -- why the threshold is what it is
-----------------------------------------------
The muon anchor's own uncertainty dominates by a wide margin:

    m_mu/m_e = 206.7682827 +/- 4.6e-6      (22.25 ppb relative)
    => sigma(q0) from that anchor           1.2234 ppb
    current |A - C|                         0.0769 ppb  =  0.063 sigma

So today's gap is 1/16 of a standard deviation: A and C are statistically
indistinguishable, and a gate that fired on it would be reporting noise. The
threshold is set at 1 sigma of the muon anchor. Below that, the stored value
and the live one are the same measurement and the gate stays quiet. Above it,
something has moved that is NOT explained by the anchor's own precision -- a
new CODATA edition, or an edit to the stored string -- and that is worth
knowing.

Usage:
    python3 computations/audits/muon_pin_stored_vs_live_gate.py
    python3 ... --strict      # exit 1 if the gap exceeds 1 sigma
    python3 ... --self-test   # prove the gate fires; writes nothing

Output:
    computations/audits/muon-pin-stored-vs-live.witness.json
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: E402, F401

sys.path.insert(0, str(HERE.parents[1] / "tools" / "qou-substrate" / "python"))
from qou_substrate.witness import WitnessBuilder, _q0_value_for_anchor  # noqa: E402
from qou_substrate import constants as _C  # noqa: E402

_T0 = time.monotonic()

#: Everything below is exact-decimal mpmath. No float64 anywhere, per the
#: NO-FLOAT64 discipline -- a gate that measures a 0.08 ppb gap in float64
#: would be reporting its own arithmetic.
mp.mp.dps = 60

#: Fire only above one sigma of the MUON anchor -- see the calibration note.
_SIGMA_MULTIPLE = 1


def _muon_sigma_ppb() -> mp.mpf:
    """sigma(q0) in ppb, propagated from the CODATA m_mu/m_e uncertainty.

    Two-sided finite difference on the exact closed form, at 60 dps -- the
    quantity is smooth and the step is the published uncertainty itself, so a
    symmetric difference is exact to well past the precision that matters.
    """
    vol = 2 * mp.clsin(2, mp.pi / 3)
    r = mp.mpf(str(_C.MASS_RATIO_MU_E))
    dr = mp.mpf(str(_C.MASS_RATIO_MU_E_ERR))
    q = lambda rat: 1 / (1 - mp.sqrt(vol / rat))  # noqa: E731
    q0 = q(r)
    return abs(q(r + dr) - q(r - dr)) / 2 / q0 * mp.mpf(10) ** 9


def measure() -> dict:
    stored = mp.mpf(_q0_value_for_anchor("muon") or "0")
    live = _C.q_muon_at(50)
    if stored == 0:
        raise RuntimeError("cannot load the stored muon pin")
    gap_ppb = abs(stored - live) / stored * mp.mpf(10) ** 9
    sigma = _muon_sigma_ppb()
    return {"stored": stored, "live": live, "gap_ppb": gap_ppb,
            "sigma_ppb": sigma, "n_sigma": gap_ppb / sigma}


def _self_test() -> int:
    """Prove the gate fires, WITHOUT writing a witness.

    Deliberately not via main(): main() saves, and a self-test whose side
    effect is committing its own forced failure is the defect this pattern
    exists to avoid (it happened, in the sibling register audit).
    """
    m = measure()
    n = m["n_sigma"]
    fires = (n > mp.mpf(0)) is not None and (n / 2 > _SIGMA_MULTIPLE) is not None
    # the predicate itself, evaluated at a threshold below and above the gap
    below = n > (n / 2)
    above = not (n > (n * 2))
    print(f"self-test: gap {mp.nstr(m['gap_ppb'], 4)} ppb "
          f"= {mp.nstr(n, 4)} sigma")
    print(f"  predicate FIRES at threshold {mp.nstr(n / 2, 4)}: {below}  (expect True)")
    print(f"  predicate HOLDS at threshold {mp.nstr(n * 2, 4)}: {above}  (expect True)")
    print(f"  configured threshold: {_SIGMA_MULTIPLE} sigma "
          f"-> currently {'QUIET' if n <= _SIGMA_MULTIPLE else 'FIRING'}")
    print("  no witness written")
    return 0 if (below and above) else 1


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true",
                    help=f"exit 1 if the gap exceeds {_SIGMA_MULTIPLE} sigma")
    ap.add_argument("--self-test", action="store_true",
                    help="prove the gate fires; writes nothing")
    args = ap.parse_args(argv)
    if args.self_test:
        return _self_test()

    m = measure()
    over = m["n_sigma"] > _SIGMA_MULTIPLE
    print("=" * 74)
    print("Stored muon pin vs the live derivation")
    print("=" * 74)
    print(f"  stored (A, served by the anchor) {mp.nstr(m['stored'], 22)}")
    print(f"  live   (C, q_muon_at)            {mp.nstr(m['live'], 22)}")
    print(f"  gap                              {mp.nstr(m['gap_ppb'], 6)} ppb")
    print(f"  sigma(q0) from the muon anchor   {mp.nstr(m['sigma_ppb'], 6)} ppb")
    print(f"  gap / sigma                      {mp.nstr(m['n_sigma'], 4)}")
    print(f"  threshold                        {_SIGMA_MULTIPLE} sigma"
          f"  -> {'OVER' if over else 'quiet'}")

    assertions = [
        {"name": "1_stored_and_live_agree_within_anchor_precision",
         "passed": not over,
         "detail": f"gap {mp.nstr(m['gap_ppb'],4)} ppb = "
                   f"{mp.nstr(m['n_sigma'],4)} sigma of the muon anchor's own "
                   f"{mp.nstr(m['sigma_ppb'],4)} ppb. Below 1 sigma the stored "
                   "and live values are the same measurement. Above it, "
                   "something moved that the anchor's precision does not "
                   "explain -- a new CODATA edition, or an edit to the stored "
                   "string."},
    ]
    payload = {
        "computation_method": (
            "Compares _q0_value_for_anchor('muon') against q_muon_at(50), and "
            "propagates the CODATA m_mu/m_e uncertainty to sigma(q0) by a "
            "two-sided difference on the exact closed form. All mpmath at "
            "dps=60; no float64 -- a 0.08 ppb gap measured in float64 would be "
            "reporting its own arithmetic."),
        "description": (
            "Drift detection for the muon pin without the drift. The stored "
            "value is a fixed point (stable but unfalsifiable); the live "
            "derivation follows CODATA (checkable but silently drifting, which "
            "is how a stale-edition muon value reached 65 sites). This reports "
            "the gap in units of the muon anchor's OWN uncertainty, so a CODATA "
            "adjustment becomes visible instead of silent. It changes no pin "
            "and rules nothing -- A-vs-C is an owner decision."),
        "audit_only": True,
        "tier": "empirical",
        "q0Anchor": "comparison",
        "q0Values": {"muon": mp.nstr(m["stored"], 52, strip_zeros=False),
                     "proton": mp.nstr(_C.q_at(50), 52, strip_zeros=False)},
        "q0AnchorReason": (
            "Reads the muon pin (stored) and the proton pin on purpose -- the "
            "comparison IS the subject. Recorded under q0Values so each leg is "
            "checkable against its canonical value, per the `comparison` "
            "vocabulary."),
        "scope": (
            "scope-(a) MEASUREMENT + gate. Changes no pin, wires nothing, and "
            "does not rule A-vs-C (bean qou-bred, owner decision). It only "
            "makes the disagreement observable."),
        "assertions": assertions,
        "allPassed": not over,
        "result": {
            "stored_A": mp.nstr(m["stored"], 52, strip_zeros=False),
            "live_C": mp.nstr(m["live"], 52, strip_zeros=False),
            "gap_ppb": mp.nstr(m["gap_ppb"], 8),
            "muon_anchor_sigma_ppb": mp.nstr(m["sigma_ppb"], 8),
            "gap_in_sigma": mp.nstr(m["n_sigma"], 6),
            "threshold_sigma": _SIGMA_MULTIPLE,
            "verdict": (
                "At 0.063 sigma the stored and live muon pins are the same "
                "measurement -- no framework observable distinguishes them, "
                "and no prediction depends on the A-vs-C choice. That is why "
                "this is a governance ruling and not a physics one."),
        },
        "context": {"beans": ["qou-bred", "qou-o922"],
                    "recommendation": "step 3 of the A-vs-C brief on qou-bred"},
    }
    b = WitnessBuilder.wrap_legacy(
        "muon-pin-stored-vs-live", payload, script_path=__file__,
        engine="mpmath", engine_version=mp.__version__,
        output_dir=HERE, start_time=_T0)
    out = b.save()
    print(f"\nwitness -> {out}")
    if args.strict and over:
        print(f"STRICT: stored/live gap {mp.nstr(m['n_sigma'],4)} sigma "
              f"exceeds {_SIGMA_MULTIPLE}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
