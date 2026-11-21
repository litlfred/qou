/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import QOU.MathlibExt.TwistedQuantumDimension
import Mathlib.CategoryTheory.Monoidal.Linear
import Mathlib.Tactic.LinearCombination

/-!
# QOU.MathlibExt.RibbonHeckeDimension — a Hecke skein relation fixes the quantum dimension

In a `k`-linear ribbon category, let `V` be an object whose self-braiding `c = β_{V,V}` satisfies
the Hecke skein relation `c − c⁻¹ = (q − q⁻¹)·𝟙_{V⊗V}` and whose twist is a scalar `θ_V = a·𝟙_V`.
If the twisted (ribbon) quantum dimension `qDimTwistedWith V Vᘁ` is the scalar `d`, then

    (q − q⁻¹)·d = a − a⁻¹.

With `a = q²` and `q² ≠ 1` this gives `d = q + q⁻¹ = [2]_q` (`ribbon_hecke_qDim_eq_qint_two`).
This is Step 2 of the Drinfeld–Kohno route in
`docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md`, proved here as an abstract statement about
ribbon categories: nothing about `D_ℏ` is used or assumed.

## Proof

Apply the twisted right partial trace `ptrTwistWith V V Vᘁ` (the twistless `ptrWith` of
`TwistedQuantumDimension` with a `θ` on the closed strand, so that it closes with the ribbon
evaluation `(θ ▷ Vᘁ) ≫ β ≫ ε`, the convention of `qDimTwistedWith`) to the Hecke relation. Three
facts, all proved here:

* `ptrTwistWith_id` — the trace of `𝟙` is `qDimTwistedWith` acting on `V`.
* `ptrTwistWith_braiding` — the **positive curl**: the trace of `c` is `θ_V`. It reduces to
  `ptrWith_braiding`, which says the *twistless* partial trace of `c` is `𝟙_V` in any braided rigid
  category (hexagon + braiding naturality + one zigzag): the curl of the closure cancels the curl
  of `c`, so all of `θ_V` comes from the twist on the closing strand.
* `ptrTwistWith_braiding_inv` — the **negative curl**: the trace of `c⁻¹` is `θ_V⁻¹`. This is the
  only place the **ribbon axiom** `θ_{Vᘁ} = (θ_V)ᘁ` is used: `twist_closure_eq` shows the ribbon
  evaluation can equally be written with the inverse braiding and the inverse twist,
  `(θ ▷ Vᘁ) ≫ β_{V,Vᘁ} ≫ ε = (θ⁻¹ ▷ Vᘁ) ≫ β_{Vᘁ,V}⁻¹ ≫ ε`, from the balancing axiom at `(Vᘁ, V)`,
  naturality of `θ` along `ε`, and `rightAdjointMate_comp_evaluation`. The mirror-image braided
  computation `ptrInvWith_braiding_inv` then finishes it.

Linearity of the partial trace (`ptrTwistWith_sub`, `ptrTwistWith_smul`) needs
`MonoidalPreadditive` / `MonoidalLinear k`.

## Scope

* The scalar hypotheses `θ_V = a·𝟙` and `qDimTwistedWith V Vᘁ = d·𝟙_{𝟙}` are hypotheses, not
  consequences; in a category with `End(𝟙) = k` and `V` simple they hold, but neither is derived
  here.
* **No nondegenerate instance is constructed.** The only ribbon instances in the tree are the
  symmetric ones (`RibbonCategory.ofSymmetric`, `θ = 𝟙`), where `c = c⁻¹` forces `q = q⁻¹`: the
  theorem is then true with both sides `0`, which tests nothing. A genuine instance with `q² ≠ 1`
  needs a quantum-group or KZ category, which is bean `qou-zoyv`.
* Base ring (§7c): a generic field `k`; nothing archimedean.

-- Ref: [leitner2026] docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md (Step 2)
-/

namespace QOU.MathlibExt
open CategoryTheory MonoidalCategory Category BraidedCategory

section Braided
variable {C : Type*} [Category C] [MonoidalCategory C] [BraidedCategory C]

/-- **The twistless partial trace of the self-braiding is the identity** in any braided category:
the curl of the braided closure `β ≫ ε` cancels the curl of `β_{V,V}`. -/
theorem ptrWith_braiding (V V' : C) [ExactPairing V V'] :
    ptrWith V V V' (β_ V V).hom = 𝟙 V := by
  have hex := braiding_tensor_right_hom V V V'
  have hnat := braiding_naturality_right V (η_ V V')
  calc ptrWith V V V' (β_ V V).hom
      = 𝟙 V ⊗≫ V ◁ η_ V V' ⊗≫ ((α_ V V V').inv ≫ (β_ V V).hom ▷ V' ≫ (α_ V V V').hom
          ≫ V ◁ (β_ V V').hom ≫ (α_ V V' V).inv) ⊗≫ V ◁ ε_ V V' ⊗≫ 𝟙 V := by
        simp only [ptrWith]; monoidal
    _ = 𝟙 V ⊗≫ (V ◁ η_ V V' ≫ (β_ V (V ⊗ V')).hom) ⊗≫ V ◁ ε_ V V' ⊗≫ 𝟙 V := by
        rw [hex]; monoidal
    _ = 𝟙 V ⊗≫ ((β_ V (𝟙_ C)).hom ≫ η_ V V' ▷ V) ⊗≫ V ◁ ε_ V V' ⊗≫ 𝟙 V := by
        rw [hnat]
    _ = 𝟙 V := by
        rw [braiding_tensorUnit_right]
        calc _ = 𝟙 V ⊗≫ (η_ V V' ▷ V ⊗≫ V ◁ ε_ V V') ⊗≫ 𝟙 V := by monoidal
          _ = 𝟙 V := by rw [ExactPairing.evaluation_coevaluation'']; monoidal

/-- **Right partial trace closed with the inverse braiding**: the mirror image of `ptrWith`. -/
noncomputable def ptrInvWith (X Y Y' : C) [ExactPairing Y Y'] (f : X ⊗ Y ⟶ X ⊗ Y) : X ⟶ X :=
  𝟙 X ⊗≫ X ◁ η_ Y Y' ⊗≫ f ▷ Y' ⊗≫ X ◁ ((β_ Y' Y).inv ≫ ε_ Y Y') ⊗≫ 𝟙 X

/-- Mirror image of `ptrWith_braiding`: the inverse-closed partial trace of `β_{V,V}⁻¹` is `𝟙`. -/
theorem ptrInvWith_braiding_inv (V V' : C) [ExactPairing V V'] :
    ptrInvWith V V V' (β_ V V).inv = 𝟙 V := by
  have hex := braiding_tensor_left_inv V V' V
  have hnat := braiding_inv_naturality_right V (η_ V V')
  calc ptrInvWith V V V' (β_ V V).inv
      = 𝟙 V ⊗≫ V ◁ η_ V V' ⊗≫ ((α_ V V V').inv ≫ (β_ V V).inv ▷ V' ≫ (α_ V V V').hom
          ≫ V ◁ (β_ V' V).inv ≫ (α_ V V' V).inv) ⊗≫ V ◁ ε_ V V' ⊗≫ 𝟙 V := by
        simp only [ptrInvWith]; monoidal
    _ = 𝟙 V ⊗≫ (V ◁ η_ V V' ≫ (β_ (V ⊗ V') V).inv) ⊗≫ V ◁ ε_ V V' ⊗≫ 𝟙 V := by
        rw [hex]; monoidal
    _ = 𝟙 V ⊗≫ ((β_ (𝟙_ C) V).inv ≫ η_ V V' ▷ V) ⊗≫ V ◁ ε_ V V' ⊗≫ 𝟙 V := by
        rw [hnat]
    _ = 𝟙 V := by
        rw [braiding_inv_tensorUnit_left]
        calc _ = 𝟙 V ⊗≫ (η_ V V' ▷ V ⊗≫ V ◁ ε_ V V') ⊗≫ 𝟙 V := by monoidal
          _ = 𝟙 V := by rw [ExactPairing.evaluation_coevaluation'']; monoidal

theorem ptrWith_whiskerRight_comp (X Y Y' : C) [ExactPairing Y Y'] (g : X ⟶ X)
    (f : X ⊗ Y ⟶ X ⊗ Y) : ptrWith X Y Y' (g ▷ Y ≫ f) = g ≫ ptrWith X Y Y' f := by
  simp only [ptrWith, comp_whiskerRight]
  calc _ = 𝟙 X ⊗≫ (g ▷ (𝟙_ C) ≫ X ◁ η_ Y Y') ⊗≫ f ▷ Y' ⊗≫
        X ◁ ((β_ Y Y').hom ≫ ε_ Y Y') ⊗≫ 𝟙 X := by rw [← whisker_exchange]; monoidal
    _ = _ := by monoidal

theorem ptrInvWith_whiskerRight_comp (X Y Y' : C) [ExactPairing Y Y'] (g : X ⟶ X)
    (f : X ⊗ Y ⟶ X ⊗ Y) : ptrInvWith X Y Y' (g ▷ Y ≫ f) = g ≫ ptrInvWith X Y Y' f := by
  simp only [ptrInvWith, comp_whiskerRight]
  calc _ = 𝟙 X ⊗≫ (g ▷ (𝟙_ C) ≫ X ◁ η_ Y Y') ⊗≫ f ▷ Y' ⊗≫
        X ◁ ((β_ Y' Y).inv ≫ ε_ Y Y') ⊗≫ 𝟙 X := by rw [← whisker_exchange]; monoidal
    _ = _ := by monoidal

theorem ptrWith_comp_whiskerLeft (X Y Y' : C) [ExactPairing Y Y'] (f : X ⊗ Y ⟶ X ⊗ Y)
    (h : Y ⟶ Y) : ptrWith X Y Y' (f ≫ X ◁ h)
      = 𝟙 X ⊗≫ X ◁ η_ Y Y' ⊗≫ f ▷ Y' ⊗≫ X ◁ (h ▷ Y' ≫ (β_ Y Y').hom ≫ ε_ Y Y') ⊗≫ 𝟙 X := by
  simp only [ptrWith]; monoidal

theorem ptrInvWith_comp_whiskerLeft (X Y Y' : C) [ExactPairing Y Y'] (f : X ⊗ Y ⟶ X ⊗ Y)
    (h : Y ⟶ Y) : ptrInvWith X Y Y' (f ≫ X ◁ h)
      = 𝟙 X ⊗≫ X ◁ η_ Y Y' ⊗≫ f ▷ Y' ⊗≫ X ◁ (h ▷ Y' ≫ (β_ Y' Y).inv ≫ ε_ Y Y') ⊗≫ 𝟙 X := by
  simp only [ptrInvWith]; monoidal

end Braided

section Balanced
variable {C : Type*} [Category C] [MonoidalCategory C] [BraidedCategory C] [BalancedCategory C]

/-- **The ribbon right partial trace**: close the right strand with the ribbon evaluation
`(θ ▷ Y') ≫ β ≫ ε`, the convention of `qDimTwistedWith`. -/
noncomputable def ptrTwistWith (X Y Y' : C) [ExactPairing Y Y'] (f : X ⊗ Y ⟶ X ⊗ Y) : X ⟶ X :=
  ptrWith X Y Y' (f ≫ X ◁ BalancedCategory.twist Y)

/-- **Positive curl = twist**: `ptr(β_{V,V}) = θ_V`. Holds in any balanced category. -/
theorem ptrTwistWith_braiding (V V' : C) [ExactPairing V V'] :
    ptrTwistWith V V V' (β_ V V).hom = BalancedCategory.twist V := by
  rw [ptrTwistWith, ← braiding_naturality_left, ptrWith_whiskerRight_comp, ptrWith_braiding,
    comp_id]

/-- The ribbon partial trace of `𝟙` is the twisted quantum dimension acting on `X`. -/
theorem ptrTwistWith_id (X Y Y' : C) [ExactPairing Y Y'] :
    ptrTwistWith X Y Y' (𝟙 (X ⊗ Y)) = (ρ_ X).inv ≫ (X ◁ qDimTwistedWith Y Y') ≫ (ρ_ X).hom := by
  simp [ptrTwistWith, ptrWith, qDimTwistedWith, monoidalComp]
  simp only [← whiskerLeft_comp_assoc]
  congr 2
  simp

end Balanced

section Ribbon
variable {C : Type*} [Category C] [MonoidalCategory C] [BraidedCategory C] [RightRigidCategory C]
  [RibbonCategory C]

open BalancedCategory in
/-- **The ribbon evaluation via the inverse braiding**: in a ribbon category
`(θ ▷ Vᘁ) ≫ β_{V,Vᘁ} ≫ ε = (θ⁻¹ ▷ Vᘁ) ≫ β_{Vᘁ,V}⁻¹ ≫ ε`. Uses the balancing axiom at `(Vᘁ, V)`
and the ribbon axiom `θ_{Vᘁ} = (θ_V)ᘁ`. -/
theorem twist_closure_eq (V : C) :
    (twist V ▷ Vᘁ) ≫ (β_ V Vᘁ).hom ≫ ε_ V Vᘁ
      = (inv (twist V) ▷ Vᘁ) ≫ (β_ Vᘁ V).inv ≫ ε_ V Vᘁ := by
  -- balancing at (Vᘁ, V), pushed through the evaluation
  have hbal : (β_ Vᘁ V).hom ≫ (β_ V Vᘁ).hom ≫ (Vᘁ ◁ twist V) ≫ (Vᘁ ◁ twist V) ≫ ε_ V Vᘁ
      = ε_ V Vᘁ := by
    have h1 : twist (Vᘁ ⊗ V) ≫ ε_ V Vᘁ = ε_ V Vᘁ := by
      rw [twist_naturality, twist_unit, comp_id]
    rw [twist_tensor, tensorHom_def', RibbonCategory.twist_dual] at h1
    simp only [assoc] at h1
    rw [rightAdjointMate_comp_evaluation] at h1
    exact h1
  have hcomm : (Vᘁ ◁ inv (twist V)) ≫ (β_ Vᘁ V).hom ≫ (β_ V Vᘁ).hom
      = (β_ Vᘁ V).hom ≫ (β_ V Vᘁ).hom ≫ (Vᘁ ◁ inv (twist V)) := by
    rw [braiding_naturality_right_assoc, braiding_naturality_left]
  have key : (β_ Vᘁ V).hom ≫ (β_ V Vᘁ).hom ≫ (Vᘁ ◁ twist V) ≫ ε_ V Vᘁ
      = (Vᘁ ◁ inv (twist V)) ≫ ε_ V Vᘁ := by
    have := congrArg (fun k => (Vᘁ ◁ inv (twist V)) ≫ k) hbal
    simp only at this
    rw [← this, reassoc_of% hcomm]
    rw [← whiskerLeft_comp_assoc, IsIso.inv_hom_id, whiskerLeft_id, id_comp]
  rw [braiding_naturality_left_assoc, braiding_inv_naturality_left_assoc]
  rw [← cancel_epi (β_ Vᘁ V).hom, Iso.hom_inv_id_assoc, key]

/-- The ribbon partial trace rewritten through the inverse closure (`twist_closure_eq`). -/
theorem ptrTwistWith_eq_ptrInvWith (V : C) (f : V ⊗ V ⟶ V ⊗ V) :
    ptrTwistWith V V Vᘁ f = ptrInvWith V V Vᘁ (f ≫ V ◁ inv (BalancedCategory.twist V)) := by
  rw [ptrTwistWith, ptrWith_comp_whiskerLeft, ptrInvWith_comp_whiskerLeft, twist_closure_eq]

/-- **Negative curl = inverse twist**: `ptr(β_{V,V}⁻¹) = θ_V⁻¹`. Needs the ribbon axiom. -/
theorem ptrTwistWith_braiding_inv (V : C) :
    ptrTwistWith V V Vᘁ (β_ V V).inv = inv (BalancedCategory.twist V) := by
  rw [ptrTwistWith_eq_ptrInvWith, ← braiding_inv_naturality_left, ptrInvWith_whiskerRight_comp,
    ptrInvWith_braiding_inv, comp_id]

end Ribbon

section Linear
variable {C : Type*} [Category C] [MonoidalCategory C] [BraidedCategory C] [Preadditive C]
  [MonoidalPreadditive C]

omit [BraidedCategory C] in
private theorem sub_whiskerRight' {X Y : C} (f g : X ⟶ Y) (Z : C) :
    (f - g) ▷ Z = f ▷ Z - g ▷ Z :=
  eq_sub_of_add_eq (by rw [← MonoidalPreadditive.add_whiskerRight, sub_add_cancel])

theorem ptrTwistWith_sub [BalancedCategory C] (X Y Y' : C) [ExactPairing Y Y']
    (f g : X ⊗ Y ⟶ X ⊗ Y) :
    ptrTwistWith X Y Y' (f - g) = ptrTwistWith X Y Y' f - ptrTwistWith X Y Y' g := by
  simp [ptrTwistWith, ptrWith, monoidalComp, Preadditive.sub_comp, sub_whiskerRight']

variable {k : Type*} [Field k] [Linear k C] [MonoidalLinear k C]

theorem ptrTwistWith_smul [BalancedCategory C] (X Y Y' : C) [ExactPairing Y Y'] (r : k)
    (f : X ⊗ Y ⟶ X ⊗ Y) : ptrTwistWith X Y Y' (r • f) = r • ptrTwistWith X Y Y' f := by
  simp [ptrTwistWith, ptrWith, monoidalComp]

variable [RightRigidCategory C] [RibbonCategory C]

/-- **Hecke skein relation ⟹ `(q − q⁻¹)·dim_q V = a − a⁻¹`.** In a `k`-linear ribbon category, if
`β_{V,V} − β_{V,V}⁻¹ = (q − q⁻¹)·𝟙`, `θ_V = a·𝟙` and `dim_q V = d·𝟙_{𝟙}`, then
`((q − q⁻¹)·d)·𝟙_V = (a − a⁻¹)·𝟙_V`. -/
theorem ribbon_hecke_dimension (V : C) (q a d : k) (ha : a ≠ 0)
    (hHecke : (β_ V V).hom - (β_ V V).inv = (q - q⁻¹) • 𝟙 (V ⊗ V))
    (hθ : BalancedCategory.twist V = a • 𝟙 V)
    (hd : qDimTwistedWith V Vᘁ = d • 𝟙 (𝟙_ C)) :
    ((q - q⁻¹) * d) • 𝟙 V = (a - a⁻¹) • 𝟙 V := by
  have hinv : inv (BalancedCategory.twist V) = a⁻¹ • 𝟙 V := by
    apply IsIso.inv_eq_of_hom_inv_id
    rw [hθ]; simp [smul_smul, ha]
  have h := congrArg (ptrTwistWith V V Vᘁ) hHecke
  rw [ptrTwistWith_sub, ptrTwistWith_braiding, ptrTwistWith_braiding_inv, ptrTwistWith_smul,
    ptrTwistWith_id, hd, hinv, hθ] at h
  rw [sub_smul, h]
  simp [MonoidalLinear.whiskerLeft_smul, smul_smul]

/-- **`dim_q V = [2]_q`.** Under the hypotheses of `ribbon_hecke_dimension` with `a = q²`,
`q² ≠ 1` (as `q − q⁻¹ ≠ 0`) and `𝟙_V ≠ 0`, the quantum dimension is `q + q⁻¹`. -/
theorem ribbon_hecke_qDim_eq_qint_two (V : C) (q d : k) (hV : 𝟙 V ≠ 0) (hq : q - q⁻¹ ≠ 0)
    (hHecke : (β_ V V).hom - (β_ V V).inv = (q - q⁻¹) • 𝟙 (V ⊗ V))
    (hθ : BalancedCategory.twist V = (q ^ 2) • 𝟙 V)
    (hd : qDimTwistedWith V Vᘁ = d • 𝟙 (𝟙_ C)) :
    d = q + q⁻¹ := by
  have hq0 : q ≠ 0 := by rintro rfl; simp at hq
  have h := ribbon_hecke_dimension V q (q ^ 2) d (pow_ne_zero 2 hq0) hHecke hθ hd
  have h0 : (q - q⁻¹) * d - (q ^ 2 - (q ^ 2)⁻¹) = 0 := by
    have h' := sub_eq_zero.mpr h
    rw [← sub_smul] at h'
    exact (smul_eq_zero.mp h').resolve_right hV
  apply mul_left_cancel₀ hq
  linear_combination h0

end Linear

end QOU.MathlibExt
