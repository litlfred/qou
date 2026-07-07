import Mathlib.Tactic
import Mathlib.LinearAlgebra.UnitaryGroup

open Matrix

theorem su2_emergence_dagger_unitarity
    (g : Matrix (Fin 2) (Fin 2) ℂ)
    (h_preserves_inner : ∀ x y : Fin 2 → ℂ, dotProduct (star (g *v x)) (g *v y) = dotProduct (star x) y) :
    g ∈ Matrix.unitaryGroup (Fin 2) ℂ := by
  sorry
