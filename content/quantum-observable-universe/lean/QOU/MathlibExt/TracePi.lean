import Mathlib.LinearAlgebra.Trace
import Mathlib.LinearAlgebra.StdBasis
import Mathlib.LinearAlgebra.Matrix.ToLin

/-!
# QOU.MathlibExt.TracePi — the trace of a block-diagonal endomorphism of a product

Bean `qou-kwoa`.

Mathlib has `LinearMap.trace_prodMap'` for a **binary** product `M × N`, and nothing for
an arbitrary finite product `∀ i, M i`.  This file supplies the missing statement:

    trace (⨁ᵢ fᵢ) = ∑ᵢ trace fᵢ

Everything here is about `LinearMap.trace` alone — no algebra structure, no Hecke input —
so it is a pure Mathlib-gap file and belongs under `MathlibExt`.

## Why it is needed here

`QOU.SchurWeyl.heckeWedderburn` lands in `∀ lam : Partition (n + 1), Matrix (SYT lam) (SYT lam) K`,
an arbitrary finite product rather than an iterated binary one.  The nondegeneracy converse in
`RegTraceGramNondegenerate` proves its block statement for a **simple** ring, and a product of
matrix algebras is not simple, so the block verdicts have to be reassembled — which is exactly
this sum formula, applied to `lmul`.

## Proof

Via `LinearMap.trace_eq_matrix_trace` in the basis `Pi.basis b` indexed by `Σ i, ι i`: the
diagonal entry at `⟨j, k⟩` is `(b j).repr (f j (b j k)) k`, because a block-diagonal map sends
`Pi.single j v` to `Pi.single j (f j v)`.  Summing over the sigma type in two stages gives the
per-block matrix traces.
-/

namespace QOU.MathlibExt

open LinearMap Module

variable {K : Type*} [CommRing K]
variable {ι : Type*} [Fintype ι] [DecidableEq ι]
variable {M : ι → Type*} [∀ i, AddCommGroup (M i)] [∀ i, Module K (M i)]
variable [∀ i, Module.Free K (M i)] [∀ i, Module.Finite K (M i)]

/-- The block-diagonal endomorphism of `∀ i, M i` assembled from a family `f i : M i →ₗ M i`. -/
def piDiag (f : ∀ i, M i →ₗ[K] M i) : (∀ i, M i) →ₗ[K] (∀ i, M i) :=
  LinearMap.pi fun i => (f i).comp (LinearMap.proj i)

omit [Fintype ι] [DecidableEq ι] [∀ i, Module.Free K (M i)] [∀ i, Module.Finite K (M i)] in
@[simp] theorem piDiag_apply (f : ∀ i, M i →ₗ[K] M i) (x : ∀ i, M i) (i : ι) :
    piDiag f x i = f i (x i) := rfl

omit [Fintype ι] [∀ i, Module.Free K (M i)] [∀ i, Module.Finite K (M i)] in
theorem piDiag_single (f : ∀ i, M i →ₗ[K] M i) (j : ι) (v : M j) :
    piDiag f (Pi.single j v) = Pi.single j (f j v) := by
  funext i
  rcases eq_or_ne i j with rfl | hij
  · simp
  · simp [piDiag_apply, Pi.single_eq_of_ne hij]

/-- **The trace of a block-diagonal endomorphism of a finite product is the sum of the block
traces.**

The `∀ i` analogue of Mathlib's binary `LinearMap.trace_prodMap'`. -/
theorem trace_piDiag (f : ∀ i, M i →ₗ[K] M i) :
    LinearMap.trace K (∀ i, M i) (piDiag f) = ∑ i, LinearMap.trace K (M i) (f i) := by
  classical
  let b : ∀ i, Basis (Module.Free.ChooseBasisIndex K (M i)) K (M i) := fun i =>
    Module.Free.chooseBasis K (M i)
  have hpi : LinearMap.trace K (∀ i, M i) (piDiag f)
      = ∑ ji : (Σ i, Module.Free.ChooseBasisIndex K (M i)),
          LinearMap.toMatrix (Pi.basis b) (Pi.basis b) (piDiag f) ji ji := by
    rw [LinearMap.trace_eq_matrix_trace K (Pi.basis b) (piDiag f)]
    rfl
  have hentry : ∀ ji : (Σ i, Module.Free.ChooseBasisIndex K (M i)),
      LinearMap.toMatrix (Pi.basis b) (Pi.basis b) (piDiag f) ji ji
        = LinearMap.toMatrix (b ji.1) (b ji.1) (f ji.1) ji.2 ji.2 := by
    rintro ⟨j, k⟩
    rw [LinearMap.toMatrix_apply, LinearMap.toMatrix_apply]
    rw [Pi.basis_apply, piDiag_single, Pi.basis_repr]
    simp
  rw [hpi]
  simp only [hentry]
  rw [Fintype.sum_sigma]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [LinearMap.trace_eq_matrix_trace K (b j) (f j)]
  rfl

end QOU.MathlibExt
