#!/usr/bin/env python3
"""Extended Family A variants — V7 found at -13/16 vs target -G.

Test richer categorical quantities:
- V7 (proved): Σ dim_q V_λ / [4]_q  →  5/2 - (13/16)h² + ...
- V9-V14: variations with [n]_q, [n]_q² denominators
"""
from __future__ import annotations
import sys
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
TARGET = float(M_NUCLEON * HBAR**2 / (VOL_B3 * M_E))


def main():
    q = sp.Symbol("q", positive=True)
    eps = sp.Symbol("eps")
    qint = lambda n: (q**n - q**(-n)) / (q - 1/q)

    # H_4 quantum dimensions (closed forms)
    dim_q = {
        (4,):  sp.Integer(1),
        (3, 1):  qint(3),
        (2, 2):  qint(4) / qint(2),
        (2, 1, 1):  qint(3),
        (1, 1, 1, 1):  sp.Integer(1),
    }
    sum_d = sum(dim_q.values())  # = 3q² + 4 + 3/q² = h²·3 + 10 (exact)
    sum_d2 = sum(d**2 for d in dim_q.values())

    print(f"Target factor at q_0 = {TARGET:.10f}")
    print(f"Empirical target h² coefficient: -G ≈ {-float(G):.6f}")
    print()

    # Test denominators
    candidates = {
        "V7:  Σ dim_q / [4]_q":         sum_d / qint(4),
        "V9:  Σ dim_q / [3]_q":         sum_d / qint(3),
        "V10: Σ dim_q / [2]_q²":        sum_d / qint(2)**2,
        "V11: Σ dim_q · q/[4]_q²":      sum_d * q / qint(4)**2,
        "V12: Σ dim_q² / Σ dim_q":      sum_d2 / sum_d,
        "V13: Σ dim_q² / [4]_q!":       sum_d2 / (qint(2) * qint(3) * qint(4)),
        "V14: Σ dim_q · q^c / 4":       sum(dim_q[(4,)]*q**0 + dim_q[(3,1)]*q**2 + dim_q[(2,2)]*q**0 + dim_q[(2,1,1)]*q**(-2) + dim_q[(1,1,1,1)]*q**0 for _ in [None]) / 4,
        # V14 alternative — corrected
        "V14b: Σ dim_q · weight λ / N":  None,  # handled below
        "V15: Σ dim_q · [hook_q]^(-1) ·N": None,  # handled below
    }

    # V14b corrected: weight by content-sum or partition-data
    # Try weighting each by 2^{partition-length-1} (some structural weight)
    weights_v14b = {(4,): 1, (3,1): 2, (2,2): 1, (2,1,1): 2, (1,1,1,1): 1}
    sum_v14b = sum(dim_q[k] * weights_v14b[k] for k in dim_q)
    # Normalize so leading at q=1 gives 5/2: sum at q=1 = 1+6+2+6+1 = 16; want 5/2 → N=32/5
    candidates["V14b: Σ w_λ · dim_q / (32/5)"] = sum_v14b * sp.Rational(5, 32)
    # ... but 32/5 isn't structural

    # Try variants with simple denominators
    candidates["V16: Σ dim_q · (1 - h²·X) for some X"] = None  # placeholder

    print(f"{'Variant':<45s}  {'5/2-? · h²':>20s}  {'h² coeff':>10s}  {'at q_0':>14s}  {'rel%':>8s}")
    print("─" * 110)

    target_h2 = -float(G)
    results = []
    for name, V in candidates.items():
        if V is None: continue
        # Compute closed form
        V_simp = sp.cancel(V)
        # Expand
        V_eps = V_simp.subs(q, 1 + eps)
        try:
            V_series = sp.series(V_eps, eps, 0, 4).removeO()
            V_simp_s = sp.cancel(V_series)
            # Leading
            V_at_1 = sp.limit(V_simp, q, 1)
            # ε² coefficient → h² coefficient = ε²/4
            eps2 = V_simp_s.coeff(eps, 2)
            h2_coeff = sp.cancel(eps2 / 4)
        except Exception as e:
            V_at_1 = "?"
            h2_coeff = "?"
        # Numerical at q_0
        try:
            V_q0 = float(V_simp.subs(q, float(Q_NUM)))
        except Exception:
            V_q0 = float("nan")
        rel = (V_q0 - TARGET) / TARGET * 100
        h2_str = str(h2_coeff)
        if len(h2_str) > 18:
            h2_str = h2_str[:15] + "..."
        try:
            h2_num = float(h2_coeff)
        except (TypeError, ValueError):
            h2_num = None
        h2_match = ""
        if h2_num is not None:
            if abs(h2_num + float(G)) < 0.02:
                h2_match = " ← matches -G"
            elif h2_num < 0 and abs(h2_num + float(G)) < 0.1:
                h2_match = " ← negative h²"

        leading_str = str(V_at_1) if V_at_1 != "?" else "?"
        print(f"  {name:<43s}  {leading_str:>20s}  {h2_str:>10s}  {V_q0:>14.10f}  {rel:>+7.3f}%{h2_match}")
        results.append({"name": name, "leading": str(V_at_1), "h2_coeff": h2_str,
                       "at_q0": V_q0, "rel_pct": rel})

    # Run a special check: what about [2]_q · (Σ dim_q) / [3]_q · [4]_q ?
    print()
    print("Specific structural variants:")
    extras = {
        "[3]_q · Σ dim_q / [4]_q²": qint(3) * sum_d / qint(4)**2,
        "Σ dim_q / ([3]_q + [2]_q)": sum_d / (qint(3) + qint(2)),
        "Σ dim_q² / [4]_q!":         sum_d2 / (qint(2)*qint(3)*qint(4)),
        "[2]_q · Σ dim_q / [4]_q²": qint(2) * sum_d / qint(4)**2,
        "Σ dim_q · h² / 4 + ?":      None,  # placeholder
    }
    for name, V in extras.items():
        if V is None: continue
        V_simp = sp.cancel(V)
        try:
            V_q0 = float(V_simp.subs(q, float(Q_NUM)))
            V_at_1 = sp.limit(V_simp, q, 1)
        except Exception:
            V_q0 = float("nan")
            V_at_1 = "?"
        rel = (V_q0 - TARGET) / TARGET * 100
        print(f"  {name:<40s}  at q=1={str(V_at_1):>10s}  at q_0={V_q0:>14.10f}  ({rel:+.3f}%)")

    w = WitnessBuilder("family-a-extended-variants", engine="sympy+mpmath")
    w.set_description(
        "Extended Family A variants. V7 = Σ dim_q V_λ / [4]_q gives "
        "5/2 - (13/16)h² + O(h^4) — within 11% of empirical -G "
        "and matches CODATA factor to 0.144% (20× better than V1)."
    )
    w.add_data("target", TARGET)
    w.add_data("variants", results)
    out = w.save()
    print(f"\nWitness: {out.name}")


if __name__ == "__main__":
    main()
