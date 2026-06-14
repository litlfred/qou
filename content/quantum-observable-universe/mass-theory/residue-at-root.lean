import QOU.BraidKnot.ResidueAtRoot

namespace QOU.BraidKnot

universe u

/-- **Theorem (residue of product).**
    The cyclotomic residue of a product is the product of residues. -/
theorem residue_of_product {R : Type u} [CommRing R] [ResidueAtRoot R]
    (n : ℕ) (x y : R) :
    ResidueAtRoot.residue n (x * y) =
      ResidueAtRoot.residue n x * ResidueAtRoot.residue n y := by
  -- Ref: [manuscript] prop:residue-at-root
  exact RingHom.map_mul _ x y

end QOU.BraidKnot
