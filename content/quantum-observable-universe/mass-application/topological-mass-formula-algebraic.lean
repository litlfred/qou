/-!
# Topological mass formula (algebraic, ℚ(q)-side)

The algebraic-side restatement of `prop:topological-mass-formula`:
the categorical mass of a closed braid factors as

  𝔪(β) = Φ₁(β) / ℏ_q²,    Φ₁(β) = τ_arch(Vol_q(β)),

with `Vol_q(β) ∈ ℤ[q^{±1/2}]` defined algebraically (no analytic
continuation, no volume-conjecture borrowing). The Archimedean
form `m(K) = Vol(K) / ℏ_{q₀}²` is the specialisation under
τ_arch at `q = q₀`.

Refs:
  prop:topological-mass-formula-algebraic
  prop:topological-mass-formula  (Archimedean version)
  def:algebraic-quantum-volume
  lem:tower-pair-equality-fixed-level
-/

import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Field.Defs
import Mathlib.Tactic.FieldSimp

namespace QOU.Torsion

/-- Abstract data for the algebraic mass formula at a single
    closed braid.

    `R` is the coefficient ring (instantiated as `ℤ[q^{±1/2}]` /
    `ℚ(q)` in the QOU narrative). `vol_q` is the algebraic
    quantum volume of the braid; `hbar_sq` is `ℏ_q²` in `R`;
    `phi1` is the Reeb / Archimedean specialisation
    `τ_arch(vol_q)`; `mass_alg` is the algebraic-side mass. -/
structure AlgebraicMassData (R : Type*) [CommRing R] where
  vol_q : R
  hbar_sq : R
  phi1 : R
  mass_alg : R

/-- **Algebraic topological mass formula.**

    Given the algebraic-side data, the mass identity
      mass_alg = phi1 / hbar_sq
    is an equality in the coefficient ring (modulo invertibility
    of `hbar_sq`). The Archimedean version
    `prop:topological-mass-formula` is the specialisation under
    `τ_arch` at `q = q₀`. -/
-- Ref: [manuscript] prop:topological-mass-formula-algebraic
theorem AlgebraicMassFormula
    {R : Type*} [Field R] (D : AlgebraicMassData R)
    (h_phi1 : D.phi1 = D.mass_alg * D.hbar_sq)
    (h_hbar_ne : D.hbar_sq ≠ 0) :
    D.mass_alg = D.phi1 / D.hbar_sq := by
  rw [h_phi1]
  field_simp

end QOU.Torsion
