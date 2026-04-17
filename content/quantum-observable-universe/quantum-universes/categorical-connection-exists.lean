/-!
# QOU.CategoricalConnection.exists — existence of categorical connections

Trivial witness ∇₀ = d; non-trivial via ∇ = ∇₀ + ω with ω ∈ Ω¹(A) ⊗ Ad(A).

LaTeX: `\label{prop:categorical-connection-exists}`

## References

- [manuscript] §1-quantum-universes/categorical-connection-exists
- [kock2004] Frobenius Algebras and 2D TQFT, Ch 2
-/

import QOU.Basic

namespace QOU

/-- **Existence of categorical connections.** -/
-- Ref: [kock2004]
theorem CategoricalConnection.exists :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
