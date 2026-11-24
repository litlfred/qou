import Mathlib.Analysis.InnerProductSpace.PiL2
import Mathlib.LinearAlgebra.Trace
import Mathlib.GroupTheory.SpecificGroups.Alternating

/-!
# QOU.MathlibExt.TraceLeDim — `‖tr U‖ ≤ dim V` for an isometry, with equality iff scalar

Issue #8985 (the `q = 1` shadow of the sign of the partition-weight binding log-trace, #8983).

## Main results

* `QOU.MathlibExt.trace_eq_sum_inner` — the trace of an endomorphism of a finite-dimensional
  inner-product space is `∑ i, ⟪b i, T (b i)⟫` for any orthonormal basis `b`.
* `QOU.MathlibExt.norm_trace_le_finrank` — if `U` preserves norms then `‖tr U‖ ≤ finrank V`.
* `QOU.MathlibExt.norm_trace_eq_finrank_iff` — equality holds iff `U = c • id` with `‖c‖ = 1`.
* `QOU.MathlibExt.norm_trace_lt_finrank_of_not_scalar` — the strict form.
* `QOU.MathlibExt.abs_trace_eq_finrank_iff_real` — over `ℝ` (orthogonal maps, Young's
  orthogonal form): `|tr O| = n ↔ O = id ∨ O = -id`.
* `QOU.MathlibExt.norm_trace_rep_lt_finrank` — for a norm-preserving representation
  `ρ : G →* End V` whose kernel lies in a subgroup `K` and whose image is centreless,
  `‖tr ρ g‖ < finrank V` for every `g ∉ K`.
* `QOU.MathlibExt.norm_trace_perm_rep_lt_finrank_of_sign_eq_neg_one` — the `S_k` case with
  `K = A_k`: an odd permutation has `‖tr ρ w‖ < finrank V`.

## Route

No spectral theorem and no finite-order hypothesis are needed. For an orthonormal basis `b`,
`tr U = ∑ ⟪b i, U (b i)⟫` and each term has norm `≤ 1` by Cauchy–Schwarz, giving the bound.
For equality put `c = tr U / n`, so `‖c‖ = 1`. Then
`∑ ‖U (b i) − c • b i‖² = 2n − 2 Re(c̄ · tr U) = 2n − 2n = 0`, so `U (b i) = c • b i` for each
`i`, and `U = c • id`. The bound therefore holds for every linear isometry, not only for
finite-order unitaries.

## What is NOT formalised here

Mathlib has no Specht modules. The `S_k` statement takes as **hypotheses** the two facts the
issue's proof uses about an irreducible `ρ_λ` with `f^λ > 1`: its kernel lies in `A_k`, and its
image is centreless (the image is `S_k`, or `S₃` for `λ = (2,2)`, both centreless for `k ≥ 3`).
Those facts are not proved here. Nothing in this file is evaluated at `q₀`; it is the `q = 1`
statement only.
-/

namespace QOU.MathlibExt

open LinearMap Module

section Core

variable {𝕜 E : Type*} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [FiniteDimensional 𝕜 E]

omit [FiniteDimensional 𝕜 E] in
/-- Trace via an orthonormal basis: `tr T = ∑ i, ⟪b i, T (b i)⟫`. -/
theorem trace_eq_sum_inner {ι : Type*} [Fintype ι] [DecidableEq ι]
    (b : OrthonormalBasis ι 𝕜 E) (T : E →ₗ[𝕜] E) :
    trace 𝕜 E T = ∑ i, inner 𝕜 (b i) (T (b i)) := by
  rw [trace_eq_matrix_trace 𝕜 b.toBasis, Matrix.trace]
  simp [LinearMap.toMatrix_apply, OrthonormalBasis.coe_toBasis,
    OrthonormalBasis.coe_toBasis_repr_apply, OrthonormalBasis.repr_apply_apply]

/-- A norm-preserving endomorphism of a finite-dimensional inner-product space has
`‖tr U‖ ≤ finrank`. -/
theorem norm_trace_le_finrank (U : E →ₗ[𝕜] E) (hU : ∀ x, ‖U x‖ = ‖x‖) :
    ‖trace 𝕜 E U‖ ≤ finrank 𝕜 E := by
  set b := stdOrthonormalBasis 𝕜 E
  rw [trace_eq_sum_inner b]
  calc ‖∑ i, inner 𝕜 (b i) (U (b i))‖
      ≤ ∑ i, ‖inner 𝕜 (b i) (U (b i))‖ := norm_sum_le _ _
    _ ≤ ∑ _i : Fin (finrank 𝕜 E), (1 : ℝ) := by
        refine Finset.sum_le_sum fun i _ => ?_
        calc ‖inner 𝕜 (b i) (U (b i))‖ ≤ ‖b i‖ * ‖U (b i)‖ := norm_inner_le_norm _ _
          _ = 1 := by rw [hU, b.orthonormal.1 i]; norm_num
    _ = finrank 𝕜 E := by simp

/-- Equality case: a norm-preserving `U` has `‖tr U‖ = finrank` iff `U = c • id` for a
unit scalar `c`. -/
theorem norm_trace_eq_finrank_iff (U : E →ₗ[𝕜] E) (hU : ∀ x, ‖U x‖ = ‖x‖) :
    ‖trace 𝕜 E U‖ = finrank 𝕜 E ↔ ∃ c : 𝕜, ‖c‖ = 1 ∧ U = c • LinearMap.id := by
  constructor
  · intro h
    set b := stdOrthonormalBasis 𝕜 E
    by_cases hn : finrank 𝕜 E = 0
    · refine ⟨1, by simp, ?_⟩
      apply b.toBasis.ext
      intro i
      exact absurd i.2 (by omega)
    have hnR : (0 : ℝ) < finrank 𝕜 E := by exact_mod_cast Nat.pos_of_ne_zero hn
    set c : 𝕜 := trace 𝕜 E U / (finrank 𝕜 E : 𝕜) with hc
    have hcn : ‖c‖ = 1 := by
      rw [hc, norm_div, h, RCLike.norm_natCast]; exact div_self hnR.ne'
    refine ⟨c, hcn, ?_⟩
    -- `∑ ‖U (b i) − c • b i‖² = 0`
    have key : ∑ i, ‖U (b i) - c • b i‖ ^ 2 = 0 := by
      have hterm : ∀ i, ‖U (b i) - c • b i‖ ^ 2
          = 2 - 2 * RCLike.re (c * inner 𝕜 (U (b i)) (b i)) := by
        intro i
        rw [norm_sub_sq (𝕜 := 𝕜), inner_smul_right, norm_smul, hcn, hU, b.orthonormal.1 i]
        ring
      simp_rw [hterm]
      rw [Finset.sum_sub_distrib, ← Finset.mul_sum, ← map_sum (RCLike.re (K := 𝕜)),
        ← Finset.mul_sum]
      have hsum : ∑ i, inner 𝕜 (U (b i)) (b i) = (starRingEnd 𝕜) (trace 𝕜 E U) := by
        rw [trace_eq_sum_inner b, map_sum]
        exact Finset.sum_congr rfl fun i _ => (inner_conj_symm _ _).symm
      rw [hsum]
      have hre : RCLike.re (c * (starRingEnd 𝕜) (trace 𝕜 E U)) = finrank 𝕜 E := by
        have htr : trace 𝕜 E U = c * (finrank 𝕜 E : 𝕜) := by
          rw [hc, div_mul_cancel₀]; exact_mod_cast hn
        rw [htr, RingHom.map_mul, map_natCast, ← mul_assoc, RCLike.mul_conj, hcn]
        simp
      rw [hre]
      simp only [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
      ring
    have hzero : ∀ i, U (b i) = c • b i := by
      intro i
      have h0 := (Finset.sum_eq_zero_iff_of_nonneg (fun j _ => by positivity)).1 key i
        (Finset.mem_univ i)
      have : ‖U (b i) - c • b i‖ = 0 := by simpa using h0
      exact sub_eq_zero.1 (norm_eq_zero.1 this)
    apply b.toBasis.ext
    intro i
    simpa [OrthonormalBasis.coe_toBasis] using hzero i
  · rintro ⟨c, hc, rfl⟩
    rw [map_smul, LinearMap.trace_id, norm_smul, hc, one_mul, RCLike.norm_natCast]

/-- Strict form: a norm-preserving `U` that is not a unit scalar has `‖tr U‖ < finrank`. -/
theorem norm_trace_lt_finrank_of_not_scalar (U : E →ₗ[𝕜] E) (hU : ∀ x, ‖U x‖ = ‖x‖)
    (hns : ∀ c : 𝕜, U ≠ c • LinearMap.id) :
    ‖trace 𝕜 E U‖ < finrank 𝕜 E := by
  refine lt_of_le_of_ne (norm_trace_le_finrank U hU) fun h => ?_
  obtain ⟨c, -, hc⟩ := (norm_trace_eq_finrank_iff U hU).1 h
  exact hns c hc

end Core

section Real

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]

/-- Real (orthogonal) form: `|tr O| = n ↔ O = id ∨ O = -id`. -/
theorem abs_trace_eq_finrank_iff_real (O : E →ₗ[ℝ] E) (hO : ∀ x, ‖O x‖ = ‖x‖) :
    |trace ℝ E O| = finrank ℝ E ↔ O = LinearMap.id ∨ O = -LinearMap.id := by
  rw [← Real.norm_eq_abs, norm_trace_eq_finrank_iff O hO]
  constructor
  · rintro ⟨c, hc, rfl⟩
    rcases (abs_eq zero_le_one).1 (by rwa [Real.norm_eq_abs] at hc) with rfl | rfl
    · left; simp
    · right; simp
  · rintro (rfl | rfl)
    · exact ⟨1, by simp, by simp⟩
    · exact ⟨-1, by simp, by simp⟩

end Real

section Rep

variable {𝕜 E G : Type*} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [FiniteDimensional 𝕜 E] [Group G]

omit [FiniteDimensional 𝕜 E] in
/-- If `ρ g` is a scalar, the kernel of `ρ` lies in `K`, and the image of `ρ` is centreless,
then `g ∈ K`. -/
theorem mem_of_rep_scalar (ρ : G →* (E →ₗ[𝕜] E)) (K : Subgroup G)
    (hker : ∀ g, ρ g = 1 → g ∈ K)
    (hcentre : ∀ g, (∀ h, ρ g * ρ h = ρ h * ρ g) → ρ g = 1)
    {g : G} {c : 𝕜} (hg : ρ g = c • LinearMap.id) : g ∈ K := by
  refine hker g (hcentre g fun h => ?_)
  rw [hg]
  ext x
  simp

/-- A norm-preserving representation with kernel in `K` and centreless image has
`‖tr ρ g‖ < finrank` for every `g ∉ K`. -/
theorem norm_trace_rep_lt_finrank (ρ : G →* (E →ₗ[𝕜] E)) (K : Subgroup G)
    (hiso : ∀ g x, ‖ρ g x‖ = ‖x‖)
    (hker : ∀ g, ρ g = 1 → g ∈ K)
    (hcentre : ∀ g, (∀ h, ρ g * ρ h = ρ h * ρ g) → ρ g = 1)
    {g : G} (hg : g ∉ K) :
    ‖trace 𝕜 E (ρ g)‖ < finrank 𝕜 E :=
  norm_trace_lt_finrank_of_not_scalar (ρ g) (hiso g)
    fun _ hc => hg (mem_of_rep_scalar ρ K hker hcentre hc)

/-- **`S_k`, `q = 1`.** Let `ρ` be a norm-preserving representation of `S_k` whose kernel lies
in `A_k` and whose image is centreless (the facts an irreducible `ρ_λ` with `f^λ > 1` has; they
are hypotheses here, since Mathlib has no Specht modules). Then every odd permutation `w`
has `‖tr ρ w‖ < finrank`, i.e. `|χ_λ(w)| < f^λ`. -/
theorem norm_trace_perm_rep_lt_finrank_of_sign_eq_neg_one {k : ℕ}
    (ρ : Equiv.Perm (Fin k) →* (E →ₗ[𝕜] E))
    (hiso : ∀ g x, ‖ρ g x‖ = ‖x‖)
    (hker : ∀ g, ρ g = 1 → g ∈ alternatingGroup (Fin k))
    (hcentre : ∀ g, (∀ h, ρ g * ρ h = ρ h * ρ g) → ρ g = 1)
    {w : Equiv.Perm (Fin k)} (hw : Equiv.Perm.sign w = -1) :
    ‖trace 𝕜 E (ρ w)‖ < finrank 𝕜 E := by
  refine norm_trace_rep_lt_finrank ρ (alternatingGroup (Fin k)) hiso hker hcentre ?_
  rw [Equiv.Perm.mem_alternatingGroup, hw]
  decide

end Rep

end QOU.MathlibExt
