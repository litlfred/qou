import QOU.Archimedean.DilogPartARiemannSum

/-!
# Where `ArchimedeanLimit x` can hold (issue #7942)

`ArchimedeanLimit x` already has instances at `x = 0`
(`archimedeanLimit_zero`) and for every `x ∈ (0,1)` (`archimedeanLimit_Ioo`,
`DilogPartAConvergence.lean`).

This file shows the class is **false for `x < -1`**.  The reason is the
target, not the limit: `LiTwo x` is a `tsum`, and for `|x| > 1` the series
`Σ xᵏ⁺¹/(k+1)²` is not summable, so Mathlib's convention makes `LiTwo x = 0`.
The rescaled log-product does not tend to `0` there: for `x < -1` every factor
`1 - x qᵏ` exceeds `1`, and the first `m/2` factors (with `q = 1 - 1/m`) each
exceed `3/2`, so `(1-q) · (-log Φ_n) ≥ ½ log(3/2)`.

The corrected statement for `|x| > 1` must aim at the analytically continued
real part, `Re Li₂(x)`, not at the `tsum`; that needs the complex dilogarithm
(PR #7913 has the reflection bricks).  For the α_EM chain only `x ∈ (0,1)`
is used.

-- Ref: [leitner2026] conj:dilogarithm-archimedean-limit
-/

namespace QOU.Archimedean

open QOU.QPochhammer

/-- For `|x| > 1` the dilogarithm series is not summable, so `LiTwo x = 0`. -/
theorem LiTwo_eq_zero_of_one_lt_abs {x : ℝ} (hx : 1 < |x|) : LiTwo x = 0 := by
  unfold LiTwo
  apply tsum_eq_zero_of_not_summable
  intro hs
  have ht := hs.tendsto_atTop_zero
  -- `(k+1)² / |x|^(k+1) → 0`, so eventually `|x|^(k+1) > (k+1)²`.
  have hlim : Filter.Tendsto (fun k : ℕ => ((k : ℝ) ^ 2) / |x| ^ k)
      Filter.atTop (nhds 0) :=
    tendsto_pow_const_div_const_pow_of_one_lt 2 hx
  have hlim' : Filter.Tendsto (fun k : ℕ => (((k + 1 : ℕ) : ℝ) ^ 2) / |x| ^ (k + 1))
      Filter.atTop (nhds 0) := hlim.comp (Filter.tendsto_add_atTop_nat 1)
  have e1 := (hlim'.eventually (gt_mem_nhds (by norm_num : (0 : ℝ) < 1)))
  have e2 := (ht.norm.eventually (gt_mem_nhds (by rw [norm_zero]; norm_num : ‖(0 : ℝ)‖ < 1)))
  obtain ⟨k, hk1, hk2⟩ := (e1.and e2).exists
  have hxk : 0 < |x| ^ (k + 1) := pow_pos (lt_trans one_pos hx) _
  have hk0 : (0 : ℝ) < ((k : ℝ) + 1) ^ 2 := by positivity
  push_cast at hk1
  rw [div_lt_one hxk] at hk1
  rw [norm_div, norm_pow, Real.norm_eq_abs, Real.norm_eq_abs, abs_of_pos hk0,
    div_lt_one hk0] at hk2
  linarith

/-- For `x < 0` (all factors `> 1`), `log Φ_n = -Σ log(1 - x qᵏ)`. -/
theorem log_partialProduct_eq_neg_sum_of_neg {q x : ℝ} (hx : x < 0) (hq0 : 0 < q)
    (n : ℕ) :
    Real.log (partialProductLocal q x n)
      = -∑ k ∈ Finset.range n, Real.log (1 - x * q ^ k) := by
  have hfac : ∀ k ∈ Finset.range n, (1 - x * q ^ k) ≠ 0 := by
    intro k _
    have : x * q ^ k < 0 := mul_neg_of_neg_of_pos hx (pow_pos hq0 k)
    exact ne_of_gt (by linarith)
  unfold partialProductLocal
  rw [Real.log_inv, denomPolyLocal_eq_prod, Real.log_prod _ _ hfac]

/-- **`ArchimedeanLimit x` is false for every `x < -1`.** -/
theorem not_archimedeanLimit_of_lt_neg_one {x : ℝ} (hx : x < -1) :
    ¬ ArchimedeanLimit x := by
  intro h
  have hL : LiTwo x = 0 :=
    LiTwo_eq_zero_of_one_lt_abs (by rw [abs_of_neg (by linarith)]; linarith)
  set ε : ℝ := Real.log (3 / 2) / 2 with hε
  have hε0 : 0 < ε := by
    have : 0 < Real.log (3 / 2) := Real.log_pos (by norm_num)
    positivity
  obtain ⟨δ, hδ, hδP⟩ := h.faddeev_limit ε hε0
  -- choose `j > 1/δ`, `m = 2j`, `q = 1 - 1/m`, `n = m j`
  obtain ⟨j, hj⟩ := exists_nat_gt δ⁻¹
  have hj0 : (0 : ℝ) < j := lt_trans (inv_pos.mpr hδ) hj
  have hj1 : 1 ≤ j := Nat.one_le_iff_ne_zero.mpr (by rintro rfl; simp at hj0)
  set m : ℕ := 2 * j with hm
  have hmR : (m : ℝ) = 2 * j := by rw [hm]; push_cast; ring
  have hm0 : (0 : ℝ) < m := by rw [hmR]; positivity
  set q : ℝ := 1 - 1 / (m : ℝ) with hq
  set n : ℕ := m * j with hn
  have hnR : (n : ℝ) = m * j := by rw [hn]; push_cast; ring
  have h1q : 1 - q = 1 / (m : ℝ) := by rw [hq]; ring
  have hq0 : 0 < q := by
    rw [hq, hmR]
    have : (1 : ℝ) ≤ j := by exact_mod_cast hj1
    rw [sub_pos, div_lt_one (by positivity)]; linarith
  have hq1 : q < 1 := by rw [hq]; have := one_div_pos.mpr hm0; linarith
  have hcond : (1 - δ < q) ∧ (q < 1) ∧ (n : ℝ) * (1 - q) > δ⁻¹ := by
    refine ⟨?_, hq1, ?_⟩
    · rw [hq, hmR]
      have hjinv : (j : ℝ)⁻¹ < δ := by
        rw [inv_lt_comm₀ hj0 hδ]; exact hj
      have : 1 / (2 * (j : ℝ)) < δ := by
        rw [one_div, mul_inv]
        have : (2 : ℝ)⁻¹ * (j : ℝ)⁻¹ ≤ (j : ℝ)⁻¹ := by
          have := inv_pos.mpr hj0; nlinarith
        linarith
      linarith
    · have e : (m : ℝ) * j * (1 / (m : ℝ)) = j := by field_simp
      rw [h1q, hnR, e]; exact hj
  have hbd := hδP q n hcond
  rw [hL, sub_zero, log_partialProduct_eq_neg_sum_of_neg (by linarith) hq0] at hbd
  -- lower bound: each term is ≥ 0, and the first `j` terms are ≥ log(3/2)
  have hterm_nonneg : ∀ k, 0 ≤ Real.log (1 - x * q ^ k) := by
    intro k
    apply Real.log_nonneg
    have : x * q ^ k ≤ 0 := mul_nonpos_of_nonpos_of_nonneg (by linarith) (pow_pos hq0 k).le
    linarith
  have hterm_big : ∀ k < j, Real.log (3 / 2) ≤ Real.log (1 - x * q ^ k) := by
    intro k hk
    have hbern : 1 + (k : ℝ) * (-(1 / (m : ℝ))) ≤ q ^ k := by
      have := one_add_mul_le_pow (a := -(1 / (m : ℝ)))
        (by have : 1 / (m : ℝ) ≤ 1 := by
              rw [div_le_one hm0, hmR]
              have : (1 : ℝ) ≤ j := by exact_mod_cast hj1
              linarith
            linarith) k
      rw [hq]; simpa [sub_eq_add_neg] using this
    have hk' : (k : ℝ) + 1 ≤ j := by exact_mod_cast hk
    have hhalf : (1 : ℝ) / 2 ≤ q ^ k := by
      refine le_trans ?_ hbern
      rw [hmR]
      have h2j : (0 : ℝ) < 2 * j := by positivity
      have hkj : (k : ℝ) / (2 * j) ≤ 1 / 2 := by
        rw [div_le_iff₀ h2j]; nlinarith
      have : (k : ℝ) * (-(1 / (2 * (j : ℝ)))) = -((k : ℝ) / (2 * j)) := by ring
      rw [this]; linarith
    apply Real.log_le_log (by norm_num)
    nlinarith
  have hjn : j ≤ n := by
    rw [hn, hm]
    have h2 : j ≤ 2 * j := by omega
    calc j ≤ 2 * j := h2
      _ ≤ 2 * j * j := Nat.le_mul_of_pos_right _ hj1
  have hsub : Finset.range j ⊆ Finset.range n := by
    intro k hk
    simp only [Finset.mem_range] at hk ⊢
    omega
  have hsum : (j : ℝ) * Real.log (3 / 2)
      ≤ ∑ k ∈ Finset.range n, Real.log (1 - x * q ^ k) := by
    calc (j : ℝ) * Real.log (3 / 2)
        = ∑ _k ∈ Finset.range j, Real.log (3 / 2) := by simp
      _ ≤ ∑ k ∈ Finset.range j, Real.log (1 - x * q ^ k) :=
          Finset.sum_le_sum (fun k hk => hterm_big k (Finset.mem_range.mp hk))
      _ ≤ ∑ k ∈ Finset.range n, Real.log (1 - x * q ^ k) :=
          Finset.sum_le_sum_of_subset_of_nonneg hsub (fun k _ _ => hterm_nonneg k)
  have hval : ε ≤ (1 - q) * ∑ k ∈ Finset.range n, Real.log (1 - x * q ^ k) := by
    rw [h1q, hε]
    have hpos : 0 < Real.log (3 / 2) := Real.log_pos (by norm_num)
    rw [hmR]
    rw [div_mul_eq_mul_div, one_mul, le_div_iff₀ (by positivity)]
    nlinarith
  rw [Real.norm_eq_abs, mul_neg, abs_neg,
    abs_of_nonneg (by linarith : (0 : ℝ) ≤ (1 - q) * ∑ k ∈ Finset.range n,
      Real.log (1 - x * q ^ k))] at hbd
  linarith

end QOU.Archimedean
