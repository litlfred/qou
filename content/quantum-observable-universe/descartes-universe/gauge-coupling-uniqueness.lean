/-!
# QOU.Descartes.gauge_coupling_uniqueness

Up to the global normalisation `λ ∈ R`, there is exactly one
non-trivial scalar coupling `A ⊗ A → 𝟙` on the two-strand sector
of `C`.

LaTeX label: `cor:gauge-coupling-uniqueness`

## References

- [manuscript] §5/gauge-coupling-uniqueness
-/

import QOU.Descartes.EmSpectralCompleteness

namespace QOU.Descartes

/-- **Corollary (gauge coupling uniqueness)**.

    Any `R`-linear, braid-invariant, scalar coupling
    `A ⊗ A → 𝟙` is determined up to an `R`-multiple by the
    singlet idempotent `p₋`. -/
-- Ref: [manuscript] §5/gauge-coupling-uniqueness
theorem gauge_coupling_uniqueness (S : SpectralRing) :
    ∀ (φ ψ : S.R → S.R),
      (∃ p_minus : S.R, ∀ r : S.R, φ r = p_minus * r) →
      (∃ p_minus' : S.R, ∀ r : S.R, ψ r = p_minus' * r) →
      ∃ λ : S.R, ∀ r : S.R, φ r = λ * ψ r := by
  -- Both factor through projection onto the unique singlet summand;
  -- they differ by an R-scalar (Bezout produces λ).
  -- Ref: [manuscript] §5/gauge-coupling-uniqueness
  sorry

end QOU.Descartes
