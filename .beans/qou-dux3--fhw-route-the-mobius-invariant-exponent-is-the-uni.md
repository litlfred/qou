---
# qou-dux3
title: 'FHW route: the Mobius-invariant exponent is the unique endpoint of the BFHW admissible window'
status: in-progress
type: task
priority: normal
created_at: 2026-09-13T15:19:31Z
updated_at: 2026-09-13T15:40:10Z
---

## RESULT: two independent criteria pin the exponent, and mine is the stronger

QOU/FHWExponentWindow.lean, 7 declarations, all [propext, Classical.choice,
Quot.sound], 0 sorryAx, lean -DautoImplicit=false -s 65536 exit 0.

THE SETUP. Bryson-Freedman-He-Wang (Bull. AMS 28 (1993) 99-103, now held at
library/arxiv-math-9301212v1/) treat the exponent -2 as A CHOICE AMONG
CANDIDATES, verbatim:

  "there are competing candidates for the exponent = -2 ... the Newtonian
   potential in R^3 has exponent = -1. When the exponent is strictly larger
   than -3, finite values are obtained for smooth simple loops. Exponents
   smaller or equal to -2 yield energies which blow up as a simple loop begins
   to acquire a double point, thus creating an infinite energy barrier to a
   change of topology."

So their two requirements bracket it: finiteness needs e > -3, the topological
barrier needs e <= -2. Window (-3, -2]. A CONTINUUM -- it excludes Newtonian
-1 but admits -2.5 (bfhwWindow_not_singleton proves the window is not a point;
neg_one_not_mem_bfhwWindow checks the encoding against their own remark).

MobiusMutualChannel section 7 pins it to exactly -2.
mobiusInvariant_rpow_exponent_eq_neg_two specialises section 7 to power laws
and solves: d^e Mobius-invariant against arclength ==> e = -2.

## 🛑 THE SHARPEST FORM IS NOT "THEY INTERSECT"

bfhw_window_mobius_unique carries the window hypothesis and DOES NOT USE IT --
Lean flags `_hw` unused, correctly. Mobius invariance alone pins the exponent.
So the relation is not a joint derivation of a shared point: the conformal
criterion is STRICTLY STRONGER, and BFHW's window is an independent CHECK on
it that it passes, landing on the endpoint.

That distinction is the whole epistemic value. A joint derivation would be two
assumptions doing one job. What this is instead: one criterion determines the
answer, and a second, unrelated one (finiteness + an energy barrier to changing
knot type, from the literature, not from this corpus) is consistent with it.

## WHAT IS CITED AND NOT PROVED

BFHWWindow is a PREDICATE ENCODING BFHW's two claims. This file does not prove
that e > -3 gives finiteness or that e <= -2 gives the barrier -- those are
analytic results of [bryson-freedman-he-wang1993]. The corpus holds the paper,
not a proof. Do not cite this file as establishing them.

## WHAT DOES NOT TRANSFER

BFHW's Theorem D, 2*pi*c([gamma]) + 4 <= E(gamma), is about the SELF energy of
a SINGLE CLOSED CURVE. qou-o6ml route 2 owns the PAIRWISE term. I checked the
paper for a link/multi-component version: there is none -- the only hit for
"link|component|disjoint" across its sections is an unrelated use of
"disjointness" in a normal-fibre argument. So the crossing bound does NOT bound
the mutual channel, and this file does not pretend otherwise. What transfers is
the EXPONENT question, which is about the kernel and is shared by both channels.

BEAN STAYS OPEN: the crossing bound's own route to a mutual-channel
discriminator needs a link version, which the corpus does not hold.


## 🛑 I OVER-CLAIMED WHAT BFHW SUPPLY — caught before merge, corrected in the file

My first draft said the window facts "are analytic results of
[bryson-freedman-he-wang1993]". Wrong on BOTH halves, found by reading the page
around the quote instead of the quote:

1. NOT A THEOREM OF THEIRS. The passage is an UNNUMBERED REMARK sitting between
   the statement of Theorem E and the proof of Theorem A. No proof in that
   document.
2. NOT THEIRS TO PROVE. It defers, verbatim: "We refer to [O1-O3] for detailed
   discussions." Those are O'Hara -- [O1] Energy of a knot (Topology 30 1991,
   HELD), [O2] Family of energy functionals of knots (Topology Appl.), [O3]
   Energy functionals of knots (World Scientific). [O2] and [O3] are where the
   exponent range actually lives and the corpus holds NEITHER -- checked by
   title across every library/*/structure.json.

So BFHWWindow encodes a claim whose proof is in no held document. That is now
said in the file.

## 🛑 AND THE RESULT IS NOT NEWS TO THEM

The same remark closes: "Similarity and Mobius invariance are, OF COURSE,
special to the exponent -2."

I missed that sentence on the first read and it changes the standing of the
result. The statement mobiusInvariant_rpow_exponent_eq_neg_two establishes was
regarded as evident in 1993. This file does NOT discover it.

WHAT SURVIVES, and it is narrower but real:
  - it PROVES what they assert without proof, sorry-free, from the invariance
    hypothesis alone;
  - it proves UNIQUENESS. BFHW say invariance is "special to" -2, i.e. that -2
    HAS the property. The theorem here is that -2 is the ONLY exponent that
    does. That direction is not in their sentence.

DO NOT describe this work as showing the exponent was open, or as settling
something BFHW left open. They left the MODELLING choice open among candidate
knot energies while treating the Mobius characterisation as obvious. Different
things.

## Provenance of the catch

A sibling agent landed 8f6f0a8af8 ("I over-claimed 'the FHW bound is now held'
-- reading the PROOF sharpens it three ways") correcting their own reading of
the same paper. Their point 3 confirms my Lean is untouched. Re-reading the
document on the strength of that is what surfaced my own over-claim, which they
could not have caught -- #7317 did not exist when they wrote.
