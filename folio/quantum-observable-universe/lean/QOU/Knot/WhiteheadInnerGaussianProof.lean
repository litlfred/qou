import QOU.Knot.WhiteheadMasterErrRate
import Mathlib.Analysis.SpecialFunctions.Pow.Asymptotics

/-!
# vdV Lemma 2a/2b in `L¹`: an instance of `WhiteheadInnerGaussianModel`

Per-term tail decay outside the `R`-window (from the continuum quadratic decay of
`whiteheadFunctional2` plus the grid ceiling and the logarithmic `masterErr` rate),
the window Taylor estimate (`Dw_window`), and the assembly with `R = t³`,
`t = N^{1/5}`.
-/

namespace QOU.Knot.WhiteheadInner

open Real QOU.Knot.FigureEightVolume

theorem quad_out_ge {x y R s : ℝ} (hR : 0 ≤ R) (hs0 : 0 ≤ s)
    (hout : R < |x| ∨ (|x| ≤ R ∧ R < |y| ∧ 1 / 2 ≤ s)) :
    R ^ 2 ≤ x ^ 2 + s * (x + 2 * y) ^ 2 := by
  rcases hout with h | ⟨_, hy, hs⟩
  · have h1 : R ^ 2 ≤ x ^ 2 := by
      rw [← sq_abs x]; exact pow_le_pow_left₀ hR h.le 2
    have : 0 ≤ s * (x + 2 * y) ^ 2 := by positivity
    linarith
  · have h1 : R ^ 2 ≤ y ^ 2 := by
      rw [← sq_abs y]; exact pow_le_pow_left₀ hR hy.le 2
    have h2 : (1 / 2) * (x + 2 * y) ^ 2 ≤ s * (x + 2 * y) ^ 2 :=
      mul_le_mul_of_nonneg_right hs (by positivity)
    nlinarith [sq_nonneg (3 * x + 2 * y)]

/-- **Per-term tail decay (vdV Lemma 2b).** Outside the `R`-window,
`log S_{n,k} ≤ log S_centre − R²/(2N) + 4 + 4 N·masterErr N`. -/
theorem log_term_le_tail {N n k : ℕ} {R : ℝ} (hN : 24 ≤ N) (hnk : n + k ≤ N - 1)
    (hR : 0 ≤ R) (hRN : 24 * R ≤ N)
    (hout : R < |(n : ℝ) - N / 2| ∨ R < |(k : ℝ) - N / 4|) :
    Real.log (whiteheadTerm N n k)
      ≤ Real.log (whiteheadTerm N (N / 2) (N / 4)) - R ^ 2 / (2 * N) + 4
          + 4 * ((N : ℝ) * masterErr N) := by
  have hpi := Real.pi_pos
  have hpi3 := Real.pi_gt_three
  have hNpos : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
  have hN0 : (N : ℝ) ≠ 0 := hNpos.ne'
  have hme := masterErr_nonneg N
  have hnkR : ((n : ℝ) + k) ≤ N - 1 := by
    have : n + k + 1 ≤ N := by omega
    have : ((n + k + 1 : ℕ) : ℝ) ≤ N := by exact_mod_cast this
    push_cast at this; linarith
  have hn0 : (0 : ℝ) ≤ n := Nat.cast_nonneg n
  have hk0 : (0 : ℝ) ≤ k := Nat.cast_nonneg k
  set h : ℝ := π / N with hh
  have hhN : h * N = π := by rw [hh]; field_simp
  have hh0 : 0 < h := by positivity
  have hA := two_pi_log_whiteheadTerm_le_functional (by omega : 4 ≤ N) hnk
  have hu0 : 0 ≤ 2 * ((n : ℝ) * h) := by positivity
  have hv0 : 0 ≤ 2 * ((k : ℝ) * h) := by positivity
  have huv : 2 * ((n : ℝ) * h) + 2 * ((k : ℝ) * h) ≤ 2 * π := by
    have : ((n : ℝ) + k) * h ≤ N * h := mul_le_mul_of_nonneg_right (by linarith) hh0.le
    nlinarith
  have hD := functional2_decay hu0 hv0 huv
  have hCc := functional_centre_ge hN
  have hC0 := functional_le_two_pi_log_centre (by omega : 4 ≤ N)
  rw [← hh] at hCc hC0 hA
  -- the quadratic penalty in signed offsets
  set x : ℝ := (n : ℝ) - N / 2 with hx
  set y : ℝ := (k : ℝ) - N / 4 with hy
  set s : ℝ := Real.sin (2 * ((n : ℝ) * h) / 2) with hs
  have hs0 : 0 ≤ s := by
    apply Real.sin_nonneg_of_nonneg_of_le_pi (by positivity)
    have : (n : ℝ) * h ≤ N * h := mul_le_mul_of_nonneg_right (by linarith) hh0.le
    linarith
  have hP : (2 * ((n : ℝ) * h) - π) ^ 2 / (4 * π)
      + s / π * (2 * ((k : ℝ) * h) - (π - 2 * ((n : ℝ) * h) / 2)) ^ 2
      = π / (N : ℝ) ^ 2 * (x ^ 2 + s * (x + 2 * y) ^ 2) := by
    rw [hx, hy, hh]; field_simp; ring
  have hq : R ^ 2 ≤ x ^ 2 + s * (x + 2 * y) ^ 2 := by
    apply quad_out_ge hR hs0
    rcases hout with hxo | hyo
    · exact Or.inl hxo
    · rcases le_or_gt |x| R with hxR | hxR
      · refine Or.inr ⟨hxR, hyo, ?_⟩
        rw [hs]
        have hxh : |x * h| ≤ π / 24 := by
          rw [abs_mul, abs_of_pos hh0]
          have : R * h ≤ π / 24 := by
            rw [hh, mul_div_assoc', div_le_div_iff₀ hNpos (by norm_num)]; nlinarith
          calc |x| * h ≤ R * h := mul_le_mul_of_nonneg_right hxR hh0.le
            _ ≤ _ := this
        have heq : 2 * ((n : ℝ) * h) / 2 = π / 2 + x * h := by
          rw [hx]; linear_combination (1/2:ℝ) * hhN
        rw [heq]
        rw [abs_le] at hxh
        exact sin_ge_half (by linarith [hxh.1]) (by linarith [hxh.2])
      · exact Or.inl hxR
  have hPR : π * R ^ 2 / (N : ℝ) ^ 2 ≤ π / (N : ℝ) ^ 2 * (x ^ 2 + s * (x + 2 * y) ^ 2) := by
    rw [div_mul_eq_mul_div, div_le_div_iff_of_pos_right (by positivity)]
    exact mul_le_mul_of_nonneg_left hq hpi.le
  -- combine
  have key : (2 * π / N) * (Real.log (whiteheadTerm N n k)
      - Real.log (whiteheadTerm N (N / 2) (N / 4)))
      ≤ -(π * R ^ 2 / (N : ℝ) ^ 2) + 8 * h + 20 * masterErr N := by
    rw [mul_sub]; linarith
  have key2 : 2 * π * (Real.log (whiteheadTerm N n k)
      - Real.log (whiteheadTerm N (N / 2) (N / 4)))
      ≤ 2 * π * (-(R ^ 2 / (2 * N)) + 4 + 4 * ((N : ℝ) * masterErr N)) := by
    have := mul_le_mul_of_nonneg_left key hNpos.le
    have e1 : (N : ℝ) * ((2 * π / N) * (Real.log (whiteheadTerm N n k)
        - Real.log (whiteheadTerm N (N / 2) (N / 4))))
        = 2 * π * (Real.log (whiteheadTerm N n k)
        - Real.log (whiteheadTerm N (N / 2) (N / 4))) := by field_simp
    have e2 : (N : ℝ) * (-(π * R ^ 2 / (N : ℝ) ^ 2) + 8 * h + 20 * masterErr N)
        = 2 * π * (-(R ^ 2 / (2 * N)) + 4) + 20 * ((N : ℝ) * masterErr N) := by
      rw [hh]; field_simp; ring
    rw [e1, e2] at this
    have hNm : 0 ≤ (N : ℝ) * masterErr N := mul_nonneg hNpos.le hme
    have h20 : 20 * ((N : ℝ) * masterErr N) ≤ 2 * π * (4 * ((N : ℝ) * masterErr N)) := by
      have h24 : (20 : ℝ) ≤ 2 * π * 4 := by linarith
      calc 20 * ((N : ℝ) * masterErr N) ≤ (2 * π * 4) * ((N : ℝ) * masterErr N) :=
            mul_le_mul_of_nonneg_right h24 hNm
        _ = _ := by ring
    linarith
  have := le_of_mul_le_mul_left key2 (by positivity)
  linarith

theorem Qf_nonneg (x y : ℝ) : 0 ≤ Qf x y := by
  unfold Qf; nlinarith [sq_nonneg (x + y), sq_nonneg y]

theorem Qf_ge_out {x y R : ℝ} (hR : 0 ≤ R) (hout : R < |x| ∨ R < |y|) : R ^ 2 / 2 ≤ Qf x y := by
  unfold Qf
  rcases hout with h | h
  · have h1 : R ^ 2 ≤ x ^ 2 := by rw [← sq_abs x]; exact pow_le_pow_left₀ hR h.le 2
    nlinarith [sq_nonneg (x + 2 * y)]
  · have h1 : R ^ 2 ≤ y ^ 2 := by rw [← sq_abs y]; exact pow_le_pow_left₀ hR h.le 2
    nlinarith [sq_nonneg (x + y)]

theorem abs_exp_sub_one_le (t : ℝ) : |Real.exp t - 1| ≤ Real.exp |t| - 1 := by
  rcases le_total 0 t with ht | ht
  · rw [abs_of_nonneg ht, abs_of_nonneg (by linarith [Real.add_one_le_exp t])]
  · rw [abs_of_nonpos ht, abs_of_nonpos (by linarith [Real.exp_le_one_iff.mpr ht])]
    have h1 := Real.add_one_le_exp t
    have h2 := Real.add_one_le_exp (-t)
    have h3 : Real.exp t * Real.exp (-t) = 1 := by rw [← Real.exp_add]; simp
    nlinarith [Real.exp_pos t, Real.exp_pos (-t)]

/-- The amplitude `B_N = exp D(⌊N/2⌋, ⌊N/4⌋)`. -/
noncomputable def ampB (N : ℕ) : ℝ := Real.exp (Dw N (N / 2) (N / 4))

/-- Window factor `η = exp(δ) − 1`, `δ = ε(R+2)(2R+2)`. -/
noncomputable def winF (N : ℕ) (R : ℝ) : ℝ := Real.exp (stepErr N (R + 2) * (2 * R + 2)) - 1

/-- Tail factor `exp(−R²/(2N)) (exp(4 + 4 N masterErr N) + 1)`. -/
noncomputable def tailF (N : ℕ) (R : ℝ) : ℝ :=
  Real.exp (-(R ^ 2 / (2 * N))) * (Real.exp (4 + 4 * ((N : ℝ) * masterErr N)) + 1)

theorem winF_nonneg (N : ℕ) {R : ℝ} (hR : 0 ≤ R) : 0 ≤ winF N R := by
  unfold winF
  have := stepErr_nonneg N (R + 2)
  have : 0 ≤ stepErr N (R + 2) * (2 * R + 2) := by positivity
  linarith [Real.add_one_le_exp (stepErr N (R + 2) * (2 * R + 2))]

theorem tailF_nonneg (N : ℕ) (R : ℝ) : 0 ≤ tailF N R := by unfold tailF; positivity

/-- **Pointwise vdV Lemma 2a + 2b.** -/
theorem term_bound {N n k : ℕ} {R : ℝ} (hN : 24 ≤ N) (hR : 0 ≤ R) (hRN : 24 * (R + 2) ≤ N)
    (hn : n < N) (hk : k < N - n) :
    |whiteheadTerm N n k - ampB N * whitehead2DGauss N n k|
      ≤ ampB N * (whitehead2DGauss N n k * winF N R + tailF N R) := by
  have hpi3 := Real.pi_gt_three
  have hNpos : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
  have hnk : n + k ≤ N - 1 := by omega
  have hSpos : 0 < whiteheadTerm N n k := whiteheadTerm_pos (by omega)
  set x : ℝ := (n : ℝ) - N / 2 with hx
  set y : ℝ := (k : ℝ) - N / 4 with hy
  have hE : whitehead2DGauss N n k = Real.exp (-(π / N) * Qf x y) := by
    rw [whitehead2DGauss_eq (by omega) hn.le]; unfold Qf; rfl
  have hS : whiteheadTerm N n k = Real.exp (Dw N n k) * whitehead2DGauss N n k := by
    rw [hE, ← Real.exp_add, Dw]
    rw [show Real.log (whiteheadTerm N n k) + π / N * Qf x y + -(π / N) * Qf x y
      = Real.log (whiteheadTerm N n k) by ring, Real.exp_log hSpos]
  have hB := Real.exp_pos (Dw N (N / 2) (N / 4))
  have hEpos : 0 < whitehead2DGauss N n k := by rw [hE]; exact Real.exp_pos _
  have hwin := winF_nonneg N hR
  have htail := tailF_nonneg N R
  by_cases hin : |x| ≤ R ∧ |y| ≤ R
  · have hDw := Dw_window (by omega) hR hRN hin.1 hin.2
    have hdiff : whiteheadTerm N n k - ampB N * whitehead2DGauss N n k
        = ampB N * whitehead2DGauss N n k * (Real.exp (Dw N n k - Dw N (N / 2) (N / 4)) - 1) := by
      rw [hS, ampB, Real.exp_sub]; field_simp
    rw [hdiff, abs_mul, abs_of_pos (by unfold ampB; positivity)]
    have h1 := abs_exp_sub_one_le (Dw N n k - Dw N (N / 2) (N / 4))
    have h2 : Real.exp |Dw N n k - Dw N (N / 2) (N / 4)| - 1 ≤ winF N R := by
      unfold winF; linarith [Real.exp_le_exp.mpr hDw]
    have h3 : ampB N * whitehead2DGauss N n k * |Real.exp (Dw N n k - Dw N (N / 2) (N / 4)) - 1|
        ≤ ampB N * whitehead2DGauss N n k * winF N R :=
      mul_le_mul_of_nonneg_left (h1.trans h2) (by unfold ampB; positivity)
    have h4 : 0 ≤ ampB N * tailF N R := by unfold ampB; positivity
    nlinarith
  · have hout : R < |x| ∨ R < |y| := by
      by_contra hc; push_neg at hc; exact hin hc
    have hRN' : 24 * R ≤ N := by linarith
    have hlog := log_term_le_tail hN hnk hR hRN' hout
    have hS0pos : 0 < whiteheadTerm N (N / 2) (N / 4) := whiteheadTerm_pos (by omega)
    have hlogB : Real.log (whiteheadTerm N (N / 2) (N / 4)) ≤ Dw N (N / 2) (N / 4) := by
      unfold Dw
      have := Qf_nonneg (((N / 2 : ℕ) : ℝ) - N / 2) (((N / 4 : ℕ) : ℝ) - N / 4)
      have : 0 ≤ π / N * Qf (((N / 2 : ℕ) : ℝ) - N / 2) (((N / 4 : ℕ) : ℝ) - N / 4) := by positivity
      linarith
    have hSle : whiteheadTerm N n k
        ≤ ampB N * (Real.exp (-(R ^ 2 / (2 * N))) * Real.exp (4 + 4 * ((N : ℝ) * masterErr N))) := by
      rw [← Real.exp_log hSpos, ampB, ← Real.exp_add, ← Real.exp_add]
      apply Real.exp_le_exp.mpr; linarith
    have hEle : whitehead2DGauss N n k ≤ Real.exp (-(R ^ 2 / (2 * N))) := by
      rw [hE]; apply Real.exp_le_exp.mpr
      have hq := Qf_ge_out hR hout
      have : R ^ 2 / (2 * N) ≤ π / N * Qf x y := by
        rw [div_mul_eq_mul_div, div_le_div_iff₀ (by positivity) hNpos]
        have hQ0 : 0 ≤ Qf x y := Qf_nonneg x y
        have h1 : R ^ 2 ≤ π * Qf x y * 2 := by nlinarith
        have := mul_le_mul_of_nonneg_right h1 hNpos.le
        linarith
      linarith
    have hBE : 0 ≤ ampB N * whitehead2DGauss N n k := by unfold ampB; positivity
    have habs : |whiteheadTerm N n k - ampB N * whitehead2DGauss N n k|
        ≤ whiteheadTerm N n k + ampB N * whitehead2DGauss N n k := by
      rw [abs_le]; constructor <;> linarith
    have hBEle : ampB N * whitehead2DGauss N n k ≤ ampB N * Real.exp (-(R ^ 2 / (2 * N))) :=
      mul_le_mul_of_nonneg_left hEle (by unfold ampB; positivity)
    have hEw : 0 ≤ ampB N * (whitehead2DGauss N n k * winF N R) := by unfold ampB; positivity
    have : ampB N * (whitehead2DGauss N n k * winF N R + tailF N R)
        = ampB N * (whitehead2DGauss N n k * winF N R)
          + ampB N * (Real.exp (-(R ^ 2 / (2 * N))) * Real.exp (4 + 4 * ((N : ℝ) * masterErr N)))
          + ampB N * Real.exp (-(R ^ 2 / (2 * N))) := by unfold tailF; ring
    rw [this]; linarith

theorem inner_sum_bound {N n : ℕ} {R : ℝ} (hN : 24 ≤ N) (hR : 0 ≤ R) (hRN : 24 * (R + 2) ≤ N)
    (hn : n < N) :
    ∑ k ∈ Finset.range (N - n), |whiteheadTerm N n k - ampB N * whitehead2DGauss N n k|
      ≤ ampB N * (winF N R * (whiteheadGaussianProfile N n * (2 * Real.sqrt ((N : ℝ) / 2)))
          + N * tailF N R) := by
  have hBpos : 0 < ampB N := by unfold ampB; positivity
  have hw := winF_nonneg N hR
  have ht := tailF_nonneg N R
  have hprof : 0 ≤ whiteheadGaussianProfile N n := by
    rw [whiteheadGaussianProfile_eq]; positivity
  calc ∑ k ∈ Finset.range (N - n), |whiteheadTerm N n k - ampB N * whitehead2DGauss N n k|
      ≤ ∑ k ∈ Finset.range (N - n), ampB N * (whitehead2DGauss N n k * winF N R + tailF N R) :=
        Finset.sum_le_sum fun k hk => term_bound hN hR hRN hn (Finset.mem_range.mp hk)
    _ = ampB N * (winF N R * (whiteheadGaussianProfile N n
          * ∑ k ∈ Finset.range (N - n), whiteheadInnerGauss N n k)
          + ((N - n : ℕ) : ℝ) * tailF N R) := by
        rw [← Finset.mul_sum, Finset.sum_add_distrib, Finset.sum_const, Finset.card_range,
          nsmul_eq_mul, Finset.mul_sum, ← Finset.sum_mul]
        unfold whitehead2DGauss; ring
    _ ≤ _ := by
        apply mul_le_mul_of_nonneg_left _ hBpos.le
        have h1 := whiteheadInnerSum_le (by omega : 1 ≤ N) n
        have h2 : ((N - n : ℕ) : ℝ) ≤ N := by exact_mod_cast Nat.sub_le N n
        have h3 := mul_le_mul_of_nonneg_left h1 hprof
        have h4 := mul_le_mul_of_nonneg_left h3 hw
        have h5 := mul_le_mul_of_nonneg_right h2 ht
        linarith

/-- **Summed vdV Lemma 2 (`L¹`).** -/
theorem sum_bound {N : ℕ} {R : ℝ} (hN : 24 ≤ N) (hR : 0 ≤ R) (hRN : 24 * (R + 2) ≤ N) :
    ∑ n ∈ Finset.range N, ((2 * n + 1 : ℕ) : ℝ) *
        ∑ k ∈ Finset.range (N - n), |whiteheadTerm N n k - ampB N * whitehead2DGauss N n k|
      ≤ ampB N * ((N : ℝ) ^ 2 * (8 * winF N R + 2 * N * tailF N R)) := by
  have hBpos : 0 < ampB N := by unfold ampB; positivity
  have hw := winF_nonneg N hR
  have ht := tailF_nonneg N R
  have hNpos : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
  set c : ℝ := 2 * Real.sqrt ((N : ℝ) / 2) with hc
  have hc0 : 0 ≤ c := by positivity
  have hstep : ∀ n ∈ Finset.range N, ((2 * n + 1 : ℕ) : ℝ) *
        ∑ k ∈ Finset.range (N - n), |whiteheadTerm N n k - ampB N * whitehead2DGauss N n k|
      ≤ (2 * N) * (ampB N * (winF N R * (whiteheadGaussianProfile N n * c) + N * tailF N R)) := by
    intro n hn
    have hn' := Finset.mem_range.mp hn
    have hprof : 0 ≤ whiteheadGaussianProfile N n := by
      rw [whiteheadGaussianProfile_eq]; positivity
    apply mul_le_mul _ (inner_sum_bound hN hR hRN hn') (Finset.sum_nonneg fun _ _ => abs_nonneg _)
      (by positivity)
    have : 2 * n + 1 ≤ 2 * N := by omega
    exact_mod_cast this
  refine (Finset.sum_le_sum hstep).trans ?_
  rw [← Finset.mul_sum, ← Finset.mul_sum, Finset.sum_add_distrib, ← Finset.mul_sum,
    ← Finset.sum_mul, Finset.sum_const, Finset.card_range, nsmul_eq_mul]
  have hP := sum_whiteheadGaussianProfile_le (by omega : 1 ≤ N)
  have hsq : c * (2 * Real.sqrt (2 * N)) = 4 * N := by
    rw [hc, show 2 * Real.sqrt ((N : ℝ) / 2) * (2 * Real.sqrt (2 * N))
      = 4 * (Real.sqrt ((N : ℝ) / 2) * Real.sqrt (2 * N)) by ring,
      ← Real.sqrt_mul (by positivity), show (N : ℝ) / 2 * (2 * N) = (N : ℝ) ^ 2 by ring,
      Real.sqrt_sq hNpos.le]
  have h1 : (∑ n ∈ Finset.range N, whiteheadGaussianProfile N n) * c ≤ 4 * N := by
    have := mul_le_mul_of_nonneg_right hP hc0
    linarith
  have h2 : winF N R * ((∑ n ∈ Finset.range N, whiteheadGaussianProfile N n) * c)
      ≤ winF N R * (4 * N) := mul_le_mul_of_nonneg_left h1 hw
  have h3 : ampB N * (winF N R * ((∑ n ∈ Finset.range N, whiteheadGaussianProfile N n) * c)
      + N * (N * tailF N R)) ≤ ampB N * (winF N R * (4 * N) + N * (N * tailF N R)) :=
    mul_le_mul_of_nonneg_left (by linarith) hBpos.le
  have h4 := mul_le_mul_of_nonneg_left h3 (by positivity : (0 : ℝ) ≤ 2 * N)
  exact h4.trans (le_of_eq (by ring))

/-- Window error with `N = t⁵`, `R = t³`: `δ ≤ (8π + 1440π²)/t`. -/
theorem delta_le {N : ℕ} {t : ℝ} (ht1 : 1 ≤ t) (hN5 : t ^ 5 = N) :
    stepErr N (t ^ 3 + 2) * (2 * t ^ 3 + 2) ≤ (8 * π + 1440 * π ^ 2) * t⁻¹ := by
  have hpi := Real.pi_pos
  have ht0 : 0 < t := by linarith
  set s : ℝ := t⁻¹ with hs
  have hs0 : 0 < s := by positivity
  have hts : t * s = 1 := by rw [hs]; field_simp
  have hNs : ((N : ℝ))⁻¹ = s ^ 5 := by rw [← hN5, hs, inv_pow]
  have ht3 : 1 ≤ t ^ 3 := one_le_pow₀ ht1
  have hst3 : t ^ 3 * s ^ 3 = 1 := by rw [← mul_pow, hts, one_pow]
  have hst6 : t ^ 6 * s ^ 6 = 1 := by rw [← mul_pow, hts, one_pow]
  unfold stepErr
  rw [div_eq_mul_inv (2 * π), div_eq_mul_inv _ ((N : ℝ) ^ 2), ← inv_pow, hNs]
  have hR2 : (t ^ 3 + 2) ^ 2 ≤ 9 * t ^ 6 := by nlinarith
  have hA : 40 * π ^ 2 * (t ^ 3 + 2) ^ 2 * (s ^ 5) ^ 2 ≤ 360 * π ^ 2 * s ^ 4 := by
    have := mul_le_mul_of_nonneg_left hR2 (by positivity : (0 : ℝ) ≤ 40 * π ^ 2 * (s ^ 5) ^ 2)
    calc 40 * π ^ 2 * (t ^ 3 + 2) ^ 2 * (s ^ 5) ^ 2
        = 40 * π ^ 2 * (s ^ 5) ^ 2 * (t ^ 3 + 2) ^ 2 := by ring
      _ ≤ 40 * π ^ 2 * (s ^ 5) ^ 2 * (9 * t ^ 6) := this
      _ = 360 * π ^ 2 * s ^ 4 * (t ^ 6 * s ^ 6) := by ring
      _ = _ := by rw [hst6, mul_one]
  have hB : 2 * t ^ 3 + 2 ≤ 4 * t ^ 3 := by linarith
  have hsum : 2 * π * s ^ 5 + 40 * π ^ 2 * (t ^ 3 + 2) ^ 2 * (s ^ 5) ^ 2
      ≤ 2 * π * s ^ 5 + 360 * π ^ 2 * s ^ 4 := by linarith
  have hs1 : s ≤ 1 := by rw [hs]; exact inv_le_one_of_one_le₀ ht1
  calc (2 * π * s ^ 5 + 40 * π ^ 2 * (t ^ 3 + 2) ^ 2 * (s ^ 5) ^ 2) * (2 * t ^ 3 + 2)
      ≤ (2 * π * s ^ 5 + 360 * π ^ 2 * s ^ 4) * (4 * t ^ 3) :=
        mul_le_mul hsum hB (by positivity) (by positivity)
    _ = (8 * π * s ^ 2 + 1440 * π ^ 2 * s) * (t ^ 3 * s ^ 3) := by ring
    _ = 8 * π * s ^ 2 + 1440 * π ^ 2 * s := by rw [hst3, mul_one]
    _ ≤ (8 * π + 1440 * π ^ 2) * s := by
        have : s ^ 2 ≤ s := by nlinarith
        nlinarith

/-- The tail profile `f(t) = 2 t⁵ e^{−t/2} (e^{244} t^{1200} + 1)`. -/
noncomputable def tailProf (t : ℝ) : ℝ :=
  2 * t ^ 5 * Real.exp (-(t / 2)) * (Real.exp 244 * t ^ 1200 + 1)

theorem tendsto_pow_mul_exp_neg_half (k : ℕ) :
    Filter.Tendsto (fun t : ℝ => t ^ k * Real.exp (-(t / 2))) Filter.atTop (nhds 0) := by
  have h := (Real.tendsto_pow_mul_exp_neg_atTop_nhds_zero k).comp
    (Filter.tendsto_id.atTop_div_const (by norm_num : (0 : ℝ) < 2))
  have h2 := h.const_mul ((2 : ℝ) ^ k)
  rw [mul_zero] at h2
  refine h2.congr fun t => ?_
  simp only [Function.comp, id]
  rw [← mul_assoc, ← mul_pow]; congr 2; ring

theorem tendsto_tailProf : Filter.Tendsto tailProf Filter.atTop (nhds 0) := by
  have h1 := (tendsto_pow_mul_exp_neg_half 1205).const_mul (2 * Real.exp 244)
  have h2 := (tendsto_pow_mul_exp_neg_half 5).const_mul 2
  have := h1.add h2
  simp only [mul_zero, add_zero] at this
  refine this.congr fun t => ?_
  unfold tailProf; ring

theorem two_mul_tailF_le {N : ℕ} {t : ℝ} (hN : 4 ≤ N) (ht1 : 1 ≤ t) (hN5 : t ^ 5 = N) :
    2 * N * tailF N (t ^ 3) ≤ tailProf t := by
  have ht0 : 0 < t := by linarith
  have hNpos : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
  have hrate := nat_mul_masterErr_le hN
  have hexp : Real.exp (4 + 4 * ((N : ℝ) * masterErr N)) ≤ Real.exp 244 * t ^ 1200 := by
    have hlog : Real.exp (240 * Real.log N) = t ^ 1200 := by
      rw [show (240 : ℝ) * Real.log N = ((240 : ℕ) : ℝ) * Real.log N by norm_num,
        Real.exp_nat_mul, Real.exp_log hNpos, ← hN5, ← pow_mul]
    rw [← hlog, ← Real.exp_add]
    apply Real.exp_le_exp.mpr; linarith
  have hR : -((t ^ 3) ^ 2 / (2 * N)) = -(t / 2) := by
    rw [← hN5]; field_simp; try ring
  unfold tailF tailProf
  rw [hR, ← hN5]
  have : 0 ≤ 2 * t ^ 5 * Real.exp (-(t / 2)) := by positivity
  calc 2 * t ^ 5 * (Real.exp (-(t / 2)) * (Real.exp (4 + 4 * ((t ^ 5 : ℝ) * masterErr N)) + 1))
      = 2 * t ^ 5 * Real.exp (-(t / 2)) * (Real.exp (4 + 4 * ((N : ℝ) * masterErr N)) + 1) := by
        rw [hN5]; ring
    _ ≤ _ := mul_le_mul_of_nonneg_left (by linarith) this

theorem final_le {N : ℕ} {t : ℝ} (hN : 24 ≤ N) (h5 : 5 ≤ t) (hN5 : t ^ 5 = N)
    (hδ : (8 * π + 1440 * π ^ 2) * t⁻¹ ≤ 1 / 2048) (hf : tailProf t ≤ 1 / 16) :
    24 * (t ^ 3 + 2) ≤ N ∧ 8 * winF N (t ^ 3) + 2 * N * tailF N (t ^ 3) ≤ 1 / 8 := by
  have ht1 : 1 ≤ t := by linarith
  have ht3 : 125 ≤ t ^ 3 := by nlinarith [sq_nonneg t]
  refine ⟨?_, ?_⟩
  · rw [← hN5]
    have : 25 * t ^ 3 ≤ t ^ 2 * t ^ 3 := mul_le_mul_of_nonneg_right (by nlinarith) (by positivity)
    nlinarith
  · have hd := delta_le ht1 hN5
    have hd0 : 0 ≤ stepErr N (t ^ 3 + 2) * (2 * t ^ 3 + 2) := by
      have := stepErr_nonneg N (t ^ 3 + 2); positivity
    have hd1 : stepErr N (t ^ 3 + 2) * (2 * t ^ 3 + 2) ≤ 1 / 2048 := hd.trans hδ
    have hw : winF N (t ^ 3) ≤ 1 / 1024 := by
      unfold winF
      have := Real.abs_exp_sub_one_le (x := stepErr N (t ^ 3 + 2) * (2 * t ^ 3 + 2))
        (by rw [abs_of_nonneg hd0]; linarith)
      rw [abs_of_nonneg hd0] at this
      linarith [le_abs_self (Real.exp (stepErr N (t ^ 3 + 2) * (2 * t ^ 3 + 2)) - 1)]
    have ht := two_mul_tailF_le (by omega) ht1 hN5
    linarith

/-- **vdV Lemma 2 (signed, `L¹`), proved.** -/
instance whiteheadInnerGaussianModel : WhiteheadInnerGaussianModel where
  model := by
    refine ⟨ampB, ?_⟩
    have htend : Filter.Tendsto (fun N : ℕ => (N : ℝ) ^ ((1 : ℝ) / 5)) Filter.atTop
        Filter.atTop :=
      (tendsto_rpow_atTop (by norm_num)).comp tendsto_natCast_atTop_atTop
    have e1 : ∀ᶠ t : ℝ in Filter.atTop, 5 ≤ t := Filter.eventually_ge_atTop 5
    have e2 : ∀ᶠ t : ℝ in Filter.atTop, (8 * π + 1440 * π ^ 2) * t⁻¹ ≤ 1 / 2048 := by
      have h := tendsto_inv_atTop_zero.const_mul (8 * π + 1440 * π ^ 2)
      rw [mul_zero] at h
      exact h.eventually (Iic_mem_nhds (by norm_num))
    have e3 : ∀ᶠ t : ℝ in Filter.atTop, tailProf t ≤ 1 / 16 :=
      tendsto_tailProf.eventually (Iic_mem_nhds (by norm_num))
    filter_upwards [htend.eventually (e1.and (e2.and e3)), Filter.eventually_ge_atTop 24]
      with N ⟨h5, hδ, hf⟩ hN
    have hN5 : ((N : ℝ) ^ ((1 : ℝ) / 5)) ^ 5 = N := by
      rw [← Real.rpow_natCast, ← Real.rpow_mul (Nat.cast_nonneg _)]; norm_num
    obtain ⟨hRN, hfin⟩ := final_le hN h5 hN5 hδ hf
    have hBpos : 0 < ampB N := by unfold ampB; positivity
    refine ⟨hBpos, ?_⟩
    have hsum := sum_bound hN (R := ((N : ℝ) ^ ((1 : ℝ) / 5)) ^ 3) (by positivity) hRN
    refine hsum.trans ?_
    have hN2 : (0 : ℝ) ≤ (N : ℝ) ^ 2 := by positivity
    have := mul_le_mul_of_nonneg_left (mul_le_mul_of_nonneg_left hfin hN2) hBpos.le
    linarith

end QOU.Knot.WhiteheadInner

namespace QOU.Knot.FigureEightVolume

/-- **vdV Lemma 4, unconditional** (the outer model follows from the inner instance). -/
example : WhiteheadInnerGaussianModel := inferInstance

end QOU.Knot.FigureEightVolume

