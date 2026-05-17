#!/usr/bin/env python3
"""Probe: per-Wedderburn-block χ_λ(β) at ε^10 and ε^12 for c_5/c_6.

Item 3 from `rem:post-pr665-open-rd-inventory`. Tests whether the
empirical c_5 ≈ -395, c_6 ≈ -45485 arise from a per-Wedderburn-block
weighted sum

    c_k = Σ_{λ ⊢ 3} y_λ · c_k^(λ)

where c_k^(λ) is the order-(q-1)^(2k) coefficient of χ_λ(β; q)
expanded at q = 1 + ε, and y_λ is the Wenzl-bridge weight.

For each λ ∈ {(3), (2,1), (1,1,1)}:
  1. Compute χ_λ(β_p) and χ_λ(β_n) symbolically in q.
  2. Substitute q = 1 + ε and expand to order ε^12.
  3. Extract ε^10 (c_5 candidate) and ε^12 (c_6 candidate) coeffs.
  4. Report per-block and weighted sum.

This is **a numerical probe**, not a claim of c_k closure. If the
weighted sum matches empirical c_5, c_6, that's a substantive R&D
result. If not, the negative result rules out the simple per-block
hypothesis.

Output: `per-wedderburn-block-ck.witness.json`.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

mp.mp.dps = 50


def main() -> int:
    from hecke_character_symbolic import (
        atomic_braid_to_crossings,
        q_character_on_braid_word,
        partitions_of,
    )

    print("=" * 96)
    print("  Per-Wedderburn-block χ_λ(β) at ε^10, ε^12 for c_5/c_6 candidates")
    print("=" * 96)
    print()

    q = sp.Symbol("q", positive=True, real=True)
    eps = sp.Symbol("epsilon", real=True)

    # Canonical typed-B_3 braids for proton (uud) and neutron (udd).
    print("Computing per-irrep χ_λ(β_p), χ_λ(β_n) symbolically in q...")
    crossings_p = atomic_braid_to_crossings(Z=1, N=0, include_inter=False)
    crossings_n = atomic_braid_to_crossings(Z=0, N=1, include_inter=False)
    print(f"  β_p length = {len(crossings_p)} crossings")
    print(f"  β_n length = {len(crossings_n)} crossings")
    print()

    per_lambda = {}
    for lam in partitions_of(3):
        lam_str = str(lam)
        print(f"  λ = {lam_str}:")
        chi_p = q_character_on_braid_word(lam, crossings_p, q)
        chi_n = q_character_on_braid_word(lam, crossings_n, q)
        # Substitute q = 1 + eps; expand to order ε^13 so ε^12 is exact.
        chi_p_eps = sp.series(chi_p.subs(q, 1 + eps), eps, 0, 13).removeO()
        chi_n_eps = sp.series(chi_n.subs(q, 1 + eps), eps, 0, 13).removeO()
        # Difference χ_λ(β_n) − χ_λ(β_p): the n−p contribution.
        chi_diff_eps = sp.expand(chi_n_eps - chi_p_eps)
        # Extract ε^10 and ε^12 coefficients.
        c10_diff = chi_diff_eps.coeff(eps, 10)
        c12_diff = chi_diff_eps.coeff(eps, 12)
        # Express as floats for readability.
        c10_float = float(c10_diff) if c10_diff.is_number else None
        c12_float = float(c12_diff) if c12_diff.is_number else None
        per_lambda[lam_str] = {
            "chi_p_eps_polynomial": str(chi_p_eps),
            "chi_n_eps_polynomial": str(chi_n_eps),
            "c10_diff_symbolic": str(sp.nsimplify(c10_diff)),
            "c12_diff_symbolic": str(sp.nsimplify(c12_diff)),
            "c10_diff_float": c10_float,
            "c12_diff_float": c12_float,
        }
        print(f"    c10 (ε^10 coeff of χ_n − χ_p): {c10_float}")
        print(f"    c12 (ε^12 coeff of χ_n − χ_p): {c12_float}")
        print()

    # Empirical c_5, c_6 reference from
    # `probe_q_beta_c5_c6_multilink.py`:
    emp_c5 = mp.mpf("-395.41")
    emp_c6 = mp.mpf("-45485")

    # Weighted sum hypothesis: Σ_λ (dim V_λ / [3]!) · c_k^(λ)
    # = (1·c10_a + 2·c10_b + 1·c10_c) / 6 (Plancherel weights)
    # where a, b, c are the three partitions in canonical order.
    print("Weighted sum hypotheses (Plancherel weights):")
    weights = {"(3,)": 1 / 6, "(2, 1)": 2 / 6, "(1, 1, 1)": 1 / 6}
    c10_sum = sum(
        weights.get(lam, 0) * (per_lambda[lam]["c10_diff_float"] or 0)
        for lam in per_lambda
    )
    c12_sum = sum(
        weights.get(lam, 0) * (per_lambda[lam]["c12_diff_float"] or 0)
        for lam in per_lambda
    )
    print(f"  Σ y_λ · c10 = {c10_sum}")
    print(f"  Σ y_λ · c12 = {c12_sum}")
    print(f"  empirical c_5 ≈ {float(emp_c5)}")
    print(f"  empirical c_6 ≈ {float(emp_c6)}")
    print()

    # Result interpretation
    if abs(c10_sum) < 1e-10:
        c5_match = "ZERO at ε^10 — c_5 contribution requires deeper expansion"
    else:
        ratio5 = float(emp_c5) / c10_sum if c10_sum != 0 else None
        c5_match = f"non-zero c_10; ratio emp/Plancherel-sum = {ratio5}"

    if abs(c12_sum) < 1e-10:
        c6_match = "ZERO at ε^12 — c_6 contribution requires deeper expansion"
    else:
        ratio6 = float(emp_c6) / c12_sum if c12_sum != 0 else None
        c6_match = f"non-zero c_12; ratio emp/Plancherel-sum = {ratio6}"

    print("Interpretation:")
    print(f"  c_5 match: {c5_match}")
    print(f"  c_6 match: {c6_match}")
    print()

    from witness_base import WitnessBuilder

    builder = WitnessBuilder.wrap_legacy(
        "per-wedderburn-block-ck",
        {
            "description": (
                "Per-Wedderburn-block χ_λ(β) expansion at q = 1+ε to "
                "order ε^12. For each λ ∈ {(3), (2,1), (1,1,1)}, "
                "computes χ_λ(β_p) and χ_λ(β_n) symbolically, expands "
                "at q = 1+ε, extracts ε^10 and ε^12 coefficients of "
                "the n−p difference. Tests whether the per-block "
                "weighted sum matches empirical c_5 ≈ -395, c_6 ≈ "
                "-45485. Item 3 from rem:post-pr665-open-rd-inventory."
            ),
            "data": {
                "beta_p_length": len(crossings_p),
                "beta_n_length": len(crossings_n),
                "per_lambda": per_lambda,
                "plancherel_weighted_c10_sum": c10_sum,
                "plancherel_weighted_c12_sum": c12_sum,
                "empirical_c5_reference": str(emp_c5),
                "empirical_c6_reference": str(emp_c6),
                "c5_match_status": c5_match,
                "c6_match_status": c6_match,
            },
        },
        script_path=__file__,
        engine="sympy+mpmath",
    )
    out_path = builder.save()
    print(f"  Witness: {Path(out_path).name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
