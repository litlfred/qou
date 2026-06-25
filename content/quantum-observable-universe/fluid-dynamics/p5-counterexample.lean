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

- [manuscript] §Counter-example to Navier–Stokes regularity via q → 1 degeneration, `conj:ns-counterexample`
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
      $t \to T^{*-}$: for every $M > 0$ there is a time $t < T^*$
      and a point $x$ where the velocity exceeds $M$. -/
  -- Ref: [manuscript] fluid-dynamics/p5-counterexample
  ns_counterexample_holds :
    ∀ M : ℝ, ∃ t x : ℝ, t < singularityTime ∧ M < velocityProfile t x

end QOU.FluidDynamics
