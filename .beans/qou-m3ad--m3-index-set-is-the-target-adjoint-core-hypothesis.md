---
# qou-m3ad
title: 'M3: H_Ad is the dtMin projection (R1 is dtMax) -- not a re-description; but support is ONE data point and rival H_floor survives'
status: in-progress
type: task
priority: high
tags:
    - g3-aomega
    - route-c
created_at: 2026-08-18T21:00:00Z
updated_at: 2026-08-18T22:30:00Z
parent: qou-rtec
---

## The reframing (the main contribution)

M2 showed the closed-sector BPS spectrum would be ABELIAN — every Borel ray distinct,
trivial Davison-Meinhardt plethystic log, dim BPS_d = |Omega_d|, all multiplicities 1.
CONSEQUENCE: a direct sum of 1-dimensional spaces carries no information beyond WHICH
RAYS EXIST. So M3's real target is NOT "build a cohomological Hall algebra" (the
original Route C framing) but **derive the index set Omega**. That is a materially
sharper and more tractable goal, and it is what qou-rtec's M3 rung should now read.

## H_Ad — the hypothesis (NOT a derivation; do not upgrade without a proof)

The knot-INDEPENDENT core of the index set is the weight set of the ADJOINT rep of
sl_2: for meridian eigenvalues (m,1/m) and x=m^2, Ad has eigenvalues (x,1,1/x), so
chi_Ad(x) = x + 1 + 1/x = s(x) exactly and chi_Ad(1) = 3 = dim sl_2.

MECHANISM (why not numerology): in complex Chern-Simons the Borel singularities are
differences of complex volumes of flat connections, and the deformation theory of a
flat connection is governed by H^1(M, Ad rho) — the adjoint local system is the
CANONICAL coefficient object, not a chosen one. In QOU terms Ad = Sym^2 V = the
partition-(2) Wedderburn block of H_2(q), so it is expressible in Hecke language.

## What was tested (probe: computations/probes/aomega_m3_adjoint_index_set.py, 4/4)

 T1 chi_Ad reproduces M2's s(x) exactly — exponents AND multiplicities, no free parameter.
 T2 H_Ad PREDICTS knot-independence; observed (same s(x) governs 5_2, GGM 239/277/307).
    This is the fact that defeated every knot-specific reading (Driver14's eight + R1).
 T3 ADVERSARIAL: H_Ad FAILS as a scalar — knot-independent gives (3,3) vs certified
    (3,4), exactly like blockCountH3. So its content is the GRADING, not the count.
    Recorded so H_Ad cannot be mis-sold as a counting answer.
 T4 ADVERSARIAL: the 3-element palindromic SHAPE is generic ({a,0,-a} for any a), so
    the shape proves nothing; H_Ad rests entirely on its mechanism + the a=1
    normalization forced by x=m^2.

## Lean (QOU/QBeta/AdjointIndexSetM3.lean, core Int, lean-direct exit 0, sorry-free)

 adjoint_multiplicity_free / adjoint_dim_three / adjoint_palindromic / s_at_one_eq_three
 knot_independent_core_forces_unit_remainder  <- THE LOAD-BEARING ONE: any
     knot-independent core forces a knot-DEPENDENT remainder differing by exactly 1.
 adjoint_core_pins_remainder  -> under H_Ad the remainder is pinned to (0, 1).
 no_purely_knot_independent_count -> H_Ad alone is PROVABLY incomplete (derived, not
     conceded).

This converts the otherwise-unfalsifiable move "add one more state for 5_2" into a
structural requirement with a definite value.

## Part 2 (2026-08-18): is H_Ad just R1 again? -- answered, both ways

The adversarial objection was that H_Ad might be a re-description of Route A's
surviving reading R1 (DT integer = #boundary-parabolic SL_2(C) flat connections =
A-polynomial L-degree), since both hand back 3 for 4_1. Settled, using the certified
chirality-split data (4_1 amphichiral -> (S+,S-)=(3,3); 5_2 chiral -> (4,3)):

 NO, IT IS NOT (T5). R1 is the dtMax projection; H_Ad's core is dtMin. Different
   halves of the same datum. And the PAIR reconstructs the 2-element set {3,4} --
   which is NOT in tension with no_scalar_matches_chirality_split_datum, because that
   theorem excludes ONE scalar equalling a 2-set, not two scalars naming it between
   them. This is the sharpest positive structural statement M3 has produced.

 BUT THE EVIDENCE IS ONE DATA POINT (T6). 4_1's amphichirality collapses dtMin onto
   dtMax, so 4_1 gives NO evidence for H_Ad independent of R1. The entire support for
   "the core is knot-independently 3" is the single observation S-(5_2) = 3.

 AND A RIVAL SURVIVES (T7). H_floor: the core is the {0, g, gbar} triple that EVERY
   hyperbolic knot carries -- i.e. R1's own universal floor, with no sl_2 anywhere.
   Its core is also 3, so it imposes identical constraints and makes identical
   predictions; and its Chern-Simons values {0,+V,-V} give a palindromic 3-element
   grading too, so T4's shape screen cannot arbitrate either. The data CANNOT
   separate H_Ad from H_floor. Only the grading VARIABLE could (meridian x=m^2 vs
   Chern-Simons value); GGM's s(x) is written in the meridian variable, which weakly
   favours H_Ad -- "weakly" is the honest word.

 SELF-CORRECTIONS made at source (probe + Lean):
   - T2's note claimed R1 "fails precisely here" (knot-independence). WRONG, retracted.
     R1 hits the dtMax vector (3,4) exactly; its proved failure is single-valuedness
     against a set-valued datum. Conflating the two failure modes would have hidden T5.
   - The previously-proposed completion ("5_2 has one extra flat connection") IS R1.
     So that completion composes two imported readings; it derives nothing from Hecke
     data. Recorded so it is not later mis-sold as a derivation.

Lean added (same file, core Int, lean-direct exit 0, sorry-free): dtPlus / dtMinus /
dtMin / dtMax, r1_is_the_dtmax_projection, h_ad_is_the_dtmin_projection,
min_max_pair_reconstructs_datum, two_scalars_name_what_one_cannot,
fourone_is_a_degenerate_observation, h_ad_and_h_floor_are_indistinguishable,
palindromic_shape_does_not_arbitrate. Probe now 7/7 (T5/T6/T7 added).

## NEXT STEP (the open piece)

Separate H_Ad from H_floor -- that, not "find the extra 5_2 ray", is now the live
question, since the extra ray is just R1. The discriminator is the grading variable:
H_Ad grades the index set by meridian eigenvalue x = m^2, H_floor by Chern-Simons
value. Two ways in: (a) a THIRD knot -- if some hyperbolic K has more than 3
boundary-parabolic connections while its s(x) core stays x+1+1/x, H_floor breaks and
H_Ad survives (GGM covers 4_1 and 5_2; Gu-Marino-type data on 6_1/7_2 would decide);
(b) show the QOU-side Ad = Sym^2 V = partition-(2) block of H_2(q) reproduces the
meridian grading, which H_floor has no route to. Until one lands: HYPOTHESIS ONLY,
now with a NAMED RIVAL, and no derivation of the DT spectrum from Hecke data claimed.
