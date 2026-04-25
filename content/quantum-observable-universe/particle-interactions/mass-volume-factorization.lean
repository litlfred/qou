/-
  Mass-volume factorization conjecture.

  The categorical mass endomorphism of an atomic link complement
  factorizes as
      m(K; q) = ρ_F · Vol_hyp(complement)
  where ρ_F ∈ {m_e, 2m_e} is the Frobenius packing density
  (single-chirality vs CPT-saturated).

  Since this is a conjecture, we axiomatize it as a class whose
  `sorry`-valued instances encode the statement.  Downstream
  results can be proved conditional on [MassVolumeFactorization].

  Ref: [manuscript] Ch 11 §8 / mass-volume-factorization
  Ref: [thurston1978] http://library.msri.org/books/gt3m/
  Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
-/

import Mathlib.Data.Real.Basic
import Mathlib.Data.List.Basic

namespace QOU.ParticleInteractions

/-- Frobenius packing density: either single-chirality (m_e) or
    CPT-saturated (2 m_e).  Encoded as a Boolean flag plus a
    reference scale. -/
structure FrobeniusPackingDensity where
  scaleMe : ℝ        -- the base scale m_e
  cptSaturated : Bool -- whether the alt block is populated

/-- The density value: m_e or 2 m_e. -/
noncomputable def FrobeniusPackingDensity.value
    (ρ : FrobeniusPackingDensity) : ℝ :=
  if ρ.cptSaturated then 2 * ρ.scaleMe else ρ.scaleMe

/-- **Mass-volume factorization** (conjectural class).
    An instance asserts the factorization
        mass = density · hyperbolic volume
    for a given atomic link configuration.  The `factorization`
    field is `sorry` — this is the conjecture itself, not a
    derivable theorem. -/
class MassVolumeFactorization
    (K : Type*) -- atomic link configuration
    where
  density      : K → FrobeniusPackingDensity
  volume       : K → ℝ          -- Thurston hyperbolic volume
  mass         : K → ℝ          -- categorical mass endomorphism
  factorization :
    ∀ k : K, mass k = (density k).value * volume k
  -- Ref: [thurston1978] http://library.msri.org/books/gt3m/
  -- Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
  -- The `factorization` field is taken as an axiom of the class;
  -- instances must provide evidence per atomic link configuration
  -- (via SnapPy volume computation and Wedderburn block analysis).

/-- Binding energy derived from the factorization for a list of
    JSJ pieces.  Conditional on `MassVolumeFactorization`.
    Uses the `mass` field directly; by the `factorization` axiom
    this equals `Σ (density k).value * volume k`. -/
noncomputable def bindingFromJSJ
    {K : Type*} [MassVolumeFactorization K]
    (pieces : List K) : ℝ :=
  (pieces.map MassVolumeFactorization.mass).sum

end QOU.ParticleInteractions
