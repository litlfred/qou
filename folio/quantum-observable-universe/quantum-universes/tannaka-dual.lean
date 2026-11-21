import Mathlib.CategoryTheory.Monoidal.NaturalTransformation
import Mathlib.CategoryTheory.Endomorphism

/-!
# QOU.TannakaDual — the emergent gauge group `G = Aut⊗(τ)`

The gauge group of a quantum observable universe emerges from the pair
`(𝐂, τ)` with `τ` the fibre functor. A symmetry is a monoidal natural
automorphism of `τ` — a family of automorphisms compatible with the tensor
product. The **Tannaka dual** `G = Aut⊗(τ)` collects these. Because a
`LaxMonoidalFunctor` lives in a category whose morphisms are *monoidal* natural
transformations, `Aut τ` is exactly the tensor-automorphism group, and it
carries a canonical `Group` structure. By Tannaka–Krein duality `G` is an
affine group scheme and `𝐂 ≃ Rep(G)`.

## References
- [deligne1990] Deligne, "Catégories tannakiennes"
- [leitner2026] §"The fundamental object and the emergent gauge group"
-/

namespace QOU

open CategoryTheory MonoidalCategory

universe u v w

/-- **Tannaka dual / emergent gauge group** `G = Aut⊗(τ)` of a fibre functor
    `τ`. Automorphisms are taken in the category of monoidal functors — whose
    morphisms are monoidal natural transformations — so `Aut τ` is precisely
    the group of *tensor*-natural automorphisms. -/
abbrev TannakaDual {C : Type u} [Category.{v} C] [MonoidalCategory C]
    {D : Type w} [Category.{v} D] [MonoidalCategory D]
    (τ : LaxMonoidalFunctor C D) : Type _ := Aut τ

/-- The Tannaka dual is a group: monoidal natural automorphisms of `τ` compose
    and invert. (The instance is inherited from `Aut`; stated explicitly as the
    gauge-group content.) -/
noncomputable instance groupTannakaDual
    {C : Type u} [Category.{v} C] [MonoidalCategory C]
    {D : Type w} [Category.{v} D] [MonoidalCategory D]
    (τ : LaxMonoidalFunctor C D) : Group (TannakaDual τ) :=
  inferInstanceAs (Group (Aut τ))

end QOU
