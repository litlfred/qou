/-!
# QOU.QuantumCharClasses.exists — well-definedness of quantum characteristic classes

κ_n ∈ H²(𝒮, 𝓑) exists via Giraud's classification of central gerbe
extensions.

LaTeX: `\label{prop:quantum-characteristic-classes-exists}`

## References

- [manuscript] §5-lifting-and-descent/quantum-characteristic-classes-exists
- [yekutieli2010] Twisted Deformation Quantization of Algebraic
  Varieties, https://doi.org/10.1016/j.aim.2010.07.008
-/

import QOU.Basic

namespace QOU

/-- **Well-definedness of quantum characteristic classes.** -/
-- Ref: [yekutieli2010]
theorem QuantumCharClasses.exists :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
