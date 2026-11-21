import QOU.QuantumObservableUniverse.GaugeTheory
import QOU.QuantumObservableUniverses.QDifferentialGeometry
import QOU.Archimedean.GroundRing
import Mathlib.CategoryTheory.Linear.Basic


/-!
# QOU.CategoricalQConnection.exists — existence of the categorical q-connection

`∇_q = q⁻¹ ∇ + (1 - q⁻¹) (ξ ⌟ ∇) θ` exists as a morphism `A → A ⊗ Ω¹` in the
`R_q`-linear monoidal category `C`: it is the explicit `R_q`-linear combination
of the classical connection `∇` and the composite `(ξ ⌟ ∇) ≫ θ`, well-defined
in any `R_q`-linear category.  The witness genuinely realises the defining
formula — the `nabla_q` field of the constructed q-connection **equals** the
combination, pinned by `nabla_q_formula` (not a trivial identity).

This file imports the relocated, **strengthened** `CategoricalQConnection`
structure from `QOU.QuantumObservableUniverses.QDifferentialGeometry` (the
content-object snippet that defines the structure is not importable on its own).
The `qinv` + `q_unit` fields encode `q⁻¹` without needing an inverse in the
Laurent ring `R_q`.

LaTeX: `\label{prop:categorical-q-connection-exists}`

## References

- [leitner2026] §2-quantum-observable-universes/categorical-q-connection-exists
- [connes1994] Noncommutative Geometry
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Existence of the categorical q-connection.**

    In an `R_q`-linear monoidal category `C`, given the Frobenius–Hopf object
    `A`, the 1-forms object `Ω¹`, the classical connection `∇`, the Reeb
    contraction `ξ ⌟ ∇`, the canonical 1-form `θ`, and a unit substrate
    parameter `q` (`q · qinv = 1`), there exists a `CategoricalQConnection C`
    whose underlying objects and classical data are exactly the inputs and
    whose q-deformed connection morphism is exactly the `R_q`-linear
    combination `q⁻¹ ∇ + (1 - q⁻¹) (ξ ⌟ ∇) θ`.

    Since the q-connection bundles its objects (`A`, `Ω¹` are fields), the
    object identifications use `=` and the morphism identifications use `HEq`
    transported along them (the `MassGap` ∃-repackaging pattern, §U4).  The
    existential pins the `nabla_q` field to the defining formula, so the
    witness genuinely realises [`def:categorical-q-connection`]. -/
-- Ref: [connes1994] Noncommutative Geometry
theorem CategoricalQConnection.exists
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    [CategoryTheory.Preadditive C]
    [CategoryTheory.Linear Archimedean.R_q C]
    (A Omega1 : C)
    (nabla : A ⟶ (A ⊗ Omega1))
    (xi_contract_nabla : A ⟶ A)
    (theta_nabla : A ⟶ (A ⊗ Omega1))
    (q qinv : Archimedean.R_q) (q_unit : q * qinv = 1) :
    ∃ cqc : CategoricalQConnection C,
      cqc.A = A ∧ cqc.Omega1 = Omega1 ∧
      HEq cqc.nabla (nabla) ∧
      HEq cqc.xi_contract_nabla (xi_contract_nabla) ∧
      HEq cqc.theta_nabla (theta_nabla) ∧
      cqc.q = q ∧ cqc.qinv = qinv ∧
      HEq cqc.nabla_q
        (qinv • nabla + (1 - qinv) • (xi_contract_nabla ≫ theta_nabla)) :=
  ⟨{ A := A
     Omega1 := Omega1
     nabla := nabla
     xi_contract_nabla := xi_contract_nabla
     theta_nabla := theta_nabla
     q := q
     qinv := qinv
     q_unit := q_unit
     nabla_q := qinv • nabla + (1 - qinv) • (xi_contract_nabla ≫ theta_nabla)
     nabla_q_formula := rfl },
   rfl, rfl, HEq.rfl, HEq.rfl, HEq.rfl, rfl, rfl, HEq.rfl⟩

end QOU
