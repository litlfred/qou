import Mathlib.MeasureTheory.Integral.CircleIntegral
import Mathlib.Analysis.Meromorphic.Divisor
import Mathlib.Analysis.Analytic.IsolatedZeros

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
open MeasureTheory Filter Set Topology

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

section IdentityTheorem

/-- Analytic functions agreeing codiscretely on a preconnected set agree on it. -/
theorem eqOn_of_eventuallyEq_codiscreteWithin {f g : ℂ → ℂ} {U : Set ℂ}
    (hf : AnalyticOnNhd ℂ f U) (hg : AnalyticOnNhd ℂ g U) (hU : IsPreconnected U)
    [NeBot (codiscreteWithin U)]
    (h : f =ᶠ[codiscreteWithin U] g) : EqOn f g U := by
  rcases hf.eqOn_or_eventually_ne_of_preconnected hg hU with h' | h'
  · exact h'
  · exact absurd (eventually_false_iff_eq_bot.mp ((h.and h').mono fun _ hx => hx.2 hx.1))
      (NeBot.ne inferInstance)



section NeBot

open Topology

/-- For a nonempty open `U ⊆ ℂ`, the codiscrete-within filter is non-trivial.
Without this the lemma above is vacuous. -/
theorem codiscreteWithin_neBot {U : Set ℂ} (hU : IsOpen U) (hne : U.Nonempty) :
    NeBot (codiscreteWithin U) := by
  obtain ⟨x, hx⟩ := hne
  rw [neBot_iff]
  intro hbot
  have hmem : (∅ : Set ℂ) ∈ codiscreteWithin U := hbot ▸ Filter.mem_bot
  rw [mem_codiscreteWithin] at hmem
  have hdis := hmem x hx
  rw [Set.diff_empty, disjoint_iff] at hdis
  -- `𝓝[≠] x ⊓ 𝓟 U = 𝓝[{x}ᶜ ∩ U] x`, and restricting to the neighbourhood `U`
  -- does not change it, so it is `𝓝[≠] x` — non-trivial, as `ℂ` has no
  -- isolated points.
  rw [nhdsWithin, inf_assoc, inf_principal, ← nhdsWithin] at hdis
  have hUmem : U ∈ 𝓝[{x}ᶜ] x := nhdsWithin_le_nhds (hU.mem_nhds hx)
  have heq : 𝓝[{x}ᶜ ∩ U] x = 𝓝[≠] x := nhdsWithin_inter_of_mem' hUmem
  rw [heq] at hdis
  exact (PerfectSpace.not_isolated x).ne hdis

end NeBot

end IdentityTheorem

end QOU.Mathlib
