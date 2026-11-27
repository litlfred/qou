/-
# `U(1) = 3·lk` on two-strand torus links

Analytic half of `QOU.Observations.RingMassLinkingNumber`. With the ring mass
`m_n(q) = [3] q⁻ⁿ + (−1)ⁿ q^{−3n}` of the closure of `σ₁ⁿ`, the energy reading
`U = −q ∂_q log m` at `q = 1` is

* `uAtOne_even`: `U(1) = 3k` for `n = 2k`, the torus link `T(2, 2k)` with `lk = k`;
* `uAtOne_odd`: `U(1) = 0` for `n = 2k + 1`, a knot;
* `not_const_three`: so no constant (in particular not `N² − 1 = 3`) matches the family.

This is the two-strand case of the Jones-derivative identity `V′(1) = −3·lk·V(1)` (Murakami). The
general link case is not proved here.
-/
import QOU.Observations.RingMassLinkingNumber
import Mathlib.Analysis.Calculus.Deriv.Inv
import Mathlib.Analysis.Calculus.Deriv.Pow
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Tactic

namespace QOU.Transcendental.MassTheory.RingMassLinkingNumber

open QOU.Observations.RingMassLinkingNumber

/-- The ring mass of `σ₁ⁿ` as a real function of `q`. -/
noncomputable def massFn (n : ℕ) (x : ℝ) : ℝ := qInt3 x * x⁻¹ ^ n + (-1) ^ n * x⁻¹ ^ (3 * n)

theorem hasDerivAt_inv_pow_one (m : ℕ) :
    HasDerivAt (fun x : ℝ => x⁻¹ ^ m) (-(m : ℝ)) 1 := by
  have h := (hasDerivAt_inv (one_ne_zero : (1 : ℝ) ≠ 0)).pow m
  convert h using 1
  simp

theorem hasDerivAt_qInt3_one : HasDerivAt (fun x : ℝ => qInt3 x) 0 1 := by
  have h1 : HasDerivAt (fun x : ℝ => x ^ 2) 2 1 := by simpa using hasDerivAt_pow 2 (1 : ℝ)
  have h3 := hasDerivAt_inv_pow_one 2
  have := (h1.add_const 1).add h3
  unfold qInt3
  convert this using 1
  norm_num

/-- **`m_n′(1) = −3n(1 + (−1)ⁿ)`.** -/
theorem hasDerivAt_massFn_one (n : ℕ) :
    HasDerivAt (massFn n) (-(3 * n * (1 + (-1) ^ n))) 1 := by
  have h := (hasDerivAt_qInt3_one.mul (hasDerivAt_inv_pow_one n)).add
    ((hasDerivAt_inv_pow_one (3 * n)).const_mul ((-1 : ℝ) ^ n))
  unfold massFn
  convert h using 1
  unfold qInt3
  push_cast
  ring

/-- The energy reading at `q = 1`: `U(1) = −m′(1)/m(1)`. -/
noncomputable def uAtOne (n : ℕ) : ℝ := -(deriv (massFn n) 1) / massFn n 1

theorem massFn_one (n : ℕ) : massFn n 1 = 3 + (-1) ^ n := by
  unfold massFn qInt3; norm_num

theorem uAtOne_eq (n : ℕ) : uAtOne n = 3 * n * (1 + (-1) ^ n) / (3 + (-1) ^ n) := by
  unfold uAtOne
  rw [(hasDerivAt_massFn_one n).deriv, massFn_one, neg_neg]

/-- **`T(2, 2k)`, `lk = k`: `U(1) = 3k = 3·lk`.** -/
theorem uAtOne_even (k : ℕ) : uAtOne (2 * k) = 3 * k := by
  rw [uAtOne_eq, pow_mul]
  norm_num
  ring

/-- **Knots `T(2, 2k+1)`: `U(1) = 0`.** -/
theorem uAtOne_odd (k : ℕ) : uAtOne (2 * k + 1) = 0 := by
  rw [uAtOne_eq, pow_succ, pow_mul]
  norm_num

/-- The Hopf link gives the electron's `3`. -/
theorem uAtOne_hopf : uAtOne 2 = 3 := by
  simpa using uAtOne_even 1

/-- **No constant matches the family**: `U(1)` takes the values `3` (Hopf) and `6` (`T(2,4)`),
so the `3` is not `N² − 1`. -/
theorem not_const_three : ¬ ∀ k : ℕ, 1 ≤ k → uAtOne (2 * k) = 3 := by
  intro h
  have := h 2 (by norm_num)
  rw [uAtOne_even] at this
  norm_num at this

end QOU.Transcendental.MassTheory.RingMassLinkingNumber
