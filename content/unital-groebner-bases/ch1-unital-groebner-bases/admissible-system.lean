/-!
# Fred2005.AdmissibleSystem

A monomial ordering and admissible system: a monomial basis equipped
with a well-ordering compatible with two-sided multiplication.

Reference: Frédéric (2005), "Unital Gröbner bases for noncommutative
algebras", following Leitner–Pawłoski (2004).

LaTeX label: `def:admissible-system`
-/

import Mathlib.Data.Real.Basic
import Mathlib.Order.WellFounded

namespace Fred2005

universe u v

/-- An **admissible system** for an R-algebra A: a monomial basis
    together with a well-ordering on the basis that is compatible
    with two-sided multiplication.

    LaTeX: `\label{def:admissible-system}`
    -- Ref: [leitnerpawloski2004] https://arxiv.org/abs/math/0409565 -/
structure AdmissibleSystem (R : Type u) (A : Type v) [CommRing R] [Ring A]
    [Algebra R A] where
  /-- Index set for algebra generators. -/
  Λ : Type*
  /-- The set of basis monomials. -/
  basis : Set A
  /-- Leading monomial function. -/
  leadingMonomial : A → A
  /-- Leading coefficient function. -/
  leadingCoefficient : A → R
  /-- Leading term function. -/
  leadingTerm : A → A
  /-- A linear order on the basis elements. -/
  basisOrder : A → A → Prop
  /-- The ordering is well-founded. -/
  basisWellFounded : WellFounded basisOrder
  /-- Compatibility: if b < b' then r·b·s < r·b'·s whenever the
      products are nonzero. -/
  compat_mul : ∀ b b' r s : A, b ∈ basis → b' ∈ basis →
    r ∈ basis → s ∈ basis →
    basisOrder b b' →
    r * b * s ≠ 0 →
    basisOrder (r * b * s) (r * b' * s) := by
    -- Ref: [leitnerpawloski2004] https://arxiv.org/abs/math/0409565
    sorry
  /-- Noetherianity: if b' = LM(r·b·s) with r or s ≠ 1, then b < LM(b'). -/
  compat_lm : ∀ b r s : A, b ∈ basis → r ∈ basis → s ∈ basis →
    r * b * s ≠ 0 →
    (r ≠ 1 ∨ s ≠ 1) →
    basisOrder b (leadingMonomial (r * b * s)) := by
    -- Ref: [leitnerpawloski2004] https://arxiv.org/abs/math/0409565
    sorry

end Fred2005
