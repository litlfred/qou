import QOU.BraidsAndKnots.HAdicDrinfeld.ModuleUnit
import QOU.BraidsAndKnots.HAdicDrinfeld.ModulePentagon
import Mathlib.CategoryTheory.Monoidal.Category

/-!
# The monoidal category of representations modulo `h^N`

Epic `qou-dk7p`, step B of `docs/audits/2026-11-27-kz-trio-strangler-plan.md`.

The previous files give every piece of a monoidal structure on `Rep.{u, w, u} D`: the tensor
product of objects and morphisms (`ModuleCategory`), the associator `α = a ∘ ρ(Φ)`
(`ModuleAssociator`), the unit and unitors with the triangle (`ModuleUnit`) and the pentagon
(`ModulePentagon`). This file assembles them into Mathlib's `MonoidalCategory`, through
`MonoidalCategory.ofTensorHom`.

The hypotheses on the associator `Φ ∈ FreeAlgebra ℚ (Fin 2)` are collected in `AssocData`:
`Φ` is invertible modulo the filtration (`Inv512 (Fil N 1) Φ`), has constant term `1`, and
satisfies the pentagon in `U4 N`. Over `k = ℚ[h]/(h^N)` with `c = h`, every rational associator
gives such data. No analysis and no numerical value is used.
-/

namespace QOU.BraidsAndKnots.HAdicDrinfeld

open scoped TensorProduct
open CategoryTheory
open QOU.HeckeTemperleyLieb.QuasiYangBaxterFromHexagon
open QOU.BraidsAndKnots.RationalAssociator

set_option linter.unusedSectionVars false

universe u w

variable {k : Type u} {A : Type w} [CommRing k] [Algebra ℚ k] [Ring A] [Algebra k A]
  [Algebra ℚ A] [IsScalarTower ℚ k A]

/-- The data of a truncated h-adic associator for a `CasimirData`: a nilpotent scale `c`
(`c ^ N = 0`), a counit, and a rational `Φ` that is invertible modulo the filtration, has
constant term `1`, and satisfies the pentagon in `U4 N`. -/
structure AssocData (D : CasimirData k A) where
  /-- The truncation order. -/
  N : ℕ
  /-- The scale, e.g. `h` in `ℚ[h]/(h^N)`. -/
  c : k
  hc : c ^ N = 0
  /-- The counit. -/
  U : CounitData D
  /-- The associator, a word series in two letters. -/
  Φ : FreeAlgebra ℚ (Fin 2)
  inv : Inv512 (Fil N 1) Φ
  const : FreeAlgebra.algebraMapInv Φ = 1
  pentagon : Pentagon Φ (RationalAssociator.t N 0) (RationalAssociator.t N 1)
    (RationalAssociator.t N 3) (RationalAssociator.t N 4) (RationalAssociator.t N 5)

namespace Rep

variable {D : CasimirData k A} (P : AssocData D)

/-- The monoidal structure data on `Rep.{u, w, u} D` for the associator data `P`. -/
@[reducible] noncomputable def monoidalStruct : MonoidalCategoryStruct (Rep.{u, w, u} D) where
  tensorObj := tensorObj
  whiskerLeft X _ _ f := tensorHom (𝟙 X) f
  whiskerRight f Y := tensorHom f (𝟙 Y)
  tensorHom := tensorHom
  tensorUnit := unit P.U
  associator := associator P.c P.hc P.U P.inv
  leftUnitor := leftUnitor P.U
  rightUnitor := rightUnitor P.U

/-- **The monoidal category of representations modulo `h^N`**, with tensor product through the
coproduct `Δ`, unit `k` through the counit, and associator `a ∘ ρ(Φ)`. -/
noncomputable def monoidal : MonoidalCategory (Rep.{u, w, u} D) :=
  letI := monoidalStruct P
  MonoidalCategory.ofTensorHom
    (id_tensorHom_id := fun X Y => tensorHom_id X Y)
    (id_tensorHom := fun _ _ _ _ => rfl)
    (tensorHom_id := fun _ _ => rfl)
    (tensorHom_comp_tensorHom := fun f₁ f₂ g₁ g₂ => (tensorHom_comp f₁ g₁ f₂ g₂).symm)
    (associator_naturality := fun f₁ f₂ f₃ => associatorHom_naturality P.c P.hc P.U f₁ f₂ f₃)
    (leftUnitor_naturality := fun f => leftUnitor_naturality P.U f)
    (rightUnitor_naturality := fun f => rightUnitor_naturality P.U f)
    (pentagon := fun W X Y Z => pentagon W X Y Z P.c P.hc P.U P.pentagon)
    (triangle := fun X Y => triangle P.U P.c P.hc P.const X Y)

end Rep

end QOU.BraidsAndKnots.HAdicDrinfeld
