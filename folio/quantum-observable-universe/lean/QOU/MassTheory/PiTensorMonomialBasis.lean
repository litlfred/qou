import Mathlib.Tactic
import Mathlib.LinearAlgebra.PiTensorProduct

/-!
# The monomial basis of a tensor power, and the factor permutation on it

Bean `qou-uinl`, stage 2. Supplies the piece `TensorTraceCharacter` records as
missing, and it is missing from **Mathlib**, not merely from this repo.

## What Mathlib lacks, measured

`Mathlib/LinearAlgebra/PiTensorProduct.lean` contains **zero occurrences of `Basis`**
(checked 2026-09-05), and there is no `finrank` lemma for `⨂[R] i : ι, M` either.
Mathlib has the *action* — `PiTensorProduct.reindex` — but nothing that lets you
compute in coordinates, which is why `TensorTraceCharacter` had to work in the
concrete model `((α → κ) → R)` instead of over `⨂`.

This file closes that, in the case the character computation needs: for `V = κ → R`
free with basis indexed by `κ`,

    monoEquiv : (⨂[R] _ : α, (κ → R)) ≃ₗ[R] ((α → κ) → R)

the **monomial basis** — a pure tensor `⨂ᵢ vᵢ` goes to `f ↦ ∏ᵢ vᵢ (f i)`, and the
inverse sends `g` to `∑_f g f • ⨂ᵢ single (f i) 1`. The forward round trip is a
Kronecker-delta computation; the backward one is the monomial *expansion*
`vᵢ = ∑ₖ vᵢ k • single k 1` pushed through `MultilinearMap.map_sum` and
`map_smul_univ`.

## The correspondence

`monoEquiv_tensorPerm` is the payoff: under this basis, permuting the tensor
**factors** (`PiTensorProduct.reindex`) is precomposition on index tuples,

    monoEquiv (tensorPerm σ x) g = monoEquiv x (g ∘ σ)

which is exactly the `indexPerm` of `TensorTraceCharacter`. So the `q = 1` character
`(card κ)^{c(σ)}` proved there in the concrete model is a statement about the genuine
tensor power, transported along `monoEquiv`.

**DONE, same day:** `QOU.MassTheory.TensorPowerTrace` supplies exactly that — the
`Module.Free`/`Module.Finite` instances transported along `monoEquiv`, and
`trace_tensorPerm : LinearMap.trace R (⨂[R] _ : α, (κ → R)) (tensorPerm σ) =
(card κ) ^ orbitCount σ`. So the character is now stated with `LinearMap.trace` over
the tensor power itself.

🛑 **What is still not here**, and is a different order of problem: quantum
Schur–Weyl at `q ≠ 1`. Bean `qou-mpq5` scoped that as a multi-week gap and refused to
fake it; nothing in this arc bears on it.

-- Ref: [leitner2026] bean qou-uinl; the monomial basis of a tensor power is classical.
-/

open scoped TensorProduct
open Finset

namespace QOU.MassTheory

variable {R : Type*} [CommSemiring R]
variable {α : Type*} [Fintype α] [DecidableEq α]
variable {κ : Type*} [Fintype κ] [DecidableEq κ]

omit [Fintype κ] [DecidableEq κ] in
/-- Splitting the monomial product at the updated slot. The product body is
`update v i b j (f j)` — the update *applied* — so `Finset.prod_update_of_mem` cannot
match it; `Finset.mul_prod_erase` peels slot `i` off by hand instead. -/
private theorem prod_update_expand (v : α → (κ → R)) (i : α) (f : α → κ) (b : κ → R) :
    (∏ j, Function.update v i b j (f j))
      = b (f i) * ∏ j ∈ univ.erase i, v j (f j) := by
  rw [← Finset.mul_prod_erase univ (fun j => Function.update v i b j (f j)) (mem_univ i)]
  simp only [Function.update_apply]
  congr 1
  refine Finset.prod_congr rfl fun j hj => ?_
  rw [if_neg (Finset.ne_of_mem_erase hj)]

def monoMultilinear : MultilinearMap R (fun _ : α => (κ → R)) ((α → κ) → R) where
  toFun v := fun f => ∏ i, v i (f i)
  map_update_add' := by
    intro _ v i x y
    funext f
    simp only [prod_update_expand, Pi.add_apply, add_mul]
  map_update_smul' := by
    intro _ v i c x
    funext f
    simp only [prod_update_expand, Pi.smul_apply, smul_eq_mul, mul_assoc]

omit [DecidableEq α] [Fintype κ] [DecidableEq κ] in
@[simp] theorem monoMultilinear_apply (v : α → (κ → R)) (f : α → κ) :
    monoMultilinear (R := R) v f = ∏ i, v i (f i) := rfl

/-- Forward: the tensor power to functions on index tuples. -/
noncomputable def toMono : (⨂[R] _ : α, (κ → R)) →ₗ[R] ((α → κ) → R) :=
  PiTensorProduct.lift monoMultilinear

omit [DecidableEq α] [Fintype κ] [DecidableEq κ] in
@[simp] theorem toMono_tprod (v : α → (κ → R)) :
    toMono (R := R) (κ := κ) (PiTensorProduct.tprod R v) = fun f => ∏ i, v i (f i) :=
  PiTensorProduct.lift.tprod v

/-- Backward, as a linear map: a function on index tuples to the tensor power. -/
noncomputable def ofMono : ((α → κ) → R) →ₗ[R] (⨂[R] _ : α, (κ → R)) where
  toFun g := ∑ f : α → κ, g f • PiTensorProduct.tprod R
    (fun i => (Pi.single (f i) (1 : R) : κ → R))
  map_add' g h := by simp [add_smul, Finset.sum_add_distrib]
  map_smul' c g := by simp [smul_smul, Finset.smul_sum]

theorem ofMono_apply (g : (α → κ) → R) :
    ofMono (R := R) g = ∑ f : α → κ, g f • PiTensorProduct.tprod R
      (fun i => (Pi.single (f i) (1 : R) : κ → R)) := rfl

theorem toMono_ofMono (g : (α → κ) → R) : toMono (R := R) (ofMono g) = g := by
  classical
  funext h
  rw [ofMono_apply, map_sum]
  simp only [map_smul, toMono_tprod, Finset.sum_apply, Pi.smul_apply, smul_eq_mul]
  have key : ∀ f : α → κ,
      (∏ i, (Pi.single (f i) (1 : R) : κ → R) (h i)) = (if f = h then 1 else 0 : R) := by
    intro f
    by_cases hf : f = h
    · subst hf; simp
    · rw [if_neg hf]
      obtain ⟨i, hi⟩ : ∃ i, f i ≠ h i := Function.ne_iff.mp hf
      refine prod_eq_zero (mem_univ i) ?_
      simp [hi]
  simp only [key, mul_ite, mul_one, mul_zero]
  simp

/-- The generator case of the round trip: this is the monomial EXPANSION of a pure
tensor, `v i = ∑ k, v i k • single k 1` pushed through multilinearity. -/
theorem ofMono_toMono_tprod (v : α → (κ → R)) :
    ofMono (R := R) (toMono (PiTensorProduct.tprod R v)) = PiTensorProduct.tprod R v := by
  classical
  have hv : (fun i => ∑ k : κ, v i k • (Pi.single k (1 : R) : κ → R)) = v := by
    funext i
    funext j
    simp [Pi.single_apply]
  rw [toMono_tprod, ofMono_apply]
  calc ∑ f : α → κ, (∏ i, v i (f i)) • PiTensorProduct.tprod R
          (fun i => (Pi.single (f i) (1 : R) : κ → R))
      = ∑ f : α → κ, PiTensorProduct.tprod R
          (fun i => v i (f i) • (Pi.single (f i) (1 : R) : κ → R)) := by
        refine Finset.sum_congr rfl fun f _ => ?_
        rw [MultilinearMap.map_smul_univ]
    _ = PiTensorProduct.tprod R (fun i => ∑ k : κ, v i k • (Pi.single k (1 : R) : κ → R)) :=
        (MultilinearMap.map_sum (PiTensorProduct.tprod R)
          (fun i k => v i k • (Pi.single k (1 : R) : κ → R))).symm
    _ = PiTensorProduct.tprod R v := by rw [hv]

theorem ofMono_toMono (x : ⨂[R] _ : α, (κ → R)) : ofMono (R := R) (toMono x) = x := by
  classical
  refine x.induction_on ?_ ?_
  · intro r v
    rw [map_smul, map_smul, ofMono_toMono_tprod]
  · intro y z hy hz
    rw [map_add, map_add, hy, hz]

/-- **The missing Mathlib basis, in the case that matters.** For `V` free with basis
indexed by `κ`, the tensor power `V^{⊗α}` is the free module on index tuples `α → κ`
— the monomial basis. -/
noncomputable def monoEquiv : (⨂[R] _ : α, (κ → R)) ≃ₗ[R] ((α → κ) → R) :=
  LinearEquiv.ofLinear toMono ofMono (by ext g; simp [toMono_ofMono])
    (by ext x; simpa using ofMono_toMono_tprod (R := R) x)

/-- Permuting the tensor factors, as `PiTensorProduct.reindex`. -/
noncomputable def tensorPerm (σ : Equiv.Perm α) :
    (⨂[R] _ : α, (κ → R)) ≃ₗ[R] (⨂[R] _ : α, (κ → R)) :=
  PiTensorProduct.reindex R (fun _ => (κ → R)) σ

/-- **The correspondence.** Under the monomial basis, permuting the tensor FACTORS is
precomposition on index tuples — i.e. exactly `indexPerm`, at `σ⁻¹`.

This is what transports the `q = 1` character computation from the concrete model onto
the actual tensor power. -/
theorem monoEquiv_tensorPerm (σ : Equiv.Perm α) (x : ⨂[R] _ : α, (κ → R)) (g : α → κ) :
    monoEquiv (tensorPerm σ x) g = monoEquiv (R := R) x (g ∘ σ) := by
  classical
  refine x.induction_on ?_ ?_
  · intro r v
    simp only [map_smul, tensorPerm, PiTensorProduct.reindex_tprod, Pi.smul_apply,
      monoEquiv, LinearEquiv.ofLinear_apply, toMono_tprod]
    congr 1
    rw [← Equiv.prod_comp σ (fun i => v (σ.symm i) (g i))]
    simp
  · intro y z hy hz
    simp only [map_add, Pi.add_apply] at *
    rw [hy, hz]

end QOU.MassTheory
