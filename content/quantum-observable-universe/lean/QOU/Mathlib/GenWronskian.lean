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

  The converse — a vanishing Wronskian forces a dependence — is proved here **at `m = 2`
  over a characteristic-zero field** (`exists_dependence_of_wronskian_eq_zero`), which is the
  base case of the induction the general statement needs.

  ⚠ **General `m` is not proved.**  The induction step needs the ratio argument in the
  function field and is materially harder.  Characteristic zero is not a convenience: in
  characteristic `p` the statement is outright false for the naive derivative, since `xᵖ`
  has all derivatives zero, so `1, xᵖ` are independent with vanishing Wronskian.
-/
import Mathlib.LinearAlgebra.Matrix.ToLinearEquiv
import Mathlib.RingTheory.Polynomial.Wronskian
import Mathlib.RingTheory.EuclideanDomain
import Mathlib.RingTheory.Polynomial.Content

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

/-! ### The converse at `m = 2`, in characteristic zero

The base case of the induction the general statement needs. Mathlib already supplies the
two facts that make it short — `IsCoprime.wronskian_eq_zero_iff` (for coprime arguments the
Wronskian vanishes exactly when both derivatives do) and `eq_C_of_derivative_eq_zero` (in
characteristic zero a polynomial with zero derivative is constant). What is missing is the
reduction to the coprime case, which is the scaling identity below. -/

/-- **The Wronskian scales quadratically under a common factor**: `W(ga, gb) = g² W(a, b)`.

This is what reduces the general case to the coprime one — divide out the gcd. -/
theorem wronskian_mul_mul (g a b : R[X]) :
    wronskian (g * a) (g * b) = g ^ 2 * wronskian a b := by
  simp only [wronskian, derivative_mul]
  ring

/-- **The converse at `m = 2` in characteristic zero:** a vanishing Wronskian forces a
linear dependence with constant coefficients.

Divide by the gcd to reach coprime `a₁, b₁`; the scaling identity kills `g²`, so
`W(a₁, b₁) = 0`; coprimality turns that into `a₁' = b₁' = 0`; characteristic zero makes both
constant; and `b₁ · a − a₁ · b = 0` is then the dependence.

⚠ Stated for a **field** because the gcd step needs one. The general-`m` statement, which
Roth's lemma actually consumes, is an induction with this as its base — and the induction
step is materially harder, needing the ratio argument in the function field. -/
theorem exists_dependence_of_wronskian_eq_zero {K : Type*} [Field K] [CharZero K]
    [DecidableEq K] {a b : K[X]} (ha : a ≠ 0) (hw : wronskian a b = 0) :
    ∃ c d : K, c ≠ 0 ∧ C c * b + C d * a = 0 := by
  -- `b = 0` is degenerate: the dependence is `1 · b + 0 · a = 0`.
  by_cases hb : b = 0
  · exact ⟨1, 0, one_ne_zero, by simp [hb]⟩
  -- ⚠ `isCoprime_div_gcd_div_gcd` needs the SECOND argument non-zero, and uses
  -- `GCDMonoid.gcd`, not `EuclideanDomain.gcd`.  Hence the split on `b`, not on `a`.
  set g := GCDMonoid.gcd a b with hg
  have hgne : g ≠ 0 := gcd_ne_zero_of_right hb
  set a₁ := a / g with ha₁def
  set b₁ := b / g with hb₁def
  have hga : g * a₁ = a := EuclideanDomain.mul_div_cancel' hgne (gcd_dvd_left a b)
  have hgb : g * b₁ = b := EuclideanDomain.mul_div_cancel' hgne (gcd_dvd_right a b)
  have hcop : IsCoprime a₁ b₁ := isCoprime_div_gcd_div_gcd hb
  -- the scaling identity turns the hypothesis into a statement about the coprime pair
  have hw₁ : wronskian a₁ b₁ = 0 := by
    have : g ^ 2 * wronskian a₁ b₁ = 0 := by
      rw [← wronskian_mul_mul, hga, hgb]; exact hw
    exact (mul_eq_zero.mp this).resolve_left (pow_ne_zero 2 hgne)
  obtain ⟨hda, hdb⟩ := hcop.wronskian_eq_zero_iff.mp hw₁
  -- characteristic zero: zero derivative means constant
  have hac : a₁ = C (a₁.coeff 0) := eq_C_of_derivative_eq_zero hda
  have hbc : b₁ = C (b₁.coeff 0) := eq_C_of_derivative_eq_zero hdb
  have ha₁ne : a₁ ≠ 0 := fun h => ha (by rw [← hga, h, mul_zero])
  refine ⟨a₁.coeff 0, -(b₁.coeff 0), ?_, ?_⟩
  · intro h
    exact ha₁ne (by rw [hac, h, map_zero])
  · rw [map_neg, ← hga, ← hgb, ← hac, ← hbc]
    ring

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
