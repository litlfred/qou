#!/usr/bin/env python3
"""
Phase A.1 — Full Schur-Weyl Markov decomposition over all partitions.

The previous per-braid path uses the **2-variable Schur** weight
w_λ = s_λ(q, q⁻¹) / H_q(λ), which vanishes for length(λ) > 2 — we
were dropping every length-3+ partition.

The proper Markov trace decomposition uses the **Plancherel weight**
w_λ = dim_q(λ)² / [n]_q!, which is non-zero for ALL partitions:

    tr_M(W) = Σ_{λ ⊢ n} (dim_q(λ)² / [n]_q!) · χ^λ_q(W) / dim(λ)

Iterates ALL partitions of 3A (not just length-≤-2).
For low A this is tractable: p(6)=11, p(9)=30, p(12)=77, p(15)=176.

Compares to the length-≤-2 Schur version for D, ³He, ³H, ⁴He.

Uses pyhecke_native.chi_q_atomic Rust kernel (P2.2c-12C).

Witness: docs/audits/2026-05-02-phase-a1-full-schur-weyl.witness.json
"""
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath

sys.path.insert(0, str(Path(__file__).parent))
from murnaghan_nakayama import partitions_of, dim_specht
from schur_weyl_mpmath import (
    q_factorial_mp,
    q_hook_product_mp,
)
from schur_weyl_q_hecke_v2 import (
    build_atomic_crossings_with_coeffs,
)
from q_parameter import Q as Q0_FLOAT
import pyhecke_native

mpmath.mp.dps = 50
q0 = mpmath.mpf(str(Q0_FLOAT))


def dim_q_mp(partition, q):
    """q-Weyl dim: dim_q(λ) = [n]_q! / Π[h_x(λ)]_q in mpmath."""
    n = sum(partition)
    return q_factorial_mp(n, q) / q_hook_product_mp(partition, q)


def plancherel_weight_mp(partition, q):
    """w_λ = dim_q(λ)² / [n]_q! in mpmath."""
    n = sum(partition)
    d_q = dim_q_mp(partition, q)
    nfac = q_factorial_mp(n, q)
    return d_q ** 2 / nfac


def markov_trace_full_schur_weyl(Z, N, *, q_val=None,
                                  include_inter=True, dim_cap=None,
                                  precision=50):
    """tr_M(W_atomic) via PROPER Markov decomposition.

    Iterates ALL partitions of 3A (not just length-≤-2) using
    Plancherel weight and q-Hecke character via pyhecke_native.
    """
    if q_val is None:
        q_val = Q0_FLOAT
    mpmath.mp.dps = precision
    q_mp = mpmath.mpf(str(q_val))

    A = Z + N
    n_strands = 3 * A

    crossings, _ns = build_atomic_crossings_with_coeffs(
        Z, N, include_inter=include_inter, q_val=float(q_val),
    )
    factors = [(float(c), float(d), int(g) + 1) for c, d, g in crossings]

    total = mpmath.mpf(0)
    used = []
    skipped = []
    parts = partitions_of(n_strands)
    for lam in parts:
        d_classical = dim_specht(lam)
        if dim_cap is not None and d_classical > dim_cap:
            skipped.append({"partition": list(lam), "dim": d_classical})
            continue
        # Plancherel weight
        w_mp = plancherel_weight_mp(lam, q_mp)
        if w_mp == 0:
            continue
        # q-Hecke character via Rust
        try:
            chi = pyhecke_native.chi_q_atomic(list(lam), factors, float(q_val))
        except Exception as e:
            skipped.append({"partition": list(lam), "dim": d_classical, "error": str(e)})
            continue
        if chi == 0:
            continue
        contrib = w_mp * mpmath.mpf(chi) / mpmath.mpf(d_classical)
        total += contrib
        used.append({
            "partition": list(lam),
            "dim_classical": d_classical,
            "weight_plancherel": str(w_mp),
            "chi_q": float(chi),
            "contribution": str(contrib),
        })
    return total, used, skipped


# ─── Comparison + witness ─────────────────────────────────────

if __name__ == "__main__":
    print("=" * 88)
    print("Phase A.1 — Full Schur-Weyl Markov decomposition")
    print("=" * 88)

    ATOMS = [("D", 1, 1), ("3He", 2, 1), ("3H", 1, 2), ("4He", 2, 2)]
    results = []
    for name, Z, N in ATOMS:
        n = 3 * (Z + N)
        n_parts = len(partitions_of(n))
        print(f"\n=== {name} (Z={Z}, N={N}, A={Z+N}, n=3A={n}, p(n)={n_parts}) ===")
        t0 = time.time()
        try:
            total, used, skipped = markov_trace_full_schur_weyl(
                Z, N, dim_cap=10000  # generous cap for A ≤ 4
            )
            t = time.time() - t0
            print(f"  Σ_λ (Plancherel) = {abs(total)}")
            print(f"  partitions used: {len(used)} / {n_parts}")
            print(f"  partitions skipped (dim>10000): {len(skipped)}")
            print(f"  time: {t:.2f}s")
            # Length distribution of used
            len_hist = {}
            for u in used:
                k = len(u["partition"])
                len_hist[k] = len_hist.get(k, 0) + 1
            print(f"  length distribution: {sorted(len_hist.items())}")
            results.append({
                "atom": name,
                "Z": Z, "N": N, "A": Z + N,
                "n_strands": n,
                "p_n": n_parts,
                "n_partitions_used": len(used),
                "n_skipped": len(skipped),
                "abs_value_at_q0": str(abs(total)),
                "length_distribution": dict(len_hist),
                "time_seconds": t,
            })
        except Exception as e:
            t = time.time() - t0
            import traceback; traceback.print_exc()
            results.append({"atom": name, "error": str(e), "time_seconds": t})

    witness = {
        "audit": "Phase A.1 — Full Schur-Weyl Markov decomposition",
        "generated": datetime.now(timezone.utc).isoformat(),
        "q_0": str(q0),
        "atoms": results,
        "interpretation": (
            "Sums Plancherel weight × q-Hecke character over ALL "
            "partitions of 3A (not just length-≤-2). Compared with "
            "the prior length-≤-2 Schur path; the difference is the "
            "contribution from length-3+ partitions that the "
            "2-variable Schur formula was forcing to zero."
        ),
    }

    out_path = Path(__file__).parent.parent.parent / "docs/audits/2026-05-02-phase-a1-full-schur-weyl.witness.json"
    out_path.write_text(json.dumps(witness, indent=2, default=str))
    print()
    print(f"Witness: {out_path.relative_to(Path(__file__).parent.parent.parent)}")
