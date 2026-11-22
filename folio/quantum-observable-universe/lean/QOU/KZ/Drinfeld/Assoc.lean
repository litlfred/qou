import QOU.KZ.Drinfeld.Whisker
import QOU.KZ.KZHexagonCentral

/-!
# The associator of `D_ℏ`

Stage S2 of bean `qou-zoyv`. For objects `X, Y, Z` the legs of `(X ⊗ Y) ⊗ Z` split into three
blocks `S_X, S_Y, S_Z`. The associator is

  `α_{X,Y,Z} = reidx(sumAssoc) · Φ_KZ(ℏ t_{S_X,S_Y}, ℏ t_{S_Y,S_Z})`

and its inverse is `Φ_KZ(ℏ t_{S_Y,S_Z}, ℏ t_{S_X,S_Y}) · reidx(sumAssoc)⁻¹`. Both are
`sl₂`-equivariant: `Φ` commutes with the diagonal action, because every block Casimir does, and
`reidx` intertwines it. Non-resonance holds for transcendental `ℏ`
(`BlockResidues.nonResonant_cast`).

Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S2)
-/

noncomputable section

namespace QOU.KZ.Drinfeld

open CategoryTheory Finset QOU.KZ.FuchsianFormal QOU.KZ.BlockResidues QOU.KZ.DrinfeldAssociator Obj

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

variable (Ψ : Associator.{0}) {c : ℂ} (hc : Transcendental ℚ c)
include Ψ hc

section Blocks

variable {L : Type} [Fintype L] [DecidableEq L]

theorem nonResonant_tB (S T : Finset L) : NonResonant (c • tB ℂ 2 S T) := by
  rw [tB_intCast]; exact nonResonant_cast hc _

omit Ψ hc in
theorem commute_smul_tB_diag (S T : Finset L) (a : Matrix (Fin 2) (Fin 2) ℂ) :
    Commute (diag L a) (c • tB ℂ 2 S T) :=
  ((commute_tB_diag S T a).symm).smul_right c

/-- `Φ(ℏ t_{S,T}, ℏ t_{T,U})` on `V^{⊗L}`. -/
def ΦB (S T U : Finset L) : EndL L :=
  Ψ.ΦN (c • tB ℂ 2 S T) (c • tB ℂ 2 T U) (nonResonant_tB Ψ hc S T) (nonResonant_tB Ψ hc T U)

theorem commute_diag_ΦB (S T U : Finset L) (a : Matrix (Fin 2) (Fin 2) ℂ) :
    Commute (diag L a) (ΦB Ψ hc S T U) :=
  Ψ.commute_ΦN _ _ (commute_smul_tB_diag S T a) (commute_smul_tB_diag T U a)

theorem ΦB_mul_ΦB_swap (S T U : Finset L) :
    ΦB Ψ hc S T U * Ψ.ΦN (c • tB ℂ 2 T U) (c • tB ℂ 2 S T) (nonResonant_tB Ψ hc T U)
      (nonResonant_tB Ψ hc S T) = 1 :=
  (Ψ.ΦN_swap_mul _ _ _ _).2

theorem ΦB_swap_mul_ΦB (S T U : Finset L) :
    Ψ.ΦN (c • tB ℂ 2 T U) (c • tB ℂ 2 S T) (nonResonant_tB Ψ hc T U) (nonResonant_tB Ψ hc S T) *
      ΦB Ψ hc S T U = 1 :=
  (Ψ.ΦN_swap_mul _ _ _ _).1

end Blocks

/-- The leg blocks of `(X ⊗ Y) ⊗ Z`. -/
def blkX (X Y Z : Obj) : Finset (Leaves (tensor (tensor X Y) Z)) :=
  (univ : Finset (Leaves X)).map (Function.Embedding.inl.trans Function.Embedding.inl)
def blkY (X Y Z : Obj) : Finset (Leaves (tensor (tensor X Y) Z)) :=
  (univ : Finset (Leaves Y)).map (Function.Embedding.inr.trans Function.Embedding.inl)
def blkZ (X Y Z : Obj) : Finset (Leaves (tensor (tensor X Y) Z)) :=
  (univ : Finset (Leaves Z)).map Function.Embedding.inr

/-- The leg bijection `(X ⊗ Y) ⊗ Z ≃ X ⊗ (Y ⊗ Z)`. -/
def assocLegs (X Y Z : Obj) : Leaves (tensor (tensor X Y) Z) ≃ Leaves (tensor X (tensor Y Z)) :=
  Equiv.sumAssoc _ _ _

/-- The associator matrix. -/
def αmat (X Y Z : Obj) :
    Matrix (Idx (tensor X (tensor Y Z))) (Idx (tensor (tensor X Y) Z)) ℂ :=
  reidx (assocLegs X Y Z) * ΦB Ψ hc (blkX X Y Z) (blkY X Y Z) (blkZ X Y Z)

/-- The inverse associator matrix. -/
def αinv (X Y Z : Obj) :
    Matrix (Idx (tensor (tensor X Y) Z)) (Idx (tensor X (tensor Y Z))) ℂ :=
  Ψ.ΦN (c • tB ℂ 2 (blkY X Y Z) (blkZ X Y Z)) (c • tB ℂ 2 (blkX X Y Z) (blkY X Y Z))
      (nonResonant_tB Ψ hc _ _) (nonResonant_tB Ψ hc _ _) * reidx (assocLegs X Y Z).symm

theorem αmat_mul_αinv (X Y Z : Obj) : αmat Ψ hc X Y Z * αinv Ψ hc X Y Z = 1 := by
  rw [αmat, αinv, Matrix.mul_assoc, ← Matrix.mul_assoc (ΦB Ψ hc _ _ _), ΦB_mul_ΦB_swap,
    Matrix.one_mul, reidx_mul, Equiv.symm_trans_self, reidx_refl]

theorem αinv_mul_αmat (X Y Z : Obj) : αinv Ψ hc X Y Z * αmat Ψ hc X Y Z = 1 := by
  rw [αmat, αinv, Matrix.mul_assoc, ← Matrix.mul_assoc (reidx _), reidx_mul,
    Equiv.self_trans_symm, reidx_refl, Matrix.one_mul, ΦB_swap_mul_ΦB]

theorem equivariant_αmat (X Y Z : Obj) : Equivariant (αmat Ψ hc X Y Z) := by
  intro a _
  rw [ρ_eq_diag, ρ_eq_diag, αmat, ← Matrix.mul_assoc, ← reidx_diag, Matrix.mul_assoc,
    (commute_diag_ΦB Ψ hc _ _ _ a).eq, Matrix.mul_assoc]

theorem equivariant_αinv (X Y Z : Obj) : Equivariant (αinv Ψ hc X Y Z) := by
  intro a _
  rw [ρ_eq_diag, ρ_eq_diag, αinv, ← Matrix.mul_assoc,
    (Ψ.commute_ΦN _ _ (commute_smul_tB_diag _ _ a)
      (commute_smul_tB_diag _ _ a)).eq, Matrix.mul_assoc, Matrix.mul_assoc]
  congr 1
  have := reidx_diag (assocLegs X Y Z).symm a
  exact this.symm

end QOU.KZ.Drinfeld
