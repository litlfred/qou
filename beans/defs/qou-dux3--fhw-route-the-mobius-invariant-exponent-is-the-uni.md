---
# qou-dux3
title: 'FHW route: the Mobius-invariant exponent is the unique endpoint of the BFHW admissible window'
status: completed
type: task
priority: normal
created_at: 2026-09-13T15:19:31Z
updated_at: 2026-09-13T17:19:32Z
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


## THE LINK VERSION EXISTS. I DERIVED IT, AND IT IS EMPTY ON A BRUNNIAN PAIR

The paragraph above says "BEAN STAYS OPEN: the crossing bound's own route to a
mutual-channel discriminator needs a link version, which the corpus does not
hold." The premise is right and the conclusion drawn from it was too weak: a
link version does not have to be HELD, it can be DERIVED, and this one costs a
determinant estimate.

MobiusMutualChannel.lean section 9, 17 declarations, all [propext,
Classical.choice, Quot.sound], 0 sorryAx; whole file 43/43,
lean -DautoImplicit=false -s 65536 exit 0, zero warnings.

THE DERIVATION, in one line. Gauss's linking integral has |gamma_1 - gamma_2|^3
in the denominator; |det(a,b,c)| <= |a||b||c| spends one power of that on the
numerator's |c|; what is left is EXACTLY the Mobius mutual integrand. Hence

    4*pi*|lk(gamma_1, gamma_2)|  <=  E_mutual(gamma_1, gamma_2).

  det3_sq_le / abs_det3_le           Cauchy-Schwarz against a x b, then
                                     Lagrange's identity to drop the <a,b>^2.
                                     Both `ring` facts; nothing imported.
  gaussIntegrand_le_mutualIntegrand  the pointwise domination, PROVED.
  four_pi_abs_lk_le_energy           the bound, by monotonicity of the integral.

A CONSISTENCY CHECK ON SECTION 7, not a new assumption: the inverse square is
not put in, it FALLS OUT of that cancellation. So the kernel sections 7-8 force
by Mobius invariance is the same kernel for which a topological lower bound
exists.

## AND IT DOES NOT REACH THE CHANNEL THE FRAMEWORK NEEDS

qou-o6ml's gate for route 2 is a mutual channel NONZERO on a pairwise-unlinked
pair. Every pairwise lk of the Borromean link is 0
(mirror_split_s3_em_functional_probe.py A3). Against that gate the bound is
empty, and lk_bound_iff_nonneg_of_lk_zero proves the emptiness rather than
asserting it: at lk = 0 its conclusion is EQUIVALENT to 0 <= E_mutual, which
section 3's innerPairEnergy_nonneg already gives with no hypotheses at all.

The failure is not specific to this bound. no_positive_uniform_mutual_lower_bound:
NO positive constant lower-bounds the mutual pair energy, because the
separatedLink family realises every small positive value via section 3's own
innerPairEnergy_le. Scope (b) in the AGENTS.md sense, invariant cited; it
excludes TOPOLOGICAL lower bounds only.

CONSEQUENCE FOR ROUTE 2, and this is the reusable part: the Mobius mutual
channel is a GEOMETRIC quantity. Any magnitude it supplies must come from a
DERIVED CONFIGURATION, never from the pair's link type. An agent hoping the
knot-energy literature would hand route 2 a parameter-free number off the
topology should stop -- the first-order bound is the one that exists, and it
vanishes exactly where the Borromean configuration sits.

## WHAT IS ASSUMED, AND THE NEGATIVE I AM CAREFUL ABOUT

ASSUMED: Gauss's integral formula for the linking number, carried as the
explicit hypothesis hgauss rather than as a class field. Monotonicity and
oddness of the integral are the other two. The pointwise domination is NOT
assumed -- section 9b proves it.

NOT CLAIMED: that this is new. I DID NOT FIND the bound in the held literature
-- searched content/, computations/, docs/, .beans/ and library/*/sections/ +
library/*/ocr/ for "gauss linking", "cross energy", "4 pi lk", and a linking-
number-versus-energy comparison; zero hits. That is a statement about THE
SURFACE I SEARCHED, not about the mathematics: the argument is two classical
inequalities and the result is very likely standard in the Mobius-energy
literature (the sharp non-split bound of Agol-Marques-Neves would be the place
to look, and the corpus does not hold it). Cite this file for the DERIVATION,
never for priority.

NOT CLAIMED: that inf E_mutual = 0 over an ISOTOPY CLASS. LinkEmbedding carries
no isotopy data, so section 9d quantifies over the separatedLink family, not
over configurations reachable from a fixed link. The classical fact that a
pairwise-unlinked pair is isotopic to a split link would upgrade it; it is not
formalised here.

## STATUS OF THIS BEAN

Both halves of the FHW route are now answered. The exponent question: settled,
-2 uniquely, sections 7-8 + FHWExponentWindow.lean. The crossing-bound
question: settled with a NEGATIVE, section 9. The positive target -- a derived
geometry for the mutual channel -- is qou-o6ml's, not this bean's. Staying
in-progress only until the PR lands.



## LANDED 2026-09-13 — PR #7317 merged as ea1220654e

Merge-commit route (four merge commits on the branch; qou-md01 measures that
rebase-merge 500s deterministically on such a branch).

Both halves of the FHW route are answered and this bean's own question is
closed:

  the exponent question   settled, -2 uniquely, sections 7-8 of
                          MobiusMutualChannel.lean + FHWExponentWindow.lean.
  the crossing bound      settled with a NEGATIVE, section 9: the link version
                          of Theorem D is derivable, and is EMPTY on a
                          Brunnian pair.

Final verification at the merged head: MobiusMutualChannel.lean 52/52 and
FHWExponentWindow.lean 7/7, all [propext, Classical.choice, Quot.sound], 0
sorryAx, lean -DautoImplicit=false -s 65536 exit 0, zero warnings, against a
shadow with all 41 cone modules rebuilt from source.

WHAT IS NOT CLOSED BY THIS, and it is not this bean's: the POSITIVE target --
a derived geometry for the mutual channel. That is qou-o6ml (constraints 3 and
3b) and, for the configuration itself, qou-ales. Completing this bean records
that the FHW ROUTE is worked out; it does not record that route 2 has a
magnitude.
