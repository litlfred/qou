import QOU.QuantumObservableUniverse.GaugeTheory
import QOU.Archimedean.GroundRing
import Mathlib.CategoryTheory.Linear.Basic


/-!
# QOU.QuantumObservableUniverses.QDifferentialGeometry — q-differential-geometry display structures

Authoritative, **importable** library home for the categorical Dirac
operator, Lagrangian, and q-connection data, so the companion
`*-unique.lean` display files can `import` the real structures and carry
genuinely type-checked uniqueness statements (the content-object snippets
that define these structures live outside the `QOU` Lake library and are
not importable on their own).

These match the **strengthened** statements introduced on `main` by the
`proof-integrity(dirac|lagrangian)` sweep (commits `2864d683`,
`e0c6bb38`): over an `R`-linear monoidal category the defining
morphism is **pinned by a `*_formula` law field** rather than left free,
so uniqueness is a genuine *determination* (not mere extensionality on
free fields).  `CategoricalQConnection` is strengthened here the same
way (`qinv` + `q_unit` + `nabla_q` + `nabla_q_formula`).

`FrobeniusHopfData` / `CategoricalConnection` from
`QOU.QuantumObservableUniverse.GaugeTheory`; `R_q` from
`QOU.Archimedean.GroundRing`.

## References

- [leitner2026] §2-quantum-observable-universes
- [connes1994] Noncommutative Geometry
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Categorical Dirac operator** `𝒟_∇ = q⁻¹ ∇ + (1 − q⁻¹) ι_ξ∇`, over an
    `R`-linear monoidal category.  `dirac` is pinned by `dirac_formula`. -/
-- Ref: [connes1994] Noncommutative Geometry
structure CategoricalDiracOperator (R : Type*) [CommRing R]
    (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear R C]
    (fh : FrobeniusHopfData C) where
  /-- The underlying connection `∇`. -/
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
  /-- **Defining formula**: `𝒟_∇ = q⁻¹ ∇ + (1 − q⁻¹) ι_ξ∇`. -/
  dirac_formula : dirac = qinv • nablaEndo + (1 - qinv) • reeb

/-- **Categorical Lagrangian** `ℒ_q = 𝒟_∇² + ψ* ⊗ 𝒟_∇ψ`, over an
    `R`-linear monoidal category.  `lagrangian` is pinned by
    `lagrangian_formula`. -/
-- Ref: [connes1994] Noncommutative Geometry
structure CategoricalLagrangian (R : Type*) [CommRing R]
    (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear R C]
    (fh : FrobeniusHopfData C) where
  /-- The Dirac operator `𝒟_∇`. -/
  dirac : CategoricalDiracOperator R C fh
  /-- The state `ψ : 𝟙 → A`. -/
  state : (𝟙_ C) ⟶ fh.obj
  /-- The costate `ψ* : A → 𝟙`. -/
  costate : fh.obj ⟶ (𝟙_ C)
  /-- The Lagrangian endomorphism `ℒ_q ∈ End(A)`. -/
  lagrangian : fh.obj ⟶ fh.obj
  /-- **Defining formula**: `ℒ_q = 𝒟_∇² + ψ* ⊗ 𝒟_∇ψ`. -/
  lagrangian_formula :
    lagrangian = dirac.dirac ≫ dirac.dirac + costate ≫ state ≫ dirac.dirac

/-- **Categorical q-deformed connection** data
    `∇_q = q⁻¹ ∇ + (1 − q⁻¹)(ξ ⌟ ∇) θ`, over an `R_q`-linear monoidal
    category.  `nabla_q` is pinned by `nabla_q_formula` (`qinv` + `q_unit`
    encode `q⁻¹` without needing an inverse in the Laurent ring `R_q`). -/
-- Ref: [connes1994] Noncommutative Geometry
structure CategoricalQConnection (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear Archimedean.R_q C] where
  /-- The Frobenius–Hopf object `A`. -/
  A : C
  /-- The object of 1-forms `Ω¹`. -/
  Omega1 : C
  /-- The classical connection `∇ : A → A ⊗ Ω¹`. -/
  nabla : A ⟶ (A ⊗ Omega1)
  /-- The contracted connection `ξ ⌟ ∇`. -/
  xi_contract_nabla : A ⟶ A
  /-- The canonical 1-form `θ_A`. -/
  theta_nabla : A ⟶ (A ⊗ Omega1)
  /-- The deformation parameter `q ∈ R_q`. -/
  q : Archimedean.R_q
  /-- The inverse `q⁻¹ ∈ R_q`. -/
  qinv : Archimedean.R_q
  /-- `q` is a unit: `q · q⁻¹ = 1`. -/
  q_unit : q * qinv = 1
  /-- The q-deformed connection `∇_q : A → A ⊗ Ω¹`. -/
  nabla_q : A ⟶ (A ⊗ Omega1)
  /-- **Defining formula**: `∇_q = q⁻¹ ∇ + (1 − q⁻¹)(ξ ⌟ ∇) θ`. -/
  nabla_q_formula :
    nabla_q = qinv • nabla + (1 - qinv) • (xi_contract_nabla ≫ theta_nabla)

end QOU
