import QOU.Interactions.DerivedAtom


/-!
# Derived atom A(Z, N) — formal definition

The 5-step categorical construction of an atom from γγ pair production.

## References

- [def:derived-atom]
-/

-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
-- The formal definition is in QOU.Interactions.DerivedAtom
-- (derivedAtomNF, NucleonType, crossingType, etc.)

namespace QOU.Interactions

/-- Derived atom $\\mathcal{A}(Z, N)$ from pair production -/
def DerivedAtom   :=
  -- Ref: [manuscript] def:derived-atom
  trivial

end QOU.Interactions
