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
import Mathlib.LinearAlgebra.Matrix.Nondegenerate
import Mathlib.LinearAlgebra.LinearIndependent.Basic

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

/-! ### Towards the converse: the coefficient minor

The converse asks for an operator family witnessing independence.  The linear algebra under
it does not mention derivatives at all: a family of polynomials is independent over the base
field exactly when some `m × m` minor of its **coefficient** matrix is non-singular.  That is
proved here in full; what remains to reach the Wronskian converse is the bridge from
coefficient functionals to differential operators, which in characteristic zero is a diagonal
rescaling by factorials. -/

section CoeffMinor

variable {K : Type*} [Field K]

/-- The matrix of coefficients of `f` at the multi-indices `α`. -/
noncomputable def coeffMatrix {m : ℕ} (α : Fin m → (σ →₀ ℕ)) (f : Fin m → MvPolynomial σ K) :
    Matrix (Fin m) (Fin m) K :=
  Matrix.of fun i j => coeff (α i) (f j)

/-- **An independent family has a non-singular coefficient minor.**

Induction on `m`, by cofactor expansion along the new row. If *every* extension of the
inductive minor were singular, the cofactors along that row would give a fixed linear
relation `∑ⱼ cⱼ · coeff β (fⱼ) = 0` holding at **every** multi-index `β` — and a relation
holding at every coefficient is a relation between the polynomials themselves. The cofactor
in the last column is the inductive minor, so `c` is not the zero vector, contradicting
independence.

⚠ The cofactors must not depend on `β`, which is why the expansion is along the *last* row:
deleting it removes every entry `β` occurs in. -/
theorem exists_coeffMatrix_det_ne_zero :
    ∀ {m : ℕ} (f : Fin m → MvPolynomial σ K), LinearIndependent K f →
      ∃ α : Fin m → (σ →₀ ℕ), (coeffMatrix α f).det ≠ 0 := by
  intro m
  induction m with
  | zero =>
    intro f _
    exact ⟨fun i => i.elim0, by simp [coeffMatrix]⟩
  | succ n ih =>
    intro f hf
    have hinit : LinearIndependent K (Fin.init f) :=
      hf.comp Fin.castSucc (Fin.castSucc_injective n)
    obtain ⟨α', hα'⟩ := ih (Fin.init f) hinit
    by_contra hcon
    push_neg at hcon
    set N : (σ →₀ ℕ) → Matrix (Fin (n+1)) (Fin (n+1)) K :=
      fun β => coeffMatrix (Fin.snoc α' β) f with hN
    set c : Fin (n+1) → K :=
      fun j => (-1) ^ ((Fin.last n : ℕ) + (j : ℕ)) *
        ((N 0).submatrix (Fin.last n).succAbove j.succAbove).det with hc
    have hsub : ∀ (β : σ →₀ ℕ) (j : Fin (n+1)),
        (N β).submatrix (Fin.last n).succAbove j.succAbove
          = (N 0).submatrix (Fin.last n).succAbove j.succAbove := by
      intro β j
      ext i k
      simp [hN, coeffMatrix, Fin.succAbove_last, Fin.snoc_castSucc]
    have hexp : ∀ β : σ →₀ ℕ, (N β).det = ∑ j, c j * coeff β (f j) := by
      intro β
      rw [Matrix.det_succ_row (N β) (Fin.last n)]
      refine Finset.sum_congr rfl fun j _ => ?_
      rw [hsub β j, hc]
      have hentry : N β (Fin.last n) j = coeff β (f j) := by
        simp [hN, coeffMatrix, Fin.snoc_last]
      rw [hentry]
      ring
    have hzero : ∑ j, c j • f j = 0 := by
      ext β
      have hβ := hexp β
      rw [hcon (Fin.snoc α' β)] at hβ
      simpa [coeff_sum, coeff_smul, smul_eq_mul] using hβ.symm
    have hlast : c (Fin.last n) ≠ 0 := by
      have hminor : (N 0).submatrix (Fin.last n).succAbove (Fin.last n).succAbove
          = coeffMatrix α' (Fin.init f) := by
        ext i k
        simp [hN, coeffMatrix, Fin.succAbove_last, Fin.snoc_castSucc, Fin.init]
      have hsign : (-1 : K) ^ ((Fin.last n : ℕ) + ((Fin.last n : ℕ))) = 1 := by
        rw [← two_mul, pow_mul]; norm_num
      rw [hc]
      simp only [hminor, hsign, one_mul]
      exact hα'
    exact hlast (Fintype.linearIndependent_iff.mp hf c hzero (Fin.last n))

/-- A non-singular coefficient minor certifies independence. -/
theorem linearIndependent_of_coeffMatrix_det_ne_zero {m : ℕ} (α : Fin m → (σ →₀ ℕ))
    (f : Fin m → MvPolynomial σ K) (h : (coeffMatrix α f).det ≠ 0) :
    LinearIndependent K f := by
  classical
  rw [Fintype.linearIndependent_iff]
  intro c hc
  have hker : coeffMatrix α f *ᵥ c = 0 := by
    funext i
    have hi : coeff (α i) (∑ j, c j • f j) = 0 := by rw [hc]; simp
    rw [coeff_sum] at hi
    simp only [Matrix.mulVec, dotProduct, coeffMatrix, Matrix.of_apply, Pi.zero_apply]
    rw [← hi]
    exact Finset.sum_congr rfl fun j _ => by rw [coeff_smul, smul_eq_mul]; ring
  intro i
  exact congrFun (Matrix.eq_zero_of_mulVec_eq_zero h hker) i

/-- **Independence is exactly a non-singular coefficient minor.** -/
theorem linearIndependent_iff_exists_coeffMatrix_det_ne_zero {m : ℕ}
    (f : Fin m → MvPolynomial σ K) :
    LinearIndependent K f ↔ ∃ α : Fin m → (σ →₀ ℕ), (coeffMatrix α f).det ≠ 0 :=
  ⟨exists_coeffMatrix_det_ne_zero f, fun ⟨α, h⟩ =>
    linearIndependent_of_coeffMatrix_det_ne_zero α f h⟩

end CoeffMinor

/-! ### Next

The **converse** — some generalized Wronskian is non-zero whenever the family is
independent — now has its linear algebra done (`exists_coeffMatrix_det_ne_zero`). What is
left is a bridge, not another existence argument:

1. `coeff γ (pderiv j g) = (γⱼ + 1) · coeff (γ + eⱼ) g`, iterated along a list, giving
   `coeff 0 (pderivList l g) = c_l · coeff (multi-index of l) g` with `c_l` a positive
   integer depending only on `l`.
2. Every multi-index is the multi-index of some list, so the `α` produced above can be
   realised by an operator family `D`.
3. `eval 0` is a ring hom and `eval 0 P = coeff 0 P`, so it commutes with `det`
   (`RingHom.map_det`). The resulting matrix is `diagonal (c_{D i}) * coeffMatrix α f`,
   whose determinant is `(∏ᵢ c_{D i}) · det (coeffMatrix α f) ≠ 0` — **in characteristic
   zero**, where the positive integers `c` stay invertible.

So the Wronskian is non-zero because it is non-zero *at the origin*.

⚠ Step 3 is exactly where characteristic zero enters, and it is not removable by care: in
characteristic `p` the factorials `c_l` can vanish in `K`, which is the same failure that
makes the univariate converse false there. A characteristic-free statement needs Hasse
derivatives, whose whole point is to carry the `1/α!` already divided out. -/

end MvPolynomial
