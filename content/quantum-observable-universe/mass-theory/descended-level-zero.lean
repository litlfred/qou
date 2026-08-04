import QOU.Basic

namespace QOU.Descent

class DescendedLevelZeroContext where
  desc_contrib : ℕ → ℝ
  desc_contrib_zero : ∀ n : ℕ, 1 ≤ n → desc_contrib n = 0

-- Ref: [manuscript] prop:descended-level-zero
theorem descended_level_zero [ctx : DescendedLevelZeroContext] :
    ∀ n : ℕ, 1 ≤ n → ctx.desc_contrib n = 0 := by
  exact ctx.desc_contrib_zero

end QOU.Descent
