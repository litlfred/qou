import QOU.KZ.Drinfeld.Assoc
import QOU.KZ.KZIntertwine
import QOU.KZ.NonResonantInt

/-!
# Transporting `ΦB` along reindexing and whiskering

Stage S2 of bean `qou-zoyv`.

* `reidx_ΦB`: `reidx e · Φ(ℏt_{S,T}, ℏt_{T,U}) = Φ(ℏt_{eS,eT}, ℏt_{eT,eU}) · reidx e`, from
  `KZIntertwine.Φ_intertwine`. The block-diagonal residues are integer matrices, hence
  non-resonant for transcendental `ℏ`.
* `kron_ΦB_one`, `one_kron_ΦB`: whiskering maps `ΦB` to `ΦB` of the mapped blocks.
* `kron_reidx_one`, `one_kron_reidx`: whiskering a reindexing is a reindexing.

Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S2)
-/

noncomputable section

namespace QOU.KZ.Drinfeld

open Finset QOU.KZ.FuchsianFormal QOU.KZ.BlockResidues QOU.KZ.DrinfeldAssociator

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

variable (Ψ : Associator.{0}) {c : ℂ} (hc : Transcendental ℚ c)
include Ψ hc

variable {L L' : Type} [Fintype L] [DecidableEq L] [Fintype L'] [DecidableEq L']

theorem nonResonant_fromBlocks_tB (S T : Finset L) (S' T' : Finset L') :
    NonResonant (Matrix.fromBlocks (c • tB ℂ 2 S T) 0 0 (c • tB ℂ 2 S' T')) := by
  have e : Matrix.fromBlocks (c • tB ℂ 2 S T) 0 0 (c • tB ℂ 2 S' T') =
      c • (Matrix.fromBlocks (tBZ 2 S T) 0 0 (tBZ 2 S' T')).map (Int.cast : ℤ → ℂ) := by
    rw [tB_intCast, tB_intCast]
    ext (i | i) (j | j) <;> simp [RingHom.mapMatrix_apply]
  rw [e]
  exact NonResonantInt.nonResonant_smul_intMatrix _ c hc

theorem reidx_ΦB (e : L ≃ L') (S T U : Finset L) :
    reidx e * ΦB Ψ hc S T U =
      ΦB Ψ hc (S.map e.toEmbedding) (T.map e.toEmbedding) (U.map e.toEmbedding) * reidx e :=
  Ψ.ΦN_intertwine _ _ _ _ (reidx e)
    (by rw [Matrix.mul_smul, Matrix.smul_mul, reidx_tB])
    (by rw [Matrix.mul_smul, Matrix.smul_mul, reidx_tB])
    _ _ _ _ (nonResonant_fromBlocks_tB Ψ hc _ _ _ _) (nonResonant_fromBlocks_tB Ψ hc _ _ _ _)

theorem ΦB_congr {S T U S' T' U' : Finset L} (h1 : S = S') (h2 : T = T') (h3 : U = U') :
    ΦB Ψ hc S T U = ΦB Ψ hc S' T' U' := by
  subst h1 h2 h3; rfl

theorem kron_ΦB_one (S T U : Finset L) :
    kron (ΦB Ψ hc S T U) (1 : EndL L') =
      ΦB Ψ hc (S.map Function.Embedding.inl) (T.map Function.Embedding.inl)
        (U.map Function.Embedding.inl) := by
  unfold ΦB
  rw [kron_Φ_one Ψ _ _ _ _ (by rw [kron_smul_left, kron_tB_one]; exact nonResonant_tB Ψ hc _ _)
    (by rw [kron_smul_left, kron_tB_one]; exact nonResonant_tB Ψ hc _ _)]
  exact Ψ.ΦN_congr (by rw [kron_smul_left, kron_tB_one])
    (by rw [kron_smul_left, kron_tB_one]) _ _ _ _

theorem one_kron_ΦB (S T U : Finset L') :
    kron (1 : EndL L) (ΦB Ψ hc S T U) =
      ΦB Ψ hc (S.map Function.Embedding.inr) (T.map Function.Embedding.inr)
        (U.map Function.Embedding.inr) := by
  unfold ΦB
  rw [one_kron_Φ Ψ _ _ _ _ (by rw [kron_smul_right, one_kron_tB]; exact nonResonant_tB Ψ hc _ _)
    (by rw [kron_smul_right, one_kron_tB]; exact nonResonant_tB Ψ hc _ _)]
  exact Ψ.ΦN_congr (by rw [kron_smul_right, one_kron_tB])
    (by rw [kron_smul_right, one_kron_tB]) _ _ _ _

omit Ψ hc in
theorem kron_reidx_one {M : Type*} [Fintype M] [DecidableEq M] (e : L ≃ L') :
    kron (reidx e) (1 : EndL M) = reidx (Equiv.sumCongr e (Equiv.refl M)) := by
  ext y x
  simp only [kron_apply, reidx, Matrix.of_apply, Matrix.one_apply]
  by_cases h1 : x ∘ Sum.inl = (y ∘ Sum.inl) ∘ e
  · by_cases h2 : y ∘ Sum.inr = x ∘ Sum.inr
    · rw [if_pos h1, if_pos h2, one_mul, if_pos]
      funext k; rcases k with k | k
      · exact congrFun h1 k
      · exact (congrFun h2 k).symm
    · rw [if_neg h2, mul_zero, if_neg]
      intro h; apply h2; funext k; exact (congrFun h (Sum.inr k)).symm
  · rw [if_neg h1, zero_mul, if_neg]
    intro h; apply h1; funext k; exact congrFun h (Sum.inl k)

omit Ψ hc in
theorem one_kron_reidx {M : Type*} [Fintype M] [DecidableEq M] (e : L ≃ L') :
    kron (1 : EndL M) (reidx e) = reidx (Equiv.sumCongr (Equiv.refl M) e) := by
  ext y x
  simp only [kron_apply, reidx, Matrix.of_apply, Matrix.one_apply]
  by_cases h1 : x ∘ Sum.inr = (y ∘ Sum.inr) ∘ e
  · by_cases h2 : y ∘ Sum.inl = x ∘ Sum.inl
    · rw [if_pos h1, if_pos h2, one_mul, if_pos]
      funext k; rcases k with k | k
      · exact (congrFun h2 k).symm
      · exact congrFun h1 k
    · rw [if_neg h2, zero_mul, if_neg]
      intro h; apply h2; funext k; exact (congrFun h (Sum.inl k)).symm
  · rw [if_neg h1, mul_zero, if_neg]
    intro h; apply h1; funext k; exact congrFun h (Sum.inr k)

end QOU.KZ.Drinfeld
