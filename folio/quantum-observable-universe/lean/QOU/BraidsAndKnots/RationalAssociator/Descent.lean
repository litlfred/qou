import Mathlib.LinearAlgebra.Basis.VectorSpace
import Mathlib.LinearAlgebra.TensorProduct.Tower

/-!
# Linear descent along a field extension

Bean `qou-3fdg` (stage 2 of the rational-associator plan, under epic `qou-dk7p`).

In Bar-Natan's degree-by-degree construction (*On associators and the Grothendieck–Teichmüller
group I*, 1998), the next homogeneous coefficient of an associator solves an inhomogeneous
**linear** system `L x = w` whose operator `L` and right-hand side `w` are defined over `ℚ`,
because they depend only on the already-fixed rational lower-degree coefficients. If the
system has a solution after extending scalars to a field `K ⊇ ℚ` (for instance the degree
component of an associator over `K`), it has one over `ℚ`.

`exists_of_baseChange` proves this for any field `k`, any nontrivial `k`-algebra `K` and any
`k`-linear `L : V → W`, with no finiteness hypothesis. The proof applies a `k`-linear retraction
`π : K → k` with `π 1 = 1`, which exists because `k` is a field. No analysis, limit or
numerical value is used.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

open TensorProduct

variable {k K V W : Type*} [Field k] [CommRing K] [Nontrivial K] [Algebra k K]
  [AddCommGroup V] [Module k V] [AddCommGroup W] [Module k W]

/-- A `k`-linear retraction `π : K → k` of the structure map, so `π 1 = 1`. -/
theorem exists_retraction : ∃ π : K →ₗ[k] k, π 1 = 1 := by
  have hinj : Function.Injective (Algebra.linearMap k K) := by
    intro a b hab
    by_contra hne
    have h0 : algebraMap k K (a - b) = 0 := by
      rw [map_sub, sub_eq_zero]; exact hab
    exact ((IsUnit.mk0 _ (sub_ne_zero.2 hne)).map (algebraMap k K)).ne_zero h0
  obtain ⟨π, hπ⟩ := (Algebra.linearMap k K).exists_leftInverse_of_injective
    (LinearMap.ker_eq_bot.2 hinj)
  refine ⟨π, ?_⟩
  simpa using LinearMap.congr_fun hπ 1

/-- Contract `K ⊗ M → M` along a functional `π : K → k`: `a ⊗ m ↦ π a • m`. -/
noncomputable def contract (π : K →ₗ[k] k) (M : Type*) [AddCommGroup M] [Module k M] :
    K ⊗[k] M →ₗ[k] M :=
  TensorProduct.lift ((LinearMap.lsmul k M).comp π)

omit [Nontrivial K] in
@[simp] theorem contract_tmul (π : K →ₗ[k] k) {M : Type*} [AddCommGroup M] [Module k M]
    (a : K) (m : M) : contract π M (a ⊗ₜ m) = π a • m := by
  simp [contract]

omit [Nontrivial K] in
theorem contract_baseChange (π : K →ₗ[k] k) (L : V →ₗ[k] W) (x : K ⊗[k] V) :
    contract π W (L.baseChange K x) = L (contract π V x) := by
  induction x using TensorProduct.induction_on with
  | zero => simp
  | tmul a v => simp [LinearMap.baseChange_tmul]
  | add x y hx hy => simp only [map_add, hx, hy]

/-- **Linear descent.** If the `k`-linear system `L x = w` has a solution after extending
scalars to `K`, it has a solution over `k`. -/
theorem exists_of_baseChange (L : V →ₗ[k] W) (w : W)
    (h : ∃ x : K ⊗[k] V, L.baseChange K x = (1 : K) ⊗ₜ w) : ∃ v : V, L v = w := by
  obtain ⟨π, hπ⟩ := exists_retraction (k := k) (K := K)
  obtain ⟨x, hx⟩ := h
  refine ⟨contract π V x, ?_⟩
  rw [← contract_baseChange, hx, contract_tmul, hπ, one_smul]

end QOU.BraidsAndKnots.RationalAssociator
