import Mathlib.RingTheory.MatrixAlgebra
import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.Algebra.Module.LinearMap.Polynomial
import Mathlib.LinearAlgebra.TensorProduct.Basis

/-!
# QOU.MathlibExt.EndBaseChange — the endomorphism algebra base-changes

For a finite free module `M` over a commutative ring `R` and an `R`-algebra `A`,
extension of scalars carries the endomorphism algebra to the endomorphism
algebra:

`A ⊗[R] Module.End R M ≃ₐ[R] Module.End A (A ⊗[R] M)`.

## Why this file exists

Mathlib carries the *map* but not its bijectivity. `Module.End.baseChangeHom`
has type `Module.End R M →ₐ[R] Module.End A (A ⊗[R] M)`, and
`Module.endTensorEndAlgHom` is likewise an algebra hom; neither comes with a
lemma saying the induced map out of `A ⊗[R] Module.End R M` is an equivalence.
A name scan over all 6990 Mathlib modules in the workspace found no such lemma
(bean `qou-dr1c`).

The gap matters for the `k[S_n]` division-ring collapse — residual item 1 of
`SnWedderburnPartitionBridge.sn_isotypic_specht_split`, scoped in
[`docs/audits/2026-08-10-sn-division-ring-collapse-scoping.md`](../../../../../docs/audits/2026-08-10-sn-division-ring-collapse-scoping.md).
The collapse argument needs `S^μ` to stay simple after extending scalars to an
algebraic closure, and the standard route to that runs
`End ⊗ K ≅ End_K(· ⊗ K)` followed by Schur. This file supplies that step at the
level of plain modules.

**Scope.** This is the module-level statement only. The application needs the
*equivariant* version, `K ⊗_k End_{k[G]}(V) ≅ End_{K[G]}(K ⊗_k V)`, which does
not follow formally from this one: it additionally needs that taking
`G`-invariants commutes with the base change. For finite `G` in characteristic
zero that is available through the averaging idempotent, since extension of
scalars preserves the image of an idempotent, but it is not proved here. So
this file is a rung, not the item.

## Construction

Through matrices, which keeps every step an existing Mathlib equivalence:

`A ⊗[R] End R M ≃ A ⊗[R] Matrix ι ι R ≃ Matrix ι ι A ≃ End A (A ⊗[R] M)`

using `LinearMap.toMatrixAlgEquiv` at both ends and `matrixEquivTensor` in the
middle. `endBaseChangeEquiv_tmul` then identifies the result with the canonical
map `a ⊗ₜ f ↦ a • LinearMap.baseChange A f`, which is what makes the
equivalence usable rather than merely an existence statement — without it the
definition would only say that *some* isomorphism exists.

The equivalence is stated over `R`. It is in fact `A`-linear, but `A`-linearity
is not needed by the intended consumer and `matrixEquivTensor` is itself only
an `R`-algebra equivalence, so no attempt is made to strengthen it here.
-/

open TensorProduct

namespace QOU.MathlibExt

variable {R A M ι : Type} [CommRing R] [CommRing A] [Algebra R A]
  [AddCommGroup M] [Module R M]

/-- Extension of scalars carries `End R M` to `End A (A ⊗[R] M)`, for `M` free
with a finite basis `b`. See `endBaseChangeEquiv_tmul` for the value on
generators, which identifies this with the canonical map. -/
noncomputable def endBaseChangeEquiv [Fintype ι] [DecidableEq ι]
    (b : Module.Basis ι R M) :
    A ⊗[R] Module.End R M ≃ₐ[R] Module.End A (A ⊗[R] M) :=
  ((Algebra.TensorProduct.congr (AlgEquiv.refl (R := R) (A₁ := A))
      (LinearMap.toMatrixAlgEquiv b)).trans (matrixEquivTensor ι R A).symm).trans
    ((LinearMap.toMatrixAlgEquiv (Algebra.TensorProduct.basis A b)).symm.restrictScalars R)

/-- `endBaseChangeEquiv` is the canonical map: it sends `a ⊗ₜ f` to
`a • f.baseChange A`. -/
theorem endBaseChangeEquiv_tmul [Fintype ι] [DecidableEq ι]
    (b : Module.Basis ι R M) (a : A) (f : Module.End R M) :
    endBaseChangeEquiv (A := A) b (a ⊗ₜ f) = a • LinearMap.baseChange A f := by
  have h : (LinearMap.toMatrixAlgEquiv (Algebra.TensorProduct.basis A b))
      (LinearMap.baseChange A f) = ((LinearMap.toMatrixAlgEquiv b) f).map (algebraMap R A) := by
    simp [LinearMap.toMatrixAlgEquiv, LinearMap.toMatrix_baseChange (R := R) (A := A) f b b]
  simp [endBaseChangeEquiv, ← h]

/-- Basis-free form: for `M` finite and free over `R`, the endomorphism algebra
base-changes. Stated as `Nonempty` because the equivalence depends on a choice
of basis. -/
theorem nonempty_endBaseChangeEquiv [Module.Free R M] [Module.Finite R M] :
    Nonempty (A ⊗[R] Module.End R M ≃ₐ[R] Module.End A (A ⊗[R] M)) := by
  classical
  exact ⟨endBaseChangeEquiv (Module.Free.chooseBasis R M)⟩

end QOU.MathlibExt
