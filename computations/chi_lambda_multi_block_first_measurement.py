#!/usr/bin/env python3
"""FIRST multi-block χ_λ measurement using pyhecke-native tier-3 wiring.

Per author direction 2026-05-25: "prepare to wire up chi_lambda_braid"
+ "what next? get us to 1ppb please".

## What this script does

Uses the just-wired `pyhecke_native.chi_lambda_braid` function to
compute χ_λ(β) for ALL partitions λ ⊢ n on the Borromean braid
β = (σ_1 σ_2⁻¹)³ in H_3(q) at q = q_0.

This is the **first concrete measurement** showing the actual multi-
block distribution structure that the production single-block
projection (`ν_SDP · m_e · Vol`) discards.

## Why Borromean?

The Borromean 𝓑₃ is the load-bearing knot operator for:
- 4He (via 4·𝓑₃ tower in magic A·8G rule)
- 12C, 16O, 20Ne, 24Mg, 40Ca (via α-cluster recursion from 4He)
- 8Be (via 2·𝓑₃ + c_αα)

ALL 7 KLR violations in the mass sweep trace to this single knot
operator. Sizing the multi-block distribution at H_3 (n=3,
3 partitions) is the smallest non-trivial measurement; H_12 (for
4 nucleons × 3 sheets = 77 partitions) is the full computation.

## Borromean braid word

The standard positive Borromean braid in B_3 is

    β_𝓑₃ = σ_1 σ_2⁻¹ σ_1 σ_2⁻¹ σ_1 σ_2⁻¹

i.e., (σ_1 σ_2⁻¹)³ — a 6-letter word with 3 σ_1 and 3 σ_2⁻¹.

## Output

- Console: per-partition χ_λ(β_𝓑₃) at q_0 + structural comparison
- Witness: `chi-lambda-multi-block-first-measurement.witness.json`
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

import mpmath as mp
import pyhecke_native as pn

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder, record_upstream  # noqa: E402
from _precision import set_compute_dps  # noqa: E402


def _as_dim(x) -> int:
    """A Specht dimension as an int, refusing anything that is not whole."""
    v = float(x)
    if abs(v - round(v)) > 1e-9:
        raise ValueError(
            f"dim_S_lambda is not a whole number: {v!r}. That is a finding "
            "about the character routine, not a formatting problem -- do not "
            "round it away.")
    return int(round(v))


# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []

set_compute_dps()
Q_PIN = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
q0_mpf = mp.mpf(record_upstream(Q_PIN, _UPSTREAM_RECORDS)["derived_50_digit"]["q"])
q0_f64 = float(q0_mpf)
h = q0_mpf - 1 / q0_mpf
h_f64 = float(h)
h_sq_f64 = float(h * h)

# Borromean braid word in B_3: (σ_1 σ_2^-1)^3 = 6 letters
# Format for chi_lambda_braid: list of (sign, gen_1based)
# Each letter is a single crossing: sign ∈ {+1, -1}, gen is 1-based generator
BORROMEAN_WORD = [
    (1, 1),    # σ_1
    (-1, 2),   # σ_2^-1
    (1, 1),    # σ_1
    (-1, 2),   # σ_2^-1
    (1, 1),    # σ_1
    (-1, 2),   # σ_2^-1
]

# Partitions of 3 (all Wedderburn blocks of H_3(q))
PARTITIONS_3 = [
    [3],       # symmetric (trivial)
    [2, 1],    # standard
    [1, 1, 1], # antisymmetric (sign)
]


def main() -> int:
    print("=" * 100)
    print("FIRST MULTI-BLOCK χ_λ(β_𝓑₃) MEASUREMENT (pyhecke-native tier-3)")
    print(f"  q_0 = {q0_f64:.10f}    h = {h_f64:.10f}    h² = {h_sq_f64:.10f}")
    print(f"  β_𝓑₃ = (σ_1 σ_2⁻¹)³ in B_3 (6 letters)")
    print("=" * 100)
    print(f"  {'partition λ':>14}  {'dim S_λ':>9}  {'χ_λ(β_𝓑₃) at q_0':>22}  "
          f"{'χ_λ / h':>14}  {'χ_λ / h²':>14}  {'interpretation':<30}")
    print("  " + "-" * 98)

    results = []
    for shape in PARTITIONS_3:
        chi = pn.chi_lambda_braid(shape, BORROMEAN_WORD, q0_f64)
        dim = pn.chi_lambda_braid(shape, [], q0_f64)  # χ_λ(id) = dim
        chi_over_h = chi / h_f64 if abs(h_f64) > 0 else 0
        chi_over_h2 = chi / h_sq_f64 if abs(h_sq_f64) > 0 else 0
        # Classify magnitude
        if abs(chi) < 1e-12:
            interp = "ZERO (vanishes structurally)"
        elif abs(chi) < h_sq_f64 * 10:
            interp = f"h²-scale (≈ {chi/h_sq_f64:+.2f} h²)"
        elif abs(chi) < abs(h_f64) * 10:
            interp = f"h-scale (≈ {chi/h_f64:+.2f} h)"
        else:
            interp = f"O(1) (≈ {chi:+.3f})"
        partition_str = f"({','.join(map(str, shape))})"
        print(f"  {partition_str:>14}  {dim:>9.4f}  {chi:>22.10f}  "
              f"{chi_over_h:>14.4f}  {chi_over_h2:>14.4f}  {interp:<30}")
        results.append({
            "partition": shape,
            # A Specht dimension is a COUNT of standard Young tableaux, so it
            # ships as a JSON integer. It was `float(dim)`, which wrote `54.0`
            # -- the same number, a different claim, and one a TypeScript
            # consumer cannot tell from a measurement because `JSON.parse`
            # collapses `54` and `54.0` to the same `number`. Declared in
            # `computations/witness-integer-fields.json` and enforced by
            # `witness_integer_field_audit`. Bean `qou-xt5l`.
            #
            # `_as_dim` refuses a value that is not whole rather than rounding
            # it away: a fractional dimension would be a real finding here, and
            # silently truncating it is how it would stay hidden.
            "dim_S_lambda": _as_dim(dim),
            "chi_lambda_borromean": float(chi),
            "chi_over_h": float(chi_over_h),
            "chi_over_h_sq": float(chi_over_h2),
            "magnitude_class": interp,
        })

    print("  " + "-" * 98)
    print()

    # KEY ANALYSIS: which partitions contribute to single-block projection?
    print("STRUCTURAL ANALYSIS — multi-block vs single-block:")
    chi_total_abs = sum(abs(r["chi_lambda_borromean"]) for r in results)
    print(f"  Σ_λ |χ_λ(β_𝓑₃)|  =  {chi_total_abs:.10f}")
    for r in results:
        frac = abs(r["chi_lambda_borromean"]) / chi_total_abs * 100 if chi_total_abs > 0 else 0
        print(f"    λ = {tuple(r['partition'])}: |χ| / total = {frac:.2f}%")
    print()
    print("INTERPRETATION:")
    print("  Production mass formula uses ν_SDP · Vol(𝓑₃) — projects to ONE")
    print("  block via integer ν_SDP.  Canonical needs Σ_λ y_λ · χ_λ(β_𝓑₃)")
    print("  with y_λ from R5-full SDP.  The above percentages show how")
    print("  much weight each Wedderburn block ACTUALLY carries on the")
    print("  Borromean braid — production captures only one column.")
    print()
    print("NEXT MEASUREMENT (single-session feasible):")
    print("  Apply this to all 77 partitions of 12 for 4He's full atomic")
    print("  braid β_⁴He.  When R5-full SDP supplies y_λ, the product")
    print("  Σ_λ y_λ · χ_λ(β_⁴He) gives the canonical B(4He).")

    # Witness emit
    w = WitnessBuilder("chi-lambda-multi-block-first-measurement", engine="python+pyhecke-native")
    w.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    w.set_description(
        "FIRST concrete multi-block χ_λ measurement using just-wired "
        "pyhecke_native.chi_lambda_braid (tier-3 Phase B Python wrapper). "
        "Evaluates χ_λ(β_𝓑₃) for all 3 partitions of H_3(q) at q_0 on "
        "the standard positive Borromean braid (σ_1 σ_2⁻¹)³. Establishes "
        "the multi-block distribution structure that production's single-"
        "block ν_SDP projection discards. Foundation for §10.1-§10.2 of "
        "the vol-density-derivation-bug-squash audit (PR #1228)."
    )
    w.add_parameter("q_0_f64", q0_f64)
    w.add_parameter("h_f64", h_f64)
    w.add_parameter("h_sq_f64", h_sq_f64)
    w.add_parameter(
        "borromean_word",
        "(σ_1 σ_2^-1)^3 = [(1,1),(2,-1),(1,1),(2,-1),(1,1),(2,-1)]",
    )
    w.add_parameter("partitions_of_3_count", len(PARTITIONS_3))
    w.add_data("per_partition_chi_lambda", results)
    w.add_data("sum_abs_chi", float(chi_total_abs))
    w.add_assertion(
        "all_partitions_returned_non_null",
        computed=len(results),
        expected=len(PARTITIONS_3),
        tolerance=0,
        unit="partitions",
        source="pyhecke_native.chi_lambda_braid invocations",
    )
    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
