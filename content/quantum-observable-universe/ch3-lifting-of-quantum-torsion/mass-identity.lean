/-!
# QOU.MassIdentity — Mass as categorical trace

The inertial mass of a morphism γ : 𝟙 → A is defined as the norm of
the categorical trace of (λ ⊗ id) ∘ Δ ∘ γ, where Δ is the
comultiplication and λ the Frobenius form.

## References

- [manuscript] §3 Lifting and Descent
-/

import Mathlib.Algebra.Module.Basic
import Mathlib.Analysis.Normed.Group.Basic

namespace QOU

/-- The data needed to define mass in a Frobenius–Hopf object. -/
-- Ref: [manuscript] §3, Definition: Mass (categorical trace)
structure FrobeniusHopfData (R : Type*) [NormedCommRing R] where
  /-- The categorical trace tr : End(A) → R. -/
  trace : R → R
  /-- The comultiplication Δ : A → A ⊗ A (as a scalar value after trace). -/
  comult_trace : R → R
  /-- The Frobenius form λ : A → 𝟙 (as a scalar). -/
  frobenius_form : R → R

/-- The inertial mass of a closed cycle γ : 𝟙 → A.
    m(γ) = ‖tr((λ ⊗ id) ∘ Δ ∘ γ)‖

    LaTeX: `\label{def:mass-identity}` -/
-- Ref: [manuscript] §3, Definition: Mass (categorical trace)
noncomputable def categoricalMass {R : Type*} [NormedCommRing R]
    (fhd : FrobeniusHopfData R) (γ : R) : ℝ :=
  ‖fhd.trace (fhd.frobenius_form (fhd.comult_trace γ))‖

/-- Mass is non-negative. -/
theorem categoricalMass_nonneg {R : Type*} [NormedCommRing R]
    (fhd : FrobeniusHopfData R) (γ : R) :
    0 ≤ categoricalMass fhd γ :=
  norm_nonneg _

end QOU
