#!/usr/bin/env python3
"""qbeta_c3_habiro_3rung_crossanchor_rigidity_probe.py — falsification test
for the [3]_q/25 3-rung c_3 closure (PR #1781).

## The question (Δ_λ-gate-safe — falsification, NOT a new fit)

PR #1781 found a 3-rung Habiro closure that reproduces empirical c_3 to
2.65 ppm AT THE PROTON ANCHOR:

    c_3(q) = -(q² + q⁻²)·(1 + ℏ_q·[3]_q/25 + ℏ_q³/[2]_q)

Is this a GENUINE fibre-level Habiro element (reproduces empirical c_3
at EVERY q₀ anchor) or a PROTON-ANCHOR COINCIDENCE (matches at one q₀
only)? Per AGENTS.md §"Im(q) at fibre vs observable level":
  ❌ a REAL formula c_3 = f(q_real) matching multiple anchors — known to fail
  ✓ a FIBRE Habiro element F(q) at roots of unity — different question

This probe runs the discriminator: evaluate the real-q 3-rung formula at
BOTH established anchors and compare its swing to the empirical c_3 swing.

## The established cross-anchor facts (from PR #1609 infra)

| anchor | q₀ | empirical c_3 |
|--------|-----|---------------|
| proton (m_p) | 1.10997858275… | -2.0693 |
| muon   (m_μ) | 1.10997859555… | -2.0097 |

Anchor separation ≈ 1.3e-8, yet empirical c_3 swings ≈ 2.88% — c_3 is a
hyper-sensitive EXTRACTED quantity (it's the tiny c_3·u³ ladder term, so
minute q shifts get amplified ~4.6e6×).

## Prediction

A smooth real-q formula CANNOT have a derivative dc_3/dq ≈ 4.6e6 near the
anchor, so the 3-rung formula's swing should be MICROSCOPIC vs the 2.88%
empirical swing — REFUTING it as a real-q fibre element and CONFIRMING it
is a proton-anchor near-match. That sharpens the search: the genuine
Habiro element must be complex-analytic / root-of-unity, NOT the real-q
[3]_q/25 form (which stays the production-honest NEAR-MATCH tier).
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent.parent / "tools" / "qou-substrate" / "python"))

import _path_bridge  # noqa: E402, F401
from mpmath import mp, mpf  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

try:
    from qou_substrate.constants import q_at, q_muon_at
except ImportError:
    print("ERROR: qou_substrate not importable", file=sys.stderr)
    sys.exit(1)

# Established empirical c_3 at each anchor (PR #1609 cross-anchor infra).
EMPIRICAL_C3_PROTON = mpf("-2.0693")
EMPIRICAL_C3_MUON = mpf("-2.0097")

# "Tracks" criteria — a genuine fibre element must (a) swing by a comparable
# magnitude to empirical c_3 (swing ratio within ~2× of 1.0) AND (b) land on
# empirical c_3 at the *second* anchor too. Both are deliberately loose: any
# real-q form fails them by orders of magnitude (see audit).
MAX_SWING_RATIO_DEVIATION = 1.0  # |swing_ratio − 1| < this  ⇒ "within ~2×"
MAX_ERR_PCT = 1.0                # |err at muon anchor| < this (%)


def quantum_int(n: int, q: mpf) -> mpf:
    return (q ** n - q ** (-n)) / (q - q ** (-1))


def c3_habiro_3rung(q: mpf) -> mpf:
    """3-rung [3]_q/25 closure (matches MmuR9V9Closure.qbetaC3Closure)."""
    hbar = (q - 1) / q
    base = -(q ** 2 + q ** (-2))
    rung1 = hbar * quantum_int(3, q) / 25
    rung2 = hbar ** 3 / quantum_int(2, q)
    return base * (1 + rung1 + rung2)


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()
    wb = WitnessBuilder("qbeta-c3-habiro-3rung-crossanchor-rigidity",
                        engine="mpmath", start_time=t0)

    q_p = mpf(str(q_at()))
    q_m = mpf(str(q_muon_at()))
    sep = abs(q_p - q_m)

    c3_p = c3_habiro_3rung(q_p)
    c3_m = c3_habiro_3rung(q_m)

    # Errors vs the anchor-specific empirical c_3.
    err_p_pct = float((c3_p - EMPIRICAL_C3_PROTON) / abs(EMPIRICAL_C3_PROTON) * 100)
    err_m_pct = float((c3_m - EMPIRICAL_C3_MUON) / abs(EMPIRICAL_C3_MUON) * 100)

    # Swings.
    formula_swing = c3_p - c3_m
    formula_swing_pct = float(formula_swing / abs(c3_p) * 100)
    empirical_swing = EMPIRICAL_C3_PROTON - EMPIRICAL_C3_MUON
    empirical_swing_pct = float(empirical_swing / abs(EMPIRICAL_C3_PROTON) * 100)
    swing_ratio = formula_swing_pct / empirical_swing_pct if empirical_swing_pct else float("inf")

    print("=" * 78)
    print(" c_3 [3]_q/25 3-rung — cross-anchor rigidity (falsification) test")
    print("=" * 78)
    print(f"  anchor separation |q_p - q_m| = {fmt(sep)[:22]}")
    print()
    print(f"  PROTON anchor  q = {fmt(q_p)[:24]}")
    print(f"    formula c_3    = {fmt(c3_p)[:22]}   empirical = {EMPIRICAL_C3_PROTON}")
    print(f"    err vs empir.  = {err_p_pct:+.4f}%")
    print()
    print(f"  MUON anchor    q = {fmt(q_m)[:24]}")
    print(f"    formula c_3    = {fmt(c3_m)[:22]}   empirical = {EMPIRICAL_C3_MUON}")
    print(f"    err vs empir.  = {err_m_pct:+.4f}%")
    print()
    print("─" * 78)
    print(f"  formula swing  = {fmt(formula_swing)[:22]} ({formula_swing_pct:+.6f}%)")
    print(f"  empirical swing= {fmt(empirical_swing)} ({empirical_swing_pct:+.4f}%)")
    print(f"  swing ratio (formula/empirical) = {swing_ratio:.3e}")
    print()
    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)

    # The formula TRACKS the empirical swing iff its swing is within ~2x of
    # empirical (i.e. it reproduces empirical c_3 at BOTH anchors).
    tracks = (abs(swing_ratio - 1.0) < MAX_SWING_RATIO_DEVIATION
              and abs(err_m_pct) < MAX_ERR_PCT)
    # Magnitude-only mismatch factor (how many × bigger the empirical swing is
    # than the formula swing); guard the formula-swing-rounds-to-0 case.
    if formula_swing_pct == 0.0:
        mismatch_factor = float("inf")
    else:
        mismatch_factor = abs(empirical_swing_pct / formula_swing_pct)
    if tracks:
        print("  ★ GENUINE FIBRE ELEMENT — formula tracks empirical c_3 at BOTH")
        print("  anchors. The [3]_q/25 closure has real cross-anchor rigidity.")
    else:
        print("  PROTON-ANCHOR NEAR-MATCH (as predicted). The real-q formula is")
        print(f"  RIGID (swing {formula_swing_pct:+.2e}%) while empirical c_3 swings")
        print(f"  {empirical_swing_pct:+.2f}% — a {mismatch_factor:.1e}× mismatch. At the muon")
        print(f"  anchor the formula misses empirical c_3 by {err_m_pct:+.2f}%.")
        print()
        print("  INTERPRETATION (consistent with AGENTS.md §Im(q) fibre-vs-observable):")
        print("  empirical c_3 has dc_3/dq ~ 4.6e6 near the anchor — NO smooth real-q")
        print("  formula can track that. So [3]_q/25 is NOT a real-q fibre element;")
        print("  the genuine Habiro element (if any) is complex-analytic / evaluated")
        print("  at roots of unity. This CONFIRMS the NEAR-MATCH tier and REDIRECTS")
        print("  the fibre-level Composite 4 search away from real-q forms.")

    wb.add_assertion(
        "c3_habiro_3rung_tracks_empirical_across_anchors",
        computed=tracks,
        expected=False,
        source="Whether the real-q 3-rung [3]_q/25 formula reproduces empirical "
               "c_3 at BOTH the proton and muon anchors (genuine fibre rigidity) "
               "vs. matching only at the proton anchor (near-match). Expected "
               "False — a smooth real-q form cannot track the ~4.6e6 dc_3/dq of "
               "the hyper-sensitive extracted c_3.",
    )

    wb.add_data("q_proton", fmt(q_p))
    wb.add_data("q_muon", fmt(q_m))
    wb.add_data("anchor_separation", fmt(sep))
    wb.add_data("c3_formula_proton", fmt(c3_p))
    wb.add_data("c3_formula_muon", fmt(c3_m))
    wb.add_data("c3_empirical_proton", str(EMPIRICAL_C3_PROTON))
    wb.add_data("c3_empirical_muon", str(EMPIRICAL_C3_MUON))
    wb.add_data("err_proton_pct", err_p_pct)
    wb.add_data("err_muon_pct", err_m_pct)
    wb.add_data("formula_swing_pct", formula_swing_pct)
    wb.add_data("empirical_swing_pct", empirical_swing_pct)
    wb.add_data("swing_ratio_formula_over_empirical", swing_ratio)
    wb.add_data("mismatch_factor_empirical_over_formula", mismatch_factor)
    wb.add_data("tracks_across_anchors", tracks)
    wb.add_data("interpretation", (
        f"The real-q 3-rung [3]_q/25 c_3 closure swings {formula_swing_pct:+.2e}% "
        f"across the two anchors while empirical c_3 swings {empirical_swing_pct:+.2f}% "
        f"(ratio {swing_ratio:.2e}). The formula is RIGID; it reproduces empirical "
        f"c_3 only at the proton anchor (miss {err_m_pct:+.2f}% at muon). This "
        "CONFIRMS [3]_q/25 is a proton-anchor NEAR-MATCH, not a real-q fibre "
        "element — consistent with the known impossibility of a real-q c_3=f(q) "
        "matching multiple anchors (AGENTS.md). The genuine Habiro element, if it "
        "exists, is complex-analytic / root-of-unity. Falsification test; no fit, "
        "no production change."
    ))

    out = wb.save()
    print()
    print(f"✓ Witness: {out.name}  ({len(wb.assertions)} assertions, "
          f"{'all passed' if all(a.passed for a in wb.assertions) else 'FAILURES'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
