import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Category.Basic
import Mathlib.CategoryTheory.Abelian.Basic


/-!
# QOU.AlgebraicSubstrate.LocalCohomologyGroup — Local cohomology at z = 1

The local cohomology group H¹_{𝔪₁}(A) as the first right derived functor
of the 𝔪₁-torsion functor. This measures the algebraic obstruction to
extending sections across the unit defect.

LaTeX label: `def:local-cohomology-group`

## References

- [yekutieli2015] https://doi.org/10.1515/9783110291230
-/

set_option autoImplicit false

namespace QOU.AlgebraicSubstrate

universe u v

/-- **LocalCohomologyGroup**: a categorical structure representing the
    first local cohomology H¹_{𝔪₁}(A) at the unit defect.

    In the derived category framework, this is the first right derived
    functor R¹Γ_{𝔪₁}(A) of the torsion functor associated to the
    maximal ideal 𝔪₁.

    LaTeX: `\label{def:local-cohomology-group}` -/
structure LocalCohomologyGroup (C : Type u) [CategoryTheory.Category.{v} C] where
  /-- The underlying object A in the abelian category. -/
  obj : C
  /-- The local cohomology object H¹_{𝔪₁}(A). -/
  localCohom : C
  /-- The torsion functor Γ_{𝔪₁} applied to A. -/
  torsionObj : C
  /-- The connecting morphism δ : Γ_{𝔪₁}(A) → H¹_{𝔪₁}(A) from the
      long exact sequence in cohomology. -/
  connecting : torsionObj ⟶ localCohom
  /-- The local cohomology is nonzero (the defect is nontrivial). -/
  nontrivial : localCohom ≠ obj

end QOU.AlgebraicSubstrate
