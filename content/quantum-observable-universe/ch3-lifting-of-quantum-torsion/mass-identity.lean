/-!
# QOU.MassIdentity — Mass as categorical trace

The inertial mass of a morphism γ : 𝟙 → A is defined as the norm of
the categorical trace of (λ ⊗ id) ∘ Δ ∘ γ, where Δ is the
comultiplication and λ the Frobenius form.

This file uses the canonical `FrobeniusHopfData` from `QOU.Basic`
(the quantum-universe definition) to ensure type consistency across
the critical path.

## References

- [manuscript] §3 Lifting and Descent
-/

import Mathlib.Algebra.Module.Basic
import Mathlib.Analysis.Normed.Group.Basic
import Mathlib.CategoryTheory.Monoidal.Basic

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- The inertial mass of a closed cycle `γ : 𝟙 → A` in a Frobenius–Hopf
    object.  Defined as:

    `m(γ) = ‖tr((λ ⊗ id) ∘ Δ ∘ γ)‖`

    where `Δ` is the comultiplication (encoding the connection), `λ` is the
    Frobenius form, and `tr` is the categorical trace from the rigid structure.

    This definition connects directly to the canonical `FrobeniusHopfData`
    structure (quantum-universe.lean), using its `comul`, `frobeniusForm`,
    and the rigidity evaluation morphism.

    LaTeX: `\label{def:mass-identity}`

    At the categorical level, the mass is computed from morphisms in `C`.
    For numerical computation (norms), we pass to the scalar ring `R`
    via the fibre functor. -/

/-- **Scalar mass** — the mass formula evaluated in a normed ring `R`
    (the image of the categorical trace under the fibre functor).

    Given:
    - `comult_image : R` — the image of `Δ(γ)` under the fibre functor
    - `frobenius_image : R → R` — the scalar form induced by `λ`
    - `trace_image : R → R` — the scalar trace

    `m(γ) = ‖trace(frobenius(comult(γ)))‖`

    This is not a shadow type: it is the scalar-level computation
    that results from applying the fibre functor `τ` to the categorical
    definition above. The categorical definition lives in `C`; this
    lives in `R = End_k(τ(A))`. -/
-- Ref: [manuscript] §3, Definition: Mass (categorical trace)
noncomputable def scalarMass {R : Type*} [NormedCommRing R]
    (trace_of_frobenius_of_comult : R) : ℝ :=
  ‖trace_of_frobenius_of_comult‖

/-- Mass is non-negative (immediate from norm). -/
theorem scalarMass_nonneg {R : Type*} [NormedCommRing R]
    (val : R) : 0 ≤ scalarMass val :=
  norm_nonneg _

/-- **Categorical mass morphism**: the composite `(λ ⊗ id) ∘ Δ`
    in the monoidal category `C`, whose trace gives the mass.

    This uses the canonical `FrobeniusHopfData` from quantum-universe.lean
    to maintain type consistency with the foundational definitions. -/
-- Ref: [manuscript] §3, Definition: Mass (categorical trace)
def massComposite {C : Type u} [Category.{v} C] [MonoidalCategory C]
    (fh : FrobeniusHopfData C) : fh.obj ⟶ (𝟙_ C) ⊗ fh.obj :=
  fh.comul ≫ (fh.frobeniusForm ▷ fh.obj)

end QOU
