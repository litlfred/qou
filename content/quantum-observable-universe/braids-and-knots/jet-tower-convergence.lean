import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Analysis.SpecificLimits.Normed
import Mathlib.Topology.Algebra.InfiniteSum.Basic
import Mathlib.Topology.Algebra.InfiniteSum.Real

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

open scoped BigOperators
open Filter Topology

/-- Comparison: `r^(n+1) * |Δ (n+1)| ≤ r^(n+1) * Δmax` when `|Δ k| ≤
Δmax` and `r ≥ 0`.  Used for Weierstrass M-test. -/
lemma abs_term_le_geom {r : ℝ} (hr0 : 0 ≤ r)
    {Δ : ℕ → ℝ} {Δmax : ℝ} (hbound : ∀ n, |Δ n| ≤ Δmax) (n : ℕ) :
    |r ^ (n + 1) * Δ (n + 1)| ≤ r ^ (n + 1) * Δmax := by
  rw [abs_mul, abs_of_nonneg (pow_nonneg hr0 _)]
  exact mul_le_mul_of_nonneg_left (hbound _) (pow_nonneg hr0 _)

/-- Summability of the brane-tower term series from the comparison
bound with a convergent geometric.

Ref: [leitner2026] https://github.com/litlfred/qou -/
lemma summable_tower_terms {r : ℝ} (hr0 : 0 ≤ r) (hr1 : r < 1)
    {Δ : ℕ → ℝ} {Δmax : ℝ} (hΔmax : 0 ≤ Δmax)
    (hbound : ∀ n, |Δ n| ≤ Δmax) :
    Summable (fun n : ℕ => r ^ (n + 1) * Δ (n + 1)) := by
  -- Ref: [leitner2026]
  -- Weierstrass M-test against the convergent ∑ r^(n+1) · Δmax.
  sorry

/-- Tail bound for the geometric series `∑_{k} r^k = r^N / (1 - r)`
after truncation at N. -/
lemma geometric_tail_bound {r : ℝ} (hr0 : 0 ≤ r) (hr1 : r < 1)
    (N : ℕ) :
    ∑' n : ℕ, r ^ (n + N + 1) = r ^ (N + 1) / (1 - r) := by
  -- Ref: [leitner2026]
  -- Shift by N+1 and apply `tsum_geometric_of_lt_one`.
  sorry

/-- Geometric-series tail bound for the brane-tower sum.

For any ratio `r ∈ [0, 1)`, any sequence `Δ : ℕ → ℝ` with pointwise
bound `|Δ n| ≤ Δmax`, and any truncation point `N : ℕ`, the tail of
the `∑ r^(n+1) · Δ (n+1)` series is bounded by
`Δmax · r^(N+1) / (1 - r)`.

This theorem reduces the jet-tower convergence question
(`rem:mass-endomorphism-jet-tower` open subconjecture 1) to a
boundedness statement on `Δ n`: once that is established, the
geometric series tail gives the absolute truncation error.

Ref: [leitner2026] https://github.com/litlfred/qou -/
theorem jet_tower_tail_bound
    (r : ℝ) (hr0 : 0 ≤ r) (hr1 : r < 1)
    (Δ : ℕ → ℝ) (Δmax : ℝ) (hΔmax : 0 ≤ Δmax)
    (hbound : ∀ n, |Δ n| ≤ Δmax)
    (N : ℕ) :
    ∃ T : ℝ,
      (HasSum (fun n => r ^ (n + 1) * Δ (n + 1)) T) ∧
      |T - ∑ n ∈ Finset.range N, r ^ (n + 1) * Δ (n + 1)|
        ≤ Δmax * r ^ (N + 1) / (1 - r) := by
  -- Ref: [leitner2026] — summability and the explicit tail bound
  -- follow from `summable_tower_terms` and `geometric_tail_bound`.
  have hsum : Summable (fun n : ℕ => r ^ (n + 1) * Δ (n + 1)) :=
    summable_tower_terms hr0 hr1 hΔmax hbound
  refine ⟨∑' n, r ^ (n + 1) * Δ (n + 1), hsum.hasSum, ?_⟩
  -- Tail = T - Σ_{n<N}; bound by Δmax · r^(N+1) / (1-r).
  sorry

/-- Engineering-facing corollary: number of jet levels needed to
achieve binding-energy precision `ε`.

The bound `E₀ · Δmax · r^(N+1) / (1 - r) ≤ ε` becomes a log
inequality:  `N ≥ ⌈log((ε · (1 - r)) / (E₀ · Δmax)) / log(r)⌉ - 1`.

Ref: [leitner2026] https://github.com/litlfred/qou -/
theorem jet_levels_for_precision
    (r : ℝ) (hr0 : 0 < r) (hr1 : r < 1)
    (E₀ Δmax ε : ℝ) (hE₀ : 0 < E₀) (hΔmax : 0 < Δmax) (hε : 0 < ε) :
    ∃ N : ℕ, E₀ * Δmax * r ^ (N + 1) / (1 - r) ≤ ε := by
  -- Ref: [leitner2026]
  -- r^n → 0 as n → ∞ since 0 < r < 1; take N large enough.
  have hr_tendsto : Filter.Tendsto (fun n : ℕ => r ^ n) Filter.atTop
      (𝓝 0) := tendsto_pow_atTop_nhds_zero_of_lt_one hr0.le hr1
  sorry

end QOU.MassEndomorphism
