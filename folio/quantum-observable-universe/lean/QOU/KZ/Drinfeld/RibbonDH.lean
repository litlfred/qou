import QOU.KZ.Drinfeld.Twist
import QOU.KZ.Drinfeld.Linear
import QOU.KZ.Drinfeld.Duals
import QOU.KZ.Drinfeld.BraidingVV
import QOU.MathlibExt.RibbonHeckeDimension
import Mathlib.Analysis.SpecialFunctions.Complex.Log

/-!
# `D_ℏ` is a ribbon category, and `dim_q V = [2]_q`

Stages S5–S6 of bean `qou-zoyv`. Sorry-free.

* `balanced` — `D_ℏ` (`ℏ` transcendental) is balanced with twist `θ_X = exp(iπℏ Ω_X)`, `Ω_X` the
  `sl₂` Casimir of `V^{⊗X}` (`Twist`).
* `ribbon` — for every Drinfeld associator `Ψ` (`D_ℏ` is right rigid by `Duals`), the ribbon axiom
  `θ_{Xᘁ} = (θ_X)ᘁ` holds. Proof: an invariant pairing `ε : Xᘁ ⊗ X → 𝟙` satisfies
  `ε(ρ(a) ⊗ 1) = −ε(1 ⊗ ρ(a))`, hence `ε(Ω ⊗ 1) = ε(1 ⊗ Ω)` and `ε(θ ⊗ 1) = ε(1 ⊗ θ)`
  (`eps_twist`); mates are detected by the evaluation (`eq_of_whiskerRight_comp_evaluation`).
* `hecke_DH` — with `s = e^{iπℏ/2}`, `q = e^{iπℏ}`:
  `s·β_{V,V} − s⁻¹·β_{V,V}⁻¹ = (q − q⁻¹)·𝟙`. The braiding uses the `sl₂` Casimir `t = P − ½`, so
  `β` has eigenvalues `s` on `Sym²V` and `−s⁻³` on `Λ²V`. The *unscaled* relation
  `β − β⁻¹ ∈ ℂ·𝟙` is false for every transcendental `ℏ` (`not_hecke_unscaled`), so
  `ribbon_hecke_qDim_eq_qint_two` does not apply verbatim; its scaled form
  `ribbon_hecke_dimension_scaled` (same proof) is used.
* `qDim_V_eq_qint_two` — `qDimTwistedWith V Vᘁ = (q + q⁻¹)·𝟙_𝟙`, `q = e^{iπℏ}`.
  Convention: `θ_V = e^{3iπℏ/2} = q^{C_V}`, `C_V = 3/2`.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stages S5, S6)
-/

noncomputable section

namespace QOU.KZ.Drinfeld

open QOU.KZ.DrinfeldAssociator CategoryTheory MonoidalCategory Finset QOU.KZ.FuchsianFormal QOU.KZ.BlockResidues Obj

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra


/-! ### Mates are detected by the evaluation -/

section Mate

variable {C : Type*} [Category C] [MonoidalCategory C]

/-- Precomposing the evaluation `ε : Y ⊗ X ⟶ 𝟙` with `g ▷ X` is injective in `g`. -/
theorem eq_of_whiskerRight_comp_evaluation {X Y : C} [ExactPairing X Y] {g h : Y ⟶ Y}
    (H : (g ▷ X) ≫ ε_ X Y = (h ▷ X) ≫ ε_ X Y) : g = h := by
  have key : ∀ g : Y ⟶ Y,
      tensorRightHomEquiv Y X Y (𝟙_ C) ((g ▷ X) ≫ ε_ X Y) = g ≫ (λ_ Y).inv := by
    intro g
    simp only [tensorRightHomEquiv, Equiv.coe_fn_mk]
    calc (ρ_ Y).inv ≫ Y ◁ η_ X Y ≫ (α_ Y X Y).inv ≫ ((g ▷ X) ≫ ε_ X Y) ▷ Y
        = g ≫ (ρ_ Y).inv ≫ Y ◁ η_ X Y ≫ (α_ Y X Y).inv ≫ ε_ X Y ▷ Y := by
          rw [comp_whiskerRight, ← associator_inv_naturality_left_assoc,
            whisker_exchange_assoc, rightUnitor_inv_naturality_assoc]
      _ = g ≫ (λ_ Y).inv := by
          rw [ExactPairing.coevaluation_evaluation, Iso.inv_hom_id_assoc]
  have := congrArg (tensorRightHomEquiv Y X Y (𝟙_ C)) H
  rw [key, key] at this
  exact (cancel_mono _).1 this

end Mate

/-! ### The twist of `D_ℏ` -/

section Pairings

variable {X Y : Obj}

theorem eps_flip (e : (tensor Y X : Obj) ⟶ unit) (a : Matrix (Fin 2) (Fin 2) ℂ) (ha : a.trace = 0) :
    e.1 * kron (ρ Y a) (1 : EndL (Leaves X)) = -(e.1 * kron (1 : EndL (Leaves Y)) (ρ X a)) := by
  have h := e.2 a ha
  rw [ρ_tensor, show ρ unit a = 0 from rfl, Matrix.zero_mul, Matrix.mul_add] at h
  exact eq_neg_of_add_eq_zero_left h.symm

theorem kron_one_comm {L L' : Type*} [Fintype L] [DecidableEq L] [Fintype L'] [DecidableEq L']
    (A : EndL L) (B : EndL L') : Commute (kron A (1 : EndL L')) (kron (1 : EndL L) B) := by
  show kron A 1 * kron 1 B = kron 1 B * kron A 1
  rw [kron_mul, kron_mul, Matrix.mul_one, Matrix.one_mul, Matrix.mul_one, Matrix.one_mul]

theorem eps_pair (e : (tensor Y X : Obj) ⟶ unit) (a b : Matrix (Fin 2) (Fin 2) ℂ)
    (ha : a.trace = 0) (hb : b.trace = 0) :
    e.1 * kron (ρ Y a * ρ Y b) 1 = e.1 * kron 1 (ρ X b * ρ X a) := by
  rw [kron_mul_one, one_kron_mul, ← Matrix.mul_assoc, eps_flip e a ha, Matrix.neg_mul,
    Matrix.mul_assoc, ← (kron_one_comm (ρ Y b) (ρ X a)).eq, ← Matrix.mul_assoc, eps_flip e b hb,
    Matrix.neg_mul, neg_neg, Matrix.mul_assoc]

/-- An invariant pairing `Y ⊗ X → 𝟙` sees the Casimir of `Y` as the Casimir of `X`. -/
theorem eps_casimir (e : (tensor Y X : Obj) ⟶ unit) :
    e.1 * kron (tsl (univ : Finset (Leaves Y)) univ) 1 =
      e.1 * kron 1 (tsl (univ : Finset (Leaves X)) univ) := by
  simp only [tsl, blk_univ, ← ρ_eq_diag, kron_add_left, kron_add_right, kron_smul_left,
    kron_smul_right, Matrix.mul_add, Matrix.mul_smul]
  rw [eps_pair e _ _ trace_eS trace_fS, eps_pair e _ _ trace_fS trace_eS,
    eps_pair e _ _ trace_hS trace_hS, add_comm (e.1 * kron 1 (ρ X fS * ρ X eS))]

variable (c : ℂ)

/-- **The twist passes through an invariant pairing**: `ε ∘ (θ_Y ⊗ 1) = ε ∘ (1 ⊗ θ_X)`. -/
theorem eps_twist (e : (tensor Y X : Obj) ⟶ unit) :
    e.1 * kron (θmat c Y) 1 = e.1 * kron 1 (θmat c X) := by
  rw [θmat, θmat, kron_expi_one, one_kron_expi]
  apply mul_expi_congr _ (kron_one_comm _ _)
  rw [kron_smul_left, kron_smul_right, Matrix.mul_smul, Matrix.mul_smul, eps_casimir]

end Pairings

section Balanced

variable (Ψ : Associator.{0}) (c : ℂ) [hc : Fact (Transcendental ℚ c)]

omit hc in
theorem θinv_mul_θmat (X : Obj) : θinv c X * θmat c X = 1 := expi_neg_mul_expi _
omit hc in
theorem θmat_mul_θinv (X : Obj) : θmat c X * θinv c X = 1 := expi_mul_expi_neg _

/-- **`D_ℏ` is balanced**: `θ_X = exp(iπℏ Ω_X)`. -/
instance balanced : QOU.MathlibExt.BalancedCategory (DH Ψ c) where
  twist X := ⟨θmat c X, equivariant_θmat c X⟩
  twist_isIso X := ⟨⟨⟨θinv c X, equivariant_θinv c X⟩, hom_ext (θinv_mul_θmat c X),
    hom_ext (θmat_mul_θinv c X)⟩⟩
  twist_unit := hom_ext (θmat_unit c)
  twist_naturality f := hom_ext (θmat_natural c f)
  twist_tensor X Y := hom_ext (by
    rw [comp_val, comp_val]
    show θmat c (tensor X Y) = _
    rw [θmat_tensor]
    rfl)

theorem twist_val (X : DH Ψ c) : (QOU.MathlibExt.BalancedCategory.twist X).1 = θmat c X := rfl

end Balanced

section Ribbon

variable (Ψ : Associator.{0}) (c : ℂ) [hc : Fact (Transcendental ℚ c)]

/-- **`D_ℏ` is ribbon** (`ℏ` transcendental, any associator `Ψ`). -/
instance ribbon : QOU.MathlibExt.RibbonCategory (DH Ψ c) where
  twist_dual X := by
    apply eq_of_whiskerRight_comp_evaluation (X := X)
    rw [rightAdjointMate_comp_evaluation]
    apply hom_ext
    rw [comp_val, comp_val]
    exact eps_twist c (ε_ X Xᘁ)

end Ribbon


/-! ### A scaled Hecke relation fixes the ribbon quantum dimension -/

section ScaledHecke

open QOU.MathlibExt BraidedCategory

variable {C : Type*} [Category C] [MonoidalCategory C] [BraidedCategory C] [Preadditive C]
  [MonoidalPreadditive C] {k : Type*} [Field k] [Linear k C] [MonoidalLinear k C]
  [RightRigidCategory C] [RibbonCategory C]

/-- **Scaled Hecke relation ⟹ dimension.** If `s·β − s⁻¹·β⁻¹ = (q − q⁻¹)·𝟙` on `V ⊗ V`,
`θ_V = a·𝟙` and `dim_q V = d·𝟙`, then `((q − q⁻¹)·d)·𝟙_V = (s·a − s⁻¹·a⁻¹)·𝟙_V`. With `s = 1` this
is `ribbon_hecke_dimension`. -/
theorem ribbon_hecke_dimension_scaled (V : C) (s q a d : k) (ha : a ≠ 0)
    (hHecke : s • (β_ V V).hom - s⁻¹ • (β_ V V).inv = (q - q⁻¹) • 𝟙 (V ⊗ V))
    (hθ : BalancedCategory.twist V = a • 𝟙 V)
    (hd : qDimTwistedWith V Vᘁ = d • 𝟙 (𝟙_ C)) :
    ((q - q⁻¹) * d) • 𝟙 V = (s * a - s⁻¹ * a⁻¹) • 𝟙 V := by
  have hinv : inv (BalancedCategory.twist V) = a⁻¹ • 𝟙 V := by
    apply IsIso.inv_eq_of_hom_inv_id
    rw [hθ]; simp [smul_smul, ha]
  have h := congrArg (ptrTwistWith V V Vᘁ) hHecke
  rw [ptrTwistWith_sub, ptrTwistWith_smul, ptrTwistWith_smul, ptrTwistWith_braiding,
    ptrTwistWith_braiding_inv, ptrTwistWith_smul, ptrTwistWith_id, hd, hinv, hθ] at h
  rw [sub_smul, mul_smul, mul_smul, mul_smul, h]
  simp [MonoidalLinear.whiskerLeft_smul, smul_smul]

end ScaledHecke


/-! ### S6: `dim_q V = [2]_q` in `D_ℏ` -/

section Dimension

open QOU.MathlibExt BraidedCategory

theorem casimir_V : tsl (univ : Finset (Leaves V)) univ = (3 / 2 : ℂ) • 1 := by
  have hu : (univ : Finset (Leaves V)) = {()} := rfl
  have hb : ∀ a, blk ({()} : Finset (Leaves V)) a = leafOp () a := fun a => by
    simp [blk]
  have hm : eS * fS + fS * eS + (1 / 2 : ℂ) • (hS * hS) = (3 / 2 : ℂ) • 1 := by
    ext i j; fin_cases i <;> fin_cases j <;> simp [eS, fS, hS] <;> norm_num
  rw [hu, tsl, hb, hb, hb, leafOp_mul_same, leafOp_mul_same, leafOp_mul_same, ← leafOp_smul,
    ← leafOp_add, ← leafOp_add, hm, leafOp_smul, leafOp_one]

variable (Ψ : Associator.{0}) (c : ℂ)

/-- `e^{3iπℏ/2}`, the twist of `V` (`θ_V = q^{C_V}` with `C_V = 3/2`). -/
def aV : ℂ := Complex.exp (Real.pi * Complex.I * (c * (3 / 2)))

theorem θmat_V : θmat c V = aV c • 1 := by
  rw [θmat, casimir_V, smul_smul, expi_smul_one]; rfl

theorem aV_eq : aV c = sV c ^ 3 := by
  unfold aV sV; rw [← Complex.exp_nat_mul]; ring_nf

/-- `V` as an object of `D_ℏ`. -/
def Vd : DH Ψ c := Obj.V

variable [hc : Fact (Transcendental ℚ c)]

/-- **The Hecke skein relation in `D_ℏ`**: `s·β_{V,V} − s⁻¹·β_{V,V}⁻¹ = (q − q⁻¹)·𝟙`,
`s = e^{iπℏ/2}`, `q = e^{iπℏ}`. -/
theorem hecke_DH :
    sV c • (β_ (Vd Ψ c) (Vd Ψ c)).hom - (sV c)⁻¹ • (β_ (Vd Ψ c) (Vd Ψ c)).inv
      = (qV c - (qV c)⁻¹) • 𝟙 (Vd Ψ c ⊗ Vd Ψ c) :=
  hom_ext (hecke_mat c)

/-- **The twist of `V`** is the scalar `e^{3iπℏ/2}`. -/
theorem twist_V : BalancedCategory.twist (Vd Ψ c) = aV c • 𝟙 (Vd Ψ c) :=
  hom_ext (θmat_V c)

/-- `End(𝟙) = ℂ`. -/
theorem end_unit_eq (f : (𝟙_ (DH Ψ c)) ⟶ 𝟙_ (DH Ψ c)) :
    f = (f.1 default default) • 𝟙 (𝟙_ (DH Ψ c)) := by
  apply hom_ext
  ext y x
  have hy : y = default := Subsingleton.elim _ _
  have hx : x = default := Subsingleton.elim _ _
  subst hy hx
  erw [smul_val, id_val]
  simp

omit hc in
theorem id_V_ne_zero : 𝟙 (Vd Ψ c) ≠ 0 := by
  intro h
  have := congrArg Subtype.val h
  rw [id_val, zero_val] at this
  exact one_ne_zero this

/-- **S6: `dim_q V = [2]_q` in `D_ℏ`.** For `ℏ` transcendental and any associator `Ψ`, the ribbon
quantum dimension of `V = ℂ²` in the Drinfeld category is `q + q⁻¹` with `q = e^{iπℏ}`. -/
theorem qDim_V_eq_qint_two :
    qDimTwistedWith (Vd Ψ c) (Vd Ψ c)ᘁ = (qV c + (qV c)⁻¹) • 𝟙 (𝟙_ (DH Ψ c)) := by
  have hd := end_unit_eq Ψ c (qDimTwistedWith (Vd Ψ c) (Vd Ψ c)ᘁ)
  set d := (qDimTwistedWith (Vd Ψ c) (Vd Ψ c)ᘁ).1 default default
  have hs := sV_ne_zero c
  have ha : aV c ≠ 0 := Complex.exp_ne_zero _
  have h := ribbon_hecke_dimension_scaled (Vd Ψ c) (sV c) (qV c) (aV c) d ha (hecke_DH Ψ c)
    (twist_V Ψ c) hd
  have h0 : (qV c - (qV c)⁻¹) * d - (sV c * aV c - (sV c)⁻¹ * (aV c)⁻¹) = 0 := by
    have h' := sub_eq_zero.mpr h
    rw [← sub_smul] at h'
    exact (smul_eq_zero.mp h').resolve_right (id_V_ne_zero Ψ c)
  have hq := qV_sub_inv_ne_zero c hc.out
  have hdq : d = qV c + (qV c)⁻¹ := by
    apply mul_left_cancel₀ hq
    rw [aV_eq] at h0
    rw [qV_eq] at h0 ⊢
    field_simp at h0 ⊢
    linear_combination h0
  rw [hd, hdq]

end Dimension


end QOU.KZ.Drinfeld
