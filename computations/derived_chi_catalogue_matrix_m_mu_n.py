#!/usr/bin/env python3
"""derived_chi_catalogue_matrix_m_mu_n.py — Phase 1.3 PROTOTYPE.

Within each μ_p-block of V_λ (already extracted in PR #1985 / #2000
via `chi_lambda_via_mu_p_decomposition`), further decompose under
the right H_3(σ_4, σ_5) action via **q-Young symmetrizers** to
isolate the (μ_p, μ_n)-isotypics.

Per the audit doc
[`docs/audits/2026-06-08-matrix-m-optimization-A-8-9-path.md`](../../docs/audits/2026-06-08-matrix-m-optimization-A-8-9-path.md)
this is the critical enabling step for A=8, A=9 — it turns the
per-partition cost from `dim²(λ)` (~10⁹+ for ⁹Be) to
**bounded block² (≤ ~40²)** — taking ⁹Be from 8 years to minutes.

## q-Young symmetrizers (Hecke H_3(q))

For H_3(q) with relation `σ_i² = (q − q⁻¹) σ_i + 1`, the three
primitive idempotents projecting onto the irreps λ ⊢ 3 are
constructed from the q-deformed symmetrizers:

  y₊ = Σ_{w ∈ S₃} q^{ℓ(w)} T_w        →  projects onto V_(3) (trivial)
  y₋ = Σ_{w ∈ S₃} (−q⁻¹)^{ℓ(w)} T_w   →  projects onto V_(1,1,1) (sign)
  e₀ = I − e₊ − e₋                    →  projects onto V_(2,1)

with normalisation:

  e₊ = y₊ / [(1+q²)(1+q²+q⁴)]   (the scalar y₊ acts on V_(3))
  e₋ = y₋ · q⁶ / [(1+q²)(1+q²+q⁴)]

At substrate q_0 ≈ 1.11: `(1+q²)(1+q²+q⁴) ≈ 8.37`, well away from
zero. No numerical concerns.

## Verification — this prototype

For λ = (4, 2) ⊢ 6 (dim V_λ = 9), within the μ_p = (3) block of
size 5:
  - Build σ_4, σ_5 block-restricted matrices
  - Build T_w for w ∈ S_3, then y₊, y₋, e₀
  - Verify im(e_{μ_n}) dimension = c_LR · dim(V_μ_n)
  - Cross-check: Σ_{μ_n} c_LR · dim(V_μ_n) = block size

If validation passes, the (μ_p, μ_n) trace formula

    χ^λ(T_β) = Σ_{(μ_p, μ_n)} Tr [ B_p · M(μ_p, μ_n, λ) · B_n ]

becomes tractable per-block: each M is `c_LR · dim_p · dim_n` ≤ ~4
square instead of the current μ_p-block (size up to dim V_skew(λ/μ_p)).

## NO f64 in compute path

sympy symbolic q throughout for the prototype; mpfr wire-in follows.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: E402, F401

import sympy as sp  # noqa: E402

import pyhecke_native as ph  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

from derived_chi_catalogue_matrix_m import (  # noqa: E402
    seminormal_matrices_qrat,
    group_syts_by_mu_p,
    standard_young_tableaux,
)


# ── q-Young symmetrizers for H_3 ─────────────────────────────────


# All 6 elements of S_3 expressed as words in s_1, s_2 (1-based).
# Each entry is (length, sequence of generator indices in {1, 2}).
# Indices here are RELATIVE to a 2-generator H_3 — the caller maps
# them to the actual (σ_4, σ_5) or (σ_g, σ_{g+1}) generators of the
# right sub-algebra.
_S3_ELEMENTS: list[tuple[int, tuple[int, ...]]] = [
    (0, ()),
    (1, (1,)),
    (1, (2,)),
    (2, (1, 2)),
    (2, (2, 1)),
    (3, (1, 2, 1)),
]


def q_young_symmetrizer_matrix(
    mu_n: tuple[int, ...],
    sigma_g: sp.Matrix,
    sigma_g_plus_1: sp.Matrix,
    q: sp.Symbol,
) -> sp.Matrix:
    """Return the matrix e_{μ_n} (primitive idempotent of H_3) acting
    on the subspace where σ_g, σ_{g+1} are given.

    `sigma_g` and `sigma_g_plus_1` are the matrices of the two
    generators of the right H_3 sub-algebra restricted to U (typically
    a μ_p-block of V_λ).

    Returns the matrix of e_{μ_n} on U. For μ_n ∈ {(3), (2,1), (1,1,1)}:

      - μ_n = (3): trivial rep projector
      - μ_n = (1,1,1): sign rep projector
      - μ_n = (2,1): standard rep projector (computed as I - e₊ - e₋)
    """
    sigmas_by_idx = {1: sigma_g, 2: sigma_g_plus_1}
    dim = sigma_g.shape[0]
    eye = sp.eye(dim)
    # Build T_w for each w ∈ S_3 as a matrix product.
    T_w: list[sp.Matrix] = []
    for (length, seq) in _S3_ELEMENTS:
        mat = eye
        for idx in seq:
            mat = mat * sigmas_by_idx[idx]
        T_w.append(mat)
    # y_+ = Σ_w q^{ℓ(w)} T_w
    y_plus = sp.zeros(dim, dim)
    for (length, _), mat in zip(_S3_ELEMENTS, T_w):
        y_plus = y_plus + (q ** length) * mat
    # y_- = Σ_w (-q^{-1})^{ℓ(w)} T_w
    y_minus = sp.zeros(dim, dim)
    for (length, _), mat in zip(_S3_ELEMENTS, T_w):
        y_minus = y_minus + ((-1 / q) ** length) * mat
    # Normalisation scalar for both:
    #   y₊ acts as (1+q²)(1+q²+q⁴) on V_(3)
    #   y₋ acts as q^{-6}·(1+q²)(1+q²+q⁴) on V_(1,1,1)
    norm_scalar = sp.cancel((1 + q ** 2) * (1 + q ** 2 + q ** 4))
    e_plus = y_plus / norm_scalar
    e_minus = (y_minus * q ** 6) / norm_scalar
    if mu_n == (3,):
        return e_plus.applyfunc(sp.cancel)
    if mu_n == (1, 1, 1):
        return e_minus.applyfunc(sp.cancel)
    if mu_n == (2, 1):
        e_zero = eye - e_plus - e_minus
        return e_zero.applyfunc(sp.cancel)
    raise ValueError(f"mu_n must be one of (3,), (2,1), (1,1,1); got {mu_n!r}")


# ── (μ_p, μ_n)-block decomposition validation ────────────────────


def _matrix_rank(M: sp.Matrix) -> int:
    """Rank of a symbolic sympy matrix (uses .rank())."""
    return M.rank()


def decompose_mu_p_block_into_mu_n(
    shape: tuple[int, ...],
    mu_p: tuple[int, ...],
    k_split: int,
    q: sp.Symbol,
) -> dict:
    """For the μ_p-block of V_λ, decompose under H_3(right) via the
    q-Young symmetrizers and return per-(μ_n) image dimensions.

    Validates: dim(im e_{μ_n}) = c^λ_{μ_p, μ_n} · dim(V_{μ_p}) · dim(V_{μ_n})

    The dim(V_{μ_p}) factor enters because the H_3(left)-isotypic
    U_{μ_p} = V_{μ_p} ⊗ V_skew(λ/μ_p); the right-H_3 symmetrizer acts
    trivially on the V_{μ_p} factor and projects only V_skew.

    Returns dict mapping μ_n → {im_dim, c_LR, dim_V_mu_p, dim_V_mu_n,
    expected_dim, match}.
    """
    n = sum(shape)
    # We need σ_{k_split+1} and σ_{k_split+2} for the right-H_3 action,
    # so n must be ≥ k_split + 3 (else sigmas[k_split + 1] is out of
    # range). For k_split=3 (deuteron split), this means n ≥ 6.
    if n < k_split + 3:
        raise ValueError(
            f"shape={shape!r} (sum {n}) too small for right-H_3 split at "
            f"k_split={k_split}: need n ≥ k_split + 3 = {k_split + 3} so "
            f"σ_{k_split+1}, σ_{k_split+2} both exist as generators."
        )
    sigmas = seminormal_matrices_qrat(shape, q)
    groups = group_syts_by_mu_p(shape, k_split)
    if mu_p not in groups:
        raise ValueError(
            f"μ_p={mu_p!r} not present in λ={shape!r} grouping at "
            f"k_split={k_split} (groups: {sorted(groups.keys())})"
        )
    idxs = groups[mu_p]
    block_size = len(idxs)
    # σ_{k_split+1} and σ_{k_split+2} = first two generators of H_3(right).
    sigma_g_full = sigmas[k_split]          # σ_{k_split+1}
    sigma_g_plus_1_full = sigmas[k_split + 1]  # σ_{k_split+2}
    sigma_g = sigma_g_full.extract(idxs, idxs)
    sigma_g_plus_1 = sigma_g_plus_1_full.extract(idxs, idxs)

    results: dict[tuple[int, ...], dict] = {}
    H3_PARTITIONS = [(3,), (2, 1), (1, 1, 1)]
    H3_DIMS = {(3,): 1, (2, 1): 2, (1, 1, 1): 1}
    # The H_3(left)-isotypic U_{μ_p} = V_{μ_p} ⊗ V_skew(λ/μ_p) (where
    # V_skew = ⊕_{μ_n} c_LR · V_{μ_n}). The right-H_3 q-Young
    # symmetrizer e_{μ_n} acts trivially on the V_{μ_p} factor, so its
    # image has dimension dim(V_{μ_p}) · c_LR · dim(V_{μ_n}).
    dim_V_mu_p = H3_DIMS[mu_p]
    for mu_n in H3_PARTITIONS:
        e = q_young_symmetrizer_matrix(mu_n, sigma_g, sigma_g_plus_1, q)
        im_dim = _matrix_rank(e)
        c_LR = ph.lr_coefficient(list(shape), list(mu_p), list(mu_n))
        expected = c_LR * dim_V_mu_p * H3_DIMS[mu_n]
        results[mu_n] = {
            "im_dim": im_dim,
            "c_LR": c_LR,
            "dim_V_mu_p": dim_V_mu_p,
            "dim_V_mu_n": H3_DIMS[mu_n],
            "expected_dim": expected,
            "match": im_dim == expected,
        }
    sum_expected = sum(r["expected_dim"] for r in results.values())
    sum_computed = sum(r["im_dim"] for r in results.values())
    # Strict validation: each per-μ_n match must hold (computed rank
    # equals LR-predicted dim) AND the computed ranks sum to the block
    # size. The previous formulation only checked the LR-predicted dim
    # summed correctly, which doesn't actually use the q-Young
    # symmetrizers at all.
    all_per_mu_n_match = all(r["match"] for r in results.values())
    block_decomposition_correct = (
        all_per_mu_n_match
        and sum_computed == block_size
        and sum_expected == block_size
    )
    return {
        "shape": shape,
        "mu_p": mu_p,
        "block_size": block_size,
        "sum_expected_dim": sum_expected,
        "sum_computed_dim": sum_computed,
        "block_decomposition_correct": block_decomposition_correct,
        "by_mu_n": results,
    }


# ── Main: prototype validation on small λ ────────────────────────


def main() -> int:
    import time
    t0 = time.monotonic()
    wb = WitnessBuilder(
        "derived-chi-catalogue-matrix-m-mu-n-prototype",
        engine="python",
        start_time=t0,
    )
    wb.set_description(
        "Phase 1.3 prototype: (μ_p, μ_n)-block extraction via q-Young "
        "symmetrizers for H_3(q). Validates that the per-block image "
        "rank matches the LR-predicted dimension c^λ_{μ_p, μ_n} · "
        "dim(V_{μ_p}) · dim(V_{μ_n}) for each μ_p of λ ⊢ 6. NO f64 "
        "in compute path (symbolic sympy q throughout)."
    )
    print("=" * 78)
    print(" Phase 1.3 prototype — (μ_p, μ_n)-block extraction via q-Young symmetrizers")
    print("=" * 78)

    q = sp.Symbol("q", positive=True)

    # Test cases: a handful of λ ⊢ 6 (deuteron) with each μ_p ∈ {(3), (2,1), (1,1,1)}
    test_shapes = [(6,), (4, 2), (3, 2, 1), (2, 2, 2), (1, 1, 1, 1, 1, 1)]
    k_split = 3
    n_pass = 0
    n_fail = 0
    n_total = 0
    per_block_records: list[dict] = []
    for shape in test_shapes:
        print(f"\n  λ = {shape}   (dim V_λ = {len(standard_young_tableaux(shape))})")
        groups = group_syts_by_mu_p(shape, k_split)
        for mu_p in sorted(groups.keys()):
            n_total += 1
            try:
                report = decompose_mu_p_block_into_mu_n(shape, mu_p, k_split, q)
            except Exception as exc:  # noqa: BLE001
                print(f"    μ_p={mu_p}: ERROR  {type(exc).__name__}: {exc}")
                n_fail += 1
                continue
            ok = report["block_decomposition_correct"]
            n_pass += 1 if ok else 0
            n_fail += 0 if ok else 1
            status = "✓" if ok else "✗"
            print(f"    {status} μ_p={mu_p!s:>10}  block_size={report['block_size']:>2}  "
                  f"sum_dims={report['sum_expected_dim']:>2}")
            for mu_n, r in report["by_mu_n"].items():
                tick = "✓" if r["match"] else "✗"
                print(f"        μ_n={mu_n!s:>10}  c_LR={r['c_LR']:>2}  "
                      f"dim_V_μ_n={r['dim_V_mu_n']}  "
                      f"expected={r['expected_dim']}  "
                      f"im(e)={r['im_dim']}  {tick}")
            # Convert tuple-keyed dicts to lists for JSON-serialisable witness.
            per_block_records.append({
                "shape": list(shape),
                "mu_p": list(mu_p),
                "block_size": report["block_size"],
                "sum_expected_dim": report["sum_expected_dim"],
                "sum_computed_dim": report["sum_computed_dim"],
                "block_decomposition_correct": ok,
                "by_mu_n": [
                    {
                        "mu_n": list(mu_n),
                        "c_LR": r["c_LR"],
                        "dim_V_mu_p": r["dim_V_mu_p"],
                        "dim_V_mu_n": r["dim_V_mu_n"],
                        "expected_dim": r["expected_dim"],
                        "im_dim": r["im_dim"],
                        "match": r["match"],
                    }
                    for mu_n, r in report["by_mu_n"].items()
                ],
            })

    print(f"\n  ── Summary ──")
    print(f"    Total μ_p blocks tested: {n_total}")
    print(f"    Block decomposition correct: {n_pass}")
    print(f"    Failed: {n_fail}")
    wb.add_assertion(
        "all_mu_p_blocks_decompose_via_q_young_symmetrizers",
        computed=(n_fail == 0 and n_pass == n_total and n_total > 0),
        expected=True,
        source="Whether every μ_p-block of every test λ ⊢ 6 decomposes "
               "into (μ_p, μ_n)-isotypics via the q-Young symmetrizers, "
               "with the per-projector image rank matching the "
               "Littlewood-Richardson prediction c^λ_{μ_p, μ_n} · "
               "dim(V_{μ_p}) · dim(V_{μ_n}) AND the ranks summing to "
               "the block size.",
    )
    wb.add_data("n_blocks_tested", n_total)
    wb.add_data("n_pass", n_pass)
    wb.add_data("n_fail", n_fail)
    wb.add_data("per_block", per_block_records)
    out = wb.save()
    print(f"\n  ✓ Witness: {out.name}")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
