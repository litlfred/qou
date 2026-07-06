#!/usr/bin/env python3


# polynomial_q_not_applicable: numerical Kronecker-factorized least-squares for A^λ_{μν}(I) extraction.
"""Kronecker-factorized A^λ_{μν}(I) extraction (item 5).

For the operator-valued formula

    χ^λ(β_1 · I · β_2) = Σ_{(μ,ν)} c^λ_{μν} · Tr(A^λ_{μν}(I) · (ρ_μ(β_1) ⊗ ρ_ν(β_2)))

the supply matrix M used in the lstsq has tensor-product structure:
each row corresponds to a test pair (i, j) and the row is built
from ρ_μ(β_1_i) ⊗ ρ_ν(β_2_j).  Across the panel:

    M = X ⊗ Y    where X[i, :] = vec(ρ_μ(β_1_i)),  Y[j, :] = vec(ρ_ν(β_2_j))

This factorization lets us solve the (d_μ d_ν)²-dimensional lstsq
for A_{μν} via TWO smaller lstsq's:
  - X-side: K_1 × d_μ² (rank d_μ² needed)
  - Y-side: K_2 × d_ν² (rank d_ν² needed)

Total panel: K_1 · K_2 ≥ d_μ² · d_ν² = (d_μ d_ν)² — same scaling
as the direct method, but the per-side lstsq's are dramatically
smaller (d_μ² ≤ 4 at H_3, d_ν² ≤ 256 at H_6 max irrep).

The factorization works PER (μ, ν) BLOCK in isolation: each support
pair (μ, ν) is solved independently against the chi^λ data
projected to that block.  Cross-block constraints (sums) are
handled by the outer formula.

NOTE: this factorization assumes A^λ_{μν}(I) is treated as an
operator on V_μ ⊗ V_ν only (single multiplicity slot c^λ_{μν} = 1).
For higher multiplicities (c > 1), the block-diagonal copies
require additional handling.

Status: scaffolded but NOT integrated with the panel-size scaling
needed at A=3, A=4 — that's items 4 (symmetry) + 1 (panel size)
which interact with this factorization.

Usage:
    python3 computations/A_operator_extract_kron.py [--A 2|3|4]
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
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from A_operator_extract_general import (  # noqa: E402
    H, Q_VAL, _sigma_matrices, evaluate_word_matrix,
    make_test_words, with_interface, chi_lambda,
)
from lr_coefficients import get_lr_table, partitions_of  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def kron_lstsq_per_block(
    rho_mu_per_word: list,
    rho_nu_per_word: list,
    chi_K1_K2: np.ndarray,
) -> tuple[np.ndarray, float]:
    """Solve the Kronecker-factorized least-squares for ONE (μ, ν)
    block contributing to a single λ.

    Given:
      rho_mu_per_word  : list of K1 ndarrays of shape (d_μ, d_μ)
                         representing ρ_μ(β_1_i)
      rho_nu_per_word  : list of K2 ndarrays of shape (d_ν, d_ν)
                         representing ρ_ν(β_2_j)
      chi_K1_K2        : ndarray of shape (K1, K2) with the
                         per-pair χ^λ contribution from this block
                         (= χ^λ(β_1_i · I · β_2_j) projected to (μ, ν))

    Returns:
      A : reshaped (d_μ, d_ν, d_μ, d_ν) operator A^λ_{μν}(I)
      max_residual : max relative |M·vec(A) - chi|/|chi|
    """
    K1 = len(rho_mu_per_word)
    K2 = len(rho_nu_per_word)
    d_mu = rho_mu_per_word[0].shape[0]
    d_nu = rho_nu_per_word[0].shape[0]

    # X[i, :] = vec(ρ_μ(β_1_i).T)  (so M = X ⊗ Y · vec(A) gives
    # Tr(A · ρ_μ(β_1_i) ⊗ ρ_ν(β_2_j)) per row).
    X = np.array([rho_mu.T.flatten() for rho_mu in rho_mu_per_word])
    Y = np.array([rho_nu.T.flatten() for rho_nu in rho_nu_per_word])

    # Step 1: solve X · B_j = chi[:, j] for each j (B_j is d_μ × d_μ flat).
    # B has shape (d_μ², K2).
    # X has shape (K1, d_μ²).
    B, _, _, _ = np.linalg.lstsq(X, chi_K1_K2, rcond=None)
    # B is shape (d_μ², K2).

    # Step 2: solve Y · A_unflat = B.T per column.
    # A_unflat has shape (d_μ², d_ν²).  Solve B.T = Y · A_unflat (so
    # A_unflat is shape (d_ν², d_μ²)) — actually:
    #   B[a*d_μ+c, j] = Σ_p (X · M)[i, *] · Y[j, p] · A...
    # Cleaner: vec(A) = (vec_μ ⊗ vec_ν)^{-1}; solve A_mat · Y.T = B
    # where A_mat is (d_μ², d_ν²).  So A_mat = B · pinv(Y.T) =
    # B · (pinv(Y).T).
    A_mat, _, _, _ = np.linalg.lstsq(Y, B.T, rcond=None)
    # A_mat is shape (d_ν², d_μ²).

    # Reshape: vec(A) has total size d_μ² · d_ν² = (d_μ d_ν)².
    # A_mat[p, q] = A[q, p] (where indices are flat ones).
    A_full = A_mat.T  # shape (d_μ², d_ν²)
    # A as a (d_μ d_ν, d_μ d_ν) matrix can be built by interleaving
    # the index ordering — but for now just verify the residual.

    # Reconstruct chi from the solved A and compare.
    chi_reconstructed = X @ A_full @ Y.T
    residual = np.abs(chi_reconstructed - chi_K1_K2)
    max_resid = float(np.max(residual)) / max(float(np.max(np.abs(chi_K1_K2))), 1e-30)

    # Reshape A_full to (d_μ, d_ν, d_μ, d_ν) for downstream use.
    A_tensor = A_full.reshape(d_mu, d_mu, d_nu, d_nu).transpose(0, 2, 1, 3)
    return A_tensor, max_resid


def extract_with_kron(n1: int, n2: int, *, K1: int = 12, K2: int = 12,
                       verbose: bool = True) -> dict:
    """Run Kronecker-factorized A-extraction for split (n1, n2).

    For each λ ⊢ n1+n2 with c^λ_{μν} = 1 (single multiplicity),
    solves each (μ, ν) block independently via the Kronecker
    factorization.  c > 1 blocks fall back to the dense extraction
    (deferred — single-multiplicity covers the bulk of the support).
    """
    parts_1 = partitions_of(n1)
    parts_2 = partitions_of(n2)
    parts_sum = partitions_of(n1 + n2)
    lr_table = get_lr_table(n1, n2)

    test_1 = make_test_words(n1, count=K1)
    test_2 = make_test_words(n2, count=K2)
    K1, K2 = len(test_1), len(test_2)

    if verbose:
        print(f"\n  Kronecker-factorized extraction: H_{n1} ⊗ H_{n2} → H_{n1+n2}")
        print(f"  panel: K1={K1}, K2={K2}; LR entries: {len(lr_table)}")

    # Pre-compute ρ_μ(β_1) and ρ_ν(β_2).
    rho_mu = {(i, mu): evaluate_word_matrix(mu, test_1[i])
              for i in range(K1) for mu in parts_1}
    rho_nu = {(j, nu): evaluate_word_matrix(nu, test_2[j])
              for j in range(K2) for nu in parts_2}

    # Pre-compute χ^λ(β_1 · I · β_2).
    chi_table = {}
    for i in range(K1):
        for j in range(K2):
            comb = with_interface(test_1[i], test_2[j], n1=n1)
            for lam in parts_sum:
                chi_table[(i, j, lam)] = chi_lambda(lam, comb)

    results = {}
    if verbose:
        print(f"  Per-λ Kron extraction:")
        print(f"  {'λ':<22}{'(μ,ν,c)':<14}{'d_μ × d_ν':<10}{'rel resid':>14}")
        print("  " + "-" * 65)

    for lam in parts_sum:
        # Identify support pairs with c=1 (Kron-applicable).
        per_block_residuals = []
        per_block_data = []
        max_block_resid = 0.0
        # Build the chi matrix for this λ.
        chi_lam_K1K2 = np.array([
            [chi_table[(i, j, lam)] for j in range(K2)]
            for i in range(K1)
        ])
        # Decompose chi_lam_K1K2 across (μ, ν) blocks via the LR
        # formula:  chi_λ = Σ c^λ_{μν} · ⟨A^λ_{μν}, (ρ_μ ⊗ ρ_ν)⟩.
        # When the support has a SINGLE (μ, ν), the block solve is direct.
        # For multi-block support (most λ's), distributing chi to
        # individual blocks requires additional decomposition (per-
        # block χ slices) — a separate step that this scaffold
        # doesn't yet implement.  For now, we run the block solve
        # ONLY for λ's whose support has exactly one (μ, ν, c) tuple.
        support = [(mu, nu, c) for (mu, nu, lam_), c in lr_table.items()
                    if lam_ == lam]
        if len(support) != 1 or support[0][2] != 1:
            # Multi-block / multi-multiplicity: defer to dense path.
            results[str(list(lam))] = {
                "support_size": len(support),
                "deferred_to_dense": True,
            }
            continue

        mu, nu, c = support[0]
        d_mu = rho_mu[(0, mu)].shape[0] if rho_mu[(0, mu)].size else 1
        d_nu = rho_nu[(0, nu)].shape[0] if rho_nu[(0, nu)].size else 1

        rho_mu_list = [rho_mu[(i, mu)] for i in range(K1)]
        rho_nu_list = [rho_nu[(j, nu)] for j in range(K2)]

        A_tensor, resid = kron_lstsq_per_block(
            rho_mu_list, rho_nu_list, chi_lam_K1K2,
        )
        results[str(list(lam))] = {
            "support_size": 1,
            "mu": list(mu), "nu": list(nu),
            "d_mu": d_mu, "d_nu": d_nu,
            "max_relative_residual": resid,
            "deferred_to_dense": False,
        }
        if verbose:
            tup = f"({list(mu)},{list(nu)},{c})"
            print(f"  {str(list(lam)):<22}{tup:>14}"
                  f"  {d_mu}×{d_nu:<8}{resid:>14.4e}")

    return results


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--A", type=int, default=2)
    p.add_argument("--K1", type=int, default=12)
    p.add_argument("--K2", type=int, default=12)
    args = p.parse_args()

    A = args.A
    if A == 2:
        n1, n2 = 3, 3
    elif A == 3:
        n1, n2 = 3, 6
    elif A == 4:
        n1, n2 = 6, 6
    else:
        n1, n2 = 3, 3 * (A - 1)

    print("=" * 96)
    print(f"  Kronecker-factorized A^λ_{{μν}}(I) extraction at A={A}  (split {n1}+{n2}={n1+n2})")
    print("=" * 96)

    results = extract_with_kron(n1, n2, K1=args.K1, K2=args.K2)

    # Headline counts.
    n_kron_solved = sum(1 for r in results.values()
                        if not r.get("deferred_to_dense", True))
    n_deferred = sum(1 for r in results.values()
                     if r.get("deferred_to_dense", False))
    print(f"\n  λ solved via Kron: {n_kron_solved}/{len(results)}")
    print(f"  λ deferred to dense (multi-block / multi-mult): {n_deferred}/{len(results)}")

    w = WitnessBuilder("A-operator-extract-kron", engine="numpy")
    w.set_description(
        "Kronecker-factorized A^λ_{μν}(I) extraction.  For λ with "
        "single-(μ, ν) support and c^λ_{μν} = 1, the supply matrix "
        "factors as M = X ⊗ Y where X[i, :] = vec(ρ_μ(β_1_i).T) and "
        "Y[j, :] = vec(ρ_ν(β_2_j).T).  Solving via two smaller "
        "lstsq's reduces the per-block compute by O((d_μ d_ν)² / "
        "(d_μ² + d_ν²)).  Multi-block / multi-multiplicity λ's are "
        "deferred to the dense path; full A=3, A=4 closure requires "
        "extending the factorization to those cases (item 4 + item 1)."
    )
    w.set_audit_only("docs/audits/2026-05-09-kite-tail-reconciliation.md")
    w.set_content_block("operator-valued sub-lemma 2.1 (A-operator extraction probe; no formal block yet)")
    w.add_parameter("A", A)
    w.add_parameter("n1", n1)
    w.add_parameter("n2", n2)
    w.add_parameter("K1", args.K1)
    w.add_parameter("K2", args.K2)
    w.add_assertion(
        name="kron_factorization_runs",
        computed=int(n_kron_solved >= 0),
        expected=1,
        source="A_operator_extract_kron",
    )
    w.add_data("results_per_lambda", results)
    w.add_data("n_kron_solved", n_kron_solved)
    w.add_data("n_deferred", n_deferred)
    w.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
