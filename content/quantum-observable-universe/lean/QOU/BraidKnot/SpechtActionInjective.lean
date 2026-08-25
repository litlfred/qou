import QOU.BraidKnot.SpechtRegularMultiplicity
import QOU.MathlibExt.OfModuleAsModule
import QOU.BraidKnot.MaschkeSnSemisimple
import Mathlib.RingTheory.SimpleModule.Basic

/-!
# QOU.BraidKnot.SpechtActionInjective — the Specht action map is injective

Brick 4c of **W1+W3** of the Wedderburn epic (`qou-bxw4`), after #5139 (W2), #5151 (Schur
orthonormality), #5156 (`Hom_G(k[G], V) ≃ V`), #5162 (both sides of the dimension count),
#5167 (per-partition multiplicity) and #5174 (the `ofModule`/`asModule` round-trip).

The product of the Specht actions

  `Φ : k[S_n] →ₐ[k] ∏_{μ ⊢ n} End_k(S^μ)`

is **injective**. With the target's dimension from `SpechtBlockDimension` this gives

  `n! ≤ Σ_μ (dim_k S^μ)²`.

## Honest scope

**One inequality, not the RSK identity.** `n! = Σ_μ (dim S^μ)²` additionally needs
`Σ_μ (dim S^μ)² ≤ n!`, i.e. that the blocks do not overlap — the isotypic independence of the
multiplicity spaces that bricks 1–4b count. That is not proved here, and
`sn_isotypic_specht_split` remains open, as do the two keystones that inherit `sorryAx` from it.

## The argument

An `x` in the kernel acts as zero on every Specht module, hence — via
`SpechtClassification.specht_exhausts_irreducibles`, which says the Specht modules exhaust the
simples — as zero on *every* simple `k[S_n]`-module. `k[S_n]` is semisimple (Maschke), so as a
module over itself it is the supremum of its simple submodules; an element of a supremum of
submodules is a finite sum of elements of them, so `x` acts as zero on all of `k[S_n]`. Then
`x = x • 1 = 0`.

Two general lemmas carry the weight and are stated for an arbitrary ring / group:
`eq_zero_of_smul_simples_eq_zero` (the semisimple sweep) and `asAlgebraHom_of_intertwiner`
(transport of the *algebra* action along a rep-iso, which the intertwining hypothesis gives
only on group elements).

## Base ring (§7c)

`variable {k : Type} [Field k] [CharZero k]` for the Specht layer; the two general lemmas are
over `[Ring R]` / `[Field k] [Monoid G]` respectively. No `ℝ`.
-/

namespace QOU.BraidKnot.SpechtActionInjective

open QOU.BraidKnot
open QOU.BraidKnot.Specht
open QOU.BraidKnot.SpechtClassification
open QOU.MathlibExt.OfModuleAsModule
open Equiv (Perm)
open Module

/-! ## 1. Two general lemmas -/

/-- **The semisimple sweep.** In a semisimple module, an element of the ring that kills every
simple submodule kills everything.

The supremum of a family of submodules consists of finite sums of their elements
(`Submodule.iSup_induction` — note it has no `smul` case, which is what makes this work:
`y ↦ x • y = 0` is closed under addition but *not* under multiplication by the ring on the
right, since the ring need not be commutative). -/
theorem eq_zero_of_smul_simples_eq_zero {R M : Type*} [Ring R] [AddCommGroup M] [Module R M]
    [IsSemisimpleModule R M] (x : R)
    (h : ∀ N : Submodule R M, IsSimpleModule R N → ∀ y ∈ N, x • y = 0) :
    ∀ y : M, x • y = 0 := by
  intro y
  have hy : y ∈ (⊤ : Submodule R M) := Submodule.mem_top
  rw [← IsSemisimpleModule.sSup_simples_eq_top R M, sSup_eq_iSup'] at hy
  refine Submodule.iSup_induction (motive := fun z => x • z = 0) _ hy
    (fun N z hz => h (N : Submodule R M) N.2 z hz) (smul_zero x) ?_
  intro a b ha hb
  rw [smul_add, ha, hb, add_zero]

/-- **Transport of the algebra action along a rep-iso.** A `k`-linear equivalence intertwining
two representations intertwines the induced `MonoidAlgebra` actions.

The hypothesis is stated on group elements; extending it to a general `x : k[G]` is a
`Finsupp` induction, using `Representation.asAlgebraHom_single`. -/
theorem asAlgebraHom_of_intertwiner {k G V W : Type*} [CommSemiring k] [Monoid G]
    [AddCommMonoid V] [Module k V] [AddCommMonoid W] [Module k W]
    (ρV : Representation k G V) (ρW : Representation k G W) (e : V ≃ₗ[k] W)
    (he : ∀ (g : G) (v : V), e (ρV g v) = ρW g (e v)) (x : MonoidAlgebra k G) (v : V) :
    e (ρV.asAlgebraHom x v) = ρW.asAlgebraHom x (e v) := by
  induction x using Finsupp.induction_linear with
  | zero => simp
  | add a b ha hb =>
      rw [map_add, map_add, LinearMap.add_apply, LinearMap.add_apply, map_add, ha, hb]
  | single g r =>
      rw [Representation.asAlgebraHom_single, Representation.asAlgebraHom_single,
        LinearMap.smul_apply, LinearMap.smul_apply, map_smul, he]

/-! ## 2. The Specht action map -/

variable {k : Type} [Field k] [CharZero k]

/-- The product of the Specht actions, `Φ : k[S_n] →ₐ[k] ∏_{μ ⊢ n} End_k(S^μ)`. -/
noncomputable def spechtProduct (n : ℕ) :
    MonoidAlgebra k (Perm (Fin n)) →ₐ[k]
      (∀ i : PartitionIndex n, Module.End k (SpechtSubmodule (k := k) i.diagram)) :=
  Pi.algHom k _ (fun i => (spechtRepAt (k := k) i.property).asAlgebraHom)

omit [CharZero k] in
@[simp] theorem spechtProduct_apply (n : ℕ) (x : MonoidAlgebra k (Perm (Fin n)))
    (i : PartitionIndex n) :
    spechtProduct (k := k) n x i = (spechtRepAt (k := k) i.property).asAlgebraHom x := rfl

/-- **The Specht action map is injective.**

An `x` in the kernel kills every Specht module; the classification
(`specht_exhausts_irreducibles`) makes every simple `k[S_n]`-module a Specht module, so `x`
kills every simple; semisimplicity (Maschke) then makes it kill `k[S_n]` itself, and
`x = x • 1 = 0`.

`-- Ref: [sagan2001] §1.10; [james1984representation]`. -/
theorem spechtProduct_injective (n : ℕ) :
    Function.Injective (spechtProduct (k := k) n) := by
  classical
  rw [injective_iff_map_eq_zero]
  intro x hx
  haveI : IsSemisimpleRing (MonoidAlgebra k (Perm (Fin n))) :=
    MaschkeSnSemisimple.sn_isSemisimpleRing n
  -- `x` kills every simple submodule of the regular module.
  have hsimple : ∀ N : Submodule (MonoidAlgebra k (Perm (Fin n)))
      (MonoidAlgebra k (Perm (Fin n))),
      IsSimpleModule (MonoidAlgebra k (Perm (Fin n))) N → ∀ y ∈ N, x • y = 0 := by
    intro N hN y hy
    haveI := hN
    -- view `N` as a representation and identify it with a Specht module
    obtain ⟨μ, hμ, hiso⟩ :=
      specht_exhausts_irreducibles (k := k) (Representation.ofModule (k := k) (G := Perm (Fin n)) N)
        inferInstance
    obtain ⟨e, he⟩ := hiso.exists_intertwiner
    -- the Specht component of `x` is zero, so `x` acts as zero on `N`'s representation
    have hzero : (spechtRepAt (k := k) hμ).asAlgebraHom x = 0 := by
      have := congrFun hx ⟨μ, hμ⟩
      simpa using this
    have hact : ∀ m, (Representation.ofModule (k := k) (G := Perm (Fin n)) N).asAlgebraHom x m
        = 0 := by
      intro m
      refine e.injective ?_
      rw [asAlgebraHom_of_intertwiner _ _ e he]
      -- `spechtRepAt hμ` is by definition the composite `he` mentions; `show` bridges the two.
      show (spechtRepAt (k := k) hμ).asAlgebraHom x (e m) = e 0
      simp [hzero]
    -- unwind `ofModule`'s action back to the module action on `N`
    have hy' := hact ((RestrictScalars.addEquiv k (MonoidAlgebra k (Perm (Fin n)))
      (N : Type _)).symm ⟨y, hy⟩)
    rw [Representation.ofModule_asAlgebraHom_apply_apply] at hy'
    have := congrArg (RestrictScalars.addEquiv k (MonoidAlgebra k (Perm (Fin n))) (N : Type _)) hy'
    simp only [AddEquiv.apply_symm_apply, map_zero] at this
    exact congrArg Subtype.val this
  -- hence `x` kills the whole regular module, in particular `1`.
  have := eq_zero_of_smul_simples_eq_zero x hsimple 1
  simpa using this

/-! ## 3. The inequality -/

/-- **`n! ≤ Σ_{μ ⊢ n} (dim_k S^μ)²`.**

Injectivity of the Specht action map, read through the two dimension computations of
`SpechtBlockDimension`.

**This is one inequality, not the RSK identity.** The reverse `Σ_μ (dim S^μ)² ≤ n!` needs the
blocks not to overlap — the isotypic independence of the multiplicity spaces — and is not
proved here. -/
theorem factorial_le_sum_sq (n : ℕ) :
    Nat.factorial n
      ≤ ∑ i : PartitionIndex n, (finrank k (SpechtSubmodule (k := k) i.diagram)) ^ 2 := by
  have hsrc := SpechtBlockDimension.finrank_group_algebra (k := k) n
  have htgt := SpechtBlockDimension.finrank_specht_blocks (k := k) n
  have hle := (spechtProduct (k := k) n).toLinearMap.finrank_le_finrank_of_injective
    (spechtProduct_injective (k := k) n)
  rw [hsrc, htgt] at hle
  exact hle

end QOU.BraidKnot.SpechtActionInjective
