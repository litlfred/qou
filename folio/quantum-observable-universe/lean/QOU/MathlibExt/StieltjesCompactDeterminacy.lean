import QOU.MathlibExt.FrechetShohat
import Mathlib.Topology.ContinuousMap.Weierstrass
import Mathlib.Analysis.SpecificLimits.Basic

/-!
# QOU.MathlibExt.StieltjesCompactDeterminacy

The **compact-support leg** of Stieltjes moment determinacy, proved
sorry-free on top of the predicates `HasStieltjesMoments` /
`StieltjesDeterminate` of `QOU.MathlibExt.FrechetShohat`.

## What is proved

1. `measure_Ioi_eq_zero_of_moment_bound` — if a finite measure `μ` on `ℝ`
   has Stieltjes moment data `M` with `M k ≤ C · R^k` for every `k`
   (`0 ≤ R`), then `μ (Ioi R) = 0`: the moment bound forces the support
   into `[0, R]` (Markov's inequality on `s^k`, then `k → ∞`).
2. `eq_of_ae_mem_Icc_of_moments_eq` — two finite measures on `ℝ`, both
   concentrated on a compact interval `[a, b]`, with equal integrals of
   every monomial `s^k` (all integrable), are equal (Weierstrass
   approximation on `[a, b]` + separation of finite measures by bounded
   continuous functions, `ext_of_forall_integral_eq_of_IsFiniteMeasure`).
3. `stieltjesDeterminate_of_moment_bound` — **main theorem**: if
   `M k ≤ C · R^k` for all `k` (some `C`, some `R ≥ 0`), then the Stieltjes
   moment problem for `M` is determinate (`StieltjesDeterminate M`).
4. `eq_of_hasStieltjesMoments_of_Ioi_null` — measure-level form: a
   probability measure `μ` supported in `[0, R]` is the unique probability
   measure on `[0, ∞)` with its moment sequence.

## What is NOT proved here

- Carleman's criterion (`CarlemanDeterminacyStieltjes`) and
  Fréchet–Shohat (`FrechetShohatStieltjes`) remain Mathlib-gap hypothesis
  classes in `FrechetShohat.lean`; nothing here instantiates them.
  Geometric moment growth (`M k ≤ C R^k`) is far stronger than Carleman
  and does NOT cover the factorial (Schwinger) moments `M k = k!`, which
  are the case the q-Borel kernel-convergence theorem needs.

-- Ref: [leitner2026] P. Billingsley, Probability and Measure, 3rd ed.,
-- Wiley 1995, Thm 30.1 (compactly supported / bounded measures are
-- determined by their moments); N. I. Akhiezer, The Classical Moment
-- Problem, Oliver & Boyd 1965, Ch. 2.
-/

namespace QOU.MathlibExt.StieltjesCompactDeterminacy

open MeasureTheory Filter Topology Set
open QOU.MathlibExt.FrechetShohat

/-- A Stieltjes-moment measure is a.e. nonnegative. -/
lemma ae_nonneg_of_hasStieltjesMoments {μ : Measure ℝ} {M : ℕ → ℝ}
    (h : HasStieltjesMoments μ M) : ∀ᵐ s ∂μ, 0 ≤ s := by
  rw [ae_iff]
  have : {a : ℝ | ¬ 0 ≤ a} = Iio 0 := by ext a; simp
  rw [this]; exact h.1

/-- Markov step: under geometric moment bounds, `μ([R', ∞)) = 0` for
every `R' > R ≥ 0`. -/
lemma measure_Ici_eq_zero_of_moment_bound {μ : Measure ℝ} [IsFiniteMeasure μ]
    {M : ℕ → ℝ} (h : HasStieltjesMoments μ M) {C R : ℝ} (hR : 0 ≤ R)
    (hM : ∀ k, M k ≤ C * R ^ k) {R' : ℝ} (hR' : R < R') :
    μ (Ici R') = 0 := by
  have hR'pos : 0 < R' := lt_of_le_of_lt hR hR'
  have hnn := ae_nonneg_of_hasStieltjesMoments h
  -- μ.real (Ici R') ≤ C * (R/R')^k for every k
  have hbound : ∀ k : ℕ, μ.real (Ici R') ≤ C * (R / R') ^ k := by
    intro k
    have hmk := mul_meas_ge_le_integral_of_nonneg
      (f := fun s : ℝ => s ^ k) (hnn.mono fun s hs => pow_nonneg hs k)
      (h.2 k).1 (R' ^ k)
    rw [(h.2 k).2] at hmk
    have hsub : Ici R' ⊆ {x : ℝ | R' ^ k ≤ x ^ k} := by
      intro x hx
      exact pow_le_pow_left₀ hR'pos.le hx k
    have hmono : μ.real (Ici R') ≤ μ.real {x : ℝ | R' ^ k ≤ x ^ k} :=
      measureReal_mono hsub
    have hpk : 0 < R' ^ k := pow_pos hR'pos k
    have h1 : R' ^ k * μ.real (Ici R') ≤ C * R ^ k :=
      le_trans (mul_le_mul_of_nonneg_left hmono hpk.le) (le_trans hmk (hM k))
    rw [div_pow, ← mul_div_assoc, le_div_iff₀ hpk]
    linarith
  have hlim : Tendsto (fun k : ℕ => C * (R / R') ^ k) atTop (𝓝 0) := by
    have := tendsto_pow_atTop_nhds_zero_of_lt_one (div_nonneg hR hR'pos.le)
      ((div_lt_one hR'pos).2 hR')
    simpa using this.const_mul C
  have hle : μ.real (Ici R') ≤ 0 :=
    ge_of_tendsto hlim (Eventually.of_forall hbound)
  have h0 : μ.real (Ici R') = 0 := le_antisymm hle measureReal_nonneg
  exact (measureReal_eq_zero_iff (measure_ne_top μ _)).1 h0

/-- **Support bound from geometric moment growth.** If `μ` (finite) has
Stieltjes moments `M` with `M k ≤ C · R^k`, then `μ` puts no mass on
`(R, ∞)`. -/
theorem measure_Ioi_eq_zero_of_moment_bound {μ : Measure ℝ} [IsFiniteMeasure μ]
    {M : ℕ → ℝ} (h : HasStieltjesMoments μ M) {C R : ℝ} (hR : 0 ≤ R)
    (hM : ∀ k, M k ≤ C * R ^ k) : μ (Ioi R) = 0 := by
  have hU : Ioi R = ⋃ n : ℕ, Ici (R + 1 / ((n : ℝ) + 1)) := by
    ext x
    simp only [mem_Ioi, mem_iUnion, mem_Ici]
    constructor
    · intro hx
      obtain ⟨n, hn⟩ := exists_nat_one_div_lt (sub_pos.2 hx)
      exact ⟨n, by linarith⟩
    · rintro ⟨n, hn⟩
      have : (0 : ℝ) < 1 / ((n : ℝ) + 1) := by positivity
      linarith
  rw [hU]
  refine measure_iUnion_null fun n => ?_
  apply measure_Ici_eq_zero_of_moment_bound h hR hM
  have : (0 : ℝ) < 1 / ((n : ℝ) + 1) := by positivity
  linarith

/-- Integral of a polynomial against a measure with integrable monomials,
expressed through the monomial integrals. -/
lemma integrable_and_integral_eval {μ : Measure ℝ}
    (hint : ∀ k : ℕ, Integrable (fun s : ℝ => s ^ k) μ) (p : Polynomial ℝ) :
    Integrable (fun s => p.eval s) μ ∧
      ∫ s, p.eval s ∂μ = ∑ i ∈ Finset.range (p.natDegree + 1),
        p.coeff i * ∫ s, s ^ i ∂μ := by
  have hfun : (fun s => p.eval s)
      = fun s => ∑ i ∈ Finset.range (p.natDegree + 1), p.coeff i * s ^ i := by
    funext s; exact Polynomial.eval_eq_sum_range s
  have hi : ∀ i ∈ Finset.range (p.natDegree + 1),
      Integrable (fun s : ℝ => p.coeff i * s ^ i) μ :=
    fun i _ => (hint i).const_mul _
  rw [hfun]
  refine ⟨integrable_finset_sum _ hi, ?_⟩
  rw [integral_finset_sum _ hi]
  refine Finset.sum_congr rfl fun i _ => ?_
  exact integral_const_mul _ _

/-- **Compact-support moment uniqueness.** Two finite measures on `ℝ`,
both concentrated on `[a, b]`, whose monomials are integrable with equal
integrals, are equal. -/
theorem eq_of_ae_mem_Icc_of_moments_eq {μ ν : Measure ℝ} [IsFiniteMeasure μ]
    [IsFiniteMeasure ν] {a b : ℝ}
    (hμ : ∀ᵐ s ∂μ, s ∈ Icc a b) (hν : ∀ᵐ s ∂ν, s ∈ Icc a b)
    (hμi : ∀ k : ℕ, Integrable (fun s : ℝ => s ^ k) μ)
    (hνi : ∀ k : ℕ, Integrable (fun s : ℝ => s ^ k) ν)
    (hmom : ∀ k : ℕ, ∫ s, s ^ k ∂μ = ∫ s, s ^ k ∂ν) : μ = ν := by
  apply ext_of_forall_integral_eq_of_IsFiniteMeasure
  intro f
  set K : ℝ := μ.real univ + ν.real univ with hK
  have hK0 : 0 ≤ K := add_nonneg measureReal_nonneg measureReal_nonneg
  apply eq_of_forall_dist_le
  intro ε hε
  set δ : ℝ := ε / (K + 1) with hδ
  have hδpos : 0 < δ := div_pos hε (by linarith)
  obtain ⟨p, hp⟩ := exists_polynomial_near_of_continuousOn a b (fun x => f x)
    f.continuous.continuousOn δ hδpos
  obtain ⟨hpμ, hpμ'⟩ := integrable_and_integral_eval hμi p
  obtain ⟨hpν, hpν'⟩ := integrable_and_integral_eval hνi p
  have hpeq : ∫ s, p.eval s ∂μ = ∫ s, p.eval s ∂ν := by
    rw [hpμ', hpν']
    exact Finset.sum_congr rfl fun i _ => by rw [hmom i]
  -- error estimates
  have herr : ∀ (ρ : Measure ℝ) [IsFiniteMeasure ρ], (∀ᵐ s ∂ρ, s ∈ Icc a b) →
      Integrable (fun s => p.eval s) ρ →
      |∫ s, f s ∂ρ - ∫ s, p.eval s ∂ρ| ≤ δ * ρ.real univ := by
    intro ρ _ hρ hpρ
    rw [← integral_sub (f.integrable ρ) hpρ]
    have := norm_integral_le_of_norm_le_const (μ := ρ)
      (f := fun s => f s - p.eval s) (C := δ) (hρ.mono fun s hs => by
        have := hp s hs
        rw [Real.norm_eq_abs, abs_sub_comm]; exact this.le)
    simpa [Real.norm_eq_abs] using this
  have e1 := herr μ hμ hpμ
  have e2 := herr ν hν hpν
  rw [Real.dist_eq]
  have hsum : |∫ s, f s ∂μ - ∫ s, f s ∂ν| ≤ δ * K := by
    have htri : ∫ s, f s ∂μ - ∫ s, f s ∂ν
        = (∫ s, f s ∂μ - ∫ s, p.eval s ∂μ) - (∫ s, f s ∂ν - ∫ s, p.eval s ∂ν) := by
      rw [hpeq]; ring
    rw [htri, hK, mul_add]
    exact le_trans (abs_sub _ _) (add_le_add e1 e2)
  have hδK : δ * K ≤ ε := by
    rw [hδ, div_mul_eq_mul_div, div_le_iff₀ (by linarith)]
    nlinarith
  linarith

/-- If `μ` has Stieltjes moments and no mass right of `R`, it lives on
`[0, R]` almost everywhere. -/
lemma ae_mem_Icc_of_hasStieltjesMoments {μ : Measure ℝ} {M : ℕ → ℝ}
    (h : HasStieltjesMoments μ M) {R : ℝ} (hR : μ (Ioi R) = 0) :
    ∀ᵐ s ∂μ, s ∈ Icc 0 R := by
  have h2 : ∀ᵐ s ∂μ, s ≤ R := by
    rw [ae_iff]
    have : {a : ℝ | ¬ a ≤ R} = Ioi R := by ext a; simp
    rw [this]; exact hR
  filter_upwards [ae_nonneg_of_hasStieltjesMoments h, h2] with s h0 h1
  exact ⟨h0, h1⟩

/-- **Main theorem (compact-support determinacy).** A moment sequence
with geometric growth `M k ≤ C · R^k` (some `C`, some `R ≥ 0`) is
Stieltjes-determinate: at most one probability measure on `[0, ∞)` has
these moments. -/
theorem stieltjesDeterminate_of_moment_bound {M : ℕ → ℝ} {C R : ℝ}
    (hR : 0 ≤ R) (hM : ∀ k, M k ≤ C * R ^ k) : StieltjesDeterminate M := by
  intro μ ν _ _ hμ hν
  have sμ := ae_mem_Icc_of_hasStieltjesMoments hμ
    (measure_Ioi_eq_zero_of_moment_bound hμ hR hM)
  have sν := ae_mem_Icc_of_hasStieltjesMoments hν
    (measure_Ioi_eq_zero_of_moment_bound hν hR hM)
  exact eq_of_ae_mem_Icc_of_moments_eq sμ sν (fun k => (hμ.2 k).1)
    (fun k => (hν.2 k).1) (fun k => by rw [(hμ.2 k).2, (hν.2 k).2])

/-- The special case `M k ≤ R ^ k`. -/
theorem stieltjesDeterminate_of_bounded {M : ℕ → ℝ} {R : ℝ} (hR : 0 ≤ R)
    (hM : ∀ k, M k ≤ R ^ k) : StieltjesDeterminate M :=
  stieltjesDeterminate_of_moment_bound (C := 1) hR (fun k => by simpa using hM k)

/-- **Measure-level form.** If a probability measure `μ` has Stieltjes
moments `M` and carries no mass on `(R, ∞)` (`0 ≤ R`), then every
probability measure `ν` on `[0, ∞)` with the same moments equals `μ`. -/
theorem eq_of_hasStieltjesMoments_of_Ioi_null {μ ν : Measure ℝ}
    [IsProbabilityMeasure μ] [IsProbabilityMeasure ν] {M : ℕ → ℝ} {R : ℝ}
    (hR : 0 ≤ R) (hμ : HasStieltjesMoments μ M) (hμR : μ (Ioi R) = 0)
    (hν : HasStieltjesMoments ν M) : μ = ν := by
  have sμ := ae_mem_Icc_of_hasStieltjesMoments hμ hμR
  -- moments of μ are bounded by R^k
  have hM : ∀ k, M k ≤ 1 * R ^ k := by
    intro k
    rw [← (hμ.2 k).2, one_mul]
    have := norm_integral_le_of_norm_le_const (μ := μ) (f := fun s : ℝ => s ^ k)
      (C := R ^ k) (sμ.mono fun s hs => by
        rw [Real.norm_eq_abs, abs_pow, abs_of_nonneg hs.1]
        exact pow_le_pow_left₀ hs.1 hs.2 k)
    rw [measureReal_univ_eq_one, mul_one, Real.norm_eq_abs] at this
    exact le_trans (le_abs_self _) this
  exact stieltjesDeterminate_of_moment_bound hR hM μ ν inferInstance inferInstance hμ hν

end QOU.MathlibExt.StieltjesCompactDeterminacy
