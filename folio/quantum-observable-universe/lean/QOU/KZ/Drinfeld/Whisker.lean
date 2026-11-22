import QOU.KZ.Drinfeld.Reindex
import QOU.KZ.DrinfeldAssociator
import Mathlib.Analysis.Matrix

/-!
# Whiskering: `X ↦ X ⊗ 1` and `X ↦ 1 ⊗ X` carry the KZ associator to the KZ associator

Stage S2 of bean `qou-zoyv`.

* The leg embeddings `inl`, `inr` turn flips into flips: `P_{ij} ⊗ 1 = P_{inl i, inl j}`
  (`kron_flip_one`), and similarly block Casimirs (`kron_tB_one`, `one_kron_tB`).
* `X ↦ X ⊗ 1` and `X ↦ 1 ⊗ X` are continuous `ℂ`-algebra maps (`whL`, `whR`). By
  `KZFunctorial.map_Φ` they carry `Φ(A, B)` to `Φ(A ⊗ 1, B ⊗ 1)` (`kron_Φ_one`, `one_kron_Φ`).

Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S2)
-/

noncomputable section

namespace QOU.KZ.Drinfeld

open Finset QOU.KZ.FuchsianFormal QOU.KZ.BlockResidues QOU.KZ.DrinfeldAssociator

universe u

variable {L L' : Type u} [Fintype L] [DecidableEq L] [Fintype L'] [DecidableEq L']

theorem swap_inl_apply (i j : L) (k : L ⊕ L') :
    Equiv.swap (Sum.inl i : L ⊕ L') (Sum.inl j) k = Sum.map (Equiv.swap i j) id k := by
  rcases k with k | k
  · exact (Sum.inl_injective.swap_apply i j k)
  · rw [Equiv.swap_apply_of_ne_of_ne (by simp) (by simp)]; rfl

theorem swap_inr_apply (i j : L') (k : L ⊕ L') :
    Equiv.swap (Sum.inr i : L ⊕ L') (Sum.inr j) k = Sum.map id (Equiv.swap i j) k := by
  rcases k with k | k
  · rw [Equiv.swap_apply_of_ne_of_ne (by simp) (by simp)]; rfl
  · exact (Sum.inr_injective.swap_apply i j k)

theorem kron_flip_one (i j : L) :
    kron (flipL ℂ 2 i j) (1 : Matrix (L' → Fin 2) (L' → Fin 2) ℂ) =
      flipL ℂ 2 (Sum.inl i : L ⊕ L') (Sum.inl j) := by
  ext y x
  simp only [kron_apply, flipL, permL, permMat, Matrix.of_apply, Matrix.one_apply]
  by_cases h1 : (x ∘ Sum.inl) ∘ Equiv.swap i j = y ∘ Sum.inl
  · by_cases h2 : y ∘ Sum.inr = x ∘ Sum.inr
    · rw [if_pos h1, if_pos h2, one_mul, if_pos]
      funext k; rcases k with k | k
      · simpa [swap_inl_apply] using congrFun h1 k
      · simpa [swap_inl_apply] using (congrFun h2 k).symm
    · rw [if_neg h2, mul_zero, if_neg]
      intro h; apply h2; funext k; have := congrFun h (Sum.inr k)
      simpa [swap_inl_apply] using this.symm
  · rw [if_neg h1, zero_mul, if_neg]
    intro h; apply h1; funext k; have := congrFun h (Sum.inl k)
    simpa [swap_inl_apply] using this

theorem one_kron_flip (i j : L') :
    kron (1 : Matrix (L → Fin 2) (L → Fin 2) ℂ) (flipL ℂ 2 i j) =
      flipL ℂ 2 (Sum.inr i : L ⊕ L') (Sum.inr j) := by
  ext y x
  simp only [kron_apply, flipL, permL, permMat, Matrix.of_apply, Matrix.one_apply]
  by_cases h1 : (x ∘ Sum.inr) ∘ Equiv.swap i j = y ∘ Sum.inr
  · by_cases h2 : y ∘ Sum.inl = x ∘ Sum.inl
    · rw [if_pos h1, if_pos h2, one_mul, if_pos]
      funext k; rcases k with k | k
      · simpa [swap_inr_apply] using (congrFun h2 k).symm
      · simpa [swap_inr_apply] using congrFun h1 k
    · rw [if_neg h2, zero_mul, if_neg]
      intro h; apply h2; funext k; have := congrFun h (Sum.inl k)
      simpa [swap_inr_apply] using this.symm
  · rw [if_neg h1, mul_zero, if_neg]
    intro h; apply h1; funext k; have := congrFun h (Sum.inr k)
    simpa [swap_inr_apply] using this

theorem kron_add_left {α β α' β' : Type*} (f g : Matrix (α → Fin 2) (β → Fin 2) ℂ)
    (h : Matrix (α' → Fin 2) (β' → Fin 2) ℂ) : kron (f + g) h = kron f h + kron g h := by
  ext y x; simp [kron_apply, add_mul]

theorem kron_add_right {α β α' β' : Type*} (f : Matrix (α → Fin 2) (β → Fin 2) ℂ)
    (g h : Matrix (α' → Fin 2) (β' → Fin 2) ℂ) : kron f (g + h) = kron f g + kron f h := by
  ext y x; simp [kron_apply, mul_add]

theorem kron_smul_left {α β α' β' : Type*} (c : ℂ) (f : Matrix (α → Fin 2) (β → Fin 2) ℂ)
    (h : Matrix (α' → Fin 2) (β' → Fin 2) ℂ) : kron (c • f) h = c • kron f h := by
  ext y x; simp [kron_apply, mul_assoc]

theorem kron_smul_right {α β α' β' : Type*} (c : ℂ) (f : Matrix (α → Fin 2) (β → Fin 2) ℂ)
    (h : Matrix (α' → Fin 2) (β' → Fin 2) ℂ) : kron f (c • h) = c • kron f h := by
  ext y x; simp [kron_apply, mul_left_comm]

theorem kron_tB_one (S T : Finset L) :
    kron (tB ℂ 2 S T) (1 : Matrix (L' → Fin 2) (L' → Fin 2) ℂ) =
      tB ℂ 2 (S.map Function.Embedding.inl) (T.map Function.Embedding.inl) := by
  simp only [tB, kron_sum_left, kron_flip_one, Finset.sum_map]
  rfl

theorem one_kron_tB (S T : Finset L') :
    kron (1 : Matrix (L → Fin 2) (L → Fin 2) ℂ) (tB ℂ 2 S T) =
      tB ℂ 2 (S.map Function.Embedding.inr) (T.map Function.Embedding.inr) := by
  simp only [tB, kron_sum_right, one_kron_flip, Finset.sum_map]
  rfl

section Normed

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

/-- `End(V^{⊗L})` as a normed ring (operator `ℓ^∞` norm). -/
abbrev EndL (L : Type*) [Fintype L] [DecidableEq L] := Matrix (L → Fin 2) (L → Fin 2) ℂ

variable (L L')

/-- `X ↦ X ⊗ 1` as a `ℂ`-algebra map (stated with the normed-ring instances). -/
def whL : @AlgHom ℂ (EndL L) (EndL (L ⊕ L')) _
    (NormedRing.toRing (α := EndL L)).toSemiring (NormedRing.toRing (α := EndL (L ⊕ L'))).toSemiring
    (NormedAlgebra.toAlgebra (𝕜 := ℂ) (𝕜' := EndL L))
    (NormedAlgebra.toAlgebra (𝕜 := ℂ) (𝕜' := EndL (L ⊕ L'))) where
  toFun X := kron X 1
  map_one' := kron_one
  map_mul' X Y := by
    show kron (X * Y) 1 = kron X 1 * kron Y 1
    rw [kron_mul, Matrix.one_mul]
  map_zero' := by ext; simp [kron_apply]
  map_add' X Y := kron_add_left X Y 1
  commutes' r := by
    show kron (algebraMap ℂ (EndL L) r) 1 = algebraMap ℂ (EndL (L ⊕ L')) r
    rw [Algebra.algebraMap_eq_smul_one, Algebra.algebraMap_eq_smul_one, kron_smul_left, kron_one]

/-- `X ↦ 1 ⊗ X` as a `ℂ`-algebra map. -/
def whR : @AlgHom ℂ (EndL L') (EndL (L ⊕ L')) _
    (NormedRing.toRing (α := EndL L')).toSemiring (NormedRing.toRing (α := EndL (L ⊕ L'))).toSemiring
    (NormedAlgebra.toAlgebra (𝕜 := ℂ) (𝕜' := EndL L'))
    (NormedAlgebra.toAlgebra (𝕜 := ℂ) (𝕜' := EndL (L ⊕ L'))) where
  toFun X := kron 1 X
  map_one' := kron_one
  map_mul' X Y := by
    show kron 1 (X * Y) = kron 1 X * kron 1 Y
    rw [kron_mul, Matrix.one_mul]
  map_zero' := by ext; simp [kron_apply]
  map_add' X Y := kron_add_right 1 X Y
  commutes' r := by
    show kron 1 (algebraMap ℂ (EndL L') r) = algebraMap ℂ (EndL (L ⊕ L')) r
    rw [Algebra.algebraMap_eq_smul_one, Algebra.algebraMap_eq_smul_one, kron_smul_right, kron_one]

variable {L L'} (Ψ : Associator.{u})

/-- `Φ(A, B) ⊗ 1 = Φ(A ⊗ 1, B ⊗ 1)`. -/
theorem kron_Φ_one (A B : EndL L) (hA : NonResonant A) (hB : NonResonant B)
    (hA' : NonResonant (kron A (1 : EndL L'))) (hB' : NonResonant (kron B (1 : EndL L'))) :
    kron (Ψ.ΦN A B hA hB) (1 : EndL L') = Ψ.ΦN (kron A 1) (kron B 1) hA' hB' :=
  Ψ.map_ΦN (whL L L') (LinearMap.continuous_of_finiteDimensional (whL L L').toLinearMap)
    A B hA hB hA' hB'

/-- `1 ⊗ Φ(A, B) = Φ(1 ⊗ A, 1 ⊗ B)`. -/
theorem one_kron_Φ (A B : EndL L') (hA : NonResonant A) (hB : NonResonant B)
    (hA' : NonResonant (kron (1 : EndL L) A)) (hB' : NonResonant (kron (1 : EndL L) B)) :
    kron (1 : EndL L) (Ψ.ΦN A B hA hB) = Ψ.ΦN (kron 1 A) (kron 1 B) hA' hB' :=
  Ψ.map_ΦN (whR L L') (LinearMap.continuous_of_finiteDimensional (whR L L').toLinearMap)
    A B hA hB hA' hB'

end Normed

end QOU.KZ.Drinfeld
