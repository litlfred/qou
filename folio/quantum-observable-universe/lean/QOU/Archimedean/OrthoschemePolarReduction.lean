/-
  H4-3: the POLAR REDUCTION — the joint between the two ends of `qou-w3eg` H4.

      H4-2  Vol(chimney T R)  =  ∫∫_T dA / (2(R² − x² − y²))        [#4827]
      H4-3  ∫∫_{orthoBase} …  =  ∫₀^ψ −¼ log((cos²φ − cos²ψ)/cos²φ) [HERE]
      H4-4  ∫₀^ψ …            =  ½ Λ(ψ)                              [#4842]

  Composing all three gives `hypVolume_chimney_orthoBase` at the bottom of this
  file: the hyperbolic volume of the chimney over ONE orthoscheme base triangle
  is `½Λ(ψ)`.  That is the first statement in the chain with a three-dimensional
  hyperbolic volume on the left and `Λ` on the right.

  **It is still not a statement about ideal tetrahedra.**  That a chimney over a
  triangle inscribed in the circle IS the ideal tetrahedron of the corresponding
  dihedral angles is Milnor's geometric identification, and it is untouched —
  Mathlib has no ideal tetrahedra.  Assembling six orthoschemes into
  `Λ(α)+Λ(β)+Λ(γ)` is H4-5 and is open; that is where the obtuse case (the
  circumcentre outside the triangle, one piece entering with a MINUS sign) has
  to be faced.

  THE BASE TRIANGLE IS DEFINED IN CARTESIAN COORDINATES, deliberately.  Polar is
  where the computation happens, but a polar-parameterised *definition* would
  assume what has to be proved — that the region is the one Milnor cuts out.
  `orthoBase R ψ` is the open Euclidean triangle with vertices

      (0, 0),  (R cos ψ, 0),  (R cos ψ, R sin ψ),

  i.e. the circumcentre, the foot of the perpendicular to a chord, and the point
  where that chord meets the circle of radius `R`.  `mem_orthoBase_polar` is then
  a THEOREM: in polar coordinates the same region is `0 < φ < ψ`,
  `0 < r < R cos ψ / cos φ` — the description the computation consumes, derived
  rather than posited.

  Note the radial integral is INDEPENDENT OF `R`: with `r₀ = R cos ψ / cos φ`,
  `(R² − r₀²)/R² = (cos²φ − cos²ψ)/cos²φ`.  That is H2's dilation invariance
  showing up in the base integral, and it is why H4-4 could be stated with no
  radius at all.

  Archimedean (ℝ): `cos`, `tan`, `log`, Lebesgue integration, ordering — §7c.

  -- Ref: [milnor1982] Appendix (the circumcentre subdivision)
  -- Ref: [thurston1978] Ch. 7
  -- Ref: [leitner2026] beans qou-w3eg (H4-3), qou-5gai (H4)
-/

import QOU.Archimedean.OrthoschemeBaseIntegral
import QOU.Archimedean.HyperbolicVolumeFubini
import Mathlib.Analysis.SpecialFunctions.PolarCoord

namespace QOU.Archimedean.HyperbolicVolume

open Real MeasureTheory intervalIntegral Set
open QOU.Archimedean QOU.Archimedean.IdealTetrahedronConcavity

/-! ### 1. The radial integral

Elementary, and the step that turns a two-dimensional integral into Milnor's
angular one.  The `r` in the numerator is the polar Jacobian, and it is exactly
what makes the radial primitive a logarithm. -/

/-- The radial integrand is continuous on `[0, r₀]` when `r₀ < R`, hence
interval-integrable there.  Unlike the angular integrand, there is no singularity
inside the interval: the chord stays strictly inside the circle. -/
theorem intervalIntegrable_radial {R r₀ : ℝ} (hR : 0 < R) (h0 : 0 ≤ r₀) (hlt : r₀ < R) :
    IntervalIntegrable (fun r : ℝ => r / (2 * (R ^ 2 - r ^ 2))) volume 0 r₀ := by
  refine ContinuousOn.intervalIntegrable ?_
  refine ContinuousOn.div continuousOn_id (by fun_prop) ?_
  intro r hr
  rw [Set.uIcc_of_le h0] at hr
  obtain ⟨hr0, hrr⟩ := hr
  have : 0 < R ^ 2 - r ^ 2 := by nlinarith
  positivity

/-- **`∫₀^{r₀} r dr / (2(R² − r²)) = −¼ log((R² − r₀²)/R²)`** for `0 ≤ r₀ < R`.

The polar Jacobian `r` against the density `1/(2(R²−r²))` integrates to a log —
which is why the angular integrand of the orthoscheme is a `log`, and hence why
`Λ` (the primitive of `−log(2 sin)`) is the answer at all. -/
theorem integral_radial {R r₀ : ℝ} (hR : 0 < R) (h0 : 0 ≤ r₀) (hlt : r₀ < R) :
    ∫ r in (0:ℝ)..r₀, r / (2 * (R ^ 2 - r ^ 2))
      = -(1/4 : ℝ) * Real.log ((R ^ 2 - r₀ ^ 2) / R ^ 2) := by
  have hpos : ∀ r ∈ Set.uIcc (0:ℝ) r₀, 0 < R ^ 2 - r ^ 2 := by
    intro r hr
    rw [Set.uIcc_of_le h0] at hr
    obtain ⟨hr0, hrr⟩ := hr
    nlinarith
  -- the primitive
  have hderiv : ∀ r ∈ Set.uIcc (0:ℝ) r₀,
      HasDerivAt (fun s : ℝ => -(1/4 : ℝ) * Real.log (R ^ 2 - s ^ 2))
        (r / (2 * (R ^ 2 - r ^ 2))) r := by
    intro r hr
    have hne : R ^ 2 - r ^ 2 ≠ 0 := ne_of_gt (hpos r hr)
    have hbase : HasDerivAt (fun s : ℝ => R ^ 2 - s ^ 2) (-(2 * r)) r := by
      simpa using ((hasDerivAt_pow 2 r).const_sub (R ^ 2))
    have hlog := (hbase.log hne).const_mul (-(1/4 : ℝ))
    have hval : -(1/4 : ℝ) * (-(2 * r) / (R ^ 2 - r ^ 2)) = r / (2 * (R ^ 2 - r ^ 2)) := by
      field_simp
      ring
    rw [hval] at hlog
    exact hlog
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv
    (intervalIntegrable_radial hR h0 hlt)]
  have hR2 : (0:ℝ) < R ^ 2 := by positivity
  rw [Real.log_div (ne_of_gt (by nlinarith : (0:ℝ) < R ^ 2 - r₀ ^ 2)) (ne_of_gt hR2)]
  simp
  ring

/-! ### 2. The base triangle, and its polar description

The definition is Cartesian; the polar description is proved. -/

/-- **The orthoscheme base triangle** — the OPEN Euclidean triangle with vertices
`(0,0)`, `(R cos ψ, 0)`, `(R cos ψ, R sin ψ)`: the circumcentre, the foot of the
perpendicular to a chord, and that chord's endpoint on the circle of radius `R`.

One of the six pieces Milnor's circumcentre subdivision cuts an inscribed
triangle into. -/
def orthoBase (R ψ : ℝ) : Set (ℝ × ℝ) :=
  {w | 0 < w.1 ∧ w.1 < R * Real.cos ψ ∧ 0 < w.2 ∧ w.2 < w.1 * Real.tan ψ}

theorem isOpen_orthoBase (R ψ : ℝ) : IsOpen (orthoBase R ψ) := by
  unfold orthoBase
  have h₁ : IsOpen {w : ℝ × ℝ | 0 < w.1} := isOpen_lt continuous_const continuous_fst
  have h₂ : IsOpen {w : ℝ × ℝ | w.1 < R * Real.cos ψ} := isOpen_lt continuous_fst continuous_const
  have h₃ : IsOpen {w : ℝ × ℝ | 0 < w.2} := isOpen_lt continuous_const continuous_snd
  have h₄ : IsOpen {w : ℝ × ℝ | w.2 < w.1 * Real.tan ψ} :=
    isOpen_lt continuous_snd (continuous_fst.mul continuous_const)
  simpa [Set.setOf_and, Set.inter_assoc] using
    ((h₁.inter h₂).inter (h₃.inter h₄))

theorem measurableSet_orthoBase (R ψ : ℝ) : MeasurableSet (orthoBase R ψ) :=
  (isOpen_orthoBase R ψ).measurableSet

/-- **The polar description of the base triangle** — proved, not assumed.

For `r > 0` and `φ ∈ (−π, π)`, the point `(r cos φ, r sin φ)` lies in the
triangle exactly when `0 < φ < ψ` and `r < R cos ψ / cos φ`.  This is the step
that would have been smuggled in by defining the region in polar coordinates. -/
theorem mem_orthoBase_polar {R ψ r φ : ℝ} (hψ0 : 0 < ψ) (hψ : ψ < π / 2)
    (hr : 0 < r) (hφ₁ : -π < φ) (hφ₂ : φ < π) :
    ((r * Real.cos φ, r * Real.sin φ) ∈ orthoBase R ψ)
      ↔ (0 < φ ∧ φ < ψ ∧ r < R * Real.cos ψ / Real.cos φ) := by
  have hπ : 0 < π := Real.pi_pos
  have hcosψ : 0 < Real.cos ψ := Real.cos_pos_of_mem_Ioo ⟨by linarith, hψ⟩
  have hsinψ : 0 < Real.sin ψ := Real.sin_pos_of_pos_of_lt_pi hψ0 (by linarith)
  -- The angular comparison used in both directions:
  -- `sin x cos ψ < cos x sin ψ ↔ x < ψ`, from strict monotonicity of `sin` on
  -- `[-π/2, π/2]` applied to `sin (x - ψ)` against `sin 0`.  The hypothesis
  -- `0 ≤ x` is what keeps `x - ψ` inside that interval.
  have hangle : ∀ {x : ℝ}, 0 ≤ x → x ≤ π / 2 →
      (Real.sin x * Real.cos ψ < Real.cos x * Real.sin ψ ↔ x < ψ) := by
    intro x hx₁ hx₂
    have hmem₁ : x - ψ ∈ Set.Icc (-(π / 2)) (π / 2) := ⟨by linarith, by linarith⟩
    have hmem₀ : (0 : ℝ) ∈ Set.Icc (-(π / 2)) (π / 2) := ⟨by linarith, by linarith⟩
    have hsub : Real.sin (x - ψ) = Real.sin x * Real.cos ψ - Real.cos x * Real.sin ψ :=
      Real.sin_sub x ψ
    have hiff := Real.strictMonoOn_sin.lt_iff_lt hmem₁ hmem₀
    rw [hsub, Real.sin_zero] at hiff
    constructor
    · intro h; have := hiff.mp (by linarith); linarith
    · intro h; have := hiff.mpr (by linarith); linarith
  constructor
  · rintro ⟨hx0, hxlt, hy0, hylt⟩
    -- restate the four defining inequalities without the `Prod` projections
    have hx0' : 0 < r * Real.cos φ := hx0
    have hxlt' : r * Real.cos φ < R * Real.cos ψ := hxlt
    have hy0' : 0 < r * Real.sin φ := hy0
    have hylt' : r * Real.sin φ < r * Real.cos φ * Real.tan ψ := hylt
    -- `r cos φ > 0` and `r sin φ > 0` place `φ` in the open first quadrant
    have hcosφ : 0 < Real.cos φ := by nlinarith
    have hsinφ : 0 < Real.sin φ := by nlinarith
    have hφpos : 0 < φ := by
      by_contra hle
      push_neg at hle
      exact absurd (Real.sin_nonpos_of_nonpos_of_neg_pi_le hle (by linarith)) (by linarith)
    have hφhalf : φ < π / 2 := by
      by_contra hle
      push_neg at hle
      exact absurd (Real.cos_nonpos_of_pi_div_two_le_of_le hle (by linarith)) (by linarith)
    refine ⟨hφpos, ?_, ?_⟩
    · -- `y < x tan ψ` IS the angular comparison, once `cos ψ` is cleared
      rw [Real.tan_eq_sin_div_cos,
        show r * Real.cos φ * (Real.sin ψ / Real.cos ψ)
          = r * Real.cos φ * Real.sin ψ / Real.cos ψ by ring,
        lt_div_iff₀ hcosψ] at hylt'
      exact (hangle hφpos.le hφhalf.le).mp (by nlinarith)
    · rw [lt_div_iff₀ hcosφ]
      linarith
  · rintro ⟨hφpos, hφψ, hrlt⟩
    have hcosφ : 0 < Real.cos φ := Real.cos_pos_of_mem_Ioo ⟨by linarith, by linarith⟩
    have hsinφ : 0 < Real.sin φ := Real.sin_pos_of_pos_of_lt_pi hφpos (by linarith)
    have hxlt : r * Real.cos φ < R * Real.cos ψ := by
      rw [lt_div_iff₀ hcosφ] at hrlt
      linarith
    have hcmp : Real.sin φ * Real.cos ψ < Real.cos φ * Real.sin ψ :=
      (hangle hφpos.le (by linarith)).mpr hφψ
    refine ⟨by positivity, hxlt, by positivity, ?_⟩
    show r * Real.sin φ < r * Real.cos φ * Real.tan ψ
    rw [Real.tan_eq_sin_div_cos,
      show r * Real.cos φ * (Real.sin ψ / Real.cos ψ)
        = r * Real.cos φ * Real.sin ψ / Real.cos ψ by ring,
      lt_div_iff₀ hcosψ]
    nlinarith


/-! ### 3. The radial mass in `ℝ≥0∞`

`hypVolume` integrates in `ℝ≥0∞`; the radial computation is Bochner.  This is the
same bridge H4-2 needed for the vertical fibre, now for the radial one — and, as
there, it is the integrand's honest integrability that licenses it. -/

/-- **The radial mass of one polar ray**, in `ℝ≥0∞`. -/
theorem lintegral_radial {R r₀ : ℝ} (hR : 0 < R) (h0 : 0 ≤ r₀) (hlt : r₀ < R) :
    ∫⁻ r in Set.Ioo 0 r₀, ENNReal.ofReal (r / (2 * (R ^ 2 - r ^ 2)))
      = ENNReal.ofReal (-(1/4 : ℝ) * Real.log ((R ^ 2 - r₀ ^ 2) / R ^ 2)) := by
  have hint : IntegrableOn (fun r : ℝ => r / (2 * (R ^ 2 - r ^ 2))) (Set.Ioo 0 r₀) volume :=
    ((intervalIntegrable_iff_integrableOn_Ioc_of_le h0).mp
      (intervalIntegrable_radial hR h0 hlt)).mono_set Set.Ioo_subset_Ioc_self
  have hnn : (0 : ℝ → ℝ) ≤ᵐ[volume.restrict (Set.Ioo 0 r₀)]
      fun r : ℝ => r / (2 * (R ^ 2 - r ^ 2)) := by
    filter_upwards [ae_restrict_mem measurableSet_Ioo] with r hr
    have hpos : 0 < R ^ 2 - r ^ 2 := by nlinarith [hr.1, hr.2]
    exact div_nonneg hr.1.le (by linarith)
  rw [← ofReal_integral_eq_lintegral_ofReal hint hnn, ← integral_Ioc_eq_integral_Ioo,
    ← intervalIntegral.integral_of_le h0, integral_radial hR h0 hlt]

/-! ### 4. H4-3 — the polar reduction

The change of variables itself.  Everything above is input; this is the theorem
that joins H4-2's two-dimensional base integral to H4-4's one-dimensional one. -/

/-- **H4-3 — the base integral over one orthoscheme triangle collapses to
Milnor's angular integral.**

    ∫∫_{orthoBase R ψ} dA / (2(R² − x² − y²))
        =  ∫₀^ψ −¼ log((cos²φ − cos²ψ)/cos²φ) dφ   ( = ½Λ(ψ), by H4-4 )

Three things happen here, and each is where the corresponding hypothesis is used:

* the polar change of variables (`lintegral_comp_polarCoord_symm`), whose
  Jacobian `r` is what makes the radial primitive a logarithm;
* Tonelli with the ANGLE outermost, so the inner integral is the radial one —
  the order Milnor computes in;
* the radial evaluation, whose upper limit `R cos ψ / cos φ` is `< R` exactly
  because `φ < ψ` (the chord stays inside the circle).

The right-hand side carries no `R`: the radial value depends on `r₀/R`, and
`r₀/R = cos ψ / cos φ`.  That is H2's dilation invariance visible in the base
integral. -/
theorem lintegral_orthoBase {R ψ : ℝ} (hR : 0 < R) (hψ0 : 0 < ψ) (hψ : ψ < π / 2) :
    ∫⁻ w in orthoBase R ψ, ENNReal.ofReal (1 / (2 * (R ^ 2 - w.1 ^ 2 - w.2 ^ 2)))
      = ENNReal.ofReal (Lob ψ / 2) := by
  classical
  have hπ : 0 < π := Real.pi_pos
  have hcosψ : 0 < Real.cos ψ := Real.cos_pos_of_mem_Ioo ⟨by linarith, hψ⟩
  set g : ℝ × ℝ → ENNReal :=
    fun w => ENNReal.ofReal (1 / (2 * (R ^ 2 - w.1 ^ 2 - w.2 ^ 2))) with hgdef
  have hgm : Measurable g := by
    refine ENNReal.measurable_ofReal.comp ?_
    fun_prop
  set f : ℝ × ℝ → ENNReal := (orthoBase R ψ).indicator g with hfdef
  have hfm : Measurable f := hgm.indicator (measurableSet_orthoBase R ψ)
  have hFm : Measurable fun p : ℝ × ℝ => ENNReal.ofReal p.1 * f (polarCoord.symm p) :=
    (ENNReal.measurable_ofReal.comp measurable_fst).mul
      (hfm.comp continuous_polarCoord_symm.measurable)
  -- (1) the set integral is an indicator integral, and (2) polar coordinates
  have step12 : ∫⁻ w in orthoBase R ψ, g w
      = ∫⁻ p in polarCoord.target, ENNReal.ofReal p.1 * f (polarCoord.symm p) := by
    rw [← lintegral_indicator (measurableSet_orthoBase R ψ) g, ← hfdef]
    simpa [smul_eq_mul] using (lintegral_comp_polarCoord_symm f).symm
  -- (3) Tonelli, ANGLE outermost
  have step3 : ∫⁻ p in polarCoord.target, ENNReal.ofReal p.1 * f (polarCoord.symm p)
      = ∫⁻ φ in Set.Ioo (-π) π, ∫⁻ r in Set.Ioi (0:ℝ),
          ENNReal.ofReal r * f (polarCoord.symm (r, φ)) := by
    rw [polarCoord_target,
      show (volume : Measure (ℝ × ℝ)).restrict (Set.Ioi 0 ×ˢ Set.Ioo (-π) π)
          = ((volume : Measure ℝ).restrict (Set.Ioi 0)).prod
              ((volume : Measure ℝ).restrict (Set.Ioo (-π) π)) by
        rw [Measure.prod_restrict, ← Measure.volume_eq_prod]]
    exact lintegral_prod_symm _ hFm.aemeasurable
  -- (4) the inner (radial) integral, angle by angle
  have hinner : Set.EqOn
      (fun φ => ∫⁻ r in Set.Ioi (0:ℝ), ENNReal.ofReal r * f (polarCoord.symm (r, φ)))
      ((Set.Ioo 0 ψ).indicator (fun φ => ENNReal.ofReal ((-(1/4 : ℝ)) *
        Real.log ((Real.cos φ ^ 2 - Real.cos ψ ^ 2) / Real.cos φ ^ 2))))
      (Set.Ioo (-π) π) := by
    intro φ hφ
    obtain ⟨hφ₁, hφ₂⟩ := hφ
    show ∫⁻ r in Set.Ioi (0:ℝ), ENNReal.ofReal r * f (polarCoord.symm (r, φ))
        = (Set.Ioo 0 ψ).indicator (fun φ => ENNReal.ofReal ((-(1/4 : ℝ)) *
            Real.log ((Real.cos φ ^ 2 - Real.cos ψ ^ 2) / Real.cos φ ^ 2))) φ
    by_cases hmem : φ ∈ Set.Ioo 0 ψ
    · obtain ⟨hφ0, hφψ⟩ := hmem
      have hcosφ : 0 < Real.cos φ := Real.cos_pos_of_mem_Ioo ⟨by linarith, by linarith⟩
      set r₀ : ℝ := R * Real.cos ψ / Real.cos φ with hr₀def
      have hr₀0 : 0 < r₀ := div_pos (mul_pos hR hcosψ) hcosφ
      have hcoslt : Real.cos ψ < Real.cos φ :=
        Real.cos_lt_cos_of_nonneg_of_le_pi hφ0.le (by linarith) hφψ
      have hr₀R : r₀ < R := by
        rw [hr₀def, div_lt_iff₀ hcosφ]
        nlinarith
      -- the radial integrand, off the region and on it
      have hcongr : ∀ r ∈ Set.Ioi (0:ℝ), ENNReal.ofReal r * f (polarCoord.symm (r, φ))
          = (Set.Ioo 0 r₀).indicator
              (fun r => ENNReal.ofReal (r / (2 * (R ^ 2 - r ^ 2)))) r := by
        intro r hr
        have hr0 : 0 < r := hr
        have hpolar : polarCoord.symm (r, φ) = (r * Real.cos φ, r * Real.sin φ) :=
          polarCoord_symm_apply (r, φ)
        by_cases hlt : r < r₀
        · have hin : polarCoord.symm (r, φ) ∈ orthoBase R ψ := by
            rw [hpolar]
            exact (mem_orthoBase_polar hψ0 hψ hr0 (by linarith) (by linarith)).mpr
              ⟨hφ0, hφψ, by rw [← hr₀def]; exact hlt⟩
          rw [hfdef, Set.indicator_of_mem hin, Set.indicator_of_mem (Set.mem_Ioo.mpr ⟨hr0, hlt⟩),
            hgdef, hpolar]
          have hsq : R ^ 2 - (r * Real.cos φ) ^ 2 - (r * Real.sin φ) ^ 2 = R ^ 2 - r ^ 2 := by
            have := Real.sin_sq_add_cos_sq φ
            nlinarith [this]
          simp only [hsq]
          rw [← ENNReal.ofReal_mul hr0.le]
          congr 1
          field_simp
        · have hnotin : polarCoord.symm (r, φ) ∉ orthoBase R ψ := by
            rw [hpolar]
            intro hcon
            have := (mem_orthoBase_polar hψ0 hψ hr0 (by linarith) (by linarith)).mp hcon
            rw [← hr₀def] at this
            exact hlt this.2.2
          rw [hfdef, Set.indicator_of_notMem hnotin,
            Set.indicator_of_notMem (by simp [Set.mem_Ioo, hlt]), mul_zero]
      rw [setLIntegral_congr_fun measurableSet_Ioi hcongr,
        setLIntegral_indicator measurableSet_Ioo,
        Set.inter_eq_self_of_subset_left (Set.Ioo_subset_Ioi_self),
        lintegral_radial hR hr₀0.le hr₀R,
        Set.indicator_of_mem (Set.mem_Ioo.mpr ⟨hφ0, hφψ⟩)]
      congr 2
      rw [hr₀def]
      field_simp
    · -- outside `(0, ψ)` nothing of the region lies over `φ`
      have hzero : ∀ r ∈ Set.Ioi (0:ℝ), ENNReal.ofReal r * f (polarCoord.symm (r, φ)) = 0 := by
        intro r hr
        have hr0 : 0 < r := hr
        have hnotin : polarCoord.symm (r, φ) ∉ orthoBase R ψ := by
          rw [polarCoord_symm_apply (r, φ)]
          intro hcon
          have := (mem_orthoBase_polar hψ0 hψ hr0 (by linarith) (by linarith)).mp hcon
          exact hmem (Set.mem_Ioo.mpr ⟨this.1, this.2.1⟩)
        rw [hfdef, Set.indicator_of_notMem hnotin, mul_zero]
      rw [setLIntegral_congr_fun measurableSet_Ioi hzero, lintegral_zero,
        Set.indicator_of_notMem hmem]
  -- (5) the outer (angular) integral
  rw [step12, step3, setLIntegral_congr_fun measurableSet_Ioo hinner,
    setLIntegral_indicator measurableSet_Ioo,
    Set.inter_eq_self_of_subset_left
      (Set.Ioo_subset_Ioo (by linarith) (by linarith))]
  -- the `∫⁻`/Bochner bridge, then H4-4
  have hnn : (0 : ℝ → ℝ) ≤ᵐ[volume.restrict (Set.Ioo 0 ψ)]
      fun φ => (-(1/4 : ℝ)) * Real.log ((Real.cos φ ^ 2 - Real.cos ψ ^ 2) / Real.cos φ ^ 2) := by
    filter_upwards [ae_restrict_mem measurableSet_Ioo] with φ hφ
    obtain ⟨hφ0, hφψ⟩ := hφ
    have hcosφ : 0 < Real.cos φ := Real.cos_pos_of_mem_Ioo ⟨by linarith, by linarith⟩
    have hcoslt : Real.cos ψ < Real.cos φ :=
      Real.cos_lt_cos_of_nonneg_of_le_pi hφ0.le (by linarith) hφψ
    have hu0 : 0 < (Real.cos φ ^ 2 - Real.cos ψ ^ 2) / Real.cos φ ^ 2 := by
      apply div_pos (by nlinarith) (by positivity)
    have hu1 : (Real.cos φ ^ 2 - Real.cos ψ ^ 2) / Real.cos φ ^ 2 ≤ 1 := by
      rw [div_le_one (by positivity)]
      nlinarith
    have hlog := Real.log_nonpos hu0.le hu1
    have hgoal : (0:ℝ) ≤ (-(1/4 : ℝ)) *
        Real.log ((Real.cos φ ^ 2 - Real.cos ψ ^ 2) / Real.cos φ ^ 2) := by nlinarith
    exact hgoal
  rw [← ofReal_integral_eq_lintegral_ofReal (integrableOn_orthoscheme hψ0 hψ) hnn,
    ← integral_Ioc_eq_integral_Ioo, ← intervalIntegral.integral_of_le hψ0.le,
    integral_orthoscheme hψ0 hψ]


/-! ### 5. The chimney over one orthoscheme base

Composing with H4-2 gives the first statement in this chain relating a
THREE-dimensional hyperbolic volume to `Λ`. -/

/-- The open base triangle lies strictly inside the disk.

Its third vertex `(R cos ψ, R sin ψ)` is ON the circle, but the triangle is open,
so no point of it is: `x² + y² < x²(1 + tan²ψ) = x²/cos²ψ < R²`.  This is the
pointwise disk hypothesis H4-2's corollary wants, so the a.e. form is not needed
for a single orthoscheme — it will be, for the closed triangle H4-5 assembles. -/
theorem orthoBase_subset_disk {R ψ : ℝ} (hR : 0 < R) (hψ0 : 0 < ψ) (hψ : ψ < π / 2) :
    ∀ w ∈ orthoBase R ψ, w.1 ^ 2 + w.2 ^ 2 < R ^ 2 := by
  rintro w ⟨hx0, hxlt, hy0, hylt⟩
  have hπ : 0 < π := Real.pi_pos
  have hcosψ : 0 < Real.cos ψ := Real.cos_pos_of_mem_Ioo ⟨by linarith, hψ⟩
  have hpyth := Real.sin_sq_add_cos_sq ψ
  have htan : Real.tan ψ = Real.sin ψ / Real.cos ψ := Real.tan_eq_sin_div_cos ψ
  rw [htan] at hylt
  -- `y < x sin ψ / cos ψ`, so `y cos ψ < x sin ψ`
  have hy' : w.2 * Real.cos ψ < w.1 * Real.sin ψ := by
    rw [show w.1 * (Real.sin ψ / Real.cos ψ) = w.1 * Real.sin ψ / Real.cos ψ by ring,
      lt_div_iff₀ hcosψ] at hylt
    exact hylt
  -- then `(x² + y²) cos²ψ < x² (cos²ψ + sin²ψ) = x² < (R cos ψ)²`
  have ha : 0 ≤ w.2 * Real.cos ψ := by positivity
  have hsq : (w.2 * Real.cos ψ) ^ 2 < (w.1 * Real.sin ψ) ^ 2 := by
    have h := mul_self_lt_mul_self ha hy'
    nlinarith [h]
  have hcos2 : 0 < Real.cos ψ ^ 2 := by positivity
  have hx2 : w.1 ^ 2 < R ^ 2 * Real.cos ψ ^ 2 := by nlinarith
  nlinarith [hsq, hx2, hpyth, hcos2]

/-- **The hyperbolic volume of the chimney over one orthoscheme base triangle
is `½Λ(ψ)`.**

The first statement in this chain with a THREE-dimensional hyperbolic volume on
the left and `Λ` on the right.  H4-2 collapses the solid to its base integral,
H4-3 turns that into Milnor's angular integral, H4-4 evaluates it.

**This is not a statement about an ideal tetrahedron.**  It says that a
particular region of `H³` — the region above the radius-`R` hemisphere over an
open Euclidean right triangle — has hyperbolic volume `½Λ(ψ)`.  That such a
chimney over a triangle INSCRIBED in the circle IS the ideal tetrahedron with
dihedral angles `(α,β,γ)` is Milnor's geometric identification, and it is
untouched: Mathlib has no ideal tetrahedra.  Assembling six of these into
`Λ(α)+Λ(β)+Λ(γ)` is H4-5, also open — and that step is where the obtuse case
(circumcentre outside the triangle, one piece entering with a minus sign) finally
has to be faced. -/
theorem hypVolume_chimney_orthoBase {R ψ : ℝ} (hR : 0 < R) (hψ0 : 0 < ψ) (hψ : ψ < π / 2) :
    hypVolume (chimney (orthoBase R ψ) R) = ENNReal.ofReal (Lob ψ / 2) := by
  rw [hypVolume_chimney_of_subset_disk (measurableSet_orthoBase R ψ)
      (orthoBase_subset_disk hR hψ0 hψ),
    lintegral_orthoBase hR hψ0 hψ]

end QOU.Archimedean.HyperbolicVolume
