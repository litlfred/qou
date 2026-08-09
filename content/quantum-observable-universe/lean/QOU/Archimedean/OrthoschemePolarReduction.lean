/-
  H4-3 (the two inputs): the ORTHOSCHEME BASE TRIANGLE and the RADIAL INTEGRAL.

  H4-3 is the joint between the two ends of `qou-w3eg` H4:

      H4-2  Vol(chimney T R)  =  ∫∫_T dA / (2(R² − x² − y²))        [done, #4827]
      H4-3  ∫∫_{orthoBase} …  =  ∫₀^ψ −¼ log((cos²φ − cos²ψ)/cos²φ) [OPEN]
      H4-4  ∫₀^ψ …            =  ½ Λ(ψ)                              [done, #4842]

  **H4-3 IS NOT CLOSED BY THIS FILE.**  What is here is its two inputs — the
  region, and the radial integral — plus the polar description of the region,
  which is the step most easily got wrong.  The change of variables itself (the
  `lintegral_comp_polarCoord_symm` application and the Tonelli split) is not
  proved; no theorem below equates a two-dimensional integral with a
  one-dimensional one.

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
  -- Ref: [manuscript] beans qou-w3eg (H4-3), qou-5gai (H4)
-/

import QOU.Archimedean.OrthoschemeBaseIntegral
import Mathlib.Analysis.SpecialFunctions.PolarCoord

namespace QOU.Archimedean.HyperbolicVolume

open Real MeasureTheory intervalIntegral Set
open QOU.Archimedean QOU.Archimedean.IdealTetrahedronConcavity

/-! ### 1. The radial integral

Elementary, and the step that turns a two-dimensional integral into Milnor's
angular one.  The `r` in the numerator is the polar Jacobian, and it is exactly
what makes the radial primitive a logarithm. -/

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
  have hcont : IntervalIntegrable (fun r : ℝ => r / (2 * (R ^ 2 - r ^ 2))) volume 0 r₀ := by
    refine ContinuousOn.intervalIntegrable ?_
    refine ContinuousOn.div continuousOn_id (by fun_prop) ?_
    intro r hr
    have := hpos r hr
    positivity
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hcont]
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

end QOU.Archimedean.HyperbolicVolume
