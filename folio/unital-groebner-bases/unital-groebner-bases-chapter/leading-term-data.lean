import Mathlib.Order.WellFounded
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Module.Basic

/-!
# Leading monomial, coefficient, and term

Content block for `def:leading-term-data`.

Split out of `def:monomial-basis`. For `f ∈ A` (with the monomial basis
`B` well-ordered), records the leading-term data: `LM(f)`, `LC(f)`, and
`LT(f) = LC(f)·LM(f)`. The authoritative formalization lives in
`UGB.UnitalGroebner.LeadingTerm`.

## References
- [leitnerpawloski2004] https://arxiv.org/abs/math/0409565, Definition 3
-/

namespace QOU.GrobnerShirshov.ContentBlock

universe u

variable (R : Type u) [CommRing R]
variable (B : Type u) [LinearOrder B] [WellFoundedLT B]

/-- Leading-term data for a nonzero element `f ∈ A` written in the
    monomial basis `B` with respect to a well-ordering `<`.

    Given `f = c₁b₁ + c₂b₂ + ⋯ + cₙbₙ` with `b₁ > b₂ > ⋯ > bₙ`:
    - `LM(f) = b₁`  (leading monomial)
    - `LC(f) = c₁`  (leading coefficient)
    - `LT(f) = c₁ · b₁` (leading term) -/
-- Ref: [leitnerpawloski2004] Leitner & Pawloski, "Unital Gröbner Bases over Arbitrary Commutative Ground Rings," arXiv:math/0409565
structure LeadingTermData where
  /-- The leading monomial `LM(f)`: the largest basis element in the support. -/
  leadingMono : B
  /-- The leading coefficient `LC(f)`: the coefficient of `LM(f)`. -/
  leadingCoeff : R
  /-- The leading coefficient is nonzero (it lies in `R* = R ∖ {0}`). -/
  leadingCoeff_ne_zero : leadingCoeff ≠ 0

end QOU.GrobnerShirshov.ContentBlock
