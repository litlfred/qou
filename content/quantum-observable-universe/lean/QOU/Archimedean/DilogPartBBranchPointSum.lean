import QOU.Archimedean.DilogPartAConvergence

/-!
# Part B of `conj:dilogarithm-archimedean-limit` — the positive-factor branch-point sum (V3)

The `W-P1` half of the Part-B cusp cancellation: for the substrate side `q > 1`,
the positive factors `k ≤ k*` (`k* = log_q(1/x)`, `x qᵏ < 1`) give a geometric
Riemann sum running **up to the branch point** `x u = 1`, converging to
`Li₂(x) − π²/6`.

This file builds the target-integral bricks. The genuine analytic core — the
improper limit at the branch point and the variable-term (`k* = ⌊log_q(1/x)⌋`)
Riemann sum — is scoped in bean `qou-jplv` and not yet discharged here.

* `integral_Icc_eq_LiTwo_sub` — **V3 brick 1**, the *interior* target integral
  `∫_x^c −log(1−t)/t = Li₂(c) − Li₂(x)` for `0 < x ≤ c < 1`, straight from the
  dilog derivative `hasDerivAt_LiTwo` + FTC (both endpoints in `(0,1)`, so the
  integrand is continuous — no branch-point/`t=0` singularity).

-- Ref: [manuscript] conj:dilogarithm-archimedean-limit
-- Ref: [faddeev1994] https://doi.org/10.1142/S0217732394002793
-/

namespace QOU.Archimedean

open QOU.QPochhammer intervalIntegral MeasureTheory

/-- **V3 brick 1 — the interior target integral.**  For `0 < x ≤ c < 1`,
    `∫_x^c −log(1−t)/t = Li₂(c) − Li₂(x)`.  Since `−log(1−t)/t` is the derivative
    of `Li₂` (`hasDerivAt_LiTwo`) and both endpoints lie in `(0,1)`, this is a
    proper FTC — the integrand is continuous on `[x,c]` (no `t=0` or branch-point
    singularity).  Taking `c → 1⁻` (with `LiTwo_one`) will give the branch-point
    value `π²/6 − Li₂(x)` (V3 brick 2, the improper step). -/
theorem integral_Icc_eq_LiTwo_sub {x c : ℝ} (hx0 : 0 < x) (hxc : x ≤ c)
    (hc1 : c < 1) : (∫ t in (x : ℝ)..c, -Real.log (1 - t) / t) = LiTwo c - LiTwo x := by
  have hderiv : ∀ t ∈ Set.uIcc x c, HasDerivAt LiTwo (-Real.log (1 - t) / t) t := by
    intro t ht
    rw [Set.uIcc_of_le hxc] at ht
    exact hasDerivAt_LiTwo (lt_of_lt_of_le hx0 ht.1) (lt_of_le_of_lt ht.2 hc1)
  have hint : IntervalIntegrable (fun t => -Real.log (1 - t) / t) volume x c := by
    apply ContinuousOn.intervalIntegrable
    rw [Set.uIcc_of_le hxc]
    refine ContinuousOn.div ?_ continuousOn_id
      (fun t ht => ne_of_gt (lt_of_lt_of_le hx0 ht.1))
    refine ContinuousOn.neg (ContinuousOn.log (continuousOn_const.sub continuousOn_id)
      (fun t ht => ne_of_gt ?_))
    have := ht.2; linarith
  exact intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hint

end QOU.Archimedean
