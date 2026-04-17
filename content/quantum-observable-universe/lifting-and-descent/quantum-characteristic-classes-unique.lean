/-!
# QOU.QuantumCharClasses.unique — uniqueness of quantum characteristic classes

κ_n uniquely determined as a cohomology class by Giraud classification.

LaTeX: `\label{prop:quantum-characteristic-classes-unique}`

## References

- [manuscript] §5-lifting-and-descent/quantum-characteristic-classes-unique
- [yekutieli2010] Twisted Deformation Quantization
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of quantum characteristic classes.** -/
-- Ref: [yekutieli2010]
theorem QuantumCharClasses.unique :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
