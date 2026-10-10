#!/usr/bin/env python3
"""
High-precision (80-digit mpmath) computation of Σ_λ 1/dim_q(λ) at
q = q_0 for n = 3, 6, 9, 11.  Verifies the analytical identity
2 + 1/[2]_q = Σ at n=3.

Then compares per-vortex (A × n=3), per-atom (n=3A), and universal
(n=3) interpretations of the Frobenius co-Casimir correction for
light isotopes.
"""
from __future__ import annotations

import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 80

from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from hecke_characters import partitions_of, young_hooks

Q0 = Q_MP  # was f64 roundtrip
QI = Q_INV_MP
me = mp.mpf('0.51099895')


def q_int_n(n):
    return (Q0**n - QI**n) / (Q0 - QI)


def q_fact_n(n):
    out = mp.mpf(1)
    for k in range(2, n + 1):
        out *= q_int_n(k)
    return out


def dim_q_mp(shape):
    """Q-deformed dim via q-hook-length formula at 80 digits."""
    n = sum(shape)
    hooks = young_hooks(shape)
    num = q_fact_n(n)
    den = mp.mpf(1)
    for h_ in hooks:
        den *= q_int_n(h_)
    return num / den


def sum_inv_dim_q(n):
    total = mp.mpf(0)
    for shape in partitions_of(n):
        d = dim_q_mp(shape)
        if d > 0:
            total += 1 / d
    return total


def classical_dim(shape) -> int:
    nn = sum(shape); hooks = young_hooks(shape)
    f = 1
    for k in range(2, nn + 1): f *= k
    hp = 1
    for x in hooks: hp *= x
    return f // hp


def sum_inv_classical(n) -> Fraction:
    total = Fraction(0)
    for shape in partitions_of(n):
        d = classical_dim(shape)
        if d > 0:
            total += Fraction(1, d)
    return total


def main() -> int:
    print("=" * 100)
    print("HIGH-PRECISION Frobenius co-Casimir trace Σ 1/dim_q(λ)")
    print("=" * 100)
    print(f"  dps = 80,  q_0 = {Q0_FLOAT}")
    print()

    # Verify n=3 identity
    s_n3 = sum_inv_dim_q(3)
    b2 = Q0 + QI
    analytical = 2 + 1 / b2
    print(f"  n = 3:  Σ 1/dim_q(λ) = {mp.nstr(s_n3, 40)}")
    print(f"          2 + 1/[2]_q   = {mp.nstr(analytical, 40)}")
    print(f"          diff          = {mp.nstr(s_n3 - analytical, 30)}  (should be 0)")
    print()

    # High-prec values for n = 3, 6, 9, 11
    print(f"  {'n':>4} {'Σ 1/dim_q(λ)  [q_0]':>30} "
          f"{'Σ 1/d_λ  [classical]':>25} "
          f"{'m_e · Σ (MeV)':>16}")
    results = []
    for n in [3, 6, 9, 11]:
        s_q = sum_inv_dim_q(n)
        s_c = sum_inv_classical(n)
        corr = s_q * me
        print(f"  {n:>4} {mp.nstr(s_q, 22):>30} {str(s_c)[:25]:>25} "
              f"{mp.nstr(corr, 12):>16}")
        results.append({
            "n": n,
            "sum_inv_dim_q_q0": mp.nstr(s_q, 50),
            "sum_inv_dim_classical": str(s_c),
            "m_e_correction_MeV": mp.nstr(corr, 25),
        })

    # Per-vortex vs per-atom interpretation
    print()
    print("=" * 100)
    print("Per-vortex (A × n=3) vs per-atom (n=3A) vs universal (single n=3)")
    print("=" * 100)
    print(f"  {'A':>3} {'per-vortex (A·n=3)':>22} {'per-atom (n=3A)':>20} "
          f"{'universal (n=3)':>18} {'B_CODATA':>12}")
    iso_map = {1: ('p', 0), 2: ('D', 2.22456612), 3: ('T', 8.48),
                4: ('⁴He', 28.30)}
    n3_value_MeV = float(s_n3 * me)
    for A in [1, 2, 3, 4]:
        label, B = iso_map[A]
        if 3 * A <= 11:
            s_full = sum_inv_dim_q(3 * A)
            per_atom = float(s_full * me)
        else:
            per_atom = float("nan")
        per_vortex = A * n3_value_MeV
        universal = n3_value_MeV
        print(f"  {A:>3} {per_vortex:>22.4f} {per_atom:>20.4f} "
              f"{universal:>18.4f} {B:>12}")

    # Save witness
    witness = {
        "computation": "frobenius-high-prec",
        "description": (
            "High-precision (80-digit) Σ 1/dim_q(λ) at q_0 for "
            "n = 3, 6, 9, 11.  Verifies analytical closed form "
            "2 + 1/[2]_q at n=3.  Compares per-vortex, per-atom, "
            "universal Frobenius interpretations."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "q_0": Q0_FLOAT,
        "dps_used": 80,
        "n_table": results,
        "n3_value_MeV": mp.nstr(s_n3 * me, 30),
    }
    out = Path(__file__).parent / "frobenius-high-prec.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
