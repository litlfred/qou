#!/usr/bin/env python3
"""The uncoloured Markov trace assigns the SAME binding to the deuteron and
the diproton -- exactly, at every z.

What is measured
----------------
Three two-nucleon systems on six strands, differing only in which nucleon
words sit on the two B_3 blocks:

    p + n   the DEUTERON, bound by 2.2246 MeV
    p + p   the diproton,  NO bound state
    n + n   the dineutron, NO bound state

For each, the Ocneanu/Markov trace `tr(T_w) = z^(n - cycles(w))`, extended
linearly, with BOTH q and z free.

Result, as a polynomial identity in two free variables -- not a numerical
coincidence and not a specialisation artifact:

    tr(free)  is identical across all three
    tr(bound) is identical across all three
    hence  Delta_tr = tr(free) - tr(bound)  is identical across all three

Because it vanishes identically in `z`, it vanishes at EVERY specialisation
of z, so the conclusion does not depend on the convention-D value
z = q^3/(q^2+1) or on any other choice.

The mechanism
-------------
    tr(proton alone on 3 strands) == tr(neutron alone on 3 strands)

exactly. The proton (s1 s2^-1)^3 and neutron (s1^-1 s2)^3 are mirror words,
and the trace of the bound six-strand system factorises over the two disjoint
blocks -- visibly, as (...)*(block)^2/q^11. A product of equal block traces
cannot depend on which block is which. Swapping a proton for a neutron is
invisible to it by construction.

Why this is not a claim that the binding compute is broken
----------------------------------------------------------
It is the precise structural reason the COLOUR WEIGHTING is load-bearing.
`bring_color_weighted` was made the canonical p/n convention by the
2026-08-15 owner ruling R3, and `computations/_deprecated/schur_weyl_q_hecke.py`
was deprecated with the note that it works from cycle type and "cannot
distinguish proton from neutron". This probe measures exactly how far that
blindness goes and where it comes from: not a coarse invariant, not the
specialisation, but the factorisation of the trace over blocks whose traces
are equal.

So the scope is scope-(a) and narrow: the UNCOLOURED Markov trace cannot
separate these three at any z. It says nothing about the coloured trace, and
this probe does not evaluate the production path. What it does supply is a
sharp requirement on any p/n-sensitive weighting: it must break the block
factorisation, because anything that respects it inherits this blindness.

Companion result (`isospin_triplet_filtration_probe.py`, merged d5c779878):
20 of 50 individual T_w coefficients DO differ between pn and pp. The
information is present in the algebra; the trace and the grade-mass are the
two projections that discard it.

Exact throughout: symbolic q AND symbolic z over QQ(q,z). No floats, no
substrate anchor, no z-specialisation.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import sympy as sp  # noqa: E402

from jet_history_retention_probe import word_to_elem  # noqa: E402
from isospin_triplet_filtration_probe import (  # noqa: E402
    P_A, N_A, P_B, N_B, BRIDGE,
)

z = sp.symbols("z")


def n_cycles(w: tuple) -> int:
    """Number of cycles of the permutation (1-indexed images)."""
    seen, c = set(), 0
    for s in range(len(w)):
        if s in seen:
            continue
        c += 1
        x = s
        while x not in seen:
            seen.add(x)
            x = w[x] - 1
    return c


def markov_trace(E) -> sp.Expr:
    """Ocneanu/Markov trace with FREE parameter z: tr(T_w) = z^(n - cycles(w))."""
    return sp.simplify(sum(c * z ** (E.n - n_cycles(w)) for w, c in E.terms.items()))


def main():
    print("Is the uncoloured Markov trace blind to p vs n?\n")
    systems = {"p n (deuteron, BOUND)": (P_A, N_B),
               "p p (diproton, unbound)": (P_A, P_B),
               "n n (dineutron, unbound)": (N_A, N_B)}
    free, bound = {}, {}
    for k, (a, b) in systems.items():
        F, _ = word_to_elem(6, a + b)
        B, _ = word_to_elem(6, a + b + [BRIDGE, BRIDGE])
        free[k], bound[k] = markov_trace(F), markov_trace(B)

    ref = "p n (deuteron, BOUND)"
    print("  Differences against the deuteron, as polynomials in q and z:")
    all_zero = True
    for k in systems:
        if k == ref:
            continue
        df = sp.simplify(free[k] - free[ref])
        db = sp.simplify(bound[k] - bound[ref])
        dd = sp.simplify((free[k] - bound[k]) - (free[ref] - bound[ref]))
        all_zero &= (df == 0 and db == 0 and dd == 0)
        print(f"    {k}")
        print(f"      tr(free)  difference : {df}")
        print(f"      tr(bound) difference : {db}")
        print(f"      Delta_tr  difference : {dd}")

    print(f"\n  All identical, for free q and free z: {all_zero}")
    print("  Vanishing identically in z means it vanishes at EVERY z, so this")
    print("  is not an artifact of the convention-D choice z = q^3/(q^2+1).")

    print("\n  MECHANISM -- the block traces are equal:")
    pA, _ = word_to_elem(3, [1, -2, 1, -2, 1, -2])
    nA, _ = word_to_elem(3, [-1, 2, -1, 2, -1, 2])
    eq = sp.simplify(markov_trace(pA) - markov_trace(nA)) == 0
    print(f"    tr(proton alone) == tr(neutron alone) : {eq}")
    print("    and the six-strand trace factorises over the two disjoint")
    print("    blocks, so a product of equal factors cannot depend on order.")
    print("\n  Consequence: any p/n-sensitive weighting must BREAK the block")
    print("  factorisation. Anything respecting it inherits this blindness.")
    assert all_zero and eq
    return {"all_identical": all_zero, "block_traces_equal": bool(eq)}


if __name__ == "__main__":
    main()
