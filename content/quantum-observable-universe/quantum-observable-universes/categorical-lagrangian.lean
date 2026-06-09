import QOU.QuantumObservableUniverse.GaugeTheory
import Mathlib.CategoryTheory.Linear.Basic


/-!
# QOU.CategoricalLagrangian

The categorical Lagrangian `ℒ_q(∇, ψ) = 𝒟_∇² + ψ* ⊗ 𝒟_∇ψ`,
an endomorphism of `A` encoding the full physics before tracing.

Stated over an `R`-linear monoidal category `C` (the `k`-linearity of the
`(𝐂, A, τ)` triple), so the sum of the two endomorphisms is expressible.
The matter term `ψ* ⊗ 𝒟_∇ψ` is the rank-one endomorphism
`A --ψ*--> 𝟙 --𝒟_∇ψ--> A`, i.e. `costate ≫ (state ≫ 𝒟_∇)`.

LaTeX: `\label{def:categorical-lagrangian}`
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Categorical Lagrangian** `ℒ_q = 𝒟_∇² + ψ* ⊗ 𝒟_∇ψ`.

    The endomorphism of `A` whose categorical trace yields the categorical
    action.  The `lagrangian` morphism is pinned by `lagrangian_formula` to:

    - `𝒟_∇²` — `dirac.dirac ≫ dirac.dirac`, the bosonic sector (gravity + gauge);
    - `ψ* ⊗ 𝒟_∇ψ` — `costate ≫ state ≫ dirac.dirac`, the rank-one fermionic
      coupling (apply `𝒟_∇` to the state, then pair against the costate `ψ*`).

    Ref: [manuscript] §1-quantum-observable-universe -/
-- Ref: [manuscript] §1-quantum-observable-universe
structure CategoricalLagrangian (R : Type*) [CommRing R]
    (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear R C]
    (fh : FrobeniusHopfData C) where
  /-- The Dirac operator `𝒟_∇`. -/
  dirac : CategoricalDiracOperator R C fh
  /-- The state `ψ : 𝟙 → A`. -/
  state : (𝟙_ C) ⟶ fh.obj
  /-- The costate `ψ* : A → 𝟙` (Frobenius mate of the state). -/
  costate : fh.obj ⟶ (𝟙_ C)
  /-- The Lagrangian endomorphism `ℒ_q ∈ End(A)`. -/
  lagrangian : fh.obj ⟶ fh.obj
  /-- **Defining formula**: `ℒ_q = 𝒟_∇² + ψ* ⊗ 𝒟_∇ψ`. -/
  lagrangian_formula :
    lagrangian = dirac.dirac ≫ dirac.dirac + costate ≫ state ≫ dirac.dirac

end QOU
