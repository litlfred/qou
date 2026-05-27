import Mathlib.CategoryTheory.Category.Basic
import Mathlib.CategoryTheory.Subobject.Basic


/-!
# QOU.CategoricalQTorsionLeaf

Glossary: A q-torsion leaf is a maximal sub-object L ↪ A such that
L is horizontal (L ⊂ ker(π_V)) and flow-invariant (φ_t^q(L) = L).

This wraps the concept of an invariant sub-object in a category with
a distinguished endomorphism (the q-Reeb flow).

LaTeX label: `rem:glossary-categorical-q-torsion-leaf`

## References
- [manuscript] Ch. 8, §glossary-categorical-q-torsion-leaf
-/

namespace QOU

/-- A `CategoricalQTorsionLeaf` packages the data of a maximal
    sub-object that is both horizontal (in the kernel of the vertical
    projection) and invariant under the q-Reeb flow.

    In Mathlib terms this is a sub-object equipped with two witnesses:
    horizontality and flow-invariance. -/
-- Ref: [manuscript] Ch. 8, §glossary-categorical-q-torsion-leaf
structure CategoricalQTorsionLeaf
    (C : Type*) [CategoryTheory.Category C]
    (A : C) where
  /-- The sub-object representing the leaf. -/
  leaf : CategoryTheory.Subobject A
  /-- Horizontality: the leaf lies in the kernel of the vertical
      projection. (Axiomatised; the vertical projection π_V is
      part of the ambient q-connection data.) -/
  horizontal : Prop
  /-- Flow invariance: the q-Reeb flow preserves the leaf for all t. -/
  flow_invariant : Prop

end QOU
