import QOU.Interactions.AlgebraicPrimality


/-!
# QOU.ParticleInteractions.OneVacuousMagic (sibling)

Sibling-block `.lean` for `prop:n-equals-1-vacuous-magic`. Re-exports
the proved theorem from `QOU.Interactions.AlgebraicPrimality`.

LaTeX label: `prop:n-equals-1-vacuous-magic`
-/

namespace QOU.ParticleInteractions

/-- **Re-export.** For every `q : ℝ`, the integer `n = 1` is
    algebraically prime — proved via vacuous truth on the empty
    set of valid decompositions. See
    `QOU.Interactions.AlgebraicPrimality.one_isAlgebraicallyPrime`
    for the proof. -/
-- Ref: [leitner2026] prop:n-equals-1-vacuous-magic
theorem one_isAlgebraicallyPrime (q : ℝ) :
    QOU.Interactions.AlgebraicPrimality.IsAlgebraicallyPrime 1 q :=
  QOU.Interactions.AlgebraicPrimality.one_isAlgebraicallyPrime q

end QOU.ParticleInteractions
