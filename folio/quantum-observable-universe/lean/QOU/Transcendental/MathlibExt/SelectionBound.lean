import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic

/-!
# QOU.MathlibExt.SelectionBound — a menu minimum is not evidence

This repository has a documented fitting problem
(`docs/audits/2026-06-04-hidden-fitting-verification-gap-mass-binding-walkthrough.md`,
and the `(1+q)/2` back-solve antipattern of PR #1578). One recurring shape is
the **menu minimum**: enumerate `N` candidate expressions, report the one whose
error is smallest, and quote that error as if it were a prediction.

The quantitative correction is elementary and is proved here so it can be cited
rather than re-argued. If each of `N` independent candidates lands within the
quoted tolerance with probability `p`, then

    P(at least one lands within tolerance) = 1 - (1 - p)^N  ≥  1 - exp(-N p)

so a small quoted error is *expected* once `N p ≳ 1`, and carries no evidential
weight until `N p ≪ 1`.

## The worked case this was written for

`t7qv` Gap #3 (A=3 mirror magnitude, ³H/³He) records "best structural 2.52 %".
Per `2026-05-31-option-e-kashiwara-refresh-assessment.md` that figure is the
minimum over a **9 scales × 9 inputs = 81 candidate** menu, and that audit
already says so: *"The 81-candidate menu min (+2.52 %) is also a fit."* Against
it, the parameter-free link-volume ratio for the same pair gives **2.899 %**
(`wlambda_binding_a3_mirror_selection.py`). So the menu bought a 13 % reduction
in the error at the cost of 81 degrees of selection freedom, and by the bound
above, with `N = 81` and candidate errors uniform on `[0, 1]`,
`P(min ≤ 0.0252) ≥ 1 - exp(-2.04) = 0.870`.

A result reproducible by chance seven times in eight is not evidence for the
structure that produced it.
-/

namespace QOU.MathlibExt.SelectionBound

/-- `(1 - p)^N ≤ exp(-(N·p))` for `p ≤ 1`. The elementary step behind the
selection bound. No lower bound on `p` is needed — only `1 - p ≥ 0`, so that
the power is monotone, and `1 - p ≤ exp(-p)`, which holds for every real. -/
theorem pow_one_sub_le_exp (N : ℕ) {p : ℝ} (hp1 : p ≤ 1) :
    (1 - p) ^ N ≤ Real.exp (-(N * p)) := by
  have hstep : (1 - p) ≤ Real.exp (-p) := by
    have := Real.add_one_le_exp (-p)
    linarith
  have hnn : (0:ℝ) ≤ 1 - p := by linarith
  calc (1 - p) ^ N ≤ (Real.exp (-p)) ^ N := by
        gcongr
    _ = Real.exp (-(N * p)) := by
        rw [← Real.exp_nat_mul]
        ring_nf

/-- **A menu minimum is expected, not surprising.** With `N` independent
candidates each landing inside the tolerance with probability `p`, the chance
that the best of them does is at least `1 - exp(-N p)`. -/
theorem menu_min_prob_ge (N : ℕ) {p : ℝ} (hp1 : p ≤ 1) :
    1 - Real.exp (-(N * p)) ≤ 1 - (1 - p) ^ N := by
  have := pow_one_sub_le_exp N hp1
  linarith

/-- The contrapositive, in the form a reviewer wants: to make a best-of-`N`
result surprising at level `α` — i.e. to force the chance of getting it by
selection below `α` — the per-candidate probability must satisfy
`N · p ≤ -log α`. With `N = 81` and `α = 0.05` that is `p ≤ 0.037`: each
individual candidate must already have been a 3.7 % shot. -/
theorem selection_needs_small_Np {N : ℕ} {p α : ℝ} (hp1 : p ≤ 1)
    (h : 1 - (1 - p) ^ N < α) :
    Real.exp (-(N * p)) > 1 - α := by
  have := pow_one_sub_le_exp N hp1
  have hlt : (1 - p) ^ N > 1 - α := by linarith
  linarith

end QOU.MathlibExt.SelectionBound
