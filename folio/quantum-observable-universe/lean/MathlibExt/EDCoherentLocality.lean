/-
  Locality on the exceptional divisor from spin-coherent overlaps.

  The exceptional divisor `𝒮_p ≅ ℙ¹ ≅ S²` (`def:exceptional-divisor`) is also the
  coadjoint orbit of `SU(2)` of radius `j`, i.e. the sphere of spin-`j`
  coherent states.  Two states at directions separated by the angle `γ` have
  overlap probability

      p_n(γ) = cos(γ/2)^(2n),     n = 2j  (a standard identity, Perelomov).

  This file proves the decay that makes the pre-collision interaction LOCAL on
  the divisor, with a neighbourhood that shrinks as the label grows:

  * `overlap_zero`   : `p_n(0) = 1`;
  * `overlap_le`     : `p_n(γ) ≤ (1 + γ²/4)^{-n}` for `|γ| ≤ π`;
  * `overlap_le_inv` : `p_n(γ) ≤ 1 / (1 + n γ²/4)`, so `p_n(γ) ≤ ε` as soon as
    `γ² ≥ 4 (1/ε − 1) / n` — the interaction lives within an angle
    `O(1/√n)` of coincidence.

  The overlap is fibre data on the divisor: it is not a base-level observable
  (`virtual-particles-exceptional-divisor`), which is the precise sense of
  "non-directly-observable behaviour before the collision".  The identity
  `p = cos^{2n}(γ/2)` is cited, not re-derived here.

  Archimedean (ℝ): real trigonometry.
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Bounds
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith

namespace QOU.Archimedean.EDCoherentLocality

open Real

/-- Spin-coherent overlap probability at angle `γ`, label `n = 2j`. -/
noncomputable def overlap (n : ℕ) (γ : ℝ) : ℝ := (Real.cos (γ / 2)) ^ (2 * n)

theorem overlap_zero (n : ℕ) : overlap n 0 = 1 := by
  simp [overlap]

/-- `cos² x ≤ 1/(x² + 1)` for `|x| ≤ π/2`. -/
theorem cos_sq_le {x : ℝ} (hx : |x| ≤ π / 2) : Real.cos x ^ 2 ≤ 1 / (x ^ 2 + 1) := by
  have h1 : -(3 * π / 2) ≤ x := by
    have := neg_abs_le x; linarith [Real.pi_pos]
  have h2 : x ≤ 3 * π / 2 := by
    have := le_abs_self x; linarith [Real.pi_pos]
  have hc := Real.cos_le_one_div_sqrt_sq_add_one h1 h2
  have hc0 : 0 ≤ Real.cos x := by
    apply Real.cos_nonneg_of_neg_pi_div_two_le_of_le
    · have := neg_abs_le x; linarith
    · have := le_abs_self x; linarith
  have hpos : 0 < x ^ 2 + 1 := by positivity
  have hs : (1 / Real.sqrt (x ^ 2 + 1)) ^ 2 = 1 / (x ^ 2 + 1) := by
    rw [div_pow, one_pow, Real.sq_sqrt hpos.le]
  calc Real.cos x ^ 2 ≤ (1 / Real.sqrt (x ^ 2 + 1)) ^ 2 := pow_le_pow_left₀ hc0 hc 2
    _ = 1 / (x ^ 2 + 1) := hs

/-- **Gaussian-type decay**: `p_n(γ) ≤ (1 + γ²/4)^{-n}` for `|γ| ≤ π`. -/
theorem overlap_le (n : ℕ) {γ : ℝ} (hγ : |γ| ≤ π) :
    overlap n γ ≤ (1 / (1 + γ ^ 2 / 4)) ^ n := by
  have hx : |γ / 2| ≤ π / 2 := by
    rw [abs_div, abs_two]; linarith
  have h := cos_sq_le hx
  have e : (γ / 2) ^ 2 + 1 = 1 + γ ^ 2 / 4 := by ring
  rw [e] at h
  unfold overlap
  rw [pow_mul]
  exact pow_le_pow_left₀ (sq_nonneg _) h n

/-- **Locality with an explicit radius**: `p_n(γ) ≤ 1 / (1 + n γ²/4)`. -/
theorem overlap_le_inv (n : ℕ) {γ : ℝ} (hγ : |γ| ≤ π) :
    overlap n γ ≤ 1 / (1 + n * (γ ^ 2 / 4)) := by
  have h := overlap_le n hγ
  have ha : 0 ≤ γ ^ 2 / 4 := by positivity
  have hb : 1 + n * (γ ^ 2 / 4) ≤ (1 + γ ^ 2 / 4) ^ n :=
    one_add_mul_le_pow (by linarith) n
  have hpos : 0 < 1 + n * (γ ^ 2 / 4) := by positivity
  calc overlap n γ ≤ (1 / (1 + γ ^ 2 / 4)) ^ n := h
    _ = 1 / (1 + γ ^ 2 / 4) ^ n := by rw [div_pow, one_pow]
    _ ≤ 1 / (1 + n * (γ ^ 2 / 4)) := one_div_le_one_div_of_le hpos hb

end QOU.Archimedean.EDCoherentLocality
