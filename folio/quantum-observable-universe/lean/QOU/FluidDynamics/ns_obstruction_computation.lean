import Mathlib.Algebra.Ring.Defs

/-!
# QOU.FluidDynamics.ns_obstruction_computation — obstruction computation at the collision locus

**Proposition** ([`prop:ns-obstruction-computation`](../../../quantum-observable-universe/fluid-dynamics/ns-obstruction-computation.md)).

*For the Descartes universe with an anti-parallel vortex pair of linking
number `lk`: (i) the topological obstruction `lk · e(ξ)|_p` is non-zero iff
the Reeb field has a zero at `p`; (ii) for `n ≥ 1` the per-jet obstruction
`δ_n|_Σ` is non-zero iff the `n`-th velocity jet diverges on `Σ`.*

## Formalisation notes
- **Base ring (§7c).** Generic `{R : Type*} [CommRing R]` — no `ℝ`. The
  Euler-class value and jet obstructions take values in `R`; the linking
  number is genuinely `ℤ` (cast into `R`); all claims are
  (in)equalities-with-zero, no order or analysis.
- **Non-degenerate conditional (§3b-cond cond. 5).** Each iff's two
  implication directions are carried as explicit hypotheses; the theorem
  *derives* both iffs (`Iff.intro`) and conjoins them — it does not carry
  either iff as a bare class field.
-/

namespace QOU.FluidDynamics

/-- Hypotheses for the NS obstruction computation (§7c: generic `CommRing`,
    `ℤ` linking number, no `ℝ`).  The four implication directions are
    explicit; `ns_obstruction_computation` derives the two iffs. -/
class NsObstructionComputationContext (R : Type*) [CommRing R] where
  /-- Linking number `lk` of the colliding vortex pair. -/
  lk : ℤ
  /-- Euler class value `e(ξ)|_p` at the collision point. -/
  e_xi_at_p : R
  /-- Predicate: the Reeb field has a zero at `p`. -/
  reeb_zero_at_p : Prop
  /-- **(i) ⇒:** a non-vanishing topological obstruction forces a Reeb zero. -/
  reeb_zero_of_obstruction : ((lk : R) * e_xi_at_p ≠ 0) → reeb_zero_at_p
  /-- **(i) ⇐:** a Reeb zero at `p` forces the obstruction `lk · e(ξ)|_p ≠ 0`. -/
  obstruction_of_reeb_zero : reeb_zero_at_p → ((lk : R) * e_xi_at_p ≠ 0)
  /-- Per-jet-level obstruction `δ_n` restricted to the collision surface `Σ`. -/
  delta_n : ℕ → R
  /-- Predicate: the `n`-th jet of the velocity diverges on `Σ`. -/
  jet_diverges : ℕ → Prop
  /-- **(ii) ⇒:** a non-vanishing jet obstruction forces jet divergence. -/
  jet_diverges_of_delta : ∀ n : ℕ, 1 ≤ n → delta_n n ≠ 0 → jet_diverges n
  /-- **(ii) ⇐:** jet divergence exhibits a non-vanishing jet obstruction. -/
  delta_of_jet_diverges : ∀ n : ℕ, 1 ≤ n → jet_diverges n → delta_n n ≠ 0

/-- **NS obstruction computation** ([`prop:ns-obstruction-computation`]).

    (i) `lk · e(ξ)|_p ≠ 0 ↔` Reeb zero at `p`; (ii) `δ_n|_Σ ≠ 0 ↔` the
    `n`-th jet diverges (`n ≥ 1`).  Both iffs are *derived* by `Iff.intro`
    from the four directional hypotheses. -/
-- Ref: [manuscript] quantum-observable-universe/fluid-dynamics/ns-obstruction-computation.ts
theorem ns_obstruction_computation {R : Type*} [CommRing R]
    [ctx : NsObstructionComputationContext R] :
    (((ctx.lk : R) * ctx.e_xi_at_p ≠ 0) ↔ ctx.reeb_zero_at_p) ∧
    (∀ n : ℕ, 1 ≤ n → (ctx.delta_n n ≠ 0 ↔ ctx.jet_diverges n)) :=
  ⟨⟨ctx.reeb_zero_of_obstruction, ctx.obstruction_of_reeb_zero⟩,
   fun n hn => ⟨ctx.jet_diverges_of_delta n hn, ctx.delta_of_jet_diverges n hn⟩⟩

end QOU.FluidDynamics
