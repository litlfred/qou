/-!
# QOU.BraidKnot.IsotopeKnot.equivalence — isotope is an equivalence relation

LaTeX: `\label{prop:isotope-knot-equivalence}`
-/

import QOU.Basic

namespace QOU.BraidKnot

/-- **Isotope relation is reflexive.** -/
theorem AtomKnot.isIsotope_refl (K : AtomKnot) : K.isIsotope K :=
  ⟨rfl, rfl⟩

/-- **Isotope relation is symmetric.** -/
theorem AtomKnot.isIsotope_symm (K₁ K₂ : AtomKnot)
    (h : K₁.isIsotope K₂) : K₂.isIsotope K₁ :=
  ⟨h.1.symm, h.2.symm⟩

/-- **Isotope relation is transitive.** -/
theorem AtomKnot.isIsotope_trans (K₁ K₂ K₃ : AtomKnot)
    (h₁₂ : K₁.isIsotope K₂) (h₂₃ : K₂.isIsotope K₃) :
    K₁.isIsotope K₃ :=
  ⟨h₁₂.1.trans h₂₃.1, h₁₂.2.trans h₂₃.2⟩

end QOU.BraidKnot
