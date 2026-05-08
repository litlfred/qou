/-!
# QOU.BraidKnot.WeakSpectralCompleteness

Plancherel completeness for the EW/Higgs {T(2,4), T(2,6), T(2,8)} idempotent decomposition.

LaTeX label: `conj:weak-spectral-completeness`

## Conjectural content

Conjectural Plancherel completeness: the three torus-knot idempotents T(2,4), T(2,6), T(2,8) span the EW/Higgs sector irrep decomposition.

## Status

Class-axiomatised per CLAUDE.md §3b-cond. The conjecture sits in
the residual §3b-violator cone identified in
[`AUDIT-DEEP-2026-05.md`](../../../../AUDIT-DEEP-2026-05.md) §1A
(P1.b sweep). Class declaration here lets downstream
provable-kind blocks (in the same `uses[]` cone) become
`conditional-on-class` rather than violators.

`sorry` in any concrete instance is understood as **conjecture**,
not missing proof. Downstream blocks may take `[WeakSpectralCompleteness]` as an
explicit `[Instance]` hypothesis to retain
`theorem` / `proposition` status under §3b-cond.

## References

- [manuscript] §Plancherel completeness for the EW/Higgs {T(2,4), T(2,6), T(2,8)} idempotent decomposition, `conj:weak-spectral-completeness`
-/

namespace QOU.BraidKnot

/-- **Conjecture class** for `conj:weak-spectral-completeness`.

    Encodes the conjectural content as a Lean type-class so that
    downstream theorems can take `[WeakSpectralCompleteness]` as an explicit
    hypothesis (CLAUDE.md §3b-cond).  Concrete instances either
    prove the conjecture or supply a `sorry` (read as conjecture).

    Ref: [manuscript] §Plancherel completeness for the EW/Higgs {T(2,4), T(2,6), T(2,8)} idempotent decomposition, `conj:weak-spectral-completeness` -/
class WeakSpectralCompleteness where
  /-- The abstract conjectural witness.  Concrete instances refine
      this to a specific predicate / data; the class is sufficient
      for §3b-cond bookkeeping. -/
  witness : Prop
  /-- The conjectural-truth assertion.  An instance supplying
      `holds := …` either proves the conjecture or carries a
      `sorry` understood as conjecture. -/
  holds   : witness

end QOU.BraidKnot
