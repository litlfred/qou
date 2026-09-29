/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import QOU.MathlibExt.Ribbon
import QOU.MathlibExt.BraidedQuantumDimension
import QOU.MathlibExt.RigidTensorDual
import QOU.MathlibExt.BraidedSlide

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
*inverse* twist.

**The inverse is load-bearing, so it needs a justification that is not "it makes the theorem
come out".**  `qDimTwistedLeftWith_eq_of_cap` works precisely because `θ_A` meets `θ_A⁻¹` and
cancels; with `θ_A` on both sides one is left with `θ_A²`, and the identity would require
`θ² = 𝟙`, which is false in general.  So the exponent is not cosmetic and cannot be waved through.

Two things justify it, and it is worth separating them:

1. **The opposite-exponent shape is the standard one.**  Barrett–Westbury, *Spherical Categories*,
   Prop. 3.6, give the two traces of a spherical Hopf algebra as `tr_L(θ) = tr(θw)` and
   `tr_R(θ) = tr(θw⁻¹)` — the same element in the two traces, with opposite exponents.
2. **That shape does not smuggle in sphericality.**  This is the non-circularity check, and it is
   the more important of the two: Barrett–Westbury's Example 3.5 — the quantised enveloping algebra
   of the Borel of `SL₂(ℂ)` — uses *this very convention* to exhibit a category satisfying every
   spherical axiom **except** that "the left and right traces are distinct".  A convention under
   which sphericality is still refutable is not one that assumes it.

**What this does NOT establish, stated so it is not read as more than it is.**  Barrett–Westbury's
`w` is the **pivotal element** (`γ²(b) = w b w⁻¹`), *not* the ribbon twist `θ`.  The two are related
in a ribbon category but are not the same object.  So the citation supports the *shape* of this
definition and its non-circularity; it is **not** a citation that this particular `θ`/`θ⁻¹` pairing
is the standard ribbon left trace.  Establishing that identification would need Turaev's
construction of the left duality from the right one, which is not formalised here.

-- Ref: [barrett1993] Barrett, Westbury, *Spherical Categories*, Prop. 3.6 and Example 3.5. -/
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

section PartialTrace

/-- **Braided trace of an ENDOMORPHISM**, relative to a chosen pairing: `η ≫ (f ▷ B) ≫ β ≫ ε`.

This is the common generalisation of the two dimensions in this file — `qDimWith` is its value at
`𝟙`, `qDimTwistedWith` its value at `θ`, recorded as `qTrWith_id` and `qTrWith_twist` below. Having
it is what lets a *partial* trace be composed with a full one, which is the shape the
multiplicativity route needs (bean `qou-l64i`). -/
noncomputable def qTrWith (A B : C) [ExactPairing A B] (f : A ⟶ A) : (𝟙_ C ⟶ 𝟙_ C) :=
  η_ A B ≫ (f ▷ B) ≫ (β_ A B).hom ≫ ε_ A B

theorem qTrWith_id (A B : C) [ExactPairing A B] : qTrWith A B (𝟙 A) = qDimWith A B := by
  simp [qTrWith, qDimWith]

theorem qTrWith_twist [BalancedCategory C] (A B : C) [ExactPairing A B] :
    qTrWith A B (BalancedCategory.twist A) = qDimTwistedWith A B := rfl

/-- **Right partial trace over `Y`**, relative to a chosen pairing `Y ⊣ Y'`: close only the `Y`
strand of an endomorphism of `X ⊗ Y`, leaving an endomorphism of `X`. -/
noncomputable def ptrWith (X Y Y' : C) [ExactPairing Y Y'] (f : X ⊗ Y ⟶ X ⊗ Y) : X ⟶ X :=
  𝟙 X ⊗≫ X ◁ η_ Y Y' ⊗≫ f ▷ Y' ⊗≫ X ◁ ((β_ Y Y').hom ≫ ε_ Y Y') ⊗≫ 𝟙 X

/-- **The partial trace of the identity is the dimension**, acting on `X` through the right unitor.

`End(𝟙_C)` acts on every hom-set by whiskering-and-unitors, and this says the partial trace of
`𝟙_{X⊗Y}` over `Y` is exactly `qDimWith Y Y'` acting on `X` that way — the categorical form of
"tracing out a factor multiplies by its dimension".

This is the FIRST of the two steps the multiplicativity route needs (bean `qou-l64i`, route 1). The
second — that the *nested* closure of `X ⊗ Y` factors as a full trace of a partial trace — is the
crux and is NOT proved here; its statement is recorded in that bean. Do not read this lemma as
progress on the nesting: it deliberately sits on the easy side of it. -/
theorem ptrWith_id (X Y Y' : C) [ExactPairing Y Y'] :
    ptrWith X Y Y' (𝟙 (X ⊗ Y)) = (ρ_ X).inv ≫ (X ◁ qDimWith Y Y') ≫ (ρ_ X).hom := by
  simp [ptrWith, qDimWith, monoidalComp]

set_option maxHeartbeats 1600000 in
/-- **The monodromy factorisation for the nested closure** (bean `qou-l64i`).

Closing the 2-cable `X ⊗ Y` against the nested dual `Y' ⊗ X'` of `tensorExactPairing`, with a
monodromy `β_{X,Y} ≫ β_{Y,X}` inserted in front of `g ⊗ h`, splits into the two separate closures.

The monodromy is not decoration: `tensorExactPairing` nests the two dual pairs in **opposite orders
at its two ends** — the cup is `X, Y, Y', X'` (X outside) while the cap is `Y', X', X, Y` (Y
outside) — so the nested closure links the `X`-loop with the `Y`-loop.  The monodromy is exactly the
crossing that unlinks them, which is why the statement is false without it.  This is also why the
earlier attempt to route the proof through a partial trace (`ptrWith`) could not work: no
trace-of-partial-trace factorisation respects two opposite nestings at once.

Proof shape: the hexagon splits `β_{X⊗Y, Y'⊗X'}` into the `X`- and `Y`-halves; braiding naturality
detaches the `X`-strand onto the cup and then carries `g` and `h` back to the two loops; what is
left is a single strand crossing a cap, discharged by `braiding_slide_cap_right`. -/
theorem qTrWith_tensor_monodromy (X X' Y Y' : C)
    [ExactPairing X X'] [ExactPairing Y Y'] (g : X ⟶ X) (h : Y ⟶ Y) :
    @qTrWith C _ _ _ (X ⊗ Y) (Y' ⊗ X') (tensorExactPairing X X' Y Y')
        ((β_ X Y).hom ≫ (β_ Y X).hom ≫ (g ⊗ₘ h))
      = qTrWith X X' g ≫ qTrWith Y Y' h := by
  have hrec : ∀ (W A B Z : C) (k : A ⊗ (B ⊗ W) ⟶ Z),
      (α_ W A B).hom ≫ (β_ W (A ⊗ B)).hom ≫ (α_ A B W).hom ≫ k
        = (β_ W A).hom ▷ B ≫ (α_ A W B).hom ≫ A ◁ (β_ W B).hom ≫ k := by
    intro W A B Z k; rw [braiding_tensor_right_hom]; simp
  have hsl : 𝟙 (((Y' ⊗ Y) ⊗ X') ⊗ X) ⊗≫ (Y' ◁ (β_ Y X').hom) ▷ X
        ⊗≫ (Y' ⊗ X') ◁ (β_ Y X).hom ⊗≫ Y' ◁ ε_ X X' ▷ Y ⊗≫ 𝟙 (Y' ⊗ Y)
      = 𝟙 (((Y' ⊗ Y) ⊗ X') ⊗ X) ⊗≫ Y' ◁ Y ◁ ε_ X X' ⊗≫ 𝟙 (Y' ⊗ Y) := by
    have hh := braiding_slide_cap_right (W := Y) (A := X') (B := X) (ε_ X X')
    calc _ = 𝟙 (((Y' ⊗ Y) ⊗ X') ⊗ X) ⊗≫ Y' ◁ (𝟙 ((Y ⊗ X') ⊗ X) ⊗≫ (β_ Y X').hom ▷ X
              ⊗≫ X' ◁ (β_ Y X).hom ⊗≫ ε_ X X' ▷ Y ⊗≫ 𝟙 Y) ⊗≫ 𝟙 (Y' ⊗ Y) := by monoidal
      _ = _ := by rw [hh]; monoidal
  have hfin : ∀ (v : 𝟙_ C ⟶ Y' ⊗ Y),
      ((λ_ X').inv ≫ v ▷ X' ≫ (α_ Y' Y X').hom ≫ Y' ◁ (β_ Y X').hom ≫ (α_ Y' X' Y).inv) ▷ X
        ≫ (α_ (Y' ⊗ X') Y X).hom ≫ (Y' ⊗ X') ◁ (β_ Y X).hom
        ≫ 𝟙 ((Y' ⊗ X') ⊗ X ⊗ Y) ⊗≫ Y' ◁ ε_ X X' ▷ Y ⊗≫ ε_ Y Y'
      = ε_ X X' ≫ v ≫ ε_ Y Y' := by
    intro v
    calc _ = (𝟙 (X' ⊗ X) ⊗≫ (v ▷ X') ▷ X ⊗≫ 𝟙 (((Y' ⊗ Y) ⊗ X') ⊗ X))
            ≫ (𝟙 (((Y' ⊗ Y) ⊗ X') ⊗ X) ⊗≫ (Y' ◁ (β_ Y X').hom) ▷ X
                ⊗≫ (Y' ⊗ X') ◁ (β_ Y X).hom ⊗≫ Y' ◁ ε_ X X' ▷ Y ⊗≫ 𝟙 (Y' ⊗ Y))
            ≫ ε_ Y Y' := by monoidal
      _ = (𝟙 (X' ⊗ X) ⊗≫ (v ▷ X') ▷ X ⊗≫ 𝟙 (((Y' ⊗ Y) ⊗ X') ⊗ X))
            ≫ (𝟙 (((Y' ⊗ Y) ⊗ X') ⊗ X) ⊗≫ Y' ◁ Y ◁ ε_ X X' ⊗≫ 𝟙 (Y' ⊗ Y))
            ≫ ε_ Y Y' := by rw [hsl]
      _ = ε_ X X' ≫ v ≫ ε_ Y Y' := by
            rw [← Category.assoc]
            rw [show (𝟙 (X' ⊗ X) ⊗≫ (v ▷ X') ▷ X ⊗≫ 𝟙 (((Y' ⊗ Y) ⊗ X') ⊗ X))
                  ≫ (𝟙 (((Y' ⊗ Y) ⊗ X') ⊗ X) ⊗≫ Y' ◁ Y ◁ ε_ X X' ⊗≫ 𝟙 (Y' ⊗ Y))
                = (λ_ (X' ⊗ X)).inv ≫ v ▷ (X' ⊗ X) ≫ (Y' ⊗ Y) ◁ ε_ X X' ≫ (ρ_ (Y' ⊗ Y)).hom from by monoidal]
            simp only [Category.assoc]
            rw [← whisker_exchange_assoc]
            simp [unitors_inv_equal]
  have hpre : ∀ (Z : C) (k : (X ⊗ Y) ⊗ (Y' ⊗ X') ⟶ Z),
      (η_ X X' ⊗≫ X ◁ η_ Y Y' ▷ X' ⊗≫ 𝟙 ((X ⊗ Y) ⊗ Y' ⊗ X')) ≫ k
        = η_ X X' ≫ X ◁ ((λ_ X').inv ≫ η_ Y Y' ▷ X' ≫ (α_ Y Y' X').hom)
            ≫ (α_ X Y (Y' ⊗ X')).inv ≫ k := by
    intro Z k; monoidal
  simp only [ExactPairing.coevaluation] at hpre
  simp only [qTrWith, tensorExactPairing, ExactPairing.coevaluation, ExactPairing.evaluation]
  rw [hpre]
  rw [braiding_naturality_left_assoc, braiding_tensor_left_hom]
  simp only [Category.assoc, Iso.inv_hom_id_assoc]
  simp only [MonoidalCategory.whiskerLeft_comp, Category.assoc]
  rw [← hrec X (Y' ⊗ X') Y, Iso.inv_hom_id_assoc]
  simp only [← MonoidalCategory.whiskerLeft_comp_assoc]
  rw [braiding_naturality_right_assoc]
  conv_rhs => rw [braiding_naturality_left_assoc]
  refine congrArg _ (congrArg _ ?_)
  rw [← braiding_naturality, tensorHom_def']
  simp only [MonoidalCategory.whiskerLeft_comp, Category.assoc]
  rw [← MonoidalCategory.associator_naturality_right_assoc,
    ← MonoidalCategory.whisker_exchange_assoc]
  refine congrArg _ ?_
  rw [← MonoidalCategory.associator_naturality_middle_assoc, ← comp_whiskerRight_assoc]
  simp only [Category.assoc]
  rw [← braiding_naturality_left]
  rw [← MonoidalCategory.associator_naturality_left_assoc, ← comp_whiskerRight_assoc]
  rw [braiding_tensor_right_hom]
  simp only [Category.assoc, Iso.hom_inv_id_assoc, ← comp_whiskerRight_assoc]
  have hf := hfin (η_ Y Y' ≫ h ▷ Y' ≫ (β_ Y Y').hom)
  simp only [ExactPairing.coevaluation, ExactPairing.evaluation, Category.assoc] at hf ⊢
  exact hf

/-- **Multiplicativity, CONDITIONAL on the monodromy factorisation.**

The hypothesis `hmono` is `qTrWith_tensor_monodromy` above, proved unconditionally as of bean
`qou-l64i`; the unconditional form is `qDimTwistedWith_tensor` below.  This conditional form is kept
because it isolates where the balancing axiom is used.  Closing the 2-cable `X ⊗ Y` with a
monodromy `β_{X,Y} ≫ β_{Y,X}` on the input splits into the two separate closures.  Given it, the
twisted quantum dimension is multiplicative, and the derivation uses the balancing axiom exactly
once — `twist_tensor` is precisely what puts the required monodromy in front of `θ_X ⊗ θ_Y`.

It was stated conditionally on purpose.  I had asserted in the bean that multiplicativity "is then
a corollary"; that assertion is what this theorem replaces with a machine-checked implication, after
an earlier assertion of the same kind (that the nested closure factors through `ptrWith`) turned out
to be false.  A named hypothesis discharged by `rw` is worth more than a claim that a step will go
through. -/
theorem qDimTwistedWith_tensor_of_monodromy [BalancedCategory C] (X X' Y Y' : C)
    [ExactPairing X X'] [ExactPairing Y Y']
    (hmono : ∀ (g : X ⟶ X) (h : Y ⟶ Y),
      @qTrWith C _ _ _ (X ⊗ Y) (Y' ⊗ X') (tensorExactPairing X X' Y Y')
          ((β_ X Y).hom ≫ (β_ Y X).hom ≫ (g ⊗ₘ h))
        = qTrWith X X' g ≫ qTrWith Y Y' h) :
    @qDimTwistedWith C _ _ _ _ (X ⊗ Y) (Y' ⊗ X') (tensorExactPairing X X' Y Y')
      = qDimTwistedWith X X' ≫ qDimTwistedWith Y Y' := by
  show @qTrWith C _ _ _ (X ⊗ Y) (Y' ⊗ X') (tensorExactPairing X X' Y Y')
        (BalancedCategory.twist (X ⊗ Y))
      = qTrWith X X' (BalancedCategory.twist X) ≫ qTrWith Y Y' (BalancedCategory.twist Y)
  rw [BalancedCategory.twist_tensor, hmono]

/-- **Multiplicativity of the twisted quantum dimension**, unconditionally.

`qDimTwistedWith_tensor_of_monodromy` with its hypothesis discharged by
`qTrWith_tensor_monodromy`.  This is the ribbon-category fact that the quantum dimension is a
monoid homomorphism, for the nested `tensorExactPairing` dual and with no rigidity assumed beyond
the two exact pairings. -/
theorem qDimTwistedWith_tensor [BalancedCategory C] (X X' Y Y' : C)
    [ExactPairing X X'] [ExactPairing Y Y'] :
    @qDimTwistedWith C _ _ _ _ (X ⊗ Y) (Y' ⊗ X') (tensorExactPairing X X' Y Y')
      = qDimTwistedWith X X' ≫ qDimTwistedWith Y Y' :=
  qDimTwistedWith_tensor_of_monodromy X X' Y Y' (qTrWith_tensor_monodromy X X' Y Y')

end PartialTrace

end QOU.MathlibExt
