---
# qou-l8az
title: 'Step 1: ExactPairing (X⊗Y) (Yᘁ⊗Xᘁ) — Mathlib Future-work entry, not done'
status: in-progress
type: task
priority: normal
created_at: 2026-08-26T18:00:27Z
updated_at: 2026-08-26T18:11:08Z
---


## Status 2026-08-26: construction FOUND and verified to elaborate; the snake is NOT proved

### What is settled (real progress, do not redo)

The coevaluation and evaluation formulas are correct and TYPECHECK against the
required signatures:

    coevaluation' := eta_X (X) (X2) tensorcomp X <| eta_Y (Y) (Y2) |> X2 tensorcomp id
    evaluation'   := id tensorcomp Y2 <| eps_X (X) (X2) |> Y tensorcomp eps_Y (Y) (Y2)

i.e. in Lean notation
    coevaluation' := eta_ X X' ⊗≫ X ◁ eta_ Y Y' ▷ X' ⊗≫ 𝟙 _
    evaluation'   := 𝟙 _ ⊗≫ Y' ◁ eps_ X X' ▷ Y ⊗≫ eps_ Y Y'

Both were checked standalone against
    𝟙_C ⟶ (X ⊗ Y) ⊗ (Y' ⊗ X')   and   (Y' ⊗ X') ⊗ (X ⊗ Y) ⟶ 𝟙_C
and elaborate clean. So the DEFINITION is not the open part.

### What is open

Both ExactPairing snake fields. Neither is dischargeable by the autoparam.

RULED OUT (each run, each fails):
  cat_disch (the class's own autoparam), simp, monoidal, aesop_cat,
  simp [monoidalComp], simp only [monoidalComp] + simp,
  + [whisker_exchange], + [<- whisker_exchange] (rw and simp forms), 6 variants.

### Diagnosis

monoidal handles associators and unitors ONLY. The missing step is the
INTERCHANGE law: the two snakes are NESTED (X2 from the dual pairs with X from
eta_X; Y2 pairs with Y), and moving eta_Y past eps_X on disjoint strands is
whisker_exchange, which monoidal does not apply and which simp does not place
correctly on its own.

So this needs a HAND-WRITTEN calc in Mathlib's own idiom -- the shape used by
exactPairingCongrLeft (Rigid/Basic.lean ~line 388) and
coevaluation_evaluation_braided' (Rigid/Braided.lean): normalise with monoidal
into ⊗≫ form until a literal `A ◁ g ≫ f ▷ B` pattern is exposed, rw
[whisker_exchange], monoidal again, repeat.

### Attempted intermediate that does NOT work

    Y' ◁ (X' ◁ eta_X ⊗≫ eps_X ▷ X') ⊗≫ (Y' ◁ eta_Y ⊗≫ eps_Y ▷ Y') ▷ X'

The decomposition is mathematically right -- it is the two component snakes,
each in coevaluation_evaluation'' form -- but `monoidal` cannot bridge the outer
composite to it, for the interchange reason above. An earlier version with
`▷ 𝟙_ C` appended failed differently, on MonoidalCoherence synthesis, because
its endpoints were wrong (𝟙_C instead of Y' ⊗ X').

### Honest cost estimate

This is a genuine string-diagram coherence proof of the kind Mathlib left on its
Future-work list. Comparable proofs in Rigid/Braided.lean run 20-30 lines of calc
with a Yang-Baxter/Whitney step. NOT the sixty-lines-of-mate-algebra shape that
closed rtqd and the drinfeldIso naturality -- I predicted in PR #5848 that this
one would be different, and so far it is.

### METHOD ERROR to avoid repeating

My first tactic battery reported "field 1 PASSED" on cat_disch. It had not. The
battery's success test keyed on WHICH FIELD the error message named, which tests
nothing -- an error naming field 2 is equally consistent with field 1 failing
first. Verified properly by putting `sorry` in field 2 and cat_disch in field 1:
field 1 fails. A pass/fail harness whose success condition is not the thing being
tested is worse than no harness.
