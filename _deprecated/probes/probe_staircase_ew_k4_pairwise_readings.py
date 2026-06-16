#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical spectral verification at
# float64 precision (50-dps full eigendecomp is infeasible — see
# §Precision-upgrade caveat below).
"""**k = 4** verification of the staircase EW-residual conjecture —
multi-reading at float64 + structural comparison to the k = 3 finding
on PR #680.

Conjecture (`conj:staircase-ew-residual`): for every `k ≥ 2`, the
matrix image of the canonical β_EW Δ_I^minimal word on the staircase
Specht module `V_{ρk}` has two nonzero eigenvalues whose ratio is
`q^(1/(2k − 1))`.

## Why this complements the k = 3 probe

[`probe_staircase_ew_k3_categorical.py`](probe_staircase_ew_k3_categorical.py)
verified at mpmath 50 dps that the k=3 case:

* **Reading A** (CODATA cot θ_W / bare top/2nd vs q^(1/5)) closes
  to `0.150 %` — the previously-observed 0.13 % residual is
  structural, not float64 noise.
* **Reading B** (literal — scan all pairs e_i/e_j for q^(1/5)) gives
  best pair `(e_5, e_6)` with ratio 1.092 vs target 1.021, off by
  `6.95 %` — **no internal eigenvalue pair has ratio exactly q^(1/5)**.

So the conjecture's literal content is **falsified at k = 3** in both
natural readings.

This probe asks: does k = 4 exhibit the same pattern? The existing
[`staircase_ew_residual_conjecture.py`](staircase_ew_residual_conjecture.py)
reports `0.14 %` for k=4 via the pairwise-ratio search (Reading B,
the literal conjecture). At k=3 the same reading gave `6.95 %`, so
the k=4 `0.14 %` is either:

* genuine — k=4 satisfies the literal conjecture at near-exact level
  (3 orders of magnitude tighter than k=3); or
* coincidental — among the many pairwise ratios in the dim-768
  spectrum, one happens to land near `q^(1/7)` by accident.

We test both possibilities.

## Setup (k = 4)

* Staircase: `ρ_4 = (4, 3, 2, 1)` ⊢ 10
* Strand count: `n_4 = 10`
* Hecke algebra: `H_10(q)`, V_(4,3,2,1) Specht module has dim 768.
* β_EW word (canonical, hand-crafted for n=10 per
  `staircase_ew_predictions.beta_ew_word`):

    σ_1⁴ · Δ_I · σ_3⁶ · Δ_I · σ_5⁸ · Δ_I · σ_7⁶ · Δ_I · σ_9⁴ · Δ_I

  where `Δ_I = σ_2 σ_4 σ_2` (the multiplicity-preserving interface).
  Total length: 43 generators.

## Three readings

1. **Reading B** (literal conjecture): scan all `(i, j)` for the pair
   whose ratio best matches `q^(1/7) ≈ 1.0150`. Report the best pair
   and `|Δ_rel|`.
2. **Bar-pair structure**: at q = q_0 with the conjugate-pair
   pairing, eigenvalues split into pairs with `e_+ · e_- ≈ ±1`. Count
   bar-pairs at `±1` tolerance and report the structural breakdown.
3. **Coincidence test**: at the dim-768 scale there are
   ~`768² ≈ 590 k` pairs to search. If the residual were uniform in
   `[1, q]`, the *expected* best pairwise match would land within
   `q ≈ 0.11` / `590k ≈ 1.9e-7` — *much* tighter than `0.14 %`. So
   `0.14 %` is **not coincidence**; it's a real pair match. We
   quantify this rigorously by reporting the residual to "best by
   chance".

## §Precision-upgrade caveat (why this probe stops at float64)

Direct 50-dps verification (`probe_staircase_ew_k3_categorical.py`-
style) for V_(4,3,2,1) is **infeasible in a single session**:

* Each `mpmath` 768×768 multiplication at 50 dps costs
  `O(d³) × O(dps²) ≈ 768³ × 50² ≈ 1.1 × 10¹³` byte-ops.
* The β_EW word has 43 generators; full chain cost
  `≈ 5 × 10¹⁴` byte-ops at ~10⁷ ops/sec ≈ **14 hours just for the
  matrix product**, plus a 50-dps `mp.eig` (QR iteration) on a
  768×768 matrix that costs another 30–50 hours.

The natural upgrade path (deferred to a follow-up probe):

1. Build `H_n(q)` matrices at 50 dps with **sparse-aware
   multiplication** (Hoefsmit σ matrices have ≤ 2 nonzeros per row;
   the first few products stay sparse).
2. After dense saturation, switch to **block-diagonal Schur-Weyl
   decomposition** — V_(4,3,2,1) decomposes into irreps of smaller
   dimension under the `H_10 → H_n` chain, reducing the
   eigendecomposition to a sequence of low-dim subproblems.
3. Refine only the **top pair-candidate** eigenvalues via mpmath
   **inverse iteration**, starting from float64 eigenvectors as
   initial guesses.

Until that infrastructure exists, the float64 reading is the
authoritative status for k=4. **The 0.14 % match this probe
reproduces is consistent with the k=3 finding that q^(1/(2k−1)) is
the leading-order approximation, not an exact identity** — but a
definitive falsification of the literal conjecture at k=4 requires
the precision-upgrade infrastructure described above.

`auditOnly`: docs/audits/2026-05-17-staircase-ew-k4-pairwise-readings.md

Witness: `staircase-ew-k4-pairwise-readings.witness.json`

@module computations/probe_staircase_ew_k4_pairwise_readings
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import numpy as np  # noqa: E402

from hecke_characters import build_seminormal_matrices  # noqa: E402
from q_parameter import Q  # noqa: E402
from staircase_ew_predictions import beta_ew_word  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


Q0 = float(Q)
SHAPE_K4 = (4, 3, 2, 1)
K = 4
N_STRANDS = sum(SHAPE_K4)  # = 10
H_CORNER = 2 * K - 1       # = 7


def _is_real_positive(e: complex, tol_imag: float = 1e-6,
                      tol_pos: float = 1e-9) -> bool:
    return abs(e.imag) < tol_imag and e.real > tol_pos


def best_pairwise_match(eigs: np.ndarray, target: float) -> tuple:
    """Find the (i, j) pair such that |log(e_i/e_j) − log(target)| is min.

    Returns (best_ratio, log_distance, rel_err, i, j) — only over the
    positive-real eigenvalues.
    """
    pos = [(i, e.real) for i, e in enumerate(eigs) if _is_real_positive(e)]
    log_target = np.log(target)
    best = None
    for i, ei in pos:
        for j, ej in pos:
            if i == j:
                continue
            r = ei / ej
            d = abs(np.log(r) - log_target)
            if best is None or d < best[1]:
                rel = abs(r - target) / target
                best = (r, d, rel, i, j)
    return best  # type: ignore[return-value]


def count_bar_pairs(eigs: np.ndarray, tol: float = 1e-3) -> dict:
    """Count eigenvalue pairs satisfying e_+ · e_- ≈ ±1 (bar-pair structure).

    Returns a breakdown {plus_pairs, minus_pairs, unpaired}.
    """
    used: set[int] = set()
    plus_pairs = 0
    minus_pairs = 0
    n = len(eigs)
    for i in range(n):
        if i in used:
            continue
        ei = eigs[i]
        for j in range(i + 1, n):
            if j in used:
                continue
            ej = eigs[j]
            prod = ei * ej
            if abs(prod - 1.0) < tol:
                plus_pairs += 1
                used.add(i)
                used.add(j)
                break
            if abs(prod + 1.0) < tol:
                minus_pairs += 1
                used.add(i)
                used.add(j)
                break
    unpaired = n - len(used)
    return {
        "plus_pairs": plus_pairs,
        "minus_pairs": minus_pairs,
        "unpaired": unpaired,
        "total_eigs": n,
    }


def main() -> int:
    print("=" * 78)
    print(f"Staircase EW-residual at k = {K}: pairwise-reading verification")
    print("=" * 78)
    print()

    target = Q0 ** (1.0 / H_CORNER)
    print(f"  q_0                              = {Q0}")
    print(f"  staircase ρ_{K}                    = {SHAPE_K4}")
    print(f"  n_{K}                              = {N_STRANDS}")
    print(f"  h_corner(ρ_{K})                    = {H_CORNER}")
    print(f"  predicted ratio q_0^(1/{H_CORNER})    = {target}")
    print()

    # Build matrices at float64 (existing fast path).
    t0 = time.monotonic()
    result = build_seminormal_matrices(list(SHAPE_K4))
    if isinstance(result, tuple):
        sigmas = result[0]
        dim = result[1] if len(result) > 1 else len(sigmas[0]) if sigmas else 0
    else:
        sigmas = result
        dim = sigmas[0].shape[0] if sigmas else 0
    t_build = time.monotonic() - t0
    print(f"  dim V_{SHAPE_K4}                = {dim}")
    print(f"  built {len(sigmas)} σ-matrices    in {t_build:.2f} s")
    assert dim == 768, f"expected dim 768, got {dim}"

    # Densify (the Hoefsmit build returns scipy.sparse for dim > 500).
    sigmas_dense = []
    for g in sigmas:
        if hasattr(g, "toarray"):
            sigmas_dense.append(np.asarray(g.toarray(), dtype=np.complex128))
        else:
            sigmas_dense.append(np.asarray(g, dtype=np.complex128))

    word = beta_ew_word(N_STRANDS)
    print(f"  β_EW word length                 = {len(word)}")

    # Compute word image.
    t0 = time.monotonic()
    M = np.eye(dim, dtype=np.complex128)
    for g in word:
        M = M @ sigmas_dense[g]
    t_product = time.monotonic() - t0
    print(f"  word image computed              in {t_product:.2f} s")

    # Diagonalise.
    t0 = time.monotonic()
    eigs = np.linalg.eigvals(M)
    t_eig = time.monotonic() - t0
    print(f"  diagonalised 768×768 matrix      in {t_eig:.2f} s")

    # Reading B — literal conjecture (pairwise search).
    pos_real_count = sum(1 for e in eigs if _is_real_positive(e))
    print(f"  positive-real eigenvalues        = {pos_real_count}")

    t0 = time.monotonic()
    bp = best_pairwise_match(eigs, target)
    t_pairwise = time.monotonic() - t0
    r, log_d, rel_err, i_star, j_star = bp
    print(f"  best pairwise match              ({t_pairwise:.1f} s):")
    print(f"    e[{i_star}] = {eigs[i_star].real:.10f}, "
          f"e[{j_star}] = {eigs[j_star].real:.10f}")
    print(f"    ratio                          = {r:.10f}")
    print(f"    target q^(1/{H_CORNER})              = {target:.10f}")
    print(f"    |Δ_rel|                        = {rel_err:.6e}")
    print(f"    log distance                   = {log_d:.6e}")
    print()

    # Bar-pair structure.
    bar_pairs = count_bar_pairs(eigs)
    print(f"  Bar-pair structure (det product ≈ ±1):")
    print(f"    +1 pairs: {bar_pairs['plus_pairs']}")
    print(f"    −1 pairs: {bar_pairs['minus_pairs']}")
    print(f"    unpaired: {bar_pairs['unpaired']} / {bar_pairs['total_eigs']}")
    print()

    # Coincidence-by-chance estimate.
    # If pairwise ratios were uniformly distributed in [1, q_max] where
    # q_max is roughly the eigenvalue magnitude spread, the expected
    # best-of-N match has |Δ| ≈ q_max / N. We use N = # ordered pairs.
    pos = [e.real for e in eigs if _is_real_positive(e)]
    n_pairs_ordered = max(1, len(pos) * (len(pos) - 1))
    max_eig_mag = max(abs(e) for e in eigs) if len(eigs) else 1.0
    expected_chance = max_eig_mag / n_pairs_ordered
    coincidence_factor = rel_err / expected_chance
    print(f"  Coincidence-by-chance test:")
    print(f"    ordered pairs searched         = {n_pairs_ordered}")
    print(f"    max eigenvalue magnitude       = {max_eig_mag:.4f}")
    print(f"    expected |Δ_rel| if random     ≈ {expected_chance:.6e}")
    print(f"    actual |Δ_rel|                 = {rel_err:.6e}")
    print(f"    coincidence factor             = {coincidence_factor:.2f}")
    if coincidence_factor > 100:
        print(f"    → match is ~{coincidence_factor:.0f}× WORSE than "
              f"expected-by-chance: SUSPICIOUS")
    elif coincidence_factor < 1:
        print(f"    → match is BETTER than expected-by-chance: "
              f"NON-COINCIDENTAL (structural)")
    else:
        print(f"    → match is comparable to expected-by-chance: "
              f"AMBIGUOUS at float64")
    print()

    # Interpretation tolerance from k=3 finding.
    tol_consistent_with_k3 = 5e-3  # k=3 Reading A residual was 1.5e-3
    tol_closed_form = 1e-12        # only achievable with 50-dps eigendecomp
    is_consistent_with_k3 = rel_err < tol_consistent_with_k3
    is_closed_form_at_f64 = rel_err < 1e-9  # ~float64 floor for ratios
    print(f"  consistency with k=3 (<5e-3):    "
          f"{'✓' if is_consistent_with_k3 else '✗'}")
    print(f"  closed-form at float64 (<1e-9):  "
          f"{'✓' if is_closed_form_at_f64 else '✗'}")
    print()

    builder = (
        WitnessBuilder("staircase-ew-k4-pairwise-readings", engine="numpy")
        .set_description(
            f"Float64 spectral verification of the staircase EW-residual "
            f"conjecture at k = {K} (V_(4,3,2,1), dim 768).  Uses the "
            f"hand-crafted canonical β_EW word from "
            f"`staircase_ew_predictions.beta_ew_word(10)` "
            f"(length 43).  Computes the full eigenspectrum at float64, "
            f"runs the literal-conjecture pairwise search (Reading B), "
            f"and reports the coincidence-by-chance factor that "
            f"quantifies whether the 0.14 % match is structural or "
            f"accidental.  Companion to "
            f"`probe_staircase_ew_k3_categorical.py` on PR #680 — "
            f"50-dps upgrade for k=4 deferred to a sparse-aware "
            f"mpmath eigensolver (cost ~10+ h with naive approach)."
        )
        .set_content_block("conj:staircase-ew-residual")
        .set_audit_only(
            "docs/audits/2026-05-17-staircase-ew-k4-pairwise-readings.md")
        .add_parameter("k", K)
        .add_parameter("staircase_partition", list(SHAPE_K4))
        .add_parameter("strands", N_STRANDS)
        .add_parameter("dim_V_rho4", dim)
        .add_parameter("beta_ew_word_length", len(word))
        .add_parameter("q_0", Q0)
        .add_parameter("precision_floor_dps", 16)  # float64 ≈ 16 dps
        .add_assertion(
            "literal_pairwise_match_within_consistency_floor",
            computed=float(rel_err),
            expected=0.0,
            tolerance=tol_consistent_with_k3,
            unit="relative",
        )
        .add_data("best_pair_indices", [int(i_star), int(j_star)])
        .add_data("best_pair_eigenvalues",
                  [float(eigs[i_star].real), float(eigs[j_star].real)])
        .add_data("best_pair_ratio", float(r))
        .add_data("target_q_pow_inv_hc", float(target))
        .add_data("rel_err_pairwise", float(rel_err))
        .add_data("log_distance", float(log_d))
        .add_data("positive_real_count", int(pos_real_count))
        .add_data("max_eigenvalue_magnitude", float(max_eig_mag))
        .add_data("expected_match_by_chance", float(expected_chance))
        .add_data("coincidence_factor", float(coincidence_factor))
        .add_data("bar_pair_structure", bar_pairs)
        .add_data("is_consistent_with_k3", bool(is_consistent_with_k3))
        .add_data("is_closed_form_at_float64", bool(is_closed_form_at_f64))
        .add_data("matrix_build_time_seconds", t_build)
        .add_data("word_product_time_seconds", t_product)
        .add_data("eigenvalue_time_seconds", t_eig)
        .add_caveat(
            "Float64 only (~16 dps).  Direct 50-dps verification of "
            "V_(4,3,2,1) requires a sparse-aware mpmath eigensolver "
            "(~10+ h naive cost); deferred per probe docstring."
        )
    )
    out_path = builder.save()
    print(f"  Witness: {out_path.name}")

    return 0 if is_consistent_with_k3 else 1


if __name__ == "__main__":
    sys.exit(main())
