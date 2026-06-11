import Mathlib.Data.Real.Basic

/-!
# QOU.FluidDynamics.q_bkm_criterion — `q`-Beale–Kato–Majda criterion

**Theorem** ([`thm:q-bkm-criterion`](../../../quantum-observable-universe/fluid-dynamics/q-bkm-criterion.md)).

*Let `v` be the solution of the `q`-NS system with `q > 1` on
`[0, T)` and let `ω_q = d_q v` be the `q`-vorticity.  Then `v`
extends smoothly beyond `T` if and only if*

```
  ∫₀^T ‖ω_q(t)‖_{L^∞} dt < ∞.
```

*Equivalently: if the solution loses regularity at time `T*`, then
the integral diverges to `+∞`.  Since the `q`-NS wellposedness
theorem shows solutions are global for `q > 1`, the integral is
always finite when `q > 1`; the criterion becomes non-trivial only
in the classical limit `q → 1`.*

The Lean encoding records the iff as a `Prop`-valued statement
against an abstract `QBKMContext` carrying the time-evolution
data `(v, ω_q, T)` and the `L^∞`-norm integral predicate.

-- Ref: [manuscript] quantum-observable-universe/fluid-dynamics/q-bkm-criterion.md
-/

namespace QOU.FluidDynamics

/-- Abstract context for the `q`-Beale–Kato–Majda criterion. -/
class QBKMContext where
  /-- The terminal time `T > 0`. -/
  T : ℝ
  T_pos : 0 < T
  /-- The substrate parameter `q > 1`. -/
  q : ℝ
  q_gt_one : 1 < q
  /-- Predicate "`v` extends smoothly beyond `T`". -/
  extendsSmoothly : Prop
  /-- Predicate "`∫₀^T ‖ω_q(t)‖_{L^∞} dt < ∞`". -/
  vorticityIntegralFinite : Prop
  /-- Manuscript BKM iff: smooth extension past T equals finite
      L^∞-vorticity integral. -/
  claim_bkm_iff : extendsSmoothly ↔ vorticityIntegralFinite

/-- **`q`-Beale–Kato–Majda criterion** ([`thm:q-bkm-criterion`]).

    The `q`-NS solution extends smoothly past `T` if and only if
    the time-integrated `L^∞` norm of the `q`-vorticity is finite.
-/
-- Ref: [manuscript] quantum-observable-universe/fluid-dynamics/q-bkm-criterion.md
theorem q_bkm_criterion [ctx : QBKMContext] :
    ctx.extendsSmoothly ↔ ctx.vorticityIntegralFinite :=
  ctx.claim_bkm_iff

end QOU.FluidDynamics
