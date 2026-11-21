import Mathlib.Order.WellFounded
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Module.Basic
import Mathlib.Algebra.Algebra.Defs


/-!
# QOU.UnitalGroebner.LeadingTerm — Leading monomial, coefficient, and term

For f ∈ A (with B well-ordered), defines LM(f), LC(f), LT(f), and
the divisibility relation β | f.

LaTeX label: `def:leading-terms`

## References
- [leitner2026] §1/leading-terms
-/

namespace QOU.UnitalGroebner

universe u

variable (R : Type u) [CommRing R]
variable (B : Type u) [LinearOrder B] [WellFoundedLT B]
variable (A : Type u) [Ring A] [Algebra R A]

/-- A monomial basis element together with its coefficient.
    Represents a term c · b where c ∈ R* and b ∈ B. -/
structure Term where
  coeff : R
  mono : B
  coeff_ne_zero : coeff ≠ 0

/-- Leading term data for a nonzero element f ∈ A written in the
    monomial basis B with respect to a well-ordering <.

    Given f = c₁b₁ + c₂b₂ + ⋯ + cₙbₙ with b₁ > b₂ > ⋯ > bₙ:
    - LM(f) = b₁  (leading monomial)
    - LC(f) = c₁  (leading coefficient)
    - LT(f) = c₁ · b₁ (leading term) -/
-- Ref: [leitner2026] §1/leading-terms
structure LeadingTerm where
  /-- The leading monomial LM(f): largest basis element. -/
  leadingMono : B
  /-- The leading coefficient LC(f): coefficient of LM(f). -/
  leadingCoeff : R
  /-- The leading coefficient is nonzero. -/
  leadingCoeff_ne_zero : leadingCoeff ≠ 0

/-- Divisibility: β divides f if there exist u, v ∈ B and scalar ∈ R*
    such that scalar · LT(u · β · v) = LT(f). -/
-- Ref: [leitner2026] §1/leading-terms
structure Divides (β : B) (lt_f : LeadingTerm R B) where
  /-- Left multiplier in B. -/
  u : B
  /-- Right multiplier in B. -/
  v : B
  /-- Scalar factor in R*. -/
  scalar : R
  /-- The scalar is nonzero. -/
  scalar_ne_zero : scalar ≠ 0

end QOU.UnitalGroebner
