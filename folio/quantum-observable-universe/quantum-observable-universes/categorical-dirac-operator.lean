import QOU.QuantumObservableUniverse.GaugeTheory
import Mathlib.CategoryTheory.Linear.Basic


/-!
# QOU.CategoricalDiracOperator

The q-deformed covariant derivative `𝒟_∇ = q⁻¹ ∇ + (1 - q⁻¹) ι_ξ∇`,
serving as the categorical Dirac operator.

The defining formula is an `R`-linear combination of two endomorphisms
(`∇` and its Reeb contraction `ι_ξ∇`), so the ambient category `C` must be
`R`-linear — exactly the `k`-linear hypothesis the `(𝐂, A, τ)` triple of
[`def:quantum-observable-universe`] already carries (`𝐂 = 𝐑𝐞𝐩(SU_q(2))`,
the fibre functor abstracting `Vect_k`).  Without `R`-linearity the sum is
not even expressible; with it the operator is pinned to the formula by the
`dirac_formula` field rather than being a free morphism.

LaTeX: `\label{def:categorical-dirac-operator}`
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Categorical Dirac operator** `𝒟_∇ = q⁻¹ ∇ + (1 - q⁻¹) ι_ξ∇`.

    The `q`-deformed covariant derivative on a quantum observable universe,
    stated over an `R`-linear monoidal category `C` (the `k`-linearity of the
    `(𝐂, A, τ)` triple).  The `dirac` morphism is **not** a free field: the
    `dirac_formula` field forces it to equal the `R`-linear combination
    `q⁻¹ ∇ + (1 - q⁻¹) ι_ξ∇`, where:

    - `nablaEndo` is the endomorphism representative of the connection `∇`;
    - `reeb` is the Reeb contraction `ι_ξ∇`;
    - `q`, `qinv` are the substrate parameter and its inverse (`q_unit`).

    When `qinv = 1` the formula reduces to `nablaEndo`, the undeformed
    connection.

    Ref: [leitner2026] §1-quantum-observable-universe -/
-- Ref: [leitner2026] §1-quantum-observable-universe
structure CategoricalDiracOperator (R : Type*) [CommRing R]
    (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear R C]
    (fh : FrobeniusHopfData C) where
  /-- The underlying connection `∇` (Definition `def:categorical-connection`). -/
  connection : CategoricalConnection C fh
  /-- The substrate parameter `q ∈ R`. -/
  q : R
  /-- The inverse `q⁻¹ ∈ R`. -/
  qinv : R
  /-- `q` is a unit: `q · q⁻¹ = 1`. -/
  q_unit : q * qinv = 1
  /-- The endomorphism representative of the connection `∇ : A → A`. -/
  nablaEndo : fh.obj ⟶ fh.obj
  /-- The Reeb contraction `ι_ξ∇ : A → A`. -/
  reeb : fh.obj ⟶ fh.obj
  /-- The Dirac morphism `𝒟_∇ : A → A`. -/
  dirac : fh.obj ⟶ fh.obj
  /-- **Defining formula**: `𝒟_∇ = q⁻¹ ∇ + (1 - q⁻¹) ι_ξ∇`, the `R`-linear
      combination of the connection and its Reeb contraction. -/
  dirac_formula : dirac = qinv • nablaEndo + (1 - qinv) • reeb

end QOU
