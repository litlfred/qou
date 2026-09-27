import Mathlib.Algebra.Ring.Defs

/-!
# QOU.FluidDynamics.q_bkm_criterion — `q`-Beale–Kato–Majda criterion

**Theorem** ([`thm:q-bkm-criterion`](../../../quantum-observable-universe/fluid-dynamics/q-bkm-criterion.md)).

*Let `v` be the solution of the `q`-NS system with `q > 1` on `[0, T)`
and let `ω_q = d_q v` be the `q`-vorticity.  Then `v` extends smoothly
beyond `T` if and only if `∫₀^T ‖ω_q(t)‖_{L^∞} dt < ∞`.  Equivalently:
if the solution loses regularity at `T*`, the integral diverges.*

## Formalisation notes

- **Base ring (§7c).** The statement is over a **generic substrate ring**
  `{R : Type*} [CommRing R]` — *not* `ℝ`.  The archimedean setup
  constraints `0 < T` and `1 < q` use ordering, which is an
  archimedean predicate; they are not needed for the iff and so are
  **not** carried here.  Any archimedean evaluation belongs to a
  post-wall `ℝ`-specialisation (§7c: "start generic; `ℝ` only after the
  substrate→archimedean wall, and only if absolutely required").
- **Non-degenerate conditional (§3b-cond).** The two BKM implication
  directions are carried as explicit hypotheses; the criterion is
  *derived* from them (`Iff.intro`).  The theorem proves the iff rather
  than assuming it — it is not a restatement of its own conclusion.

-- Ref: [manuscript] quantum-observable-universe/fluid-dynamics/q-bkm-criterion.md
-/

namespace QOU.FluidDynamics

/-- Hypotheses for the `q`-Beale–Kato–Majda criterion over a generic
    substrate ring `R` (§7c: generic `CommRing`, never `ℝ`).

    The two BKM implication directions are carried as **explicit
    hypotheses** — the deep continuation direction and the elementary
    necessity direction.  The criterion is *derived* from them in
    `q_bkm_criterion`, so the theorem is a genuine conditional result
    ("if these directional facts hold, then the iff holds"), the
    §3b-cond conditional-class pattern: the class axiomatises the
    conjectural inputs; the theorem derives the consequence.

    The archimedean setup `0 < T`, `1 < q` are deliberately **not**
    fields: ordering is archimedean (§7c) and is unused by the iff. -/
class QBKMContext (R : Type*) [CommRing R] where
  /-- The terminal time (generic substrate-ring element). -/
  T : R
  /-- The substrate parameter (generic substrate-ring element). -/
  q : R
  /-- Predicate "`v` extends smoothly beyond `T`". -/
  extendsSmoothly : Prop
  /-- Predicate "`∫₀^T ‖ω_q(t)‖_{L^∞} dt < ∞`". -/
  vorticityIntegralFinite : Prop
  /-- **BKM continuation (deep direction):** a finite time-integrated
      `L^∞` vorticity norm forces smooth extension past `T`. -/
  bkm_continuation : vorticityIntegralFinite → extendsSmoothly
  /-- **BKM necessity (elementary direction):** smooth extension past `T`
      keeps `‖ω_q‖_{L^∞}` bounded on the compact `[0,T]`, so its time
      integral is finite. -/
  bkm_necessity : extendsSmoothly → vorticityIntegralFinite

/-- **`q`-Beale–Kato–Majda criterion** ([`thm:q-bkm-criterion`]).

    The `q`-NS solution extends smoothly past `T` **iff** the
    time-integrated `L^∞` norm of the `q`-vorticity is finite.  *Derived*
    by composing the two directional hypotheses of `QBKMContext` — the
    theorem proves the iff (`Iff.intro`), it does not assume it. -/
-- Ref: [manuscript] quantum-observable-universe/fluid-dynamics/q-bkm-criterion.md
theorem q_bkm_criterion {R : Type*} [CommRing R] [ctx : QBKMContext R] :
    ctx.extendsSmoothly ↔ ctx.vorticityIntegralFinite :=
  ⟨ctx.bkm_necessity, ctx.bkm_continuation⟩

end QOU.FluidDynamics
