---
# qou-l64i
title: 'GAP: multiplicativity of the twisted quantum dimension, dim(X tensor Y) = dim X * dim Y'
status: todo
type: task
priority: normal
created_at: 2026-08-26T22:59:50Z
updated_at: 2026-08-27T01:09:19Z
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
