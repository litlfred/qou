import Mathlib.Algebra.Module.Basic
import Mathlib.LinearAlgebra.Projection
import Mathlib.Tactic.Abel


/-!
# QOU.Torsion.descent_eigenspaces — Eigenspaces of the descent involution

The descent involution τₙ = ℓₙ ∘ 𝔡_{n+1} is idempotent on
End_𝒞(A_{n+1}), so the standard idempotent splitting gives a direct sum
decomposition into descended (im τₙ) and transient (ker τₙ) subalgebras.

## References

- [leitner2026] §3 Lifting and Descent
-/

namespace QOU.Torsion

/-! ## Abstract setup: idempotent on an R-algebra -/

variable {R : Type*} [CommRing R]
variable {M : Type*} [AddCommGroup M] [Module R M]

/-- An idempotent R-linear endomorphism. -/
structure IdempotentEndomorphism (M : Type*) [AddCommGroup M] [Module R M] where
  toFun : M →ₗ[R] M
  idem : toFun ∘ₗ toFun = toFun

/-- The descended subalgebra: image of the idempotent. -/
def IdempotentEndomorphism.descended (τ : IdempotentEndomorphism (R := R) M) :
    Submodule R M :=
  LinearMap.range τ.toFun

/-- The transient complement: kernel of the idempotent. -/
def IdempotentEndomorphism.transient (τ : IdempotentEndomorphism (R := R) M) :
    Submodule R M :=
  LinearMap.ker τ.toFun

/-- Every element decomposes uniquely as descended + transient. -/
-- Ref: [leitner2026] §3, Proposition: Eigenspaces of the descent involution
theorem idempotent_direct_sum_decomposition
    (τ : IdempotentEndomorphism (R := R) M) :
    τ.descended ⊔ τ.transient = ⊤ := by
  rw [eq_top_iff]
  intro x _
  rw [Submodule.mem_sup]
  refine ⟨τ.toFun x, LinearMap.mem_range_self τ.toFun x,
         x - τ.toFun x, ?_, by abel⟩
  show τ.toFun (x - τ.toFun x) = 0
  rw [map_sub, show τ.toFun (τ.toFun x) = τ.toFun x from
    congr_fun (congr_arg DFunLike.coe τ.idem) x, sub_self]

/-- The descended and transient submodules intersect trivially. -/
-- Ref: [leitner2026] §3, Proposition: Eigenspaces of the descent involution
theorem idempotent_direct_sum_disjoint
    (τ : IdempotentEndomorphism (R := R) M) :
    Disjoint τ.descended τ.transient := by
  rw [Submodule.disjoint_def]
  intro x hx_desc hx_trans
  simp only [IdempotentEndomorphism.transient, LinearMap.mem_ker] at hx_trans
  simp only [IdempotentEndomorphism.descended, LinearMap.mem_range] at hx_desc
  obtain ⟨y, rfl⟩ := hx_desc
  rwa [show τ.toFun (τ.toFun y) = τ.toFun y from
    congr_fun (congr_arg DFunLike.coe τ.idem) y] at hx_trans

/-- An element in the image of the ascent ℓₙ is fixed by τₙ (descended). -/
-- Ref: [leitner2026] §3, Proposition: Eigenspaces of the descent involution
theorem ascent_image_is_descended
    {N : Type*} [AddCommGroup N] [Module R N]
    (ℓ : N →ₗ[R] M) (𝔡 : M →ₗ[R] N)
    (retraction : 𝔡 ∘ₗ ℓ = LinearMap.id)
    (τ : IdempotentEndomorphism (R := R) M)
    (hτ : τ.toFun = ℓ ∘ₗ 𝔡)
    (x : M) (hx : x ∈ LinearMap.range ℓ) :
    τ.toFun x = x := by
  obtain ⟨y, rfl⟩ := hx
  simp only [hτ, LinearMap.comp_apply]; congr 1
  simpa [LinearMap.comp_apply] using congr_fun (congr_arg DFunLike.coe retraction) y

/-- An element with no pre-image under descent is transient. -/
-- Ref: [leitner2026] §3, Proposition: Eigenspaces of the descent involution
theorem no_preimage_is_transient
    {N : Type*} [AddCommGroup N] [Module R N]
    (ℓ : N →ₗ[R] M) (𝔡 : M →ₗ[R] N)
    (τ : IdempotentEndomorphism (R := R) M)
    (hτ : τ.toFun = ℓ ∘ₗ 𝔡)
    (x : M) (hx : 𝔡 x = 0) :
    τ.toFun x = 0 := by
  simp only [hτ, LinearMap.comp_apply, hx, map_zero]

end QOU.Torsion
