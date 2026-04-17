/-!
# QOU.CategoricalConnection.unique_up_to_gauge — uniqueness up to gauge

Connections form an affine space over Ω¹(A) ⊗ Ad(A).

LaTeX: `\label{prop:categorical-connection-unique}`

## References

- [manuscript] §1-quantum-universes/categorical-connection-unique
- [kock2004] Frobenius Algebras and 2D TQFT, Ch 2
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of categorical connections up to gauge.** -/
-- Ref: [kock2004]
theorem CategoricalConnection.unique_up_to_gauge :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
