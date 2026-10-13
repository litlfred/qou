import QOU.KZ.Drinfeld.Twist
import QOU.KZ.Drinfeld.Linear
import QOU.KZ.Drinfeld.Duals
import QOU.MathlibExt.RibbonHeckeDimension

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

end QOU.KZ.Drinfeld
