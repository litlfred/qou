#!/usr/bin/env python3
"""option_e_v9_bar_symmetric_test_probe.py — does the v9 (1+q)/2
correction survive bar-symmetric replacement?

CONTEXT. Option-E v9 closed mirror-pair B_T − B_³He to 0.11% via:

    B_T − B_³He = m_π · ℏ_q · (1+q)/2 · Σ_λ y_λ · (χ^λ(β_T) + χ^{λᵀ}(β_³He))/2

Per PR #1643 (`prop:li2q-phiq-bar-symmetrization` + my paper audit):
binding-context formulas (Q_β, Δ_λ, mirror-pair binding differences)
should be **bar-symmetric** under q ↔ q⁻¹.

But (1+q)/2 is BAR-ASYMMETRIC:
    bar((1+q)/2) = (1+q⁻¹)/2 = (q+1)/(2q) ≠ (1+q)/2

This is a discipline violation per the framework's bar-symmetrization
prop. This probe replaces (1+q)/2 with bar-symmetric candidates and
reports whether the 0.11% closure survives.

CANDIDATES TESTED (in code order):
  C1: (1+q)/2          — original v9 (bar-asymmetric, baseline)
  C2: (2 + [2]_q)/4    — bar-symmetric average: ((1+q) + (1+q⁻¹))/4
  C3: √((2+[2]_q)/4)   — bar-modulus: √((1+q)/2 · (1+q⁻¹)/2)
  C4: [2]_{q^(1/2)}/2  — bar-symmetric, half-q
  C5: (2 + [2]_q)/2    — bar-symmetric, 2× C2
  C6: [2]_{q^(1/2)}    — bar-symmetric, 2× C4

VERDICTS:
  - If a bar-symmetric form matches the 0.11% closure: v9 was secretly
    bar-symmetric (correctly rewritten); discipline-aligned.
  - If NO bar-symmetric form matches: v9 (1+q)/2 was a bar-asymmetric
    near-match — confirms it's NOT a structural derivation. The 0.11%
    closure was anchor-coincidental.

DISCIPLINE: this probe is DIAGNOSTIC. Per CLAUDE.md, do NOT use the
result to WIRE a new factor; report the verdict honestly.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

try:
    from qou_substrate.constants import q_at
except ImportError:
    print("ERROR: qou_substrate not available", file=sys.stderr)
    sys.exit(1)


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()

    builder = WitnessBuilder(
        "option-e-v9-bar-symmetric-test-probe",
        engine="python+mpmath", start_time=t0,
    )
    builder.set_description(
        "Tests bar-symmetric replacements of v9's (1+q)/2 factor against "
        "the 0.11% empirical mirror-pair closure. Discipline-driven probe "
        "per PR #1643's bar-symmetrization audit."
    )
    builder.set_audit_only(
        "docs/audits/2026-06-01-bar-symmetric-discipline-tests.md"
    )

    q = q_at()
    q_inv = 1 / q
    h = q - q_inv

    # Bar-symmetry test of (1+q)/2
    original = (1 + q) / 2
    bar_original = (1 + q_inv) / 2
    bar_asymmetric_diff = original - bar_original
    is_bar_symmetric = abs(bar_asymmetric_diff) < mp.mpf("1e-40")

    print("=" * 78)
    print(" Option-E v9 (1+q)/2 — bar-symmetric replacement test")
    print("=" * 78)
    print()
    print(f"q_proton = {fmt(q)}")
    print(f"q⁻¹      = {fmt(q_inv)}")
    print()
    print(f"Original v9 factor: (1+q)/2 = {fmt(original)}")
    print(f"bar((1+q)/2) = (1+q⁻¹)/2 = {fmt(bar_original)}")
    print(f"diff = {fmt(bar_asymmetric_diff)}")
    print(f"bar-symmetric? {is_bar_symmetric}")
    print()

    # v8_base is the v9-PRIOR framework prediction (before (1+q)/2),
    # an upstream PROBE INPUT — not a CODATA constant; carried over from
    # the Option-E master ledger v8 row (PR #1594).
    # The target B_T - B_³He = 8.4817983 - 7.7180428 = 0.7637555 MeV
    # is derived from AME 2020 isotope binding values (³H, ³He).
    # (AME isotope bindings are not yet centralized in
    # experimental_constants.py; if/when added, swap these literals.)
    v8_base_MeV = mp.mpf("0.7232")  # PROBE INPUT from v8 audit
    B_T_AME_MeV = mp.mpf("8.4817983")    # AME 2020 ³H binding
    B_He3_AME_MeV = mp.mpf("7.7180428")  # AME 2020 ³He binding
    target_MeV = B_T_AME_MeV - B_He3_AME_MeV
    required_factor = target_MeV / v8_base_MeV

    print(f"v8_base = {fmt(v8_base_MeV)} MeV")
    print(f"target  = {fmt(target_MeV)} MeV")
    print(f"required correction factor = {fmt(required_factor)}")
    print()

    # Candidates
    two_q = q + q_inv  # [2]_q
    sqrt_q = mp.sqrt(q)
    two_q_half = sqrt_q + 1 / sqrt_q  # [2]_{q^(1/2)}

    candidates = [
        ("C1: (1+q)/2 [BAR-ASYMMETRIC — v9 original]", original),
        ("C2: (2 + [2]_q)/4 [bar-symmetric avg]", (2 + two_q) / 4),
        ("C3: √((2+[2]_q)/4) [bar-modulus]", mp.sqrt((2 + two_q) / 4)),
        ("C4: [2]_{q^(1/2)}/2 [bar-symmetric, half-q]", two_q_half / 2),
        ("C5: (2 + [2]_q)/2 [bar-symmetric, 2× C2]", (2 + two_q) / 2),
        ("C6: [2]_{q^(1/2)} [bar-symmetric]", two_q_half),
    ]

    print(f"{'Candidate':<55} {'Value':<25} {'Err vs target':>15}")
    print("-" * 100)
    results = []
    for name, val in candidates:
        err_pct = float((val - required_factor) / required_factor * 100)
        print(f"  {name:<53} {fmt(val)[:24]:<25} {err_pct:+15.4f}%")
        results.append({
            "name": name,
            "value": fmt(val),
            "value_at_q_proton": float(val),
            "err_vs_required_factor_pct": err_pct,
            "predicted_B_diff_MeV": float(v8_base_MeV * val),
            "err_vs_target_pct": float(
                (v8_base_MeV * val - target_MeV) / target_MeV * 100
            ),
        })

    print()

    # VERDICT
    bar_sym_candidates = [r for i, r in enumerate(results) if i > 0]
    best_bar_sym = min(bar_sym_candidates, key=lambda r: abs(r["err_vs_target_pct"]))
    original_err = results[0]["err_vs_target_pct"]
    best_bar_sym_err = best_bar_sym["err_vs_target_pct"]

    print("=" * 78)
    print(" VERDICTS")
    print("=" * 78)
    print()
    if abs(best_bar_sym_err) < 0.5:
        verdict = (
            f"BAR-SYMMETRIC CANDIDATE MATCHES — best is "
            f"{best_bar_sym['name']} with err {best_bar_sym_err:+.4f}%. "
            f"v9 (1+q)/2 was secretly bar-symmetric (a rewriting of the "
            f"true form); discipline-aligned."
        )
    elif abs(best_bar_sym_err) < 5:
        verdict = (
            f"BAR-SYMMETRIC CANDIDATES NEAR-MATCH — best is "
            f"{best_bar_sym['name']} with err {best_bar_sym_err:+.2f}% "
            f"(v9 original was {original_err:+.4f}%). Discipline-aligned "
            f"version exists but differs by ~5% — suggests v9 was a "
            f"bar-ASYMMETRIC near-match that doesn't survive symmetrization."
        )
    else:
        verdict = (
            f"BAR-SYMMETRIC REPLACEMENT FAILS — best candidate is "
            f"{best_bar_sym['name']} at err {best_bar_sym_err:+.2f}% vs "
            f"v9 original at {original_err:+.4f}%. The (1+q)/2 v9 form "
            f"is INHERENTLY bar-asymmetric near-match — NOT a structural "
            f"derivation. The 0.11% closure was anchor-coincidental, "
            f"violating the bar-discipline of prop:li2q-phiq-bar-symmetrization."
        )

    print(verdict)
    print()

    builder.add_data("q_proton", str(q))
    builder.add_data("v8_base_MeV", str(v8_base_MeV))
    builder.add_data("empirical_target_MeV", str(target_MeV))
    builder.add_data("required_correction_factor", str(required_factor))
    builder.add_data("original_v9_factor", str(original))
    builder.add_data("original_is_bar_symmetric", is_bar_symmetric)
    builder.add_data("candidates", results)
    builder.add_data("best_bar_symmetric", best_bar_sym)
    builder.add_data("verdict", verdict)

    builder.add_assertion(
        name="v9_original_factor_is_bar_asymmetric",
        computed=not is_bar_symmetric,
        expected=True,
        tolerance=0.0,
        source="(1+q)/2 - (1+q⁻¹)/2 ≠ 0 at q_proton",
    )

    out = builder.save()
    print(f"✓ Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
