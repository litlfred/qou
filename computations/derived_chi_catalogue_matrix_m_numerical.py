#!/usr/bin/env python3
"""derived_chi_catalogue_matrix_m_numerical.py — Phase 1.4 numerical
backend for the matrix-M μ_p factorisation.

Per the audit doc roadmap (Step 4):
[`docs/audits/2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation.md`](../../docs/audits/2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation.md)
the matrix-M factorisation is structurally correct (PR #1980 — 42/42
cross-validation passes) but symbolic computation is slower than the
production Rust path. This module delivers the **block-scoped
numerical-cache backend** that turns the structural decomposition
into a competitive runtime path.

## What is cached

`precompute_block_tables(λ, k_split, q_0)` returns a per-μ_p block
dict containing:

  - `sigmas_left[g]` — block-restricted σ_g for g = 1, …, k_split-1
    (left H_{k_split} parabolic generators, which preserve μ_p)
  - `sigmas_right[g]` — block-restricted σ_g for g = k_split+1, …,
    n-1 (right H_{n-k_split} generators, also preserve μ_p)
  - `M_pp` — block-restricted σ_{k_split} (the BRIDGE; its full
    matrix mixes μ_p blocks, but only the diagonal block enters the
    trace formula)

Each block is `dim(μ_p)` × `dim(μ_p)` of exact `sp.Rational` entries
at substrate `q_0` — never built dim_V_λ × dim_V_λ at evaluation
time. The one-time full seminormal pass is used only to extract the
per-block sub-matrices and is then discarded.

## What runs at call time

`chi_via_numerical_matrix_m(...)` operates entirely on block matrices.
For each μ_p:

  - `B_p` = product of block-restricted left generators
  - `B_n` = product of block-restricted right generators
  - trace contribution = `Tr[B_p · M_pp · B_n]`

Total cost is `Σ_{μ_p} word_length · block_size²` of concrete
`sp.Rational` arithmetic — independent of `dim(V_λ)`. The Hecke
inverse `σ_g⁻¹ = σ_g - h·I` carries through to blocks (block
extraction is linear, so the block of σ_g⁻¹ is just the block of
σ_g minus h·I_block).

## NO f64 in the production compute path

Both the symbolic and the numerical backends are exact: matrix
entries at `q_0` are `sp.Rational` (50-digit canonical substrate
expressed as an exact rational), and all matrix operations stay in
ℚ. The benchmark below compares to Rust `chi_q_via_gp`, which
returns **exact integer Laurent coefficients in q**; we sum them at
`q_0` as `sp.Rational`. No f64 anywhere in the compute path.

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
      - `mu_p_groups`: dict mu_p → SYT indices in V_λ.
      - `blocks`: dict mu_p → block dict containing
        - `size`: dim of the μ_p-block (= count of SYTs whose first-
          k_split-cells form shape μ_p).
        - `sigmas_left[g]`: block-restricted σ_g for left H_{k_split}
          generators g = 1, …, k_split-1 (these preserve μ_p, so the
          block restriction is the full action).
        - `sigmas_right[g]`: block-restricted σ_g for right
          H_{n-k_split} generators g = k_split+1, …, n-1.
        - `M_pp`: block-restricted σ_{k_split} (diagonal-μ_p block
          of the bridge — the matrix-M(μ_p, ·, λ; q_0) summed over
          μ_n. Per-μ_n decomposition is future Phase 1.3 work).
      - `q`, `shape`, `k_split`: echoed.

    Implementation note: the full dim_V_λ × dim_V_λ seminormal pass
    is run ONCE here to extract the per-block sub-matrices; the full
    matrices are NOT retained in the cache. All call-time work
    happens on the small block matrices.
    """
    q = q_value
    n = sum(shape)
    # One-time full seminormal pass to extract block sub-matrices;
    # we discard the full matrices once blocks are pulled.
    sigmas = seminormal_matrices_qrat(shape, q)
    groups = group_syts_by_mu_p(shape, k_split)
    blocks: dict[tuple[int, ...], dict] = {}
    for mu_p, idxs in groups.items():
        sigmas_left = {
            g: sigmas[g - 1].extract(idxs, idxs)
            for g in range(1, k_split)
        }
        sigmas_right = {
            g: sigmas[g - 1].extract(idxs, idxs)
            for g in range(k_split + 1, n)
        }
        M_pp = sigmas[k_split - 1].extract(idxs, idxs)
        blocks[mu_p] = {
            "size": len(idxs),
            "indices": idxs,
            "sigmas_left": sigmas_left,
            "sigmas_right": sigmas_right,
            "M_pp": M_pp,
        }
    # Drop the full sigmas — block extraction is done.
    return {
        "shape": shape,
        "k_split": k_split,
        "q": q,
        "mu_p_groups": groups,
        "blocks": blocks,
    }


def chi_via_numerical_matrix_m(
    shape: tuple[int, ...],
    word_left: list[tuple[int, int]],
    bridge_sign: int,
    word_right: list[tuple[int, int]],
    cache: dict,
) -> sp.Rational:
    """Compute χ^λ(T_β) at the cached q_0 via the μ_p-block trace
    formula, operating entirely on the pre-computed BLOCK matrices —
    never building dim_V_λ × dim_V_λ matrices at call time.

    For each μ_p:
      B_p[μ_p]  = ∏ (block-restricted left generators)
      B_n[μ_p]  = ∏ (block-restricted right generators)
      contrib   = Tr [ B_p · M_pp · B_n ]   (per cache["blocks"][μ_p]["M_pp"])
      χ        += contrib

    The Hecke inverse `σ_g⁻¹ = σ_g - h·I` carries through to blocks
    (block extraction is linear); we use it for both the parabolic
    generators (where the block-restriction is exact) and for the
    bridge (where the diagonal block of σ_{k_split}⁻¹ is the
    diagonal block of σ_{k_split} minus h · I_block).
    """
    q = cache["q"]
    k_split = cache["k_split"]
    h = q - 1 / q
    total = sp.Integer(0)

    for mu_p, block in cache["blocks"].items():
        size = block["size"]
        eye_block = sp.eye(size)
        sigmas_left = block["sigmas_left"]
        sigmas_right = block["sigmas_right"]
        M_pp_pos = block["M_pp"]

        def block_sigma(table: dict, g_1based: int, sign: int) -> sp.Matrix:
            mat = table[g_1based]
            return mat if sign >= 0 else mat - h * eye_block

        # B_p on the μ_p-block.
        B_p = eye_block
        for (sign, g_1based) in word_left:
            B_p = B_p * block_sigma(sigmas_left, g_1based, sign)
        # B_n on the μ_p-block.
        B_n = eye_block
        for (sign, g_1based) in word_right:
            B_n = B_n * block_sigma(sigmas_right, g_1based, sign)
        # Bridge: positive direct, negative via Hecke inverse on block.
        M = M_pp_pos if bridge_sign >= 0 else (M_pp_pos - h * eye_block)
        total = total + sp.trace(B_p * M * B_n)
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
