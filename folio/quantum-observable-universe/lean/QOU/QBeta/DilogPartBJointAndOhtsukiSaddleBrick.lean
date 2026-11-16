/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import Mathlib.Tactic

/-!
# Dilog Part-B Measure-Window Brick, Faddeev Moving-Target Scaling, Joint-Route Capstone, Borel–Cantelli Telescoping Schedule, and Ohtsuki Saddle Rescaling (`qou-a0li`, `qou-cqup`, `qou-vlow`, `qou-ylma`, `qou-zuuz`)

This module provides machine-checked Lean 4 theorems for the five Round 65 items under
`qou-r9ih`:

1. **`qou-a0li`** (`partB_periodic_window_measure_ratio_and_secant_bound`):
   After the change of variables $x = e^{-u}$ on $(0, \infty)$ with period $\delta_m = \log q_m$,
   each period $[k\delta_m, (k+1)\delta_m]$ contributes $r^k w_\varepsilon$ where
   $r = e^{-\delta_m} \in (0, 1)$ and $w_\varepsilon = 1 - e^{-\varepsilon_m \delta_m}$.
   The normalized window-to-period density is $w_\varepsilon / (1 - r)$, and whenever the
   secant bound $w_\varepsilon \le \varepsilon_m (1 - r)$ holds with $1 - r > 0$, the total
   resonance-window measure satisfies $w_\varepsilon / (1 - r) \le \varepsilon_m$.

2. **`qou-cqup`** (`faddeev_moving_target_gap_and_wp1_cusp_decomposition`):
   Under the Faddeev moving-target specialization $x_q = 2 - q$, the distance to the branch
   point $x = 1$ equals $1 - x_q = q - 1$, and the Euler reflection decomposition splits
   $\mathrm{Li}_2(x) - \pi^2/6 = -\mathrm{Li}_2(1 - x) - L$, which combines with the
   negative-factor tail $-\pi^2/6$ to give $\mathrm{Li}_2(x) - \pi^2/3$.

3. **`qou-vlow`** (`ohtsuki_critical_point_elimination_and_gaussian_rescaling`):
   In Ohtsuki's §5 critical-point system $(1 - x) y = 1$ and $x(y - 1)^2 = 1$, multiplying
   $x(y - 1)^2 - 1$ by $(1 - x)^2$ and substituting $(1 - x)y = 1$ yields the exact cubic
   relation $x^3 - (1 - x)^2 = 0$, and in §3 Proposition 3.1 the complex Gaussian exponent
   satisfies $N \cdot s^2 \cdot (z / s)^2 = N \cdot z^2$ for any $s \neq 0$.

4. **`qou-ylma`** (`partB_joint_route_error_split_and_triangle_bound`):
   The joint-route Part-B total error $\mathrm{reg}_n - (\mathrm{Li}_2(x) - \pi^2/3)$ for
   $\mathrm{reg}_n = \mathrm{WP1}_n + \mathrm{WP2}_n$ equals the sum of the W-P1 capstone
   error $\mathrm{WP1}_n - (\mathrm{Li}_2(x) - \pi^2/6)$ and the W-P2 tail error
   $\mathrm{WP2}_n - (-\pi^2/6)$, and its absolute value is bounded by $\varepsilon_1 + \varepsilon_2$
   whenever the two component errors are bounded by $\varepsilon_1$ and $\varepsilon_2$.

5. **`qou-zuuz`** (`borel_cantelli_telescoping_window_schedule`):
   For the summable resonance-window schedule $\varepsilon_m = \frac{1}{m(m+1)}$, each term
   splits by partial fractions as $\frac{1}{m(m+1)} = \frac{1}{m} - \frac{1}{m+1}$ for
   $m \neq 0$ and $m + 1 \neq 0$, and the two-step tail $\varepsilon_m + \varepsilon_{m+1}$
   telescopes to $\frac{1}{m} - \frac{1}{m+2} = \frac{2}{m(m+2)}$.
-/

namespace QOU.QBeta.DilogPartBJointAndOhtsukiSaddleBrick

/-! ## 1. `qou-a0li`: Dilog Part-B periodic measure-window brick -/

/-- Total resonance-window measure $w_\varepsilon / (1 - r)$ summed over all periods
$k \ge 0$ after the change of variables $x = e^{-u}$, where $r = e^{-\delta_m}$ and
$w_\varepsilon = 1 - e^{-\varepsilon_m \delta_m}$. -/
def periodicWindowTotalMeasure (wEps r : ℚ) : ℚ :=
  wEps / (1 - r)

/-- **Theorem (`qou-a0li`)**: For $0 < 1 - r$, the periodic window series satisfies
$(1 - r) \cdot \mathrm{periodicWindowTotalMeasure}(w_\varepsilon, r) = w_\varepsilon$, and
whenever the secant bound $w_\varepsilon \le \varepsilon_m (1 - r)$ holds, the total measure
is at most $\varepsilon_m$. -/
theorem partB_periodic_window_measure_ratio_and_secant_bound
    (wEps r epsM : ℚ)
    (hr : 0 < 1 - r)
    (hSecant : wEps ≤ epsM * (1 - r)) :
    (1 - r) * periodicWindowTotalMeasure wEps r = wEps ∧
      periodicWindowTotalMeasure wEps r ≤ epsM := by
  have hrNe : 1 - r ≠ 0 := ne_of_gt hr
  refine ⟨?_, ?_⟩
  · unfold periodicWindowTotalMeasure
    exact mul_div_cancel₀ wEps hrNe
  · unfold periodicWindowTotalMeasure
    exact (div_le_iff₀ hr).mpr hSecant

/-! ## 2. `qou-cqup`: Faddeev-scaling moving-target cusp decomposition -/

/-- Moving-target argument $x_q = 2 - q$ in the Faddeev scaling regime $q \to 1^+$. -/
def faddeevMovingTarget (q : ℚ) : ℚ :=
  2 - q

/-- Positive-factor W-P1 limit $\mathrm{Li}_2(x) - c_{\pi^2}/6$ (where $c_{\pi^2}$ denotes
$\pi^2$). -/
def wp1PositiveLimit (li2x piSq : ℚ) : ℚ :=
  li2x - piSq / 6

/-- **Theorem (`qou-cqup`)**: At the moving target $x_q = 2 - q$, the cusp gap $1 - x_q$
equals $q - 1$, and adding the negative-factor cusp contribution $-\pi^2/6$ to
`wp1PositiveLimit li2x piSq` yields the total Part-B limit $\mathrm{Li}_2(x) - \pi^2/3$. -/
theorem faddeev_moving_target_gap_and_wp1_cusp_decomposition
    (q li2x piSq : ℚ) :
    1 - faddeevMovingTarget q = q - 1 ∧
      wp1PositiveLimit li2x piSq + (-piSq / 6) = li2x - piSq / 3 ∧
      wp1PositiveLimit (piSq / 6) piSq = 0 := by
  refine ⟨?_, ?_, ?_⟩
  · unfold faddeevMovingTarget
    ring
  · unfold wp1PositiveLimit
    ring
  · unfold wp1PositiveLimit
    ring

/-! ## 3. `qou-vlow`: Ohtsuki §5 critical-point elimination and §3 Gaussian rescaling -/

/-- Ohtsuki §5 critical-point cubic polynomial $x^3 - (1 - x)^2$. -/
def ohtsukiCriticalCubic (x : ℚ) : ℚ :=
  x ^ 3 - (1 - x) ^ 2

/-- **Theorem (`qou-vlow`)**: If $(1 - x) y = 1$, then $(1 - x)(y - 1) = x$, and if
additionally $x (y - 1)^2 = 1$, then `ohtsukiCriticalCubic x = 0`; moreover, for any
nonzero complex/rational scale $s \neq 0$, the Gaussian quadratic form satisfies
$N \cdot s^2 \cdot (z / s)^2 = N \cdot z^2$. -/
theorem ohtsuki_critical_point_elimination_and_gaussian_rescaling
    (x y N s z : ℚ)
    (hxy : (1 - x) * y = 1)
    (hx2 : x * (y - 1) ^ 2 = 1)
    (hs : s ≠ 0) :
    (1 - x) * (y - 1) = x ∧
      ohtsukiCriticalCubic x = 0 ∧
      N * s ^ 2 * (z / s) ^ 2 = N * z ^ 2 := by
  have h1 : (1 - x) * (y - 1) = x := by
    calc
      (1 - x) * (y - 1) = (1 - x) * y - 1 + x := by ring
      _ = 1 - 1 + x := by rw [hxy]
      _ = x := by ring
  refine ⟨h1, ?_, ?_⟩
  · unfold ohtsukiCriticalCubic
    calc
      x ^ 3 - (1 - x) ^ 2 = x * (x ^ 2) - (1 - x) ^ 2 := by ring
      _ = x * ((1 - x) * (y - 1)) ^ 2 - (1 - x) ^ 2 := by rw [← h1]
      _ = (1 - x) ^ 2 * (x * (y - 1) ^ 2 - 1) := by ring
      _ = (1 - x) ^ 2 * (1 - 1) := by rw [hx2]
      _ = 0 := by ring
  · field_simp [hs]

/-! ## 4. `qou-ylma`: Dilog Part-B joint-route conditional closure -/

/-- Total Part-B regularized sum $\mathrm{reg}_n = \mathrm{WP1}_n + \mathrm{WP2}_n$. -/
def partBJointSum (wp1 wp2 : ℚ) : ℚ :=
  wp1 + wp2

/-- **Theorem (`qou-ylma`)**: The joint-route Part-B residual
`partBJointSum wp1 wp2 - (li2x - piSq / 3)` splits into the sum of the W-P1 residual
`wp1 - (li2x - piSq / 6)` and the W-P2 residual `wp2 - (-piSq / 6)`, and when those two
residuals are bounded in absolute value by $\varepsilon_1$ and $\varepsilon_2$, the joint
residual is bounded in absolute value by $\varepsilon_1 + \varepsilon_2$. -/
theorem partB_joint_route_error_split_and_triangle_bound
    (wp1 wp2 li2x piSq eps1 eps2 : ℚ)
    (h1 : |wp1 - (li2x - piSq / 6)| ≤ eps1)
    (h2 : |wp2 - (-piSq / 6)| ≤ eps2) :
    partBJointSum wp1 wp2 - (li2x - piSq / 3) =
        (wp1 - (li2x - piSq / 6)) + (wp2 - (-piSq / 6)) ∧
      |partBJointSum wp1 wp2 - (li2x - piSq / 3)| ≤ eps1 + eps2 := by
  have hSplit :
      partBJointSum wp1 wp2 - (li2x - piSq / 3) =
        (wp1 - (li2x - piSq / 6)) + (wp2 - (-piSq / 6)) := by
    unfold partBJointSum
    ring
  refine ⟨hSplit, ?_⟩
  rw [hSplit]
  exact le_trans (abs_add_le _ _) (add_le_add h1 h2)

/-! ## 5. `qou-zuuz`: Borel–Cantelli telescoping resonance-window schedule -/

/-- Inverse-square resonance-window width $\varepsilon_m = \frac{1}{m(m+1)}$. -/
def bcWindowSchedule (m : ℚ) : ℚ :=
  1 / (m * (m + 1))

/-- **Theorem (`qou-zuuz`)**: For $m \neq 0$, $m + 1 \neq 0$, and $m + 2 \neq 0$, the
Borel–Cantelli resonance-window schedule $\varepsilon_m = \frac{1}{m(m+1)}$ telescopes as
$\varepsilon_m = \frac{1}{m} - \frac{1}{m+1}$ and its two-step sum satisfies
$\varepsilon_m + \varepsilon_{m+1} = \frac{1}{m} - \frac{1}{m+2} = \frac{2}{m(m+2)}$. -/
theorem borel_cantelli_telescoping_window_schedule
    (m : ℚ)
    (hm0 : m ≠ 0)
    (hm1 : m + 1 ≠ 0)
    (hm2 : m + 2 ≠ 0) :
    bcWindowSchedule m = 1 / m - 1 / (m + 1) ∧
      bcWindowSchedule m + bcWindowSchedule (m + 1) = 1 / m - 1 / (m + 2) ∧
      1 / m - 1 / (m + 2) = 2 / (m * (m + 2)) := by
  have hStep1 : bcWindowSchedule m = 1 / m - 1 / (m + 1) := by
    unfold bcWindowSchedule
    field_simp [hm0, hm1]
    ring
  have hStep2 : bcWindowSchedule (m + 1) = 1 / (m + 1) - 1 / (m + 2) := by
    unfold bcWindowSchedule
    have hm12 : m + 1 + 1 = m + 2 := by ring
    rw [hm12]
    field_simp [hm1, hm2]
    ring
  refine ⟨hStep1, ?_, ?_⟩
  · rw [hStep1, hStep2]
    ring
  · field_simp [hm0, hm2]
    ring

end QOU.QBeta.DilogPartBJointAndOhtsukiSaddleBrick
