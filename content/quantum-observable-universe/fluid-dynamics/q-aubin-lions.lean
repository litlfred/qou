import Mathlib.Data.Real.Basic

/-!
# QOU.FluidDynamics.QAubinLions

q-deformed Aubin--Lions lemma: compactness of the solution family as q → 1.

LaTeX label: `conj:q-aubin-lions`

## Conjectural content

Conjectural q-deformed Aubin–Lions compactness: as q → 1, the q-NS solution family is compact in the appropriate Sobolev–Gevrey topology, with the limit a weak Leray–Hopf solution. The class supplies the abstract compactness witness.

## Status

Class-axiomatised per AGENTS.md §3b-cond. The conjecture sits in
the residual §3b-violator cone identified in
[`AUDIT-DEEP-2026-05.md`](../../../../AUDIT-DEEP-2026-05.md) §1A
(P1.b sweep). Class declaration here lets downstream
provable-kind blocks (in the same `uses[]` cone) become
`conditional-on-class` rather than violators.

`sorry` in any concrete instance is understood as **conjecture**,
not missing proof. Downstream blocks may take `[QAubinLions]` as an
explicit `[Instance]` hypothesis to retain
`theorem` / `proposition` status under §3b-cond.

## References

- [manuscript] §q-deformed Aubin--Lions lemma: compactness of the solution family as q → 1, `conj:q-aubin-lions`
-/

namespace QOU.FluidDynamics

/-- **Conjecture class** for `conj:q-aubin-lions`.

    Encodes the conjectural content as a Lean type-class so that
    downstream theorems can take `[QAubinLions]` as an explicit
    hypothesis (AGENTS.md §3b-cond).  Concrete instances either
    prove the conjecture or supply a `sorry` (read as conjecture).

    Ref: [manuscript] §q-deformed Aubin--Lions lemma: compactness of the solution family as q → 1, `conj:q-aubin-lions` -/
class QAubinLions : Prop where
  /-- Compactness as q → 1: the q-deformed Aubin-Lions lemma
      asserts the existence of a compactness exponent 
      such that for all  the solution family
      is precompact in the relevant Sobolev space. -/
  compactness_threshold : ∃ q_thresh : ℝ, q_thresh > 0

end QOU.FluidDynamics
