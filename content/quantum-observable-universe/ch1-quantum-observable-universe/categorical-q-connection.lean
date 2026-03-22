/-!
# QOU.CategoricalQConnection

The `q`-deformed connection:
`∇_q = q⁻¹ ∇ + (1 − q⁻¹)(ξ ⌟ ∇) θ_A`.

Extracted from lean-archive/ for content-block co-location.
Source: lean-archive/QOU/QuantumObservableUniverse.lean (monolithic)
-/

import Mathlib.CategoryTheory.Monoidal.Basic
import Mathlib.CategoryTheory.Category.Basic
import Mathlib.Data.Real.Basic

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- **Categorical q-deformed connection**.

    Given a connection `∇ : A → A ⊗ Ω¹` and the Reeb derivation `ξ`,
    the q-deformed connection is:
    `∇_q = q⁻¹ · ∇ + (1 − q⁻¹) · (ξ ⌟ ∇) · θ_A`

    At `q = 1`, `∇_q = ∇`.

    LaTeX: `\label{def:categorical-q-connection}`
    Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443 -/
structure CategoricalQConnection (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [Preadditive C] [Linear ℝ C] where
  /-- The Frobenius–Hopf object `A`. -/
  A : C
  /-- The object of 1-forms `Ω¹` in `C`. -/
  Omega1 : C
  /-- The classical connection `∇ : A → A ⊗ Ω¹`. -/
  nabla : A ⟶ (A ⊗ Omega1)
  /-- The contracted connection `ξ ⌟ ∇`, abstractly a morphism `A → A`. -/
  xi_contract_nabla : A ⟶ A
  /-- The canonical 1-form `θ_A` as a morphism `A → A ⊗ Ω¹`. -/
  theta_nabla : A ⟶ (A ⊗ Omega1)
  /-- The deformation parameter `q`, non-zero. -/
  q : ℝ
  q_ne_zero : q ≠ 0

/-- The q-deformed connection morphism `∇_q : A → A ⊗ Ω¹`.

    `∇_q = q⁻¹ · ∇ + (1 − q⁻¹) · (ξ ⌟ ∇) · θ` -/
noncomputable def CategoricalQConnection.nabla_q {C : Type u}
    [Category.{v} C] [MonoidalCategory C] [Preadditive C] [Linear ℝ C]
    (cqc : CategoricalQConnection C) : cqc.A ⟶ (cqc.A ⊗ cqc.Omega1) :=
  cqc.q⁻¹ • cqc.nabla + (1 - cqc.q⁻¹) • (cqc.xi_contract_nabla ≫ cqc.theta_nabla)

/-- At `q = 1`, the q-connection reduces to the classical connection. -/
theorem CategoricalQConnection.nabla_q_classical {C : Type u}
    [Category.{v} C] [MonoidalCategory C] [Preadditive C] [Linear ℝ C]
    (cqc : CategoricalQConnection C) (hq : cqc.q = 1) :
    cqc.nabla_q = cqc.nabla := by
  unfold nabla_q
  simp [hq, inv_one, sub_self, zero_smul, one_smul, add_zero]

end QOU
