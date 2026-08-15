/-
# Whitehead link (b = 1) scaffold: complex carrier, majorant bound, and the
# vdV-Lemma-4 conditional class (bean qou-ybpk)

The `b ≥ 2` Whitehead-chain volume-conjecture instance is proved sorry-free
in `WhiteheadChainVolume.lean` because its Kashaev-point modulus is a
phase-free positive sum.  The `b = 1` Whitehead link proper
(`W_{0,1,1,0}` = L5a1, Vol = 4G) is different: vdV Lemma 1 gives

    J_N = φ_N Σ_{n=0}^{N-1} (2n+1) χ_{N,n}^{-1} (Σ_{k=0}^{N-1-n} S_{n,k}),
    χ_{N,n} = exp(n(n+1-N)πi/(2N)),  φ_N = exp((N-1)πi/N),

whose outer `n`-sum carries Fresnel phases.  Van der Veen's Lemma 4 (the
Gaussian/erfc stationary-phase analysis, arXiv:math/0611181 §3 Steps 3-6)
shows the phases cost only polynomially — `J_N ∼ C·N^{(c+d+3)/2}·S̃^{c+d}`
with `C ≠ 0` — but that analysis is NOT elementary and is not reproduced
here.  This file records the honest split:

* **Sorry-free**: the complex carrier `whiteheadLinkKashaev` (faithful
  Lemma-1 transcription, anchor-verified numerically in
  `computations/whitehead_vdv_lemma1.py`), the positive majorant
  `whiteheadLinkMajorant`, its positivity, and the triangle inequality
  `‖J_N‖ ≤ majorant` — the upper half of a future squeeze.
* **Conditional class** `VdVWhiteheadLemma4` (a PRIMARY conjecture carrier,
  §3b-tax): the single content field `phase_cost` states Lemma 4's analytic
  essence — the majorant exceeds the modulus by at most a fixed power of
  `N`.  No instance is provided: the class is the open analytic input.
* **Derived conditional theorem**
  `tendsto_log_norm_whiteheadLinkKashaev_of_majorant`: GIVEN the class and
  the majorant volume rate (the open 2D brick W6, bean qou-oiv6 — the
  2-variable functional `f(x,y) = Λ(x) + 2Λ(y) − 2Λ(x+y)` maximised at
  `(π/2, π/4)`), the Whitehead-link volume limit follows by an elementary
  log-squeeze.  The conclusion is derived, not axiomatised.

Route context: `docs/audits/2026-08-02-whitehead-chain-positive-sum-route.md`.
-/

import QOU.Knot.WhiteheadChainVolume

namespace QOU.Knot.FigureEightVolume

open Real

/-- The Fresnel phase `χ_{N,n}^{-1} = exp(−n(n+1−N)πi/(2N))` of vdV
    Lemma 1 at exponent `4a−c+d = −1` (the Whitehead link `W_{0,1,1,0}`). -/
noncomputable def whiteheadLinkPhase (N n : ℕ) : ℂ :=
  Complex.exp (((-((n:ℝ) * ((n:ℝ) + 1 - (N:ℝ)) * π / (2 * N)) : ℝ) : ℂ)
    * Complex.I)

/-- The `b = 1` Whitehead-link Lemma-1 sum at the Kashaev point (faithful
    transcription; `φ_N = exp((N−1)πi/N)` for `c+d = 1`, inner sums are the
    positive `S_{n,k}` of the chain file with the `M`-slot at `n`). -/
noncomputable def whiteheadLinkKashaev (N : ℕ) : ℂ :=
  Complex.exp (((((N:ℝ) - 1) * π / N : ℝ) : ℂ) * Complex.I)
    * ∑ n ∈ Finset.range N, ((2 * n + 1 : ℕ) : ℂ) * whiteheadLinkPhase N n
        * (((∑ k ∈ Finset.range (N - n), whiteheadTerm N n k : ℝ)) : ℂ)

/-- The positive majorant: the same double sum with the phases dropped. -/
noncomputable def whiteheadLinkMajorant (N : ℕ) : ℝ :=
  ∑ n ∈ Finset.range N,
    ((2 * n + 1 : ℕ) : ℝ) * (∑ k ∈ Finset.range (N - n), whiteheadTerm N n k)

/-- Each inner sum is strictly positive (`n ≤ N−1` leaves at least the
    `k = 0` term, and every term is an in-grid positive `S_{n,k}`). -/
theorem whiteheadLink_inner_pos {N n : ℕ} (hn : n < N) :
    0 < ∑ k ∈ Finset.range (N - n), whiteheadTerm N n k := by
  apply Finset.sum_pos
  · intro k hk
    have hk' := Finset.mem_range.mp hk
    exact whiteheadTerm_pos (by omega)
  · exact ⟨0, Finset.mem_range.mpr (by omega)⟩

/-- The majorant is strictly positive for `N ≥ 1`. -/
theorem whiteheadLinkMajorant_pos {N : ℕ} (hN : 1 ≤ N) :
    0 < whiteheadLinkMajorant N := by
  unfold whiteheadLinkMajorant
  apply Finset.sum_pos
  · intro n hn
    have hn' := Finset.mem_range.mp hn
    have hinner := whiteheadLink_inner_pos (N := N) (n := n) hn'
    have h2n : (0:ℝ) < ((2 * n + 1 : ℕ) : ℝ) := by
      exact_mod_cast (by omega : 0 < 2 * n + 1)
    exact mul_pos h2n hinner
  · exact ⟨0, Finset.mem_range.mpr (by omega)⟩

/-- **The triangle bound (sorry-free)** — the upper half of the future
    `b = 1` squeeze: `‖J_N‖ ≤ majorant N`.  The global `φ_N` and each
    `χ_{N,n}^{-1}` are unimodular, the inner sums are positive. -/
theorem norm_whiteheadLinkKashaev_le (N : ℕ) :
    ‖whiteheadLinkKashaev N‖ ≤ whiteheadLinkMajorant N := by
  unfold whiteheadLinkKashaev whiteheadLinkMajorant
  rw [norm_mul, Complex.norm_exp_ofReal_mul_I, one_mul]
  refine le_trans (norm_sum_le _ _) ?_
  apply Finset.sum_le_sum
  intro n hn
  have hn' := Finset.mem_range.mp hn
  have hinner := (whiteheadLink_inner_pos (N := N) (n := n) hn').le
  rw [norm_mul, norm_mul]
  unfold whiteheadLinkPhase
  rw [Complex.norm_exp_ofReal_mul_I, mul_one]
  rw [Complex.norm_natCast, Complex.norm_real, Real.norm_eq_abs,
    abs_of_nonneg hinner]

/-- **vdV Lemma 4, axiomatised as a primary conjecture class** (§3b-tax; no
    instance is provided — this is the open analytic input).  Content: the
    Fresnel phases of the `b = 1` outer sum cost at most a fixed power of
    `N` — the stationary-phase constant is nonzero, so modulus and majorant
    share their exponential growth.  This is the analytic essence of
    van der Veen's Lemma 4 (Gaussian → erfc, arXiv:math/0611181 §3); a
    future sorry-free discharge would formalize that argument.
    -- Ref: [manuscript] library/arxiv-math-0611181v2/0611181v2.pdf, Lemma 4 -/
class VdVWhiteheadLemma4 : Prop where
  /-- The majorant exceeds the modulus by at most `N^p` for some fixed `p`,
      eventually in `N` — phases cost polynomially, never exponentially. -/
  phase_cost : ∃ p : ℕ, ∀ᶠ N in Filter.atTop,
    whiteheadLinkMajorant N ≤ (N:ℝ) ^ p * ‖whiteheadLinkKashaev N‖

/-- **Conditional volume limit for the Whitehead link (derived, not
    axiomatised).**  Given the Lemma-4 class AND the majorant volume rate
    (the open 2D brick W6, bean qou-oiv6), the Whitehead-link Kashaev
    modulus obeys the volume conjecture:
    `(2π/N)·log ‖J_N‖ → 4·Cl₂(π/2) = 4G = Vol(L5a1)`.  Proof: an
    elementary log-squeeze between `log majorant − p·log N` (the class) and
    `log majorant` (the sorry-free triangle bound). -/
theorem tendsto_log_norm_whiteheadLinkKashaev_of_majorant [VdVWhiteheadLemma4]
    (hMaj : Filter.Tendsto
      (fun N : ℕ => (2 * π / N) * Real.log (whiteheadLinkMajorant N))
      Filter.atTop (nhds (QOU.Archimedean.Vol_Borromean / 2))) :
    Filter.Tendsto
      (fun N : ℕ => (2 * π / N) * Real.log ‖whiteheadLinkKashaev N‖)
      Filter.atTop (nhds (QOU.Archimedean.Vol_Borromean / 2)) := by
  have hpi := Real.pi_pos
  obtain ⟨p, hp⟩ := VdVWhiteheadLemma4.phase_cost
  -- p·(2π/N)·log N → 0
  have hlogN : Filter.Tendsto
      (fun N : ℕ => (p:ℝ) * ((2 * π / N) * Real.log N))
      Filter.atTop (nhds 0) := by
    have h1 : Filter.Tendsto (fun x : ℝ => Real.log x / x)
        Filter.atTop (nhds 0) :=
      Real.isLittleO_log_id_atTop.tendsto_div_nhds_zero
    have h2 := Filter.Tendsto.const_mul ((p:ℝ) * (2 * π))
      (h1.comp tendsto_natCast_atTop_atTop)
    rw [mul_zero] at h2
    refine h2.congr (fun N => ?_)
    simp only [Function.comp_apply]
    ring
  -- lower envelope: (2π/N)·log majorant − p·(2π/N)·log N → target
  have hlow : Filter.Tendsto
      (fun N : ℕ => (2 * π / N) * Real.log (whiteheadLinkMajorant N)
        - (p:ℝ) * ((2 * π / N) * Real.log N))
      Filter.atTop (nhds (QOU.Archimedean.Vol_Borromean / 2)) := by
    have h := hMaj.sub hlogN
    rwa [sub_zero] at h
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le' hlow hMaj ?_ ?_
  · -- from the class: log ‖J‖ ≥ log majorant − p·log N
    filter_upwards [hp, Filter.eventually_ge_atTop 2] with N hpN hN2
    have hNpos : (0:ℝ) < N := by exact_mod_cast (by omega : 0 < N)
    have h2πN : (0:ℝ) ≤ 2 * π / N := by positivity
    have hMpos := whiteheadLinkMajorant_pos (N := N) (by omega)
    have hJpos : 0 < ‖whiteheadLinkKashaev N‖ := by
      by_contra h
      push_neg at h
      have hJ0 : ‖whiteheadLinkKashaev N‖ = 0 :=
        le_antisymm h (norm_nonneg _)
      rw [hJ0, mul_zero] at hpN
      linarith
    have hNp : (0:ℝ) < (N:ℝ) ^ p := by positivity
    have hlogle : Real.log (whiteheadLinkMajorant N)
        ≤ (p:ℝ) * Real.log N + Real.log ‖whiteheadLinkKashaev N‖ := by
      calc Real.log (whiteheadLinkMajorant N)
          ≤ Real.log ((N:ℝ) ^ p * ‖whiteheadLinkKashaev N‖) :=
            Real.log_le_log hMpos hpN
        _ = (p:ℝ) * Real.log N + Real.log ‖whiteheadLinkKashaev N‖ := by
            rw [Real.log_mul hNp.ne' hJpos.ne', Real.log_pow]
    have hmul := mul_le_mul_of_nonneg_left hlogle h2πN
    calc (2 * π / N) * Real.log (whiteheadLinkMajorant N)
          - (p:ℝ) * ((2 * π / N) * Real.log N)
        ≤ ((2 * π / N) * ((p:ℝ) * Real.log N
            + Real.log ‖whiteheadLinkKashaev N‖))
          - (p:ℝ) * ((2 * π / N) * Real.log N) := by linarith [hmul]
      _ = (2 * π / N) * Real.log ‖whiteheadLinkKashaev N‖ := by ring
  · -- from the triangle bound: log ‖J‖ ≤ log majorant
    filter_upwards [hp, Filter.eventually_ge_atTop 2] with N hpN hN2
    have hNpos : (0:ℝ) < N := by exact_mod_cast (by omega : 0 < N)
    have h2πN : (0:ℝ) ≤ 2 * π / N := by positivity
    have hJpos : 0 < ‖whiteheadLinkKashaev N‖ := by
      by_contra h
      push_neg at h
      have hJ0 : ‖whiteheadLinkKashaev N‖ = 0 :=
        le_antisymm h (norm_nonneg _)
      have hMpos := whiteheadLinkMajorant_pos (N := N) (by omega)
      rw [hJ0, mul_zero] at hpN
      linarith
    have hlogle : Real.log ‖whiteheadLinkKashaev N‖
        ≤ Real.log (whiteheadLinkMajorant N) :=
      Real.log_le_log hJpos (norm_whiteheadLinkKashaev_le N)
    exact mul_le_mul_of_nonneg_left hlogle h2πN

end QOU.Knot.FigureEightVolume
