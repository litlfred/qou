import Mathlib.Data.Real.Basic

namespace QOU.Appendix.DeltaMaxNumericalScale

/-- Context for the uniform `Δ_max` scale bound.

    **Restated 2026-08-21** (vacuity ledger, `proof-no-trivial-true` /
    `reflexive-tautology-ascribed-literal`).  The class previously carried
    the single field `holds : (1 : ℝ) = 1` — provable by `rfl`, so it
    constrained no instance at all, and the theorem below projected it to
    conclude `(1 : ℝ) = 1`: vacuous with *or* without an instance.

    The fields now state the actual hypothesis the appendix block names —
    that `Δ_max` is uniformly bounded by a positive scale.  The bound is
    carried as a **parameter**, not a numeral: the block's numerical value
    is not derived anywhere in the corpus, and inventing one here would be
    a fit.  Supplying it is the open work (bean `qou-7fyw`). -/
class DeltaMaxNumericalScaleContext where
  /-- The uniform bound on the jet-filtration defect. -/
  bound : ℝ
  /-- The bound is a genuine (positive) scale. -/
  bound_pos : 0 < bound
  /-- The quantity being bounded. -/
  deltaMax : ℝ
  /-- The uniform bound holds. -/
  deltaMax_abs_le : |deltaMax| ≤ bound

/-- **Numerical scale of the uniform bound.**  From the uniform bound on
    `|Δ_max|`, the two-sided enclosure `-bound ≤ Δ_max ≤ bound` follows,
    and the bound is strictly positive so the enclosing interval is
    non-degenerate.

    §3b-conditional on `DeltaMaxNumericalScaleContext`: the bound itself is
    assumed, not established.  The conclusion is *derived* from the
    hypothesis fields rather than projected from a conclusion field, so
    this is not a self-assuming projection. -/
theorem delta_max_numerical_scale [ctx : DeltaMaxNumericalScaleContext] :
    -ctx.bound ≤ ctx.deltaMax ∧ ctx.deltaMax ≤ ctx.bound ∧ 0 < ctx.bound := by
  obtain ⟨hlo, hhi⟩ := abs_le.mp ctx.deltaMax_abs_le
  exact ⟨hlo, hhi, ctx.bound_pos⟩

end QOU.Appendix.DeltaMaxNumericalScale
