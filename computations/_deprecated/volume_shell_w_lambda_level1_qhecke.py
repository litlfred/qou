#!/usr/bin/env python3
"""
Volume + Shell w_λ^(1) probe — q-Hecke character (path a).

Re-runs the level-1 sum with the FULL q-deformed Hecke character
(hecke_character_q_deformed.q_mn_character) instead of the q=1 MN
limit. Per the prior probe's negative result, q=1 MN characters
on self-conjugate λ cancel pairwise; the q-deformation should
break the cancellation.

Ansatz unchanged:
    w_λ^(1) = (d_q(λ)² / [n]_q!) · δ(c(λ)=0)

Level-1 sum:
    m^(1)(Z, N) = Σ_{λ self-conj of 3A} w_λ^(1) · χ^λ_q(W_atom)

If this gives nonzero values at 4He, 16O (and correlates with
AME binding/nucleon), the q-deformed character breaks the
cancellation and the path-(a) hypothesis is confirmed.

Cost: q-Hecke characters are slower than q=1 MN. Capped to
A ≤ 9 for tractable runtime.
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath
import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from per_braid_tower_hybrid import q0, M_E_MEV, AME_MASS_MEV
from enumerate_self_conjugate_partitions import (
    all_self_conjugate_partitions, content_sum,
)
from schur_weyl_mpmath import q_factorial_mp
from hecke_character_q_deformed import q_character_on_atomic_braid


def w_lambda_level0(lam: tuple, q: mpmath.mpf, nfac: mpmath.mpf) -> mpmath.mpf:
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


def level1_q_hecke(Z: int, N: int, q: mpmath.mpf,
                    include_inter: bool = True) -> dict:
    """m^(1)(Z, N) = Σ_{λ self-conj of 3A, c=0} w_λ^(1) · χ^λ_q(W_atom).

    Uses q-deformed Hecke character q_character_on_atomic_braid.
    Substantially slower than q=1 MN; cap A ≤ 9.
    """
    A = Z + N
    n = 3 * A
    nfac = q_factorial_mp(n, q)
    parts = all_self_conjugate_partitions(n)

    q_sym = sp.Rational(str(q))  # use rational q for sympy character
    total = mpmath.mpf(0)
    contribs = []
    for lam_list in parts:
        lam = tuple(lam_list)
        if content_sum(lam) != 0:
            continue
        try:
            chi_sp, _ = q_character_on_atomic_braid(
                lam, Z, N, q_sym, include_inter=include_inter)
            chi_val = mpmath.mpf(str(sp.N(chi_sp, 30)))
        except Exception as exc:
            chi_val = mpmath.mpf(0)
            contribs.append({
                "partition": list(lam),
                "weight": float("nan"),
                "character": "error",
                "error": str(exc)[:80],
            })
            continue
        if chi_val == 0:
            continue
        w = w_lambda_level0(lam, q, nfac)
        c = w * chi_val
        total += c
        contribs.append({
            "partition": list(lam),
            "weight": float(w),
            "character_q": float(chi_val),
            "contribution": float(c),
        })
    return {
        "Z": Z, "N": N, "A": A, "n_strands": n,
        "n_self_conj_partitions": len(parts),
        "total_level1_q": float(total),
        "abs_level1_q": float(abs(total)),
        "top_contributions": sorted(
            contribs, key=lambda c: -abs(c.get("contribution", 0)))[:5],
    }


if __name__ == "__main__":
    print("=" * 88)
    print("Volume + Shell w_λ^(1) probe — q-deformed Hecke character (path a)")
    print("=" * 88)
    print(f"q_0 = {q0}")
    print()

    ATOMS = [
        ("D", 1, 1), ("3He", 2, 1), ("3H", 1, 2), ("4He", 2, 2),
        ("6Li", 3, 3), ("9Be", 4, 5),
        # 12C+ skipped: 33+ self-conj partitions × q-Hecke is slow.
    ]

    print(f"  {'atom':>5} {'A':>3} {'n_strands':>9} "
          f"{'#self-conj':>11} {'|m^(1)_q|':>16} {'time (s)':>9}")
    print("  " + "-" * 70)
    rows = []
    for name, Z, N in ATOMS:
        t0 = time.time()
        try:
            r = level1_q_hecke(Z, N, q0)
        except Exception as exc:
            r = {"Z": Z, "N": N, "A": Z + N, "n_strands": 3 * (Z + N),
                 "n_self_conj_partitions": -1,
                 "total_level1_q": float("nan"),
                 "abs_level1_q": float("nan"),
                 "error": str(exc)[:120]}
        elapsed = time.time() - t0
        bn = (938.272 - AME_MASS_MEV[name] / r["A"])
        if "error" in r:
            print(f"  {name:>5} {r['A']:>3} {r['n_strands']:>9} "
                  f"{'?':>11} {r['error'][:60]}")
        else:
            print(f"  {name:>5} {r['A']:>3} {r['n_strands']:>9} "
                  f"{r['n_self_conj_partitions']:>11} "
                  f"{r['abs_level1_q']:>16.6e}  ({elapsed:>7.1f})")
        rows.append({**r, "atom": name, "binding_per_nucleon_AME": bn,
                     "time_s": elapsed})

    import numpy as np
    valid = [r for r in rows if "error" not in r and not np.isnan(r["abs_level1_q"])]
    if len(valid) > 1:
        levels = np.array([r["abs_level1_q"] for r in valid])
        binds = np.array([r["binding_per_nucleon_AME"] for r in valid])
        corr = np.corrcoef(levels, binds)[0, 1] if len(levels) > 1 else None
        print()
        print(f"  Correlation |m^(1)_q| vs binding/nucleon: "
              f"{corr:+.4f}" if corr is not None else "  insufficient data")

        # 4He cancellation broken?
        m_4He_q = next((r["abs_level1_q"] for r in valid if r["atom"] == "4He"), None)
        if m_4He_q is not None and m_4He_q > 0:
            print(f"  m^(1)_q(4He) = {m_4He_q:.6e}  ← q-Hecke breaks q=1 cancellation")
        elif m_4He_q == 0:
            print(f"  m^(1)_q(4He) = 0  (cancellation persists at q-deformed level)")

    out = {
        "computation": "volume-shell-w-lambda-level1-q-hecke-probe",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q0": float(q0),
        "ansatz": ("w_λ^(1) = (d_q(λ)² / [n]_q!) · δ(c(λ)=0); "
                    "character = q-deformed Hecke chi^λ_q (vs q=1 MN)"),
        "atoms": rows,
        "interpretation": (
            "Path (a) of the corrective options from the q=1 MN probe's "
            "negative result. Tests whether q-deformation breaks the "
            "self-conjugate character cancellations seen at q=1."
        ),
    }
    out_path = (Path(__file__).parent.parent.parent
                / "docs/audits/2026-05-02-w-lambda-level1-q-hecke.witness.json")
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print()
    print(f"Witness: {out_path.relative_to(Path(__file__).parent.parent.parent)}")
