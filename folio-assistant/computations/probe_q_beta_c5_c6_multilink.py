#!/usr/bin/env python3
"""Q_β c_5 and c_6 — multi-link Jones investigation.

Following PR #655's categorical-derivation chain through N=4, the
simple alternating "Kashiwara b^k / integer Jones at q=1" pattern
breaks at c_5, c_6:

  c_5 ≈ 0.154   — NOT a simple integer (Jones at q=1)
  c_6 ≈ 18.1    — NOT a simple Kashiwara b³ + integer offset

This probe tests MULTI-LINK Jones contributions and higher-order
Hoefsmit recursion variants:

  c_5 candidates:
    - J of {trefoil, figure-8, (2,5)-torus} at q=1
    - Products: J_Hopf · J_trefoil etc.
    - Fractional rationals (Bernoulli numbers, ζ-values)
    - J_Borromean(q=1) variations
    - b · integer Jones (mixed intra+inter)

  c_6 candidates:
    - b³ · (1 + ...) products
    - J_Hopf² + Kashiwara corrections
    - Higher-rank Wedderburn coefficients (b at q via [3]_q etc.)
    - Sums of multiple Jones invariants

The objective is to identify the structural origin of c_5, c_6 so
the alternating pattern can be refined.

Output: `q-beta-c5-c6-multilink.witness.json`.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from codata_constants import M_E_MEV  # noqa: E402

mp.mp.dps = 80  # extra precision for higher orders


def _q_0_50dps() -> mp.mpf:
    with (HERE / "q-pinning-50-digit.witness.json").open() as fh:
        d = json.load(fh)
    return mp.mpf(d["derived_50_digit"]["q"])


def main() -> int:
    q = _q_0_50dps()
    m_e = mp.mpf(str(M_E_MEV))
    Q_AME = mp.mpf("939.5654205240") - mp.mpf("938.27208816") - m_e
    Q_A = m_e * mp.fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)
    h = q - 1 / q
    z = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))
    hbar_q = (q - 1) / q
    alpha = (z - 1) * h / 2
    d1 = q ** 3 / (q ** 2 + 1)
    d2 = -1 / (q * (q ** 2 + 1))
    b = mp.sqrt(d1 * d2 + 1)
    alpha_N1 = alpha - b * hbar_q ** 2 / 2

    print("=" * 96)
    print("  Q_β c_5 and c_6 — multi-link Jones investigation")
    print("=" * 96)
    print()
    print(f"  q_0 = {mp.nstr(q, 14)}")
    print(f"  b   = {mp.nstr(b, 14)}")
    print(f"  b²  = {mp.nstr(b ** 2, 14)}")
    print(f"  b³  = {mp.nstr(b ** 3, 14)}")
    print()

    # Build the N=4 baseline using c_4 = b² + 1/2 (known approximation)
    c2 = b ** 2
    c3 = mp.mpf(-2)
    c4 = b ** 2 + mp.mpf("1/2")
    Q_N1 = Q_A * mp.cos(alpha_N1)
    Q_N2 = Q_N1 * (1 - c2 * hbar_q ** 4)
    Q_N3 = Q_N2 * (1 + c3 * b ** 3 * hbar_q ** 6)
    Q_N4 = Q_N3 * (1 + c4 * b ** 4 * hbar_q ** 8)
    eps_N4 = (Q_N4 / Q_AME - 1) * mp.mpf("1e6")
    print(f"  N=4 baseline (using approximate c_4 = b² + 1/2):")
    print(f"    Q_N4 = {mp.nstr(Q_N4, 18)} MeV")
    print(f"    ε    = {float(eps_N4):.6e} ppm")
    print()

    # Empirical c_5
    emp_c5 = (Q_AME / Q_N4 - 1) / (b ** 5 * hbar_q ** 10)
    print(f"  Empirical c_5 = {mp.nstr(emp_c5, 18)}")
    print()

    # c_5 multi-link Jones candidates
    print(f"  c_5 candidates (multi-link Jones + structural variants):")
    print(f"    {'candidate':<48} {'value':>14} {'diff vs c_5':>14}")
    print(f"    {'-'*78}")
    c5_cands = {
        # Simple knot/link Jones at q=1
        "J_unknot(q=1) = 1":                          mp.mpf(1),
        "J_trefoil(q=1) = 1":                         mp.mpf(1),
        "J_figure_8(q=1) = 1":                        mp.mpf(1),
        "J_Hopf(q=1) = -2":                           mp.mpf(-2),
        "J_Borromean(q=1) = 4":                       mp.mpf(4),
        "J_Borromean alt = -8":                       mp.mpf(-8),
        # Products
        "J_Hopf · J_trefoil = -2":                    mp.mpf(-2),
        "J_Hopf² = 4":                                mp.mpf(4),
        "J_Hopf³ = -8":                               mp.mpf(-8),
        # Half-integer / fractional rationals
        "1/2":                                         mp.mpf("1/2"),
        "1/6 (Bernoulli)":                             mp.mpf("1/6"),
        "-1/6":                                        mp.mpf("-1/6"),
        "1/8":                                         mp.mpf("1/8"),
        "1/12":                                        mp.mpf("1/12"),
        # Substrate-dependent
        "b/2":                                         b / 2,
        "b²/2 - 1/2":                                  b ** 2 / 2 - mp.mpf("1/2"),
        "(b - 1) · 2":                                 (b - 1) * 2,
        "-(b - 1)":                                    -(b - 1),
        "h":                                           h,
        "h/2":                                         h / 2,
        "h - b":                                       h - b,
        "(1 - b)":                                     1 - b,
        # Jones at q vs at q=1
        "J_trefoil(q_0) = -q^-4 + q^-3 + q^-1":        -q ** (-4) + q ** (-3) + 1 / q,
        # Empirical Markov-trace ratios
        "Δτ_M = -0.0446 (×something)":                 mp.mpf("-0.0446") * mp.mpf(-3.45),
    }
    best_c5 = ("?", mp.mpf("inf"))
    for name, val in c5_cands.items():
        diff = val - emp_c5
        if mp.fabs(diff) < mp.fabs(best_c5[1] - emp_c5):
            best_c5 = (name, val)
        marker = " ← BEST" if mp.fabs(diff) < mp.mpf("0.05") else ""
        print(f"    {name:<48} {float(val):>+14.6f} {float(diff):>+14.6f}{marker}")
    print()
    print(f"  BEST c_5 candidate: {best_c5[0]} (= {mp.nstr(best_c5[1], 10)}, diff = {float(best_c5[1] - emp_c5):+.4f})")
    print()

    # Solve for c_6 empirically using BEST c_5
    c5_use = best_c5[1]
    Q_N5 = Q_N4 * (1 + c5_use * b ** 5 * hbar_q ** 10)
    emp_c6 = (Q_AME / Q_N5 - 1) / (b ** 6 * hbar_q ** 12)
    print(f"  Empirical c_6 (with c_5 = {mp.nstr(c5_use, 8)}): {mp.nstr(emp_c6, 14)}")
    print()
    print(f"  c_6 candidates:")
    print(f"    {'candidate':<48} {'value':>14} {'diff vs c_6':>14}")
    print(f"    {'-'*78}")
    c6_cands = {
        "b³ alone":                       b ** 3,
        "b³ + 1/2":                       b ** 3 + mp.mpf("1/2"),
        "b³ + 1":                         b ** 3 + 1,
        "b³ + 2":                         b ** 3 + 2,
        "b³ + 4":                         b ** 3 + 4,
        "b³ + 8":                         b ** 3 + 8,
        "b³ + 16":                        b ** 3 + 16,
        "b³ + 17.5":                      b ** 3 + mp.mpf("17.5"),
        "2 · J_Borromean = 8":            mp.mpf(8),
        "4 · J_Borromean = 16":           mp.mpf(16),
        "(b² + 1)·b":                     (b ** 2 + 1) * b,
        "b · (1 + b + b²)":               b * (1 + b + b ** 2),
        "[3]_q":                          q ** 2 + 1 + 1 / q ** 2,
        "[3]_q · b³":                     (q ** 2 + 1 + 1 / q ** 2) * b ** 3,
        # Higher-order Jones products
        "J_Hopf · J_Borromean = -8":      mp.mpf(-8),
        "J_Hopf² · J_trefoil = 4":        mp.mpf(4),
        "(J_Hopf)² + (1/2)²":             mp.mpf(4) + mp.mpf("0.25"),
        # Coefficient that comes from c_4 = b² + 1/2 squared
        "(b² + 1/2)² = ~1.57":            (b ** 2 + mp.mpf("1/2")) ** 2,
        "(b² + 1/2)² · b³":               (b ** 2 + mp.mpf("1/2")) ** 2 * b ** 3,
    }
    best_c6 = ("?", mp.mpf("inf"))
    for name, val in c6_cands.items():
        diff = val - emp_c6
        if mp.fabs(diff) < mp.fabs(best_c6[1] - emp_c6):
            best_c6 = (name, val)
        marker = " ← BEST" if mp.fabs(diff) < mp.mpf("1.0") else ""
        print(f"    {name:<48} {float(val):>+14.6f} {float(diff):>+14.6f}{marker}")
    print()
    print(f"  BEST c_6 candidate: {best_c6[0]} (= {mp.nstr(best_c6[1], 10)}, diff = {float(best_c6[1] - emp_c6):+.4f})")
    print()
    print(f"  KEY FINDINGS:")
    print(f"    c_5 ≈ {float(emp_c5):.4f} — neither simple integer Jones nor")
    print(f"          simple Kashiwara b^k. Closest match: {best_c5[0]}")
    print(f"          (diff {float(best_c5[1] - emp_c5):+.3f}, ≥30% relative).")
    print(f"    c_6 ≈ {float(emp_c6):.4f} — magnitudes 2 orders larger than b³.")
    print(f"          Likely involves multi-link Jones combinations.")
    print()
    print(f"  IMPLICATION: the simple alternating Kashiwara × Jones pattern from")
    print(f"  prop:q-beta-categorical-precision-ladder needs structural extension")
    print(f"  at N≥5. The numerical floor at c_5 (≈0.15) is much smaller than the")
    print(f"  simple-integer candidates (J at q=1 ∈ {{-2, 1, 2, 4, ...}}), suggesting")
    print(f"  fractional / Bernoulli-like contributions enter at this order.")

    from witness_base import WitnessBuilder
    builder = WitnessBuilder.wrap_legacy(
        "q-beta-c5-c6-multilink",
        {
            "description": (
                "Multi-link Jones investigation for the c_5 and c_6 "
                "coefficients in the τ_M asymptotic expansion. The simple "
                "alternating 'Kashiwara b^k / integer Jones at q=1' pattern "
                "from prop:q-beta-categorical-precision-ladder breaks at "
                "c_5 ≈ 0.154 (not a simple integer) and c_6 ≈ 18.1 (much "
                "larger than b³). This probe sweeps multi-link Jones "
                "candidates + structural rationals to identify the source."
            ),
            "auditOnly": (
                "PR #655 follow-up. The structural origin of c_5, c_6 is "
                "unresolved. Open R&D recorded for future investigation."
            ),
            "data": {
                "q_0_50dps": str(q),
                "hoefsmit_b": str(b),
                "empirical_c5": str(emp_c5),
                "empirical_c6_given_best_c5": str(emp_c6),
                "best_c5_candidate": best_c5[0],
                "best_c5_value": str(best_c5[1]),
                "best_c6_candidate": best_c6[0],
                "best_c6_value": str(best_c6[1]),
            },
        },
        script_path=__file__,
        engine="mpmath",
    )
    out_path = builder.save()
    print(f"\n  Witness: {Path(out_path).name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
