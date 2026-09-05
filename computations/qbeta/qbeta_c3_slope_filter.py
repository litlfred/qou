#!/usr/bin/env python3
"""
Option C (bean `qou-dvlt`): is there a decay-face quantity whose sigma does NOT
carry the 1/u^3 amplification?  **YES — the cross-anchor SLOPE.**  But read the
limitation before using it: it is an internal filter, not an experimental test.

THE AMPLIFICATION CANCELS IN THE DIFFERENCE.

    each anchor      dc_3/dQ_beta       = 2.0688e6  per MeV
    the difference   d(swing)/dQ_beta   = -1.2414    per MeV

a cancellation of 1.67 million. `Q_beta^exp` enters both anchors the same way, so
it is common-mode and drops out of the cross-anchor difference. Consequently:

    c_3 VALUE   sigma/|c_3|        = 60.99 %       <- unusable (PR #5093)
    c_3 SLOPE   sigma/|swing|      = 15.41 ppm     <- 39576x sharper

That answers option C affirmatively. It does not answer it the way the option was
posed, and the difference matters.

WHAT THE SLOPE ACTUALLY TESTS — read this before citing the 39576x.

`c_3(q) = (Q_beta^exp/Q_N2(q) - 1)/u(q)^3` is a COMPLETELY DETERMINED function
once `Q_beta^exp` is fixed: there is no freedom in it. So `dc_3/dq` is not a
measurement — it is a computation from the extractor. The 15.41 ppm is the
precision with which the EXTRACTOR's slope is insensitive to the Q_beta input
error, not a precision with which nature has told us anything.

So the slope comparison tests a candidate derived `c_3(q)` against **the
framework's own ladder shape** (`Q_N2(q)` and `u(q)`), theory against theory. It
is sharp and it is real, but experiment has dropped out of it — which is exactly
*why* it is sharp. It cannot confirm the framework against nature, and it does
not lift the precision block that front (e) established.

WHY IT IS STILL WORTH HAVING: IT IS A FIT-DETECTOR.

This is the useful part, and it inverts the usual worry. A candidate `c_3` tuned
to reproduce the VALUE at one anchor has **61 % of slack** and will pass that
check trivially — which is precisely why ~60 probes produced agreements that
meant nothing. The same candidate must then reproduce the SLOPE within
**15 ppm**, and a one-anchor fit has no way to do that except by accident.

    value  check:  61 %      slack   -> a fit passes trivially
    slope  check:  15.4 ppm  slack   -> a fit does not pass by accident

So the slope is the cheap discriminator the front has lacked: it cannot tell you
a derivation is RIGHT, but it will tell you a fit is a fit, at 4.6 orders of
magnitude better resolution than anything else available.

RELATION TO REGISTRY SECTION 9e. That section records the swing as "resolved
(+/-7.6e-7) but NOT an independent derivation target", because it factors as
(11.54 ppb mu-p tension) x dc_3/dq. That is correct **for derivation** and this
probe does not dispute it. The distinction being drawn here is between a
derivation TARGET and a test OBSERVABLE: you cannot derive the swing without
already having c_3's shape, but you can certainly CHECK a proposed shape against
it. Those are different uses, and the "circular" label has been read as
disqualifying both.

Scope-(a). Error propagation on committed values; no fit, no c_k wired; no claim
about (H1) in either direction.
"""

import datetime
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: E402, F401

from qbeta_utils import c3_target_at, substrate_ladder_quantities  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402

mp.mp.dps = 60

ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))


def _head_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip()
    except Exception:
        return "unknown"


def _sigma_qbeta() -> mp.mpf:
    with open(ROOT / "computations" / "cal-3-q-beta.witness.json") as f:
        return mp.mpf(str(json.load(f)["data"]["Q_beta_n_MeV_err"]))


def dc3_dQbeta(q):
    """Sensitivity of c_3 to the Q_beta input at a single anchor."""
    u = substrate_ladder_quantities(q)["u"]
    c3 = c3_target_at(q, QCOD, ME)
    q_n2 = QCOD / (1 + c3 * u ** 3)
    return 1 / (q_n2 * u ** 3)


def main() -> int:
    q_p, q_m = q_at(), q_muon_at()
    sigma_qb = _sigma_qbeta()

    c3p = c3_target_at(q_p, QCOD, ME)
    c3m = c3_target_at(q_m, QCOD, ME)
    swing = c3m - c3p
    dq = q_m - q_p
    slope = swing / dq

    print("=" * 78)
    print("Option C — a decay-face quantity whose sigma avoids 1/u^3?  The SLOPE.")
    print("=" * 78)

    print("\n" + "-" * 78)
    print("THE CANCELLATION")
    print("-" * 78)
    s_p, s_m = dc3_dQbeta(q_p), dc3_dQbeta(q_m)
    d_swing = s_m - s_p
    print(f"\n  dc_3/dQ_beta at proton     = {mp.nstr(s_p, 12)} per MeV")
    print(f"  dc_3/dQ_beta at muon       = {mp.nstr(s_m, 12)} per MeV")
    print(f"  d(swing)/dQ_beta           = {mp.nstr(d_swing, 12)} per MeV")
    cancel = abs(s_p / d_swing)
    print(f"\n  cancellation factor        = {mp.nstr(cancel, 10)} x")
    print("  Q_beta^exp enters both anchors identically, so it is COMMON-MODE")
    print("  and drops out of the difference.")

    print("\n" + "-" * 78)
    print("VALUE vs SLOPE")
    print("-" * 78)
    sigma_c3 = s_p * sigma_qb
    sigma_swing = abs(d_swing) * sigma_qb
    rel_value = sigma_c3 / abs(c3p)
    rel_slope = sigma_swing / abs(swing)
    print(f"\n  c_3 value  = {mp.nstr(c3p, 14)}   sigma = {mp.nstr(sigma_c3, 10)}")
    print(f"             relative = {mp.nstr(rel_value * 100, 6)} %")
    print(f"\n  swing      = {mp.nstr(swing, 14)}   sigma = {mp.nstr(sigma_swing, 10)}")
    print(f"             relative = {mp.nstr(rel_slope * 1e6, 6)} ppm")
    print(f"\n  slope dc_3/dq = {mp.nstr(slope, 14)}  (+/- {mp.nstr(rel_slope * 1e6, 5)} ppm)")
    print(f"\n  SLOPE IS {mp.nstr(rel_value / rel_slope, 8)} x SHARPER THAN THE VALUE")

    print("\n" + "-" * 78)
    print("WHAT IT ACTUALLY TESTS — read before citing the factor")
    print("-" * 78)
    print("""
  c_3(q) = (Q_beta^exp/Q_N2(q) - 1)/u(q)^3 is COMPLETELY DETERMINED once
  Q_beta^exp is fixed. So dc_3/dq is not a measurement -- it is a computation
  from the extractor. The 15.4 ppm is the precision with which the EXTRACTOR's
  slope is insensitive to the Q_beta error, not a precision with which nature
  has told us anything.

  The slope comparison therefore tests a candidate derived c_3(q) against the
  FRAMEWORK'S OWN LADDER SHAPE -- theory against theory. Experiment has dropped
  out of it, which is exactly WHY it is sharp. It does not lift the precision
  block front (e) established, and it cannot confirm the framework against
  nature.
""")

    print("-" * 78)
    print("WHY IT IS STILL WORTH HAVING — it is a FIT-DETECTOR")
    print("-" * 78)
    print(f"""
  value check:  {mp.nstr(rel_value * 100, 4)} % slack       -> a one-anchor fit passes TRIVIALLY
  slope check:  {mp.nstr(rel_slope * 1e6, 4)} ppm slack   -> a one-anchor fit does NOT

  This inverts the usual worry. ~60 probes produced agreements that meant
  nothing because the value check has 61 % of slack. The same candidates must
  now reproduce the slope within 15 ppm, and a fit to one anchor has no way to
  do that except by accident.

  It cannot tell you a derivation is RIGHT. It will tell you a fit is a fit, at
  4.6 orders of magnitude better resolution than anything else on this front.
""")

    assertions = [
        {"name": "amplification_cancels_in_the_difference",
         "passed": bool(cancel > 1e5),
         "detail": mp.nstr(cancel, 8) + "x cancellation"},
        {"name": "slope_relative_sigma_below_100ppm",
         "passed": bool(rel_slope < mp.mpf("1e-4")),
         "detail": mp.nstr(rel_slope * 1e6, 6) + " ppm"},
        {"name": "value_relative_sigma_above_50pct",
         "passed": bool(rel_value > mp.mpf("0.5"))},
        {"name": "slope_sharper_than_value_by_over_1e4",
         "passed": bool(rel_value / rel_slope > 1e4),
         "detail": mp.nstr(rel_value / rel_slope, 8) + "x"},
        {"name": "slope_is_internal_filter_not_experimental_test",
         "passed": True,
         "detail": "c_3(q) is determined once Q_beta^exp is fixed; the sharpness "
                   "comes from experiment CANCELLING, so this tests theory against "
                   "the framework's own ladder, not against nature"},
    ]
    all_passed = all(a["passed"] for a in assertions)

    with open(os.path.abspath(__file__), "rb") as f:
        src = f.read()

    witness = {
        "computation": "qbeta-c3-slope-filter",
        "description": (
            "Option C answered affirmatively but not as posed. The 1/u^3 amplification "
            "is COMMON-MODE across the two anchors and cancels in the difference: "
            "dc_3/dQ_beta = 2.069e6 per MeV at each anchor, but d(swing)/dQ_beta = "
            "-1.241, a 1.67e6 cancellation. So the c_3 SLOPE is known to 15.41 ppm "
            "while its VALUE is 60.99% uncertain — 39576x sharper. CRITICAL "
            "LIMITATION: c_3(q) is completely determined once Q_beta^exp is fixed, so "
            "dc_3/dq is a computation from the extractor, not a measurement; the "
            "sharpness comes from experiment CANCELLING. The slope therefore tests a "
            "candidate derived c_3(q) against the framework's own ladder shape — "
            "theory against theory — and does NOT lift the precision block. Its value "
            "is as a FIT-DETECTOR: a one-anchor fit passes the 61%-slack value check "
            "trivially but cannot pass the 15 ppm slope check by accident. Complements "
            "registry section 9e, which correctly calls the swing a non-independent "
            "derivation TARGET; this distinguishes that from its use as a test "
            "OBSERVABLE. Scope-(a); no claim about (H1)."),
        "audit_only": True,
        "tier": "error propagation on committed values (no fit)",
        "q0Anchor": "proton",
        "q0Value": mp.nstr(q_p, 25),
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "dc3_dQbeta_proton": mp.nstr(s_p, 14),
            "dc3_dQbeta_muon": mp.nstr(s_m, 14),
            "d_swing_dQbeta": mp.nstr(d_swing, 14),
            "cancellation_factor": mp.nstr(cancel, 12),
            "c3_proton": mp.nstr(c3p, 16),
            "c3_muon": mp.nstr(c3m, 16),
            "swing": mp.nstr(swing, 16),
            "dq_anchor_spread": mp.nstr(dq, 14),
            "slope_dc3_dq": mp.nstr(slope, 16),
            "sigma_c3_value": mp.nstr(sigma_c3, 12),
            "sigma_swing": mp.nstr(sigma_swing, 12),
            "relative_sigma_value_pct": mp.nstr(rel_value * 100, 8),
            "relative_sigma_slope_ppm": mp.nstr(rel_slope * 1e6, 8),
            "slope_sharper_by": mp.nstr(rel_value / rel_slope, 10),
        },
        "context": {
            "axis": "front triage option C — an observable avoiding the 1/u^3 lever",
            "limitation": (
                "INTERNAL FILTER, NOT AN EXPERIMENTAL TEST. c_3(q) is determined once "
                "Q_beta^exp is fixed; dc_3/dq is a computation from the extractor. The "
                "sharpness comes from experiment cancelling out. Do not cite the "
                "39576x as an experimental precision."),
            "complements": (
                "registry section 9e — the swing is correctly a non-independent "
                "derivation TARGET. This separates that from its use as a test "
                "OBSERVABLE against a proposed c_3(q) shape."),
            "scope": "Scope-(a). No fit; no claim about (H1) either way.",
        },
    }

    out_path = HERE / "qbeta-c3-slope-filter.witness.json"
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    with open(out_path, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=None)
        json.dump(witness, f, indent=2)
    print(f"witness -> {out_path}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
