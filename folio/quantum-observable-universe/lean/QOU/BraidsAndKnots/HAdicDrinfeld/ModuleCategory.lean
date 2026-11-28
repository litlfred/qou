import QOU.BraidsAndKnots.HAdicDrinfeld.CasimirData
import Mathlib.RingTheory.TensorProduct.Basic
import Mathlib.CategoryTheory.Category.Basic

/-!
# Modules over a Casimir datum: the category and the tensor product

Epic `qou-dk7p`, step B of `docs/audits/2026-11-27-kz-trio-strangler-plan.md`.

The h-adic Drinfeld category is the category of `A`-modules, with the tensor product given
by the coproduct `Δ` of a `CasimirData`, the associator `Φ = φ(c t₁₂, c t₂₃)` and the
braiding `σ ∘ R`. This file builds the first layer, which uses neither `Φ` nor `R`:

* `Rep D`: a `k`-module `V` with an algebra map `ρ : A →ₐ[k] End k V`;
* the category `Rep D`, whose morphisms are the `k`-linear maps that commute with `ρ`;
* `Rep.tensorObj`: `V ⊗[k] W` with `a ↦ (ρ_V ⊗ ρ_W)(Δ a)`, through Mathlib's
  `Module.endTensorEndAlgHom`;
* `Rep.tensorHom`: `f ⊗ g` is again a morphism, and the assignment is functorial.

The associator, the unit and the braiding come in later files. Everything is over an
arbitrary commutative ring `k` and an arbitrary `k`-algebra `A`. No analysis is used.
-/

namespace QOU.BraidsAndKnots.HAdicDrinfeld

open scoped TensorProduct
open CategoryTheory

universe u w

variable {k : Type u} {A : Type w} [CommRing k] [Ring A] [Algebra k A]

/-- A module over the Casimir datum `D`: a `k`-module with an action of `A`. -/
structure Rep.{v} (_D : CasimirData k A) where
  /-- The underlying type. -/
  V : Type v
  [isAddCommGroup : AddCommGroup V]
  [isModule : Module k V]
  /-- The action. -/
  ρ : A →ₐ[k] Module.End k V

attribute [instance] Rep.isAddCommGroup Rep.isModule

universe v

namespace Rep

variable {D : CasimirData k A}

/-- A morphism of representations: a `k`-linear map that commutes with the action. -/
@[ext]
structure Hom (X Y : Rep.{u, w, v} D) where
  /-- The underlying linear map. -/
  f : X.V →ₗ[k] Y.V
  comm : ∀ a, f ∘ₗ X.ρ a = Y.ρ a ∘ₗ f

instance : Category (Rep.{u, w, v} D) where
  Hom := Hom
  id X := ⟨LinearMap.id, fun a => by simp⟩
  comp φ ψ := ⟨ψ.f ∘ₗ φ.f, fun a => by
    rw [LinearMap.comp_assoc, φ.comm, ← LinearMap.comp_assoc, ψ.comm, LinearMap.comp_assoc]⟩

@[ext]
theorem hom_ext {X Y : Rep.{u, w, v} D} {φ ψ : X ⟶ Y} (h : φ.f = ψ.f) : φ = ψ := Hom.ext h

@[simp] theorem id_f (X : Rep.{u, w, v} D) : (𝟙 X : X ⟶ X).f = LinearMap.id := rfl

@[simp] theorem comp_f {X Y Z : Rep.{u, w, v} D} (φ : X ⟶ Y) (ψ : Y ⟶ Z) :
    (φ ≫ ψ).f = ψ.f ∘ₗ φ.f := rfl

/-! ### The tensor product -/

/-- The action of `A ⊗ A` on `V ⊗ W`. -/
noncomputable def pairAction (X Y : Rep.{u, w, v} D) :
    A ⊗[k] A →ₐ[k] Module.End k (X.V ⊗[k] Y.V) :=
  (Module.endTensorEndAlgHom (R := k) (S := k) (A := k)).comp
    (Algebra.TensorProduct.map X.ρ Y.ρ)

theorem pairAction_tmul (X Y : Rep.{u, w, v} D) (a b : A) :
    pairAction X Y (a ⊗ₜ b) = TensorProduct.map (X.ρ a) (Y.ρ b) := rfl

/-- The tensor product of two representations: `a` acts on `V ⊗ W` by `(ρ_V ⊗ ρ_W)(Δ a)`. -/
noncomputable def tensorObj (X Y : Rep.{u, w, v} D) : Rep.{u, w, v} D where
  V := X.V ⊗[k] Y.V
  ρ := (pairAction X Y).comp D.Δ

theorem tensorObj_ρ (X Y : Rep.{u, w, v} D) (a : A) :
    (tensorObj X Y).ρ a = pairAction X Y (D.Δ a) := rfl

/-- `f ⊗ g` commutes with the action of every element of `A ⊗ A`. -/
theorem map_comm_pairAction {X X' Y Y' : Rep.{u, w, v} D} (φ : X ⟶ X') (ψ : Y ⟶ Y')
    (x : A ⊗[k] A) :
    TensorProduct.map φ.f ψ.f ∘ₗ pairAction X Y x =
      pairAction X' Y' x ∘ₗ TensorProduct.map φ.f ψ.f := by
  induction x using TensorProduct.induction_on with
  | zero => simp
  | tmul a b =>
    rw [pairAction_tmul, pairAction_tmul, ← TensorProduct.map_comp, ← TensorProduct.map_comp,
      φ.comm, ψ.comm]
  | add x y hx hy => rw [map_add, map_add, LinearMap.comp_add, LinearMap.add_comp, hx, hy]

/-- The tensor product of two morphisms. -/
noncomputable def tensorHom {X X' Y Y' : Rep.{u, w, v} D} (φ : X ⟶ X') (ψ : Y ⟶ Y') :
    tensorObj X Y ⟶ tensorObj X' Y' :=
  ⟨TensorProduct.map φ.f ψ.f, fun a => map_comm_pairAction φ ψ (D.Δ a)⟩

@[simp] theorem tensorHom_f {X X' Y Y' : Rep.{u, w, v} D} (φ : X ⟶ X') (ψ : Y ⟶ Y') :
    (tensorHom φ ψ).f = TensorProduct.map φ.f ψ.f := rfl

theorem tensorHom_id (X Y : Rep.{u, w, v} D) :
    tensorHom (𝟙 X) (𝟙 Y) = 𝟙 (tensorObj X Y) := by
  ext1; simp [TensorProduct.map_id]

theorem tensorHom_comp {X₁ X₂ X₃ Y₁ Y₂ Y₃ : Rep.{u, w, v} D} (φ₁ : X₁ ⟶ X₂) (φ₂ : X₂ ⟶ X₃)
    (ψ₁ : Y₁ ⟶ Y₂) (ψ₂ : Y₂ ⟶ Y₃) :
    tensorHom (φ₁ ≫ φ₂) (ψ₁ ≫ ψ₂) = tensorHom φ₁ ψ₁ ≫ tensorHom φ₂ ψ₂ := by
  ext1; simp [TensorProduct.map_comp]

end Rep

end QOU.BraidsAndKnots.HAdicDrinfeld
