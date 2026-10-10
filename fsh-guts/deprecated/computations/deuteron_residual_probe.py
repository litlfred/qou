#!/usr/bin/env python3
"""
Probe: does a partition-sum residual close the deuteron 1.23 MeV gap?

Observation: my Schur-Weyl deuteron binding B_pred = 0.995 MeV vs
B_AME = 2.225 MeV.  Gap = 1.23 MeV.

Upstream (residual_partition_sum.py) found: single-proton tower
residual equals m_e · Σ_{λ ⊢ 3} 1/d_λ = (5/2)·m_e = 1.278 MeV
(exact, sub-0.04%).  The proton value (5/2)·m_e is suspiciously
close to my deuteron gap of 1.23 MeV.

Test candidate corrections:

  (a) (5/2) · m_e                        [= 1.278 MeV]
  (b) m_e · Σ_{λ ⊢ 3A = 6} 1/d_λ          [= (473/144)·m_e = 1.676 MeV]
  (c) m_e · (A - 1) · (5/2)              [= 1.278 MeV for A=2]
  (d) m_e · (Σ_{λ ⊢ 6} − 2·Σ_{λ ⊢ 3}) 1/d_λ [= (473/144 − 5)·m_e = -1.843]
  (e) m_e · (2·Σ_{λ ⊢ 3} − Σ_{λ ⊢ 6}) 1/d_λ [= (5 − 473/144)·m_e = +0.844]

All ad hoc — the goal is to see which closed-form matches 1.23 MeV
and thereby hint at the algebraic origin of the missing deuteron term.

Witness: deuteron-residual-probe.witness.json
"""
import json
import sys
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction

sys.path.insert(0, str(Path(__file__).parent))
from experimental_constants import M_E_MEV
from hecke_characters import partitions_of
from murnaghan_nakayama import dim_specht


def sum_inv_d(n):
    """Σ_{λ ⊢ n} 1/d_λ as an exact Fraction."""
    total = Fraction(0)
    for lam in partitions_of(n):
        d = dim_specht(lam)
        total += Fraction(1, d)
    return total


if __name__ == "__main__":
    print("DEUTERON RESIDUAL PROBE")
    print("=" * 72)
    print(f"m_e = {M_E_MEV} MeV")
    print()

    # Observed deuteron gap from deuteron-first-principles.witness.json
    B_pred = 0.995256
    B_AME = 2.224570
    gap = B_AME - B_pred
    print(f"Observed deuteron gap  B_AME - B_pred = {gap:.6f} MeV")
    print()

    # Partition-sum computations
    print("Σ_{λ ⊢ n} 1/d_λ for n = 3, 6, 9, 12:")
    sums = {}
    for n in [3, 6, 9, 12]:
        s = sum_inv_d(n)
        sums[n] = s
        s_float = float(s)
        print(f"  n = {n:>2}: {s} = {s_float:.6f}")
    print()

    # Candidate corrections
    candidates = {
        "(5/2)·m_e":
            float(sums[3]) * M_E_MEV,
        "Σ_{λ⊢6} 1/d_λ · m_e  [= (473/144)·m_e]":
            float(sums[6]) * M_E_MEV,
        "(A-1)·(5/2)·m_e = 1·(5/2)·m_e":
            1 * float(sums[3]) * M_E_MEV,
        "(Σ_{λ⊢6} − Σ_{λ⊢3}) · m_e":
            float(sums[6] - sums[3]) * M_E_MEV,
        "(2·Σ_{λ⊢3} − Σ_{λ⊢6}) · m_e":
            float(2 * sums[3] - sums[6]) * M_E_MEV,
        "(Σ_{λ⊢3})² / Σ_{λ⊢6} · m_e":
            float(sums[3] ** 2 / sums[6]) * M_E_MEV,
        "A · m_e [= 2·m_e]":
            2 * M_E_MEV,
        "(3A − 1) · m_e [= 5·m_e]":
            5 * M_E_MEV,
        "[3]_q · m_e  approximation":
            (1 + 2 * 1.1099786) * M_E_MEV * 0.25,  # placeholder
    }

    print("Candidate corrections vs observed gap:")
    print(f"  {'formula':<50}  {'value (MeV)':>12}  {'gap diff':>10}  {'%':>7}")
    print("  " + "-" * 85)
    results = {}
    for name, val in candidates.items():
        diff = val - gap
        pct = (val - gap) / gap * 100
        match = "★" if abs(pct) < 5 else " "
        print(f"  {name:<50}  {val:>12.6f}  {diff:>+10.6f}  "
              f"{pct:>+6.2f}% {match}")
        results[name] = {
            "value_MeV": val,
            "diff_vs_gap_MeV": diff,
            "rel_err_pct": pct,
        }

    # Best additive match
    best_name = min(results, key=lambda n: abs(results[n]["rel_err_pct"]))
    print()
    print(f"Best match: {best_name}")
    print(f"  closes gap to within {abs(results[best_name]['rel_err_pct']):.2f}%")
    print(f"  implied B_pred + correction = "
          f"{B_pred + results[best_name]['value_MeV']:.6f} MeV")
    print(f"  B_AME                         = {B_AME:.6f} MeV")

    witness = {
        "computation": "deuteron-residual-probe",
        "description": (
            "Empirical probe: does a partition-sum residual close the "
            "deuteron 1.23 MeV gap between my Schur-Weyl B_pred and "
            "B_AME?  Tests several closed-form candidates against the "
            "observed gap."
        ),
        "reference_blocks": [
            "rem:deuteron-first-principles",
            "prop:partition-sum-proton-residual",
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "m_e_MeV": M_E_MEV,
            "B_pred_MeV": B_pred,
            "B_AME_MeV": B_AME,
            "gap_MeV": gap,
        },
        "partition_sums": {str(n): str(s) for n, s in sums.items()},
        "candidates": results,
        "best_match": {
            "name": best_name,
            "rel_err_pct": results[best_name]["rel_err_pct"],
        },
    }
    out = Path(__file__).parent / "deuteron-residual-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
