import Mathlib.Tactic
import Mathlib.LinearAlgebra.UnitaryGroup

open Matrix

theorem su2_emergence_dagger_unitarity
    (g : Matrix (Fin 2) (Fin 2) ℂ)
    (h_preserves_inner : ∀ x y : Fin 2 → ℂ, dotProduct (star (mulVec g x)) (mulVec g y) = dotProduct (star x) y) :
    g ∈ Matrix.unitaryGroup (Fin 2) ℂ := by
  rw [mem_unitaryGroup_iff]
  ext i j
  have h := h_preserves_inner (Pi.single i 1) (Pi.single j 1)
  have h_dot2 : dotProduct (star (Pi.single i 1 : Fin 2 → ℂ)) (Pi.single j 1) = (1 : Matrix (Fin 2) (Fin 2) ℂ) i j := by
    fin_cases i <;> fin_cases j <;> rfl
  have h_dot1 : dotProduct (star (mulVec g (Pi.single i 1))) (mulVec g (Pi.single j 1)) = (star g * g) i j := by
    fin_cases i <;> fin_cases j <;>
      simp [dotProduct, mulVec, Matrix.mul_apply, Pi.single, starRingEnd_apply, star] <;>
      ring
  rw [h_dot1, h_dot2] at h
  exact h
