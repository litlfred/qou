import QOU.Archimedean.DilogPartAConvergence

/-!
# Dilog Part B — B3.3 / B3.4 in their bean-stated forms

The analytic content of B3.3 (telescoping left-Riemann error) and B3.4 (tail
bound, `qⁿ ≤ e^{−n(1−q)}`) is proved in `DilogPartAConvergence.lean`
(`riemann_error_bound`, `tail_bound`, `pow_le_exp_neg_mul`).  This file
restates them exactly as the beans `qou-e86p` / `qou-8f2p` phrase them, with
`h(u) = −log(1 − x u)/u`, `0 < x < 1`, `0 < q < 1`:

* **B3.3** `|Σ_{k<n} h(qᵏ)(qᵏ−qᵏ⁺¹) − ∫_{qⁿ}^1 h| ≤ (1−q)(h(1)−h(qⁿ)) ≤ (1−q)(−log(1−x))`;
* **B3.4** `|∫₀^{qⁿ} h| ≤ qⁿ/(1−x)`, `qⁿ ≤ e^{−n(1−q)}`, and `qⁿ → 0` along any
  family with `n(1−q) → ∞`.

-- Ref: [leitner2026] conj:dilogarithm-archimedean-limit
-/

namespace QOU.Archimedean

open intervalIntegral MeasureTheory Filter Topology

/-- **B3.3 (abs form, first inequality).** -/
theorem riemann_error_abs_le {x q : ℝ} (hx0 : 0 < x) (hx1 : x < 1)
    (hq0 : 0 < q) (hq1 : q < 1) (n : ℕ) :
    |(∑ k ∈ Finset.range n,
          (-Real.log (1 - x * q ^ k) / q ^ k) * (q ^ k - q ^ (k + 1)))
        - ∫ u in q ^ n..(1 : ℝ), -Real.log (1 - x * u) / u|
      ≤ (1 - q) * ((-Real.log (1 - x * 1) / 1)
          - (-Real.log (1 - x * q ^ n) / q ^ n)) := by
  obtain ⟨hlo, hhi⟩ := riemann_error_bound hx0 hx1 hq0 hq1 n
  rw [abs_of_nonneg hlo]; exact hhi

/-- **B3.3 (second inequality).** `(1−q)(h(1) − h(qⁿ)) ≤ (1−q)(−log(1−x))`,
    since `h ≥ 0` on `(0,1]`. -/
theorem riemann_error_rhs_le {x q : ℝ} (hx0 : 0 < x) (hx1 : x < 1)
    (hq0 : 0 < q) (hq1 : q < 1) (n : ℕ) :
    (1 - q) * ((-Real.log (1 - x * 1) / 1)
        - (-Real.log (1 - x * q ^ n) / q ^ n))
      ≤ (1 - q) * (-Real.log (1 - x)) := by
  have hnn := (h_bounds_Ioc hx0 hx1 (pow_pos hq0 n) (pow_le_one₀ hq0.le hq1.le)).1
  rw [mul_one, div_one]
  exact mul_le_mul_of_nonneg_left (by linarith) (by linarith)

/-- **B3.3 (bean form).**
    `|Σ_{k<n} h(qᵏ)(qᵏ−qᵏ⁺¹) − ∫_{qⁿ}^1 h| ≤ (1−q)(−log(1−x))`. -/
theorem riemann_error_abs_le_log {x q : ℝ} (hx0 : 0 < x) (hx1 : x < 1)
    (hq0 : 0 < q) (hq1 : q < 1) (n : ℕ) :
    |(∑ k ∈ Finset.range n,
          (-Real.log (1 - x * q ^ k) / q ^ k) * (q ^ k - q ^ (k + 1)))
        - ∫ u in q ^ n..(1 : ℝ), -Real.log (1 - x * u) / u|
      ≤ (1 - q) * (-Real.log (1 - x)) :=
  (riemann_error_abs_le hx0 hx1 hq0 hq1 n).trans (riemann_error_rhs_le hx0 hx1 hq0 hq1 n)

/-- **B3.4 (tail, bean form).** `|∫₀^{qⁿ} h| ≤ qⁿ/(1−x)` (in fact `≤ qⁿ·x/(1−x)`). -/
theorem tail_abs_le {x q : ℝ} (hx0 : 0 < x) (hx1 : x < 1)
    (hq0 : 0 < q) (hq1 : q ≤ 1) (n : ℕ) :
    |∫ u in (0 : ℝ)..q ^ n, -Real.log (1 - x * u) / u| ≤ q ^ n / (1 - x) := by
  have hqn := pow_pos hq0 n
  obtain ⟨hlo, hhi⟩ := tail_bound hx0 hx1 hqn (pow_le_one₀ hq0.le hq1)
  rw [abs_of_nonneg hlo]
  refine hhi.trans ?_
  rw [mul_div_assoc']
  exact div_le_div_of_nonneg_right (by nlinarith) (by linarith)

/-- **B3.4 (decay).** Along any family with `n(1−q) → ∞` (and `q > 0`),
    `qⁿ → 0`, via `0 < qⁿ ≤ e^{−n(1−q)}` (`pow_le_exp_neg_mul`). -/
theorem tendsto_pow_zero_of_mul_one_sub {ι : Type*} {l : Filter ι}
    {q : ι → ℝ} {n : ι → ℕ} (hq0 : ∀ i, 0 < q i)
    (hn : Tendsto (fun i => (n i : ℝ) * (1 - q i)) l atTop) :
    Tendsto (fun i => q i ^ n i) l (𝓝 0) := by
  have hexp : Tendsto (fun i => Real.exp (-((n i : ℝ) * (1 - q i)))) l (𝓝 0) :=
    Real.tendsto_exp_neg_atTop_nhds_zero.comp hn
  exact tendsto_of_tendsto_of_tendsto_of_le_of_le tendsto_const_nhds hexp
    (fun i => (pow_pos (hq0 i) _).le) (fun i => pow_le_exp_neg_mul (hq0 i) (n i))

end QOU.Archimedean
