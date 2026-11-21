import QOU.MathlibExt.RSZIsoformalInterface
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum

/-!
# `IntegralSlopeSetting` is a hypothesis bundle, inhabited — not a debt

`IntegralSlopeSetting k μ` packages the standing hypotheses of
Ramis–Sauloy–Zhang §3.3 (`k ≥ 2` slopes, integral, strictly increasing). It is
an *input assumption*, not a theorem to be proved.

**What is proved (sorry-free).**
* `integralSlopeSetting_01` — the two-slope setting `μ = (0, 1)` satisfies it.
* `integralSlopeSetting_range` — for every `k ≥ 2` the slopes `μ i = i`
  satisfy it, so it is inhabited at every admissible `k`.
* `rszIsoformalDim_01` — on the first example, with ranks `(1, 1)`, the
  isoformal dimension formula gives `1`.
Together with the source's `not_integralSlopeSetting_one` this shows the class
is a genuine, satisfiable side condition. It should not be counted as debt.

**What is not proved.** RSZ Thm 3.3.5 itself (the isoformal classes form an
affine space of the stated dimension); the source states only the formula.

-- Ref: [leitner2026] QOU.MathlibExt.RSZIsoformalInterface; [rsz2013]
-- J.-P. Ramis, J. Sauloy, C. Zhang, Local analytic classification of
-- q-difference equations, Astérisque 355 (2013), §3.3, Thm 3.3.5.
-/

namespace QOU.MathlibExt.RSZ.Instances

open QOU.MathlibExt.RSZ

theorem integralSlopeSetting_01 : IntegralSlopeSetting 2 ![0, 1] where
  two_or_more := le_rfl
  strictly_increasing i j hij := by
    fin_cases i <;> fin_cases j <;> simp_all

theorem integralSlopeSetting_range (k : ℕ) (hk : 2 ≤ k) :
    IntegralSlopeSetting k (fun i => (i : ℤ)) where
  two_or_more := hk
  strictly_increasing i j hij := by exact_mod_cast hij

theorem rszIsoformalDim_01 : rszIsoformalDim 2 ![1, 1] ![0, 1] = 1 := by
  rw [rszIsoformalDim_two]; simp [rszLevel]

end QOU.MathlibExt.RSZ.Instances
