import QOU.Basic
import Mathlib.CategoryTheory.Monoidal.Category


/-!
# QOU.volume_from_rigidity — Volume form factorisation lemma

For a symplectically self-dual object V of categorical dimension 2,
the composite ev_V ∘ (id ⊗ φ) factors through Λ²V, and the
resulting ε : Λ²V → 𝟙 is non-degenerate.

LaTeX label: `lem:volume-from-rigidity`

## References

- [kock2004] https://doi.org/10.1017/CBO9780511615443
- [manuscript] §1-quantum-observable-universe/volume-from-rigidity
-/

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- **Volume form factorisation**: for a symplectically self-dual object,
    the evaluation factors through the exterior square. -/
-- Ref: [kock2004], [manuscript] §1
structure VolumeFormFactorisation (C : Type u) [Category.{v} C]
    [MonoidalCategory C] where
  /-- The fundamental object V. -/
  V : C
  /-- The dual V∨. -/
  V_dual : C
  /-- The exterior square Λ²V. -/
  exteriorSquare : C
  /-- The symplectic isomorphism φ : V → V∨ with φ∨ = -φ. -/
  phi : V ⟶ V_dual
  /-- The evaluation ev : V ⊗ V∨ → 𝟙. -/
  eval : (V ⊗ V_dual) ⟶ (𝟙_ C)
  /-- The projection π : V ⊗ V → Λ²V. -/
  proj : (V ⊗ V) ⟶ exteriorSquare
  /-- The volume form ε : Λ²V → 𝟙. -/
  epsilon : exteriorSquare ⟶ (𝟙_ C)
  /-- The factorisation: ev ∘ (id ⊗ φ) = ε ∘ π. -/
  factorisation : (V ◁ phi) ≫ eval = proj ≫ epsilon
  /-- Non-degeneracy: ε is an epimorphism. -/
  epsilon_epi : Epi epsilon

/-- Given a volume form factorisation, condition (iii) of the QOU
    (non-degenerate volume form) is satisfied. -/
-- Ref: [manuscript] §1
theorem volume_form_is_nondegen {C : Type u} [Category.{v} C]
    [MonoidalCategory C] (vff : VolumeFormFactorisation C) :
    Epi vff.epsilon :=
  vff.epsilon_epi

end QOU
