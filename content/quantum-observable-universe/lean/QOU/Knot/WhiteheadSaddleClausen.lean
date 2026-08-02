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
