/-!
# Fred2005.MonomialBasis

Monomials, monomial bases, and leading terms for a noncommutative
R-algebra A that is free as an R-module.

Reference: Frédéric (2005), "Unital Gröbner bases for noncommutative
algebras", following Leitner–Pawłoski (2004).

LaTeX label: `def:monomial-basis`
-/

import Mathlib.Data.Real.Basic
import Mathlib.Order.WellFounded

namespace Fred2005

universe u v

/-- A **monomial basis** for an R-algebra A, subordinate to a set of
    generators indexed by `Λ`. The carrier type `A` is free as an
    R-module with basis elements given by finite words in `Λ`.

    LaTeX: `\label{def:monomial-basis}`
    -- Ref: [leitnerpawloski2004] https://arxiv.org/abs/math/0409565 -/
structure MonomialBasis (R : Type u) (A : Type v) [CommRing R] [Ring A]
    [Algebra R A] where
  /-- Index set for algebra generators. -/
  Λ : Type*
  /-- The set of basis monomials (finite words in Λ). -/
  basis : Set A
  /-- Leading monomial: the largest basis element in the support of f. -/
  leadingMonomial : A → A
  /-- Leading coefficient: the coefficient of the leading monomial. -/
  leadingCoefficient : A → R
  /-- Leading term: LC(f) · LM(f). -/
  leadingTerm : A → A
  /-- The leading term equals the leading coefficient times the
      leading monomial. -/
  lt_eq_lc_mul_lm : ∀ f : A, leadingTerm f =
    leadingCoefficient f • leadingMonomial f := by
    -- Ref: [leitnerpawloski2004] https://arxiv.org/abs/math/0409565
    sorry
  /-- The leading monomial of a nonzero element lies in the basis. -/
  lm_mem_basis : ∀ f : A, f ≠ 0 → leadingMonomial f ∈ basis := by
    -- Ref: [leitnerpawloski2004] https://arxiv.org/abs/math/0409565
    sorry

end Fred2005
