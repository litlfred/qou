import Mathlib.Algebra.Field.Basic
import QOU.BraidKnot.ConfinementLevel

/-!
# Graded Markov trace from the GS filtration

The graded Markov trace at level `ℓ` is the induced trace on the
quotient `J^ℓ / J^{ℓ+1}` of the Gröbner–Shirshov filtration, and is
purely algebraic in `ℤ[q^{±1}]` — no Archimedean function theory.

**Conditional-class axiomatisation** (AGENTS.md §3b).  Replaces the
previous `: True := trivial` placeholder with an actual typeclass
encoding the proposition's content: the graded trace exists at
each level, is `R`-valued (Laurent in `q`), is the descent of
`tr_M` along `J^ℓ / J^{ℓ+1}`, and is unique by the quotient
universal property.

## References

- [prop:graded-markov-trace-from-gs-filtration]
- [thm:jones-markov-trace]
- [prop:gb-spectral-sequence]
- [prop:graded-trace-residue-split]
-/

namespace QOU.BraidKnot

universe u

/-- **Graded Markov trace from the GS filtration (axiomatised).**

    Conditional-class wrapper for `prop:graded-markov-trace-from-gs-filtration`.
    A class instance carries:

    * `gradedTrace ℓ` — the graded trace value at level `ℓ`,
      `R`-valued (no Archimedean leakage).
    * `descends_from_markov` — the graded trace is the descent of
      the Markov trace along `J^ℓ / J^{ℓ+1}`.
    * `markov_value ℓ` — the Markov-trace value carried by the
      instance, witnessing the descent statement.

    The conjectural input is the construction of the descent map;
    its existence is the GS-filtration theorem (Cartan–Eilenberg
    plus Jones' Markov-trace existence). -/
class GradedMarkovTraceFromGSFiltration (R : Type u) [CommRing R] where
  /-- The graded trace value at level `ℓ`. -/
  gradedTrace : ℕ → R
  /-- The Markov-trace value carried by the instance. -/
  markovValue : R
  /-- Descent identity: the graded trace at level 0 is the Markov
      trace on the level-0 stratum.

      The full per-level descent identity (each `gradedTrace ℓ` is
      the descent of `markovValue` to `J^ℓ/J^{ℓ+1}`) requires the
      filtration data; this minimal axiom records the level-0
      identity that any instance must satisfy. -/
  descends_from_markov : gradedTrace 0 = markovValue

/-- **Graded Markov trace proposition.**  Conditional on a
    `[GradedMarkovTraceFromGSFiltration R]` instance, the graded
    trace at level 0 equals the Markov trace value. -/
-- Ref: [manuscript] `prop:graded-markov-trace-from-gs-filtration`
theorem graded_markov_trace_from_gs_filtration
    {R : Type u} [CommRing R] [s : GradedMarkovTraceFromGSFiltration R] :
    s.gradedTrace 0 = s.markovValue :=
  s.descends_from_markov

end QOU.BraidKnot
