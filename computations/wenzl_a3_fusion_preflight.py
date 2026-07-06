#!/usr/bin/env python3
"""H6 pre-flight for the path-(b) fusion derivation of A^λ_{μν}(I).

Verifies the closed-form identity derived in
docs/audits/2026-06-16-wenzl-a3-fusion-operator-derivation.md eqn (5)/(4'):

    χ^λ(β_1 · I · β_2)
        = Σ_{μ,ν} Tr_{V_λ}[ P_{μν} · ρ_λ(I) · P_{μν} · ρ_λ(β_1·β_2) ]

where P_{μν} = P_μ P_ν is the H_{n_1}=⟨σ_0,σ_1⟩ ⊗ H_{n_2}=⟨σ_3,σ_4⟩ isotypic
projector on V_λ (λ ⊢ 6), and I = c·σ_2 + d·1 is the deuteron interface.

This is convention-free (no skew→straight basis alignment, no least-squares):
it tests the structural claim directly. If it holds to ~1e-12 across the
test-word panel for all λ ⊢ 6, the fusion derivation is verified and the A≥3
implementation (skew CoB + recursion) is unblocked.

The isotypic projectors are built as Lagrange spectral projectors of the
central element C = σ_a + σ_b + σ_aσ_bσ_a (the q-image of the sum of the three
transpositions of S_3), which is central in each H_3 factor with distinct
scalar eigenvalues c_μ on the three irreps μ ⊢ 3.

NOTE: f64 cross-check (numpy). The committed witness re-runs at 50-dps mpmath
once the gate is green (compute-author §1).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from sublemma_2_1_A_operator_extract import (  # noqa: E402
    evaluate_word_matrix, with_interface, disjoint_word,
    make_test_words, partitions_of, H,
)


def central_C_word(g_lo: int) -> list:
    """C = σ_{g_lo} + σ_{g_lo+1} + σ_{g_lo}σ_{g_lo+1}σ_{g_lo} as a SUM of three
    Hecke words. Returns the three words (caller sums their matrices)."""
    a, b = g_lo, g_lo + 1
    return [
        [(1.0, 0.0, a)],
        [(1.0, 0.0, b)],
        [(1.0, 0.0, a), (1.0, 0.0, b), (1.0, 0.0, a)],
    ]


def central_C_matrix(shape: tuple, g_lo: int) -> np.ndarray:
    words = central_C_word(g_lo)
    mats = [evaluate_word_matrix(shape, w) for w in words]
    dim = mats[0].shape[0]
    out = np.zeros((dim, dim), dtype=complex)
    for m in mats:
        out += m
    return out


def central_eigenvalue(mu: tuple) -> complex:
    """Scalar eigenvalue c_μ of C on irrep V_μ (μ ⊢ 3): C is central so a
    scalar multiple of identity; value = Tr(C|_{V_μ}) / d_μ."""
    C = central_C_matrix(mu, 0)
    d = C.shape[0]
    if d == 0:
        return 0.0 + 0j
    return complex(np.trace(C)) / d


def lagrange_projectors(C: np.ndarray, eigs: dict) -> dict:
    """P_μ = Π_{μ'≠μ} (C - c_{μ'} I)/(c_μ - c_{μ'}) for each μ in eigs.
    eigs: {μ: c_μ}. Returns {μ: P_μ} (only those whose c_μ appears in C's
    spectrum give a non-zero projector)."""
    dim = C.shape[0]
    I = np.eye(dim, dtype=complex)
    cvals = list(eigs.items())
    out = {}
    for mu, c_mu in cvals:
        P = I.copy()
        ok = True
        for mu2, c_mu2 in cvals:
            if mu2 == mu:
                continue
            denom = c_mu - c_mu2
            if abs(denom) < 1e-9:
                ok = False
                break
            P = P @ ((C - c_mu2 * I) / denom)
        if ok:
            out[mu] = P
    return out


def main() -> int:
    parts_3 = partitions_of(3)
    parts_6 = partitions_of(6)
    test_words = make_test_words()

    # c_μ eigenvalues (same for both H_3 factors — isomorphic).
    eigs = {mu: central_eigenvalue(mu) for mu in parts_3}
    print("Central element C = σ_a+σ_b+σ_aσ_bσ_a — eigenvalue per μ ⊢ 3:")
    for mu, c in eigs.items():
        print(f"  μ={str(mu):<10} c_μ = {c.real:+.10f}{c.imag:+.2e}i")
    distinct = len({round(c.real, 8) for c in eigs.values()}) == len(eigs)
    print(f"  distinct eigenvalues (separates irreps): {distinct}")
    if not distinct:
        print("  ✗ central element does NOT separate — need a better separator")
        return 1

    print(f"\nPer-λ verification of the fusion identity (4') over "
          f"{len(test_words)**2} test pairs:")
    print(f"  {'λ ⊢ 6':<14} {'dim':>4} {'max |LHS-RHS|':>16}  status")
    print("  " + "-" * 50)

    all_ok = True
    worst_overall = 0.0
    for lam in parts_6:
        dim = evaluate_word_matrix(lam, []).shape[0]
        if dim == 0:
            continue
        # Build isotypic projectors on V_λ for both H_3 factors.
        C1 = central_C_matrix(lam, 0)   # H_3 = ⟨σ_0,σ_1⟩
        C2 = central_C_matrix(lam, 3)   # H_3' = ⟨σ_3,σ_4⟩
        Pmu = lagrange_projectors(C1, eigs)
        Pnu = lagrange_projectors(C2, eigs)

        rho_I = evaluate_word_matrix(lam, [(1.0, -H / 2, 2)])  # I = σ_2 - h/2

        worst = 0.0
        for wp in test_words:
            for wn in test_words:
                # LHS: χ^λ(β_1 · I · β_2)
                lhs = complex(np.trace(
                    evaluate_word_matrix(lam, with_interface(wp, wn))))
                # RHS: Σ_{μ,ν} Tr[ P_μ P_ν ρ_λ(I) P_μ P_ν ρ_λ(β_1·β_2) ]
                rho_b = evaluate_word_matrix(lam, disjoint_word(wp, wn))
                rhs = 0.0 + 0j
                for mu, Pm in Pmu.items():
                    for nu, Pn in Pnu.items():
                        Pmn = Pm @ Pn
                        block = Pmn @ rho_I @ Pmn
                        rhs += np.trace(block @ rho_b)
                worst = max(worst, abs(lhs - rhs))
        worst_overall = max(worst_overall, worst)
        ok = worst < 1e-9
        all_ok = all_ok and ok
        print(f"  {str(lam):<14} {dim:>4} {worst:>16.3e}  {'✓' if ok else '✗'}")

    print(f"\n  worst over all λ: {worst_overall:.3e}")
    if all_ok:
        print("  ✅ Fusion identity (5)/(4') VERIFIED at H_6 — derivation confirmed.")
        print("     A≥3 implementation (skew CoB + recursion) is unblocked.")
    else:
        print("  ✗ identity failed for some λ — investigate before A≥3 work.")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
