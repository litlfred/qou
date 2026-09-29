import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Category.Basic
import Mathlib.CategoryTheory.Linear.Basic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.CategoricalQConnection

The `q`-deformed connection:
`∇_q = q⁻¹ ∇ + (1 − q⁻¹)(ξ ⌟ ∇) θ_A`.

Extracted from folio/quantum-observable-universe/lean/ for content-block co-location.
Source: folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverse.lean (monolithic)

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

open CategoryTheory MonoidalCategory

namespace QOU

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

universe u v

/-- **Categorical q-deformed connection**.

    Given a connection `∇ : A → A ⊗ Ω¹` and the Reeb derivation `ξ`,
    the q-deformed connection is:
    `∇_q = q⁻¹ · ∇ + (1 − q⁻¹) · (ξ ⌟ ∇) · θ_A`

    At `q = 1`, `∇_q = ∇`.

    LaTeX: `\label{def:categorical-q-connection}`
    Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443 -/
structure CategoricalQConnection (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [Preadditive C] [Linear R_q C] where
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
  /-- The deformation parameter `q`. -/
  q : R_q
  /-- The inverse `q⁻¹` as an element of the ring `R_q = ℤ[q, q⁻¹]`.
      (`R_q` is not a field, so `q⁻¹` is carried as an explicit element
      satisfying `q * q_inv = 1`, e.g. `q_param` and `q_inv_param`.) -/
  q_inv : R_q
  /-- `q_inv` is a two-sided inverse of `q` in `R_q`. -/
  q_mul_inv : q * q_inv = 1

/-- The q-deformed connection morphism `∇_q : A → A ⊗ Ω¹`.

    `∇_q = q⁻¹ · ∇ + (1 − q⁻¹) · (ξ ⌟ ∇) · θ` -/
noncomputable def CategoricalQConnection.nabla_q {C : Type u}
    [Category.{v} C] [MonoidalCategory C] [Preadditive C] [Linear R_q C]
    (cqc : CategoricalQConnection C) : cqc.A ⟶ (cqc.A ⊗ cqc.Omega1) :=
  cqc.q_inv • cqc.nabla + (1 - cqc.q_inv) • (cqc.xi_contract_nabla ≫ cqc.theta_nabla)

/-- At `q = 1`, the q-connection reduces to the classical connection. -/
theorem CategoricalQConnection.nabla_q_classical {C : Type u}
    [Category.{v} C] [MonoidalCategory C] [Preadditive C] [Linear R_q C]
    (cqc : CategoricalQConnection C) (hq : cqc.q = 1) :
    cqc.nabla_q = cqc.nabla := by
  have hinv : cqc.q_inv = 1 := by
    have := cqc.q_mul_inv
    rw [hq, one_mul] at this
    exact this
  simp [nabla_q, hinv, sub_self, zero_smul, one_smul, add_zero]

end

end QOU
