---
# qou-l64i
title: 'GAP: multiplicativity of the twisted quantum dimension, dim(X tensor Y) = dim X * dim Y'
status: completed
type: task
priority: normal
created_at: 2026-08-26T22:59:50Z
updated_at: 2026-08-30T06:35:59Z
---

Parent: qou-djk4 (PR #5866, QOU/MathlibExt/TwistedQuantumDimension.lean).

TARGET, stated and TYPE-CHECKED (the instances resolve; only the proof is missing):

    theorem qDimTwistedWith_tensor [BalancedCategory C] (X X' Y Y' : C)
        [ExactPairing X X'] [ExactPairing Y Y'] :
        @qDimTwistedWith C _ _ _ _ (X ⊗ Y) (Y' ⊗ X') (tensorExactPairing X X' Y Y')
          = qDimTwistedWith X X' ≫ qDimTwistedWith Y Y'

I expect `[BalancedCategory C]` to SUFFICE — no ribbon axiom. `twist_dual` is about duals, the
balancing axiom is about tensor, and this is a tensor statement. Do not assume ribbon is needed
without trying balanced first.

WHY IT SHOULD BE TRUE, and the consistency check I ran before spending anything on it: at θ = 𝟙
the balancing axiom reads 𝟙 = β_{X,Y} ≫ β_{Y,X}, i.e. the MONODROMY IS TRIVIAL, i.e. the category
is symmetric — and in a symmetric category the twistless dimension IS multiplicative. So the
θ = 𝟙 specialisation is consistent rather than contradictory, and the balancing axiom is doing
exactly the geometric work of undoing the crossing that the NESTED tensor closure introduces
between the X and Y strands. That nesting is visible in `tensorExactPairing`: its coevaluation
nests η_Y inside η_X, and its evaluation contracts ε_X first and ε_Y second.

WHAT IS ALREADY RULED OUT (measured, each a full compile at maxHeartbeats 1600000; all four FAIL
FAST rather than exhausting heartbeats, so these are genuine failures and not budget artifacts):

    monoidal      fails
    aesop_cat     fails
    coherence     fails
    simp [qDimTwistedWith, tensorExactPairing, ExactPairing.coevaluation,
          ExactPairing.evaluation, BalancedCategory.twist_tensor,
          braiding_tensor_left_hom, braiding_tensor_right_hom, whisker_exchange]   fails

This is the SAME profile as `tensorExactPairing`'s own two snake fields, whose docstring records
that ~35 automated placements were tried and none closed either. Expect a hand-built string-diagram
calc, not a tactic.

THE IDIOM THAT WORKS HERE (from `RigidTensorDual.tensorExactPairing`, learned the hard way — read
that proof before starting): pad every calc term with `𝟙 _ ⊗≫ … ⊗≫ 𝟙 _`, parenthesise the
interesting part as a single `⊗≫` group, and regroup until a BARE `W ◁ g ≫ f ▷ Z` appears with no
compound whiskering around it. That bare shape is what `whisker_exchange` matches; compound forms
hide it. `monoidal` can never reach it on its own, because the move required is the INTERCHANGE
LAW, not coherence.

TOOLS ALREADY IN THE TREE, built for exactly this kind of step:
- `QOU.MathlibExt.BraidedSlide` (PR #5848) — `braiding_slide_cap_right` and its inverse form slide
  a braiding past a cap. This is the tool for pushing the closure's braiding through the nested
  ε's.
- `QOU.MathlibExt.RigidTensorDual` — `tensorExactPairing`, `tensorDoubleDualIso`.
- `braiding_tensor_left_hom` / `braiding_tensor_right_hom` expand β_{X⊗Y, Z} into elementary
  braidings.

SUGGESTED DECOMPOSITION, in the order I would try it:
1. A PARTIAL-TRACE lemma: closing only the Y strand of an endo of X ⊗ Y yields an endo of X.
   Then multiplicativity is `tr = tr_X ∘ tr_Y` plus the θ bookkeeping. This is the standard
   literature route and is the one I would back, but it is real infrastructure Mathlib lacks.
2. Direct: expand β_{X⊗Y, Y'⊗X'} into its four elementary braidings, then use the double braiding
   from `twist_tensor` to cancel two of them against the nesting, leaving two independent closures.
3. Warm-up worth doing first if 1 and 2 both stall: prove the SYMMETRIC, TWISTLESS case
   (`qDimWith_tensor` under `[SymmetricCategory C]`). Strictly easier, no θ bookkeeping, and it
   tells you whether the diagram manipulation is tractable at all before committing to the general
   case.

CORPUS STATUS — DO NOT PRESENT THIS AS A NEW RESULT. The mathematical claim is ALREADY HELD by the
corpus, by citation: `computations/_deprecated/rho_k_markov_multiplicativity_probe.py` and its
witness conclude "Markov multiplicativity for disjoint p+n is a categorical consequence of
Wenzl 1988 Theorem 5, verified numerically. ρ_K^LO is therefore CATEGORICALLY DERIVED, not an
empirical ansatz." What a Lean proof adds is (a) a SECOND, INDEPENDENT route — ribbon-categorical
rather than Hecke-branching-specific — and (b) machine-checked exactness in place of "verified
numerically to machine precision", which per the AGENTS.md no-float64 directive is not an answer to
an EXACTNESS question at all. Both are worth having; neither is a discovery.

Corpus-grep run before opening this: paths 1 (audits), 2 (content), 3 (lean), 4 (computations) and
6 (beans) are clear of any categorical `dim(X⊗Y)` statement. Path 5 (library/) was NOT run — do it
before writing "open" in any durable artifact, since Turaev 1994 certainly contains this and may be
ingested.


MEASURED FOLLOW-UP, same session — MY OWN ROUTE-3 ADVICE ABOVE IS PARTLY WRONG, corrected here.

I recommended the SYMMETRIC TWISTLESS case as an easier warm-up ("strictly easier, no θ
bookkeeping"). I then ran it. It is NOT easier in the way I predicted:

    theorem qDimWith_tensor [SymmetricCategory C] (X X' Y Y' : C)
        [ExactPairing X X'] [ExactPairing Y Y'] :
        @qDimWith C _ _ _ (X ⊗ Y) (Y' ⊗ X') (tensorExactPairing X X' Y Y')
          = qDimWith X X' ≫ qDimWith Y Y'

    monoidal      fails
    aesop_cat     fails
    simp [qDimWith, tensorExactPairing, ExactPairing.coevaluation, ExactPairing.evaluation,
          SymmetricCategory.symmetry, braiding_tensor_left_hom, braiding_tensor_right_hom,
          whisker_exchange]                                                            fails

All fail fast, same profile as the twisted goal — and note this version has `SymmetricCategory`
available, so `β_{X,Y} ≫ β_{Y,X} = 𝟙` is in scope and simp still cannot get there.

WHAT THAT ACTUALLY TELLS US, and it is the useful part: THE DIFFICULTY IS THE NESTING, NOT THE
TWIST. Removing θ entirely and handing simp the symmetry axiom changes nothing. So the obstruction
is `tensorExactPairing`'s nested η/ε structure — the same interchange-law obstruction its own two
snake fields hit — and any effort spent on θ bookkeeping is spent on the wrong half of the problem.

CONSEQUENCE FOR THE ROUTE RANKING: route 3 is demoted. It is still worth doing as a SMALLER
TARGET (fewer moving parts once you are hand-building the calc), but not as a FEASIBILITY PROBE —
it has already been probed and it fails identically. Route 1 (partial trace) is now clearly the one
to back, because a partial-trace lemma attacks the nesting directly, which is where the difficulty
has now been measured to live.

FEEDBACK MECHANISM, since there is no working LSP in this container: `trace_state` inside a tactic
block prints the goal to the compiler output. That is the substitute for interactive goal
inspection — the goals are large but it is real feedback, and hand-building a diagram calc blind
without it is not realistic.

BUILD NOTE: `lean`-direct cannot `import QOU.MathlibExt.TwistedQuantumDimension` because that
module has no committed olean. To experiment against it, append the scratch to the module file
itself and restore afterwards; do NOT `lake build`, which evicts the restored olean cache
(bean qou-r13s).


2026-08-27 — ROUTE 1 STEP 1 IS DONE AND LANDED; the crux is now ISOLATED to one lemma.

Landed on PR #5866 (QOU/MathlibExt/TwistedQuantumDimension.lean, sorry-free, lean-direct exit 0):

    qTrWith (A B : C) [ExactPairing A B] (f : A ⟶ A) : (𝟙_ C ⟶ 𝟙_ C)
      := η_ A B ≫ (f ▷ B) ≫ (β_ A B).hom ≫ ε_ A B
    qTrWith_id     : qTrWith A B (𝟙 A) = qDimWith A B
    qTrWith_twist  : qTrWith A B (twist A) = qDimTwistedWith A B     (by rfl)

    ptrWith (X Y Y' : C) [ExactPairing Y Y'] (f : X ⊗ Y ⟶ X ⊗ Y) : X ⟶ X
      := 𝟙 X ⊗≫ X ◁ η_ Y Y' ⊗≫ f ▷ Y' ⊗≫ X ◁ ((β_ Y Y').hom ≫ ε_ Y Y') ⊗≫ 𝟙 X
    ptrWith_id     : ptrWith X Y Y' (𝟙 (X ⊗ Y))
                       = (ρ_ X).inv ≫ (X ◁ qDimWith Y Y') ≫ (ρ_ X).hom

`ptrWith_id` closed with `simp [ptrWith, qDimWith, monoidalComp]` FIRST TRY. `qTrWith` matters more
than it looks: without a MORPHISM-level trace there is nothing for a partial trace to be composed
INTO, so the whole route is unstatable. That is why this step came first.

THE CRUX, now a single named lemma — state it exactly like this, it elaborates cleanly:

    theorem qTrWith_tensor_eq_ptr (X X' Y Y' : C)
        [ExactPairing X X'] [ExactPairing Y Y'] (f : X ⊗ Y ⟶ X ⊗ Y) :
        @qTrWith C _ _ _ (X ⊗ Y) (Y' ⊗ X') (tensorExactPairing X X' Y Y') f
          = qTrWith X X' (ptrWith X Y Y' f) := by
      sorry

MEASURED ON IT: `simp [qTrWith, ptrWith, tensorExactPairing, ExactPairing.coevaluation,
ExactPairing.evaluation, monoidalComp]` dies on MAXIMUM RECURSION DEPTH (not a heartbeat timeout —
a different failure from the earlier probes, and raising maxRecDepth is unlikely to help since the
term is genuinely large). `monoidal` fails. NOT COMMITTED, because committing it means committing a
`sorry` and this repo does not take them.

ONCE THE CRUX LANDS, multiplicativity is short and needs no new ideas:

    qDimWith (X⊗Y) (Y'⊗X')
      = qTrWith (X⊗Y) (Y'⊗X') (𝟙)              -- qTrWith_id
      = qTrWith X X' (ptrWith X Y Y' 𝟙)         -- THE CRUX
      = qTrWith X X' ((ρ_ X).inv ≫ (X ◁ qDimWith Y Y') ≫ (ρ_ X).hom)   -- ptrWith_id
      = qDimWith X X' ≫ qDimWith Y Y'           -- scalar pull-out, End(𝟙) acting by whiskering

The last step needs a small "scalars pull out of the trace" lemma
(`qTrWith A B ((ρ).inv ≫ (A ◁ s) ≫ (ρ).hom) = qDimWith A B ≫ s` for `s : 𝟙 ⟶ 𝟙`), which should be
easy and is NOT the obstruction. The TWISTED version is the same chain with `qTrWith_twist` in
place of `qTrWith_id`, plus `twist_tensor` — so proving the crux buys BOTH.

HONEST SCOPE: this is progress on the framework, NOT on the nesting. The obstruction measured
earlier (interchange, not coherence) is untouched and now sits entirely inside
`qTrWith_tensor_eq_ptr`. Do not read step 1 landing as the route being half done — it is the easy
half, and the docstring in the file says so.


🛑 SAME-SESSION CORRECTION — P2's TRUTH IS NOT ESTABLISHED, AND THERE IS A SPECIFIC REASON TO
DOUBT IT AS STATED. Read this before attempting it.

I recorded `qTrWith_tensor_eq_ptr` above as "the crux", i.e. as a true lemma awaiting a proof. That
was an overstatement: I DEFINED `ptrWith` and then ASSERTED that the nested closure factors through
it, without checking the factorisation holds. That is the "defined residual ≠ derived
decomposition" trap in AGENTS.md, applied to a decomposition of a trace rather than of a number.
The landed lemmas are unaffected — `ptrWith_id` is proved and true, and `qTrWith` is a definition —
but the TARGET may be false.

THE COUNT THAT RAISES THE DOUBT. `β_{X⊗Y, Y'⊗X'}` is ONE braiding on the left-hand side, but it
decomposes: `braiding_tensor_left_hom` splits `β_{X⊗Y, Z}` into two elementary braidings, and each
of those with `Z = Y' ⊗ X'` splits into two more by `braiding_tensor_right_hom`. So the LHS carries
FOUR elementary braidings:

    β_{X,Y'}   β_{X,X'}   β_{Y,Y'}   β_{Y,X'}

The right-hand side carries exactly TWO: `β_{Y,Y'}` inside `ptrWith` and `β_{X,X'}` inside the
outer `qTrWith`. So the identity as stated REQUIRES the cross terms `β_{X,Y'}` and `β_{Y,X'}` — the
crossings between the X-loop and the Y-loop — to cancel each other.

WHY THAT IS SUSPICIOUS, and it is the same argument that motivated this whole bean: if those two
cancelled unconditionally, the identity would hold with NO twist anywhere, i.e. the TWISTLESS
braided dimension would be multiplicative in ANY braided category. But the reason the twisted
dimension is the right object at all is that the balancing axiom is what undoes the crossing the
nested closure introduces between the X and Y strands (recorded above). Both cannot be true. Either
the cross terms do not cancel on their own — so P2 as stated is FALSE — or they do, and my
motivating story for why the twist is needed is wrong. I have not determined which, and I am not
going to assert either.

TWO REPAIRS TO TRY, in preference order:

1. **A BRAIDED partial trace.** `ptrWith` may simply be the wrong partial trace for a braided
   category: the X strand has to be threaded past the Y-closure, so the correct definition probably
   carries the cross braidings itself. If so P2 becomes true by construction of the right object,
   and `ptrWith_id` will need re-checking against the new definition (it may still hold, since at
   `f = 𝟙` there is nothing to thread).
2. **State P2 for the TWISTED trace directly**, with `twist_tensor` available, so the double
   braiding from `θ_{X⊗Y}` is present to cancel the cross terms. This matches the motivating story
   and is the version actually needed for multiplicativity anyway.

CHEAPEST WAY TO DECIDE WHICH: specialise to a SYMMETRIC category, where `β_{X,Y'}` and `β_{Y,X'}`
compose to the identity if they are an R2 pair. If P2 holds symmetrically but not braided, repair 2
is right. If it fails even symmetrically, `ptrWith` is the wrong object and repair 1 is right.
That is one compile, and it should be the next thing anyone does on this bean.

DO NOT treat the statement recorded above as a theorem to be proved until one of these settles it.


RESOLVED (geometrically, not in Lean) — P2 AS STATED IS FALSE; REPAIR 2 IS THE RIGHT ONE.

First, a correction to the paragraph immediately above: I wrote that specialising to a symmetric
category "is one compile, and it should be the next thing anyone does". THAT IS WRONG and I should
not have written it. A tactic FAILING proves nothing — every tactic already fails on every version
of this goal. Only a proof settles true, and only a counterexample settles false. The prescription
was worthless as stated; ignore it.

Worked out from the diagram instead, which does settle it:

The braided trace `η ≫ β ≫ ε` of `𝟙_A` is the closure of the A-strand THROUGH ONE CROSSING — not
the plain Markov closure. For a single object that is an unknot with framing ±1, which is exactly
why a framing correction (the twist) belongs in the trace at all.

Now take `A = X ⊗ Y`, a 2-CABLE. The block braiding `β_{X⊗Y, Y'⊗X'}` crosses the whole cable past
the whole dual cable, so on closure it contributes the two cross terms counted above,
`β_{X,Y'}` and `β_{Y,X'}`. Those are crossings BETWEEN THE TWO COMPONENTS: after closing, the X
circle and the Y circle have LINKING NUMBER ±1. But `dim(X) · dim(Y)` is two UNLINKED circles. The
two sides therefore differ by a Hopf link's worth of linking, and no amount of rearranging inside a
braided category removes it — there is no R2 pair to cancel, the crossings have the same sign.

WHICH IS EXACTLY WHAT `twist_tensor` SUPPLIES. The balancing axiom

    θ_{X⊗Y} = β_{X,Y} ≫ β_{Y,X} ≫ (θ_X ⊗ θ_Y)

carries a DOUBLE BRAIDING — the monodromy, linking number ∓1 — whose whole job here is to unlink
the two components, leaving the per-object twists `θ_X ⊗ θ_Y` to supply the two framings. So the
twist is not bookkeeping around the identity; it IS the identity's content, and the twistless
version is false for a reason that can be named rather than merely suspected.

CONSEQUENCES:
1. Do NOT attempt `qTrWith_tensor_eq_ptr` as stated (twistless, general `f`). It is false.
2. Repair 1 (a "braided partial trace" carrying the cross braidings) is a WORSE idea than it looked:
   it would be defining the answer into the object — the same defined-residual trap that produced
   this correction in the first place. Only take it if the resulting object matches an independent
   definition in the literature.
3. GO STRAIGHT TO REPAIR 2: state the factorisation for the TWISTED trace, where `twist_tensor` is
   available to cancel the cross terms. That is the version multiplicativity needs anyway.

EPISTEMIC STATUS: this is a string-diagram argument, NOT a Lean proof and NOT a counterexample. It
is strong enough to redirect effort and to stop anyone proving a false lemma; it is not strong
enough to write "refuted" in a durable artifact per the (a)/(b) rule. Scope (a): this construction,
as stated, does not factor — the ingredient is not excluded, and indeed repair 2 uses it.

STILL TRUE AND LANDED, unaffected by any of this: `qTrWith`, `qTrWith_id`, `qTrWith_twist`,
`ptrWith`, `ptrWith_id`. `ptrWith_id` is about `f = 𝟙` on a SINGLE closure and never meets the
cross terms.


REPAIR 2, IN A BETTER FORM THAN "state it for the twisted trace". VERIFIED TO ELABORATE.

Rather than restate the factorisation with `θ` baked in, put the UNLINKING DOUBLE BRAIDING
EXPLICITLY ON THE INPUT. This isolates the geometric content — "a monodromy on the input unlinks
the cable closure" — and makes multiplicativity a corollary rather than a restatement:

    set_option maxHeartbeats 1600000 in
    theorem qTrWith_tensor_monodromy (X X' Y Y' : C)
        [ExactPairing X X'] [ExactPairing Y Y'] (g : X ⟶ X) (h : Y ⟶ Y) :
        @qTrWith C _ _ _ (X ⊗ Y) (Y' ⊗ X') (tensorExactPairing X X' Y Y')
            ((β_ X Y).hom ≫ (β_ Y X).hom ≫ (g ⊗ₘ h))
          = qTrWith X X' g ≫ qTrWith Y Y' h

MEASURED: the statement ELABORATES (checked with `sorry`; instances resolve, no metavariable or
universe trouble). `monoidal` fails on it, re-run on a clean file — see the harness note below.
Not committed: a `sorry` would be.

WHY THIS SHAPE IS THE RIGHT ONE:
- It says exactly what the diagram argument above establishes, and nothing more. The two cross
  terms `β_{X,Y'}` and `β_{Y,X'}` are a linking number; `β_{X,Y} ≫ β_{Y,X}` is the monodromy that
  cancels it. Everything else on both sides is per-object.
- It is `g`/`h`-general, so it is one lemma rather than one per application.
- MULTIPLICATIVITY IS THEN A COROLLARY, not a re-proof: take `g = θ_X`, `h = θ_Y`, and
  `BalancedCategory.twist_tensor` rewrites `θ_{X⊗Y}` into exactly the LHS's input. With
  `qTrWith_twist` (already landed, by `rfl`) both sides become the twisted dimensions and the
  original target falls out.
- It needs only `[BraidedCategory C]` — no balanced structure — so the balancing axiom is used
  ONLY in the corollary, which is where it belongs. That is the same "the axiom enters at exactly
  one step" separation as the sphericality proof in this file.

HARNESS NOTE, recorded because it cost a wrong measurement here. I probed tactics by regex-swapping
the proof line, and the pattern `simp \[qTrWith.*` also matched `simp [qTrWith, qDimWith]` inside
`qTrWith_id` — so two of the three verdicts were measured against a CORRUPTED file and were
worthless. The `monoidal` verdict above is the re-run on a restored tree. When swapping tactics by
regex in this module, anchor on a unique placeholder token, never on a tactic name that occurs in
another proof.


MONODROMY DIRECTION — a doubt I could not resolve by hand, recorded so nobody "fixes" the statement.

Setting up the proof I counted crossings, and the count does not obviously come out. Recording it
because the natural response — flip the monodromy to its inverse — would be WRONG, and the reason
is worth stating.

The count. `β_{X⊗Y, Y'⊗X'}` is four elementary crossings: (X,Y'), (X,X'), (Y,Y'), (Y,X'). Sorting
them by component — X-circle is the X and X' strands, Y-circle the Y and Y' strands:

    within X-circle:  (X,X')            -> the framing ±1, corrected by θ_X
    within Y-circle:  (Y,Y')            -> the framing ±1, corrected by θ_Y
    BETWEEN circles:  (X,Y') and (Y,X') -> two crossings, hence a linking number

That is even, as it must be, and it is the linking that makes the twistless version false. So far so
good. But `β_{X,Y} ≫ β_{Y,X}` is the FULL TWIST σ², i.e. two crossings of the SAME handedness,
adding linking ±1 rather than cancelling it — which by that reading makes the total WORSE, not zero,
and would mean the correcting factor is the INVERSE monodromy.

WHY I AM NOT ACTING ON THAT, and why the recorded statement stands:

1. **The direction is FORCED, not chosen.** `BalancedCategory.twist_tensor` gives
   `θ_{X⊗Y} = β_{X,Y} ≫ β_{Y,X} ≫ (θ_X ⊗ θ_Y)` — the FORWARD monodromy. The landed conditional
   `qDimTwistedWith_tensor_of_monodromy` consumes exactly that, so if the lemma is true at all it is
   true in the direction the statement already has. Flipping it would break the corollary and prove
   nothing about the twisted dimension.
2. **Multiplicativity in a ribbon category is classical.** If the forward monodromy really made the
   linking worse, the classical theorem would be false. Between "the textbook theorem is wrong" and
   "my crossing count has a sign error", the second is overwhelmingly more likely.
3. **I have already made exactly this error once this session.** In the step-4 work I read two
   leftover crossings as a cancelling R2 pair, and counting again WITH THE ORIENTATION REVERSAL AT
   EACH CAP showed they were same-sign (Hopf-linked). The dual strands run backwards through the
   caps, so naive handedness bookkeeping across a cap is exactly where I get it wrong.

SO: treat the recorded `qTrWith_tensor_monodromy` as correct-as-stated, and treat this paragraph as
a warning that the crossing arithmetic is subtle at the caps rather than as evidence against it. If
a serious proof attempt hits a genuine sign obstruction, resolve it by working the orientations
carefully — do NOT flip the statement to the inverse monodromy on the strength of a naive count,
mine included.

ALSO MEASURED THIS ROUND, both useful:
- `trace_state` prints this goal COMPACTLY (about ten lines, fully readable) once
  `simp only [qTrWith, tensorExactPairing, ExactPairing.coevaluation, ExactPairing.evaluation]` has
  run. Blind hand-building is NOT necessary here; get the goal first.
- Mathlib has NO compact-closed structure and NO categorical trace anywhere under
  `CategoryTheory/Monoidal/` — checked directly. So there is no shortcut to borrow, and this is
  genuinely new infrastructure rather than a re-derivation.
- `braiding_tensor_left_hom` and `braiding_tensor_right_hom` are both `@[simp]`, so the big `simp`
  that failed ALREADY had the four-way expansion available. That localises the difficulty further:
  it is not the expansion, it is the interchange regrouping afterwards.


DIRECTION DOUBT RESOLVED — AFFIRMATIVELY. The forward monodromy is right, my count was wrong, and
the proof mechanism is now identified.

Printed the goal with the block braiding expanded (`simp only [qTrWith, tensorExactPairing,
ExactPairing.coevaluation, ExactPairing.evaluation, braiding_tensor_left_hom,
braiding_tensor_right_hom, Category.assoc]` then `trace_state`). The six braidings are explicit:

    (β_ X Y).hom ≫ (β_ Y X).hom     -- the input monodromy
    X ◁ (β_ Y Y').hom               -- Y-closure, survives to the RHS
    (β_ X Y').hom ▷ Y               -- CROSS TERM
    X ◁ (β_ Y X').hom               -- CROSS TERM
    (β_ X X').hom ▷ Y               -- X-closure, survives to the RHS

WHERE MY EARLIER COUNT WENT WRONG. I assumed the monodromy crossings had to cancel the cross terms
DIRECTLY, and since both pairs are same-handed that looked impossible. They are not the same
objects, so they cannot cancel directly at all — `β_{X,Y}` is X-past-Y, the cross term is
X-past-Y'. The cancellation goes THROUGH A CAP: `β_{X,Y'}` and `β_{X,Y}` are X passing the two legs
`Y'` and `Y` of the Y-cap `ε_ Y Y' : Y' ⊗ Y ⟶ 𝟙`, and a strand passing both legs of a cap is the
R2-through-a-cap move. Symmetrically `β_{Y,X'}` pairs with `β_{Y,X}` across the X-cap. So it is two
absorptions, not two cancellations, and the parity objection evaporates.

THE MECHANISM IS A LEMMA WE ALREADY HAVE. `QOU.MathlibExt.braiding_slide_cap_right` (PR #5848) is
exactly this move:

    braiding_slide_cap_right (c : A ⊗ B ⟶ 𝟙_ C) :
      𝟙 _ ⊗≫ (β_ W A).hom ▷ B ⊗≫ A ◁ (β_ W B).hom ⊗≫ c ▷ W ⊗≫ 𝟙 W
        = 𝟙 _ ⊗≫ W ◁ c ⊗≫ 𝟙 W

Instantiate `W := X`, `A := Y'`, `B := Y`, `c := ε_ Y Y'` for the first absorption, and
`W := Y`, `A := X'`, `B := X`, `c := ε_ X X'` for the second. It was proved for precisely this kind
of step and has been sitting unused since #5848.

CONFIDENCE, stated honestly: the OBJECT-MATCHING is verified — the lemma's shape and the goal's
braidings line up on `W, A, B, c` as above. What is NOT yet verified is the ORDERING: the goal
presents the monodromy BEFORE the cross terms (`β_{X,Y}` … then `β_{X,Y'}`), whereas the lemma wants
W-past-A before W-past-B, i.e. `β_{X,Y'}` first. Those two act on disjoint strands so interchange
should reorder them, but I have not executed that. So: the mechanism is IDENTIFIED, the proof is not
DONE, and the remaining work is the regrouping — which is the same interchange obstruction measured
all along, now with a named target to regroup TOWARD instead of an open search.

NEXT CONCRETE STEP for whoever picks this up: regroup the goal (pad with `𝟙 _ ⊗≫ … ⊗≫ 𝟙 _`, per the
`tensorExactPairing` idiom) until the bare `(β_ W A).hom ▷ B ≫ A ◁ (β_ W B).hom ≫ c ▷ W` pattern is
visible, then `rw [braiding_slide_cap_right]` twice. Use `trace_state` between steps — the goal
prints compactly.


TACTIC LEDGER — SEVEN approaches now ruled out on `qTrWith_tensor_monodromy`. Do not re-run these.

Earlier rounds:  monoidal;  aesop_cat;  coherence;  a loaded `simp` with the braiding_tensor
expansions, tensorHom_def and whisker_exchange.

This round (each a full compile at maxHeartbeats 1600000, all FAIL FAST — none is a budget artifact):

    simp [qTrWith, tensorExactPairing, ExactPairing.coevaluation, ExactPairing.evaluation,
          braiding_naturality_right, braiding_naturality_left, whisker_exchange, monoidalComp]
    simp only [qTrWith, tensorExactPairing, …] ; rw [braiding_slide_cap_right]
    simp [qTrWith, tensorExactPairing, …, monoidalComp] ; coherence

The second is the informative one. `braiding_slide_cap_right` IS the right mechanism (established
last round) but it does NOT fire as a rewrite, and the reason is structural rather than incidental:
its statement is phrased with `⊗≫`, so its LHS carries baked-in coherence isomorphisms that no
un-regrouped goal will match syntactically. It has to be reached by CONSTRUCTING the matching term
in a `calc`, exactly as `tensorExactPairing`'s own snake fields do — not by `rw` or `simp`.

CONCLUSION, and this closes out what can be learned without doing the proof: this is a hand-built
string-diagram `calc` of the `tensorExactPairing` kind, and nothing shorter will reach it. Everything
needed is now recorded — the true statement, the verified direction, the mechanism, the
instantiations of `W/A/B/c`, the goal-printing recipe, and seven dead ends. The next agent should
budget a real session for the calc rather than another round of tactic probing.

STOPPING HERE deliberately. Further hourly check-in windows on this bean would produce more negative
tactic results, which is thin value against a target that is now fully characterised.


2026-08-27 — A SECOND, SYNTACTICALLY CHECKABLE REASON THE ptrWith FACTORISATION WAS FALSE.

Worth recording because it is cheaper to check than the linking argument and it rules out the wrong
shape by READING A DEFINITION rather than by reasoning about diagrams.

`tensorExactPairing` nests the two pairs in OPPOSITE orders at the two ends:

    coevaluation' := η_ X X' ⊗≫ X ◁ η_ Y Y' ▷ X'      -- η_X OUTER, η_Y INNER
    evaluation'   := Y' ◁ ε_ X X' ▷ Y ⊗≫ ε_ Y Y'      -- ε_X INNER, ε_Y OUTER

So X is the OUTER cup but the INNER cap, and Y is the INNER cup but the OUTER cap. A factorisation
`qTrWith (X⊗Y) … f = qTrWith X X' (ptr_Y f)` needs X to be outer at BOTH ends — it is not. Nor is
the opposite order available, because Y is likewise mismatched. So NEITHER nesting order can support
a clean trace-of-partial-trace, and this is visible directly in the definition without any crossing
count.

This is INDEPENDENT of, and complementary to, the linking argument recorded earlier: linking says
the twistless version is false, and this says the ptrWith SHAPE is wrong regardless of twisting. Both
point at the same conclusion; this one is checkable in ten seconds.

ALSO MEASURED THIS ROUND:
- `braiding_slide_cap_right` is NOT IMPORTED by TwistedQuantumDimension.lean. Whoever takes this up
  must add `import QOU.MathlibExt.BraidedSlide` first — I did not add it, since an unused import is
  churn, but the missing import will otherwise read as "unknown identifier" and look like the lemma
  does not exist.
- With the import in place, `simp` including `braiding_slide_cap_right` (and its `_inv` companion)
  STILL fails, confirming the earlier structural finding from the other direction: a `⊗≫`-phrased
  lemma cannot fire as a rewrite at all, so no amount of adding it to a simp set will help. It has to
  be reached by CONSTRUCTING its LHS in a calc.
- Neither `rw [braiding_naturality_right]` nor its reverse fires on the normalised goal — the
  associators sit between, so the bare pattern is absent. That is the interchange obstruction again,
  now confirmed at the level of a single rewrite.

TACTIC LEDGER NOW AT NINE ruled-out approaches. The search is closed; the remaining work is the
hand-constructed calc, and everything needed to start it is recorded above.


2026-08-27 — SUBSTANTIAL PROGRESS. A WORKING REWRITE PREFIX, AND BOTH SLIDES IDENTIFIED WITH
MATCHING ORDER. This supersedes "nothing fires" — two rewrites DO fire, and the goal is now fully
exposed.

THE PREFIX THAT WORKS (verified, reaches a readable goal):

    simp only [qTrWith, tensorExactPairing, ExactPairing.coevaluation, ExactPairing.evaluation,
      monoidalComp, Category.assoc, Category.id_comp, Category.comp_id]
    rw [braiding_naturality_left_assoc, braiding_tensor_left_hom]
    simp only [braiding_tensor_right_hom, Category.assoc]

`braiding_naturality_left_assoc` is the one I had missed: `m ▷ (Y'⊗X') ≫ β_{X⊗Y,Y'⊗X'}` matches it
exactly, and it moves the MONODROMY across the block braiding to sit just before the caps. That is
what makes everything else line up.

AFTER THE PREFIX, all six braidings are explicit and IN THIS ORDER:

    β_{Y,Y'}   -- keeper: the Y-loop framing, appears on the RHS
    β_{Y,X'}   -- CROSS
    β_{X,Y'}   -- CROSS
    β_{X,X'}   -- keeper: the X-loop framing, appears on the RHS
    β_{X,Y} ≫ β_{Y,X}   -- the monodromy, now adjacent to the caps
    then  Y' ◁ ε_X ▷ Y  then  ε_Y

BOTH SLIDES ARE INSTANTIATED, AND THE ORDER IS ALREADY RIGHT — this is the key finding:

  slide 1:  W = Y, A = X', B = X, c = ε_X
            needs  Y-past-X'  then  Y-past-X  then  ε_X
            has    β_{Y,X'}   then  β_{Y,X} (2nd monodromy factor)  then  ε_X     ✓ ORDER MATCHES

  slide 2:  W = X, A = Y', B = Y, c = ε_Y
            needs  X-past-Y'  then  X-past-Y  then  ε_Y
            has    β_{X,Y'}   then  β_{X,Y} (1st monodromy factor)  then  ε_Y     ✓ ORDER MATCHES

So the monodromy's TWO factors serve the TWO slides, one each — `β_{Y,X}` feeds the X-cap slide and
`β_{X,Y}` feeds the Y-cap slide. That is why the forward monodromy is the right one and why there
are exactly two of them: one per cap. The earlier "linking number" story was the right intuition;
this is the mechanism at the level of the actual term.

WHAT REMAINS is purely the INTERCHANGE REGROUPING: the terms of each slide are separated by
morphisms acting on disjoint strands (`β_{X,Y'}`, `β_{X,X'}` sit between `β_{Y,X'}` and the
monodromy), so `whisker_exchange` must commute them into adjacency before either slide can fire.
That is the same obstruction measured all along, but it is now a FINITE, NAMED list of commutations
toward a KNOWN target rather than an open search.

MECHANISM NOTE for the implementer: `braiding_slide_cap_right` cannot be `rw`-applied (⊗≫ form, per
the earlier finding). Its CONTENT is `braiding_naturality_right W c` at the cap, plus
`← braiding_tensor_right_hom` to recombine `β_{W,A}` and `β_{W,B}` into `β_{W,A⊗B}`. Recombining is
the step to aim the regrouping at.

STILL NOT PROVED. Tactic finishers from the exposed state (`monoidal`, two loaded `simp`s) all still
fail — twelve approaches ruled out now. But the remaining work is construction, not search.


CORRECTION TO THE PLAN ABOVE — THE TWO SLIDES INTERLEAVE, so "both orders already match" is true but
NOT sufficient. Traced the object positions by hand; recording before the plan misleads someone.

Position trace, starting from `(X ⊗ Y) ⊗ (Y' ⊗ X')` i.e. order  X, Y, Y', X':

    β_{Y,Y'}   ->  X, Y', Y, X'     (Y-loop framing, keeper)
    β_{Y,X'}   ->  X, Y', X', Y     (cross, slide 1)
    β_{X,Y'}   ->  Y', X, X', Y     (cross, slide 2)
    β_{X,X'}   ->  Y', X', X, Y     (X-loop framing, keeper)
    β_{X,Y}    ->  Y', X', Y, X     (monodromy 1st, slide 2)
    β_{Y,X}    ->  Y', X', X, Y     (monodromy 2nd, slide 1)
    ε_X contracts X'(2) with X(3);  ε_Y contracts Y'(1) with Y(4)

So the assignment is confirmed — slide 1 consumes {β_{Y,X'}, β_{Y,X}}, slide 2 consumes
{β_{X,Y'}, β_{X,Y}}, one monodromy factor each. THE PROBLEM IS WHAT SITS BETWEEN:

  * between slide 1's two factors sit β_{X,Y'}, β_{X,X'} AND β_{X,Y} — and β_{X,Y} TOUCHES Y,
    so it cannot be commuted away by `whisker_exchange` (which needs disjoint strands).
  * between slide 2's two factors sit β_{X,X'} — which TOUCHES X, likewise not disjoint from
    slide 2's W = X.

So NEITHER slide can be brought to adjacency by interchange alone while the other is still in place.
They are mutually blocking, and the resolution has to be either (i) an order of application where
firing one first clears the other's obstruction — note firing slide 2 removes β_{X,Y}, which is
exactly slide 1's blocker, so SLIDE 2 FIRST is the candidate — or (ii) a braid relation
(hexagon/Yang-Baxter) to reorder crossings that share a strand, which interchange cannot do.

RECOMMENDED NEXT STEP, concretely: try SLIDE 2 FIRST (W = X, A = Y', B = Y, c = ε_Y). Its only
in-between term is β_{X,X'}. That is still not disjoint from X, so it likely needs Yang-Baxter
rather than whisker_exchange — check whether Mathlib's `hexagon_forward` / `hexagon_reverse` (or
`braiding_naturality` on the braiding itself) reorders β_{X,X'} past β_{X,Y}. If it does, slide 2
fires, β_{X,Y} disappears, and slide 1's path is then clear of Y-touching obstructions.

THIS IS THE FIRST TIME THE OBSTRUCTION HAS A NAME BEYOND "interchange": it is that two of the six
crossings share a strand with the terms that must move past them, so `whisker_exchange` is
provably insufficient and a BRAID RELATION is required. Every earlier round, mine included,
assumed interchange would be enough. It is not.

Tactic ledger now FIFTEEN ruled out (added: simp[whisker_exchange], aesop_cat, simp[←whisker_exchange]
+ monoidal, all from the exposed state).


YANG-BAXTER IS AVAILABLE AND STILL DOES NOT CLOSE IT — measured, so the next attempt does not need
to go looking for the tool.

`CategoryTheory.yang_baxter` exists in this Mathlib (Braided/Basic.lean:155), along with
`yang_baxter'`, `yang_baxter_iso`, and the `hexagon_forward/reverse` family with their `_iso` and
`_inv` variants. So the braid relation the previous entry says is REQUIRED is present.

    simp [hexagon_forward, hexagon_reverse, whisker_exchange, monoidalComp]   fails
    simp [yang_baxter, whisker_exchange, monoidalComp]                       fails

Both from the exposed state. These are genuine proof failures, not unknown-identifier errors — I
checked. Seventeen approaches ruled out in total.

WHAT THIS MEANS FOR THE NEXT ATTEMPT: every ingredient is now present and named — the working
prefix, the two slide instantiations with their assignment, the mutual-blocking diagnosis, and the
braid relation that the diagnosis says is needed. What is missing is the HAND APPLICATION: aiming
`yang_baxter` at the specific crossing pair that blocks slide 2 (β_{X,X'} against β_{X,Y}), which a
simp set will not do because it has no reason to prefer that direction. This is a targeted `rw` at a
located subterm, i.e. `slice_lhs`/`conv` work, not a tactic search.

SESSION SUMMARY (2026-08-27, dedicated session at the author's request): moved this bean from "no
tactic fires, mechanism unknown" to "prefix verified, mechanism identified, obstruction named and
diagnosed, required tool confirmed present". Still NOT PROVED, and no `sorry` committed.


🛑 CORRECTION — MY SLIDE-2 INSTANTIATION WAS WRONG. It is a CUP slide, not a cap slide.

I published "slide 2: W = X, A = Y', B = Y, c = ε_Y" in this bean and in PR #5879. It is wrong, and
the reason is simple enough that it should have been caught before publishing: **X does not survive
to ε_Y.** Read the position trace above — `Y' ◁ ε_X ▷ Y` contracts X'(2) with X(3), so the X strand
is CONSUMED BY ε_X. `braiding_slide_cap_right` requires W to survive past the cap (its conclusion is
`W ◁ c`), so X cannot slide across ε_Y. There is no such move.

WHAT ACTUALLY HANDLES β_{X,Y'} AND β_{X,Y}: the Y-**CUP**, not the Y-cap. Y and Y' are the two legs
of `η_Y : 𝟙 ⟶ Y ⊗ Y'`, and X crosses both, so this is a strand sliding across a CUP — the mirror
move. `QOU.MathlibExt.braiding_slide_cup_right` already exists in BraidedSlide.lean (I wrote it in
#5848 and had forgotten it; the file has FOUR slide lemmas — cap right/left, cup right/left — plus
the cap inverse form):

    braiding_slide_cup_right (u : 𝟙_ C ⟶ A ⊗ B) :
      u ▷ W = W ◁ u ≫ (β_ W A).hom ▷ B ≫ A ◁ (β_ W B).hom          (⊗≫-padded)

CORRECTED PLAN:

    slide 1  CAP  — W = Y, A = X', B = X, c = ε_X   consumes β_{Y,X'}, β_{Y,X}
                    order in the goal MATCHES the lemma                              ✓
    slide 2  CUP  — W = X, A = Y,  B = Y', u = η_Y  consumes β_{X,Y},  β_{X,Y'}
                    order in the goal is REVERSED: the goal has β_{X,Y'} (from the
                    block braiding) BEFORE β_{X,Y} (monodromy), the lemma wants
                    X-past-A=Y first                                                 ✗

AND THAT REVERSAL INDEPENDENTLY CONFIRMS THE BRAID-RELATION FINDING. β_{X,Y'} and β_{X,Y} both
involve X, so they are NOT disjoint and `whisker_exchange` cannot swap them — only Yang-Baxter can.
So the previous entry's conclusion ("a braid relation is required, interchange is provably
insufficient") stands, and now it is pinned to a specific swap: reorder β_{X,Y'} past β_{X,Y} so the
cup slide can fire.

Handedness note, checked: our braidings are `β_{X,·}` (X on the left), which matches the `_right`
family; `braiding_slide_cup_left` is the wrong handedness here.

LESSON, recorded because it is the second time this session: I asserted a slide instantiation from
the SHAPE of the crossings without checking WHICH CAP CONSUMES THE STRAND. Both times the fix came
from tracing object positions through the composite. Trace positions first; the crossing pattern
alone does not determine which absorption applies.


SYMMETRIC TWISTLESS CASE ALSO FAILS BY TACTIC — the smaller target is not a shortcut either.

Tried `qDimWith_tensor_symm` — the `[SymmetricCategory C]` twistless case, where the monodromy is
the identity and the two cross terms β_{Y,X'}, β_{X,Y'} should form an R2 pair that
`SymmetricCategory.symmetry` kills. With the working prefix in front:

    simp [SymmetricCategory.symmetry, whisker_exchange, monoidalComp]                    fails
    simp [SymmetricCategory.symmetry, braiding_slide_cup_right, braiding_slide_cap_right,
          monoidalComp]                                                                  fails

NINETEEN approaches ruled out. The symmetric case is genuinely smaller and genuinely true, and it
still needs the same hand construction — so it remains worth doing FIRST as a warm-up (fewer moving
parts once someone is hand-building), but it is NOT a feasibility shortcut and should not be
attempted as one. That is the second time this bean has recorded "the smaller case is not easier";
the first was the earlier symmetric probe, before the prefix existed.

FINAL STATE OF THIS TRANCHE (two dedicated sessions). Everything below is verified:

  KNOWN     the statement, and that it type-checks
  KNOWN     the direction (forward monodromy), forced by twist_tensor and no longer doubted
  KNOWN     the working rewrite prefix (three lines, reaches a compact readable goal)
  KNOWN     the mechanism: ONE CAP SLIDE + ONE CUP SLIDE, not two cap slides
              slide 1  CAP  W=Y, A=X', B=X, c=ε_X   order MATCHES
              slide 2  CUP  W=X, A=Y,  B=Y', u=η_Y  order REVERSED, needs Yang-Baxter
  KNOWN     both slide lemmas already exist (BraidedSlide.lean, four of them)
  KNOWN     yang_baxter exists in this Mathlib and is the required tool
  KNOWN     19 tactic approaches that do not work, including on the symmetric sub-case
  OPEN      the construction itself: a conv/slice_lhs surgery to reorder β_{X,Y'} past β_{X,Y}
            so the cup slide fires, then the cap slide

WHAT I WOULD TELL THE NEXT AGENT: stop probing tactics — that is exhausted. Open the goal with the
prefix, print it with `trace_state`, and do `conv`-level surgery aimed at the two named slides. The
single decisive question is whether `yang_baxter` can be aimed at the β_{X,Y'}/β_{X,Y} pair in
context; if it can, both slides fire and the rest is coherence.


2026-08-30 — `comp_whiskerRight` CHANGES THE STATE MATERIALLY, and my "order is reversed" finding
was an ARTIFACT of not distributing it.

Adding `MonoidalCategory.comp_whiskerRight` to the prefix's simp set distributes
`(β_{X,Y} ≫ β_{Y,X} ≫ (g ⊗ₘ h)) ▷ (Y'⊗X')` into three separate whiskerings. The monodromy then
sits at the FRONT, adjacent to the cups, and only `(g ⊗ₘ h)` gets carried across by
`braiding_naturality_left_assoc`. Revised prefix:

    simp only [qTrWith, tensorExactPairing, ExactPairing.coevaluation, ExactPairing.evaluation,
      monoidalComp, Category.assoc, Category.id_comp, Category.comp_id,
      MonoidalCategory.comp_whiskerRight]
    rw [braiding_naturality_left_assoc, braiding_tensor_left_hom]
    simp only [Category.assoc, MonoidalCategory.comp_whiskerRight]

Resulting order:  β_{X,Y} ▷(Y'⊗X') ; β_{Y,X} ▷(Y'⊗X') ; X ◁ β_{Y,Y'⊗X'} ; β_{X,Y'⊗X'} ▷ Y ;
(Y'⊗X') ◁ (g⊗ₘh) ; caps.

SO THE EARLIER "cup slide order is REVERSED" ENTRY IS WITHDRAWN. It was measured on a goal where
the monodromy had not been distributed. With distribution, β_{X,Y} comes BEFORE β_{X,Y'}, which is
the order `braiding_slide_cup_right` wants.

THE MECHANISM, now coherent — the cup slide DETACHES the Y-loop:

    braiding_slide_cup_right (W = X, A = Y, B = Y', u = η_Y) read right-to-left:
        X ◁ η_Y ≫ β_{X,Y} ▷ Y' ≫ Y ◁ β_{X,Y'}  =  η_Y ▷ X

The goal opens with `X ◁ η_Y ▷ X'` and has `β_{X,Y}` immediately after. If `β_{X,Y'}` can be
brought up to follow it, the three collapse to `η_Y ▷ X` — the Y-cup moves to the LEFT of X, i.e.
the Y-loop DETACHES from the X strand. That detachment is what the whole theorem is about, and it
is now a single named move rather than a vague "absorb the cross terms".

WHAT BLOCKS IT, per-crossing (this is the finite list the earlier entry promised):
`β_{X,Y'}` must move up past three crossings —

    past β_{Y,X'}   objects {Y,X'} vs {X,Y'}   DISJOINT      -> whisker_exchange      ✓
    past β_{Y,Y'}   share Y'                   NOT disjoint  -> Yang-Baxter           ✗
    past β_{Y,X}    share X                    NOT disjoint  -> Yang-Baxter           ✗

So TWO Yang-Baxter applications, both named, plus one interchange. The cap slide (Y across ε_X) then
handles what remains.

STILL NOT PROVED. Finishers retried from the improved state — `monoidal`, `simp` with both slide
lemmas, `simp` with `braiding_tensor_right_hom`+`whisker_exchange` — all fail. TWENTY-TWO approaches
ruled out.

BOOKKEEPING WARNING FOR THE NEXT AGENT, and for me: this is the THIRD time in this bean that a
crossing-pairing claim of mine turned out to be wrong (first the linking-number direction, then the
cap-vs-cup mix-up, now the order-reversal artifact). Each time the error came from reasoning about
the diagram instead of reading the printed goal. PRINT THE GOAL AFTER EVERY SIMP-SET CHANGE — the
simp set materially changes which crossings are adjacent, and conclusions drawn under one set do not
survive to another.


2026-08-30 — MAJOR REDUCTION: SIX BRAIDINGS TO TWO. Verified, reproducible, and it makes the earlier
"two Yang-Baxter applications needed" plan obsolete — NO Yang-Baxter was used.

The whole reduction is `braiding_naturality` plus one recombination helper. The key was stating the
helper in REASSOC form: after `Category.assoc` the goal is right-nested, so a plain `rw` pattern ends
mid-chain and never matches. Every earlier failure of this kind was that, not a mathematical
obstruction.

THE HELPER (proves by `rw [braiding_tensor_right_hom]; simp`):

    have hrec : ∀ (W A B Z : C) (k : A ⊗ (B ⊗ W) ⟶ Z),
        (α_ W A B).hom ≫ (β_ W (A ⊗ B)).hom ≫ (α_ A B W).hom ≫ k
          = (β_ W A).hom ▷ B ≫ (α_ A W B).hom ≫ A ◁ (β_ W B).hom ≫ k := by
      intro W A B Z k; rw [braiding_tensor_right_hom]; simp

THE FULL VERIFIED PREFIX (each step confirmed to fire, goal printed after each):

    simp only [qTrWith, tensorExactPairing, ExactPairing.coevaluation, ExactPairing.evaluation,
      monoidalComp, Category.assoc, Category.id_comp, Category.comp_id,
      MonoidalCategory.comp_whiskerRight]
    rw [braiding_naturality_left_assoc, braiding_tensor_left_hom]
    simp only [Category.assoc, MonoidalCategory.comp_whiskerRight]
    rw [← hrec Y X (Y' ⊗ X')]                                  -- recombines Y's whole journey
    simp only [Iso.hom_inv_id_assoc, Category.assoc]            -- kills an α.hom ≫ α.inv pair
    rw [← braiding_naturality_right_assoc, ← hrec X Y (Y' ⊗ X')] -- recombines X's whole journey

RESULTING GOAL — two braidings, down from six:

    η_X ≫ coh ≫ X ◁ η_Y ▷ X' ≫ coh
      ≫ (α_ X Y (Y'⊗X')).hom ≫ β_{X, Y⊗Y'⊗X'}
      ≫ (α_ Y (Y'⊗X') X).hom ≫ β_{Y, (Y'⊗X')⊗X}
      ≫ (α_ (Y'⊗X') X Y).hom ≫ (Y'⊗X') ◁ (g ⊗ₘ h)
      ≫ coh ≫ Y' ◁ ε_X ▷ Y ≫ coh ≫ ε_Y

Each strand's ENTIRE journey is now ONE braiding: X past (Y,Y',X'), then Y past (Y',X',X).

WHAT THIS SUPERSEDES. The "two Yang-Baxter applications" plan is withdrawn — not wrong exactly, but
unnecessary: recombining each strand's journey into a single braiding avoids the crossing-reordering
problem entirely rather than solving it. That is the fourth time in this bean a crossing-level plan
of mine was superseded by simply reading the printed goal after a rewrite. The standing warning
stands and is now well-earned.

WHAT REMAINS — the detachment. `X ◁ η_Y ▷ X'` followed by `β_{X, Y⊗Y'⊗X'}` should collapse by
`braiding_naturality_right X (η_Y ▷ X')`, moving the Y-cup to the LEFT of X and leaving `β_{X,X'}` —
which is exactly the X-loop framing crossing the RHS wants. Blocker is a GROUPING mismatch, not a
mathematical one: the goal has `β_{X, Y⊗(Y'⊗X')}` while the naturality needs `β_{X, (Y⊗Y')⊗X'}`.
`rw [braiding_naturality_right_assoc]` and `rw [← hrec X (Y⊗Y') X']` both fail to match for that
reason alone. Next step is a calc step (or a grouping-aware helper) bridging the two associativities,
which `monoidal` should discharge.

Finishers retried on the two-braiding goal — `monoidal`, two loaded `simp`s — still fail. TWENTY-FIVE
approaches ruled out, but the shape of the remaining work has changed completely: it is now ONE
grouping bridge plus the detachment, not a braid-relation search.


GROUPING BRIDGE ALSO FIRES — verified. Braidings are natural in the ASSOCIATOR itself, which is what
converts between the two groupings:

    have hgrp : ∀ (Z : C) (k : (Y ⊗ Y' ⊗ X') ⊗ X ⟶ Z),
        (β_ X (Y ⊗ Y' ⊗ X')).hom ≫ k
          = X ◁ (α_ Y Y' X').inv ≫ (β_ X ((Y ⊗ Y') ⊗ X')).hom ≫ (α_ Y Y' X').hom ▷ X ≫ k := by
      intro Z k
      rw [← braiding_naturality_right_assoc]
      simp

    rw [hgrp]

After it the braiding is `β_{X, (Y⊗Y')⊗X'}` — the grouping `braiding_naturality_right X (η_Y ▷ X')`
needs for the cup detachment. So the blocker named in the previous entry is CLEARED.

WHAT STILL BLOCKS THE DETACHMENT, and it is now the last thing: the cup `X ◁ η_Y ▷ X'` and the
braiding are separated by coherence — `⊗𝟙.hom ≫ (α_ X Y (Y'⊗X')).hom ≫ X ◁ (α_ Y Y' X').inv`.
`braiding_naturality_right` wants `X ◁ f ≫ β_{X,·}` ADJACENT. Tried and failed:
`simp only [← MonoidalCategory.whiskerLeft_comp, Category.assoc]` then
`rw [braiding_naturality_right_assoc]`; and `monoidal` on the whole thing. TWENTY-SEVEN ruled out.

The remaining task is therefore narrow and purely coherence: merge the two `X ◁ (…)` factors and
absorb the `⊗𝟙.hom` between them so the naturality pattern is adjacent, then one
`braiding_naturality_right` detaches the Y-cup and leaves `β_{X,X'}` — the X-loop framing crossing
the RHS wants. After that only the Y side remains, by the same method.

STATE OF THE PROOF: six braidings reduced to two, groupings reconciled, one coherence merge away from
the detachment. No Yang-Baxter, no slide lemma, no `sorry`. Every step above is verified to fire and
the goal was printed after each.


END OF 2026-08-30 SESSION — where the coherence merge stands.

After `hgrp` the braiding is `β_{X, (Y⊗Y')⊗X'}`, flanked by `X ◁ (α_ Y Y' X').inv` before and
`(α_ Y Y' X').hom ▷ X` after. Attempts to go further, all failing:

    rw [hrec X (Y ⊗ Y') X']                     -- forward split; hrec's LHS needs ITS OWN
                                                   associators around the braiding, and the ones
                                                   hgrp leaves are different ones
    aesop_cat
    simp [braiding_tensor_right_hom_assoc, braiding_naturality_right_assoc, monoidalComp,
          Category.assoc]
    simp [monoidalComp, braiding_naturality_right, braiding_naturality_left, Category.assoc]
    rw [braiding_naturality_right_assoc X ((λ_ X').inv ≫ η_ Y Y' ▷ X')]
    simp only [← MonoidalCategory.whiskerLeft_comp, Category.assoc]
      then rw [braiding_naturality_right_assoc]

THIRTY approaches ruled out.

A TENSION WORTH RECORDING, because it may be the real reason this last step resists. Recombining
each strand's journey into ONE braiding is what produced the 6→2 reduction — but
`braiding_slide_cup_right`, the lemma that performs the detachment, is stated with the braidings
SPLIT (`(β_ W A).hom ▷ B ⊗≫ A ◁ (β_ W B).hom`). So the reduction and the detachment want opposite
normal forms. Either the detachment must be restated for a recombined `β_{W, A⊗B}` — which is just
`braiding_naturality_right W u` at the cup, no slide lemma needed — or the recombination has to be
undone locally at the cup. The first is much the better bet and is what the failed attempts above
were reaching for; what defeats them is only that the cup and the braiding are not ADJACENT.

CONCRETE NEXT STEP: build a `calc` step whose right-hand side states the prefix as
`η_X ≫ X ◁ ((λ_ X').inv ≫ η_ Y Y' ▷ X') ≫ β_{X, (Y⊗Y')⊗X'} ≫ …` and discharge that step with
`monoidal`. `monoidal` handles composites containing arbitrary morphisms via `⊗≫`, so it should
absorb the `⊗𝟙.hom` and the two associators around `η_Y`. Every `rw`-based route tried so far fails
for the same syntactic-adjacency reason, so stop trying `rw` and write the term.


ALL THREE LEMMAS THE PROOF NEEDS ARE NOW VERIFIED. Only adjacency remains.

    hrec  (recombination, REASSOC form)  — proves by `rw [braiding_tensor_right_hom]; simp`
    hgrp  (grouping bridge)              — proves by `rw [← braiding_naturality_right_assoc]; simp`
    hdet  (the detachment)               — proves by `braiding_naturality_right X _`  ← VERIFIED

`hdet` in full, confirmed to typecheck and prove:

    have hdet : X ◁ ((λ_ X').inv ≫ η_ Y Y' ▷ X') ≫ (β_ X ((Y ⊗ Y') ⊗ X')).hom
        = (β_ X X').hom ≫ ((λ_ X').inv ≫ η_ Y Y' ▷ X') ▷ X :=
      braiding_naturality_right X _

It moves the Y-cup to the LEFT of X and leaves `β_{X,X'}` — precisely the X-loop framing crossing
the right-hand side wants. This is the detachment, and it is a one-liner.

SO THE MATHEMATICAL CONTENT IS COMPLETE. What is left is purely making `hdet` APPLICABLE: the goal
holds `X ◁ η_Y ▷ X'` and `β_{X, (Y⊗Y')⊗X'}` separated by `⊗𝟙.hom` and two associators, and both
`rw` and `simp` need them syntactically adjacent.

THE FIX TO TRY NEXT, and why the current route fights it: the prefix does
`simp only [..., monoidalComp, ...]`, which UNFOLDS `⊗≫` into raw coherence isos — and raw
coherence isos are exactly what cannot be absorbed. The `tensorExactPairing` idiom does the
opposite: it KEEPS `⊗≫` and pads every calc term with `𝟙 _ ⊗≫ … ⊗≫ 𝟙 _`, because `monoidal`
absorbs `⊗≫` but not unfolded coherence. So drop `monoidalComp` from the prefix's simp set and
state the intermediate in `⊗≫` form; `monoidal` should then bridge the cup to the braiding and
`hdet` fires.

HARNESS TRAP, cost one wasted run: `/tmp/tqd.base` had been rebuilt from the WORKING TREE while a
scratch copy of the theorem was still in it, so the next run failed with
"`qTrWith_tensor_monodromy` has already been declared" — which reads like a Lean problem and is not.
Rebuild the scratch base from `git show HEAD:<path>`, never from the working tree, and assert the
theorem name is absent.


🛑 MY OWN HARNESS HYPOTHESIS IS FALSIFIED. Recorded because I stated it as the likely fix.

I predicted that unfolding `monoidalComp` in the prefix was what prevented the slide lemmas and
`monoidal` from bridging the cup to the braiding — reasoning that `⊗≫` is absorbable and raw
coherence isos are not, so KEEPING `⊗≫` should let them fire. Tested directly.

Prefix without `monoidalComp` (the `⊗≫` survives, and the goal IS much cleaner):

    simp only [qTrWith, tensorExactPairing, ExactPairing.coevaluation, ExactPairing.evaluation,
      Category.assoc, Category.id_comp, Category.comp_id, MonoidalCategory.comp_whiskerRight]

    ⊢ (η_X ⊗≫ X ◁ η_Y ▷ X' ⊗≫ 𝟙) ≫ β_{X,Y} ▷ (Y'⊗X') ≫ β_{Y,X} ▷ (Y'⊗X')
        ≫ (g⊗ₘh) ▷ (Y'⊗X') ≫ β_{X⊗Y, Y'⊗X'} ≫ 𝟙 ⊗≫ Y' ◁ ε_X ▷ Y ⊗≫ ε_Y

From that state, ALL of these still fail:

    simp [braiding_slide_cup_right, braiding_slide_cap_right, braiding_slide_cap_right_inv,
          monoidalComp]
    rw [braiding_slide_cup_right]
    monoidal

So the `⊗≫`-vs-unfolded distinction is NOT the blocker. THIRTY-THREE approaches ruled out. The
slide lemmas do not match this goal even in their own native notation, which means the earlier
inference "a ⊗≫-phrased lemma cannot fire as a rewrite" was RIGHT about the mechanism but the
proposed remedy (keep ⊗≫) does not follow from it — matching needs the surrounding term to be
literally the lemma's LHS, and padding alone does not produce that.

WHAT THIS LEAVES. The three lemmas (hrec, hgrp, hdet) are all verified and the mathematics is
complete; what is unsolved is purely getting Lean to see the pattern. Every remedy tried has been a
variation on "make the rewrite fire". The remaining honest option is the one never actually
attempted: write the full `calc` with each intermediate term SPELLED OUT, discharging each step with
`monoidal`, rather than trying to steer the goal into a lemma's shape. That is what
`tensorExactPairing`'s own snake proofs do, and it is laborious precisely because the terms must be
written by hand.

SIXTH superseded plan of mine on this bean. The pattern is now unmistakable and worth stating
plainly for whoever picks this up: my predictions about WHICH REWRITE WILL FIRE have been wrong
essentially every time, while my measurements of what DID fire have all held. Trust the printed goal;
do not trust a plan — including this entry's.


## CLOSED 2026-08-30 — `qTrWith_tensor_monodromy` proved, sorry-free

Commit `85f590a1a8` on `claude/qtr-tensor-monodromy-2026-08-27`. The lemma is
proved unconditionally (braided + two exact pairings; no rigidity, no balancing),
and `qDimTwistedWith_tensor_of_monodromy` is now discharged into the
unconditional `qDimTwistedWith_tensor` — multiplicativity of the twisted quantum
dimension over `tensorExactPairing`.

**The blocker was a prime, not the mathematics.** `η_` / `ε_` notation
elaborates to `ExactPairing.coevaluation` / `.evaluation`; the goal, after
`simp only [ExactPairing.coevaluation, ExactPairing.evaluation]`, is in the
**primed** `coevaluation'` form. Every hand-written `have` in this bean's history
used the notation and therefore never matched — `rw` said "did not find an
occurrence" and `simp only` said "no progress" against goal terms that **print
identically**. That is why 33 tactic approaches all failed and why the mechanism
stayed unknown: the failures were not about coherence, `monoidalComp`, or the
hexagons at all.

Fix, one line: `simp only [ExactPairing.coevaluation, ExactPairing.evaluation] at <have>`.
Found by extracting the hypothesis and the goal under `set_option pp.explicit true`
and diffing them character by character. **That diff is the diagnostic to reach
for whenever a rewrite fails against a goal it visibly matches** — the pretty
printer showed `ExactPairing.coevaluation'` on both sides.

### Proof shape (all steps machine-checked)

1. `hpre` — normalise the `⊗≫`-padded cup to `η_X ≫ X ◁ u ≫ (α).inv`, by `monoidal`.
2. `braiding_naturality_left` + `braiding_tensor_left_hom` — move `(g ⊗ h)` past
   the block braiding and hexagon-split `β_{X⊗Y, Y'⊗X'}`.
3. `hrec` (from `braiding_tensor_right_hom`) — recombine the X-half.
4. `braiding_naturality_right` — detach the X-strand onto the cup; both sides now
   open `η_X ≫ β_{X,X'}`, peeled with `congrArg`.
5. `braiding_naturality` + `tensorHom_def'` + `whisker_exchange` — carry `g` to
   the front and `h` back into the Y-cup; peel `g` with `congrArg`.
6. `hsl` — `braiding_slide_cap_right` (QOU.MathlibExt.BraidedSlide) whiskered by
   `Y'`, bridged in and out by `monoidal`. This is the only genuinely
   knot-theoretic step: one strand crossing a cap.
7. `hfin` — assemble, `whisker_exchange` + `unitors_inv_equal` to finish.

### Why the monodromy is load-bearing (unchanged, now machine-checked)

`tensorExactPairing` nests the pairs in **opposite orders at its two ends** — cup
`X, Y, Y', X'`, cap `Y', X', X, Y`. The nested closure therefore links the
X-loop with the Y-loop, and `β_{X,Y} ≫ β_{Y,X}` is exactly the crossing that
unlinks them. The statement is false without it. This is the same asymmetry that
made the earlier `ptrWith` factorisation false, and that retraction stands.

### Verification (CI is `workflow_dispatch`-only; agent verification is the gate)

- `lean`-direct on `QOU/MathlibExt/TwistedQuantumDimension.lean`: **exit 0**, no warnings.
- `#print axioms` on both new declarations: `[propext, Classical.choice, Quot.sound]` — **no `sorryAx`**.
- `scripts/check-sidecars.sh`: clean; no §7c flags (file stays generic over `C`, no `ℝ`).
- Only consumer is the `QOU.lean` aggregator; nothing downstream to re-verify.

### Standing caveat, re-confirmed

Across this bean my predictions about **which rewrite would fire** were wrong
essentially every time; my **measurements of what did fire** all held. The final
unlock came from a measurement (`pp.explicit` diff), not a plan. Print the goal
after every simp-set change.
