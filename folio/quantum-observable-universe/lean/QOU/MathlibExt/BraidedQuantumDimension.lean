/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import Mathlib.CategoryTheory.Monoidal.Rigid.Braided

/-!
# QOU.MathlibExt.BraidedQuantumDimension — the braided quantum dimension, and its duality symmetry

The **braided quantum dimension** of an object `A` with a chosen right dual `B` is the scalar

    qDimWith A B = η_ A B ≫ (β_ A B).hom ≫ ε_ A B  :  𝟙_C ⟶ 𝟙_C

— the *braided*, **twistless** closure of the identity. Mathlib has the coevaluation, the
evaluation and the braiding, but no name for their composite and no lemma about it.

**This is not the ribbon trace, and calling it that is a category error.** The ribbon trace carries
the balancing twist, `η ≫ (θ_A ▷ B) ≫ β ≫ ε`; no `θ` appears above and none can, because
`BalancedCategory` is not in scope here. The two agree exactly when `θ = 𝟙`. The genuine twisted
trace is `QOU.MathlibExt.qDimTwistedWith`, and the difference is not cosmetic: sphericality
(left trace = right trace) is provable for the twisted one from the ribbon axiom and is
*structurally unavailable* for this one, since the two twistless closures differ by the monodromy,
which no braided-rigid axiom kills.

What the twistless closure *does* have, and keeps: `qDimWith_congr_dual` and `qDimWith_rightDual`
below, both on a plain braided (right-rigid) category with no balanced or ribbon structure — the
latter is strictly *cheaper* here than its twisted counterpart, which needs the ribbon axiom.

## Main statements

* `qDimWith_congr_dual` — **the quantum dimension does not depend on the choice of dual.** For any
  two exact pairings `A ⊣ B₁` and `A ⊣ B₂`, the two scalars agree. The proof transports `η` and `ε`
  across `rightDualIso` (Mathlib's `coevaluation_comp_rightAdjointMate` and
  `rightAdjointMate_comp_evaluation` at `f = 𝟙`) and cancels the comparison map by braiding
  naturality. This is the quantum-dimension analogue of `rightAdjointMate_congr_dual` in
  [`PivotalCategory.lean`](PivotalCategory.lean).
* `qDimWith_swap` — read against the **swapped** pairing, which makes `X` a right dual *of* `Xᘁ`,
  the dimension of `Xᘁ` collapses to that of `X`: the swapped coevaluation carries a `β⁻¹` that
  cancels the trace's own `β` on the nose.
* `qDimWith_rightDual` — **the braided quantum dimension is conjugation-symmetric**,
  `qDim(Xᘁ) = qDim(X)`, unconditionally in any braided right-rigid category.

## Why this is not the statement the corpus expected to need

`KeystonePivotalSpherical.lean` factors this symmetry into two hypotheses — *pivotal transport*
(`qDimObj (Xᘁ) = leftQDim X`) and *sphericality* — and `KeystoneRibbonCategory.lean` recorded the
general-object case as blocked, on the reasoning that `qDimObj (Xᘁ)` traverses the double dual
`Xᘁᘁ`, which a braided right-rigid category does not identify with `X`, so the statement was "not
merely unproved but *not expressible as a computation on the existing data*".

**The premise is right and the conclusion does not follow.** `Xᘁᘁ` genuinely is not identified with
`X` by that data — but the *dimension* never needs the identification. It needs only that the
dimension of a fixed object is the same whichever dual is used to compute it, and `X` is *also* a
right dual of `Xᘁ` (`BraidedCategory.exactPairing_swap`). Dual-**independence** is strictly weaker
than double-dual **identification**, and it is what the trace actually consumes.

The conditional theorems in `KeystonePivotalSpherical.lean` remain valid; they are simply no longer
the only route, and neither hypothesis is needed for this conclusion. Sphericality is untouched and
is a genuinely separate condition.

## Name collision (§notation-collisions)

`QOU.BraidKnot.C2QDimTranspose.qDim_conj` is a **different theorem**: `d_q(λ) = d_q(λ')` for a
partition `λ` over `ℝ`, the transpose-invariance of the combinatorial hook-length q-dimension.
Nothing here refers to it. The declaration below is named `qDimWith_rightDual` to keep the two
apart.

-- Ref: [leitner2026] docs/coordination/s5-so3-keystone.md
-/

namespace QOU.MathlibExt

open CategoryTheory MonoidalCategory BraidedCategory

variable {C : Type*} [Category C] [MonoidalCategory C] [BraidedCategory C]

/-- **The braided quantum dimension** of `A` taken against a *named* right dual `B`: the ribbon
trace of the identity, `η ≫ β ≫ ε`. Writing the dual explicitly is what lets `qDimWith_congr_dual`
say the choice does not matter. -/
noncomputable def qDimWith (A B : C) [ExactPairing A B] : (𝟙_ C ⟶ 𝟙_ C) :=
  η_ A B ≫ (β_ A B).hom ≫ ε_ A B

/-- **The quantum dimension does not depend on the choice of dual.**

`rightDualIso p₁ p₂ : B₁ ≅ B₂` is the comparison map. Mathlib's
`coevaluation_comp_rightAdjointMate` and `rightAdjointMate_comp_evaluation`, at `f = 𝟙 A` with
mixed instances, say exactly that it transports `η` and `ε` between the two pairings; braiding
naturality then slides it from one side of the crossing to the other, where the two occurrences
cancel. -/
theorem qDimWith_congr_dual {A B₁ B₂ : C}
    (p₁ : ExactPairing A B₁) (p₂ : ExactPairing A B₂) :
    @qDimWith C _ _ _ A B₁ p₁ = @qDimWith C _ _ _ A B₂ p₂ := by
  have hη : η_ A B₁ ≫ (A ◁ (rightDualIso p₁ p₂).hom) = η_ A B₂ := by
    simpa using (@coevaluation_comp_rightAdjointMate C _ _ A A ⟨B₂⟩ ⟨B₁⟩ (𝟙 A))
  have hε : ((rightDualIso p₁ p₂).hom ▷ A) ≫ ε_ A B₂ = ε_ A B₁ := by
    simpa using (@rightAdjointMate_comp_evaluation C _ _ A A ⟨B₂⟩ ⟨B₁⟩ (𝟙 A))
  simp only [qDimWith]
  rw [← hη, ← hε]
  simp

/-- **Against the swapped pairing, the dimension of `Xᘁ` is the dimension of `X`.**

`BraidedCategory.exactPairing_swap` makes `X` a right dual of `Xᘁ`, with coevaluation
`η_ X Xᘁ ≫ (β_ Xᘁ X).inv` and evaluation `(β_ X Xᘁ).hom ≫ ε_ X Xᘁ`. The `β⁻¹` the coevaluation
carries meets the trace's own `β` and cancels, leaving `qDim(X)` exactly. -/
theorem qDimWith_swap (X : C) [HasRightDual X] :
    @qDimWith C _ _ _ ((X : C)ᘁ) X (exactPairing_swap X ((X : C)ᘁ))
      = η_ X ((X : C)ᘁ) ≫ (β_ X ((X : C)ᘁ)).hom ≫ ε_ X ((X : C)ᘁ) := by
  simp [qDimWith, exactPairing_swap, ExactPairing.coevaluation, ExactPairing.evaluation]

/-- **The braided quantum dimension is conjugation-symmetric**: `qDim(Xᘁ) = qDim(X)`, in any
braided right-rigid category, with no pivotal, spherical or transport hypothesis.

Both duals of `Xᘁ` — the canonical `Xᘁᘁ` and the swapped `X` — give the same dimension by
`qDimWith_congr_dual`; against the swapped one it is `qDim(X)` by `qDimWith_swap`.

Distinct from `QOU.BraidKnot.C2QDimTranspose.qDim_conj`, which is the partition-transpose statement
`d_q(λ) = d_q(λ')` over `ℝ`. -/
theorem qDimWith_rightDual [RightRigidCategory C] (X : C) :
    @qDimWith C _ _ _ ((X : C)ᘁ) (((X : C)ᘁ : C)ᘁ) inferInstance
      = @qDimWith C _ _ _ X ((X : C)ᘁ) inferInstance := by
  have h := qDimWith_congr_dual (A := (X : C)ᘁ)
      (HasRightDual.exact (X := (X : C)ᘁ)) (exactPairing_swap X ((X : C)ᘁ))
  rw [h]
  exact qDimWith_swap X

end QOU.MathlibExt
