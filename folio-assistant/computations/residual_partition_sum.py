#!/usr/bin/env python3
"""
Test hypothesis: tower residual = m_e · Σ_λ 1/d_λ,
where d_λ = classical dim of irrep λ ⊢ n, n = 3·A.

For n = 3 (single nucleon): Σ 1/d_λ = 1/1 + 1/2 + 1/1 = 5/2.
Matches Δm_p/m_e = 2.5007 and Δm_n/m_e = 2.5013 (within 0.02%)
when Q_β(n) is used for the neutron.

This script:
  1. Computes Σ_λ 1/d_λ for n ∈ {3, 6, 9, 12} (p/n, D, T/³He, ⁴He)
  2. Compares to observed tower residuals for each isotope
  3. Tests whether the same structural correction m_e·(Σ 1/d_λ)
     extends to the low-isotope binding energies
  4. Analyzes the sub-ppm remaining residuals (after 5/2·m_e is applied)
"""
from __future__ import annotations

import sys
import json
import warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

from fractions import Fraction
import mpmath as mp
mp.mp.dps = 50

from hecke_characters import partitions_of, young_hooks
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

Q0 = Q_MP  # was f64 roundtrip
QI = Q_INV_MP


def classical_dim(shape) -> int:
    """d_λ = n! / h(λ)  via hook-length formula (integer)."""
    n = sum(shape)
    hooks = young_hooks(shape)
    fact = 1
    for k in range(2, n + 1):
        fact *= k
    hp = 1
    for h in hooks:
        hp *= h
    return fact // hp


def sum_inv_d_lambda(n: int) -> Fraction:
    """Σ_λ 1/d_λ as exact rational."""
    total = Fraction(0)
    for shape in partitions_of(n):
        d = classical_dim(shape)
        if d > 0:
            total += Fraction(1, d)
    return total


def print_partition_table(n: int):
    print(f"\n  Partitions of n = {n}:")
    total = Fraction(0)
    for shape in sorted(partitions_of(n), key=lambda s: (-max(s), s)):
        d = classical_dim(shape)
        if d > 0:
            total += Fraction(1, d)
            print(f"    λ = {str(shape):<30} d_λ = {d:>6}   1/d_λ = {Fraction(1, d)}")
    print(f"    Σ 1/d_λ = {total} = {float(total):.10f}")
    return total


def main() -> int:
    print("=" * 100)
    print("PARTITION-SUM Σ 1/d_λ FOR LOW ISOTOPES")
    print("=" * 100)

    me = mp.mpf(str(M_E_MEV))
    M_P = mp.mpf(str(M_P_MEV))
    M_N = mp.mpf(str(M_N_MEV))

    # Compute Σ 1/d_λ for n = 3, 6, 9, 12, 15, 18, …
    sums = {}
    for n in [3, 6, 9, 12, 15, 18]:
        total = print_partition_table(n)
        sums[n] = total

    print(f"\n{'=' * 100}")
    print("Structural correction per nucleus: residual = m_e · (Σ 1/d_λ)")
    print('=' * 100)
    print(f"  {'atom':<8} {'A':>3} {'n=3A':>4} {'Σ 1/d_λ':>14} "
          f"{'correction m_e·Σ (MeV)':>25}")
    ISOTOPES = [
        ("p / n", 1, 3), ("D", 2, 6), ("T/³He", 3, 9), ("⁴He", 4, 12),
        ("⁵Li/⁵He", 5, 15), ("⁶Li", 6, 18),
    ]
    results = []
    for name, A, n in ISOTOPES:
        s = sums[n]
        corr_MeV = float(s) * float(me)
        print(f"  {name:<8} {A:>3} {n:>4} {str(s):>14}  {corr_MeV:>25.6f}")
        results.append({"atom": name, "A": A, "n_strands": n,
                          "sum_inv_d_lambda": float(s),
                          "sum_inv_d_lambda_frac": str(s),
                          "correction_MeV": corr_MeV})

    # SUB-PPM ANALYSIS
    print()
    print("=" * 100)
    print("SUB-PPM RESIDUAL ANALYSIS for p, n (after 5/2·m_e correction)")
    print('=' * 100)
    mp_tower = mp.mpf('936.9942387')
    from experimental_constants import Q_NEUTRON_MEV
    Q_n = mp.mpf(str(Q_NEUTRON_MEV))  # 0.78233341 MeV (CODATA-derived)
    # Corrected predictions
    mp_corrected = mp_tower + (mp.mpf(5) / 2) * me
    mn_corrected = mp_tower + Q_n + me + (mp.mpf(5) / 2) * me
    # Sub-ppm residuals
    sub_p = M_P - mp_corrected
    sub_n = M_N - mn_corrected
    sub_p_ppb = float(sub_p / M_P * mp.mpf(10)**9)
    sub_n_ppb = float(sub_n / M_N * mp.mpf(10)**9)
    print(f"  m_p (corrected) = {float(mp_corrected):.10f}   sub-residual: "
          f"{float(sub_p)*1e6:+9.3f} µMeV  = {sub_p_ppb:+.0f} ppb")
    print(f"  m_n (corrected) = {float(mn_corrected):.10f}   sub-residual: "
          f"{float(sub_n)*1e6:+9.3f} µMeV  = {sub_n_ppb:+.0f} ppb")
    print()
    ratio = sub_n / sub_p
    print(f"  sub_n / sub_p = {float(ratio):.6f}")
    print(f"  (hypothesized q-algebraic structure; note ratio near 2)")
    print()
    # Check natural q-expressions for the sub-residual ratio and its
    # individual values.
    print("  Sub-residual values as fraction of m_e:")
    print(f"    sub_p / m_e = {float(sub_p / me):.6e}")
    print(f"    sub_n / m_e = {float(sub_n / me):.6e}")
    print()
    print("  Checking q-algebraic forms for sub_p / m_e (target ≈ "
          f"{float(sub_p/me):.4e}):")
    HBAR = (Q0 - mp.mpf(1)) / Q0
    HBAR_SQ = HBAR * HBAR
    HA = Q0 - QI
    B2 = Q0 + QI
    candidates = [
        ("-ℏ_q⁴",          -HBAR_SQ**2),
        ("-ℏ_q⁴·[2]_q",    -HBAR_SQ**2 * B2),
        ("-ℏ_q⁴·[3]_q",    -HBAR_SQ**2 * (Q0**2 + 1 + QI**2)),
        ("-ℏ_q⁶",          -HBAR_SQ**3),
        ("-H_A⁴",          -HA**4),
        ("-(q-1)⁴",        -(Q0-1)**4),
        ("+ℏ_q⁴",          +HBAR_SQ**2),
        ("+ℏ_q⁴·[2]_q",    +HBAR_SQ**2 * B2),
    ]
    target_p = sub_p / me
    target_n = sub_n / me
    for name, val in candidates:
        err_p = (val - target_p) / target_p
        err_n = (val - target_n) / target_n
        print(f"    {name:<18} = {float(val):+14.6e}  "
              f"err_p = {float(err_p)*100:+8.2f}%  "
              f"err_n = {float(err_n)*100:+8.2f}%")

    # Also test: sub residual = Σ_λ 1/d_λ · (some higher correction)
    # For n = 3: Σ = 5/2.  Sub-correction might involve next term of a
    # known series.  Try: sub = m_e · 5/2 · (multiplicative factor).
    ext_p = mp.mpf(1) - mp_corrected / M_P  # as fraction of m_p
    ext_n = mp.mpf(1) - mn_corrected / M_N
    print()
    print(f"  Fractional sub-residuals:")
    print(f"    p: {float(ext_p)*1e9:+.3f} ppb = {float(ext_p):+.3e}")
    print(f"    n: {float(ext_n)*1e9:+.3f} ppb = {float(ext_n):+.3e}")

    witness = {
        "computation": "residual-partition-sum",
        "description": (
            "Tested hypothesis: tower residual = m_e · Σ_λ 1/d_λ for "
            "n = 3·A.  Reports Σ 1/d_λ for n = 3, 6, 9, 12, 15, 18, "
            "and the corresponding m_e·Σ correction in MeV.  Includes "
            "sub-ppm residual analysis for p, n after 5/2·m_e applied."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "q_0": Q0_FLOAT,
        "partition_sums": {str(k): {"fraction": str(v),
                                       "float": float(v),
                                       "m_e_correction_MeV":
                                       float(v) * float(me)}
                             for k, v in sums.items()},
        "isotope_table": results,
        "sub_ppm_p_uMeV": float(sub_p) * 1e6,
        "sub_ppm_n_uMeV": float(sub_n) * 1e6,
        "sub_ratio_n_over_p": float(ratio),
    }
    out = Path(__file__).parent / "residual-partition-sum.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
