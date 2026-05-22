#!/usr/bin/env python3
"""Investigate Family A and its natural variants.

User question: "why 3% in family A. restate A.... was that just
first/second order approx? maybe more? investigate"

Family A (as proved on PR #701):
  λ_A(q) = (1/4) · Σ_{λ ⊢ 4} dim_q V_λ
         = (3q² + 4 + 3q⁻²)/4
         = 5/2 + (3/4)·h²

The series TERMINATES exactly at h². The dim_q V_λ for partitions
of 4 are themselves exact polynomials in q² + q⁻²:
  dim_q V_(4)        = 1                  (exact)
  dim_q V_(3,1)      = [3]_q = 3 + h²     (exact, NO higher terms)
  dim_q V_(2,2)      = [4]_q/[2]_q = 2 + h²  (exact)
  dim_q V_(2,1,1)    = [3]_q = 3 + h²     (exact)
  dim_q V_(1,1,1,1)  = 1                  (exact)

So `5/2 + (3/4)·h²` is an EXACT identity, not a truncation.

The 3% gap to CODATA at q_0 (Family A gives 2.5328 vs target 2.4600)
is STRUCTURAL, not due to omitted higher orders. Family A is the
"wrong" categorical quantity, not an under-resolved one.

This script tests OTHER natural Wedderburn-sum variants to see if
any gives a leading 5/2 AND a NEGATIVE h² coefficient closer to -G:

  V1 = (1/4) Σ dim_q V_λ                    (Family A — original)
  V2 = (1/N) Σ dim_q² V_λ                   (Plancherel-style)
  V3 = (1/N) Σ dim_q V_λ · dim V_λ          (mixed q + classical)
  V4 = (1/N) Σ [hook_λ]_q · dim_q V_λ       (hook-weighted)
  V5 = (1/N) Σ (−1)^|λ_conj_pair| dim_q V_λ (signed conjugate)
  V6 = (1/N) Σ dim_q V_λ for λ self-conj only  (restricted)
  V7 = (1/[4]_q) Σ dim_q V_λ                (q-normalized denominator)
  V8 = harmonic mean of dim_q V_λ
"""
from __future__ import annotations
import json, sys
from pathlib import Path

import sympy as sp
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from witness_base import WitnessBuilder
from q_parameter import Q_50_DIGIT_STR
from experimental_constants import M_E_MEV, M_P_MEV, Q_NEUTRON_MEV

mp.mp.dps = 80
Q_NUM = mp.mpf(Q_50_DIGIT_STR)
HBAR = (Q_NUM - 1) / Q_NUM
G = mp.catalan
VOL_B3 = 8 * G

M_E = mp.mpf(repr(M_E_MEV))
M_P = mp.mpf(repr(M_P_MEV))
M_NUCLEON = (M_P + M_P + mp.mpf(repr(Q_NEUTRON_MEV)) + M_E) / 2

# Required factor for m_N match
TARGET_FACTOR = M_NUCLEON * HBAR**2 / (VOL_B3 * M_E)


def main():
    print(f"Target factor (M_N · ℏ_q²/(Vol(B_3)·m_e)) = {mp.nstr(TARGET_FACTOR, 12)}")
    print()

    # Sympy symbols
    q = sp.Symbol("q", positive=True)
    h = q - 1/q
    eps = sp.Symbol("eps")

    def qint(n):
        return (q**n - q**(-n)) / (q - 1/q)

    # Quantum dimensions at H_4 (closed forms in q²+q⁻²)
    dim_q = {
        (4,):        sp.Integer(1),
        (3, 1):      qint(3),
        (2, 2):      qint(4) / qint(2),
        (2, 1, 1):   qint(3),
        (1, 1, 1, 1): sp.Integer(1),
    }
    # Classical dimensions (= χ_λ(identity))
    dim_cl = {
        (4,): 1, (3, 1): 3, (2, 2): 2, (2, 1, 1): 3, (1, 1, 1, 1): 1,
    }
    # Self-conjugate flag
    sc = {
        (4,): False, (3, 1): False, (2, 2): True,
        (2, 1, 1): False, (1, 1, 1, 1): False,
    }
    # Conjugate orbit sign (+1 for one of each pair, -1 for the other; 0 for sc)
    conj_sign = {
        (4,): 1, (3, 1): 1, (2, 2): 0,  # 0 used to mean "self-conj"
        (2, 1, 1): -1, (1, 1, 1, 1): -1,
    }

    # Hook products (for hook-weighted variant)
    hook_prod = {
        (4,):        sp.Integer(24),   # 4! = product of hook lengths
        (3, 1):      sp.Integer(8),    # 4·2·1·1
        (2, 2):      sp.Integer(12),   # 3·2·2·1
        (2, 1, 1):   sp.Integer(8),    # 4·1·2·1
        (1, 1, 1, 1): sp.Integer(24),
    }

    variants = {}

    # V1: Family A (original)
    V1 = sum(dim_q.values()) / 4
    variants["V1: (1/4) Σ dim_q V_λ (Family A)"] = V1

    # V2: (1/N) Σ dim_q²; choose N so leading = 5/2 at q=1
    sum_dim_q2 = sum(d**2 for d in dim_q.values())
    sum_dim_q2_at_1 = sp.limit(sum_dim_q2, q, 1)
    N2 = sum_dim_q2_at_1 / sp.Rational(5, 2)
    V2 = sum_dim_q2 / N2
    variants[f"V2: (1/{N2}) Σ dim_q² V_λ"] = V2

    # V3: (1/N) Σ dim_q · dim_classical
    sum_mixed = sum(dim_q[k] * dim_cl[k] for k in dim_q)
    sum_mixed_at_1 = sp.limit(sum_mixed, q, 1)
    N3 = sum_mixed_at_1 / sp.Rational(5, 2)
    V3 = sum_mixed / N3
    variants[f"V3: (1/{N3}) Σ dim_q · dim_cl"] = V3

    # V4: (1/N) Σ hook_q · dim_q (note hook_prod gives sum at q=1)
    # Use [h_x(λ)]_q product as q-deformed hook
    # Simplification: use classical hook product
    sum_v4 = sum(dim_q[k] * sp.Integer(hook_prod[k]) for k in dim_q)
    sum_v4_at_1 = sp.limit(sum_v4, q, 1)
    N4 = sum_v4_at_1 / sp.Rational(5, 2)
    V4 = sum_v4 / N4
    variants[f"V4: (1/{N4}) Σ hook_cl · dim_q"] = V4

    # V5: (1/N) Σ sign · dim_q  (sign convention: +1 for first member of pair, -1 for partner, 0 for sc)
    # Don't include self-conjugate
    # That would give: dim_q(4) + dim_q(3,1) - dim_q(2,1,1) - dim_q(1,1,1,1)
    sum_v5 = (
        dim_q[(4,)] + dim_q[(3, 1)]
        - dim_q[(2, 1, 1)] - dim_q[(1, 1, 1, 1)]
    )
    sum_v5_at_1 = sp.limit(sum_v5, q, 1)
    print(f"V5 sum at q=1: {sum_v5_at_1}")  # = 1+3-3-1 = 0
    # Can't normalize to 5/2; skip

    # V6: only self-conjugate (just (2,2))
    sum_v6 = dim_q[(2, 2)]
    sum_v6_at_1 = sp.limit(sum_v6, q, 1)
    N6 = sum_v6_at_1 / sp.Rational(5, 2)
    V6 = sum_v6 / N6
    variants[f"V6: (1/{N6}) · dim_q V_(2,2) only"] = V6

    # V7: (1/[4]_q) Σ dim_q
    V7 = sum(dim_q.values()) / qint(4)
    variants["V7: Σ dim_q V_λ / [4]_q"] = V7

    # V8: harmonic mean style: 5/Σ(1/dim_q)
    sum_inv = sum(1/d for d in dim_q.values())
    V8 = 5 / sum_inv
    variants["V8: 5/Σ(1/dim_q V_λ) (harmonic)"] = V8

    # Try V9-V12: more variants
    # V9: (1/4) Σ dim_q · (1 + dim_cl·h²)
    # V10: Σ dim_q V_λ · y_λ (Markov weights — gives 5/3 not 5/2, skip)

    # Now expand each in h
    print(f"\n{'Variant':<55s}  {'at q=1':>10s}  {'h² coeff':>14s}  {'value at q_0':>15s}  {'vs target':>10s}")
    print("─" * 110)
    target_at_q0 = float(TARGET_FACTOR)

    results = []
    for name, V in variants.items():
        # Expand in ε — use sp.limit for q→1 to handle q-integer 0/0
        # (Copilot review on PR #751)
        V_at_1 = sp.limit(V, q, 1)
        V_eps = V.subs(q, 1 + eps)
        try:
            V_series = sp.series(V_eps, eps, 0, 6).removeO()
            V_series_s = sp.cancel(V_series)
            # eps^2 coefficient ≈ h²/4 coefficient
            eps2_coeff = V_series_s.coeff(eps, 2)
            h2_coeff = eps2_coeff / 4  # since h = 2ε at leading
        except Exception:
            h2_coeff = "?"
        # Numerical at q_0
        try:
            V_at_q0 = float(V.subs(q, float(Q_NUM)))
        except Exception:
            V_at_q0 = float('nan')
        rel = (V_at_q0 - target_at_q0) / target_at_q0 * 100
        print(f"  {name:<53s}  {str(V_at_1):>10s}  {str(h2_coeff):>14s}  {V_at_q0:>15.10f}  {rel:>+9.3f}%")
        results.append({
            "name": name,
            "value_at_q1": str(V_at_1),
            "h2_coefficient": str(h2_coeff),
            "value_at_q0": V_at_q0,
            "rel_pct_vs_target": rel,
        })

    print()
    print(f"Target: 2.4599534 (CODATA m_p/m_e ·ℏ_q²/Vol(B_3))")
    print(f"  h² coeff target (from empirical 5/2 - h²·G): {-float(G):.6f}")
    print()
    print("VERDICT:")
    best_at_q0 = min(results, key=lambda r: abs(r["rel_pct_vs_target"]))
    print(f"  Closest at q_0: {best_at_q0['name']}")
    print(f"    value = {best_at_q0['value_at_q0']:.6f}, rel = {best_at_q0['rel_pct_vs_target']:+.3f}%")

    w = WitnessBuilder("family-a-variants-investigation", engine="sympy+mpmath")
    w.set_content_block("conj:lambda-scale-substrate-form")  # noqa: linkage per Copilot review on PR #751
    w.set_description(
        "Investigation of Family A variants: 8 natural Wedderburn-sum "
        "normalizations tested for leading 5/2 at q=1 and h² coefficient. "
        "Family A is EXACT (not truncated). Variants test whether other "
        "natural sums close the 3% gap to CODATA."
    )
    # Content-block linkage (Copilot review on PR #751).
    w.set_content_block("conj:flavor-dressed-mass-from-substrate-split")
    w.add_data("target_at_q0", target_at_q0)
    w.add_data("variants", results)
    out = w.save()
    print(f"\nWitness: {out.name}")


if __name__ == "__main__":
    main()
