import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Algebra.Polynomial.Monomial
import Mathlib.Tactic

/-!
# Is the GB rewriting map a differential? (`prop:gb-spectral-sequence`)

`prop:gb-spectral-sequence` (mass-endomorphism) opens by defining
`d = d_H + d_F + d_YB` as the sum of the three Gröbner–Shirshov rewriting rules
of the Hecke normal form, `d_H(σᵢ²) = (q − q⁻¹)σᵢ + 1` among them, and asserts
`d ∘ d = 0`. This file tests that assertion under the two natural readings of
"apply the rewriting rule" as a linear map on words, restricted to the
single-generator words `σᵏ` (encoded as `Xᵏ` in `R[X]`, with `h = q − q⁻¹`):

* **leftmost:** rewrite the first `σσ` (`dLeft`);
* **all occurrences:** sum the rewrites of every `σσ` (`dAll`).

Both give `d(d(σ³)) ≠ 0` whenever `h ≠ 0` (resp. `2h ≠ 0`):
`dLeft (dLeft σ³) = h²σ + h` and `dAll (dAll σ³) = 2h²σ + 2h`.

## Scope (read before citing)

This refutes `d ∘ d = 0` **for the rewriting map as the definition paragraph
states it**, scope (a): this construction, read either way, is not a
differential. It does **not** touch the block's proof, which silently switches
to the standard Hochschild differential on `C^k = Hom(Hₙ^{⊗k}, Hₙ)`, where
`d ∘ d = 0` is the classical theorem. The defect is that the block's definition
and its proof name different objects. Bean `qou-6qbv`.
-/

open Polynomial

namespace QOU.BraidKnot.GBRewriteDifferential

variable {R : Type*} [CommRing R]

/-- Leftmost Hecke rewrite on the single-generator word `σ^k` (encoded `X^k`). -/
-- Ref: [leitner2026] mass-endomorphism/gb-spectral-sequence
noncomputable def dLeftMon (h : R) (k : ℕ) : R[X] :=
  if 2 ≤ k then C h * X ^ (k - 1) + X ^ (k - 2) else 0

noncomputable def dLeft (h : R) (p : R[X]) : R[X] :=
  p.sum fun k a => C a * dLeftMon h k

theorem dLeft_X_pow (h : R) (k : ℕ) : dLeft h (X ^ k) = dLeftMon h k := by
  unfold dLeft
  rw [← monomial_one_right_eq_X_pow, sum_monomial_index]
  · simp
  · simp

theorem dLeft_dLeft_X_cubed (h : R) :
    dLeft h (dLeft h (X ^ 3)) = C (h ^ 2) * X + C h := by
  rw [dLeft_X_pow]
  have : dLeftMon h 3 = C h * X ^ 2 + X ^ 1 := by simp [dLeftMon]
  rw [this]
  unfold dLeft
  rw [sum_add_index]
  · rw [show C h * X ^ 2 = monomial 2 h by simp [C_mul_X_pow_eq_monomial],
        ← monomial_one_right_eq_X_pow, sum_monomial_index, sum_monomial_index]
    · simp [dLeftMon]; ring
    · simp
    · simp
  · simp
  · intro n a b; simp [add_mul]

theorem dLeft_sq_ne_zero (h : R) (hh : h ≠ 0) :
    dLeft h (dLeft h (X ^ 3)) ≠ 0 := by
  rw [dLeft_dLeft_X_cubed]
  intro H
  have := congrArg (fun p => coeff p 0) H
  simp at this
  exact hh this

/-- Sum over all occurrences of `σσ` in `σ^k`: there are `k - 1` of them, each
rewritten to `hσ + 1` in place. -/
noncomputable def dAllMon (h : R) (k : ℕ) : R[X] :=
  if 2 ≤ k then ((k - 1 : ℕ) : R) • (C h * X ^ (k - 1) + X ^ (k - 2)) else 0

noncomputable def dAll (h : R) (p : R[X]) : R[X] :=
  p.sum fun k a => C a * dAllMon h k

theorem dAll_X_pow (h : R) (k : ℕ) : dAll h (X ^ k) = dAllMon h k := by
  unfold dAll
  rw [← monomial_one_right_eq_X_pow, sum_monomial_index]
  · simp
  · simp

theorem dAll_dAll_X_cubed (h : R) :
    dAll h (dAll h (X ^ 3)) = C (2 * h ^ 2) * X + C (2 * h) := by
  rw [dAll_X_pow]
  have : dAllMon h 3 = C (2 * h) * X ^ 2 + C 2 * X ^ 1 := by
    simp [dAllMon, smul_eq_C_mul]; ring
  rw [this]
  unfold dAll
  rw [sum_add_index]
  · rw [C_mul_X_pow_eq_monomial, C_mul_X_pow_eq_monomial, sum_monomial_index,
        sum_monomial_index]
    · simp [dAllMon]; ring
    · simp
    · simp
  · simp
  · intro n a b; simp [add_mul]

theorem dAll_sq_ne_zero (h : R) (hh : (2 : R) * h ≠ 0) :
    dAll h (dAll h (X ^ 3)) ≠ 0 := by
  rw [dAll_dAll_X_cubed]
  intro H
  have := congrArg (fun p => coeff p 0) H
  simp at this
  exact hh this

end QOU.BraidKnot.GBRewriteDifferential
