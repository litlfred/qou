import Mathlib.Algebra.Algebra.Defs

/-!
# QOU.QuantumBlochGroup — the quantum Bloch group and the pentagon identity

The classical Bloch group `𝓑(ℂ)` is presented by the five-term relation
of the dilogarithm `Li₂`.  The **quantum Bloch group** `𝔅(q)(R)` replaces
this with the **pentagon identity** of the quantum dilogarithm `Φ_q`,

  `Φ_q(u) Φ_q(v) = Φ_q(v) Φ_q(u v) Φ_q(u)`,   where  `u v = q (v u)`,

i.e. the Yang–Baxter equation in exponential form.  The generating data
of the group is a pair `(u, v)` in an `R`-algebra satisfying the
quantum-torus relation `u v = q • (v u)` — the operator condition under
which the pentagon identity holds.  This is the algebraic (pre-archimedean)
object over a generic base ring `R`; the archimedean regulator
`𝔅(q) → ℝ` recovering the hyperbolic volume is a separate specialisation
(see the `observations` / archimedean blocks).

Base ring: generic `R` (AGENTS.md §7c) — the construction is purely
algebraic, with no `ℝ`-specific (ordering / radical / analytic) content.
-/

namespace QOU

/-- The **quantum Bloch group** `𝔅(q)(R)` generating datum: a
quantum-torus pair `(u, v)` in an `R`-algebra `A` satisfying
`u * v = q • (v * u)`.  This is exactly the relation under which the
quantum-dilogarithm pentagon identity
`Φ_q(u) Φ_q(v) = Φ_q(v) Φ_q(u v) Φ_q(u)` (Yang–Baxter in exponential
form) holds, and it linearises to the Hecke relation
`σ² = (q − q⁻¹) σ + 1` on the traced volumes. -/
structure QuantumBlochGroup (R : Type*) [CommRing R] (q : R)
    (A : Type*) [Ring A] [Algebra R A] where
  /-- First quantum-torus generator. -/
  u : A
  /-- Second quantum-torus generator. -/
  v : A
  /-- Quantum-torus relation `u v = q (v u)` driving the pentagon identity. -/
  quantum_torus : u * v = q • (v * u)

end QOU
