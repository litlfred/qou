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
  simp [genWronskian, wronskianMatrix]

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

/-! ### The crux of the general-`m` induction: derivative descent

The general converse (a vanishing Wronskian forces a **constant** dependence, any `m`) goes
classically like this: the vanishing determinant gives a kernel vector `c` over the
*function field*, so `∑ⱼ cⱼ · fⱼ⁽ⁱ⁾ = 0` for `i = 0, …, m−1`; one then shows the `cⱼ` are
constants, which is what upgrades a `K(X)`-dependence to the `K`-dependence wanted.

That upgrade is the mathematical content, and it is the lemma below. Everything else in the
induction is rank and minor bookkeeping over `RatFunc K`.

Stated over a plain commutative ring — no field, no characteristic hypothesis — because the
argument is only the product rule plus re-indexing. -/

/-- **Derivative descent.**  If a coefficient vector annihilates the first `k + 1`
derivative rows, its own derivative annihilates the first `k`.

Differentiating the `i`-th relation gives `∑ⱼ cⱼ′ fⱼ⁽ⁱ⁾ + ∑ⱼ cⱼ fⱼ⁽ⁱ⁺¹⁾ = 0`, and the
second sum *is* the `(i+1)`-st relation, hence zero — **which is exactly why the hypothesis
must reach one row further than the conclusion.**

Iterating this is what forces every `cⱼ` to be constant in the classical proof. -/
theorem sum_derivative_of_forall_sum_eq_zero {m : ℕ} (f c : Fin m → R[X]) (k : ℕ)
    (h : ∀ i, i ≤ k → ∑ j, c j * derivative^[i] (f j) = 0) :
    ∀ i, i < k → ∑ j, derivative (c j) * derivative^[i] (f j) = 0 := by
  intro i hi
  have hnext : ∑ j, c j * derivative^[i + 1] (f j) = 0 := h (i + 1) hi
  have hdiff : derivative (∑ j, c j * derivative^[i] (f j)) = 0 := by
    rw [h i (le_of_lt hi), map_zero]
  rw [map_sum] at hdiff
  simp only [derivative_mul] at hdiff
  rw [Finset.sum_add_distrib] at hdiff
  -- the second block is the `(i+1)`-st relation, re-indexed
  have h2 : ∑ j, c j * derivative (derivative^[i] (f j)) = 0 := by
    simpa [Function.iterate_succ_apply'] using hnext
  rw [h2, add_zero] at hdiff
  exact hdiff

/-- ⚠ **The hypothesis is satisfiable with a non-constant `c`**, so the lemma is not about
an empty range.

At `k = 0` the conclusion quantifies over `i < 0` and says nothing, so the content lives
entirely at `k ≥ 1` — and a reader could reasonably wonder whether the hypothesis can hold
that far with `c` non-constant, since for *independent* `f` it cannot. It can when the `f`
are dependent, which is exactly the situation the induction is in: `f = ![X, X]` with
`c = ![X, −X]` annihilates every derivative row. -/
theorem sum_derivative_descent_witness :
    ∀ i, i < 3 → ∑ j, derivative ((![X, -X] : Fin 2 → ℚ[X]) j)
      * derivative^[i] ((![X, X] : Fin 2 → ℚ[X]) j) = 0 :=
  sum_derivative_of_forall_sum_eq_zero _ _ 3 (by intro i _; simp [Fin.sum_univ_two])

/-- **The Wronskian combination of a kernel vector is again a kernel vector** (one row
shorter), and its `l`-th entry is zero.

`∑ⱼ W(c_l, cⱼ) · fⱼ⁽ⁱ⁾ = c_l · (∑ⱼ cⱼ′ fⱼ⁽ⁱ⁾) − c_l′ · (∑ⱼ cⱼ fⱼ⁽ⁱ⁾)`, and both brackets
vanish — the first by derivative descent, the second by hypothesis.

⚠ **This is what removes the need for the function field.**  The classical proof normalises
the kernel vector so that its last entry is `1`, which requires dividing and so forces the
argument into `RatFunc K`.  Multiplying by `c_l` instead of dividing achieves the same
cancellation inside `R[X]`, and the resulting entries are literally `wronskian (c l) (c j)`
— so `exists_dependence_of_wronskian_eq_zero` above applies to them directly. -/
theorem sum_wronskian_combo_eq_zero {m : ℕ} (f c : Fin m → R[X]) (k : ℕ) (l : Fin m)
    (h : ∀ i, i ≤ k → ∑ j, c j * derivative^[i] (f j) = 0) :
    ∀ i, i < k → ∑ j, wronskian (c l) (c j) * derivative^[i] (f j) = 0 := by
  intro i hi
  have hdesc := sum_derivative_of_forall_sum_eq_zero f c k h i hi
  have horig := h i (le_of_lt hi)
  have expand : ∑ j, wronskian (c l) (c j) * derivative^[i] (f j)
      = c l * (∑ j, derivative (c j) * derivative^[i] (f j))
        - derivative (c l) * (∑ j, c j * derivative^[i] (f j)) := by
    rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_sub_distrib]
    exact Finset.sum_congr rfl fun j _ => by simp only [wronskian]; ring
  rw [expand, hdesc, horig, mul_zero, mul_zero, sub_zero]

/-! ### Next

**The general-`m` converse now has a route that stays inside `R[X]`.**  Earlier notes in
this file said it needs the ratio argument in `RatFunc K`; with `sum_wronskian_combo_eq_zero`
it does not.  Sketch, with the pieces that exist marked:

1. `genWronskian f = 0` over the domain `K[X]` gives a non-zero kernel vector `c` in
   `K[X]^m` — `Matrix.exists_mulVec_eq_zero_iff`, the same lemma the forward direction uses.
2. Induct on `m`.  If `W(f₁ … f_{m−1}) = 0`, the inductive hypothesis finishes.  Otherwise
   that minor is invertible, which forces `c_m ≠ 0`.
3. **[proved]** `sum_wronskian_combo_eq_zero` gives a kernel vector for the shorter system
   whose `m`-th entry is `0`; invertibility of the minor makes it **zero**, i.e.
   `wronskian (c_m) (c_j) = 0` for every `j`.
4. **[proved]** `exists_dependence_of_wronskian_eq_zero` turns each of those into
   `c_j = λ_j · c_m` with `λ_j` constant.
5. Substituting, `c_m · (∑ⱼ λⱼ fⱼ) = 0`, and `c_m ≠ 0` in a domain gives the constant
   dependence.

So steps 3 and 4 — the two that carry the mathematics — are done, and what is left is the
matrix bookkeeping of steps 1, 2 and 5.  **This is a materially smaller job than the
`RatFunc` route it replaces**, and it is why the `m = 2` case was worth proving first:
step 4 consumes it directly.

Also still open, and materially harder:

* it is **false in characteristic `p`** for the naive derivative (`xᵖ` has every derivative
  zero, so `1, xᵖ` are independent with vanishing Wronskian), so it needs characteristic
  zero or a restatement over Hasse derivatives;
* in several variables it needs *generalized* operators — products of partials of bounded
  total order — not just the iterated single derivative used here, and a choice of which
  `m` of them to take.

Stated rather than assumed, so nothing downstream can quietly consume it. -/

end Polynomial
