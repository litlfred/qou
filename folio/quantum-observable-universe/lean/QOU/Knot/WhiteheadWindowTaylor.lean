import QOU.Knot.WhiteheadOuterGaussianWindow

/-!
# Whitehead window Taylor bound (vdV Lemma 2a, signed form) — bean qou-vy77

Second-order Taylor control of `log(2 sin θ)` on `[π/6, 5π/6]`.
-/

namespace QOU.Knot.WhiteheadInner

open Real

theorem sin_ge_half {t : ℝ} (h1 : π / 6 ≤ t) (h2 : t ≤ 5 * π / 6) : 1 / 2 ≤ Real.sin t := by
  have hpi := Real.pi_pos
  rcases le_total t (π / 2) with h | h
  · rw [← Real.sin_pi_div_six]
    exact Real.sin_le_sin_of_le_of_le_pi_div_two (by linarith) h h1
  · rw [← Real.sin_pi_sub, ← Real.sin_pi_div_six]
    exact Real.sin_le_sin_of_le_of_le_pi_div_two (by linarith) (by linarith) (by linarith)

/-- **Taylor brick.** On `[π/6, 5π/6]`,
`|log(2 sin θ) − log(2 sin c) − cot c · (θ − c)| ≤ 4 (θ − c)²`. -/
theorem log_two_sin_taylor {c θ : ℝ} (hc1 : π / 6 ≤ c) (hc2 : c ≤ 5 * π / 6)
    (hθ1 : π / 6 ≤ θ) (hθ2 : θ ≤ 5 * π / 6) :
    |Real.log (2 * Real.sin θ) - Real.log (2 * Real.sin c)
        - Real.cos c / Real.sin c * (θ - c)| ≤ 4 * (θ - c) ^ 2 := by
  set s := Set.uIcc c θ with hs
  have hsub : ∀ t ∈ s, π / 6 ≤ t ∧ t ≤ 5 * π / 6 := by
    intro t ht
    rcases Set.mem_uIcc.mp ht with h | h
    · exact ⟨by linarith [h.1], by linarith [h.2]⟩
    · exact ⟨by linarith [h.1], by linarith [h.2]⟩
  have hsc : 1 / 2 ≤ Real.sin c := sin_ge_half hc1 hc2
  set F : ℝ → ℝ := fun t => Real.log (2 * Real.sin t) - Real.cos c / Real.sin c * t with hF
  set F' : ℝ → ℝ := fun t => Real.cos t / Real.sin t - Real.cos c / Real.sin c with hF'
  have hderiv : ∀ t ∈ s, HasDerivWithinAt F (F' t) s t := by
    intro t ht
    have hst : 1 / 2 ≤ Real.sin t := sin_ge_half (hsub t ht).1 (hsub t ht).2
    have h1 : HasDerivAt (fun t => 2 * Real.sin t) (2 * Real.cos t) t :=
      (Real.hasDerivAt_sin t).const_mul 2
    have h2 := h1.log (by linarith)
    have h3 := h2.sub ((hasDerivAt_id t).const_mul (Real.cos c / Real.sin c))
    have heq : 2 * Real.cos t / (2 * Real.sin t) - Real.cos c / Real.sin c * 1 = F' t := by
      simp only [hF']; field_simp
    rw [heq] at h3
    exact h3.hasDerivWithinAt
  have hbound : ∀ t ∈ s, ‖F' t‖ ≤ 4 * |θ - c| := by
    intro t ht
    have hst : 1 / 2 ≤ Real.sin t := sin_ge_half (hsub t ht).1 (hsub t ht).2
    have hdist : |t - c| ≤ |θ - c| := by
      rcases Set.mem_uIcc.mp ht with h | h
      · rw [abs_of_nonneg (by linarith [h.1]), abs_of_nonneg (by linarith [h.1, h.2])]; linarith [h.2]
      · rw [abs_of_nonpos (by linarith [h.2]), abs_of_nonpos (by linarith [h.1, h.2])]; linarith [h.1]
    have hkey : F' t = Real.sin (c - t) / (Real.sin t * Real.sin c) := by
      simp only [hF']
      rw [Real.sin_sub]
      field_simp
    rw [Real.norm_eq_abs, hkey, abs_div, abs_of_pos (by positivity : 0 < Real.sin t * Real.sin c)]
    have hsn : |Real.sin (c - t)| ≤ |θ - c| := by
      refine le_trans Real.abs_sin_le_abs ?_
      rw [abs_sub_comm]; exact hdist
    have hprod : 1 / 4 ≤ Real.sin t * Real.sin c := by nlinarith
    rw [div_le_iff₀ (by linarith)]
    nlinarith [abs_nonneg (θ - c)]
  have hmain := Convex.norm_image_sub_le_of_norm_hasDerivWithin_le hderiv hbound
    (convex_uIcc c θ) (Set.left_mem_uIcc) (Set.right_mem_uIcc)
  rw [Real.norm_eq_abs, Real.norm_eq_abs] at hmain
  have hrw : F θ - F c = Real.log (2 * Real.sin θ) - Real.log (2 * Real.sin c)
        - Real.cos c / Real.sin c * (θ - c) := by simp only [hF]; ring
  rw [hrw] at hmain
  calc _ ≤ 4 * |θ - c| * |θ - c| := hmain
    _ = 4 * (θ - c) ^ 2 := by rw [mul_assoc, ← sq, sq_abs]


open QOU.Knot.FigureEightVolume

/-- The grid log-sine `g(t) = log(2 sin(tπ/N))`. -/
noncomputable def lg (N : ℕ) (t : ℝ) : ℝ := Real.log (2 * Real.sin (t * (π / N)))

/-- Partial sums `G(K) = Σ_{j=1}^K g(j)`. -/
noncomputable def Gs (N K : ℕ) : ℝ := ∑ j ∈ Finset.Icc 1 K, lg N (j : ℝ)

theorem Gs_succ (N K : ℕ) : Gs N (K + 1) = Gs N K + lg N ((K + 1 : ℕ) : ℝ) := by
  unfold Gs
  rw [Finset.sum_Icc_succ_top (by omega : 1 ≤ K + 1)]

theorem log_whiteheadTerm_Gs {N n k : ℕ} (h : k + n ≤ N - 1) :
    Real.log (whiteheadTerm N n k) = 2 * (Gs N (k + n) - Gs N k) - Gs N n := by
  rw [log_whiteheadTerm h]; rfl

/-- The signed quadratic form `Q(x,y) = x² + 2xy + 2y²`. -/
def Qf (x y : ℝ) : ℝ := x ^ 2 + 2 * x * y + 2 * y ^ 2

/-- The window deviation `D(n,k) = log S_{n,k} + (π/N) Q(n − N/2, k − N/4)`. -/
noncomputable def Dw (N n k : ℕ) : ℝ :=
  Real.log (whiteheadTerm N n k) + (π / N) * Qf ((n : ℝ) - N / 2) ((k : ℝ) - N / 4)

/-- The per-step error `ε = 2π/N + 40π²ρ²/N²`. -/
noncomputable def stepErr (N : ℕ) (ρ : ℝ) : ℝ := 2 * π / N + 40 * π ^ 2 * ρ ^ 2 / (N : ℝ) ^ 2

theorem two_log_two_sin_pi_div_four :
    2 * Real.log (2 * Real.sin (π / 4)) = Real.log (2 * Real.sin (π / 2)) := by
  rw [Real.sin_pi_div_four, Real.sin_pi_div_two, ← Real.log_rpow (by positivity)]
  congr 1
  rw [show (2 : ℝ) = ((2 : ℕ) : ℝ) by norm_num, Real.rpow_natCast]
  push_cast
  ring_nf
  rw [Real.sq_sqrt (by norm_num)]

theorem sin_three_pi_div_four : Real.sin (3 * π / 4) = Real.sin (π / 4) := by
  rw [show 3 * π / 4 = π - π / 4 by ring, Real.sin_pi_sub]

theorem cot_pi_div_four : Real.cos (π / 4) / Real.sin (π / 4) = 1 := by
  rw [Real.cos_pi_div_four, Real.sin_pi_div_four]
  have : (0 : ℝ) < √2 / 2 := by positivity
  field_simp

theorem cot_three_pi_div_four : Real.cos (3 * π / 4) / Real.sin (3 * π / 4) = -1 := by
  rw [sin_three_pi_div_four, show 3 * π / 4 = π - π / 4 by ring, Real.cos_pi_sub,
    Real.cos_pi_div_four, Real.sin_pi_div_four]
  have : (0 : ℝ) < √2 / 2 := by positivity
  field_simp

theorem lg_taylor {N : ℕ} {t c : ℝ} (hc1 : π / 6 ≤ c) (hc2 : c ≤ 5 * π / 6)
    (ht1 : π / 6 ≤ t * (π / N)) (ht2 : t * (π / N) ≤ 5 * π / 6) :
    |lg N t - Real.log (2 * Real.sin c) - Real.cos c / Real.sin c * (t * (π / N) - c)|
      ≤ 4 * (t * (π / N) - c) ^ 2 :=
  log_two_sin_taylor hc1 hc2 ht1 ht2

theorem rho_h_le {N : ℕ} (hN : 0 < N) {ρ : ℝ} (hρ : 24 * ρ ≤ N) :
    ρ * (π / N) ≤ π / 24 := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  rw [← mul_div_assoc, div_le_div_iff₀ hNpos (by norm_num)]
  nlinarith [Real.pi_pos]

/-- Common Taylor package at the three centres. -/
theorem taylor_quarter {N : ℕ} {t : ℝ} (ht1 : π / 6 ≤ t * (π / N)) (ht2 : t * (π / N) ≤ 5 * π / 6) :
    |lg N t - Real.log (2 * Real.sin (π / 4)) - (t * (π / N) - π / 4)|
      ≤ 4 * (t * (π / N) - π / 4) ^ 2 := by
  have hpi := Real.pi_pos
  have h := lg_taylor (N := N) (t := t) (c := π / 4) (by linarith) (by linarith) ht1 ht2
  rwa [cot_pi_div_four, one_mul] at h

theorem taylor_three_quarter {N : ℕ} {t : ℝ} (ht1 : π / 6 ≤ t * (π / N))
    (ht2 : t * (π / N) ≤ 5 * π / 6) :
    |lg N t - Real.log (2 * Real.sin (π / 4)) + (t * (π / N) - 3 * π / 4)|
      ≤ 4 * (t * (π / N) - 3 * π / 4) ^ 2 := by
  have hpi := Real.pi_pos
  have h := lg_taylor (N := N) (t := t) (c := 3 * π / 4) (by linarith) (by linarith) ht1 ht2
  rw [cot_three_pi_div_four, sin_three_pi_div_four] at h
  have he : lg N t - Real.log (2 * Real.sin (π / 4)) - -1 * (t * (π / N) - 3 * π / 4)
      = lg N t - Real.log (2 * Real.sin (π / 4)) + (t * (π / N) - 3 * π / 4) := by ring
  rwa [he] at h

theorem taylor_half {N : ℕ} {t : ℝ} (ht1 : π / 6 ≤ t * (π / N)) (ht2 : t * (π / N) ≤ 5 * π / 6) :
    |lg N t - Real.log (2 * Real.sin (π / 2))| ≤ 4 * (t * (π / N) - π / 2) ^ 2 := by
  have hpi := Real.pi_pos
  have h := lg_taylor (N := N) (t := t) (c := π / 2) (by linarith) (by linarith) ht1 ht2
  rwa [Real.cos_pi_div_two, zero_div, zero_mul, sub_zero] at h

/-- **`k`-step brick.** One step in `k` changes `D` by at most `ε = 2π/N + 40π²ρ²/N²`
on the window `|x|, |y| ≤ ρ − 1`, `24ρ ≤ N`. -/
theorem Dw_kstep {N n k : ℕ} {ρ : ℝ} (hN : 0 < N) (hρ : 24 * ρ ≤ N)
    (hx : |(n : ℝ) - N / 2| ≤ ρ - 1) (hy : |(k : ℝ) - N / 4| ≤ ρ - 1) :
    |Dw N n (k + 1) - Dw N n k| ≤ stepErr N ρ := by
  have hpi := Real.pi_pos
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  set h : ℝ := π / N with hh
  have hhpos : 0 < h := by positivity
  have hNh : (N : ℝ) * h = π := by rw [hh]; field_simp
  have hρh := rho_h_le hN hρ
  rw [← hh] at hρh
  set x : ℝ := (n : ℝ) - N / 2 with hxdef
  set y : ℝ := (k : ℝ) - N / 4 with hydef
  obtain ⟨hx1, hx2⟩ := abs_le.mp hx
  obtain ⟨hy1, hy2⟩ := abs_le.mp hy
  have hρ1 : 1 ≤ ρ := by linarith
  -- grid validity
  have hvalid : k + 1 + n ≤ N - 1 := by
    have hr : ((k + 1 + n + 1 : ℕ) : ℝ) ≤ (N : ℝ) := by
      push_cast; nlinarith
    have : k + 1 + n + 1 ≤ N := by exact_mod_cast hr
    omega
  have hL1 := log_whiteheadTerm_Gs (N := N) (n := n) (k := k + 1) hvalid
  have hL0 := log_whiteheadTerm_Gs (N := N) (n := n) (k := k) (by omega)
  have hG1 : Gs N (k + 1 + n) = Gs N (k + n) + lg N ((k + n + 1 : ℕ) : ℝ) := by
    rw [show k + 1 + n = (k + n) + 1 by ring, Gs_succ]
  have hG2 := Gs_succ N k
  -- angles
  have hθ1 : ((k + 1 : ℕ) : ℝ) * h = π / 4 + (y + 1) * h := by
    push_cast; rw [hydef]; linear_combination hNh / 4
  have hθ3 : ((k + n + 1 : ℕ) : ℝ) * h = 3 * π / 4 + (x + y + 1) * h := by
    push_cast; rw [hydef, hxdef]; linear_combination 3 * hNh / 4
  have hb1 : |(y + 1) * h| ≤ π / 24 := by
    rw [abs_mul, abs_of_pos hhpos]
    have : |y + 1| ≤ ρ := by rw [abs_le]; constructor <;> linarith
    have := mul_le_mul_of_nonneg_right this hhpos.le
    linarith
  have hb3 : |(x + y + 1) * h| ≤ π / 12 := by
    rw [abs_mul, abs_of_pos hhpos]
    have : |x + y + 1| ≤ 2 * ρ := by rw [abs_le]; constructor <;> linarith
    have := mul_le_mul_of_nonneg_right this hhpos.le
    linarith
  obtain ⟨hb1a, hb1b⟩ := abs_le.mp hb1
  obtain ⟨hb3a, hb3b⟩ := abs_le.mp hb3
  have hT1 := taylor_quarter (N := N) (t := ((k + 1 : ℕ) : ℝ))
    (by rw [← hh, hθ1]; linarith) (by rw [← hh, hθ1]; linarith)
  have hT3 := taylor_three_quarter (N := N) (t := ((k + n + 1 : ℕ) : ℝ))
    (by rw [← hh, hθ3]; linarith) (by rw [← hh, hθ3]; linarith)
  rw [← hh, hθ1] at hT1
  rw [← hh, hθ3] at hT3
  set L := Real.log (2 * Real.sin (π / 4))
  set e1 := lg N ((k + 1 : ℕ) : ℝ) - L - (π / 4 + (y + 1) * h - π / 4) with he1
  set e3 := lg N ((k + n + 1 : ℕ) : ℝ) - L + (3 * π / 4 + (x + y + 1) * h - 3 * π / 4) with he3
  have hdiff : Dw N n (k + 1) - Dw N n k = -2 * h + 2 * e3 - 2 * e1 := by
    unfold Dw
    rw [hL1, hL0, hG1, hG2, ← hh]
    have hy1' : ((k + 1 : ℕ) : ℝ) - N / 4 = y + 1 := by push_cast; rw [hydef]; ring
    rw [hy1', ← hxdef, ← hydef]
    simp only [Qf, he1, he3]
    ring
  rw [hdiff]
  have hq1 : (π / 4 + (y + 1) * h - π / 4) ^ 2 ≤ ρ ^ 2 * h ^ 2 := by
    have : |y + 1| ≤ ρ := by rw [abs_le]; constructor <;> linarith
    have h2 : (y + 1) ^ 2 ≤ ρ ^ 2 := by
      rw [← sq_abs]; exact pow_le_pow_left₀ (abs_nonneg _) this 2
    rw [show (π / 4 + (y + 1) * h - π / 4) ^ 2 = (y + 1) ^ 2 * h ^ 2 by ring]
    exact mul_le_mul_of_nonneg_right h2 (sq_nonneg h)
  have hq3 : (3 * π / 4 + (x + y + 1) * h - 3 * π / 4) ^ 2 ≤ 4 * ρ ^ 2 * h ^ 2 := by
    have : |x + y + 1| ≤ 2 * ρ := by rw [abs_le]; constructor <;> linarith
    have h2 : (x + y + 1) ^ 2 ≤ (2 * ρ) ^ 2 := by
      rw [← sq_abs]; exact pow_le_pow_left₀ (abs_nonneg _) this 2
    rw [show (3 * π / 4 + (x + y + 1) * h - 3 * π / 4) ^ 2 = (x + y + 1) ^ 2 * h ^ 2 by ring]
    have := mul_le_mul_of_nonneg_right h2 (sq_nonneg h)
    linarith
  have hse : stepErr N ρ = 2 * h + 40 * ρ ^ 2 * h ^ 2 := by
    unfold stepErr; rw [hh]; field_simp
  rw [hse]
  calc |-2 * h + 2 * e3 - 2 * e1| ≤ |-2 * h| + |2 * e3| + |2 * e1| := by
        have := abs_sub (-2 * h + 2 * e3) (2 * e1)
        have := abs_add_le (-2 * h) (2 * e3)
        linarith
    _ = 2 * h + 2 * |e3| + 2 * |e1| := by
        rw [abs_mul, abs_mul, abs_mul, abs_of_pos hhpos]; norm_num
    _ ≤ 2 * h + 40 * ρ ^ 2 * h ^ 2 := by linarith

/-- **`n`-step brick.** One step in `n` changes `D` by at most `ε`. -/
theorem Dw_nstep {N n k : ℕ} {ρ : ℝ} (hN : 0 < N) (hρ : 24 * ρ ≤ N)
    (hx : |(n : ℝ) - N / 2| ≤ ρ - 1) (hy : |(k : ℝ) - N / 4| ≤ ρ - 1) :
    |Dw N (n + 1) k - Dw N n k| ≤ stepErr N ρ := by
  have hpi := Real.pi_pos
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  set h : ℝ := π / N with hh
  have hhpos : 0 < h := by positivity
  have hNh : (N : ℝ) * h = π := by rw [hh]; field_simp
  have hρh := rho_h_le hN hρ
  rw [← hh] at hρh
  set x : ℝ := (n : ℝ) - N / 2 with hxdef
  set y : ℝ := (k : ℝ) - N / 4 with hydef
  obtain ⟨hx1, hx2⟩ := abs_le.mp hx
  obtain ⟨hy1, hy2⟩ := abs_le.mp hy
  have hρ1 : 1 ≤ ρ := by linarith
  have hvalid : k + (n + 1) ≤ N - 1 := by
    have hr : ((k + (n + 1) + 1 : ℕ) : ℝ) ≤ (N : ℝ) := by
      push_cast; nlinarith
    have : k + (n + 1) + 1 ≤ N := by exact_mod_cast hr
    omega
  have hL1 := log_whiteheadTerm_Gs (N := N) (n := n + 1) (k := k) hvalid
  have hL0 := log_whiteheadTerm_Gs (N := N) (n := n) (k := k) (by omega)
  have hG1 : Gs N (k + (n + 1)) = Gs N (k + n) + lg N ((k + n + 1 : ℕ) : ℝ) := by
    rw [show k + (n + 1) = (k + n) + 1 by ring, Gs_succ]
  have hG2 := Gs_succ N n
  have hθ2 : ((n + 1 : ℕ) : ℝ) * h = π / 2 + (x + 1) * h := by
    push_cast; rw [hxdef]; linear_combination hNh / 2
  have hθ3 : ((k + n + 1 : ℕ) : ℝ) * h = 3 * π / 4 + (x + y + 1) * h := by
    push_cast; rw [hydef, hxdef]; linear_combination 3 * hNh / 4
  have hb2 : |(x + 1) * h| ≤ π / 24 := by
    rw [abs_mul, abs_of_pos hhpos]
    have : |x + 1| ≤ ρ := by rw [abs_le]; constructor <;> linarith
    have := mul_le_mul_of_nonneg_right this hhpos.le
    linarith
  have hb3 : |(x + y + 1) * h| ≤ π / 12 := by
    rw [abs_mul, abs_of_pos hhpos]
    have : |x + y + 1| ≤ 2 * ρ := by rw [abs_le]; constructor <;> linarith
    have := mul_le_mul_of_nonneg_right this hhpos.le
    linarith
  obtain ⟨hb2a, hb2b⟩ := abs_le.mp hb2
  obtain ⟨hb3a, hb3b⟩ := abs_le.mp hb3
  have hT2 := taylor_half (N := N) (t := ((n + 1 : ℕ) : ℝ))
    (by rw [← hh, hθ2]; linarith) (by rw [← hh, hθ2]; linarith)
  have hT3 := taylor_three_quarter (N := N) (t := ((k + n + 1 : ℕ) : ℝ))
    (by rw [← hh, hθ3]; linarith) (by rw [← hh, hθ3]; linarith)
  rw [← hh, hθ2] at hT2
  rw [← hh, hθ3] at hT3
  rw [← two_log_two_sin_pi_div_four] at hT2
  set L := Real.log (2 * Real.sin (π / 4))
  set e2 := lg N ((n + 1 : ℕ) : ℝ) - 2 * L with he2
  set e3 := lg N ((k + n + 1 : ℕ) : ℝ) - L + (3 * π / 4 + (x + y + 1) * h - 3 * π / 4) with he3
  have hdiff : Dw N (n + 1) k - Dw N n k = -h + 2 * e3 - e2 := by
    unfold Dw
    rw [hL1, hL0, hG1, hG2, ← hh]
    have hx1' : ((n + 1 : ℕ) : ℝ) - N / 2 = x + 1 := by push_cast; rw [hxdef]; ring
    rw [hx1', ← hxdef, ← hydef]
    simp only [Qf, he2, he3]
    ring
  rw [hdiff]
  have hq2 : (π / 2 + (x + 1) * h - π / 2) ^ 2 ≤ ρ ^ 2 * h ^ 2 := by
    have : |x + 1| ≤ ρ := by rw [abs_le]; constructor <;> linarith
    have h2 : (x + 1) ^ 2 ≤ ρ ^ 2 := by
      rw [← sq_abs]; exact pow_le_pow_left₀ (abs_nonneg _) this 2
    rw [show (π / 2 + (x + 1) * h - π / 2) ^ 2 = (x + 1) ^ 2 * h ^ 2 by ring]
    exact mul_le_mul_of_nonneg_right h2 (sq_nonneg h)
  have hq3 : (3 * π / 4 + (x + y + 1) * h - 3 * π / 4) ^ 2 ≤ 4 * ρ ^ 2 * h ^ 2 := by
    have : |x + y + 1| ≤ 2 * ρ := by rw [abs_le]; constructor <;> linarith
    have h2 : (x + y + 1) ^ 2 ≤ (2 * ρ) ^ 2 := by
      rw [← sq_abs]; exact pow_le_pow_left₀ (abs_nonneg _) this 2
    rw [show (3 * π / 4 + (x + y + 1) * h - 3 * π / 4) ^ 2 = (x + y + 1) ^ 2 * h ^ 2 by ring]
    have := mul_le_mul_of_nonneg_right h2 (sq_nonneg h)
    linarith
  have hse : stepErr N ρ = 2 * h + 40 * ρ ^ 2 * h ^ 2 := by
    unfold stepErr; rw [hh]; field_simp
  rw [hse]
  have hρh2 : 0 ≤ ρ ^ 2 * h ^ 2 := by positivity
  calc |-h + 2 * e3 - e2| ≤ |-h| + |2 * e3| + |e2| := by
        have := abs_sub (-h + 2 * e3) e2
        have := abs_add_le (-h) (2 * e3)
        linarith
    _ = h + 2 * |e3| + |e2| := by
        rw [abs_mul, abs_neg, abs_of_pos hhpos]; norm_num
    _ ≤ 2 * h + 40 * ρ ^ 2 * h ^ 2 := by linarith

theorem abs_sub_le_steps_of_le (f : ℕ → ℝ) (a : ℕ) (ε : ℝ) :
    ∀ d : ℕ, (∀ i, a ≤ i → i < a + d → |f (i + 1) - f i| ≤ ε) → |f (a + d) - f a| ≤ ε * d := by
  intro d
  induction d with
  | zero => intro _; simp
  | succ d ih =>
    intro hs
    have h1 := ih (fun i hi1 hi2 => hs i hi1 (by omega))
    have h2 := hs (a + d) (by omega) (by omega)
    have htri : |f (a + (d + 1)) - f a| ≤ |f (a + d + 1) - f (a + d)| + |f (a + d) - f a| := by
      rw [show a + (d + 1) = a + d + 1 by ring]
      exact abs_sub_le _ _ _
    push_cast
    linarith

/-- **Telescoping brick.** -/
theorem abs_sub_le_steps (f : ℕ → ℝ) (a b : ℕ) (ε : ℝ)
    (hs : ∀ i, min a b ≤ i → i < max a b → |f (i + 1) - f i| ≤ ε) :
    |f b - f a| ≤ ε * |(b : ℝ) - a| := by
  rcases le_total a b with hab | hab
  · obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_le hab
    have := abs_sub_le_steps_of_le f a ε d
      (fun i h1 h2 => hs i (by rw [min_eq_left hab]; exact h1) (by rw [max_eq_right hab]; exact h2))
    push_cast
    rwa [show (a : ℝ) + d - a = d by ring, abs_of_nonneg (Nat.cast_nonneg (α := ℝ) d)]
  · obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_le hab
    have := abs_sub_le_steps_of_le f b ε d
      (fun i h1 h2 => hs i (by rw [min_eq_right hab]; exact h1) (by rw [max_eq_left hab]; exact h2))
    rw [abs_sub_comm]
    push_cast
    rwa [show (b : ℝ) - (b + d) = -d by ring, abs_neg, abs_of_nonneg (Nat.cast_nonneg (α := ℝ) d)]

theorem abs_div_four_sub_le (N : ℕ) : |((N / 4 : ℕ) : ℝ) - N / 4| ≤ 1 := by
  have h1 : (N / 4) * 4 ≤ N := Nat.div_mul_le_self N 4
  have h2 : N < (N / 4 + 1) * 4 := by omega
  have h1' : ((N / 4 : ℕ) : ℝ) * 4 ≤ N := by exact_mod_cast h1
  have h2' : (N : ℝ) < (((N / 4 : ℕ) : ℝ) + 1) * 4 := by exact_mod_cast h2
  rw [abs_le]; constructor <;> linarith

theorem abs_div_two_sub_le (N : ℕ) : |((N / 2 : ℕ) : ℝ) - N / 2| ≤ 1 := by
  have h1 : (N / 2) * 2 ≤ N := Nat.div_mul_le_self N 2
  have h2 : N < (N / 2 + 1) * 2 := by omega
  have h1' : ((N / 2 : ℕ) : ℝ) * 2 ≤ N := by exact_mod_cast h1
  have h2' : (N : ℝ) < (((N / 2 : ℕ) : ℝ) + 1) * 2 := by exact_mod_cast h2
  rw [abs_le]; constructor <;> linarith

theorem stepErr_nonneg (N : ℕ) (ρ : ℝ) : 0 ≤ stepErr N ρ := by
  unfold stepErr; have := Real.pi_pos; positivity

/-- Points between `a` and `b` stay within `max(|a−c|,|b−c|)` of a centre `c`. -/
theorem abs_between_le {a b i : ℕ} {c M : ℝ} (ha : |(a : ℝ) - c| ≤ M) (hb : |(b : ℝ) - c| ≤ M)
    (h1 : min a b ≤ i) (h2 : i ≤ max a b) : |(i : ℝ) - c| ≤ M := by
  have h1' : ((min a b : ℕ) : ℝ) ≤ i := by exact_mod_cast h1
  have h2' : (i : ℝ) ≤ ((max a b : ℕ) : ℝ) := by exact_mod_cast h2
  push_cast at h1' h2'
  obtain ⟨ha1, ha2⟩ := abs_le.mp ha
  obtain ⟨hb1, hb2⟩ := abs_le.mp hb
  rw [abs_le]
  constructor
  · rcases le_total (a : ℝ) b with h | h
    · rw [min_eq_left h] at h1'; linarith
    · rw [min_eq_right h] at h1'; linarith
  · rcases le_total (a : ℝ) b with h | h
    · rw [max_eq_right h] at h2'; linarith
    · rw [max_eq_left h] at h2'; linarith

/-- **Window brick (vdV Lemma 2a, signed, quantitative).**  On the window
`|n − N/2| ≤ R`, `|k − N/4| ≤ R` with `24(R+2) ≤ N`,
`|D(n,k) − D(⌊N/2⌋,⌊N/4⌋)| ≤ (2R+2)·(2π/N + 40π²(R+2)²/N²)`. -/
theorem Dw_window {N n k : ℕ} {R : ℝ} (hN : 0 < N) (hR : 0 ≤ R) (hRN : 24 * (R + 2) ≤ N)
    (hx : |(n : ℝ) - N / 2| ≤ R) (hy : |(k : ℝ) - N / 4| ≤ R) :
    |Dw N n k - Dw N (N / 2) (N / 4)| ≤ stepErr N (R + 2) * (2 * R + 2) := by
  have hε := stepErr_nonneg N (R + 2)
  have hk0 := abs_div_four_sub_le N
  have hn0 := abs_div_two_sub_le N
  -- k-leg at row n
  have hK : |Dw N n k - Dw N n (N / 4)| ≤ stepErr N (R + 2) * |(k : ℝ) - ((N / 4 : ℕ) : ℝ)| := by
    refine abs_sub_le_steps (fun i => Dw N n i) (N / 4) k _ (fun i h1 h2 => ?_)
    refine Dw_kstep hN hRN (by linarith) ?_
    exact abs_between_le (by linarith) (by linarith) h1 h2.le
  -- n-leg at column ⌊N/4⌋
  have hNl : |Dw N n (N / 4) - Dw N (N / 2) (N / 4)|
      ≤ stepErr N (R + 2) * |(n : ℝ) - ((N / 2 : ℕ) : ℝ)| := by
    refine abs_sub_le_steps (fun i => Dw N i (N / 4)) (N / 2) n _ (fun i h1 h2 => ?_)
    refine Dw_nstep hN hRN ?_ (by linarith)
    exact abs_between_le (by linarith) (by linarith) h1 h2.le
  have hdk : |(k : ℝ) - ((N / 4 : ℕ) : ℝ)| ≤ R + 1 := by
    calc |(k : ℝ) - ((N / 4 : ℕ) : ℝ)| = |((k : ℝ) - N / 4) - (((N / 4 : ℕ) : ℝ) - N / 4)| := by
          congr 1; ring
      _ ≤ |(k : ℝ) - N / 4| + |((N / 4 : ℕ) : ℝ) - N / 4| := abs_sub _ _
      _ ≤ R + 1 := by linarith
  have hdn : |(n : ℝ) - ((N / 2 : ℕ) : ℝ)| ≤ R + 1 := by
    calc |(n : ℝ) - ((N / 2 : ℕ) : ℝ)| = |((n : ℝ) - N / 2) - (((N / 2 : ℕ) : ℝ) - N / 2)| := by
          congr 1; ring
      _ ≤ |(n : ℝ) - N / 2| + |((N / 2 : ℕ) : ℝ) - N / 2| := abs_sub _ _
      _ ≤ R + 1 := by linarith
  have h1 := mul_le_mul_of_nonneg_left hdk hε
  have h2 := mul_le_mul_of_nonneg_left hdn hε
  calc |Dw N n k - Dw N (N / 2) (N / 4)|
      ≤ |Dw N n k - Dw N n (N / 4)| + |Dw N n (N / 4) - Dw N (N / 2) (N / 4)| := abs_sub_le _ _ _
    _ ≤ stepErr N (R + 2) * (R + 1) + stepErr N (R + 2) * (R + 1) := by linarith
    _ = stepErr N (R + 2) * (2 * R + 2) := by ring

end QOU.Knot.WhiteheadInner
