#!/usr/bin/env python3
"""
Hyperbolic-volume witness for the encounter-chapter `MostowRigidity`
class instances.

Computes:

    Vol(4_1) = 2 · Cl_2(π/3)        (figure-eight knot complement;
                                     Cao-Meyerhoff 2001 minimum)

at 50 decimal digits via the Clausen-function identity (mpmath
`clsin`), and rounds to a 15-digit decimal string for use as a Lean
literal under the `:leanval[vol_4_1]` tag.

`Vol(5_2)` is **not** computed here — its hyperbolic structure
requires shape parameters of the 5_2 ideal triangulation and is
typically obtained from SnapPy.  The witness instead records a
**conservative literature lower bound** `gap_lower_bound = 0.5` on

    Vol(5_2) - Vol(4_1) ≈ 2.828 - 2.030 ≈ 0.798

which is what the `MostowRigidity.figureEight.mostow_gap` field
needs.  When SnapPy is added to the witness-pipeline image, this
script will be extended to emit a verified `vol_5_2` field.

This module follows the standard QOU witness conventions
(`witness_base.WitnessBuilder`); the single source of truth for
the displayed Lean literal is the `vol_4_1_decimal_15` data field,
which the `:leanval` codemod (`content/pipeline/codemod-leanval.ts`)
substitutes on demand.
"""
from __future__ import annotations

import sys
from pathlib import Path

# Allow this script to be run from anywhere — make sibling helpers
# importable without manual PYTHONPATH munging.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from mpmath import mp, mpf  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import vol_4_1_at  # noqa: E402


def main() -> int:
    mp.dps = 60  # 50-digit precision + 10 guard digits

    vol_4_1 = vol_4_1_at(50)
    vol_4_1_50 = mp.nstr(vol_4_1, 50, strip_zeros=False)
    vol_4_1_15 = mp.nstr(vol_4_1, 15, strip_zeros=False)

    # Conservative gap: well below Vol(5_2) - Vol(4_1) ≈ 0.798.
    # Literature-derived safe under-bound, not internally computed.
    gap_lower_bound = mpf("0.5")

    in_window = mpf("2.0298") < vol_4_1 < mpf("2.0299")
    matches_5dps = mp.nstr(vol_4_1, 5, strip_zeros=False) == "2.0299"
    gap_below_lit = gap_lower_bound < mpf("0.798")

    w = WitnessBuilder("hyperbolic-volumes", engine="mpmath")
    w.set_description(
        "Hyperbolic volumes used by the MostowRigidity class instances "
        "in the encounter chapter.  Vol(4_1) computed via the Clausen-"
        "function identity at 50 decimal digits "
        "(Vol(4_1) = 2 · Cl_2(pi/3)); the gap_lower_bound is a "
        "conservative literature under-approximation.  Source of truth "
        "for the Lean literal volume := … in MostowRigidity.figureEight "
        "via the :leanval[vol_4_1] tag."
    )
    w.set_content_block("prop:mostow-confinement")
    w.add_parameter("dps", 50)
    w.add_parameter("guard_digits", 10)

    # Assertions phrased as equality checks (the framework does
    # string-equality on computed vs expected to set `passed`).
    w.add_assertion(
        name="vol_4_1_in_cao_meyerhoff_window",
        computed=str(in_window),
        expected="True",
        source="hyperbolic_volumes",
    )
    w.add_assertion(
        name="vol_4_1_matches_5dps_literature",
        computed=mp.nstr(vol_4_1, 5, strip_zeros=False),
        expected="2.0299",
        source="hyperbolic_volumes",
    )
    w.add_assertion(
        name="gap_lower_bound_below_literature",
        computed=str(gap_below_lit),
        expected="True",
        source="hyperbolic_volumes",
    )

    w.add_data("vol_4_1_decimal_50", vol_4_1_50)
    w.add_data("vol_4_1_decimal_15", vol_4_1_15)
    w.add_data("gap_lower_bound", str(gap_lower_bound))
    w.add_data(
        "gap_note",
        "Conservative under-bound on Vol(5_2) - Vol(4_1) ≈ 0.798; "
        "not internally computed.  Replace with a SnapPy-computed "
        "witness once SnapPy is added to the pipeline image.",
    )
    w.save()

    ok = in_window and matches_5dps and gap_below_lit
    print(
        f"hyperbolic_volumes: {'PASS' if ok else 'FAIL'}  "
        f"Vol(4_1) = {vol_4_1_15}  gap≥{gap_lower_bound}"
    )
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
