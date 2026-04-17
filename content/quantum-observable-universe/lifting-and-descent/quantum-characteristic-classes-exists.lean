/-!
# QOU.QuantumCharClasses.exists — well-definedness of quantum characteristic classes

κ_n ∈ H²(𝒮, 𝓑) exists via Giraud's classification of central gerbe
extensions.

LaTeX: `\label{prop:quantum-characteristic-classes-exists}`

## References

- [manuscript] §5-lifting-and-descent/quantum-characteristic-classes-exists
- [yekutieli2010] https://doi.org/10.1016/j.aim.2010.07.008
-/

import QOU.Basic

namespace QOU

/-- **Well-definedness of quantum characteristic classes.**

    A `QuantumCharacteristicClass` term exists for every stage of the
    recursive brane tower, arising as the obstruction class of a
    central gerbe extension (Giraud's classification). -/
-- Ref: [yekutieli2010]
theorem QuantumCharClasses.exists : Nonempty QuantumCharacteristicClass := by
  -- Witness: κ_n built from a Čech 2-cocycle on 𝒮.
  -- Ref: [yekutieli2010]
  sorry

end QOU
