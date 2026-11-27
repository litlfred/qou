import Mathlib.NumberTheory.Transcendental.Liouville.LiouvilleNumber
import Mathlib.RingTheory.Localization.Integral
import Mathlib.RingTheory.Algebraic.Integral
import Mathlib.Analysis.Complex.Basic

/-!
# The hypotheses on `ℏ` used for `D_ℏ` are jointly satisfiable

`D_ℏ` is monoidal and braided for `ℏ` transcendental over `ℚ` (`Monoidal`, `Braided`), and right
rigid when additionally `‖ℏ‖ ≤ 1/12` (`Duals`). This file shows the two conditions are not
vacuous together: `ℏ = L/14` with `L = ∑ 10^{-k!}` Liouville's number works. Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S4)
-/

namespace QOU.KZ.Drinfeld

open LiouvilleNumber

/-- **Admissible `ℏ` exist**: transcendental over `ℚ` with `‖ℏ‖ ≤ 1/12`. -/
theorem exists_admissible : ∃ c : ℂ, Transcendental ℚ c ∧ ‖c‖ ≤ 1 / 12 := by
  set x : ℝ := liouvilleNumber 10
  have hZ : Transcendental ℤ x := transcendental_liouvilleNumber (by norm_num)
  have hQ : Transcendental ℚ x := fun h => hZ ((IsFractionRing.isAlgebraic_iff ℤ ℚ ℝ).2 h)
  have hC : Transcendental ℚ (x : ℂ) := by
    have := (transcendental_algebraMap_iff (R := ℚ) (A := ℂ) (a := x)
      (algebraMap ℝ ℂ).injective).2 hQ
    simpa using this
  have hsplit := partialSum_add_remainder (m := (10 : ℝ)) (by norm_num) 0
  have hp : partialSum 10 0 = 1 / 10 := by simp [partialSum]
  have hr := remainder_lt 0 (m := (10 : ℝ)) (by norm_num)
  have hr0 := remainder_pos (m := (10 : ℝ)) (by norm_num) 0
  have hx0 : 0 < x := by
    show 0 < liouvilleNumber 10
    rw [← hsplit, hp]; linarith
  have hx1 : x < 11 / 10 := by
    show liouvilleNumber 10 < 11 / 10
    rw [← hsplit, hp]; simp at hr; linarith
  refine ⟨(x : ℂ) / 14, ?_, ?_⟩
  · intro h
    apply hC
    have h14 : IsAlgebraic ℚ ((14 : ℂ)) := by
      have := isAlgebraic_algebraMap (R := ℚ) (A := ℂ) (14 : ℚ)
      simpa using this
    have := h.mul h14
    rwa [div_mul_cancel₀ _ (by norm_num : (14 : ℂ) ≠ 0)] at this
  · rw [norm_div, Complex.norm_real, Real.norm_eq_abs, abs_of_pos hx0]
    simp only [Complex.norm_ofNat]
    linarith
