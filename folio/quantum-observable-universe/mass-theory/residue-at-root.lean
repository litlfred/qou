import QOU.BraidKnot.ResidueAtRoot

/-!
# prop:residue-at-root — cyclotomic residue as projection image

**Proposition (conditional on `conj:gs-residue-at-root-existence`,
per AGENTS.md §3b-cond).**  The class `QOU.BraidKnot.ResidueAtRoot`
is the class axiomatisation of the existence conjecture: an instance
supplies the Habiro-completion cyclotomic projection
`π_n : R →+* ℤ[q]/Φ_n(q)`.  Conditional on that instance, this file
*derives* the proposition's content — the cyclotomic residue is well
defined as the image under the projection, realised by a ring
homomorphism (hence multiplicative).

LaTeX label: `prop:residue-at-root`
-/

namespace QOU.BraidKnot

universe u

/-- **Proposition (conditional on `conj:gs-residue-at-root-existence`).**
    Given the cyclotomic-projection machinery `[ResidueAtRoot R]` (the
    class axiomatisation of the existence conjecture), the residue at
    root index `n` is well defined as the image under a ring
    homomorphism into the target ring `ℤ[q]/Φ_n(q)`. -/
theorem residue_isRingHom_of_residueAtRoot {R : Type u} [CommRing R]
    [r : ResidueAtRoot R] (n : ℕ) :
    ∃ f : R →+* r.target n, ∀ x : R, residue n x = f x :=
  ⟨r.project n, fun _ => rfl⟩

/-- **Residue of product (conditional corollary).**
    The cyclotomic residue of a product is the product of residues. -/
theorem residue_of_product {R : Type u} [CommRing R] [ResidueAtRoot R]
    (n : ℕ) (x y : R) :
    residue n (x * y) =
      residue n x * residue n y := by
  -- Ref: [leitner2026] prop:residue-at-root
  exact RingHom.map_mul _ x y

end QOU.BraidKnot
