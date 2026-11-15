import Mathlib.Data.Real.Basic

/-!
# QOU.NS.NSCounterexample — `conj:ns-counterexample` axiomatised

Conjectural content: **the classical limit $q \to 1$ of the
$q$-NS evolution exhibits an explicit finite-time singularity** — a
concrete velocity profile and a finite singularity time $T^*$ such
that the velocity becomes unbounded as $t \to T^{*-}$.

LaTeX label: `conj:ns-counterexample`

## Conjectural content

Conjectural NS-counterexample: existence of a smooth initial datum whose q-deformed flow develops a finite-time singularity at q = 1, refuting the smoothness Millennium variant.

## Status

Class-axiomatised per AGENTS.md §3b-cond. The conjecture sits in
the residual §3b-violator cone identified in
[`AUDIT-DEEP-2026-05.md`](../../../../AUDIT-DEEP-2026-05.md) §1A
(P1.b sweep). Class declaration here lets downstream
provable-kind blocks (in the same `uses[]` cone) become
`conditional-on-class` rather than violators.

`sorry` in any concrete instance is understood as **conjecture**,
not missing proof. Downstream blocks may take `[NSCounterexample]` as an
explicit `[Instance]` hypothesis to retain
`theorem` / `proposition` status under §3b-cond.

## References

- [leitner2026] §Counter-example to Navier–Stokes regularity via q → 1 degeneration, `conj:ns-counterexample`
-/

namespace QOU.FluidDynamics

/-- **`conj:ns-counterexample` (axiomatised).**

    The classical limit $q \to 1$ of the $q$-NS evolution admits a
    finite-time singularity: a concrete velocity profile $u(t, x)$
    and time $T^*$ at which $\sup_x |u(t, x)|$ blows up. -/
class NSCounterexample where
  /-- A finite singularity time $T^* > 0$. -/
  singularityTime : ℝ
  /-- The velocity profile $u : \mathrm{time} \to \mathrm{space} \to \mathbb{R}$. -/
  velocityProfile : ℝ → ℝ → ℝ
  /-- Singularity time is strictly positive. -/
  singularityTime_pos : 0 < singularityTime
  /-- **The conjecture itself.**  The velocity is unbounded as
      $t \to T^{*-}$: on *every* left neighbourhood of $T^*$ it exceeds
      every bound $M$.

      The `T* - ε < t` conjunct is what puts the blow-up *at* $T^*$ and
      is not optional: without it the field says only that the velocity
      is unbounded somewhere on $t < T^*$, which is satisfied by
      `velocityProfile t x = max (-t) 0` with `T* = 1` — a profile that
      tends to $0$ as $t \to T^{*-}$ and so exhibits no finite-time
      singularity at all (verified counterexample:
      `docs/audits/2026-08-29-q-ns-conjecture-statement-strength-probe.lean`). -/
  -- Ref: [leitner2026] fluid-dynamics/p5-counterexample
  ns_counterexample_holds :
    ∀ M : ℝ, ∀ ε : ℝ, 0 < ε →
      ∃ t x : ℝ, singularityTime - ε < t ∧ t < singularityTime ∧
        M < velocityProfile t x

end QOU.FluidDynamics
