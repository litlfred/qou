#!/usr/bin/env python3
"""
Phase 3: per-partition h-expansion for deuteron (H₆) and tritium (H₉).

Extends Phase 1a methodology to A=2 (D) and A=3 (T, ³He) isotopes.
For each, evaluates y_λ·χ^λ(T_w_atom) at multiple q values and
extracts h-series coefficients via Vandermonde solve.

The deuteron (H₆, p(6)=11 partitions) and tritium (H₉, p(9)=30
partitions) are small enough to evaluate ALL partitions (not just
trace-dominant 2-row), giving the COMPLETE h² budget.

Cross-isotope comparison: does the h²=0 cancellation (proved for
proton at H₃) also hold at H₆ and H₉?
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 3, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
import time
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from hecke_characters import (  # noqa: E402
    standard_young_tableaux,
    build_seminormal_matrices,
    partitions_of,
)
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A, chi_lambda_of_word  # noqa: E402
from partition_utils import hook_lengths_with_cells  # noqa: E402


def dim_syt(shape):
    from math import factorial, prod
    n = sum(shape)
    cells = hook_lengths_with_cells(list(shape))
    return factorial(n) // prod(hk for (_, _, hk) in cells)


def yl_chi_for_atom(shape, Z, N, q_val, dps=60):
    """Compute y_λ·χ^λ(T_w_atom) at specific q for atom (Z,N)."""
    mp.mp.dps = dps
    q_f = float(q_val)

    y_val = y_lambda_wenzl_bridge_numeric(list(shape), q_val, dps=dps)

    sigmas, dim, syts = build_seminormal_matrices(shape, q=q_f)
    if dim == 0:
        return mp.mpf(0), mp.mpf(0), mp.mpf(0)

    n = sum(shape)
    word = atom_braid_word_3A(Z, N)
    chi_val = chi_lambda_of_word(sigmas, dim, word, n - 1)

    return mp.mpf(y_val) * mp.mpf(chi_val), mp.mpf(y_val), mp.mpf(chi_val)


def h_expand_atom(Z, N, atom_name, q_points, h_points, n_terms=5, dps=60):
    """Per-partition h-expansion for atom (Z,N) at H_{3(Z+N)}."""
    A = Z + N
    n = 3 * A
    parts = list(partitions_of(n))

    print(f"\n  {atom_name} (Z={Z}, N={N}, A={A}, n={n}, p({n})={len(parts)} partitions)")

    all_results = []
    h2_total = mp.mpf(0)

    for shape_list in parts:
        shape = tuple(shape_list)
        d = dim_syt(shape)

        if d > 500:
            all_results.append({
                "partition": list(shape), "d_lambda": d,
                "status": "skipped_too_large",
            })
            continue

        f_vals = []
        y0 = chi0 = None
        for qi_idx, qi in enumerate(q_points[:n_terms]):
            prod_val, y_val, chi_val = yl_chi_for_atom(shape, Z, N, qi, dps=dps)
            f_vals.append(prod_val)
            if qi_idx == 0:
                y0, chi0 = y_val, chi_val

        mp.mp.dps = dps
        V = mp.matrix(n_terms, n_terms)
        for i in range(n_terms):
            for k in range(n_terms):
                V[i, k] = h_points[i] ** k
        rhs = mp.matrix(n_terms, 1)
        for i in range(n_terms):
            rhs[i] = f_vals[i]

        try:
            coeffs = mp.lu_solve(V, rhs)
            c2 = coeffs[2]
            h2_total += c2

            all_results.append({
                "partition": list(shape),
                "d_lambda": d,
                "y_at_q0": str(mp.nstr(y0, 15)),
                "chi_at_q0": str(mp.nstr(chi0, 12)),
                "product_at_q0": str(mp.nstr(f_vals[0], 15)),
                "h2_coefficient": str(mp.nstr(c2, 15)),
            })
        except Exception:
            all_results.append({
                "partition": list(shape), "d_lambda": d,
                "status": "solve_failed",
            })

    # Sort by |product| at q₀
    evaluated = [r for r in all_results if "product_at_q0" in r]
    evaluated.sort(key=lambda r: -abs(mp.mpf(r["product_at_q0"])))

    # Print top contributors
    print(f"    Top 5 trace-dominant partitions:")
    tr_total = sum(abs(mp.mpf(r["product_at_q0"])) for r in evaluated)
    for rank, r in enumerate(evaluated[:5], 1):
        pct = abs(mp.mpf(r["product_at_q0"])) / tr_total * 100 if tr_total > 0 else 0
        print(f"      {rank}. {str(r['partition']):>20s}  d={r['d_lambda']:>4d}  "
              f"|y·χ|={mp.nstr(abs(mp.mpf(r['product_at_q0'])), 8):>12s}  "
              f"h²={mp.nstr(mp.mpf(r['h2_coefficient']), 8):>12s}  "
              f"({mp.nstr(mp.mpf(str(pct)), 4)}%)")

    print(f"\n    h² TOTAL (all partitions): {mp.nstr(h2_total, 15)}")
    is_zero = abs(h2_total) < 1e-6
    print(f"    h² = 0 cancellation: {'YES ✓' if is_zero else 'NO — non-zero h²'}")

    return all_results, h2_total


def main():
    set_compute_dps()
    w = WitnessBuilder("phase3-deuteron-tritium-h-expansion", engine="mpmath")
    t0 = time.time()
    print("=" * 70)
    print("  Phase 3: deuteron + tritium per-partition h-expansion")
    print("=" * 70)

    q0 = Q_MP
    offsets = [0, 0.005, -0.005, 0.012, -0.012, 0.025, -0.025]
    q_points = [q0 + mp.mpf(str(off)) for off in offsets]
    h_points = [qi - 1/qi for qi in q_points]
    n_terms = 5

    atoms = [
        (1, 1, "Deuteron (D)"),
        (1, 2, "Tritium (T)"),
        (2, 1, "Helium-3 (³He)"),
    ]

    all_atom_results = {}
    h2_totals = {}

    for Z, N, name in atoms:
        t1 = time.time()
        results, h2_total = h_expand_atom(Z, N, name, q_points, h_points, n_terms)
        wall = time.time() - t1
        print(f"    Wall time: {wall:.1f}s")
        all_atom_results[name] = results
        h2_totals[name] = h2_total

    # Cross-isotope h² comparison
    print("\n" + "=" * 70)
    print("  Cross-isotope h² cancellation test")
    print("=" * 70)
    print(f"\n  {'Atom':>15s}  {'H_n':>5s}  {'h² total':>15s}  {'h²=0?':>8s}")
    print(f"  {'Proton':>15s}  {'H₃':>5s}  {'0 (exact)':>15s}  {'YES ✓':>8s}  (Phase 1c)")
    for Z, N, name in atoms:
        n = 3 * (Z + N)
        h2 = h2_totals[name]
        is_zero = abs(h2) < 1e-6
        print(f"  {name:>15s}  {'H_'+str(n):>5s}  {mp.nstr(h2, 10):>15s}  "
              f"{'YES ✓' if is_zero else 'NO':>8s}")

    # Also recall ⁴He from Phase 1a (partial — only 5 of 77 partitions)
    print(f"  {'⁴He (partial)':>15s}  {'H₁₂':>5s}  {'0.509 (5/77)':>15s}  {'partial':>8s}  (Phase 1a, 5 partitions only)")

    elapsed = time.time() - t0
    print(f"\n  Total wall time: {elapsed:.1f}s")

    # Witness
    w.set_description(
        "Per-partition h-expansion for deuteron (H₆), tritium (H₉), "
        "and ³He (H₉). Tests whether the h²=0 cancellation proved at "
        "H₃ (proton) extends to heavier isotopes. Complete partition "
        "enumeration (not just trace-dominant)."
    )
    w.set_content_block("conj:proton-mass-substrate-identity")

    for Z, N, name in atoms:
        w.add_data(f"atom_{name.split()[0].lower()}", {
            "Z": Z, "N": N, "n": 3*(Z+N),
            "h2_total": str(mp.nstr(h2_totals[name], 15)),
            "h2_is_zero": abs(h2_totals[name]) < 1e-6,
            "n_partitions": len(all_atom_results[name]),
        })

    w.add_data("cross_isotope_h2_cancellation", {
        "proton_H3": "0 (exact, Phase 1c)",
        "deuteron_H6": str(mp.nstr(h2_totals["Deuteron (D)"], 15)),
        "tritium_H9": str(mp.nstr(h2_totals["Tritium (T)"], 15)),
        "he3_H9": str(mp.nstr(h2_totals["Helium-3 (³He)"], 15)),
    })

    all_zero = all(abs(h2_totals[name]) < 1e-6 for _, _, name in atoms)
    w.add_assertion(
        name="h2_cancellation_extends",
        computed=1 if all_zero else 0,
        expected=1,
        tolerance=0,
        source="h²=0 cancellation should extend from proton to D, T, ³He"
    )

    out = w.save()
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
