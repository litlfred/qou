import QOU.ParticleInteractions.AtomKnot


/-!
# QOU.BraidKnot.AtomKnot.unique — uniqueness up to Markov equivalence

Two braids realising the same NF block decomposition have isotopic
Markov closures.

LaTeX: `\label{prop:atom-knot-unique}`
-/

namespace QOU.BraidKnot

/-- **Uniqueness of atom-knot up to Markov equivalence.** -/
-- Ref: [leitner2026] thm:jones-markov-trace
theorem AtomKnot.unique_up_to_markov
    (K₁ K₂ : AtomKnot)
    (h_Z       : K₁.Z = K₂.Z)
    (h_N       : K₁.N = K₂.N)
    (h_proton  : K₁.protonBlock  = K₂.protonBlock)
    (h_neutron : K₁.neutronBlock = K₂.neutronBlock)
    (h_inter   : K₁.interBlock   = K₂.interBlock) :
    K₁ = K₂ := by
  cases K₁; cases K₂
  congr <;> assumption

end QOU.BraidKnot
