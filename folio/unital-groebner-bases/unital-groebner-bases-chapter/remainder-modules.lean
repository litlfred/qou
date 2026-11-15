import Mathlib.Order.WellFounded
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Algebra.Defs
import Mathlib.Algebra.Module.Basic
import Mathlib.LinearAlgebra.Span.Basic


/-!
# QOU.UnitalGroebner.RemainderModule — Remainder modules O(I) and Õ(I)

Given a subset I ⊆ A, defines:
- O(I): R-submodule spanned by {λβ | λ ∈ R*, β ∈ B, ∀h ∈ I: LT(h) ≠ λβ}
- Õ(I): R-submodule spanned by B \ {LM(h) | h ∈ I}  (free R-module)

LaTeX label: `def:remainder-modules`

## References
- [leitner2026] §1/remainder-modules
-/

namespace QOU.UnitalGroebner

universe u

variable (R : Type u) [CommRing R]
variable (B : Type u) [LinearOrder B] [WellFoundedLT B]
variable (A : Type u) [Ring A] [Algebra R A] [Module R A]

/-- The set o(I) of "non-leading" scaled monomials:
    {λβ | λ ∈ R*, β ∈ B, ∀h ∈ I: LT(h) ≠ λβ}.

    These are the monomials (with coefficients) that do NOT appear
    as the leading term of any element of I. -/
-- Ref: [leitner2026] §1/remainder-modules
structure RemainderModule where
  /-- The subset I ⊆ A whose leading terms are avoided. -/
  ideal : Set A
  /-- The monomial basis. -/
  basis : Set B
  /-- O(I): the R-submodule spanned by non-leading scaled monomials. -/
  remainder : Submodule R A
  /-- Õ(I): the free R-submodule spanned by non-leading monomials. -/
  freeRemainder : Submodule R A
  /-- Õ(I) is contained in O(I). -/
  free_le_remainder : freeRemainder ≤ remainder

end QOU.UnitalGroebner
