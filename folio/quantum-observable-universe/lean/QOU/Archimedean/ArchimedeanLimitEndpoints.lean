import QOU.Archimedean.ArchimedeanLimitNegative

/-!
# `ArchimedeanLimit` at the endpoints `x = 1` and `x = -1` (bean `qou-adgd`, issue #7942)

* **`x = 1`: the class is false as stated** (`not_archimedeanLimit_one`). The
  denominator `D_n(x; q) = ∏_{k<n} (1 - x qᵏ)` starts at `k = 0`, so at `x = 1` its
  first factor is `1 - q⁰ = 0`. Then `Φ_n(1; q) = 0⁻¹ = 0` in Lean, `log 0 = 0`, and the
  rescaled log-product is `0` for every `n ≥ 1`, while `LiTwo 1 ≥ 1`. This is a defect
  of the indexing at the single point `x = 1`, not of the limit: the classical
  statement for `x = 1` uses `(q; q)_n = ∏_{k≥1}`. A restatement is an owner decision.
* **`x = -1`: the limit holds** (`archimedeanLimit_neg_one`). No duplication is needed.
  The rescaled log-product is uniformly Lipschitz in the left endpoint: for
  `-1 < y < 0`,
  `0 ≤ (1-q) log D_n(-1) - (1-q) log D_n(y) ≤ (1+y)(1 - qⁿ) ≤ 1 + y`
  for every `q ∈ [0,1)` and every `n`. Together with the limit at `y`
  (`archimedeanLimit_neg_Ioo`) and the continuity of `LiTwo` on `[-1,1]` (Weierstrass
  M-test), a three-ε argument gives the limit at `-1`.

-- Ref: [leitner2026] conj:dilogarithm-archimedean-limit
-/

namespace QOU.Archimedean

open QOU.QPochhammer

/-! ## `x = 1`: the stated class fails -/

theorem denomPolyLocal_one_succ (q : ℝ) (m : ℕ) : denomPolyLocal q 1 (m + 1) = 0 := by
  induction m with
  | zero => simp [denomPolyLocal]
  | succ m ih => rw [denomPolyLocal, ih, mul_zero]

theorem one_le_LiTwo_one : 1 ≤ LiTwo 1 := by
  have hs := summable_LiTwo_terms (x := 1) (by norm_num)
  have h := hs.le_tsum 0 (fun j _ => by positivity)
  simpa [LiTwo] using h

/-- `ArchimedeanLimit 1` is false as stated: the `k = 0` factor of the denominator
    vanishes at `x = 1`. -/
theorem not_archimedeanLimit_one : ¬ ArchimedeanLimit 1 := by
  intro h
  obtain ⟨δ, hδ, hlim⟩ := h.faddeev_limit (1 / 2) (by norm_num)
  set d := min δ 1 with hd
  have hd0 : 0 < d := lt_min hδ one_pos
  have hdδ : d ≤ δ := min_le_left _ _
  obtain ⟨m, hm⟩ := exists_nat_gt (2 / (δ * d))
  set q := 1 - d / 2
  have hq1 : 1 - δ < q := by simp only [q]; linarith
  have hq2 : q < 1 := by simp only [q]; linarith
  have hn : ((m + 1 : ℕ) : ℝ) * (1 - q) > δ⁻¹ := by
    have h1q : 1 - q = d / 2 := by simp only [q]; ring
    rw [h1q]
    have hm' : (2 / (δ * d)) < ((m + 1 : ℕ) : ℝ) := by push_cast; linarith
    have := (div_lt_iff₀ (by positivity : 0 < δ * d)).1 hm'
    rw [gt_iff_lt, inv_lt_iff_one_lt_mul₀ hδ]
    nlinarith
  have key := hlim q (m + 1) ⟨hq1, hq2, hn⟩
  rw [partialProductLocal, denomPolyLocal_one_succ, inv_zero, Real.log_zero, mul_zero,
    zero_sub, norm_neg, Real.norm_eq_abs] at key
  have := one_le_LiTwo_one
  rw [abs_of_pos (by linarith)] at key
  linarith

/-! ## `x = -1`: the limit holds -/

theorem denomPolyLocal_pos_of_nonpos {q x : ℝ} (hq0 : 0 ≤ q) (hx : x ≤ 0) (n : ℕ) :
    0 < denomPolyLocal q x n := by
  induction n with
  | zero => simp [denomPolyLocal]
  | succ n ih =>
    rw [denomPolyLocal]
    have : 0 ≤ -x * q ^ n := mul_nonneg (by linarith) (pow_nonneg hq0 n)
    exact mul_pos (by linarith) ih

/-- The gap between the log-denominators at `-1` and at `y ∈ (-1, 0)`. -/
theorem log_denom_gap {q y : ℝ} (hq0 : 0 ≤ q) (hy0 : y < 0) (hy1 : -1 < y) (n : ℕ) :
    0 ≤ Real.log (denomPolyLocal q (-1) n) - Real.log (denomPolyLocal q y n) ∧
      Real.log (denomPolyLocal q (-1) n) - Real.log (denomPolyLocal q y n) ≤
        (1 + y) * ∑ k ∈ Finset.range n, q ^ k := by
  induction n with
  | zero => simp [denomPolyLocal]
  | succ n ih =>
    have hA := denomPolyLocal_pos_of_nonpos hq0 (by norm_num : (-1 : ℝ) ≤ 0) n
    have hB := denomPolyLocal_pos_of_nonpos hq0 hy0.le n
    have hqn : 0 ≤ q ^ n := pow_nonneg hq0 n
    set a := 1 - (-1) * q ^ n
    set b := 1 - y * q ^ n
    have hb1 : 1 ≤ b := by simp only [b]; nlinarith
    have hb0 : 0 < b := by linarith
    have hab : b ≤ a := by simp only [a, b]; nlinarith
    have ha0 : 0 < a := by linarith
    have hamb : a - b = (1 + y) * q ^ n := by simp only [a, b]; ring
    rw [denomPolyLocal, denomPolyLocal, Real.log_mul ha0.ne' hA.ne',
      Real.log_mul hb0.ne' hB.ne', Finset.sum_range_succ]
    have hlog0 : Real.log b ≤ Real.log a := Real.log_le_log hb0 hab
    have hlog1 : Real.log a - Real.log b ≤ (1 + y) * q ^ n := by
      rw [← Real.log_div ha0.ne' hb0.ne']
      have h1 := Real.log_le_sub_one_of_pos (div_pos ha0 hb0)
      have h2 : a / b - 1 = (a - b) / b := by field_simp
      have h3 : (a - b) / b ≤ a - b :=
        div_le_self (by linarith) hb1
      linarith
    obtain ⟨ih0, ih1⟩ := ih
    constructor
    · linarith
    · nlinarith

/-- The rescaled log-products at `-1` and at `y ∈ (-1, 0)` differ by at most `1 + y`,
    uniformly in `q ∈ [0, 1)` and `n`. -/
theorem rescaled_log_gap {q y : ℝ} (hq0 : 0 ≤ q) (hq1 : q < 1) (hy0 : y < 0) (hy1 : -1 < y)
    (n : ℕ) :
    |(1 - q) * Real.log (partialProductLocal q (-1) n) -
        (1 - q) * Real.log (partialProductLocal q y n)| ≤ 1 + y := by
  obtain ⟨h0, h1⟩ := log_denom_gap hq0 hy0 hy1 n
  have hgeo : (∑ k ∈ Finset.range n, q ^ k) * (1 - q) = 1 - q ^ n := by
    have := geom_sum_mul q n
    linarith
  have hqn : 0 ≤ q ^ n := pow_nonneg hq0 n
  rw [partialProductLocal, partialProductLocal, Real.log_inv, Real.log_inv]
  have h1q : 0 ≤ 1 - q := by linarith
  set g := Real.log (denomPolyLocal q (-1) n) - Real.log (denomPolyLocal q y n)
  have he : (1 - q) * -Real.log (denomPolyLocal q (-1) n) -
      (1 - q) * -Real.log (denomPolyLocal q y n) = -((1 - q) * g) := by
    simp only [g]; ring
  rw [he, abs_neg, abs_of_nonneg (mul_nonneg h1q h0)]
  calc (1 - q) * g ≤ (1 - q) * ((1 + y) * ∑ k ∈ Finset.range n, q ^ k) :=
        mul_le_mul_of_nonneg_left h1 h1q
    _ = (1 + y) * (1 - q ^ n) := by rw [← hgeo]; ring
    _ ≤ 1 + y := by nlinarith

/-- `LiTwo` is continuous on `[-1, 1]` (Weierstrass M-test). -/
theorem continuousOn_LiTwo : ContinuousOn LiTwo (Set.Icc (-1) 1) := by
  have hone := summable_LiTwo_terms (x := 1) (by norm_num)
  unfold LiTwo
  refine continuousOn_tsum (fun k => (continuous_pow (k + 1)).div_const _ |>.continuousOn)
    (u := fun k : ℕ => (1 : ℝ) ^ (k + 1) / ((k : ℝ) + 1) ^ 2) hone ?_
  intro k x hx
  rw [Real.norm_eq_abs, abs_div, abs_pow, abs_of_pos (by positivity : (0 : ℝ) < ((k : ℝ) + 1) ^ 2)]
  apply div_le_div_of_nonneg_right _ (by positivity)
  exact pow_le_pow_left₀ (abs_nonneg x) (abs_le.2 ⟨by linarith [hx.1], hx.2⟩) _

/-- **`ArchimedeanLimit (-1)`.** -/
theorem archimedeanLimit_neg_one : ArchimedeanLimit (-1) := by
  refine ⟨fun ε hε => ?_⟩
  have hc : ContinuousWithinAt LiTwo (Set.Icc (-1) 1) (-1) :=
    continuousOn_LiTwo (-1) ⟨le_refl _, by norm_num⟩
  obtain ⟨η, hη, hcont⟩ := Metric.continuousWithinAt_iff.1 hc (ε / 3) (by positivity)
  set t := min (min (η / 2) (ε / 6)) (1 / 2) with ht
  have ht0 : 0 < t := lt_min (lt_min (by positivity) (by positivity)) (by norm_num)
  have htη : t ≤ η / 2 := le_trans (min_le_left _ _) (min_le_left _ _)
  have htε : t ≤ ε / 6 := le_trans (min_le_left _ _) (min_le_right _ _)
  have ht1 : t ≤ 1 / 2 := min_le_right _ _
  set y := -1 + t
  have hy0 : y < 0 := by simp only [y]; linarith
  have hy1 : -1 < y := by simp only [y]; linarith
  have hLi : |LiTwo y - LiTwo (-1)| < ε / 3 := by
    have hmem : y ∈ Set.Icc (-1 : ℝ) 1 := ⟨hy1.le, by linarith⟩
    have hd : dist y (-1) < η := by
      rw [Real.dist_eq]; simp only [y]; rw [abs_of_pos (by linarith)]; linarith
    simpa [Real.dist_eq] using hcont hmem hd
  obtain ⟨δ, hδ, hlim⟩ := (archimedeanLimit_neg_Ioo hy0 hy1).faddeev_limit (ε / 3)
    (by positivity)
  refine ⟨min δ (1 / 2), lt_min hδ (by norm_num), ?_⟩
  rintro q n ⟨hq1, hq2, hn⟩
  have hδ' : min δ (1 / 2) ≤ δ := min_le_left _ _
  have hq0 : 0 ≤ q := by linarith [min_le_right δ (1 / 2)]
  have hnδ : (n : ℝ) * (1 - q) > δ⁻¹ :=
    lt_of_le_of_lt (inv_anti₀ (lt_min hδ (by norm_num)) hδ') hn
  have hy := hlim q n ⟨by linarith, hq2, hnδ⟩
  rw [Real.norm_eq_abs] at hy ⊢
  have hg := rescaled_log_gap hq0 hq2 hy0 hy1 n
  have h1y : 1 + y ≤ ε / 6 := by simp only [y]; linarith
  calc |(1 - q) * Real.log (partialProductLocal q (-1) n) - LiTwo (-1)|
      ≤ |(1 - q) * Real.log (partialProductLocal q (-1) n) -
            (1 - q) * Real.log (partialProductLocal q y n)| +
          |(1 - q) * Real.log (partialProductLocal q y n) - LiTwo y| +
          |LiTwo y - LiTwo (-1)| := by
        have := abs_sub_le ((1 - q) * Real.log (partialProductLocal q (-1) n))
          ((1 - q) * Real.log (partialProductLocal q y n)) (LiTwo (-1))
        have := abs_sub_le ((1 - q) * Real.log (partialProductLocal q y n)) (LiTwo y)
          (LiTwo (-1))
        linarith
    _ < ε := by linarith

end QOU.Archimedean
