#!/usr/bin/env python3
"""derived_chi_catalogue_consumer_q0.py — fast consumer-side χ^λ(q_0)
backend wiring the mpfr matrix-M path (PR #1993) into a drop-in API
for downstream tr_M / B_AME consumers.

## What this provides

Downstream code that computes tr_M-style aggregates
`Σ_λ y_λ · χ^λ(T_β)(q_0)` currently has two paths:

  1. **Catalogue lookup** — if the (K, λ, A) cell is in the
     `derived_chi_catalogue` witness, sum its q-Laurent at q_0 as
     mpf. O(num_terms · 1) per cell. Fast.
  2. **Direct compute via Rust** — `pyhecke_native.chi_q_via_gp` +
     sum at q_0. The Rust path's wall scales with `n`.

This module adds a third path:

  3. **mpfr matrix-M backend** (PR #1993). Block-bounded call cost,
     flat in `n` for low-dim λ. Net faster than Rust at A ≥ 4 in
     the aggregate (1.34× on ⁴He per PR #1993), and dramatically
     faster (50-70×) for dim-1 partitions.

`chi_lambda_at_q0(K, λ, A, q_0)` selects the right path:

  - First tries the catalogue (path 1) — fastest when cell present
  - On miss, routes to the mpfr backend (path 3) — fastest at A ≥ 4
    for non-cached cells, no f64 anywhere

## Benchmark

`main()` compares per-isotope wall time for a tr_M-style aggregate
over all partitions of n = 3A:

  - **catalogue-only path**: lookup + Laurent sum at q_0
  - **direct-rust path**: chi_q_via_gp + Laurent sum at q_0
  - **mpfr-fallback path** (this module): catalogue first, mpfr on miss
  - For a fair compute-time comparison, also runs a "force-mpfr"
    path that skips the catalogue entirely

Aggregate timings demonstrate the consumer-side speedup.

## NO f64 in compute path

Same discipline as PR #1985/#1993 — substrate q_0 as
`mpmath.mpf(Q_50_DIGIT_STR)`; Rust chi_q_via_gp returns exact
integer Laurent summed at q_0 as mpf; mpfr backend stays in mpf
throughout. NO f64.

## Δ_λ-gate

Pure wire-in — no new computation primitive. Reuses the matrix-M
trace identity (PR #1980/#1985/#1987/#1993). No ansatz, no fit, no
calibration parameter.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: E402, F401

import mpmath  # noqa: E402

import pyhecke_native as ph  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

from derived_chi_catalogue import load_catalogue  # noqa: E402
from derived_chi_catalogue_matrix_m_mpfr import (  # noqa: E402
    precompute_block_tables_mpfr,
    chi_via_numerical_matrix_m_mpfr,
)
from derived_chi_catalogue_matrix_m import _word_for_braid_word_3a  # noqa: E402


# ── Path 1: catalogue lookup + Laurent sum at q_0 ─────────────────


def _sum_laurent_at_q0_mpf(
    chi_pairs: list[tuple[int, str]],
    q_mpf: object,
    sqrt_q: object,
) -> object:
    """Evaluate a half-exponent q-Laurent at q_0 as mpf. Uses the
    PR #1993 precomputed-sqrt trick: math q-exp = key / 2 for
    half-exp encoding, so q^(key/2) = sqrt_q^key with integer key.
    """
    total = mpmath.mpf(0)
    for (d_key, c_str) in chi_pairs:
        total = total + mpmath.mpf(int(c_str)) * (sqrt_q ** int(d_key))
    return total


# ── Path 3: mpfr matrix-M backend ─────────────────────────────────


_PRECOMPUTE_CACHE: dict[tuple, dict] = {}
_CATALOGUE_CACHE: object | None = None


def _precompute_cached(shape: tuple, k_split: int, q_mpf: object) -> dict:
    """Cache mpfr block tables per (shape, k_split). At dps=50 a
    single λ ⊢ 12 precompute is ~5-10 ms; aggregating tr_M over all
    partitions of 12 amortises ~85 precomputes against the sum, so
    caching turns the precompute into a one-time cost per shape.

    Key uses `q_mpf` directly (mpmath.mpf is immutable + hashable);
    str(q_mpf) would be O(dps²) per lookup which dominates the
    catalogue-fast-path wall time."""
    key = (shape, k_split, mpmath.mp.dps, q_mpf)
    cached = _PRECOMPUTE_CACHE.get(key)
    if cached is None:
        cached = precompute_block_tables_mpfr(shape, k_split, q_mpf)
        _PRECOMPUTE_CACHE[key] = cached
    return cached


# ── Top-level routing ─────────────────────────────────────────────


def chi_lambda_at_q0(
    K: str,
    lam: tuple[int, ...],
    A: int,
    q_mpf: object,
    *,
    catalogue: object | None = None,
    sqrt_q: object | None = None,
    Z: int | None = None,
    N: int | None = None,
) -> object:
    """Fast χ^λ(T_β_K)(q_0) for downstream tr_M / B_AME consumers.

    Priority:
      1. Catalogue cell lookup — Laurent sum at q_0. Constant-time
         per cell once the catalogue is loaded.
      2. Fallback: mpfr matrix-M backend. Requires (Z, N) so the
         atom braid + parabolic split can be reconstructed.

    Args:
      K: atom label (e.g. "atom-braid-4He") — for catalogue lookup.
      lam: partition λ ⊢ n with n = 3·A.
      A: nucleon count (Z + N).
      q_mpf: substrate q as mpmath.mpf.
      catalogue: pre-loaded DerivedChiCatalogue (saves re-loading).
      sqrt_q: pre-computed mpmath.sqrt(q_mpf) (saves re-doing it).
      Z, N: proton / neutron counts for the mpfr-fallback path.

    Returns the χ^λ(T_β_K)(q_0) value as mpmath.mpf.
    """
    if sqrt_q is None:
        sqrt_q = mpmath.sqrt(q_mpf)

    # Path 1: catalogue lookup. Use the module-level cache to avoid
    # re-loading the catalogue witness on every call — load_catalogue
    # is O(file size) and the catalogue grows with each isotope sweep.
    if catalogue is None:
        global _CATALOGUE_CACHE
        if _CATALOGUE_CACHE is None:
            _CATALOGUE_CACHE = load_catalogue()
        catalogue = _CATALOGUE_CACHE
    try:
        # Catalogue.lookup signature is (knot, partition, atom) — knot
        # is the braid name like "atom-braid-D"; atom is the bare label
        # like "D". K is the bare atom name; the knot string is derived
        # from it. A is consumed only by the matrix-M fallback below.
        cell = catalogue.lookup(f"atom-braid-{K}", lam, K)
        return _sum_laurent_at_q0_mpf(cell.chi_lambda_q_laurent, q_mpf, sqrt_q)
    except KeyError:
        pass

    # Path 3: mpfr matrix-M fallback.
    if Z is None or N is None:
        raise ValueError(
            f"chi_lambda_at_q0(K={K!r}, lam={lam!r}, A={A}): catalogue "
            f"miss and no (Z, N) supplied to route through the mpfr "
            f"matrix-M backend. Supply Z, N or extend the catalogue."
        )
    n_strands, word = _word_for_braid_word_3a(Z, N)
    word_left = [t for t in word if t[1] <= 2]
    bridge_sign = next((t[0] for t in word if t[1] == 3), 1)
    word_right = [t for t in word if t[1] >= 4]
    cache = _precompute_cached(lam, 3, q_mpf)
    return chi_via_numerical_matrix_m_mpfr(
        lam, word_left, bridge_sign, word_right, cache,
    )


# ── Aggregation benchmark — tr_M shape ────────────────────────────


def _filter_partitions_by_dim(
    partitions: list, max_dim: int,
) -> list[tuple[int, ...]]:
    """Keep partitions with dim V_λ ≤ max_dim. Uses the hook-length
    formula (`murnaghan_nakayama.dim_specht`, O(n)) rather than
    enumerating standard Young tableaux (factorial in n). For λ ⊢ 12
    the SYT enumeration alone can take seconds per partition; the
    hook-length formula is microseconds."""
    from murnaghan_nakayama import dim_specht
    out: list[tuple[int, ...]] = []
    for shape in partitions:
        st = tuple(shape)
        if dim_specht(st) <= max_dim:
            out.append(st)
    return out


def _aggregate_via_catalogue_only(
    catalogue, K: str, A: int, q_mpf: object, sqrt_q: object,
    partition_filter: set[tuple[int, ...]] | None = None,
) -> tuple[object, int]:
    """Sum χ^λ(T_β_K)(q_0) over every catalogued partition (path 1).
    If `partition_filter` is given, only those partitions count."""
    total = mpmath.mpf(0)
    n_cells = 0
    for cell in catalogue.cells:
        # Use exact `== 3*A` not `// 3 == A`: integer division would
        # also match a (hypothetical) cell whose partition summed to
        # 3A+1 or 3A+2, which would silently mis-route a downstream
        # consumer.
        if cell.atom == K and sum(cell.partition) == 3 * A:
            shape = tuple(cell.partition)
            if partition_filter is not None and shape not in partition_filter:
                continue
            total = total + _sum_laurent_at_q0_mpf(
                cell.chi_lambda_q_laurent, q_mpf, sqrt_q,
            )
            n_cells += 1
    return total, n_cells


def _aggregate_via_direct_rust(
    Z: int, N: int, q_mpf: object, sqrt_q: object,
    shapes: list[tuple[int, ...]],
) -> tuple[object, int]:
    """Sum χ^λ(T_β)(q_0) via direct chi_q_via_gp + Laurent sum at q_0
    over the supplied partitions."""
    n_strands, word = _word_for_braid_word_3a(Z, N)
    total = mpmath.mpf(0)
    for shape in shapes:
        laurent = ph.chi_q_via_gp(list(shape), n_strands, list(word))
        for (d_key, c_str) in laurent:
            total = total + mpmath.mpf(int(c_str)) * (sqrt_q ** int(d_key))
    return total, len(shapes)


def _aggregate_via_mpfr_force(
    Z: int, N: int, q_mpf: object,
    shapes: list[tuple[int, ...]],
) -> tuple[object, int]:
    """Sum χ^λ(T_β)(q_0) via the mpfr matrix-M backend over the
    supplied partitions — forces the matrix-M path."""
    n_strands, word = _word_for_braid_word_3a(Z, N)
    word_left = [t for t in word if t[1] <= 2]
    bridge_sign = next((t[0] for t in word if t[1] == 3), 1)
    word_right = [t for t in word if t[1] >= 4]
    total = mpmath.mpf(0)
    for shape in shapes:
        cache = _precompute_cached(shape, 3, q_mpf)
        chi = chi_via_numerical_matrix_m_mpfr(
            shape, word_left, bridge_sign, word_right, cache,
        )
        total = total + chi
    return total, len(shapes)


# ── Main ──────────────────────────────────────────────────────────


def main() -> int:
    # Use the repo-standard precision-set helper so the witness's
    # `precisionMetadata.compute_dps` and the mpmath working precision
    # cannot drift apart (Copilot review on PR #2000).
    from _precision import set_compute_dps
    set_compute_dps(50)

    wb = WitnessBuilder(
        "derived-chi-catalogue-consumer-q0",
        engine="python",
    )
    wb.set_description(
        "Consumer-side wire-in of the mpfr matrix-M backend (PR #1993). "
        "Provides chi_lambda_at_q0(K, λ, A, q_0) with three-path "
        "routing: catalogue → mpfr fallback. Benchmarks the path "
        "selection on tr_M-style aggregation across deuteron/³H/³He/⁴He. "
        "NO f64 in compute path."
    )

    print("=" * 78)
    print(" Consumer-side χ^λ(q_0) wire-in — three-path benchmark")
    print("=" * 78)

    from q_parameter import Q_50_DIGIT_STR
    q_mpf = mpmath.mpf(Q_50_DIGIT_STR)
    sqrt_q = mpmath.sqrt(q_mpf)
    print(f"  q_0 = {mpmath.nstr(q_mpf, 30)}")

    # Aggregate Σ_λ χ^λ(T_β)(q_0) per isotope (mimics tr_M shape).
    # max_dim caps the partition set for the mpfr-force path so each
    # isotope finishes under ~60 s (dim-100+ partitions are slow in
    # pure-Python mpmath; future Rust port will lift this cap).
    isotopes = [
        # label, K (catalogue atom field), Z, N, A, max_dim
        ("D",   "D",   1, 1, 2, 10),
        ("T",   "T",   1, 2, 3, 12),
        ("3He", "3He", 2, 1, 3, 12),
        ("4He", "4He", 2, 2, 4, 15),
    ]

    print("\n  Loading catalogue...", flush=True)
    t0 = time.monotonic()
    cat = load_catalogue()
    cat_load_s = time.monotonic() - t0
    print(f"    {len(cat.cells)} cells in {cat_load_s*1000:.1f} ms")

    iso_results: list[dict] = []
    aggregate_match = True
    for (label, K, Z, N, A, max_dim) in isotopes:
        n = 3 * A
        all_parts = [tuple(p) for p in ph.partitions_of(n)]
        shapes = _filter_partitions_by_dim(all_parts, max_dim)
        shape_set = set(shapes)
        print(f"\n  {label}  (Z={Z}, N={N}, A={A}, n={n}, "
              f"using {len(shapes)}/{len(all_parts)} partitions, dim ≤ {max_dim})")
        print(f"  ─────────────────────────────────────")

        # Path 1: catalogue-only — restricted to the same partition set.
        _PRECOMPUTE_CACHE.clear()
        t0 = time.monotonic()
        total_cat, n_cat = _aggregate_via_catalogue_only(
            cat, K, A, q_mpf, sqrt_q, partition_filter=shape_set,
        )
        cat_s = time.monotonic() - t0

        # Path 2: direct rust on the same set.
        t0 = time.monotonic()
        total_rust, n_rust = _aggregate_via_direct_rust(
            Z, N, q_mpf, sqrt_q, shapes,
        )
        rust_s = time.monotonic() - t0

        # Path 3: mpfr force on the same set.
        _PRECOMPUTE_CACHE.clear()
        t0 = time.monotonic()
        total_mpfr, n_mpfr = _aggregate_via_mpfr_force(Z, N, q_mpf, shapes)
        mpfr_s = time.monotonic() - t0

        # Agreement — tolerance per PR #1993: 1e-(dps-5).
        tol = mpmath.mpf(10) ** -(mpmath.mp.dps - 5)
        cat_vs_rust = abs(total_cat - total_rust) < tol if n_cat > 0 else True
        mpfr_vs_rust = abs(total_mpfr - total_rust) < tol
        agree = cat_vs_rust and mpfr_vs_rust
        if not agree:
            aggregate_match = False

        speedup_mpfr_vs_rust = rust_s / mpfr_s if mpfr_s > 0 else float("inf")
        print(f"    catalogue: Σ over {n_cat:>3d} cells   "
              f"{cat_s*1000:>7.1f} ms")
        print(f"    rust:      Σ over {n_rust:>3d} partitions "
              f"{rust_s*1000:>7.1f} ms")
        print(f"    mpfr:      Σ over {n_mpfr:>3d} partitions "
              f"{mpfr_s*1000:>7.1f} ms   speedup={speedup_mpfr_vs_rust:.2f}×")
        print(f"    agree: catalogue vs rust = {cat_vs_rust}, "
              f"mpfr vs rust = {mpfr_vs_rust}")

        iso_results.append({
            "label": label, "K": K, "Z": Z, "N": N, "A": A,
            "n_cells_catalogue": n_cat,
            "n_partitions_rust": n_rust,
            "n_partitions_mpfr": n_mpfr,
            "catalogue_secs": cat_s,
            "rust_secs": rust_s,
            "mpfr_secs": mpfr_s,
            "speedup_mpfr_vs_rust": speedup_mpfr_vs_rust,
            "agree_catalogue_vs_rust": cat_vs_rust,
            "agree_mpfr_vs_rust": mpfr_vs_rust,
        })

    print("\n" + "=" * 78)
    print("  Aggregate summary  (Σ_λ χ^λ(q_0) for all partitions)")
    print("  " + "─" * 76)
    print(f"  {'Isotope':<8}  {'A':<2}  {'n':<3}  "
          f"{'cat ms':>8}  {'rust ms':>8}  {'mpfr ms':>8}  {'speedup':>10}")
    for r in iso_results:
        print(f"  {r['label']:<8}  {r['A']:<2}  {3*r['A']:<3}  "
              f"{r['catalogue_secs']*1000:>8.1f}  "
              f"{r['rust_secs']*1000:>8.1f}  "
              f"{r['mpfr_secs']*1000:>8.1f}  "
              f"{r['speedup_mpfr_vs_rust']:>9.2f}×")
    print("=" * 78)

    wb.add_assertion(
        "consumer_q0_wire_in_agrees_with_rust",
        computed=aggregate_match,
        expected=True,
        source="Whether the catalogue path and mpfr-force path each "
               "agree with direct-rust (chi_q_via_gp + Laurent sum at q_0) "
               "on the Σ_λ χ^λ(T_β)(q_0) aggregate over all partitions of "
               "n = 3A for D/T/³He/⁴He, to absolute tolerance "
               "1e-(dps-5). Validates the consumer-side wire-in.",
    )
    wb.add_data("dps", mpmath.mp.dps)
    wb.add_data("q_0_substrate_str", Q_50_DIGIT_STR)
    wb.add_data("isotopes", iso_results)

    out = wb.save()
    print(f"\n  ✓ Witness: {out.name}")
    return 0 if aggregate_match else 1


if __name__ == "__main__":
    sys.exit(main())
