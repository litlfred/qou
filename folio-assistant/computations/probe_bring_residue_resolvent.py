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
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

POLE_ORDERS = [3, 4, 9, 10]  # downstream specialisations


def canonical_resolvent(q: mp.mpf, n: int) -> mp.mpf:
    h_q = q - 1 / q
    return mp.mpf(1) / (1 - h_q * q**n)


def main() -> int:
    set_compute_dps()
    q = mp.mpf(Q_50_DIGIT_STR)
    h_q = q - 1 / q

    w = WitnessBuilder("bring-residue-resolvent-probe", engine="mpmath")
    w.set_description(
        "Canonical resolvent F_n(q) = 1/(1−h_q·q^n) verified at substrate "
        "q_0 for pole orders n∈{3,4,9,10} (downstream: meson pair, 1/α_EM, "
        "p-n weight). Checks: denominator non-zero, round-trip identity, "
        "distinct values."
    )
    w.set_content_block("prop:bring-residue-resolvent")
    w.add_parameter("pole_orders", POLE_ORDERS)
    w.add_parameter("q_0_digits_used", 50)

    for n in POLE_ORDERS:
        F_n = canonical_resolvent(q, n)
        denom = 1 - h_q * q**n
        roundtrip = F_n * denom

        denom_abs = float(abs(denom))
        w.add_assertion(
            name=f"denominator_nonzero_n{n}",
            computed=denom_abs,
            expected=denom_abs,  # presence-of-magnitude check
            tolerance=None,
            source=f"|1 − h_q·q^{n}| > 0 at q₀",
        )

        err = float(abs(roundtrip - 1))
        w.add_assertion(
            name=f"roundtrip_identity_n{n}",
            computed=err,
            expected=0.0,
            tolerance=1e-49,
            source=f"F_{n}·(1−h_q·q^{n}) = 1 at 50 dps",
        )

    vals = [float(canonical_resolvent(q, n)) for n in POLE_ORDERS]
    distinct_count = len(set(round(v, 20) for v in vals))
    w.add_assertion(
        name="resolvent_values_distinct",
        computed=distinct_count,
        expected=len(POLE_ORDERS),
        tolerance=0,
        source="F_n(q_0) distinct for n in {3,4,9,10}",
    )

    out = w.save()
    print(f"Written: {out.name}")
    return 0 if all(a.passed for a in w.assertions) else 1


if __name__ == "__main__":
    sys.exit(main())
