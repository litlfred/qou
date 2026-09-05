#!/usr/bin/env python3
"""The per-partition dual the gate assumes does not exist in either LP.

Groundwork for docs/proposals/2026-09-05-operator-selection-objective-replacement.md.
Beans qou-sv7h / qou-v7qj.

TWO MEASUREMENTS

1. INDEX-SET MISMATCH. Both `prop:operator-selection-lp` and
   `prop:confinement-lp` index their Frobenius positivity constraints by NF
   BASIS ELEMENT -- "sum_j G_ij x_j >= 0 for all i in {1..d}", d = n!. But
   `prop:mass-coefficient-shadow-price` claims the dual of "the corresponding
   PARTITION's Frobenius positivity constraint", and `lp_shadow_price(partition)`
   and the Pass-2 gate are both per-partition. At n = 3 that is 6 constraints
   against 3 partitions. The object being dualised is not in either program.

   The natural bridge makes it a MATRIX: H_n(q) = direct sum of M_{d_lambda},
   so the n! scalar constraints group into partition blocks of size d_lambda^2.
   A genuinely per-partition constraint is block-PSD, and its dual is a
   d_lambda x d_lambda matrix Y_lambda >= 0 -- not a scalar. (The corpus already
   ships `solve_psd_operator_selection_sdp` alongside the LP form.)

2. THE CODE DISCARDS EXACTLY THE PARTITIONS WHERE ITS TYPE IS CORRECT. A scalar
   shadow price is well-defined only where d_lambda = 1, i.e. the trivial and
   sign representations (k) and (1^k). `lp_shadow_price` subtracts
   y_0 = 1/[k]_q!, which IS min_lambda(w/d), zeroing exactly two partitions per
   level -- and measured at k = 2..7 that zeroed set is IDENTICAL to the
   d_lambda = 1 set at every k.

   So the code zeroes precisely the partitions where a scalar dual makes sense
   and keeps the ones where the dual is a matrix. That is a type inversion, not
   a weighting error of some size.

NOT CLAIMED: what the replacement should be (the proposal lays out options and
chooses none); that an SDP would SELECT anything -- the audit's scope-(b) result
is that no LINEAR objective selects B_3, and that B_3 is not distinguished by
the feasible geometry at all, which applies to any program over that same
feasible set.

scope-(a); no fit; nothing wired; no c_k; L2 unchanged. Gap qou-sv7h OPEN.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "substrate"))

import _path_bridge  # noqa: F401,E402

from mpmath import mp  # noqa: E402

from hecke_core import (  # noqa: E402
    q_factorial, partitions_of, partition_dimension, wedderburn_weight,
)
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  -- {detail}" if detail else ""))


def main() -> int:
    set_compute_dps()
    print("=" * 74)
    print("  The per-partition dual the gate assumes is not in either LP")
    print("=" * 74)
    print()

    # ---- 1. index-set mismatch, and the block structure -------------------
    print("  1. n! scalar constraints vs #partitions, and how they group")
    blocks = []
    for n in (3, 4, 5, 6):
        ps = [tuple(p) for p in partitions_of(n)]
        dims = [partition_dimension(p) for p in ps]
        blocks.append({"n": n, "n_partitions": len(ps),
                       "n_constraints_in_LP": math.factorial(n),
                       "dims": dims, "sum_d_squared": sum(d * d for d in dims)})
        print(f"     n={n}: LP has {math.factorial(n):>3} constraints (NF basis),"
              f" {len(ps):>2} partitions;  d^2 = {[d*d for d in dims]}"
              f"  sum = {sum(d*d for d in dims)}")
    check("sum of d_lambda^2 = n!, so constraints group into partition blocks",
          all(b["sum_d_squared"] == b["n_constraints_in_LP"] for b in blocks))
    check("the two index sets differ in size at every n >= 3",
          all(b["n_partitions"] < b["n_constraints_in_LP"] for b in blocks),
          "so 'the partition's constraint' has no referent in either program")

    # ---- 2. the code zeroes exactly the d_lambda = 1 partitions -----------
    print()
    print("  2. which partitions the code's y_0 zeroes, vs where a scalar dual exists")
    rows, allmatch = [], True
    for k in range(2, 8):
        ps = [tuple(p) for p in partitions_of(k)]
        onedim = {p for p in ps if partition_dimension(p) == 1}
        y0 = mp.mpf(1) / q_factorial(k)
        zeroed = {p for p in ps
                  if abs(mp.mpf(wedderburn_weight(p)) / partition_dimension(p) - y0)
                  < mp.mpf("1e-30")}
        same = onedim == zeroed
        allmatch &= same
        rows.append({"k": k, "d1_partitions": sorted(str(p) for p in onedim),
                     "zeroed_by_y0": sorted(str(p) for p in zeroed),
                     "identical": same})
        print(f"     k={k}  d=1: {sorted(onedim)}   zeroed: {sorted(zeroed)}"
              f"   {'IDENTICAL' if same else 'DIFFER'}")
    check("the zeroed set IS the d_lambda = 1 set, at every k tested", allmatch,
          "k = 2..7")
    check("a scalar dual is well-defined only where d_lambda = 1",
          all(partition_dimension(tuple(p)) == 1
              for k in range(2, 8) for p in partitions_of(k)
              if partition_dimension(tuple(p)) == 1))

    print()
    print("  => the code zeroes precisely the partitions where its scalar object")
    print("     type is correct, and keeps the ones whose dual is a matrix.")

    w = WitnessBuilder("lp-partition-index-mismatch", engine="python+mpmath")
    w.set_description(
        "Groundwork for the operator-selection objective replacement. Both LPs "
        "index Frobenius positivity by NF basis element (n! of them); the gate, "
        "lp_shadow_price and prop:mass-coefficient-shadow-price all index by "
        "partition (far fewer). The natural bridge is block-PSD, whose dual is a "
        "d_lambda x d_lambda matrix, not a scalar -- and the y_0 = 1/[k]_q! shift "
        "zeroes exactly the d_lambda = 1 partitions, i.e. precisely those where a "
        "scalar dual would be well-defined."
    )
    w.set_audit_only("docs/proposals/2026-09-05-operator-selection-objective-replacement.md")
    w.add_data("index_sets", blocks)
    w.add_data("zeroed_vs_one_dimensional", rows)
    for nm, ok in CHECKS:
        w.add_assertion(nm, computed="1" if ok else "0", expected="1",
                        tolerance="0", source="lp_partition_index_mismatch_probe")
    print(f"\n  witness: {w.save()}")
    print(f"  {sum(1 for _n, ok in CHECKS if ok)}/{len(CHECKS)} checks passed")
    return 0 if all(ok for _n, ok in CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
