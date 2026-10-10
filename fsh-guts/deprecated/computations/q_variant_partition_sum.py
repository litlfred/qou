#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical/intermediate-sympy witness; no symbolic-q polynomial in output.
"""
q-variants of Σ_{λ⊢3} 1/d_λ tested against deuteron binding gap.

Classical: Σ_{λ⊢3} 1/d_λ = 1/1 + 1/2 + 1/1 = 5/2 → 5/2 · m_e = 1.2775 MeV
Deuteron gap (from deuteron_residual_probe.py): 1.2293 MeV (3.92% below 5/2·m_e).

Candidate q-deformations:

  (A) Σ 1/dim_q(λ) — using q-hook-length dimension:
      dim_q((3))     = 1
      dim_q((2,1))   = [2]_q
      dim_q((1,1,1)) = 1
      Sum = 2 + 1/[2]_q

  (B) Σ 1/H_q(λ) — using raw q-hook products (not normalised):
      H_q((3)) = [3][2][1],  H_q((2,1)) = [3],  H_q((1,1,1)) = [3][2][1]

  (C) Σ w_λ / d_λ = Σ (dim_q² / [3]!_q) / d_λ — Wedderburn-weighted.

  (D) (5/2)_q — naive q-rational with q-factorial-like ratio.

  (E) Σ dim_q(λ) / [3]!_q — partition of unity type sum (should = 1 exactly
      since w_λ = dim_q(λ) is the rank-squared over q-factorial).
      Wait, that's Σ dim_q² / [3]!_q (by Wedderburn).

  (F) q-Catalan number or other named q-deformation.

All evaluated at q_0 ≈ 1.10998 and compared to 1.2293 MeV gap.

Witness: q-variant-partition-sum.witness.json
"""
import json
import sys
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction

import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from experimental_constants import M_E_MEV
from q_parameter import Q as _Q_CANONICAL

q0 = _Q_CANONICAL
q0_mp = sp.Rational(int(q0 * 10**16), 10**16)


def q_int(k, q=q0_mp):
    """[k]_q = (q^k - q^{-k}) / (q - q^{-1})."""
    if k == 0:
        return sp.Integer(0)
    return (q**k - q**(-k)) / (q - q**(-1))


def q_factorial(n, q=q0_mp):
    return sp.prod(q_int(k, q) for k in range(1, n + 1))


def q_binomial(n, k, q=q0_mp):
    return q_factorial(n, q) / (q_factorial(k, q) * q_factorial(n - k, q))


if __name__ == "__main__":
    print("q-VARIANTS of Σ_{λ⊢3} 1/d_λ vs deuteron binding gap")
    print("=" * 72)
    print(f"q_0 = {q0}")
    print(f"m_e = {M_E_MEV} MeV")
    gap = 1.229314
    print(f"deuteron gap = {gap} MeV\n")

    # Classical reference
    classical = sp.Rational(5, 2)
    print(f"(ref)  Σ 1/d_λ (classical)       = 5/2 = {float(classical):.6f}  "
          f"→ {float(classical) * M_E_MEV:.6f} MeV  "
          f"[{(float(classical) * M_E_MEV - gap)/gap*100:+.3f}%]")
    print()

    candidates = {}

    # (A) Σ 1/dim_q(λ):  dim_q((3))=1, dim_q((2,1))=[2]_q, dim_q((1,1,1))=1
    A_sum = sp.Integer(1) + 1 / q_int(2) + sp.Integer(1)
    candidates["(A) Σ 1/dim_q(λ) = 2 + 1/[2]_q"] = A_sum

    # (B) Σ 1/H_q(λ) — raw hook product
    H_3 = q_int(3) * q_int(2) * q_int(1)    # (3)
    H_21 = q_int(3) * q_int(1) * q_int(1)   # (2,1) hooks are 3,1,1
    H_111 = q_int(3) * q_int(2) * q_int(1)  # (1,1,1)
    B_sum = 1/H_3 + 1/H_21 + 1/H_111
    candidates["(B) Σ 1/H_q(λ) (raw hook products)"] = B_sum

    # (C) Σ dim_q(λ) · 1/d_λ (mix classical dim d_λ with q-dim weight)
    # d_(3) = 1, d_(2,1) = 2, d_(1,1,1) = 1
    C_sum = sp.Integer(1) / 1 + q_int(2) / 2 + sp.Integer(1) / 1
    candidates["(C) Σ dim_q(λ)/d_λ = 2 + [2]_q/2"] = C_sum

    # (D) (5/2)_q as q-integer ratio: [5]_q / [2]_q (classical: 5/2)
    D_sum = q_int(5) / q_int(2)
    candidates["(D) [5]_q / [2]_q"] = D_sum

    # (E) Σ dim_q(λ)² / [3]!_q   (should equal 1 by Schur-Weyl / Wedderburn)
    E_sum = (1**2 + q_int(2)**2 + 1**2) / q_factorial(3)
    candidates["(E) Σ dim_q(λ)² / [3]!_q = 1 (Wedderburn check)"] = E_sum

    # (F) Σ [dim_q(λ)] / [3]!_q × d_λ — q-deformation using both
    F_sum = (1 * 1 + q_int(2) * 2 + 1 * 1) / q_factorial(3)
    candidates["(F) Σ d_λ · dim_q(λ) / [3]!_q"] = F_sum

    # (G) 5/2 replaced by [5]_q / [2]_q + correction
    G_sum = q_int(5) / q_int(2) - sp.Rational(1, 2) * (q0_mp - 1/q0_mp)
    candidates["(G) [5]_q/[2]_q − (q − q⁻¹)/2"] = G_sum

    # (H) Σ 1/[d_λ]_q — classical d_λ wrapped as q-integer
    # [1]_q = 1, [2]_q, [1]_q = 1
    H_sum = 1 + 1/q_int(2) + 1
    candidates["(H) Σ 1/[d_λ]_q (same as (A))"] = H_sum

    # (I) Σ_λ 1/(dim_q(λ) · d_λ) — both weights
    I_sum = sp.Rational(1, 1)*1 + sp.Rational(1, 2)/q_int(2) + sp.Rational(1, 1)*1
    candidates["(I) Σ 1/(dim_q(λ)·d_λ) = 2 + 1/(2·[2]_q)"] = I_sum

    results = {}
    print(f"  {'formula':<50}  {'sum':>16}  {'×m_e (MeV)':>12}  {'vs gap':>8}")
    print("  " + "-" * 94)
    for name, expr in candidates.items():
        s_float = float(expr.evalf(30))
        mev = s_float * M_E_MEV
        diff_pct = (mev - gap) / gap * 100
        match = "★" if abs(diff_pct) < 3 else (" " if abs(diff_pct) > 20 else "·")
        s_simpl = sp.nsimplify(expr, rational=False)
        try:
            s_str = f"{float(s_simpl):.6f}"
        except Exception:
            s_str = str(s_simpl)[:16]
        print(f"  {name:<50}  {s_str:>16}  {mev:>12.6f}  "
              f"{diff_pct:>+7.3f}% {match}")
        results[name] = {
            "symbolic": str(sp.nsimplify(expr)),
            "value_at_q0": s_float,
            "value_MeV": mev,
            "diff_vs_gap_pct": diff_pct,
        }

    best = min(results, key=lambda n: abs(results[n]["diff_vs_gap_pct"]))
    print()
    print(f"Best match: {best}")
    print(f"  diff = {results[best]['diff_vs_gap_pct']:+.3f}% vs gap")
    print(f"  value @ q_0 = {results[best]['value_at_q0']}")
    print(f"  symbolic    = {results[best]['symbolic']}")

    witness = {
        "computation": "q-variant-partition-sum",
        "description": (
            "q-deformations of Σ_{λ⊢3} 1/d_λ = 5/2 tested against the "
            "deuteron binding gap (1.229 MeV after the Schur-Weyl "
            "first-principles prediction).  Classical (5/2)·m_e closes "
            "gap to 3.92%; q-variants may do better."
        ),
        "reference_blocks": [
            "prop:partition-sum-proton-residual",
            "rem:deuteron-first-principles",
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": str(q0),
            "m_e_MeV": M_E_MEV,
            "deuteron_gap_MeV": gap,
        },
        "classical_reference": {
            "formula": "Σ_{λ⊢3} 1/d_λ = 5/2",
            "value_MeV": float(classical) * M_E_MEV,
            "diff_vs_gap_pct": (float(classical) * M_E_MEV - gap) / gap * 100,
        },
        "q_variants": results,
        "best": best,
    }
    out = Path(__file__).parent / "q-variant-partition-sum.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
