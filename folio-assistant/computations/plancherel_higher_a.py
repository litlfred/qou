#!/usr/bin/env python3
"""
Test Plancherel weighting (1/dim_q² instead of 1/dim_q) for the
k=3A self-conjugate correction at higher A.

Motivation: current Scheme C (1/dim_q) gives:
  3A=12 (4He):  Σ H_q/dim_q  ≈ 130    → -33 MeV (works, +2.5%)
  3A=18 (6Li):  Σ H_q/dim_q  ≈ 65k    → diverges
  3A=21 (7Li):  Σ H_q/dim_q  ≈ 363M   → diverges

Plancherel (1/dim_q²) is the natural Markov-trace weight from the
Wedderburn-Plancherel decomposition of H_n(q):
  tr_M = Σ_λ (dim_q²/[n]_q!) · χ_λ/dim_q

Try several power scalings 1/dim_q^p for p = 1.0, 1.5, 2.0.
"""
from __future__ import annotations
import sys, warnings
from pathlib import Path

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 30

from hecke_characters import dim_q, young_hooks, partitions_of
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
me = mp.mpf(str(M_E_MEV))

def q_int(n): return (Q0**n - QI**n) / (Q0 - QI)
def q_fact(n):
    out = mp.mpf(1)
    for i in range(2, n+1): out *= q_int(i)
    return out
def transpose_partition(lam):
    if not lam: return tuple()
    return tuple(sum(1 for p in lam if p > j) for j in range(lam[0]))
def hook_product_q(lam):
    out = mp.mpf(1)
    for h in young_hooks(lam): out *= q_int(int(h))
    return out
def dim_q_lam(lam):
    return q_fact(sum(lam)) / hook_product_q(lam)
def self_conjugate(n):
    return [tuple(lam) for lam in partitions_of(n)
             if transpose_partition(tuple(lam)) == tuple(lam)]


def main():
    print("=" * 100)
    print("Plancherel test: k=3A self-conjugate sums under different normalizations")
    print("=" * 100)
    print()

    # Required sum for each isotope to give correct binding (back-solving)
    # Δ_3A = -m_e · Σ · min(Z,N)/A → Σ_target = -Δ_target / (m_e · min/A)
    #   4He: Δ ≈ -29 MeV (after other corrections), m_e·0.5 = 0.255 → Σ ≈ 113
    #   6Li: Δ ≈ -32 MeV, m_e·0.5 = 0.255 → Σ ≈ 125
    #   So Σ around 100-130 needed for both — flat in A is the goal.

    targets = {12: 130, 18: 100, 21: 80}  # rough targets (small variation)

    print(f"  {'3A':>3} {'#λ':>3} {'p=1.0':>14} {'p=1.5':>14} {'p=2.0':>14} {'p=3.0':>14} {'target':>9}")
    for n in [3, 6, 9, 12, 18, 21]:
        sc = self_conjugate(n)
        sums = {}
        for p in [1.0, 1.5, 2.0, 3.0]:
            s = sum(hook_product_q(lam) / (dim_q_lam(lam) ** p) for lam in sc)
            sums[p] = float(s)
        target = targets.get(n, 'n/a')
        print(f"  {n:>3} {len(sc):>3} {sums[1.0]:>14.4e} {sums[1.5]:>14.4e} "
              f"{sums[2.0]:>14.4e} {sums[3.0]:>14.4e} {str(target):>9}")
    print()
    print("  Reading: target column shows ROUGH desired magnitude for the k=3A correction.")
    print("  The right power p makes Σ stay near the target across A.")


if __name__ == "__main__":
    main()
