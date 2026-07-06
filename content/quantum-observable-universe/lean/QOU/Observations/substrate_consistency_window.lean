import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

/-!
# QOU.Observations.substrate_consistency_window

**Canonical declaration** for content block
[`prop:substrate-consistency-window`](../../../quantum-observable-universe/observations/substrate-consistency-window.md): *Overdetermination of the substrate parameter*.

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.
-/

namespace QOU.Observations


/-- Abstract context for the `substrate_consistency_window` claim — manuscript-themed
    typed fields below; `holds` carries the residual `Prop` claim. -/
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
  /-- Half-width is non-negative. -/
  epsilon_nonneg : ∀ k : ℕ, 0 ≤ epsilon k
  /-- The lower bound is q* - epsilon k. -/
  q_lo_def : ∀ k : ℕ, q_lo k = q_star - epsilon k
  /-- The upper bound is q* + epsilon k. -/
  q_hi_def : ∀ k : ℕ, q_hi k = q_star + epsilon k

/-- **Content statement** (from manuscript):

The QOU framework has **one free parameter**: the substrate
parameter $q$.  Every observable quantity --- masses, couplings,
decay rates, causal structure --- is a function of $q$ alone.
The parameter is **overdetermined**: independent classes of
measurements each fix $q$ to a narrow range, and these ranges
overlap.

    The Lean encoding below states the manuscript claim over a context class and discharges it from the class's fields (§3b-conditional). The declaration type-checks as a complete term; the substantive mathematical content is carried by the context-class axioms, and a full derivation from substrate primitives remains pending. -/
-- Ref: [manuscript] quantum-observable-universe/observations/substrate-consistency-window.ts
theorem substrate_consistency_window [ctx : SubstrateConsistencyWindowContext] :
    ∀ k : ℕ, k < ctx.n_classes →
      ctx.q_lo k ≤ ctx.q_star ∧ ctx.q_star ≤ ctx.q_hi k := by
  intro k _hk
  rw [ctx.q_lo_def k, ctx.q_hi_def k]
  have h_eps := ctx.epsilon_nonneg k
  constructor
  · linarith
  · linarith

end QOU.Observations
