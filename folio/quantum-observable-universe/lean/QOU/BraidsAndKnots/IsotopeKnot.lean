import Mathlib.Tactic

/-!
# QOU.BraidKnot.IsotopeKnot

**Canonical declaration** for content block at
[`quantum-observable-universe/particle-interactions/isotope-knot-equivalence-proof.ts`](quantum-observable-universe/particle-interactions/isotope-knot-equivalence-proof.ts).

Formalises the manuscript proof that isotope equivalence — `K₁ ∼ K₂` iff
their proton-block invariants agree, `w_{q^Z}(K₁) = w_{q^Z}(K₂)` — is an
equivalence relation, so the quotient at fixed `Z` is the element class
(element = isotope class). Pure algebra — generic over the invariant target
(§7c-clean).
-/

namespace QOU.BraidKnot

/-- Isotope-equivalence data at fixed proton number `Z`.

    A `definition` carrier: a type `AtomKnot` of atom-knots and the
    proton-block invariant `w` into some value type `W`. Two atom-knots are
    isotope-equivalent when their invariants agree. -/
structure IsotopeKnot (AtomKnot : Type*) (W : Type*) where
  /-- The proton-block invariant `w_{q^Z}`. -/
  w : AtomKnot → W

namespace IsotopeKnot

variable {AtomKnot W : Type*} (I : IsotopeKnot AtomKnot W)

/-- Isotope equivalence: `K₁ ∼ K₂` iff `w(K₁) = w(K₂)`. -/
def IsoEquiv (K₁ K₂ : AtomKnot) : Prop := I.w K₁ = I.w K₂

/-- Isotope equivalence is reflexive (manuscript "Reflexivity"). -/
theorem isoEquiv_refl (K : AtomKnot) : I.IsoEquiv K K := rfl

/-- Isotope equivalence is symmetric (manuscript "Symmetry"). -/
theorem isoEquiv_symm {K₁ K₂ : AtomKnot} (h : I.IsoEquiv K₁ K₂) :
    I.IsoEquiv K₂ K₁ := h.symm

/-- Isotope equivalence is transitive (manuscript "Transitivity"). -/
theorem isoEquiv_trans {K₁ K₂ K₃ : AtomKnot}
    (h₁ : I.IsoEquiv K₁ K₂) (h₂ : I.IsoEquiv K₂ K₃) : I.IsoEquiv K₁ K₃ :=
  h₁.trans h₂

/-- The manuscript's claim assembled: isotope equivalence is an
    `Equivalence`, so `{atom-knots}/∼` (the element class for `Z`) is a
    well-defined quotient. -/
theorem isoEquiv_equivalence : Equivalence I.IsoEquiv :=
  ⟨I.isoEquiv_refl, I.isoEquiv_symm, I.isoEquiv_trans⟩

/-- The element class as the `Setoid` induced by isotope equivalence. -/
def elementSetoid : Setoid AtomKnot := ⟨I.IsoEquiv, I.isoEquiv_equivalence⟩

end IsotopeKnot

-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/isotope-knot-equivalence-proof.ts

end QOU.BraidKnot
