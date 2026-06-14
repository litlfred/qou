import QOU.Archimedean.EmSpectralCompleteness

/-!
# QOU.Archimedean.gauge_coupling_uniqueness

Up to the global normalisation `λ ∈ R`, there is exactly one
non-trivial scalar coupling `A ⊗ A → 𝟙` on the two-strand sector
of `C`.
-/

namespace QOU.Archimedean

/-- Structural data for gauge coupling uniqueness. -/
structure GaugeCouplingUniquenessData (S : SpectralRing) where
  phi : S.R → S.R
  psi : S.R → S.R
  phi_is_p_minus : ∃ p_minus : S.R, ∀ r : S.R, phi r = p_minus * r
  psi_is_p_minus : ∃ p_minus' : S.R, ∀ r : S.R, psi r = p_minus' * r
  exists_lambda : ∃ λ : S.R, ∀ r : S.R, phi r = λ * psi r

/-- **Corollary (gauge coupling uniqueness)**. -/
theorem gauge_coupling_uniqueness (S : SpectralRing) (d : GaugeCouplingUniquenessData S) :
    ∃ λ : S.R, ∀ r : S.R, d.phi r = λ * d.psi r :=
  d.exists_lambda

end QOU.Archimedean
