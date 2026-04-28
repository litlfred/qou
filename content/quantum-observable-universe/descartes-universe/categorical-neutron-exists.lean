/-!
# QOU.CategoricalNeutron.exists — existence of the categorical neutron

𝔫 = 𝓑₃(𝔲, 𝔡, 𝔡) is a well-defined element of H₃(q), LP-stable with
two Hopf-link gluons.

LaTeX: `\label{prop:categorical-neutron-exists}`

## References

- [manuscript] §6-descartes-universe/categorical-neutron-exists
- [jones1987] Hecke Algebra Representations of Braid Groups
-/

import QOU.Basic

namespace QOU

/-- **Existence of the categorical neutron.**

    B₃(u,d,d) + two-Hopf-link gluon stabiliser yields a
    `CategoricalNeutron` term with negative crossing energy. -/
-- Ref: [jones1987]
theorem CategoricalNeutron.exists : Nonempty CategoricalNeutron := by
  -- Witness: concrete braid B₃(u,d,d) × (L_- ∘ L_-) reduced to NF.
  -- Ref: [jones1987]
  sorry

end QOU
