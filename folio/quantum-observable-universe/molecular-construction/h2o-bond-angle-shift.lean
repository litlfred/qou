import Mathlib.Tactic

/-!
# QOU.Molecular.BondAngleShift — bent angle as a quadratic-well shift

Near the symmetric (tetrahedral) value `θ₀`, the bond-bending energy is
harmonic: a **quadratic** restoring term `a·(θ-θ₀)²` with stiffness
`a > 0`. A lone-pair asymmetry adds a **linear** perturbation `b·θ`
(the net angular penalty from the stronger lone-pair repulsion; writing
`b = 2·a·s`, `s` is the shift). The minimiser of the sum is

    argmin_θ [ a(θ-θ₀)² + b·θ ]  =  θ₀ − b/(2a)  =  θ₀ − s,

a LINEAR response set by the quadratic stiffness `a`. For water the
lone-pair term has `b > 0` (it penalises the wider symmetric angle), so
`s > 0` and `θ* < θ₀`: the `109.5° → 104.5°` reduction is exactly the
quadratic well's minimum displaced by the lone-pair term. The sign is
structural; the magnitude `s = b/(2a)` is the compute/experimental input.

This file states the energy with `b = 2·a·s` to stay division-free.

## References
- [leitner2026] Ch. 12, Proposition: bent angle from the quadratic well
-/

namespace QOU.Molecular

/-- **Bent angle = quadratic-well minimum shifted by the lone-pair term.**
The harmonic bending energy `a(θ-θ₀)²` plus the linear lone-pair
perturbation `(2as)·θ` is minimised at `θ₀ - s` (so `s = b/(2a)` for
`b = 2as`). The energy minus its value at the minimiser is the perfect
square `a(θ - (θ₀ - s))² ≥ 0`. -/
theorem bond_angle_shift (a θ₀ s θ : ℝ) (ha : 0 < a) :
    a * ((θ₀ - s) - θ₀) ^ 2 + (2 * a * s) * (θ₀ - s)
      ≤ a * (θ - θ₀) ^ 2 + (2 * a * s) * θ := by
  nlinarith [mul_nonneg ha.le (sq_nonneg (θ - θ₀ + s)), ha,
    sq_nonneg (θ - θ₀ + s)]

end QOU.Molecular
