import QOU.KZ.KZPentagon

/-!
# Quantitative bound `‖Φ_KZ(A, B) − 1‖ ≤ F(a)` for small residues

Stage S4 of bean `qou-zoyv` (small-`ℏ` route to the duals of `D_ℏ`). For residues with
`‖A‖, ‖B‖ ≤ a`, `a < 1/4`:

* `norm_coeff_le_small`: the normalised formal solution of `kzM0 A B` has
  `‖H_{k+1}‖ ≤ β (1 + β)^k`, `β = a/(1 − 2a)`;
* `norm_series_half_sub_one`: `‖H(1/2) − 1‖ ≤ β/(1 − β) = a/(1 − 3a)`;
* `norm_Φ_sub_one_le`: `‖Φ(A, B) − 1‖ ≤ (1 + δₑ)² (1 + δ)(1 + δ') − 1`, with
  `δₑ = e^{a log 2} − 1`, `δ = a/(1 − 3a)`, `δ' = a/(1 − 4a)`. Here
  `Φ = (1/2)^{−B} H₁(1/2)^{−1} H₀(1/2) (1/2)^{A}`.

Base: complete normed `ℂ`-algebra with `‖1‖ = 1`. Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S4)
-/

namespace QOU.KZ.SmallHbar

open Finset QOU.KZ.FuchsianFormal QOU.KZ.FuchsianAnalytic QOU.KZ.AssociatorKZ

section Banach

variable {R : Type*} [NormedRing R] [NormedAlgebra ℝ R] [CompleteSpace R]

/-- `‖e^x − 1‖ ≤ e^{‖x‖} − 1`. -/
theorem norm_exp_sub_one_le (x : R) : ‖NormedSpace.exp ℝ x - 1‖ ≤ Real.exp ‖x‖ - 1 := by
  have hs := NormedSpace.expSeries_summable' (𝕂 := ℝ) x
  have hr := Real.summable_pow_div_factorial ‖x‖
  have e1 : NormedSpace.exp ℝ x = ∑' n : ℕ, ((n.factorial : ℝ))⁻¹ • x ^ n := by
    rw [NormedSpace.exp_eq_tsum]
  have e2 : Real.exp ‖x‖ = ∑' n : ℕ, ((n.factorial : ℝ))⁻¹ • ‖x‖ ^ n := by
    rw [Real.exp_eq_exp_ℝ, NormedSpace.exp_eq_tsum]
  rw [e1, e2, hs.tsum_eq_zero_add,
    (NormedSpace.expSeries_summable' (𝕂 := ℝ) ‖x‖).tsum_eq_zero_add]
  simp only [pow_zero, Nat.factorial_zero, Nat.cast_one, inv_one, one_smul, add_sub_cancel_left]
  have hs1 : Summable fun n : ℕ => ‖((n + 1).factorial : ℝ)⁻¹ • x ^ (n + 1)‖ :=
    Summable.of_nonneg_of_le (fun _ => norm_nonneg _) (fun n => by
      rw [norm_smul, Real.norm_eq_abs, abs_inv, Nat.abs_cast]
      calc ((n + 1).factorial : ℝ)⁻¹ * ‖x ^ (n + 1)‖ ≤ ((n + 1).factorial : ℝ)⁻¹ * ‖x‖ ^ (n + 1) :=
            by gcongr; exact norm_pow_le' x n.succ_pos
        _ = ‖x‖ ^ (n + 1) / (n + 1).factorial := by rw [div_eq_inv_mul])
      ((summable_nat_add_iff 1).2 hr)
  refine (norm_tsum_le_tsum_norm hs1).trans (hs1.tsum_le_tsum (fun n => ?_)
    ((NormedSpace.expSeries_summable' (𝕂 := ℝ) ‖x‖).comp_injective (add_left_injective 1)))
  simp only [smul_eq_mul]
  rw [norm_smul, Real.norm_eq_abs, abs_inv, Nat.abs_cast]
  gcongr
  exact norm_pow_le' x n.succ_pos

omit [NormedAlgebra ℝ R] in
/-- **Inverse near `1`.** If `‖u − 1‖ < 1` then `u` is a unit and
`‖u⁻¹ − 1‖ ≤ ‖u − 1‖ / (1 − ‖u − 1‖)`. -/
theorem norm_inverse_sub_one_le (u : R) (h : ‖u - 1‖ < 1) :
    IsUnit u ∧ ‖Ring.inverse u - 1‖ ≤ ‖u - 1‖ / (1 - ‖u - 1‖) := by
  set t := 1 - u with ht
  have htn : ‖t‖ < 1 := by rw [ht, norm_sub_rev]; exact h
  have hu : u = 1 - t := by rw [ht]; abel
  set s := ∑' i : ℕ, t ^ i
  have h1 : s * u = 1 := by rw [hu]; exact geom_series_mul_neg t htn
  have h2 : u * s = 1 := by rw [hu]; exact mul_neg_geom_series t htn
  have hunit : IsUnit u := ⟨⟨u, s, h2, h1⟩, rfl⟩
  refine ⟨hunit, ?_⟩
  have hinv : Ring.inverse u = s := Ring.inverse_unit ⟨u, s, h2, h1⟩
  have hsum := summable_geometric_of_norm_lt_one htn
  have hsn : Summable fun i : ℕ => ‖t‖ ^ (i + 1) :=
    (summable_nat_add_iff 1).2 (summable_geometric_of_lt_one (norm_nonneg _) htn)
  rw [hinv, show s = ∑' i : ℕ, t ^ i from rfl, hsum.tsum_eq_zero_add, pow_zero,
    add_sub_cancel_left, show ‖u - 1‖ = ‖t‖ by rw [ht, norm_sub_rev]]
  calc ‖∑' i : ℕ, t ^ (i + 1)‖ ≤ ∑' i : ℕ, ‖t‖ ^ (i + 1) :=
        (norm_tsum_le_tsum_norm (Summable.of_nonneg_of_le (fun _ => norm_nonneg _)
          (fun i => norm_pow_le' t i.succ_pos) hsn)).trans
          (Summable.tsum_le_tsum (fun i => norm_pow_le' t i.succ_pos)
            (Summable.of_nonneg_of_le (fun _ => norm_nonneg _)
              (fun i => norm_pow_le' t i.succ_pos) hsn) hsn)
    _ = ‖t‖ / (1 - ‖t‖) := by
        simp only [pow_succ, tsum_mul_right, tsum_geometric_of_lt_one (norm_nonneg _) htn]
        rw [div_eq_inv_mul]

omit [NormedAlgebra ℝ R] [CompleteSpace R] in
/-- `‖xy − 1‖ ≤ ‖x − 1‖ + ‖y − 1‖ + ‖x − 1‖‖y − 1‖`. -/
theorem norm_mul_sub_one_le (x y : R) :
    ‖x * y - 1‖ ≤ (1 + ‖x - 1‖) * (1 + ‖y - 1‖) - 1 := by
  have e : x * y - 1 = (x - 1) * (y - 1) + (x - 1) + (y - 1) := by noncomm_ring
  rw [e]
  calc ‖(x - 1) * (y - 1) + (x - 1) + (y - 1)‖
      ≤ ‖x - 1‖ * ‖y - 1‖ + ‖x - 1‖ + ‖y - 1‖ := by
        refine (norm_add_le _ _).trans (add_le_add_right ((norm_add_le _ _).trans
          (add_le_add_right (norm_mul_le _ _) _)) _)
    _ = _ := by ring

omit [CompleteSpace R] in
/-- One step of the coefficient estimate: for `k ≥ 1`,
`k (1 − 2a) ‖H_k‖ ≤ a ∑_{j<k} ‖H_j‖`. -/
theorem coeff_step (A B : R) (H : ℕ → R) (h0 : H 0 = 1) (hH : IsFormalGauge (kzM0 A B) H)
    {a : ℝ} (hA : ‖A‖ ≤ a) (hB : ‖B‖ ≤ a) (k : ℕ) (hk : 0 < k) :
    (k : ℝ) * (1 - 2 * a) * ‖H k‖ ≤ a * ∑ j ∈ range k, ‖H j‖ := by
  have hrec := ((isFormalGauge_iff _ H h0).1 hH) k hk
  have ha : 0 ≤ a := (norm_nonneg _).trans hA
  have hk1 : (1 : ℝ) ≤ k := by exact_mod_cast hk
  -- lower bound on the indicial operator
  have h1 : ‖(k : R) * H k‖ = k * ‖H k‖ := by
    rw [FuchsianConvergence.natCast_mul_eq_smul, norm_smul, Real.norm_natCast]
  have h2 : ‖(k : R) * H k‖ ≤ ‖indicial A k (H k)‖ + ‖ad A (H k)‖ := by
    unfold indicial
    calc ‖(k : R) * H k‖ = ‖((k : R) * H k - ad A (H k)) + ad A (H k)‖ := by rw [sub_add_cancel]
      _ ≤ _ := norm_add_le _ _
  have h3 := FuchsianConvergence.norm_ad_le A (H k)
  have h4 : ‖indicial A k (H k)‖ ≤ a * ∑ j ∈ range k, ‖H j‖ := by
    rw [show kzM0 A B 0 = A from rfl] at hrec
    rw [hrec]
    refine (norm_sum_le _ _).trans ?_
    rw [mul_sum]
    refine sum_le_sum fun j hj => ?_
    have hj := mem_range.1 hj
    obtain ⟨m, hm⟩ : ∃ m, k - j = m + 1 := ⟨k - j - 1, by omega⟩
    rw [hm]
    simp only [kzM0, neg_mul, norm_neg]
    exact (norm_mul_le _ _).trans (mul_le_mul_of_nonneg_right hB (norm_nonneg _))
  have hHk := norm_nonneg (H k)
  have : (k : ℝ) * ‖H k‖ ≤ a * ∑ j ∈ range k, ‖H j‖ + 2 * a * ‖H k‖ := by
    nlinarith [mul_le_mul_of_nonneg_right hA hHk]
  nlinarith [mul_le_mul_of_nonneg_left hk1 (mul_nonneg (mul_nonneg zero_le_two ha) hHk)]

omit [CompleteSpace R] in
/-- **Coefficient estimate for small residues.** With `β = a/(1 − 2a)` and `λ = 1 + β`:
`∑_{j ≤ k} ‖H_j‖ ≤ λ^k` and `‖H_{k+1}‖ ≤ β λ^k`. -/
theorem norm_coeff_le_small [NormOneClass R] (A B : R) (H : ℕ → R) (h0 : H 0 = 1)
    (hH : IsFormalGauge (kzM0 A B) H) {a : ℝ} (hA : ‖A‖ ≤ a) (hB : ‖B‖ ≤ a)
    (ha : 2 * a < 1) (k : ℕ) :
    ∑ j ∈ range (k + 1), ‖H j‖ ≤ (1 + a / (1 - 2 * a)) ^ k ∧
      ‖H (k + 1)‖ ≤ a / (1 - 2 * a) * (1 + a / (1 - 2 * a)) ^ k := by
  have ha0 : 0 ≤ a := (norm_nonneg _).trans hA
  have hd : 0 < 1 - 2 * a := by linarith
  set β := a / (1 - 2 * a)
  have hβ : 0 ≤ β := div_nonneg ha0 hd.le
  induction k with
  | zero =>
    have hs : ∑ j ∈ range 1, ‖H j‖ ≤ 1 := by simp [h0]
    refine ⟨by simpa using hs, ?_⟩
    have st := coeff_step A B H h0 hH hA hB 1 one_pos
    simp only [Nat.cast_one, one_mul] at st
    rw [pow_zero, mul_one, le_div_iff₀ hd]
    calc ‖H (0 + 1)‖ * (1 - 2 * a) = (1 - 2 * a) * ‖H 1‖ := by ring
      _ ≤ a * ∑ j ∈ range 1, ‖H j‖ := st
      _ ≤ a * 1 := by gcongr
      _ = a := mul_one a
  | succ k ih =>
    obtain ⟨hS, hh⟩ := ih
    have hS' : ∑ j ∈ range (k + 1 + 1), ‖H j‖ ≤ (1 + β) ^ (k + 1) := by
      rw [sum_range_succ, pow_succ]
      nlinarith [pow_nonneg (show (0 : ℝ) ≤ 1 + β by linarith) k]
    refine ⟨hS', ?_⟩
    have st := coeff_step A B H h0 hH hA hB (k + 2) (by omega)
    have hk1 : (1 : ℝ) ≤ ((k + 2 : ℕ) : ℝ) := by norm_cast; omega
    have hHn := norm_nonneg (H (k + 1 + 1))
    have : (1 - 2 * a) * ‖H (k + 1 + 1)‖ ≤ a * (1 + β) ^ (k + 1) := by
      calc (1 - 2 * a) * ‖H (k + 1 + 1)‖ ≤ ((k + 2 : ℕ) : ℝ) * (1 - 2 * a) * ‖H (k + 2)‖ := by
            nlinarith [mul_nonneg hd.le hHn]
        _ ≤ a * ∑ j ∈ range (k + 2), ‖H j‖ := st
        _ ≤ a * (1 + β) ^ (k + 1) := by gcongr
    rw [show β * (1 + β) ^ (k + 1) = a * (1 + β) ^ (k + 1) / (1 - 2 * a) by
      simp only [β]; ring, le_div_iff₀ hd]
    linarith

omit [CompleteSpace R] in
theorem norm_coeff_succ_le [NormOneClass R] (A B : R) (H : ℕ → R) (h0 : H 0 = 1)
    (hH : IsFormalGauge (kzM0 A B) H) {a : ℝ} (hA : ‖A‖ ≤ a) (hB : ‖B‖ ≤ a)
    (ha : 2 * a < 1) (k : ℕ) :
    ‖H (k + 1)‖ ≤ a / (1 - 2 * a) * (1 + a / (1 - 2 * a)) ^ k :=
  (norm_coeff_le_small A B H h0 hH hA hB ha k).2

/-- **The gauge series at `t = 1/2`.** `‖H(1/2) − 1‖ ≤ β/(1 − β)`, `β = a/(1 − 2a)`, for
`a < 1/3`. -/
theorem norm_series_half_sub_one [NormOneClass R] (A B : R) (H : ℕ → R) (h0 : H 0 = 1)
    (hH : IsFormalGauge (kzM0 A B) H) {a : ℝ} (hA : ‖A‖ ≤ a) (hB : ‖B‖ ≤ a)
    (ha : 3 * a < 1) :
    ‖series H (1 / 2) - 1‖ ≤ a / (1 - 3 * a) := by
  have ha0 : 0 ≤ a := (norm_nonneg _).trans hA
  have h2 : 2 * a < 1 := by linarith
  have hd : 0 < 1 - 2 * a := by linarith
  set β := a / (1 - 2 * a) with hβdef
  have hβ0 : 0 ≤ β := div_nonneg ha0 hd.le
  have hβ1 : β < 1 := by rw [hβdef, div_lt_one hd]; linarith
  set r := (1 + β) / 2
  have hr0 : 0 ≤ r := by positivity
  have hr1 : r < 1 := by simp only [r]; linarith
  have hb := boundedOn_kz_solution A B H h0 hH
  have hs := (summable_norm_of_bounded hb (t := 1 / 2) (by norm_num)).of_norm
  have hdom : ∀ k : ℕ, ‖(1 / 2 : ℝ) ^ (k + 1) • H (k + 1)‖ ≤ β / 2 * r ^ k := by
    intro k
    rw [norm_smul, Real.norm_eq_abs, abs_of_pos (by positivity)]
    calc (1 / 2 : ℝ) ^ (k + 1) * ‖H (k + 1)‖ ≤ (1 / 2) ^ (k + 1) * (β * (1 + β) ^ k) := by
          gcongr; exact norm_coeff_succ_le A B H h0 hH hA hB h2 k
      _ = β / 2 * r ^ k := by simp only [r]; rw [div_pow, div_pow, pow_succ]; field_simp; ring
  have hgs : Summable fun k : ℕ => β / 2 * r ^ k :=
    (summable_geometric_of_lt_one hr0 hr1).mul_left _
  unfold series
  rw [hs.tsum_eq_zero_add, pow_zero, one_smul, h0, add_sub_cancel_left]
  calc ‖∑' k : ℕ, (1 / 2 : ℝ) ^ (k + 1) • H (k + 1)‖
      ≤ ∑' k : ℕ, β / 2 * r ^ k :=
        (norm_tsum_le_tsum_norm (Summable.of_nonneg_of_le (fun _ => norm_nonneg _) hdom hgs)).trans
          (Summable.tsum_le_tsum hdom (Summable.of_nonneg_of_le (fun _ => norm_nonneg _) hdom hgs)
            hgs)
    _ = β / 2 * (1 - r)⁻¹ := by rw [tsum_mul_left, tsum_geometric_of_lt_one hr0 hr1]
    _ = a / (1 - 3 * a) := by
        have h3 : 1 - 3 * a ≠ 0 := by linarith
        have hd' : 1 - 2 * a ≠ 0 := hd.ne'
        have hβu : β * (1 - 2 * a) = a := div_mul_cancel₀ a hd'
        have e : 1 - r = (1 - 3 * a) / (2 * (1 - 2 * a)) := by
          rw [eq_div_iff (mul_ne_zero two_ne_zero hd')]; simp only [r]
          linear_combination (-1 : ℝ) * hβu
        rw [e, inv_div, hβdef]
        field_simp
        rw [mul_comm a]
        exact mul_div_mul_left a _ (by intro h; apply hd'; linarith)

end Banach

section Associator

open QOU.KZ.KZPentagon

variable {R : Type*} [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R] [NormOneClass R]

omit [NormedAlgebra ℂ R] [CompleteSpace R] [NormOneClass R] in
theorem norm_mul_sub_one_le' {x y : R} {d e : ℝ} (hx : ‖x - 1‖ ≤ d) (hy : ‖y - 1‖ ≤ e) :
    ‖x * y - 1‖ ≤ (1 + d) * (1 + e) - 1 := by
  refine (norm_mul_sub_one_le x y).trans ?_
  have := norm_nonneg (x - 1); have := norm_nonneg (y - 1)
  nlinarith

omit [NormOneClass R] in
theorem norm_tpow_half_sub_one (X : R) {a : ℝ} (hX : ‖X‖ ≤ a) (s : ℝ) (hs : |s| = Real.log 2) :
    ‖NormedSpace.exp ℝ (s • X) - 1‖ ≤ Real.exp (Real.log 2 * a) - 1 := by
  refine (norm_exp_sub_one_le _).trans ?_
  gcongr
  rw [norm_smul, Real.norm_eq_abs, hs]
  exact mul_le_mul_of_nonneg_left hX (Real.log_nonneg one_le_two)

/-- **Quantitative bound on the KZ associator for small residues.** If `‖A‖, ‖B‖ ≤ a < 1/4`,
then `‖Φ(A, B) − 1‖ ≤ e^{2 a log 2}·(1 + a/(1 − 3a))(1 + a/(1 − 4a)) − 1`
(written as `(1 + δₑ)² (1 + δ)(1 + δ') − 1`). -/
theorem norm_Φ_sub_one_le (A B : R) (hA : NonResonant A) (hB : NonResonant B) {a : ℝ}
    (hAa : ‖A‖ ≤ a) (hBa : ‖B‖ ≤ a) (ha : 4 * a < 1) :
    ‖Φ A B hA hB - 1‖ ≤ (1 + (Real.exp (Real.log 2 * a) - 1)) * (1 + a / (1 - 4 * a)) *
      (1 + a / (1 - 3 * a)) * (1 + (Real.exp (Real.log 2 * a) - 1)) - 1 := by
  have ha0 : 0 ≤ a := (norm_nonneg _).trans hAa
  have h3 : 3 * a < 1 := by linarith
  obtain ⟨-, hΦ⟩ := phiKZ_spec A B (H0 A B hA) (H0 B A hB) (H0_zero _ _ hA) (H0_gauge _ _ hA)
    (H0_zero _ _ hB) (H0_gauge _ _ hB)
  have ht : (1 / 2 : ℝ) ∈ Set.Ioo (0 : ℝ) 1 := ⟨by norm_num, by norm_num⟩
  have hG := hΦ (1 / 2) ht
  set S₀ := series (H0 A B hA) (1 / 2)
  set S₁ := series (H0 B A hB) (1 / 2)
  set TA := NormedSpace.exp ℝ (Real.log (1 / 2) • A)
  set TB := NormedSpace.exp ℝ (Real.log (1 / 2) • B)
  set TB' := NormedSpace.exp ℝ ((-Real.log (1 / 2)) • B)
  have hG' : S₀ * TA = S₁ * TB * Φ A B hA hB := by
    have e : (1 : ℝ) - 1 / 2 = 1 / 2 := by norm_num
    simpa only [G₀, G₁, tpow, e] using hG
  have hlog : |Real.log (1 / 2)| = Real.log 2 := by
    rw [one_div, Real.log_inv, abs_neg, abs_of_nonneg (Real.log_nonneg one_le_two)]
  have hlog' : |-Real.log (1 / 2)| = Real.log 2 := by rw [abs_neg, hlog]
  have hTB : TB' * TB = 1 := by
    rw [← NormedSpace.exp_add_of_commute ((Commute.refl B).smul_left _ |>.smul_right _), neg_smul,
      neg_add_cancel, NormedSpace.exp_zero]
  -- the four bounds
  have b₀ : ‖S₀ - 1‖ ≤ a / (1 - 3 * a) :=
    norm_series_half_sub_one A B _ (H0_zero _ _ hA) (H0_gauge _ _ hA) hAa hBa h3
  have b₁ : ‖S₁ - 1‖ ≤ a / (1 - 3 * a) :=
    norm_series_half_sub_one B A _ (H0_zero _ _ hB) (H0_gauge _ _ hB) hBa hAa h3
  have hδ1 : a / (1 - 3 * a) < 1 := by rw [div_lt_one (by linarith)]; linarith
  obtain ⟨hU₁, b₁'⟩ := norm_inverse_sub_one_le S₁ (b₁.trans_lt hδ1)
  have b₁'' : ‖Ring.inverse S₁ - 1‖ ≤ a / (1 - 4 * a) := by
    refine b₁'.trans ?_
    have hn := norm_nonneg (S₁ - 1)
    have hd3 : 0 < 1 - 3 * a := by linarith
    have hd4 : 0 < 1 - 4 * a := by linarith
    calc ‖S₁ - 1‖ / (1 - ‖S₁ - 1‖) ≤ (a / (1 - 3 * a)) / (1 - a / (1 - 3 * a)) := by
          gcongr
          · linarith
    _ = a / (1 - 4 * a) := by
          rw [show (1 : ℝ) - a / (1 - 3 * a) = (1 - 4 * a) / (1 - 3 * a) by
            rw [eq_div_iff hd3.ne', sub_mul, div_mul_cancel₀ _ hd3.ne']; ring,
            div_div_div_cancel_right₀ hd3.ne']
  have bA := norm_tpow_half_sub_one A hAa _ hlog
  have bB := norm_tpow_half_sub_one B hBa _ hlog'
  -- the factorisation `Φ = (1/2)^{−B} H₁(1/2)^{−1} H₀(1/2) (1/2)^A`
  have hfac : Φ A B hA hB = TB' * Ring.inverse S₁ * S₀ * TA := by
    calc Φ A B hA hB = TB' * (Ring.inverse S₁ * S₁) * TB * Φ A B hA hB := by
          rw [Ring.inverse_mul_cancel _ hU₁, mul_one, hTB, one_mul]
      _ = TB' * Ring.inverse S₁ * (S₀ * TA) := by rw [hG']; noncomm_ring
      _ = _ := by noncomm_ring
  rw [hfac]
  exact (norm_mul_sub_one_le' (norm_mul_sub_one_le' (norm_mul_sub_one_le' bB b₁'') b₀) bA).trans
    (le_of_eq (by ring))

/-- **Explicit radius.** If `‖A‖, ‖B‖ ≤ 1/12`, then `‖Φ(A, B) − 1‖ < 1/2`. -/
theorem norm_Φ_sub_one_lt_half (A B : R) (hA : NonResonant A) (hB : NonResonant B) {a : ℝ}
    (hAa : ‖A‖ ≤ a) (hBa : ‖B‖ ≤ a) (ha : a ≤ 1 / 12) :
    ‖Φ A B hA hB - 1‖ < 1 / 2 := by
  have ha0 : 0 ≤ a := (norm_nonneg _).trans hAa
  refine (norm_Φ_sub_one_le A B hA hB hAa hBa (by linarith)).trans_lt ?_
  have hl : Real.log 2 ≤ 1 := by
    have := Real.log_le_sub_one_of_pos (show (0 : ℝ) < 2 by norm_num); linarith
  have he : Real.exp (Real.log 2 * a) ≤ 12 / 11 := by
    have hx : Real.log 2 * a ≤ 1 / 12 := by nlinarith [Real.log_nonneg one_le_two]
    have hx0 : 0 ≤ Real.log 2 * a := mul_nonneg (Real.log_nonneg one_le_two) ha0
    rcases hx0.eq_or_lt with h | h
    · rw [← h, Real.exp_zero]; norm_num
    · calc Real.exp (Real.log 2 * a) ≤ 1 / (1 - Real.log 2 * a) :=
            (Real.exp_bound_div_one_sub_of_interval' h (by linarith)).le
        _ ≤ 12 / 11 := by rw [div_le_div_iff₀ (by linarith) (by norm_num)]; linarith
  have h1 : a / (1 - 3 * a) ≤ 1 / 9 := by
    rw [div_le_div_iff₀ (by linarith) (by norm_num)]; linarith
  have h2 : a / (1 - 4 * a) ≤ 1 / 8 := by
    rw [div_le_div_iff₀ (by linarith) (by norm_num)]; linarith
  have he1 : 0 ≤ 1 + (Real.exp (Real.log 2 * a) - 1) := by linarith [Real.exp_pos (Real.log 2 * a)]
  have hp1 : 0 ≤ 1 + a / (1 - 4 * a) := by have := div_nonneg ha0 (show (0:ℝ) ≤ 1 - 4 * a by linarith); linarith
  have hp2 : 0 ≤ 1 + a / (1 - 3 * a) := by have := div_nonneg ha0 (show (0:ℝ) ≤ 1 - 3 * a by linarith); linarith
  calc (1 + (Real.exp (Real.log 2 * a) - 1)) * (1 + a / (1 - 4 * a)) * (1 + a / (1 - 3 * a)) *
        (1 + (Real.exp (Real.log 2 * a) - 1)) - 1
      ≤ (12 / 11) * (1 + 1 / 8) * (1 + 1 / 9) * (12 / 11) - 1 := by
        gcongr <;> linarith
    _ < 1 / 2 := by norm_num

end Associator

end QOU.KZ.SmallHbar
