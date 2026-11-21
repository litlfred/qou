/-
# HyperbolicMetricSeparation.lean (T2, WALL / metric axiom) — the HORIZONTAL half
# of separation, so that `dH` is a CERTIFIED metric.

`HyperbolicMetric` proves the *vertical* half of separation unconditionally
(`dH_eq_zero_height`: `dH x y = 0 → y₂ = x₂`, via the FTC applied to `log z`).
This file closes the *horizontal* half (bean `qou-v8u3`): `dH x y = 0` forces the
horizontal coordinates to agree too, hence `x = y`.  With `dH_self`, `dH_comm`,
`dH_triangle` (all on `HyperbolicMetric`) this makes `dH` a genuine metric —
NOT the conjectural `HypMinimizerUnique` route, which is the sibling z-axis
approach; this half is unconditional.

## Mathematical content (the height-controlled horizontal bound)

For an admissible `γ : x → y` of finite hyperbolic length `L := (pathLenH γ).toReal`
and any coordinate `i`:

    |y i − x i| = |∫₀¹ (γ' t) i dt| ≤ ∫₀¹ |(γ' t) i| dt ≤ ∫₀¹ ‖γ' t‖ dt.

Writing `g t := ‖γ' t‖ / z t` (the integrand of `pathLenH`, so `∫ g = L`), the
Euclidean bound `|(γ' t) i| ≤ ‖γ' t‖ = g t · z t` and the **height ceiling**
`z t ≤ x₂ · e^L` (FTC on `[0,t]` for `log z`, exactly the upper companion of
`dH_ge_logHeight`) give the pointwise domination `|(γ' t) i| ≤ (x₂ e^L) · g t`,
hence

    |y i − x i| ≤ (x₂ e^L) · ∫₀¹ g = (x₂ e^L) · L .

`dH x y = 0` means `L` can be made arbitrarily small over admissible paths;
`r ↦ x₂ e^r r → 0` as `r → 0⁺`, so `|y i − x i| = 0`.  No geodesic-uniqueness
hypothesis; the argument is the calculus-of-variations lower bound run on the
horizontal coordinate rather than the height.

Archimedean (ℝ): `exp`, `log`, `‖·‖`, ordering `0 < z` — §7c.

  -- Ref: [thurston1978] Ch. 2 §2.3 p. 12 (the metric `ds² = (dx²+dy²+dz²)/z²`)
  -- Ref: [ratcliffe] §4.6 (the upper half-space distance is a metric)
  -- Ref: [leitner2026] beans qou-v8u3 (horizontal separation), qou-322e (metric walls)
-/

import QOU.Archimedean.HyperbolicMetric

namespace QOU.Archimedean.HyperbolicMetric

open MeasureTheory Set
open scoped ENNReal

/-! ### Shared integrability packaging for a finite-length admissible path

The FTC arguments (height ceiling, horizontal bound) both need: the speed
integrand `g = ‖γ'‖/z` is integrable on `Icc 0 1` and its integral is the real
length `L`.  We package it once. -/

/-- The **real hyperbolic length** of a path: `(pathLenH γ).toReal`. -/
noncomputable def realLen (γ : ℝ → E) : ℝ := (pathLenH γ 0 1).toReal

/-- The speed integrand `g t = ‖γ' t‖ / (γ t)₂` whose lintegral is `pathLenH`. -/
noncomputable def speedFn (γ : ℝ → E) : ℝ → ℝ := fun t => ‖deriv γ t‖ / (γ t) 2

theorem speedFn_nonneg {γ : ℝ → E} {x y : E} (hγ : AdmissiblePath γ x y)
    {t : ℝ} (ht : t ∈ Set.Icc (0:ℝ) 1) : 0 ≤ speedFn γ t :=
  div_nonneg (norm_nonneg _) (le_of_lt (hγ.mem t ht))

/-- The speed integrand is a.e.-strongly-measurable on `Icc 0 1`. -/
theorem speedFn_aesm {γ : ℝ → E} {x y : E} (hγ : AdmissiblePath γ x y) :
    AEStronglyMeasurable (speedFn γ) (volume.restrict (Set.Icc (0:ℝ) 1)) := by
  have hγc : ContinuousOn γ (Set.Icc (0:ℝ) 1) :=
    fun t ht => (hγ.diff t ht).continuousAt.continuousWithinAt
  have hheightC : ContinuousOn (fun t => (γ t) 2) (Set.Icc (0:ℝ) 1) :=
    (coordCLM 2).continuous.comp_continuousOn hγc
  have hnumNorm : AEStronglyMeasurable (fun t => ‖deriv γ t‖)
      (volume.restrict (Set.Icc (0:ℝ) 1)) := ((measurable_deriv γ).norm).aestronglyMeasurable
  have hden : AEStronglyMeasurable (fun t => (γ t) 2)
      (volume.restrict (Set.Icc (0:ℝ) 1)) := hheightC.aestronglyMeasurable measurableSet_Icc
  exact (hnumNorm.aemeasurable.div hden.aemeasurable).aestronglyMeasurable

/-- On a finite-length admissible path, the speed integrand is integrable on
`Icc 0 1`. -/
theorem speedFn_integrableOn {γ : ℝ → E} {x y : E} (hγ : AdmissiblePath γ x y)
    (hL : pathLenH γ 0 1 ≠ ∞) : IntegrableOn (speedFn γ) (Set.Icc (0:ℝ) 1) := by
  refine ⟨speedFn_aesm hγ, ?_⟩
  have hgnn : 0 ≤ᵐ[volume.restrict (Set.Icc (0:ℝ) 1)] speedFn γ :=
    (ae_restrict_iff' measurableSet_Icc).mpr (ae_of_all _ (fun t ht => speedFn_nonneg hγ ht))
  rw [hasFiniteIntegral_iff_ofReal hgnn]
  -- pathLenH γ = ∫⁻ ofReal (speedFn γ) on Icc, which is < ∞
  have : ∫⁻ t in Set.Icc (0:ℝ) 1, ENNReal.ofReal (speedFn γ t) = pathLenH γ 0 1 := rfl
  rw [this]; exact lt_top_iff_ne_top.mpr hL

/-- `∫_{Ioc 0 1} g ≥ 0`. -/
theorem integral_speedFn_nonneg {γ : ℝ → E} {x y : E} (hγ : AdmissiblePath γ x y) :
    0 ≤ ∫ t in Set.Ioc (0:ℝ) 1, speedFn γ t :=
  setIntegral_nonneg measurableSet_Ioc
    (fun _t ht => speedFn_nonneg hγ (Set.Ioc_subset_Icc_self ht))

/-- **`realLen γ = ∫_{Ioc 0 1} g`** — the real length is the Bochner integral of the
speed (the `ofReal`↔`lintegral` bridge). -/
theorem realLen_eq_integral {γ : ℝ → E} {x y : E} (hγ : AdmissiblePath γ x y)
    (hL : pathLenH γ 0 1 ≠ ∞) :
    realLen γ = ∫ t in Set.Ioc (0:ℝ) 1, speedFn γ t := by
  have hgintIoc : IntegrableOn (speedFn γ) (Set.Ioc (0:ℝ) 1) :=
    (speedFn_integrableOn hγ hL).mono_set Set.Ioc_subset_Icc_self
  have hgnnIoc : 0 ≤ᵐ[volume.restrict (Set.Ioc (0:ℝ) 1)] speedFn γ :=
    (ae_restrict_iff' measurableSet_Ioc).mpr
      (ae_of_all _ (fun t ht => speedFn_nonneg hγ (Set.Ioc_subset_Icc_self ht)))
  have hbridge : ENNReal.ofReal (∫ t in Set.Ioc (0:ℝ) 1, speedFn γ t) = pathLenH γ 0 1 := by
    rw [ofReal_integral_eq_lintegral_ofReal hgintIoc hgnnIoc]
    exact MeasureTheory.setLIntegral_congr Ioc_ae_eq_Icc
  rw [realLen, ← hbridge, ENNReal.toReal_ofReal (integral_speedFn_nonneg hγ)]

/-! ### The height ceiling `z t ≤ x₂ · e^L` -/

/-- **Height ceiling (upper companion of `dH_ge_logHeight`).**  On a finite-length
admissible path, the height stays below `x₂ · e^L`: `(γ s)₂ ≤ (x)₂ · exp (realLen γ)`
for every `s ∈ [0,1]`.  Proof: FTC on `[0,s]` for `log∘z` gives
`log z(s) − log z(0) = ∫₀ˢ z'/z ≤ ∫₀ˢ ‖γ'‖/z ≤ ∫₀¹ g = L`, then exponentiate. -/
theorem height_le {γ : ℝ → E} {x y : E} (hγ : AdmissiblePath γ x y)
    (hL : pathLenH γ 0 1 ≠ ∞) {s : ℝ} (hs : s ∈ Set.Icc (0:ℝ) 1) :
    (γ s) 2 ≤ (x) 2 * Real.exp (realLen γ) := by
  set g : ℝ → ℝ := speedFn γ with hg
  set φ' : ℝ → ℝ := fun t => (deriv γ t) 2 / (γ t) 2 with hφ'
  set φ : ℝ → ℝ := fun t => Real.log ((γ t) 2) with hφ
  have hs0 : 0 ≤ s := hs.1
  have hs1 : s ≤ 1 := hs.2
  have hx2 : 0 < (x) 2 := by have := hγ.mem 0 ⟨le_refl _, by norm_num⟩; rwa [hγ.source] at this
  -- integrable pieces on Icc 0 1
  have hgint : IntegrableOn g (Set.Icc (0:ℝ) 1) := speedFn_integrableOn hγ hL
  -- φ' measurability + domination |φ'| ≤ g
  have hnumCoord : AEStronglyMeasurable (fun t => (deriv γ t) 2)
      (volume.restrict (Set.Icc (0:ℝ) 1)) :=
    (((coordCLM 2).measurable.comp (measurable_deriv γ)).aestronglyMeasurable)
  have hγc : ContinuousOn γ (Set.Icc (0:ℝ) 1) :=
    fun t ht => (hγ.diff t ht).continuousAt.continuousWithinAt
  have hden : AEStronglyMeasurable (fun t => (γ t) 2)
      (volume.restrict (Set.Icc (0:ℝ) 1)) :=
    ((coordCLM 2).continuous.comp_continuousOn hγc).aestronglyMeasurable measurableSet_Icc
  have hφ'm : AEStronglyMeasurable φ' (volume.restrict (Set.Icc (0:ℝ) 1)) :=
    (hnumCoord.aemeasurable.div hden.aemeasurable).aestronglyMeasurable
  have hbound : ∀ t ∈ Set.Icc (0:ℝ) 1, ‖φ' t‖ ≤ g t := by
    intro t ht
    have hz : 0 < (γ t) 2 := hγ.mem t ht
    rw [hg, speedFn, hφ', Real.norm_eq_abs, abs_div, abs_of_pos hz, div_le_div_iff_of_pos_right hz]
    exact abs_coord_le_norm _ 2
  have hφ'int : IntegrableOn φ' (Set.Icc (0:ℝ) 1) :=
    Integrable.mono' hgint hφ'm
      ((ae_restrict_iff' measurableSet_Icc).mpr (ae_of_all _ hbound))
  -- restrict to Icc 0 s
  have hsub : Set.Icc (0:ℝ) s ⊆ Set.Icc (0:ℝ) 1 := Set.Icc_subset_Icc_right hs1
  have hφ'intS : IntegrableOn φ' (Set.Icc (0:ℝ) s) := hφ'int.mono_set hsub
  -- FTC on [0,s]
  have hderiv : ∀ t ∈ Set.uIcc (0:ℝ) s, HasDerivAt φ (φ' t) t := by
    intro t ht
    rw [Set.uIcc_of_le hs0] at ht
    exact (deriv_coord (hγ.diff t (hsub ht)) 2).log (ne_of_gt (hγ.mem t (hsub ht)))
  have hii : IntervalIntegrable φ' volume 0 s := by
    rw [intervalIntegrable_iff_integrableOn_Icc_of_le hs0]; exact hφ'intS
  have hftc : ∫ t in (0:ℝ)..s, φ' t = φ s - φ 0 :=
    intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hii
  -- ∫_0^s φ' = ∫_{Ioc 0 s} φ' ≤ ∫_{Ioc 0 s} g ≤ ∫_{Ioc 0 1} g = L
  have hIoc : ∫ t in (0:ℝ)..s, φ' t = ∫ t in Set.Ioc (0:ℝ) s, φ' t :=
    intervalIntegral.integral_of_le hs0
  have hgintIocS : IntegrableOn g (Set.Ioc (0:ℝ) s) :=
    hgint.mono_set (Set.Ioc_subset_Icc_self.trans hsub)
  have hφ'intIocS : IntegrableOn φ' (Set.Ioc (0:ℝ) s) :=
    hφ'intS.mono_set Set.Ioc_subset_Icc_self
  have hgintIoc1 : IntegrableOn g (Set.Ioc (0:ℝ) 1) :=
    hgint.mono_set Set.Ioc_subset_Icc_self
  have hstep1 : ∫ t in Set.Ioc (0:ℝ) s, φ' t ≤ ∫ t in Set.Ioc (0:ℝ) s, g t := by
    refine setIntegral_mono_on hφ'intIocS hgintIocS measurableSet_Ioc (fun t ht => ?_)
    have := hbound t (Set.Ioc_subset_Icc_self.trans hsub ht)
    calc φ' t ≤ |φ' t| := le_abs_self _
      _ = ‖φ' t‖ := (Real.norm_eq_abs _).symm
      _ ≤ g t := this
  have hstep2 : ∫ t in Set.Ioc (0:ℝ) s, g t ≤ ∫ t in Set.Ioc (0:ℝ) 1, g t := by
    refine setIntegral_mono_set hgintIoc1 ?_ ?_
    · exact (ae_restrict_iff' measurableSet_Ioc).mpr
        (ae_of_all _ (fun t ht => speedFn_nonneg hγ (Set.Ioc_subset_Icc_self ht)))
    · exact (Set.Ioc_subset_Ioc_right hs1).eventuallyLE
  have hLr : ∫ t in Set.Ioc (0:ℝ) 1, g t = realLen γ := (realLen_eq_integral hγ hL).symm
  have hchain : φ s - φ 0 ≤ realLen γ := by
    rw [← hftc, hIoc, ← hLr]; exact le_trans hstep1 hstep2
  -- exponentiate: log z(s) ≤ log x₂ + L
  have hφ0 : φ 0 = Real.log ((x) 2) := by rw [hφ]; simp only []; rw [hγ.source]
  have hlogle : Real.log ((γ s) 2) ≤ Real.log ((x) 2) + realLen γ := by
    have : φ s ≤ φ 0 + realLen γ := by linarith [hchain]
    rw [hφ0] at this; exact this
  have hzs : 0 < (γ s) 2 := hγ.mem s hs
  calc (γ s) 2 = Real.exp (Real.log ((γ s) 2)) := (Real.exp_log hzs).symm
    _ ≤ Real.exp (Real.log ((x) 2) + realLen γ) := Real.exp_le_exp.mpr hlogle
    _ = Real.exp (Real.log ((x) 2)) * Real.exp (realLen γ) := Real.exp_add _ _
    _ = (x) 2 * Real.exp (realLen γ) := by rw [Real.exp_log hx2]

/-! ### The horizontal displacement bound -/

/-- **Horizontal displacement bound.**  On a finite-length admissible path, for any
coordinate `i`, `|y i − x i| ≤ (x₂ · e^L) · L` with `L = realLen γ`.  The height
ceiling `height_le` dominates the coordinate derivative by `(x₂ e^L)·g`, and the
FTC on coordinate `i` turns the displacement into `∫ (γ' )i`. -/
theorem horizDisplacement_le {γ : ℝ → E} {x y : E} (hγ : AdmissiblePath γ x y)
    (hL : pathLenH γ 0 1 ≠ ∞) (i : Fin 3) :
    |(y) i - (x) i| ≤ (x) 2 * Real.exp (realLen γ) * realLen γ := by
  set g : ℝ → ℝ := speedFn γ with hg
  set C : ℝ := (x) 2 * Real.exp (realLen γ) with hC
  have hx2 : 0 < (x) 2 := by have := hγ.mem 0 ⟨le_refl _, by norm_num⟩; rwa [hγ.source] at this
  have hCpos : 0 < C := mul_pos hx2 (Real.exp_pos _)
  have hgint : IntegrableOn g (Set.Icc (0:ℝ) 1) := speedFn_integrableOn hγ hL
  have hgintIoc : IntegrableOn g (Set.Ioc (0:ℝ) 1) := hgint.mono_set Set.Ioc_subset_Icc_self
  -- the coordinate derivative d/dt (γ t) i
  set di : ℝ → ℝ := fun t => (deriv γ t) i with hdi
  have hdiAesm : AEStronglyMeasurable di (volume.restrict (Set.Icc (0:ℝ) 1)) :=
    (((coordCLM i).measurable.comp (measurable_deriv γ)).aestronglyMeasurable)
  -- pointwise domination: |di t| ≤ C · g t  on Icc
  have hdom : ∀ t ∈ Set.Icc (0:ℝ) 1, ‖di t‖ ≤ (fun t => C * g t) t := by
    intro t ht
    have hz : 0 < (γ t) 2 := hγ.mem t ht
    have hcoord : |(deriv γ t) i| ≤ ‖deriv γ t‖ := abs_coord_le_norm _ i
    have hgz : g t * (γ t) 2 = ‖deriv γ t‖ := by
      rw [hg, speedFn, div_mul_cancel₀ _ (ne_of_gt hz)]
    have hzle : (γ t) 2 ≤ C := by rw [hC]; exact height_le hγ hL ht
    have hgnn : 0 ≤ g t := speedFn_nonneg hγ ht
    calc ‖di t‖ = |(deriv γ t) i| := by rw [hdi, Real.norm_eq_abs]
      _ ≤ ‖deriv γ t‖ := hcoord
      _ = g t * (γ t) 2 := hgz.symm
      _ ≤ g t * C := by apply mul_le_mul_of_nonneg_left hzle hgnn
      _ = C * g t := by ring
  have hCgint : IntegrableOn (fun t => C * g t) (Set.Icc (0:ℝ) 1) := hgint.const_mul C
  have hdiint : IntegrableOn di (Set.Icc (0:ℝ) 1) :=
    Integrable.mono' hCgint hdiAesm
      ((ae_restrict_iff' measurableSet_Icc).mpr (ae_of_all _ hdom))
  have hdiintIoc : IntegrableOn di (Set.Ioc (0:ℝ) 1) := hdiint.mono_set Set.Ioc_subset_Icc_self
  -- FTC on coordinate i: ∫_0^1 di = (γ · i) 1 - (γ · i) 0 = y i - x i
  have hderiv : ∀ t ∈ Set.uIcc (0:ℝ) 1, HasDerivAt (fun s => (γ s) i) (di t) t := by
    intro t ht
    rw [Set.uIcc_of_le (by norm_num)] at ht
    exact deriv_coord (hγ.diff t ht) i
  have hii : IntervalIntegrable di volume 0 1 := by
    rw [intervalIntegrable_iff_integrableOn_Icc_of_le (by norm_num)]; exact hdiint
  have hftc : ∫ t in (0:ℝ)..1, di t = (γ 1) i - (γ 0) i :=
    intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hii
  have hIoc : ∫ t in (0:ℝ)..1, di t = ∫ t in Set.Ioc (0:ℝ) 1, di t :=
    intervalIntegral.integral_of_le (by norm_num)
  -- assemble the bound
  have hyx : (y) i - (x) i = ∫ t in Set.Ioc (0:ℝ) 1, di t := by
    rw [← hIoc, hftc, hγ.target, hγ.source]
  rw [hyx, ← Real.norm_eq_abs]
  calc ‖∫ t in Set.Ioc (0:ℝ) 1, di t‖ ≤ ∫ t in Set.Ioc (0:ℝ) 1, ‖di t‖ :=
        norm_integral_le_integral_norm _
    _ ≤ ∫ t in Set.Ioc (0:ℝ) 1, C * g t := by
        refine setIntegral_mono_on hdiintIoc.norm (hgintIoc.const_mul C) measurableSet_Ioc
          (fun t ht => hdom t (Set.Ioc_subset_Icc_self ht))
    _ = C * ∫ t in Set.Ioc (0:ℝ) 1, g t := integral_const_mul C g
    _ = C * realLen γ := by rw [← realLen_eq_integral hγ hL]
    _ = (x) 2 * Real.exp (realLen γ) * realLen γ := by rw [hC]

/-! ### Horizontal separation, and `dH` as a certified metric -/

/-- For `r ∈ [0,1]` and `A > 0`: `A · e^r · r ≤ A · e · r`.  (Monotone majorant used
in the limit.) -/
theorem majorant_le {A r : ℝ} (hA : 0 ≤ A) (hr0 : 0 ≤ r) (hr1 : r ≤ 1) :
    A * Real.exp r * r ≤ A * Real.exp 1 * r := by
  have hle : Real.exp r ≤ Real.exp 1 := Real.exp_le_exp.mpr hr1
  have h1 : A * Real.exp r ≤ A * Real.exp 1 := mul_le_mul_of_nonneg_left hle hA
  exact mul_le_mul_of_nonneg_right h1 hr0

/-- **Horizontal separation (bean `qou-v8u3`).**  `dH x y = 0` forces every
coordinate of `x` and `y` to agree.  For the height coordinate this is
`dH_eq_zero_height`; here we run the calculus-of-variations bound on coordinate
`i`: for every admissible `γ`, `|y i − x i| ≤ (x₂ e^L)·L`, and `dH x y = 0` lets
`L → 0`, so `|y i − x i| = 0`. -/
theorem dH_eq_zero_coord {x y : E} (hx : x ∈ upperH) (h : dH x y = 0) (i : Fin 3) :
    (y) i = (x) i := by
  have hx2 : 0 < (x) 2 := hx
  -- it suffices to show |y i − x i| ≤ ε for every ε > 0
  have hkey : ∀ ε : ℝ, 0 < ε → |(y) i - (x) i| ≤ ε := by
    intro ε hε
    -- choose δ ∈ (0,1] with (x₂·e)·δ ≤ ε
    set A : ℝ := (x) 2 * Real.exp 1 with hA
    have hApos : 0 < A := mul_pos hx2 (Real.exp_pos _)
    set δ : ℝ := min 1 (ε / A) with hδ
    have hδpos : 0 < δ := lt_min one_pos (div_pos hε hApos)
    have hδ1 : δ ≤ 1 := min_le_left _ _
    have hδA : A * δ ≤ ε := by
      have : δ ≤ ε / A := min_le_right _ _
      calc A * δ ≤ A * (ε / A) := mul_le_mul_of_nonneg_left this (le_of_lt hApos)
        _ = ε := by field_simp
    -- from dH = 0 < ofReal δ, get an admissible γ with pathLenH γ < ofReal δ
    have hcpos : (0 : ℝ≥0∞) < ENNReal.ofReal δ := ENNReal.ofReal_pos.mpr hδpos
    have hexists : ∃ γ, ∃ _ : AdmissiblePath γ x y, pathLenH γ 0 1 < ENNReal.ofReal δ := by
      by_contra hcon
      push_neg at hcon
      have hle : ENNReal.ofReal δ ≤ dH x y := le_iInf₂ hcon
      rw [h] at hle
      exact absurd hle (not_le.mpr hcpos)
    obtain ⟨γ, hγ, hlt⟩ := hexists
    have hLfin : pathLenH γ 0 1 ≠ ∞ := ne_top_of_lt (hlt.trans_le le_top)
    -- realLen γ < δ  and ≥ 0
    have hLnn : 0 ≤ realLen γ := ENNReal.toReal_nonneg
    have hLlt : realLen γ < δ := by
      have := (ENNReal.toReal_lt_toReal hLfin (ENNReal.ofReal_ne_top)).mpr hlt
      rwa [ENNReal.toReal_ofReal (le_of_lt hδpos)] at this
    have hLle1 : realLen γ ≤ 1 := le_of_lt (hLlt.trans_le hδ1)
    -- bound the coordinate displacement
    have hbound := horizDisplacement_le hγ hLfin i
    have hmaj : (x) 2 * Real.exp (realLen γ) * realLen γ ≤ A * realLen γ := by
      rw [hA]; exact majorant_le (le_of_lt hx2) hLnn hLle1
    have hmono : A * realLen γ ≤ A * δ := mul_le_mul_of_nonneg_left (le_of_lt hLlt) (le_of_lt hApos)
    calc |(y) i - (x) i| ≤ (x) 2 * Real.exp (realLen γ) * realLen γ := hbound
      _ ≤ A * realLen γ := hmaj
      _ ≤ A * δ := hmono
      _ ≤ ε := hδA
  -- |y i − x i| ≤ 0, hence = 0
  have hnonpos : |(y) i - (x) i| ≤ 0 := by
    by_contra hpos
    push_neg at hpos
    have hhalf := hkey (|(y) i - (x) i| / 2) (by linarith)
    linarith
  have habs0 : |(y) i - (x) i| = 0 := le_antisymm hnonpos (abs_nonneg _)
  exact sub_eq_zero.mp (abs_eq_zero.mp habs0)

/-- **Full separation — `dH` is a certified metric.**  `dH x y = 0 → x = y`,
combining every coordinate via `dH_eq_zero_coord` (which covers the height
coordinate too — the vertical FTC bound is the special case `i = 2`).  Together
with `dH_self`, `dH_comm`, `dH_triangle`, and `dH_nonneg` (all on `HyperbolicMetric`)
this is the full `ℝ≥0∞`-valued metric axiom set for `dH`, DERIVED — unconditional,
independent of the `HypMinimizerUnique` conjecture. -/
theorem dH_eq_zero_eq {x y : E} (hx : x ∈ upperH) (h : dH x y = 0) : x = y := by
  ext i
  exact (dH_eq_zero_coord hx h i).symm

end QOU.Archimedean.HyperbolicMetric
