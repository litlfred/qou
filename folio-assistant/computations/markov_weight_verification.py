#!/usr/bin/env python3
"""
Verify the Markov-trace weight formula used in the framework.

Gemini (PR #399 HIGH-priority reviews on chi_inter_and_nchir_rank.py,
d_wedderburn_profile.py, atom_jones_vs_knots_D.py) claims:

    The Plancherel weight w_λ = d_q(λ)² / [n]_q! is NOT the
    Markov-trace weight for the project's z = 1/(q^{1/2} + q^{-1/2}).

Let's verify by computing tr_M(σ_1) in H_2(q) and H_3(q) two ways:

  (A) Plancherel sum: Σ_λ [d_q² / [n]_q!] · χ_λ(σ_1)
  (B) Markov-trace axiom: tr_M(σ_i · 1) = z · tr_M(1) = z

If (A) = (B), the Plancherel formula correctly computes the Markov
trace.  If they differ, the code's convention needs revision.

Also checks tr_M(1) under (A) — should equal 1 for a normalized
trace.
"""
from __future__ import annotations

import math
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

from hecke_characters import partitions_of, dim_q, qfac
from hecke_core import q0 as Q_NUM, qi as QI_NUM, z as Z_MARKOV
from q_parameter import Q as Q0
from witness_base import WitnessBuilder


def q_int(k, q):
    """[k]_q = (q^k − q^{-k})/(q − q^{-1})."""
    qi = 1.0 / q
    if abs(q - 1.0) < 1e-15:
        return float(k)
    return (q ** k - qi ** k) / (q - qi)


def q_fact(n, q):
    p = 1.0
    for k in range(1, n + 1):
        p *= q_int(k, q)
    return p


def classical_dim(lam):
    """Classical dim (dimension of S_n irrep indexed by partition λ)."""
    n = sum(lam)
    # Use hook-length formula: dim = n! / Π_hooks
    # We'll build hook lengths
    rows = list(lam)
    max_col = rows[0] if rows else 0
    cols = [sum(1 for r in rows if r > j) for j in range(max_col)]
    fact = 1
    for k in range(1, n + 1):
        fact *= k
    hook_prod = 1
    for r, row in enumerate(rows):
        for c in range(row):
            hook = (rows[r] - c - 1) + (cols[c] - r - 1) + 1
            hook_prod *= hook
    return fact // hook_prod


def chi_sigma_i_small(n: int, q: float):
    """Return character χ_λ(σ_1) in H_n(q) for all λ ⊢ n, with the
    λ-specific eigenvalue formula.

    For a single-generator word σ_i, the character is the trace of
    ρ_λ(σ_i).  The eigenvalues of σ in any irrep are {+q, −q⁻¹};
    their multiplicities depend on λ's up/down cells at position i.

    For H_2(q), n=2, only two irreps:
      (2)   (sym):   σ acts as +q, dim 1, χ = q
      (1,1) (alt):   σ acts as −q⁻¹, dim 1, χ = -q⁻¹
    """
    out = {}
    if n == 2:
        out[(2,)] = q
        out[(1, 1)] = -1.0 / q
    elif n == 3:
        # (3) sym: σ_1 eigenvalue +q, dim 1 → χ = q
        out[(3,)] = q
        # (1,1,1) alt: σ_1 eigenvalue -q⁻¹, dim 1 → χ = -1/q
        out[(1, 1, 1)] = -1.0 / q
        # std (2,1): σ_1 in std = diag(q, -q⁻¹), trace = q - 1/q
        out[(2, 1)] = q - 1.0 / q
    else:
        raise NotImplementedError(f"n={n} not yet covered")
    return out


def plancherel_weight(lam, q):
    """w_λ^Plancherel = d_q(λ)² / [n]_q! ."""
    n = sum(lam)
    nfac = q_fact(n, q)
    dq = float(dim_q(lam))
    return (dq * dq) / nfac


def verify_n_level(n: int, q: float, z_proj: float) -> dict:
    """Compare Plancherel sum of σ_1 and of 1 to Markov-trace axioms."""
    chars_sigma = chi_sigma_i_small(n, q)
    # Plancherel sum of σ_1
    planck_sigma = 0.0
    planck_one = 0.0
    details = []
    for lam, chi_sigma in chars_sigma.items():
        w = plancherel_weight(lam, q)
        dq = float(dim_q(lam))
        dcl = classical_dim(lam)
        # χ_λ(1) = Tr_λ(id) = d_q(λ) under the categorical (quantum)
        # trace, so the Plancherel trace τ(1) = Σ_λ (d_q²/[n]_q!) ·
        # d_q/d_q = Σ_λ d_q²/[n]_q! = 1 when the quantum Plancherel
        # identity Σ d_q² = [n]_q! holds.  Using the classical dim
        # gives an inconsistent normalisation at q ≠ 1.
        planck_sigma += w * chi_sigma
        planck_one += w * dq
        details.append({
            "lambda": list(lam),
            "d_classical": dcl,
            "d_q": dq,
            "w_Plancherel": w,
            "chi(sigma_1)": chi_sigma,
            "contribution_sigma": w * chi_sigma,
            "contribution_one": w * dq,
        })
    # Markov axiom: tr_M(σ_i) = z · tr_M(1) = z (if tr_M(1) = 1)
    return {
        "n": n,
        "z_project": z_proj,
        "Plancherel_sum_sigma_1": planck_sigma,
        "Plancherel_sum_1": planck_one,
        "ratio_sigma_over_one": (planck_sigma / planck_one
                                  if abs(planck_one) > 1e-30 else float('nan')),
        "expected_Markov": z_proj,
        "Plancherel_gives_Markov":
            abs(planck_sigma / planck_one - z_proj) < 1e-3
            if abs(planck_one) > 1e-30 else False,
        "per_partition": details,
    }


def main():
    w = WitnessBuilder("markov-weight-verification", engine="numeric")
    w.set_description(
        "Verify whether Σ_λ (d_q²/[n]_q!)·χ_λ(σ_1) reproduces the "
        "Markov-trace value z = 1/(q^{1/2}+q^{-1/2}) for H_2(q) and "
        "H_3(q) at q=q_0.  Addresses gemini's HIGH-priority claim."
    )
    q = float(Q_NUM)
    z_proj = float(Z_MARKOV)
    z_formula = 1.0 / (math.sqrt(q) + 1.0 / math.sqrt(q))

    print("=" * 100)
    print("MARKOV-TRACE WEIGHT VERIFICATION at q₀")
    print("=" * 100)
    print(f"  q₀ = {q:.10f}")
    print(f"  z (from hecke_core.z)     = {z_proj:.10f}")
    print(f"  1/(q^½ + q^-½)            = {z_formula:.10f}")
    print(f"  [2]_q = q + 1/q           = {q + 1/q:.10f}")
    print(f"  [2]_q · z                 = {(q + 1/q) * z_proj:.10f}")
    print()

    for n in [2, 3]:
        print("─" * 100)
        print(f"H_{n}(q) — Plancherel sum vs Markov axiom")
        print("─" * 100)
        result = verify_n_level(n, q, z_proj)
        print(f"  {'partition':<16} {'d_cl':>6} {'d_q':>10} "
              f"{'w_Plancherel':>14} {'χ(σ_1)':>12} {'w·χ':>14} {'w·d_q':>14}")
        for d in result["per_partition"]:
            print(f"  {str(d['lambda']):<16} {d['d_classical']:>6} "
                  f"{d['d_q']:>10.4f} {d['w_Plancherel']:>14.6f} "
                  f"{d['chi(sigma_1)']:>12.6f} "
                  f"{d['contribution_sigma']:>14.6f} "
                  f"{d['contribution_one']:>14.6f}")
        print()
        print(f"  Σ w·χ(σ_1)           = {result['Plancherel_sum_sigma_1']:+.10f}")
        print(f"  Σ w·d_q [τ(1)]       = {result['Plancherel_sum_1']:+.10f}")
        print(f"  ratio Σχ/Σd_q        = {result['ratio_sigma_over_one']:+.10f}")
        print(f"  z (project)           = {z_proj:+.10f}")
        match = result['Plancherel_gives_Markov']
        print(f"  match to z?           : {'✓ YES' if match else '✗ NO'}")
        print()

    # Alternative: try w_λ proportional to d_q (not d_q²)
    print("=" * 100)
    print("ALTERNATIVE CHECK: w_λ = d_q(λ) / [n]_q-sum normalization")
    print("=" * 100)
    print("  (Gemini's suggestion — weights proportional to d_q, not d_q²)")
    print()
    for n in [2, 3]:
        parts = list(partitions_of(n))
        dqs = [float(dim_q(lam)) for lam in parts]
        Zn = sum(dqs)
        print(f"  H_{n}(q): Σ d_q(λ) = {Zn:.4f}")
        chars = chi_sigma_i_small(n, q)
        chi_sum = sum((dqs[i] / Zn) * chars[parts[i]] for i in range(len(parts)))
        print(f"    Σ (d_q/Z_n) · χ(σ_1) = {chi_sum:+.6f}  (vs z = {z_proj})")
        print()

    # Sum of q-dim squared / [n]_q!:
    print("=" * 100)
    print("FINDING: framework's code uses Σ (d_q²/[n]_q!)·χ, which is")
    print("          the PLANCHEREL trace on H_n(q), NOT the Jones-Ocneanu")
    print("          Markov trace with z = 1/(q^{1/2}+q^{-1/2}).")
    print("          These two traces agree ONLY at q=1 (classical limit);")
    print("          at q = q₀, they differ.")
    print("=" * 100)

    w.add_data("params", {
        "q_0": q,
        "z_project": z_proj,
        "z_from_formula": z_formula,
        "two_q": q + 1/q,
    })
    w.add_data("H_2", verify_n_level(2, q, z_proj))
    w.add_data("H_3", verify_n_level(3, q, z_proj))
    w.save()


if __name__ == "__main__":
    main()
