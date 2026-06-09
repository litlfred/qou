import QOU.QuantumObservableUniverse.GaugeTheory
import QOU.Archimedean.GroundRing
import Mathlib.CategoryTheory.Linear.Basic


/-!
# QOU.QuantumObservableUniverses.QDifferentialGeometry — q-differential-geometry display structures

Authoritative library home for the categorical Dirac operator,
Lagrangian, and q-connection data, previously defined only inside
content-object display snippets (`categorical-dirac-operator.lean`,
`categorical-lagrangian.lean`, `categorical-q-connection.lean`).
Relocated here (2026-06-09 axiom audit) so the companion
`*-unique.lean` display files can `import` the real structures and
carry genuinely type-checked uniqueness statements.

`FrobeniusHopfData` / `CategoricalConnection` are taken from
`QOU.QuantumObservableUniverse.GaugeTheory`; the ground ring
`R_q = ℤ[q, q⁻¹]` from `QOU.Archimedean.GroundRing`.  The derived
`nabla_q` morphism (content helper) needs an inverse of `q` in `R_q`,
which the Laurent ring does not provide; it is intentionally omitted
here — the uniqueness theorems are about the structures themselves.

## References

- [manuscript] §2-quantum-observable-universes
- [connes1994] Noncommutative Geometry
-/

namespace QOU

open CategoryTheory
open MonoidalCategory

universe u v

/-- **Categorical Dirac operator** `𝒟_∇ = q⁻¹∇ + (1 − q⁻¹)ι_ξ∇`. -/
-- Ref: [connes1994] Noncommutative Geometry
structure CategoricalDiracOperator (C : Type u) [Category.{v} C]
    [MonoidalCategory C]
    (fh : FrobeniusHopfData C) where
  /-- The underlying connection. -/
  connection : CategoricalConnection C fh
  /-- The substrate parameter q. -/
  q : (𝟙_ C) ⟶ (𝟙_ C)
  /-- The Reeb derivation ξ. -/
  reeb : fh.obj ⟶ fh.obj
  /-- The Dirac morphism `𝒟_∇ : A → Ω¹(A)`. -/
  dirac : fh.obj ⟶ fh.obj

/-- **Categorical Lagrangian** `ℒ_q = 𝒟_∇² + ψ* ⊗ 𝒟_∇ψ`. -/
-- Ref: [connes1994] Noncommutative Geometry
structure CategoricalLagrangian (C : Type u) [Category.{v} C]
    [MonoidalCategory C]
    (fh : FrobeniusHopfData C) where
  /-- The Dirac operator. -/
  dirac : CategoricalDiracOperator C fh
  /-- The state `ψ : 𝟙 → A`. -/
  state : (𝟙_ C) ⟶ fh.obj
  /-- The Lagrangian endomorphism `ℒ_q ∈ End(A)`. -/
  lagrangian : fh.obj ⟶ fh.obj

/-- **Categorical q-deformed connection** data
    `∇_q = q⁻¹ ∇ + (1 − q⁻¹)(ξ ⌟ ∇) θ_A`.  (The derived `nabla_q`
    morphism is omitted — it needs `q⁻¹` in `R_q`, which the Laurent
    ring lacks; the structure is what the uniqueness theorem ranges
    over.) -/
-- Ref: [connes1994] Noncommutative Geometry
structure CategoricalQConnection (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [Preadditive C] [Linear Archimedean.R_q C] where
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
  /-- The deformation parameter `q`, non-zero. -/
  q : Archimedean.R_q
  q_ne_zero : q ≠ 0

end QOU
