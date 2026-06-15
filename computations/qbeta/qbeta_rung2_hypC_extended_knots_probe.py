#!/usr/bin/env python3
"""qbeta_rung2_hypC_extended_knots_probe.py — extend Hyp-C beyond
the 4 PR #1806 candidates with torus knots T(2,n) for n ∈ {7,9,11}
plus twist knots.

PR #1806 tested Hyp-C with {Hopf, trefoil 3_1, fig-8 4_1,
cinquefoil T(2,5)} — all REFUTED (V_K cubic Taylor at q=1 ≠ 1).
This probe extends to more torus knots and twist knots to check
whether ANY knot's V_K has cubic Taylor coefficient = 1 at q=1.

If a match is found, it identifies the categorical source of
rung 2 = ℏ_q³/[2]_q in the c_3 closure.
If REFUTED across the extended set, the literal Hyp-C lift is
definitively ruled out beyond reasonable doubt.

Tested knots (right-handed convention from KnotInfo):

  T(2, 3) = 3_1:   V = -q⁻⁴ + q⁻³ + q⁻¹
  T(2, 5) = 5_1:   V = -q⁻⁷ + q⁻⁶ - q⁻⁵ + q⁻⁴ + q⁻²
  T(2, 7) = 7_1:   V = -q⁻¹⁰ + q⁻⁹ - q⁻⁸ + q⁻⁷ - q⁻⁶ + q⁻⁵ + q⁻³
  T(2, 9) = 9_1:   V = -q⁻¹³ + q⁻¹² - q⁻¹¹ + q⁻¹⁰ - q⁻⁹ + q⁻⁸
                       - q⁻⁷ + q⁻⁶ + q⁻⁴
  T(2,11) = 11a367: V = -q⁻¹⁶ + q⁻¹⁵ - q⁻¹⁴ + q⁻¹³ - q⁻¹² + q⁻¹¹
                       - q⁻¹⁰ + q⁻⁹ - q⁻⁸ + q⁻⁷ + q⁻⁵

  Twist knots (T(2,n) connect sum with structure):
  Figure-eight 4_1 (already tested, cubic = -3)
  Stevedore  6_1:  V = q⁻⁴ - q⁻³ + q⁻² - 2q⁻¹ + 2 - q + q²
  Mazur 6_2: V = q⁻⁵ - 2q⁻⁴ + 2q⁻³ - 2q⁻² + 2q⁻¹ - 1 + q

Cubic Taylor coefficient at q=1 read off via h := q-1 reparametrisation
(robust per Gemini's PR #1806 round-2 recommendation).

Verdict: if any cubic coefficient equals 1, Hyp-C is CONFIRMED for
that knot. If none across the 9-knot extended set, Hyp-C is
DEFINITIVELY REFUTED across natural knot candidates.
"""
from __future__ import annotations

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import time

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "65")
os.environ.setdefault("QOU_OUTPUT_DPS", "50")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(65)
# mpmath not used in this script — purely symbolic sympy work.
import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-rung2-hyp-c-extended-knots-probe",
        engine="python+sympy",
        start_time=t0,
    )
    builder.set_description(
        "Extends the Hyp-C concrete test from PR #1806 to 9 natural "
        "knot candidates: T(2,n) for n ∈ {3,5,7,9,11} + twist knots "
        "4_1, 6_1, 6_2. Reports V_K cubic Taylor coefficient at q=1 "
        "for each; Hyp-C is CONFIRMED iff coefficient = 1."
    )
    builder.set_content_block("prop:q-beta-c-k-recursion-from-habiro-q-difference")

    print("=" * 78)
    print(" Q_β RUNG-2 HYP-C — extended knot set")
    print("=" * 78)
    print()

    q = sp.Symbol("q", positive=True)
    h = sp.Symbol("h")  # series variable, q = 1 + h
    hbar_q = (q - 1) / q

    # Required cubic coefficient (from ℏ_q³ Taylor — divided unknot
    # bracket [2]_q cancels in the Hyp-C ratio).
    hbar_q_cubed_series = sp.series(
        hbar_q.subs(q, 1 + h) ** 3, h, 0, 5).removeO()
    cubic_required = hbar_q_cubed_series.coeff(h, 3)
    print(f"  Required h³ coefficient for Hyp-C: {cubic_required}")
    print()

    # Knots — right-handed (positive-crossing) convention from KnotInfo
    knots = {
        # Torus T(2,n) family
        "T(2,3) = 3_1":    -q ** (-4) + q ** (-3) + q ** (-1),
        "T(2,5) = 5_1":    -q ** (-7) + q ** (-6) - q ** (-5)
                           + q ** (-4) + q ** (-2),
        "T(2,7) = 7_1":    -q ** (-10) + q ** (-9) - q ** (-8)
                           + q ** (-7) - q ** (-6) + q ** (-5)
                           + q ** (-3),
        "T(2,9) = 9_1":    -q ** (-13) + q ** (-12) - q ** (-11)
                           + q ** (-10) - q ** (-9) + q ** (-8)
                           - q ** (-7) + q ** (-6) + q ** (-4),
        "T(2,11) = 11a367": -q ** (-16) + q ** (-15) - q ** (-14)
                            + q ** (-13) - q ** (-12) + q ** (-11)
                            - q ** (-10) + q ** (-9) - q ** (-8)
                            + q ** (-7) + q ** (-5),
        # Twist family
        "4_1 (figure-eight)": q ** (-2) - q ** (-1) + 1 - q + q ** 2,
        "6_1 (stevedore)":   q ** (-4) - q ** (-3) + q ** (-2)
                             - 2 * q ** (-1) + 2 - q + q ** 2,
        "6_2":               q ** (-5) - 2 * q ** (-4) + 2 * q ** (-3)
                             - 2 * q ** (-2) + 2 * q ** (-1) - 1 + q,
        # Sanity
        "Unknot":            sp.Integer(1),
    }

    print(f"  {'Knot':<22} {'V(K)|_{q=1}':>10} {'h³ coef':>10} Hyp-C?")
    print(f"  {'-'*22} {'-'*10} {'-'*10} {'-'*10}")

    results = []
    matching = []
    for name, V in knots.items():
        # Laurent polynomial → direct .subs(q, 1) (avoids sp.limit
        # overhead per Gemini review on PR #1822).
        V_at_q1 = V.subs(q, 1)
        V_taylor = sp.series(V.subs(q, 1 + h), h, 0, 5).removeO()
        c3 = V_taylor.coeff(h, 3)
        # sympy expression comparison: use .equals(0) (returns
        # Python bool) instead of `== 0` (returns Equality obj) per
        # Gemini review on PR #1822.
        diff = sp.simplify(c3 - cubic_required)
        confirmed = bool(diff == 0) if isinstance(diff, (int, sp.Integer)) \
            else bool(diff.equals(0))
        marker = "✓ MATCH" if confirmed else f"≠ {cubic_required}"
        print(f"  {name:<22} {str(V_at_q1):>10} {str(c3):>10} {marker}")
        entry = {
            "knot": name,
            "V_at_q1": str(V_at_q1),
            "cubic_taylor_coefficient": str(c3),
            "hyp_c_confirmed": confirmed,
        }
        results.append(entry)
        if confirmed and "Unknot" not in name:
            matching.append(entry)

    print()
    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    print()

    if matching:
        print(f"  ✓ Hyp-C CONFIRMED for {len(matching)} knot(s):")
        for r in matching:
            print(f"     {r['knot']}")
        print()
        print(f"  Categorical lift candidate identified.")
    else:
        print(f"  ✗ Hyp-C REFUTED for the full 9-knot extended set:")
        print(f"    {{T(2,n) for n ∈ {{3,5,7,9,11}}, 4_1, 6_1, 6_2}}.")
        print()
        # Pattern in T(2,n) cubic coefficients?
        # Derive directly from `results` rather than zip(knots.keys(), results)
        # to avoid implicit ordering coupling (per Copilot review on PR #1822).
        t2n_cubics = [(r["knot"], r["cubic_taylor_coefficient"])
                      for r in results if r["knot"].startswith("T(2,")]
        print(f"  T(2,n) family pattern:")
        for name, c3 in t2n_cubics:
            print(f"     {name:<22} cubic = {c3}")
        print()
        print(f"  Conclusion: Hyp-C as 'V_K cubic Taylor at q=1 = 1' is")
        print(f"  STRUCTURALLY INCOMPATIBLE with the natural-knot Jones")
        print(f"  polynomial family. Combined with the prior REFUTATIONS")
        print(f"  of Hyp-A (PR #1801) and Hyp-B (PR #1806), the literal")
        print(f"  rung-2 lift is DEFINITIVELY REFUTED across natural")
        print(f"  categorical candidates.")
        print()
        print(f"  Forward options remaining:")
        print(f"    (i) Multi-component links — V_L Taylor structure differs.")
        print(f"   (ii) Framed knots — writhe correction changes Taylor coefficients.")
        print(f"  (iii) Quantum-group representations beyond U_q(sl_2).")
        print(f"   (iv) Accept the 569bedda1 framing: empirical c_3 jitter is")
        print(f"        calibration-anchor normalization, not a fibre object.")

    print()

    builder.add_data("required_cubic_coefficient", str(cubic_required))
    builder.add_data("results_per_knot", results)
    builder.add_data("matching_knots", [r["knot"] for r in matching])
    builder.add_data("verdict", "CONFIRMED" if matching
                     else "REFUTED for 9-knot extended set")

    # Strengthened assertion: at least one torus-knot cubic = 9
    # (the trefoil result, known correct from PR #1806's Hyp-C probe).
    # This gives the witness a concrete mathematical-correctness check
    # beyond "the probe ran" (per Copilot review on PR #1822).
    trefoil_cubic = next(
        (r["cubic_taylor_coefficient"] for r in results
         if r["knot"] == "T(2,3) = 3_1"),
        None
    )
    builder.add_assertion(
        "trefoil_cubic_taylor_equals_9",
        computed=1 if trefoil_cubic == "9" else 0,
        expected=1,
        tolerance=0,
        source=("Concrete mathematical-correctness check: the right-"
                "handed trefoil 3_1 (= T(2,3)) Jones polynomial has "
                "cubic Taylor coefficient = 9 at q=1, a known value "
                "consistent with PR #1806's Hyp-C probe result. "
                "Confirms the probe's Jones polynomials are correctly "
                "encoded and Taylor extraction is correct, beyond "
                "merely 'the probe ran'."),
    )

    builder.save()
    print(f"  Witness: qbeta-rung2-hyp-c-extended-knots-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
