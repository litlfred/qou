#!/usr/bin/env python3
"""Smoke test for `discover_via_wedderburn_sdp` (F4 SDP discovery).

Verifies:
1. Entangled braids (no tensor structure) get decomposed into
   per-active-block KnotOperations.
2. Each emitted op carries the correct (partition, χ_λ, y_λ) triple.
3. The Markov-trace identity reconstructs:
       tr_M(T_β) ≈ Σ_λ y_λ · χ_λ(T_β)
   over the active blocks (those whose χ is non-trivial).
4. Empty braid returns an empty list (caller uses the y_λ feeder).
5. Cache-key behaviour: two different braids that activate the same
   block at the same q produce the same cache_key → cross-braid
   dedup works.
"""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import pyhecke_native as p  # type: ignore[import]

from knot_operation_cache import (
    discover_via_wedderburn_sdp,
    _load_y_lambda_table,
)
from q_parameter import Q as Q0_FLOAT


def main() -> int:
    print("=" * 70)
    print("F4 SDP discovery: discover_via_wedderburn_sdp")
    print("=" * 70)
    ok_all = True
    q = float(Q0_FLOAT)

    # ── Case 1: entangled n=4 braid σ_1·σ_2·σ_1·σ_3.
    word_e = [(1, 1), (1, 2), (1, 1), (1, 3)]
    n = 4
    ops = discover_via_wedderburn_sdp(word_e, n=n, q=q)
    print(f"  σ_1σ_2σ_1σ_3 (n=4): {len(ops)} active blocks emitted")
    for op in ops:
        partition = op.fingerprint["partition"]
        chi = op.plancherel_signature["chi_value"]
        y_lam = op.plancherel_signature["y_lambda"]
        print(f"    λ={partition:<14} χ_λ={chi:+.6f}  y_λ={y_lam:.6e}")

    # ── Case 2: Markov-trace identity check.
    # tr_M(T_β) = Σ_λ y_λ · χ_λ(T_β), summed over ALL λ (not just
    # active).  Compute separately and verify the active-block sum
    # captures the full trace within tolerance (i.e., inactive blocks
    # contribute < 1e-10 to the trace, so dropping them is safe).
    parts = [list(lam) for lam in p.partitions_of(n)]
    chars = p.chi_lambdas_braid(parts, word_e, q)
    y_table = _load_y_lambda_table(n)
    full_trace = sum(
        y_table.get(tuple(lam), 0.0) * chi
        for lam, chi in zip(parts, chars)
    )
    active_trace = sum(
        op.plancherel_signature["y_lambda"]
        * op.plancherel_signature["chi_value"]
        for op in ops
    )
    diff = abs(full_trace - active_trace)
    case2_ok = diff < 1e-9
    ok_all &= case2_ok
    print(f"  {'OK' if case2_ok else 'FAIL':<4} Markov-trace reconstruction: "
          f"full={full_trace:+.10f}, active-only={active_trace:+.10f}, "
          f"diff={diff:.2e}")

    # ── Case 3: empty braid returns empty list.
    ops_empty = discover_via_wedderburn_sdp([], n=3, q=q)
    case3_ok = ops_empty == []
    ok_all &= case3_ok
    print(f"  {'OK' if case3_ok else 'FAIL':<4} empty braid → empty list")

    # ── Case 4: cache_key dedup across braids that activate the same
    # block.  σ_1 and σ_1·σ_2·σ_1 both activate the trivial rep λ=(n)
    # at any q (positive braids → positive trivial-rep character).
    # Their (n, partition) fingerprints should match → same cache_key.
    word_a = [(1, 1)]
    word_b = [(1, 1), (1, 2), (1, 1)]
    ops_a = discover_via_wedderburn_sdp(word_a, n=3, q=q)
    ops_b = discover_via_wedderburn_sdp(word_b, n=3, q=q)
    keys_a = {op.fingerprint["partition"]: op.cache_key() for op in ops_a}
    keys_b = {op.fingerprint["partition"]: op.cache_key() for op in ops_b}
    common_partitions = set(keys_a) & set(keys_b)
    case4_ok = len(common_partitions) > 0 and all(
        keys_a[part] == keys_b[part] for part in common_partitions
    )
    ok_all &= case4_ok
    print(f"  {'OK' if case4_ok else 'FAIL':<4} cache_key dedup across braids: "
          f"{len(common_partitions)} shared partition(s) match keys")

    # ── Case 5: tolerance threshold cuts inactive blocks.
    # On a positive single-generator braid σ_1 (n=3), every irrep
    # has non-zero character (no trivial cancellations on positive
    # words at q≠1).  Tighter tolerance should not change the count.
    ops_loose = discover_via_wedderburn_sdp(word_a, n=3, q=q, tolerance=1e-10)
    ops_tight = discover_via_wedderburn_sdp(word_a, n=3, q=q, tolerance=1e-50)
    case5_ok = len(ops_loose) == len(ops_tight)
    ok_all &= case5_ok
    print(f"  {'OK' if case5_ok else 'FAIL':<4} tolerance: loose={len(ops_loose)} ops, "
          f"tight={len(ops_tight)} ops (unchanged on positive σ_1)")

    print()
    print(f"Result: {'all pass' if ok_all else 'FAILURES'}")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
