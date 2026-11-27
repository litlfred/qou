/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.LiftingDescent.FormalGroupLaw
import MathlibExt.MatrixCoefficientBialgebra
import Mathlib.Algebra.MvPolynomial.Basic
import Mathlib.RingTheory.TensorProduct.MvPolynomial

/-!
# The comultiplication of a formal group law

A formal group law `F` over `R` in `ι` coordinates makes `R⟦X⟧` a complete Hopf algebra: its
comultiplication is substitution, `Δ f = f(F(X ⊗ 1, 1 ⊗ X))`. It lands in the *completed*
tensor product `R⟦X⟧ ⊗̂ R⟦X⟧ = R⟦Fin 2 × ι⟧`, where `X (0, j)` is `X_j ⊗ 1` and `X (1, j)` is
`1 ⊗ X_j`.

* `FormalGroupLaw.comul` is `Δ`, and `comul_X` says `Δ X_j = F_j`.
* `comul_coassoc` is `(Δ ⊗̂ id) ∘ Δ = (id ⊗̂ Δ) ∘ Δ`, and it **is** the associativity axiom
  of `F`.
* `comul_counit_right` and `comul_counit_left` are the counit laws, and they **are** the unit
  axioms of `F`. They are stated with `R⟦Fin 1 × ι⟧` as the target, the form the unit axioms
  of `FormalGroupLaw` already take.

## Polynomial laws are matrix-coefficient coproducts

When `F` is a polynomial, `Δ` restricts to polynomials. For the affine law
`F = (X₀ + Y₀ + X₀Y₀, X₁ + Y₁ + X₀Y₁)`, the coordinates of `x ↦ (1 + u)x + b`, the restricted
`Δ` is the matrix-coefficient coproduct of `MatrixCoefficientBialgebra.lean` for the matrix
`((1 + X₀, X₁), (0, 1))`, and it is the only one (`affinePolyComul_unique`). The additive
law is the case of the matrix `((1, X), (0, 1))`; see
`MatrixCoefficientCoproducts.lean`. A general power-series law needs the infinite
triangular matrix of the powers of `F`, which is why it lives in the completed tensor product.

Generic commutative ring; no analysis; no axiom.
-/

set_option linter.unusedSectionVars false

namespace QOU.FormalGroups

open MvPowerSeries

noncomputable section

variable {R : Type*} [CommRing R] {ι : Type*} [Finite ι]

namespace FormalGroupLaw

variable (G : FormalGroupLaw R ι)

theorem hasSubst_F : HasSubst G.F := hasSubst_of_constantCoeff_zero G.noConst

/-- **The comultiplication** `Δ f = f(F(X ⊗ 1, 1 ⊗ X))`, into the completed tensor product. -/
def comul : MvPowerSeries ι R →ₐ[R] MvPowerSeries (Fin 2 × ι) R :=
  substAlgHom G.hasSubst_F

@[simp] theorem comul_X (j : ι) : G.comul (X j) = G.F j := by
  simp [comul, substAlgHom_apply, subst_X G.hasSubst_F]

/-- The tuple of `Δ ⊗̂ id`: `X (0, j) ↦ F_j(X₀, X₁)`, `X (1, j) ↦ X₂_j`. -/
def leftTuple : Fin 2 × ι → MvPowerSeries (Fin 3 × ι) R := fun p =>
  (![fun i => subst2 (coords 0) (coords 1) (G.F i), coords 2] :
    Fin 2 → ι → MvPowerSeries (Fin 3 × ι) R) p.1 p.2

/-- The tuple of `id ⊗̂ Δ`: `X (0, j) ↦ X₀_j`, `X (1, j) ↦ F_j(X₁, X₂)`. -/
def rightTuple : Fin 2 × ι → MvPowerSeries (Fin 3 × ι) R := fun p =>
  (![coords 0, fun i => subst2 (coords 1) (coords 2) (G.F i)] :
    Fin 2 → ι → MvPowerSeries (Fin 3 × ι) R) p.1 p.2

theorem hasSubst_leftTuple : HasSubst G.leftTuple :=
  hasSubst2 (noConst_subst2 (noConst_coords 0) (noConst_coords 1) G.noConst) (noConst_coords 2)

theorem hasSubst_rightTuple : HasSubst G.rightTuple :=
  hasSubst2 (noConst_coords 0) (noConst_subst2 (noConst_coords 1) (noConst_coords 2) G.noConst)

/-- `Δ ⊗̂ id`. -/
def comulLeft : MvPowerSeries (Fin 2 × ι) R →ₐ[R] MvPowerSeries (Fin 3 × ι) R :=
  substAlgHom G.hasSubst_leftTuple

/-- `id ⊗̂ Δ`. -/
def comulRight : MvPowerSeries (Fin 2 × ι) R →ₐ[R] MvPowerSeries (Fin 3 × ι) R :=
  substAlgHom G.hasSubst_rightTuple

/-- **Coassociativity** `(Δ ⊗̂ id) ∘ Δ = (id ⊗̂ Δ) ∘ Δ`; it is the associativity of `F`. -/
theorem comul_coassoc : G.comulLeft.comp G.comul = G.comulRight.comp G.comul := by
  ext1 f
  simp only [AlgHom.coe_comp, Function.comp_apply, comulLeft, comulRight, comul,
    substAlgHom_apply]
  rw [subst_comp_subst_apply G.hasSubst_F G.hasSubst_leftTuple,
    subst_comp_subst_apply G.hasSubst_F G.hasSubst_rightTuple]
  exact congrArg (fun a => subst a f) G.assoc

/-- The inclusion `R⟦X⟧ ≅ R⟦Fin 1 × ι⟧`, `X_j ↦ X (0, j)`. -/
def incl : MvPowerSeries ι R →ₐ[R] MvPowerSeries (Fin 1 × ι) R :=
  substAlgHom (hasSubst_of_constantCoeff_zero (noConst_coords (R := R) (ι := ι) (m := 1) 0))

/-- `id ⊗̂ ε`: set the second variable to zero. -/
def counitRight : MvPowerSeries (Fin 2 × ι) R →ₐ[R] MvPowerSeries (Fin 1 × ι) R :=
  substAlgHom (hasSubst2 (noConst_coords (R := R) (ι := ι) (m := 1) 0) noConst_zero)

/-- `ε ⊗̂ id`: set the first variable to zero. -/
def counitLeft : MvPowerSeries (Fin 2 × ι) R →ₐ[R] MvPowerSeries (Fin 1 × ι) R :=
  substAlgHom (hasSubst2 noConst_zero (noConst_coords (R := R) (ι := ι) (m := 1) 0))

/-- **Right counit law** `(id ⊗̂ ε) ∘ Δ = id`; it is `F(X, 0) = X`. -/
theorem comul_counit_right : (counitRight (R := R) (ι := ι)).comp G.comul = incl := by
  ext1 f
  simp only [AlgHom.coe_comp, Function.comp_apply, counitRight, comul, incl, substAlgHom_apply]
  rw [subst_comp_subst_apply G.hasSubst_F
    (hasSubst2 (noConst_coords (R := R) (ι := ι) (m := 1) 0) noConst_zero)]
  exact congrArg (fun a => subst a f) G.unit_left

/-- **Left counit law** `(ε ⊗̂ id) ∘ Δ = id`; it is `F(0, Y) = Y`. -/
theorem comul_counit_left : (counitLeft (R := R) (ι := ι)).comp G.comul = incl := by
  ext1 f
  simp only [AlgHom.coe_comp, Function.comp_apply, counitLeft, comul, incl, substAlgHom_apply]
  rw [subst_comp_subst_apply G.hasSubst_F
    (hasSubst2 noConst_zero (noConst_coords (R := R) (ι := ι) (m := 1) 0))]
  exact congrArg (fun a => subst a f) G.unit_right

/-- For the affine law, `Δ u = u ⊗ 1 + 1 ⊗ u + u ⊗ u` and `Δ b = b ⊗ 1 + 1 ⊗ b + u ⊗ b`. -/
theorem affine_comul_X (j : Fin 2) : (affine (R := R)).comul (X j) = affineF j :=
  comul_X _ j

end FormalGroupLaw

/-! ## The affine law on polynomials is a matrix-coefficient coproduct -/

section AffinePoly

open TensorProduct QOU.Coproduct

variable (R)

local notation "P" => MvPolynomial (Fin 2) R

/-- The affine law's `Δ` restricted to polynomials, in the algebraic tensor product. -/
def affinePolyComul : P →ₐ[R] P ⊗[R] P :=
  MvPolynomial.aeval fun j =>
    ![MvPolynomial.X 0 ⊗ₜ 1 + 1 ⊗ₜ MvPolynomial.X 0 + MvPolynomial.X 0 ⊗ₜ MvPolynomial.X 0,
      MvPolynomial.X 1 ⊗ₜ 1 + 1 ⊗ₜ MvPolynomial.X 1 + MvPolynomial.X 0 ⊗ₜ MvPolynomial.X 1] j

/-- The matrix `((1 + u, b), (0, 1))` of `x ↦ (1 + u) x + b`. -/
def affineMatrix : Matrix (Fin 2) (Fin 2) P :=
  Matrix.of ![![1 + MvPolynomial.X 0, MvPolynomial.X 1], ![0, 1]]

theorem affinePolyComul_isMatrixCoproduct :
    IsMatrixCoproduct (affineMatrix R) (affinePolyComul R) := by
  rw [isMatrixCoproduct_iff]
  intro i j
  fin_cases i <;> fin_cases j <;>
    simp [affineMatrix, affinePolyComul, Fin.sum_univ_two, add_tmul, tmul_add,
      Algebra.TensorProduct.one_def] <;> abel

theorem affine_present_surjective :
    Function.Surjective (present (R := R) (affineMatrix R)) := by
  rw [← AlgHom.range_eq_top, eq_top_iff, ← MvPolynomial.adjoin_range_X, Algebra.adjoin_le_iff]
  rintro _ ⟨j, rfl⟩
  fin_cases j
  · exact ⟨u R 0 0 - 1, by simp [affineMatrix]⟩
  · exact ⟨u R 0 1, by simp [affineMatrix]⟩

/-- The affine `Δ` is the only matrix-coefficient coproduct for `((1 + u, b), (0, 1))`. -/
theorem affinePolyComul_unique {Δ : P →ₐ[R] P ⊗[R] P}
    (h : IsMatrixCoproduct (affineMatrix R) Δ) : Δ = affinePolyComul R :=
  IsMatrixCoproduct.unique (affine_present_surjective R) h
    (affinePolyComul_isMatrixCoproduct R)

end AffinePoly

end

end QOU.FormalGroups
