import Mathlib.CategoryTheory.Sites.SheafHom
import Mathlib.CategoryTheory.Sites.Subsheaf

/-!
# Stacks and gerbes, design D3: first milestone (descent of morphisms for `A`-presheaves)

Mathlib (rev `f897ebc`) has no stacks, gerbes or descent data. This file is the first
genuine step of design D3 (bean `qou-t1dx`, parent `qou-533l`): the **descent of
morphisms** (prestack) condition for the fibred category of presheaves carrying an
action of a presheaf of operators `A`. For `A = G ⋙ forget GrpCat` this category
contains the stack `Tors(G)` of `G`-torsors (Yekutieli, arXiv:0801.0083, §1–2) as the
full subcategory of locally trivial objects.

The statement proved (`isSheaf_equivariantHom`): if `Q` is a sheaf, then for every
presheaf `P`, the presheaf on `C` sending `X` to the set of `A`-equivariant morphisms
`P|_{C/X} ⟶ Q|_{C/X}` is a sheaf. For `Q` a torsor this is the prestack axiom for
`Tors(G)` stated for morphisms. Every morphism of `G`-torsors is an isomorphism, so on
torsors the iso presheaf agrees with this one; that identification is NOT proved here.

What this file does NOT do: it does not define a pseudofunctor-valued stack, does not
prove effective descent of objects, and defines no gerbe. See
`docs/audits/2026-10-12-t3-d3-stacks.md` for the design and the cost estimate.
-/

universe w v u

namespace QOU.MathlibExt.StackGerbe

open CategoryTheory Opposite

variable {C : Type u} [Category.{v} C]

/-- An action of a presheaf of operators `A` on a presheaf `P`, natural in the base.
For a presheaf of groups `G` take `A = G ⋙ forget GrpCat`. The group axioms are not
needed for the descent-of-morphisms statement below, so they are not imposed here. -/
structure PresheafAction (A P : Cᵒᵖ ⥤ Type w) where
  /-- The action on sections over `U`. -/
  smul : ∀ U : Cᵒᵖ, A.obj U → P.obj U → P.obj U
  /-- Restriction commutes with the action. -/
  map_smul : ∀ {U V : Cᵒᵖ} (f : U ⟶ V) (a : A.obj U) (p : P.obj U),
    P.map f (smul U a p) = smul V (A.map f a) (P.map f p)

variable {A P Q : Cᵒᵖ ⥤ Type w}

/-- The subpresheaf of `presheafHom P Q` of `A`-equivariant morphisms over `C/X`. -/
def equivariantHom (αP : PresheafAction A P) (αQ : PresheafAction A Q) :
    Subpresheaf (presheafHom P Q) where
  obj X := {φ | ∀ (Y : (Over X.unop)ᵒᵖ) (a : A.obj (op Y.unop.left))
      (p : P.obj (op Y.unop.left)),
      φ.app Y (αP.smul _ a p) = αQ.smul _ a (φ.app Y p)}
  map f _ hφ := fun Y a p => hφ (op ((Over.map f.unop).obj Y.unop)) a p

/-- **Descent of morphisms for `A`-presheaves.** If `Q` is a sheaf, the presheaf of
`A`-equivariant morphisms `P|_{C/X} ⟶ Q|_{C/X}` is a sheaf, for every presheaf `P`. -/
theorem isSheaf_equivariantHom (J : GrothendieckTopology C)
    (αP : PresheafAction A P) (αQ : PresheafAction A Q) (hQ : Presheaf.IsSheaf J Q) :
    Presieve.IsSheaf J (equivariantHom αP αQ).toPresheaf := by
  have hQ' : Presieve.IsSheaf J Q := (isSheaf_iff_isSheaf_of_type J Q).mp hQ
  have hH : Presieve.IsSheaf J (presheafHom P Q) :=
    (isSheaf_iff_isSheaf_of_type J _).mp (Presheaf.IsSheaf.hom P Q hQ)
  rw [Subpresheaf.isSheaf_iff _ hH]
  intro X φ hφ Y a p
  obtain ⟨Y⟩ := Y
  have hcov := J.pullback_stable Y.hom hφ
  refine (hQ' _ hcov).isSeparatedFor.ext ?_
  intro Z k hk
  have heq := hk (op (Over.mk (𝟙 Z))) (A.map k.op a) (P.map k.op p)
  rw [presheafHom_map_app_op_mk_id] at heq
  have nat := fun (x : P.obj (op Y.left)) =>
    congr_fun (φ.naturality (Over.homMk k : Over.mk (k ≫ Y.hom) ⟶ Y).op) x
  simp only [types_comp_apply] at nat
  calc Q.map k.op (φ.app (op Y) (αP.smul _ a p))
      = φ.app (op (Over.mk (k ≫ Y.hom))) (P.map k.op (αP.smul _ a p)) := (nat _).symm
    _ = φ.app (op (Over.mk (k ≫ Y.hom))) (αP.smul _ (A.map k.op a) (P.map k.op p)) := by
        rw [αP.map_smul]; rfl
    _ = αQ.smul _ (A.map k.op a) (φ.app (op (Over.mk (k ≫ Y.hom))) (P.map k.op p)) := heq
    _ = αQ.smul _ (A.map k.op a) (Q.map k.op (φ.app (op Y) p)) :=
        congrArg (αQ.smul _ (A.map k.op a)) (nat p)
    _ = Q.map k.op (αQ.smul _ a (φ.app (op Y) p)) := (αQ.map_smul _ _ _).symm

end QOU.MathlibExt.StackGerbe
