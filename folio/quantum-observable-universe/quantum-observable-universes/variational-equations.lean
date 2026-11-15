import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.variational_equations — Three variational equations

From δS_q = 0, three variational equations emerge:

1. Gravity: R_λ - ½ tr(R_λ) id_A = T_q[∇, ψ]  (Einstein)
2. Gauge: ∇ ⋆_q F_∇ + q · [F_∇, ⋆_q F_∇] = J_ψ  (Yang–Mills)
3. Matter: D_∇ ψ = 0  (transport)

LaTeX label: `prop:variational-equations`

## References

- [leitner2026] §1-quantum-observable-universe/variational-equations

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ

/-- The canonical indeterminate `q` of `R_q`. -/
def q_param : R_q := LaurentPolynomial.T 1

/-- The inverse indeterminate `q⁻¹` of `R_q`. -/
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- **Variational equations**: the three Euler–Lagrange equations
    from the unified categorical action S_q. -/
-- Ref: [leitner2026] §1
inductive VariationalEquationType
  | gravity    -- Einstein field equation
  | gauge      -- Yang–Mills equation
  | matter     -- Transport/Dirac equation

/-- **Variational equation data**: each equation relates a
    left-hand side (kinematic) to a right-hand side (source). -/
-- Ref: [leitner2026] §1
structure VariationalEquation where
  /-- The type of variational equation. -/
  eqType : VariationalEquationType
  /-- The substrate parameter q. (Positivity `0 < q` is archimedean and
      not meaningful over `R_q`; it is imposed after the
      substrate→archimedean specialisation `R_q → ℝ`.) -/
  q : R_q
  /-- The kinematic side (LHS). -/
  kinematic : R_q
  /-- The source side (RHS). -/
  source : R_q
  /-- The equation holds: LHS = RHS. -/
  equation : kinematic = source

/-- **The gravitational equation**: Einstein's equation with
    q-deformed stress-energy tensor. -/
-- Ref: [leitner2026] §1
structure GravitationalEquation extends VariationalEquation where
  /-- The Ricci curvature scalar. -/
  ricciScalar : R_q
  /-- The stress-energy trace. -/
  stressEnergyTrace : R_q
  /-- This is a gravity equation. -/
  is_gravity : eqType = .gravity

/-- **The gauge equation**: Yang–Mills with q-deformed nonlinear term. -/
-- Ref: [leitner2026] §1
structure GaugeEquation extends VariationalEquation where
  /-- The covariant divergence of the curvature. -/
  covDiv : R_q
  /-- The nonlinear q-correction: q · [F, ⋆F]. -/
  qCorrection : R_q
  /-- This is a gauge equation. -/
  is_gauge : eqType = .gauge

/-- **The matter equation**: parallel transport D_∇ ψ = 0. -/
-- Ref: [leitner2026] §1
structure MatterEquation extends VariationalEquation where
  /-- The matter field norm. -/
  fieldNorm : R_q
  /-- Source vanishes: the matter equation is D_∇ ψ = 0. -/
  source_zero : source = 0
  /-- This is a matter equation. -/
  is_matter : eqType = .matter

/-- The matter equation is purely kinematic (zero source). -/
-- Ref: [leitner2026] §1
theorem matter_eq_zero_source (m : MatterEquation) :
    m.kinematic = 0 := by
  rw [m.equation, m.source_zero]

/-- All three equations emerge from a single variational principle. -/
-- Ref: [leitner2026] §1
structure UnifiedAction where
  /-- The substrate parameter. (Positivity `0 < q` is archimedean and
      not meaningful over `R_q`; imposed after `R_q → ℝ`.) -/
  q : R_q
  /-- The three equations. -/
  gravity : GravitationalEquation
  gauge : GaugeEquation
  matter : MatterEquation
  /-- All share the same q. -/
  shared_q : gravity.q = q ∧ gauge.q = q ∧ matter.q = q

end

end QOU
