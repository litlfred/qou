import Mathlib.Tactic
import Mathlib.LinearAlgebra.UnitaryGroup

open Matrix

theorem su2_emergence_dagger_unitarity
    (g : Matrix (Fin 2) (Fin 2) ℂ)
    (h_preserves_inner : ∀ x y : Fin 2 → ℂ, dotProduct (star (mulVec g x)) (mulVec g y) = dotProduct (star x) y) :
    g ∈ Matrix.unitaryGroup (Fin 2) ℂ := by
  rw [mem_unitaryGroup_iff']
  ext i j
  have h := h_preserves_inner (Pi.single i 1) (Pi.single j 1)
  fin_cases i <;> fin_cases j <;>
    revert h <;>
    simp [dotProduct, mulVec, Matrix.mul_apply, Pi.single, starRingEnd_apply, star] <;>
    intro h <;>
    exact h
