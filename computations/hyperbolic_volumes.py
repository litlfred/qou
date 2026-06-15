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

Records `Vol(5_2)` at 50 decimal digits from SnapPy high precision
(ManifoldHP 3.3.2, in-sandbox 2026-06-12; positively-oriented
solution, cross-checked against the live census in
`audits/snappy-census-volume-verification.witness.json`).  This
replaces the former 15-dps literature anchor `2.82812208833410`
(Adams–Hildebrand–Weeks 1991), whose digits 13–15 were a
transcription error (true continuation `...330783...`).  The
15-digit rounding feeds the `:leanval[vol_5_2]` tag in
`MostowRigidity.knot5_2`.

The volume gap `mostow_gap = Vol(5_2) − Vol(4_1)` is computed from
both quantities and exported as `gap_5_2_minus_4_1_15`; the older
`gap_lower_bound = 0.5` is retained for backward compatibility with
`MostowRigidity.figureEight.mostow_gap` (which uses a conservative
under-bound rather than the precise gap, so the field stays robust
to small future precision shifts in either Vol(5_2) or Vol(4_1)).

This module follows the standard QOU witness conventions
(`witness_base.WitnessBuilder`); the single source of truth for the
Lean literals is the per-quantity `*_decimal_15` data fields, which
the `:leanval` codemod (`content/pipeline/codemod-leanval.ts`)
substitutes on demand.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

# Allow this script to be run from anywhere — make sibling helpers
# importable without manual PYTHONPATH munging.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from mpmath import mp, mpf  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import vol_4_1_at  # noqa: E402

# ── Census constants ─────────────────────────────────────────────
# Vol(5_2) is the second-smallest known orientable cusped hyperbolic
# knot-complement volume (Adams–Hildebrand–Weeks 1991). 50-dps value
# from SnapPy ManifoldHP 3.3.2 (in-sandbox 2026-06-12), cross-checked
# in audits/snappy-census-volume-verification.witness.json. The old
# 15-dps literature anchor "2.82812208833410" had a digit-13–15
# transcription error.
VOL_5_2_SNAPPY_HP_50 = "2.8281220883307831627638988092766349427709813173006"


def main() -> int:
    mp.dps = 60  # 50-digit precision + 10 guard digits

    vol_4_1 = vol_4_1_at(50)
    vol_4_1_50 = mp.nstr(vol_4_1, 50, strip_zeros=False)
    vol_4_1_15 = mp.nstr(vol_4_1, 15, strip_zeros=False)

    vol_5_2 = mpf(VOL_5_2_SNAPPY_HP_50)
    vol_5_2_50 = mp.nstr(vol_5_2, 50, strip_zeros=False)
    vol_5_2_15 = mp.nstr(vol_5_2, 15, strip_zeros=False)

    # Computed gap from both literals.  Matches Vol(5_2) - Vol(4_1)
    # ≈ 0.798238875515... when both are precise to 15 dps.
    gap_5_2_minus_4_1 = vol_5_2 - vol_4_1
    gap_5_2_minus_4_1_15 = mp.nstr(gap_5_2_minus_4_1, 15, strip_zeros=False)

    # Conservative gap (legacy, kept for the figureEight class field):
    # well below Vol(5_2) - Vol(4_1) ≈ 0.798.
    gap_lower_bound = mpf("0.5")

    in_window = mpf("2.0298") < vol_4_1 < mpf("2.0299")
    matches_5dps = mp.nstr(vol_4_1, 5, strip_zeros=False) == "2.0299"
    gap_below_lit = gap_lower_bound < gap_5_2_minus_4_1
    vol_5_2_above_4_1 = vol_5_2 > vol_4_1

    w = WitnessBuilder("hyperbolic-volumes", engine="mpmath")
    w.set_description(
        "Hyperbolic volumes used by the MostowRigidity class instances "
        "in the encounter chapter.  Vol(4_1) computed via the Clausen-"
        "function identity at 50 decimal digits "
        "(Vol(4_1) = 2 · Cl_2(pi/3)); Vol(5_2) at 50 dps from SnapPy "
        "ManifoldHP 3.3.2 (replaces the 15-dps AHW-1991 anchor whose "
        "digits 13-15 were a transcription error).  "
        "Source of truth for the Lean literals "
        "MostowRigidity.figureEight.volume / .mostow_gap and "
        "MostowRigidity.knot5_2.volume via the :leanval[vol_4_1], "
        ":leanval[vol_5_2], :leanval[mostow_gap_4_1] tags."
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
        name="vol_5_2_above_vol_4_1",
        computed=str(vol_5_2_above_4_1),
        expected="True",
        source="hyperbolic_volumes",
    )
    w.add_assertion(
        name="gap_lower_bound_below_computed_gap",
        computed=str(gap_below_lit),
        expected="True",
        source="hyperbolic_volumes",
    )

    w.add_data("vol_4_1_decimal_50", vol_4_1_50)
    w.add_data("vol_4_1_decimal_15", vol_4_1_15)
    w.add_data("vol_5_2_decimal_50", vol_5_2_50)
    w.add_data("vol_5_2_decimal_15", vol_5_2_15)
    w.add_data(
        "vol_5_2_source",
        "SnapPy ManifoldHP 3.3.2 (in-sandbox 2026-06-12); "
        "Adams-Hildebrand-Weeks 1991; cross-check: "
        "snappy-census-volume-verification witness",
    )
    w.add_data("gap_5_2_minus_4_1_15", gap_5_2_minus_4_1_15)
    w.add_data("gap_lower_bound", str(gap_lower_bound))
    w.add_data(
        "gap_note",
        "gap_lower_bound is a conservative under-approximation of "
        "Vol(5_2) - Vol(4_1); see gap_5_2_minus_4_1_15 for the "
        "computed value at 15 dps.  Both volumes are now 50-dps "
        "(Clausen identity / SnapPy ManifoldHP).",
    )
    w.save()

    ok = (
        in_window
        and matches_5dps
        and vol_5_2_above_4_1
        and gap_below_lit
    )
    print(
        f"hyperbolic_volumes: {'PASS' if ok else 'FAIL'}  "
        f"Vol(4_1) = {vol_4_1_15}  Vol(5_2) = {vol_5_2_15}  "
        f"gap = {gap_5_2_minus_4_1_15}"
    )
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
