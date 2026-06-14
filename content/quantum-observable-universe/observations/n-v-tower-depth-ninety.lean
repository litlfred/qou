import Mathlib.Data.Real.Basic

/-!
# QOU.Observations.n_v_tower_depth_ninety

Brane-tower depth from m_e to v equals 90
-/

namespace QOU.Observations

-- Abstract classes for the categorical structure
class GBCategory (C : Type*)
class BraneTower {C : Type*} [GBCategory C] (tower : C → Type*)
def tower_depth {C : Type*} [GBCategory C] {tower : C → Type*} [BraneTower tower] (A B : C) : ℕ := sorry

/-- **CONJECTURE.** The Coxeter-length tower depth between the m_e level and the
    v level equals 90 Hecke generations. -/
theorem tower_depth_m_e_to_v_is_ninety
    {C : Type*} [GBCategory C] {tower : C → Type*} [BraneTower tower]
    (level_m_e level_v : C) :
    tower_depth level_m_e level_v = 90 := by
  -- Ref: [manuscript] conj:n-v-tower-depth-ninety
  sorry

end QOU.Observations
