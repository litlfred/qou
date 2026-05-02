/-!
# Graded Markov trace from the GS filtration

Narrative anchor for the previously-opaque `gradedMarkovTrace`
declaration.

The graded Markov trace at level ℓ is the induced trace on the
quotient `J^ℓ / J^{ℓ+1}` of the Gröbner-Shirshov filtration, and is
purely algebraic in `ℤ[q^{±1}]` — no Archimedean function theory.

## References

- [prop:graded-markov-trace-from-gs-filtration]
- [thm:jones-markov-trace]
- [prop:gb-spectral-sequence]
- [prop:graded-trace-residue-split]
-/

namespace QOU.BraidKnot

/--
Placeholder type signature for the graded Markov trace at level `ℓ`.
The substantive content lives in the narrative .md (see Ref) and in
the GS-filtration formalization tracked separately.
-/
def graded_markov_trace_from_gs_filtration : True := by
  -- Ref: [manuscript] `prop:graded-markov-trace-from-gs-filtration`,
  -- §"Proof". The construction is mechanical given the GS
  -- filtration and the centrality of the Markov trace.
  trivial

end QOU.BraidKnot
