import QOU.KZ.Drinfeld.Hexagon
import Mathlib.CategoryTheory.Monoidal.Braided.Basic

/-!
# `D_ℏ` is a braided monoidal category

Stage S3 of bean `qou-zoyv`. For `ℏ` transcendental over `ℚ`, the Drinfeld category `DH ℏ`
(tensor words in `V = ℂ²`, `sl₂`-equivariant maps, the KZ associator) carries the braiding
`β_{X,Y} = swap · exp(iπℏ t^{sl}_{X,Y})`. Naturality is `βmat_natural`; the two hexagons are
`hexagon_fwd_mat` / `hexagon_rev_mat`. Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S3)
-/

noncomputable section

namespace QOU.KZ.Drinfeld

open CategoryTheory MonoidalCategory QOU.KZ.DrinfeldAssociator

variable (Ψ : Associator.{0}) (c : ℂ) [hc : Fact (Transcendental ℚ c)]

/-- **`D_ℏ` is a braided monoidal category** (`ℏ` transcendental). -/
instance : BraidedCategory (DH Ψ c) where
  braiding X Y :=
    { hom := ⟨βmat c X Y, equivariant_βmat c X Y⟩
      inv := ⟨βinv c X Y, equivariant_βinv c X Y⟩
      hom_inv_id := hom_ext (βinv_mul_βmat c X Y)
      inv_hom_id := hom_ext (βmat_mul_βinv c X Y) }
  braiding_naturality_right X Y Z f := hom_ext (βmat_natural c (𝟙 (X : Obj)) f)
  braiding_naturality_left f Z := hom_ext (βmat_natural c f (𝟙 (Z : Obj)))
  hexagon_forward X Y Z := hom_ext (by
    show αmat Ψ hc.out Y Z X * βmat c X (Obj.tensor Y Z) * αmat Ψ hc.out X Y Z =
      kron (1 : EndL (Obj.Leaves Y)) (βmat c X Z) * αmat Ψ hc.out Y X Z *
        kron (βmat c X Y) (1 : EndL (Obj.Leaves Z))
    rw [Matrix.mul_assoc, Matrix.mul_assoc]
    exact hexagon_fwd_mat X Y Z Ψ hc.out)
  hexagon_reverse X Y Z := hom_ext (by
    show αinv Ψ hc.out Z X Y * βmat c (Obj.tensor X Y) Z * αinv Ψ hc.out X Y Z =
      kron (βmat c X Z) (1 : EndL (Obj.Leaves Y)) * αinv Ψ hc.out X Z Y *
        kron (1 : EndL (Obj.Leaves X)) (βmat c Y Z)
    rw [Matrix.mul_assoc, Matrix.mul_assoc]
    exact hexagon_rev_mat X Y Z Ψ hc.out)

end QOU.KZ.Drinfeld

