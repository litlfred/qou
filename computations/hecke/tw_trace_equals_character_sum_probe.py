#!/usr/bin/env python3
"""tr(L_{T_u}) = sum_lambda d_lambda chi_lambda(T_u), verified across two
independent constructions -- and the convention bridge between them.

Beans `qou-0y6h` (the T_w side) and `qou-avt2` (the character side).

`qou-0y6h` established that the blocker for `det(twGram)` at rank >= 2 is the
diagonal structure constant `[T_u T_w : T_w]`, i.e. `tr(L_{T_u})`, and that it
is NOT determined by `length(u)`, `cycleType(u)`, or the pair
(`tw_regular_trace_statistics_probe.py`).  The reason is that it is a CHARACTER
sum, and Hecke characters are governed by Geck-Pfeiffer's minimal-length
class-representative theory.

This probe confirms that reading rather than asserting it, by computing both
sides independently and symbolically:

* LEFT  -- `tr(L_{T_u})` from the `T_w` multiplication rule alone (the
  construction formalised in `QOU/Hecke/TwMul.lean`), with no character theory
  anywhere in it;
* RIGHT -- `sum_lambda d_lambda chi_lambda(T_u)` from the corpus's Hoefsmit
  seminormal engine, `computations/hecke/hecke_characters.chi_lambda_braid`
  with `precision='symbolic_q'`.

They agree for every element of `S_3`, as exact rational functions.

## The convention bridge, which is the reusable part

The two live in DIFFERENT quadratic normalisations, and the identity is false
without the rescaling:

    this file / QOU.Hecke.IwahoriHecke :  sigma^2 = (Q - 1) sigma + Q
    hecke_characters (seminormal)      :  sigma^2 = (q - 1/q) sigma + 1

Setting `sigma_mine = c sigma_theirs` and matching coefficients gives `c^2 = Q`
and `c(q - 1/q) = Q - 1`, hence

    Q = q^2      and      sigma_mine = q sigma_theirs

so `tr_mine(L_{T_u}) = q^{length(u)} * sum_lambda d_lambda chi_lambda(word)`.
This is the same rescaling `QOU/Hecke/TwFullRank.lean` records between
`QOU.Hecke.IwahoriHecke` and the class `QOU.Hecke.HeckeAlgebra`; here it is
measured rather than quoted.

## Why this matters for the hand-off

It says WHO supplies the missing piece.  `qou-avt2` put exact symbolic
`chi_lambda` for general `lambda` into `hecke_characters.py`; combined with the
identity above, the compute side of `[T_u T_w : T_w]` is already solved at
every rank.  What remains for `qou-0y6h`'s successor is the LEAN formalisation
of that character theory -- not its discovery, and not a search for a
combinatorial shortcut, which is refuted.

It is also a genuine cross-validation of the `T_w` stack: `TwRep ->
TwIndependent -> TwBasisField -> TwMul -> TwTrace` is a `RingQuot` construction
that knows nothing about Young tableaux, and the seminormal engine is built
from axial distances and knows nothing about `T_w`.  Agreement is evidence
about both.

## Precision

Exact symbolic rational functions in `q` throughout (`precision='symbolic_q'`,
sympy).  No float anywhere and none admissible.

Usage:  python3 -u computations/hecke/tw_trace_equals_character_sum_probe.py
"""
from __future__ import annotations

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_COMPUTATIONS = os.path.dirname(_HERE)
if _COMPUTATIONS not in sys.path:
    sys.path.insert(0, _COMPUTATIONS)

from tw_regular_trace_statistics_probe import (  # noqa: E402
    length,
    perms,
    reduced_word,
    regular_traces,
)


def main() -> None:
    import sympy as sp

    from hecke.hecke_characters import (  # noqa: E402
        chi_lambda_braid,
        partitions_of,
        specht_dim,
    )
    from hecke import hecke_characters_symbolic as hcs  # noqa: E402

    q = hcs.q          # the seminormal engine's parameter
    Q = q ** 2         # this file's parameter; see the module docstring

    print("tr(L_{T_u}) = sum_lambda d_lambda chi_lambda(T_u)\n")
    print("  LEFT   the T_w multiplication rule alone   (QOU/Hecke/TwMul.lean)")
    print("  RIGHT  the Hoefsmit seminormal engine      (hecke_characters.py)")
    print("  bridge Q = q^2,  sigma_mine = q sigma_theirs\n")

    m = 3
    left = regular_traces(m, Q)
    shapes = [tuple(lam) for lam in partitions_of(m)]

    all_match = True
    for u in perms(m):
        # The engine wants a signed, 1-BASED braid word.
        word = [(1, i + 1) for i in reduced_word(u)]
        right = sp.Integer(0)
        for lam in shapes:
            right += specht_dim(lam) * sp.sympify(
                chi_lambda_braid(lam, word, precision="symbolic_q")
            )
        scaled = sp.expand(q ** length(u) * right)
        lhs = sp.expand(left[u])
        match = sp.simplify(lhs - scaled) == 0
        all_match = all_match and match
        print(
            f"  u={u} l={length(u)}   {sp.factor(lhs)}"
            f"   {'==' if match else '!='} q^l * sum d chi"
        )

    print()
    assert all_match, "the two constructions disagree — check the bridge first"
    print("Every element of S_3 agrees, as exact rational functions in q.")
    print()
    print("Consequence: the qou-0y6h blocker [T_u T_w : T_w] IS a character sum,")
    print("and qou-avt2 already supplies chi_lambda symbolically at general n.")
    print("What remains is the LEAN formalisation, not the mathematics.")


if __name__ == "__main__":
    main()
