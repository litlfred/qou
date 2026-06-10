#!/usr/bin/env python3
"""active_set_lr_profile — scaling profile for the active-set / nucleon-cache
chi decomposition (the large-A fix).

χ^λ(β_atom), λ ⊢ 3A, restricted to the Young subgroup (H_3)^A:

    χ^λ = Σ_{(μ_1,…,μ_A): μ_i ⊢ 3}
            c^λ_{μ_1…μ_A} · A_op(I_1,…,I_{A-1}) · Π_i χ^{μ_i}(β_{nuc_i})

The current production path (`chi_q_atomic` / `chi_lambda_all_partitions_mpfr`)
is a per-basis-vector trace, O(L·d_λ²) per λ ⇒ L·n! per atom — the d_λ²
wall (3.6 years at ⁶Li, §docs/audits/2026-06-09-large-A-chi-bottleneck-
scaling-plan.md). This profiler quantifies the active-set alternative:

  - nucleon cache: only 6 base χ^{μ⊢3}(β_{p,n}), computed once;
  - active set of λ: tuples (μ_1,…,μ_A) with c^λ_{μ_1…μ_A} > 0 (the rest
    are structural zeros); per-tuple block work ≤ (Π dim V_{μ_i})² ≤ (2^A)².

It also serves as the `active_lr_tuples(λ)` enumerator (step 2 of the
implementation plan): `multi_lr(A)[λ]` is `{(μ_1,…,μ_A): multiplicity}`.

Usage:  python3 active_set_lr_profile.py [--max-A 7]
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import argparse  # noqa: E402
import math  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
from pathlib import Path  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from lr_coefficients import get_lr_table, partitions_of  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

P3 = [tuple(p) for p in partitions_of(3)]


def dim_syt(lam: tuple[int, ...]) -> int:
    """Hook-length dimension of the S_n irrep V_λ."""
    n = sum(lam)
    lam = list(lam)
    conj = [sum(1 for l in lam if l > j) for j in range(lam[0] if lam else 0)]
    prod = 1
    for i, l in enumerate(lam):
        for j in range(l):
            prod *= (l - j) + (conj[j] - i) - 1
    return math.factorial(n) // prod


_DIM3 = {p: dim_syt(p) for p in P3}  # {(3):1,(2,1):2,(1,1,1):1}


def multi_lr(A: int) -> dict[tuple, dict[tuple, int]]:
    """`{λ ⊢ 3A: {(μ_1,…,μ_A): c^λ_{μ_1…μ_A}}}` via iterated LR.

    The inner dict is the ACTIVE SET of λ (only nonzero-multiplicity
    tuples appear). Built by folding one nucleon (μ_k ⊢ 3) in at a time.
    """
    cur: dict[tuple, dict[tuple, int]] = {mu: {(mu,): 1} for mu in P3}
    for k in range(2, A + 1):
        lr = get_lr_table(3 * (k - 1), 3)  # (ξ⊢3(k-1), ν⊢3, λ⊢3k) -> c
        nxt: dict[tuple, dict[tuple, int]] = {}
        for (xi, nu, lam), c in lr.items():
            if c == 0 or xi not in cur or nu not in _DIM3:
                continue
            tgt = nxt.setdefault(lam, {})
            for tup, m in cur[xi].items():
                key = tup + (nu,)
                tgt[key] = tgt.get(key, 0) + m * c
        cur = nxt
    return cur


def _block(tup: tuple) -> int:
    p = 1
    for mu in tup:
        p *= _DIM3[mu]
    return p


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--max-A", type=int, default=7)
    args = ap.parse_args()

    rows = []
    print(f"{'A':>2} {'n':>3} {'p(n)':>5} {'Sigma|active|':>13} "
          f"{'maxblk':>7} {'LRcost':>14} {'n!(f64)':>11} {'speedup':>10}")
    for A in range(2, args.max_A + 1):
        n = 3 * A
        t0 = time.time()
        ml = multi_lr(A)
        tot_active = sum(len(t) for t in ml.values())
        maxblk = max((_block(t) for tup in ml.values() for t in tup),
                     default=1)
        lrcost = sum(_block(t) ** 2 for tup in ml.values() for t in tup)
        fact = math.factorial(n)
        rows.append({
            "A": A, "n": n, "p_n": len(ml),
            "active_tuples_total": tot_active,
            "max_block_dim": maxblk,
            "lr_block_cost": lrcost,
            "f64_cost_n_factorial": str(fact),
            "speedup_vs_f64": fact / max(lrcost, 1),
        })
        print(f"{A:>2} {n:>3} {len(ml):>5} {tot_active:>13,} {maxblk:>7} "
              f"{lrcost:>14,} {fact:>11.2e} {fact / max(lrcost, 1):>10.2e} "
              f" [{time.time() - t0:.1f}s]")

    w = WitnessBuilder("active-set-lr-scaling-profile", engine="python")
    w.set_description(
        "Active-set / nucleon-cache scaling profile for atomic χ^λ: "
        "multi-LR enumeration of nonzero c^λ_{μ_1…μ_A} (μ_i⊢3) per λ⊢3A. "
        "Quantifies the d_λ² → 2^A-block scaling-law change vs the "
        "per-basis-vector f64 path (cost n!). See docs/audits/"
        "2026-06-09-large-A-chi-bottleneck-scaling-plan.md §8."
    )
    w.add_data("rows", rows)
    w.add_data("nucleon_cache_size",
               "6 base χ^{μ⊢3}(β_{p,n}) values, computed once")
    # Reproducible structural assertion: the per-λ block size is bounded
    # by 2^A (dim V_{μ⊢3} ≤ 2), i.e. the d_λ² wall is gone. Check the
    # largest A computed.
    last = rows[-1]
    w.add_assertion(
        f"max_block_dim_eq_2_pow_A_at_A{last['A']}",
        computed=float(last["max_block_dim"]),
        expected=float(2 ** last["A"]),
        tolerance=0,
        unit="block dim",
        source="multi_lr enumeration (this script)",
    )
    w.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
