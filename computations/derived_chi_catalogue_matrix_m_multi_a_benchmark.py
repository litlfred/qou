#!/usr/bin/env python3
"""derived_chi_catalogue_matrix_m_multi_a_benchmark.py — generalise
the numerical matrix-M backend past the deuteron (A=2) onto
multi-bridge atomic braids and measure cross-over wall time vs Rust
`chi_q_via_gp`.

## The recursive μ_0 structure

For any atom β = β_0 · σ_3 · β_1 · σ_6 · β_2 · … · σ_{3(A-1)} · β_{A-1}
on `n = 3A` strands, the FIRST parabolic split at `k_split = 3`
gives the audit-doc §5 / §6.2 decomposition:

    χ^λ(T_β) = Σ_{μ_0 ⊢ 3} Tr [ B_0[μ_0]
                              · M_pp[μ_0, λ]
                              · ρ_rest[μ_0](T_{β_1 · σ_6 · … · β_{A-1}}) ]

The same `chi_lambda_via_mu_p_decomposition` (Phase 1.2, PR #1980 +
#1985) handles this for arbitrary A because `word_right` may
contain any number of further bridges (σ_6, σ_9, …) — they're all
in the right half of the parabolic structure. The audit doc §6.2
fully recursive (μ_0, ν_1, …, ν_{A-1}) factorisation is a strict
refinement that drops the per-call block size further; this PR
gates the recursion at the μ_0 (first nucleon) level only, which is
already sufficient to test the architectural premise.

## What this benchmark measures

For each isotope (A=2 ²H, A=3 ³H, A=4 ⁴He):
  1. Parse `atom_braid_word_3A(Z, N)` into the left / bridge / right
     split at `k_split = 3` (first bridge).
  2. For each small-dim partition λ ⊢ 3A, precompute the block
     tables at the substrate q_0.
  3. Compute χ^λ via the numerical matrix-M backend; compute the
     same via Rust `chi_q_via_gp` evaluated at q_0; verify they
     agree EXACTLY (sp.Rational comparison, no f64).
  4. Time each — report the cross-over.

If the matrix-M / Rust speedup ratio crosses 1.0× somewhere between
A=2 and A=4, the architectural premise (block-size-bounded call
cost, flat in `n`) is empirically validated. If not, Phase 1.3
((μ_p, μ_n)-level block extraction via H_3 idempotents) is the
next refinement to investigate.

## NO f64 in production

Same discipline as `derived_chi_catalogue_matrix_m_numerical.py`:
substrate q_0 is `sp.Rational(Q_50_DIGIT_STR)`; all matrix entries
are `sp.Rational`; Rust path returns exact integer Laurent
coefficients summed at q_0 in ℚ. The benchmark times the EXACT
compute path used in production.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: E402, F401

import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

from derived_chi_catalogue_matrix_m import (  # noqa: E402
    standard_young_tableaux,
    _shape_partitions_of,
    _word_for_braid_word_3a,
)
from derived_chi_catalogue_matrix_m_numerical import (  # noqa: E402
    precompute_block_tables,
    chi_via_numerical_matrix_m,
    chi_rust_at_q,
)


# ── Per-atom benchmark ─────────────────────────────────────────────


def split_atom_braid_at_first_bridge(
    Z: int, N: int
) -> tuple[
    int,  # n_strands
    list[tuple[int, int]],  # word_left  (gens ≤ 2)
    int,  # bridge sign (±1)
    list[tuple[int, int]],  # word_right (gens ≥ 4)
]:
    """Parse atom_braid_word_3A(Z, N) and split at the FIRST bridge
    σ_3. Per `mass_at_3A_proper.atom_braid_word_3A`, the production
    atom is always laid out left-nucleon · σ_3 · rest, where rest may
    contain further bridges σ_6, σ_9, … for A ≥ 3.
    """
    n_strands, word = _word_for_braid_word_3a(Z, N)
    word_left = [t for t in word if t[1] <= 2]
    bridge = [t for t in word if t[1] == 3]
    word_right = [t for t in word if t[1] >= 4]
    assert word_left + bridge + word_right == word, (
        "atom braid word is not parabolic-shaped at k_split=3 — "
        "split + reassemble does not round-trip"
    )
    assert len(bridge) == 1, (
        f"expected exactly one σ_3 bridge in atom_braid_word_3A({Z}, {N}); "
        f"got {len(bridge)}: {bridge}"
    )
    bridge_sign = bridge[0][0]
    return n_strands, word_left, bridge_sign, word_right


def benchmark_isotope(
    label: str,
    Z: int,
    N: int,
    q_0: sp.Rational,
    max_dim: int,
) -> dict:
    """Run the matrix-M backend + Rust comparison on all partitions
    of `n = 3(Z+N)` whose dim V_λ ≤ max_dim. Report wall times.
    """
    A = Z + N
    n_strands, deut_left, bridge_sign, deut_right = (
        split_atom_braid_at_first_bridge(Z, N)
    )
    full_word = deut_left + [(bridge_sign, 3)] + deut_right
    partitions = _shape_partitions_of(n_strands)
    small_partitions = [
        s for s in partitions
        if len(standard_young_tableaux(s)) <= max_dim
    ]

    print(f"\n  {label}  (Z={Z}, N={N}, A={A}, n={n_strands})")
    print(f"  ──────────────────────────────────────────────")
    # The split asserts exactly one σ_3 bridge — print the constant.
    print(f"    β = {len(full_word)} crossings  "
          f"(left={len(deut_left)}, bridge=1, "
          f"right={len(deut_right)})")
    print(f"    Testing {len(small_partitions)}/{len(partitions)} partitions "
          f"(dim V_λ ≤ {max_dim})")

    cases: list[dict] = []
    total_precompute_s = 0.0
    total_call_s = 0.0
    total_rust_s = 0.0
    for shape in small_partitions:
        dim = len(standard_young_tableaux(shape))

        t0 = time.monotonic()
        cache = precompute_block_tables(shape, k_split=3, q_value=q_0)
        precompute_s = time.monotonic() - t0
        total_precompute_s += precompute_s

        t0 = time.monotonic()
        chi_python = chi_via_numerical_matrix_m(
            shape, deut_left, bridge_sign, deut_right, cache,
        )
        call_s = time.monotonic() - t0
        total_call_s += call_s

        t0 = time.monotonic()
        chi_rust = chi_rust_at_q(shape, n_strands, full_word, q_0)
        rust_s = time.monotonic() - t0
        total_rust_s += rust_s

        # Both sides are exact sp.Rational (or sp.Integer) — direct
        # `==` is decidable and dramatically cheaper than the
        # symbolic-rational-function reducer sp.cancel.
        match = (chi_python == chi_rust)
        status = "✓" if match else "✗"
        # speedup = rust_s / call_s  — >1× means matrix-M beats Rust.
        speedup = rust_s / call_s if call_s > 0 else float("inf")

        shape_str = str(list(shape))
        print(f"      {status} λ={shape_str:<22s} dim={dim:>3d}  "
              f"pre={precompute_s*1000:>6.1f}ms  "
              f"call={call_s*1000:>6.1f}ms  "
              f"rust={rust_s*1000:>6.1f}ms  "
              f"speedup={speedup:.2f}×")

        cases.append({
            "shape": list(shape),
            "dim_V_lambda": dim,
            "precompute_secs": precompute_s,
            "call_secs": call_s,
            "rust_secs": rust_s,
            "match": match,
        })

    n_total = len(cases)
    n_pass = sum(1 for c in cases if c["match"])
    # Aggregate speedup = total_rust / total_call (>1 means matrix-M wins).
    speedup_overall = (
        total_rust_s / total_call_s if total_call_s > 0 else float("inf")
    )
    print(f"\n    Totals: pass={n_pass}/{n_total}  "
          f"precompute={total_precompute_s*1000:.1f}ms  "
          f"call={total_call_s*1000:.1f}ms  "
          f"rust={total_rust_s*1000:.1f}ms  "
          f"speedup={speedup_overall:.2f}×")
    return {
        "label": label,
        "Z": Z, "N": N, "A": A, "n_strands": n_strands,
        "n_partitions_tested": n_total,
        "n_passed": n_pass,
        "total_precompute_secs": total_precompute_s,
        "total_call_secs": total_call_s,
        "total_rust_secs": total_rust_s,
        "speedup_rust_over_call": speedup_overall,
        "cases": cases,
    }


# ── Main ──────────────────────────────────────────────────────────


def main() -> int:
    wb = WitnessBuilder(
        "derived-chi-catalogue-matrix-m-multi-a-benchmark",
        engine="python",
    )
    wb.set_description(
        "Multi-A cross-over benchmark for the numerical matrix-M μ_0 "
        "backend vs Rust chi_q_via_gp. Per the audit doc roadmap "
        "(Step 5 / Phase 2 multi-bridge): the matrix-M call wall "
        "stays nearly flat in n once σ-precompute amortises while "
        "Geck-Pfeiffer scales nontrivially — empirically tests where "
        "the cross-over lies between A=2 and A=4. NO f64 in the "
        "compute path: exact sp.Rational throughout."
    )

    from q_parameter import Q_50_DIGIT_STR
    q_0 = sp.Rational(Q_50_DIGIT_STR)

    print("=" * 78)
    print(" Multi-A matrix-M cross-over benchmark vs Rust chi_q_via_gp")
    print("=" * 78)
    print(f"  q_0 = {Q_50_DIGIT_STR[:30]}…  (proton-anchored substrate)")

    # Configure the isotope sweep. Limit dim V_λ per-A so wall time
    # stays bounded — small enough for fast iteration, big enough to
    # exercise the block-restriction path on representative partitions.
    isotopes = [
        # (label, Z, N, max_dim)
        ("²H (deuteron)", 1, 1, 5),
        ("³H (tritium)",  1, 2, 8),
        ("³He",           2, 1, 8),
        # ⁴He at n=12: largest small-dim partition is around 11. Cap
        # tight to keep wall under a few minutes on this branch.
        ("⁴He (alpha)",   2, 2, 11),
    ]

    isotope_results: list[dict] = []
    for (label, Z, N, max_dim) in isotopes:
        result = benchmark_isotope(label, Z, N, q_0, max_dim)
        isotope_results.append(result)

    n_total = sum(r["n_partitions_tested"] for r in isotope_results)
    n_pass = sum(r["n_passed"] for r in isotope_results)
    print("\n" + "=" * 78)
    print(f"  Multi-A summary: {n_pass}/{n_total} partitions match Rust at q_0")
    print("  " + "─" * 76)
    print(f"  {'Isotope':<18}  {'A':<2}  {'n':<3}  {'pass':<6}  "
          f"{'call ms':>8}  {'rust ms':>8}  {'speedup':>10}")
    for r in isotope_results:
        ratio = r["speedup_rust_over_call"]
        print(f"  {r['label']:<18}  {r['A']:<2}  {r['n_strands']:<3}  "
              f"{r['n_passed']}/{r['n_partitions_tested']:<4}  "
              f"{r['total_call_secs']*1000:>8.1f}  "
              f"{r['total_rust_secs']*1000:>8.1f}  "
              f"{ratio:>9.2f}×")
    print("=" * 78)

    wb.add_assertion(
        "matrix_m_matches_rust_on_all_isotopes",
        computed=(n_pass == n_total),
        expected=True,
        source="Whether the numerical matrix-M backend matches Rust "
               "chi_q_via_gp evaluated at the substrate q_0 across "
               "deuteron, tritium, ³He, and ⁴He (small-dim partitions). "
               "Same trace identity as PR #1980/#1985, exercised on "
               "multi-bridge braids (A ≥ 3).",
    )
    wb.add_data("q_0_substrate_str", Q_50_DIGIT_STR)
    wb.add_data("n_partitions_tested", n_total)
    wb.add_data("n_passed", n_pass)
    wb.add_data("isotopes", isotope_results)

    out = wb.save()
    print(f"\n  ✓ Witness: {out.name}")
    return 0 if n_pass == n_total else 1


if __name__ == "__main__":
    sys.exit(main())
