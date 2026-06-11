import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Category.Basic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.CategoricalQLieBracket

The `q`-deformed Lie bracket on derivations of `A`:
`[X, Y]_q = q⁻¹ [X, Y] + (1 − q⁻¹)(θ(X)[ξ, Y] − θ(Y)[ξ, X])`.

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse.lean (monolithic)

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

open CategoryTheory MonoidalCategory

namespace QOU

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

universe u v

/-- **Categorical q-Lie bracket**.

    On derivations of the Frobenius–Hopf object `A`, the `q`-deformed Lie
    bracket is defined by:
    `[X, Y]_q = q⁻¹ [X, Y] + (1 − q⁻¹)(θ_A(X) [ξ, Y] − θ_A(Y) [ξ, X])`

    At `q = 1`, this recovers the classical commutator.

    LaTeX: `\label{def:categorical-q-lie-bracket}`
    Ref: [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9 -/
structure CategoricalQLieBracket (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [Preadditive C] [Linear R_q C] where
  /-- The Frobenius–Hopf object `A`. -/
  A : C
  /-- The classical Lie bracket `[−, −] : End(A) × End(A) → End(A)`. -/
  bracket : (A ⟶ A) → (A ⟶ A) → (A ⟶ A)
  /-- The Reeb derivation `ξ : A → A`. -/
  xi : A ⟶ A
  /-- The canonical 1-form `θ_A : A → 𝟙`, dual to `ξ`. -/
  theta : A ⟶ (𝟙_ C)
  /-- The deformation parameter `q`, non-zero. -/
  q : R_q
  q_ne_zero : q ≠ 0

/-- The q-deformed bracket evaluated on two derivations.

    `[X, Y]_q = q⁻¹ · [X, Y] + (1 − q⁻¹) · (θ(X) · [ξ, Y] − θ(Y) · [ξ, X])`

    In a preadditive ℝ-linear category, this is a well-defined endomorphism. -/
noncomputable def CategoricalQLieBracket.q_bracket {C : Type u}
    [Category.{v} C] [MonoidalCategory C] [Preadditive C] [Linear R_q C]
    (qlb : CategoricalQLieBracket C) (X Y : qlb.A ⟶ qlb.A) :
    qlb.A ⟶ qlb.A :=
  qlb.q⁻¹ • qlb.bracket X Y +
    (1 - qlb.q⁻¹) • (qlb.bracket qlb.xi Y - qlb.bracket qlb.xi X)

/-- At `q = 1`, the q-bracket reduces to the classical bracket. -/
theorem CategoricalQLieBracket.q_bracket_classical {C : Type u}
    [Category.{v} C] [MonoidalCategory C] [Preadditive C] [Linear R_q C]
    (qlb : CategoricalQLieBracket C) (hq : qlb.q = 1) (X Y : qlb.A ⟶ qlb.A) :
    qlb.q_bracket X Y = qlb.bracket X Y := by
  simp [q_bracket, hq, inv_one, sub_self, zero_smul, one_smul, add_zero]

end QOU
