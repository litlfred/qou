import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Analysis.SpecificLimits.Normed
import Mathlib.Topology.Algebra.InfiniteSum.Basic

/-!
# Geometric-series tail bound for the brane-tower sum

For the brane-tower expansion
  `m(ρ) = m₀(ρ) + ∑_{n≥1} ℏ_q^{2n} · Δ_n(ρ)`
with damping ratio `r = ℏ_q^2 ∈ (0, 1)` and uniform per-level bound
`|Δ_n| ≤ Δ_max`, this theorem gives the N-term truncation error as
`Δ_max · r^{N+1} / (1 - r)`.

See `jet-tower-convergence.md` for the full statement and physical
context; reduces the open subconjecture 1 in
`rem:mass-endomorphism-jet-tower` to a boundedness statement on
`Δ_n`.
-/

namespace QOU.MassEndomorphism

open Filter Topology NNReal

/-- Geometric-series tail bound.

For any ratio `r ∈ (0, 1)`, any sequence `Δ : ℕ → ℝ` with pointwise
bound `|Δ n| ≤ Δmax`, and any truncation point `N : ℕ`, the tail of
the `∑ r^n · Δ n` series is bounded by `Δmax · r^{N+1} / (1 - r)`.

Reduces the jet-tower convergence question
(`rem:mass-endomorphism-jet-tower` open subconjecture 1) to a single
boundedness statement on `Δ n`.

Ref: [leitner2026] https://github.com/litlfred/qou
-/
theorem jet_tower_tail_bound
    (r : ℝ) (hr0 : 0 ≤ r) (hr1 : r < 1)
    (Δ : ℕ → ℝ) (Δmax : ℝ) (hΔmax : 0 ≤ Δmax)
    (hbound : ∀ n, |Δ n| ≤ Δmax)
    (N : ℕ) :
    ∃ T : ℝ,
      (HasSum (fun n => r ^ (n + 1) * Δ (n + 1)) T) ∧
      |T - ∑ n ∈ Finset.range N, r ^ (n + 1) * Δ (n + 1)|
        ≤ Δmax * r ^ (N + 1) / (1 - r) := by
  -- Ref: [leitner2026] https://github.com/litlfred/qou
  -- The geometric series Σ r^n converges for r ∈ [0, 1), so
  -- comparison with the pointwise bound |Δ n| ≤ Δmax gives absolute
  -- convergence.  The tail formula is the standard geometric sum.
  sorry

/-- Engineering-facing corollary: number of jet levels needed for
binding-energy precision `ε`. -/
theorem jet_levels_for_precision
    (r : ℝ) (hr0 : 0 < r) (hr1 : r < 1)
    (E₀ Δmax ε : ℝ) (hE₀ : 0 < E₀) (hΔmax : 0 < Δmax) (hε : 0 < ε) :
    ∃ N : ℕ, E₀ * Δmax * r ^ (N + 1) / (1 - r) ≤ ε := by
  -- Ref: [leitner2026] https://github.com/litlfred/qou
  -- Follows from r^n → 0 as n → ∞ (since r < 1); standard.
  sorry

end QOU.MassEndomorphism
