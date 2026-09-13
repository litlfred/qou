---
# qou-dux3
title: 'FHW route: the Mobius-invariant exponent is the unique endpoint of the BFHW admissible window'
status: in-progress
type: task
priority: normal
created_at: 2026-09-13T15:19:31Z
updated_at: 2026-09-13T15:25:48Z
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
