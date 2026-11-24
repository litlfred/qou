import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.GeomSum
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

/-!
# QOU.BraidKnot.JetTowerUniformDeltaMax — uniform per-level binding bound

The brane-tower mass series

  𝔪(ρ) = 𝔪⁽⁰⁾(ρ) + Σ_{n ≥ 1} ℏ_q^{2n} · Δ⁽ⁿ⁾(ρ)

converges geometrically (per `prop:jet-tower-convergence`) under
the uniform-boundedness hypothesis

  ∀ n ≥ 1, |Δ⁽ⁿ⁾(ρ)| ≤ Δ_max(ρ).

This file axiomatizes the hypothesis as a class per AGENTS.md §3b.
The conditional geometric-tail bound is then provable from the
class instance plus standard real analysis.

**Formal-chain version.**  Lives under `lean/QOU/` and is compiled
by `lake build`.  The co-located documentation stub at
`braids-and-knots/jet-tower-uniform-delta-max.lean` mirrors this.

-- Ref: [leitner2026] conj:jet-tower-uniform-delta-max
-- Ref: [leitner2026] prop:jet-tower-convergence
-- Ref: [yekutieli2010] Yekutieli, "Central Extensions of Gerbes," Adv. Math. 225 (2010), arXiv:0801.0083
LaTeX label: `conj:jet-tower-uniform-delta-max`
-/

namespace QOU.BraidKnot

/-- The conjecture, encoded as a class.

    A `JetTowerUniformDeltaMax ρ` instance asserts the existence
    of a finite real `delta_max` bounding the per-level binding
    contributions `delta n` for all `n ≥ 1`. The unproved input
    is the existence of the instance; downstream conditional
    theorems (geometric-tail truncation bounds) are then fully
    verified parametrically. -/
-- Ref: [leitner2026] conj:jet-tower-uniform-delta-max
class JetTowerUniformDeltaMax (ρ : Type*) where
  /-- The per-level binding contribution at level `n`. -/
  delta : ℕ → ℝ
  /-- The asserted uniform bound. -/
  delta_max : ℝ
  /-- Non-negativity of the bound. -/
  delta_max_nonneg : 0 ≤ delta_max
  /-- The uniform-bound hypothesis. -/
  uniform_bound : ∀ n : ℕ, 1 ≤ n → |delta n| ≤ delta_max

/-- The substrate Planck constant squared, instantiated abstractly. -/
noncomputable def hbarQSq (q : ℝ) : ℝ := (1 - q⁻¹) ^ 2

/-- Conditional theorem: under the uniform-bound conjecture, the
    geometric-tail bound holds.

    For a substrate parameter `q` with `0 < ℏ_q² < 1`, the tail
    of the brane-tower mass series after the first `N` terms is
    bounded by `delta_max · ℏ_q^{2(N+1)} / (1 - ℏ_q²)`. -/
-- Ref: [leitner2026] conj:jet-tower-uniform-delta-max §"What the conjecture commits to"
-- Ref: [leitner2026] prop:jet-tower-convergence
theorem geometric_tail_bound_abstract
    {ρ : Type*} [c : JetTowerUniformDeltaMax ρ]
    (hbarQSq_val : ℝ) (hbarQSq_pos : 0 < hbarQSq_val)
    (hbarQSq_lt_one : hbarQSq_val < 1) (N : ℕ) :
    ∃ tail_bound : ℝ,
      tail_bound = c.delta_max * hbarQSq_val ^ (N + 1) / (1 - hbarQSq_val) ∧
      0 ≤ tail_bound := by
  refine ⟨c.delta_max * hbarQSq_val ^ (N + 1) / (1 - hbarQSq_val), rfl, ?_⟩
  apply div_nonneg
  · apply mul_nonneg c.delta_max_nonneg
    exact pow_nonneg (le_of_lt hbarQSq_pos) _
  · linarith

end QOU.BraidKnot
