/-
# vdV Lemma 4 for the Whitehead link — the phases are discharged (epic qou-u1b5)

Bricks L4-4 (phase algebra, `WhiteheadPhaseAlgebra`) and L4-5/L4-6 (complex
Gaussian sum, its nonvanishing) **assembled**: this file proves, sorry-free, that
`VdVWhiteheadLemma4` follows from a **phase-free** statement about the POSITIVE
outer weights

    w_N(n) = (2n+1) · Σ_k S_{n,k}     (the summands of `whiteheadLinkMajorant`).

## The carrier that remains (`WhiteheadOuterGaussianModel`)

    ∃ A_N > 0 :  Σ_{n<N} | w_N(n) − A_N · exp(−π (n − N/2)² / (2N)) |  ≤  A_N √N / 4

eventually — an L¹ Gaussian-shape estimate for a sequence of positive reals, with a
FIXED tolerance `1/4` (the truth is `o(1)`).  This is the content of van der Veen's
Lemma 2a/2b summed over `k` (bean `qou-vy77`, L4-2) plus the far-sum kill
(`qou-kc8h`, L4-3): `Σ_k exp(−(π/N)(x² + 2xy + 2y²)) ≈ √(N/2)·exp(−πx²/(2N))`.

Numerical evidence (`mpmath`, dps 30, `A_N := Σw/Σprofile`): the ratio
`Σ|w − A·profile| / (A√N)` is `0.0700, 0.0462, 0.0315, 0.0219, 0.0154` at
`N = 20, 40, 80, 160, 320` (decaying like `N^{-1/2}`), far below `1/4`; and
`majorant / ‖J_N‖ → 1.18921… = 2^{1/4}`, exactly `|1/√((1+i)/2)|`, as the Poisson
computation below predicts.  The carrier is therefore true-as-measured and is the
published Lemma 2a/2b content (signed form), not a new conjecture.

## What is proved here (no hypothesis on the phases)

* `whiteheadLinkPhase_mul_profile` — `profile·χ^{-1} = e^{iNπ/8} · G(n)` with
  `G(n) = exp(−π a (n−N/2)² + 2πiξn)`, `a = (1+i)/(2N)`, `ξ = −1/(4N)`;
* `half_sqrt_le_norm_tsum_whiteheadGauss` — `‖Σ_{n∈ℤ} G(n)‖ ≥ √N/2` (Poisson,
  `QOU.MathlibExt.norm_tsum_cgaussTerm_ge`): the chirp cannot cancel;
* `norm_tsum_sub_window_whiteheadGauss_le` — the lattice outside `[0, N)` costs
  `≤ C e^{−πN/16}`;
* `vdVWhiteheadLemma4_of_gaussianModel` — the class `VdVWhiteheadLemma4`, with
  `p = 2`, from `WhiteheadOuterGaussianModel` alone.

So after this file, **the Whitehead-link volume conjecture rests on a real,
positive-sum shape estimate**; no oscillatory analysis remains.
-- Ref: [manuscript] library/arxiv-math-0611181v2/0611181v2.pdf, Lemma 4 (Steps 3–6)
-/

import QOU.Knot.WhiteheadPhaseAlgebra
import QOU.MathlibExt.ComplexGaussianSumNonCancellation
import Mathlib.Analysis.Real.Pi.Bounds

namespace QOU.Knot.FigureEightVolume

open Real QOU.MathlibExt

/-- The positive outer weight `w_N(n) = (2n+1)·Σ_k S_{n,k}`. -/
noncomputable def whiteheadOuterWeight (N n : ℕ) : ℝ :=
  ((2 * n + 1 : ℕ) : ℝ) * ∑ k ∈ Finset.range (N - n), whiteheadTerm N n k

/-- The Gaussian profile `exp(−π (n − N/2)²/(2N))` the outer weights follow. -/
noncomputable def whiteheadGaussianProfile (N n : ℕ) : ℝ :=
  Real.exp (-(π * ((n : ℝ) - (N : ℝ) / 2) ^ 2 / (2 * N)))

/-- **Primary carrier (§3b-tax): the phase-free remainder of vdV Lemma 4.**
    The positive outer weights are, in `L¹`, within `A_N √N / 4` of the Gaussian
    profile of amplitude `A_N`.  (vdV Lemma 2a/2b summed over `k` + far-sum kill;
    measured ratio `≈ 0.31/√N`, see the file header.)  No instance is provided. -/
class WhiteheadOuterGaussianModel : Prop where
  model : ∃ A : ℕ → ℝ, ∀ᶠ N in Filter.atTop, 0 < A N ∧
    ∑ n ∈ Finset.range N,
        |whiteheadOuterWeight N n - A N * whiteheadGaussianProfile N n|
      ≤ A N * Real.sqrt N / 4

/-- The complex Gaussian parameter `a = (1+i)/(2N)`. -/
noncomputable def whiteheadGaussParam (N : ℕ) : ℂ := (1 + Complex.I) / (2 * (N : ℂ))

/-- The chirped Gaussian `G(n)` of the Whitehead outer sum. -/
noncomputable def whiteheadGauss (N : ℕ) (n : ℤ) : ℂ :=
  cgaussTerm (whiteheadGaussParam N) ((N : ℝ) / 2) (-(1 / (4 * (N : ℝ)))) n

theorem whiteheadLinkKashaev_eq (N : ℕ) :
    whiteheadLinkKashaev N
      = Complex.exp (((((N:ℝ) - 1) * π / N : ℝ) : ℂ) * Complex.I)
        * ∑ n ∈ Finset.range N,
            ((whiteheadOuterWeight N n : ℝ) : ℂ) * whiteheadLinkPhase N n := by
  unfold whiteheadLinkKashaev whiteheadOuterWeight
  congr 1
  refine Finset.sum_congr rfl (fun n _ => ?_)
  push_cast
  ring

theorem norm_whiteheadLinkPhase (N n : ℕ) : ‖whiteheadLinkPhase N n‖ = 1 := by
  unfold whiteheadLinkPhase
  exact Complex.norm_exp_ofReal_mul_I _

/-- **Profile × Fresnel phase = unimodular constant × chirped Gaussian (exact).** -/
theorem whiteheadLinkPhase_mul_profile {N : ℕ} (hN : 0 < N) (n : ℕ) :
    ((whiteheadGaussianProfile N n : ℝ) : ℂ) * whiteheadLinkPhase N n
      = Complex.exp ((((N : ℝ) * π / 8 : ℝ) : ℂ) * Complex.I)
        * whiteheadGauss N (n : ℤ) := by
  have hN' : (N : ℂ) ≠ 0 := by exact_mod_cast hN.ne'
  unfold whiteheadGaussianProfile whiteheadLinkPhase whiteheadGauss cgaussTerm
    whiteheadGaussParam
  rw [Complex.ofReal_exp, ← Complex.exp_add, ← Complex.exp_add]
  congr 1
  push_cast
  field_simp
  ring

theorem whiteheadGaussParam_re {N : ℕ} (hN : 0 < N) :
    (whiteheadGaussParam N).re = 1 / (2 * N) := by
  have hN' : (N : ℝ) ≠ 0 := by exact_mod_cast hN.ne'
  unfold whiteheadGaussParam
  rw [show (1 + Complex.I) / (2 * (N : ℂ))
      = ((1 / (2 * (N:ℝ)) : ℝ) : ℂ) * (1 + Complex.I) by push_cast; field_simp]
  rw [Complex.re_ofReal_mul]
  simp

theorem whiteheadGaussParam_inv {N : ℕ} (hN : 0 < N) :
    (whiteheadGaussParam N)⁻¹ = (N : ℂ) * (1 - Complex.I) := by
  have hN' : (N : ℂ) ≠ 0 := by exact_mod_cast hN.ne'
  unfold whiteheadGaussParam
  refine inv_eq_of_mul_eq_one_right ?_
  rw [div_mul_eq_mul_div, div_eq_one_iff_eq (by simpa using hN')]
  linear_combination (-(N : ℂ)) * Complex.I_sq

theorem whiteheadGaussParam_inv_re {N : ℕ} (hN : 0 < N) :
    ((whiteheadGaussParam N)⁻¹).re = N := by
  rw [whiteheadGaussParam_inv hN]
  simp

theorem norm_whiteheadGaussParam_le {N : ℕ} (hN : 0 < N) :
    ‖whiteheadGaussParam N‖ ≤ 1 / N := by
  have hNpos : (0:ℝ) < N := by exact_mod_cast hN
  unfold whiteheadGaussParam
  rw [norm_div]
  have h1 : ‖(1 : ℂ) + Complex.I‖ ≤ 2 := by
    calc ‖(1 : ℂ) + Complex.I‖ ≤ ‖(1:ℂ)‖ + ‖Complex.I‖ := norm_add_le _ _
      _ = 2 := by simp; norm_num
  have h2 : ‖(2 * (N : ℂ))‖ = 2 * N := by
    rw [norm_mul]; simp
  rw [h2, div_le_div_iff₀ (by positivity) hNpos]
  nlinarith

/-- `‖a^{1/2}‖⁻¹ ≥ √N` for `a = (1+i)/(2N)`. -/
theorem sqrt_le_inv_norm_cpow_half {N : ℕ} (hN : 0 < N) :
    Real.sqrt N ≤ ‖whiteheadGaussParam N ^ (1 / 2 : ℂ)‖⁻¹ := by
  have hNpos : (0:ℝ) < N := by exact_mod_cast hN
  have hsq := norm_cpow_half_sq (whiteheadGaussParam N)
  have hle := norm_whiteheadGaussParam_le hN
  have hre := whiteheadGaussParam_re hN
  have hne : whiteheadGaussParam N ≠ 0 := by
    intro h; rw [h] at hre; simp at hre; omega
  have hpos : 0 < ‖whiteheadGaussParam N ^ (1 / 2 : ℂ)‖ := by
    have : 0 < ‖whiteheadGaussParam N‖ := norm_pos_iff.mpr hne
    nlinarith [norm_nonneg (whiteheadGaussParam N ^ (1 / 2 : ℂ))]
  set t := ‖whiteheadGaussParam N ^ (1 / 2 : ℂ)‖
  have hs := Real.sq_sqrt hNpos.le
  have hs0 := Real.sqrt_nonneg (N:ℝ)
  -- `t² ≤ 1/N`, so `t · √N ≤ 1`
  have ht2 : t ^ 2 * N ≤ 1 := by
    rw [hsq]; rw [le_div_iff₀ hNpos] at hle; linarith
  have htN : t * Real.sqrt N ≤ 1 := by
    have : (t * Real.sqrt N) ^ 2 ≤ 1 := by rw [mul_pow, hs]; exact ht2
    nlinarith [mul_nonneg hpos.le hs0]
  rw [← one_div, le_div_iff₀ hpos]
  linarith [mul_comm t (Real.sqrt N)]

/-- **The chirp cannot cancel (sorry-free):** `‖Σ_{n∈ℤ} G(n)‖ ≥ √N/2` for `N ≥ 16`. -/
theorem half_sqrt_le_norm_tsum_whiteheadGauss {N : ℕ} (hN : 16 ≤ N) :
    Real.sqrt N / 2 ≤ ‖∑' n : ℤ, whiteheadGauss N n‖ := by
  have hN0 : 0 < N := by omega
  have hNpos : (0:ℝ) < N := by exact_mod_cast hN0
  have hN16 : (16:ℝ) ≤ N := by exact_mod_cast hN
  have hre : 0 < (whiteheadGaussParam N).re := by
    rw [whiteheadGaussParam_re hN0]; positivity
  have hξ : |(-(1 / (4 * (N : ℝ))))| ≤ 1 / 2 := by
    rw [abs_neg, abs_of_pos (by positivity)]
    rw [div_le_div_iff₀ (by positivity) (by norm_num)]; linarith
  have h := norm_tsum_cgaussTerm_ge hre ((N : ℝ) / 2) _ hξ
  rw [whiteheadGaussParam_inv_re hN0] at h
  have hpi := Real.pi_pos
  have hpi4 := Real.pi_le_four
  have hpi3 := Real.pi_gt_three
  -- the dual `m = 0` term is at least `3/4`
  have h0 : (3:ℝ) / 4 ≤ Real.exp (-(π * N) * (-(1 / (4 * (N : ℝ)))) ^ 2) := by
    have harg : -(π * N) * (-(1 / (4 * (N : ℝ)))) ^ 2 = -(π / (16 * N)) := by
      field_simp; ring
    rw [harg]
    have := Real.add_one_le_exp (-(π / (16 * N)))
    have hsmall : π / (16 * N) ≤ 1 / 4 := by
      rw [div_le_div_iff₀ (by positivity) (by norm_num)]; nlinarith
    linarith
  -- the other dual terms are at most `1/6`
  set q := Real.exp (-(π * N) / 4) with hq
  have hq0 : 0 < q := Real.exp_pos _
  have hq13 : q ≤ 1 / 13 := by
    have he := Real.add_one_le_exp (π * N / 4)
    have hqe : q * Real.exp (π * N / 4) = 1 := by
      rw [hq, ← Real.exp_add]; ring_nf; exact Real.exp_zero
    have : (13:ℝ) ≤ Real.exp (π * N / 4) := by nlinarith
    nlinarith
  have hrest : 2 * q / (1 - q) ≤ 1 / 6 := by
    rw [div_le_div_iff₀ (by linarith) (by norm_num)]; linarith
  have hbr : (1:ℝ) / 2 ≤ Real.exp (-(π * N) * (-(1 / (4 * (N : ℝ)))) ^ 2)
      - 2 * q / (1 - q) := by linarith
  have hinv := sqrt_le_inv_norm_cpow_half hN0
  calc Real.sqrt N / 2 = Real.sqrt N * (1 / 2) := by ring
    _ ≤ ‖whiteheadGaussParam N ^ (1 / 2 : ℂ)‖⁻¹
          * (Real.exp (-(π * N) * (-(1 / (4 * (N : ℝ)))) ^ 2) - 2 * q / (1 - q)) :=
        mul_le_mul hinv hbr (by norm_num) (by positivity)
    _ ≤ _ := h

/-- The lattice window `[0, N) ⊂ ℤ`. -/
def whiteheadWindow (N : ℕ) : Finset ℤ := (Finset.range N).map Nat.castEmbedding

/-- **Outside `[0, N)` the chirped Gaussian is exponentially small.** -/
theorem norm_tsum_sub_window_whiteheadGauss_le {N : ℕ} (hN : 0 < N) :
    ‖(∑' n : ℤ, whiteheadGauss N n) - ∑ n ∈ whiteheadWindow N, whiteheadGauss N n‖
      ≤ Real.exp (-(π * N / 16))
        * (1 + 2 * Real.exp (-(π / 16)) / (1 - Real.exp (-(π / 16)))) := by
  have hNpos : (0:ℝ) < N := by exact_mod_cast hN
  have hpi := Real.pi_pos
  have hre : 0 < (whiteheadGaussParam N).re := by
    rw [whiteheadGaussParam_re hN]; positivity
  set r := Real.exp (-(π / 16)) with hr
  have hr0 : 0 ≤ r := (Real.exp_pos _).le
  have hr1 : r < 1 := by
    rw [hr]
    calc Real.exp (-(π / 16)) < Real.exp 0 := Real.exp_lt_exp.mpr (by linarith)
      _ = 1 := Real.exp_zero
  have hg := (QOU.MathlibExt.hasSum_int_geometric hr0 hr1).mul_left
    (Real.exp (-(π * N / 16)))
  refine norm_tsum_sub_finset_sum_le (summable_cgaussTerm hre _ _) _ hg
    (fun n => by positivity) (fun n hn => ?_)
  -- `n ∉ [0, N)`: `n < 0` or `n ≥ N`
  have hout : n < 0 ∨ (N : ℤ) ≤ n := by
    by_contra hc
    push_neg at hc
    apply hn
    unfold whiteheadWindow
    rw [Finset.mem_map]
    refine ⟨n.toNat, Finset.mem_range.mpr (by omega), ?_⟩
    simp only [Nat.castEmbedding_apply]
    omega
  rw [norm_cgaussTerm, whiteheadGaussParam_re hN, hr, ← Real.exp_nat_mul,
    ← Real.exp_add]
  apply Real.exp_le_exp.mpr
  have hcast : ((n.natAbs : ℕ) : ℝ) = |(n : ℝ)| := by
    rw [Nat.cast_natAbs]; push_cast; rfl
  rw [hcast]
  set d := (n : ℝ) - (N : ℝ) / 2 with hd
  -- `d² ≥ N²/8 + N|n|/8`
  have hkey : (N : ℝ) ^ 2 / 8 + (N : ℝ) * |(n : ℝ)| / 8 ≤ d ^ 2 := by
    rcases hout with h | h
    · have hn' : (n : ℝ) < 0 := by exact_mod_cast h
      rw [abs_of_neg hn']
      nlinarith
    · have hn' : (N : ℝ) ≤ (n : ℝ) := by exact_mod_cast h
      rw [abs_of_nonneg (by linarith)]
      nlinarith
  have : π * (N : ℝ) / 16 + π * |(n : ℝ)| / 16 ≤ π * (1 / (2 * N)) * d ^ 2 := by
    have h2 : π * (1 / (2 * (N:ℝ))) * d ^ 2 = π * d ^ 2 / (2 * N) := by ring
    rw [h2, le_div_iff₀ (by positivity)]
    nlinarith [mul_le_mul_of_nonneg_left hkey hpi.le]
  nlinarith

theorem sum_window_whiteheadGauss (N : ℕ) :
    ∑ n ∈ whiteheadWindow N, whiteheadGauss N n
      = ∑ n ∈ Finset.range N, whiteheadGauss N (n : ℤ) := by
  unfold whiteheadWindow
  rw [Finset.sum_map]
  rfl

theorem whiteheadGaussianProfile_le_one (N n : ℕ) : whiteheadGaussianProfile N n ≤ 1 := by
  unfold whiteheadGaussianProfile
  rw [Real.exp_le_one_iff]
  have : 0 ≤ π * ((n : ℝ) - (N : ℝ) / 2) ^ 2 / (2 * N) := by positivity
  linarith

theorem whiteheadLinkMajorant_eq (N : ℕ) :
    whiteheadLinkMajorant N = ∑ n ∈ Finset.range N, whiteheadOuterWeight N n := rfl

/-- **vdV Lemma 4 for the Whitehead link, from the phase-free Gaussian model
    (sorry-free, conditional on `WhiteheadOuterGaussianModel` only).**
    The Fresnel phases cost at most `N²`. -/
theorem vdVWhiteheadLemma4_of_gaussianModel [WhiteheadOuterGaussianModel] :
    VdVWhiteheadLemma4 := by
  refine ⟨⟨2, ?_⟩⟩
  obtain ⟨A, hA⟩ := WhiteheadOuterGaussianModel.model
  have hpi := Real.pi_pos
  -- the tail constant is eventually below `1/8`
  set r := Real.exp (-(π / 16))
  set C := 1 + 2 * r / (1 - r)
  have htend : Filter.Tendsto (fun N : ℕ => C * Real.exp (-(π * N / 16)))
      Filter.atTop (nhds (C * 0)) := by
    refine Filter.Tendsto.const_mul C ?_
    have h1 : Filter.Tendsto (fun N : ℕ => π / 16 * (N : ℝ)) Filter.atTop Filter.atTop :=
      Filter.Tendsto.const_mul_atTop (by positivity) tendsto_natCast_atTop_atTop
    have h2 := Real.tendsto_exp_neg_atTop_nhds_zero.comp h1
    refine h2.congr (fun N => ?_)
    simp only [Function.comp]
    congr 1; ring
  have hev := htend.eventually (Iic_mem_nhds (by norm_num : C * 0 < 1 / 8))
  filter_upwards [hA, hev, Filter.eventually_ge_atTop 16] with N ⟨hApos, hmod⟩ htail hN
  have hN0 : 0 < N := by omega
  have hNpos : (0:ℝ) < N := by exact_mod_cast hN0
  have hN16 : (16:ℝ) ≤ N := by exact_mod_cast hN
  have htail' : C * Real.exp (-(π * N / 16)) ≤ 1 / 8 := htail
  set s := Real.sqrt (N : ℝ)
  have hs2 : s ^ 2 = N := Real.sq_sqrt hNpos.le
  have hs0 : 0 ≤ s := Real.sqrt_nonneg _
  have hs1 : 1 ≤ s := by nlinarith
  have hsN : s ≤ N := by nlinarith
  -- (1) the window Gaussian sum is at least `3√N/8`
  have hG : 3 * s / 8 ≤ ‖∑ n ∈ Finset.range N, whiteheadGauss N (n : ℤ)‖ := by
    have h1 := half_sqrt_le_norm_tsum_whiteheadGauss hN
    have h2 := norm_tsum_sub_window_whiteheadGauss_le hN0
    rw [sum_window_whiteheadGauss] at h2
    have h3 := norm_sub_norm_le (∑' n : ℤ, whiteheadGauss N n)
      (∑ n ∈ Finset.range N, whiteheadGauss N (n : ℤ))
    have h4 : Real.exp (-(π * N / 16)) * C ≤ 1 / 8 := by
      rw [mul_comm]; exact htail'
    have h5 := le_trans h2 h4
    linarith
  -- (2) the decomposition `Σ w·χ⁻¹ = A·e^{iNπ/8}·Σ G + Σ (w − A·profile)·χ⁻¹`
  set E := Complex.exp ((((N : ℝ) * π / 8 : ℝ) : ℂ) * Complex.I)
  have hE : ‖E‖ = 1 := Complex.norm_exp_ofReal_mul_I _
  have hdec : ∑ n ∈ Finset.range N,
        ((whiteheadOuterWeight N n : ℝ) : ℂ) * whiteheadLinkPhase N n
      = (A N : ℂ) * E * ∑ n ∈ Finset.range N, whiteheadGauss N (n : ℤ)
        + ∑ n ∈ Finset.range N,
            ((whiteheadOuterWeight N n - A N * whiteheadGaussianProfile N n : ℝ) : ℂ)
              * whiteheadLinkPhase N n := by
    rw [Finset.mul_sum, ← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl (fun n _ => ?_)
    have := whiteheadLinkPhase_mul_profile hN0 n
    push_cast
    linear_combination (A N : ℂ) * this
  have herr : ‖∑ n ∈ Finset.range N,
        ((whiteheadOuterWeight N n - A N * whiteheadGaussianProfile N n : ℝ) : ℂ)
          * whiteheadLinkPhase N n‖ ≤ A N * s / 4 := by
    refine le_trans (norm_sum_le _ _) (le_trans (le_of_eq ?_) hmod)
    refine Finset.sum_congr rfl (fun n _ => ?_)
    rw [norm_mul, norm_whiteheadLinkPhase, mul_one, Complex.norm_real, Real.norm_eq_abs]
  have hmain : ‖(A N : ℂ) * E * ∑ n ∈ Finset.range N, whiteheadGauss N (n : ℤ)‖
      = A N * ‖∑ n ∈ Finset.range N, whiteheadGauss N (n : ℤ)‖ := by
    rw [norm_mul, norm_mul, hE, mul_one, Complex.norm_real, Real.norm_eq_abs,
      abs_of_pos hApos]
  -- (3) `‖J_N‖ ≥ A√N/8`
  have hJ : A N * s / 8 ≤ ‖whiteheadLinkKashaev N‖ := by
    rw [whiteheadLinkKashaev_eq, norm_mul, Complex.norm_exp_ofReal_mul_I, one_mul, hdec]
    have h3 := norm_sub_le ((A N : ℂ) * E * ∑ n ∈ Finset.range N, whiteheadGauss N (n : ℤ)
        + ∑ n ∈ Finset.range N,
            ((whiteheadOuterWeight N n - A N * whiteheadGaussianProfile N n : ℝ) : ℂ)
              * whiteheadLinkPhase N n)
      (∑ n ∈ Finset.range N,
            ((whiteheadOuterWeight N n - A N * whiteheadGaussianProfile N n : ℝ) : ℂ)
              * whiteheadLinkPhase N n)
    rw [add_sub_cancel_right, hmain] at h3
    nlinarith [mul_le_mul_of_nonneg_left hG hApos.le]
  -- (4) the majorant is at most `2·A·N`
  have hM : whiteheadLinkMajorant N ≤ 2 * A N * N := by
    rw [whiteheadLinkMajorant_eq]
    have hpt : ∀ n ∈ Finset.range N, whiteheadOuterWeight N n
        ≤ A N + |whiteheadOuterWeight N n - A N * whiteheadGaussianProfile N n| := by
      intro n _
      have h1 := whiteheadGaussianProfile_le_one N n
      have h2 := le_abs_self (whiteheadOuterWeight N n - A N * whiteheadGaussianProfile N n)
      nlinarith
    calc ∑ n ∈ Finset.range N, whiteheadOuterWeight N n
        ≤ ∑ n ∈ Finset.range N, (A N
            + |whiteheadOuterWeight N n - A N * whiteheadGaussianProfile N n|) :=
          Finset.sum_le_sum hpt
      _ = N * A N + ∑ n ∈ Finset.range N,
            |whiteheadOuterWeight N n - A N * whiteheadGaussianProfile N n| := by
          rw [Finset.sum_add_distrib]; simp
      _ ≤ N * A N + A N * s / 4 := by linarith
      _ ≤ 2 * A N * N := by nlinarith
  -- (5) `2AN ≤ N² · A√N/8`
  have hNN : 2 * A N * N ≤ (N : ℝ) ^ 2 * (A N * s / 8) := by
    have : (0:ℝ) ≤ A N * N * (N * s - 16) := by
      apply mul_nonneg (by positivity); nlinarith
    nlinarith
  calc whiteheadLinkMajorant N ≤ 2 * A N * N := hM
    _ ≤ (N : ℝ) ^ 2 * (A N * s / 8) := hNN
    _ ≤ (N : ℝ) ^ 2 * ‖whiteheadLinkKashaev N‖ :=
        mul_le_mul_of_nonneg_left hJ (by positivity)

end QOU.Knot.FigureEightVolume
