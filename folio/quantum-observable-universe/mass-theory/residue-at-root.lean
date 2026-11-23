import QOU.BraidKnot.ResidueAtRoot
import QOU.BraidKnot.QHabiroCompletion

/-!
# prop:residue-at-root — cyclotomic residue as projection image

The cyclotomic projection `π_n : Ẑ[q] →+* ℤ[q]/Φ_n(q)` on the Habiro
completion is **constructed**, not assumed: `QOU.BraidKnot.QHabiro.project`
in `QOU/BraidKnot/QHabiroCompletion.lean` (thread ring of compatible classes
modulo `(q;q)_N`, then the factor map along `Φ_n ∣ (q;q)_n`). The class
`ResidueAtRoot` therefore has an instance, `QHabiro.instResidueAtRoot`.

The proposition is proved for every element of the Habiro ring: the residue
at root index `n` is the image under a ring homomorphism, hence additive and
multiplicative, and on polynomials it is reduction modulo `Φ_n`.

**What is not proved here.** That `Φ_q · tr_{M,ℓ}(T_w)` is an element of the
Habiro ring, that its residue is real, and that it depends only on the class
of `T_w` modulo `J^{ℓ+1}`. Those are the open content of
`conj:gs-residue-at-root-existence`; the proposition takes membership as a
hypothesis on its argument (`x : Habiro`).

The generic statements over an arbitrary `[ResidueAtRoot R]` are kept below;
they now have a concrete instance.

LaTeX label: `prop:residue-at-root`
-/

namespace QOU.BraidKnot

universe u

/-- Over any carrier with a cyclotomic projection, the residue at root index
    `n` is the image under a ring homomorphism. -/
theorem residue_isRingHom_of_residueAtRoot {R : Type u} [CommRing R]
    [r : ResidueAtRoot R] (n : ℕ) :
    ∃ f : R →+* r.target n, ∀ x : R, residue n x = f x :=
  ⟨r.project n, fun _ => rfl⟩

/-- The cyclotomic residue of a product is the product of residues. -/
theorem residue_of_product {R : Type u} [CommRing R] [ResidueAtRoot R]
    (n : ℕ) (x y : R) :
    residue n (x * y) =
      residue n x * residue n y := by
  -- Ref: [habiro2004] §1.2 (evaluation at a root of unity extends to the Habiro ring)
  exact RingHom.map_mul _ x y

open Polynomial in
/-- **Proposition (`prop:residue-at-root`), on the constructed Habiro ring.**
    For every element `x` of the Habiro completion and every `n ≥ 1`, the
    residue at the primitive `n`-th root of unity is `π_n x`, the image of `x`
    under the constructed ring homomorphism `Ẑ[q] →+* ℤ[q]/Φ_n(q)`; on a
    polynomial `p` it is the class of `p` modulo `Φ_n`. -/
theorem residue_at_root (n : ℕ) (x : QHabiro.Habiro) (p : ℤ[X]) :
    residue (R := QHabiro.Habiro) n x = QHabiro.project (n + 1) (Nat.succ_ne_zero n) x ∧
      residue (R := QHabiro.Habiro) n (QHabiro.ofPoly p)
        = Ideal.Quotient.mk (Ideal.span {cyclotomic (n + 1) ℤ}) p :=
  ⟨rfl, QHabiro.residue_ofPoly n p⟩

end QOU.BraidKnot
