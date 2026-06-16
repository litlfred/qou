#!/usr/bin/env python3


# polynomial_q_not_applicable: numerical lstsq of A^λ_{μν}(I) for three interfaces.
"""Per-interface operator extract + linearity verification (item 1 of
the symmetry-reduction sweep).

Extracts A^λ_{μν}(I) for the three canonical interface types
  pp:  σ                       (c, d) = (1, 0)
  nn:  σ⁻¹  = σ - h            (c, d) = (1, -h)
  pn:  (σ + σ⁻¹)/2 = σ - h/2   (c, d) = (1, -h/2)

at A=3 (split 3+6 → 9), and verifies the linearity identity

    A^λ_{μν}((σ + σ⁻¹)/2) = (1/2)(A^λ_{μν}(σ) + A^λ_{μν}(σ⁻¹))

across all 22 rank-determined partitions λ ⊢ 9.

Output: `A-operator-per-interface.witness.json` with per-(λ, I)
operator residuals + per-λ linearity-identity errors.

Usage:
    python3 computations/A_operator_per_interface_probe.py
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
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


def extract_per_interface(n1: int, n2: int) -> dict:
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

    # Compute χ^λ for ALL THREE interfaces in one chi_table sweep.
    # Each interface only changes the inserted (c_int, d_int, n1-1)
    # tuple in the combined word.
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

    # Per-λ extraction for each interface.  Build M ONCE per λ (M is
    # interface-independent), reuse across the three RHSs.
    results = {}
    n_resolved = {iface: 0 for iface in INTERFACES}
    n_linearity_ok = 0
    n_linearity_total = 0
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
                                        "n_unknowns": n_unknowns,
                                        "n_equations": n_eq}
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

        # Solve for each interface.
        sols = {}
        residuals = {}
        for iface in INTERFACES:
            rhs = np.array([chi_table[iface][(i, j, lam)]
                            for i in range(K1) for j in range(K2)])
            sol, _, rank, _ = np.linalg.lstsq(M, rhs, rcond=None)
            res = np.abs(M @ sol - rhs)
            max_rel = float(np.max(res)) / max(float(np.max(np.abs(rhs))), 1e-30)
            sols[iface] = sol
            residuals[iface] = max_rel
            n_resolved[iface] += 1

        # Linearity identity:  A_pn = (A_pp + A_nn) / 2
        predicted_pn = (sols["pp"] + sols["nn"]) / 2.0
        actual_pn = sols["pn"]
        linearity_diff = predicted_pn - actual_pn
        # Compare in the rank subspace (M-projection):
        # ||M (predicted - actual)|| should be small for consistent solns.
        diff_in_chi = np.abs(M @ linearity_diff)
        max_chi_diff = float(np.max(diff_in_chi))
        # Norm in solution space (depends on min-norm choice; less meaningful).
        norm_diff = float(np.linalg.norm(linearity_diff))
        linearity_ok = max_chi_diff < 1e-10
        if linearity_ok:
            n_linearity_ok += 1
        n_linearity_total += 1

        results[str(list(lam))] = {
            "status": "extracted",
            "n_unknowns": n_unknowns,
            "rank": int(rank),
            "residuals_per_interface": residuals,
            "linearity_max_chi_diff": max_chi_diff,
            "linearity_solution_norm_diff": norm_diff,
            "linearity_ok_at_chi_level": linearity_ok,
        }

    return results, n_resolved, n_linearity_ok, n_linearity_total


def main() -> int:
    n1, n2 = 3, 6
    print("=" * 92)
    print(f"  Per-interface A^λ_{{μν}}(I) extraction at A=3 (split {n1}+{n2})")
    print(f"  Interfaces: pp=σ, nn=σ⁻¹, pn=(σ+σ⁻¹)/2")
    print(f"  Linearity identity: A_pn = (A_pp + A_nn) / 2")
    print("=" * 92)

    results, n_resolved, n_linearity_ok, n_linearity_total = extract_per_interface(n1, n2)

    print()
    print(f"  λ resolved per interface: pp={n_resolved['pp']}, "
          f"nn={n_resolved['nn']}, pn={n_resolved['pn']} (each of 30 total)")
    print(f"  Linearity identity OK at χ-level: {n_linearity_ok} / {n_linearity_total}")
    print()
    # Print per-λ linearity status.
    print(f"  {'λ':<22}{'rank':>6}{'res pp':>14}{'res nn':>14}{'res pn':>14}{'lin (χ)':>14}")
    print("  " + "-" * 90)
    for k, r in results.items():
        if r.get("status") != "extracted":
            continue
        rs = r["residuals_per_interface"]
        ld = r["linearity_max_chi_diff"]
        print(f"  {k:<22}{r['rank']:>6}{rs['pp']:>14.3e}{rs['nn']:>14.3e}"
              f"{rs['pn']:>14.3e}{ld:>14.3e}")

    w = WitnessBuilder("A-operator-per-interface", engine="numpy")
    w.set_description(
        "Per-interface A^λ_{μν}(I) extraction at A=3 (split 3+6) for "
        "the three canonical interfaces pp, nn, pn.  Verifies the "
        "linearity identity A_pn = (A_pp + A_nn) / 2 (which follows "
        "from the linearity of the LR projection in I per refined "
        "Sub-lemma 2.1).  Identity is checked at the χ-level: "
        "M·(predicted_pn - actual_pn) should be zero, since both "
        "sides of the identity reproduce the same χ^λ(β_1·I_pn·β_2)."
    )
    w.set_audit_only("docs/audits/2026-05-09-A-operator-rank-structure.md")
    w.set_content_block("operator-valued sub-lemma 2.1 (A-operator extraction probe; no formal block yet)")
    w.add_parameter("A", 3)
    w.add_parameter("split", f"{n1}+{n2}")
    w.add_data("results_per_lambda", results)
    w.add_data("n_resolved_per_interface", n_resolved)
    w.add_data("n_linearity_ok_at_chi_level", n_linearity_ok)
    w.add_data("n_linearity_total", n_linearity_total)
    w.add_assertion(
        name="linearity_identity_holds_at_chi_level",
        computed=n_linearity_ok,
        expected=n_linearity_total,
        source="A_operator_per_interface_probe",
    )
    w.save()
    return 0 if n_linearity_ok == n_linearity_total else 1


if __name__ == "__main__":
    sys.exit(main())
