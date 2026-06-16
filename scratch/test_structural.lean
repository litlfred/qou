import Mathlib.Analysis.SpecialFunctions.Pow.Real

namespace Test

noncomputable def chirality_factor_first_order (h : ℝ) (writhe : ℤ) (avg_content : ℝ) : ℝ :=
  1 + (writhe : ℝ) * avg_content * h

class ChiralityFactorClass : Prop where
  kauffman_derivation :
    ∃ (a_K : ℝ → ℤ → ℝ) (error_term : ℝ → ℤ → ℝ),
      ∀ (h : ℝ) (writhe : ℤ) (avg_content : ℝ),
        a_K h writhe = chirality_factor_first_order h writhe avg_content + error_term h writhe * h^2

noncomputable def brane_tower_pole : ℝ := 1.11

class ZHabiroConvergenceClass : Prop where
  uniform_bound :
    ∃ (brane_tower_sum : ℝ → ℝ) (M : ℝ),
      M > 0 ∧ M < brane_tower_pole ∧
      ∀ z < brane_tower_pole, brane_tower_sum z ≤ M

noncomputable def alpha_over_4pi_target (alpha : ℝ) : ℝ :=
  alpha / (4 * Real.pi)

class AlphaOver4PiClass : Prop where
  higher_bloch_realised :
    ∃ (HigherBlochGroup : Type) (regulator : HigherBlochGroup → ℝ) (elem : HigherBlochGroup),
      ∀ alpha : ℝ, regulator elem = alpha_over_4pi_target alpha

end Test
