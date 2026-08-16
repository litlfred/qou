/-
  **Generalized Wronskians** — the `m × m` determinant of iterated derivatives.

  Bean `qou-br3w`, second Roth prerequisite.  ⚠ Mathlib-style, Mathlib imports only, no QOU
  dependency: liftable verbatim.

  ═══ WHAT MATHLIB HAS, AND WHAT IT DOES NOT ═══

  `Mathlib/RingTheory/Polynomial/Wronskian.lean` defines the Wronskian of **two**
  polynomials, `W(a,b) = a·b' − a'·b`, and proves the Mason–Stothers material over it.
  Roth's lemma needs the `m`-polynomial version — the determinant of the matrix whose
  `i`-th row is the `i`-th derivative — and that is not there.

  This file supplies it, and `genWronskian_two` checks the two cases agree, so the
  generalisation is pinned to the existing definition rather than merely resembling it.

  ═══ WHY ROTH NEEDS IT ═══

  Roth's lemma is an induction on the number of variables.  The step needs to know that a
  family of polynomials is linearly **independent**, and the standard certificate for that
  is a non-vanishing generalized Wronskian.  The direction actually used is the
  contrapositive of `genWronskian_eq_zero_of_dependent` below: a non-zero Wronskian forces
  independence.

  ⚠ The converse — independence forces *some* generalized Wronskian to be non-zero — is the
  harder half, needs characteristic zero (or Hasse derivatives), and is **not** proved here.
  It is stated as the next target rather than assumed, because in characteristic `p` it is
  outright false for the naive derivative: `x^p` has all derivatives zero.
-/
import Mathlib.LinearAlgebra.Matrix.ToLinearEquiv
import Mathlib.RingTheory.Polynomial.Wronskian

namespace Polynomial

variable {R : Type*} [CommRing R]

/-- The **Wronskian matrix** of `m` polynomials: entry `(i, j)` is the `i`-th derivative of
`f j`, so row `i` is the `i`-th derivative of the whole family. -/
noncomputable def wronskianMatrix {m : ℕ} (f : Fin m → R[X]) :
    Matrix (Fin m) (Fin m) R[X] :=
  Matrix.of fun i j => derivative^[(i : ℕ)] (f j)

@[simp]
theorem wronskianMatrix_apply {m : ℕ} (f : Fin m → R[X]) (i j : Fin m) :
    wronskianMatrix f i j = derivative^[(i : ℕ)] (f j) := rfl

/-- The **generalized Wronskian** of `m` polynomials. -/
noncomputable def genWronskian {m : ℕ} (f : Fin m → R[X]) : R[X] :=
  (wronskianMatrix f).det

/-- ⚠ **Agreement with Mathlib's two-polynomial Wronskian.**

Without this the generalisation would only *resemble* the existing definition. With it, the
`m = 2` case is pinned: `genWronskian ![a, b] = wronskian a b` on the nose. -/
theorem genWronskian_two (a b : R[X]) : genWronskian ![a, b] = wronskian a b := by
  simp [genWronskian, wronskianMatrix, Matrix.det_fin_two, wronskian]
  ring

/-- A one-polynomial Wronskian is the polynomial itself. -/
@[simp]
theorem genWronskian_one (a : R[X]) : genWronskian ![a] = a := by
  simp [genWronskian, wronskianMatrix, Matrix.det_fin_one]

/-- **A linear dependence kills the generalized Wronskian.**

If `∑ⱼ cⱼ · fⱼ = 0` with the constants `c` not all zero, then differentiating `i` times
gives `∑ⱼ cⱼ · fⱼ⁽ⁱ⁾ = 0` for every `i` — that is exactly the statement that the constant
vector `c` is in the kernel of the Wronskian matrix, so the determinant vanishes.

The contrapositive is what Roth's lemma consumes: a non-zero generalized Wronskian
certifies linear independence. -/
theorem genWronskian_eq_zero_of_dependent {m : ℕ} [IsDomain R] (f : Fin m → R[X])
    (c : Fin m → R) (hc : c ≠ 0) (h : ∑ j, C (c j) * f j = 0) :
    genWronskian f = 0 := by
  classical
  -- the constant vector, viewed in `R[X]`
  set v : Fin m → R[X] := fun j => C (c j) with hv
  have hvne : v ≠ 0 := by
    intro hzero
    apply hc
    funext j
    have : C (c j) = (0 : R[X]) := by rw [hv] at hzero; exact congrFun hzero j
    exact C_eq_zero.mp this
  refine (Matrix.exists_mulVec_eq_zero_iff.mp ⟨v, hvne, ?_⟩)
  funext i
  -- `(W *ᵥ v) i = ∑ⱼ fⱼ⁽ⁱ⁾ · cⱼ = (∑ⱼ cⱼ fⱼ)⁽ⁱ⁾ = 0`
  simp only [Matrix.mulVec, dotProduct, wronskianMatrix_apply, hv, Pi.zero_apply]
  have key : ∑ j, derivative^[(i : ℕ)] (f j) * C (c j)
      = derivative^[(i : ℕ)] (∑ j, C (c j) * f j) := by
    rw [iterate_derivative_sum]
    -- `iterate_derivative_C_mul` wants the constant on the LEFT, so commute after, not
    -- before: rewriting to `f j * C (c j)` first leaves no lemma to apply.
    exact Finset.sum_congr rfl fun j _ => by rw [iterate_derivative_C_mul, mul_comm]
  rw [key, h, iterate_derivative_zero]

/-- ⚠ **Non-vacuity: a non-zero generalized Wronskian occurs.**

`genWronskian_eq_zero_of_dependent` is used through its contrapositive — *non-zero
Wronskian ⟹ linearly independent* — which certifies nothing if the Wronskian is always
zero. It is not: `1` and `X` give the identity matrix and Wronskian `1`.

Worth pinning because the vanishing theorem alone is consistent with a definition that
returns `0` identically, and every downstream use would still typecheck. -/
theorem genWronskian_one_X : genWronskian (R := ℚ) ![1, X] = 1 := by
  simp [genWronskian, wronskianMatrix, Matrix.det_fin_two]

/-! ### Next

The converse — **linear independence forces some generalized Wronskian to be non-zero** —
is the half Roth's lemma also needs, and it is materially harder:

* it is **false in characteristic `p`** for the naive derivative (`xᵖ` has every derivative
  zero, so `1, xᵖ` are independent with vanishing Wronskian), so it needs characteristic
  zero or a restatement over Hasse derivatives;
* in several variables it needs *generalized* operators — products of partials of bounded
  total order — not just the iterated single derivative used here, and a choice of which
  `m` of them to take.

Stated rather than assumed, so nothing downstream can quietly consume it. -/

end Polynomial
