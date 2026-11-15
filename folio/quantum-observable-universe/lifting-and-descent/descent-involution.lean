import Mathlib.Algebra.Module.Basic
import Mathlib.Algebra.Module.LinearMap.Defs


/-!
# QOU.DescentInvolution — The descent involution τₙ = ℓₙ ∘ 𝔡_{n+1}

The descent involution is the idempotent endomorphism on End_𝒞(A_{n+1})
formed by composing jet prolongation with descent.  Its eigenspace
decomposition gives the descended/transient splitting.

## References

- [leitner2026] §3 Lifting and Descent
-/

namespace QOU

variable {R : Type*} [CommRing R]

/-- The descent involution τₙ = ℓₙ ∘ 𝔡_{n+1} at level n of the brane tower.

    Given ascent ℓₙ : End(Aₙ) → End(A_{n+1}) and descent 𝔡_{n+1},
    the composition τₙ is idempotent: τₙ² = τₙ.

    LaTeX: `\label{def:descent-involution}` -/
-- Ref: [leitner2026] §3, Definition: Descent involution
structure DescentInvolution (M : Type*) [AddCommGroup M] [Module R M] where
  /-- The ascent embedding ℓₙ. -/
  ascent : M →ₗ[R] M
  /-- The descent map 𝔡_{n+1}. -/
  descent : M →ₗ[R] M
  /-- Retraction: 𝔡 ∘ ℓ = id. -/
  retraction : descent ∘ₗ ascent = LinearMap.id

/-- The involution τ = ℓ ∘ 𝔡. -/
def DescentInvolution.tau {M : Type*} [AddCommGroup M] [Module R M]
    (di : DescentInvolution (R := R) M) : M →ₗ[R] M :=
  di.ascent ∘ₗ di.descent

/-- τₙ is idempotent. -/
-- Ref: [leitner2026] §3
theorem DescentInvolution.tau_idem {M : Type*} [AddCommGroup M] [Module R M]
    (di : DescentInvolution (R := R) M) :
    di.tau ∘ₗ di.tau = di.tau := by
  ext x
  simp only [DescentInvolution.tau, LinearMap.comp_apply]
  rw [show di.descent (di.ascent (di.descent x)) = di.descent x from
    congr_fun (congr_arg DFunLike.coe di.retraction) (di.descent x)]

end QOU
