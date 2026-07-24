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

-- Ref: [manuscript] conj:dilogarithm-archimedean-limit
-- Ref: [faddeev1994] https://doi.org/10.1142/S0217732394002793
-/

namespace QOU.QPochhammer

open scoped BigOperators

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

end QOU.QPochhammer
