import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.RingTheory.Multiplicity

/-!
# QOU.MathlibExt.LaurentTwoValuation — the `[2]_q`-adic valuation on `ℤ[q^{±1}]`

The corpus's `[2]_q`-adic valuation (`QCollatz.qTwoValuation`) is defined only on
`Polynomial ℤ` (multiplicity of the root `q = -1`). This file fills the
**Mathlib-gap** noted there (bean `qou-4atn`): the same valuation on the Laurent
ring `LaurentPolynomial ℤ = ℤ[q^{±1}]`, the Skein module where the `q`-Collatz
fundamental cycle `{q⁻¹, 1+q⁻¹}` lives.

The valuation is the `(q+1) = [2]_q`-adic multiplicity (`emultiplicity`). The key
inputs, all sorry-free:

* `[2]_q = q+1` is **not a unit** (it vanishes at `q = -1`, via the `eval₂`
  ring hom at the unit `-1`);
* so the fundamental-cycle values are `v_[2](q⁻¹) = 0` (a unit) and
  `v_[2](1+q⁻¹) = 1` (`1+q⁻¹ = q⁻¹·(q+1)`).

These are exactly the values the `q`-Collatz even-branch descent needs on the
attractor cycle: `C(1+q⁻¹) = q⁻¹` drops `v_[2]` from `1` to `0`.

Base ring is the fibre-level `ℤ[q^{±1}]` (§7c: no archimedean structure). -/

namespace QOU.MathlibExt.LaurentTwoValuation

open LaurentPolynomial

/-! ## Evaluation at `q = -1` and the non-unit lemma -/

/-- **Evaluation at `q = -1`** as a ring hom `ℤ[q^{±1}] → ℤ` (`-1` is a unit in
    `ℤ`, so `T ↦ -1` extends over the Laurent ring). -/
noncomputable def evalNegOne : LaurentPolynomial ℤ →+* ℤ :=
  eval₂ (RingHom.id ℤ) (-1 : ℤˣ)

/-- **Evaluation at `q = 1`** as a ring hom `ℤ[q^{±1}] → ℤ`. -/
noncomputable def evalOne : LaurentPolynomial ℤ →+* ℤ :=
  eval₂ (RingHom.id ℤ) (1 : ℤˣ)

theorem evalNegOne_T1_add_one : evalNegOne (T 1 + 1) = 0 := by
  unfold evalNegOne
  rw [map_add, map_one, eval₂_T]
  simp

theorem evalOne_T1_add_one : evalOne (T 1 + 1) = 2 := by
  unfold evalOne
  rw [map_add, map_one, eval₂_T]
  simp

/-- **`[2]_q = q+1` is not a unit in `ℤ[q^{±1}]`** — it vanishes at `q = -1`. -/
theorem T1_add_one_not_isUnit : ¬ IsUnit (T 1 + 1 : LaurentPolynomial ℤ) := by
  intro h
  have h2 : IsUnit (evalNegOne (T 1 + 1)) := h.map evalNegOne
  rw [evalNegOne_T1_add_one] at h2
  exact not_isUnit_zero h2

/-- **`[2]_q = q+1 ≠ 0`** in `ℤ[q^{±1}]` (its value at `q = 1` is `2`). -/
theorem T1_add_one_ne_zero : (T 1 + 1 : LaurentPolynomial ℤ) ≠ 0 := by
  intro h
  have := congrArg evalOne h
  rw [evalOne_T1_add_one, map_zero] at this
  norm_num at this

/-- `[2]_q` does not divide a unit — in particular not `T n`. -/
theorem not_T1_add_one_dvd_T (n : ℤ) :
    ¬ (T 1 + 1 : LaurentPolynomial ℤ) ∣ T n :=
  fun hd => T1_add_one_not_isUnit (isUnit_of_dvd_unit hd (isUnit_T n))

/-! ## The Laurent `[2]_q`-adic valuation and its cycle values -/

/-- The **`[2]_q`-adic valuation** on `ℤ[q^{±1}]`: the `(q+1)`-adic multiplicity. -/
noncomputable def laurentTwoVal (P : LaurentPolynomial ℤ) : ℕ∞ :=
  emultiplicity (T 1 + 1) P

/-- **`v_[2](q⁻¹) = 0`** — `q⁻¹ = T(-1)` is a unit, with no `[2]_q` factor. -/
theorem laurentTwoVal_qinv : laurentTwoVal (T (-1)) = 0 := by
  unfold laurentTwoVal
  have h : emultiplicity (T 1 + 1 : LaurentPolynomial ℤ) (T (-1)) = ((0 : ℕ) : ℕ∞) :=
    emultiplicity_eq_of_dvd_of_not_dvd (by rw [pow_zero]; exact one_dvd _)
      (by rw [pow_one]; exact not_T1_add_one_dvd_T (-1))
  exact_mod_cast h

/-- `1 + q⁻¹ = q⁻¹·(q+1)` — the odd-branch image of `q⁻¹` in the fundamental
    cycle, exhibiting the single `[2]_q` factor. -/
theorem one_add_qinv_eq : (1 + T (-1) : LaurentPolynomial ℤ) = (T 1 + 1) * T (-1) := by
  rw [add_mul, one_mul, ← T_add]
  simp [T_zero]

/-- **`v_[2](1+q⁻¹) = 1`** — the single `[2]_q` factor of `1+q⁻¹ = q⁻¹·(q+1)`. -/
theorem laurentTwoVal_one_add_qinv : laurentTwoVal (1 + T (-1)) = 1 := by
  unfold laurentTwoVal
  have hdvd : (T 1 + 1 : LaurentPolynomial ℤ) ^ 1 ∣ (1 + T (-1)) := by
    rw [pow_one, one_add_qinv_eq]
    exact Dvd.intro _ rfl
  have hnot : ¬ (T 1 + 1 : LaurentPolynomial ℤ) ^ 2 ∣ (1 + T (-1)) := by
    rw [one_add_qinv_eq, sq]
    intro hd
    rw [mul_dvd_mul_iff_left T1_add_one_ne_zero] at hd
    exact not_T1_add_one_dvd_T (-1) hd
  have h : emultiplicity (T 1 + 1 : LaurentPolynomial ℤ) (1 + T (-1)) = ((1 : ℕ) : ℕ∞) :=
    emultiplicity_eq_of_dvd_of_not_dvd hdvd hnot
  simpa using h

end QOU.MathlibExt.LaurentTwoValuation
