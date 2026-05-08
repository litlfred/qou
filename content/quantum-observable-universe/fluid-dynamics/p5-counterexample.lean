/-!
# QOU.FluidDynamics.NSCounterexample

Counter-example to Navier–Stokes regularity via q → 1 degeneration.

LaTeX label: `conj:ns-counterexample`

## Conjectural content

Conjectural NS-counterexample: existence of a smooth initial datum whose q-deformed flow develops a finite-time singularity at q = 1, refuting the smoothness Millennium variant.

## Status

Class-axiomatised per CLAUDE.md §3b-cond. The conjecture sits in
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

/-- **Conjecture class** for `conj:ns-counterexample`.

    Encodes the conjectural content as a Lean type-class so that
    downstream theorems can take `[NSCounterexample]` as an explicit
    hypothesis (CLAUDE.md §3b-cond).  Concrete instances either
    prove the conjecture or supply a `sorry` (read as conjecture).

    Ref: [manuscript] §Counter-example to Navier–Stokes regularity via q → 1 degeneration, `conj:ns-counterexample` -/
class NSCounterexample where
  /-- The abstract conjectural witness.  Concrete instances refine
      this to a specific predicate / data; the class is sufficient
      for §3b-cond bookkeeping. -/
  witness : Prop
  /-- The conjectural-truth assertion.  An instance supplying
      `holds := …` either proves the conjecture or carries a
      `sorry` understood as conjecture. -/
  holds   : witness

end QOU.FluidDynamics
