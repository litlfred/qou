import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.Trace
import QOU.MassTheory.OrbitQuotientCount

/-!
# The permutation character on a tensor power, as an actual trace

Bean `qou-uinl`, stage 2. `OrbitQuotientCount` proved the *count*

    #{f : α → κ // ∀ x, f (σ x) = f x} = (card κ) ^ orbitCount σ

and said plainly that identifying it with a trace was a further step. This file takes
that step, in the concrete free-module model.

## The statement

For `V` free of rank `card κ`, the tensor power `V^{⊗α}` has monomial basis indexed by
`α → κ`, and `σ` permuting the tensor factors acts on that basis by **precomposition**
`f ↦ f ∘ σ⁻¹`. That is a permutation of the basis, so its matrix is a permutation
matrix and its trace is a fixed-point count (`trace_permMatrixOf` below). Those fixed
points are exactly the invariant functions, so

    trace (σ on V^{⊗α}) = (card κ) ^ orbitCount σ

which at `card κ = 2` is `2^{c(σ)}` — `ClassicalTraceFloor`'s step 1.

## 🛑 Why the model is concrete rather than `PiTensorProduct`

**Measured, 2026-09-05: `Mathlib/LinearAlgebra/PiTensorProduct.lean` contains zero
occurrences of `Basis`.** Mathlib has `PiTensorProduct.reindex` — the action itself —
but **no basis for `⨂[R] i : ι, M`**, and no `finrank` lemma for it either. A literal
`LinearMap.trace (PiTensorProduct.reindex …)` statement therefore cannot be written
without first *constructing* that basis, which is a Mathlib-scale contribution in its
own right and is presumably why Mathlib lacks it.

**SUPERSEDED IN PART, same day:** `QOU.MassTheory.PiTensorMonomialBasis` now
*constructs* that basis in the case needed —
`monoEquiv : (⨂[R] _ : α, (κ → R)) ≃ₗ[R] ((α → κ) → R)` — and proves
`monoEquiv_tensorPerm`, that permuting the tensor **factors** corresponds to the
`indexPerm` below. So the concrete model used here is no longer a *substitute* for the
tensor power; it is the tensor power in coordinates, with the identification proved.
And `QOU.MassTheory.TensorPowerTrace` completes it: `trace_tensorPerm` states the
same character with `LinearMap.trace` over the tensor power itself. The matrix-trace
form below remains the computational core both of those rest on.

So this file works in the standard concrete model `V^{⊗α} = ((α → κ) → R)`, where the
monomial basis is definitionally the index type and the whole argument is a
permutation-matrix trace. That is not a workaround for the mathematics — it *is* the
monomial-basis computation — but it is a weaker statement than one phrased over `⨂`,
and the difference is recorded here rather than papered over.

## Why the permutation matrix is defined here rather than imported

Mathlib's `Equiv.Perm.permMatrix` and `Matrix.trace_permutation` live in
`Mathlib.LinearAlgebra.Matrix.Permutation`, whose import cone reaches
`Mathlib.Analysis.CStarAlgebra.Matrix` — measured, by trying to build it. Pulling a
C*-algebra cone into a statement about counting fixed points of a permutation is
disproportionate, so `permMatrixOf` below is defined directly over
`Mathlib.LinearAlgebra.Matrix.Trace` and `trace_permMatrixOf` reproves the one fact
needed (a five-line `Finset.sum` computation). If the cone is ever trimmed upstream,
this should be replaced by the Mathlib pair.

-- Ref: [leitner2026] bean qou-uinl; the permutation character on a tensor power is
-- classical, and `d^{c(σ)}` is its standard form.
-/

namespace QOU.MassTheory

open Equiv Equiv.Perm Finset

variable {α : Type*} [Fintype α] [DecidableEq α]

/-- `σ` permuting tensor factors acts on the monomial basis `α → κ` by precomposition.
This is the index-level shadow of `PiTensorProduct.reindex`. -/
def indexPerm (σ : Perm α) (κ : Type*) : Perm (α → κ) :=
  Equiv.arrowCongr σ (Equiv.refl κ)

omit [Fintype α] [DecidableEq α] in
@[simp] theorem indexPerm_apply (σ : Perm α) {κ : Type*} (f : α → κ) (x : α) :
    indexPerm σ κ f x = f (σ.symm x) := rfl

omit [Fintype α] [DecidableEq α] in
/-- A monomial basis vector is fixed by `σ` exactly when its index function is
constant on each cycle — i.e. exactly the invariant functions counted in
`OrbitQuotientCount`. -/
theorem indexPerm_fixed_iff (σ : Perm α) {κ : Type*} (f : α → κ) :
    indexPerm σ κ f = f ↔ ∀ x, f (σ x) = f x := by
  constructor
  · intro h x
    have := congrFun (congrArg (fun g : α → κ => g) h) (σ x)
    simpa using this.symm
  · intro h
    funext x
    have := h (σ.symm x)
    simpa using this.symm

/-- **The number of fixed monomial basis vectors is `(card κ) ^ orbitCount σ`.**
The combinatorial half of the trace computation — this is where
`orbitCount_invariant_functions` enters. -/
theorem card_filter_fixed_indexPerm (σ : Perm α) (κ : Type*) [Fintype κ] [DecidableEq κ] :
    #(univ.filter fun f : α → κ => indexPerm σ κ f = f)
      = Fintype.card κ ^ orbitCount σ := by
  classical
  rw [← orbitCount_invariant_functions σ κ, Fintype.card_subtype]
  congr 1
  ext f
  simp [indexPerm_fixed_iff]

/-- The matrix of a permutation of basis vectors. Defined here rather than imported —
see the module docstring: Mathlib's `permMatrix` drags in a C*-algebra cone. -/
def permMatrixOf {β : Type*} [DecidableEq β] (τ : Perm β) (R : Type*) [Zero R] [One R] :
    Matrix β β R :=
  Matrix.of fun i j => if τ j = i then 1 else 0

/-- **The trace of a permutation matrix is its number of fixed points.** The Mathlib
equivalent is `Matrix.trace_permutation`; reproved here to avoid its import cone. -/
theorem trace_permMatrixOf {β : Type*} [Fintype β] [DecidableEq β] (τ : Perm β)
    (R : Type*) [AddCommMonoidWithOne R] :
    Matrix.trace (permMatrixOf τ R) = (#(univ.filter fun i => τ i = i) : ℕ) := by
  classical
  rw [Matrix.trace]
  simp only [Matrix.diag, permMatrixOf, Matrix.of_apply]
  simp [Finset.sum_boole]

/-- **The permutation character on a tensor power, as an actual matrix trace.**

`σ` permuting the factors of `V^{⊗α}` with `V` free of rank `card κ` acts on the
monomial basis by the permutation `indexPerm σ κ`; its matrix is a permutation matrix
and its trace is `(card κ) ^ orbitCount σ`.

At `card κ = 2` this is the `2^{c(σ)}` of `ClassicalTraceFloor`'s step 1 — now a
trace, not a count. -/
theorem trace_permMatrixOf_indexPerm (σ : Perm α) (κ : Type*) [Fintype κ] [DecidableEq κ]
    (R : Type*) [AddCommMonoidWithOne R] :
    Matrix.trace (permMatrixOf (indexPerm σ κ) R)
      = (Fintype.card κ ^ orbitCount σ : ℕ) := by
  classical
  rw [trace_permMatrixOf, card_filter_fixed_indexPerm]

/-- The `card κ = 2` specialisation, in the exact shape `ClassicalTraceFloor` assumes:
the `q = 1` Markov trace of a braid word is `2^{c(σ)}` before the `2^{-n}`
normalisation. -/
theorem trace_permMatrixOf_two (σ : Perm α) (R : Type*) [AddCommMonoidWithOne R] :
    Matrix.trace (permMatrixOf (indexPerm σ (Fin 2)) R) = (2 ^ orbitCount σ : ℕ) := by
  rw [trace_permMatrixOf_indexPerm]
  simp

end QOU.MassTheory
