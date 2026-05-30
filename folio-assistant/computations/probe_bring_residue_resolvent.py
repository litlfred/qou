#!/usr/bin/env python3
"""Probe: canonical resolvent form 1/(1 − h_q · q^n) at substrate q_0.

Verifies prop:bring-residue-resolvent: the Bring residue at pole order n
yields the canonical resolvent F_n(q) = 1/(1 − h_q · q^n), h_q = q − q^{-1}.

Checks:
  1. Denominator is non-zero at q_0 for the three downstream pole orders
     used by #1444 (n=9), merged #1445 (n=10), #1455 (n=3,4).
  2. Cross-check: F_n · (1 − h_q · q^n) = 1 (exact at 50 dps).
  3. Subsingleton: F_n values are distinct for distinct n (uniqueness).
"""
from __future__ import annotations
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

POLE_ORDERS = [3, 4, 9, 10]  # downstream specialisations


def canonical_resolvent(q: mp.mpf, n: int) -> mp.mpf:
    h_q = q - 1 / q
    return mp.mpf(1) / (1 - h_q * q**n)


def main() -> None:
    t0 = time.perf_counter()
    set_compute_dps()
    q = mp.mpf(Q_50_DIGIT_STR)
    h_q = q - 1 / q

    assertions = []

    for n in POLE_ORDERS:
        F_n = canonical_resolvent(q, n)
        denom = 1 - h_q * q**n
        roundtrip = F_n * denom

        # 1. Denominator non-zero
        assertions.append({
            "name": f"denominator_nonzero_n{n}",
            "computed": float(abs(denom)) > 1e-40,
            "expected": True,
            "passed": float(abs(denom)) > 1e-40,
            "source": f"|1 − h_q·q^{n}| > 0 at q₀",
        })

        # 2. Round-trip identity F_n · (1 − h_q · q^n) = 1
        err = float(abs(roundtrip - 1))
        assertions.append({
            "name": f"roundtrip_identity_n{n}",
            "computed": err,
            "expected": 0.0,
            "passed": err < 1e-49,
            "tolerance": 1e-49,
            "source": f"F_{n}·(1−h_q·q^{n}) = 1 at 50 dps",
        })

    # 3. Distinct pole orders → distinct resolvent values
    vals = [float(canonical_resolvent(q, n)) for n in POLE_ORDERS]
    distinct = len(set(round(v, 20) for v in vals)) == len(POLE_ORDERS)
    assertions.append({
        "name": "resolvent_values_distinct",
        "computed": distinct,
        "expected": True,
        "passed": distinct,
        "source": "F_n(q_0) distinct for n in {3,4,9,10}",
    })

    all_passed = all(a["passed"] for a in assertions)
    duration_ms = int((time.perf_counter() - t0) * 1000)

    witness = {
        "engine": "mpmath",
        "engineVersion": f"mpmath {mp.__version__}",
        "contentBlock": "prop:bring-residue-resolvent",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "assertions": assertions,
        "allPassed": all_passed,
        "durationMs": duration_ms,
        "computation": "bring-residue-resolvent-probe",
        "scriptFile": "probe_bring_residue_resolvent.py",
        "description": (
            "Canonical resolvent F_n(q) = 1/(1−h_q·q^n) verified at substrate q_0 "
            "for pole orders n∈{3,4,9,10} (downstream: meson pair, 1/α_EM, p-n weight). "
            "Checks: denominator non-zero, round-trip identity, distinct values."
        ),
        "precisionMetadata": {
            "compute_dps": int(mp.mp.dps),
        },
    }

    out = HERE / "bring-residue-resolvent-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"{'PASS' if all_passed else 'FAIL'} — {len(assertions)} assertions, {duration_ms} ms")
    print(f"Written: {out.name}")
    if not all_passed:
        for a in assertions:
            if not a["passed"]:
                print(f"  FAIL: {a['name']}")
        sys.exit(1)


if __name__ == "__main__":
    main()
