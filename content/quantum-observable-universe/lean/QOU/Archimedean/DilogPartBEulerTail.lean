import QOU.Archimedean.DilogarithmArchimedeanLimit
import Mathlib.Algebra.Order.Ring.GeomSum

/-!
# Part B of `conj:dilogarithm-archimedean-limit` — the Euler-tail coefficient limit (V1)

The regularized negative-factor piece of Part B (`W-P2`) reduces, after the
substitution `p = 1/q` (`q→1⁺ ⟺ p→1⁻`) and `m = k − k*`, to the
**Euler-function / Dedekind-eta asymptotic**

`(1−p)·log ∏_{m≥1}(1−pᵐ) → −π²/6`   as `p → 1⁻`.

Via the Lambert series `log ∏(1−pᵐ) = −Σ_{j≥1}(1/j)·pʲ/(1−pʲ)` this is a
Tannery/dominated-convergence limit whose **termwise** input is the coefficient
limit proved here:

`(1−p)·pʲ/(1−pʲ) → 1/j`   as `p → 1⁻`,

after which `Σ_{j≥1} 1/j² = ζ(2) = π²/6` (`hasSum_zeta_two`) supplies the
constant. This is the cheap, load-bearing first brick (V1) of the Part-B
cusp-cancellation attack (`docs/coordination/dilog-part-b-cusp-attack.md`); the
Tannery exchange itself is V2.

The proof is elementary: `1 − pʲ = (1−p)·Σ_{i<j} pⁱ` (`geom_sum_mul`), so the
`(1−p)` cancels and the ratio is `pʲ / Σ_{i<j} pⁱ`, continuous at `p=1` with
value `1/j`.

-- Ref: [manuscript] conj:dilogarithm-archimedean-limit
-- Ref: [faddeev1994] https://doi.org/10.1142/S0217732394002793
-/

namespace QOU.QPochhammer

open Filter Topology
open scoped BigOperators

/-- **V1 — Euler-tail termwise coefficient limit.**  As `p → 1⁻`, the `j`-th
    Lambert coefficient `(1−p)·pʲ/(1−pʲ)` tends to `1/j`.  Since
    `1 − pʲ = (1−p)·Σ_{i<j} pⁱ`, the `(1−p)` cancels, leaving `pʲ/Σ_{i<j}pⁱ`,
    whose limit at `p=1` is `1/j` (numerator `→ 1`, denominator `→ j`).  This is
    the termwise input to the Tannery/DCT giving the negative-factor Euler tail
    `(1−p)·log ∏(1−pᵐ) → −π²/6` (Part B, `W-P2`). -/
theorem euler_tail_coeff_limit (j : ℕ) (hj : 1 ≤ j) :
    Tendsto (fun p : ℝ => (1 - p) * p ^ j / (1 - p ^ j)) (𝓝[<] 1)
      (𝓝 (1 / (j : ℝ))) := by
  -- On `p < 1` the function equals `pʲ / Σ_{i<j} pⁱ`.
  have hcong : (fun p : ℝ => (1 - p) * p ^ j / (1 - p ^ j))
      =ᶠ[𝓝[<] 1] (fun p : ℝ => p ^ j / ∑ i ∈ Finset.range j, p ^ i) := by
    filter_upwards [self_mem_nhdsWithin] with p hp
    have hp1 : p < 1 := hp
    have hsum : (1 : ℝ) - p ^ j = (1 - p) * ∑ i ∈ Finset.range j, p ^ i := by
      have h2 : (∑ i ∈ Finset.range j, p ^ i) * (p - 1) = p ^ j - 1 :=
        geom_sum_mul p j
      linear_combination h2
    rw [hsum, mul_div_mul_left _ _ (sub_pos.mpr hp1).ne']
  refine Tendsto.congr' hcong.symm ?_
  -- Numerator `pʲ → 1`.
  have hnum : Tendsto (fun p : ℝ => p ^ j) (𝓝[<] (1 : ℝ)) (𝓝 (1 : ℝ)) := by
    have h := (continuous_pow j).tendsto (1 : ℝ)
    simpa using h.mono_left nhdsWithin_le_nhds
  -- Denominator `Σ_{i<j} pⁱ → j`.
  have hden : Tendsto (fun p : ℝ => ∑ i ∈ Finset.range j, p ^ i) (𝓝[<] (1 : ℝ))
      (𝓝 (j : ℝ)) := by
    have hc : Continuous (fun p : ℝ => ∑ i ∈ Finset.range j, p ^ i) :=
      continuous_finset_sum _ (fun i _ => continuous_pow i)
    have h := hc.tendsto (1 : ℝ)
    simp only [one_pow, Finset.sum_const, Finset.card_range, nsmul_eq_mul,
      mul_one] at h
    exact h.mono_left nhdsWithin_le_nhds
  have hjne : (j : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr (by omega)
  simpa using hnum.div hden hjne

/-- **V1 — Euler-tail coefficient uniform bound.**  For `0 < p < 1` and `j ≥ 1`,
    `(1−p)·pʲ/(1−pʲ) ≤ 1/j`.  Together with `euler_tail_coeff_limit` (the termwise
    limit `→ 1/j`) this is the second Tannery/dominated-convergence input for
    `W-P2`: the coefficient times `1/j` is dominated by the summable `1/j²`.
    Proof: `(1−p)pʲ/(1−pʲ) = pʲ/Σ_{i<j}pⁱ`, and each of the `j` summands
    `pⁱ (i<j)` is `≥ pʲ`, so `Σ_{i<j}pⁱ ≥ j·pʲ`. -/
theorem euler_tail_coeff_le {j : ℕ} (hj : 1 ≤ j) {p : ℝ} (hp0 : 0 < p)
    (hp1 : p < 1) : (1 - p) * p ^ j / (1 - p ^ j) ≤ 1 / (j : ℝ) := by
  have hspos : 0 < ∑ i ∈ Finset.range j, p ^ i :=
    Finset.sum_pos (fun i _ => pow_pos hp0 i)
      (Finset.nonempty_range_iff.mpr (by omega))
  have hsum : (1 : ℝ) - p ^ j = (1 - p) * ∑ i ∈ Finset.range j, p ^ i := by
    have h2 : (∑ i ∈ Finset.range j, p ^ i) * (p - 1) = p ^ j - 1 :=
      geom_sum_mul p j
    linear_combination h2
  have heq : (1 - p) * p ^ j / (1 - p ^ j) = p ^ j / ∑ i ∈ Finset.range j, p ^ i := by
    rw [hsum, mul_div_mul_left _ _ (sub_pos.mpr hp1).ne']
  have hjpos : (0 : ℝ) < (j : ℝ) := by exact_mod_cast (by omega : (0 : ℕ) < j)
  -- `Σ_{i<j} pⁱ ≥ j·pʲ` since each of the `j` summands is `≥ pʲ`.
  have hbound : (j : ℝ) * p ^ j ≤ ∑ i ∈ Finset.range j, p ^ i := by
    have hterm : ∀ i ∈ Finset.range j, p ^ j ≤ p ^ i := by
      intro i hi
      exact pow_le_pow_of_le_one hp0.le hp1.le (Finset.mem_range.mp hi).le
    have hle := Finset.card_nsmul_le_sum (Finset.range j) (fun i => p ^ i) (p ^ j) hterm
    rwa [Finset.card_range, nsmul_eq_mul] at hle
  rw [heq, div_le_iff₀ hspos]
  calc p ^ j = 1 / (j : ℝ) * ((j : ℝ) * p ^ j) := by field_simp
    _ ≤ 1 / (j : ℝ) * ∑ i ∈ Finset.range j, p ^ i :=
        mul_le_mul_of_nonneg_left hbound (by positivity)

end QOU.QPochhammer
