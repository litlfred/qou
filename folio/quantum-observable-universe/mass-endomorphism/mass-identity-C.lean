import Mathlib.Analysis.Normed.Group.Basic


/-!
# QOU.MassIdentityC — Archimedean realisation of the mass identity

In the archimedean QOU (C, θ, G, S) with instanton connection A,
Levi form L, and self-dual curvature F⁺, the categorical mass is
realised as Yekutieli's nonabelian multiplicative integral.

The nonabelian Stokes theorem equating the multiplicative integral
to the holonomy is a deep analytic result ([yekutieli2015]) that
cannot currently be formalised in Lean/Mathlib. It is recorded as
an axiom with full bibliographic citation.

## References

- [yekutieli2015] Nonabelian multiplicative integration on surfaces
- [leitner2026] §3

**Ground ring**: `ℝ` (geometric/analytic realisation).
Uses ℝ-specific analysis (trig, norms, real powers).
NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU

/-- **Archimedean mass corollary**: the categorical mass of a closed
    cycle γ encircling a vortex filament equals the Killing-form norm
    of the holonomy of the instanton connection around γ.

    m(γ) = ‖MI∫_Σ (∇_A q, L ∧ F⁺)‖ = ‖Hol_{∇_A}(γ; 𝔊)‖

    LaTeX: `\label{cor:mass-identity-C}`
    Ref: [yekutieli2015] -/
-- Ref: [yekutieli2015] Yekutieli, "Nonabelian Multiplicative Integration on Surfaces," World Scientific 2015 (DOI: 10.1142/9537)
structure ArchimedeanMassData where
  /-- The holonomy value ‖Hol_{∇_A}(γ; 𝔊)‖. -/
  holonomy_norm : ℝ
  /-- The multiplicative integral value ‖MI∫_Σ (∇_A q, L ∧ F⁺)‖. -/
  mult_integral_norm : ℝ
  /-- The categorical mass ‖tr((λ ⊗ id) ∘ Δ ∘ γ)‖, computed via
      scalarMass from mass-identity.lean. -/
  categorical_mass_norm : ℝ
  /-- Mass is non-negative. -/
  mass_nonneg : 0 ≤ holonomy_norm

/-! ## The three norms are FREE FIELDS -- two axioms deleted 2026-09-06

`ArchimedeanMassData` carries `holonomy_norm`, `mult_integral_norm` and
`categorical_mass_norm` as three independent real fields.  Its only
relating field, `mass_nonneg`, constrains one of them to be
non-negative and says nothing about the other two.  So

    axiom nonabelian_stokes (data) :
      data.mult_integral_norm = data.holonomy_norm

    axiom categorical_equals_multiplicative_integral (data) :
      data.categorical_mass_norm = data.mult_integral_norm

both fail at the record `⟨0, 1, 0, le_refl 0⟩`, and so did
`mass_is_holonomy` -- the Lean backing `cor:mass-identity-C` -- which
was derived from the two.

The mathematics is not in dispute.  Yekutieli's nonabelian Stokes
theorem is a real and deep result about path-ordered exponentials, and
the corollary's prose argument is the right one.  What was wrong is that
the Lean asserted an equality between two numbers a record is free to
choose independently: no path, no connection, no surface appears in
`ArchimedeanMassData`, so nothing in the type could ever have made the
equality hold.

Stating it needs the connection and the multiplicative integral as
constructions, with the norms **derived** from them -- the shape the
repaired `transfer_matrix_level_independence` uses.  That is a real
formalisation and is deliberately not guessed at here. -/

/-- Three norms chosen independently; `mass_nonneg` is satisfied. -/
def freeNormData : ArchimedeanMassData where
  holonomy_norm := 0
  mult_integral_norm := 1
  categorical_mass_norm := 0
  mass_nonneg := le_refl 0

/-- **`nonabelian_stokes` is false as stated.** -/
theorem not_nonabelian_stokes :
    ¬ (∀ data : ArchimedeanMassData,
        data.mult_integral_norm = data.holonomy_norm) := by
  intro h
  simpa [freeNormData] using h freeNormData

/-- **`categorical_equals_multiplicative_integral` is false as stated.** -/
theorem not_categorical_equals_multiplicative_integral :
    ¬ (∀ data : ArchimedeanMassData,
        data.categorical_mass_norm = data.mult_integral_norm) := by
  intro h
  simpa [freeNormData] using h freeNormData

/-- **And so was the corollary derived from them**, `cor:mass-identity-C`. -/
theorem not_mass_is_holonomy :
    ¬ (∀ data : ArchimedeanMassData,
        data.categorical_mass_norm = data.holonomy_norm) := by
  intro h
  -- the same witness does not separate these two (both are 0), so use one
  -- that does: holonomy 1, categorical 0, with mass_nonneg still satisfied.
  have hne : ((0 : ℝ)) ≠ 1 := by norm_num
  exact hne (h ⟨1, 1, 0, by norm_num⟩)

end QOU
