#!/usr/bin/env python3
"""derived_chi_catalogue_matrix_m_numerical.py — Phase 1.4 numerical
backend for the matrix-M μ_p factorisation.

Per the audit doc roadmap (Step 4):
[`docs/audits/2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation.md`](../../docs/audits/2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation.md)
the matrix-M factorisation is structurally correct (PR #1980 — 42/42
cross-validation passes) but symbolic computation is slower than the
Rust Geck-Pfeiffer engine. This module delivers the **numerical-cache
backend** that turns the structural decomposition into a competitive
runtime path:

  - **Pre-compute** σ_3, σ_4, σ_5 (and inverses) for V_λ at the
    substrate q_0 ONCE per λ. Result: tiny sympy.Rational matrices.
  - **At call time**: form the product `B_p · σ_3 · B_n` numerically
    on the small μ_p-blocks, sum the traces. Each call is O(word
    length · max_block_size²) of concrete-rational arithmetic.
  - **Validate vs Rust** `chi_q_via_gp` at q_0 — same Laurent
    coefficients required.

## Why this matters

For A=2 (deuteron, n=6) Rust `chi_q_via_gp` is already fast (~10 ms
per call). The numerical-cache backend isn't expected to win here —
the value is the **architecture proof**: showing that the block-
reduction structure is real (not just symbolically convenient), and
that the cache scales to larger atoms where Geck-Pfeiffer's Solomon-
Tits reduction time dominates.

## Δ_λ-gate

Same matrix identity as PR #1980 — pure structural rearrangement, no
new ansatz, no calibration parameter, no empirical fit.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: E402, F401

import sympy as sp  # noqa: E402

import pyhecke_native as ph  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

from derived_chi_catalogue_matrix_m import (  # noqa: E402
    seminormal_matrices_qrat,
    standard_young_tableaux,
    group_syts_by_mu_p,
    _shape_partitions_of,
    _word_for_braid_word_3a,
    chi_lambda_via_mu_p_decomposition,
    chi_lambda_via_matrix_product,
)


# ── Precomputed numerical block tables ────────────────────────────


def precompute_block_tables(
    shape: tuple[int, ...],
    k_split: int,
    q_value: sp.Rational,
) -> dict:
    """Pre-build the per-μ_p block data at numerical q.

    Args:
      shape: λ ⊢ n.
      k_split: position of the parabolic split (deuteron: 3).
      q_value: substrate q as exact sp.Rational.

    Returns a dict with:
      - `sigmas`: list of σ_i matrices on V_λ (numerical entries)
      - `sigma_invs`: list of σ_i⁻¹ matrices (numerical)
      - `mu_p_groups`: dict mu_p → SYT indices in V_λ
      - `M_pp`: dict mu_p → sub-matrix of σ_{k_split} restricted to the
        μ_p-block. This is the matrix-M(μ_p, ·, λ; q_0) summed over
        μ_n (the per-μ_n decomposition would split this further;
        future Phase 1.3 work).
      - `q`: the substrate q value (echoed for inspection).
    """
    q = q_value
    # Build σ_i matrices in seminormal form, but evaluate at q_value
    # directly (sp.Rational entries, no symbolic q).
    sigmas = seminormal_matrices_qrat(shape, q)
    dim = sigmas[0].shape[0] if sigmas else 1
    h = q - 1 / q
    eye = sp.eye(dim)
    sigma_invs = [
        (mat - h * eye).applyfunc(sp.cancel) for mat in sigmas
    ]
    # σ_{k_split} matrix (1-based gen — k_split is also the 1-based
    # bridge generator index).
    sigma_bridge = sigmas[k_split - 1]
    groups = group_syts_by_mu_p(shape, k_split)
    M_pp: dict[tuple[int, ...], sp.Matrix] = {}
    for mu_p, idxs in groups.items():
        M_pp[mu_p] = sigma_bridge.extract(idxs, idxs)
    return {
        "shape": shape,
        "k_split": k_split,
        "q": q,
        "dim": dim,
        "sigmas": sigmas,
        "sigma_invs": sigma_invs,
        "mu_p_groups": groups,
        "M_pp": M_pp,
    }


def chi_via_numerical_matrix_m(
    shape: tuple[int, ...],
    word_left: list[tuple[int, int]],
    bridge_sign: int,
    word_right: list[tuple[int, int]],
    cache: dict,
) -> sp.Rational:
    """Compute χ^λ(T_β) at the cached q_0 via the μ_p-block trace
    formula, using the pre-computed σ matrices.

    The matrix-M is `cache["M_pp"][μ_p]` (positive-bridge case) or
    its appropriate q-Hecke transform for negative-bridge. For
    bridge_sign = -1, we use the inverse formula
    `σ_{k_split}⁻¹ = σ_{k_split} - h · I`.
    """
    k_split = cache["k_split"]
    sigmas = cache["sigmas"]
    sigma_invs = cache["sigma_invs"]
    groups = cache["mu_p_groups"]
    dim = cache["dim"]
    eye = sp.eye(dim)

    def get_sigma(g_1based: int, sign: int) -> sp.Matrix:
        idx = g_1based - 1
        return sigmas[idx] if sign >= 0 else sigma_invs[idx]

    def word_to_matrix(word: list[tuple[int, int]]) -> sp.Matrix:
        prod = eye
        for (sign, g_1based) in word:
            # No applyfunc(cancel) needed — entries are concrete sp.Rationals,
            # multiplication keeps them as Rationals automatically.
            prod = prod * get_sigma(g_1based, sign)
        return prod

    B_p_full = word_to_matrix(word_left)
    B_n_full = word_to_matrix(word_right)
    M_full = get_sigma(k_split, bridge_sign)

    total = sp.Integer(0)
    for mu_p, idxs in groups.items():
        sub_B_p = B_p_full.extract(idxs, idxs)
        sub_M = M_full.extract(idxs, idxs)
        sub_B_n = B_n_full.extract(idxs, idxs)
        total = total + sp.trace(sub_B_p * sub_M * sub_B_n)
    return total


# ── Validation + benchmark vs Rust ────────────────────────────────


def chi_rust_at_q(
    shape: tuple[int, ...],
    n_strands: int,
    word: list[tuple[int, int]],
    q_value: sp.Rational,
) -> sp.Rational:
    """Evaluate Rust `chi_q_via_gp` and sum Laurent terms at the
    given exact q_value (sp.Rational).

    Handles both half-exp (even key) and direct-encoded (odd key)
    catalogue conventions per PR #1979's encoding fix.
    """
    laurent = ph.chi_q_via_gp(list(shape), n_strands, list(word))
    total = sp.Integer(0)
    for (d_key, c_str) in laurent:
        d_int = int(d_key)
        if d_int % 2 == 0:
            total += sp.Integer(int(c_str)) * q_value ** (d_int // 2)
        else:
            total += sp.Integer(int(c_str)) * q_value ** sp.Rational(d_int, 2)
    return total


# ── Main: benchmark + validate ────────────────────────────────────


def main() -> int:
    wb = WitnessBuilder(
        "derived-chi-catalogue-matrix-m-numerical",
        engine="python",
    )
    wb.set_description(
        "Phase 1.4 numerical-cache backend for the matrix-M μ_p "
        "factorisation. Pre-computes σ matrices at substrate q_0 "
        "ONCE per λ, then uses small Rational matrix products on "
        "the μ_p-blocks per call. Validates against Rust "
        "chi_q_via_gp at q_0 and benchmarks wall time."
    )

    print("=" * 78)
    print(" Numerical-cache matrix-M backend — validation + benchmark")
    print("=" * 78)

    # Substrate q_0 from canonical pin.
    from q_parameter import Q_50_DIGIT_STR
    q_0 = sp.Rational(Q_50_DIGIT_STR)
    print(f"\n  q_0 = {Q_50_DIGIT_STR[:30]}…")

    # Production deuteron braid β = atom_braid_word_3A(1, 1).
    n_strands, deut_word = _word_for_braid_word_3a(1, 1)
    print(f"  Production deuteron β: n={n_strands}, "
          f"{len(deut_word)} crossings")

    # Split into left / bridge / right (parabolic shape).
    deut_left = [t for t in deut_word if t[1] <= 2]
    deut_bridge = [t for t in deut_word if t[1] == 3]
    deut_right = [t for t in deut_word if t[1] >= 4]
    assert deut_left + deut_bridge + deut_right == deut_word
    assert len(deut_bridge) == 1
    bridge_sign = deut_bridge[0][0]

    print(f"  β_left = {len(deut_left)}, bridge = σ_3^{bridge_sign},"
          f" β_right = {len(deut_right)}\n")

    # Validate on all small-dim partitions of 6.
    cases: list[dict] = []
    small_partitions = [
        s for s in _shape_partitions_of(6)
        if len(standard_young_tableaux(s)) <= 5
    ]
    total_precompute_s = 0.0
    total_call_s = 0.0
    total_rust_s = 0.0
    for shape in small_partitions:
        dim = len(standard_young_tableaux(shape))

        # Precompute the block tables at q_0.
        t0 = time.monotonic()
        cache = precompute_block_tables(shape, k_split=3, q_value=q_0)
        precompute_s = time.monotonic() - t0
        total_precompute_s += precompute_s

        # Call: compute χ via numerical matrix-M.
        t0 = time.monotonic()
        chi_python = chi_via_numerical_matrix_m(
            shape, deut_left, bridge_sign, deut_right, cache,
        )
        call_s = time.monotonic() - t0
        total_call_s += call_s

        # Rust gold standard at q_0 (sum Laurent at q_0).
        t0 = time.monotonic()
        chi_rust = chi_rust_at_q(shape, n_strands, deut_word, q_0)
        rust_s = time.monotonic() - t0
        total_rust_s += rust_s

        # Compare exactly (both sides are sp.Rational at substrate q_0).
        delta = sp.cancel(chi_python - chi_rust)
        match = (delta == 0)
        status = "✓" if match else "✗"

        # Speedup ratio. The fair comparison is Rust wall time vs
        # numerical-backend call wall time (precompute is one-time
        # amortizable over many calls).
        call_speedup = rust_s / call_s if call_s > 0 else float("inf")

        print(f"  {status} λ={list(shape)} dim={dim}  "
              f"precompute={precompute_s*1000:6.1f} ms  "
              f"call={call_s*1000:6.2f} ms  "
              f"rust={rust_s*1000:6.2f} ms  "
              f"call/rust={call_speedup:.2f}×")
        cases.append({
            "shape": list(shape),
            "dim_V_lambda": dim,
            "precompute_secs": precompute_s,
            "call_secs": call_s,
            "rust_secs": rust_s,
            "call_speedup_vs_rust": call_speedup,
            "match": match,
        })

    n_total = len(cases)
    n_pass = sum(1 for c in cases if c["match"])
    print(f"\n  ── Summary ──")
    print(f"    Tests:               {n_total}")
    print(f"    Passed:              {n_pass}")
    print(f"    Failed:              {n_total - n_pass}")
    print(f"    Total precompute:    {total_precompute_s:.3f} s")
    print(f"    Total call:          {total_call_s*1000:.1f} ms")
    print(f"    Total rust:          {total_rust_s*1000:.1f} ms")
    if total_call_s > 0:
        print(f"    Call speedup:        {total_rust_s / total_call_s:.2f}×")
    print(f"    (Note: precompute is one-time per λ; the meaningful "
          f"runtime comparison is call vs rust.)")

    wb.add_assertion(
        "numerical_matrix_m_matches_rust_at_substrate_q",
        computed=(n_pass == n_total),
        expected=True,
        source="Whether the pre-computed numerical matrix-M backend "
               "(σ matrices at q_0 cached per λ; small Rational matrix "
               "product per call) reproduces Rust chi_q_via_gp's Laurent "
               "sum evaluated at q_0 on the production deuteron braid "
               "for all 6 small-dim partitions of 6. This is the Phase 1.4 "
               "(audit-doc Step 4) backend-validation criterion.",
    )
    wb.add_data("q_0_substrate_str", Q_50_DIGIT_STR)
    wb.add_data("n_test_cases", n_total)
    wb.add_data("n_pass", n_pass)
    wb.add_data("cases", cases)
    wb.add_data("total_precompute_secs", total_precompute_s)
    wb.add_data("total_call_secs", total_call_s)
    wb.add_data("total_rust_secs", total_rust_s)
    out = wb.save()
    print(f"\n  ✓ Witness: {out.name}")
    print("=" * 78)
    return 0 if n_pass == n_total else 1


if __name__ == "__main__":
    sys.exit(main())
