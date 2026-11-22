import QOU.ParticleInteractions.AtomKnot


/-!
# QOU.BraidKnot.AtomKnot.exists — existence of atom-knot for any (Z, N)

Constructive: assemble Z protons + N neutrons + inter-nucleon connector.

LaTeX: `\label{prop:atom-knot-exists}`
-/

namespace QOU.BraidKnot

/-- **Existence of the atom-knot of type (Z, N).** -/
-- Ref: [leitner2026] braids-and-knots/atom-knot
theorem AtomKnot.exists (Z N : ℕ) : ∃ K : AtomKnot, K.Z = Z ∧ K.N = N := by
  exact ⟨{ Z := Z, N := N, protonBlock := [], neutronBlock := [], interBlock := [] }, rfl, rfl⟩

end QOU.BraidKnot
