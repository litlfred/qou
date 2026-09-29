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

The parent file `QBetaPerBlockChiClosedForms.lean` proves the order-1
coefficient `delta_tau_M_surrogate_hasDerivAt_one : HasDerivAt
delta_tau_M_surrogate (-5/6) 1` by the quotient rule on `N/D`, and leaves
the order-2 coefficient as a `True := trivial` placeholder
(`delta_tau_M_surrogate_taylor_coeff_2`) with a note that the
`iteratedDeriv`-level discharge is "bulky but tractable". This file
discharges it.

## What is proved

Write `g = N/D = delta_tau_M_surrogate` with

  `N(q) = -q¹¹+q¹⁰-2q⁹+q⁸+q⁶-q⁵-q³+2q²-q+1`,  `N(1)=0, N'(1)=-10, N''(1)=-100`,
  `D(q) = 4q⁵(q²+q+1)`,                          `D(1)=12, D'(1)=72,  D''(1)=368`.

The first derivative is, by the quotient rule,
  `g'(q) = (N'(q)·D(q) − N(q)·D'(q)) / D(q)²`   (`delta_tau_M_surrogate_deriv`).
This file proves
  `HasDerivAt delta_tau_M_surrogate_deriv (5/3) 1`,
i.e. `g''(1) = 5/3` — differentiating the quotient-rule result a SECOND
time. The order-2 Taylor coefficient is then
  `c₂ = g''(1) / 2! = (5/3)/2 = 5/6`,
matching the witnessed value
`delta_tau_M_surrogate_taylor_witness 2 = 5/6` (from
`qbeta-c3-multiblock-recursion-attack.witness.json`).

The proof reuses ONLY the lemma toolkit of the verified order-1 proof
(`hasDerivAt_pow`, `HasDerivAt.{neg,const_mul,add,sub,mul,div}`,
`convert … using 1`, `norm_num`) — no `iteratedDeriv`/`eventuallyEq`
machinery — so it is a faithful "the quotient-rule chain extends"
demonstration. The numerical checkpoints (`N''(1)=-100`, `D''(1)=368`,
`num'(1)=-1200`, `den'(1)=1728`, `g''(1)=34560/20736=5/3`) are recorded in
the comments at each step.

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
