import QOU.Basic

namespace QOU.Descent

universe u

/-- Context for the descended-level-zero claim, over a generic base ring.

    §7c: the descended contribution is a Markov-trace value in the
    substrate ring. Nothing in the vanishing claim `desc_contrib n = 0`
    uses an ordering, a square root, or any other archimedean construct —
    the only structure required of the carrier is a distinguished `0` —
    so the carrier is a type variable with `[Zero R]`. The archimedean
    realisation is the instantiation `R := ℝ`. -/
class DescendedLevelZeroContext (R : Type u) [Zero R] where
  desc_contrib : ℕ → R
  desc_contrib_zero : ∀ n : ℕ, 1 ≤ n → desc_contrib n = 0

-- Ref: [manuscript] prop:descended-level-zero
theorem descended_level_zero {R : Type u} [Zero R]
    [ctx : DescendedLevelZeroContext R] :
    ∀ n : ℕ, 1 ≤ n → ctx.desc_contrib n = 0 := by
  exact ctx.desc_contrib_zero

end QOU.Descent
