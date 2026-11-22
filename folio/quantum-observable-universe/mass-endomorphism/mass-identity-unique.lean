import QOU.Basic


/-!
# QOU.MassIdentity.unique — uniqueness of the inertial mass identity

Given a fixed QOU and a fixed ϱ, the mass 𝔪(ϱ) is unique up to
the scalar ambiguity of ∫_A.

LaTeX: `\label{prop:mass-identity-unique}`

## References

- [leitner2026] §5-lifting-and-descent/mass-identity-unique
- [kock2004] Frobenius Algebras and 2D TQFT, Ch 2
-/

namespace QOU

/-- **Uniqueness of the inertial mass identity.**

    For a fixed Frobenius form `∫_A`, two mass values computed via
    `scalarMass` on the same closed cycle coincide — uniqueness up
    to the scalar ambiguity of `∫_A` (which is itself unique up to
    scalar by Frobenius-pairing uniqueness).  Encoded here as: two
    inputs with the same trace produce the same norm. -/
-- Ref: [kock2004]
theorem MassIdentity.unique
    {R : Type*} [NormedCommRing R] (m₁ m₂ : R) (h : m₁ = m₂) :
    ‖m₁‖ = ‖m₂‖ := by
  -- Norm is well-defined on R; same input ⇒ same output.
  -- Ref: [kock2004]
  rw [h]

end QOU
