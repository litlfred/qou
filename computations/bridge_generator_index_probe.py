#!/usr/bin/env python3
"""
bridge_generator_index_probe — WHERE the inter-nucleon bridges sit in the 3A-strand
word, measured; the companion to the Lean proof that those are the only ones there.

Bean `qou-brng`, arc `bk-crossing-mass-binding`. Companion to
`QOU.Mass.StrandLayoutForcesChain`.

## What is measured

`mass_at_3A_proper.atom_braid_word_3A(Z, N, include_inter=...)` emits a list of
`(c, d, gen_idx)` triples. Diffing the `include_inter=False` and `include_inter=True`
words gives exactly the generators the inter-nucleon bridges occupy — read off the
producer rather than off its docstring.

Prediction, from the layout in which nucleon `k` owns strands `3k, 3k+1, 3k+2`:
a bridge between nucleon `k` and `k+1` must be `σ_{3k+2}`, so the added generators
should be `{3k+2 : k = 0 … A−2}` and there should be exactly `A−1` of them.

## Why it matters

`QOU.Mass.StrandLayoutForcesChain` proves (sorry-free, pure ℕ arithmetic) that a
single generator `σ_m` joins two different nucleons iff `m % 3 = 2`, and that when it
does the two nucleons are **consecutive**. So the chain is not one bond set chosen
among others — it is the only one expressible as single crossings under this layout.

This probe supplies the premise: that the producer does in fact place its bridges at
those generators. A theorem about the layout says nothing about a producer until the
producer is measured against it (AGENTS.md §"Grep the claim SHAPE": a conditional
result proves the implication, never the premise).

## Scope

Scope **(a)**: a statement about where this producer puts its crossings. It does not
say which bond set the physics wants.

NO FLOAT64: the measurement is over integer generator indices; no arithmetic on
values occurs at all.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401

from collections import Counter  # noqa: E402

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402


NUCLEI = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2),
          ("6Li", 3, 3), ("7Li", 3, 4), ("9Be", 4, 5), ("12C", 6, 6)]


def main() -> int:
    print("bridge_generator_index_probe")
    print("=" * 78)
    print("Diffing atom_braid_word_3A(include_inter=False) against (=True): the")
    print("generators the inter-nucleon bridges occupy, read off the producer.")
    print()
    print(f"{'nucleus':>8} {'A':>3} {'strands':>8} {'bridge generators':>34} "
          f"{'count':>6} {'= A-1':>6} {'= 3k+2':>7}")

    all_idx_ok = all_count_ok = True
    for name, Z, N in NUCLEI:
        A = Z + N
        w0 = atom_braid_word_3A(Z, N, include_inter=False)
        w1 = atom_braid_word_3A(Z, N, include_inter=True)
        extra = Counter(g for _c, _d, g in w1) - Counter(g for _c, _d, g in w0)
        gens = sorted(extra.elements())
        predicted = [3 * k + 2 for k in range(A - 1)]
        idx_ok = gens == predicted
        count_ok = len(gens) == A - 1
        all_idx_ok &= idx_ok
        all_count_ok &= count_ok
        print(f"{name:>8} {A:>3} {3*A:>8} {str(gens):>34} {len(gens):>6} "
              f"{('yes' if count_ok else 'NO'):>6} {('yes' if idx_ok else 'NO'):>7}")
    print()
    print(f"  every bridge at 3k+2, k = 0..A-2 : {all_idx_ok}")
    print(f"  exactly A-1 bridges              : {all_count_ok}")
    print()

    # The layout claim itself, checked numerically over a wide range: which
    # generators of a 3A-strand braid cross a nucleon boundary at all?
    print("Which generators of a 3A-strand braid cross a nucleon boundary?")
    print("  block(m) = m // 3 ; sigma_m swaps strands m, m+1.")
    print(f"{'A':>4} {'crossing gens (m//3 != (m+1)//3)':>44} {'all m%3==2':>11} "
          f"{'all consecutive':>16}")
    layout_ok = True
    for A in (2, 3, 4, 6, 10):
        cross = [m for m in range(3 * A - 1) if m // 3 != (m + 1) // 3]
        mod_ok = all(m % 3 == 2 for m in cross)
        adj_ok = all((m + 1) // 3 == m // 3 + 1 for m in cross)
        layout_ok &= mod_ok and adj_ok
        shown = str(cross if len(cross) <= 9 else cross[:9] + ["..."])
        print(f"{A:>4} {shown:>44} {str(mod_ok):>11} {str(adj_ok):>16}")
    print(f"  layout claim holds on every A tried: {layout_ok}")
    print()

    ok = all_idx_ok and all_count_ok and layout_ok
    print("Reading")
    print("-" * 78)
    if ok:
        print("  * The producer places its inter-nucleon bridges at 3k+2 for")
        print("    k = 0..A-2 -- exactly the generators that cross a nucleon")
        print("    boundary, and exactly A-1 of them.")
        print("  * Every boundary-crossing generator joins CONSECUTIVE nucleons.")
        print("    So under this layout the chain is not one bond set chosen among")
        print("    others: it is the only one expressible as single crossings.  A")
        print("    non-adjacent bond would need a word transporting strands past")
        print("    each other, which this producer does not write.")
        print("  * Proved for all A, not just those tabulated, in")
        print("    QOU.Mass.StrandLayoutForcesChain (crossesBlocks_iff,")
        print("    adjacent_of_crosses, no_single_generator_joins_nonadjacent).")
        print("  * Consequence: the layout is a LINEAR ORDER on nucleons, so the")
        print("    chain bond set and the nucleon-ordering convention are the SAME")
        print("    unlicensed choice -- merging this question into qou-48is, where")
        print("    the ordering is measured to move tr_M by O(10 %) at A >= 3.")
    else:
        print("  * A check FAILED above; do not quote the conclusion.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
