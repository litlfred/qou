import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Group.Units.Basic


/-!
# Topological mass formula (algebraic, ℚ(q)-side)

The algebraic-side restatement of `conj:topological-mass-formula`:
the categorical mass of a closed braid factors as

  𝔪(β) = Φ₁(β) / ℏ_q²,    Φ₁(β) = τ_arch(Vol_q(β)),

with `Vol_q(β) ∈ ℤ[q^{±1/2}]` defined algebraically (no analytic
continuation, no volume-conjecture borrowing). The Archimedean
form `m(K) = Vol(K) / ℏ_{q₀}²` is the specialisation under
τ_arch at `q = q₀`.

Refs:
  prop:topological-mass-formula-algebraic
  conj:topological-mass-formula  (Archimedean version)
  def:algebraic-quantum-volume
  lem:tower-pair-equality-fixed-level
-/

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
      mass_alg = phi1 · ℏ_q⁻²
    is an equality in the coefficient ring, with the invertibility
    of `hbar_sq` carried explicitly as a **unit** `u : Rˣ` with
    `↑u = hbar_sq` (§7c: the `Units` form over `[CommRing R]`
    rather than `x ≠ 0` over a field — the ring the narrative names,
    `ℤ[q^{±1/2}]` localised at `ℏ_q`, is not a field).  Taking
    `R` a field and `u = Units.mk0 hbar_sq h` recovers the divided
    form `mass_alg = phi1 / hbar_sq`.  The Archimedean version
    `conj:topological-mass-formula` is the specialisation under
    `τ_arch` at `q = q₀`.

    Scope (2026-11-16): the mass formula enters as the hypothesis
    `h_phi1 : phi1 = mass_alg · ℏ_q²`; the theorem only multiplies by the
    inverse unit. It does not derive the formula, and none of the four
    `AlgebraicMassData` fields is tied to a braid. -/
-- Ref: [leitner2026] prop:topological-mass-formula-algebraic
theorem AlgebraicMassFormula
    {R : Type*} [CommRing R] (D : AlgebraicMassData R)
    (u : Rˣ) (hu : (u : R) = D.hbar_sq)
    (h_phi1 : D.phi1 = D.mass_alg * D.hbar_sq) :
    D.mass_alg = D.phi1 * ↑u⁻¹ := by
  rw [h_phi1, ← hu, mul_assoc, u.mul_inv, mul_one]

end QOU.Torsion
