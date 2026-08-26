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

section Spherical

/-- **The twisted LEFT quantum dimension**: the same strand closed on the other side, carrying the
*inverse* twist.  The inverse is not a choice — it is what makes the closure a framed-link
invariant of the same unknot, and it is what `qDimTwistedLeftWith_eq_of_cap` below needs. -/
noncomputable def qDimTwistedLeftWith [BalancedCategory C] (A B : C) [ExactPairing A B] :
    (𝟙_ C ⟶ 𝟙_ C) :=
  η_ A B ≫ (inv (BalancedCategory.twist A) ▷ B) ≫ (β_ B A).inv ≫ ε_ A B

/-- **Sphericality, reduced to one identity at the cap.**

Left trace = right trace *as soon as* the two twists agree across the evaluation,

    (θ_B ▷ A) ≫ ε  =  (B ◁ θ_A) ≫ ε.

Everything else is the balancing axiom.  Read as a decomposition this says exactly where the
content of sphericality sits: the Joyal–Street axiom `θ_{A⊗B} = β_{A,B} ≫ β_{B,A} ≫ (θ_A ⊗ θ_B)`
does all of the geometric work — it converts the *left* closure into the *right* one by feeding the
double braiding through the coevaluation — and leaves behind precisely one residue, the twist that
ended up on the dual leg.  A braided category alone cannot discharge that residue, because nothing
relates `θ_B` to `θ_A`.  That is the job of the ribbon axiom, and it is the whole job. -/
theorem qDimTwistedLeftWith_eq_of_cap [BalancedCategory C] (A B : C) [ExactPairing A B]
    (hcap : (BalancedCategory.twist B ▷ A) ≫ ε_ A B
      = (B ◁ BalancedCategory.twist A) ≫ ε_ A B) :
    qDimTwistedLeftWith A B = qDimTwistedWith A B := by
  -- `θ` is natural and `θ_𝟙 = 𝟙`, so the coevaluation absorbs `θ_{A⊗B}`.
  have hη : η_ A B ≫ BalancedCategory.twist (A ⊗ B) = η_ A B := by
    rw [← BalancedCategory.twist_naturality, BalancedCategory.twist_unit, Category.id_comp]
  -- The balancing axiom, with the `A`-twists cancelling and the `B`-twist swept past the braiding.
  have key : BalancedCategory.twist (A ⊗ B) ≫ (inv (BalancedCategory.twist A) ▷ B)
        ≫ (β_ B A).inv
      = (β_ A B).hom ≫ (BalancedCategory.twist B ▷ A) := by
    rw [BalancedCategory.twist_tensor, tensorHom_def]
    simp only [Category.assoc]
    rw [whisker_exchange_assoc, ← comp_whiskerRight_assoc, IsIso.hom_inv_id, id_whiskerRight,
      Category.id_comp, ← braiding_naturality_left_assoc, Iso.hom_inv_id, Category.comp_id]
  rw [qDimTwistedWith_twist_right, qDimTwistedLeftWith]
  conv_lhs => rw [← hη]
  simp only [Category.assoc]
  rw [reassoc_of% key, hcap]

/-- **Ribbon ⇒ spherical**: in a ribbon category the left and right twisted quantum dimensions of
every object agree.

This is the statement that is *unavailable* for the twistless trace `qDimWith`, and the reason is
visible in the proof: the cap identity is discharged by `RibbonCategory.twist_dual` together with
`rightAdjointMate_comp_evaluation` at `f = θ_X`, and with `θ = 𝟙` both sides of the cap identity
collapse to `ε` — true, but then `qDimTwistedLeftWith` and `qDimTwistedWith` are two *different*
twistless closures (`(β_ B A).inv` versus `(β_ A B).hom`) whose difference is the monodromy, and no
axiom of a braided rigid category forces that to vanish.  So the twistless pair is not made
spherical by this argument at any twist, including the trivial one; it is the twist that carries the
statement. -/
theorem qDimTwistedLeftWith_eq [RightRigidCategory C] [RibbonCategory C] (X : C) :
    qDimTwistedLeftWith X (Xᘁ) = qDimTwistedWith X (Xᘁ) := by
  refine qDimTwistedLeftWith_eq_of_cap X (Xᘁ) ?_
  rw [RibbonCategory.twist_dual]
  simpa using (@rightAdjointMate_comp_evaluation C _ _ X X _ _ (BalancedCategory.twist X))

end Spherical

section TwistlessSpecialisation

/-- **The twistless dimension is exactly the `θ = 𝟙` case.**  The module docstring asserts this;
here it is as a lemma, so the claim is backed rather than merely stated.

Note the hypothesis is *pointwise* — only `θ_A = 𝟙` is required, not `θ = 𝟙` globally.  So this
also covers an object that happens to be transparent in an otherwise non-trivially balanced
category, which is the case one actually meets. -/
theorem qDimTwistedWith_eq_qDimWith_of_twist_id [BalancedCategory C] (A B : C) [ExactPairing A B]
    (h : BalancedCategory.twist A = 𝟙 A) :
    qDimTwistedWith A B = qDimWith A B := by
  simp [qDimTwistedWith, qDimWith, h]

/-- **At the monoidal unit the twist is invisible**: `θ_𝟙 = 𝟙` is a `BalancedCategory` axiom, so
the twisted and twistless dimensions of the unit agree unconditionally.

This is why nothing in the RT-input vacuum normalisation moves when the twistless trace is
correctly renamed: `qDim_unit` is a statement about `𝟙_C`, and at `𝟙_C` there is no difference to
be made. -/
theorem qDimTwistedWith_unit [BalancedCategory C] (B : C) [ExactPairing (𝟙_ C) B] :
    qDimTwistedWith (𝟙_ C) B = qDimWith (𝟙_ C) B :=
  qDimTwistedWith_eq_qDimWith_of_twist_id _ _ BalancedCategory.twist_unit

end TwistlessSpecialisation

end QOU.MathlibExt
