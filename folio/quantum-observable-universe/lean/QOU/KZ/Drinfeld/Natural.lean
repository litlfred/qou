import QOU.KZ.Drinfeld.Casimir
import QOU.KZ.Drinfeld.Transport

/-!
# Naturality of the associator of `D_ℏ`

Stage S2 of bean `qou-zoyv`. For equivariant `f₁, f₂, f₃`:

  `α_{Y₁,Y₂,Y₃} · ((f₁ ⊗ f₂) ⊗ f₃) = (f₁ ⊗ (f₂ ⊗ f₃)) · α_{X₁,X₂,X₃}`.

The key point: the `sl₂` block Casimirs `t^{sl}_{S,T} = E^S F^T + F^S E^T + ½ H^S H^T` are
intertwined by tensor products of equivariant maps. They differ from the `𝔤𝔩₂` residues
`t_{S,T}` by the central scalar `½ |S||T|`, which shift invariance removes from `Φ`. Then
`KZIntertwine.Φ_intertwine` applies.

Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S2)
-/

noncomputable section

namespace QOU.KZ.Drinfeld

open CategoryTheory Finset QOU.KZ.FuchsianFormal QOU.KZ.BlockResidues QOU.KZ.DrinfeldAssociator Obj

variable {L : Type*} [Fintype L] [DecidableEq L]

/-- `a` acting diagonally on the legs in `S`. -/
def blk (S : Finset L) (a : Matrix (Fin 2) (Fin 2) ℂ) : Matrix (L → Fin 2) (L → Fin 2) ℂ :=
  ∑ i ∈ S, leafOp i a

/-- The `sl₂` block Casimir. -/
def tsl (S T : Finset L) : Matrix (L → Fin 2) (L → Fin 2) ℂ :=
  blk S eS * blk T fS + blk S fS * blk T eS + (1 / 2 : ℂ) • (blk S hS * blk T hS)

theorem tB_eq_tsl {S T : Finset L} (h : Disjoint S T) :
    tB ℂ 2 S T = tsl S T + ((1 / 2 : ℂ) * (S.card * T.card : ℕ)) • 1 := by
  have hne : ∀ i ∈ S, ∀ j ∈ T, i ≠ j := fun i hi j hj e =>
    Finset.disjoint_left.1 h hi (e ▸ hj)
  rw [tB, Finset.sum_congr rfl fun i hi => Finset.sum_congr rfl fun j hj =>
    flip_eq_casimir (hne i hi j hj)]
  simp only [Finset.sum_add_distrib]
  rw [tsl, blk, blk, blk, blk, blk, blk, Finset.sum_mul_sum, Finset.sum_mul_sum, Finset.sum_mul_sum,
    Finset.smul_sum]
  simp only [Finset.smul_sum]
  congr 1
  simp only [Finset.sum_const, ← Nat.cast_smul_eq_nsmul ℂ, smul_smul]
  congr 1
  push_cast; ring

section Blk

variable {L' : Type*} [Fintype L'] [DecidableEq L']

theorem blk_inl (S : Finset L) (a : Matrix (Fin 2) (Fin 2) ℂ) :
    blk (S.map (Function.Embedding.inl : L ↪ L ⊕ L')) a = kron (blk S a) (1 : EndL L') := by
  rw [blk, Finset.sum_map, blk, kron_sum_left]
  exact Finset.sum_congr rfl fun i _ => leafOp_inl i a

theorem blk_inr (S : Finset L') (a : Matrix (Fin 2) (Fin 2) ℂ) :
    blk (S.map (Function.Embedding.inr : L' ↪ L ⊕ L')) a = kron (1 : EndL L) (blk S a) := by
  rw [blk, Finset.sum_map, blk, kron_sum_right]
  exact Finset.sum_congr rfl fun i _ => leafOp_inr i a

theorem blk_univ (a : Matrix (Fin 2) (Fin 2) ℂ) : blk (univ : Finset L) a = diag L a := rfl

end Blk

theorem blk_blkX (X Y Z : Obj) (a : Matrix (Fin 2) (Fin 2) ℂ) :
    blk (blkX X Y Z) a = kron (kron (ρ X a) (1 : EndL (Leaves Y))) (1 : EndL (Leaves Z)) := by
  rw [blkX, ← Finset.map_map, blk_inl, blk_inl, blk_univ, ρ_eq_diag]

theorem blk_blkY (X Y Z : Obj) (a : Matrix (Fin 2) (Fin 2) ℂ) :
    blk (blkY X Y Z) a = kron (kron (1 : EndL (Leaves X)) (ρ Y a)) (1 : EndL (Leaves Z)) := by
  rw [blkY, ← Finset.map_map, blk_inl, blk_inr, blk_univ, ρ_eq_diag]

theorem blk_blkZ (X Y Z : Obj) (a : Matrix (Fin 2) (Fin 2) ℂ) :
    blk (blkZ X Y Z) a = kron (1 : EndL (Leaves (tensor X Y))) (ρ Z a) := by
  rw [blkZ, blk_inr, blk_univ, ρ_eq_diag]

/-- Intertwining the `sl₂` block Casimir. -/
theorem intertwine_tsl {L L' : Type*} [Fintype L] [DecidableEq L] [Fintype L'] [DecidableEq L']
    (M : Matrix (L' → Fin 2) (L → Fin 2) ℂ) {S T : Finset L} {S' T' : Finset L'}
    (hS : ∀ a, a.trace = 0 → M * blk S a = blk S' a * M)
    (hT : ∀ a, a.trace = 0 → M * blk T a = blk T' a * M) :
    M * tsl S T = tsl S' T' * M := by
  have k : ∀ a b, a.trace = 0 → b.trace = 0 →
      M * (blk S a * blk T b) = blk S' a * blk T' b * M := fun a b ha hb => by
    rw [← Matrix.mul_assoc, hS a ha, Matrix.mul_assoc, hT b hb, Matrix.mul_assoc]
  rw [tsl, tsl, Matrix.mul_add, Matrix.mul_add, Matrix.mul_smul, k _ _ trace_eS trace_fS,
    k _ _ trace_fS trace_eS, k _ _ trace_hS trace_hS, Matrix.add_mul, Matrix.add_mul,
    Matrix.smul_mul]

section Tensor3

variable {X₁ X₂ X₃ Y₁ Y₂ Y₃ : Obj} (f₁ : X₁ ⟶ Y₁) (f₂ : X₂ ⟶ Y₂) (f₃ : X₃ ⟶ Y₃)

/-- `(f₁ ⊗ f₂) ⊗ f₃` as a matrix. -/
abbrev T3 : Matrix (Idx (tensor (tensor Y₁ Y₂) Y₃)) (Idx (tensor (tensor X₁ X₂) X₃)) ℂ :=
  kron (kron f₁.1 f₂.1) f₃.1

theorem T3_blkX (a : Matrix (Fin 2) (Fin 2) ℂ) (ha : a.trace = 0) :
    T3 f₁ f₂ f₃ * blk (blkX X₁ X₂ X₃) a = blk (blkX Y₁ Y₂ Y₃) a * T3 f₁ f₂ f₃ := by
  rw [blk_blkX, blk_blkX, T3, kron_mul, kron_mul, kron_mul, kron_mul, Matrix.mul_one,
    Matrix.mul_one, Matrix.one_mul, Matrix.one_mul, f₁.2 a ha]

theorem T3_blkY (a : Matrix (Fin 2) (Fin 2) ℂ) (ha : a.trace = 0) :
    T3 f₁ f₂ f₃ * blk (blkY X₁ X₂ X₃) a = blk (blkY Y₁ Y₂ Y₃) a * T3 f₁ f₂ f₃ := by
  rw [blk_blkY, blk_blkY, T3, kron_mul, kron_mul, kron_mul, kron_mul, Matrix.mul_one,
    Matrix.mul_one, Matrix.one_mul, Matrix.one_mul, f₂.2 a ha]

theorem T3_blkZ (a : Matrix (Fin 2) (Fin 2) ℂ) (ha : a.trace = 0) :
    T3 f₁ f₂ f₃ * blk (blkZ X₁ X₂ X₃) a = blk (blkZ Y₁ Y₂ Y₃) a * T3 f₁ f₂ f₃ := by
  rw [blk_blkZ, blk_blkZ, T3, kron_mul, kron_mul, Matrix.mul_one, Matrix.one_mul, f₃.2 a ha]

end Tensor3

section Shift

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

variable (Ψ : Associator.{0}) {c : ℂ} (hc : Transcendental ℚ c)
include Ψ hc

omit Ψ in
theorem transcendental_half : Transcendental ℚ (c / 2) := by
  intro h
  apply hc
  have := h.mul (isAlgebraic_algebraMap (R := ℚ) (A := ℂ) (2 : ℚ))
  rwa [show c / 2 * algebraMap ℚ ℂ 2 = c by simp] at this

variable {L L' : Type} [Fintype L] [DecidableEq L] [Fintype L'] [DecidableEq L']

omit Ψ hc in
theorem smul_tsl_eq {S T : Finset L} (h : Disjoint S T) :
    c • tsl S T = (c / 2) • (Int.castRingHom ℂ).mapMatrix
      ((2 : ℤ) • tBZ 2 S T - ((S.card * T.card : ℕ) : ℤ) • 1) := by
  have e : tsl S T = tB ℂ 2 S T - ((1 / 2 : ℂ) * (S.card * T.card : ℕ)) • 1 := by
    rw [tB_eq_tsl h]; abel
  rw [e, tB_intCast]
  ext i j
  simp only [Matrix.smul_apply, Matrix.sub_apply, RingHom.mapMatrix_apply, Matrix.map_apply,
    Matrix.one_apply, smul_eq_mul]
  split_ifs <;> simp only [eq_intCast] <;> push_cast <;> ring

theorem nonResonant_tsl {S T : Finset L} (h : Disjoint S T) : NonResonant (c • tsl S T) := by
  rw [smul_tsl_eq h]
  exact NonResonantInt.nonResonant_smul_intMatrix _ _ (transcendental_half hc)

theorem nonResonant_fromBlocks_tsl {S T : Finset L} {S' T' : Finset L'} (h : Disjoint S T)
    (h' : Disjoint S' T') :
    NonResonant (Matrix.fromBlocks (c • tsl S T) 0 0 (c • tsl S' T')) := by
  rw [smul_tsl_eq h, smul_tsl_eq h']
  have e : Matrix.fromBlocks ((c / 2) • (Int.castRingHom ℂ).mapMatrix
      ((2 : ℤ) • tBZ 2 S T - ((S.card * T.card : ℕ) : ℤ) • 1)) 0 0
      ((c / 2) • (Int.castRingHom ℂ).mapMatrix
      ((2 : ℤ) • tBZ 2 S' T' - ((S'.card * T'.card : ℕ) : ℤ) • 1)) =
      (c / 2) • (Matrix.fromBlocks ((2 : ℤ) • tBZ 2 S T - ((S.card * T.card : ℕ) : ℤ) • 1) 0 0
        ((2 : ℤ) • tBZ 2 S' T' - ((S'.card * T'.card : ℕ) : ℤ) • 1)).map (Int.cast : ℤ → ℂ) := by
    ext (i | i) (j | j) <;> simp [RingHom.mapMatrix_apply]
  rw [e]
  exact NonResonantInt.nonResonant_smul_intMatrix _ _ (transcendental_half hc)

omit Ψ hc in
theorem commute_scalar (r : ℂ) (X : EndL L) : Commute (r • (1 : EndL L)) X :=
  (Commute.one_left X).smul_left r

/-- `ΦB` computed with the `sl₂` residues. -/
theorem ΦB_eq_sl {S T U : Finset L} (hST : Disjoint S T) (hTU : Disjoint T U) :
    ΦB Ψ hc S T U = Ψ.ΦN (c • tsl S T) (c • tsl T U) (nonResonant_tsl Ψ hc hST)
      (nonResonant_tsl Ψ hc hTU) := by
  set z₁ : EndL L := (c * ((1 / 2 : ℂ) * (S.card * T.card : ℕ))) • 1
  set z₂ : EndL L := (c * ((1 / 2 : ℂ) * (T.card * U.card : ℕ))) • 1
  have e₁ : c • tB ℂ 2 S T = c • tsl S T + z₁ := by
    rw [tB_eq_tsl hST, smul_add, smul_smul]
  have e₂ : c • tB ℂ 2 T U = c • tsl T U + z₂ := by
    rw [tB_eq_tsl hTU, smul_add, smul_smul]
  have hB' : NonResonant (c • tsl T U + z₂) := e₂ ▸ nonResonant_tB Ψ hc T U
  have hA' : NonResonant (c • tsl S T + z₁) := e₁ ▸ nonResonant_tB Ψ hc S T
  rw [ΦB, Ψ.ΦN_congr e₁ e₂ _ _ hA' hB',
    Ψ.ΦN_shift_left _ _ z₁ (nonResonant_tsl Ψ hc hST) hB' hA' (commute_scalar _ _)
      (commute_scalar _ _),
    Ψ.ΦN_shift_right _ _ z₂ (nonResonant_tsl Ψ hc hST) (nonResonant_tsl Ψ hc hTU) hB'
      (commute_scalar _ _) (commute_scalar _ _)]

end Shift

theorem disj_blkXY (X Y Z : Obj) : Disjoint (blkX X Y Z) (blkY X Y Z) := by
  rw [Finset.disjoint_left]; intro k; rcases k with (k | k) | k <;> simp [blkX, blkY]

theorem disj_blkYZ (X Y Z : Obj) : Disjoint (blkY X Y Z) (blkZ X Y Z) := by
  rw [Finset.disjoint_left]; intro k; rcases k with (k | k) | k <;> simp [blkY, blkZ]

theorem reidx_T3 {X₁ X₂ X₃ Y₁ Y₂ Y₃ : Obj} (f₁ : X₁ ⟶ Y₁) (f₂ : X₂ ⟶ Y₂) (f₃ : X₃ ⟶ Y₃) :
    reidx (assocLegs Y₁ Y₂ Y₃) * T3 f₁ f₂ f₃ =
      kron f₁.1 (kron f₂.1 f₃.1) * reidx (assocLegs X₁ X₂ X₃) := by
  ext y x
  rw [reidx_mul_apply, mul_reidx_apply]
  simp only [T3, kron_apply, mul_assoc]
  rfl

section Nat

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

variable (Ψ : Associator.{0}) {c : ℂ} (hc : Transcendental ℚ c)
include Ψ hc

/-- **Naturality of the associator** (matrix form). -/
theorem natural_mat {X₁ X₂ X₃ Y₁ Y₂ Y₃ : Obj} (f₁ : X₁ ⟶ Y₁) (f₂ : X₂ ⟶ Y₂) (f₃ : X₃ ⟶ Y₃) :
    αmat Ψ hc Y₁ Y₂ Y₃ * T3 f₁ f₂ f₃ = kron f₁.1 (kron f₂.1 f₃.1) * αmat Ψ hc X₁ X₂ X₃ := by
  have hA : T3 f₁ f₂ f₃ * (c • tsl (blkX X₁ X₂ X₃) (blkY X₁ X₂ X₃)) =
      (c • tsl (blkX Y₁ Y₂ Y₃) (blkY Y₁ Y₂ Y₃)) * T3 f₁ f₂ f₃ := by
    rw [Matrix.mul_smul, Matrix.smul_mul,
      intertwine_tsl _ (T3_blkX f₁ f₂ f₃) (T3_blkY f₁ f₂ f₃)]
  have hB : T3 f₁ f₂ f₃ * (c • tsl (blkY X₁ X₂ X₃) (blkZ X₁ X₂ X₃)) =
      (c • tsl (blkY Y₁ Y₂ Y₃) (blkZ Y₁ Y₂ Y₃)) * T3 f₁ f₂ f₃ := by
    rw [Matrix.mul_smul, Matrix.smul_mul,
      intertwine_tsl _ (T3_blkY f₁ f₂ f₃) (T3_blkZ f₁ f₂ f₃)]
  have hΦ := Ψ.ΦN_intertwine _ _ _ _ (T3 f₁ f₂ f₃) hA hB
    (nonResonant_tsl Ψ hc (disj_blkXY X₁ X₂ X₃)) (nonResonant_tsl Ψ hc (disj_blkYZ X₁ X₂ X₃))
    (nonResonant_tsl Ψ hc (disj_blkXY Y₁ Y₂ Y₃)) (nonResonant_tsl Ψ hc (disj_blkYZ Y₁ Y₂ Y₃))
    (nonResonant_fromBlocks_tsl Ψ hc (disj_blkXY _ _ _) (disj_blkXY _ _ _))
    (nonResonant_fromBlocks_tsl Ψ hc (disj_blkYZ _ _ _) (disj_blkYZ _ _ _))
  rw [αmat, αmat, ΦB_eq_sl Ψ hc (disj_blkXY _ _ _) (disj_blkYZ _ _ _),
    ΦB_eq_sl Ψ hc (disj_blkXY _ _ _) (disj_blkYZ _ _ _), Matrix.mul_assoc, ← hΦ,
    ← Matrix.mul_assoc, reidx_T3, Matrix.mul_assoc]

end Nat

end QOU.KZ.Drinfeld
