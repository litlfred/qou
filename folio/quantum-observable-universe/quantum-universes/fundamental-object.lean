import Mathlib.CategoryTheory.Monoidal.Category

/-!
# QOU.FundamentalObject — the fundamental object `V`

A rigid monoidal category's **fundamental object**: a simple object `V` carrying
a non-degenerate volume form `volume : V ⊗ V ⟶ 𝟙` (the categorical determinant
`Λ²V → 𝟙`) together with its adjoint coform, satisfying the two snake identities
that make `V` self-dual. Over `Rep(SU(2))` this is `V = V_{1/2} ≅ ℂ²`; abstractly
it is the unique simple object of categorical dimension `2` (Deligne–Milne). The
self-duality via an antisymmetric form is exactly what cuts `SL₂/SU(2)` out of
`GL₂` (a *symplectic self-dual object* of dimension 2).

## References
- [deligne1990] Deligne, "Catégories tannakiennes"
- [leitner2026] §"The fundamental object and the emergent gauge group"
-/

namespace QOU

open CategoryTheory MonoidalCategory

universe u v

/-- **Fundamental object.** A self-dual object `V` of a monoidal category
    together with a volume form `volume : V ⊗ V ⟶ 𝟙` (the categorical
    determinant `Λ²V → 𝟙`) and its adjoint `coform : 𝟙 ⟶ V ⊗ V`, satisfying
    the two snake identities. Together `(volume, coform)` exhibit `V ⊣ V`, i.e.
    `V` is its own dual. The volume constraint pins the categorical dimension to
    `2`; abstractly `V` is the unique such simple object and tensor-generates
    the category. -/
structure FundamentalObject (C : Type u) [Category.{v} C] [MonoidalCategory C] where
  /-- the fundamental object itself. -/
  V : C
  /-- the volume form `ε : V ⊗ V ⟶ 𝟙` — the categorical determinant `Λ²V → 𝟙`. -/
  volume : V ⊗ V ⟶ 𝟙_ C
  /-- its adjoint coform `η : 𝟙 ⟶ V ⊗ V`, exhibiting self-duality. -/
  coform : 𝟙_ C ⟶ V ⊗ V
  /-- left snake (zig-zag) identity: `(volume, coform)` is a duality `V ⊣ V`. -/
  snake_left :
    (λ_ V).inv ≫ coform ▷ V ≫ (α_ V V V).hom ≫ V ◁ volume ≫ (ρ_ V).hom = 𝟙 V
  /-- right snake (zig-zag) identity. -/
  snake_right :
    (ρ_ V).inv ≫ V ◁ coform ≫ (α_ V V V).inv ≫ volume ▷ V ≫ (λ_ V).hom = 𝟙 V

end QOU
