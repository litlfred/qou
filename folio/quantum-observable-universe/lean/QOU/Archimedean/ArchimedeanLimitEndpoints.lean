import QOU.Archimedean.ArchimedeanLimitNegative

/-!
# `ArchimedeanLimit` at the endpoints `x = 1` and `x = -1` (bean `qou-adgd`, issue #7942)

* **`x = 1`: the class is false as stated** (`not_archimedeanLimit_one`). The
  denominator `D_n(x; q) = ∏_{k<n} (1 - x qᵏ)` starts at `k = 0`, so at `x = 1` its
  first factor is `1 - q⁰ = 0`. Then `Φ_n(1; q) = 0⁻¹ = 0` in Lean, `log 0 = 0`, and the
  rescaled log-product is `0` for every `n ≥ 1`, while `LiTwo 1 ≥ 1`.
* **`x = 1` with shifted index `k ≥ 1` (Owner Default B1)**: keeping `denomPolyLocal`
  unchanged (`k = 0..n-1` for `x < 1`) and `not_archimedeanLimit_one` intact, the
  classical `(q; q)_n = ∏_{k=1}^n (1 - qᵏ)` partial product `partialProductShiftedOne`
  converges under Faddeev scaling to `LiTwo 1 = π²/6`
  (`archimedeanLimit_shifted_one`, `archimedeanLimit_shifted_one_pi_sq_div_six`).
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

/-! ## `x = 1` with shifted index `k ≥ 1`: classical `(q; q)_n` limit (Owner Default B1) -/

/-- Classical shifted-index `q`-Pochhammer denominator
    `(q; q)_n = ∏_{k=0}^{n-1} (1 - q^{k+1}) = ∏_{j=1}^n (1 - q^j)` at `x = 1`,
    omitting the vanishing `k = 0` factor `1 - q⁰ = 0` while leaving `denomPolyLocal`
    unchanged for `x < 1` (Owner Default B1). -/
def qPochhammerShiftedOne (q : ℝ) (n : ℕ) : ℝ :=
  ∏ k ∈ Finset.range n, (1 - q ^ (k + 1))

/-- Classical shifted-index partial product `(q; q)_n⁻¹` at `x = 1`. -/
noncomputable def partialProductShiftedOne (q : ℝ) (n : ℕ) : ℝ :=
  (qPochhammerShiftedOne q n)⁻¹

/-- `(q; q)_n` agrees with `denomPolyLocal q q n` (`x = q` shifts every exponent by `1`). -/
theorem qPochhammerShiftedOne_eq_denomPolyLocal (q : ℝ) (n : ℕ) :
    qPochhammerShiftedOne q n = denomPolyLocal q q n := by
  rw [qPochhammerShiftedOne, denomPolyLocal_eq_prod]
  refine Finset.prod_congr rfl (fun k _ => ?_)
  ring

/-- `partialProductShiftedOne q n` agrees with `partialProductLocal q q n`. -/
theorem partialProductShiftedOne_eq_partialProductLocal (q : ℝ) (n : ℕ) :
    partialProductShiftedOne q n = partialProductLocal q q n := by
  rw [partialProductShiftedOne, partialProductLocal, qPochhammerShiftedOne_eq_denomPolyLocal]

/-- Per-mode `m`-series summand of `(1 - q) log((q; q)_n⁻¹)`. -/
private noncomputable def shiftedOneTerm (q : ℝ) (n m : ℕ) : ℝ :=
  (1 - q) * (q ^ (m + 1) / ((m : ℝ) + 1) * ((q ^ ((m + 1) * n) - 1) / (q ^ (m + 1) - 1)))

private theorem shiftedOneTerm_eq_geom {q : ℝ} (hq0 : 0 < q) (hq1 : q < 1) (n m : ℕ) :
    shiftedOneTerm q n m =
      (q ^ (m + 1) / ∑ j ∈ Finset.range (m + 1), q ^ j) *
        (1 - q ^ ((m + 1) * n)) / ((m : ℝ) + 1) := by
  set S : ℝ := ∑ j ∈ Finset.range (m + 1), q ^ j
  have hS1 : 1 ≤ S := by
    have h0 : (0 : ℕ) ∈ Finset.range (m + 1) := Finset.mem_range.mpr (Nat.succ_pos m)
    have := Finset.single_le_sum (fun j _ => pow_nonneg hq0.le j) h0
    simpa using this
  have hSne : S ≠ 0 := by linarith
  have h1qne : 1 - q ≠ 0 := by linarith
  have hgm : q ^ (m + 1) - 1 = -((1 - q) * S) := by
    have := geom_sum_mul q (m + 1)
    linarith
  have hqmne : q ^ (m + 1) - 1 ≠ 0 := by rw [hgm]; exact neg_ne_zero.mpr (mul_ne_zero h1qne hSne)
  have hmne : ((m : ℝ) + 1) ≠ 0 := by positivity
  unfold shiftedOneTerm
  rw [hgm]
  field_simp
  ring

private theorem shiftedOneTerm_bounds {q : ℝ} (hq0 : 0 < q) (hq1 : q < 1) (n m : ℕ) :
    0 ≤ shiftedOneTerm q n m ∧
      shiftedOneTerm q n m ≤ 1 / ((m : ℝ) + 1) ^ 2 ∧
      1 / ((m : ℝ) + 1) ^ 2 - shiftedOneTerm q n m ≤ (1 - q) + q ^ n := by
  set S : ℝ := ∑ j ∈ Finset.range (m + 1), q ^ j
  have hm_pos : (0 : ℝ) < (m : ℝ) + 1 := by positivity
  have hS1 : 1 ≤ S := by
    have h0 : (0 : ℕ) ∈ Finset.range (m + 1) := Finset.mem_range.mpr (Nat.succ_pos m)
    have := Finset.single_le_sum (fun j _ => pow_nonneg hq0.le j) h0
    simpa using this
  have hSpos : 0 < S := by linarith
  have hS_lo : ((m : ℝ) + 1) * q ^ (m + 1) ≤ S := by
    calc ((m : ℝ) + 1) * q ^ (m + 1)
        = ∑ _j ∈ Finset.range (m + 1), q ^ (m + 1) := by
            simp [Finset.sum_const, Nat.cast_add, Nat.cast_one]
      _ ≤ ∑ j ∈ Finset.range (m + 1), q ^ j := by
            refine Finset.sum_le_sum (fun j hj => ?_)
            exact pow_le_pow_of_le_one hq0.le hq1.le
              (Nat.le_of_lt (Finset.mem_range.mp hj))
  have hS_hi : S ≤ (m : ℝ) + 1 := by
    calc ∑ j ∈ Finset.range (m + 1), q ^ j
        ≤ ∑ _j ∈ Finset.range (m + 1), (1 : ℝ) :=
          Finset.sum_le_sum (fun j _ => pow_le_one₀ hq0.le hq1.le)
      _ = (m : ℝ) + 1 := by simp
  set u : ℝ := q ^ (m + 1) / S
  set v : ℝ := 1 - q ^ ((m + 1) * n)
  have hu0 : 0 ≤ u := div_nonneg (pow_nonneg hq0.le _) hSpos.le
  have hu_hi : u ≤ 1 / ((m : ℝ) + 1) := by
    rw [div_le_div_iff₀ hSpos hm_pos, one_mul, mul_comm]
    exact hS_lo
  have hv0 : 0 ≤ v := by
    have : q ^ ((m + 1) * n) ≤ 1 := pow_le_one₀ hq0.le hq1.le
    linarith
  have hv_hi : v ≤ 1 := by
    have : 0 ≤ q ^ ((m + 1) * n) := pow_nonneg hq0.le _
    linarith
  rw [shiftedOneTerm_eq_geom hq0 hq1 n m]
  change 0 ≤ u * v / ((m : ℝ) + 1) ∧
    u * v / ((m : ℝ) + 1) ≤ 1 / ((m : ℝ) + 1) ^ 2 ∧
    1 / ((m : ℝ) + 1) ^ 2 - u * v / ((m : ℝ) + 1) ≤ (1 - q) + q ^ n
  refine ⟨div_nonneg (mul_nonneg hu0 hv0) hm_pos.le, ?_, ?_⟩
  · have huv : u * v ≤ 1 / ((m : ℝ) + 1) := by
      calc u * v ≤ (1 / ((m : ℝ) + 1)) * 1 :=
            mul_le_mul hu_hi hv_hi hv0 (by positivity)
        _ = 1 / ((m : ℝ) + 1) := mul_one _
    calc u * v / ((m : ℝ) + 1)
        ≤ (1 / ((m : ℝ) + 1)) / ((m : ℝ) + 1) :=
          div_le_div_of_nonneg_right huv hm_pos.le
      _ = 1 / ((m : ℝ) + 1) ^ 2 := by rw [div_div, sq]
  · -- Bernoulli lower bound on `q^{m+1}` and `q^{(m+1)n} ≤ q^n`
    have hbern : 1 - ((m : ℝ) + 1) * (1 - q) ≤ q ^ (m + 1) := by
      have h := one_add_mul_le_pow (a := -(1 - q)) (by linarith) (m + 1)
      have heq : 1 + -(1 - q) = q := by ring
      rw [heq] at h
      push_cast at h
      linarith
    have hu_lo : 1 / ((m : ℝ) + 1) - (1 - q) ≤ u := by
      have hstep1 : q ^ (m + 1) / ((m : ℝ) + 1) ≤ q ^ (m + 1) / S :=
        div_le_div_of_nonneg_left (pow_nonneg hq0.le _) hSpos hS_hi
      have hstep2 : 1 / ((m : ℝ) + 1) - (1 - q) ≤ q ^ (m + 1) / ((m : ℝ) + 1) := by
        rw [le_div_iff₀ hm_pos]
        have : (1 / ((m : ℝ) + 1) - (1 - q)) * ((m : ℝ) + 1) =
            1 - ((m : ℝ) + 1) * (1 - q) := by field_simp
        linarith
      exact le_trans hstep2 hstep1
    have hqmn : q ^ ((m + 1) * n) ≤ q ^ n :=
      pow_le_pow_of_le_one hq0.le hq1.le (Nat.le_mul_of_pos_left n (Nat.succ_pos m))
    have hv_lo : 1 - q ^ n ≤ v := by simp only [v]; linarith
    have hgap : 1 / ((m : ℝ) + 1) - u * v ≤ (1 - q) + q ^ n := by
      have h1 : 1 / ((m : ℝ) + 1) - u ≤ 1 - q := by linarith
      have h2 : u * (1 - v) ≤ q ^ n := by
        have h1v : 1 - v ≤ q ^ n := by linarith
        have hu1 : u ≤ 1 := le_trans hu_hi (by rw [div_le_one hm_pos]; linarith)
        calc u * (1 - v) ≤ 1 * q ^ n :=
              mul_le_mul hu1 h1v (by linarith) zero_le_one
          _ = q ^ n := one_mul _
      linarith
    have hdiv : 1 / ((m : ℝ) + 1) ^ 2 - u * v / ((m : ℝ) + 1) =
        (1 / ((m : ℝ) + 1) - u * v) / ((m : ℝ) + 1) := by
      field_simp
    rw [hdiv]
    calc (1 / ((m : ℝ) + 1) - u * v) / ((m : ℝ) + 1)
        ≤ ((1 - q) + q ^ n) / ((m : ℝ) + 1) :=
          div_le_div_of_nonneg_right hgap hm_pos.le
      _ ≤ (1 - q) + q ^ n :=
          div_le_self (by linarith [pow_nonneg hq0.le n]) (by linarith [Nat.cast_nonneg (α := ℝ) m])

private theorem summable_shiftedOneTerm {q : ℝ} (hq0 : 0 < q) (hq1 : q < 1) (n : ℕ) :
    Summable (shiftedOneTerm q n) := by
  have hone : Summable (fun m : ℕ => (1 : ℝ) / ((m : ℝ) + 1) ^ 2) := by
    simpa using summable_LiTwo_terms (x := 1) (by norm_num)
  refine Summable.of_nonneg_of_le (fun m => (shiftedOneTerm_bounds hq0 hq1 n m).1)
    (fun m => (shiftedOneTerm_bounds hq0 hq1 n m).2.1) hone

private theorem rescaled_log_shiftedOne_eq_tsum {q : ℝ} (hq0 : 0 < q) (hq1 : q < 1) (n : ℕ) :
    (1 - q) * Real.log (partialProductShiftedOne q n) = ∑' m : ℕ, shiftedOneTerm q n m := by
  rw [partialProductShiftedOne_eq_partialProductLocal]
  have hpos : ∀ k ∈ Finset.range n, (0 : ℝ) < 1 - q * q ^ k := by
    intro k _
    have : q * q ^ k < 1 := by
      rw [← pow_succ']
      exact pow_lt_one₀ hq0.le hq1 (Nat.succ_ne_zero k)
    linarith
  have hlt : ∀ k ∈ Finset.range n, |q * q ^ k| < 1 := by
    intro k _
    rw [← pow_succ', abs_of_pos (pow_pos hq0 (k + 1))]
    exact pow_lt_one₀ hq0.le hq1 (Nat.succ_ne_zero k)
  have hqpow : ∀ m : ℕ, q ^ (m + 1) ≠ 1 :=
    fun m => (pow_lt_one₀ hq0.le hq1 (Nat.succ_ne_zero m)).ne
  rw [partialProduct_log_eq_mseries q q n hpos hlt hqpow, ← tsum_mul_left]
  rfl

/-- **Shifted-index Faddeev limit at `x = 1` (Owner Default B1).**
    With the classical `(q; q)_n = ∏_{k=1}^n (1 - q^k)` partial product
    `partialProductShiftedOne q n = (q; q)_n⁻¹`, the Faddeev-rescaled log-product
    converges to `LiTwo 1` as `q → 1⁻` and `n(1 - q) → ∞`. -/
theorem archimedeanLimit_shifted_one :
    ∀ ε > (0 : ℝ),
      ∃ δ > (0 : ℝ), ∀ (q : ℝ) (n : ℕ),
        (1 - δ < q) ∧ (q < 1) ∧ (n : ℝ) * (1 - q) > δ⁻¹ →
          ‖(1 - q) * Real.log (partialProductShiftedOne q n) - LiTwo 1‖ < ε := by
  intro ε hε
  have hone : Summable (fun m : ℕ => (1 : ℝ) / ((m : ℝ) + 1) ^ 2) := by
    simpa using summable_LiTwo_terms (x := 1) (by norm_num)
  have hhas : HasSum (fun m : ℕ => (1 : ℝ) / ((m : ℝ) + 1) ^ 2) (LiTwo 1) := by
    rw [LiTwo_one_eq_tsum]
    exact hone.hasSum
  obtain ⟨M, hM⟩ := Metric.tendsto_atTop.mp hhas.tendsto_sum_nat (ε / 2) (by positivity)
  have hM' := hM M le_rfl
  rw [Real.dist_eq] at hM'
  set K : ℝ := (M : ℝ) + 1
  have hK1 : (1 : ℝ) ≤ K := by simp only [K]; linarith [Nat.cast_nonneg (α := ℝ) M]
  have hK0 : 0 < K := lt_of_lt_of_le one_pos hK1
  set D : ℝ := max 1 (Real.log (4 * K / ε))
  have hD1 : (1 : ℝ) ≤ D := le_max_left _ _
  have hD0 : 0 < D := lt_of_lt_of_le one_pos hD1
  set δ : ℝ := min (min (ε / (4 * K)) (1 / D)) (1 / 2)
  have hδ0 : 0 < δ := lt_min (lt_min (by positivity) (by positivity)) (by norm_num)
  refine ⟨δ, hδ0, ?_⟩
  rintro q n ⟨hq_lo, hq1, hn⟩
  have hδ_half : δ ≤ 1 / 2 := min_le_right _ _
  have hδ_ε : δ ≤ ε / (4 * K) := le_trans (min_le_left _ _) (min_le_left _ _)
  have hδ_D : δ ≤ 1 / D := le_trans (min_le_left _ _) (min_le_right _ _)
  have hq0 : 0 < q := by linarith
  have hsum_q := summable_shiftedOneTerm hq0 hq1 n
  -- Upper bound: `(1 - q) log((q; q)_n⁻¹) ≤ LiTwo 1`
  have h_le : (1 - q) * Real.log (partialProductShiftedOne q n) ≤ LiTwo 1 := by
    rw [rescaled_log_shiftedOne_eq_tsum hq0 hq1 n, LiTwo_one_eq_tsum]
    exact hsum_q.tsum_le_tsum (fun m => (shiftedOneTerm_bounds hq0 hq1 n m).2.1) hone
  -- Lower bound via partial sum at `M`
  have h_part_le : ∑ m ∈ Finset.range M, shiftedOneTerm q n m ≤
      (1 - q) * Real.log (partialProductShiftedOne q n) := by
    rw [rescaled_log_shiftedOne_eq_tsum hq0 hq1 n]
    exact hsum_q.sum_le_tsum (Finset.range M)
      (fun m _ => (shiftedOneTerm_bounds hq0 hq1 n m).1)
  have h_fin_gap :
      (∑ m ∈ Finset.range M, (1 : ℝ) / ((m : ℝ) + 1) ^ 2) -
        ∑ m ∈ Finset.range M, shiftedOneTerm q n m ≤
        (M : ℝ) * ((1 - q) + q ^ n) := by
    rw [← Finset.sum_sub_distrib]
    calc ∑ m ∈ Finset.range M, ((1 : ℝ) / ((m : ℝ) + 1) ^ 2 - shiftedOneTerm q n m)
        ≤ ∑ _m ∈ Finset.range M, ((1 - q) + q ^ n) :=
          Finset.sum_le_sum (fun m _ => (shiftedOneTerm_bounds hq0 hq1 n m).2.2)
      _ = (M : ℝ) * ((1 - q) + q ^ n) := by simp; ring
  -- Bound `K * (1 - q) < ε / 4` and `K * q^n < ε / 4`
  have hb1 : K * (1 - q) < ε / 4 := by
    have h1q : 1 - q < δ := by linarith
    calc K * (1 - q) < K * δ := mul_lt_mul_of_pos_left h1q hK0
      _ ≤ K * (ε / (4 * K)) := mul_le_mul_of_nonneg_left hδ_ε hK0.le
      _ = ε / 4 := by field_simp
  have hb2 : K * q ^ n < ε / 4 := by
    have hqn_le : q ^ n ≤ Real.exp (-((n : ℝ) * (1 - q))) := pow_le_exp_neg_mul hq0 n
    have hlt : Real.exp (-((n : ℝ) * (1 - q))) < Real.exp (-δ⁻¹) :=
      Real.exp_lt_exp.mpr (by linarith [hn])
    have hDδinv : D ≤ δ⁻¹ := by
      rw [← one_div, le_div_iff₀ hδ0, mul_comm]
      exact (le_div_iff₀ hD0).mp hδ_D
    have hexp_le : Real.exp (-δ⁻¹) ≤ ε / (4 * K) := by
      have hy : (0 : ℝ) < 4 * K / ε := by positivity
      have hstep : Real.exp (-δ⁻¹) ≤ Real.exp (-Real.log (4 * K / ε)) :=
        Real.exp_le_exp.mpr (by linarith [le_max_right (1 : ℝ) (Real.log (4 * K / ε))])
      have hval : Real.exp (-Real.log (4 * K / ε)) = ε / (4 * K) := by
        rw [Real.exp_neg, Real.exp_log hy, inv_div]
      rwa [hval] at hstep
    calc K * q ^ n ≤ K * Real.exp (-((n : ℝ) * (1 - q))) :=
          mul_le_mul_of_nonneg_left hqn_le hK0.le
      _ < K * Real.exp (-δ⁻¹) := mul_lt_mul_of_pos_left hlt hK0
      _ ≤ K * (ε / (4 * K)) := mul_le_mul_of_nonneg_left hexp_le hK0.le
      _ = ε / 4 := by field_simp
  have hMK : (M : ℝ) * ((1 - q) + q ^ n) ≤ K * ((1 - q) + q ^ n) := by
    apply mul_le_mul_of_nonneg_right _ (by linarith [pow_nonneg hq0.le n])
    simp only [K]; linarith
  have htail : LiTwo 1 - ε / 2 < ∑ m ∈ Finset.range M, (1 : ℝ) / ((m : ℝ) + 1) ^ 2 := by
    linarith [(abs_lt.mp hM').1]
  rw [Real.norm_eq_abs, abs_lt]
  refine ⟨?_, by linarith⟩
  linarith

/-- **Basel-constant form of the shifted-index `x = 1` Faddeev limit (`ζ(2) = π²/6`).** -/
theorem archimedeanLimit_shifted_one_pi_sq_div_six :
    ∀ ε > (0 : ℝ),
      ∃ δ > (0 : ℝ), ∀ (q : ℝ) (n : ℕ),
        (1 - δ < q) ∧ (q < 1) ∧ (n : ℝ) * (1 - q) > δ⁻¹ →
          ‖(1 - q) * Real.log (partialProductShiftedOne q n) - Real.pi ^ 2 / 6‖ < ε := by
  rw [← LiTwo_one]
  exact archimedeanLimit_shifted_one

end QOU.Archimedean
