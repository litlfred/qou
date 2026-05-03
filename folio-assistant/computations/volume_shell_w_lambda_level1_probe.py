#!/usr/bin/env python3
"""
Volume + Shell w_λ^(1) derivation probe.

Per conj:homological-shell-condensation, the level-1 Plancherel
weight w_λ^(1) is enriched on self-conjugate partitions (content
sum c(λ) = 0). At saturated n (magic numbers), E_∞^(p,>0) = 0
collapses the spectral sequence, contributing all level-1
content to those partitions.

Candidate ansatz:

    w_λ^(1) = w_λ^(0) · δ(c(λ)=0)
            = (d_q(λ)² / [n]_q!) · δ(c(λ)=0)

i.e., the standard Plancherel weight, restricted to self-conjugate
λ. Level-1 contribution to atom (Z, N) at strand count n=3A:

    m^(1)(Z, N) = Σ_{λ ⊢ 3A, c(λ)=0} w_λ^(1) · χ^λ_q(W_atom)

This probe computes the level-1 sum for each atom and asks:
- Does it match a Volume term (∝ A) at low A?
- Does it spike at magic shells (A = 4, 16, 40)?
- Does the partition character's q-deformation (vs MN q=1 limit)
  give p/n distinction?

Negative results are also informative — they would say the simple
δ(c=0) ansatz is too crude, and the actual w_λ^(1) needs the full
BB-spectral-sequence structure.
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath

sys.path.insert(0, str(Path(__file__).parent))
from per_braid_tower_hybrid import q0, M_E_MEV, AME_MASS_MEV
from enumerate_self_conjugate_partitions import (
    all_self_conjugate_partitions, content_sum,
)
from schur_weyl_mpmath import schur_weyl_weight_mp, q_factorial_mp
from murnaghan_nakayama import (
    cycle_type_of_permutation,
    permutation_from_braid_word,
    atomic_braid_word,
    mn_character,
)


def w_lambda_level0(lam: tuple, q: mpmath.mpf, nfac: mpmath.mpf) -> mpmath.mpf:
    """Standard Plancherel weight d_q(λ)² / [n]_q!.

    Reuses schur_weyl_weight_mp which gives s_λ(q,q⁻¹)/H_q(λ),
    the 2-variable specialisation. For length > 2 this returns 0
    — but we WANT length > 2 in this probe!
    Fallback: q-dim²/q-fact computed directly from the partition.
    """
    n = sum(lam)
    if not lam:
        return mpmath.mpf(1)
    # Compute q-dim via hook lengths
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


def level1_contribution(Z: int, N: int, q: mpmath.mpf,
                         include_inter: bool = True) -> dict:
    """m^(1)(Z, N) = Σ_{λ self-conj, c=0} w_λ^(1) · χ^λ(W_atom).

    Uses MN character (q=1 limit) — full q-Hecke would refine
    isobar splitting but is more expensive.
    """
    A = Z + N
    n = 3 * A
    word = atomic_braid_word(Z, N, include_inter=include_inter)
    perm = permutation_from_braid_word(word, n)
    cyc = cycle_type_of_permutation(perm)
    nfac = q_factorial_mp(n, q)
    parts = all_self_conjugate_partitions(n)

    total = mpmath.mpf(0)
    contribs = []
    for lam_list in parts:
        lam = tuple(lam_list)
        if content_sum(lam) != 0:
            continue
        chi = mn_character(lam, cyc)
        if chi == 0:
            continue
        w = w_lambda_level0(lam, q, nfac)
        c = w * mpmath.mpf(chi)
        total += c
        contribs.append({
            "partition": list(lam),
            "weight": float(w),
            "character": int(chi),
            "contribution": float(c),
        })
    return {
        "Z": Z, "N": N, "A": A, "n_strands": n,
        "n_self_conj_partitions": len(parts),
        "total_level1": float(total),
        "abs_level1": float(abs(total)),
        "top_contributions": sorted(
            contribs, key=lambda c: -abs(c["contribution"]))[:5],
    }


if __name__ == "__main__":
    print("=" * 88)
    print("Volume + Shell w_λ^(1) probe — self-conjugate Plancherel ansatz")
    print("=" * 88)
    print(f"q_0 = {q0}")
    print(f"Ansatz: w_λ^(1) = (d_q(λ)² / [n]_q!) · δ(c(λ)=0)")
    print()

    ATOMS = [
        ("D", 1, 1), ("3He", 2, 1), ("3H", 1, 2), ("4He", 2, 2),
        ("6Li", 3, 3), ("9Be", 4, 5), ("12C", 6, 6), ("16O", 8, 8),
    ]

    print(f"  {'atom':>5} {'A':>3} {'n_strands':>9} "
          f"{'#self-conj':>11} {'|m^(1)|':>16} {'time (s)':>9}")
    print("  " + "-" * 70)
    rows = []
    for name, Z, N in ATOMS:
        t0 = time.time()
        r = level1_contribution(Z, N, q0)
        elapsed = time.time() - t0
        bn_AME = (938.272 - AME_MASS_MEV[name] / r["A"])
        print(f"  {name:>5} {r['A']:>3} {r['n_strands']:>9} "
              f"{r['n_self_conj_partitions']:>11} "
              f"{r['abs_level1']:>16.6e}  ({elapsed:>7.1f})")
        rows.append({**r, "atom": name,
                     "binding_per_nucleon_AME": bn_AME,
                     "time_s": elapsed})

    # Correlation with binding/nucleon
    import numpy as np
    levels = np.array([r["abs_level1"] for r in rows])
    binds = np.array([r["binding_per_nucleon_AME"] for r in rows])
    if len(levels) > 1:
        corr = np.corrcoef(levels, binds)[0, 1]
        print()
        print(f"  Correlation |m^(1)| vs binding/nucleon: {corr:+.4f}")
        # Magic check: A in {4, 16} should have m^(1) spike if shell-aware
        m_4He = next(r["abs_level1"] for r in rows if r["atom"] == "4He")
        m_3He = next(r["abs_level1"] for r in rows if r["atom"] == "3He")
        m_6Li = next(r["abs_level1"] for r in rows if r["atom"] == "6Li")
        ratio_3He = m_4He / m_3He if m_3He > 0 else float("inf")
        ratio_6Li = m_4He / m_6Li if m_6Li > 0 else float("inf")
        print(f"  4He spike check: m^(1)(4He)/m^(1)(3He) = "
              f"{ratio_3He}")
        print(f"                   m^(1)(4He)/m^(1)(6Li) = "
              f"{ratio_6Li}")

    out = {
        "computation": "volume-shell-w-lambda-level1-probe",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q0": float(q0),
        "ansatz": "w_λ^(1) = (d_q(λ)² / [n]_q!) · δ(c(λ)=0)",
        "atoms": rows,
        "correlation_level1_vs_binding": (
            float(corr) if len(levels) > 1 else None),
        "interpretation": (
            "Tests whether the Plancherel weight restricted to "
            "self-conjugate partitions of 3A captures the level-1 "
            "binding-energy structure. δ(c=0) is the simplest "
            "shell-aware enrichment from conj:categorical-neutrality-"
            "saturated-shells. If correlation > 0.7 and 4He shows "
            "spike vs neighbours, ansatz captures Volume+Shell. "
            "Negative or noisy result → need full BB-spectral-"
            "sequence weight, not bare Plancherel restriction."
        ),
    }
    out_path = (Path(__file__).parent.parent.parent
                / "docs/audits/2026-05-02-w-lambda-level1-probe.witness.json")
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print()
    print(f"Witness: {out_path.relative_to(Path(__file__).parent.parent.parent)}")
