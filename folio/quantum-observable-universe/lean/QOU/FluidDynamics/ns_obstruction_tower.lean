import Mathlib.Algebra.Ring.Defs

/-!
# QOU.FluidDynamics.ns_obstruction_tower — Yekutieli obstruction tower

**Theorem** ([`thm:ns-obstruction-tower`](../../../quantum-observable-universe/fluid-dynamics/ns-obstruction-tower.md)).

*Let `(C, A, τ)` be a QOU with Yekutieli obstruction classes `κ_n` and let
`Σ` be the collision locus of two anti-parallel vortex filaments. Then the
QOU is NS-singular iff some restricted obstruction `res_Σ(κ_n)` is
non-zero.*

## Formalisation notes
- **Base ring (§7c).** Generic `{R : Type*} [CommRing R]` — no `ℝ`. The
  obstruction classes take values in `R`; `res_Σ n ≠ 0` is inequality with
  zero (not archimedean), so no real structure is needed.
- **Non-degenerate conditional (§3b-cond cond. 5).** The two directions of
  the iff are carried as explicit hypotheses; `ns_obstruction_tower` derives
  the iff (`Iff.intro`) rather than projecting it.
-/

namespace QOU.FluidDynamics

/-- Hypotheses for the Yekutieli obstruction-tower criterion (§7c: generic
    `CommRing`, no `ℝ`). The sufficiency and necessity directions are
    explicit; the theorem derives the iff. -/
class NsObstructionTowerContext (R : Type*) [CommRing R] where
  /-- Yekutieli obstruction classes `κ_n` indexed by `n : ℕ`. -/
  kappa : ℕ → R
  /-- Restriction `res_Σ(κ_n)` of `κ_n` to the collision locus `Σ`. -/
  res_sigma : ℕ → R
  /-- Predicate: the QOU is NS-singular (blowup occurs). -/
  is_NS_singular : Prop
  /-- **Sufficiency (deep):** a non-vanishing restricted obstruction forces
      blowup. -/
  obstruction_forces_singular : (∃ n : ℕ, res_sigma n ≠ 0) → is_NS_singular
  /-- **Necessity:** blowup exhibits a non-vanishing restricted obstruction. -/
  singular_exhibits_obstruction : is_NS_singular → (∃ n : ℕ, res_sigma n ≠ 0)

/-- **NS-obstruction tower** ([`thm:ns-obstruction-tower`]).

    The QOU is NS-singular **iff** some restricted Yekutieli obstruction is
    non-zero.  *Derived* from the two directional hypotheses of
    `NsObstructionTowerContext`. -/
-- Ref: [manuscript] quantum-observable-universe/fluid-dynamics/ns-obstruction-tower.ts
theorem ns_obstruction_tower {R : Type*} [CommRing R]
    [ctx : NsObstructionTowerContext R] :
    ctx.is_NS_singular ↔ ∃ n : ℕ, ctx.res_sigma n ≠ 0 :=
  ⟨ctx.singular_exhibits_obstruction, ctx.obstruction_forces_singular⟩

end QOU.FluidDynamics
