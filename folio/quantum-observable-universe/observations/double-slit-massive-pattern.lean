import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic


/-!
# QOU.Experimental.double_slit_massive_pattern

Massive-particle interference pattern: the q-deformed double-slit
intensity pattern with q-corrected fringe spacing and envelope width.
At q = 1 the standard Fraunhofer pattern is recovered.

LaTeX label: `prop:double-slit-massive-pattern`

## References
- [bach2013] https://doi.org/10.1088/1367-2630/15/3/033018
- [leitner2026] Ch. 7, §double-slit-massive-pattern

**Ground ring**: `ℝ` (archimedean realisation).
Evaluates formal results at q₀ ≈ 1.1098 for comparison with
experimental data. NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU.Experimental

/-- The q-deformed interference phase difference.
    ΔΦ_q(θ) = q⁻¹ · (2π d sin θ / λ) + (1 − q⁻¹) · Δφ_ξ(θ). -/
noncomputable def interference_phase (q : ℝ) (hq : q ≠ 0)
    (d_slit lambda_ theta Delta_phi_Reeb : ℝ) : ℝ :=
  q⁻¹ * (2 * Real.pi * d_slit * Real.sin theta / lambda_)
  + (1 - q⁻¹) * Delta_phi_Reeb

/-- The q-deformed envelope parameter.
    β_q(θ) = q⁻¹ · (π a sin θ / λ) + (1 − q⁻¹)² · β_ξ(θ). -/
noncomputable def envelope_param (q : ℝ) (hq : q ≠ 0)
    (a_slit lambda_ theta beta_Reeb : ℝ) : ℝ :=
  q⁻¹ * (Real.pi * a_slit * Real.sin theta / lambda_)
  + (1 - q⁻¹)^2 * beta_Reeb

/-- The q-corrected fringe spacing: Δy_q = q λ L / d. -/
noncomputable def fringe_spacing (q lambda_ L d_slit : ℝ) : ℝ :=
  q * lambda_ * L / d_slit

/-- The q-corrected envelope half-width:
    w_q = q² λ L / a · (1 + (1 − q⁻¹)² · (⟨Δ_ξ⟩/⟨Δ⟩)). -/
noncomputable def envelope_width (q : ℝ) (hq : q ≠ 0)
    (lambda_ L a_slit ratio_Reeb_spatial : ℝ) : ℝ :=
  q^2 * lambda_ * L / a_slit * (1 + (1 - q⁻¹)^2 * ratio_Reeb_spatial)

/-- At q = 1 the q-deformed intensity reduces to the standard
    Fraunhofer double-slit pattern: the fringe spacing is λL/d. -/
-- Ref: [leitner2026] Ch. 7, §double-slit-massive-pattern
theorem double_slit_massive_pattern_classical_fringe
    (lambda_ L d_slit : ℝ) :
    fringe_spacing 1 lambda_ L d_slit = lambda_ * L / d_slit := by
  unfold fringe_spacing
  ring

/-- At q = 1 the interference phase reduces to the standard
    Young formula: ΔΦ₁ = 2π d sin θ / λ. -/
-- Ref: [leitner2026] Ch. 7, §double-slit-massive-pattern
theorem double_slit_massive_pattern_classical_phase
    (d_slit lambda_ theta Delta_phi_Reeb : ℝ) :
    interference_phase 1 one_ne_zero d_slit lambda_ theta Delta_phi_Reeb
    = 2 * Real.pi * d_slit * Real.sin theta / lambda_ := by
  simp [interference_phase, inv_one]

/-- At q = 1 the envelope parameter reduces to the Fraunhofer form:
    β₁ = π a sin θ / λ. -/
-- Ref: [leitner2026] Ch. 7, §double-slit-massive-pattern
theorem double_slit_massive_pattern_classical_envelope
    (a_slit lambda_ theta beta_Reeb : ℝ) :
    envelope_param 1 one_ne_zero a_slit lambda_ theta beta_Reeb
    = Real.pi * a_slit * Real.sin theta / lambda_ := by
  simp [envelope_param, inv_one]

/-- **Massive-particle interference: the envelope is wider than Fraunhofer**
    in the physical substrate regime `q > 1`.

    The classical (`q = 1`) fringe spacing `λL/a` is strictly smaller than
    the `q`-corrected envelope half-width
    `w_q = q²·(λL/a)·(1 + (1 − q⁻¹)²·⟨Δ_ξ⟩/⟨Δ⟩)`, because `q² > 1` and the
    Reeb-broadening factor `1 + (1 − q⁻¹)²·ratio ≥ 1`. This is the excess
    width of order `(1 − q⁻¹)²` observed in precision electron/molecular
    diffraction. Proved directly (no axiom): the previous
    `double_slit_massive_pattern_axiom` asserted the claim for the wrong
    regime (`q ≠ 0, q ≠ 1`), where it is in fact false for `q ∈ (0,1)`
    with small `ratio`. The physical substrate has `q > 1`. -/
-- Ref: [bach2013] Controlled double-slit electron diffraction — see folio/schema/references.ts
-- Ref: [leitner2026] Ch. 7, §double-slit-massive-pattern
theorem double_slit_massive_pattern (q : ℝ) (hq : q ≠ 0) (hq1 : 1 < q)
    (lambda_ L a_slit : ℝ) (ha : a_slit ≠ 0)
    (hpos : 0 < lambda_ * L / a_slit)
    (ratio_Reeb_spatial : ℝ) (hr : 0 < ratio_Reeb_spatial) :
    fringe_spacing 1 lambda_ L a_slit <
    envelope_width q hq lambda_ L a_slit ratio_Reeb_spatial := by
  unfold fringe_spacing envelope_width
  have hq0 : 0 < q := by linarith
  -- The classical LHS `1·λL/a` and the RHS `q²·λL/a·K` share the factor `λL/a > 0`.
  have hlhs : (1 : ℝ) * lambda_ * L / a_slit = lambda_ * L / a_slit := by ring
  have hrhs : q ^ 2 * lambda_ * L / a_slit
        * (1 + (1 - q⁻¹) ^ 2 * ratio_Reeb_spatial)
      = (lambda_ * L / a_slit)
        * (q ^ 2 * (1 + (1 - q⁻¹) ^ 2 * ratio_Reeb_spatial)) := by ring
  rw [hlhs, hrhs]
  -- It remains to show `X < X · (q²·K)` with `X > 0` and `q²·K > 1`.
  have hq2 : 1 < q ^ 2 := by nlinarith
  have hK0 : 0 ≤ (1 - q⁻¹) ^ 2 * ratio_Reeb_spatial :=
    mul_nonneg (sq_nonneg _) (le_of_lt hr)
  have hfac : 1 < q ^ 2 * (1 + (1 - q⁻¹) ^ 2 * ratio_Reeb_spatial) := by
    have hprod : 0 ≤ q ^ 2 * ((1 - q⁻¹) ^ 2 * ratio_Reeb_spatial) :=
      mul_nonneg (le_of_lt (by positivity : (0 : ℝ) < q ^ 2)) hK0
    nlinarith [hq2, hprod]
  calc lambda_ * L / a_slit
      = (lambda_ * L / a_slit) * 1 := by ring
    _ < (lambda_ * L / a_slit)
          * (q ^ 2 * (1 + (1 - q⁻¹) ^ 2 * ratio_Reeb_spatial)) :=
        mul_lt_mul_of_pos_left hfac hpos

end QOU.Experimental
