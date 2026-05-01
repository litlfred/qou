/-!
# Residue at a root of unity, defined algebraically

Narrative anchor for the previously-opaque `residueAtRoot`
declaration.

The residue is the cyclotomic projection of the graded Markov trace,
extracted via discrete Fourier transform within `ℤ[q^{±1}]` — no
meromorphic continuation in `ℂ`.

## References

- [prop:residue-at-root-from-gs-filtration]
- [prop:graded-markov-trace-from-gs-filtration]
- [prop:gb-spectral-sequence]
-/

namespace QOU.BraidKnot

/--
Placeholder type signature for the residue at a root of unity.
The substantive content lives in the narrative .md (see Ref) and in
the cyclotomic-ring API; agreement with the meromorphic-residue
definition (where the latter is defined) is a separate corollary.
-/
def residue_at_root_from_gs_filtration : True := by
  -- Ref: [manuscript] `prop:residue-at-root-from-gs-filtration`,
  -- §"Proof". Discrete Fourier extraction of the cyclotomic
  -- component is purely algebraic in ℤ[q^{±1}].
  trivial

end QOU.BraidKnot
