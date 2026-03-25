/-!
# Fred2005.RemainderModule

The remainder modules O(I) and Õ(I): R-submodules of A spanned by
basis elements whose leading terms (resp. leading monomials) are not
leading terms (resp. leading monomials) of any element of I.

Reference: Frédéric (2005), "Unital Gröbner bases for noncommutative
algebras", following Leitner–Pawłoski (2004).

LaTeX label: `def:remainder-module`
-/

import Mathlib.Data.Real.Basic
import Mathlib.Order.WellFounded

namespace Fred2005

universe u v

/-- The **remainder module** O(I) for a subset I of an R-algebra A
    with admissible system. The module is spanned by scalar multiples
    λβ of basis elements β whose leading terms do not coincide with
    the leading term of any element of I.

    LaTeX: `\label{def:remainder-module}`
    -- Ref: [leitnerpawloski2004] https://arxiv.org/abs/math/0409565 -/
structure RemainderModule (R : Type u) (A : Type v) [CommRing R] [Ring A]
    [Algebra R A] where
  /-- The set of basis monomials. -/
  basis : Set A
  /-- Leading monomial function. -/
  leadingMonomial : A → A
  /-- Leading term function. -/
  leadingTerm : A → A
  /-- The subset I ⊆ A. -/
  I : Set A
  /-- The generating set o(I): scalar–monomial pairs λβ not matching
      any leading term from I. -/
  oI : Set A
  /-- The tilde remainder module generating set õ(I): basis elements
      not appearing as leading monomials of elements of I. -/
  otildeI : Set A
  /-- o(I) consists of basis elements scaled by nonzero coefficients
      whose leading terms avoid LT(h) for all h ∈ I. -/
  oI_spec : ∀ a ∈ oI, ∃ β ∈ basis,
    ∀ h ∈ I, leadingTerm h ≠ a := by
    -- Ref: [leitnerpawloski2004] https://arxiv.org/abs/math/0409565
    sorry
  /-- õ(I) = B \ {LM(h) | h ∈ I}. -/
  otildeI_spec : otildeI = basis \ (leadingMonomial '' I) := by
    -- Ref: [leitnerpawloski2004] https://arxiv.org/abs/math/0409565
    sorry

end Fred2005
