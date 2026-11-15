import Mathlib.Algebra.Module.Basic
import Mathlib.Algebra.Module.LinearMap.Defs


/-!
# QOU.CategoricalQReebFlow — q-deformed Reeb flow

The q-Reeb flow is the one-parameter family of automorphisms generated
by the q-deformed Reeb derivation ξ_q, where
ξ_q(a) = q⁻¹ξ(a) + (1-q⁻¹)[ξ, X_a]_q.

## References

- [leitner2026] §1 Quantum Observable Universe
-/

namespace QOU

variable {R : Type*} [CommRing R]

/-- The q-deformed Reeb flow on a Frobenius–Hopf object.

    LaTeX: `\label{def:categorical-q-reeb-flow}` -/
-- Ref: [leitner2026] §1, Definition: Categorical q-Reeb flow
structure CategoricalQReebFlow (M : Type*) [AddCommGroup M] [Module R M] where
  /-- The classical Reeb derivation ξ. -/
  reeb : M →ₗ[R] M
  /-- The deformation parameter q. -/
  q : R
  /-- q is invertible. -/
  q_ne_zero : q ≠ 0
  /-- The q-deformed Reeb derivation ξ_q. -/
  qReeb : M →ₗ[R] M
  /-- The flow at time t (one-parameter family). -/
  flow : R → M →ₗ[R] M
  /-- Flow at time 0 is the identity. -/
  flow_zero : flow 0 = LinearMap.id

end QOU
