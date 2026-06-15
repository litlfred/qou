#!/usr/bin/env python3
"""
P2.2c — q-deformed Hecke character path for Schur-Weyl.

The mpmath path (`schur_weyl_mpmath.py`) uses the q=1 limit of the
Hecke character (Murnaghan-Nakayama on the underlying permutation
cycle type). This is fast but cannot distinguish proton from
neutron sub-braids — both have identical S_3 cycle structure.

This module wires the **q-deformed Hecke character** χ^λ_q(T_w)
from `hecke_characters.chi_lambda_braid` (Hoefsmit seminormal
matrices) into the Schur-Weyl framework. The expectation:

  - 3He vs 3H now split (~0.53 MeV physical splitting)
  - n-p mass splitting (~1.293 MeV) emerges from per-nucleon
    sub-braid traces (proton trace ≠ neutron trace)
  - per-braid total still scales linearly in A but with
    proton/neutron-discriminating coefficients

Witness: docs/audits/2026-05-01-p2-2c-q-hecke.witness.json
"""
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath

sys.path.insert(0, str(Path(__file__).parent))
from murnaghan_nakayama import atomic_braid_word as _legacy_braid_word
from schur_weyl_mpmath import (
    length_le_2_partitions_of,
    schur_weyl_weight_mp,
)
from hecke_characters import chi_lambda_braid
from q_parameter import Q as Q0_FLOAT


def atomic_braid_word_1based(Z, N, include_inter=True):
    """Atomic braid word in chi_lambda_braid's [(sign, gen_1based)] format.

    Murnaghan-Nakayama uses 0-based generator indices; chi_lambda_braid
    uses 1-based.
    """
    word_0 = _legacy_braid_word(Z, N, include_inter=include_inter)
    return [(sign, gen_idx + 1) for gen_idx, sign in word_0]


def markov_trace_q_hecke(Z, N, *, q_val=None, precision=50,
                          include_inter=True):
    """tr_M of an atomic braid via Schur-Weyl with q-deformed Hecke characters.

    Σ_{λ ⊢ 3A, len(λ)≤2} w_λ(q) · χ^λ_q(T_w)

    Returns (total, partitions_used, info).
    """
    if q_val is None:
        q_val = Q0_FLOAT
    mpmath.mp.dps = precision
    q = mpmath.mpf(str(q_val))

    A = Z + N
    n_strands = 3 * A
    word = atomic_braid_word_1based(Z, N, include_inter=include_inter)

    total = mpmath.mpf(0)
    partitions_used = []
    for lam in length_le_2_partitions_of(n_strands):
        # q-deformed Hecke character at q_val
        # Default to f64 (16-dps native Python; mpfr_50dps needs Rust kernel)
        try:
            chi_val = chi_lambda_braid(
                shape=tuple(lam),
                word=word,
                q_value=float(q_val),
                precision="f64",
            )
            chi = mpmath.mpf(str(chi_val))
        except Exception as e:
            print(f"  WARN: chi_lambda_braid failed for λ={lam}: {e}")
            continue
        if chi == 0:
            continue
        w = schur_weyl_weight_mp(lam, q)
        if w == 0:
            continue
        contrib = w * chi
        total += contrib
        partitions_used.append({
            "partition": list(lam),
            "weight": str(w),
            "chi_q": str(chi),
            "contribution": str(contrib),
        })
    return total, partitions_used, {"word_length": len(word), "n_strands": n_strands}


# ─── Witness + comparison ─────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 80)
    print("P2.2c — q-deformed Hecke character path (Schur-Weyl × q-Hecke)")
    print("=" * 80)

    ATOMS = [
        ("D", 1, 1, 2),
        ("3He", 2, 1, 3),
        ("3H", 1, 2, 3),
        ("4He", 2, 2, 4),
    ]

    results = []
    for name, Z, N, A in ATOMS:
        print(f"\n=== {name} (Z={Z}, N={N}, A={A}, n=3A={3*A}) ===")
        t0 = time.time()
        try:
            total, parts, info = markov_trace_q_hecke(Z, N, precision=50)
            t = time.time() - t0
            mag = abs(total)
            print(f"  word length = {info['word_length']}")
            print(f"  |Σ_λ w_λ χ^λ_q| = {mag}")
            print(f"  {len(parts)} non-zero partitions")
            print(f"  time: {t:.3f}s")
            q0_f = float(Q0_FLOAT)
            convergent = float(mag) < q0_f
            print(f"  Φ_q convergence (|·| < q_0={q0_f:.4f}):  → {'✅' if convergent else '🔴'}")
            results.append({
                "atom": name, "Z": Z, "N": N, "A": A,
                "n_strands": 3 * A,
                "word_length": info["word_length"],
                "n_partitions_used": len(parts),
                "abs_value_at_q0": str(mag),
                "phi_q_convergent": convergent,
                "time_seconds": t,
                "partitions": parts,
            })
        except Exception as e:
            t = time.time() - t0
            import traceback
            traceback.print_exc()
            results.append({"atom": name, "error": str(e), "time_seconds": t})

    # ³He vs ³H splitting check
    he3 = next((r for r in results if r.get("atom") == "3He"), None)
    h3 = next((r for r in results if r.get("atom") == "3H"), None)
    if he3 and h3 and "abs_value_at_q0" in he3 and "abs_value_at_q0" in h3:
        v_he3 = mpmath.mpf(he3["abs_value_at_q0"])
        v_h3 = mpmath.mpf(h3["abs_value_at_q0"])
        diff = v_he3 - v_h3
        print(f"\n=== ³He vs ³H splitting (q-Hecke) ===")
        print(f"  3He: {v_he3}")
        print(f"  3H : {v_h3}")
        print(f"  diff: {diff}  (expected non-zero with q-Hecke)")
        if abs(diff) > mpmath.mpf("1e-20"):
            print(f"  ✅ NON-ZERO splitting detected — q-Hecke distinguishes 3He from 3H")
        else:
            print(f"  🔴 still identical (expected with q=1 MN; ?? at q-Hecke)")
        results.append({
            "comparison": "3He vs 3H splitting",
            "3He_value": str(v_he3),
            "3H_value": str(v_h3),
            "diff": str(diff),
            "diff_abs": str(abs(diff)),
        })

    witness = {
        "audit": "P2.2c — q-deformed Hecke character path",
        "generated": datetime.now(timezone.utc).isoformat(),
        "q_0": str(Q0_FLOAT),
        "atoms": results,
        "interpretation": (
            "Replaces the q=1 Murnaghan-Nakayama character in the "
            "Schur-Weyl path with the q-deformed Hecke character "
            "χ^λ_q(T_w) via Hoefsmit seminormal matrices (from "
            "hecke_characters.chi_lambda_braid). Expected to split "
            "3He vs 3H and produce per-nucleon n-p mass splitting."
        ),
    }

    out_path = Path(__file__).parent.parent.parent / "docs/audits/2026-05-01-p2-2c-q-hecke.witness.json"
    out_path.write_text(json.dumps(witness, indent=2, default=str))
    print()
    print(f"Witness: {out_path.relative_to(Path(__file__).parent.parent.parent)}")
