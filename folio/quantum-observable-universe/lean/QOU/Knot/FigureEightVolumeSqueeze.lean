/-
  E5d — the figure-eight volume-conjecture limit, machine-proved (the final
  squeeze of the saddle program, milestone qou-cpfn).

  Assembles, sorry-free:
    E1   (log Σ ≈ max log-term, ± log N)          [FigureEightVolumeSaddle]
    E5a  (log kashaevProd = 2·Riemann sum)        [FigureEightVolumeSaddle]
    E5c  (all-k uniform deviation ≤ E(N) → 0)     [Clausen: abs_deviation_le,
                                                    tendsto_master_error]
    E2/E3 (Cl₂ global min = −Cl₂(π/3) at 5π/3)    [Clausen + Saddle]
  into the Kashaev–Murakami–Murakami limit for the figure-eight knot:

    (2π/N) · log ⟨4₁⟩_N  →  2·Cl₂(π/3)  =  Vol(4₁)     (N → ∞)

  Upper envelope: log kashaev ≤ log N + log sup ≤ log N + 2·S(k₀), and the
  deviation bound + the Cl₂ minimum push (2π/N)·2·S(k₀) ≤ 2Cl₂(π/3) + 4E(N).
  Lower envelope: the single grid term at k* = ⌊5N/6⌋ (the saddle x = 5/6)
  gives (2π/N)·log kashaev ≥ 4F(k*π/N) − 4E(N) → 2Cl₂(π/3) by continuity of
  `clausen` at 5π/3 and Cl₂(5π/3) = −Cl₂(π/3).

  This DISCHARGES the `VolumeConjecture41` literature sorry (the Andersen–
  Hansen / Ohtsuki theorem, with the honest exact target `VOL_4_1 = 2·Cl₂(π/3)`
  after the qou-yf47 statement repair): `FigureEightVolumeLiterature.lean` now
  supplies the instance from `tendsto_log_kashaev_vol` with no sorry.

  Archimedean (ℝ).

  -- Ref: [kashaev1997] https://doi.org/10.1007/BF01239527
  -- Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
  -- Ref: [andersen-hansen2006] https://doi.org/10.1142/S0218216506004555
-/

import QOU.Knot.FigureEightVolumeSaddle

namespace QOU.Knot.FigureEightVolume

open Real

/-- The E5c-4 master deviation error
    `E(N) = |F(π/N)| + (π/N)|f(π/N)| + 7·(π/N)(|f(π/N)| + log 2)` — the
    k-independent bound of `abs_deviation_le`, packaged as a named function
    for the squeeze. -/
noncomputable def masterErr (N : ℕ) : ℝ :=
  |(-clausen (2 * (π / N)) / 2)|
    + (π / N) * |Real.log (2 * Real.sin (π / N))|
    + 7 * ((π / N) * (|Real.log (2 * Real.sin (π / N))| + Real.log 2))

theorem masterErr_nonneg (N : ℕ) : 0 ≤ masterErr N := by
  unfold masterErr
  have h1 : (0:ℝ) ≤ π / N := by positivity
  have h2 : (0:ℝ) ≤ Real.log 2 := Real.log_nonneg (by norm_num)
  have h3 := abs_nonneg (-clausen (2 * (π / N)) / 2)
  have h4 := abs_nonneg (Real.log (2 * Real.sin (π / N)))
  nlinarith [mul_nonneg h1 h4, mul_nonneg h1 (add_nonneg h4 h2)]

/-- E5c-5 in `masterErr` form. -/
theorem tendsto_masterErr :
    Filter.Tendsto masterErr Filter.atTop (nhds 0) :=
  tendsto_master_error

/-- E5c-4 in `masterErr` form. -/
theorem abs_deviation_le_masterErr {N k : ℕ} (hN : 4 ≤ N) (hk : 1 ≤ k)
    (hkN : k ≤ N - 1) :
    |(π / N) * (∑ j ∈ Finset.Icc 1 k,
          Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
        - (-clausen (2 * ((k : ℝ) * (π / N))) / 2)|
      ≤ masterErr N :=
  abs_deviation_le hN hk hkN

/-- The Kashaev product is strictly positive for `k < N` (each `4 sin²` factor
    is positive on the interior grid). -/
theorem kashaevProd_pos {N k : ℕ} (hkN : k < N) : 0 < kashaevProd N k := by
  have hpi := Real.pi_pos
  have hNpos : (0:ℝ) < N := by exact_mod_cast (by omega : 0 < N)
  have hfield : (N:ℝ) * (π / N) = π := by field_simp
  have hh : (0:ℝ) < π / N := by positivity
  rw [kashaevProd_eq_sin]
  have hprod : 0 < ∏ j ∈ Finset.Icc 1 k, Real.sin (π * j / N) := by
    apply Finset.prod_pos
    intro j hj
    obtain ⟨hj1, hjk⟩ := Finset.mem_Icc.mp hj
    have hj1' : (1:ℝ) ≤ (j:ℝ) := by exact_mod_cast hj1
    have hjN : (j:ℝ) < N := by exact_mod_cast lt_of_le_of_lt hjk hkN
    apply Real.sin_pos_of_pos_of_lt_pi
    · exact div_pos (by nlinarith) hNpos
    · have h1 : π * (j:ℝ) / N = (j:ℝ) * (π / N) := by ring
      rw [h1]
      calc (j:ℝ) * (π / N) < (N:ℝ) * (π / N) := by nlinarith
        _ = π := hfield
  positivity

/-- **The grid Clausen primitive never exceeds half the volume.** For any
    interior grid point `1 ≤ k ≤ N − 1`,
    `F(kπ/N) = −clausen(2kπ/N)/2 ≤ Cl₂(π/3)/2` — the E3 global-minimum bound
    transported through the series↔integral bridge. -/
theorem F_le_half_vol {N k : ℕ} (hk : 1 ≤ k) (hkN : k ≤ N - 1) :
    -clausen (2 * ((k : ℝ) * (π / N))) / 2
      ≤ QOU.Archimedean.Cl_2 (π / 3) / 2 := by
  have hpi := Real.pi_pos
  have hNpos : (0:ℝ) < N := by exact_mod_cast (by omega : 0 < N)
  have hh : (0:ℝ) < π / N := by positivity
  have hk' : (1:ℝ) ≤ (k:ℝ) := by exact_mod_cast hk
  have hkN' : (k:ℝ) ≤ (N:ℝ) - 1 := by
    have h : ((k:ℕ):ℝ) ≤ ((N-1:ℕ):ℝ) := by exact_mod_cast hkN
    rwa [Nat.cast_sub (by omega), Nat.cast_one] at h
  have hfield : (N:ℝ) * (π / N) = π := by field_simp
  have hmem : 2 * ((k:ℝ) * (π / N)) ∈ Set.Ioo (0:ℝ) (2 * π) := by
    constructor
    · nlinarith [mul_nonneg (by linarith : (0:ℝ) ≤ (k:ℝ) - 1) (le_of_lt hh)]
    · nlinarith [mul_le_mul_of_nonneg_right hkN' (le_of_lt hh), hfield, hh]
  have heq : clausen (2 * ((k:ℝ) * (π / N)))
      = QOU.Archimedean.Cl_2 (2 * ((k:ℝ) * (π / N))) := clausen_eq_series hmem
  have hmin := neg_Cl_2_pi_div_three_le (θ := 2 * ((k:ℝ) * (π / N)))
    ⟨le_of_lt hmem.1, le_of_lt hmem.2⟩
  rw [heq]
  linarith

/-- **E5d — the squeeze (sorry-free).** The scaled Kashaev log,
    `(2π/N)·log ⟨4₁⟩_N`, tends to `2·Cl₂(π/3) = Vol(4₁)`. (bean qou-f248) -/
theorem tendsto_two_pi_log_kashaev :
    Filter.Tendsto (fun N : ℕ => (2 * π / (N : ℝ)) * Real.log (kashaev N))
      Filter.atTop (nhds (2 * QOU.Archimedean.Cl_2 (π / 3))) := by
  have hpi := Real.pi_pos
  -- (a) (2π/N)·log N → 0
  have hlogN : Filter.Tendsto (fun N : ℕ => (2 * π / (N : ℝ)) * Real.log N)
      Filter.atTop (nhds 0) := by
    have h1 : Filter.Tendsto (fun x : ℝ => Real.log x / x)
        Filter.atTop (nhds 0) :=
      Real.isLittleO_log_id_atTop.tendsto_div_nhds_zero
    have h2 := Filter.Tendsto.const_mul (2 * π)
      (h1.comp tendsto_natCast_atTop_atTop)
    rw [mul_zero] at h2
    refine h2.congr (fun N => ?_)
    simp only [Function.comp_apply]
    ring
  -- (b) the moving saddle grid point 2·⌊5N/6⌋·(π/N) → 5π/3
  have hsaddlept : Filter.Tendsto
      (fun N : ℕ => 2 * ((↑(5 * N / 6) : ℝ) * (π / N)))
      Filter.atTop (nhds (5 * π / 3)) := by
    have h0 := tendsto_const_div_atTop_nhds_zero_nat (5 * π / 3)
    have hlow := Filter.Tendsto.const_sub (5 * π / 3) h0
    rw [sub_zero] at hlow
    refine tendsto_of_tendsto_of_tendsto_of_le_of_le' hlow tendsto_const_nhds
      ?_ ?_
    · -- 5π/3 − (5π/3)/N ≤ 2·k*·(π/N)
      filter_upwards [Filter.eventually_ge_atTop 1] with N hN1
      have hNpos : (0:ℝ) < N := by exact_mod_cast hN1
      have hN0 : (N:ℝ) ≠ 0 := ne_of_gt hNpos
      have hh : (0:ℝ) < π / N := by positivity
      have h6 : 5 * N ≤ 6 * (5 * N / 6) + 5 := by omega
      have h6' : (5:ℝ) * N ≤ 6 * (↑(5 * N / 6) : ℝ) + 5 := by exact_mod_cast h6
      have hmul := mul_le_mul_of_nonneg_right h6' (le_of_lt hh)
      have h5π : (5:ℝ) * ↑N * (π / ↑N) = 5 * π := by field_simp
      rw [h5π] at hmul
      have hdivN : (5:ℝ) * π / 3 / ↑N = 5 / 3 * (π / ↑N) := by ring
      rw [hdivN]
      linarith [hmul]
    · -- 2·k*·(π/N) ≤ 5π/3
      filter_upwards [Filter.eventually_ge_atTop 1] with N hN1
      have hNpos : (0:ℝ) < N := by exact_mod_cast hN1
      have hh : (0:ℝ) < π / N := by positivity
      have h6 : 6 * (5 * N / 6) ≤ 5 * N := by omega
      have h6' : (6:ℝ) * (↑(5 * N / 6) : ℝ) ≤ 5 * N := by exact_mod_cast h6
      have hfield : (N:ℝ) * (π / N) = π := by field_simp
      nlinarith [mul_le_mul_of_nonneg_right h6' (le_of_lt hh), hfield]
  -- (c) clausen at the moving grid point → clausen(5π/3) = −Cl₂(π/3)
  have hclsaddle : Filter.Tendsto
      (fun N : ℕ => clausen (2 * ((↑(5 * N / 6) : ℝ) * (π / N))))
      Filter.atTop (nhds (-QOU.Archimedean.Cl_2 (π / 3))) := by
    have hcomp := (continuous_clausen.tendsto (5 * π / 3)).comp hsaddlept
    have h53 : clausen (5 * π / 3) = -QOU.Archimedean.Cl_2 (π / 3) := by
      have heq : clausen (5 * π / 3) = QOU.Archimedean.Cl_2 (5 * π / 3) :=
        clausen_eq_series ⟨by linarith, by linarith⟩
      have h2 := Cl_2_two_pi_sub (π / 3)
      rw [show 2 * π - π / 3 = 5 * π / 3 by ring] at h2
      rw [heq, h2]
    rw [← h53]
    exact hcomp
  -- (d) the two envelopes and their common limit 2·Cl₂(π/3)
  have hglim : Filter.Tendsto
      (fun N : ℕ => 4 * (-clausen (2 * ((↑(5 * N / 6) : ℝ) * (π / N))) / 2)
        - 4 * masterErr N)
      Filter.atTop (nhds (2 * QOU.Archimedean.Cl_2 (π / 3))) := by
    have h1 := Filter.Tendsto.const_mul (4:ℝ) ((hclsaddle.neg).div_const 2)
    have h2 := Filter.Tendsto.const_mul (4:ℝ) tendsto_masterErr
    have h3 := h1.sub h2
    have hval : (4:ℝ) * (-(-QOU.Archimedean.Cl_2 (π / 3)) / 2) - 4 * 0
        = 2 * QOU.Archimedean.Cl_2 (π / 3) := by ring
    rw [hval] at h3
    exact h3
  have hhlim : Filter.Tendsto
      (fun N : ℕ => (2 * π / (N : ℝ)) * Real.log N
        + 2 * QOU.Archimedean.Cl_2 (π / 3) + 4 * masterErr N)
      Filter.atTop (nhds (2 * QOU.Archimedean.Cl_2 (π / 3))) := by
    have h : Filter.Tendsto
        (fun N : ℕ => ((2 * π / (N : ℝ)) * Real.log N
          + 2 * QOU.Archimedean.Cl_2 (π / 3)) + 4 * masterErr N)
        Filter.atTop
        (nhds (((0:ℝ) + 2 * QOU.Archimedean.Cl_2 (π / 3)) + 4 * 0)) :=
      (hlogN.add tendsto_const_nhds).add
        (Filter.Tendsto.const_mul (4:ℝ) tendsto_masterErr)
    have hval : ((0:ℝ) + 2 * QOU.Archimedean.Cl_2 (π / 3)) + 4 * 0
        = 2 * QOU.Archimedean.Cl_2 (π / 3) := by ring
    rw [hval] at h
    exact h
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le' hglim hhlim ?_ ?_
  · -- lower envelope: the single saddle grid term
    filter_upwards [Filter.eventually_ge_atTop 6] with N hN6
    set k := 5 * N / 6 with hkdef
    have hk1 : 1 ≤ k := by omega
    have hkN1 : k ≤ N - 1 := by omega
    have hkN : k < N := by omega
    have hN4 : 4 ≤ N := by omega
    have hNpos : (0:ℝ) < N := by exact_mod_cast (by omega : 0 < N)
    have h2πN : (0:ℝ) ≤ 2 * π / N := by positivity
    have hdev := abs_deviation_le_masterErr (N := N) (k := k) hN4 hk1 hkN1
    rw [abs_le] at hdev
    have hlogP := log_kashaevProd (N := N) (k := k) hkN
    have hpos := kashaevProd_pos (N := N) (k := k) hkN
    have hle : kashaevProd N k ≤ kashaev N := by
      have hmem : k ∈ Finset.range N := Finset.mem_range.mpr hkN
      exact Finset.single_le_sum (f := kashaevProd N)
        (fun i _ => kashaevProd_nonneg N i) hmem
    have hloglog : Real.log (kashaevProd N k) ≤ Real.log (kashaev N) :=
      Real.log_le_log hpos hle
    have hmul := mul_le_mul_of_nonneg_left hloglog h2πN
    rw [hlogP] at hmul
    calc 4 * (-clausen (2 * ((k:ℝ) * (π / N))) / 2) - 4 * masterErr N
        ≤ 4 * ((π / N) * (∑ j ∈ Finset.Icc 1 k,
            Real.log (2 * Real.sin ((j : ℝ) * (π / N))))) := by
          linarith [hdev.1]
      _ = (2 * π / N) * (2 * (∑ j ∈ Finset.Icc 1 k,
            Real.log (2 * Real.sin ((j : ℝ) * (π / N))))) := by ring
      _ ≤ (2 * π / N) * Real.log (kashaev N) := hmul
  · -- upper envelope: E1 + the sup term
    filter_upwards [Filter.eventually_ge_atTop 6] with N hN6
    have hN1 : 1 ≤ N := by omega
    have hN4 : 4 ≤ N := by omega
    have hNpos : (0:ℝ) < N := by exact_mod_cast (by omega : 0 < N)
    have h2πN : (0:ℝ) ≤ 2 * π / N := by positivity
    have hE1 := log_kashaev_le_log_add N hN1
    obtain ⟨k₀, hk₀mem, hEq⟩ := Finset.exists_mem_eq_sup'
      (Finset.nonempty_range_iff.mpr (show N ≠ 0 by omega)) (kashaevProd N)
    rw [hEq] at hE1
    have hk₀N : k₀ < N := Finset.mem_range.mp hk₀mem
    have hmulE1 := mul_le_mul_of_nonneg_left hE1 h2πN
    have hEnn := masterErr_nonneg N
    have hclpos := QOU.Knot.Cl_2_pi_div_three_pos
    rcases Nat.eq_zero_or_pos k₀ with hk₀0 | hk₀1
    · rw [hk₀0, kashaevProd_zero, Real.log_one] at hmulE1
      calc (2 * π / (N:ℝ)) * Real.log (kashaev N)
          ≤ (2 * π / N) * (Real.log N + 0) := hmulE1
        _ = (2 * π / N) * Real.log N := by ring
        _ ≤ (2 * π / N) * Real.log N + 2 * QOU.Archimedean.Cl_2 (π / 3)
              + 4 * masterErr N := by linarith
    · have hk₀N1 : k₀ ≤ N - 1 := by omega
      have hdev := abs_deviation_le_masterErr (N := N) (k := k₀) hN4 hk₀1 hk₀N1
      rw [abs_le] at hdev
      have hlogP := log_kashaevProd (N := N) (k := k₀) hk₀N
      rw [hlogP] at hmulE1
      have hF := F_le_half_vol (N := N) (k := k₀) hk₀1 hk₀N1
      calc (2 * π / (N:ℝ)) * Real.log (kashaev N)
          ≤ (2 * π / N) * (Real.log N + 2 * (∑ j ∈ Finset.Icc 1 k₀,
              Real.log (2 * Real.sin ((j : ℝ) * (π / N))))) := hmulE1
        _ = (2 * π / N) * Real.log N + 4 * ((π / N) * (∑ j ∈ Finset.Icc 1 k₀,
              Real.log (2 * Real.sin ((j : ℝ) * (π / N))))) := by ring
        _ ≤ (2 * π / N) * Real.log N + 2 * QOU.Archimedean.Cl_2 (π / 3)
              + 4 * masterErr N := by linarith [hdev.2, hF]

/-- **The figure-eight volume-conjecture limit, machine-proved (E5d).**
    `(2π/N)·log ⟨4₁⟩_N → VOL_4_1 = 2·Cl₂(π/3)` — the Kashaev–Murakami–
    Murakami statement for `4₁`, proved in the literature by Andersen–Hansen /
    Ohtsuki and here by the elementary Riemann-sum squeeze of the saddle
    program (E1 + E5a + E5c + E2/E3), with the exact transcendental target
    after the qou-yf47 statement repair. Discharges the
    `VolumeConjecture41` sorry. -/
theorem tendsto_log_kashaev_vol :
    Filter.Tendsto (fun N : ℕ => (2 * π / (N : ℝ)) * Real.log (kashaev N))
      Filter.atTop (nhds VOL_4_1) := by
  have h : VOL_4_1 = 2 * QOU.Archimedean.Cl_2 (π / 3) := rfl
  rw [h]
  exact tendsto_two_pi_log_kashaev

end QOU.Knot.FigureEightVolume
