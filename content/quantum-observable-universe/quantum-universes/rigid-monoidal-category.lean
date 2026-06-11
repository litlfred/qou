import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Category.Basic


/-!
# QOU.RigidMonoidalCategory

A rigid monoidal category: a monoidal category where every object has
a dual satisfying the snake identities (evaluation/coevaluation).

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse.lean (monolithic)
-/

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- **Rigid monoidal category data**: for a given object `V` in a monoidal
    category `C`, a rigidity structure consists of a dual `V∨`, evaluation
    `ev : V ⊗ V∨ → 𝟙`, and coevaluation `coev : 𝟙 → V∨ ⊗ V` satisfying
    the snake identities.

    LaTeX: `\label{def:rigid-monoidal-category}`
    Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443 -/
structure RigidMonoidalCategory (C : Type u) [Category.{v} C]
    [MonoidalCategory C] where
  /-- The object for which we exhibit rigidity. -/
  V : C
  /-- The (right) dual object `V∨`. -/
  V_dual : C
  /-- Evaluation morphism `ev : V ⊗ V∨ → 𝟙`. -/
  eval : (V ⊗ V_dual) ⟶ (𝟙_ C)
  /-- Coevaluation morphism `coev : 𝟙 → V∨ ⊗ V`. -/
  coeval : (𝟙_ C) ⟶ (V_dual ⊗ V)
  /-- **Snake identity (left)**: the composite
      `V →[ρ⁻¹] V ⊗ 𝟙 →[V ◁ coev] V ⊗ (V∨ ⊗ V) →[α⁻¹] (V ⊗ V∨) ⊗ V
       →[ev ▷ V] 𝟙 ⊗ V →[λ_] V`
      equals `𝟙 V`. -/
  snake_left :
    (ρ_ V).inv ≫ (V ◁ coeval) ≫ (α_ V V_dual V).inv ≫
      (eval ▷ V) ≫ (λ_ V).hom = 𝟙 V
  /-- **Snake identity (right)**: the composite
      `V∨ →[λ_⁻¹] 𝟙 ⊗ V∨ →[coev ▷ V∨] (V∨ ⊗ V) ⊗ V∨ →[α] V∨ ⊗ (V ⊗ V∨)
       →[V∨ ◁ ev] V∨ ⊗ 𝟙 →[ρ_] V∨`
      equals `𝟙 V∨`. -/
  snake_right :
    (λ_ V_dual).inv ≫ (coeval ▷ V_dual) ≫ (α_ V_dual V V_dual).hom ≫
      (V_dual ◁ eval) ≫ (ρ_ V_dual).hom = 𝟙 V_dual

end QOU
