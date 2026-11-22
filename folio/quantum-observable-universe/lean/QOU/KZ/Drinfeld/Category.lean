import QOU.KZ.Drinfeld.Kron
import Mathlib.CategoryTheory.Category.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Data.Complex.Basic

/-!
# The underlying category of `D_ℏ`: `sl₂`-equivariant maps between tensor powers of `ℂ²`

Stage S2 of bean `qou-zoyv`. The objects are parenthesised tensor words in `V = ℂ²` (`Obj`), with
leg set `Leaves X`. The tensor power `V^{⊗X}` has basis `Leaves X → Fin 2`. A morphism `X ⟶ Y` is
a matrix `V^{⊗X} → V^{⊗Y}` commuting with the diagonal action `ρ` of every traceless `a`.
`ρ` is defined recursively by `ρ_{X⊗Y}(a) = ρ_X(a) ⊗ 1 + 1 ⊗ ρ_Y(a)`. Composition is matrix
multiplication.

Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S2)
-/

noncomputable section

namespace QOU.KZ.Drinfeld

open CategoryTheory

/-- Parenthesised tensor words in `V`. -/
inductive Obj : Type
  | unit : Obj
  | V : Obj
  | tensor : Obj → Obj → Obj

namespace Obj

/-- The tensor legs of a word. -/
@[reducible] def Leaves : Obj → Type
  | unit => Empty
  | V => Unit
  | tensor X Y => Leaves X ⊕ Leaves Y

/-- `Fintype` structure on the legs. -/
@[reducible] def leavesFintype : (X : Obj) → Fintype (Leaves X)
  | unit => inferInstanceAs (Fintype Empty)
  | V => inferInstanceAs (Fintype Unit)
  | tensor X Y => @instFintypeSum _ _ (leavesFintype X) (leavesFintype Y)

/-- Decidable equality on the legs. -/
@[reducible] def leavesDecEq : (X : Obj) → DecidableEq (Leaves X)
  | unit => inferInstanceAs (DecidableEq Empty)
  | V => inferInstanceAs (DecidableEq Unit)
  | tensor X Y => @instDecidableEqSum _ _ (leavesDecEq X) (leavesDecEq Y)

instance (X : Obj) : Fintype (Leaves X) := leavesFintype X
instance (X : Obj) : DecidableEq (Leaves X) := leavesDecEq X

instance : IsEmpty (Leaves unit) := inferInstanceAs (IsEmpty Empty)
instance : Unique (Leaves V) := inferInstanceAs (Unique Unit)

/-- Basis indices of `V^{⊗X}`. -/
abbrev Idx (X : Obj) := Leaves X → Fin 2

/-- The diagonal action of `a ∈ 𝔤𝔩₂` on `V^{⊗X}`. -/
def ρ : (X : Obj) → Matrix (Fin 2) (Fin 2) ℂ → Matrix (Idx X) (Idx X) ℂ
  | unit, _ => 0
  | V, a => Matrix.of fun y x => a (y ()) (x ())
  | tensor X Y, a => kron (ρ X a) 1 + kron 1 (ρ Y a)

theorem ρ_tensor (X Y : Obj) (a : Matrix (Fin 2) (Fin 2) ℂ) :
    ρ (tensor X Y) a = kron (ρ X a) 1 + kron 1 (ρ Y a) := rfl

end Obj

open Obj

/-- `f` intertwines the diagonal `sl₂`-actions. -/
def Equivariant {X Y : Obj} (f : Matrix (Idx Y) (Idx X) ℂ) : Prop :=
  ∀ a : Matrix (Fin 2) (Fin 2) ℂ, a.trace = 0 → ρ Y a * f = f * ρ X a

/-- Morphisms of the underlying category of `D_ℏ`. -/
def Hom (X Y : Obj) : Type := { f : Matrix (Idx Y) (Idx X) ℂ // Equivariant f }

instance : Category Obj where
  Hom := Hom
  id X := ⟨1, fun a _ => by rw [Matrix.mul_one, Matrix.one_mul]⟩
  comp f g := ⟨g.1 * f.1, fun a ha => by
    rw [← Matrix.mul_assoc, g.2 a ha, Matrix.mul_assoc, f.2 a ha, Matrix.mul_assoc]⟩
  id_comp f := Subtype.ext (Matrix.mul_one _)
  comp_id f := Subtype.ext (Matrix.one_mul _)
  assoc f g h := Subtype.ext (Matrix.mul_assoc _ _ _).symm

@[ext]
theorem hom_ext {X Y : Obj} {f g : X ⟶ Y} (h : f.1 = g.1) : f = g := Subtype.ext h

theorem comp_val {X Y Z : Obj} (f : X ⟶ Y) (g : Y ⟶ Z) : (f ≫ g).1 = g.1 * f.1 := rfl
theorem id_val (X : Obj) : (𝟙 X : X ⟶ X).1 = 1 := rfl

/-- The tensor product of equivariant maps is equivariant. -/
theorem equivariant_kron {X X' Y Y' : Obj} {f : Matrix (Idx Y) (Idx X) ℂ}
    {g : Matrix (Idx Y') (Idx X') ℂ} (hf : Equivariant f) (hg : Equivariant g) :
    Equivariant (Y := tensor Y Y') (X := tensor X X') (kron f g) := by
  intro a ha
  rw [ρ_tensor, ρ_tensor, Matrix.add_mul, Matrix.mul_add, kron_mul, kron_mul, kron_mul, kron_mul,
    hf a ha, hg a ha, Matrix.one_mul, Matrix.mul_one, Matrix.one_mul, Matrix.mul_one]

end QOU.KZ.Drinfeld
