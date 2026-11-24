import Mathlib.CategoryTheory.Category.Basic
import Mathlib.CategoryTheory.Subobject.Basic
import Mathlib.CategoryTheory.Subobject.Limits
import Mathlib.CategoryTheory.Limits.Shapes.Pullback.HasPullback


/-!
# QOU.CategoricalQTorsionLeaf

Glossary: A q-torsion leaf is a maximal sub-object L ↪ A such that
L is horizontal (L ⊂ ker(π_V)) and flow-invariant (φ_t^q(L) = L).

This wraps the concept of an invariant sub-object in a category with
a distinguished endomorphism (the q-Reeb flow).

LaTeX label: `rem:glossary-categorical-q-torsion-leaf`

## References
- [leitner2026] Ch. 8, §glossary-categorical-q-torsion-leaf
-/

namespace QOU

open CategoryTheory

/-- A `CategoricalQTorsionLeaf` packages the data of a maximal
    sub-object that is both horizontal (in the kernel of the vertical
    projection) and invariant under the q-Reeb flow.

    In Mathlib terms this is a sub-object equipped with two witnesses:
    horizontality and flow-invariance. -/
-- Ref: [leitner2026] Ch. 8, §glossary-categorical-q-torsion-leaf
structure CategoricalQTorsionLeaf
    (C : Type*) [Category C]
    [Limits.HasZeroMorphisms C]
    [Limits.HasPullbacks C]
    (A : C)
    (piV : A ⟶ A) (flow : A ⟶ A) where
  /-- The sub-object representing the leaf. -/
  leaf : Subobject A
  /-- **Horizontality**: the leaf lies in the kernel of the vertical
      projection — its arrow composed with `π_V` is zero.

      Was `horizontal : Prop`, a field typed with the universe `Prop`, so the
      instance chose the condition and `True` discharged it. The docstring
      said the projection is "part of the ambient q-connection data"; `piV`
      is now a parameter, which is what that sentence means in a type. -/
  horizontal : leaf.arrow ≫ piV = 0
  /-- **Flow invariance**: the q-Reeb flow preserves the leaf, stated as
      `φ^*(L) = L` on sub-objects. -/
  flow_invariant : (Subobject.pullback flow).obj leaf = leaf

end QOU
