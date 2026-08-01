import QOU.Information.SkeinObservationBridge
import QOU.Information.MagnitudeTraceCommutator

/-!
# QOU.Information.SkeinShadowConjInvariance — why the trace-shadow is lossy

`SkeinObservationBridge.haltsObserved_of_halts` proves `Halts ⟹ HaltsObserved`
with the **converse false** — "distinct states can share a Skein value, which is
exactly why the observable is easy and the halting is hard." This file supplies
the **algebraic reason** for that converse-failure, wiring in
`MagnitudeTraceCommutator`: the observation `obs = tr_M` is a *trace*, hence
**conjugation-invariant**, so the observed shadow is blind to any relabeling the
observation collapses — even when the underlying dynamics (`Halts`) is not.

The core is a general fact about any `SkeinObservationSystem`: if a relabeling
`τ : S → S` is one the observation collapses (`obs ∘ τ = obs`) and the reduction
step commutes with (`step ∘ τ = τ ∘ step`), then the whole *observed orbit* is
`τ`-invariant, so `HaltsObserved` cannot tell `P` from `τ P`. For `obs = tr_M`
and `τ =` conjugation-by-`u`, the collapse hypothesis is exactly
`MagnitudeTraceCommutator.magnitude_trace_conj` (`tr(u x u⁻¹) = tr x`) — the
`M ∘ Q = M` operator lemma. So the magnitude/decision wall's easy side (the
trace shadow) is provably conjugation-blind; the hard side (halting/decision)
is not.

All sorry-free. The abstract lemmas are ring-free; the concrete trace witness is
over a generic `{R} [CommRing R]` free finite module (§7c — no archimedean
structure).
-/

universe u v

namespace QOU.Information

open SkeinObservationSystem

variable {S : Type u} {V : Type v} (sys : SkeinObservationSystem S V)

/-- **The observed orbit is invariant under an obs-collapsed, step-equivariant
    relabeling (sorry-free).**  If `τ` commutes with `step` and `obs` collapses
    it (`obs ∘ τ = obs`), then `obs (stepᵏ (τ x)) = obs (stepᵏ x)` for every `k`
    — the observation reads `τ`-conjugate states identically at every stage. -/
theorem obs_iterate_relabel (τ : S → S)
    (hstep : ∀ x, sys.step (τ x) = τ (sys.step x))
    (hobs : ∀ x, sys.obs (τ x) = sys.obs x) :
    ∀ (k : ℕ) (x : S), sys.obs (sys.step^[k] (τ x)) = sys.obs (sys.step^[k] x) := by
  intro k
  induction k with
  | zero => intro x; simpa using hobs x
  | succ n ih =>
      intro x
      rw [Function.iterate_succ_apply, Function.iterate_succ_apply, hstep]
      exact ih (sys.step x)

/-- **The trace-shadow is lossy (sorry-free).**  `HaltsObserved` cannot
    distinguish a state from its relabel: `HaltsObserved (τ P) ↔ HaltsObserved P`
    whenever `τ` is obs-collapsed and step-equivariant.  Since `Halts` is *not*
    `τ`-invariant in general, this is precisely the failed converse of
    `haltsObserved_of_halts` — the observation is easy (blind to `τ`) while the
    dynamics is hard (sees `τ`). -/
theorem haltsObserved_relabel_iff (τ : S → S)
    (hstep : ∀ x, sys.step (τ x) = τ (sys.step x))
    (hobs : ∀ x, sys.obs (τ x) = sys.obs x) (P : S) :
    sys.HaltsObserved (τ P) ↔ sys.HaltsObserved P := by
  constructor
  · rintro ⟨k, hk⟩
    exact ⟨k, by rw [← obs_iterate_relabel sys τ hstep hobs k P]; exact hk⟩
  · rintro ⟨k, hk⟩
    exact ⟨k, by rw [obs_iterate_relabel sys τ hstep hobs k P]; exact hk⟩

/-- **The concrete collapse hypothesis for `obs = tr_M` is `M ∘ Q = M`
    (sorry-free).**  When the observation is the Markov trace, the relabeling the
    shadow is blind to is conjugation `conjOp u`, and the `hobs` hypothesis above
    is exactly `MagnitudeTraceCommutator.magnitude_trace_conj`.  This grounds the
    abstract lossy-shadow lemma in the operator lemma — the trace shadow's
    conjugation-blindness is not assumed but proved. -/
theorem trace_obs_collapses_conj {R : Type*} [CommRing R] {W : Type*}
    [AddCommGroup W] [Module R W] [Module.Free R W] [Module.Finite R W]
    (u : (W →ₗ[R] W)ˣ) (x : W →ₗ[R] W) :
    LinearMap.trace R W (conjOp u x) = LinearMap.trace R W x := by
  rw [conjOp_apply]; exact magnitude_trace_conj u x

end QOU.Information
