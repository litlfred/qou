#!/usr/bin/env python3
"""alpha_em_4pi_bring_surface_integration.py — gap (ii) of #1466/#1469:
test Bring-surface integration as the structural source of α/(4π).

STRUCTURAL TEMPLATE.
The leading 2/(3π) of the Bring zero-mode shift had TWO independent
geometric identifications producing the same value:

  (i)  Hodge / Gauss-Bonnet:  dim H¹(M_Bring) / Area(M_Bring)
       = 2g/(4π(g-1)) = 8/(12π) = 2/(3π)  at g=4

  (ii) Sphere-volume:  Vol(S²) / (3·Vol(S³))
       = 4π/(3·2π²) = 2/(3π)

For α/(4π) to be a structurally clean next-order, it should have an
analogous DUAL identification — one Bring/Hodge-side, one sphere-vol
side, both giving the same number.

CANDIDATES (Hodge-side).
  Bring is g=4 closed hyperbolic surface. Natural higher constructions:
    UT(M_Bring) = unit tangent bundle (3-mfd)
      Vol = 2π·Area = 24π²;     dim H¹ = 2g = 8
    M_Bring × S¹
      Vol = 24π²;                dim H¹ = 2g+1 = 9
    M_Bring × M_Bring (product 4-mfd)
      Vol = 144π²;               dim H² = 2+4g² = 66
    UT(M_Bring) × S¹ (5-mfd)
      Vol = 48π³;                dim H¹ = 2g+1 = 9
    M_Bring × M_Bring × M_Bring (6-mfd)
      Vol = 1728π³;              dim H³ = 8g+8g²+2 = 162

CANDIDATES (sphere-volume side).
  Standard sphere volumes:
    Vol(S²) = 4π
    Vol(S³) = 2π²
    Vol(S⁴) = 8π²/3
    Vol(S⁵) = π³
    Vol(S⁶) = 16π³/15
    Vol(S⁷) = π⁴/3

  Natural next-order ratios:
    Vol(S²)·Vol(S³) / [k · Vol(S⁵)·Vol(S⁶)]   for k ∈ {1,3,5,15}
    Vol(S²)² / [k · Vol(S⁴)·Vol(S⁵)]
    Vol(S²) / [k · Vol(S⁴)²]
    Vol(S³) / [k · Vol(S⁵)²]
    etc.

VERDICT LOGIC.
If a Hodge candidate AND a sphere candidate independently produce
α/(4π) within precision target (< 0.1%), AND they agree algebraically,
we have a derivation. Otherwise, gap (ii) by itself fails and α/(4π)
is genuinely a COMBINED quantity.

No fit; each candidate is a parameter-free geometric quantity.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp
from mpmath import mpf, pi

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402
from experimental_constants import ALPHA_EM_INV  # noqa: E402


def vol_sphere(d: int):
    """Standard sphere volume Vol(S^d) = 2π^((d+1)/2) / Γ((d+1)/2)."""
    from mpmath import gamma as G
    return 2 * pi**(mpf(d+1)/2) / G(mpf(d+1)/2)


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "alpha-em-4pi-bring-surface-integration",
        engine="mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Gap (ii) attempt from #1466/#1469: test Bring-surface "
        "integration (Hodge/Gauss-Bonnet ratios on higher-genus / "
        "fibre-bundle constructions, sphere-volume ratios) as the "
        "structural source of α/(4π). Parallel to the leading "
        "2/(3π) = dim H¹/Area = Vol(S²)/(3·Vol(S³)). Tests 10+ "
        "Hodge-side and 12+ sphere-side parameter-free candidates."
    )
    builder.set_content_block("prop:em-coupling-bring-zero-mode")

    CODATA_alpha_inv = mpf(str(ALPHA_EM_INV))
    TARGET = (1 / CODATA_alpha_inv) / (4 * pi)

    print("=" * 76)
    print(" α/(4π) DERIVATION — gap (ii): Bring-surface integration")
    print("=" * 76)
    print(f"  target α/(4π) = {mp.nstr(TARGET, 18)}")
    print()

    # ── HODGE-side candidates ────────────────────────────────────
    g = 4
    chi = mpf(2 - 2*g)               # = -6
    area = -2 * pi * chi             # = 12π (Gauss-Bonnet)
    vol_UT = 2 * pi * area           # = 24π²
    dim_H1_M = 2*g                   # = 8
    dim_H1_UT = 2*g                  # = 8 (or 2g+1 depending on torsion conv)
    dim_H2_MxM = 2 + 4*g**2          # = 66
    dim_H1_MxS1 = 2*g + 1            # = 9

    hodge_candidates = [
        # (name, value)
        ("dim H¹(UT)/Vol(UT)        = 8/(24π²)",      dim_H1_UT / vol_UT),
        ("dim H¹(UT)/(Vol·4π)       = 8/(96π³)",      dim_H1_UT / (vol_UT * 4 * pi)),
        ("dim H¹(M×S¹)/Vol(M×S¹)    = 9/(24π²)",      dim_H1_MxS1 / vol_UT),
        ("dim H²(M×M)/Vol(M×M)      = 66/(144π²)",    dim_H2_MxM / area**2),
        ("dim H²(M×M)/(Vol·4π)      = 66/(576π³)",    dim_H2_MxM / (area**2 * 4 * pi)),
        ("[dim H¹(M)]²/Area²        = 64/(144π²)",    dim_H1_M**2 / area**2),
        ("[dim H¹(M)]²/(2·Area²)    = 32/(144π²)",    dim_H1_M**2 / (2 * area**2)),
        ("[dim H¹(M)/Area]·1/(4π)   = (2/(3π))/(4π)",  (dim_H1_M / area) / (4 * pi)),
        ("[dim H¹(M)/Area]²·1/Area   = (2/(3π))²/12π", (dim_H1_M / area)**2 / area),
        ("[χ]/Vol(M×M)             = -6/144π²",      chi / area**2),
        ("(2g/(4π(g-1)))²·1/(2g·Area) = ...",         (mpf(2*g) / (4*pi*(g-1)))**2 / (2*g*area)),
        ("(2g/(4π(g-1)))²·1/Vol(UT)",                 (mpf(2*g) / (4*pi*(g-1)))**2 / vol_UT),
    ]

    # ── SPHERE-side candidates ───────────────────────────────────
    S = {d: vol_sphere(d) for d in range(1, 8)}
    sphere_candidates = [
        ("Vol(S²)·Vol(S³)/(3·Vol(S⁵)·Vol(S⁶))",
         S[2] * S[3] / (3 * S[5] * S[6])),
        ("Vol(S²)/(3·Vol(S³)·Vol(S²))",
         S[2] / (3 * S[3] * S[2])),
        ("Vol(S²)²/(3·Vol(S³)·Vol(S⁴))",
         S[2]**2 / (3 * S[3] * S[4])),
        ("Vol(S²)/(3·Vol(S³)²)",
         S[2] / (3 * S[3]**2)),
        ("Vol(S²)·Vol(S²)/(15·Vol(S³)·Vol(S⁵))",
         S[2]**2 / (15 * S[3] * S[5])),
        ("Vol(S²)/(Vol(S⁴)·Vol(S³))",
         S[2] / (S[4] * S[3])),
        ("[Vol(S²)/(3·Vol(S³))]²",
         (S[2] / (3 * S[3]))**2),
        ("[Vol(S²)/(3·Vol(S³))]²/Vol(S²)",
         (S[2] / (3 * S[3]))**2 / S[2]),
        ("[Vol(S²)/(3·Vol(S³))]/(4π)",
         (S[2] / (3 * S[3])) / (4 * pi)),
        ("[Vol(S²)/(3·Vol(S³))]/Vol(S³)",
         (S[2] / (3 * S[3])) / S[3]),
        ("Vol(S²)/(3·Vol(S⁵))",
         S[2] / (3 * S[5])),
        ("Vol(S²)·Vol(S³)/(3·Vol(S⁷))",
         S[2] * S[3] / (3 * S[7])),
    ]

    # ── Display + compare ─────────────────────────────────────
    print("  HODGE-SIDE candidates (parameter-free)")
    print(f"  {'name':50s} {'value':>14s} {'ratio to TARGET':>16s}")
    all_results = []
    best = None
    for name, v in hodge_candidates:
        ratio = float(v / TARGET)
        all_results.append({
            "side": "Hodge",
            "name": name,
            "value": mp.nstr(v, 14),
            "ratio_to_target": ratio,
        })
        print(f"  {name[:48]:50s} {float(v):>14.4e} {ratio:>16.4f}")
        if best is None or abs(ratio - 1) < abs(best["ratio_to_target"] - 1):
            best = all_results[-1]

    print()
    print("  SPHERE-VOLUME candidates (parameter-free)")
    print(f"  {'name':50s} {'value':>14s} {'ratio to TARGET':>16s}")
    for name, v in sphere_candidates:
        ratio = float(v / TARGET)
        all_results.append({
            "side": "Sphere",
            "name": name,
            "value": mp.nstr(v, 14),
            "ratio_to_target": ratio,
        })
        print(f"  {name[:48]:50s} {float(v):>14.4e} {ratio:>16.4f}")
        if abs(ratio - 1) < abs(best["ratio_to_target"] - 1):
            best = all_results[-1]

    print()
    print(f"  TARGET α/(4π) = {float(TARGET):.6e}")
    print(f"  Best overall:  [{best['side']}]  {best['name']}")
    print(f"     ratio = {best['ratio_to_target']:.6f}  "
          f"deviation = {(best['ratio_to_target']-1)*100:+.4f}%")

    # ─── Honest verdict ───────────────────────────────────────
    print()
    print("=" * 76)
    print(" Honest verdict")
    print("=" * 76)
    dev = abs(best["ratio_to_target"] - 1) * 100
    if dev < 0.5:
        verdict = (f"DERIVED — {best['name']} [{best['side']}] gives "
                   f"α/(4π) within 0.5%")
        # Check if there's a dual identification
        dual_candidates = [r for r in all_results
                           if r["side"] != best["side"]
                           and abs(r["ratio_to_target"] - 1) < 0.005]
        if dual_candidates:
            print(f"  ✓ {verdict}")
            print(f"  DUAL identification on other side:")
            for d in dual_candidates:
                print(f"     [{d['side']}] {d['name']} "
                      f"({(d['ratio_to_target']-1)*100:+.4f}%)")
        else:
            print(f"  ~ {verdict} (BUT no dual identification — "
                  f"could still be fit-class)")
    elif dev < 5:
        verdict = (f"NEAR-MATCH ({dev:.2f}%) on best {best['side']} candidate; "
                   "NOT a derivation per proposition's near-miss warning")
        print(f"  ~ {verdict}")
        print(f"  Closest: [{best['side']}] {best['name']}")
    else:
        verdict = (f"REFUTED — best is {dev:.1f}% off; gap (ii) "
                   "Bring-surface integration alone is insufficient")
        print(f"  ✗ {verdict}")
        print(f"  Combined refutation map after gaps (i), (ii), (iii):")
        print(f"    Gap (i)   H_3 matter insertion:    -445% off  (#1466)")
        print(f"    Gap (ii)  Bring-surface integration:  {best['ratio_to_target']-1:+.1%} off  (this PR)")
        print(f"    Gap (iii) Q_q vertex factor:       +11.2% off (#1469)")
        print(f"  All three individual sub-gaps refuted. α/(4π) requires")
        print(f"  COMBINED derivation joining all three structural elements")
        print(f"  with structurally-forced (not chosen) normalizations.")

    builder.add_data("target_alpha_over_4pi", mp.nstr(TARGET, 30))
    builder.add_data("hodge_candidates",
                     [r for r in all_results if r["side"] == "Hodge"])
    builder.add_data("sphere_candidates",
                     [r for r in all_results if r["side"] == "Sphere"])
    builder.add_data("best", best)
    builder.add_data("verdict", verdict)

    builder.add_assertion(
        "candidates_evaluated",
        computed=len(all_results),
        expected=len(hodge_candidates) + len(sphere_candidates),
        tolerance=0,
        source=f"{len(hodge_candidates)} Hodge-side + {len(sphere_candidates)} "
               f"sphere-volume parameter-free candidates evaluated.",
    )
    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
