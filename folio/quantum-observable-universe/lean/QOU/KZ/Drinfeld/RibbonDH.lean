import QOU.KZ.Drinfeld.Twist
import QOU.KZ.Drinfeld.Linear
import QOU.KZ.Drinfeld.Duals
import QOU.MathlibExt.RibbonHeckeDimension
import Mathlib.Analysis.SpecialFunctions.Complex.Log

/-!
# `D_ℏ` is a ribbon category, and `dim_q V = [2]_q`

Stages S5–S6 of bean `qou-zoyv`. Sorry-free.

* `balanced` — `D_ℏ` (`ℏ` transcendental) is balanced with twist `θ_X = exp(iπℏ Ω_X)`, `Ω_X` the
  `sl₂` Casimir of `V^{⊗X}` (`Twist`).
* `ribbon` — with `‖ℏ‖ ≤ 1/12` (so that `D_ℏ` is right rigid, `Duals`), the ribbon axiom
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

open CategoryTheory MonoidalCategory Finset QOU.KZ.FuchsianFormal QOU.KZ.BlockResidues Obj

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

section Annihilate

variable {m L : Type*} [Fintype L] [DecidableEq L]

/-- If `A * D = 0` then `A * exp D = A`. -/
theorem mul_exp_of_mul_eq_zero (A : Matrix m (L → Fin 2) ℂ) (D : EndL L) (h : A * D = 0) :
    A * NormedSpace.exp ℂ D = A := by
  have hpow : ∀ n : ℕ, A * D ^ (n + 1) = 0 := fun n => by
    rw [pow_succ', ← Matrix.mul_assoc, h, Matrix.zero_mul]
  let g : EndL L →+ Matrix m (L → Fin 2) ℂ :=
    { toFun := fun M => A * M, map_zero' := Matrix.mul_zero A, map_add' := Matrix.mul_add A }
  have hg : Continuous g := continuous_const.matrix_mul continuous_id
  have hs := ((NormedSpace.expSeries_summable' (𝕂 := ℂ) D).hasSum.map g hg).tsum_eq
  rw [NormedSpace.exp_eq_tsum (𝕂 := ℂ)]
  show g _ = A
  rw [← hs, tsum_eq_single 0]
  · simp [g]
  · intro n hn
    obtain ⟨k, rfl⟩ := Nat.exists_eq_succ_of_ne_zero hn
    simp [g, Matrix.mul_smul, hpow k]

/-- If `A * X = A * Y` with `X`, `Y` commuting, then `A * expi X = A * expi Y`. -/
theorem mul_expi_congr (A : Matrix m (L → Fin 2) ℂ) {X Y : EndL L} (hXY : Commute X Y)
    (h : A * X = A * Y) : A * expi X = A * expi Y := by
  have hX : X = (X - Y) + Y := by abel
  have hc : Commute (X - Y) Y := (hXY.sub_left (Commute.refl Y))
  rw [hX, expi_add hc, ← Matrix.mul_assoc]
  congr 1
  apply mul_exp_of_mul_eq_zero
  rw [Matrix.mul_smul, Matrix.mul_sub, h, sub_self, smul_zero]

end Annihilate

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

variable (c : ℂ) [hc : Fact (Transcendental ℚ c)]

omit hc in
theorem θinv_mul_θmat (X : Obj) : θinv c X * θmat c X = 1 := expi_neg_mul_expi _
omit hc in
theorem θmat_mul_θinv (X : Obj) : θmat c X * θinv c X = 1 := expi_mul_expi_neg _

/-- **`D_ℏ` is balanced**: `θ_X = exp(iπℏ Ω_X)`. -/
instance balanced : QOU.MathlibExt.BalancedCategory (DH c) where
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

theorem twist_val (X : DH c) : (QOU.MathlibExt.BalancedCategory.twist X).1 = θmat c X := rfl

end Balanced

section Ribbon

variable (c : ℂ) [hc : Fact (Transcendental ℚ c)] [hsm : Fact (‖c‖ ≤ 1 / 12)]

/-- **`D_ℏ` is ribbon** (`ℏ` transcendental, `‖ℏ‖ ≤ 1/12`). -/
instance ribbon : QOU.MathlibExt.RibbonCategory (DH c) where
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

/-! ### The braiding on `V ⊗ V` -/

section Hecke

/-- The flip of the two legs of `V ⊗ V`. -/
abbrev PV : EndL (Leaves (tensor V V)) := flipL ℂ 2 (Sum.inl ()) (Sum.inr ())

theorem PV_mul_PV : PV * PV = 1 := by
  rw [PV, flipL, permL_mul, Equiv.swap_mul_self]
  ext y x
  simp [permL, permMat, Matrix.one_apply, eq_comm]

theorem reidx_swapLegs_VV : reidx (swapLegs V V) = PV := by
  have key : ∀ x y : Idx (tensor V V),
      (x = y ∘ swapLegs V V) ↔ (x ∘ Equiv.swap (Sum.inl ()) (Sum.inr ()) = y) := by
    intro x y
    constructor
    · rintro rfl; funext k; rcases k with ⟨⟩ | ⟨⟩ <;> simp [swapLegs]
    · rintro rfl; funext k; rcases k with ⟨⟩ | ⟨⟩ <;> simp [swapLegs]
  ext y x
  simp only [reidx, PV, flipL, permL, permMat, Matrix.of_apply, key]

theorem bL_VV : bL V V = {Sum.inl ()} := by
  ext k; rcases k with ⟨⟩ | ⟨⟩ <;> simp [bL]

theorem bR_VV : bR V V = {Sum.inr ()} := by
  ext k; rcases k with ⟨⟩ | ⟨⟩ <;> simp [bR]

/-- On `V ⊗ V` the `sl₂` block Casimir is `t = P − ½`. -/
theorem tsl_VV : tsl (bL V V) (bR V V) = PV - (1 / 2 : ℂ) • 1 := by
  have h := tB_eq_tsl (disj_bLR V V)
  rw [bL_VV, bR_VV] at h ⊢
  rw [tB, sum_singleton, sum_singleton, card_singleton] at h
  rw [eq_sub_of_add_eq h.symm, card_singleton]; norm_num

/-- `exp(iπ r·1) = e^{iπr}·1`. -/
theorem expi_smul_one {L : Type*} [Fintype L] [DecidableEq L] (r : ℂ) :
    expi (r • (1 : EndL L)) = Complex.exp (Real.pi * Complex.I * r) • 1 := by
  unfold expi
  rw [smul_smul, ← Algebra.algebraMap_eq_smul_one, ← NormedSpace.algebraMap_exp_comm,
    ← Complex.exp_eq_exp_ℂ, Algebra.algebraMap_eq_smul_one]

/-- The two spectral projections of the flip. -/
def Pp : EndL (Leaves (tensor V V)) := (1 / 2 : ℂ) • (1 + PV)
def Pm : EndL (Leaves (tensor V V)) := (1 / 2 : ℂ) • (1 - PV)

theorem Pp_mul_PV : Pp * PV = Pp := by
  rw [Pp, Matrix.smul_mul, Matrix.add_mul, PV_mul_PV, Matrix.one_mul, add_comm]

theorem Pm_mul_PV : Pm * PV = -Pm := by
  rw [Pm, Matrix.smul_mul, Matrix.sub_mul, PV_mul_PV, Matrix.one_mul, ← smul_neg, neg_sub]

theorem Pp_add_Pm : Pp + Pm = 1 := by
  rw [Pp, Pm, ← smul_add]; module

theorem PV_eq : PV = Pp - Pm := by
  rw [Pp, Pm]; module

theorem Pp_mul_Pp : Pp * Pp = Pp := by
  show Pp * ((1 / 2 : ℂ) • (1 + PV)) = Pp
  rw [Matrix.mul_smul, Matrix.mul_add, Matrix.mul_one, Pp_mul_PV, ← two_smul ℂ Pp, smul_smul]
  norm_num

theorem Pm_mul_Pm : Pm * Pm = Pm := by
  show Pm * ((1 / 2 : ℂ) • (1 - PV)) = Pm
  rw [Matrix.mul_smul, Matrix.mul_sub, Matrix.mul_one, Pm_mul_PV, sub_neg_eq_add, ← two_smul ℂ Pm,
    smul_smul]
  norm_num

theorem Pp_mul_Pm : Pp * Pm = 0 := by
  conv_lhs => rw [show (Pm : EndL _) = (1 / 2 : ℂ) • (1 - PV) from rfl]
  rw [Matrix.mul_smul, Matrix.mul_sub, Matrix.mul_one, Pp_mul_PV, sub_self, smul_zero]

theorem Pm_mul_Pp : Pm * Pp = 0 := by
  conv_lhs => rw [show (Pp : EndL _) = (1 / 2 : ℂ) • (1 + PV) from rfl]
  rw [Matrix.mul_smul, Matrix.mul_add, Matrix.mul_one, Pm_mul_PV, add_neg_cancel, smul_zero]

variable (c : ℂ)

/-- `e^{iπℏ/2}`, the eigenvalue of `β_{V,V}` on `Sym² V`. -/
def sV : ℂ := Complex.exp (Real.pi * Complex.I * (c / 2))
/-- `e^{−3iπℏ/2}`, minus the eigenvalue of `β_{V,V}` on `Λ² V`. -/
def tV : ℂ := Complex.exp (Real.pi * Complex.I * (-(3 * c / 2)))
/-- `q = e^{iπℏ}`. -/
def qV : ℂ := Complex.exp (Real.pi * Complex.I * c)

theorem Pp_mul_expi : Pp * expi (c • tsl (bL V V) (bR V V)) = sV c • Pp := by
  have h : Pp * (c • tsl (bL V V) (bR V V)) = Pp * ((c / 2) • (1 : EndL _)) := by
    rw [tsl_VV, Matrix.mul_smul, Matrix.mul_sub, Pp_mul_PV, Matrix.mul_smul, Matrix.mul_one,
      Matrix.mul_smul, Matrix.mul_one]
    module
  rw [mul_expi_congr Pp (commute_scalar (c / 2) _).symm h, expi_smul_one, Matrix.mul_smul,
    Matrix.mul_one]
  rfl

theorem Pm_mul_expi : Pm * expi (c • tsl (bL V V) (bR V V)) = tV c • Pm := by
  have h : Pm * (c • tsl (bL V V) (bR V V)) = Pm * ((-(3 * c / 2)) • (1 : EndL _)) := by
    rw [tsl_VV, Matrix.mul_smul, Matrix.mul_sub, Pm_mul_PV, Matrix.mul_smul, Matrix.mul_one,
      Matrix.mul_smul, Matrix.mul_one]
    module
  rw [mul_expi_congr Pm (commute_scalar (-(3 * c / 2)) _).symm h, expi_smul_one, Matrix.mul_smul,
    Matrix.mul_one]
  rfl

theorem βmat_VV : βmat c V V = sV c • Pp - tV c • Pm := by
  rw [βmat, reidx_swapLegs_VV, PV_eq, Matrix.sub_mul, Pp_mul_expi, Pm_mul_expi]

theorem sV_ne_zero : sV c ≠ 0 := Complex.exp_ne_zero _
theorem tV_ne_zero : tV c ≠ 0 := Complex.exp_ne_zero _

theorem βinv_VV : βinv c V V = (sV c)⁻¹ • Pp - (tV c)⁻¹ • Pm := by
  have hs := sV_ne_zero c
  have ht := tV_ne_zero c
  have h1 : βmat c V V * ((sV c)⁻¹ • Pp - (tV c)⁻¹ • Pm) = 1 := by
    rw [βmat_VV]
    simp only [Matrix.sub_mul, Matrix.mul_sub, Matrix.smul_mul, Matrix.mul_smul]
    rw [Pp_mul_Pp, Pm_mul_Pm, Pp_mul_Pm, Pm_mul_Pp]
    conv_rhs => rw [← Pp_add_Pm]
    match_scalars <;> field_simp
  calc βinv c V V = βinv c V V * (βmat c V V * ((sV c)⁻¹ • Pp - (tV c)⁻¹ • Pm)) := by
        rw [h1, Matrix.mul_one]
    _ = _ := by rw [← Matrix.mul_assoc, βinv_mul_βmat, Matrix.one_mul]

theorem sV_mul_sV : sV c * sV c = qV c := by
  unfold sV qV; rw [← Complex.exp_add]; ring_nf

theorem sV_mul_tV : sV c * tV c = (qV c)⁻¹ := by
  unfold sV tV qV; rw [← Complex.exp_add, ← Complex.exp_neg]; ring_nf

/-- **The Hecke skein relation in `D_ℏ`** (matrix form): with `s = e^{iπℏ/2}`, `q = e^{iπℏ}`,
`s·β − s⁻¹·β⁻¹ = (q − q⁻¹)·1` on `V ⊗ V`. -/
theorem tV_eq : tV c = ((sV c) ^ 3)⁻¹ := by
  unfold tV sV; rw [← Complex.exp_nat_mul, ← Complex.exp_neg]; ring_nf

theorem qV_eq : qV c = sV c ^ 2 := by rw [sq, sV_mul_sV]

/-- **The Hecke skein relation in `D_ℏ`** (matrix form): with `s = e^{iπℏ/2}`, `q = e^{iπℏ}`,
`s·β − s⁻¹·β⁻¹ = (q − q⁻¹)·1` on `V ⊗ V`. -/
theorem hecke_mat :
    sV c • βmat c V V - (sV c)⁻¹ • βinv c V V = (qV c - (qV c)⁻¹) • 1 := by
  have hs := sV_ne_zero c
  rw [βmat_VV, βinv_VV, tV_eq, qV_eq]
  conv_rhs => rw [← Pp_add_Pm]
  match_scalars <;> field_simp <;> ring

end Hecke

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

variable (c : ℂ)

/-- `e^{3iπℏ/2}`, the twist of `V` (`θ_V = q^{C_V}` with `C_V = 3/2`). -/
def aV : ℂ := Complex.exp (Real.pi * Complex.I * (c * (3 / 2)))

theorem θmat_V : θmat c V = aV c • 1 := by
  rw [θmat, casimir_V, smul_smul, expi_smul_one]; rfl

theorem aV_eq : aV c = sV c ^ 3 := by
  unfold aV sV; rw [← Complex.exp_nat_mul]; ring_nf

theorem qV_sub_inv_ne_zero (hc : Transcendental ℚ c) : qV c - (qV c)⁻¹ ≠ 0 := by
  intro h
  have hq0 : qV c ≠ 0 := Complex.exp_ne_zero _
  have h2 : qV c * qV c = 1 := by
    have := congrArg (qV c * ·) h
    simp only [mul_sub, mul_inv_cancel₀ hq0, mul_zero] at this
    exact sub_eq_zero.1 this
  have he : Complex.exp (c * (2 * Real.pi * Complex.I)) = 1 := by
    rw [← h2]; unfold qV; rw [← Complex.exp_add]; ring_nf
  obtain ⟨n, hn⟩ := Complex.exp_eq_one_iff.1 he
  have h2pi : (2 * Real.pi * Complex.I : ℂ) ≠ 0 := by
    simp [Real.pi_ne_zero, Complex.I_ne_zero]
  have hcn : c = n := mul_right_cancel₀ h2pi hn
  exact hc (hcn ▸ isAlgebraic_int (R := ℚ) (A := ℂ) n)

/-- `V` as an object of `D_ℏ`. -/
def Vd (c : ℂ) : DH c := Obj.V

variable [hc : Fact (Transcendental ℚ c)]

/-- **The Hecke skein relation in `D_ℏ`**: `s·β_{V,V} − s⁻¹·β_{V,V}⁻¹ = (q − q⁻¹)·𝟙`,
`s = e^{iπℏ/2}`, `q = e^{iπℏ}`. -/
theorem hecke_DH :
    sV c • (β_ (Vd c) (Vd c)).hom - (sV c)⁻¹ • (β_ (Vd c) (Vd c)).inv
      = (qV c - (qV c)⁻¹) • 𝟙 (Vd c ⊗ Vd c) :=
  hom_ext (hecke_mat c)

/-- **The twist of `V`** is the scalar `e^{3iπℏ/2}`. -/
theorem twist_V : BalancedCategory.twist (Vd c) = aV c • 𝟙 (Vd c) :=
  hom_ext (θmat_V c)

/-- `End(𝟙) = ℂ`. -/
theorem end_unit_eq (f : (𝟙_ (DH c)) ⟶ 𝟙_ (DH c)) :
    f = (f.1 default default) • 𝟙 (𝟙_ (DH c)) := by
  apply hom_ext
  ext y x
  have hy : y = default := Subsingleton.elim _ _
  have hx : x = default := Subsingleton.elim _ _
  subst hy hx
  erw [smul_val, id_val]
  simp

omit hc in
theorem id_V_ne_zero : 𝟙 (Vd c) ≠ 0 := by
  intro h
  have := congrArg Subtype.val h
  rw [id_val, zero_val] at this
  exact one_ne_zero this

variable [hsm : Fact (‖c‖ ≤ 1 / 12)]

/-- **S6: `dim_q V = [2]_q` in `D_ℏ`.** For `ℏ` transcendental with `‖ℏ‖ ≤ 1/12`, the ribbon
quantum dimension of `V = ℂ²` in the Drinfeld category is `q + q⁻¹` with `q = e^{iπℏ}`. -/
theorem qDim_V_eq_qint_two :
    qDimTwistedWith (Vd c) (Vd c)ᘁ = (qV c + (qV c)⁻¹) • 𝟙 (𝟙_ (DH c)) := by
  have hd := end_unit_eq c (qDimTwistedWith (Vd c) (Vd c)ᘁ)
  set d := (qDimTwistedWith (Vd c) (Vd c)ᘁ).1 default default
  have hs := sV_ne_zero c
  have ha : aV c ≠ 0 := Complex.exp_ne_zero _
  have h := ribbon_hecke_dimension_scaled (Vd c) (sV c) (qV c) (aV c) d ha (hecke_DH c)
    (twist_V c) hd
  have h0 : (qV c - (qV c)⁻¹) * d - (sV c * aV c - (sV c)⁻¹ * (aV c)⁻¹) = 0 := by
    have h' := sub_eq_zero.mpr h
    rw [← sub_smul] at h'
    exact (smul_eq_zero.mp h').resolve_right (id_V_ne_zero c)
  have hq := qV_sub_inv_ne_zero c hc.out
  have hdq : d = qV c + (qV c)⁻¹ := by
    apply mul_left_cancel₀ hq
    rw [aV_eq] at h0
    rw [qV_eq] at h0 ⊢
    field_simp at h0 ⊢
    linear_combination h0
  rw [hd, hdq]

end Dimension

/-! ### The unscaled Hecke relation fails in the `sl₂` normalisation

`ribbon_hecke_qDim_eq_qint_two` assumes `β − β⁻¹ = (q − q⁻¹)·𝟙`. In `D_ℏ` the braiding is built
from the `sl₂` Casimir `t = P − ½` (forced by naturality, see `Braiding`), so its eigenvalues are
`s = e^{iπℏ/2}` on `Sym²V` and `−s⁻³` on `Λ²V`; `β − β⁻¹` is then **not** a scalar for any
transcendental `ℏ`. Only the rescaled braiding `s·β` satisfies the Hecke relation (`hecke_DH`),
which is why `ribbon_hecke_dimension_scaled` is used. -/

section Unscaled

theorem Pp_ne_zero : Pp ≠ 0 := by
  intro h
  have := congrFun (congrFun h (fun _ => 0)) (fun _ => 0)
  have hc : (fun _ : Leaves (tensor V V) => (0 : Fin 2)) ∘ ⇑(Equiv.swap (Sum.inl ()) (Sum.inr ()))
      = fun _ => 0 := rfl
  simp [Pp, PV, permL, permMat] at this
  rw [if_pos hc] at this
  norm_num at this

theorem Pm_ne_zero : Pm ≠ 0 := by
  intro h
  set y : Idx (tensor V V) := Sum.elim (fun _ => 0) (fun _ => 1)
  have hy : ¬ (y ∘ Equiv.swap (Sum.inl ()) (Sum.inr ()) = y) := by
    intro e
    have := congrFun e (Sum.inl ())
    simp [y] at this
  have := congrFun (congrFun h y) y
  simp [Pm, PV, permL, permMat, hy] at this

theorem not_hecke_unscaled (c : ℂ) (hc : Transcendental ℚ c) :
    ¬ ∃ r : ℂ, βmat c V V - βinv c V V = r • 1 := by
  rintro ⟨r, hr⟩
  have hs := sV_ne_zero c
  rw [βmat_VV, βinv_VV, ← Pp_add_Pm] at hr
  have hp := congrArg (Pp * ·) hr
  have hm := congrArg (Pm * ·) hr
  simp only [Matrix.mul_sub, Matrix.mul_add, Matrix.mul_smul] at hp hm
  rw [Pp_mul_Pp, Pp_mul_Pm] at hp
  rw [Pm_mul_Pp, Pm_mul_Pm] at hm
  have e1 : (sV c - (sV c)⁻¹) • Pp = r • Pp := by
    rw [show r • Pp = r • (Pp + 0) by rw [add_zero], ← hp]; module
  have e2 : ((tV c)⁻¹ - tV c) • Pm = r • Pm := by
    rw [show r • Pm = r • (0 + Pm) by rw [zero_add], ← hm]; module
  have f1 := smul_left_injective ℂ Pp_ne_zero e1
  have f2 := smul_left_injective ℂ Pm_ne_zero e2
  have e : sV c - (sV c)⁻¹ = (tV c)⁻¹ - tV c := f1.trans f2.symm
  rw [tV_eq, inv_inv] at e
  have h8 : sV c ^ 8 = 1 := by
    field_simp at e
    linear_combination (exp := 1) (-(sV c ^ 2 + 1)) * e
  have he : Complex.exp ((2 * c) * (2 * Real.pi * Complex.I)) = 1 := by
    rw [← h8]; unfold sV; rw [← Complex.exp_nat_mul]; ring_nf
  obtain ⟨n, hn⟩ := Complex.exp_eq_one_iff.1 he
  have h2pi : (2 * Real.pi * Complex.I : ℂ) ≠ 0 := by
    simp [Real.pi_ne_zero, Complex.I_ne_zero]
  have hcn : c = ((n / 2 : ℚ) : ℂ) := by
    have := mul_right_cancel₀ h2pi hn
    push_cast
    linear_combination this / 2
  exact hc (hcn ▸ isAlgebraic_algebraMap (R := ℚ) (A := ℂ) ((n : ℚ) / 2))

end Unscaled

end QOU.KZ.Drinfeld
