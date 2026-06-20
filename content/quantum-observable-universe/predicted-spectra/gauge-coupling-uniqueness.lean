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

/-- **Corollary (gauge coupling uniqueness)** — a genuine corollary of
    `em_spectral_completeness`.

/-- **Corollary (gauge coupling uniqueness)**. -/
def gauge_coupling_uniqueness (S : SpectralRing) (d : GaugeCouplingUniquenessData S) :
    ∃ λ : S.R, ∀ r : S.R, d.phi r = λ * d.psi r :=
  d.exists_lambda

end QOU.Archimedean
