#!/usr/bin/env python3
"""alpha_em_4pi_qq_vertex_factor.py — gap (iii) of #1466: test the
Q_q charge-vertex hypothesis for the 1-loop self-energy α/(4π).

STRUCTURAL ARGUMENT (from em-coupling-projection.md, Layer 1).
The canonical EM charge of a knot K in this framework is its q-writhe:
  Q_q(K) = [w(K)]_q = (q^w − q^{−w}) / (q − q^{−1})
where w(K) is the signed-crossing sum.

A 1-loop self-energy diagram has TWO photon-matter vertices, each
contributing one Q_q factor. The "matter loop" between the vertices
is a closed strand of some matter knot K_m. The structural template,
parallel to how the leading 2/(3π) came from dim H¹/Area:

  Π_1-loop(K_m)  =  Q_q(K_m)² / ([9]_q·[10]_q · N(K_m))

where N(K_m) is a Bring-derived normalization (the categorical analog
of the QED 1/(4π) factor coming from dimensional analysis on Bring's
surface).

WHAT WE TEST.
For each candidate matter knot K_m, compute Π_1-loop with three
candidate normalizations N:
  (N1) 4π            — single Bring-area factor (parallel to 2/(3π) leading)
  (N2) Area_Bring    = 12π
  (N3) 4π · Area_Bring = 48π²

Candidate matter knots (drawn from canonical small-crossing list):
  K_m       w(K_m)   [w]_q at q_0    structural motivation
  unknot    0        0               TRIVIAL (gives Π=0; sanity)
  T_{2,3}   3        [3]_q ≈ 3.31    SIMPLEST nontrivial torus knot
  4_1       0        [0]_q = 0       Figure-8; framework's electron knot
                                      (mass via Vol(4_1)/ℏ²); writhe 0
  T_{2,5}   5        [5]_q ≈ 5.50    Next torus knot after T_{2,3}
  T_{3,4}   8        [8]_q ≈ 9.51    Genus-3 torus knot
  σ_2 (B_2)  1       [1]_q = 1       Single H_2 crossing as "matter"
  σ_1·σ_2   2        [2]_q ≈ 2.01    H_3 simplest two-crossing

HONEST DERIVE-OR-REFUTE.
- If a structurally-motivated K_m + N gives Π_1-loop = α/(4π) to high
  precision, we have a candidate derivation. Verify with second
  independent check (e.g. q-expansion).
- If best match is in the 0.5-5% range, it's a near-miss; report
  honestly as fit-class trap (proposition's explicit warning).
- If all candidates miss by >5%, gap (iii) by itself is also
  insufficient; need to combine with extensions (i)+(ii) from #1466.
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
        "alpha-em-4pi-qq-vertex-factor",
        engine="mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Gap (iii) attempt from #1466: test the Q_q charge-vertex "
        "hypothesis for the 1-loop self-energy α/(4π). The canonical "
        "EM charge in this framework is Q_q(K) = [w(K)]_q (Layer 1 of "
        "em-coupling-projection.md). A 1-loop self-energy diagram has "
        "two photon-matter vertices, so the contribution scales as "
        "Q_q(K_m)² for matter knot K_m. We test 7 canonical matter "
        "knots × 3 Bring normalizations = 21 derive-or-refute "
        "candidates, honestly reporting matches/non-matches."
    )
    builder.set_content_block("prop:em-coupling-bring-zero-mode")

    q = mpf(Q_50_DIGIT_STR)
    CODATA_alpha_inv = mpf(str(ALPHA_EM_INV))
    TARGET = (1 / CODATA_alpha_inv) / (4 * pi)
    bra9 = q_bracket(9, q)
    bra10 = q_bracket(10, q)
    photon_denom = bra9 * bra10  # the tree denominator

    print("=" * 76)
    print(" α/(4π) DERIVATION — gap (iii): Q_q charge-vertex hypothesis")
    print("=" * 76)
    print(f"  q₀ = {float(q):.14f}")
    print(f"  target α/(4π) = {mp.nstr(TARGET, 18)}")
    print(f"  photon denom [9]_q·[10]_q = {float(photon_denom):.6f}")
    print()

    # ── canonical matter-knot candidates with structural motivation ─
    matter_knots = [
        ("unknot",         0, "TRIVIAL — sanity (Π should vanish)"),
        ("T_{2,3} trefoil", 3, "SIMPLEST nontrivial torus knot; genus 1"),
        ("4_1 figure-8",    0, "Framework's electron mass anchor (Vol/ℏ²); w=0"),
        ("T_{2,5}",         5, "Next torus knot; genus 2"),
        ("T_{3,4}",         8, "Genus-3 torus knot"),
        ("σ_2 (B_2)",       1, "Single H_2 crossing as 'matter'"),
        ("σ_1·σ_2 (B_3)",   2, "H_3 simplest two-crossing"),
    ]

    # ── three Bring normalizations ──────────────────────────────
    normalizations = [
        ("N1 = 4π",            4 * pi,                "Single Bring-area factor"),
        ("N2 = 12π (Area_Bring)", 12 * pi,            "Full Bring-surface area"),
        ("N3 = 4π·Area = 48π²",  4 * pi * 12 * pi,    "Bring·QED combined"),
    ]

    print(f"  Testing {len(matter_knots)} × {len(normalizations)} = "
          f"{len(matter_knots) * len(normalizations)} candidates:")
    print()
    print(f"  {'matter knot':25s} {'[w]_q²':>10s}  ", end="")
    for nname, _, _ in normalizations:
        print(f"  {nname[:14]:>14s}", end="")
    print()
    print("  " + "-" * 78)

    results = []
    best_overall = None
    for kname, w, krat in matter_knots:
        qw = q_bracket(w, q)
        qw_sq = qw * qw
        row = []
        for nname, N, nrat in normalizations:
            if abs(qw_sq) < mpf("1e-50"):
                pi_loop = mpf(0)
                dev_pct = float("nan")  # undefined for zero candidate
            else:
                pi_loop = qw_sq / (photon_denom * N)
                dev_pct = float((pi_loop / TARGET - 1) * 100)
            results.append({
                "matter_knot": kname,
                "writhe": w,
                "q_bracket_w": mp.nstr(qw, 12),
                "normalization_label": nname,
                "normalization_value": mp.nstr(N, 12),
                "pi_loop": mp.nstr(pi_loop, 14),
                "ratio_to_target": float(pi_loop / TARGET) if abs(pi_loop) > 0 else 0.0,
                "deviation_percent": dev_pct,
            })
            row.append((pi_loop, dev_pct))
            if dev_pct == dev_pct and pi_loop > 0:  # not NaN, real candidate
                if best_overall is None or abs(dev_pct) < abs(best_overall["deviation_percent"]):
                    best_overall = results[-1]
        # Print row
        print(f"  {kname[:23]:25s} {float(qw_sq):>10.4f}  ", end="")
        for pi_v, dev in row:
            print(f"  {float(pi_v):>14.4e}", end="")
        print()
        print(f"  {' '*25} {' '*10}  ", end="")
        for pi_v, dev in row:
            tag = ""
            if isinstance(dev, float) and dev == dev:  # not NaN
                if abs(dev) < 0.5:
                    tag = "✓✓"
                elif abs(dev) < 5:
                    tag = "~"
                else:
                    tag = " "
                print(f"  {dev:>+12.2f}%{tag:1s}", end="")
            else:
                print(f"  {'(undef)':>14s} ", end="")
        print()

    print()
    print(f"  TARGET α/(4π) = {float(TARGET):.6e}")
    print()
    print(f"  Best overall: {best_overall['matter_knot']} × "
          f"{best_overall['normalization_label']}")
    print(f"    Π_1-loop = {best_overall['pi_loop']}")
    print(f"    deviation = {best_overall['deviation_percent']:+.4f}%")

    # ─── honest verdict ────────────────────────────────────────
    print()
    print("=" * 76)
    print(" Honest verdict")
    print("=" * 76)
    abs_dev = abs(best_overall["deviation_percent"])
    if abs_dev < 0.5:
        verdict = (f"DERIVED — {best_overall['matter_knot']} × "
                   f"{best_overall['normalization_label']} gives α/(4π) within 0.5%")
        print(f"  ✓ {verdict}")
        print(f"  Pin: matter = {best_overall['matter_knot']}, normalization = "
              f"{best_overall['normalization_label']}")
        print(f"  Required next step: independent verification via q-expansion")
        print(f"  or alternative derivation (e.g. RT shadow-world).")
    elif abs_dev < 5:
        verdict = (f"NEAR-MATCH ({abs_dev:.2f}%) but NOT a derivation — "
                   f"in fit-class regime per proposition warning")
        print(f"  ~ {verdict}")
        print(f"  Best: {best_overall['matter_knot']} × "
              f"{best_overall['normalization_label']} ({best_overall['deviation_percent']:+.2f}%)")
        print(f"  This level of match could be coincidence — the proposition")
        print(f"  explicitly warns: 'The simplest fits are all near-misses.'")
        print(f"  Required next step: identify a CANONICAL reason to prefer")
        print(f"  this matter knot + normalization over the others.")
    else:
        verdict = (f"REFUTED — best candidate {abs_dev:.1f}% off; "
                   "Q_q-vertex hypothesis alone is insufficient")
        print(f"  ✗ {verdict}")
        print(f"  Combined with #1466 (H_3 matter insertion REFUTED at -445%),")
        print(f"  the structural conclusion is: neither gap (i) nor gap (iii)")
        print(f"  alone closes α/(4π). The remaining open path is gap (ii)")
        print(f"  Bring-surface integration, or a COMBINED derivation that")
        print(f"  joins all three structural elements.")

    print()

    builder.add_data("inputs", {
        "q0": mp.nstr(q, 30),
        "CODATA_source": "experimental_constants.ALPHA_EM_INV",
        "target_alpha_over_4pi": mp.nstr(TARGET, 30),
        "photon_denom": mp.nstr(photon_denom, 20),
    })
    builder.add_data("candidates", results)
    builder.add_data("best", best_overall)
    builder.add_data("verdict", verdict)
    builder.add_data("structural_argument", (
        "Q_q(K) = [w(K)]_q is Layer 1 of the em-coupling-projection.md "
        "tree-term derivation (canonical EM charge in this framework). "
        "A 1-loop self-energy diagram has 2 photon-matter vertices, so "
        "Π ~ Q_q(K_m)². The hypothesis tested here is "
        "Π = Q_q(K_m)² / (photon_denom · N) for matter knot K_m and "
        "Bring normalization N. Result documents which K_m + N "
        "structurally produce α/(4π) (if any)."
    ))

    builder.add_assertion(
        "candidates_evaluated",
        computed=len(results),
        expected=len(matter_knots) * len(normalizations),
        tolerance=0,
        source=f"{len(matter_knots)} matter knots × {len(normalizations)} "
               f"Bring normalizations = {len(matter_knots)*len(normalizations)} "
               "candidates evaluated honestly.",
    )
    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
