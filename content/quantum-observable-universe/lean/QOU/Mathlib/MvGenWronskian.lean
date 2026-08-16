/-
  **Generalized Wronskians in several variables** — the determinant of a matrix of
  differential operators applied to `m` multivariate polynomials.

  Bean `qou-br3w`, third Roth prerequisite.  ⚠ Mathlib-style, Mathlib imports only, no QOU
  dependency: liftable verbatim.

  ═══ WHY THE UNIVARIATE VERSION IS NOT ENOUGH ═══

  `QOU.Mathlib.GenWronskian` builds the `m × m` determinant of *iterated single*
  derivatives, and proves the dependence criterion for it in full
  (`genWronskian_eq_zero_iff`).  Roth's lemma does not consume that: its auxiliary
  polynomial lives in `m` variables, and the independence certificate it needs is a
  determinant of **products of partials of bounded total order** — one operator per row,
  chosen, not canonical.

  This file supplies the several-variable object and the direction Roth's lemma actually
  uses.

  ═══ WHY THE OPERATOR FAMILY IS AN ARGUMENT ═══

  In one variable there is a canonical `i`-th row: apply `d/dx` `i` times.  In several
  variables there is no such choice, and the choice matters: taking the same operator twice
  gives a matrix with two equal rows, whose determinant vanishes whatever the polynomials
  are.  So `D : Fin m → List σ` is an explicit parameter, and the theorem below is *for
  every* `D` while the certificate it powers is *for some* `D`.

  `mvGenWronskian_one_X` pins that this is not vacuous — some family does give a non-zero
  determinant.

  ═══ WHY `pderivList` IS A LINEAR MAP ═══

  The operator is defined as a composite of `Derivation.toLinearMap`s rather than a raw
  function.  That is the whole trick: the Wronskian argument needs exactly that the operator
  carries a constant-coefficient combination through, and for a bundled linear map that is
  `map_sum` and `map_smul` rather than an induction.

  ⚠ **Characteristic.**  Ordinary partials are used, not Hasse derivatives.  That is correct
  for Roth, which lives over number fields, but it means the converse direction would be
  false in characteristic `p` for the same reason as in the univariate file.  Only the
  direction proved here is characteristic-free.
-/
import Mathlib.Algebra.MvPolynomial.PDeriv
import Mathlib.Algebra.MvPolynomial.CommRing
import Mathlib.LinearAlgebra.Matrix.ToLinearEquiv
import Mathlib.RingTheory.MvPolynomial.Basic

namespace MvPolynomial

open Matrix

variable {σ R : Type*} [CommRing R]

/-- Iterated partial derivative along a list of variables, **as a linear map** — which is
what makes the linearity the Wronskian argument needs free rather than proved. -/
noncomputable def pderivList (l : List σ) : MvPolynomial σ R →ₗ[R] MvPolynomial σ R :=
  l.foldr (fun j L => (pderiv j).toLinearMap ∘ₗ L) LinearMap.id

@[simp]
theorem pderivList_nil : pderivList (R := R) ([] : List σ) = LinearMap.id := rfl

@[simp]
theorem pderivList_cons (j : σ) (l : List σ) :
    pderivList (R := R) (j :: l) = (pderiv j).toLinearMap ∘ₗ pderivList l := rfl

/-- A differential operator carries a constant-coefficient combination through.

This is the only property of the operators the Wronskian argument uses — in particular it
never needs them to commute, which is why no ordering condition appears on `D`. -/
theorem pderivList_sum_C_mul {m : ℕ} (l : List σ) (c : Fin m → R)
    (f : Fin m → MvPolynomial σ R) :
    pderivList l (∑ j, C (c j) * f j) = ∑ j, C (c j) * pderivList l (f j) := by
  rw [map_sum]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [← smul_eq_C_mul, ← smul_eq_C_mul, map_smul]

/-- The **generalized Wronskian matrix** in several variables: entry `(i, j)` is the `i`-th
differential operator applied to `f j`. -/
noncomputable def mvWronskianMatrix {m : ℕ} (D : Fin m → List σ)
    (f : Fin m → MvPolynomial σ R) : Matrix (Fin m) (Fin m) (MvPolynomial σ R) :=
  Matrix.of fun i j => pderivList (D i) (f j)

@[simp]
theorem mvWronskianMatrix_apply {m : ℕ} (D : Fin m → List σ) (f : Fin m → MvPolynomial σ R)
    (i j : Fin m) : mvWronskianMatrix D f i j = pderivList (D i) (f j) := rfl

/-- The **generalized Wronskian** in several variables, against a chosen family of `m`
differential operators. -/
noncomputable def mvGenWronskian {m : ℕ} (D : Fin m → List σ)
    (f : Fin m → MvPolynomial σ R) : MvPolynomial σ R :=
  (mvWronskianMatrix D f).det

/-- **A constant linear dependence kills every generalized Wronskian.**

The direction Roth's lemma consumes, via its contrapositive: if *some* generalized
Wronskian is non-zero, the family is linearly independent over the constants.

The proof is the same one the univariate file uses — the constant vector sits in the kernel
of the matrix, so the determinant vanishes — and it works verbatim because
`pderivList_sum_C_mul` is all that was ever needed of the derivative. -/
theorem mvGenWronskian_eq_zero_of_dependent [IsDomain R] {m : ℕ} (D : Fin m → List σ)
    (f : Fin m → MvPolynomial σ R) (c : Fin m → R) (hc : c ≠ 0)
    (h : ∑ j, C (c j) * f j = 0) : mvGenWronskian D f = 0 := by
  classical
  set v : Fin m → MvPolynomial σ R := fun j => C (c j) with hv
  have hvne : v ≠ 0 := by
    intro hzero
    refine hc (_root_.funext fun j => ?_)
    have : C (c j) = (0 : MvPolynomial σ R) := congrFun hzero j
    exact C_eq_zero.mp this
  refine Matrix.exists_mulVec_eq_zero_iff.mp ⟨v, hvne, ?_⟩
  refine _root_.funext fun i => ?_
  simp only [Matrix.mulVec, dotProduct, mvWronskianMatrix, Matrix.of_apply, hv, Pi.zero_apply]
  have key : ∑ j, pderivList (D i) (f j) * C (c j)
      = pderivList (D i) (∑ j, C (c j) * f j) := by
    rw [pderivList_sum_C_mul]
    exact Finset.sum_congr rfl fun j _ => mul_comm _ _
  rw [key, h, map_zero]

/-- ⚠ **Non-vacuity.**  `mvGenWronskian_eq_zero_of_dependent` is used through its
contrapositive, which certifies nothing if every generalized Wronskian vanishes
identically.  It does not: against the operators `(id, ∂/∂x₀)` the family `(1, x₀)` gives
the identity matrix.

This also exhibits why `D` is *chosen* rather than canonical — with `D = (id, id)` the
matrix has two equal rows and the determinant vanishes for every family, dependent or not,
so a "for all `D`" independence certificate would be empty. -/
theorem mvGenWronskian_one_X :
    mvGenWronskian (R := ℚ) ![[], [0]] ![1, X 0] = 1 := by
  simp [mvGenWronskian, mvWronskianMatrix, Matrix.det_fin_two, Fin.isValue]

/-! ### Next

The converse — some generalized Wronskian is non-zero whenever the family is independent —
is the harder half and is **not** proved here. Unlike the univariate case it is not a
determinant identity: it requires exhibiting an operator family, which is where the
`m`-variable induction in Roth's lemma actually does its work.

Only the direction above is needed to *use* a Wronskian as an independence certificate; the
converse is needed to *find* one. -/

end MvPolynomial
