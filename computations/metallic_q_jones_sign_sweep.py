#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical-only output across counterfactual q.
"""
Metallic-q Jones-polynomial sign sweep — companion to the Wenzl probe.

The Wenzl probe `metallic_q_wenzl_sign_sweep.py` returned a NULL result:
for real q > 0 the q-integers [k]_q stay positive, so Wenzl weights
y_λ never flip sign and the count of positive Wedderburn blocks is
constant.  The structural metallic transition (if real) must therefore
live at a level that CAN sign-flip across q.

The natural next candidate: **Jones polynomials of specific knots**.
The Jones polynomial J_K(q) is a Laurent polynomial in q; its roots are
specific algebraic numbers that DO have an algebraic relation to the
metallic ratios for certain knots (e.g. the trefoil's Jones polynomial
has a sign change at q² ≈ 1.62 — close to φ).

This probe sweeps J_K(q) across the same intervals as the Wenzl probe
for a small set of canonical knots:

  - **unknot 0_1**       J = 1 (control — never flips)
  - **trefoil 3_1**      J = -q^4 + q^3 + q   (right-handed)
  - **figure-eight 4_1** J = q^2 - q + 1 - q⁻¹ + q⁻²
  - **Hopf link 2_1²**   J = -q⁻⁵/² (q + q⁻¹) for the appropriate framing
  - **5_1 torus**        J = -q^7 + q^6 - q^5 + q^4 + q^2

At each q in the sweep, record:
  - sign(J_K(q))                      — boolean
  - |J_K(q)|                          — magnitude
  - whether the sign matches q₀'s sign — flip indicator

If sign(J_K(q)) flips AT metallic ratios for some K, the conjecture is
*partially* confirmed at the topological-invariant level.  If it flips
elsewhere, the metallic structure is not the controlling boundary.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50

HERE = Path(__file__).parent


def delta_n(n: int) -> mp.mpf:
    return (mp.mpf(n) + mp.sqrt(n * n + 4)) / 2


PHI = delta_n(1)
DELTA_SILVER = delta_n(2)
DELTA_BRONZE = delta_n(3)
Q0 = mp.mpf("1.1099785955541805")


# ── Jones polynomials (standard normalisation, σ_i variable q) ────────


def J_unknot(q: mp.mpf) -> mp.mpf:
    return mp.mpf(1)


def J_trefoil_right(q: mp.mpf) -> mp.mpf:
    """Right-handed trefoil: J = -q^4 + q^3 + q (Kauffman normalised)."""
    return -mp.power(q, 4) + mp.power(q, 3) + q


def J_figure_eight(q: mp.mpf) -> mp.mpf:
    """Figure-eight (amphichiral): J = q^2 - q + 1 - q⁻¹ + q⁻²."""
    return (
        mp.power(q, 2) - q + 1 - mp.power(q, -1) + mp.power(q, -2)
    )


def J_5_1(q: mp.mpf) -> mp.mpf:
    """5_1 torus knot T(2,5): J = -q^7 + q^6 - q^5 + q^4 + q^2."""
    return (
        -mp.power(q, 7) + mp.power(q, 6) - mp.power(q, 5)
        + mp.power(q, 4) + mp.power(q, 2)
    )


def J_hopf_pos(q: mp.mpf) -> mp.mpf:
    """Positive Hopf link L_2a1+: J = -q^{5/2} - q^{1/2} (sign-relevant part)."""
    half = mp.mpf(1) / 2
    return -mp.power(q, 5 * half) - mp.power(q, half)


KNOTS = {
    "0_1_unknot": J_unknot,
    "3_1_trefoil_right": J_trefoil_right,
    "4_1_figure_eight": J_figure_eight,
    "5_1_torus": J_5_1,
    "L2a1_hopf_pos": J_hopf_pos,
}


def linspace(a: mp.mpf, b: mp.mpf, k: int) -> list[mp.mpf]:
    if k == 1:
        return [a]
    step = (b - a) / (k - 1)
    return [a + step * i for i in range(k)]


def build_sweep() -> dict[str, list[mp.mpf]]:
    eps = mp.mpf("0.005")
    return {
        "interval_q0_to_phi":         linspace(Q0 + eps, PHI - eps, 14),
        "interval_phi_to_silver":     linspace(PHI + eps, DELTA_SILVER - eps, 14),
        "interval_silver_to_bronze":  linspace(DELTA_SILVER + eps, DELTA_BRONZE - eps, 10),
        "metallic_boundaries":        [PHI, DELTA_SILVER, DELTA_BRONZE],
        "mirror_silver_to_phi":       linspace(1 / DELTA_SILVER + eps, 1 / PHI - eps, 10),
        "mirror_bronze_to_silver":    linspace(1 / DELTA_BRONZE + eps, 1 / DELTA_SILVER - eps, 8),
    }


def fmt(x: mp.mpf) -> str:
    return mp.nstr(x, 30)


def sign_of(x: mp.mpf) -> int:
    if x > 0:
        return +1
    if x < 0:
        return -1
    return 0


def main() -> None:
    print("Sweeping Jones polynomials across metallic intervals…", file=sys.stderr)
    sweep = build_sweep()

    # Reference signs at q₀ for each knot.
    sign_q0: dict[str, int] = {k: sign_of(f(Q0)) for k, f in KNOTS.items()}
    print(f"q₀ reference signs: {sign_q0}", file=sys.stderr)

    results: dict[str, list[dict]] = {}
    for interval_name, qs in sweep.items():
        rows: list[dict] = []
        for q in qs:
            row: dict = {
                "q": fmt(q),
                "q_minus_qinv": fmt(q - 1 / q),
                "knots": {},
            }
            for name, fn in KNOTS.items():
                val = fn(q)
                s = sign_of(val)
                row["knots"][name] = {
                    "value": fmt(val),
                    "sign": s,
                    "abs": fmt(abs(val)),
                    "flip_vs_q0": (s != sign_q0[name]),
                }
            rows.append(row)
        results[interval_name] = rows

    # Per-knot per-interval: count sign distinct values seen.
    summary: dict[str, dict] = {}
    for interval_name, rows in results.items():
        summary[interval_name] = {}
        for name in KNOTS:
            signs_seen = sorted({r["knots"][name]["sign"] for r in rows})
            summary[interval_name][name] = {
                "distinct_signs_in_interval": signs_seen,
                "all_same_sign": len(signs_seen) == 1,
                "matches_q0_sign": signs_seen == [sign_q0[name]],
            }

    # Detect crossings — q values where sign(J_K) changes between consecutive
    # samples in the same interval.
    crossings: dict[str, list[dict]] = {}
    for interval_name, rows in results.items():
        ints: list[dict] = []
        for name in KNOTS:
            prev: int | None = None
            for i, r in enumerate(rows):
                cur = r["knots"][name]["sign"]
                if prev is not None and cur != prev and prev != 0 and cur != 0:
                    ints.append({
                        "knot": name,
                        "between_q_index": [i - 1, i],
                        "between_q_values": [rows[i - 1]["q"], rows[i]["q"]],
                        "sign_change": [prev, cur],
                    })
                prev = cur
        crossings[interval_name] = ints

    # Boundary jumps at metallic ratios.
    above_phi = results["interval_phi_to_silver"][0]
    below_phi = results["interval_q0_to_phi"][-1]
    above_silver = results["interval_silver_to_bronze"][0]
    below_silver = results["interval_phi_to_silver"][-1]
    at_phi = results["metallic_boundaries"][0]
    at_silver = results["metallic_boundaries"][1]

    boundary_jumps: dict[str, dict] = {}
    for ratio_name, below, at, above in [
        ("golden_phi", below_phi, at_phi, above_phi),
        ("silver", below_silver, at_silver, above_silver),
    ]:
        rs: dict = {}
        for name in KNOTS:
            rs[name] = {
                "below_sign": below["knots"][name]["sign"],
                "at_sign": at["knots"][name]["sign"],
                "above_sign": above["knots"][name]["sign"],
                "jumps_at_ratio": (
                    below["knots"][name]["sign"]
                    != above["knots"][name]["sign"]
                ),
            }
        boundary_jumps[ratio_name] = rs

    witness: dict = {
        "description": (
            "Jones-polynomial sign sweep across the first three metallic-"
            "ladder intervals. Companion to the Wenzl-y_λ sweep, which "
            "returned NULL (Wenzl weights stay positive for all real "
            "q > 0). This probe tests whether the metallic-piecewise "
            "structure shows up at the level of Jones polynomials of "
            "canonical knots (unknot, trefoil, figure-eight, 5_1, Hopf)."
        ),
        "companion_to": "metallic-q-wenzl-sign-sweep.witness.json",
        "computed_at": datetime.now(timezone.utc).isoformat(),
        "precision_dps": int(mp.mp.dps),
        "anchors": {
            "q_0_substrate": fmt(Q0),
            "golden_phi": fmt(PHI),
            "silver_delta_2": fmt(DELTA_SILVER),
            "bronze_delta_3": fmt(DELTA_BRONZE),
        },
        "knots_tested": list(KNOTS.keys()),
        "sign_at_q0": sign_q0,
        "sweep": results,
        "per_interval_summary": summary,
        "crossings_within_intervals": crossings,
        "boundary_jumps_at_metallic_ratios": boundary_jumps,
        "verdict": {
            "interpretation": (
                "If sign(J_K(q)) jumps EXACTLY at metallic ratios for some "
                "knot K and stays constant within each metallic interval, "
                "the conjecture is empirically confirmed at the Jones-"
                "polynomial level for that K. If signs change WITHIN an "
                "interval (a crossing not at a metallic ratio), the "
                "metallic structure is not the controlling boundary for "
                "that knot's sign."
            ),
        },
        "limitations": [
            "Jones polynomials are simple test functions — they are not "
            "the SDP-feasibility criterion the framework actually uses. "
            "A true test needs character χ_λ(β) sign tracking, which "
            "requires re-pinning per-nucleus character witnesses at "
            "counterfactual q.",
            "Hopf link uses fractional powers; sign comparison is well-"
            "defined for q > 0 real.",
            "The 5_1 torus knot Jones polynomial uses the standard "
            "right-handed convention; mirror image would flip overall sign.",
        ],
    }

    out = HERE / "metallic-q-jones-sign-sweep.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\nWitness: {out}", file=sys.stderr)

    # Human-readable summary
    print("\n=== Verdict ===\n")
    print(f"q₀ signs:  {sign_q0}\n")
    print("Boundary jumps at metallic ratios:")
    for ratio_name, rs in boundary_jumps.items():
        print(f"  {ratio_name}:")
        for name, r in rs.items():
            tag = " ⬆ JUMPS" if r["jumps_at_ratio"] else "  smooth"
            print(
                f"    {name:24s}  below={r['below_sign']:+d}  at={r['at_sign']:+d}  above={r['above_sign']:+d}{tag}"
            )

    print("\nIn-interval sign crossings (q values where sign(J) changes between samples):")
    any_crossing = False
    for interval_name, ints in crossings.items():
        if not ints:
            continue
        any_crossing = True
        print(f"  {interval_name}:")
        for c in ints:
            print(
                f"    {c['knot']:24s}  sign {c['sign_change'][0]:+d}→{c['sign_change'][1]:+d}  "
                f"between q ≈ {c['between_q_values'][0][:8]} … {c['between_q_values'][1][:8]}"
            )
    if not any_crossing:
        print("  (none — all sign changes happen exactly at metallic ratios "
              "or not at all)")


if __name__ == "__main__":
    main()
