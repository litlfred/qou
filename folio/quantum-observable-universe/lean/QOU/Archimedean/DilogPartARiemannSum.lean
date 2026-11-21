import QOU.Archimedean.DilogarithmArchimedeanLimit

/-!
# Part A of `conj:dilogarithm-archimedean-limit` — the Riemann-sum reduction

The elementary `q → 1⁻` side of the Archimedean-limit conjecture:
`(1-q)·log Φ_n(x; q) → Li₂(x)`.  With `Φ_n = (∏_{k<n}(1 - x qᵏ))⁻¹` this is a
**Riemann-sum limit** — `(1-q)·Σ_{k<n} −log(1 - x qᵏ) → ∫₀ˣ −log(1-t)/t = Li₂(x)`
(the integral identity is `DilogReflection.LiTwo_eq_integral`, landed 2026-07-19).

This file builds the **algebraic reduction bricks** that turn the `ArchimedeanLimit`
class field into an explicit Riemann sum:

* `denomPolyLocal_eq_prod` — the recursive denominator is the finite product
  `∏_{k<n}(1 - x qᵏ)`.
* `log_partialProduct_eq_neg_sum` — `log Φ_n(x;q) = −Σ_{k<n} log(1 - x qᵏ)`
  for `0 < x < 1`, `0 < q ≤ 1` (every factor is positive).

The remaining Riemann-sum convergence (the uniform-partition limit in the
`s = k·(−log q)` variable, with the `(1-q)/(−log q) → 1` correction) is the
genuine analytic core of Part A — scoped here, not yet discharged.  Part B
(substrate continuation `q → 1⁺`, `x → 1⁻` uniformity) is untouched.

-- Ref: [leitner2026] conj:dilogarithm-archimedean-limit
-- Ref: [faddeev1994] https://doi.org/10.1142/S0217732394002793
-/

namespace QOU.QPochhammer

open scoped BigOperators
open Filter Topology

-- `denomPolyLocal_eq_prod` (the finite `q`-Pochhammer product form) is imported
-- from `QOU.Archimedean.DilogarithmArchimedeanLimit`, where the identical lemma
-- also lives. A duplicate copy declared here as well broke the build with
-- "already declared" once both landed on main (same namespace, this file imports
-- that one); removed 2026-07-24.

/-- **Brick 1 — the Riemann-sum reduction.**  For `0 < x < 1` and `0 < q ≤ 1`
    every factor `1 - x qᵏ` is positive, so the rescaled logarithm of the partial
    product is a finite sum:  `log Φ_n(x;q) = −Σ_{k<n} log(1 - x qᵏ)`. -/
theorem log_partialProduct_eq_neg_sum {q x : ℝ} (hx0 : 0 < x) (hx1 : x < 1)
    (hq0 : 0 < q) (hq1 : q ≤ 1) (n : ℕ) :
    Real.log (partialProductLocal q x n)
      = -∑ k ∈ Finset.range n, Real.log (1 - x * q ^ k) := by
  have hfac : ∀ k ∈ Finset.range n, (1 - x * q ^ k) ≠ 0 := by
    intro k _
    have hle : x * q ^ k ≤ x := by
      calc x * q ^ k ≤ x * 1 := by
            exact mul_le_mul_of_nonneg_left (pow_le_one₀ hq0.le hq1) hx0.le
        _ = x := mul_one x
    exact ne_of_gt (by linarith)
  unfold partialProductLocal
  rw [Real.log_inv, denomPolyLocal_eq_prod, Real.log_prod _ _ hfac]

/-- **Brick 2 — the Riemann-sum structure.**  The rescaled sum
    `(1-q)·Σ_{k<n} −log(1 - x qᵏ)` is *exactly* the left-endpoint Riemann sum of
    the integrand `h(u) = −log(1 - x u)/u` over the geometric partition
    `1 = q⁰ > q¹ > ⋯ > qⁿ`, whose `k`-th cell has width `qᵏ − qᵏ⁺¹ = qᵏ(1-q)`:

    `(1-q)·Σ_{k<n} −log(1 - x qᵏ) = Σ_{k<n} h(qᵏ)·(qᵏ − qᵏ⁺¹)`.

    As `q → 1⁻` (mesh → 0) with `qⁿ → 0` (the partition fills `(0,1]`), this
    Riemann sum converges to `∫₀¹ −log(1 - x u)/u du = Li₂(x)` — the remaining
    analytic core of Part A. -/
theorem riemann_sum_form {q x : ℝ} (hq0 : 0 < q) (n : ℕ) :
    (1 - q) * ∑ k ∈ Finset.range n, -Real.log (1 - x * q ^ k)
      = ∑ k ∈ Finset.range n,
          -Real.log (1 - x * q ^ k) / q ^ k * (q ^ k - q ^ (k + 1)) := by
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl (fun k _ => ?_)
  have hqk : q ^ k ≠ 0 := ne_of_gt (pow_pos hq0 k)
  rw [pow_succ]
  field_simp

/-- **m-series termwise-limit ingredient (1) — the per-term coefficient limit.**
    (Independent of the leading Riemann-sum route in `DilogPartAConvergence.lean`
    / PR #4106; this is the parallel `m`-series route.)  In the `m`-series form
    of `(1-q)·log Φ_n` (`partialProduct_log_eq_mseries`), the `q`-dependent
    rescaling of the `m`-th term is `(1-q)/(q^{m+1}-1)`, and it tends to the
    Riemann weight `-1/(m+1)` as `q → 1`.  Proof: for `q ≠ 1`,
    `q^{m+1}-1 = (q-1)·Σ_{j≤m} qʲ` (`geom_sum_eq`), so the ratio equals
    `-1/Σ_{j≤m} qʲ`, which is continuous at `q = 1` with value `-1/(m+1)`.
    Combined with `qⁿ⁽ᵐ⁺¹⁾ → 0` (when `n(1-q) → ∞`) this gives the termwise limit
    `x^{m+1}/(m+1)²`; the dominated-convergence exchange with the `m`-sum is the
    remaining core (still open). -/
theorem tendsto_one_sub_div_pow_sub_one (m : ℕ) :
    Tendsto (fun q : ℝ => (1 - q) / (q ^ (m + 1) - 1)) (𝓝[≠] 1)
      (𝓝 (-1 / ((m : ℝ) + 1))) := by
  have hcong : (fun q : ℝ => (1 - q) / (q ^ (m + 1) - 1))
      =ᶠ[𝓝[≠] 1] fun q : ℝ => -1 / (∑ j ∈ Finset.range (m + 1), q ^ j) := by
    filter_upwards [self_mem_nhdsWithin] with q hq
    have hsub : q - 1 ≠ 0 := sub_ne_zero.mpr hq
    have hgm : q ^ (m + 1) - 1 = (q - 1) * (∑ j ∈ Finset.range (m + 1), q ^ j) := by
      rw [← geom_sum_mul]; ring
    rw [hgm, show (1 : ℝ) - q = (q - 1) * (-1 : ℝ) by ring, mul_div_mul_left _ _ hsub]
  rw [tendsto_congr' hcong]
  have hcont : Tendsto (fun q : ℝ => ∑ j ∈ Finset.range (m + 1), q ^ j) (𝓝 1)
      (𝓝 ((m : ℝ) + 1)) := by
    have h := tendsto_finset_sum (Finset.range (m + 1))
      (fun j _ => (continuous_pow j).tendsto (1 : ℝ))
    simpa using h
  have hne : ((m : ℝ) + 1) ≠ 0 := by positivity
  exact (tendsto_const_nhds.div hcont hne).mono_left nhdsWithin_le_nhds

/-- **m-series termwise-limit ingredient (2) — the tail factor vanishes.**  For `0 < q < 1` the numerator
    tail `q^{(m+1)n} → 0` as `n → ∞` (`= (q^{m+1})ⁿ` with `0 < q^{m+1} < 1`).  This
    is the `n → ∞` half of the `q^{(m+1)n} → 0` behaviour that, jointly with
    `n(1-q) → ∞`, sends the numerator `(q^{(m+1)n} − 1) → −1`; combined with
    Brick 3 the `m`-th term tends to the Riemann weight `x^{m+1}/(m+1)²`. -/
theorem tendsto_pow_mul_nhds_zero {q : ℝ} (hq0 : 0 < q) (hq1 : q < 1) (m : ℕ) :
    Tendsto (fun n : ℕ => q ^ ((m + 1) * n)) atTop (𝓝 0) := by
  have hbase0 : (0 : ℝ) ≤ q ^ (m + 1) := (pow_pos hq0 _).le
  have hbase1 : q ^ (m + 1) < 1 := pow_lt_one₀ hq0.le hq1 (Nat.succ_ne_zero m)
  have h := tendsto_pow_atTop_nhds_zero_of_lt_one hbase0 hbase1
  simpa [pow_mul] using h

end QOU.QPochhammer
