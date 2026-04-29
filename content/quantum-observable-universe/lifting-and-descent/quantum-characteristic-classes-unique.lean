/-!
# QOU.QuantumCharClasses.unique — uniqueness of quantum characteristic classes

κ_n uniquely determined as a cohomology class by Giraud classification.

LaTeX: `\label{prop:quantum-characteristic-classes-unique}`

## References

- [manuscript] §5-lifting-and-descent/quantum-characteristic-classes-unique
- [yekutieli2010] https://doi.org/10.1016/j.aim.2010.07.008
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of quantum characteristic classes.**

    A `QuantumCharacteristicClass` at a given brane-tower stage is
    unique up to cohomologous Čech cocycles — encoded at the type
    level as `Subsingleton`. -/
-- Ref: [yekutieli2010]
theorem QuantumCharClasses.unique : Subsingleton QuantumCharacteristicClass := by
  -- DIAGNOSTIC: The `Subsingleton` claim is too strong. The underlying
  -- structure carries free fields (parameters / morphisms / opaque
  -- functions) that admit distinct valid values, so two instances
  -- need not coincide. To recover a meaningful uniqueness claim,
  -- sharpen with a constraining hypothesis (fixing the carrier
  -- object, fixing the substrate parameter, or quantifying over a
  -- quotient by structural equivalence) — see
  -- `frobenius-pairing-unique.lean` for the pattern. Sorry retained
  -- with this diagnosis rather than closed-as-stated.
  sorry

end QOU
