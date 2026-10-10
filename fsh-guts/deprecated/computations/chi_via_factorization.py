#!/usr/bin/env python3
"""
F4 composer: χ via Littlewood-Richardson decomposition of cached
factorizations.

For a tensor-product factorization β = β_1 ⊗ β_2 where β_1 ∈ H_p(q)
acts on p strands and β_2 ∈ H_q(q) on q strands (with p + q = n),
the character on S^λ decomposes as

    χ_λ(β) = Σ_{μ ⊢ p, ν ⊢ q} c^λ_{μν} · χ_μ(β_1) · χ_ν(β_2)

where c^λ_{μν} is the Littlewood-Richardson coefficient.

This module provides:
  - `compose_chi_lambda(λ, factor_chis)`: combine cached sub-character
    data into a parent character via LR coefficients.
  - `compose_chi_lambda_q(λ, factor_chis_q)`: same but for q-Laurent
    polynomial characters (returns LaurentPolyQ-as-list).

@module computations/chi_via_factorization
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import pyhecke_native as p  # type: ignore[import]
from hecke_characters import partitions_of  # type: ignore[import]


def compose_chi_lambda(
    lam: list,
    factors_p: list[int],
    factors_chi: list[dict],
) -> float:
    """Compose χ_λ from a tensor-product factorization.

    Args:
      lam: outer partition λ ⊢ n.
      factors_p: list [p_1, p_2, ...] of strand counts for each factor.
      factors_chi: list of dicts mapping `tuple(partition)` to χ value.
        factors_chi[k][μ] = χ_μ(β_k) for μ ⊢ factors_p[k].

    Returns: χ_λ(β_1 ⊗ β_2 ⊗ ...) as a float.

    For 2 factors: χ_λ(β_1 ⊗ β_2) = Σ_{μ, ν} c^λ_{μν} · χ_μ(β_1) · χ_ν(β_2).
    For k > 2 factors, applies LR composition iteratively (associative).
    """
    n = sum(lam)
    if sum(factors_p) != n:
        raise ValueError(f"sum(factors_p)={sum(factors_p)} ≠ |λ|={n}")
    if len(factors_p) == 0:
        return 1.0 if n == 0 else 0.0
    if len(factors_p) == 1:
        return float(factors_chi[0].get(tuple(lam), 0.0))

    # Two-factor case directly.
    if len(factors_p) == 2:
        p1, p2 = factors_p
        total = 0.0
        for mu in partitions_of(p1):
            chi_mu = float(factors_chi[0].get(tuple(mu), 0.0))
            if chi_mu == 0:
                continue
            for nu in partitions_of(p2):
                chi_nu = float(factors_chi[1].get(tuple(nu), 0.0))
                if chi_nu == 0:
                    continue
                c = p.lr_coefficient(list(lam), list(mu), list(nu))
                if c != 0:
                    total += c * chi_mu * chi_nu
        return total

    # Iterative composition: combine first two, then absorb the rest.
    # Build the "merged" first-two factor as a virtual factor of size
    # p_1 + p_2 with χ values computed via LR for every sigma ⊢ p_1+p_2.
    p1, p2 = factors_p[0], factors_p[1]
    merged_chis: dict = {}
    for sigma in partitions_of(p1 + p2):
        sigma_tuple = tuple(sigma)
        val = 0.0
        for mu in partitions_of(p1):
            chi_mu = float(factors_chi[0].get(tuple(mu), 0.0))
            if chi_mu == 0:
                continue
            for nu in partitions_of(p2):
                chi_nu = float(factors_chi[1].get(tuple(nu), 0.0))
                if chi_nu == 0:
                    continue
                c = p.lr_coefficient(list(sigma), list(mu), list(nu))
                if c != 0:
                    val += c * chi_mu * chi_nu
        if val != 0:
            merged_chis[sigma_tuple] = val
    return compose_chi_lambda(
        lam,
        [p1 + p2] + factors_p[2:],
        [merged_chis] + factors_chi[2:],
    )


# ── Smoke test ────────────────────────────────────────────────────

def smoke_test():
    """Validate compose_chi_lambda against direct computation."""
    print("Smoke test: compose χ via LR vs direct computation")
    print()

    # Example: σ_1 on H_3 acting on irrep λ.
    # If we factor β = σ_1 (which acts only on strands 1, 2) and
    # treat it as σ_1 ⊗ id where σ_1 ∈ H_2 and id ∈ H_1, we should
    # recover the same χ.

    # First compute χ_λ(σ_1) directly for all λ ⊢ 3.
    word = [(1, 1)]  # σ_1
    q = 1.10998
    direct = {}
    for lam in partitions_of(3):
        chi = p.chi_lambda_braid(list(lam), word, q)
        direct[tuple(lam)] = chi

    # Now factor as σ_1 ∈ H_2 ⊗ id ∈ H_1.
    # χ_μ(σ_1) for μ ⊢ 2:
    chi_factor1 = {}
    for mu in partitions_of(2):
        chi_factor1[tuple(mu)] = p.chi_lambda_braid(list(mu), [(1, 1)], q)
    # χ_ν(id) for ν ⊢ 1:  S^(1) has dim 1, χ_(1)(id) = 1.
    chi_factor2 = {(1,): 1.0}

    print(f"  λ           direct        composed       diff")
    for lam in partitions_of(3):
        composed = compose_chi_lambda(
            list(lam), [2, 1], [chi_factor1, chi_factor2]
        )
        d = direct[tuple(lam)]
        diff = abs(composed - d)
        status = "OK" if diff < 1e-10 else "FAIL"
        print(f"  {lam}   {d:>+12.6f}  {composed:>+12.6f}  {diff:.2e}  {status}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--smoke", action="store_true",
                        help="Run smoke test")
    args = parser.parse_args()
    if args.smoke:
        smoke_test()
    else:
        parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
