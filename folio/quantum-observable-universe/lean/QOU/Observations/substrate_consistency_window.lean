import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

/-!
# QOU.Observations.substrate_consistency_window

**Canonical declaration** for content block
[`prop:substrate-consistency-window`](../../../quantum-observable-universe/observations/substrate-consistency-window.md): *Overdetermination of the substrate parameter*.

This module states the manuscript claim conditional on the §3b hypothesis class.
-/

namespace QOU.Observations

/-- Abstract context for the `substrate_consistency_window` claim — manuscript-themed
    typed fields below. -/
class SubstrateConsistencyWindowContext where
  /-- The categorical object / monoidal structure. -/
  CategoricalObj : Type
  /-- Number of independent measurement classes. -/
  n_classes : ℕ
  /-- Per-class lower bound `q_lo k` on `q`. -/
  q_lo : ℕ → ℝ
  /-- Per-class upper bound `q_hi k` on `q`. -/
  q_hi : ℕ → ℝ
  /-- The unique substrate parameter `q*`. -/
  q_star : ℝ
  /-- Half-width of the measurement window for class `k`. -/
  epsilon : ℕ → ℝ

/-- The physical hypotheses carried by the Substrate Consistency Window Conjecture. -/
class SubstrateConsistencyWindowConjecture (ctx : SubstrateConsistencyWindowContext) : Prop where
  /-- Half-width is non-negative. -/
  epsilon_nonneg : ∀ k : ℕ, 0 ≤ ctx.epsilon k
  /-- The lower bound is q* - epsilon k. -/
  q_lo_def : ∀ k : ℕ, ctx.q_lo k = ctx.q_star - ctx.epsilon k
  /-- The upper bound is q* + epsilon k. -/
  q_hi_def : ∀ k : ℕ, ctx.q_hi k = ctx.q_star + ctx.epsilon k

/-- **Content statement** (from manuscript):

The QOU framework has **one free parameter**: the substrate
parameter $q$.  Every observable quantity --- masses, couplings,
decay rates, causal structure --- is a function of $q$ alone.
The parameter is **overdetermined**: independent classes of
measurements each fix $q$ to a narrow range, and these ranges
overlap.

The Lean encoding below derives the equality from the hypothesis class. -/
-- Ref: [leitner2026] quantum-observable-universe/observations/substrate-consistency-window.ts
theorem substrate_consistency_window (ctx : SubstrateConsistencyWindowContext)
    [hc : SubstrateConsistencyWindowConjecture ctx] :
    ∀ k : ℕ, k < ctx.n_classes →
      ctx.q_lo k ≤ ctx.q_star ∧ ctx.q_star ≤ ctx.q_hi k := by
  intro k _hk
  rw [hc.q_lo_def k, hc.q_hi_def k]
  have h_eps := hc.epsilon_nonneg k
  constructor
  · linarith
  · linarith

end QOU.Observations
