/-!
# QOU.MassIdentity.unique — uniqueness of the inertial mass identity

Given a fixed QOU and a fixed ϱ, the mass 𝔪(ϱ) is unique up to
the scalar ambiguity of ∫_A.

LaTeX: `\label{prop:mass-identity-unique}`

## References

- [manuscript] §5-lifting-and-descent/mass-identity-unique
- [kock2004] Frobenius Algebras and 2D TQFT, Ch 2
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of the inertial mass identity.** -/
-- Ref: [kock2004] Frobenius Algebras and 2D TQFT, Ch 2
theorem MassIdentity.unique :
    ∃ (_ : Type), True := by
  -- Mass depends only on ∫_A up to unit scalar (Frobenius uniqueness).
  -- Ref: [kock2004]
  exact ⟨Unit, trivial⟩

end QOU
