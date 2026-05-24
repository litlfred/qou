/-!
# QOU.ParticleInteractions.MagicEqualsEmpirical (sibling)

Sibling-block `.lean` for
`conj:algebraic-primality-equals-empirical-at-q0`. Re-exports the
typeclass `MagicEqualsEmpirical` from
`QOU.Interactions.AlgebraicPrimality`.

LaTeX label: `conj:algebraic-primality-equals-empirical-at-q0`
-/

import QOU.Interactions.AlgebraicPrimality

namespace QOU.ParticleInteractions

/-- **Re-export.** Conjectural typeclass asserting that at substrate
    `q_0`, the set of algebraically-prime integers equals the
    empirical magic ladder `{1, 2, 8, 20, 28, 50, 82, 126}`. See
    `QOU.Interactions.AlgebraicPrimality.MagicEqualsEmpirical`. -/
-- Ref: [manuscript] conj:algebraic-primality-equals-empirical-at-q0
abbrev MagicEqualsEmpirical :=
  QOU.Interactions.AlgebraicPrimality.MagicEqualsEmpirical

end QOU.ParticleInteractions
