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

-- ── Private helper: tsum splits into a finite partial sum plus tail ──────────

/-- The tsum over ℕ equals the finite partial sum up to N plus the tail
    `∑' k, f(k + N)`.  Proved by induction using `tsum_eq_zero_add`. -/
private lemma tsum_sum_add_tail {f : ℕ → ℝ} (hf : Summable f) (N : ℕ) :
    ∑' n, f n = ∑ i ∈ Finset.range N, f i + ∑' k, f (k + N) := by
  induction N with
  | zero => simp
  | succ m ih =>
    rw [ih]
    have hshift : ∑' k, f (k + m) = f m + ∑' k, f (k + (m + 1)) := by
      rw [tsum_eq_zero_add (hf.nat_add m)]
      simp only [zero_add]
      congr 1
      apply tsum_congr; intro k; ring
    rw [hshift, ← add_assoc, ← Finset.sum_range_succ]

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
  apply summable_of_norm_bounded (fun n => r ^ (n + 1) * Δmax)
  · -- The bounding series r^(n+1)*Δmax is summable: factor as (r^n*r)*Δmax.
    have hg : Summable (fun n : ℕ => r ^ (n + 1)) := by
      have : (fun n : ℕ => r ^ (n + 1)) = fun n => r ^ n * r := funext (fun n => by ring)
      rw [this]
      exact (summable_geometric_of_lt_one hr0 hr1).mul_right r
    exact hg.mul_right Δmax
  · intro n; exact abs_term_le_geom hr0 hbound n

/-- Tail bound for the geometric series `∑_{k} r^k = r^N / (1 - r)`
after truncation at N. -/
lemma geometric_tail_bound {r : ℝ} (hr0 : 0 ≤ r) (hr1 : r < 1)
    (N : ℕ) :
    ∑' n : ℕ, r ^ (n + N + 1) = r ^ (N + 1) / (1 - r) := by
  -- Ref: [leitner2026]
  -- Shift by N+1 and apply `tsum_geometric_of_lt_one`.
  simp_rw [show ∀ n : ℕ, r ^ (n + N + 1) = r ^ (N + 1) * r ^ n from fun n => by ring]
  rw [tsum_mul_left, tsum_geometric_of_lt_one hr0 hr1]
  ring

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
  -- Step 1: decompose the tsum into partial sum + tail ∑' k, r^(k+N+1)*Δ(k+N+1).
  have htail_eq : ∑' k : ℕ, r ^ (k + N + 1) * Δ (k + N + 1) =
      ∑' n, r ^ (n + 1) * Δ (n + 1) - ∑ n ∈ Finset.range N, r ^ (n + 1) * Δ (n + 1) := by
    have hsplit := tsum_sum_add_tail hsum N
    have hcong : ∑' k, (fun n : ℕ => r ^ (n + 1) * Δ (n + 1)) (k + N) =
                 ∑' k, r ^ (k + N + 1) * Δ (k + N + 1) :=
      tsum_congr (fun k => by simp; ring)
    linarith [hsplit, hcong.symm]
  -- Step 2: the tail terms are summable.
  have htail_summable : Summable (fun k : ℕ => r ^ (k + N + 1) * Δ (k + N + 1)) := by
    apply summable_of_norm_bounded (fun k => r ^ (k + N + 1) * Δmax)
    · have : (fun k : ℕ => r ^ (k + N + 1) * Δmax) =
             fun k => r ^ (N + 1) * r ^ k * Δmax := funext (fun k => by ring)
      rw [this]
      exact ((summable_geometric_of_lt_one hr0 hr1).mul_left _).mul_right _
    · intro k; exact abs_term_le_geom hr0 hbound (k + N)
  -- Step 3: bound |tail| ≤ ∑' k, r^(k+N+1)*Δmax = Δmax*r^(N+1)/(1-r).
  rw [← htail_eq]
  have hbound_sum : Summable (fun k : ℕ => r ^ (k + N + 1) * Δmax) := by
    have : (fun k : ℕ => r ^ (k + N + 1) * Δmax) =
           fun k => r ^ (N + 1) * r ^ k * Δmax := funext (fun k => by ring)
    rw [this]
    exact ((summable_geometric_of_lt_one hr0 hr1).mul_left _).mul_right _
  calc |∑' k, r ^ (k + N + 1) * Δ (k + N + 1)|
      ≤ ∑' k, |r ^ (k + N + 1) * Δ (k + N + 1)| := by
          have h := norm_tsum_le_tsum_norm htail_summable.norm
          simp only [Real.norm_eq_abs] at h; exact h
    _ ≤ ∑' k, r ^ (k + N + 1) * Δmax :=
          tsum_le_tsum (fun k => abs_term_le_geom hr0 hbound (k + N))
            (by simpa [Real.norm_eq_abs] using htail_summable.norm) hbound_sum
    _ = Δmax * r ^ (N + 1) / (1 - r) := by
          simp_rw [show ∀ k : ℕ, r ^ (k + N + 1) * Δmax = r ^ (N + 1) * Δmax * r ^ k
            from fun k => by ring]
          rw [tsum_mul_left, tsum_geometric_of_lt_one hr0 hr1]; ring

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
  have h1r : 0 < 1 - r := by linarith
  have hprod : 0 < E₀ * Δmax := mul_pos hE₀ hΔmax
  -- Set the threshold c = ε*(1-r)/(E₀*Δmax); we need r^(N+1) ≤ c.
  set c := ε * (1 - r) / (E₀ * Δmax) with hc_def
  have hc : 0 < c := by unfold_let c; positivity
  rw [Metric.tendsto_atTop] at hr_tendsto
  obtain ⟨N₀, hN₀⟩ := hr_tendsto c hc
  refine ⟨N₀, ?_⟩
  have hrN : r ^ (N₀ + 1) < c := by
    have h := hN₀ (N₀ + 1) (Nat.le_succ _)
    simp only [Real.dist_eq, sub_zero, abs_of_nonneg (pow_nonneg hr0.le _)] at h
    exact h
  rw [div_le_iff h1r]
  have h2 : E₀ * Δmax * r ^ (N₀ + 1) < E₀ * Δmax * c :=
    mul_lt_mul_of_pos_left hrN hprod
  calc E₀ * Δmax * r ^ (N₀ + 1) < E₀ * Δmax * c := h2
    _ = ε * (1 - r) := by rw [hc_def]; field_simp

end QOU.MassEndomorphism
