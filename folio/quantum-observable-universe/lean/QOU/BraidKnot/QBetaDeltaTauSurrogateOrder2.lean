import Mathlib.Data.Real.Basic
import Mathlib.Analysis.Calculus.Deriv.Basic
import Mathlib.Analysis.Calculus.Deriv.Pow
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Analysis.Calculus.Deriv.Add
import Mathlib.Analysis.Calculus.Deriv.Inv
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import QOU.BraidKnot.QBetaPerBlockChiClosedForms

/-!
# QOU.BraidKnot.QBetaDeltaTauSurrogateOrder2

**Order-2 (second-derivative) Taylor coefficient of `delta_tau_M_surrogate`
at `q = 1`, via the quotient-rule chain extended one level past the
order-1 result.**

**Status (corrected 2026-10-10, bean `qou-eddc`).** This header used to
describe the order-2 proof as living here, over the grouped-frame closed form
`N = -q¹¹+q¹⁰-2q⁹+q⁸+q⁶-q⁵-q³+2q²-q+1`, `D = 4q⁵(q²+q+1)`. Both are out of date:

- `delta_tau_M_surrogate` is now the canonical (borromean) closed form, with
  numerator of degree 17 and denominator `4q⁸(q²+q+1)`.
- The derivative proof `delta_tau_M_surrogate_deriv_hasDerivAt_one :
  HasDerivAt delta_tau_M_surrogate_deriv (5/3) 1` and the coefficient theorem
  `delta_tau_M_surrogate_taylor_coeff_2` live in
  `QBetaPerBlockChiClosedForms.lean`.

What this file proves is the two numerical identities below: `g'(1) = -5/6`
evaluated from `delta_tau_M_surrogate_deriv`, and `(5/3)/2! = 5/6`. The order-2
coefficient `c₂ = 5/6` is the same in both frames; the frames first differ at
order 3.

LaTeX label: `prop:qbeta-delta-tau-surrogate-order2`
-/

namespace QOU.BraidKnot


/-- **Consistency with order-1.** `g'(1) = -5/6`, matching
`delta_tau_M_surrogate_hasDerivAt_one`. Pure numerical identity. -/
theorem delta_tau_M_surrogate_deriv_at_one :
    delta_tau_M_surrogate_deriv 1 = -5/6 := by
  unfold delta_tau_M_surrogate_deriv
  norm_num


/-- **Corollary (order-2 Taylor coefficient = 5/6).** Since
`g''(1) = 5/3`, the second Taylor coefficient at `q = 1` is
`g''(1) / 2! = 5/6`, matching the witnessed catalogue value
`delta_tau_M_surrogate_taylor_witness 2`. -/
theorem delta_tau_M_surrogate_taylor_coeff_2_eq :
    (5 : ℝ) / 3 / (Nat.factorial 2) = 5 / 6 := by
  norm_num [Nat.factorial]

end QOU.BraidKnot
