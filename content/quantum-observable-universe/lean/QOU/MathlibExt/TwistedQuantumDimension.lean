/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import QOU.MathlibExt.Ribbon
import QOU.MathlibExt.BraidedQuantumDimension

/-!
# QOU.MathlibExt.TwistedQuantumDimension — the quantum dimension the ribbon literature means

`QOU.MathlibExt.qDimWith` is the **twistless** trace `η ≫ β ≫ ε`.  The classical quantum dimension
of a ribbon category is not that: it carries the twist,

    tr_q(f) = ε ∘ β ∘ ((θ_X ∘ f) ⊗ id) ∘ η

and `qDimWith` is exactly its `θ = 𝟙` specialisation.  That specialisation is correct in the
symmetric case and nowhere else, which is why `ribbon ⇒ spherical` — a theorem about the *twisted*
trace — cannot be stated against `qDimWith`.

This file supplies the twisted version, `qDimTwistedWith`, together with the two structural facts
`qDimWith` already has.  The interesting outcome is **where the ribbon axiom is and is not needed**:

* `qDimTwistedWith_congr_dual` — independence of the choice of dual holds on a **balanced**
  category alone.  The twist rides on `A`, not on the dual `B`, so it never meets the comparison
  map; one interchange step is the whole difference from the twistless proof.
* `qDimTwistedWith_rightDual` — conjugation symmetry `dim(Xᘁ) = dim(X)` **does** need the ribbon
  axiom, and needs it exactly once.  `RibbonCategory.twist_dual` converts `θ_{Xᘁ}` into `(θ_X)ᘁ`,
  and `rightAdjointMate_comp_evaluation` at `f = θ_X` then carries it across the evaluation.

So moving from the twistless dimension to the twisted one relocates conjugation symmetry from
"free" to "one axiom you already have", and costs nothing else.

## A display hazard, recorded because it cost real time

`ᘁ` is overloaded: postfix on an **object** it is the right dual, on a **morphism** it is
`rightAdjointMate`.  They print identically, so `RibbonCategory.twist_dual` renders as
`twist Xᘁ = twist Xᘁ` — a tautology on screen, a real rewrite in the elaborator.  A `rw` with it
looks like a no-op and is not.  Do not "simplify it away".
-/

namespace QOU.MathlibExt

open CategoryTheory MonoidalCategory Category BraidedCategory

variable {C : Type*} [Category C] [MonoidalCategory C] [BraidedCategory C]

/-- **The twisted (classical ribbon) quantum dimension**, relative to a chosen exact pairing:
`η ≫ (θ_A ▷ B) ≫ β ≫ ε`.  Setting `θ = 𝟙` recovers `qDimWith`. -/
noncomputable def qDimTwistedWith [BalancedCategory C] (A B : C) [ExactPairing A B] :
    (𝟙_ C ⟶ 𝟙_ C) :=
  η_ A B ≫ (BalancedCategory.twist A ▷ B) ≫ (β_ A B).hom ≫ ε_ A B

/-- The twist may be taken on either side of the braiding — braiding naturality, nothing more. -/
theorem qDimTwistedWith_twist_right [BalancedCategory C] (A B : C) [ExactPairing A B] :
    qDimTwistedWith A B
      = η_ A B ≫ (β_ A B).hom ≫ (B ◁ BalancedCategory.twist A) ≫ ε_ A B := by
  simp [qDimTwistedWith]

/-- **The twisted quantum dimension does not depend on the choice of right dual** — and, unlike
conjugation symmetry below, this needs **no ribbon axiom**.

The twist acts on `A`; the comparison `rightDualIso` acts on the dual leg.  They are disjoint, so
the twistless proof goes through with one interchange step added. -/
theorem qDimTwistedWith_congr_dual [BalancedCategory C] {A B₁ B₂ : C}
    (p₁ : ExactPairing A B₁) (p₂ : ExactPairing A B₂) :
    @qDimTwistedWith C _ _ _ _ A B₁ p₁ = @qDimTwistedWith C _ _ _ _ A B₂ p₂ := by
  have hη : η_ A B₁ ≫ (A ◁ (rightDualIso p₁ p₂).hom) = η_ A B₂ := by
    simpa using (@coevaluation_comp_rightAdjointMate C _ _ A A ⟨B₂⟩ ⟨B₁⟩ (𝟙 A))
  have hε : ((rightDualIso p₁ p₂).hom ▷ A) ≫ ε_ A B₂ = ε_ A B₁ := by
    simpa using (@rightAdjointMate_comp_evaluation C _ _ A A ⟨B₂⟩ ⟨B₁⟩ (𝟙 A))
  simp only [qDimTwistedWith]
  rw [← hη, ← hε]
  simp only [Category.assoc]
  rw [whisker_exchange_assoc, braiding_naturality_right_assoc]

/-- **Conjugation symmetry of the twisted quantum dimension**, `dim(Xᘁ) = dim(X)`.

This is where the ribbon axiom earns its place, and it is used exactly once:
`RibbonCategory.twist_dual` rewrites `θ_{Xᘁ}` to `(θ_X)ᘁ`, and `rightAdjointMate_comp_evaluation`
at `f = θ_X` carries that mate across the evaluation.  Everything else is braiding naturality and
`qDimTwistedWith_congr_dual`, which moves to the swapped pairing exhibiting `X` as a right dual
of `Xᘁ`.

Contrast `qDimWith_rightDual`, which needs no axiom at all — that is the price of the twist, and
it is the whole price. -/
theorem qDimTwistedWith_rightDual [RightRigidCategory C] [RibbonCategory C] (X : C) :
    @qDimTwistedWith C _ _ _ _ ((X : C)ᘁ) (((X : C)ᘁ : C)ᘁ) inferInstance
      = @qDimTwistedWith C _ _ _ _ X ((X : C)ᘁ) inferInstance := by
  have hcongr : @qDimTwistedWith C _ _ _ _ ((X : C)ᘁ) (((X : C)ᘁ : C)ᘁ) inferInstance
      = @qDimTwistedWith C _ _ _ _ ((X : C)ᘁ) X (exactPairing_swap X ((X : C)ᘁ)) :=
    qDimTwistedWith_congr_dual _ _
  rw [hcongr]
  have hmate := @rightAdjointMate_comp_evaluation C _ _ X X _ _ (BalancedCategory.twist X)
  have hdual := RibbonCategory.twist_dual (C := C) X
  show (η_ X ((X : C)ᘁ) ≫ (β_ ((X : C)ᘁ) X).inv)
        ≫ (BalancedCategory.twist ((X : C)ᘁ) ▷ X)
        ≫ (β_ ((X : C)ᘁ) X).hom ≫ ((β_ X ((X : C)ᘁ)).hom ≫ ε_ X ((X : C)ᘁ))
      = _
  rw [hdual]
  simp only [Category.assoc, braiding_naturality_left_assoc, Iso.inv_hom_id_assoc]
  rw [braiding_naturality_right_assoc, hmate]
  simp only [qDimTwistedWith]
  rw [braiding_naturality_left_assoc]

end QOU.MathlibExt
