#!/usr/bin/env python3
"""qbeta_cosh_q_sinh_q_candidate_scan.py — exhaustive scan of natural
q-hyperbolic candidates against empirical c_3 = -2.0693 at q_proton.

User-raised question 2026-06-01: 'is the swing/oscillation due to
missing cosh_q / sinh_q?' Tests 16 specific candidates with explicit
verdicts; expected outcome ALL REFUTED based on initial numerical
scan (closest matches ~0.7-0.9% off).

DISCIPLINE (CLAUDE.md no-7th-ansatz). This is a DIAGNOSTIC scan, not
a candidate-fishing run. The 16 candidates are pre-enumerated; the
goal is exhaustive documentation of cosh_q/sinh_q candidates so
future sessions can cite the audit instead of re-running.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
import time
from pathlib import Path

import mpmath as mp
from mpmath import mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))

from _precision import set_compute_dps, OUTPUT_DPS, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

try:
    from qou_substrate.constants import q_at
except ImportError:
    print("ERROR: qou_substrate not available", file=sys.stderr)
    sys.exit(1)


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()

    builder = WitnessBuilder("qbeta-cosh-q-sinh-q-candidate-scan",
                              engine="python+mpmath", start_time=t0)
    builder.set_description(
        "User-raised 2026-06-01: is c_3 deviation a missing cosh_q/"
        "sinh_q correction? Scan of 16 natural q-hyperbolic candidates "
        "at q_proton against empirical c_3 = -2.0693. Expected: ALL "
        "REFUTED (closest match ~0.7%)."
    )
    builder.set_audit_only(
        "docs/audits/2026-06-01-qbeta-cosh-q-sinh-q-candidate-scan.md"
    )

    q = q_at()
    q_inv = 1 / q
    h = q - q_inv
    h_tilde = mp.sqrt(q) - 1 / mp.sqrt(q)
    hbar = (q - 1) / q
    two_q = q + q_inv
    two_q_half = mp.sqrt(q) + 1 / mp.sqrt(q)

    EMPIRICAL = mpf("-2.0693")
    NOMINAL = mpf("-2")

    print(f"q             = {fmt(q)[:30]}")
    print(f"empirical c_3 = {EMPIRICAL}")
    print(f"nominal c_3   = {NOMINAL}")
    print(f"deviation     = {EMPIRICAL - NOMINAL} (≈ -0.0693)")
    print()

    candidates = {
        "-[2]_q (bar-sym)":          -two_q,
        "-[2]_q * (1 + hbar_q^2)":   -two_q * (1 + hbar ** 2),
        "-2 * cosh(h)":              -2 * mp.cosh(h),
        "-2 * cosh(h/2)":            -2 * mp.cosh(h / 2),
        "-2 * cosh(hbar_q)":         -2 * mp.cosh(hbar),
        "-2 - sinh(h)":              -2 - mp.sinh(h),
        "-2 - sinh(h)*h":            -2 - mp.sinh(h) * h,
        "-2 - h*hbar_q":             -2 - h * hbar,
        "-2 - h_tilde^2":            -2 - h_tilde ** 2,
        "-2 - h^2":                  -2 - h ** 2,
        "-2 - 2*h^2":                -2 - 2 * h ** 2,
        "-2 - h^2 * [2]_q":          -2 - h ** 2 * two_q,
        "-2 * (1 + h^2/2 * [2]_q)":  -2 * (1 + h ** 2 / 2 * two_q),
        "-[2]_q - sinh(h)/h":        -two_q - mp.sinh(h) / h,
        "-2 * cosh(h) * cosh(hbar_q)": -2 * mp.cosh(h) * mp.cosh(hbar),
        "-[2]_q^2 / 2":              -two_q ** 2 / 2,
    }

    results = {}
    print(f"{'candidate':<43s} {'value':>20s} {'err vs emp (%)':>16s}")
    for name, val in candidates.items():
        err_pct = float((val - EMPIRICAL) / abs(EMPIRICAL) * 100)
        results[name] = {
            "value": str(val),
            "err_pct": err_pct,
            "abs_err_pct": abs(err_pct),
        }
        marker = " ✓" if abs(err_pct) < 0.01 else ("  ←" if abs(err_pct) < 1 else "")
        print(f"  {name:<41s} {fmt(val)[:18]:>20s} {err_pct:+16.4f}{marker}")

    # Sort by |err| ascending to identify closest candidates
    sorted_results = sorted(candidates.keys(),
                            key=lambda k: results[k]["abs_err_pct"])
    closest_3 = sorted_results[:3]
    print()
    print("3 closest candidates (none < 0.01% — ALL REFUTED at compute precision):")
    for name in closest_3:
        err = results[name]["err_pct"]
        print(f"  {name:<43s} err = {err:+.4f}%")
    print()

    builder.add_data("q_proton", str(q))
    builder.add_data("empirical_c3_at_proton", str(EMPIRICAL))
    builder.add_data("nominal_c3", str(NOMINAL))
    builder.add_data("deviation", str(EMPIRICAL - NOMINAL))
    builder.add_data("substrate_quantities", {
        "h_full_q":      str(h),
        "h_tilde_half_q": str(h_tilde),
        "hbar_q":        str(hbar),
        "two_q_full":    str(two_q),
        "two_q_half":    str(two_q_half),
    })
    builder.add_data("candidate_scan", results)
    builder.add_data("closest_3_candidates", closest_3)
    builder.add_data("min_abs_err_pct", results[closest_3[0]]["abs_err_pct"])
    builder.add_data("verdict", (
        "ALL 16 CANDIDATES REFUTED at compute precision. Closest match "
        f"{closest_3[0]} at {results[closest_3[0]]['err_pct']:+.4f}% — far "
        "from the 10⁻⁵⁰ compute precision a Taylor-exact candidate would "
        "need to satisfy. The empirical c_3 deviation does NOT cleanly "
        "factor through any natural q-hyperbolic correction."
    ))
    builder.add_data("anti_pattern_guard", (
        "DO NOT wire any of these candidates. The 0.7-0.9% best matches "
        "are 'interesting' but well within the 8th-ansatz fit-trap zone. "
        "Per CLAUDE.md no-7th-ansatz discipline."
    ))

    builder.add_assertion(
        name="no_cosh_q_sinh_q_candidate_within_0.01_pct",
        computed=1.0 if results[closest_3[0]]["abs_err_pct"] > 0.01 else 0.0,
        expected=1.0,
        tolerance=0.0,
        source="Refutation: all 16 candidates miss empirical c_3 by > 0.01% at q_proton",
    )

    out = builder.save()
    print(f"✓ Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
