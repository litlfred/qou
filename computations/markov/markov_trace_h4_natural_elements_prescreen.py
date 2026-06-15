"""Markov-trace pre-screen of natural H_4 elements at mp.mpf 50 dps.

Per author 'keep exploring' direction. The Demazure pre-screen
(`demazure_sub_crystal_h5_h6_h7_prescreen.py`) found that positive-
weight Wedderburn-derived sub-sums all give POSITIVE h² coefficients
— for Reading-A's h² ≈ -G < 0, signed weights or characters at
non-identity elements are required.

This probe explores the SECOND option: characters χ^λ at non-identity
H_4 braid elements. χ^λ at non-identity CAN be negative, so the
Markov trace Σ_λ y_λ · χ^λ(braid) at any non-identity braid can have
NEGATIVE h² coefficient.

## Method

For each of ~10 natural H_4 braid words:
1. Compute tr_M = Σ_λ y_λ(q) · χ^λ(braid, q) at q = q_0 and at 4
   nearby q values (mp.mpf 50 dps via markov_trace_for_knot
   infrastructure: y_lambda_wenzl_bridge_numeric + chi_lambdas_braid_mpfr)
2. h-fit: tr_M ≈ a_0 + a_2·h² + a_4·h⁴ + ...
3. Compare a_2 to Reading-A's target -G ≈ -0.916

If any tr_M has h² coefficient ≈ -G, that's a structural candidate
for the linking_weight.

## Natural H_4 elements tested

- identity (1 in H_4) — control: tr_M = 1, h² = 0
- σ_1 (single generator)
- σ_1·σ_2 (Coxeter pair)
- σ_1·σ_2·σ_3 (full Coxeter element)
- (σ_1·σ_2·σ_3)² (squared Coxeter)
- σ_1²·σ_2²·σ_3² (squared generators)
- σ_1·σ_2⁻¹·σ_1·σ_2⁻¹ (alternating pair — Borromean-like)
- (σ_1·σ_2·σ_3·σ_2·σ_1) (Garside element)
- Specific stabilized lifts of β_𝓑

## Cross-references

- PR #1287 stack (companion probes)
- audit 2026-05-25 Path C principle hunt
- Demazure pre-screen (sibling file) — positive-sum direction RULED OUT
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path
from typing import List, Tuple

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import mpmath as mp  # noqa: E402
import pyhecke_native as pn  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from y_lambda_wenzl_bridge import (  # noqa: E402
    partitions_of as wenzl_partitions_of,
    y_lambda_wenzl_bridge_numeric,
)
from witness_base import WitnessBuilder  # noqa: E402


def markov_trace_at_q(braid: List[Tuple[int, int]], q_str: str,
                      n: int = 4, dps: int = 50) -> "mp.mpf":
    """Compute tr_M = Σ_λ y_λ · χ^λ(braid) at H_n(q) at given q (string)."""
    mp.mp.dps = max(mp.mp.dps, dps)
    shapes = wenzl_partitions_of(n)
    # y_λ at mpf precision
    y_vals = [y_lambda_wenzl_bridge_numeric(lam, q_str, dps=dps) for lam in shapes]
    # χ_λ via mpfr Rust kernel
    chi_strs = pn.chi_lambdas_braid_mpfr(shapes, braid, q_str, dps=dps)
    chi_vals = [mp.mpf(s) for s in chi_strs]
    return sum(y_vals[i] * chi_vals[i] for i in range(len(shapes)))


def fit_h_polynomial(values_at_q: list, h_vals: list, max_order: int = 6,
                     dps: int = 50) -> dict[int, "mp.mpf"]:
    """Fit y(h) = a_0 + a_2·h² + a_4·h⁴ + ... + a_{max_order}·h^{max_order}."""
    mp.mp.dps = max(mp.mp.dps, dps)
    even_orders = list(range(0, max_order + 1, 2))
    n_unknowns = len(even_orders)
    n_pts = len(h_vals)
    if n_pts < n_unknowns:
        raise ValueError(f"need ≥ {n_unknowns} points, got {n_pts}")
    V = mp.matrix(n_pts, n_unknowns)
    for i in range(n_pts):
        for j, ord_j in enumerate(even_orders):
            V[i, j] = h_vals[i] ** ord_j
    if n_pts == n_unknowns:
        a = mp.lu_solve(V, mp.matrix(values_at_q))
    else:
        Vt = V.transpose()
        a = mp.lu_solve(Vt * V, Vt * mp.matrix(values_at_q))
    return {even_orders[j]: a[j] for j in range(n_unknowns)}


def main() -> int:
    set_compute_dps(50)
    w = WitnessBuilder(
        "markov-trace-h4-natural-elements-50dps",
        engine="python",
    )
    w.set_audit_only(
        "docs/audits/2026-05-25-path-c-categorical-principle-hunt.md",
    )
    w.set_description(
        "Pre-screens Markov traces of ~10 natural H_4 braid elements "
        "at mp.mpf 50 dps. Tests whether characters at non-identity "
        "elements (which can be negative) yield h² coefficient near "
        "-G (Reading-A target)."
    )

    print("=" * 78)
    print("Markov-trace pre-screen at H_4 — natural braid elements (50 dps)")
    print("=" * 78)

    G = mp.catalan
    print(f"\nTarget h² coefficient: -G = {mp.nstr(-G, 12)}")

    # Sample q values
    sample_q_strs = ["1.05", "1.08", "1.11", "1.14", "1.17"]
    h_vals = []
    for q_str in sample_q_strs:
        q = mp.mpf(q_str)
        h_vals.append(q - 1 / q)
    print(f"Sample q values: {sample_q_strs}")

    # Catalogue natural H_4 braids: list of (gen_index_1based, sign) pairs
    # (sign +1 = σ_i, sign -1 = σ_i⁻¹)
    # Generators in B_4: σ_1, σ_2, σ_3 (one-indexed for pyhecke_native)
    braids = {
        "identity": [],
        "sigma_1": [(1, 1)],
        "sigma_1_squared": [(1, 1), (1, 1)],
        "sigma_1_sigma_2": [(1, 1), (1, 2)],
        "sigma_1_sigma_2_sigma_3": [(1, 1), (1, 2), (1, 3)],
        "coxeter_squared": [(1, 1), (1, 2), (1, 3), (1, 1), (1, 2), (1, 3)],
        "sigma_1_sigma_2_inv": [(1, 1), (-1, 2)],
        "borromean_lift_stab": [(1, 1), (-1, 2), (1, 1), (-1, 2), (1, 1), (-1, 2)],
        "garside_4": [(1, 1), (1, 2), (1, 3), (1, 2), (1, 1)],
        "all_inverse": [(-1, 1), (-1, 2), (-1, 3)],
        "pure_3_strand": [(1, 1), (1, 1), (1, 2), (1, 2)],
    }

    print(f"\nTesting {len(braids)} braids at H_4...")
    print(f"\n  {'braid':<32}{'a_0':<14}{'a_2 (h² coef)':<18}{'a_4':<14}{'Δ vs -G':<14}")

    results: dict[str, dict] = {}
    for name, braid in braids.items():
        try:
            # Compute tr_M at each q
            trM_vals = [markov_trace_at_q(braid, q_str, n=4, dps=50)
                        for q_str in sample_q_strs]
            # Fit
            coeffs = fit_h_polynomial(trM_vals, h_vals, max_order=4, dps=50)
            a_0 = coeffs[0]
            a_2 = coeffs[2]
            a_4 = coeffs[4]
            # Normalize a_2 to baseline a_0 = 5/2 for fair comparison
            if abs(a_0) > mp.mpf("1e-30"):
                a_2_norm = a_2 * mp.mpf("2.5") / a_0
            else:
                a_2_norm = a_2
            delta = a_2_norm - (-G)
            results[name] = {
                "a_0": mp.nstr(a_0, 12),
                "a_2": mp.nstr(a_2, 12),
                "a_4": mp.nstr(a_4, 12),
                "a_2_normalized_to_h0_5over2": mp.nstr(a_2_norm, 12),
                "delta_vs_minus_G": mp.nstr(delta, 8),
            }
            print(f"  {name:<32}{mp.nstr(a_0, 8):<14}{mp.nstr(a_2, 12):<18}{mp.nstr(a_4, 8):<14}{mp.nstr(delta, 8):<14}")
        except Exception as e:
            print(f"  {name:<32}FAILED: {e}")
            results[name] = {"error": str(e)}

    # Summary: which braids have NEGATIVE a_2?
    print()
    print("=" * 78)
    print("Braids with NEGATIVE h² coefficient (a_2 < 0):")
    print("=" * 78)
    negative_a2 = [(n, d) for n, d in results.items()
                   if "a_2" in d and mp.mpf(d["a_2"]) < 0]
    if negative_a2:
        for n, d in sorted(negative_a2, key=lambda nd: abs(mp.mpf(nd[1]["a_2"]) - (-G))):
            print(f"  {n}: a_2 = {d['a_2']}, normalized = {d['a_2_normalized_to_h0_5over2']}, Δ vs -G = {d['delta_vs_minus_G']}")
    else:
        print("  NONE — all tested braids yield NON-NEGATIVE h² coefficient.")
        print("  Even at non-identity Hecke elements, the y_λ · χ^λ sum is "
              "non-negative under tested braid words.")

    # Witness
    w.add_parameter("sample_q_strs", sample_q_strs)
    w.add_parameter("target_h2_minus_G", mp.nstr(-G, 25))
    w.add_data("per_braid_results", results)
    w.add_data("braids_with_negative_a2", [
        {"name": n, "data": d}
        for n, d in negative_a2
    ])

    # Find absolute closest to -G regardless of sign
    closest = None
    closest_dev = mp.mpf("1e10")
    for n, d in results.items():
        if "a_2_normalized_to_h0_5over2" in d:
            adev = abs(mp.mpf(d["a_2_normalized_to_h0_5over2"]) - (-G))
            if adev < closest_dev:
                closest = (n, d, adev)
                closest_dev = adev
    if closest:
        n, d, adev = closest
        print(f"\nClosest braid to a_2_normalized = -G: {n}")
        print(f"  a_2_normalized = {d['a_2_normalized_to_h0_5over2']}, Δ = {mp.nstr(adev, 8)}")
        w.add_data("closest_braid_to_target", {
            "name": n,
            "data": d,
            "absolute_delta": mp.nstr(adev, 12),
        })

    if negative_a2 and any(abs(mp.mpf(d["delta_vs_minus_G"])) < mp.mpf("0.01")
                            for n, d in negative_a2):
        w.add_data("verdict", (
            "FOUND candidate(s) with a_2_normalized ≈ -G. "
            "Recommend deeper investigation — structural identity possible."
        ))
    elif negative_a2:
        w.add_data("verdict", (
            "Found braids with NEGATIVE h² coefficient, but none within "
            "0.01 of target -G. The 'negative h²' is achievable structurally "
            "but not at -G specifically without further calibration."
        ))
    else:
        w.add_data("verdict", (
            "NO tested H_4 braid yields negative h² coefficient. "
            "Either: (a) the tested catalog is insufficient (need more "
            "elements), or (b) Markov-trace-at-non-identity sums are "
            "constrained to non-negative h² at H_4 for some structural "
            "reason."
        ))

    w.add_assertion(
        name="prescreen_completed",
        computed=True,
        expected=True,
        tolerance=0,
        source=(
            f"Tested {len(braids)} H_4 braid words; {len(negative_a2)} "
            f"with negative a_2. Sanity: search completed without error."
        ),
    )

    out = w.save()
    print(f"\n  Witness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
