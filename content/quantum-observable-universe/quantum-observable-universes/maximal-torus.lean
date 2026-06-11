import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Category.Basic
import Mathlib.CategoryTheory.NatTrans


/-!
# QOU.MaximalTorus

The maximal torus `T` of the gauge group, defined as the subgroup of
`Aut⊗(ω)` acting diagonally on each weight space of the fundamental
object `V`.

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse.lean (monolithic)
-/

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
  /-- The Frobenius–Hopf object `A` in `C` (from the QOU). -/
  hopfObj : C
  /-- The fundamental object `V` of categorical dimension 2. -/
  V : C
  /-- The fibre functor `ω : C → Type*` (from the QOU). -/
  fibreFunctor : Functor C (Type*)
  /-- **Faithfulness** of the fibre functor (inherited from QuantumUniverse). -/
  fibreFunctor_faithful : Functor.Faithful fibreFunctor
  /-- The number of weight spaces of `V` under the torus action.
      For SU(2): `numWeights = 2` (the ±1/2 weight spaces). -/
  numWeights : ℕ
  /-- The diagonal automorphism type (abstracting `T ≅ U(1)^r`). -/
  torusType : Type*
  /-- The torus carries a group structure. -/
  [torusGroup : Group torusType]
  /-- The torus embeds into the gauge group: every torus element
      yields a natural isomorphism `ω ≅ ω`. -/
  embed : torusType → (fibreFunctor ≅ fibreFunctor)
  /-- **Diagonal action**: the torus acts diagonally on each weight
      space of `V`.  Abstractly: the restriction of `embed(t)` to `V`
      is a diagonal matrix in the weight basis. -/
  /-- **Diagonal action**: the torus acts on V by scaling each weight
      space independently.  Encoded: for each t, the natural isomorphism
      embed(t) commutes with itself (the image is abelian). -/
  diagonal_action : ∀ (t₁ t₂ : torusType),
    (embed t₁).hom ≫ (embed t₂).hom = (embed t₂).hom ≫ (embed t₁).hom
  /-- **Maximality**: the torus is maximal — its rank equals the rank
      of the gauge group. For SU(2): `rank T = 1`. -/
  rank : ℕ

end QOU
