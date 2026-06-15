#!/usr/bin/env python3


# polynomial_q_not_applicable: numerical lstsq in the SVD-reduced rank basis.
"""Direct A^λ_{μν}(I) extraction in the SVD-reduced rank basis (item 3).

The supply matrix M for each λ has structural rank << ambient
n_unknowns (per `A_operator_rank_probe.py` — 0.135 compression
at A=3).  Instead of fitting the full ambient parameter, this
script:

  1. Builds M (interface-independent — depends only on test panel
     + LR support).
  2. Computes M = U Σ V^T (SVD) and identifies the rank-r subspace
     V[:, :r].
  3. Solves the REDUCED lstsq: U[:, :r] · diag(σ_1..σ_r) ·
     coeffs = chi  →  coeffs of dim r.
  4. Reconstructs the operator A_full = V[:, :r] · coeffs ∈ R^n
     in the original ambient space.

Compute savings vs the dense (M-of-shape-K1*K2 × n_unknowns) lstsq:
  - SVD is O(K1*K2 · n_unknowns · min(...)), same as dense lstsq
    in the worst case, but…
  - The SAME SVD decomposition is reused across the 3 interfaces
    (pp, nn, pn) since M is interface-independent.  Only the chi
    RHS changes per interface.
  - For interface SWEEPS (extracting all 3 in one pass), this is
    a 3× win over independent dense lstsq's.

Output: `A-operator-extract-reduced.witness.json` per (λ,
interface) operator residual + reduced-basis coefficient norms.

Usage:
    python3 folio-assistant/computations/A_operator_extract_reduced.py
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

import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from A_operator_extract_general import (  # noqa: E402
    H, evaluate_word_matrix, make_test_words, with_interface, chi_lambda,
)
from lr_coefficients import get_lr_table, partitions_of  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


INTERFACES = {
    "pp":  (1.0, 0.0),
    "nn":  (1.0, -H),
    "pn":  (1.0, -H / 2),
}


def extract_reduced_per_interface(n1: int, n2: int, *,
                                    rank_threshold: float = 1e-12) -> dict:
    """Reduced-basis extract for all three interfaces in one pass.

    For each λ:
      - build M once (interface-independent)
      - SVD: M = U Σ V^T
      - identify rank r (sv > rank_threshold * sv[0])
      - per interface: solve reduced lstsq U[:, :r] · σ_diag · c = chi
      - record residual + coefficient norm
    """
    parts_1 = partitions_of(n1)
    parts_2 = partitions_of(n2)
    parts_sum = partitions_of(n1 + n2)
    lr_table = get_lr_table(n1, n2)

    test_1 = make_test_words(n1)
    test_2 = make_test_words(n2)
    K1, K2 = len(test_1), len(test_2)

    print(f"  panel: K1={K1}, K2={K2}, pairs={K1*K2}")

    rho_mu = {(i, mu): evaluate_word_matrix(mu, test_1[i])
              for i in range(K1) for mu in parts_1}
    rho_nu = {(j, nu): evaluate_word_matrix(nu, test_2[j])
              for j in range(K2) for nu in parts_2}

    print(f"  Computing χ^λ for K1*K2 pairs × 3 interfaces × {len(parts_sum)} λ...")
    t0 = time.time()
    chi_table = {iface: {} for iface in INTERFACES}
    for iface, (c_int, d_int) in INTERFACES.items():
        for i in range(K1):
            for j in range(K2):
                comb = with_interface(test_1[i], test_2[j], n1=n1,
                                       int_c=c_int, int_d=d_int)
                for lam in parts_sum:
                    chi_table[iface][(i, j, lam)] = chi_lambda(lam, comb)
    print(f"    [{time.time() - t0:.1f}s]")

    print("  Per-λ reduced-basis extraction:")
    print(f"  {'λ':<22}{'ambient':>10}{'rank':>6}{'compress':>10}"
          f"{'res pp':>14}{'res nn':>14}{'res pn':>14}")
    print("  " + "-" * 90)

    results = {}
    total_ambient = 0
    total_rank = 0
    n_passed = 0
    for lam in parts_sum:
        support = [(mu, nu, c) for (mu, nu, lam_), c in lr_table.items()
                    if lam_ == lam]
        if not support:
            continue
        n_unknowns = sum((rho_mu[(0, mu)].shape[0] * rho_nu[(0, nu)].shape[0]) ** 2
                          for (mu, nu, _) in support)
        n_eq = K1 * K2
        if n_eq < n_unknowns:
            results[str(list(lam))] = {"status": "panel_too_small",
                                        "n_unknowns": n_unknowns}
            continue

        offsets = [0]
        for (mu, nu, _) in support:
            d = (rho_mu[(0, mu)].shape[0] * rho_nu[(0, nu)].shape[0]) ** 2
            offsets.append(offsets[-1] + d)
        M = np.zeros((n_eq, n_unknowns), dtype=complex)
        k = 0
        for i in range(K1):
            for j in range(K2):
                for sidx, (mu, nu, c) in enumerate(support):
                    Xi = rho_mu[(i, mu)]
                    Xj = rho_nu[(j, nu)]
                    if Xi.size == 0 or Xj.size == 0:
                        continue
                    X = np.kron(Xi, Xj)
                    M[k, offsets[sidx]:offsets[sidx + 1]] = c * X.T.flatten()
                k += 1

        # SVD once.  Reuse U, Σ, V across interfaces.
        U, sv, Vt = np.linalg.svd(M, full_matrices=False)
        threshold = max(sv[0] * rank_threshold, 1e-30)
        rank = int(np.sum(sv > threshold))

        # Reduced-basis solve per interface.
        residuals_per_iface: dict = {}
        coeff_norms: dict = {}
        for iface in INTERFACES:
            rhs = np.array([chi_table[iface][(i, j, lam)]
                            for i in range(K1) for j in range(K2)])
            # Reduced solve: U[:, :rank].T @ rhs gives coeffs in U-basis.
            # Then divide by σ to map to V-basis: coeffs = (1/σ) U.T rhs.
            # A_full = V.T[:, :rank] @ coeffs.
            U_r = U[:, :rank]
            sv_r = sv[:rank]
            Vt_r = Vt[:rank, :]
            coeffs = (U_r.conj().T @ rhs) / sv_r
            A_full = Vt_r.conj().T @ coeffs
            res = np.abs(M @ A_full - rhs)
            max_rel = float(np.max(res)) / max(float(np.max(np.abs(rhs))), 1e-30)
            residuals_per_iface[iface] = max_rel
            coeff_norms[iface] = float(np.linalg.norm(coeffs))

        # Linearity identity on the REDUCED coefficients.
        rhs_pp = np.array([chi_table["pp"][(i, j, lam)]
                            for i in range(K1) for j in range(K2)])
        rhs_nn = np.array([chi_table["nn"][(i, j, lam)]
                            for i in range(K1) for j in range(K2)])
        rhs_pn = np.array([chi_table["pn"][(i, j, lam)]
                            for i in range(K1) for j in range(K2)])
        coeffs_pp = (U[:, :rank].conj().T @ rhs_pp) / sv[:rank]
        coeffs_nn = (U[:, :rank].conj().T @ rhs_nn) / sv[:rank]
        coeffs_pn = (U[:, :rank].conj().T @ rhs_pn) / sv[:rank]
        coeffs_predicted = (coeffs_pp + coeffs_nn) / 2.0
        coeff_diff = float(np.linalg.norm(coeffs_pn - coeffs_predicted))
        # In the reduced basis the linearity identity should give
        # coeff_diff = 0 exactly (since linearity holds on the rhs).

        results[str(list(lam))] = {
            "status": "extracted",
            "n_unknowns": n_unknowns,
            "rank": rank,
            "compression": rank / n_unknowns,
            "residuals_per_interface": residuals_per_iface,
            "coeff_norms_per_interface": coeff_norms,
            "linearity_coeff_diff_norm": coeff_diff,
        }
        total_ambient += n_unknowns
        total_rank += rank
        n_passed += 1

        print(f"  {str(list(lam)):<22}{n_unknowns:>10}{rank:>6}"
              f"{rank/n_unknowns:>10.3f}"
              f"{residuals_per_iface['pp']:>14.3e}"
              f"{residuals_per_iface['nn']:>14.3e}"
              f"{residuals_per_iface['pn']:>14.3e}")

    print("  " + "-" * 90)
    print(f"  TOTAL: ambient={total_ambient}, rank={total_rank}, "
          f"compress={total_rank/total_ambient if total_ambient else 0:.3f}")

    return results, total_ambient, total_rank, n_passed


def main() -> int:
    n1, n2 = 3, 6
    print("=" * 92)
    print(f"  Reduced-basis A^λ_{{μν}}(I) extraction at A=3 (split {n1}+{n2})")
    print(f"  SVD once per λ, three-interface RHS sweep")
    print("=" * 92)

    results, total_ambient, total_rank, n_passed = extract_reduced_per_interface(n1, n2)

    print()
    print(f"  λ extracted: {n_passed} / 30 ⊢ {n1+n2}")
    print(f"  Total compression: {total_rank/total_ambient if total_ambient else 0:.3f}"
          f"  ({total_rank} / {total_ambient})")

    w = WitnessBuilder("A-operator-extract-reduced", engine="numpy")
    w.set_description(
        "Reduced-basis A^λ_{μν}(I) extraction.  Builds M once per λ, "
        "computes SVD, solves the reduced lstsq in the rank-r subspace "
        "(r << ambient n_unknowns).  Reuses the SAME SVD decomposition "
        "across the three interfaces (pp, nn, pn) since M is interface-"
        "independent — a 3× compute win over independent dense lstsq's.  "
        "Verifies the linearity identity at the reduced-coefficient "
        "level: coeffs_pn - (coeffs_pp + coeffs_nn) / 2 = 0 exactly "
        "(since linearity holds on the RHS chi vector before SVD)."
    )
    w.set_audit_only("docs/audits/2026-05-09-A-operator-rank-structure.md")
    w.set_content_block("operator-valued sub-lemma 2.1 (A-operator extraction probe; no formal block yet)")
    w.add_parameter("A", 3)
    w.add_parameter("split", f"{n1}+{n2}")
    w.add_data("results_per_lambda", results)
    w.add_data("total_ambient", total_ambient)
    w.add_data("total_rank", total_rank)
    w.add_data("compression_factor",
                total_rank / total_ambient if total_ambient else 1.0)

    # Headline assertion: all three interfaces yield extraction
    # residual ~1e-14 for every solved λ.
    n_clean = sum(
        1 for r in results.values()
        if r.get("status") == "extracted"
        and all(rr < 1e-12 for rr in r["residuals_per_interface"].values())
    )
    w.add_assertion(
        name="all_interfaces_extract_below_1e-12",
        computed=n_clean,
        expected=n_passed,
        source="A_operator_extract_reduced",
    )
    # Linearity identity should be EXACT (0) in the reduced basis.
    n_lin_exact = sum(
        1 for r in results.values()
        if r.get("status") == "extracted"
        and r.get("linearity_coeff_diff_norm", 1.0) < 1e-10
    )
    w.add_assertion(
        name="linearity_identity_exact_in_reduced_basis",
        computed=n_lin_exact,
        expected=n_passed,
        source="A_operator_extract_reduced",
    )
    w.save()
    return 0 if (n_clean == n_passed and n_lin_exact == n_passed) else 1


if __name__ == "__main__":
    sys.exit(main())
