/-
# L4-1c(ii) — the smooth part is MONOTONE (bean qou-ph2s, epic qou-u1b5)

Last input of L4-1.  After the exact singular telescope (L4-1c(i)) the
whole remaining content of the second-order log-sine expansion is the
Riemann-sum defect of

    φ(x) := log(2 sin x / x) = log(2 sin x) − log x,   φ(0⁺) = log 2,

which the bean scoped as "a Lipschitz bound across the removable
singularity at 0", with `φ' = cot x − 1/x` (each term singular at 0, the
difference regular) as the expected obstacle.

**That obstacle is avoidable.**  The cell defects do not need a derivative
*bound* — they need a *sign*, and `φ` is strictly antitone on `(0, π)`.
Antitonicity comes from the single inequality `x·cos x < sin x`, proved
here from `ψ(x) = sin x − x·cos x` having `ψ(0) = 0` and
`ψ'(x) = x·sin x > 0`.  No behaviour of `φ` *at* `0` is ever needed: the
first cell is closed off instead by the elementary ceiling
`φ(u) ≤ log 2` (which is just `sin u ≤ u`).

So the pieces this file supplies are:

* `sin_sub_mul_cos_pos` — `x·cos x < sin x` on `(0, π)`;
* `strictAntiOn_phi` — `φ` strictly antitone on `(0, π)`, hence
  `φ(x_j) ≤ φ(u)` for every `u` in the cell `(x_{j−1}, x_j]`: each cell
  defect is `≤ 0`;
* `phi_le_log_two` — `φ(u) ≤ log 2` on `(0, π)`, the surrogate for the
  missing value at `0` that closes the first cell.

Together these squeeze the smooth half between `h·(φ(nh) − log 2)` and `0`
by telescoping — an `O(h)` two-sided bound with no derivative estimate
anywhere.
-/

import Mathlib.Analysis.SpecialFunctions.Integrals.Basic
import Mathlib.Analysis.Calculus.MeanValue

namespace QOU.Knot.FigureEightVolume

open Real

/-- The smooth part of the log-sine integrand, `φ(x) = log(2 sin x / x)`
    written as a difference (so no removable-singularity bookkeeping is
    needed; the value at `0` is never used). -/
noncomputable def phi (x : ℝ) : ℝ := Real.log (2 * Real.sin x) - Real.log x

/-- `x·cos x < sin x` on `(0, π)` — the single inequality behind `φ`'s
    monotonicity.  `ψ(x) = sin x − x·cos x` vanishes at `0` and has
    `ψ'(x) = x·sin x > 0` on the interval. -/
theorem sin_sub_mul_cos_pos {x : ℝ} (h0 : 0 < x) (hπ : x < π) :
    x * Real.cos x < Real.sin x := by
  have hpi := Real.pi_pos
  set ψ : ℝ → ℝ := fun t => Real.sin t - t * Real.cos t with hψ
  have hderiv : ∀ t : ℝ, HasDerivAt ψ (t * Real.sin t) t := by
    intro t
    have h1 : HasDerivAt Real.sin (Real.cos t) t := Real.hasDerivAt_sin t
    have h2 : HasDerivAt (fun s : ℝ => s * Real.cos s)
        (1 * Real.cos t + t * (-Real.sin t)) t :=
      (hasDerivAt_id t).mul (Real.hasDerivAt_cos t)
    have h3 := h1.sub h2
    convert h3 using 1
    ring
  have hmono : StrictMonoOn ψ (Set.Icc 0 π) := by
    refine strictMonoOn_of_deriv_pos (convex_Icc _ _) ?_ ?_
    · exact (Continuous.sub Real.continuous_sin
        (continuous_id.mul Real.continuous_cos)).continuousOn
    · intro t ht
      rw [interior_Icc] at ht
      rw [(hderiv t).deriv]
      exact mul_pos ht.1 (Real.sin_pos_of_pos_of_lt_pi ht.1 ht.2)
  have h := hmono (Set.left_mem_Icc.mpr hpi.le)
    ⟨h0.le, hπ.le⟩ h0
  simp only [hψ, Real.sin_zero, zero_mul, sub_zero, sub_pos] at h
  linarith [h]

/-- `φ` has the expected derivative on `(0, π)`. -/
theorem hasDerivAt_phi {x : ℝ} (h0 : 0 < x) (hπ : x < π) :
    HasDerivAt phi
      ((2 * Real.cos x) / (2 * Real.sin x) - x⁻¹) x := by
  have hs : 0 < Real.sin x := Real.sin_pos_of_pos_of_lt_pi h0 hπ
  have h2s : (2 : ℝ) * Real.sin x ≠ 0 := by positivity
  have hd1 : HasDerivAt (fun t : ℝ => 2 * Real.sin t) (2 * Real.cos x) x := by
    simpa using (Real.hasDerivAt_sin x).const_mul (2 : ℝ)
  have hlog2 : HasDerivAt Real.log x⁻¹ x := Real.hasDerivAt_log h0.ne'
  exact (hd1.log h2s).sub hlog2

/-- **`φ` is strictly antitone on `(0, π)`** — so every cell defect
    `φ(x_j) − φ(u)`, `u ≤ x_j`, is `≤ 0`.  This is the property that
    replaces the Lipschitz bound the bean expected to need. -/
theorem strictAntiOn_phi : StrictAntiOn phi (Set.Ioo 0 π) := by
  refine strictAntiOn_of_deriv_neg (convex_Ioo _ _) ?_ ?_
  · refine ContinuousOn.sub ?_ ?_
    · refine ContinuousOn.log ?_ ?_
      · exact (continuous_const.mul Real.continuous_sin).continuousOn
      · intro x hx
        have hs : 0 < Real.sin x := Real.sin_pos_of_pos_of_lt_pi hx.1 hx.2
        positivity
    · exact Real.continuousOn_log.mono (by
        intro x hx
        exact ne_of_gt hx.1)
  · intro x hx
    rw [interior_Ioo] at hx
    rw [(hasDerivAt_phi hx.1 hx.2).deriv]
    have hs : 0 < Real.sin x := Real.sin_pos_of_pos_of_lt_pi hx.1 hx.2
    have hkey := sin_sub_mul_cos_pos hx.1 hx.2
    have hgoal : (2 * Real.cos x) / (2 * Real.sin x) < x⁻¹ := by
      rw [div_lt_iff₀ (by positivity : (0:ℝ) < 2 * Real.sin x),
        inv_mul_eq_div, lt_div_iff₀ hx.1]
      nlinarith [hkey]
    linarith [hgoal]

/-- The first-cell ceiling: `φ(u) ≤ log 2` on `(0, π)` — just `sin u ≤ u`.
    This stands in for the (unused) value `φ(0⁺) = log 2`. -/
theorem phi_le_log_two {u : ℝ} (h0 : 0 < u) (hπ : u < π) :
    phi u ≤ Real.log 2 := by
  have hs : 0 < Real.sin u := Real.sin_pos_of_pos_of_lt_pi h0 hπ
  have hlt : Real.sin u < u := Real.sin_lt h0
  unfold phi
  have h2 : Real.log (2 * Real.sin u) ≤ Real.log (2 * u) :=
    Real.log_le_log (by positivity) (by linarith)
  rw [Real.log_mul (by norm_num) h0.ne'] at h2
  linarith

end QOU.Knot.FigureEightVolume
