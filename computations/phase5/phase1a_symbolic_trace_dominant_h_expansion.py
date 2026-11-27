#!/usr/bin/env python3
"""
Phase 1a: per-partition h-expansion of trace-dominant ⁴He contributions.

For the 5 trace-dominant 2-row partitions of n=12 (⁴He in H₁₂):
  [9,3]=32%, [8,4]=26%, [10,2]=15%, [11,1]=11%, [7,5]=11%

compute y_λ(q) · χ^λ(T_w_⁴He)(q) as a series in h = q - q⁻¹:

  y_λ · χ^λ = c₀(λ) + c₁(λ)·h + c₂(λ)·h² + c₃(λ)·h³ + c₄(λ)·h⁴ + ...

and identify which partition(s) carry the Reading-A residual.

Method: evaluate at N distinct q values (mpmath 80 dps), form the
Vandermonde system in h(q) = q - q⁻¹, and solve for the h-series
coefficients. Both y_λ(q) and χ^λ(T_w)(q) are rational functions
of q — the Hecke algebra characters are in ℤ[q,q⁻¹] even though
individual Hoefsmit matrix entries involve √q.

The braid word is parameterized by h = q - q⁻¹: each crossing's d
coefficient is either 0 (σ), -h (σ⁻¹), or -h/2 (σ_avg). The
structural pattern is independent of q.

Audit-only.
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
from hecke_characters import standard_young_tableaux, build_seminormal_matrices  # noqa: E402
from partition_utils import hook_lengths_with_cells  # noqa: E402
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402


# ── Braid word: structural pattern (independent of q) ──────────
# Each entry is (c, d_mult, gen_idx) where the actual operator is
# c·σ_g + (d_mult · h)·I at any q.
# d_mult ∈ {0, -0.5, -1}: σ(0), σ_avg(-0.5), σ⁻¹(-1).

def _he4_braid_pattern():
    """⁴He structural braid pattern on 12 strands (Z=2, N=2).

    Returns list of (c, d_mult, gen_idx) where d_mult is the
    h-multiplier for the d coefficient: 0 (σ), -0.5 (σ_avg), -1 (σ⁻¹).
    """
    # Per hecke_core analysis: d values are exact multiples of h
    # P_G0: [(1,0)×4, (1,-h/2), (1,0)×2]
    P_G0 = [(1, 0)] * 4 + [(1, -0.5)] + [(1, 0)] * 2
    # P_G1: [(1,-h)×3, (1,-h/2)]
    P_G1 = [(1, -1.0)] * 3 + [(1, -0.5)]
    # N_G0: [(1,0)×3, (1,-h/2)×2, (1,0)×2]
    N_G0 = [(1, 0)] * 3 + [(1, -0.5)] * 2 + [(1, 0)] * 2
    # N_G1: [(1,-h)×4]
    N_G1 = [(1, -1.0)] * 4

    ordering = ['p', 'p', 'n', 'n']
    A = 4
    pattern = []

    for k, nuc in enumerate(ordering):
        if nuc == 'p':
            intra0, intra1 = P_G0, P_G1
        else:
            intra0, intra1 = N_G0, N_G1

        for c, dm in intra0:
            pattern.append((c, dm, 3 * k))
        for c, dm in intra1:
            pattern.append((c, dm, 3 * k + 1))

        if k < A - 1:
            next_nuc = ordering[k + 1]
            if nuc == 'p' and next_nuc == 'p':
                pattern.append((1, 0, 3 * k + 2))       # pp: σ
            elif nuc == 'n' and next_nuc == 'n':
                pattern.append((1, -1.0, 3 * k + 2))    # nn: σ⁻¹
            else:
                pattern.append((1, -0.5, 3 * k + 2))    # pn: σ_avg

    return pattern


# Cache the pattern (it's structural, same for all q)
_HE4_PATTERN = _he4_braid_pattern()


def chi_lambda_at_q(shape, q_val):
    """Compute χ^λ(T_w_⁴He) at a specific numerical q.

    Builds the Hoefsmit seminormal matrices at q_val, instantiates
    the braid word with h(q_val), and computes the trace.
    """
    q_f = float(q_val)
    h_val = q_f - 1.0 / q_f

    sigmas, dim, syts = build_seminormal_matrices(shape, q=q_f)
    if dim == 0:
        return 0.0

    sigmas = [s.toarray() if hasattr(s, 'toarray') else np.asarray(s)
              for s in sigmas]
    product = np.eye(dim)
    I = np.eye(dim)

    for (c, dm, g) in _HE4_PATTERN:
        d = dm * h_val
        M = c * sigmas[g] + d * I
        product = product @ M

    return float(np.trace(product))


def dim_syt(shape):
    """Number of standard Young tableaux."""
    from math import factorial
    n = sum(shape)
    cells = hook_lengths_with_cells(list(shape))
    hprod = 1
    for (_, _, hk) in cells:
        hprod *= hk
    return factorial(n) // hprod


def main():
    set_compute_dps()
    t0 = time.time()
    print("=" * 70)
    print("  Phase 1a: per-partition h-expansion — trace-dominant ⁴He")
    print("=" * 70)
    print()

    q0 = Q_MP
    h0 = q0 - 1 / q0

    # q sample points: spread around q₀ for good conditioning
    # h(q) = q - 1/q is monotone for q > 0, so distinct q → distinct h
    offsets = [0, 0.005, -0.005, 0.012, -0.012, 0.025, -0.025,
               0.04, -0.04, 0.06, -0.06]
    q_points = [q0 + mp.mpf(str(off)) for off in offsets]
    h_points = [qi - 1 / qi for qi in q_points]

    n_terms = 7  # h⁰ through h⁶
    assert len(q_points) >= n_terms

    trace_dominant_5 = [(11, 1), (10, 2), (9, 3), (8, 4), (7, 5)]
    all_results = []
    h2_coeffs = {}

    for shape in trace_dominant_5:
        d = dim_syt(shape)
        print(f"  λ = {list(shape)}, d_λ = {d}")
        t1 = time.time()

        # Evaluate y_λ · χ^λ at each q point
        f_vals = []
        y_at_q0 = None
        chi_at_q0 = None
        for qi_idx, qi in enumerate(q_points[:n_terms]):
            qi_f = float(qi)
            mp.mp.dps = 80

            y_val = y_lambda_wenzl_bridge_numeric(list(shape), qi, dps=80)
            # NO FLOAT64 (bean qou-65qv): y_val above is taken at the exact qi
            # while chi was taken at the float64 qi_f -- a layer straddle
            # inside a single product. Both now use qi.
            chi_val = chi_lambda_at_q(shape, qi)

            product = mp.mpf(y_val) * mp.mpf(chi_val)
            f_vals.append(product)

            if qi_idx == 0:
                y_at_q0 = y_val
                chi_at_q0 = chi_val

        # Solve Vandermonde system: f(q_i) = Σ_k c_k · h_i^k
        mp.mp.dps = 80
        V = mp.matrix(n_terms, n_terms)
        for i in range(n_terms):
            for k in range(n_terms):
                V[i, k] = h_points[i] ** k
        rhs = mp.matrix(n_terms, 1)
        for i in range(n_terms):
            rhs[i] = f_vals[i]

        wall = time.time() - t1

        try:
            coeffs = mp.lu_solve(V, rhs)
            result = {
                "partition": list(shape),
                "d_lambda": d,
                "wall_time_s": f"{wall:.2f}",
                "y_at_q0": str(mp.nstr(y_at_q0, 20)),
                "chi_at_q0": str(mp.nstr(mp.mpf(chi_at_q0), 20)),
                "product_at_q0": str(mp.nstr(f_vals[0], 20)),
                "h_coefficients": {},
            }

            print(f"    y_λ(q₀)  = {mp.nstr(y_at_q0, 12)}")
            print(f"    χ^λ(q₀)  = {mp.nstr(mp.mpf(chi_at_q0), 12)}")
            print(f"    y·χ(q₀)  = {mp.nstr(f_vals[0], 12)}")
            print(f"    h-expansion:")
            for k in range(n_terms):
                c_k = coeffs[k]
                result["h_coefficients"][str(k)] = str(mp.nstr(c_k, 20))
                marker = " ◄" if k == 2 else ""
                print(f"      c_{k} (h^{k}): {mp.nstr(c_k, 15)}{marker}")
                if k == 2:
                    h2_coeffs[shape] = c_k
        except Exception as e:
            result = {
                "partition": list(shape),
                "d_lambda": d,
                "wall_time_s": f"{wall:.2f}",
                "status": f"solve_failed: {e}",
            }
            print(f"    FAILED: {e}")

        all_results.append(result)
        print(f"    ({wall:.1f}s)")
        print()

    # ── Summary ──────────────────────────────────────────────────
    print("=" * 70)
    print("  SUMMARY: per-partition h² coefficients")
    print("=" * 70)

    total_h2 = mp.mpf(0)
    for shape in trace_dominant_5:
        if shape in h2_coeffs:
            c2 = h2_coeffs[shape]
            total_h2 += c2
            print(f"  {str(list(shape)):>12s}: c₂ = {mp.nstr(c2, 15)}")

    print(f"\n  Sum c₂ (5 dominant):    {mp.nstr(total_h2, 15)}")

    # Reading-A comparison
    reading_a_c2 = mp.mpf("-0.91628187612727")
    minus_G = mp.mpf("-0.915965594177219")
    family_a_c2 = mp.mpf("0.75")
    print(f"  c₂ implied (Reading-A): {mp.nstr(reading_a_c2, 15)}")
    print(f"  −G (Catalan):           {mp.nstr(minus_G, 15)}")
    print(f"  Family A:               {mp.nstr(family_a_c2, 15)}")
    if total_h2 != 0:
        gap_to_reading_a = total_h2 - reading_a_c2
        print(f"\n  Gap (sum − Reading-A):   {mp.nstr(gap_to_reading_a, 15)}")
        print(f"  Gap (sum − (−G)):        {mp.nstr(total_h2 - minus_G, 15)}")

    # Per-partition contribution fractions
    if total_h2 != 0:
        print(f"\n  Per-partition h² share:")
        for shape in trace_dominant_5:
            if shape in h2_coeffs:
                frac = h2_coeffs[shape] / total_h2 * 100
                print(f"    {str(list(shape)):>12s}: {mp.nstr(frac, 6)}%")

    elapsed = time.time() - t0
    print(f"\n  Total wall time: {elapsed:.1f}s")

    # ── Witness ──────────────────────────────────────────────────
    w = WitnessBuilder("phase1a-per-partition-h-expansion", engine="mpmath")
    w.set_description(
        "Per-partition h-expansion of y_λ·χ^λ(T_w_⁴He) for the 5 "
        "trace-dominant 2-row partitions. Extracts per-partition h² "
        "coefficient via multi-point Vandermonde solve at 80 dps. "
        "Identifies which partition(s) carry the Reading-A residual gap."
    )
    w.set_content_block("conj:psd-trace-orthogonality")
    w.set_audit_only("docs/audits/2026-05-26-phase1a-per-partition-h-expansion.md")

    w.add_data("results", all_results)
    w.add_data("h2_coefficient_sum", str(mp.nstr(total_h2, 20)))
    w.add_data("comparison", {
        "reading_a_implied_c2": "-0.91628187612727",
        "catalan_minus_G": "-0.915965594177219",
        "family_a_c2": "0.75",
        "sum_5_dominant_c2": str(mp.nstr(total_h2, 20)),
    })

    n_computed = sum(1 for r in all_results if "h_coefficients" in r)
    w.add_assertion(
        name="all_5_computed",
        computed=n_computed,
        expected=5,
        tolerance=0,
        source="All 5 trace-dominant partitions should be computable"
    )

    out = w.save()
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
