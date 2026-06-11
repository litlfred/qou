import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Category.Basic


/-!
# QOU.SnakeIdentity

The snake identities (zig-zag identities) for an exact pairing in a
rigid monoidal category. These are already encoded as fields of
`QOU.RigidMonoidalCategory`; this module re-exports them as
standalone propositions for cross-referencing.

LaTeX: `\label{def:snake-identity}`
Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
-/

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- **Snake identity (left)**: the composite
    `V →[ρ⁻¹] V ⊗ 𝟙 →[V ◁ coev] V ⊗ (V∨ ⊗ V) →[α⁻¹] (V ⊗ V∨) ⊗ V
     →[ev ▷ V] 𝟙 ⊗ V →[λ_] V`
    equals `𝟙 V`.

    This is the defining property of a right dual (one half of an
    exact pairing). See `RigidMonoidalCategory.snake_left`. -/
def snake_identity_left {C : Type u} [Category.{v} C] [MonoidalCategory C]
    (V V_dual : C)
    (eval : (V ⊗ V_dual) ⟶ (𝟙_ C))
    (coeval : (𝟙_ C) ⟶ (V_dual ⊗ V)) : Prop :=
  (ρ_ V).inv ≫ (V ◁ coeval) ≫ (α_ V V_dual V).inv ≫
    (eval ▷ V) ≫ (λ_ V).hom = 𝟙 V

/-- **Snake identity (right)**: the composite
    `V∨ →[λ_⁻¹] 𝟙 ⊗ V∨ →[coev ▷ V∨] (V∨ ⊗ V) ⊗ V∨ →[α] V∨ ⊗ (V ⊗ V∨)
     →[V∨ ◁ ev] V∨ ⊗ 𝟙 →[ρ_] V∨`
    equals `𝟙 V∨`. -/
def snake_identity_right {C : Type u} [Category.{v} C] [MonoidalCategory C]
    (V V_dual : C)
    (eval : (V ⊗ V_dual) ⟶ (𝟙_ C))
    (coeval : (𝟙_ C) ⟶ (V_dual ⊗ V)) : Prop :=
  (λ_ V_dual).inv ≫ (coeval ▷ V_dual) ≫ (α_ V_dual V V_dual).hom ≫
    (V_dual ◁ eval) ≫ (ρ_ V_dual).hom = 𝟙 V_dual

end QOU
