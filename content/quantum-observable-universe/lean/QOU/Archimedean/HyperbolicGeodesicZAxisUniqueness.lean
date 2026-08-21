/-
# HyperbolicGeodesicZAxisUniqueness.lean (T2, WALL-4) — z-axis geodesic
# uniqueness: a constant-speed minimiser between two z-axis points IS the
# vertical segment `vseg`, pointwise.

This is the tractable half of the geodesic-uniqueness wall (bean `qou-xidi`).
The FULL uniqueness conjecture `HypMinimizerUnique` (arbitrary endpoints) also
needs the two-point boundary-inversion normalisation (WALL-2, bean `qou-0a0z`)
and the WALL-5 assembly; those are NOT closed here and no `HypMinimizerUnique`
instance is fabricated.  What IS closed is the standalone z-axis case.

## The statement

`zaxis_minimizer_eq_vseg` : if `IsHypMinimizer γ (zpt a) (zpt b)` (a constant-
speed length-minimiser between the z-axis points `(0,0,a)`, `(0,0,b)`, `a,b>0`),
then `∀ τ ∈ [0,1], γ τ = vseg a b τ`.  The minimiser is pointwise the vertical
segment — the genuine equality-case of the FTC lower bound.

## The argument (DERIVED, not assumed)

Let `k := log b − log a`, `c := |k|`.

1. **Constant speed pins `c = |log(b/a)|`.**  `hypSpeed γ` is constant `= c`
   along `[0,1]` (minimiser hypothesis), so `pathLenH γ = ofReal c`; but the
   length is minimal, `= dH (zpt a)(zpt b) = ofReal|log(b/a)|` (`dH_zpt`), and
   both nonneg, so `c = |k|`.  Hence `‖γ' t‖ = c·(γ t)₂` pointwise.

2. **Saturation ⇒ a.e. structure.**  The FTC lower bound
   `|log b − log a| = |∫₀¹ φ'| ≤ ∫₀¹ |φ'| ≤ ∫₀¹ g = c`  (with
   `φ' = (γ')₂/z`, `g = ‖γ'‖/z`) is now an equality chain.  Casing on the sign
   of `k`, the nonnegative integrand `g ∓ φ'` has integral `c ∓ k = |k| ∓ k = 0`,
   so by `integral_eq_zero_iff_of_nonneg_ae` it vanishes a.e.  This gives, a.e.:
   `‖γ' t‖ = |(γ' t)₂|`  (horizontal velocity collapses)  AND  `φ' t = k`.

3. **Horizontal coordinates are constant `0`.**  `‖v‖ = |v 2|` in `ℝ³` forces
   `v 0 = v 1 = 0` (`horiz_zero_of_norm_eq_abs`), so `(γ')₀ = (γ')₁ = 0` a.e.;
   FTC-2 on `[0,τ]` then pins `(γ τ)₀ = (γ 0)₀ = 0`, likewise coordinate 1.

4. **Height is `heightProfile`.**  `φ' = k` a.e. and FTC-2 for `φ = log z` on
   `[0,τ]` give `log(γ τ)₂ = log a + k·τ = logInterp a b τ`, i.e.
   `(γ τ)₂ = exp(logInterp) = heightProfile a b τ`.

Then `γ τ = single 2 (heightProfile a b τ) = vseg a b τ`.

## ⚠ VERIFICATION STATUS (read before trusting)

Authored in a container whose Mathlib `.lake` oleans were ABSENT (6 present of
~2900 needed) and whose cache-restore / `lake exe cache get` paths were
explicitly disabled, so this file could NOT be machine-checked here (no
`lean`-direct build, no `#print axioms`).  It is a rigorous HAND-AUDIT against
the Mathlib 4.24.0 API, reusing patterns already verified on `main` in the
sibling files (`pathLenH_ge_logHeight`, `height_le`, `horizDisplacement_le`,
`pathLenH_vseg`).  Treat it as "complete proof, pending machine verification":
bean `qou-xidi` stays OPEN until a build with Mathlib present confirms it
sorry-free with axioms `[propext, Classical.choice, Quot.sound]` only.

Archimedean (ℝ): `exp`, `log`, `‖·‖`, ordering `0 < z`, real analysis / FTC — §7c.

  -- Ref: [thurston1978] Ch. 2 §2.3 p. 12 (the metric; vertical geodesics)
  -- Ref: [ratcliffe] §4.6 (geodesics of `H³`; the z-axis is the length-minimiser)
  -- Ref: [manuscript] beans qou-xidi (T2 WALL-4 z-axis uniqueness),
  --   qou-0a0z (WALL-2), qou-r111 (the full geodesic-uniqueness wall)
-/

import QOU.Archimedean.HyperbolicGeodesic
import QOU.Archimedean.HyperbolicGeodesicZAxis
import QOU.Archimedean.HyperbolicMetricSeparation

namespace QOU.Archimedean

open QOU.Archimedean.HyperbolicMetric
open MeasureTheory Set
open scoped ENNReal

/-- **`‖v‖ = |v 2|` collapses the horizontal velocity.**  In `ℝ³` (Euclidean),
if the norm of `v` equals the absolute value of its height component, the two
horizontal components vanish: `‖v‖² = Σ (v i)² = (v 2)²` forces
`(v 0)² + (v 1)² = 0`. -/
theorem horiz_zero_of_norm_eq_abs (v : E) (h : ‖v‖ = |v 2|) : v 0 = 0 ∧ v 1 = 0 := by
  have hns : ‖v‖ ^ 2 = ∑ i, (v i) ^ 2 := by
    rw [EuclideanSpace.norm_eq, Real.sq_sqrt (by positivity)]
    apply Finset.sum_congr rfl
    intro i _; rw [Real.norm_eq_abs, sq_abs]
  rw [Fin.sum_univ_three] at hns
  have h2 : ‖v‖ ^ 2 = (v 2) ^ 2 := by rw [h, sq_abs]
  have hv0 : (v 0) ^ 2 = 0 := le_antisymm (by nlinarith [hns, h2, sq_nonneg (v 1)]) (sq_nonneg _)
  have hv1 : (v 1) ^ 2 = 0 := le_antisymm (by nlinarith [hns, h2, sq_nonneg (v 0)]) (sq_nonneg _)
  exact ⟨(pow_eq_zero_iff (n := 2) (by norm_num)).mp hv0,
         (pow_eq_zero_iff (n := 2) (by norm_num)).mp hv1⟩

/-- **WALL-4 — z-axis geodesic uniqueness (DERIVED).**  A constant-speed
minimiser between two z-axis points is pointwise the vertical segment `vseg`.
The genuine equality-case of the FTC vertical lower bound.

This does NOT close the full `HypMinimizerUnique` conjecture (arbitrary
endpoints): no instance is fabricated; only the z-axis case is derived. -/
theorem zaxis_minimizer_eq_vseg {a b : ℝ} (ha : 0 < a) (hb : 0 < b) {γ : ℝ → E}
    (hγ : IsHypMinimizer γ (zpt a) (zpt b)) :
    ∀ τ ∈ Set.Icc (0 : ℝ) 1, γ τ = vseg a b τ := by
  classical
  have h0 : (0 : ℝ) ∈ Set.Icc (0 : ℝ) 1 := ⟨le_refl _, by norm_num⟩
  set k : ℝ := Real.log b - Real.log a with hk
  -- continuity of γ on Icc (needed repeatedly)
  have hγc : ContinuousOn γ (Set.Icc (0 : ℝ) 1) :=
    fun t ht => (hγ.admissible.diff t ht).continuousAt.continuousWithinAt
  -- constant hyperbolic speed value c
  set c : ℝ := hypSpeed γ 0 with hc
  have hconst : ∀ t ∈ Set.Icc (0 : ℝ) 1, hypSpeed γ t = c :=
    fun t ht => (hγ.constSpeed t ht 0 h0).trans hc.symm
  have hcnn : 0 ≤ c := by
    rw [hc]; exact div_nonneg (norm_nonneg _) (le_of_lt (hγ.admissible.mem 0 h0))
  -- speedFn agrees with c on Icc (speedFn = hypSpeed definitionally)
  have hgval : ∀ t ∈ Set.Icc (0 : ℝ) 1, speedFn γ t = c := by
    intro t ht; have := hconst t ht; simpa [speedFn, hypSpeed] using this
  -- pathLenH γ = ofReal c
  have hpath_c : pathLenH γ 0 1 = ENNReal.ofReal c := by
    unfold pathLenH
    have hcongr : ∀ t ∈ Set.Icc (0 : ℝ) 1,
        ENNReal.ofReal (‖deriv γ t‖ / (γ t) 2) = ENNReal.ofReal c := by
      intro t ht
      rw [show ‖deriv γ t‖ / (γ t) 2 = speedFn γ t from rfl, hgval t ht]
    rw [setLIntegral_congr_fun measurableSet_Icc hcongr, setLIntegral_const,
      Real.volume_Icc, sub_zero, ENNReal.ofReal_one, mul_one]
  have hLfin : pathLenH γ 0 1 ≠ ∞ := by rw [hpath_c]; exact ENNReal.ofReal_ne_top
  -- c = |k| (minimality + dH_zpt)
  have hc_eq : c = |k| := by
    have hlen : pathLenH γ 0 1 = ENNReal.ofReal |Real.log (b / a)| := by
      rw [hγ.minimal, dH_zpt ha hb]
    have hEq : ENNReal.ofReal c = ENNReal.ofReal |k| := by
      rw [← hpath_c, hlen, hk, Real.log_div (ne_of_gt hb) (ne_of_gt ha)]
    have := congrArg ENNReal.toReal hEq
    rwa [ENNReal.toReal_ofReal hcnn, ENNReal.toReal_ofReal (abs_nonneg _)] at this
  -- ‖γ' t‖ = |k| · (γ t)₂
  have hnorm_eq : ∀ t ∈ Set.Icc (0 : ℝ) 1, ‖deriv γ t‖ = |k| * (γ t) 2 := by
    intro t ht
    have hz : (0 : ℝ) < (γ t) 2 := hγ.admissible.mem t ht
    have hs : ‖deriv γ t‖ / (γ t) 2 = |k| := by
      have := hgval t ht; rw [hc_eq] at this; simpa [speedFn] using this
    rw [div_eq_iff (ne_of_gt hz)] at hs; exact hs
  -- |φ' t| ≤ |k| on Icc
  have hφ'_bd : ∀ t ∈ Set.Icc (0 : ℝ) 1, |(deriv γ t) 2 / (γ t) 2| ≤ |k| := by
    intro t ht
    have hz : (0 : ℝ) < (γ t) 2 := hγ.admissible.mem t ht
    rw [abs_div, abs_of_pos hz, div_le_iff₀ hz]
    calc |(deriv γ t) 2| ≤ ‖deriv γ t‖ := abs_coord_le_norm _ 2
      _ = |k| * (γ t) 2 := hnorm_eq t ht
  -- measurability of φ' on Icc
  have hnumCoord : AEStronglyMeasurable (fun t => (deriv γ t) 2)
      (volume.restrict (Set.Icc (0 : ℝ) 1)) :=
    ((coordCLM 2).measurable.comp (measurable_deriv γ)).aestronglyMeasurable
  have hden : AEStronglyMeasurable (fun t => (γ t) 2)
      (volume.restrict (Set.Icc (0 : ℝ) 1)) :=
    ((coordCLM 2).continuous.comp_continuousOn hγc).aestronglyMeasurable measurableSet_Icc
  have hφ'm : AEStronglyMeasurable (fun t => (deriv γ t) 2 / (γ t) 2)
      (volume.restrict (Set.Icc (0 : ℝ) 1)) :=
    (hnumCoord.aemeasurable.div hden.aemeasurable).aestronglyMeasurable
  -- φ' integrable on Icc (dominated by the constant |k|)
  have phi_int : IntegrableOn (fun t => (deriv γ t) 2 / (γ t) 2) (Set.Icc (0 : ℝ) 1) := by
    have hconstInt : IntegrableOn (fun _ : ℝ => |k|) (Set.Icc (0 : ℝ) 1) :=
      continuousOn_const.integrableOn_compact isCompact_Icc
    refine Integrable.mono' hconstInt hφ'm ?_
    refine (ae_restrict_iff' measurableSet_Icc).mpr (ae_of_all _ (fun t ht => ?_))
    rw [Real.norm_eq_abs]; exact hφ'_bd t ht
  -- ∫_{Ioc 0 1} φ' = k  (FTC on log z)
  have hphi_int_eq : ∫ t in Set.Ioc (0 : ℝ) 1, (deriv γ t) 2 / (γ t) 2 = k := by
    have hderiv : ∀ t ∈ Set.uIcc (0 : ℝ) 1,
        HasDerivAt (fun s => Real.log ((γ s) 2)) ((deriv γ t) 2 / (γ t) 2) t := by
      intro t ht; rw [Set.uIcc_of_le (by norm_num)] at ht
      exact (deriv_coord (hγ.admissible.diff t ht) 2).log (ne_of_gt (hγ.admissible.mem t ht))
    have hii : IntervalIntegrable (fun t => (deriv γ t) 2 / (γ t) 2) volume 0 1 := by
      rw [intervalIntegrable_iff_integrableOn_Icc_of_le (by norm_num)]; exact phi_int
    have hftc := intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hii
    rw [intervalIntegral.integral_of_le (by norm_num)] at hftc
    have hclean : ∫ t in Set.Ioc (0 : ℝ) 1, (deriv γ t) 2 / (γ t) 2
        = Real.log ((γ 1) 2) - Real.log ((γ 0) 2) := hftc
    rw [hclean, hγ.admissible.target, hγ.admissible.source, zpt_height, zpt_height, hk]
  -- ∫_{Ioc 0 1} g = c
  have hg_int_eq : ∫ t in Set.Ioc (0 : ℝ) 1, speedFn γ t = c := by
    have hEq : Set.EqOn (speedFn γ) (fun _ => c) (Set.Ioc (0 : ℝ) 1) :=
      fun t ht => hgval t (Set.Ioc_subset_Icc_self ht)
    have hcongr : ∫ t in Set.Ioc (0 : ℝ) 1, speedFn γ t = ∫ _t in Set.Ioc (0 : ℝ) 1, c :=
      setIntegral_congr_fun measurableSet_Ioc hEq
    rw [hcongr, setIntegral_const, Real.volume_Ioc, sub_zero,
      ENNReal.toReal_ofReal (by norm_num), smul_eq_mul, one_mul]
  -- integrability on Ioc
  have hgIoc : IntegrableOn (speedFn γ) (Set.Ioc (0 : ℝ) 1) :=
    (speedFn_integrableOn hγ.admissible hLfin).mono_set Set.Ioc_subset_Icc_self
  have hpIoc : IntegrableOn (fun t => (deriv γ t) 2 / (γ t) 2) (Set.Ioc (0 : ℝ) 1) :=
    phi_int.mono_set Set.Ioc_subset_Icc_self
  have hmemIoc : ∀ᵐ t ∂(volume.restrict (Set.Ioc (0 : ℝ) 1)), t ∈ Set.Ioc (0 : ℝ) 1 :=
    ae_restrict_mem measurableSet_Ioc
  -- ### the a.e. core: horizontal collapse + φ' = k
  have hcore : ∀ᵐ t ∂(volume.restrict (Set.Ioc (0 : ℝ) 1)),
      ‖deriv γ t‖ = |(deriv γ t) 2| ∧ (deriv γ t) 2 / (γ t) 2 = k := by
    rcases le_or_lt 0 k with hkpos | hkneg
    · -- k ≥ 0:  g − φ' ≥ 0,  ∫ = c − k = |k| − k = 0
      have hnn : 0 ≤ᵐ[volume.restrict (Set.Ioc (0 : ℝ) 1)]
          (fun t => speedFn γ t - (deriv γ t) 2 / (γ t) 2) := by
        refine (ae_restrict_iff' measurableSet_Ioc).mpr (ae_of_all _ (fun t ht => ?_))
        have hle : (deriv γ t) 2 / (γ t) 2 ≤ speedFn γ t := by
          calc (deriv γ t) 2 / (γ t) 2 ≤ |(deriv γ t) 2 / (γ t) 2| := le_abs_self _
            _ ≤ |k| := hφ'_bd t (Set.Ioc_subset_Icc_self ht)
            _ = c := hc_eq.symm
            _ = speedFn γ t := (hgval t (Set.Ioc_subset_Icc_self ht)).symm
        linarith
      have hint0 : ∫ t in Set.Ioc (0 : ℝ) 1,
          (speedFn γ t - (deriv γ t) 2 / (γ t) 2) = 0 := by
        rw [integral_sub hgIoc hpIoc, hg_int_eq, hphi_int_eq, hc_eq, abs_of_nonneg hkpos]
        ring
      have hzero := (integral_eq_zero_iff_of_nonneg_ae hnn (hgIoc.sub hpIoc)).mp hint0
      filter_upwards [hzero, hmemIoc] with t ht htm
      have hz : (0 : ℝ) < (γ t) 2 := hγ.admissible.mem t (Set.Ioc_subset_Icc_self htm)
      have hzne : (γ t) 2 ≠ 0 := ne_of_gt hz
      have hgc : speedFn γ t = c := hgval t (Set.Ioc_subset_Icc_self htm)
      have hht : speedFn γ t - (deriv γ t) 2 / (γ t) 2 = 0 := ht
      have hpeq : (deriv γ t) 2 / (γ t) 2 = c := by rw [hgc] at hht; linarith
      have hn : ‖deriv γ t‖ = c * (γ t) 2 := by
        have hh : ‖deriv γ t‖ / (γ t) 2 = c := by simpa [speedFn] using hgc
        rw [div_eq_iff hzne] at hh; exact hh
      have hd2 : (deriv γ t) 2 = c * (γ t) 2 := (div_eq_iff hzne).mp hpeq
      have e2 : (deriv γ t) 2 = ‖deriv γ t‖ := by rw [hd2, hn]
      refine ⟨?_, ?_⟩
      · rw [e2, abs_of_nonneg (norm_nonneg _)]
      · rw [hpeq, hc_eq, abs_of_nonneg hkpos]
    · -- k < 0:  g + φ' ≥ 0,  ∫ = c + k = |k| + k = 0
      have hnn : 0 ≤ᵐ[volume.restrict (Set.Ioc (0 : ℝ) 1)]
          (fun t => speedFn γ t + (deriv γ t) 2 / (γ t) 2) := by
        refine (ae_restrict_iff' measurableSet_Ioc).mpr (ae_of_all _ (fun t ht => ?_))
        have hpb : |(deriv γ t) 2 / (γ t) 2| ≤ speedFn γ t := by
          calc |(deriv γ t) 2 / (γ t) 2| ≤ |k| := hφ'_bd t (Set.Ioc_subset_Icc_self ht)
            _ = c := hc_eq.symm
            _ = speedFn γ t := (hgval t (Set.Ioc_subset_Icc_self ht)).symm
        have hneg := neg_abs_le ((deriv γ t) 2 / (γ t) 2)
        linarith [neg_le_neg hpb]
      have hint0 : ∫ t in Set.Ioc (0 : ℝ) 1,
          (speedFn γ t + (deriv γ t) 2 / (γ t) 2) = 0 := by
        rw [integral_add hgIoc hpIoc, hg_int_eq, hphi_int_eq, hc_eq, abs_of_neg hkneg]
        ring
      have hzero := (integral_eq_zero_iff_of_nonneg_ae hnn (hgIoc.add hpIoc)).mp hint0
      filter_upwards [hzero, hmemIoc] with t ht htm
      have hz : (0 : ℝ) < (γ t) 2 := hγ.admissible.mem t (Set.Ioc_subset_Icc_self htm)
      have hzne : (γ t) 2 ≠ 0 := ne_of_gt hz
      have hgc : speedFn γ t = c := hgval t (Set.Ioc_subset_Icc_self htm)
      have hht : speedFn γ t + (deriv γ t) 2 / (γ t) 2 = 0 := ht
      have hpeq : (deriv γ t) 2 / (γ t) 2 = -c := by rw [hgc] at hht; linarith
      have hn : ‖deriv γ t‖ = c * (γ t) 2 := by
        have hh : ‖deriv γ t‖ / (γ t) 2 = c := by simpa [speedFn] using hgc
        rw [div_eq_iff hzne] at hh; exact hh
      have hd2 : (deriv γ t) 2 = -c * (γ t) 2 := (div_eq_iff hzne).mp hpeq
      have e2 : (deriv γ t) 2 = -‖deriv γ t‖ := by rw [hd2, hn]; ring
      refine ⟨?_, ?_⟩
      · rw [e2, abs_neg, abs_of_nonneg (norm_nonneg _)]
      · rw [hpeq, hc_eq, abs_of_neg hkneg, neg_neg]
  -- split the a.e. core
  have hphi_ae : ∀ᵐ t ∂(volume.restrict (Set.Ioc (0 : ℝ) 1)),
      (deriv γ t) 2 / (γ t) 2 = k := hcore.mono (fun t h => h.2)
  have hd0_ae : ∀ᵐ t ∂(volume.restrict (Set.Ioc (0 : ℝ) 1)), (deriv γ t) 0 = 0 :=
    hcore.mono (fun t h => (horiz_zero_of_norm_eq_abs (deriv γ t) h.1).1)
  have hd1_ae : ∀ᵐ t ∂(volume.restrict (Set.Ioc (0 : ℝ) 1)), (deriv γ t) 1 = 0 :=
    hcore.mono (fun t h => (horiz_zero_of_norm_eq_abs (deriv γ t) h.1).2)
  -- integrability of each coordinate derivative on Icc (dominated by |k|·z, continuous)
  have di_int : ∀ i : Fin 3, IntegrableOn (fun t => (deriv γ t) i) (Set.Icc (0 : ℝ) 1) := by
    intro i
    have hmeas : AEStronglyMeasurable (fun t => (deriv γ t) i)
        (volume.restrict (Set.Icc (0 : ℝ) 1)) :=
      ((coordCLM i).measurable.comp (measurable_deriv γ)).aestronglyMeasurable
    have hDcont : ContinuousOn (fun t => |k| * (γ t) 2) (Set.Icc (0 : ℝ) 1) :=
      continuousOn_const.mul ((coordCLM 2).continuous.comp_continuousOn hγc)
    have hDint : IntegrableOn (fun t => |k| * (γ t) 2) (Set.Icc (0 : ℝ) 1) :=
      hDcont.integrableOn_compact isCompact_Icc
    refine Integrable.mono' hDint hmeas ?_
    refine (ae_restrict_iff' measurableSet_Icc).mpr (ae_of_all _ (fun t ht => ?_))
    calc ‖(deriv γ t) i‖ = |(deriv γ t) i| := Real.norm_eq_abs _
      _ ≤ ‖deriv γ t‖ := abs_coord_le_norm _ i
      _ = |k| * (γ t) 2 := hnorm_eq t ht
  -- horizontal reconstruction: (γ τ) i = (zpt a) i for i with (γ')ᵢ = 0 a.e.
  have recon_zero : ∀ i : Fin 3,
      (∀ᵐ t ∂(volume.restrict (Set.Ioc (0 : ℝ) 1)), (deriv γ t) i = 0) →
      ∀ τ ∈ Set.Icc (0 : ℝ) 1, (γ τ) i = (zpt a) i := by
    intro i hzero τ hτ
    have hsub : Set.Ioc (0 : ℝ) τ ⊆ Set.Ioc (0 : ℝ) 1 := Set.Ioc_subset_Ioc_right hτ.2
    have hderiv : ∀ t ∈ Set.uIcc (0 : ℝ) τ,
        HasDerivAt (fun s => (γ s) i) ((deriv γ t) i) t := by
      intro t ht; rw [Set.uIcc_of_le hτ.1] at ht
      exact deriv_coord (hγ.admissible.diff t ⟨ht.1, ht.2.trans hτ.2⟩) i
    have hii : IntervalIntegrable (fun t => (deriv γ t) i) volume 0 τ := by
      rw [intervalIntegrable_iff_integrableOn_Icc_of_le hτ.1]
      exact (di_int i).mono_set (Set.Icc_subset_Icc_right hτ.2)
    have hftc := intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hii
    rw [intervalIntegral.integral_of_le hτ.1] at hftc
    have hclean : ∫ t in Set.Ioc (0 : ℝ) τ, (deriv γ t) i = (γ τ) i - (γ 0) i := hftc
    have haez : (fun t => (deriv γ t) i) =ᵐ[volume.restrict (Set.Ioc (0 : ℝ) τ)] 0 :=
      ae_restrict_of_ae_restrict_of_subset hsub hzero
    have hint0 : ∫ t in Set.Ioc (0 : ℝ) τ, (deriv γ t) i = 0 := by
      rw [integral_congr_ae haez]; simp
    have heq : (γ τ) i = (γ 0) i := by
      have := hclean.symm.trans hint0; linarith [this]
    rw [heq, hγ.admissible.source]
  -- height reconstruction: (γ τ)₂ = heightProfile a b τ
  have recon_z : ∀ τ ∈ Set.Icc (0 : ℝ) 1, (γ τ) 2 = heightProfile a b τ := by
    intro τ hτ
    have hsub : Set.Ioc (0 : ℝ) τ ⊆ Set.Ioc (0 : ℝ) 1 := Set.Ioc_subset_Ioc_right hτ.2
    have hderiv : ∀ t ∈ Set.uIcc (0 : ℝ) τ,
        HasDerivAt (fun s => Real.log ((γ s) 2)) ((deriv γ t) 2 / (γ t) 2) t := by
      intro t ht; rw [Set.uIcc_of_le hτ.1] at ht
      exact (deriv_coord (hγ.admissible.diff t ⟨ht.1, ht.2.trans hτ.2⟩) 2).log
        (ne_of_gt (hγ.admissible.mem t ⟨ht.1, ht.2.trans hτ.2⟩))
    have hii : IntervalIntegrable (fun t => (deriv γ t) 2 / (γ t) 2) volume 0 τ := by
      rw [intervalIntegrable_iff_integrableOn_Icc_of_le hτ.1]
      exact phi_int.mono_set (Set.Icc_subset_Icc_right hτ.2)
    have hftc := intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hii
    rw [intervalIntegral.integral_of_le hτ.1] at hftc
    have hclean : ∫ t in Set.Ioc (0 : ℝ) τ, (deriv γ t) 2 / (γ t) 2
        = Real.log ((γ τ) 2) - Real.log ((γ 0) 2) := hftc
    have haek : (fun t => (deriv γ t) 2 / (γ t) 2)
        =ᵐ[volume.restrict (Set.Ioc (0 : ℝ) τ)] (fun _ => k) :=
      ae_restrict_of_ae_restrict_of_subset hsub hphi_ae
    have hintk : ∫ t in Set.Ioc (0 : ℝ) τ, (deriv γ t) 2 / (γ t) 2 = τ * k := by
      have hcongr : ∫ t in Set.Ioc (0 : ℝ) τ, (deriv γ t) 2 / (γ t) 2
          = ∫ _t in Set.Ioc (0 : ℝ) τ, k := integral_congr_ae haek
      rw [hcongr, setIntegral_const, Real.volume_Ioc, sub_zero,
        ENNReal.toReal_ofReal hτ.1, smul_eq_mul]
    rw [hintk, hγ.admissible.source, zpt_height] at hclean
    -- hclean : τ * k = Real.log ((γ τ) 2) - Real.log a
    have hzτ : (0 : ℝ) < (γ τ) 2 := hγ.admissible.mem τ hτ
    have hlogτ : Real.log ((γ τ) 2) = logInterp a b τ := by
      rw [hk] at hclean; unfold logInterp; linarith [hclean]
    calc (γ τ) 2 = Real.exp (Real.log ((γ τ) 2)) := (Real.exp_log hzτ).symm
      _ = Real.exp (logInterp a b τ) := by rw [hlogτ]
      _ = heightProfile a b τ := rfl
  -- assemble the three coordinates
  intro τ hτ
  ext i
  fin_cases i
  · simpa [zpt, vseg, EuclideanSpace.single_apply] using recon_zero 0 hd0_ae τ hτ
  · simpa [zpt, vseg, EuclideanSpace.single_apply] using recon_zero 1 hd1_ae τ hτ
  · simpa only [vseg_height] using recon_z τ hτ

end QOU.Archimedean
