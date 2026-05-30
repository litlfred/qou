#!/usr/bin/env python3
"""alpha_em_4pi_combined_derivation.py — combined gap (i+ii+iii) probe.

Each individual sub-gap has been refuted:
  Gap (i)   H_3 matter insertion:        -445% off  (#1466)
  Gap (ii)  Bring-surface integration:    -67% off  (#1471)
  Gap (iii) Q_q vertex factor:           +11.2% off (#1469)

This probe tests whether the COMBINATION of structural elements
(matter trace × charge vertices × Bring surface factor) can produce
α/(4π), and also tests the framework's OWN mentioned candidates from
em-coupling-bring-zero-mode.md line 206-210:

  "Compute next-loop self-energy as a 2-loop graph; verify the
   coefficient is exactly 1/(4π) or identifies as 1/(2π[2]_q) or
   1/(4π)·(1-ℏ_q²) (best fits at ∼ 0.4%)."

THE QED-LIKE EXPANSION.
The structural ansatz for α/(4π):

  α/(4π) = α_EM · F(q)

where α_EM ≈ 1/137.036 comes from the tree + zero-mode terms, and F(q)
is the "1/(4π)" factor — possibly q-deformed.

If F(q) = 1/(4π) exactly: α/(4π) = (1/137.036)/(4π) = 5.805e-4 ✓
If F(q) = 1/(2π[2]_q): α·F = (1/137.036) · 1/(2π·2.011) = 0.0792/137.036
If F(q) = (1-ℏ_q²)/(4π): ...

We test these honestly + several COMBINED forms involving the gap
(i), (ii), (iii) elements.
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
from q_parameter import Q_50_DIGIT_STR  # noqa: E402


def q_bracket(n: int, q):
    if n == 0:
        return mpf(0)
    return (q**n - q**(-n)) / (q - q**(-1))


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "alpha-em-4pi-combined-derivation",
        engine="mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Combined gap (i+ii+iii) probe for α/(4π) + test of "
        "framework's mentioned candidates 1/(2π[2]_q), 1/(4π)·(1-h_q²). "
        "Each individual sub-gap (matter trace, Bring integration, Q_q "
        "vertex) was refuted in #1466, #1469, #1471. This probe tests "
        "whether their COMBINATION closes α/(4π) and whether the "
        "framework's own q-deformed-1/(4π) candidates match."
    )
    builder.set_content_block("prop:em-coupling-bring-zero-mode")

    q = mpf(Q_50_DIGIT_STR)
    h = q - 1 / q
    bra2 = q_bracket(2, q)
    bra3 = q_bracket(3, q)
    bra9 = q_bracket(9, q)
    bra10 = q_bracket(10, q)
    g = 4
    area_bring = mpf(4 * pi * (g - 1))  # 12π
    bring_shift = mpf(2 * g) / (4 * pi * (g - 1))  # 2/(3π)

    CODATA_alpha_inv = mpf(str(ALPHA_EM_INV))
    alpha = 1 / CODATA_alpha_inv
    TARGET = alpha / (4 * pi)

    print("=" * 76)
    print(" α/(4π) DERIVATION — COMBINED probe + framework-mentioned candidates")
    print("=" * 76)
    print(f"  target α/(4π) = {mp.nstr(TARGET, 18)}")
    print(f"  α_EM (CODATA) = {float(alpha):.8e}")
    print(f"  h_q = q-q⁻¹ = {float(h):.6f}    h_q² = {float(h**2):.6f}")
    print(f"  [2]_q = {float(bra2):.6f}    1/(2π[2]_q) = {float(1/(2*pi*bra2)):.6e}")
    print(f"  1/(4π) = {float(1/(4*pi)):.6e}    1/(4π)·(1-h_q²) = {float((1-h**2)/(4*pi)):.6e}")
    print()

    # ── PART A: framework's mentioned candidates for 1/(4π) ──────
    # These would multiply α to give α/(4π) — equivalently, divided
    # into α should match TARGET.
    print("  PART A: framework-mentioned 1/(4π) candidates (per prop line 206-210)")
    framework_candidates = [
        ("1/(4π) standard",               mpf(1) / (4 * pi)),
        ("1/(2π·[2]_q)",                  mpf(1) / (2 * pi * bra2)),
        ("1/(4π)·(1-h_q²)",               (1 - h**2) / (4 * pi)),
        ("1/(4π)·(1-h_q²/2)",             (1 - h**2/2) / (4 * pi)),
        ("1/(4π·[2]_q/2)",                mpf(1) / (4 * pi * bra2 / 2)),
        ("1/(2π·[2]_q)·(1-h_q²/4)",       (1 - h**2/4) / (2 * pi * bra2)),
    ]
    print(f"  {'candidate':35s} {'F(q)':>14s} {'α·F(q)':>14s} {'ratio to TARGET':>16s}")
    results = []
    best = None
    for name, F_val in framework_candidates:
        product = alpha * F_val
        ratio = float(product / TARGET)
        results.append({
            "type": "framework-1/(4π)",
            "name": name,
            "F_value": mp.nstr(F_val, 12),
            "alpha_times_F": mp.nstr(product, 12),
            "ratio_to_target": ratio,
        })
        print(f"  {name[:33]:35s} {float(F_val):>14.6e} {float(product):>14.6e} {ratio:>16.6f}")
        if best is None or abs(ratio - 1) < abs(best["ratio_to_target"] - 1):
            best = results[-1]

    print()
    print("  PART B: COMBINED gap (i+ii+iii) — joint product structures")
    print(f"  {'candidate':45s} {'value':>14s} {'ratio to TARGET':>16s}")

    # ── PART B: combined structural products ────────────────────
    # Joint elements:
    #   matter Q_q factor:  [w(K_m)]_q² for matter knot K_m
    #   matter trace:       tr_M on H_n
    #   Bring factor:       (Bring shift)^k / Area^j or similar
    #   photon denom:       [9]_q · [10]_q
    photon_denom = bra9 * bra10

    combined_candidates = [
        # h_q² · Bring shift · α (q-corrected QED-like)
        ("α·h_q²/(2π·[2]_q)",
         alpha * h**2 / (2 * pi * bra2)),
        ("α·h_q²/(4π)",
         alpha * h**2 / (4 * pi)),
        ("(Bring_shift)² / (16π²)",
         bring_shift**2 / (16 * pi**2)),
        ("(Bring_shift)² · h_q² / (4π)",
         bring_shift**2 * h**2 / (4 * pi)),
        ("[3]_q² · h_q² / ([9]_q·[10]_q · 4π)",
         bra3**2 * h**2 / (photon_denom * 4 * pi)),
        ("[2]_q² · h_q²·Bring_shift / (4π · photon_denom)",
         bra2**2 * h**2 * bring_shift / (4 * pi * photon_denom)),
        ("h_q² · Bring_shift / (2π · [9]_q · [10]_q)",
         h**2 * bring_shift / (2 * pi * photon_denom)),
        ("(Bring_shift/[2]_q)² / Area",
         (bring_shift/bra2)**2 / area_bring),
        ("h_q⁴ · [9]_q · [10]_q / (4π · Area² · 2g)",
         h**4 * photon_denom / (4 * pi * area_bring**2 * 2 * g)),
        # Per em-coupling-projection.md Layer 1+2+3 product:
        ("Q²·tr_M·Bring  [2]_q²·h_q · (2/(3π)) / ([9]·[10]·4π)",
         bra2**2 * h * bring_shift / (photon_denom * 4 * pi)),
    ]
    for name, val in combined_candidates:
        ratio = float(val / TARGET) if abs(val) > 1e-50 else float("nan")
        results.append({
            "type": "combined",
            "name": name,
            "value": mp.nstr(val, 12),
            "ratio_to_target": ratio,
        })
        print(f"  {name[:43]:45s} {float(val):>14.6e} {ratio:>16.6f}")
        if ratio == ratio and abs(ratio - 1) < abs(best["ratio_to_target"] - 1):
            best = results[-1]

    print()
    print(f"  TARGET α/(4π) = {float(TARGET):.6e}")
    print()
    # Note: Part A "1/(4π) standard" is TAUTOLOGICAL — it computes
    # α·(1/(4π)) which is α/(4π) by definition. Not a derivation.
    # The MEANINGFUL best is the best NON-tautological candidate.
    meaningful_results = [r for r in results
                          if r["name"] != "1/(4π) standard"]
    best_meaningful = min(meaningful_results,
                          key=lambda r: abs(r["ratio_to_target"] - 1))
    print(f"  Best overall:  [{best['type']}]  {best['name']}")
    print(f"     ratio = {best['ratio_to_target']:.8f}")
    print(f"     deviation = {(best['ratio_to_target']-1)*100:+.4f}%")
    if best["name"] == "1/(4π) standard":
        print(f"     ⚠ TAUTOLOGICAL: α·(1/(4π)) = α/(4π) by definition.")
        print(f"  Best NON-tautological: [{best_meaningful['type']}]  "
              f"{best_meaningful['name']}")
        print(f"     ratio = {best_meaningful['ratio_to_target']:.8f}")
        print(f"     deviation = {(best_meaningful['ratio_to_target']-1)*100:+.4f}%")
        best = best_meaningful

    # ─── HONEST VERDICT ─────────────────────────────────────────
    print()
    print("=" * 76)
    print(" Honest verdict")
    print("=" * 76)
    dev = abs(best["ratio_to_target"] - 1) * 100
    if dev < 0.01:
        verdict = (f"EXACT — {best['name']} hits α/(4π) to <0.01%")
        print(f"  ✓✓ {verdict}")
    elif dev < 0.5:
        verdict = (f"DERIVED — {best['name']} matches within 0.5%")
        print(f"  ✓ {verdict}")
    elif dev < 5:
        verdict = (f"NEAR-MATCH ({dev:.2f}%) — STILL in fit-class regime")
        print(f"  ~ {verdict}")
        print(f"  Best: {best['name']}")
        print(f"  At this precision level, this is exactly the kind of")
        print(f"  near-miss the proposition warns against.")
    else:
        verdict = (f"REFUTED — best is {dev:.1f}% off")
        print(f"  ✗ {verdict}")

    print()
    print(f"  Full cumulative refutation map across all attempted")
    print(f"  approaches for the α/(4π) next-order term:")
    print(f"    Fit-class (12 candidates):              REFUTED (#1453)")
    print(f"    B_2 PSLQ at Bring-sym angles:           PARTIAL")
    print(f"    B_3 PSLQ unit-circle:                   PARTIAL (#1457)")
    print(f"    B_3 PSLQ off-circle (maxcoeff 1000):    PARTIAL (#1457)")
    print(f"    B_4 PSLQ:                               PARTIAL (#1462)")
    print(f"    Prior PSLQ uniqueness (52-elt, 1500dps): null")
    print(f"    Gap (i)   H_3 matter insertion:    -445% off  (#1466)")
    print(f"    Gap (ii)  Bring-surface integration: -67% off  (#1471)")
    print(f"    Gap (iii) Q_q vertex factor:       +11.2% off (#1469)")
    print(f"    Combined (i+ii+iii) + framework q-deformed candidates:")
    print(f"      best {best['name']} at {best['ratio_to_target']*100-100:+.2f}%")
    print()
    print(f"  All conventional structural approaches exhausted.")
    print(f"  The empirical refutation map is comprehensive.")

    builder.add_data("target_alpha_over_4pi", mp.nstr(TARGET, 30))
    builder.add_data("alpha_em_codata", mp.nstr(alpha, 30))
    builder.add_data("framework_mentioned_candidates",
                     [r for r in results if r["type"] == "framework-1/(4π)"])
    builder.add_data("combined_candidates",
                     [r for r in results if r["type"] == "combined"])
    builder.add_data("best_overall", best)
    builder.add_data("final_verdict", verdict)
    builder.add_data("cumulative_refutation_summary", {
        "fit_class": "REFUTED (#1453)",
        "B_3_unit_circle": "PARTIAL (#1457)",
        "B_3_off_circle": "PARTIAL (#1457)",
        "B_4": "PARTIAL (#1462)",
        "gap_i_H_3_matter": "REFUTED -445% (#1466)",
        "gap_ii_bring_surface": "REFUTED -67% (#1471)",
        "gap_iii_Q_q_vertex": "REFUTED +11.2% (#1469)",
        "combined": f"{best['ratio_to_target']*100-100:+.2f}% best — {verdict}",
    })

    builder.add_assertion(
        "candidates_evaluated",
        computed=len(results),
        expected=len(framework_candidates) + len(combined_candidates),
        tolerance=0,
        source="Framework-mentioned + combined structural candidates "
               "tested honestly at q_0 (50 dps).",
    )
    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
