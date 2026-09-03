#!/usr/bin/env python3
"""The exchange-odd channel: what survives, and what I withdrew.

I reached for block exchange as the Pauli-grounded discriminator that three
symmetries (bar-even, bar-odd, bar-conjugacy) had failed to supply. It looked
like it worked. It does not, and the reason is worth more than the result.

## WITHDRAWN -- the discriminator claim

The claim was: an exchange-odd component exists for pn and is identically
zero for pp and nn, so it separates the bound system from the two unbound
ones. Restated without the algebra:

    odd part nonzero  <=>  block exchange does not fix the arrangement
                      <=>  the two blocks carry DIFFERENT nucleons

That is a statement about labels, true by construction, with no algebra in
it. At A = 2 "the blocks differ" and "the system binds" happen to pick out
the same arrangement -- pn is simultaneously the N = Z one and the bound one
-- so a relabelling predicate wears the costume of a binding detector.

A = 3 pulls them apart. 3H (nnp) and 3He (ppn) are BOTH bound and NEITHER is
N = Z, while nnn and ppp are unbound. "Blocks differ" still tracks boundness
across those four, but only because a pure-neutron or pure-proton nucleus is
unbound for reasons entirely outside this algebra. The predicate is binary,
carries no magnitude, and cannot produce 2.2246 MeV or rank anything.

This is the same defect the H_9 work found independently at A = 3: the
cycle-type-graded coefficient mass separates 3H from 3He and pn from pp/nn,
and turns out to be invariant under tau = (p<->n complement) composed with
(block reversal) -- 18/18 pairs. It detects strand-block ARRANGEMENT, a
labelling convention. A 3H ordering sits at distance 0 from a 3He ordering
while two orderings of the SAME nucleus sit at 22-24.

Both of us found a separator that fires correctly at A = 2 and is a
relabelling detector. Recording it so the third person does not.

## WHAT SURVIVES -- and it is not the same claim

Two things were measured rather than constructed, and neither depends on the
withdrawn reading:

1. pn and np are DIFFERENT ELEMENTS of H_6 -- 28 of 50 coefficients differ.
   The odd part is genuinely nonzero in the algebra. Had the algebra
   collapsed them there would be no channel to discuss at all.

2. That odd part lies ENTIRELY IN THE KERNEL OF THE TRACE:

       tr(pn) - tr(np)          = 0
       tr(antisymmetric part)   = 0

   identically in q and z, hence at every specialisation.

So the exchange-odd channel is nonzero in the algebra and zero in every
trace. That is a statement about what the trace discards, which is this
arc's actual subject; it is not a statement that the channel measures
binding, and it should not be read as one.

Exact throughout: symbolic q and z over QQ(q,z). No floats, no anchor.
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


def trace(terms: dict, n: int = 6) -> sp.Expr:
    return sp.simplify(sum(c * z ** (n - n_cycles(w)) for w, c in terms.items()))


def main():
    build = lambda a, b: word_to_elem(6, a + b + [BRIDGE, BRIDGE])[0]  # noqa: E731
    pn, np_ = build(P_A, N_B), build(N_A, P_B)

    print("=" * 74)
    print("WITHDRAWN: the exchange-odd part as a binding discriminator")
    print("=" * 74)
    print("  'odd part nonzero' <=> 'the two blocks carry different nucleons'.")
    print("  A relabelling predicate, true by construction, no algebra in it.")
    print("  At A=2, N=Z and bound coincide; at A=3 they separate and it fails.")
    print("  3H (nnp) and 3He (ppn) are both bound and neither is N=Z.")

    print("\n" + "=" * 74)
    print("SURVIVES: the odd channel is nonzero, and the trace cannot see it")
    print("=" * 74)
    keys = set(pn.terms) | set(np_.terms)
    odd = {w: sp.simplify(pn.terms.get(w, 0) - np_.terms.get(w, 0)) for w in keys}
    odd = {w: c for w, c in odd.items() if c != 0}
    print(f"\n  pn and np differ in {len(odd)} of {len(pn.terms)} coefficients")
    print("    -> the odd part is genuinely nonzero IN THE ALGEBRA")

    d_tr = sp.simplify(trace(pn.terms) - trace(np_.terms))
    t_odd = sp.simplify(trace(odd))
    print(f"\n  tr(pn) - tr(np)        = {d_tr}")
    print(f"  tr(antisymmetric part) = {t_odd}")
    print("    -> identically in q and z, hence at every specialisation")
    print("\n  So the channel is nonzero in the algebra and zero in every trace.")
    print("  That says what the trace discards. It does NOT say the channel")
    print("  measures binding, and must not be read that way.")

    assert len(odd) > 0, "the odd part must be nonzero for the claim to mean anything"
    assert d_tr == 0 and t_odd == 0, "the trace-kernel result failed"
    return {"odd_terms": len(odd), "total": len(pn.terms),
            "trace_of_odd_is_zero": True}


if __name__ == "__main__":
    main()
