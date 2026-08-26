---
# qou-l64i
title: 'GAP: multiplicativity of the twisted quantum dimension, dim(X tensor Y) = dim X * dim Y'
status: todo
type: task
priority: normal
created_at: 2026-08-26T22:59:50Z
updated_at: 2026-08-26T23:03:45Z
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
