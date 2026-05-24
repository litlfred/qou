#!/usr/bin/env python3
"""probe_crystal_pole_generalisation.py — apply the crystal-pole
counter beyond atomic braids.

Generalises the framework from PR #670's `crystal_shift_nf_atomic.py`
(which targeted canonical pppnnn atomic braids) to a broader class of
Hecke braid words.  The `crystal_shift_nf(word, n_strands)` function
itself is already generic — this probe demonstrates it on:

  1. Torus knots T_{p, k} (cross-check vs prop:alpha-shift-torus-knot:
     α_shift(T_{p, k}) = k · (p − 1) via the column-rich SYT)
  2. Hopf link (= T_{2, 2})
  3. Trefoil knot (= T_{2, 3})
  4. Generic test braid words

The torus-knot case is the natural validation: `crystal_pole_order.py`
(already on main) proves `α_shift(T_{p, k}) = k(p−1)` combinatorially.
Our `crystal_shift_nf` should reproduce this — and does, because the
column SYT of (1^p) has ρ_T(j) = -1 for every adjacent pair.

Output: crystal-pole-generalisation.witness.json
"""
from __future__ import annotations

import sys
import time
from pathlib import Path
from typing import List, Tuple

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from crystal_shift_nf_atomic import crystal_shift_nf  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def torus_braid_word(p: int, k: int) -> List[Tuple]:
    """T_{p, k} torus knot/link as Hecke word on p strands.

    Braid: (σ_1 σ_2 ... σ_{p-1})^k.  In Hecke (c, d, gen) form with
    gen 0-indexed: (1, 0, 0), (1, 0, 1), …, (1, 0, p-2), repeated k times.
    """
    cycle = [(1.0, 0.0, g) for g in range(p - 1)]
    return cycle * k


def hopf_link_word() -> List[Tuple]:
    """Hopf link = T_{2, 2} = σ_1² on 2 strands."""
    return torus_braid_word(2, 2)


def trefoil_word() -> List[Tuple]:
    """Trefoil = T_{2, 3} = σ_1³ on 2 strands."""
    return torus_braid_word(2, 3)


def main() -> int:
    print("=" * 90)
    print("  Crystal-pole counter — generalisation beyond atomic braids")
    print("=" * 90)
    print()

    print("  Torus knots T_{p,k}: alpha_shift = k·(p−1) (prop:alpha-shift-torus-knot)")
    print(f"  {'object':<22} {'(p, k)':>8} {'n_strands':>10} {'word len':>10} "
          f"{'expected':>10} {'crystal_pole':>14} {'match':>7}")
    print("  " + "-" * 90)

    targets = [
        ("Hopf link",     2, 2),
        ("Trefoil",        2, 3),
        ("T_{2,5}",        2, 5),
        ("T_{2,7}",        2, 7),
        ("T_{2,9}",        2, 9),
        ("T_{3,2}",        3, 2),
        ("T_{3,4}",        3, 4),
        ("T_{3,5}",        3, 5),
        ("T_{4,3}",        4, 3),
        ("T_{5,2}",        5, 2),
    ]
    results = []
    n_pass = 0
    for name, p, k in targets:
        n_strands = p
        word = torus_braid_word(p, k)
        expected = k * (p - 1)
        t0 = time.monotonic()
        res = crystal_shift_nf(word, n_strands)
        elapsed = time.monotonic() - t0
        actual = res["shift_nf"]
        ok = (actual == expected)
        if ok:
            n_pass += 1
        status = "✓" if ok else "✗"
        print(f"  {name:<22} {f'({p},{k})':>8} {n_strands:>10} {len(word):>10} "
              f"{expected:>10} {actual:>14} {status:>7}  ({elapsed:.2f}s)")
        results.append({
            "name": name, "p": p, "k": k, "n_strands": n_strands,
            "word_length": len(word),
            "expected_alpha_shift": expected,
            "crystal_pole_actual": actual,
            "match": bool(ok),
            "compute_time_seconds": elapsed,
        })
    print()
    print(f"  Verified: {n_pass}/{len(targets)} torus knots")
    print()

    builder = (
        WitnessBuilder("crystal-pole-generalisation", engine="python")
        .set_description(
            "Crystal-pole counter applied to torus knots T_{p, k}, "
            "demonstrating that PR #670's crystal_shift_nf(word, "
            "n_strands) generalises beyond canonical atomic braids.  "
            "Cross-checks against prop:alpha-shift-torus-knot's closed "
            "form α_shift(T_{p, k}) = k · (p − 1).  Verifies "
            "10 torus knots (Hopf, trefoil, T_{2,5}, T_{2,7}, T_{2,9}, "
            "T_{3,2}, T_{3,4}, T_{3,5}, T_{4,3}, T_{5,2})."
        )
        .set_audit_only(
            "docs/audits/2026-05-08-crystal-r-matrix-sublemma-2-1.md"
        )
        .add_data("torus_knots", results)
        .add_data("n_verified", n_pass)
        .add_data("n_total", len(targets))
        .add_assertion(
            "crystal_pole_matches_alpha_shift_torus_knot_formula",
            computed=n_pass,
            expected=len(targets),
            source="prop:alpha-shift-torus-knot: α_shift(T_{p, k}) = k·(p−1)",
        )
        .add_caveat(
            "Crystal counter at n_strands ≤ 5 is fully tractable via "
            "SYT enumeration.  Higher (p, k) yielding n_strands > 5 "
            "(e.g. T_{6,2} on 6 strands) becomes slower but still "
            "tractable; the closed-form column-SYT calc in "
            "crystal_pole_order.column_syt_pole_per_cycle gives the "
            "same answer in O(1)."
        )
    )
    out = builder.save()
    print(f"  Witness: {out}")
    return 0 if n_pass == len(targets) else 1


if __name__ == "__main__":
    sys.exit(main())
