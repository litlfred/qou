#!/usr/bin/env python3
"""What an energy UPPER bound would have to achieve -- and it is not availability.

Bean qou-o6ml. The sibling result (LowerBoundCannotConstrainADifference.lean)
shows a lower bound on each of two energies constrains their difference not at
all, and names the missing ingredient: an UPPER bound, which the Freedman-He
link bound does not supply. The obvious next move is to go acquire one.

This probe asks the PRIOR question -- would an upper bound help? -- and the
answer is no, for a reason that needs no carrier, no flux value and no
acquisition.

THE ARITHMETIC. With two-sided bounds B_i <= E_i <= U_i, the difference is
pinned to [B1 - U2, U1 - B2], an interval of width exactly

    (U1 - B1) + (U2 - B2)          -- the SUM of the two slacks

For that to be narrower than the split it is meant to explain, the combined
slack must beat the split. But the mirror split is a DIFFERENCE OF TWO LARGE,
NEARLY EQUAL ENERGIES. Under the arc's own model (vertex-transitive carrier,
flux by charge: Phi_p on the Z protons, Phi_n on the N neutrons, d = 1):

    dE = c*(Phi_p - Phi_n)          against       E = c*(Z*Phi_p + N*Phi_n)

so if the fluxes lie within a factor r of each other,

    dE / E  <=  (r - 1) / A

(proved in QOU/Mass/MirrorSplitIsASmallFractionOfTheEnergy.lean,
`split_fraction_bound`, sorry-free). The budget FALLS with A: the requirement
sharpens as the nucleus grows rather than relaxing. Freedman-He-type bounds are
order-of-magnitude estimates; nothing in that literature is tight to a percent.

AND THE LIBRARY HOLDS NOTHING ANYWAY -- asserted here as a live scan rather than
a remembered grep, so that if the source is ever acquired the assertion flips and
prompts a revisit instead of this file quietly going stale.

Nothing wired. EXPLORATORY.
"""

from __future__ import annotations

import json
import pathlib
import re

import mpmath as mp

import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402

# Precision must be raised BEFORE any mpf literal below: at import time mp.dps is
# still mpmath's default 15 (~binary64) and a literal rounded there cannot be
# recovered by raising dps afterwards. Gate: mpf_import_time_dps_audit.py.
set_compute_dps()

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent
SERIES_WITNESS = HERE / "em-linking-mirror-series.witness.json"

# Flux-ratio bounds to tabulate. r = 1 is the degenerate equal-flux case (zero
# split); r = 2 means the proton tube carries at most twice the neutron tube's
# flux; r = 10 is a deliberately generous allowance.
RATIOS = ["1.1", "1.5", "2", "10"]

# The upper-bound technology one would go looking for.
ACQUISITION_TERMS = re.compile(r"ropelength|ideal knot", re.IGNORECASE)
SCAN_ROOTS = ["docs", "computations", "content", "library"]


def load_ladder() -> list[dict]:
    with SERIES_WITNESS.open() as fh:
        return json.load(fh)["data"]["series"]


def scan_for_acquisition_terms() -> dict:
    """Live scan for ropelength / ideal-knot material anywhere in the repo.

    Counted as FILES, and the matched paths are recorded, so a future acquisition
    flips the assertion rather than leaving this probe asserting a stale absence.
    """
    hits: list[str] = []
    for root in SCAN_ROOTS:
        base = REPO / root
        if not base.is_dir():
            continue
        for path in base.rglob("*"):
            if not path.is_file():
                continue
            if path.suffix.lower() not in {".md", ".txt", ".json", ".py", ".ts", ".lean"}:
                continue
            try:
                text = path.read_text(errors="ignore")
            except OSError:
                continue
            if ACQUISITION_TERMS.search(text):
                rel = str(path.relative_to(REPO))
                # This probe and its own witness name the terms by construction.
                if "upper_bound_precision_budget" in rel or "MirrorSplitIsASmall" in rel:
                    continue
                hits.append(rel)
    return {"count": len(hits), "paths": sorted(hits)[:20]}


def main() -> int:
    ladder = load_ladder()
    A_min = mp.mpf(ladder[0]["A"])
    A_max = mp.mpf(ladder[-1]["A"])

    # dE/E <= (r-1)/A, tabulated over the ladder for each ratio bound.
    budget = {}
    for r_s in RATIOS:
        r = mp.mpf(r_s)
        budget[r_s] = {
            str(int(row["A"])): mp.nstr((r - 1) / mp.mpf(row["A"]), 8)
            for row in ladder
        }

    r2 = mp.mpf("2")
    budget_at_A3 = (r2 - 1) / A_min
    budget_at_A63 = (r2 - 1) / A_max
    tightening = budget_at_A3 / budget_at_A63

    # Monotone decreasing in A, checked rather than asserted from the formula.
    seq = [(mp.mpf(row["A"]), (r2 - 1) / mp.mpf(row["A"])) for row in ladder]
    strictly_falling = all(seq[i][1] > seq[i + 1][1] for i in range(len(seq) - 1))

    acq = scan_for_acquisition_terms()

    b = WitnessBuilder(
        name="em-linking-upper-bound-precision-budget",
        _script_path=pathlib.Path(__file__),
        output_dir=HERE,
    )
    b.set_audit_only("docs/audits/2026-08-01-em-linking-reads-round1.md")
    b.set_description(
        "EXPLORATORY. Asks whether acquiring an energy UPPER bound would rescue the "
        "Freedman-He route, and finds it would not -- for a reason needing no carrier, "
        "no flux value and no acquisition. A two-sided bound pins the mirror split to "
        "an interval of width (U1-B1)+(U2-B2), the SUM of the two slacks; but the split "
        "is a difference of two large nearly-equal energies, at most (r-1)/A of the "
        "energy when the two fluxes lie within a factor r. So the combined relative "
        "slack must beat (r-1)/A -- 1.6% at A=63 for r=2, and TIGHTENING with A. "
        "Freedman-He-type bounds are order-of-magnitude. Also scans the repo live: "
        "zero ropelength / ideal-knot material anywhere, asserted so that a future "
        "acquisition flips the assertion instead of this going stale. Companion to "
        "QOU/Mass/MirrorSplitIsASmallFractionOfTheEnergy.lean. Nothing wired."
    )

    b.add_data("the_arithmetic", {
        "two_sided_interval": "[B1 - U2, U1 - B2]",
        "interval_width": "(U1 - B1) + (U2 - B2)  -- the SUM of the two slacks",
        "model": "dE = c*(Phi_p - Phi_n) against E = c*(Z*Phi_p + N*Phi_n), d = 1",
        "bound": "dE/E <= (r-1)/A when Phi_n <= Phi_p <= r*Phi_n",
        "lean": ("QOU/Mass/MirrorSplitIsASmallFractionOfTheEnergy.lean, "
                 "`split_fraction_bound` -- sorry-free, lean-direct exit 0"),
    })
    b.add_data("budget_by_ratio_and_A", budget)
    b.add_data("headline", {
        "A_range": f"{int(A_min)}..{int(A_max)}",
        "budget_at_A3_r2": mp.nstr(budget_at_A3, 8),
        "budget_at_A63_r2": mp.nstr(budget_at_A63, 8),
        "tightening_factor": mp.nstr(tightening, 8),
        "reading": ("the requirement SHARPENS with A by exactly the ratio A_max/A_min; "
                    "a bigger nucleus is a harder target, not an easier one"),
    })
    b.add_data("acquisition_scan", {
        "terms": "ropelength | ideal knot",
        "roots": SCAN_ROOTS,
        "file_hits": acq["count"],
        "paths": acq["paths"],
        "why_this_is_here": ("the cheaper-looking answer to 'the route needs an upper "
                             "bound' is 'go acquire one'. Recorded as a LIVE scan so a "
                             "future acquisition flips this assertion; but note the "
                             "precision argument above is independent of it, so "
                             "acquiring the source would not rescue the route"),
    })
    b.add_data("what_this_does_NOT_exclude", {
        "vanishing_neutron_flux": ("a model with Phi_n -> 0 has unbounded r and escapes "
                                   "the fraction bound entirely; NOT refuted here"),
        "eq43_itself": "untouched -- it remains a true lower bound",
        "scope": "scope-(a) on the same model class the sibling Lean file excludes",
    })

    b.add_assertion(
        name="split_is_at_most_1_6_percent_of_the_energy_at_A63",
        computed=mp.nstr(budget_at_A63, 8),
        expected="0.015873016",
        tolerance="1e-8",
        unit="fraction of E (r=2)",
        source=("(r-1)/A at A=63 with a factor-2 flux ratio. The combined relative slack "
                "of any two-sided bound must beat this for the interval to be narrower "
                "than the split it is meant to explain."),
    )
    b.add_assertion(
        name="budget_tightens_with_A_by_exactly_A_max_over_A_min",
        computed=mp.nstr(tightening, 8),
        expected="21",
        tolerance="1e-8",
        unit="ratio",
        source=("63/3 = 21. The precision requirement sharpens 21-fold across the "
                "ladder, so the route gets harder where the data is best, not easier."),
    )
    b.add_assertion(
        name="budget_is_strictly_decreasing_in_A",
        computed="1" if strictly_falling else "0",
        expected="1",
        tolerance="0",
        unit="bool",
        source=("checked across all 31 rungs rather than read off the formula, so a "
                "future change to the ladder cannot silently break the monotonicity "
                "the reading depends on."),
    )
    b.add_assertion(
        name="no_ropelength_or_ideal_knot_source_in_the_repo",
        computed=str(acq["count"]),
        expected="0",
        tolerance="0",
        unit="files",
        source=("LIVE scan of docs/, computations/, content/ and library/ (both the "
                "sections/ and ocr/ tiers, all library directories). Zero. Asserted so "
                "that acquiring such a source FLIPS this assertion and prompts a "
                "revisit -- rather than this probe asserting a remembered absence. Note "
                "the precision argument does not depend on this: acquisition would not "
                "rescue the route."),
    )

    out = b.save()
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
