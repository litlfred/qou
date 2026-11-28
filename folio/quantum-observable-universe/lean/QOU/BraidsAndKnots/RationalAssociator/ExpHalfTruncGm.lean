import QOU.BraidsAndKnots.RationalAssociator.ExpHalfTrunc
import QOU.LiftingDescent.GmFormalExp

/-!
# The hexagon exponential is the `G_m` point with logarithm `t/2`

`expHalfTrunc N = Σ_{k<N} X^k / (2^k k!)` (`ExpHalfTrunc.lean`) is the per-level exponential of
the associator tower. `GmFormalExp.lean` builds `exp : (t ℚ⟦t⟧, +) ≃ (1 + t ℚ⟦t⟧, ×)`, the
inverse of the formal logarithm of `G_m`.

* `expHalfTrunc_eq_trunc_gmExp`: `expHalfTrunc N` is the degree-`< N` truncation of
  `exp_{G_m}(t/2)`, evaluated at `t = X`.
* `formalLog_expHalf`: the series it truncates has `log_{G_m} = t/2`.

So the exponential the associator tower uses is not an extra choice next to the energy reading:
both come from the one isomorphism `log : Ĝ_m ≅ Ĝ_a`. No analysis, no measured values.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

open PowerSeries QOU.FormalGroups.GmLog

/-- **`expHalfTrunc N` truncates `exp_{G_m}(t/2)`.** -/
theorem expHalfTrunc_eq_trunc_gmExp (N : ℕ) :
    expHalfTrunc N = ∑ k ∈ Finset.range N,
      coeff k (gmExp (C (1 / 2 : ℚ) * X)) • FreeAlgebra.ι ℚ (0 : Fin 2) ^ k := by
  rw [expHalfTrunc]
  refine Finset.sum_congr rfl (fun k _ => ?_)
  rw [coeff_gmExp_half]

/-- **The series truncated by `expHalfTrunc` has logarithm `t/2`.** -/
theorem formalLog_expHalf : formalLog (gmExp (C (1 / 2 : ℚ) * X)) = C (1 / 2 : ℚ) * X :=
  formalLog_gmExp (by rw [map_mul, constantCoeff_X, mul_zero])

end QOU.BraidsAndKnots.RationalAssociator
