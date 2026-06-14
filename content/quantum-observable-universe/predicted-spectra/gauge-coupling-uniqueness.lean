import QOU.Archimedean.EmSpectralCompleteness


/-!
# QOU.Archimedean.gauge_coupling_uniqueness

Up to the global normalisation `λ ∈ R`, there is exactly one
non-trivial scalar coupling `A ⊗ A → 𝟙` on the two-strand sector
of `C`.

LaTeX label: `cor:gauge-coupling-uniqueness`

## References

- [manuscript] §5/gauge-coupling-uniqueness
-/

namespace QOU.Archimedean

/-- **Corollary (gauge coupling uniqueness)**.

    Any `R`-linear, braid-invariant scalar coupling `φ : A ⊗ A → 𝟙`
    is determined up to an `R`-multiple by a *non-trivial* reference
    coupling `ψ`.  We model a scalar coupling on the two-strand
    sector as multiplication by its value `p₋ ∈ R` on the singlet
    idempotent `e₋`; the reference coupling `ψ` is *non-trivial*
    exactly when its multiplier is a **unit** `p₋' ∈ Rˣ`
    (equivalently `tr_τ(e₋) ≠ 0`, non-degeneracy of the singlet
    trace).  Under that hypothesis the conclusion `φ = λ · ψ` holds
    with `λ = p₋ · p₋'⁻¹`, proved directly from the commutative-ring
    axioms.

    The non-degeneracy hypothesis is essential — and was missing
    from the earlier axiomatic formulation, which was therefore
    *false*: a degenerate `ψ ≡ 0` (multiplier `0`, not a unit)
    admits no `λ` with `φ = λ · ψ` when `φ ≢ 0`.  Replacing the
    free multiplier `p₋' : R` with a unit `p₋' : Rˣ` makes the
    statement true and discharges the former external axiom.  The
    categorical input — that exactly one singlet channel `e₋`
    exists, so the reference coupling really is non-degenerate —
    lives upstream in `em_spectral_completeness`. -/
-- Ref: [manuscript] §5/gauge-coupling-uniqueness
theorem gauge_coupling_uniqueness (S : SpectralRing) :
    ∀ (φ ψ : S.R → S.R),
      (∃ p_minus : S.R, ∀ r : S.R, φ r = p_minus * r) →
      (∃ p_minus' : S.Rˣ, ∀ r : S.R, ψ r = (p_minus' : S.R) * r) →
      ∃ lam : S.R, ∀ r : S.R, φ r = lam * ψ r := by
  rintro φ ψ ⟨p, hp⟩ ⟨u, hu⟩
  refine ⟨p * (↑u⁻¹ : S.R), fun r => ?_⟩
  have key : (↑u⁻¹ : S.R) * (↑u : S.R) = 1 := u.inv_mul
  calc φ r = p * r := hp r
    _ = p * ((↑u⁻¹ : S.R) * (↑u : S.R)) * r := by rw [key, mul_one]
    _ = (p * (↑u⁻¹ : S.R)) * ((↑u : S.R) * r) := by ring
    _ = (p * (↑u⁻¹ : S.R)) * ψ r := by rw [hu r]

end QOU.Archimedean
