import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Category.Basic


/-!
# QOU.AlgebraicSubstrate.UnitParticleState — The unit particle Liₑ(z)

The unit particle state Li_q(z) as the fundamental generator of the
local cohomology H¹_{𝔪₁}(A). It satisfies the q-differential equation
d_q Li_q(z) = dz / log_q(z).

LaTeX label: `def:unit-particle-state`

## References

- [leitner2026] Ch 8 §2, The unit particle as a cohomological defect
-/

set_option autoImplicit false

namespace QOU.AlgebraicSubstrate

open CategoryTheory

universe u v

/-- **UnitParticleState**: the fundamental generator Li_q(z) of the
    local cohomology group H¹_{𝔪₁}(A).

    This is the unique (up to scalar) element satisfying the
    q-differential equation d_q Li_q(z) = dz / log_q(z), where d_q
    is the Jackson q-derivative.

    LaTeX: `\label{def:unit-particle-state}` -/
structure UnitParticleState (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] where
  /-- The substrate algebra object A. -/
  substrate : C
  /-- The local cohomology object H¹_{𝔪₁}(A). -/
  cohomObj : C
  /-- The Jackson q-derivative endomorphism d_q : A → A. -/
  dq : substrate ⟶ substrate
  /-- The q-logarithm morphism log_q : A → A. -/
  logq : substrate ⟶ substrate
  /-- The generator morphism Li_q : 𝟙 → H¹_{𝔪₁}(A). -/
  generator : (CategoryTheory.MonoidalCategory.tensorUnit C) ⟶ cohomObj
  /-- The inclusion of the cohomology into A (for stating the ODE). -/
  incl : cohomObj ⟶ substrate
  /-- The q-differential equation: d_q Li_q = dz / log_q(z).
      Expressed categorically: applying d_q after embedding Li_q into A
      equals applying the reciprocal q-logarithm (log_q)⁻¹.
      Here `logq_inv` encodes the morphism (log_q)⁻¹ : A → A. -/
  logq_inv : substrate ⟶ substrate
  /-- logq and logq_inv are mutual inverses (on the image of incl). -/
  logq_inv_spec : logq ≫ logq_inv = 𝟙 substrate
  /-- The defining ODE: d_q ∘ incl(Li_q) = (log_q)⁻¹ ∘ incl(Li_q). -/
  q_diff_eq : generator ≫ incl ≫ dq = generator ≫ incl ≫ logq_inv
  /-- Uniqueness: the hom-space 𝟙 → H¹_{𝔪₁}(A) is at most
      one-dimensional. In a monoidal category this means any two
      global sections of the cohomology object are equal (the
      generator is essentially unique, not merely up to scalar). -/
  unique_generator : Subsingleton
    ((CategoryTheory.MonoidalCategory.tensorUnit C) ⟶ cohomObj)

end QOU.AlgebraicSubstrate
