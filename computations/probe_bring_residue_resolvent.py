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
from _precision import fmt, set_compute_dps  # noqa: E402
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

        # Serialized from the mpf at output precision. `float(...)` here
        # truncated a 70-dps magnitude to a double before it reached the
        # witness (AGENTS.md §PROBES ARE NOT EXEMPT; bean qou-p77d).
        denom_abs = fmt(abs(denom))
        # Was `computed=denom_abs, expected=denom_abs` -- the magnitude as its
        # own expectation, so it passed even at an exact pole, which is the one
        # outcome the name excludes (bean qou-3e5m). The claim in `source` is
        # already an inequality; assert it. The magnitude is not lost -- it is
        # recorded beside the flag.
        w.add_data(f"denominator_magnitude_n{n}", denom_abs)
        w.add_assertion(
            name=f"denominator_nonzero_n{n}",
            computed=1 if abs(denom) > 0 else 0,
            expected=1,
            tolerance=0,
            source=f"|1 − h_q·q^{n}| > 0 at q₀; magnitude in "
                   f"data.denominator_magnitude_n{n}",
        )

        # The residual is ~1e-72 against a 1e-49 tolerance; the cast
        # reported 17 of its digits (bean qou-p77d).
        err = fmt(abs(roundtrip - 1))
        w.add_assertion(
            name=f"roundtrip_identity_n{n}",
            computed=err,
            expected="0",
            tolerance="1e-49",
            source=f"F_{n}·(1−h_q·q^{n}) = 1 at 50 dps",
        )

    # Bean qou-p77d: evaluate distinctness in mpf at 40 significant digits
    # rather than casting canonical_resolvent(q, n) to binary64 and calling
    # round(v, 20), which is a no-op past ~17 digits on a float64.
    vals = [canonical_resolvent(q, n) for n in POLE_ORDERS]
    distinct_count = len({mp.nstr(v, 40) for v in vals})
    w.add_assertion(
        name="resolvent_values_distinct",
        # NOT stringified: this is a count, already serialized as a JSON int,
        # and the integer-field audit requires declared counts stay ints.
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
