import QOU.MathlibExt.RepresentationCharacter
import Mathlib.RepresentationTheory.Basic
import Mathlib.LinearAlgebra.Finsupp.LinearCombination

/-!
# QOU.MathlibExt.RegularHom — `Hom_G(k[G], V) ≃ V`

Third brick of **W1+W3** of the Wedderburn epic (`qou-bxw4`).

An equivariant map out of the regular representation is determined by where it sends the
identity basis vector, and every target vector occurs. So

  `Hom_G(k[G], V) ≃ₗ[k] V`,  hence  `dim_k Hom_G(k[G], V) = dim_k V`.

Combined with the Schur orthonormality of `SpechtSchurDiagonal` this is what reads the
multiplicity of `S^μ` in the regular representation off as `dim_k S^μ` — the step that turns
`dim_k k[S_n] = n!` into `n! = Σ_μ (dim S^μ)²`. The point of doing it *this* way rather than
by expanding characters is that it needs no completeness / spanning statement for the
characters, which the corpus has only as an upper bound.

This file is deliberately general: any group, any base field, any representation. Nothing
about `S_n` or Specht modules enters.

## Base ring (§7c)

Generic `{k : Type*} [Field k]`. No `ℝ`, no ordering. `Field` rather than `CommRing` only
because `homG` is stated over a field in `RepresentationCharacter`.
-/

namespace QOU.MathlibExt.RegularHom

open QOU.MathlibExt.RepresentationCharacter
open Representation Module

variable {k G V : Type*} [Field k] [Group G] [AddCommGroup V] [Module k V]

/-- The regular representation of `G` on `G →₀ k`, i.e. `Representation.ofMulAction`
applied to `G` acting on itself. -/
noncomputable abbrev regular (k G : Type*) [CommSemiring k] [Monoid G] :
    Representation k G (G →₀ k) :=
  ofMulAction k G G

/-- `ρ_reg g` sends the basis vector at `h` to the basis vector at `g * h`. -/
@[simp] theorem regular_single (g h : G) (c : k) :
    regular k G g (Finsupp.single h c) = Finsupp.single (g * h) c := by
  classical
  simp [ofMulAction_single]

/-- Evaluation of an equivariant map at the identity basis vector. -/
noncomputable def evalOne (ρ : Representation k G V) :
    homG (regular k G) ρ →ₗ[k] V where
  toFun f := (f : (G →₀ k) →ₗ[k] V) (Finsupp.single 1 1)
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

/-- The inverse construction: a vector `v` determines the equivariant map
`Σ_g c_g·[g] ↦ Σ_g c_g·(ρ g v)`. -/
noncomputable def ofVector (ρ : Representation k G V) (v : V) :
    (G →₀ k) →ₗ[k] V :=
  Finsupp.lsum k (fun g => LinearMap.toSpanSingleton k V (ρ g v))

@[simp] theorem ofVector_single (ρ : Representation k G V) (v : V) (g : G) (c : k) :
    ofVector ρ v (Finsupp.single g c) = c • ρ g v := by
  simp [ofVector, LinearMap.toSpanSingleton_apply]

theorem ofVector_mem (ρ : Representation k G V) (v : V) :
    ofVector ρ v ∈ homG (regular k G) ρ := by
  classical
  refine mem_homG_iff.mpr (fun g x => ?_)
  -- both sides are linear in `x`; check on the `Finsupp` basis.
  induction x using Finsupp.induction_linear with
  | zero => simp
  | add a b ha hb => simp [ha, hb]
  | single h c =>
      rw [regular_single, ofVector_single, ofVector_single, map_smul, ← Module.End.mul_apply,
        ← map_mul]

/-- **An equivariant map out of the regular representation is its value at `[1]`.**
`Hom_G(k[G], V) ≃ₗ[k] V`. -/
noncomputable def homGRegularEquiv (ρ : Representation k G V) :
    homG (regular k G) ρ ≃ₗ[k] V := by
  classical
  refine LinearEquiv.ofLinear (evalOne ρ)
    { toFun := fun v => ⟨ofVector ρ v, ofVector_mem ρ v⟩
      map_add' := fun v w => by
        refine Subtype.ext (Finsupp.lhom_ext' (fun g => LinearMap.ext_ring ?_))
        simp [ofVector_single, smul_add]
      map_smul' := fun c v => by
        refine Subtype.ext (Finsupp.lhom_ext' (fun g => LinearMap.ext_ring ?_))
        simp [ofVector_single, smul_comm] }
    ?_ ?_
  · -- `evalOne ∘ ofVector = id`
    refine LinearMap.ext (fun v => ?_)
    show ofVector ρ v (Finsupp.single 1 1) = v
    simp
  · -- `ofVector ∘ evalOne = id`: an equivariant `f` is determined on the basis by `f [1]`.
    refine LinearMap.ext (fun f => Subtype.ext ?_)
    refine Finsupp.lhom_ext' (fun g => LinearMap.ext_ring ?_)
    show ofVector ρ ((f : (G →₀ k) →ₗ[k] V) (Finsupp.single 1 1)) (Finsupp.single g 1)
      = (f : (G →₀ k) →ₗ[k] V) (Finsupp.single g 1)
    rw [ofVector_single, one_smul]
    have hbasis : (Finsupp.single g (1 : k)) = regular k G g (Finsupp.single 1 1) := by
      rw [regular_single, mul_one]
    rw [hbasis, mem_homG_iff.mp f.2 g (Finsupp.single 1 1)]

/-- **`dim_k Hom_G(k[G], V) = dim_k V`.**

This is the multiplicity statement in the form the Wedderburn count needs: paired with the
Schur orthonormality of `SpechtSchurDiagonal`, `dim Hom_G(k[G], S^μ)` is on one side the
multiplicity of `S^μ` in the regular representation, and on the other `dim S^μ`.

`-- Ref: [sagan2001] §1.10 (the regular representation contains each irreducible with
multiplicity equal to its dimension).` -/
theorem finrank_homG_regular (ρ : Representation k G V) :
    finrank k (homG (regular k G) ρ) = finrank k V :=
  (homGRegularEquiv ρ).finrank_eq

end QOU.MathlibExt.RegularHom
