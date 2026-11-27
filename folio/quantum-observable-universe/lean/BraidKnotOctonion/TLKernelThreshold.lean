/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import BraidKnotOctonion.TLKernelThresholdThree
import HeckeTemperleyLieb.TemperleyLiebMarkovNondegenerate

/-!
# The exact threshold on every number of strands

For `n` generators (`n + 1` strands), `q ≠ 0` and `q² + 1 ≠ 0`: the radical of the Jimbo
trace form on `H_{n+1}` equals `θ(ker π)`, the pulled-back Temperley–Lieb kernel,
**exactly when `[k]_q ≠ 0` for every `3 ≤ k ≤ n + 2`** (`rad_eq_tlKernel_iff`), i.e. when
`1 + q² + ⋯ + q^{2(k−1)} ≠ 0` for those `k` (`rad_eq_tlKernel_iff_sum`).

At `n = 2` this is `TLKernelThresholdThree.rad_eq_tlKernel_iff` (`[3]`, `[4]`), re-derived
here as `rad_eq_tlKernel_iff_two` from the general statement.

## Route

* `π ∘ θ : H_{n+1} → TL_{n+1}(q + q⁻¹)`, `σ_i ↦ q − e_i`, is surjective and commutes with
  the inclusions (`P_surjective`, `P_incl`).
* The Jimbo trace factors through it, as `tv n = (normalised q-trace) ∘ tlRep`, and the
  Markov property of `jimboMarkov` descends: `tv` is a Markov trace on the
  Temperley–Lieb tower with parameter `ε = q/(q² + 1) = (q + q⁻¹)⁻¹` (`markovTower`).
* So `rad = θ(ker π)` iff `tv n` is nondegenerate, which is
  `TemperleyLiebMarkov.nondegenerate_iff`: iff `[k] ≠ 0` for `3 ≤ k ≤ n + 2`, with `[k]`
  the Chebyshev numbers at `δ = q + q⁻¹`, `q^{k−1}[k] = 1 + q² + ⋯ + q^{2(k−1)}`
  (`pow_mul_qint`).

Pure algebra over an arbitrary field; no empirical input.

-- Ref: [jones1983]; [wenzl1988]
-/

namespace QOU.IwahoriHecke.TLKernelThreshold

open QOU.SchurWeyl QOU.SchurWeyl.HeckeInclusion
open QOU.SchurWeyl.JimboActionKernel QOU.SchurWeyl.JimboKernelGeneric
open QOU.MathlibExt.TemperleyLieb QOU.MathlibExt.TemperleyLiebDimCatalan
open QOU.IwahoriHecke.TLCarrierBridge QOU.IwahoriHecke.TLKernelConvention
open QOU.IwahoriHecke.TLKernelEquality QOU.IwahoriHecke.TLKernelRootOfUnity
open QOU.MathlibExt.IwahoriHecke QOU.IwahoriHecke.TensorEmbed QOU.IwahoriHecke.RMatrix
open QOU.MathlibExt.TemperleyLiebMarkov
open QOU.IwahoriHecke.TLKernelThresholdThree (eps delta_mul_eps)

variable {K : Type*} [Field K] (q : K) (hq : q ≠ 0)

/-! ## The quotient map and the trace on every level -/

/-- `π ∘ θ`, `σ_i ↦ q − e_i`. -/
noncomputable def P (n : ℕ) : Hecke K q q⁻¹ n →ₐ[K] TLFin K (q + q⁻¹) n :=
  (skeinToTL hq n (δ := q + q⁻¹) (by field_simp)).comp (theta q hq n)

theorem P_σ (n : ℕ) (i : Fin n) :
    P q hq n (Hecke.σ K q q⁻¹ n i) = algebraMap K _ q - e K (q + q⁻¹) adjFin i :=
  skeinToTL_theta_σ hq n i

theorem P_tlE (n : ℕ) (i : Fin n) : P q hq n (tlE q n i) = e K (q + q⁻¹) adjFin i := by
  rw [tlE, map_sub, AlgHom.commutes, P_σ, sub_sub_cancel]

theorem P_surjective (n : ℕ) : Function.Surjective (P q hq n) := by
  rw [← AlgHom.range_eq_top, eq_top_iff, ← adjoin_e_eq_top, Algebra.adjoin_le_iff]
  rintro _ ⟨i, rfl⟩
  exact ⟨tlE q n i, P_tlE q hq n i⟩

theorem P_incl (n : ℕ) (y : Hecke K q q⁻¹ n) :
    P q hq (n + 1) (heckeIncl K q q⁻¹ n y) = incl (q + q⁻¹) n (P q hq n y) := by
  have : (P q hq (n + 1)).comp (heckeIncl K q q⁻¹ n) = (incl (q + q⁻¹) n).comp (P q hq n) :=
    by
      apply Hecke.hom_ext
      intro i
      rw [AlgHom.comp_apply, AlgHom.comp_apply, heckeIncl_σ, P_σ, P_σ, map_sub, AlgHom.commutes,
        incl_e]
  exact AlgHom.congr_fun this y

theorem mem_tlKernelPulled_iff_P (n : ℕ) (x : Hecke K q q⁻¹ n) :
    theta q hq n x ∈ tlKernelPulled hq n (δ := q + q⁻¹) (by field_simp) ↔ P q hq n x = 0 := by
  rw [tlKernelPulled, TwoSidedIdeal.mem_ker]; rfl

/-- The trace on `TL_{n+1}`: normalised `q`-trace of `tlRep`. -/
noncomputable def tv (n : ℕ) : TLFin K (q + q⁻¹) n →ₗ[K] K :=
  (((1 + q ^ 2) ^ (n + 1))⁻¹ • qtrLin q (n + 1)).comp
    (tlRep (R := K) q q⁻¹ n (mul_inv_cancel₀ hq)).toLinearMap

theorem tv_P (n : ℕ) (y : Hecke K q q⁻¹ n) : tv q hq n (P q hq n y) = jimboTrace q hq n y := by
  show _ = ((1 + q ^ 2) ^ (n + 1))⁻¹ • qtrLin q (n + 1) (jimbo q hq n y)
  rw [jimbo_eq_tlRep_comp q hq n]; rfl

/-- **The Jimbo trace descends to a Markov trace on the Temperley–Lieb tower**, with
parameter `ε = q/(q² + 1)`. -/
noncomputable def markovTower (hq21 : q ^ 2 + 1 ≠ 0) : MarkovTower (q + q⁻¹) (eps q) where
  τ := tv q hq
  tr_one := by rw [← map_one (P q hq 0), tv_P]; exact (jimboMarkov q hq hq21).tr_one 0
  tr_incl n x := by
    obtain ⟨y, rfl⟩ := P_surjective q hq n x
    rw [← P_incl, tv_P, tv_P]; exact (jimboMarkov q hq hq21).tr_incl n y
  tr_comm n x y := by
    obtain ⟨x, rfl⟩ := P_surjective q hq n x
    obtain ⟨y, rfl⟩ := P_surjective q hq n y
    rw [← map_mul, ← map_mul, tv_P, tv_P]; exact (jimboMarkov q hq hq21).tr_cyclic n x y
  tr_markov n x := by
    obtain ⟨y, rfl⟩ := P_surjective q hq n x
    let T := jimboMarkov q hq hq21
    have hT : ∀ m z, jimboTrace q hq m z = T.tr m z := fun _ _ => rfl
    have halg : ∀ m, T.tr m (algebraMap K _ q) = q := fun m => by
      rw [Algebra.algebraMap_eq_smul_one, map_smul, T.tr_one, smul_eq_mul, mul_one]
    rw [← P_incl, ← P_tlE q hq (n + 1) (Fin.last n), ← map_mul, tv_P, tv_P, hT, hT, tlE,
      mul_sub, map_sub, T.tr_markov, Algebra.algebraMap_eq_smul_one, mul_smul_comm, mul_one,
      map_smul, T.tr_incl, smul_eq_mul, eps]
    field_simp
    ring

/-! ## The threshold -/

/-- `rad = θ(ker π)` on `H_{n+1}` iff the descended trace is nondegenerate on `TL_{n+1}`. -/
theorem rad_eq_tlKernel_iff_nondegenerate (hq21 : q ^ 2 + 1 ≠ 0) (n : ℕ) :
    (∀ x : Hecke K q q⁻¹ n, (∀ y, jimboTrace q hq n (x * y) = 0) ↔
        theta q hq n x ∈ tlKernelPulled hq n (δ := q + q⁻¹) (by field_simp)) ↔
      Nondegenerate (markovTower q hq hq21) n := by
  have hτ : ∀ y, (markovTower q hq hq21).τ n (P q hq n y) = jimboTrace q hq n y :=
    tv_P q hq n
  constructor
  · intro hall x hx
    obtain ⟨x, rfl⟩ := P_surjective q hq n x
    refine (mem_tlKernelPulled_iff_P q hq n x).mp ((hall x).mp fun y => ?_)
    rw [← hτ, map_mul]; exact hx _
  · intro hnd x
    rw [mem_tlKernelPulled_iff_P]
    constructor
    · intro hx
      refine hnd _ fun z => ?_
      obtain ⟨y, rfl⟩ := P_surjective q hq n z
      rw [← map_mul, hτ]; exact hx y
    · intro hx y
      rw [← hτ, map_mul, hx, zero_mul, map_zero]

/-- **The exact threshold.**  For `q ≠ 0`, `q² + 1 ≠ 0` and `n` generators: the radical of
the Jimbo trace form on `H_{n+1}` equals `θ(ker π)` iff `[k] ≠ 0` for `3 ≤ k ≤ n + 2`
(Chebyshev numbers at `δ = q + q⁻¹`). -/
theorem rad_eq_tlKernel_iff (hq21 : q ^ 2 + 1 ≠ 0) (n : ℕ) :
    (∀ x : Hecke K q q⁻¹ n, (∀ y, jimboTrace q hq n (x * y) = 0) ↔
        theta q hq n x ∈ tlKernelPulled hq n (δ := q + q⁻¹) (by field_simp)) ↔
      ∀ k, 3 ≤ k → k ≤ n + 2 → qint (q + q⁻¹) k ≠ 0 := by
  rw [rad_eq_tlKernel_iff_nondegenerate q hq hq21 n,
    nondegenerate_iff _ (delta_mul_eps q hq hq21) n]

/-! ## In terms of `q` -/

include hq in
/-- `q^k [k+1] = 1 + q² + ⋯ + q^{2k}` at `δ = q + q⁻¹`. -/
theorem pow_mul_qint (k : ℕ) :
    q ^ k * qint (q + q⁻¹) (k + 1) = ∑ j ∈ Finset.range (k + 1), q ^ (2 * j) := by
  have hqq : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  have key : ∀ k, (q ^ k * qint (q + q⁻¹) (k + 1) = ∑ j ∈ Finset.range (k + 1), q ^ (2 * j)) ∧
      (q ^ (k + 1) * qint (q + q⁻¹) (k + 2)
        = ∑ j ∈ Finset.range (k + 2), q ^ (2 * j)) := by
    intro k
    induction k with
    | zero =>
      refine ⟨by simp, ?_⟩
      rw [qint_two]
      simp only [Finset.sum_range_succ, Finset.sum_range_zero]
      linear_combination hqq
    | succ k ih =>
      refine ⟨ih.2, ?_⟩
      obtain ⟨h1, h2⟩ := ih
      have hS : ∑ j ∈ Finset.range (k + 2), q ^ (2 * j)
          = ∑ j ∈ Finset.range (k + 1), q ^ (2 * j) + q ^ (2 * (k + 1)) :=
        Finset.sum_range_succ _ _
      rw [show k + 1 + 2 = (k + 1) + 2 from rfl, qint_add_two, Finset.sum_range_succ]
      simp only [show k + 1 + 1 = k + 2 from rfl]
      linear_combination (q ^ (k + 1) * qint (q + q⁻¹) (k + 2)) * hqq + (q ^ 2 + 1) * h2
        - q ^ 2 * h1 + q ^ 2 * hS
  exact (key k).1

include hq in
theorem qint_ne_zero_iff (k : ℕ) :
    qint (q + q⁻¹) (k + 1) ≠ 0 ↔ ∑ j ∈ Finset.range (k + 1), q ^ (2 * j) ≠ 0 := by
  rw [← pow_mul_qint q hq]
  exact ⟨fun h => mul_ne_zero (pow_ne_zero _ hq) h, fun h h0 => h (by rw [h0, mul_zero])⟩

/-- **The exact threshold, in `q`.** `rad = θ(ker π)` on `H_{n+1}` iff
`1 + q² + ⋯ + q^{2(k−1)} ≠ 0` for every `3 ≤ k ≤ n + 2`. -/
theorem rad_eq_tlKernel_iff_sum (hq21 : q ^ 2 + 1 ≠ 0) (n : ℕ) :
    (∀ x : Hecke K q q⁻¹ n, (∀ y, jimboTrace q hq n (x * y) = 0) ↔
        theta q hq n x ∈ tlKernelPulled hq n (δ := q + q⁻¹) (by field_simp)) ↔
      ∀ k, 3 ≤ k → k ≤ n + 2 → ∑ j ∈ Finset.range k, q ^ (2 * j) ≠ 0 := by
  rw [rad_eq_tlKernel_iff q hq hq21 n]
  refine forall_congr' fun k => imp_congr_right fun hk => imp_congr_right fun _ => ?_
  obtain ⟨m, rfl⟩ : ∃ m, k = m + 1 := ⟨k - 1, by omega⟩
  exact qint_ne_zero_iff q hq m

/-- **Cross-check against the three-strand file**: at `n = 2` the general threshold is
`[3] ≠ 0 ∧ [4] ≠ 0`, i.e. `q⁴ + q² + 1 ≠ 0 ∧ q⁴ + 1 ≠ 0`. -/
theorem rad_eq_tlKernel_iff_two (hq21 : q ^ 2 + 1 ≠ 0) :
    (∀ x : Hecke K q q⁻¹ 2, (∀ y, jimboTrace q hq 2 (x * y) = 0) ↔
        theta q hq 2 x ∈ tlKernelPulled hq 2 (δ := q + q⁻¹) (by field_simp)) ↔
      (q ^ 4 + q ^ 2 + 1 ≠ 0 ∧ q ^ 4 + 1 ≠ 0) := by
  rw [rad_eq_tlKernel_iff_sum q hq hq21 2]
  have h3 : ∑ j ∈ Finset.range 3, q ^ (2 * j) = q ^ 4 + q ^ 2 + 1 := by
    simp [Finset.sum_range_succ]; ring
  have h4 : ∑ j ∈ Finset.range 4, q ^ (2 * j) = (q ^ 2 + 1) * (q ^ 4 + 1) := by
    simp [Finset.sum_range_succ]; ring
  constructor
  · intro h
    refine ⟨h3 ▸ h 3 le_rfl (by norm_num), fun h0 => h 4 (by norm_num) le_rfl ?_⟩
    rw [h4, h0, mul_zero]
  · rintro ⟨a, b⟩ k hk3 hk4
    interval_cases k
    · rwa [h3]
    · rw [h4]; exact mul_ne_zero hq21 b

end QOU.IwahoriHecke.TLKernelThreshold
