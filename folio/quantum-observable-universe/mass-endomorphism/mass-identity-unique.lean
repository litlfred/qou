import QOU.Core.Basic


/-!
# QOU.MassIdentity.unique — uniqueness of the inertial mass identity

Given a fixed QOU and a fixed ϱ, the mass 𝔪(ϱ) is unique up to
the scalar ambiguity of ∫_A: scaling ∫_A by c scales 𝔪(ϱ) by |c|.

LaTeX: `\label{prop:mass-identity-unique}`

## References

- [leitner2026] §5-lifting-and-descent/mass-identity-unique
- [kock2004] Frobenius Algebras and 2D TQFT, Ch 2
-/

namespace QOU

/-- **Uniqueness of the inertial mass identity: the scaling law.**

    The block's claim: if `∫_A^{(1)} = c · ∫_A^{(2)}` then
    `𝔪_{(1)}(ϱ) = |c| · 𝔪_{(2)}(ϱ)`. The mass is the norm of the trace
    (`scalarMass t = ‖t‖`, `def:mass-identity`), and the trace is linear in
    `∫_A`, so scaling the form scales the trace by `c`. That linearity is the
    hypothesis `h`; what is proved is the step from it to the mass.

    **The norm must be multiplicative.** Over a general `NormedCommRing` only
    `‖c * t‖ ≤ ‖c‖ * ‖t‖` holds, and the block's equality fails, so the
    statement needs `NormedDivisionRing` (in particular a normed field such as
    `ℝ` or `ℂ` at `q = q₀`). Fixing the normalisation `c = 1` then fixes the
    mass, which is the uniqueness the block names.

    Replaces `(h : m₁ = m₂) : ‖m₁‖ = ‖m₂‖ := by rw [h]`, which asserted only
    that a function takes equal values on equal inputs (bean `qou-jy1r`). -/
-- Ref: [kock2004]
theorem MassIdentity.unique
    {R : Type*} [NormedDivisionRing R] (c t₁ t₂ : R) (h : t₁ = c * t₂) :
    ‖t₁‖ = ‖c‖ * ‖t₂‖ := by
  rw [h, norm_mul]

end QOU
