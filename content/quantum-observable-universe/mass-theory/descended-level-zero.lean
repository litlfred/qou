import QOU.Basic

namespace QOU.Descent

class DescendedLevelZeroContext where
  desc_contrib : ℕ → ℝ

-- Ref: [manuscript] prop:descended-level-zero
theorem descended_level_zero [ctx : DescendedLevelZeroContext] :
    ∀ n : ℕ, 1 ≤ n → ctx.desc_contrib n = 0 := by
  sorry

end QOU.Descent
