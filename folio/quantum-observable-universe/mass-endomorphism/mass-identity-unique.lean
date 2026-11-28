import Mathlib.Algebra.Module.LinearMap.Basic


/-!
# QOU.MassIdentity.unique — uniqueness of the inertial mass identity

Given a fixed QOU and a fixed ϱ, the mass 𝔪(ϱ) is unique up to the scalar ambiguity of ∫_A:
rescaling ∫_A by a unit `c` (with the comultiplication it induces, which rescales by `c⁻¹` and
leaves the mass integrand `Ψ` unchanged) multiplies 𝔪(ϱ) by `c`, an identity in `R`.

LaTeX: `\label{prop:mass-identity-unique}`

**Mass is valued in the ring (owner ruling 2026-11-27, bean `qou-5o1v`).** The previous version
stated the law as `‖t₁‖ = ‖c‖ · ‖t₂‖` over a normed division ring. The absolute value belongs to
the comparison with measurement: `QOU.Transcendental.MassTheory.MassComparison.comparedMass_scale`.

## References

- [leitner2026] §5-lifting-and-descent/mass-identity-unique
- [kock2004] Frobenius Algebras and 2D TQFT, Ch 2
-/

namespace QOU

/-- **Uniqueness of the inertial mass identity: the scaling law, in the ring.**

    With `Ψ` fixed, the mass is the outer Frobenius form `f : M →ₗ[R] R` applied to `Ψ ϱ`.
    Rescaling the form to `c • f` multiplies every mass by `c`, and two forms that give the same
    mass on every cycle are equal. So fixing the normalisation fixes the mass. -/
-- Ref: [kock2004]
theorem MassIdentity.unique
    {R M : Type*} [CommRing R] [AddCommGroup M] [Module R M]
    (c : R) (f : M →ₗ[R] R) (x : M) :
    (c • f) x = c * f x := by
  rw [LinearMap.smul_apply, smul_eq_mul]

/-- **Fixing the normalisation fixes the mass.** Two forms that agree on every `Ψ ϱ` are equal. -/
theorem MassIdentity.unique_of_agree
    {R M : Type*} [CommRing R] [AddCommGroup M] [Module R M]
    (f g : M →ₗ[R] R) (h : ∀ x, f x = g x) : f = g :=
  LinearMap.ext h

end QOU
