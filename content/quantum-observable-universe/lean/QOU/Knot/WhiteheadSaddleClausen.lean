/-
  Whitehead VC — the saddle-VALUE identity (Clausen), toward discharging the
  `hsaddle` input of `whitehead_vc_of_saddle_value` (bean qou-dw20 / qou-t2sc).

  The saddle sits at `(t*, x*) = (1/2, 1/4)` (validated numerically in
  `computations/whitehead_saddle.py`).  The continuum saddle value is the
  integral

    V = 2π ∫_0^{1/2} [ log 2 + 2 log sin(π(u+1/4)) − log sin(π u) ] du.

  This file proves, sorry-free using `QOU.Knot.Clausen`, that

    V = 4 · clausen(π/2)   ( = 4G = Vol(Whitehead) ),

  the analytic VALUE half of `hsaddle`.  The Riemann-sum → V convergence (the
  other half, via `integral_le_sum_log_sin` / `sum_log_sin_le_integral`) is the
  remaining brick.

  Archimedean (ℝ).  -- Ref: [vanderveen2008] arXiv:math/0611181
-/

import QOU.Knot.Clausen
import QOU.Knot.WhiteheadVolumeConjecture

namespace QOU.Knot.WhiteheadSaddle

open Real
open scoped Real

/-- π-scaled `log(2 sin)` integral: `∫_0^b log(2 sin(π u)) du = -clausen(2πb)/(2π)`
    (substitution `w = π u` in `QOU.Knot.integral_log_two_sin`). -/
theorem integral_log_two_sin_pi (b : ℝ) :
    (∫ u in (0:ℝ)..b, Real.log (2 * Real.sin (π * u)))
      = -QOU.Knot.clausen (2 * (π * b)) / (2 * π) := by
  have hπ : (π : ℝ) ≠ 0 := ne_of_gt Real.pi_pos
  rw [intervalIntegral.integral_comp_mul_left (fun w => Real.log (2 * Real.sin w)) hπ,
      mul_zero, QOU.Knot.integral_log_two_sin (π * b), smul_eq_mul]
  field_simp

/-- **Per-term reduction (convergence brick, qou-1gkf).**  Each van der Veen
    kernel factor `2 sin²a / sin b` has log equal to the reduced saddle-integrand
    term `2 log(2 sin a) − log(2 sin b)` (the `log 2` bookkeeping that makes the
    discrete Riemann sum match `saddle_integral`).  Needs `sin a, sin b > 0`
    (holds on the summation range `(k+j)π/N, jπ/N ∈ (0, π)`). -/
theorem log_factor_reduce {a b : ℝ} (ha : 0 < Real.sin a) (hb : 0 < Real.sin b) :
    Real.log (2 * Real.sin a ^ 2 / Real.sin b)
      = 2 * Real.log (2 * Real.sin a) - Real.log (2 * Real.sin b) := by
  have h2 : (2 : ℝ) ≠ 0 := by norm_num
  rw [Real.log_div (by positivity) (ne_of_gt hb),
      Real.log_mul h2 (pow_ne_zero 2 (ne_of_gt ha)), Real.log_pow,
      Real.log_mul h2 (ne_of_gt ha), Real.log_mul h2 (ne_of_gt hb)]
  push_cast
  ring

/-- `log(2 sin(π·))` is interval-integrable (scale `QOU.Knot.intervalIntegrable_log_two_sin`). -/
theorem intervalIntegrable_log_two_sin_pi (a b : ℝ) :
    IntervalIntegrable (fun u => Real.log (2 * Real.sin (π * u))) MeasureTheory.volume a b := by
  have hπ : (π : ℝ) ≠ 0 := ne_of_gt Real.pi_pos
  have h := (QOU.Knot.intervalIntegrable_log_two_sin (π * a) (π * b)).comp_mul_left (c := π)
  rwa [mul_div_cancel_left₀ a hπ, mul_div_cancel_left₀ b hπ] at h

/-- `clausen(3π/2) = −clausen(π/2)` (via the `clausen↔Cl_2` bridge + `Cl_2_two_pi_sub`). -/
theorem clausen_three_pi_div_two :
    QOU.Knot.clausen (3 * π / 2) = -QOU.Knot.clausen (π / 2) := by
  have hpi := Real.pi_pos
  have h1 : (3 * π / 2) ∈ Set.Ioo (0:ℝ) (2 * π) := ⟨by linarith, by linarith⟩
  have h2 : (π / 2) ∈ Set.Ioo (0:ℝ) (2 * π) := ⟨by linarith, by linarith⟩
  rw [QOU.Knot.clausen_eq_series h1, QOU.Knot.clausen_eq_series h2,
      show 3 * π / 2 = 2 * π - π / 2 by ring, QOU.Knot.Cl_2_two_pi_sub]

/-- The `−log(2 sin(π u))` piece: `∫_0^{1/2} log(2 sin(π u)) du = 0`
    (`= −clausen(π)/(2π)` and `clausen π = 0`). -/
theorem integral_B_zero :
    (∫ u in (0:ℝ)..(1/2:ℝ), Real.log (2 * Real.sin (π * u))) = 0 := by
  rw [integral_log_two_sin_pi (1/2), show 2 * (π * (1/2:ℝ)) = π by ring,
      QOU.Knot.clausen_pi]
  simp

/-- The shifted `log(2 sin(π(u+¼)))` piece: `∫_0^{1/2} = clausen(π/2)/π`
    (shift to `[¼,¾]`, split, `integral_log_two_sin_pi` at `¾,¼`, antisymmetry). -/
theorem integral_A :
    (∫ u in (0:ℝ)..(1/2:ℝ), Real.log (2 * Real.sin (π * (u + 1/4))))
      = QOU.Knot.clausen (π / 2) / π := by
  have hπ : (π : ℝ) ≠ 0 := ne_of_gt Real.pi_pos
  rw [intervalIntegral.integral_comp_add_right
        (fun v => Real.log (2 * Real.sin (π * v))) (1/4),
      show (0:ℝ) + 1/4 = 1/4 by norm_num, show (1/2:ℝ) + 1/4 = 3/4 by norm_num]
  have hadj := intervalIntegral.integral_add_adjacent_intervals
    (intervalIntegrable_log_two_sin_pi 0 (1/4))
    (intervalIntegrable_log_two_sin_pi (1/4) (3/4))
  have hsplit : (∫ v in (1/4:ℝ)..(3/4:ℝ), Real.log (2 * Real.sin (π * v)))
      = (∫ v in (0:ℝ)..(3/4:ℝ), Real.log (2 * Real.sin (π * v)))
        - (∫ v in (0:ℝ)..(1/4:ℝ), Real.log (2 * Real.sin (π * v))) := by linarith
  rw [hsplit, integral_log_two_sin_pi (3/4), integral_log_two_sin_pi (1/4),
      show 2 * (π * (3/4:ℝ)) = 3 * π / 2 by ring,
      show 2 * (π * (1/4:ℝ)) = π / 2 by ring, clausen_three_pi_div_two]
  field_simp
  ring

/-- **Saddle VALUE identity (sorry-free).**  The (log2-reduced) saddle integrand
    integrates to `2·clausen(π/2)/π`, so `2π ×` it `= 4·clausen(π/2) = 4G` — the
    value half of `hsaddle`. -/
theorem saddle_integral :
    (∫ u in (0:ℝ)..(1/2:ℝ),
        (2 * Real.log (2 * Real.sin (π * (u + 1/4)))
          - Real.log (2 * Real.sin (π * u))))
      = 2 * QOU.Knot.clausen (π / 2) / π := by
  have hIntA : IntervalIntegrable
      (fun u => Real.log (2 * Real.sin (π * (u + 1/4)))) MeasureTheory.volume 0 (1/2) := by
    have h := (intervalIntegrable_log_two_sin_pi (1/4) (3/4)).comp_add_right (1/4)
    rw [show (1/4:ℝ) - 1/4 = 0 by norm_num, show (3/4:ℝ) - 1/4 = 1/2 by norm_num] at h
    exact h
  rw [intervalIntegral.integral_sub (hIntA.const_mul 2) (intervalIntegrable_log_two_sin_pi 0 (1/2)),
      intervalIntegral.integral_const_mul, integral_A, integral_B_zero]
  ring

/-- `sin((2k+1)·(π/2)) = (-1)^k` (induction; each step adds `π`, `sin_add_pi`). -/
theorem sin_two_mul_add_one_mul_pi_div_two (k : ℕ) :
    Real.sin ((2 * (k : ℝ) + 1) * (π / 2)) = (-1 : ℝ) ^ k := by
  induction k with
  | zero =>
    simp only [Nat.cast_zero, mul_zero, zero_add, one_mul, Real.sin_pi_div_two, pow_zero]
  | succ m ih =>
    have hstep : (2 * ((m : ℝ) + 1) + 1) * (π / 2)
        = (2 * (m : ℝ) + 1) * (π / 2) + π := by ring
    push_cast
    rw [hstep, Real.sin_add_pi, ih]
    ring

/-- The even-shifted van der Veen index has vanishing sine:
    `sin((2k+2)·(π/2)) = sin((k+1)π) = 0`. -/
theorem sin_odd_index_vanish (k : ℕ) :
    Real.sin (((2 * (k : ℝ) + 1) + 1) * (π / 2)) = 0 := by
  have h : ((2 * (k : ℝ) + 1) + 1) * (π / 2) = ((k + 1 : ℕ) : ℝ) * π := by
    push_cast; ring
  rw [h, Real.sin_nat_mul_pi]

/-- **catalan bridge (convergence prerequisite, qou-kvvu).**  Catalan's constant
    `G = Σ (-1)ⁿ/(2n+1)²` equals `clausen(π/2)`: the even/odd split of the `Cl_2`
    series drops the even-index (`sin(mπ)=0`) terms and reindexes the odd-index
    terms `sin((2k+1)π/2) = (-1)ᵏ`.  Connects the conditional-VC constant
    `4·catalanG` (`whitehead_vc_of_saddle_value`) to the Clausen value
    `4·clausen(π/2)` produced by `saddle_integral`. -/
theorem catalanG_eq_clausen_pi_div_two :
    QOU.Knot.WhiteheadVC.catalanG = QOU.Knot.clausen (π / 2) := by
  have hpi := Real.pi_pos
  -- majorant: `Σ 1/(k+1)²` (the Clausen `continuous_Cl_2` pattern).
  have hmaj : Summable (fun k : ℕ => 1 / ((k : ℝ) + 1) ^ 2) := by
    have h : Summable (fun n : ℕ => 1 / (n : ℝ) ^ 2) :=
      summable_one_div_nat_pow.mpr (by norm_num)
    exact ((summable_nat_add_iff 1).2 h).congr (fun n => by push_cast; ring)
  set g : ℕ → ℝ := fun j => Real.sin (((j : ℝ) + 1) * (π / 2)) / ((j : ℝ) + 1) ^ 2
    with hgdef
  -- termwise reindexing of the even/odd halves
  have heven_eq : ∀ k : ℕ, g (2 * k) = (-1 : ℝ) ^ k / (2 * (k : ℝ) + 1) ^ 2 := by
    intro k
    simp only [hgdef]
    rw [show (((2 * k : ℕ)) : ℝ) + 1 = 2 * (k : ℝ) + 1 by push_cast; ring,
        sin_two_mul_add_one_mul_pi_div_two]
  have hodd_eq : ∀ k : ℕ, g (2 * k + 1) = 0 := by
    intro k
    simp only [hgdef]
    rw [show (((2 * k + 1 : ℕ)) : ℝ) + 1 = (2 * (k : ℝ) + 1) + 1 by push_cast; ring,
        sin_odd_index_vanish, zero_div]
  -- summability of the alternating even half (Catalan) by norm comparison
  have hCat : Summable (fun k : ℕ => (-1 : ℝ) ^ k / (2 * (k : ℝ) + 1) ^ 2) := by
    refine hmaj.of_norm_bounded (fun k => ?_)
    have hk : (0 : ℝ) ≤ (k : ℝ) := Nat.cast_nonneg k
    rw [Real.norm_eq_abs, abs_div, abs_pow, abs_neg, abs_one, one_pow,
        abs_of_pos (by positivity : (0 : ℝ) < (2 * (k : ℝ) + 1) ^ 2)]
    exact one_div_le_one_div_of_le (by positivity) (by nlinarith [hk])
  have heven : Summable (fun k : ℕ => g (2 * k)) :=
    hCat.congr (fun k => (heven_eq k).symm)
  have hodd : Summable (fun k : ℕ => g (2 * k + 1)) :=
    summable_zero.congr (fun k => (hodd_eq k).symm)
  have hcombine := tsum_even_add_odd heven hodd
  have hoddsum : (∑' k : ℕ, g (2 * k + 1)) = 0 := by
    rw [tsum_congr hodd_eq, tsum_zero]
  have hevensum : (∑' k : ℕ, g (2 * k)) = QOU.Knot.WhiteheadVC.catalanG := by
    unfold QOU.Knot.WhiteheadVC.catalanG
    exact tsum_congr heven_eq
  have hCl : QOU.Archimedean.Cl_2 (π / 2) = ∑' k : ℕ, g k := by
    simp only [hgdef, QOU.Archimedean.Cl_2]
  rw [QOU.Knot.clausen_eq_series (θ := π / 2) ⟨by linarith, by linarith⟩,
      hCl, ← hcombine, hevensum, hoddsum, add_zero]

/-
  ROADMAP — remaining bricks to discharge `hsaddle` (all ingredients verified
  present in `QOU.Knot.Clausen`; algebra confirmed to 40 digits in
  `computations/whitehead_saddle.py`).

  (A) VALUE identity  V = 4·clausen(π/2)  ( = 4G ):
      · integrand `log2 + 2 log sin(π(u+¼)) − log sin(π u)` reduces (log-sin =
        log(2 sin) − log2, valid since sin>0 on the ranges) to the log2-free
        `2 log(2 sin(π(u+¼))) − log(2 sin(π u))` — the log2 terms cancel exactly.
      · ∫_0^{1/2} log(2 sin(π u)) du = integral_log_two_sin_pi (1/2)
          = −clausen(π)/(2π) = 0                        [clausen_pi]
      · ∫_0^{1/2} log(2 sin(π(u+¼))) du
          = ∫_{1/4}^{3/4} log(2 sin(π v)) dv            [integral_comp_add_right]
          = integral_log_two_sin_pi (3/4) − integral_log_two_sin_pi (1/4)
                                                        [integral_add_adjacent_intervals,
                                                         + integrability of log(2 sin(π·))]
          = (clausen(π/2) − clausen(3π/2)) / (2π)
      · clausen(3π/2) = clausen(2π − π/2) = Cl_2(2π−π/2) = −Cl_2(π/2)
          = −clausen(π/2)                     [clausen_eqOn_Cl_2 + Cl_2_two_pi_sub]
      ⇒ V = 2π·(2·(2clausen(π/2))/(2π) − 0) = 4·clausen(π/2).

  (B) CONVERGENCE  (2π/N)·log S_{n*,k*} → V, at nseq→N/2, kseq→N/4:
      the log(2 sin) Riemann sum is squeezed between the window integrals via
      integral_le_sum_log_sin / sum_log_sin_le_integral (rising) and the
      _falling variants; master-error → 0 (as in FigureEightVolumeSaddle E5c).

  (A)+(B) discharge the `hsaddle` hypothesis of
  `QOU.Knot.WhiteheadVC.whitehead_vc_of_saddle_value`, closing the unconditional
  Whitehead Volume Conjecture.  -- Ref: [vanderveen2008] arXiv:math/0611181
-/

end QOU.Knot.WhiteheadSaddle
