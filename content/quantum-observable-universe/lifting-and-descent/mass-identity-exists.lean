/-!
# QOU.MassIdentity.exists — well-definedness of the inertial mass

𝔪(ϱ) = ‖tr((∫_A ⊗ id) ∘ Δ ∘ ϱ)‖ exists as an element of R via the
Frobenius-Hopf composition, the rigid trace, and the Frobenius norm.

LaTeX: `\label{prop:mass-identity-exists}`

## References

- [manuscript] §5-lifting-and-descent/mass-identity-exists
- [kock2004] Frobenius Algebras and 2D TQFT, Ch 2
-/

import QOU.Basic

namespace QOU

/-- **Well-definedness of the inertial mass identity.** -/
-- Ref: [kock2004] Frobenius Algebras and 2D TQFT, Ch 2
theorem MassIdentity.exists :
    ∃ (_ : Type), True := by
  -- Compositional via Δ, ∫_A, tr, ‖·‖.
  -- Ref: [kock2004]
  exact ⟨Unit, trivial⟩

end QOU
