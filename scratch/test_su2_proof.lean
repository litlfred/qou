import Mathlib.Tactic
import Mathlib.LinearAlgebra.UnitaryGroup

open Matrix

theorem su2_emergence_dagger_unitarity
    (g : Matrix (Fin 2) (Fin 2) ℂ)
    (h_preserves_inner : ∀ x y : Fin 2 → ℂ, dotProduct (star (g *v x)) (g *v y) = dotProduct (star x) y) :
    g ∈ Matrix.unitaryGroup (Fin 2) ℂ := by
  rw [mem_unitaryGroup_iff]
  have h1 : ∀ x y : Fin 2 → ℂ, dotProduct (star x) ((gᴴ * g) *v y) = dotProduct (star x) y := by
    intro x y
    rw [← Matrix.mulVec_mulVec]
    -- wait, `dotProduct (star x) (A *v y) = dotProduct (star (Aᴴ *v x)) y` 
    -- so `dotProduct (star x) (gᴴ *v (g *v y)) = dotProduct (star (g *v x)) (g *v y)`
    sorry
  sorry
