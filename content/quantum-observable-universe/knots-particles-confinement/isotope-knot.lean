import QOU.Basic
import QOU.ParticleInteractions.AtomKnot


/-!
# QOU.BraidKnot.IsotopeKnot — isotope as knot variant of fixed proton block

Two atom-knots are isotopes iff their NF block decompositions agree
on the proton-quark block.

LaTeX: `\label{def:isotope-knot}`
-/

namespace QOU.BraidKnot

/-- **Isotope relation** on atom-knots: same proton-quark block. -/
def AtomKnot.isIsotope (K₁ K₂ : AtomKnot) : Prop :=
  K₁.Z = K₂.Z ∧ K₁.protonBlock = K₂.protonBlock

end QOU.BraidKnot
