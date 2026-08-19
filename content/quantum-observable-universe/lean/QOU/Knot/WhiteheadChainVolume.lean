/-
# Whitehead-chain volume — bricks W3–W4: positive-sum carrier, log identity,
# deviation (milestone qou-k49o)

Third volume-conjecture instance, following the 4₁ (E-bricks) and Borromean
(B-bricks) squeezes.  Carrier provenance and epistemic status:

* **Source.** van der Veen, "Proof of the volume conjecture for Whitehead
  chains", arXiv:math/0611181 v2 (`library/arxiv-math-0611181v2/0611181v2.pdf`), Lemma 1: for the
  Whitehead chain `W_{a,b,c,d}` with `b ≥ 2` belts at the Kashaev point
  `t = e^{2πi/N}`, the colored Jones vanishes for even `N`, and for
  `N = 2M+1`,

      J_N(W_{a,b,c,d}) = φ_N · N^b · χ_{N,M}^{4a−c+d} · (Σ_{k=0}^{M} S_{M,k})^{c+d},
      S_{M,k} = ∏_{j=1}^{M} 2 sin²((k+j)π/N) / sin(jπ/N),

  with `φ_N, χ_{N,M}` unimodular.  Hence the EXACT modulus identity
  `|J_N| = N^b (Σ_k S_{M,k})^{c+d}` — a phase-free positive sum (unlike the
  `b = 1` Whitehead link proper, whose outer phase sum needs vdV's Lemma 4
  Gaussian analysis and is NOT treated here).  Transcription verified by the
  4-anchor battery in `computations/whitehead_vdv_lemma1.py`
  (`whitehead-vdv-lemma1.witness.json`): generic-t tangle form ↔ Lemma 1
  closed form to 3.5e-19; Borromean specialization ↔ the corpus's
  independent GL2011/Habiro transcription to 1e-41; rate → 4G; positivity /
  log-identity / vanishing / modulus checks.

* **What is formalized here** (sorry-free): the positive sum
  `P_M = Σ_{k=0}^{M} S_{M,k}` as `whiteheadKashaev`, its positivity, the
  single-term floor, the exact log identity
  `log S_{M,k} = 2(s_{k+M} − s_k) − s_M` in the E4/E5 Riemann sums
  `s_m = Σ_{j≤m} log(2 sin(jπ/N))`, and the k-uniform deviation
  `|(π/N) log S_{M,k} − Ψ_N(k)| ≤ 5·masterErr N` against the Clausen
  primitive.  The identification of `P_M` with the diagrammatic invariant
  via Lemma 1 is the cited input (same epistemic tier as the Borromean
  carrier's GL2011/Habiro identification).
  -- Ref: [manuscript] docs/audits/2026-08-02-whitehead-chain-positive-sum-route.md

* **Target** (brick W5, separate): `(2π/(2M+1)) log P_M → 4·Cl₂(π/2) = 4G
  = 8Λ(π/4) = Vol(W_{a,2,1,0})` (volume by vdV's octahedral decomposition,
  his ref [10] = van der Veen's master thesis).

Indices are well-inside the grid: `j ∈ [k+1, k+M]` with `k ≤ M` gives
`j ≤ 2M = N − 1`, so every sine factor is strictly positive — no
vanishing-term analysis and no mirror-sign bookkeeping (simpler than the
Borromean carrier on both counts).
-/

import QOU.Knot.FigureEightVolumeSqueeze
import QOU.Knot.CatalanValueBounds

namespace QOU.Knot.FigureEightVolume

open Real

/-- Numerator of `S_{M,k}`: `∏_{j=k+1}^{k+M} (2 sin(jπ/N))²`. -/
noncomputable def whiteheadNum (N M k : ℕ) : ℝ :=
  ∏ j ∈ Finset.Icc (k + 1) (k + M), (2 * Real.sin ((j : ℝ) * (π / N))) ^ 2

/-- Denominator of `S_{M,k}`: `∏_{j=1}^{M} 2 sin(jπ/N)`. -/
noncomputable def whiteheadDen (N M : ℕ) : ℝ :=
  ∏ j ∈ Finset.Icc 1 M, (2 * Real.sin ((j : ℝ) * (π / N)))

/-- One term of the Whitehead-chain Kashaev sum:
    `S_{M,k} = ∏_{j=1}^{M} 2 sin²((k+j)π/N)/sin(jπ/N)` (vdV Lemma 1),
    written as the reindexed quotient of `2 sin` products. -/
noncomputable def whiteheadTerm (N M k : ℕ) : ℝ :=
  whiteheadNum N M k / whiteheadDen N M

/-- The Whitehead-chain positive sum `P_M = Σ_{k=0}^{M} S_{M,k}` at
    `N = 2M+1` (the `N` parameter is kept general; the chain instance takes
    `N = 2M+1`).  By vdV Lemma 1 the invariant modulus is
    `|J_N(W_{a,b,c,d})| = N^b · P_M^{c+d}` for `b ≥ 2`, `N = 2M+1`. -/
noncomputable def whiteheadKashaev (N M : ℕ) : ℝ :=
  ∑ k ∈ Finset.range (M + 1), whiteheadTerm N M k

/-- Interior grid sines are positive: `0 < sin(jπ/N)` for `1 ≤ j ≤ N−1`. -/
theorem sin_grid_pos {N j : ℕ} (hj1 : 1 ≤ j) (hjN : j ≤ N - 1) :
    0 < Real.sin ((j : ℝ) * (π / N)) := by
  have hN2 : 2 ≤ N := by omega
  have hpi := Real.pi_pos
  have hNpos : (0:ℝ) < N := by exact_mod_cast (by omega : 0 < N)
  have hj1' : (1:ℝ) ≤ (j:ℝ) := by exact_mod_cast hj1
  have hjN' : (j:ℝ) < (N:ℝ) := by exact_mod_cast (by omega : j < N)
  have hh : (0:ℝ) < π / N := by positivity
  have hfield : (N:ℝ) * (π / N) = π := by field_simp
  apply Real.sin_pos_of_pos_of_lt_pi
  · nlinarith
  · nlinarith

/-- The numerator is positive whenever the window stays inside the grid
    (`k + M ≤ N − 1`). -/
theorem whiteheadNum_pos {N M k : ℕ} (hkM : k + M ≤ N - 1) :
    0 < whiteheadNum N M k := by
  unfold whiteheadNum
  apply Finset.prod_pos
  intro j hj
  obtain ⟨hj1, hj2⟩ := Finset.mem_Icc.mp hj
  have hsin := sin_grid_pos (N := N) (j := j) (by omega) (by omega)
  positivity

/-- The denominator is positive for `M ≤ N − 1`. -/
theorem whiteheadDen_pos {N M : ℕ} (hM : M ≤ N - 1) :
    0 < whiteheadDen N M := by
  unfold whiteheadDen
  apply Finset.prod_pos
  intro j hj
  obtain ⟨hj1, hj2⟩ := Finset.mem_Icc.mp hj
  have hsin := sin_grid_pos (N := N) (j := j) hj1 (by omega)
  positivity

/-- Every term `S_{M,k}` with an in-grid window is strictly positive —
    no vanishing terms, no sign analysis (contrast the Borromean carrier). -/
theorem whiteheadTerm_pos {N M k : ℕ} (hkM : k + M ≤ N - 1) :
    0 < whiteheadTerm N M k :=
  div_pos (whiteheadNum_pos hkM) (whiteheadDen_pos (by omega))

/-- **The Whitehead-chain sum is positive** (`2M ≤ N − 1`, satisfied by the
    chain instance `N = 2M+1`) — `log` of it is well-defined, the floor the
    W5 squeeze stands on. -/
theorem whiteheadKashaev_pos {N M : ℕ} (h2M : 2 * M ≤ N - 1) :
    0 < whiteheadKashaev N M := by
  unfold whiteheadKashaev
  apply Finset.sum_pos
  · intro k hk
    have hk' := Finset.mem_range.mp hk
    exact whiteheadTerm_pos (by omega)
  · exact ⟨0, Finset.mem_range.mpr (by omega)⟩

/-- Single-term floor: each term bounds the sum below (the lower-envelope
    hook for the W5 squeeze). -/
theorem whiteheadTerm_le_whiteheadKashaev {N M k : ℕ} (h2M : 2 * M ≤ N - 1)
    (hk : k ∈ Finset.range (M + 1)) :
    whiteheadTerm N M k ≤ whiteheadKashaev N M := by
  unfold whiteheadKashaev
  apply Finset.single_le_sum (f := whiteheadTerm N M) _ hk
  intro i hi
  have hi' := Finset.mem_range.mp hi
  exact (whiteheadTerm_pos (by omega)).le

/-- **Whitehead brick W4a — the log identity (sorry-free, exact).**  With the
    E4/E5 Riemann sums `s_m = Σ_{j∈Icc 1 m} log(2 sin(jπ/N))`,

        log S_{M,k} = 2·(s_{k+M} − s_k) − s_M

    — the numerator window `(k, k+M]` splits off the prefix `[1, k]`, and the
    squared factors contribute the `2`. -/
theorem log_whiteheadTerm {N M k : ℕ} (hkM : k + M ≤ N - 1) :
    Real.log (whiteheadTerm N M k)
      = 2 * ((∑ j ∈ Finset.Icc 1 (k + M),
                Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
             - ∑ j ∈ Finset.Icc 1 k,
                Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
        - ∑ j ∈ Finset.Icc 1 M,
            Real.log (2 * Real.sin ((j : ℝ) * (π / N))) := by
  have hnum := whiteheadNum_pos (N := N) (M := M) (k := k) hkM
  have hden := whiteheadDen_pos (N := N) (M := M) (by omega)
  -- log of the quotient
  unfold whiteheadTerm
  rw [Real.log_div hnum.ne' hden.ne']
  -- numerator: log of a product of squares
  have hlognum : Real.log (whiteheadNum N M k)
      = 2 * ∑ j ∈ Finset.Icc (k + 1) (k + M),
          Real.log (2 * Real.sin ((j : ℝ) * (π / N))) := by
    unfold whiteheadNum
    rw [Real.log_prod]
    · rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro j hj
      obtain ⟨hj1, hj2⟩ := Finset.mem_Icc.mp hj
      have hsin := sin_grid_pos (N := N) (j := j) (by omega) (by omega)
      rw [Real.log_pow]
      push_cast
      ring
    · intro j hj
      obtain ⟨hj1, hj2⟩ := Finset.mem_Icc.mp hj
      have hsin := sin_grid_pos (N := N) (j := j) (by omega) (by omega)
      positivity
  -- denominator: log of a product
  have hlogden : Real.log (whiteheadDen N M)
      = ∑ j ∈ Finset.Icc 1 M,
          Real.log (2 * Real.sin ((j : ℝ) * (π / N))) := by
    unfold whiteheadDen
    rw [Real.log_prod]
    intro j hj
    obtain ⟨hj1, hj2⟩ := Finset.mem_Icc.mp hj
    have hsin := sin_grid_pos (N := N) (j := j) hj1 (by omega)
    positivity
  -- window split: Σ_{Icc (k+1) (k+M)} = Σ_{Icc 1 (k+M)} − Σ_{Icc 1 k}
  have hsplit : ∑ j ∈ Finset.Icc (k + 1) (k + M),
        Real.log (2 * Real.sin ((j : ℝ) * (π / N)))
      = (∑ j ∈ Finset.Icc 1 (k + M),
          Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
        - ∑ j ∈ Finset.Icc 1 k,
          Real.log (2 * Real.sin ((j : ℝ) * (π / N))) := by
    have hconsec := Finset.sum_Ioc_consecutive
      (f := fun j : ℕ => Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
      (Nat.zero_le k) (Nat.le_add_right k M)
    have h1 : Finset.Icc 1 (k + M) = Finset.Ioc 0 (k + M) := by
      exact Finset.Icc_succ_left_eq_Ioc 0 _
    have h2 : Finset.Icc 1 k = Finset.Ioc 0 k := by
      exact Finset.Icc_succ_left_eq_Ioc 0 _
    have h3 : Finset.Icc (k + 1) (k + M) = Finset.Ioc k (k + M) := by
      exact Finset.Icc_succ_left_eq_Ioc k _
    rw [h1, h2, h3]
    linarith [hconsec]
  rw [hlognum, hlogden, hsplit]

/-- **Whitehead brick W4b — the k-uniform deviation (sorry-free).**  For
    `1 ≤ k` and `k + M ≤ N − 1`, the scaled log-term deviates from the
    Clausen-primitive combination

        Ψ_N(k) = 2·(F((k+M)π/N) − F(kπ/N)) − F(Mπ/N),
        F(x) = −clausen(2x)/2

    by at most `5·masterErr N` — coefficient sum `2+2+1` of the E5c-4
    k-uniform bound applied at the indices `k+M`, `k`, `M`. -/
theorem abs_log_whiteheadTerm_deviation {N M k : ℕ} (hN : 4 ≤ N)
    (hM1 : 1 ≤ M) (hk1 : 1 ≤ k) (hkM : k + M ≤ N - 1) :
    |(π / N) * Real.log (whiteheadTerm N M k)
        - (2 * ((-clausen (2 * (((k : ℝ) + (M : ℝ)) * (π / N))) / 2)
                - (-clausen (2 * ((k : ℝ) * (π / N))) / 2))
           - (-clausen (2 * ((M : ℝ) * (π / N))) / 2))|
      ≤ 5 * masterErr N := by
  -- the three deviation instances
  have hA : |(π / N) * (∑ j ∈ Finset.Icc 1 (k + M),
        Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
      - (-clausen (2 * (((k : ℝ) + (M : ℝ)) * (π / N))) / 2)| ≤ masterErr N := by
    have h := abs_deviation_le_masterErr (N := N) (k := k + M) hN (by omega) hkM
    have hcast : (((k + M : ℕ) : ℝ)) = (k : ℝ) + (M : ℝ) := by push_cast; ring
    rwa [hcast] at h
  have hB : |(π / N) * (∑ j ∈ Finset.Icc 1 k,
        Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
      - (-clausen (2 * ((k : ℝ) * (π / N))) / 2)| ≤ masterErr N :=
    abs_deviation_le_masterErr (N := N) (k := k) hN hk1 (by omega)
  have hC : |(π / N) * (∑ j ∈ Finset.Icc 1 M,
        Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
      - (-clausen (2 * ((M : ℝ) * (π / N))) / 2)| ≤ masterErr N :=
    abs_deviation_le_masterErr (N := N) (k := M) hN hM1 (by omega)
  -- rewrite the scaled log via the W4a identity
  rw [log_whiteheadTerm hkM]
  rw [abs_le] at hA hB hC ⊢
  constructor <;> [skip; skip] <;>
    · obtain ⟨hA1, hA2⟩ := hA
      obtain ⟨hB1, hB2⟩ := hB
      obtain ⟨hC1, hC2⟩ := hC
      nlinarith [hA1, hA2, hB1, hB2, hC1, hC2]

/-! ## Brick W5a — the continuum functional, its max, and the grid ceiling -/

/-- The Whitehead-chain continuum functional in the half-angle variable
    `y = kπ/N`:  `WF(y) = 2·clausen(2y) − 2·clausen(2y + π)` — the limit of
    the scaled log-term `(2π/N)·log S_{M,k}` along `k/N → y/π`, using
    `2Mπ/N → π` and `clausen π = 0`.  Simpler than the Borromean functional
    (no duplication step). -/
noncomputable def whiteheadFunctional (y : ℝ) : ℝ :=
  2 * clausen (2 * y) - 2 * clausen (2 * y + π)

theorem continuous_whiteheadFunctional : Continuous whiteheadFunctional := by
  have h1 : Continuous fun y : ℝ => clausen (2 * y) :=
    continuous_clausen.comp (continuous_const.mul continuous_id)
  have h2 : Continuous fun y : ℝ => clausen (2 * y + π) :=
    continuous_clausen.comp ((continuous_const.mul continuous_id).add
      continuous_const)
  exact (continuous_const.mul h1).sub (continuous_const.mul h2)

theorem hasDerivAt_whiteheadFunctional {y : ℝ} (h1 : 0 < y) (h2 : y < π / 2) :
    HasDerivAt whiteheadFunctional
      (-4 * Real.log (2 * Real.sin y)
        + 4 * Real.log (2 * Real.sin (y + π / 2))) y := by
  have hpi := Real.pi_pos
  have hc1 : HasDerivAt (fun y : ℝ => clausen (2 * y))
      (-Real.log (2 * Real.sin (2 * y / 2)) * 2) y := by
    have hd := hasDerivAt_clausen (θ := 2 * y) (by linarith) (by linarith)
    have hlin : HasDerivAt (fun y : ℝ => 2 * y) 2 y := by
      simpa using (hasDerivAt_id y).const_mul 2
    exact hd.comp y hlin
  have hc2 : HasDerivAt (fun y : ℝ => clausen (2 * y + π))
      (-Real.log (2 * Real.sin ((2 * y + π) / 2)) * 2) y := by
    have hd := hasDerivAt_clausen (θ := 2 * y + π) (by linarith) (by linarith)
    have hlin : HasDerivAt (fun y : ℝ => 2 * y + π) 2 y := by
      simpa using ((hasDerivAt_id y).const_mul 2).add_const π
    exact hd.comp y hlin
  have hsum := (hc1.const_mul (2:ℝ)).sub (hc2.const_mul (2:ℝ))
  convert hsum using 1
  rw [show (2:ℝ) * y / 2 = y by ring,
    show ((2:ℝ) * y + π) / 2 = y + π / 2 by ring]
  ring

theorem whiteheadFunctional_zero : whiteheadFunctional 0 = 0 := by
  unfold whiteheadFunctional
  rw [mul_zero, clausen_zero, zero_add, clausen_pi]
  ring

theorem whiteheadFunctional_pi_div_two : whiteheadFunctional (π / 2) = 0 := by
  unfold whiteheadFunctional
  rw [show (2:ℝ) * (π / 2) = π by ring, clausen_pi,
    show π + π = 2 * π by ring, clausen_two_pi]
  ring

/-- The saddle value: `WF(π/4) = 4·Cl₂(π/2)` — series bridge + antisymmetry. -/
theorem whiteheadFunctional_quarter :
    whiteheadFunctional (π / 4) = 4 * QOU.Archimedean.Cl_2 (π / 2) := by
  have hpi := Real.pi_pos
  unfold whiteheadFunctional
  rw [show (2:ℝ) * (π / 4) = π / 2 by ring,
    show π / 2 + π = 3 * π / 2 by ring]
  have h12 : clausen (π / 2) = QOU.Archimedean.Cl_2 (π / 2) :=
    clausen_eq_series ⟨by linarith, by linarith⟩
  have h32 : clausen (3 * π / 2) = QOU.Archimedean.Cl_2 (3 * π / 2) :=
    clausen_eq_series ⟨by linarith, by linarith⟩
  have hanti := Cl_2_two_pi_sub (π / 2)
  rw [show 2 * π - π / 2 = 3 * π / 2 by ring] at hanti
  rw [h12, h32, hanti]
  ring

/-- **Whitehead brick W5a-max — the continuum max (sorry-free).**  On
    `[0, π/2]` the functional never exceeds its saddle value `4·Cl₂(π/2)`,
    attained at `y = π/4`: compactness gives a maximiser; the boundary
    values vanish while the saddle value is positive; the interior critical
    equation `2 sin(y + π/2) = 2 sin y` forces `cos y = sin y`, hence
    `cos 2y = 0` with `2y ∈ (0, π)`, hence `y = π/4`. -/
theorem whiteheadFunctional_le {y : ℝ} (hy : y ∈ Set.Icc 0 (π / 2)) :
    whiteheadFunctional y ≤ 4 * QOU.Archimedean.Cl_2 (π / 2) := by
  have hpi := Real.pi_pos
  obtain ⟨y₀, hy₀mem, hmax⟩ :=
    (isCompact_Icc (a := (0:ℝ)) (b := π / 2)).exists_isMaxOn
      (Set.nonempty_Icc.mpr (by linarith))
      continuous_whiteheadFunctional.continuousOn
  have hval : 4 * QOU.Archimedean.Cl_2 (π / 2) ≤ whiteheadFunctional y₀ := by
    have h := hmax (show (π / 4 : ℝ) ∈ Set.Icc 0 (π / 2) from
      ⟨by linarith, by linarith⟩)
    simp only [Set.mem_setOf_eq] at h
    rwa [whiteheadFunctional_quarter] at h
  have hpos := Cl_2_pi_div_two_pos
  have hne1 : y₀ ≠ 0 := by
    intro h
    rw [h, whiteheadFunctional_zero] at hval
    linarith
  have hne2 : y₀ ≠ π / 2 := by
    intro h
    rw [h, whiteheadFunctional_pi_div_two] at hval
    linarith
  have hint : y₀ ∈ Set.Ioo (0:ℝ) (π / 2) :=
    ⟨lt_of_le_of_ne hy₀mem.1 (Ne.symm hne1), lt_of_le_of_ne hy₀mem.2 hne2⟩
  have hloc : IsLocalMax whiteheadFunctional y₀ :=
    hmax.isLocalMax (Icc_mem_nhds hint.1 hint.2)
  have hd := hasDerivAt_whiteheadFunctional hint.1 hint.2
  have hzero : -4 * Real.log (2 * Real.sin y₀)
      + 4 * Real.log (2 * Real.sin (y₀ + π / 2)) = 0 := by
    rw [← hd.deriv]
    exact hloc.deriv_eq_zero
  have hsa : 0 < Real.sin y₀ :=
    Real.sin_pos_of_pos_of_lt_pi hint.1 (by linarith [hint.2])
  have hsb : 0 < Real.sin (y₀ + π / 2) :=
    Real.sin_pos_of_pos_of_lt_pi (by linarith [hint.1]) (by linarith [hint.2])
  have hexp : 2 * Real.sin y₀ = 2 * Real.sin (y₀ + π / 2) := by
    have h2 : Real.log (2 * Real.sin y₀)
        = Real.log (2 * Real.sin (y₀ + π / 2)) := by linarith [hzero]
    have hpos1 : (0:ℝ) < 2 * Real.sin y₀ := by linarith
    have hpos2 : (0:ℝ) < 2 * Real.sin (y₀ + π / 2) := by linarith
    calc 2 * Real.sin y₀
        = Real.exp (Real.log (2 * Real.sin y₀)) := (Real.exp_log hpos1).symm
      _ = Real.exp (Real.log (2 * Real.sin (y₀ + π / 2))) := by rw [h2]
      _ = 2 * Real.sin (y₀ + π / 2) := Real.exp_log hpos2
  have hcossin : Real.cos y₀ = Real.sin y₀ := by
    have hshift : Real.sin (y₀ + π / 2) = Real.cos y₀ := by
      rw [Real.sin_add, Real.sin_pi_div_two, Real.cos_pi_div_two]
      ring
    rw [hshift] at hexp
    linarith
  have hcos2 : Real.cos (2 * y₀) = 0 := by
    rw [Real.cos_two_mul']
    rw [hcossin]
    ring
  have hy4 : y₀ = π / 4 := by
    rcases Real.cos_eq_zero_iff.mp hcos2 with ⟨k, hk⟩
    have hklo : (0:ℝ) < ((2 * k + 1 : ℤ) : ℝ) := by
      have h1 : 0 < 2 * y₀ := by linarith [hint.1]
      rw [hk] at h1
      push_cast at h1 ⊢
      nlinarith
    have hkhi : ((2 * k + 1 : ℤ) : ℝ) < 2 := by
      have h1 : 2 * y₀ < π := by linarith [hint.2]
      rw [hk] at h1
      push_cast at h1 ⊢
      nlinarith
    have hk1 : (2 * k + 1 : ℤ) = 1 := by
      have hlo : (0:ℤ) < 2 * k + 1 := by exact_mod_cast hklo
      have hhi : (2 * k + 1 : ℤ) < 2 := by exact_mod_cast hkhi
      omega
    have hcast : (2 * (k:ℝ) + 1) = 1 := by exact_mod_cast hk1
    have h2y : 2 * y₀ = π / 2 := by
      rw [hk, hcast]; ring
    linarith
  have hfin := hmax hy
  simp only [Set.mem_setOf_eq] at hfin
  calc whiteheadFunctional y ≤ whiteheadFunctional y₀ := hfin
    _ = whiteheadFunctional (π / 4) := by rw [hy4]
    _ = 4 * QOU.Archimedean.Cl_2 (π / 2) := whiteheadFunctional_quarter

/-- The Whitehead grid-to-continuum slack: one half-grid log-sine cell (the
    `π/N` offset between `2Mπ/N` and `π` inside the shifted `clausen`) plus
    the endpoint `clausen` value near `π`. -/
noncomputable def whiteheadSlack (N : ℕ) : ℝ :=
  4 * ((π / (2 * N)) * (|Real.log (2 * Real.sin (π / (2 * N)))| + Real.log 2))
    + |clausen (π - π / N)|

theorem whiteheadSlack_nonneg (N : ℕ) : 0 ≤ whiteheadSlack N := by
  unfold whiteheadSlack
  have h1 : (0:ℝ) ≤ π / (2 * N) := by positivity
  have h2 : (0:ℝ) ≤ Real.log 2 := Real.log_nonneg (by norm_num)
  nlinarith [abs_nonneg (clausen (π - π / N)),
    abs_nonneg (Real.log (2 * Real.sin (π / (2 * N)))),
    mul_nonneg h1 (add_nonneg (abs_nonneg
      (Real.log (2 * Real.sin (π / (2 * N))))) h2)]

theorem tendsto_whiteheadSlack :
    Filter.Tendsto whiteheadSlack Filter.atTop (nhds 0) := by
  have hpi := Real.pi_pos
  have h2n : Filter.Tendsto (fun N : ℕ => 2 * N) Filter.atTop Filter.atTop :=
    Filter.tendsto_atTop_mono (fun N => by simp only [id_eq]; omega)
      Filter.tendsto_id
  -- the half-grid cell term, squeezed by masterErr ∘ (2·)
  have hcell : Filter.Tendsto
      (fun N : ℕ => 4 * ((π / (2 * N))
        * (|Real.log (2 * Real.sin (π / (2 * N)))| + Real.log 2)))
      Filter.atTop (nhds (4 * 0)) := by
    refine Filter.Tendsto.const_mul 4 ?_
    have hme2 := tendsto_masterErr.comp h2n
    refine tendsto_of_tendsto_of_tendsto_of_le_of_le' tendsto_const_nhds
      hme2 ?_ ?_
    · filter_upwards with N
      have h1 : (0:ℝ) ≤ π / (2 * N) := by positivity
      have h2 : (0:ℝ) ≤ Real.log 2 := Real.log_nonneg (by norm_num)
      exact mul_nonneg h1 (add_nonneg (abs_nonneg _) h2)
    · filter_upwards with N
      simp only [Function.comp_apply]
      unfold masterErr
      have hcast : ((2 * N : ℕ) : ℝ) = 2 * (N : ℝ) := by push_cast; ring
      rw [hcast]
      have h1 : (0:ℝ) ≤ π / (2 * N) := by positivity
      have h2 : (0:ℝ) ≤ Real.log 2 := Real.log_nonneg (by norm_num)
      have h3 := abs_nonneg (Real.log (2 * Real.sin (π / (2 * (N:ℝ)))))
      nlinarith [abs_nonneg (-clausen (2 * (π / (2 * (N:ℝ)))) / 2),
        mul_nonneg h1 h3, mul_nonneg h1 (add_nonneg h3 h2)]
  -- the endpoint clausen term → |clausen π| = 0
  have h0 := tendsto_const_div_atTop_nhds_zero_nat π
  have hP : Filter.Tendsto (fun N : ℕ => π - π / N)
      Filter.atTop (nhds π) := by
    have h1 := Filter.Tendsto.const_sub π h0
    rwa [sub_zero] at h1
  have hcP := (continuous_clausen.tendsto π).comp hP
  rw [clausen_pi] at hcP
  have hend : Filter.Tendsto (fun N : ℕ => |clausen (π - π / N)|)
      Filter.atTop (nhds 0) := by
    have := hcP.abs
    rw [abs_zero] at this
    exact this.congr fun N => rfl
  have hsum := hcell.add hend
  norm_num at hsum
  exact hsum

set_option maxHeartbeats 1000000 in
/-- **Whitehead brick W5a — the per-term ceiling (sorry-free).**  For every
    `k ≤ M` at `N = 2M+1`, the scaled log-term is at most the continuum
    saddle value plus the vanishing slack and deviation:

        (2π/N)·log S_{M,k} ≤ 4·Cl₂(π/2) + whiteheadSlack N + 10·masterErr N.

    For `1 ≤ k`: the W4b deviation lands on `2Ψ(k) = WF(kπ/N) −
    4·(log-sine half-cell) + clausen(2Mπ/N)`, bounded by the W5a-max plus the
    slack.  For `k = 0`: `log S_{M,0} = s_M` directly, one deviation
    instance plus the endpoint `clausen` value. -/
theorem whiteheadTerm_ceiling {N M k : ℕ} (hNM : N = 2 * M + 1)
    (hM2 : 2 ≤ M) (hk : k ≤ M) :
    (2 * π / N) * Real.log (whiteheadTerm N M k)
      ≤ 4 * QOU.Archimedean.Cl_2 (π / 2) + whiteheadSlack N
        + 10 * masterErr N := by
  have hpi := Real.pi_pos
  have hN4 : 4 ≤ N := by omega
  have hNpos : (0:ℝ) < N := by exact_mod_cast (by omega : 0 < N)
  have hN0 : (N:ℝ) ≠ 0 := ne_of_gt hNpos
  have hh : (0:ℝ) < π / N := by positivity
  have hfield : (N:ℝ) * (π / N) = π := by field_simp
  have hNr : (N:ℝ) = 2 * (M:ℝ) + 1 := by exact_mod_cast hNM
  have hhg : π / (2 * (N:ℝ)) = π / N / 2 := by
    rw [div_div, mul_comm]
  have hpos := Cl_2_pi_div_two_pos
  have hme := masterErr_nonneg N
  have hlog2 : (0:ℝ) ≤ Real.log 2 := Real.log_nonneg (by norm_num)
  -- the deterministic mid-angle: 2Mπ/N = π − π/N
  have h2M : 2 * ((M:ℝ) * (π / N)) = π - π / N := by
    have : 2 * (M:ℝ) = (N:ℝ) - 1 := by linarith [hNr]
    calc 2 * ((M:ℝ) * (π / N)) = (2 * (M:ℝ)) * (π / N) := by ring
      _ = ((N:ℝ) - 1) * (π / N) := by rw [this]
      _ = π - π / N := by rw [sub_mul, hfield, one_mul]
  rcases Nat.eq_zero_or_pos k with hk0 | hk1
  · -- k = 0: log S_{M,0} = s_M; one deviation instance + endpoint clausen
    subst hk0
    have hdev := abs_deviation_le_masterErr (N := N) (k := M) hN4
      (by omega) (by omega)
    rw [abs_le] at hdev
    have hlogT := log_whiteheadTerm (N := N) (M := M) (k := 0) (by omega)
    have hS0 : ∑ j ∈ Finset.Icc (1:ℕ) 0,
        Real.log (2 * Real.sin ((j : ℝ) * (π / N))) = 0 := by
      rw [Finset.Icc_eq_empty (by omega : ¬(1:ℕ) ≤ 0)]
      exact Finset.sum_empty
    rw [hS0] at hlogT
    have hlogT' : Real.log (whiteheadTerm N M 0)
        = ∑ j ∈ Finset.Icc 1 M,
            Real.log (2 * Real.sin ((j : ℝ) * (π / N))) := by
      rw [hlogT]
      simp only [Nat.zero_add]
      ring
    have habs := le_abs_self (clausen (π - π / N))
    have hslack : |clausen (π - π / N)| ≤ whiteheadSlack N := by
      unfold whiteheadSlack
      have h1 : (0:ℝ) ≤ π / (2 * N) := by positivity
      nlinarith [abs_nonneg (Real.log (2 * Real.sin (π / (2 * N)))),
        mul_nonneg h1 (add_nonneg (abs_nonneg
          (Real.log (2 * Real.sin (π / (2 * N))))) hlog2)]
    have hkey : (π / N) * Real.log (whiteheadTerm N M 0)
        ≤ -clausen (2 * ((M:ℝ) * (π / N))) / 2 + masterErr N := by
      rw [hlogT']
      linarith [hdev.2]
    have h2key := mul_le_mul_of_nonneg_left hkey (by norm_num : (0:ℝ) ≤ 2)
    calc (2 * π / N) * Real.log (whiteheadTerm N M 0)
        = 2 * ((π / N) * Real.log (whiteheadTerm N M 0)) := by ring
      _ ≤ 2 * (-clausen (2 * ((M:ℝ) * (π / N))) / 2 + masterErr N) := h2key
      _ = -clausen (π - π / N) + 2 * masterErr N := by rw [h2M]; ring
      _ ≤ |clausen (π - π / N)| + 2 * masterErr N := by
          have := neg_abs_le (clausen (π - π / N))
          linarith [this]
      _ ≤ 4 * QOU.Archimedean.Cl_2 (π / 2) + whiteheadSlack N
          + 10 * masterErr N := by linarith [hslack, hpos, hme]
  · -- 1 ≤ k: deviation + functional max + half-grid cell
    have hdev := abs_log_whiteheadTerm_deviation (N := N) (M := M) (k := k)
      hN4 (by omega) hk1 (by omega)
    rw [abs_le] at hdev
    -- the shifted upper angle: 2(k+M)π/N = θ + π − π/N with θ = 2kπ/N
    have hup : 2 * (((k:ℝ) + (M:ℝ)) * (π / N))
        = 2 * ((k:ℝ) * (π / N)) + π - π / N := by
      have h1 : 2 * (((k:ℝ) + (M:ℝ)) * (π / N))
          = 2 * ((k:ℝ) * (π / N)) + 2 * ((M:ℝ) * (π / N)) := by ring
      rw [h1, h2M]
      ring
    -- the functional at the grid point y = kπ/N ∈ [0, π/2]
    have hyle : (k:ℝ) * (π / N) ≤ π / 2 - π / (2 * N) := by
      have hkM' : (k:ℝ) ≤ (M:ℝ) := by exact_mod_cast hk
      have := mul_le_mul_of_nonneg_right hkM' hh.le
      nlinarith [h2M, this]
    have hymem : (k:ℝ) * (π / N) ∈ Set.Icc (0:ℝ) (π / 2) := by
      constructor
      · positivity
      · nlinarith [hyle]
    have hG := whiteheadFunctional_le hymem
    have hGexp : whiteheadFunctional ((k:ℝ) * (π / N))
        = 2 * clausen (2 * ((k:ℝ) * (π / N)))
          - 2 * clausen (2 * ((k:ℝ) * (π / N)) + π) := rfl
    rw [hGexp] at hG
    -- the half-grid cell between the shifted and unshifted upper angles
    set θ := 2 * ((k:ℝ) * (π / N)) with hθdef
    have hθ1 : 2 * (π / N) ≤ θ := by
      have hk' : (1:ℝ) ≤ (k:ℝ) := by exact_mod_cast hk1
      have := mul_le_mul_of_nonneg_right hk' hh.le
      nlinarith [this]
    have hθ2 : θ ≤ π - π / N := by
      nlinarith [hyle]
    have hcell := abs_integral_log_sin_cell_le
      (h := π / (2 * N)) (a := (θ + π) / 2 - π / (2 * N)) (b := (θ + π) / 2)
      (by positivity) (by nlinarith)
      (by nlinarith) (by nlinarith) (by nlinarith)
    rw [integral_log_sin_window] at hcell
    have hwin1 : 2 * ((θ + π) / 2) = θ + π := by ring
    have hwin2 : 2 * ((θ + π) / 2 - π / (2 * N)) = θ + π - π / N := by
      field_simp
    rw [hwin1, hwin2] at hcell
    have hcellw : (θ + π) / 2 - ((θ + π) / 2 - π / (2 * N)) = π / (2 * N) := by
      ring
    rw [hcellw, abs_le] at hcell
    -- assemble: (2π/N)·log S ≤ 2Ψ + 10E ≤ WF + cell + endpoint + 10E
    have hmain : (2 * π / N) * Real.log (whiteheadTerm N M k)
        ≤ 2 * (2 * ((-clausen (2 * (((k:ℝ) + (M:ℝ)) * (π / N))) / 2)
                - (-clausen (2 * ((k:ℝ) * (π / N))) / 2))
             - (-clausen (2 * ((M:ℝ) * (π / N))) / 2))
          + 10 * masterErr N := by
      have h1 := hdev.2
      have h2 := mul_le_mul_of_nonneg_left h1 (by norm_num : (0:ℝ) ≤ 2)
      calc (2 * π / N) * Real.log (whiteheadTerm N M k)
          = 2 * ((π / N) * Real.log (whiteheadTerm N M k)) := by ring
        _ ≤ 2 * ((2 * ((-clausen (2 * (((k:ℝ) + (M:ℝ)) * (π / N))) / 2)
                - (-clausen (2 * ((k:ℝ) * (π / N))) / 2))
             - (-clausen (2 * ((M:ℝ) * (π / N))) / 2)) + 5 * masterErr N) := by
              linarith [h2]
        _ = 2 * (2 * ((-clausen (2 * (((k:ℝ) + (M:ℝ)) * (π / N))) / 2)
                - (-clausen (2 * ((k:ℝ) * (π / N))) / 2))
             - (-clausen (2 * ((M:ℝ) * (π / N))) / 2))
          + 10 * masterErr N := by ring
    -- expand 2Ψ = 2clausen(θ) − 2clausen(θ+π−π/N) + clausen(π−π/N)
    have hpsi : 2 * (2 * ((-clausen (2 * (((k:ℝ) + (M:ℝ)) * (π / N))) / 2)
            - (-clausen (2 * ((k:ℝ) * (π / N))) / 2))
         - (-clausen (2 * ((M:ℝ) * (π / N))) / 2))
        = 2 * clausen θ - 2 * clausen (θ + π - π / N)
          + clausen (π - π / N) := by
      rw [hup, h2M]
      ring
    -- clausen(θ+π−π/N) = clausen(θ+π) + 2·∫cell  (F-bridge, so the cell
    -- controls the shift)
    have hslack1 : 2 * clausen θ - 2 * clausen (θ + π - π / N)
          + clausen (π - π / N)
        ≤ 4 * QOU.Archimedean.Cl_2 (π / 2) + whiteheadSlack N := by
      unfold whiteheadSlack
      have ha1 := le_abs_self (clausen (π - π / N))
      -- from the cell bound: |clausen(θ+π−π/N) − clausen(θ+π)| ≤ 2·cell
      have hc1 := hcell.1
      have hc2 := hcell.2
      nlinarith [hG, hc1, hc2, ha1]
    linarith [hmain, hpsi ▸ hslack1]

/-! ## Brick W5b — the squeeze -/

set_option maxHeartbeats 1000000 in
/-- **Whitehead brick W5b — the squeeze (sorry-free).**  Along the odd
    root-of-unity orders `N = 2M+1`, the scaled log of the Whitehead-chain
    positive sum tends to the octahedron volume:
    `(2π/N)·log P_M → 4·Cl₂(π/2) = 4G`.  Upper envelope: at most `M+1 ≤ N`
    terms, each below the W5a ceiling; lower envelope: the single grid term
    at `k* = ⌊N/4⌋` (the `y = π/4` saddle), whose W4b deviation target
    converges to the saddle value by continuity of `clausen`. -/
theorem tendsto_two_pi_log_whiteheadKashaev :
    Filter.Tendsto
      (fun M : ℕ => (2 * π / ((2 * M + 1 : ℕ) : ℝ))
        * Real.log (whiteheadKashaev (2 * M + 1) M))
      Filter.atTop (nhds (4 * QOU.Archimedean.Cl_2 (π / 2))) := by
  have hpi := Real.pi_pos
  have h2M1 : Filter.Tendsto (fun M : ℕ => 2 * M + 1)
      Filter.atTop Filter.atTop :=
    Filter.tendsto_atTop_mono (fun M => by simp only [id_eq]; omega)
      Filter.tendsto_id
  have hcastN : Filter.Tendsto (fun M : ℕ => ((2 * M + 1 : ℕ) : ℝ))
      Filter.atTop Filter.atTop :=
    tendsto_natCast_atTop_atTop.comp h2M1
  -- vanishing correction sequences along N = 2M+1
  have hmeM : Filter.Tendsto (fun M : ℕ => masterErr (2 * M + 1))
      Filter.atTop (nhds 0) := tendsto_masterErr.comp h2M1
  have hslM : Filter.Tendsto (fun M : ℕ => whiteheadSlack (2 * M + 1))
      Filter.atTop (nhds 0) := tendsto_whiteheadSlack.comp h2M1
  have hlogN : Filter.Tendsto
      (fun M : ℕ => (2 * π / ((2 * M + 1 : ℕ) : ℝ))
        * Real.log ((2 * M + 1 : ℕ) : ℝ))
      Filter.atTop (nhds 0) := by
    have h1 : Filter.Tendsto (fun x : ℝ => Real.log x / x)
        Filter.atTop (nhds 0) :=
      Real.isLittleO_log_id_atTop.tendsto_div_nhds_zero
    have h2 := Filter.Tendsto.const_mul (2 * π) (h1.comp hcastN)
    rw [mul_zero] at h2
    refine h2.congr (fun M => ?_)
    simp only [Function.comp_apply]
    ring
  -- the moving saddle grid angle 2·⌊N/4⌋·(π/N) → π/2  (N = 2M+1)
  have hθA : Filter.Tendsto
      (fun M : ℕ => 2 * ((↑((2 * M + 1) / 4) : ℝ)
        * (π / ((2 * M + 1 : ℕ) : ℝ))))
      Filter.atTop (nhds (π / 2)) := by
    have h0 := (tendsto_const_div_atTop_nhds_zero_nat (3 * π / 2)).comp h2M1
    have hlow := Filter.Tendsto.const_sub (π / 2) h0
    rw [sub_zero] at hlow
    refine tendsto_of_tendsto_of_tendsto_of_le_of_le' hlow tendsto_const_nhds
      ?_ ?_
    · filter_upwards [Filter.eventually_ge_atTop 1] with M hM1
      set N := 2 * M + 1 with hNdef
      have hNpos : (0:ℝ) < ((N:ℕ):ℝ) := by exact_mod_cast (by omega : 0 < N)
      have hh : (0:ℝ) < π / ((N:ℕ):ℝ) := by positivity
      have hN0 : (((N:ℕ)):ℝ) ≠ 0 := ne_of_gt hNpos
      have h6 : N ≤ 4 * (N / 4) + 3 := by omega
      have h6' : (((N:ℕ)):ℝ) ≤ 4 * ((↑(N / 4) : ℝ)) + 3 := by exact_mod_cast h6
      have hmul := mul_le_mul_of_nonneg_right h6' (le_of_lt hh)
      have hNπ : (((N:ℕ)):ℝ) * (π / ((N:ℕ):ℝ)) = π := by field_simp
      rw [hNπ] at hmul
      simp only [Function.comp_apply]
      have hdivN : (3:ℝ) * π / 2 / ((N:ℕ):ℝ) = 3 / 2 * (π / ((N:ℕ):ℝ)) := by
        ring
      rw [hdivN]
      linarith [hmul]
    · filter_upwards [Filter.eventually_ge_atTop 1] with M hM1
      set N := 2 * M + 1 with hNdef
      have hNpos : (0:ℝ) < ((N:ℕ):ℝ) := by exact_mod_cast (by omega : 0 < N)
      have hh : (0:ℝ) < π / ((N:ℕ):ℝ) := by positivity
      have hN0 : (((N:ℕ)):ℝ) ≠ 0 := ne_of_gt hNpos
      have h6 : 4 * (N / 4) ≤ N := by omega
      have h6' : (4:ℝ) * ((↑(N / 4) : ℝ)) ≤ (((N:ℕ)):ℝ) := by exact_mod_cast h6
      have hNπ : (((N:ℕ)):ℝ) * (π / ((N:ℕ):ℝ)) = π := by field_simp
      nlinarith [mul_le_mul_of_nonneg_right h6' (le_of_lt hh), hNπ]
  -- the deterministic mid angle 2·M·(π/N) → π  (equals π − π/N pointwise)
  have hθC : Filter.Tendsto
      (fun M : ℕ => 2 * (((M:ℕ) : ℝ) * (π / ((2 * M + 1 : ℕ) : ℝ))))
      Filter.atTop (nhds π) := by
    have h0 := (tendsto_const_div_atTop_nhds_zero_nat π).comp h2M1
    have h1 := Filter.Tendsto.const_sub π h0
    rw [sub_zero] at h1
    refine h1.congr (fun M => ?_)
    simp only [Function.comp_apply]
    have hN0 : (((2 * M + 1 : ℕ)):ℝ) ≠ 0 := by
      have : (0:ℝ) < ((2 * M + 1 : ℕ) : ℝ) := by
        exact_mod_cast (by omega : 0 < 2 * M + 1)
      exact ne_of_gt this
    have hcast : ((2 * M + 1 : ℕ) : ℝ) = 2 * (M:ℝ) + 1 := by push_cast; ring
    rw [hcast] at hN0 ⊢
    field_simp
    ring
  -- the shifted saddle angle 2·(⌊N/4⌋+M)·(π/N) → 3π/2
  have hθB : Filter.Tendsto
      (fun M : ℕ => 2 * (((↑((2 * M + 1) / 4) : ℝ) + ((M:ℕ) : ℝ))
        * (π / ((2 * M + 1 : ℕ) : ℝ))))
      Filter.atTop (nhds (3 * π / 2)) := by
    have hsum := hθA.add hθC
    have hval : π / 2 + π = 3 * π / 2 := by ring
    rw [hval] at hsum
    refine hsum.congr (fun M => ?_)
    ring
  -- clausen along the three moving angles
  have hv12 : clausen (π / 2) = QOU.Archimedean.Cl_2 (π / 2) :=
    clausen_eq_series ⟨by linarith, by linarith⟩
  have hv32 : clausen (3 * π / 2) = -QOU.Archimedean.Cl_2 (π / 2) := by
    have heq : clausen (3 * π / 2) = QOU.Archimedean.Cl_2 (3 * π / 2) :=
      clausen_eq_series ⟨by linarith, by linarith⟩
    have hanti := Cl_2_two_pi_sub (π / 2)
    rw [show 2 * π - π / 2 = 3 * π / 2 by ring] at hanti
    rw [heq, hanti]
  have hcA : Filter.Tendsto
      (fun M : ℕ => clausen (2 * ((↑((2 * M + 1) / 4) : ℝ)
        * (π / ((2 * M + 1 : ℕ) : ℝ)))))
      Filter.atTop (nhds (QOU.Archimedean.Cl_2 (π / 2))) := by
    have h := (continuous_clausen.tendsto (π / 2)).comp hθA
    rw [hv12] at h
    exact h
  have hcB : Filter.Tendsto
      (fun M : ℕ => clausen (2 * (((↑((2 * M + 1) / 4) : ℝ) + ((M:ℕ) : ℝ))
        * (π / ((2 * M + 1 : ℕ) : ℝ)))))
      Filter.atTop (nhds (-QOU.Archimedean.Cl_2 (π / 2))) := by
    have h := (continuous_clausen.tendsto (3 * π / 2)).comp hθB
    rw [hv32] at h
    exact h
  have hcC : Filter.Tendsto
      (fun M : ℕ => clausen (2 * (((M:ℕ) : ℝ)
        * (π / ((2 * M + 1 : ℕ) : ℝ)))))
      Filter.atTop (nhds 0) := by
    have h := (continuous_clausen.tendsto π).comp hθC
    rw [clausen_pi] at h
    exact h
  -- lower envelope limit: 2Ψ(k*) − 10E → 4·Cl₂(π/2)
  have hglim : Filter.Tendsto
      (fun M : ℕ => 2 * (2 * ((-clausen (2 * (((↑((2 * M + 1) / 4) : ℝ)
              + ((M:ℕ) : ℝ)) * (π / ((2 * M + 1 : ℕ) : ℝ)))) / 2)
            - (-clausen (2 * ((↑((2 * M + 1) / 4) : ℝ)
              * (π / ((2 * M + 1 : ℕ) : ℝ)))) / 2))
          - (-clausen (2 * (((M:ℕ) : ℝ)
              * (π / ((2 * M + 1 : ℕ) : ℝ)))) / 2))
        - 10 * masterErr (2 * M + 1))
      Filter.atTop (nhds (4 * QOU.Archimedean.Cl_2 (π / 2))) := by
    have h1 := (hcB.neg).div_const 2
    have h2 := (hcA.neg).div_const 2
    have h3 := (hcC.neg).div_const 2
    have h4 := Filter.Tendsto.const_mul (2:ℝ)
      ((Filter.Tendsto.const_mul (2:ℝ) (h1.sub h2)).sub h3)
    have h5 := Filter.Tendsto.const_mul (10:ℝ) hmeM
    have h6 := h4.sub h5
    have hval : (2:ℝ) * (2 * (-(-QOU.Archimedean.Cl_2 (π / 2)) / 2
        - -QOU.Archimedean.Cl_2 (π / 2) / 2) - -(0:ℝ) / 2) - 10 * 0
        = 4 * QOU.Archimedean.Cl_2 (π / 2) := by ring
    rw [hval] at h6
    exact h6
  -- upper envelope limit
  have hhlim : Filter.Tendsto
      (fun M : ℕ => (2 * π / ((2 * M + 1 : ℕ) : ℝ))
          * Real.log ((2 * M + 1 : ℕ) : ℝ)
        + (4 * QOU.Archimedean.Cl_2 (π / 2) + whiteheadSlack (2 * M + 1)
          + 10 * masterErr (2 * M + 1)))
      Filter.atTop (nhds (4 * QOU.Archimedean.Cl_2 (π / 2))) := by
    have hconst : Filter.Tendsto
        (fun _ : ℕ => 4 * QOU.Archimedean.Cl_2 (π / 2)) Filter.atTop
        (nhds (4 * QOU.Archimedean.Cl_2 (π / 2))) := tendsto_const_nhds
    have h1 := hconst.add hslM
    have h2 := h1.add (Filter.Tendsto.const_mul (10:ℝ) hmeM)
    have h3 := hlogN.add h2
    have hval : (0:ℝ) + (4 * QOU.Archimedean.Cl_2 (π / 2) + 0 + 10 * 0)
        = 4 * QOU.Archimedean.Cl_2 (π / 2) := by ring
    rw [hval] at h3
    exact h3
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le' hglim hhlim ?_ ?_
  · -- lower envelope: the single saddle grid term at k* = ⌊N/4⌋
    filter_upwards [Filter.eventually_ge_atTop 2] with M hM2
    set N := 2 * M + 1 with hNdef
    set k := N / 4 with hkdef
    have hNpos : (0:ℝ) < ((N:ℕ):ℝ) := by exact_mod_cast (by omega : 0 < N)
    have h2πN : (0:ℝ) ≤ 2 * π / ((N:ℕ):ℝ) := by positivity
    have hkM : k ≤ M := by omega
    have hT := whiteheadTerm_le_whiteheadKashaev (N := N) (M := M) (k := k)
      (by omega) (Finset.mem_range.mpr (by omega))
    have hTpos : 0 < whiteheadTerm N M k := whiteheadTerm_pos (by omega)
    have hlog := Real.log_le_log hTpos hT
    have hmul := mul_le_mul_of_nonneg_left hlog h2πN
    have hdev := abs_log_whiteheadTerm_deviation (N := N) (M := M) (k := k)
      (by omega) (by omega) (by omega) (by omega)
    rw [abs_le] at hdev
    calc 2 * (2 * ((-clausen (2 * (((↑k : ℝ) + ((M:ℕ) : ℝ))
              * (π / ((N:ℕ) : ℝ)))) / 2)
            - (-clausen (2 * ((↑k : ℝ) * (π / ((N:ℕ) : ℝ)))) / 2))
          - (-clausen (2 * (((M:ℕ) : ℝ) * (π / ((N:ℕ) : ℝ)))) / 2))
        - 10 * masterErr N
        ≤ 2 * ((π / ((N:ℕ):ℝ)) * Real.log (whiteheadTerm N M k)) := by
          linarith [hdev.1]
      _ = (2 * π / ((N:ℕ):ℝ)) * Real.log (whiteheadTerm N M k) := by ring
      _ ≤ (2 * π / ((N:ℕ):ℝ)) * Real.log (whiteheadKashaev N M) := hmul
  · -- upper envelope: (M+1) ≤ N terms, each below the W5a ceiling
    filter_upwards [Filter.eventually_ge_atTop 2] with M hM2
    set N := 2 * M + 1 with hNdef
    have hNpos : (0:ℝ) < ((N:ℕ):ℝ) := by exact_mod_cast (by omega : 0 < N)
    have h2πN : (0:ℝ) ≤ 2 * π / ((N:ℕ):ℝ) := by positivity
    have hne : (Finset.range (M + 1)).Nonempty :=
      ⟨0, Finset.mem_range.mpr (by omega)⟩
    obtain ⟨k₀, hk₀, hEq⟩ := Finset.exists_mem_eq_sup' hne (whiteheadTerm N M)
    have hk₀M : k₀ ≤ M := by
      have := Finset.mem_range.mp hk₀
      omega
    have hT0 : 0 < whiteheadTerm N M k₀ := whiteheadTerm_pos (by omega)
    have hsum : whiteheadKashaev N M ≤ ((N:ℕ):ℝ) * whiteheadTerm N M k₀ := by
      unfold whiteheadKashaev
      calc ∑ i ∈ Finset.range (M + 1), whiteheadTerm N M i
          ≤ ∑ _i ∈ Finset.range (M + 1), whiteheadTerm N M k₀ := by
            refine Finset.sum_le_sum fun i hi => ?_
            rw [← hEq]
            exact Finset.le_sup' (whiteheadTerm N M) hi
        _ = ((M + 1 : ℕ) : ℝ) * whiteheadTerm N M k₀ := by
            rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul]
        _ ≤ ((N:ℕ):ℝ) * whiteheadTerm N M k₀ := by
            have hcard : ((M + 1 : ℕ) : ℝ) ≤ ((N:ℕ):ℝ) := by
              exact_mod_cast (by omega : M + 1 ≤ N)
            nlinarith [hT0]
    have hlogle : Real.log (whiteheadKashaev N M)
        ≤ Real.log ((N:ℕ):ℝ) + Real.log (whiteheadTerm N M k₀) := by
      calc Real.log (whiteheadKashaev N M)
          ≤ Real.log (((N:ℕ):ℝ) * whiteheadTerm N M k₀) :=
            Real.log_le_log (whiteheadKashaev_pos (by omega)) hsum
        _ = Real.log ((N:ℕ):ℝ) + Real.log (whiteheadTerm N M k₀) :=
            Real.log_mul (ne_of_gt hNpos) hT0.ne'
    have hceil := whiteheadTerm_ceiling (N := N) (M := M) (k := k₀)
      rfl hM2 hk₀M
    have hmul := mul_le_mul_of_nonneg_left hlogle h2πN
    calc (2 * π / ((N:ℕ):ℝ)) * Real.log (whiteheadKashaev N M)
        ≤ (2 * π / ((N:ℕ):ℝ)) * (Real.log ((N:ℕ):ℝ)
            + Real.log (whiteheadTerm N M k₀)) := hmul
      _ = (2 * π / ((N:ℕ):ℝ)) * Real.log ((N:ℕ):ℝ)
          + (2 * π / ((N:ℕ):ℝ)) * Real.log (whiteheadTerm N M k₀) := by ring
      _ ≤ (2 * π / ((N:ℕ):ℝ)) * Real.log ((N:ℕ):ℝ)
          + (4 * QOU.Archimedean.Cl_2 (π / 2) + whiteheadSlack N
            + 10 * masterErr N) := by linarith [hceil]

/-- **The Whitehead-chain volume-conjecture instance, machine-proved (W5).**
    `(2π/N)·log P_M → 4·Cl₂(π/2) = 4G = 8Λ(π/4) = Vol(W_{a,2,1,0})` along
    the odd orders `N = 2M+1` — the third in-repo volume-conjecture
    instance after 4₁ and the Borromean rings, and the value shared with
    the Whitehead link proper (one regular ideal octahedron).  The carrier
    `P_M` is vdV Lemma 1's phase-free positive sum; by the exact modulus
    identity `|J_N(W_{a,b,c,d})| = N^b · P_M^{c+d}` (`b ≥ 2`) the invariant-
    level rate differs only by the vanishing `(2π/N)·b·log N`.  See the
    file header for the carrier's epistemic status. -/
theorem tendsto_log_whiteheadKashaev_vol :
    Filter.Tendsto
      (fun M : ℕ => (2 * π / ((2 * M + 1 : ℕ) : ℝ))
        * Real.log (whiteheadKashaev (2 * M + 1) M))
      Filter.atTop (nhds (QOU.Archimedean.Vol_Borromean / 2)) := by
  have h : QOU.Archimedean.Vol_Borromean / 2
      = 4 * QOU.Archimedean.Cl_2 (π / 2) := by
    have hV : QOU.Archimedean.Vol_Borromean
        = 8 * QOU.Archimedean.Cl_2 (π / 2) := rfl
    rw [hV]
    ring
  rw [h]
  exact tendsto_two_pi_log_whiteheadKashaev

/-- **The Whitehead-chain per-link volume-conjecture carrier**, mirroring
    `VolumeConjecture41` / `VolumeConjectureBorromean`: the single content
    field is the limit identity for the `W_{a,2,1,0}` chain (volume
    `4G = Vol(𝓑₃)/2`, one regular ideal octahedron).  The instance below is
    a genuine sorry-free proof (bricks W1–W5), not a citation. -/
class VolumeConjectureWhiteheadChain : Prop where
  /-- `(2π/(2M+1))·log P_M → 4·Cl₂(π/2) = 4G` as `M → ∞`. -/
  limit_eq_vol :
    Filter.Tendsto
      (fun M : ℕ => (2 * π / ((2 * M + 1 : ℕ) : ℝ))
        * Real.log (whiteheadKashaev (2 * M + 1) M))
      Filter.atTop (nhds (QOU.Archimedean.Vol_Borromean / 2))

/-- The proved instance — machine-checked (W1–W5), no sorry. -/
instance volumeConjectureWhiteheadChain_proved : VolumeConjectureWhiteheadChain :=
  ⟨tendsto_log_whiteheadKashaev_vol⟩

end QOU.Knot.FigureEightVolume
