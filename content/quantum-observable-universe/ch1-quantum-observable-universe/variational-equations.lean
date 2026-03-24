/-!
# QOU.variational_equations — Three variational equations

From δS_q = 0, three variational equations emerge:

1. Gravity: R_λ - ½ tr(R_λ) id_A = T_q[∇, ψ]  (Einstein)
2. Gauge: ∇ ⋆_q F_∇ + q · [F_∇, ⋆_q F_∇] = J_ψ  (Yang–Mills)
3. Matter: D_∇ ψ = 0  (transport)

LaTeX label: `prop:variational-equations`

## References

- [manuscript] §1-quantum-observable-universe/variational-equations
-/

import Mathlib.Data.Real.Basic

namespace QOU

/-- **Variational equations**: the three Euler–Lagrange equations
    from the unified categorical action S_q. -/
-- Ref: [manuscript] §1
inductive VariationalEquationType
  | gravity    -- Einstein field equation
  | gauge      -- Yang–Mills equation
  | matter     -- Transport/Dirac equation

/-- **Variational equation data**: each equation relates a
    left-hand side (kinematic) to a right-hand side (source). -/
-- Ref: [manuscript] §1
structure VariationalEquation where
  /-- The type of variational equation. -/
  eqType : VariationalEquationType
  /-- The substrate parameter q. -/
  q : ℝ
  /-- q > 0. -/
  q_pos : 0 < q
  /-- The kinematic side (LHS). -/
  kinematic : ℝ
  /-- The source side (RHS). -/
  source : ℝ
  /-- The equation holds: LHS = RHS. -/
  equation : kinematic = source

/-- **The gravitational equation**: Einstein's equation with
    q-deformed stress-energy tensor. -/
-- Ref: [manuscript] §1
structure GravitationalEquation extends VariationalEquation where
  /-- The Ricci curvature scalar. -/
  ricciScalar : ℝ
  /-- The stress-energy trace. -/
  stressEnergyTrace : ℝ
  /-- This is a gravity equation. -/
  is_gravity : eqType = .gravity

/-- **The gauge equation**: Yang–Mills with q-deformed nonlinear term. -/
-- Ref: [manuscript] §1
structure GaugeEquation extends VariationalEquation where
  /-- The covariant divergence of the curvature. -/
  covDiv : ℝ
  /-- The nonlinear q-correction: q · [F, ⋆F]. -/
  qCorrection : ℝ
  /-- This is a gauge equation. -/
  is_gauge : eqType = .gauge

/-- **The matter equation**: parallel transport D_∇ ψ = 0. -/
-- Ref: [manuscript] §1
structure MatterEquation extends VariationalEquation where
  /-- The matter field norm. -/
  fieldNorm : ℝ
  /-- Source vanishes: the matter equation is D_∇ ψ = 0. -/
  source_zero : source = 0
  /-- This is a matter equation. -/
  is_matter : eqType = .matter

/-- The matter equation is purely kinematic (zero source). -/
-- Ref: [manuscript] §1
theorem matter_eq_zero_source (m : MatterEquation) :
    m.kinematic = 0 := by
  rw [m.equation, m.source_zero]

/-- All three equations emerge from a single variational principle. -/
-- Ref: [manuscript] §1
structure UnifiedAction where
  /-- The substrate parameter. -/
  q : ℝ
  /-- q > 0. -/
  q_pos : 0 < q
  /-- The three equations. -/
  gravity : GravitationalEquation
  gauge : GaugeEquation
  matter : MatterEquation
  /-- All share the same q. -/
  shared_q : gravity.q = q ∧ gauge.q = q ∧ matter.q = q

end QOU
