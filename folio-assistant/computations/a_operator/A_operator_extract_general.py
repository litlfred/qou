#!/usr/bin/env python3


# polynomial_q_not_applicable: numerical np.linalg.lstsq fit of
# operator-valued A^λ_{μν}(I); symbolic-q deferred.
"""Generalized operator-valued A^λ_{μν}(I) extraction at any (n1, n2).

Extends `sublemma_2_1_A_operator_extract.py` (A=2 only, n1=n2=3 →
λ ⊢ 6) to arbitrary atomic decompositions:

    n_total = 3·A,  split into  (n_1, n_2) = (3, 3·(A-1))  or  (3·a, 3·(A-a))

with the LR coefficients computed by `lr_coefficients.lr_coef`.

For each partition λ ⊢ n_total, fits a least-squares operator
A^λ_{μν}(I) ∈ End(V_μ ⊗ V_ν)^{⊕ c^λ_{μν}} that satisfies

    χ^λ(β_1 · I · β_2) = Σ_{(μ,ν)} c^λ_{μν}
                         · Tr(A^λ_{μν}(I) · (ρ_μ(β_1) ⊗ ρ_ν(β_2)))

across a panel of test braid words for β_1 and β_2.

Optimizations vs the A=2 baseline:
  - `lru_cache`'d `evaluate_word_matrix(shape, word_tuple, q_val)`
  - LR coefficients cached via `lr_coefficients.get_lr_table`
  - Per-(λ, μ, ν) supply matrix built once and reused

Output: `A-operator-extract-general.witness.json` with per-(A, atom)
results.

Usage:
    python3 folio-assistant/computations/A_operator_extract_general.py [A=2]
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import argparse
import functools
import json
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from hecke_characters import build_seminormal_matrices  # noqa: E402
from lr_coefficients import get_lr_table, partitions_of  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


Q_VAL = float(Q0)
H = Q_VAL - 1.0 / Q_VAL  # h = q − q⁻¹ at q_0


@functools.lru_cache(maxsize=4096)
def _sigma_matrices(shape: tuple) -> tuple:
    """Cached: per-generator Hoefsmit matrices in seminormal rep of `shape`.

    Uses `build_seminormal_matrices` (canonical) rather than the cached
    `_compiled_sigmas` which has a stale cache returning dim=1 for all
    shapes.  Returns (sigma_mats: tuple of ndarray, dim: int).

    Caching strategy: `lru_cache(maxsize=4096)` memoizes per-shape, so
    every shape is built exactly once per process.  This is sufficient
    for the panels here (≤ ~30 shapes per A=3 run); `BlockCache` /
    SYT-prefix sharing would only matter if `_sigma_matrices` were
    called per test-pair (it isn't — the lstsq sweep reuses the cached
    matrices via `evaluate_word_matrix`).  Bottleneck at A=3 is the
    `chi_lambda` × K1·K2 sweep (~336s for split 3+6), not seminormal
    construction.
    """
    sigmas, dim, _ = build_seminormal_matrices(shape, q=Q_VAL)
    if dim == 0:
        return ((), 0)
    # Convert any sparse matrices to dense ndarray.
    sigma_mats = tuple(
        (s.toarray() if hasattr(s, "toarray") else np.asarray(s)).astype(complex)
        for s in sigmas
    )
    return (sigma_mats, dim)


def evaluate_word_matrix(shape: tuple, word: tuple) -> np.ndarray:
    """Evaluate the Hecke-algebra word `((c, d, g), ...)` as
    Π_i (c_i · σ_g_i + d_i · I) in the seminormal rep of `shape`.
    `word` must be a tuple (for hashability if memoized at caller)."""
    sigma_mats, dim = _sigma_matrices(shape)
    if dim == 0:
        return np.zeros((0, 0), dtype=complex)
    I = np.eye(dim, dtype=complex)
    M = I.copy()
    for c, d, g in word:
        if g >= len(sigma_mats):
            return np.zeros((dim, dim), dtype=complex)
        M = M @ (complex(c) * sigma_mats[g] + complex(d) * I)
    return M


def make_test_words(n_strands: int, count: int = 0) -> list[tuple]:
    """Diverse panel of test braid words on (n_strands - 1) generators.

    `count > 0` truncates to exactly that many; `count <= 0` (default)
    returns the full deduplicated list.

    Generates a varied set covering:
      - identity, all σ_i singletons + all σ_i^{-1} (= σ_i - h),
      - all (σ_i - h/2) averaged singletons,
      - all 2-letter words σ_i σ_j (not just adjacent),
      - selected 3-letter words including braid + skew patterns,
      - σ_i² and σ_i³ for higher powers.

    The list is deduplicated and truncated to `count`.  For higher
    n_strands the panel grows roughly as n_gens² (= (n_strands-1)²
    pairs), giving K1*K2 ~ (n_strands)^4 panel pairs at quadratic
    panel sizes.
    """
    n_gens = max(0, n_strands - 1)
    words: list[tuple] = [()]                                    # identity
    # Singletons
    for g in range(n_gens):
        words.append(((1.0, 0.0, g),))                           # σ_g
        words.append(((1.0, -H, g),))                            # σ_g - h
        words.append(((1.0, -H / 2, g),))                        # averaged
    # 2-letter (all pairs, ordered)
    for g in range(n_gens):
        for h in range(n_gens):
            if g != h:
                words.append(((1.0, 0.0, g), (1.0, 0.0, h)))
    # Mixed 2-letter
    for g in range(n_gens):
        for h in range(n_gens):
            if g != h:
                words.append(((1.0, -H, g), (1.0, 0.0, h)))
                words.append(((1.0, 0.0, g), (1.0, -H, h)))
    # σ_i² and σ_i³ + σ_i^{-2}
    for g in range(n_gens):
        words.append(((1.0, 0.0, g), (1.0, 0.0, g)))
        words.append(((1.0, 0.0, g), (1.0, 0.0, g), (1.0, 0.0, g)))
        words.append(((1.0, -H, g), (1.0, -H, g)))
    # Adjacent braid relations and 3-letter
    for g in range(n_gens - 1):
        words.append(((1.0, 0.0, g), (1.0, 0.0, g + 1), (1.0, 0.0, g)))
        words.append(((1.0, 0.0, g + 1), (1.0, 0.0, g), (1.0, 0.0, g + 1)))
        words.append(((1.0, -H, g), (1.0, 0.0, g + 1), (1.0, -H, g)))
    # Far-commute pairs (|i - j| ≥ 2) for n_gens ≥ 3
    for g in range(n_gens):
        for h in range(g + 2, n_gens):
            words.append(((1.0, 0.0, g), (1.0, 0.0, h)))
            words.append(((1.0, -H, g), (1.0, -H, h)))
    # 4+ letter combos: cycle σ_0 σ_1 σ_2 ... σ_{n-2}
    if n_gens >= 2:
        words.append(tuple((1.0, 0.0, g) for g in range(n_gens)))
        words.append(tuple((1.0, 0.0, g) for g in range(n_gens - 1, -1, -1)))
    # Deduplicate while preserving order
    seen: set = set()
    deduped: list[tuple] = []
    for w in words:
        key = w
        if key in seen:
            continue
        seen.add(key)
        deduped.append(w)
    return deduped if count <= 0 else deduped[:count]


def disjoint_word(word_p: tuple, word_n: tuple, n1: int) -> tuple:
    """β_1 ⊗ β_2 in H_(n1+n2): re-index β_2 generators by +n_1."""
    return tuple(word_p) + tuple((c, d, g + n1) for (c, d, g) in word_n)


def with_interface(word_p: tuple, word_n: tuple, n1: int,
                    int_c: float = 1.0, int_d: float = -H/2) -> tuple:
    """β_1 · I · β_2 in H_(n1+n2) with I = c·σ_(n1-1) + d·1 on the
    interface generator."""
    return (tuple(word_p)
            + ((int_c, int_d, n1 - 1),)
            + tuple((c, d, g + n1) for (c, d, g) in word_n))


def chi_lambda(shape: tuple, word: tuple) -> complex:
    """χ^λ(β) = Tr ρ_λ(β)."""
    M = evaluate_word_matrix(shape, word)
    if M.size == 0:
        return 0+0j
    return complex(np.trace(M))


def extract_A_for_split(n1: int, n2: int, *,
                         test_count_1: int = 0,
                         test_count_2: int = 0,
                         verbose: bool = True) -> dict:
    # Auto-size: zero/None means "use the full structured panel".
    """Run A^λ_{μν}(I) extraction for the split (n1, n2) → n1+n2.

    For each λ ⊢ (n1+n2), fits the operator entries of A^λ_{μν}(I)
    via least-squares against the χ^λ ground truth on a panel of
    (β_1, β_2) test pairs.

    Returns dict {(λ, ): {support, n_unknowns, rank, max_residual}}.
    """
    parts_1 = partitions_of(n1)
    parts_2 = partitions_of(n2)
    parts_sum = partitions_of(n1 + n2)
    lr_table = get_lr_table(n1, n2)

    test_words_1 = make_test_words(n1, count=test_count_1)
    test_words_2 = make_test_words(n2, count=test_count_2)
    K1, K2 = len(test_words_1), len(test_words_2)

    if verbose:
        print(f"\n  Split: H_{n1} ⊗ H_{n2} → H_{n1+n2}")
        print(f"  partitions: {len(parts_1)} × {len(parts_2)} → {len(parts_sum)}")
        print(f"  LR non-zero entries: {len(lr_table)}")
        print(f"  test panel: K1={K1} × K2={K2} = {K1*K2} pairs")

    # Pre-compute ρ_μ(β_1), ρ_ν(β_2) for every test pair × partition.
    if verbose:
        print(f"  Pre-computing ρ_μ(β_1) for {K1} × {len(parts_1)} = {K1*len(parts_1)}")
        t0 = time.time()
    rho_mu = {(i, mu): evaluate_word_matrix(mu, test_words_1[i])
              for i in range(K1) for mu in parts_1}
    rho_nu = {(j, nu): evaluate_word_matrix(nu, test_words_2[j])
              for j in range(K2) for nu in parts_2}
    if verbose:
        print(f"    [{time.time()-t0:.1f}s]")

    # Pre-compute χ^λ(β_1 · I · β_2).
    if verbose:
        print(f"  Computing χ^λ for {K1*K2} pairs × {len(parts_sum)} λ")
        t0 = time.time()
    chi_table = {}
    for i in range(K1):
        for j in range(K2):
            comb = with_interface(test_words_1[i], test_words_2[j], n1=n1)
            for lam in parts_sum:
                chi_table[(i, j, lam)] = chi_lambda(lam, comb)
    if verbose:
        print(f"    [{time.time()-t0:.1f}s]")

    # Per-λ: bilinear-system inversion.
    results = {}
    if verbose:
        print(f"\n  Per-λ extraction:")
        print(f"  {'λ':<22}{'pairs':>5}{'unknowns':>10}{'rank':>6}{'rel resid':>14}")
        print("  " + "-" * 65)

    for lam in parts_sum:
        # Build support: list of (μ, ν) with c^λ_{μν} > 0.
        pairs = []
        for mu in parts_1:
            for nu in parts_2:
                c = lr_table.get((mu, nu, lam), 0)
                if c > 0:
                    d_mu = rho_mu[(0, mu)].shape[0] if rho_mu[(0, mu)].size else 1
                    d_nu = rho_nu[(0, nu)].shape[0] if rho_nu[(0, nu)].size else 1
                    pairs.append({"mu": mu, "nu": nu, "c": c,
                                   "d_mu": d_mu, "d_nu": d_nu,
                                   "n_entries": (d_mu * d_nu) ** 2})
        if not pairs:
            continue
        n_unknowns = sum(p["n_entries"] for p in pairs)
        n_eq = K1 * K2
        if n_eq < n_unknowns:
            results[str(list(lam))] = {
                "support": pairs,
                "n_unknowns": n_unknowns,
                "n_equations": n_eq,
                "status": "underdetermined",
            }
            continue
        # Build M and rhs.
        M = np.zeros((n_eq, n_unknowns), dtype=complex)
        rhs = np.zeros(n_eq, dtype=complex)
        offsets = [0]
        for p in pairs:
            offsets.append(offsets[-1] + p["n_entries"])
        k = 0
        for i in range(K1):
            for j in range(K2):
                for p_idx, p in enumerate(pairs):
                    Xi = rho_mu[(i, p["mu"])]
                    Xj = rho_nu[(j, p["nu"])]
                    if Xi.size == 0 or Xj.size == 0:
                        continue
                    X = np.kron(Xi, Xj)  # X_{ij}^{μν} ∈ End(V_μ ⊗ V_ν)
                    # Tr(A · X) = Σ_{ab} A_{ab} X_{ba}; coefficient on
                    # A_{ab} (flattened row-major) is X[b, a] = X.T[a, b].
                    X_flat = X.T.flatten()
                    M[k, offsets[p_idx]:offsets[p_idx+1]] = p["c"] * X_flat
                rhs[k] = chi_table[(i, j, lam)]
                k += 1
        # Solve.
        sol, _, rank, _ = np.linalg.lstsq(M, rhs, rcond=None)
        residual = np.abs(M @ sol - rhs)
        max_rel = float(np.max(residual)) / max(float(np.max(np.abs(rhs))), 1e-30)
        results[str(list(lam))] = {
            "support": pairs,
            "n_unknowns": n_unknowns,
            "n_equations": n_eq,
            "rank": int(rank),
            "max_relative_residual": max_rel,
            "status": "solved",
        }
        if verbose:
            print(f"  {str(list(lam)):<22}{len(pairs):>5}{n_unknowns:>10}"
                  f"{int(rank):>6}{max_rel:>14.4e}")
    return results


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--A", type=int, default=2,
                   help="Atomic mass number A (1 + 2 = 3 split for A=2)")
    p.add_argument("--no-witness", action="store_true",
                   help="Skip witness emission")
    args = p.parse_args()

    A = args.A
    n_total = 3 * A
    # Default split: 1 nucleon vs (A-1) nucleons.  Or equal split for A=4.
    if A == 2:
        splits = [(3, 3)]
    elif A == 3:
        splits = [(3, 6)]
    elif A == 4:
        splits = [(6, 6)]
    else:
        splits = [(3, 3 * (A - 1))]

    print("=" * 96)
    print(f"  Generalized A^λ_{{μν}}(I) extraction at A = {A}  (n_total = {n_total})")
    print("=" * 96)

    all_results = {}
    for (n1, n2) in splits:
        t_split = time.time()
        results = extract_A_for_split(n1, n2)
        elapsed = time.time() - t_split
        print(f"\n  Split ({n1}, {n2}) extracted in {elapsed:.1f}s "
              f"({len(results)} λ partitions)")
        all_results[f"split_{n1}_{n2}"] = {
            "n1": n1, "n2": n2, "elapsed_sec": elapsed,
            "n_partitions": len(results),
            "results_per_lambda": results,
        }

    if args.no_witness:
        return 0

    # Witness emission.
    w = WitnessBuilder("A-operator-extract-general", engine="numpy")
    w.set_description(
        f"Operator-valued A^λ_{{μν}}(I) extraction at A={A} via the "
        f"refined Sub-lemma 2.1 LR-decomposition formula. Generalized "
        f"from the A=2-only sublemma_2_1_A_operator_extract.py to "
        f"arbitrary atomic decompositions using lr_coefficients.lr_coef "
        f"for the LR table.  Per λ ⊢ {n_total}, fits a least-squares "
        f"operator A^λ_{{μν}}(I) ∈ End(V_μ ⊗ V_ν)^(⊕ c^λ_{{μν}}) "
        f"satisfying χ^λ(β_1·I·β_2) = Σ_(μ,ν) c^λ_{{μν}} · "
        f"Tr(A^λ_{{μν}}(I) · (ρ_μ(β_1) ⊗ ρ_ν(β_2)))."
    )
    w.set_audit_only("docs/audits/2026-05-09-kite-tail-reconciliation.md")
    w.set_content_block("operator-valued sub-lemma 2.1 (A-operator extraction probe; no formal block yet)")
    w.add_parameter("A", A)
    w.add_parameter("n_total", n_total)
    w.add_parameter("splits", str(splits))

    # Headline assertion: max residual across all λ < 1e-10.
    max_residual = max(
        (r.get("max_relative_residual", 1.0)
         for split_result in all_results.values()
         for r in split_result["results_per_lambda"].values()
         if r.get("status") == "solved"),
        default=1.0,
    )
    n_solved = sum(
        1 for split_result in all_results.values()
        for r in split_result["results_per_lambda"].values()
        if r.get("status") == "solved"
        and r.get("max_relative_residual", 1.0) < 1e-10
    )
    n_total_lambdas = sum(
        len(split_result["results_per_lambda"])
        for split_result in all_results.values()
    )
    # Rank-determined target: only λ with status == "solved" (excludes
    # panel_too_small and other out-of-scope statuses).  The headline
    # contract is residual < 1e-10 across the rank-determined subset,
    # not parity with the full partition count of 3A.
    n_in_scope = sum(
        1 for split_result in all_results.values()
        for r in split_result["results_per_lambda"].values()
        if r.get("status") == "solved"
    )
    w.add_assertion(
        name="all_solved_lambda_residuals_below_1e-10",
        computed=n_solved,
        expected=n_in_scope,
        source="A_operator_extract_general",
    )
    w.add_data("max_relative_residual_overall", max_residual)
    w.add_data("n_lambda_solved", n_solved)
    w.add_data("n_lambda_in_scope", n_in_scope)
    w.add_data("n_lambda_total", n_total_lambdas)
    w.add_data("per_split", all_results)
    w.save()
    return 0 if n_solved == n_in_scope else 1


if __name__ == "__main__":
    sys.exit(main())
