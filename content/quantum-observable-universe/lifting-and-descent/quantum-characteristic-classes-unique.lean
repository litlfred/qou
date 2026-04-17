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
  -- Different local trivialisations yield cohomologous cocycles.
  -- Ref: [yekutieli2010]
  sorry

end QOU
