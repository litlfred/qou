import QOU.Basic
import QOU.QuantumObservableUniverse
import QOU.GrobnerShirshov
import Fred2005.FormalGroups
import Mathlib.Data.Real.Basic
import Mathlib.CategoryTheory.Monoidal.Category

/-!
# Formal Groups — QOU Interface

Re-exports the formal-groups integration results from the Fred 2005
dissertation and provides the QOU-specific categorical interface
(strong multiplicativity via `FrobeniusHopfData`).

The core definitions and theorems live in `Fred2005.FormalGroups`;
this module bridges them into the QOU namespace.

## Structure

1. **Re-exports** — `CommutativeFormalGroup`, `SkewedPoissonStructure`, etc.
2. **Strong multiplicativity (categorical)** — Frobenius relation on `FrobeniusHopfData`
3. **Connection to QOU jet prolongation** — unit-root ↔ integrability bridge
4. **Gröbner–Shirshov bridge** — connection to `QOU.GrobnerShirshov.*`

## Status

The Gröbner–Shirshov core (composition lemma, normal forms, flatness,
strong multiplicativity) is now formalized in `QOU.GrobnerShirshov.*`.
Remaining `sorry`s in `Fred2005.FormalGroups` mark results that depend
on domain-specific integration arguments beyond the GS framework.

## References

- [fred2005] L. Fred, PhD thesis, University of Arizona, 2005.
- [hazewinkel1978] M. Hazewinkel, *Formal Groups and Applications*, Academic Press.
- [zink2002] T. Zink, *The Display of a Formal p-Divisible Group*, Astérisque 278.
-/


open scoped CategoryTheory CategoryTheory.MonoidalCategory
open Fred2005

namespace QOU.FormalGroups

universe u v

/-! ## §1  Re-exports from Fred2005

All core formal-group structures and theorems are defined in
`Fred2005.FormalGroups`.  We re-export the namespace here so
that downstream QOU modules can use unqualified names. -/

export Fred2005 (CommutativeFormalGroup SkewedPoissonStructure
  NoncommutativeFormalGroup GrobnerShirshovBasis WittVectorLift
  UnitRootFCrystal skew_poisson_integrates reduction_mod_p_commutative
  grobner_shirshov_basis_exists strong_multiplicativity_holds
  witt_vector_lift_exists unit_root_iff_integrable)

/-! ## §2  Strong Multiplicativity (Categorical Form)

The categorical form of strong multiplicativity operates on
`FrobeniusHopfData` — the monoidal-category structure used in the QOU.
This wraps the algebraic condition from [fred2005, Theorem 4.12] into
the language of monoidal categories. -/

/-- **Strong multiplicativity condition** (categorical form):
    the Frobenius relation
    `(Id ⊗ m) ∘ (Δ ⊗ Id) = Δ ∘ m = (m ⊗ Id) ∘ (Id ⊗ Δ)`
    is preserved under the Gröbner–Shirshov deformation of the
    distribution algebra.

    LaTeX: `\label{prop:skew-poisson-integration}`, item (3).
    Reference: [fred2005, Theorem 4.12]. -/
structure StrongMultiplicativity (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] where
  /-- The Frobenius–Hopf object before deformation. -/
  base : FrobeniusHopfData C
  /-- The Frobenius–Hopf object after deformation. -/
  deformed : FrobeniusHopfData C
  /-- The deformation map preserves the Frobenius relation.
      [fred2005, Theorem 4.12] -/
  frobenius_preserved :
    deformed.mul ≫ deformed.comul =
    (deformed.comul ▷ deformed.obj) ≫ (deformed.obj ◁ deformed.mul)

end QOU.FormalGroups
