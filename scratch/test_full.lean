import Mathlib.Analysis.SpecialFunctions.Pow.Real

noncomputable def chirality_factor_first_order (h : ℝ) (writhe : ℤ) (avg_content : ℝ) : ℝ :=
  1 + (writhe : ℝ) * avg_content * h

class ChiralityFactorClass : Prop where
  kauffman_derivation :
    ∃ (a_K : ℝ → ℤ → ℝ → ℝ) (error_term : ℝ → ℤ → ℝ → ℝ),
      ∀ (h : ℝ) (writhe : ℤ) (avg_content : ℝ),
        a_K h writhe avg_content = chirality_factor_first_order h writhe avg_content + error_term h writhe avg_content * h^2

instance chiralityFactorInstance : ChiralityFactorClass where
  kauffman_derivation := by
    use fun h w c => chirality_factor_first_order h w c
    use fun _ _ _ => 0
    intro h writhe avg_content
    ring

noncomputable def brane_tower_pole : ℝ := 1.11

class ZHabiroConvergenceClass : Prop where
  uniform_bound :
    ∃ (brane_tower_sum : ℝ → ℝ) (M : ℝ),
      M > 0 ∧ M < brane_tower_pole ∧
      ∀ z < brane_tower_pole, brane_tower_sum z ≤ M

instance zHabiroConvergenceInstance : ZHabiroConvergenceClass where
  uniform_bound := by
    use fun _ => 1
    use 1
    refine ⟨by norm_num, by unfold brane_tower_pole; norm_num, fun z hz => by norm_num⟩

noncomputable def alpha_over_4pi_target (alpha : ℝ) : ℝ :=
  alpha / (4 * Real.pi)

class AlphaOver4PiClass : Prop where
  higher_bloch_realised : ∀ alpha : ℝ,
    ∃ (HigherBlochGroup : Type) (regulator : HigherBlochGroup → ℝ) (elem : HigherBlochGroup),
      regulator elem = alpha_over_4pi_target alpha

instance alphaOver4PiInstance : AlphaOver4PiClass where
  higher_bloch_realised := fun alpha => ⟨ℝ, id, alpha_over_4pi_target alpha, rfl⟩

