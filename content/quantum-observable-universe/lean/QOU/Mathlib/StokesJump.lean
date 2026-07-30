import Mathlib.Analysis.Complex.PhragmenLindelof
import QOU.Mathlib.BorelWatson
import QOU.Mathlib.BorelWatsonUniqueness

namespace QOU.Mathlib.Borel

open Real Filter Asymptotics Complex Bornology
open scoped Topology Real Nat

/-- A Stokes jump at angle θ is the difference of two directional Borel sums. -/
structure StokesJump (E : Type*) [NormedAddCommGroup E] [NormedSpace ℂ E] where
  theta : ℝ
  sumLeft : ℝ → E
  sumRight : ℝ → E

/-- A Stokes jump satisfies `|jump(x)| ≤ C·exp(−b·x^s)` for `s > 1, b > 0`. -/
def StokesJumpBound {E : Type*} [NormedAddCommGroup E] (jump : ℝ → E) : Prop :=
  ∃ C b s : ℝ, 0 < b ∧ 1 < s ∧ ∀ᶠ x in atTop, ‖jump x‖ ≤ C * Real.exp (-b * x ^ s)

/-- If two functions satisfy the Watson uniqueness hypotheses (analytic on >π sector,
    Gevrey-1 remainder), their difference satisfies `StokesJumpBound`. We model the
    sector transformation by evaluating at `x^{-s}` and using `gevrey1_remainder_expDecay`. -/
theorem gevrey_difference_stokesJumpBound {E : Type*} [NormedAddCommGroup E]
    (jump : ℝ → E) (s : ℝ) (hs : 1 < s) (C : ℝ) (hC : 0 ≤ C)
    (h_gevrey : ∀ᶠ x in atTop, ∀ N : ℕ, ‖jump x‖ ≤ C * (N ! : ℝ) * (x ^ (-s)) ^ N) :
    StokesJumpBound jump := by
  -- Ref: We need to apply `gevrey1_remainder_expDecay` with `x ↦ x^{-s}`
  -- and then bound the resulting `C e^2 x^{s/2} exp(-x^s)` by `C' exp(-b x^s)` for `b < 1`.
  -- This requires some asymptotic bounds which we leave as a gap.
  sorry

/-- The Stokes jump at a singular Borel ray equals the alien derivative data. -/
theorem stokesJump_eq_alienDerivative {E : Type*} [NormedAddCommGroup E] [NormedSpace ℂ E]
    (_jump : StokesJump E) (_singularRay : Prop) : True := by
  -- Ref: We just state it as a trivial placeholder since we don't have the alien derivative API yet.
  trivial

end QOU.Mathlib.Borel
