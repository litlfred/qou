#!/usr/bin/env python3
"""alpha_em_gauss_bonnet_measure_probe.py

Distinct-route derivation of the alpha_EM per-loop measure 1/(8pi) as a
GAUSS-BONNET object |chi|/(4*Area), genus-INDEPENDENT — NOT the b_1-object
1/(pi*b_1) the spectral-determinant route (#3864/#3870/#1552) seeks.

Posted as the deciding discriminant on #3864 (research-overlap relaxation,
2026-07-18): the spectral route requires a measure reciprocal in b_1
(1/(pi*b_1) = 1/(8pi) at b_1=8); the channel-split route (#3810,
alpha_em_channel_split_loop_measure_probe) reaches 1/(8pi) = (1/2)(1/(4pi))
with the b_1-form a genus-4 coincidence. This probe closes the channel-split's
one remaining imported input — the "standard gauge loop unit 1/(4pi)" — by
identifying it geometrically on the Bring surface.

THE IDENTITY (verified symbolically, all g):

  hyperbolic Gauss-Bonnet:   Area = -2*pi*chi = 2*pi*|chi|      (chi<0)
  gauge loop unit:           1/(4pi) = |chi|/(2*Area)           (geometric!)
  per-loop measure:          1/(8pi) = (1/2)*(1/(4pi)) = |chi|/(4*Area)

  => the measure is |chi|/(4*Area): GENUS-INDEPENDENT, since Area = 2*pi*|chi|
     makes |chi|/(4*Area) = |chi|/(8*pi*|chi|) = 1/(8pi) for EVERY g.

  The b_1 reading 1/(pi*b_1) = 1/(2*pi*g) SCALES with genus and equals
  |chi|/(4*Area) ONLY at g = 4 (b_1 = 8, |chi| = 6):
     |chi|/(4*Area) = 6/(48*pi) = 1/(8*pi) = 1/(pi*8) = 1/(pi*b_1).  [coincidence]
  At g = 5: |chi|/(4*Area) = 1/(8*pi) but 1/(pi*b_1) = 1/(10*pi).  [differ]

DISCRIMINANT ANSWERED: the measure does NOT scale with genus (Gauss-Bonnet
ties Area to |chi|), so the spectral b_1^{-1} object is the wrong scaling —
the b_1 appearance at g=4 is coincidental (b_1 = 8, |chi| = 6, and
6/(4*Area) = 1/(pi*8) only there). No new geometric assumption: the "loop
unit" 1/(4pi) IS |chi|/(2*Area) on any hyperbolic surface.

HONEST TIER — re-scope, not full closure (matches #3810). This identifies the
imported gauge-loop-unit geometrically and makes genus-independence manifest;
it does NOT independently derive the factor 1/2 (two braiding channels) or the
overall 1/4 grouping — those are the channel-split structure (#3810). What is
new: the measure is a Gauss-Bonnet (chi, Area) invariant, not a Betti (b_1)
object, resolving the #3864 tension in favour of genus-independence. No fit;
no alpha_k wired; 1/(8pi) stays a phase-4 identification. scope-(a).

Bring surface: (2,4,5)-triangle group tiling, g=4, chi=-6, Area=12*pi
(= Gauss-Bonnet 4*pi*(g-1)); see the merged EmCouplingBringZeroMode Lean.
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402, F401
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    print("=" * 76)
    print(" alpha_EM per-loop measure as a Gauss-Bonnet object |chi|/(4*Area)")
    print("=" * 76)

    g = sp.symbols("g", positive=True, integer=True)
    chi = 2 - 2 * g                      # Euler characteristic of genus-g surface
    abschi = 2 * g - 2                   # |chi| for g >= 2
    b1 = 2 * g
    Area = 4 * sp.pi * (g - 1)           # hyperbolic Gauss-Bonnet: -2*pi*chi

    gb_area_ok = sp.simplify(Area - (-2 * sp.pi * chi)) == 0
    loop_unit_ok = sp.simplify(abschi / (2 * Area) - 1 / (4 * sp.pi)) == 0
    meas_gb = sp.simplify(abschi / (4 * Area))
    meas_gb_ok = sp.simplify(meas_gb - 1 / (8 * sp.pi)) == 0
    meas_b1 = sp.simplify(1 / (sp.pi * b1))
    coincide = sp.solve(sp.Eq(abschi / (4 * Area), 1 / (sp.pi * b1)), g)

    print(f"\n  Gauss-Bonnet  Area = -2*pi*chi : {gb_area_ok}")
    print(f"  gauge loop unit  1/(4pi) = |chi|/(2*Area) : {loop_unit_ok}")
    print(f"  per-loop measure |chi|/(4*Area) = {meas_gb}  (= 1/(8pi): {meas_gb_ok}, "
          f"GENUS-INDEPENDENT)")
    print(f"  b_1 reading      1/(pi*b_1) = {meas_b1}  (scales with genus)")
    print(f"  the two coincide only at g = {coincide}  (b_1 = 8, |chi| = 6)")

    print("\n  genus scan (|chi|/(4*Area) vs 1/(pi*b_1)):")
    rows = []
    for gg in (4, 5, 6, 7):
        mg = float(meas_gb)  # constant 1/(8pi)
        mb = float(meas_b1.subs(g, gg))
        same = abs(mg - mb) < 1e-12
        rows.append({"g": gg, "gauss_bonnet": mg, "b1_reading": mb, "same": same})
        print(f"    g={gg}: |chi|/(4Area)={mg:.7f}  1/(pi*b1)={mb:.7f}  "
              f"{'SAME' if same else 'DIFFER'}")

    # Bring specifics
    bring = {"g": 4, "chi": -6, "b1": 8, "Area_over_pi": 12}
    bring_ok = (float(sp.Rational(6, 4) / (12 * sp.pi)) - float(1 / (8 * sp.pi))) == 0 \
        or abs(6 / (4 * 12 * 3.141592653589793) - 1 / (8 * 3.141592653589793)) < 1e-15
    print(f"\n  Bring: g=4, chi=-6, Area=12pi -> |chi|/(4*Area) = 6/(48pi) = 1/(8pi): {bring_ok}")

    ok = bool(gb_area_ok and loop_unit_ok and meas_gb_ok and coincide == [4] and bring_ok)

    wb = WitnessBuilder("alpha-em-gauss-bonnet-measure", engine="sympy")
    wb.set_description(
        "Distinct-route (research-overlap, #3864) identification of the alpha_EM "
        "per-loop measure 1/(8pi) as the Gauss-Bonnet object |chi|/(4*Area), "
        "GENUS-INDEPENDENT (Area=2pi|chi|), NOT the spectral b_1-object 1/(pi*b_1) "
        "which scales as 1/(2pi*g) and coincides only at g=4 (b_1=8, |chi|=6). "
        "Closes the channel-split's imported gauge-loop-unit: 1/(4pi)=|chi|/(2*Area). "
        "Re-scope not full closure (the 1/2 two-channel factor is #3810 structure); "
        "answers the #3864 discriminant in favour of genus-independence. No fit; no "
        "alpha_k wired; 1/(8pi) stays phase-4. scope-(a).")
    wb.set_content_block("prop:em-coupling-bring-zero-mode")
    wb.add_data("measure_gauss_bonnet", "|chi|/(4*Area) = 1/(8pi), genus-independent")
    wb.add_data("measure_b1_reading", "1/(pi*b1) = 1/(2*pi*g), scales; = at g=4 only")
    wb.add_data("gauge_loop_unit_geometric", "1/(4pi) = |chi|/(2*Area)")
    wb.add_data("coincide_genus", [int(x) for x in coincide])
    wb.add_data("genus_scan", rows)
    wb.add_data("bring", bring)
    wb.add_assertion("gauss_bonnet_measure_is_8pi_all_genus",
                     computed=float(meas_gb_ok), expected=1.0, tolerance=0.5,
                     source="|chi|/(4*Area) = 1/(8pi) symbolically for all g")
    wb.add_assertion("gauge_loop_unit_is_geometric",
                     computed=float(loop_unit_ok), expected=1.0, tolerance=0.5,
                     source="1/(4pi) = |chi|/(2*Area) (Gauss-Bonnet)")
    wb.add_assertion("b1_reading_coincides_only_at_g4",
                     computed=float(coincide == [4]), expected=1.0, tolerance=0.5,
                     source="|chi|/(4Area) = 1/(pi*b1) solved => g=4 unique")
    wb.save()

    print(f"\n  RESULT: {'ALL OK — measure is a Gauss-Bonnet invariant' if ok else 'CHECK'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
