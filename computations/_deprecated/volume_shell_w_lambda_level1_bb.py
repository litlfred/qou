#!/usr/bin/env python3
"""
Volume + Shell w_λ^(1) probe — path (b): BB-spectral-sequence ansatz.

Per `conj:homological-shell-condensation`, the level-1 weight should
include a BB-spectral-sequence correction beyond the bare Plancherel
restriction to self-conjugate λ. The simple δ(c=0) ansatz gave
complete cancellations at magic atoms (q=1 MN AND q-Hecke); see
2026-05-02-w-lambda-level1-probe-result.md and
2026-05-02-w-lambda-level1-q-hecke.witness.json.

Path (b) tries BB-grade-inspired multipliers that BREAK the
symmetry across self-conjugate λ. Three candidates:

  V1: w_λ · r(λ)            — weighted by Frobenius rank
  V2: w_λ / H_q(λ)           — weighted by inverse hook product
  V3: w_λ · #removable_corners(λ) — weighted by corner count

For each (Z, N), the level-1 sum is:

    m^(1)_BB(Z, N) = Σ_{λ self-conj of 3A} w_λ · M(λ) · χ^λ(W_atom)

where M(λ) is the BB-grade multiplier (V1, V2, or V3).

If any variant breaks the magic-atom cancellation AND correlates
with AME binding/nucleon, that's evidence the BB-grade structure
is the right level-1 weight refinement.
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath

sys.path.insert(0, str(Path(__file__).parent))
from per_braid_tower_hybrid import q0, AME_MASS_MEV
# Extend AME_MASS_MEV with light isotopes not in the base import dict
AME_MASS_MEV.setdefault("6Li", 5603.05182)
AME_MASS_MEV.setdefault("7Li", 6535.36573)
AME_MASS_MEV.setdefault("9Be", 8392.74912)
from enumerate_self_conjugate_partitions import (
    all_self_conjugate_partitions, content_sum,
)
from schur_weyl_mpmath import q_factorial_mp
from murnaghan_nakayama import (
    cycle_type_of_permutation,
    permutation_from_braid_word,
    atomic_braid_word,
    mn_character,
)


def w_lambda_level0(lam: tuple, q: mpmath.mpf,
                     nfac: mpmath.mpf) -> mpmath.mpf:
    if not lam:
        return mpmath.mpf(1)
    qi = 1 / q
    rows = len(lam)
    hp = mpmath.mpf(1)
    for i in range(rows):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, rows) if lam[r] > j)
            h = arm + leg + 1
            hp *= (q ** h - qi ** h) / (q - qi)
    dq = nfac / hp
    return (dq * dq) / nfac


def hook_product_q(lam: tuple, q: mpmath.mpf) -> mpmath.mpf:
    """H_q(λ) = ∏ [h_x]_q over all cells x ∈ λ."""
    if not lam:
        return mpmath.mpf(1)
    qi = 1 / q
    rows = len(lam)
    hp = mpmath.mpf(1)
    for i in range(rows):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, rows) if lam[r] > j)
            h = arm + leg + 1
            hp *= (q ** h - qi ** h) / (q - qi)
    return hp


def frobenius_rank(lam: tuple) -> int:
    """Number of diagonal cells (i, i) with i < λ_i."""
    return sum(1 for i, l in enumerate(lam) if l > i)


def removable_corners_count(lam: tuple) -> int:
    """Number of removable corners (cells (i, λ_i - 1) where removing
    keeps λ a partition)."""
    out = 0
    for i in range(len(lam)):
        if i == len(lam) - 1 or lam[i] > lam[i + 1]:
            out += 1
    return out


VARIANTS = {
    "V1_rank": lambda lam, q: mpmath.mpf(frobenius_rank(lam)),
    "V2_inv_hook": lambda lam, q: 1 / hook_product_q(lam, q),
    "V3_corners": lambda lam, q: mpmath.mpf(removable_corners_count(lam)),
}


def level1_BB(Z: int, N: int, q: mpmath.mpf, variant: str,
                include_inter: bool = True) -> dict:
    A = Z + N
    n = 3 * A
    word = atomic_braid_word(Z, N, include_inter=include_inter)
    perm = permutation_from_braid_word(word, n)
    cyc = cycle_type_of_permutation(perm)
    nfac = q_factorial_mp(n, q)
    parts = all_self_conjugate_partitions(n)
    M = VARIANTS[variant]

    total = mpmath.mpf(0)
    for lam_list in parts:
        lam = tuple(lam_list)
        if content_sum(lam) != 0:
            continue
        chi = mn_character(lam, cyc)
        if chi == 0:
            continue
        w = w_lambda_level0(lam, q, nfac)
        m = M(lam, q)
        total += w * m * mpmath.mpf(chi)
    return {
        "Z": Z, "N": N, "A": A, "variant": variant,
        "total": float(total),
        "abs_total": float(abs(total)),
    }


if __name__ == "__main__":
    print("=" * 88)
    print("Volume + Shell w_λ^(1) probe — path (b) BB-grade variants")
    print("=" * 88)
    print(f"q_0 = {q0}")
    print()

    ATOMS = [
        ("D", 1, 1), ("3He", 2, 1), ("3H", 1, 2), ("4He", 2, 2),
        ("6Li", 3, 3), ("9Be", 4, 5), ("12C", 6, 6), ("16O", 8, 8),
    ]

    rows = []
    for variant in VARIANTS:
        print()
        print("─" * 90)
        print(f"  Variant: {variant}")
        print("─" * 90)
        print(f"  {'atom':>5} {'A':>3} {'|m^(1)_BB|':>16} {'binding/nuc (MeV)':>20}")
        levels = []
        binds = []
        for name, Z, N in ATOMS:
            r = level1_BB(Z, N, q0, variant)
            bn = (938.272 - AME_MASS_MEV[name] / r["A"])
            print(f"  {name:>5} {r['A']:>3} {r['abs_total']:>16.6e} "
                  f"{bn:>20.4f}")
            levels.append(r["abs_total"])
            binds.append(bn)
            rows.append({**r, "atom": name,
                         "binding_per_nucleon_AME": bn})
        # Correlation
        import numpy as np
        if len(levels) > 1:
            corr = np.corrcoef(levels, binds)[0, 1]
            m_4He = next(r["abs_total"] for r in rows
                          if r["atom"] == "4He" and r["variant"] == variant)
            m_16O = next(r["abs_total"] for r in rows
                          if r["atom"] == "16O" and r["variant"] == variant)
            print(f"  Correlation: {corr:+.4f}    "
                  f"4He: {m_4He:.4e}  16O: {m_16O:.4e}")
            if m_4He > 0 and m_16O > 0:
                print(f"  ✓ Magic cancellations BROKEN")
            else:
                print(f"  ✗ Magic cancellations persist")

    out = {
        "computation": "volume-shell-w-lambda-level1-bb-probe",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q0": float(q0),
        "ansatz_summary": (
            "w_λ^(1)_BB = w_λ^(0) · M(λ) · δ(c(λ)=0); three M(λ) variants:\n"
            "  V1 = Frobenius rank,  V2 = 1/H_q(λ),  V3 = #removable corners.\n"
            "Each tries to break the magic-atom cancellation seen at q=1 MN."
        ),
        "atoms": rows,
        "interpretation": (
            "Path (b) of the corrective options. Tests whether BB-grade-"
            "inspired multipliers on self-conjugate Plancherel weights "
            "break the magic-atom cancellation. Variants V1/V2/V3 are "
            "structural surrogates for the full BB-spectral-sequence "
            "weight (which would require explicit GS-filtration "
            "cohomology computation)."
        ),
    }
    out_path = (Path(__file__).parent.parent.parent
                / "docs/audits/2026-05-02-w-lambda-level1-bb.witness.json")
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print()
    print(f"Witness: {out_path.relative_to(Path(__file__).parent.parent.parent)}")
