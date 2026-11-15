import Mathlib.RingTheory.Ideal.Maps
import Mathlib.Algebra.Algebra.Defs
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Category.Basic
import Mathlib.RingTheory.Ideal.Basic


/-!
# QOU.AlgebraicSubstrate.MaximalIdealDefect — Maximal ideal at z = 1

The maximal ideal 𝔪₁ ⊂ A corresponding to the unit coordinate z = 1
in the spectral fiber. This is the kernel of the evaluation homomorphism
ev₁ : A → k, and the fixed point of the antipode S.

LaTeX label: `def:maximal-ideal-defect`

## References

- [leitner2026] Ch 8 §2, The unit particle as a cohomological defect
-/

set_option autoImplicit false

namespace QOU.AlgebraicSubstrate

universe u

/-- **MaximalIdealDefect**: the maximal ideal 𝔪₁ at the unit coordinate
    z = 1 in the spectral fiber of the Frobenius–Hopf substrate.

    This ideal is the kernel of the evaluation homomorphism ev₁ : A → k,
    and is distinguished as the fixed point of the antipode S.

    LaTeX: `\label{def:maximal-ideal-defect}` -/
structure MaximalIdealDefect (R : Type*) [CommRing R] where
  /-- The ambient algebra A. -/
  algebra : Type*
  /-- Ring structure on A. -/
  [ringInst : CommRing algebra]
  /-- R-algebra structure. -/
  [algebraInst : Algebra R algebra]
  /-- The maximal ideal 𝔪₁ = ker(ev₁). -/
  maxIdeal : Ideal algebra
  /-- The evaluation homomorphism ev₁ : A → R at z = 1. -/
  eval_one : algebra →+* R
  /-- 𝔪₁ is the kernel of ev₁. -/
  -- Ref: [leitner2026] Ch 8 §2
  ideal_eq_ker : maxIdeal = RingHom.ker eval_one
  /-- 𝔪₁ is maximal. -/
  -- Ref: [leitner2026] Ch 8 §2
  is_maximal : maxIdeal.IsMaximal

attribute [instance] MaximalIdealDefect.ringInst
attribute [instance] MaximalIdealDefect.algebraInst

end QOU.AlgebraicSubstrate
