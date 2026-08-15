#!/usr/bin/env python3
"""
Probe (1b): test the PSD-dominance vs trace-dominance ORTHOGONALITY
at A=6.

At A=4 (Probe 1), the PSD-dominant pair (4,4,4)/(3,3,3,3) contributed
only 0.030% / 0.0002% of |tr_M|. The trace was dominated by 2-row
partitions ([9,3], [8,4], [10,2], [11,1], [7,5]).

At A=6, Probe (4c) shifted the PSD-dominant to (3,3,3,3,2,2,2) with
min_eig = -116.71. Does the orthogonality still hold?

This probe compares y_λ magnitudes between the PSD-dominant family
and the trace-dominant family at n=18. y_λ values come from the
LIVE closed form `y_lambda_at_q0_mpmath(18, Q)`; the cached
witness covers n = 2..12 only, so the old read raised KeyError: '18'.

Conclusion under convention D: orthogonality is EXACT. Every
PSD-dominant shape here has 3+ rows, so Schur-Weyl on the two-
dimensional fibre sends its y_λ to exactly 0 — the family
contributes identically zero, not a small residue. Under
convention C this read as a 9-order-of-magnitude gap
(y_λ ~ 10^-15 vs 10^-6); the separation is now total.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_base import WitnessBuilder
from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402


def main():
    base = Path(__file__).resolve().parent
    # y_λ at n=18 from the LIVE closed form, not the cached witness.
    #
    # This read `y-lambda-at-q0.witness.json` -> `data.by_n["18"]`, and that
    # cache covers n = 2..12 only — so the probe raised
    # `KeyError: '18'` and could not run at all. Its committed witness dates
    # from an earlier cache era, which is why it still carried convention-C
    # values (nonzero y_λ on 3+ row partitions) long after the migration:
    # the staleness was in the DATA, not in this producer's code, so no
    # amount of re-running would have fixed it while the read stayed here.
    #
    # `y_lambda_at_q0_mpmath` is the experimental-anchor path per AGENTS.md
    # §"q₀ anchor convention": `wedderburn_jones_markov.y_lambda_at` serves
    # the MUON-built cache whenever `|q - q_parameter.Q| < 1e-12`, a gate
    # satisfied trivially by passing `Q` itself. At n=18 that cache has no
    # entry so both routes compute live and agree to ~1e-16, but the direct
    # call is the one that stays correct if n=18 is ever cached.
    # Kept as mpmath.mpf, NOT float()-ed. The live closed form returns ~50
    # significant digits and a `float()` here would throw them away at the
    # point of entry, which is exactly what the raw-float64 gate objects to:
    # the witness would record 28 double-precision fields sourced from an
    # arbitrary-precision computation.
    from schur_principal_mpmath import y_lambda_at_q0_mpmath
    import q_parameter as _qp
    ydict = {tuple(k): v for k, v in y_lambda_at_q0_mpmath(18, _qp.Q).items()}

    # Trace-dominant family: top-10 by |y_λ|
    sorted_y = sorted(ydict.items(), key=lambda x: -abs(x[1]))
    trace_dominant = sorted_y[:10]

    # PSD-dominant family: scanned shapes with deepest min_eig
    # (from probe-4c and probe-4 witnesses)
    # mpf from the decimal STRING, not a float literal: these are quoted to
    # 2 dp from the probe-4c / probe-4 witnesses, and `mpf("-116.71")` is the
    # exact decimal as written whereas `-116.71` is its float64 shadow. Seven
    # raw-float64 fields were entering the witness this way.
    import mpmath as _mp
    psd_data = {
        (3, 3, 3, 3, 2, 2, 2): _mp.mpf("-116.71"),
        (5, 5, 5, 3): _mp.mpf("-110.31"),
        (4, 4, 4, 3, 3): _mp.mpf("-109.81"),
        (3, 3, 3, 3, 3, 3): _mp.mpf("-96.52"),
        (6, 6, 6): _mp.mpf("-95.72"),
        (8, 8, 2): _mp.mpf("-88.95"),
        (10, 4, 4): _mp.mpf("-80.67"),
    }
    psd_sorted = sorted(psd_data.items(), key=lambda x: x[1])

    print("=== TRACE-dominant family at n=18 (top-10 |y_λ|) ===")
    print(f"{'partition':>30s}  {'y_λ':>15s}  rows  shape kind")
    for shape, y_val in trace_dominant:
        rows = len(shape)
        kind = "2-row long-string" if rows == 2 else f"{rows}-row"
        print(f"{str(list(shape)):>30s}  {float(y_val):+13.4e}  {rows:>4d}  {kind}")

    print()
    print("=== PSD-dominant family at n=18 (deepest min_eig) ===")
    print(f"{'partition':>30s}  {'min_eig':>10s}  {'y_λ':>15s}  rows  cols  shape kind")
    for shape, m in psd_sorted:
        y_val = ydict.get(shape)
        rows = len(shape)
        cols = max(shape)
        kind = "rect" if len(set(shape)) == 1 else "multi-step"
        print(f"{str(list(shape)):>30s}  {float(m):>+10.4f}  "
              f"{float(y_val):+13.4e}  {rows:>4d}  {cols:>4d}  {kind}")

    # Magnitude separation
    max_trace_y = max(abs(y) for _, y in trace_dominant)
    deepest_shape = psd_sorted[0][0]
    deepest_y = abs(ydict[deepest_shape])
    ratio = max_trace_y / deepest_y if deepest_y > 0 else float("inf")
    print()
    print(f"=== Orthogonality magnitude separation ===")
    print(f"  Top trace |y_λ|     = {float(max_trace_y):.4e}   at λ = {list(trace_dominant[0][0])}")
    print(f"  Deepest PSD |y_λ|   = {float(deepest_y):.4e}   at λ = {list(deepest_shape)}")
    # Under convention D the PSD-dominant family is 3+ row, so every y_λ in
    # it is EXACTLY zero and the separation is total rather than large. The
    # ratio is then infinite, and `log10(inf)` raised OverflowError here —
    # the arithmetic assumed convention C, where the deepest PSD weight was
    # a small nonzero number (~1e-15) and the separation was 9 orders.
    # Report the exact case as exact instead of forcing it into a magnitude.
    if deepest_y == 0.0:
        print("  Magnitude ratio     = EXACT SEPARATION "
              "(PSD-dominant y_λ identically 0 under convention D)")
    else:
        print(f"  Magnitude ratio     = {float(ratio):.4e}  "
              f"(≈ 10^{int(round(math.log10(ratio)))})")

    out = WitnessBuilder("probe-1b-li6-orthogonality", engine="python")
    out.set_description(
        "Tests PSD-dominance vs trace-dominance orthogonality at A=6. "
        "Mirrors Probe (1) at A=4, which under convention C found "
        "PSD-dominant blocks contributing <0.03% of |tr_M|. "
        "UNDER CONVENTION D THE RESULT SHARPENS TO AN EXACT ONE: every "
        "PSD-dominant shape here has 3 or more rows, and Schur-Weyl on the "
        "two-dimensional fibre sends y_lambda to exactly 0 for ell(lambda) "
        ">= 3. So the PSD-dominant family contributes IDENTICALLY ZERO, not "
        "a small residue, and the separation from the trace-dominant family "
        "(1- and 2-row, y ~ 1e-4) is total rather than 9 orders of "
        "magnitude. The orthogonality claim survives the convention change "
        "and strengthens; it does not dissolve."
    )
    out.set_audit_only(
        "docs/audits/2026-05-25-dominant-partition-nucleon-structure.md"
    )
    out.set_content_block("conj:atom-braid-exterior-algebra")

    out.add_data("trace_dominant_top10", [
        {"partition": list(s), "y_lambda": y, "n_rows": len(s)}
        for s, y in trace_dominant
    ])
    out.add_data("psd_dominant_scanned", [
        {"partition": list(s), "min_eig": m, "y_lambda": ydict.get(s),
         "n_rows": len(s), "max_row": max(s), "n_distinct_parts": len(set(s))}
        for s, m in psd_sorted
    ])
    # `ratio` is +Infinity under convention D (deepest_psd is exactly 0), and
    # JSON has no Infinity/NaN token — writing it produces a file that will
    # not parse under a strict loader. Record null and say why in a sibling
    # field rather than stringifying the token and moving on.
    _exact = (deepest_y == 0.0)
    out.add_data("magnitude_separation", {
        "top_trace_abs_y": max_trace_y,
        "deepest_psd_abs_y": deepest_y,
        "ratio_trace_over_psd": None if _exact else ratio,
        "log10_ratio": None if _exact else math.log10(ratio),
        "separation_kind": "exact" if _exact else "finite_ratio",
        "separation_note": (
            "PSD-dominant y_lambda is identically 0 under convention D "
            "(every scanned PSD shape has ell(lambda) >= 3, and Schur-Weyl "
            "on the two-dimensional fibre sends those to exact zero), so "
            "the ratio is infinite and is recorded as null. Under "
            "convention C it was a finite ~1e9."
            if _exact else "finite ratio; PSD-dominant weight is nonzero"
        ),
    })

    out.add_assertion(
        name="orthogonality_holds_at_a6_with_8plus_order_separation",
        computed=str(int(_exact or ratio >= 1e8)),
        expected="1",
        tolerance=0,
        source=(
            "PSD-dominant y_lambda identically 0 under convention D — "
            "exact separation, which subsumes the >=1e8 threshold"
            if _exact
            else f"max trace |y_λ| / deepest PSD |y_λ| = {float(ratio):.4e}"
        ),
    )

    out.add_caveat(
        "SUPERSEDED UNDER CONVENTION D. This caveat previously read: "
        "'Magnitude separation is a NECESSARY but not sufficient condition "
        "for the orthogonality ... rigorous closure needs the tr_M "
        "computation', because a 9-OOM gap between a small y_lambda and a "
        "large chi^lambda leaves room for a nonzero product. That argument "
        "was correct under convention C and does not apply here: the "
        "PSD-dominant y_lambda are now EXACTLY 0, so their contribution "
        "y_lambda * chi^lambda to tr_M is exactly 0 for any finite "
        "chi^lambda. No Hutchinson estimator or diagonal trace is needed "
        "to close it — the vanishing is structural (Schur-Weyl on the "
        "two-dimensional fibre kills ell(lambda) >= 3), not numerical. "
        "What this probe still does NOT establish is anything about the "
        "1- and 2-row trace-dominant family, whose weights are nonzero and "
        "whose chi^lambda are not computed here."
    )

    out.add_data("lean_uniqueness_ref", lean_uniqueness_ref("⁶Li"))

    out_path = out.save()
    print(f"\nWitness: {out_path}")


if __name__ == "__main__":
    main()
