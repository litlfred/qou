import Mathlib.MeasureTheory.Integral.CircleIntegral
import Mathlib.Analysis.Meromorphic.Divisor

/-!
# Two Mathlib gaps at our pinned revision

Both statements below exist in current Mathlib but not at the revision this
project pins (`f897ebcf`). They are stated here in Mathlib's own shape so that
the eventual pin bump deletes this file rather than requiring a rewrite.

* `integral_fun_sum` — linearity of the circle integral over a `Finset` sum.
  Upstream as `circleIntegral.integral_fun_sum`.
* `divisor_support_finite_of_subset` — a meromorphic function on a *compact* set
  has finitely many zeros and poles on any subset. Upstream as
  `MeromorphicOn.divisor_support_finite_of_subset`.

Together with `MeromorphicOn.extract_zeros_poles` — which *is* present at the pin
— these are what a `Finset`-indexed argument principle consumes: the
factorisation supplies the finitely many factors, this supplies their finiteness,
and the first lets the contour integral be taken term by term.

-- Ref: [manuscript] bean `qou-argp` — the converse theta zero locus.
-/

open scoped Real
open MeasureTheory

namespace QOU.Mathlib

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℂ E]

/-- Linearity of the circle integral over a `Finset` sum.

Mirrors Mathlib's own proof: unfold `circleIntegral` and apply
`intervalIntegral.integral_finset_sum`. -/
theorem integral_fun_sum {ι : Type*} {s : Finset ι} {f : ι → ℂ → E} {c : ℂ} {R : ℝ}
    (h : ∀ i ∈ s, CircleIntegrable (f i) c R) :
    (∮ z in C(c, R), ∑ i ∈ s, f i z) = ∑ i ∈ s, ∮ z in C(c, R), f i z := by
  simp only [circleIntegral, Finset.smul_sum,
    intervalIntegral.integral_finset_sum fun i hi ↦ (h i hi).out]

section Divisor

variable {𝕜 : Type*} [NontriviallyNormedField 𝕜] {F : Type*} [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] {U : Set 𝕜}

/-- If `f` is meromorphic on a compact `U` and `V ⊆ U`, the divisor of `f` on `V`
has finite support.

The support is discrete (isolated zeros) and closed in `U`; a discrete closed
subset of a compact set is finite. `divisor_restrict` transports that from `U`
to `V`. -/
theorem divisor_support_finite_of_subset {f : 𝕜 → F} {V : Set 𝕜}
    (hf : MeromorphicOn f U) (hU : IsCompact U) (hV : V ⊆ U) :
    (MeromorphicOn.divisor f V).support.Finite := by
  rw [← MeromorphicOn.divisor_restrict hf hV]
  refine ((MeromorphicOn.divisor f U).finiteSupport hU).subset ?_
  intro z hz
  rw [Function.mem_support] at hz ⊢
  by_cases hzV : z ∈ V
  · rwa [Function.locallyFinsuppWithin.restrict_apply, if_pos hzV] at hz
  · rw [Function.locallyFinsuppWithin.restrict_apply, if_neg hzV] at hz
    exact absurd rfl hz

end Divisor

end QOU.Mathlib
