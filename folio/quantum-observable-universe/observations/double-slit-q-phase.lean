import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic


/-!
# QOU.Experimental.double_slit_q_phase

The q-deformed path phase for a double-slit geometry: the phase
accumulated along a path γ decomposes into a geometric (horizontal)
part weighted by q⁻¹ and a Reeb (vertical) part weighted by (1 − q⁻¹),
following directly from d_q = q⁻¹d + (1 − q⁻¹)π_V ∘ d.

LaTeX label: `def:double-slit-q-phase`

**Ground ring**: `ℝ` (archimedean realisation).
Evaluates formal results at q₀ ≈ 1.1098 for comparison with
experimental data. NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU.Experimental

/-- The q-deformed path phase along a path through a slit.
    Φ_q = q⁻¹ · Φ_geom + (1 − q⁻¹) · Φ_Reeb.

    LaTeX: `\label{def:double-slit-q-phase}`
    Ref: [leitner2026] Chapter 6, §Double-slit experiment -/
noncomputable def double_slit_q_phase (q : ℝ) (hq : q ≠ 0)
    (Phi_geom Phi_Reeb : ℝ) : ℝ :=
  q⁻¹ * Phi_geom + (1 - q⁻¹) * Phi_Reeb

/-- The q-deformed phase difference between two slit paths.
    ΔΦ_q = q⁻¹ · (2πd sin θ / λ) + (1 − q⁻¹) · Δφ_ξ -/
noncomputable def double_slit_q_phase_diff (q : ℝ) (hq : q ≠ 0)
    (d_slit lambda_ theta : ℝ) (Delta_phi_Reeb : ℝ) : ℝ :=
  q⁻¹ * (2 * Real.pi * d_slit * Real.sin theta / lambda_)
  + (1 - q⁻¹) * Delta_phi_Reeb

/-- At q = 1, the q-phase reduces to the geometric phase. -/
theorem double_slit_q_phase_classical (Phi_geom Phi_Reeb : ℝ) :
    double_slit_q_phase 1 one_ne_zero Phi_geom Phi_Reeb = Phi_geom := by
  simp [double_slit_q_phase, inv_one]

/-- At q = 1, the phase difference reduces to the standard Young formula. -/
theorem double_slit_q_phase_diff_classical (d_slit lambda_ theta Delta_phi_Reeb : ℝ) :
    double_slit_q_phase_diff 1 one_ne_zero d_slit lambda_ theta Delta_phi_Reeb
    = 2 * Real.pi * d_slit * Real.sin theta / lambda_ := by
  simp [double_slit_q_phase_diff, inv_one]

end QOU.Experimental
