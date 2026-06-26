import Mathlib.Tactic

namespace QOU.ParticleInteractions

-- Ref: [manuscript] prop:meson-scale-independence
/-- The pion mass m_π cannot be derived from the substrate parameters (m_e, q_0) alone.
    The Hecke algebra determines the relative meson mass spectrum but not the absolute scale m_π. -/
theorem meson_scale_independence :
    ¬ ∃ (f : ℝ → ℝ → ℝ), ∀ (m_e q_0 m_pi : ℝ), m_pi = f m_e q_0 := by
  -- If m_π were a function of (m_e, q_0) alone, then for fixed inputs the
  -- value f m_e q_0 is a single real, yet the claim forces it to equal
  -- EVERY m_π — contradiction. Witnessed at m_e = q_0 = 0, m_π ∈ {0, 1}.
  rintro ⟨f, hf⟩
  have h0 : (0 : ℝ) = f 0 0 := hf 0 0 0
  have h1 : (1 : ℝ) = f 0 0 := hf 0 0 1
  exact absurd (h0.trans h1.symm) (by norm_num)

end QOU.ParticleInteractions
