import QOU.KZ.Drinfeld.Monoidal

/-!
# The braiding of `D_ℏ`: definition, inverse, equivariance, naturality

Stage S3 of bean `qou-zoyv`. `β_{X,Y} = reidx(swap) · exp(iπℏ t^{sl}_{X,Y})`, using the `sl₂`
block Casimir. The `𝔤𝔩₂` residue would differ by the scalar `½|X||Y|`, which depends on the
objects and would break naturality for maps between tensor powers of different lengths.

Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S3)
-/

noncomputable section

namespace QOU.KZ.Drinfeld

open CategoryTheory MonoidalCategory Finset QOU.KZ.FuchsianFormal QOU.KZ.BlockResidues
  QOU.KZ.KZPentagon Obj

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

/-- `exp(iπ M)`. -/
def expi {L : Type*} [Fintype L] [DecidableEq L] (M : EndL L) : EndL L :=
  NormedSpace.exp ℂ (((Real.pi : ℂ) * Complex.I) • M)

theorem expi_add {L : Type*} [Fintype L] [DecidableEq L] {M N : EndL L} (h : Commute M N) :
    expi (M + N) = expi M * expi N := by
  unfold expi; rw [smul_add]
  exact NormedSpace.exp_add_of_commute ((h.smul_left _).smul_right _)

theorem expi_mul_expi_neg {L : Type*} [Fintype L] [DecidableEq L] (M : EndL L) :
    expi M * expi (-M) = 1 := by
  rw [← expi_add (Commute.neg_right (Commute.refl M)), add_neg_cancel]
  simp [expi]

theorem expi_neg_mul_expi {L : Type*} [Fintype L] [DecidableEq L] (M : EndL L) :
    expi (-M) * expi M = 1 := by
  rw [← expi_add (Commute.neg_left (Commute.refl M)), neg_add_cancel]
  simp [expi]

theorem commute_expi {L : Type*} [Fintype L] [DecidableEq L] {X M : EndL L} (h : Commute X M) :
    Commute X (expi M) :=
  Commute.exp_right ℂ (h.smul_right _)

/-- The blocks of `X ⊗ Y`. -/
def bL (X Y : Obj) : Finset (Leaves (tensor X Y)) := univ.map Function.Embedding.inl
def bR (X Y : Obj) : Finset (Leaves (tensor X Y)) := univ.map Function.Embedding.inr

theorem disj_bLR (X Y : Obj) : Disjoint (bL X Y) (bR X Y) := by
  rw [Finset.disjoint_left]; intro k; rcases k with k | k <;> simp [bL, bR]

/-- The braiding legs `X ⊗ Y ≃ Y ⊗ X`. -/
def swapLegs (X Y : Obj) : Leaves (tensor X Y) ≃ Leaves (tensor Y X) := Equiv.sumComm _ _

variable (c : ℂ)

/-- The braiding matrix. -/
def βmat (X Y : Obj) : Matrix (Idx (tensor Y X)) (Idx (tensor X Y)) ℂ :=
  reidx (swapLegs X Y) * expi (c • tsl (bL X Y) (bR X Y))

/-- The inverse braiding matrix. -/
def βinv (X Y : Obj) : Matrix (Idx (tensor X Y)) (Idx (tensor Y X)) ℂ :=
  expi (-(c • tsl (bL X Y) (bR X Y))) * reidx (swapLegs X Y).symm

theorem βmat_mul_βinv (X Y : Obj) : βmat c X Y * βinv c X Y = 1 := by
  rw [βmat, βinv, Matrix.mul_assoc, ← Matrix.mul_assoc (expi _), expi_mul_expi_neg,
    Matrix.one_mul, reidx_mul, Equiv.symm_trans_self, reidx_refl]

theorem βinv_mul_βmat (X Y : Obj) : βinv c X Y * βmat c X Y = 1 := by
  rw [βmat, βinv, Matrix.mul_assoc, ← Matrix.mul_assoc (reidx _), reidx_mul,
    Equiv.self_trans_symm, reidx_refl, Matrix.one_mul, expi_neg_mul_expi]

theorem commute_diag_tsl {L : Type*} [Fintype L] [DecidableEq L] {S T : Finset L}
    (h : Disjoint S T) (a : Matrix (Fin 2) (Fin 2) ℂ) : Commute (diag L a) (tsl S T) := by
  have e : tsl S T = tB ℂ 2 S T - ((1 / 2 : ℂ) * (S.card * T.card : ℕ)) • 1 := by
    rw [tB_eq_tsl h]; abel
  rw [e]
  exact ((commute_tB_diag S T a).symm).sub_right ((Commute.one_right _).smul_right _)

theorem equivariant_βmat (X Y : Obj) : Equivariant (βmat c X Y) := by
  intro a _
  rw [ρ_eq_diag, ρ_eq_diag, βmat, ← Matrix.mul_assoc, ← reidx_diag, Matrix.mul_assoc,
    (commute_expi ((commute_diag_tsl (disj_bLR X Y) a).smul_right c)).eq, Matrix.mul_assoc]

theorem equivariant_βinv (X Y : Obj) : Equivariant (βinv c X Y) := by
  intro a _
  rw [ρ_eq_diag, ρ_eq_diag, βinv, ← Matrix.mul_assoc,
    (commute_expi ((commute_diag_tsl (disj_bLR X Y) a).smul_right c).neg_right).eq,
    Matrix.mul_assoc, Matrix.mul_assoc]
  congr 1
  exact (reidx_diag (swapLegs X Y).symm a).symm

theorem blk_bL (X Y : Obj) (a : Matrix (Fin 2) (Fin 2) ℂ) :
    blk (bL X Y) a = kron (ρ X a) (1 : EndL (Leaves Y)) := by
  rw [bL, blk_inl, blk_univ, ρ_eq_diag]

theorem blk_bR (X Y : Obj) (a : Matrix (Fin 2) (Fin 2) ℂ) :
    blk (bR X Y) a = kron (1 : EndL (Leaves X)) (ρ Y a) := by
  rw [bR, blk_inr, blk_univ, ρ_eq_diag]

theorem reidx_swap_kron {X₁ X₂ Y₁ Y₂ : Obj} (f : X₁ ⟶ Y₁) (g : X₂ ⟶ Y₂) :
    reidx (swapLegs Y₁ Y₂) * kron f.1 g.1 = kron g.1 f.1 * reidx (swapLegs X₁ X₂) := by
  ext y x
  rw [reidx_mul_apply, mul_reidx_apply]
  simp only [kron_apply, mul_comm]
  rfl

/-- **Naturality of the braiding** (matrix form). -/
theorem βmat_natural {X₁ X₂ Y₁ Y₂ : Obj} (f : X₁ ⟶ Y₁) (g : X₂ ⟶ Y₂) :
    βmat c Y₁ Y₂ * kron f.1 g.1 = kron g.1 f.1 * βmat c X₁ X₂ := by
  have hL : ∀ a, a.trace = 0 → kron f.1 g.1 * blk (bL X₁ X₂) a = blk (bL Y₁ Y₂) a * kron f.1 g.1 :=
    fun a ha => by
      rw [blk_bL, blk_bL, kron_mul, kron_mul, Matrix.mul_one, Matrix.one_mul, f.2 a ha]
  have hR : ∀ a, a.trace = 0 → kron f.1 g.1 * blk (bR X₁ X₂) a = blk (bR Y₁ Y₂) a * kron f.1 g.1 :=
    fun a ha => by
      rw [blk_bR, blk_bR, kron_mul, kron_mul, Matrix.mul_one, Matrix.one_mul, g.2 a ha]
  have ht := intertwine_tsl (kron f.1 g.1) hL hR
  have he : kron f.1 g.1 * expi (c • tsl (bL X₁ X₂) (bR X₁ X₂)) =
      expi (c • tsl (bL Y₁ Y₂) (bR Y₁ Y₂)) * kron f.1 g.1 :=
    KZIntertwine.exp_intertwine _ _ _ (by
      rw [Matrix.mul_smul, Matrix.mul_smul, Matrix.smul_mul, Matrix.smul_mul, ht])
  rw [βmat, βmat, Matrix.mul_assoc, ← he, ← Matrix.mul_assoc, reidx_swap_kron, Matrix.mul_assoc]

end QOU.KZ.Drinfeld
