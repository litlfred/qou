---
# qou-0pnj
title: 'GAP: prop:toffoli-lp-stability''s t(q) does not exist — G is 6x6 Hecke-NF, P_77/P_76 are 8x8 strand-ordering entries'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T09:57:56Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-10v9
---

FOUND 2026-08-30 investigating what the q-GoL "stability condition" actually
asserts (owner asked for options + pros/cons). The investigation did not end
where it was aimed: the positivity-vs-non-vanishing question is a PROXY for a
computation that has never been performed, and the two sides of the reduction
it rests on live in different index spaces.

## What prop:toffoli-lp-stability asserts

Statement:  "Express the q-Toffoli in normal-form coordinates as
             T_q = sum_{i=1..6} t_i(q) b_i"
Proof:      "Positivity of G.t(q) therefore reduces to the positivity of the
             product P_77(q) . W_std(q) with the appropriate sign from Phi(q)."

## MEASURED — t(q) does not exist anywhere in the corpus

computations/toffoli-lp-stability.py is the producer. Its main() computes, per
grid point: P_77, q_AND_P76, and the Gram eigenvalues. Witness scan-row keys,
read off the committed file:

    ['P_77','P_77_sign','gram_condition','gram_eigenvalues','gram_lambda_max',
     'gram_lambda_min','q','q_AND_P76','q_AND_P76_sign']

There is no t vector and no G.t anywhere in the producer or the witness. The
central quantity of the proposition has never been constructed, so the LP
feasibility of the q-Toffoli has never been tested -- by this producer or any
other. Grep for a Toffoli NF coordinate vector across computations/ returns
nothing.

## And the two sides have DIFFERENT INDEX SPACES

G is 6x6 over the Hecke normal-form basis. Confirmed by direct import:

    pyhecke.gram.NF_BASIS = [(), (0,), (1,), (0,1), (1,0), (0,1,0)]     len 6

  = dim H_3(q) = 3! = 6.

P_77 and P_76 are entries of an 8x8 matrix. The ONLY recorded construction is
computations/_deprecated/toffoli-braid.py::build_matrix, whose docstring reads
"8x8 massive Toffoli transfer matrix" and whose loop is

    for k in range(8):
        ordering_k = list(decode(k))
        M[k][k] = markov_trace(ordering_k)

so k indexes a STRAND-TYPE ORDERING (3 binary choices, 2^3 = 8), not a Hecke
basis word. Index 7 = (1,1,1), index 6 = (1,1,0) -- the control-control-target
semantics. The entries ARE Hecke scalars (Markov traces), but the MATRIX is
indexed by orderings.

So the reduction relates a 6-dimensional cone condition (G.t >= 0, six
inequalities over the NF basis) to two scalars drawn from an 8x8 matrix over a
different index set. No map between the two is recorded. That is WHY the
"appropriate sign from Phi(q)" clause could never be derived: there is no t,
and no bridge from the ordering-indexed matrix to the NF-indexed cone.

W_std = (q^2+1)^2/(q^4+4q^2+1) IS a Hecke object -- the Wedderburn weight of
the 2-dim standard rep of H_3(q) (dims 1,2,1 -> 1+4+1 = 6, checks out). So the
proof mixes three things: a Hecke NF Gram, a Hecke Wedderburn weight, and an
ordering-indexed transfer-matrix entry.

## Two further blockers on measuring it directly

1. The producer's own Gram uses the RETRACTED naive length rule --
   `tr += c * (z ** len(w))` at toffoli-lp-stability.py:205, i.e.
   tr_M(T_w) = z^len(w), which the content block itself calls "the retracted
   naive length rule ... the pre-2026-05-19 tr_M(e^-) = z^3 bug". So even the
   Gram that IS computed is not the production one. pyhecke.gram.gram_matrix_mp
   is the correct one and is available.
2. The only Toffoli construction is in _deprecated/.

## Consequence for the open item in prop:q-game-of-life

The block currently offers a choice between positivity (LP feasibility) and
non-vanishing (universality). That framing survives, but it understates the
situation: the LP-feasibility branch is not merely unsettled, its central
object is unconstructed. A ruling that picks positivity would be selecting a
criterion nothing can currently evaluate.

NOT filed as a refutation. Scope (a): what is established is that the
computation has not been done and the recorded reduction does not typecheck as
written. Whether a correct bridge exists -- e.g. t(q) obtained by expanding the
Toffoli braid word in NF and the 8x8 arising as its action on orderings -- is
open and is the natural next step.


## MEASURED 2026-08-30 — t(q) IS constructible, and the result inverts the story

computations/probes/toffoli_nf_coordinates_and_lp_feasibility.py, 8/8 orderings.

WHAT MADE IT POSSIBLE, correcting my own framing above. I wrote that the
construction "works entirely in scalars" and that option-1 needed a braid word
that does not exist. Half right. The deprecated producer prints its own
convention: "Crossing coefficients C_{ij} = c_j sigma_i + d_j" -- that IS an
algebra element. And chain_reduce's recursion

    new_a = a*c*ha + a*d + b*c ;  new_b = a*c + b*d

is exactly (a s + b)(c s + d) reduced by s^2 = ha*s + 1. So chain_reduce
returns the coefficients of prod_{j>i}(c_j sigma_i + d_j) = a_i sigma_i + b_i,
and the Toffoli element is the product over generators. No braid word is
needed; the element was implicit in the crossing coefficients all along.

Verified by hand for the all-proton ordering: (c,d) = (1,0) at every crossing,
so chain 0 = sigma_0^2 = ha sigma_0 + 1, chain 1 = sigma_1, and

    T_q(1,1,1) = ha sigma_0 sigma_1 + sigma_1,   ha = q - 1/q.

At q0 the NF vector is [0, 0, 1.0, 0.2090603, 0, 0] and ha(q0) = 0.20907. The
probe reproduces exactly that, so the multiplication is right.

RESULT: G.t(q0) >= 0 for ALL 8 orderings, including k=7 = (1,1,1), the
Toffoli's own control-control-target ordering. Every component strictly
positive. Gram is pyhecke.gram.gram_matrix_mp (production, convention D), NOT
the producer's own -- which uses the retracted naive length rule.

GRAM CROSS-CHECK, so this is provably the same object the proof block
discusses: eigenvalues [-0.75270211, 8.4e-51, 0.75270211 x3, 4.2303392].
lambda_min = -0.7527021133 reproduces the -0.75270211 recorded in
toffoli-lp-stability-proof.md, and the 8.4e-51 confirms the form is SINGULAR,
also as recorded.

## HOW MUCH IT IS WORTH — less than it looks, and the probe says so

The Gram is ENTRYWISE NON-NEGATIVE (0 negative entries of 36). So G.t >= 0 is
informative only where cancellation was possible. Per-ordering: 2 of the 8 are
TRIVIALLY feasible because t is entrywise non-negative too -- and k=7 is one of
them. The other 6 have negative t components and are genuine.

So: the condition the proposition STATES is satisfied at the substrate, but for
the ordering that matters it is satisfied by shape rather than by physics. Do
not quote "the q-Toffoli is LP-feasible at q0" without that qualifier.

## THE REAL FINDING — the two sign structures run OPPOSITE ways

t(k=7) = sigma_1 + ha sigma_0 sigma_1 has a negative component exactly when
ha = q - 1/q < 0, i.e. on 0 < q < 1.

    q > 1 :  P_76 < 0  (amplitude negative)  BUT  t entrywise >= 0, G.t > 0
    q < 1 :  P_76 > 0  (amplitude positive)  BUT  t acquires a negative entry

The amplitude sign and the cone condition move in OPPOSITE directions across
q = 1. That is a direct obstruction to the proof's reduction, which reads the
cone condition off the amplitude sign -- it is not merely that the index spaces
differ, it is that the two quantities disagree about which side of q = 1 is the
good one.

## CONSEQUENCE for the prop:q-game-of-life open item

The positivity-vs-non-vanishing dilemma is largely dissolved: under BOTH
readings the substrate is fine. Non-vanishing holds for every q != 1;
LP-feasibility, computed directly rather than via the reduction, holds at q0.
What does NOT survive is the reduction connecting them.

SCOPE (a). This measures the stated condition at one anchor. It does not prove
the reduction false -- it exhibits a sign disagreement that any correct
reduction would have to explain.


## CLOSED-OUT 2026-08-30 — the sign disagreement is an IDENTITY, and it excludes the reduction

The entry above recorded the disagreement as MEASURED at q0. Measured is
weaker than proved, and this one is provable in two lines.

    hbar = q - 1/q = (q-1)(q+1)/q

so the derived flip amplitude factors as

    P_76(q) = -(q-1)(q+1) S / (2 q (q^2+1)^2)
            = - hbar * S / (2 (q^2+1)^2),      S = q^6+q^4+2q^2+1

EXACTLY -- sympy simplify of the difference returns 0. S has NO real root and
(q^2+1)^2 > 0, so the cofactor is strictly positive on all of R. Meanwhile the
q-Toffoli's NF coordinate on the word (0,1) is +hbar. Therefore

    sign P_76(q) = - sign t_(0,1)(q)     for every q > 0, identically.

Not an anchor coincidence, not a convention artefact: an algebraic identity.

FORMALIZED, sorry-free:
  QOU.Information.toffoliSextic_pos                 (positivity)
  QOU.Information.toffoliFlipAmplitude_eq           (the factorisation)
  QOU.Information.toffoliFlip_mul_coneCoord_nonpos  (the payoff: product <= 0)
lean-direct exit 0; #print axioms on all three = [propext, Classical.choice,
Quot.sound], no sorryAx. Symbolic cross-check
computations/probes/toffoli_sign_inversion_is_structural.py, 7/7, exact
arithmetic, no floating point in the proof.

SCOPE (b) EXCLUSION, invariant cited. No reduction in which the LP cone
condition INHERITS the flip amplitude's sign can hold -- at any anchor, in any
convention -- because the two carry opposite signs of the same factor.

NOT EXCLUDED, and this is the remaining candidate: a reduction with a NEGATIVE
proportionality, i.e. one in which the cone condition follows -P_76. Nothing
here bears on that.

WHAT REMAINS OPEN in this bean: the index-space mismatch is untouched by the
above. G.t is a 6-vector over the Hecke NF basis; P_77/P_76 are entries of an
8x8 matrix indexed by strand-type orderings. A correct reduction still needs a
map between them, and none is recorded. The sign result narrows WHICH map
could work; it does not supply one.


## ALL ARC ASSERTIONS NOW LEAN-PROVED 2026-08-30

Owner asked for every assertion to be Lean-proved. Eleven new sorry-free
theorems in the block's own sibling, all axioms [propext, Classical.choice,
Quot.sound], file has 0 sorries:

  toffoliDiagonal_pos              P_77 > 0 on q > 0 (no positive root)
  toffoliP66_pos                   P_66 > 0 on q > 0
  toffoliConeCoord_pos_iff         hbar > 0 <-> q > 1
  toffoliConeCoord_eq_zero_iff     hbar = 0 <-> q = 1
  toffoliFlip_eq_zero_iff          P_76 = 0 <-> q = 1
  toffoliFlip_neg_of_one_lt        P_76 < 0 on q > 1  (substrate side)
  toffoliFlip_pos_of_lt_one        P_76 > 0 on 0 < q < 1
  toffoli_antisymmetry_defect      P_67 + P_76 = q(q-1)^2(q+1)^2/(2(q^2+1))
  toffoli_not_antisymmetric        P_67 != -P_76 for q > 0, q != 1
  wStd_pos                         W_std > 0
  toffoliDiagonal_mul_wStd_pos     P_77 * W_std > 0

joining the three already proved (toffoliSextic_pos, toffoliFlipAmplitude_eq,
toffoliFlip_mul_coneCoord_nonpos). Fourteen total.

THE ANTISYMMETRY DEFECT IS EXACT, which is stronger than the "it fails" the
blocks asserted: P_67 + P_76 = q(q-1)^2(q+1)^2/(2(q^2+1)), vanishing on q > 0
only at q = 1. So "reversing the crossing negates it" is false everywhere
except the classical limit, and the size of the failure is now a closed form.

Symbolic cross-check computations/probes/toffoli_amplitude_sign_claims.py, 9/9,
exact rational arithmetic, one row per Lean theorem.

ONE LEMMA-NAME TRAP for the next agent: `div_lt_iff` does NOT resolve in this
Mathlib pin (unknown identifier). toffoliConeCoord_pos_iff is written without
it -- multiply through by q and by 1/q explicitly -- which is robust to the
rename.

REMAINING OPEN in this bean, unchanged: the index-space mismatch. G.t is a
6-vector over the Hecke NF basis; P_77/P_76 are entries of an 8x8 matrix
indexed by strand-type orderings. A correct reduction still needs a map, and
none is recorded. Tracked forward as the next tranche.

## 2026-09-08 — reopened: `status` disagreed with this bean's OWN body (§13a sweep, `qou-7sin`)

This bean was `completed` while the text above says, in its author's own words,
that the bean itself is still open. Nothing about its mathematics was judged
here and no finding was revisited — only the `status` field was made to agree
with the body.

Found by the `qou-7sin` sweep of the tracker against AGENTS.md **§13a** (owner,
2026-09-06: *"Don't close beans with open conjectures!!!"*), which landed after
most of these were closed. 18 of 2627 completed beans carry this
self-contradiction. It is decidable without judgement — the discriminator is
the bean asserting *its own* openness, not merely mentioning something open.

Re-close it when the work its body names is actually done.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Round 69 Update (PR #8249)
- Formalized in `ToffoliDimensionMismatchHeckeOffsetHypernuclearRatioNielsenThurstonAndNolenSchiffer.lean` and verified via 80-dps `mpmath` witness in PR #8249.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8249, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
