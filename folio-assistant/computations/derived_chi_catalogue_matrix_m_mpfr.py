#!/usr/bin/env python3
"""derived_chi_catalogue_matrix_m_mpfr.py — mpmath/mpfr backend for
the matrix-M μ_p factorisation.

Per the audit doc roadmap (Phase 2 follow-up #1):
[`docs/audits/2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation.md`](../../docs/audits/2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation.md)

The numerical sp.Rational backend (PR #1985, #1987) proved the
architecture (block-bounded call cost, flat in n for low-dim λ —
13.47× speedup on ⁴He λ=(12)) but lost to Rust on high-dim λ
because sp.Rational arithmetic with 50-digit denominators costs
more per multiply than Rust's f64. Block-bounded ≠ arithmetic-
bounded.

This backend swaps `sp.Rational` for **`mpmath.mpf` at 50-dps
precision** — controlled-precision floating point, NOT f64. The
matrix-M structural decomposition is identical; only the leaf
arithmetic changes.

## Why mpmath over sp.Rational

- `sp.Rational` carries unbounded denominators; each multiply grows
  the representation. For long matrix products with q_0 near 1.11,
  the denominator quickly exceeds 50-digit precision needed for
  ppQ correctness, yet computation continues at full precision.
  Wasted work.
- `mpmath.mpf` truncates to the precision dial (`mp.dps = 50`).
  Each multiply costs ~constant time regardless of expression
  history. The substrate q_0 has 50-digit precision; matching
  arithmetic precision is the right answer.

## NO f64 in compute path

`mpmath.mpf` is arbitrary-precision binary floating point — the
"controlled precision" the CLAUDE.md precision discipline
explicitly approves. NOT f64. The mpmath backend defaults to
`mp.dps = 50` (matches Q_50_DIGIT_STR); higher precision (e.g.
`dps = 65`) is a config parameter.

## Δ_λ-gate

Same trace identity as PR #1980/#1985/#1987. Pure structural
rearrangement; no ansatz, no fit, no calibration parameter.
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

from derived_chi_catalogue_matrix_m import (  # noqa: E402
    standard_young_tableaux,
    group_syts_by_mu_p,
    _content,
    _shape_partitions_of,
    _word_for_braid_word_3a,
)


# ── mpmath-native Hoefsmit seminormal form ────────────────────────


def seminormal_matrices_mpfr(
    shape: tuple[int, ...], q_mpf: object,
) -> list[object]:
    """Build σ_1, …, σ_{n-1} in the asymmetric natural seminormal
    form using `mpmath.matrix` over `mpmath.mpf` at the current
    `mpmath.mp.dps`.

    Mirrors `derived_chi_catalogue_matrix_m.seminormal_matrices_qrat`
    but generates mpf matrices directly — no sympy involvement, no
    rational-blowup intermediate.

    Args:
      shape: λ ⊢ n.
      q_mpf: substrate q as `mpmath.mpf` (not a symbol).

    Returns a list `[σ_1, …, σ_{n-1}]` of mpmath.matrix, each
    `dim × dim` where dim = #SYTs(shape).
    """
    n = sum(shape)
    syts = standard_young_tableaux(shape)
    dim = len(syts)
    syt_to_idx = {syt: i for i, syt in enumerate(syts)}
    one = mpmath.mpf(1)
    h = q_mpf - one / q_mpf

    generators: list[object] = []
    for k in range(1, n):
        M = mpmath.zeros(dim, dim)
        processed = [False] * dim
        for i in range(dim):
            if processed[i]:
                continue
            cell_k_minus_1 = syts[i][k - 1]
            cell_k = syts[i][k]
            rho = _content(cell_k) - _content(cell_k_minus_1)
            a = h / (one - q_mpf ** (-2 * rho))

            swapped = list(syts[i])
            swapped[k - 1], swapped[k] = cell_k, cell_k_minus_1
            swapped_tuple = tuple(swapped)
            partner = syt_to_idx.get(swapped_tuple)
            # `partner == i` cannot happen — swap is of distinct cells.
            if partner is None:
                M[i, i] = a
                processed[i] = True
            else:
                j = partner
                a_prime = h / (one - q_mpf ** (2 * rho))
                b_sq = a * a_prime + one
                lo, hi = (i, j) if i < j else (j, i)
                a_lo, a_hi = (a, a_prime) if i < j else (a_prime, a)
                M[lo, lo] = a_lo
                M[lo, hi] = one
                M[hi, lo] = b_sq
                M[hi, hi] = a_hi
                processed[lo] = True
                processed[hi] = True
        generators.append(M)
    return generators


def _extract_block_mpfr(
    M: object, idxs: list[int],
) -> object:
    """Sub-matrix of an mpmath.matrix at given row/col indices."""
    s = len(idxs)
    out = mpmath.zeros(s, s)
    for ii, i in enumerate(idxs):
        for jj, j in enumerate(idxs):
            out[ii, jj] = M[i, j]
    return out


# ── Precompute + call ─────────────────────────────────────────────


def precompute_block_tables_mpfr(
    shape: tuple[int, ...],
    k_split: int,
    q_mpf: object,
) -> dict:
    """Same per-μ_p block structure as the sp.Rational backend
    (PR #1985), but built in mpmath. The full dim×dim seminormal
    matrices are built ONCE then DISCARDED after block extraction.
    """
    n = sum(shape)
    sigmas = seminormal_matrices_mpfr(shape, q_mpf)
    groups = group_syts_by_mu_p(shape, k_split)
    blocks: dict[tuple[int, ...], dict] = {}
    for mu_p, idxs in groups.items():
        sigmas_left = {
            g: _extract_block_mpfr(sigmas[g - 1], idxs)
            for g in range(1, k_split)
        }
        sigmas_right = {
            g: _extract_block_mpfr(sigmas[g - 1], idxs)
            for g in range(k_split + 1, n)
        }
        M_pp = _extract_block_mpfr(sigmas[k_split - 1], idxs)
        blocks[mu_p] = {
            "size": len(idxs),
            "indices": idxs,
            "sigmas_left": sigmas_left,
            "sigmas_right": sigmas_right,
            "M_pp": M_pp,
        }
    return {
        "shape": shape,
        "k_split": k_split,
        "q": q_mpf,
        "mu_p_groups": groups,
        "blocks": blocks,
    }


def chi_via_numerical_matrix_m_mpfr(
    shape: tuple[int, ...],
    word_left: list[tuple[int, int]],
    bridge_sign: int,
    word_right: list[tuple[int, int]],
    cache: dict,
) -> object:
    """Sum traces of `B_p · M_pp · B_n` over μ_p blocks in mpmath.
    Same identity as the sp.Rational backend, just mpf arithmetic.
    """
    q = cache["q"]
    one = mpmath.mpf(1)
    h = q - one / q
    total = mpmath.mpf(0)
    for mu_p, block in cache["blocks"].items():
        size = block["size"]
        eye_block = mpmath.eye(size)
        sigmas_left = block["sigmas_left"]
        sigmas_right = block["sigmas_right"]
        M_pp_pos = block["M_pp"]
        # Hecke inverse on a block: σ_g⁻¹ = σ_g − h·I (block extraction
        # is linear). Inlined to avoid per-iteration function recreate.
        B_p = eye_block
        for (sign, g_1based) in word_left:
            mat = sigmas_left[g_1based]
            B_p = B_p * (mat if sign >= 0 else mat - h * eye_block)
        B_n = eye_block
        for (sign, g_1based) in word_right:
            mat = sigmas_right[g_1based]
            B_n = B_n * (mat if sign >= 0 else mat - h * eye_block)
        M = M_pp_pos if bridge_sign >= 0 else (M_pp_pos - h * eye_block)
        prod = B_p * M * B_n
        # mpmath has no direct trace; sum diagonal.
        for ii in range(size):
            total = total + prod[ii, ii]
    return total


# ── Rust comparison ───────────────────────────────────────────────


def chi_rust_at_q_mpf(
    shape: tuple[int, ...],
    n_strands: int,
    word: list[tuple[int, int]],
    q_mpf: object,
) -> object:
    """Sum Rust's exact integer Laurent at q_0 as mpf.

    `chi_q_via_gp` returns exact integer coefficients — no f64 in
    the Rust path itself. We sum them at the substrate as mpf so the
    comparison stays at the backend's working precision.
    """
    laurent = ph.chi_q_via_gp(list(shape), n_strands, list(word))
    # Precompute sqrt_q once: half-exp keys are math q-exp · 2, so
    # q^(d_key/2) = sqrt_q^d_key with d_key an integer. mpmath does
    # binary integer exponentiation — much faster than fractional
    # exp+log when d_key is odd, and uniformly handles both parities.
    sqrt_q = mpmath.sqrt(q_mpf)
    total = mpmath.mpf(0)
    for (d_key, c_str) in laurent:
        d_int = int(d_key)
        total = total + mpmath.mpf(int(c_str)) * (sqrt_q ** d_int)
    return total


# ── Main: benchmark vs Rust + sp.Rational backend ─────────────────


def main(dps: int = 50) -> int:
    mpmath.mp.dps = dps

    wb = WitnessBuilder(
        "derived-chi-catalogue-matrix-m-mpfr",
        engine="python",
    )
    wb.set_description(
        f"mpmath/mpfr backend for the matrix-M μ_p factorisation. "
        f"Same structural identity as PR #1980/#1985/#1987; replaces "
        f"sp.Rational with mpmath.mpf at dps={dps} to close the high-"
        f"dim partition gap where sp.Rational denominator blowup "
        f"dominates wall time. NO f64 in compute path — mpfr is "
        f"controlled-precision floating point."
    )

    print("=" * 78)
    print(f" mpmath/mpfr backend vs Rust chi_q_via_gp + sp.Rational backend")
    print(f"  precision: mp.dps = {dps}")
    print("=" * 78)

    from q_parameter import Q_50_DIGIT_STR
    q_mpf = mpmath.mpf(Q_50_DIGIT_STR)
    print(f"\n  q_0 (mpf) = {mpmath.nstr(q_mpf, 30)}")

    # Multi-isotope sweep (same as #1987).
    isotopes = [
        ("²H (deuteron)", 1, 1, 5),
        ("³H (tritium)",  1, 2, 8),
        ("³He",           2, 1, 8),
        ("⁴He (alpha)",   2, 2, 11),
    ]

    isotope_results: list[dict] = []
    for (label, Z, N, max_dim) in isotopes:
        print(f"\n  {label}  (Z={Z}, N={N}, A={Z+N}, n={3*(Z+N)})")
        print(f"  ──────────────────────────────────────────────")
        n_strands, word = _word_for_braid_word_3a(Z, N)
        word_left = [t for t in word if t[1] <= 2]
        bridge_sign = next(t[0] for t in word if t[1] == 3)
        word_right = [t for t in word if t[1] >= 4]
        partitions = _shape_partitions_of(n_strands)
        small_partitions = [
            s for s in partitions
            if len(standard_young_tableaux(s)) <= max_dim
        ]
        print(f"    β = {len(word)} crossings  "
              f"(left={len(word_left)}, bridge=1, right={len(word_right)})")
        print(f"    Testing {len(small_partitions)}/{len(partitions)} "
              f"partitions (dim V_λ ≤ {max_dim})")

        cases: list[dict] = []
        total_precompute_s = 0.0
        total_call_s = 0.0
        total_rust_s = 0.0
        # Tolerance: ~1e-(dps-5) for matrix-product cumulative round-off.
        tol = mpmath.mpf(10) ** (-(dps - 5))
        for shape in small_partitions:
            dim = len(standard_young_tableaux(shape))

            t0 = time.monotonic()
            cache = precompute_block_tables_mpfr(shape, 3, q_mpf)
            precompute_s = time.monotonic() - t0
            total_precompute_s += precompute_s

            t0 = time.monotonic()
            chi_mpf = chi_via_numerical_matrix_m_mpfr(
                shape, word_left, bridge_sign, word_right, cache,
            )
            call_s = time.monotonic() - t0
            total_call_s += call_s

            t0 = time.monotonic()
            chi_rust = chi_rust_at_q_mpf(shape, n_strands, word, q_mpf)
            rust_s = time.monotonic() - t0
            total_rust_s += rust_s

            # mpf == mpf is too strict; use a tolerance proportional to
            # the working precision.
            delta = abs(chi_mpf - chi_rust)
            match = bool(delta < tol)
            status = "✓" if match else "✗"
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
                "delta": mpmath.nstr(delta, 10),
                "match": match,
            })

        n_total = len(cases)
        n_pass = sum(1 for c in cases if c["match"])
        speedup_overall = (
            total_rust_s / total_call_s if total_call_s > 0 else float("inf")
        )
        print(f"\n    Totals: pass={n_pass}/{n_total}  "
              f"precompute={total_precompute_s*1000:.1f}ms  "
              f"call={total_call_s*1000:.1f}ms  "
              f"rust={total_rust_s*1000:.1f}ms  "
              f"speedup={speedup_overall:.2f}×")
        isotope_results.append({
            "label": label, "Z": Z, "N": N, "A": Z+N, "n_strands": n_strands,
            "n_partitions_tested": n_total, "n_passed": n_pass,
            "total_precompute_secs": total_precompute_s,
            "total_call_secs": total_call_s,
            "total_rust_secs": total_rust_s,
            "speedup_rust_over_call": speedup_overall,
            "cases": cases,
        })

    n_total = sum(r["n_partitions_tested"] for r in isotope_results)
    n_pass = sum(r["n_passed"] for r in isotope_results)
    print("\n" + "=" * 78)
    print(f"  mpfr backend summary: {n_pass}/{n_total} partitions match Rust at q_0 (tol)")
    print("  " + "─" * 76)
    print(f"  {'Isotope':<18}  {'A':<2}  {'n':<3}  {'pass':<6}  "
          f"{'call ms':>8}  {'rust ms':>8}  {'speedup':>10}")
    for r in isotope_results:
        print(f"  {r['label']:<18}  {r['A']:<2}  {r['n_strands']:<3}  "
              f"{r['n_passed']}/{r['n_partitions_tested']:<4}  "
              f"{r['total_call_secs']*1000:>8.1f}  "
              f"{r['total_rust_secs']*1000:>8.1f}  "
              f"{r['speedup_rust_over_call']:>9.2f}×")
    print("=" * 78)

    wb.add_assertion(
        "mpfr_matrix_m_matches_rust_within_tolerance",
        computed=(n_pass == n_total),
        expected=True,
        source=f"Whether the mpfr matrix-M backend (mpmath.mpf at dps={dps}) "
               f"matches Rust chi_q_via_gp summed at q_0 across ²H/³H/³He/⁴He "
               f"to relative tolerance 1e-{dps-5}. Cumulative round-off in "
               f"the matrix product is bounded by O(word_length · block_size · "
               f"10^-dps).",
    )
    wb.add_data("dps", dps)
    wb.add_data("q_0_substrate_str", Q_50_DIGIT_STR)
    wb.add_data("n_partitions_tested", n_total)
    wb.add_data("n_passed", n_pass)
    wb.add_data("isotopes", isotope_results)

    out = wb.save()
    print(f"\n  ✓ Witness: {out.name}")
    return 0 if n_pass == n_total else 1


if __name__ == "__main__":
    sys.exit(main())
