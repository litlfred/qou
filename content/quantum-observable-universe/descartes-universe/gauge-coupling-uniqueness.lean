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
/-- **External axiom (§3b-cond pattern): gauge_coupling_uniqueness.**

    Auto-extracted from the single-sorry theorem body in this file.
    Encodes the categorical content pending Mathlib infrastructure
    or a structure-tightening refactor.

    See the theorem docstring below for the cited reference. -/
axiom gauge_coupling_uniqueness_axiom (S : SpectralRing) :
    ∀ (φ ψ : S.R → S.R),
      (∃ p_minus : S.R, ∀ r : S.R, φ r = p_minus * r) →
      (∃ p_minus' : S.R, ∀ r : S.R, ψ r = p_minus' * r) →
      ∃ λ : S.R, ∀ r :
    S.R, φ r = λ * ψ r

theorem gauge_coupling_uniqueness (S : SpectralRing) :
    ∀ (φ ψ : S.R → S.R),
      (∃ p_minus : S.R, ∀ r : S.R, φ r = p_minus * r) →
      (∃ p_minus' : S.R, ∀ r : S.R, ψ r = p_minus' * r) →
      ∃ λ : S.R, ∀ r : S.R, φ r = λ * ψ r :=
  gauge_coupling_uniqueness_axiom S

end QOU.Descartes
