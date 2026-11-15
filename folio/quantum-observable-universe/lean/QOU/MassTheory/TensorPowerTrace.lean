import Mathlib.Tactic
import Mathlib.LinearAlgebra.Trace
import Mathlib.LinearAlgebra.Matrix.ToLin
import QOU.MassTheory.TensorTraceCharacter
import QOU.MassTheory.PiTensorMonomialBasis

/-!
# `LinearMap.trace` of the factor permutation on a tensor power

Bean `qou-mex9`. The last packaging step of the `qou-uinl` arc.

`TensorTraceCharacter` computed the `q = 1` character as a **matrix** trace in the
monomial model, and `PiTensorMonomialBasis` identified that model with the genuine
tensor power. Both files said the same thing was still missing: a statement phrased
with `LinearMap.trace` over `⨂` itself, which needs `Module.Free`/`Module.Finite`
instances for the tensor power and the trace-to-matrix-trace identification. This
file supplies both:

    LinearMap.trace R (⨂[R] _ : α, (κ → R)) (tensorPerm σ) = (card κ) ^ orbitCount σ

and `trace_tensorPerm_two` is the `card κ = 2` case — the `2^{c(σ)}` that
`ClassicalTraceFloor` states as its step-1 hypothesis, now over the real object.

## How

* **Free and finite** are *transported* along `monoEquiv` (`Module.Free.of_equiv`,
  `Module.Finite.equiv`). This matters rather than being bookkeeping: `LinearMap.trace`
  is defined on any module but is junk without a basis, so without these instances the
  statement above would be vacuous rather than false.
* **Conjugation.** `monoEquiv_comp_tensorPerm` says permuting the tensor *factors* is
  conjugate to precomposition on index tuples by `indexPerm σ⁻¹`, and
  `LinearMap.trace_comp_comm'` moves the trace across that conjugation.
* **`orbitCount_inv`** closes the `σ⁻¹`: orbits are inversion-invariant
  (`support_inv`, `cycleType_inv`), so the `σ⁻¹` introduced by the variance of
  precomposition costs nothing.

## 🛑 Scope

This completes the **`q = 1`** leg only. Quantum Schur–Weyl (`q ≠ 1`) is untouched —
bean `qou-mpq5` scoped that as a multi-week gap (the Jimbo double-centralizer plus
Hoefsmit matrix units) and deliberately refused to fake it. **That assessment stands.**
Nothing here bears on it.

-- Ref: [leitner2026] bean qou-mex9; the permutation character on a tensor power is
-- classical, and `d^{c(σ)}` is its standard form.
-/

open scoped TensorProduct
open Equiv Equiv.Perm Finset

namespace QOU.MassTheory

variable {α : Type*} [Fintype α] [DecidableEq α]

/-- The orbit count is inversion-invariant: `σ` and `σ⁻¹` have the same orbits. -/
theorem orbitDefect_inv (σ : Perm α) : orbitDefect σ⁻¹ = orbitDefect σ := by
  simp [orbitDefect, support_inv, cycleType_inv]

theorem orbitCount_inv (σ : Perm α) : orbitCount σ⁻¹ = orbitCount σ := by
  simp [orbitCount, orbitDefect_inv]

variable {R : Type*} [CommRing R]
variable {κ : Type*} [Fintype κ] [DecidableEq κ]

/-- Precomposition by a permutation of the monomial index set, as an endomorphism of
the coordinate space. -/
def precompLin (τ : Perm (α → κ)) : ((α → κ) → R) →ₗ[R] ((α → κ) → R) where
  toFun g := g ∘ τ
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

omit [Fintype α] [DecidableEq α] [Fintype κ] [DecidableEq κ] in
@[simp] theorem precompLin_apply (τ : Perm (α → κ)) (g : (α → κ) → R) (x : α → κ) :
    precompLin (R := R) τ g x = g (τ x) := rfl

/-- The trace of precomposition is the number of fixed index tuples. -/
theorem trace_precompLin (τ : Perm (α → κ)) :
    LinearMap.trace R _ (precompLin (R := R) τ)
      = (#(univ.filter fun g : α → κ => τ g = g) : ℕ) := by
  classical
  rw [LinearMap.trace_eq_matrix_trace R (Pi.basisFun R (α → κ)), Matrix.trace]
  simp only [Matrix.diag_apply, LinearMap.toMatrix_apply, Pi.basisFun_apply,
    Pi.basisFun_repr, precompLin_apply]
  simp [Pi.single_apply, eq_comm, Finset.sum_boole]

/-- **Free and finite**, transported from the coordinate space along `monoEquiv` —
so `LinearMap.trace` over the tensor power is a genuine trace and not the junk value
it takes on a module with no basis. -/
noncomputable instance : Module.Free R (⨂[R] _ : α, (κ → R)) :=
  Module.Free.of_equiv (monoEquiv (R := R) (α := α) (κ := κ)).symm

instance : Module.Finite R (⨂[R] _ : α, (κ → R)) :=
  Module.Finite.equiv (monoEquiv (R := R) (α := α) (κ := κ)).symm

/-- Permuting the tensor factors is conjugate, via `monoEquiv`, to precomposition on
index tuples by `indexPerm σ⁻¹`. -/
theorem monoEquiv_comp_tensorPerm (σ : Perm α) :
    (monoEquiv (R := R) (α := α) (κ := κ)).toLinearMap ∘ₗ (tensorPerm σ).toLinearMap
      = precompLin (R := R) (indexPerm σ⁻¹ κ) ∘ₗ
        (monoEquiv (R := R) (α := α) (κ := κ)).toLinearMap := by
  ext x g
  simpa using monoEquiv_tensorPerm σ (PiTensorProduct.tprod R x) g

/-- **The permutation character on the tensor power, as `LinearMap.trace`.**

`σ` permuting the factors of `V^{⊗α}` with `V` free of rank `card κ` has trace
`(card κ) ^ orbitCount σ`. At `card κ = 2` this is the `2^{c(σ)}` of
`ClassicalTraceFloor`'s step 1 — over the genuine `PiTensorProduct`, with
`LinearMap.trace`. -/
theorem trace_tensorPerm (σ : Perm α) :
    LinearMap.trace R (⨂[R] _ : α, (κ → R)) (tensorPerm σ).toLinearMap
      = (Fintype.card κ ^ orbitCount σ : ℕ) := by
  classical
  have hconj : (tensorPerm (R := R) (κ := κ) σ).toLinearMap
      = (monoEquiv (R := R) (α := α) (κ := κ)).symm.toLinearMap ∘ₗ
        (precompLin (R := R) (indexPerm σ⁻¹ κ) ∘ₗ
          (monoEquiv (R := R) (α := α) (κ := κ)).toLinearMap) := by
    rw [← monoEquiv_comp_tensorPerm, ← LinearMap.comp_assoc]
    ext x
    simp
  rw [hconj, LinearMap.trace_comp_comm']
  have : (precompLin (R := R) (indexPerm σ⁻¹ κ) ∘ₗ
      (monoEquiv (R := R) (α := α) (κ := κ)).toLinearMap) ∘ₗ
      (monoEquiv (R := R) (α := α) (κ := κ)).symm.toLinearMap
      = precompLin (R := R) (indexPerm σ⁻¹ κ) := by
    ext g; simp
  rw [this, trace_precompLin]
  congr 1
  rw [card_filter_fixed_indexPerm σ⁻¹ κ, orbitCount_inv]

/-- **The `card κ = 2` case**, the exact shape `ClassicalTraceFloor` step 1 assumes:
the `q = 1` trace of a braid word's permutation on `(ℂ²)^{⊗n}` is `2^{c(σ)}`, before
the `2^{-n}` normalisation. -/
theorem trace_tensorPerm_two (σ : Perm α) :
    LinearMap.trace R (⨂[R] _ : α, (Fin 2 → R)) (tensorPerm σ).toLinearMap
      = (2 ^ orbitCount σ : ℕ) := by
  rw [trace_tensorPerm]
  simp

end QOU.MassTheory
