#!/usr/bin/env python3
"""Strategy I (Yekutieli per-cell curvature) — falsifiable numerical test.

Per docs/audits/2026-05-22-yekutieli-percell-conjecture-formalized.md,
the Yekutieli structural argument from
docs/audits/2026-05-18-conjecture-proof-step3-yekutieli.md proposes:

    λ_scale  =  5/2  −  G · h²  +  O(h⁴)   (audit's "Reading A")

with 5/2 from half-symmetric H_4 Wedderburn count at q=1 and -G
from per-cell Yekutieli curvature on 𝓑_3's 8-fold tessellation
(load-bearing conjecture: half-sym projection extracts ONE cell).

A natural alternative reading (audit corrected for double-counting):
the Yekutieli curvature contribution is ADDED to the Wedderburn-sum
h² coefficient, giving:

    λ_scale  =  5/2  +  (3/4 − G) · h²  +  O(h⁴)   (Reading B)

This probe computes BOTH readings at q_0 + MPFR-50dps and compares
to:
  - Family A (the framework's substrate λ_scale per PR #895)
  - CODATA-derived closure target (the retired empirical match)

The probe is FALSIFIABLE in the sense that:
  - If Reading A matches CODATA to MPFR floor: strong empirical
    support for the Yekutieli load-bearing conjecture (cell-↔-
    projection bijection). Still requires categorical proof.
  - If Reading A matches CODATA only at 5.6 ppm (same as the
    known empirical coincidence): the audit's argument leads to
    the same coincidence basin PR #701 falsified for Wedderburn
    sums — Yekutieli's distinct-mechanism argument needs to be
    rigorously decoupled from the basin.
  - If Reading A matches NEITHER Family A NOR CODATA: bug in the
    audit's derivation; the Yekutieli mechanism doesn't add up
    as claimed.
  - Reading B at q_0 is ~2.49, well off from CODATA's 2.46 — if
    this is the "true" Yekutieli prediction it doesn't close the
    framework's 3% gap on its own.

NO PROOF — only numerical documentation of where the Yekutieli
structural argument lands at MPFR-50dps so the user / future agent
can decide whether the cell-↔-projection categorical step is worth
formalising. Per CLAUDE.md "no fitting": neither reading is fitted
against CODATA; both are direct evaluations of the audit's
formulas.
"""
from __future__ import annotations
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

mp.mp.dps = 80


def main() -> int:
    Q0 = mp.mpf(Q_50_DIGIT_STR)
    h_q = Q0 - 1 / Q0
    h2 = h_q * h_q
    G = mp.catalan

    # Family A (the framework's substrate λ_scale per PR #895)
    family_A = mp.mpf("2.5") + mp.mpf("0.75") * h2

    # CODATA-derived closure target (retired, kept for comparison)
    codata = mp.mpf("2.4599527869")

    # Reading A (audit's stated formula, h² coeff = -G)
    reading_A = mp.mpf("2.5") - G * h2

    # Reading B (Family A leading + Yekutieli per-cell h² correction)
    reading_B = mp.mpf("2.5") + (mp.mpf("0.75") - G) * h2

    print(f"q_0       = {mp.nstr(Q0, 25)}")
    print(f"h²(q_0)   = {mp.nstr(h2, 25)}")
    print(f"G         = {mp.nstr(G, 25)}")
    print()
    print(f"Family A     = 5/2 + (3/4)·h²        = {mp.nstr(family_A, 18)}")
    print(f"Reading A    = 5/2 - G·h²            = {mp.nstr(reading_A, 18)}")
    print(f"Reading B    = 5/2 + (3/4 - G)·h²    = {mp.nstr(reading_B, 18)}")
    print(f"CODATA tgt   =                       = {mp.nstr(codata, 18)}")
    print()
    print("Distances at q_0:")
    for name, val in [
        ("Family A vs CODATA", family_A - codata),
        ("Reading A vs CODATA", reading_A - codata),
        ("Reading B vs CODATA", reading_B - codata),
        ("Reading A vs Family A", reading_A - family_A),
        ("Reading B vs Family A", reading_B - family_A),
    ]:
        rel = val / codata if "CODATA" in name else val / family_A
        print(f"  {name:<28s} = {mp.nstr(val, 14):>20s} ({mp.nstr(rel*100, 6)} %)")
    print()

    # Verdict for each reading
    def classify(val: mp.mpf, target: mp.mpf, name: str) -> str:
        rel = abs((val - target) / target)
        if rel < mp.mpf("1e-15"):
            return f"MATCH-MPFR-FLOOR vs {name}"
        if rel < mp.mpf("1e-6"):
            return f"MATCH-1ppm vs {name}"
        if rel < mp.mpf("1e-4"):
            return f"CLOSE-100ppm vs {name}"
        if rel < mp.mpf("0.01"):
            return f"WEAK vs {name}"
        return f"FAR vs {name}"

    print("Reading A classification:")
    for tname, tval in [("Family A", family_A), ("CODATA", codata)]:
        print(f"  {classify(reading_A, tval, tname)}")
    print()
    print("Reading B classification:")
    for tname, tval in [("Family A", family_A), ("CODATA", codata)]:
        print(f"  {classify(reading_B, tval, tname)}")
    print()

    print("=" * 70)
    print("INTERPRETATION:")
    print()
    print("Reading A (audit's stated formula 5/2 - G·h²):")
    print("  Matches CODATA at the SAME 5.6 ppm level as the historical")
    print("  empirical coincidence (docs/audits/2026-05-18-lambda-scale-")
    print("  derivation-search.md §'The 5/2 − h²·G hypothesis'). Without")
    print("  the categorical-bijection proof (audit §Concrete next R&D")
    print("  item 1), Reading A is in the SAME coincidence basin PR #701")
    print("  falsified for Wedderburn-sum candidates. Distinguishing")
    print("  Yekutieli's distinct-mechanism argument from the coincidence")
    print("  requires the rigorous cell-↔-half-sym-projection bijection.")
    print()
    print("Reading B (audit corrected: Family A leading + Yekutieli h²):")
    print("  λ_scale(q_0) ≈ 2.493 — off from CODATA by ~1.3% and from")
    print("  Family A by ~1.6%. Not the CODATA value and not the framework's")
    print("  current λ_scale. If this is the 'true' Yekutieli prediction,")
    print("  it does NOT close the 3% gap (only reduces it by ~half).")
    print()
    print("STATUS: Reading A lands in the coincidence basin; Reading B does")
    print("not match anything currently in production or CODATA. The Yekutieli")
    print("structural argument is unresolved between these readings; the")
    print("audit's text gives Reading A but the natural combination with")
    print("Family A (which IS the production substrate λ_scale per #895)")
    print("would be Reading B. Either way, Family A remains production.")
    print()
    print("Concrete next R&D (per audit §'Concrete next R&D'):")
    print("  1. Construct the cell-↔-projection bijection at H_4 explicitly.")
    print("  2. Verify curvature integration gives -G at MPFR floor (vs the")
    print("     coincidence basin's empirical -G + 5.6 ppm slack).")
    print("  3. Resolve Reading A vs Reading B by deriving whether Yekutieli")
    print("     REPLACES the Wedderburn h² or ADDS to it categorically.")
    print("=" * 70)

    w = WitnessBuilder(
        "lambda-scale-alt-i-yekutieli-percell-numerical",
        engine="mpmath",
    )
    w.set_description(
        "Strategy I (Yekutieli per-cell curvature) numerical landscape: "
        "evaluates the audit's two natural readings — Reading A "
        "(λ = 5/2 - G·h² as stated) and Reading B (λ = 5/2 + (3/4 - G)·h² "
        "corrected for combination with Family A) — at q_0 + MPFR-50dps "
        "and compares to Family A (#895 production substrate λ_scale) "
        "and the retired CODATA-derived closure target. Reading A lands "
        "in the same coincidence basin PR #701 falsified for Wedderburn "
        "sums (5.6 ppm match to CODATA); Reading B lands at 2.493 which "
        "matches neither. Yekutieli's structural argument unresolved "
        "between these readings; load-bearing categorical bijection "
        "step (audit §Concrete next R&D #1) is needed to decide."
    )
    w.set_content_block("conj:lambda-scale-substrate-form")
    w.add_parameter("dps", 80)
    w.add_data("family_A_at_q0", mp.nstr(family_A, 25))
    w.add_data("reading_A_at_q0", mp.nstr(reading_A, 25))
    w.add_data("reading_B_at_q0", mp.nstr(reading_B, 25))
    w.add_data("codata_target", mp.nstr(codata, 25))
    w.add_data("reading_A_vs_codata_ppm", mp.nstr((reading_A - codata) / codata * mp.mpf("1e6"), 10))
    w.add_data("reading_B_vs_codata_pct", mp.nstr((reading_B - codata) / codata * 100, 10))
    w.add_data("reading_A_vs_family_A_pct", mp.nstr((reading_A - family_A) / family_A * 100, 10))
    w.add_data("reading_B_vs_family_A_pct", mp.nstr((reading_B - family_A) / family_A * 100, 10))
    w.add_data(
        "structural_status",
        "Reading A: in coincidence basin (5.6 ppm); structurally indistinguishable "
        "from PR #701's falsified Wedderburn-sum candidates absent cell-↔-projection "
        "bijection. Reading B: off-target (matches neither Family A nor CODATA). "
        "Yekutieli argument unresolved; categorical bijection step is the gap.",
    )

    # Per repo convention: probe documents the landscape; passes
    # iff both readings are correctly classified (no surprise match).
    a_ppm_band = bool(
        mp.mpf("1e-7") < abs((reading_A - codata) / codata) < mp.mpf("1e-4")
    )
    b_not_codata = bool(abs((reading_B - codata) / codata) > mp.mpf("0.01"))
    landscape_as_documented = int(a_ppm_band and b_not_codata)
    w.add_assertion(
        "yekutieli_landscape_matches_audit_documented_outcomes",
        computed=landscape_as_documented,
        expected=1,
        tolerance=None,
        source=(
            "Reading A lands in the 1 ppm-100 ppm coincidence-basin band "
            "vs CODATA (consistent with audit §'5.6 ppm match'); Reading "
            "B lands >1% from CODATA (consistent with not being the "
            "production λ_scale). If either condition fails the audit's "
            "derivation has a numerical bug worth re-examining."
        ),
    )

    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
