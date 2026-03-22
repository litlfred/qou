/-!
# QOU.MaximalTorus

The maximal torus `T` of the gauge group, defined as the subgroup of
`Aut⊗(ω)` acting diagonally on each weight space of the fundamental
object `V`.

Extracted from lean-archive/ for content-block co-location.
Source: lean-archive/QOU/QuantumObservableUniverse.lean (monolithic)
-/

import Mathlib.CategoryTheory.Monoidal.Basic
import Mathlib.CategoryTheory.Category.Basic
import Mathlib.CategoryTheory.NatTrans

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- **Maximal torus and weight subcategory**.

    Given a quantum observable universe `(C, A, ω)` with fundamental object
    `V`, the weight subcategory `⟨V⟩ ⊂ C` is the full subcategory whose
    objects are direct sums of weight spaces of `V`.  The maximal torus is
    `T = Aut⊗(ω|_{⟨V⟩})`, the subgroup of `G = Aut⊗(ω)` consisting of
    natural automorphisms acting diagonally on each weight space.

    LaTeX: `\label{def:maximal-torus}`
    Ref: [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9 -/
structure MaximalTorus (C : Type u) [Category.{v} C]
    [MonoidalCategory C] where
  /-- The fundamental object `V` of categorical dimension 2. -/
  V : C
  /-- The fibre functor `ω : C → Type*`. -/
  fibreFunctor : Functor C (Type*)
  /-- The number of weight spaces of `V` under the torus action. -/
  numWeights : ℕ
  /-- The diagonal automorphism type (abstracting `T ≅ U(1)^r`). -/
  torusType : Type*
  /-- The torus carries a group structure. -/
  [torusGroup : Group torusType]
  /-- The torus embeds into the gauge group: every torus element
      yields a natural isomorphism `ω ≅ ω`. -/
  embed : torusType → (fibreFunctor ≅ fibreFunctor)

end QOU
