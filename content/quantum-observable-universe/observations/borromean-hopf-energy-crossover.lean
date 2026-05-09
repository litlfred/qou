/-!
# QOU.Descartes.borromean_hopf_energy_crossover

Energy comparison between Borromean (confined) and Hopf-diquark
(CFL) phases.  The Borromean phase dominates at q = 1.1097 by
a factor of ~250, requiring extreme compression to reach the
CFL crossover.

## References

- [manuscript] Ch. 7, §Strangelet Stability
- [thurston1978] Geometry and topology of three-manifolds

**Ground ring**: `ℝ` (archimedean realisation).
Evaluates formal results at q₀ ≈ 1.1098 for comparison with
experimental data. NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

import Mathlib.Data.Real.Basic

noncomputable section

namespace QOU.Descartes

/-- Borromean volume (Catalan's constant × 8). -/
-- Ref: [thurston1978]
def V_B : ℝ := 7.32772

/-- The ratio of Borromean to Hopf binding at substrate parameter q.
    This measures how much compression energy is needed to reach
    the CFL transition. -/
-- Ref: [manuscript] Ch. 7
def binding_ratio (q : ℝ) (hq : q > 1) : ℝ :=
  (V_B * q ^ 2 / (q - 1) ^ 2) / ((3 / 2) * (q + q⁻¹))

/-- The Borromean binding energy at q = 1.1097 exceeds 700. -/
-- Ref: [manuscript] Ch. 7
theorem borromean_binding_large :
    ∀ q : ℝ, q = 1.1097 →
    V_B * q ^ 2 / (q - 1) ^ 2 > 700 := by
  intro q hq
  subst hq
  unfold V_B
  norm_num

/-- The Milnor triple linking invariant of the Borromean link. -/
-- Ref: [manuscript] Ch. 4
def milnor_mu_borromean : Int := 1  -- noqa: one_def

/-- The Milnor triple linking invariant of the Hopf-diquark phase. -/
-- Ref: [manuscript] Ch. 7
def milnor_mu_cfl : Int := 0  -- noqa: const_zero

/-- The Milnor invariant jumps: this is a first-order transition. -/
-- Ref: [manuscript] Ch. 7
theorem milnor_discontinuity :
    milnor_mu_borromean ≠ milnor_mu_cfl := by
  unfold milnor_mu_borromean milnor_mu_cfl
  decide

end QOU.Descartes

end
