/-!
# QOU.ParticleInteractions.AlgebraicPrimality (sibling)

Sibling-block `.lean` file for `def:algebraic-primality`. The
canonical implementation lives in
`QOU/Interactions/AlgebraicPrimality.lean` (re-exported from
`QOU.Interactions`); this sibling re-imports the definition and
exposes it under the chapter-conventional namespace.

LaTeX label: `def:algebraic-primality`
-/

import QOU.Interactions.AlgebraicPrimality

namespace QOU.ParticleInteractions

/-- Re-export of the algebraic-primality definition for a confined
    hadron of strand count `n` at substrate `q`. The full content,
    including the auxiliary lemma and base-case theorem at `n = 1`,
    is in `QOU.Interactions.AlgebraicPrimality`. -/
-- Ref: [manuscript] def:algebraic-primality
def IsAlgebraicallyPrime (n : ℕ) (q : ℝ) : Prop :=
  QOU.Interactions.AlgebraicPrimality.IsAlgebraicallyPrime n q

end QOU.ParticleInteractions
