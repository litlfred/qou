/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import BraidKnotOctonion.TLKernelRootOfUnity

/-!
# The exact threshold on three strands

On `H₃` (two generators), with `q ≠ 0` and `q² + 1 ≠ 0`, the radical of the Jimbo trace form
equals `θ(ker π)` **exactly when `(q⁴ + q² + 1)(q⁴ + 1) ≠ 0`**, i.e. when `[3]_q ≠ 0` and
`[4]_q ≠ 0` (`rad_eq_tlKernel_iff`).

## Method

* `TL₃(δ)` is spanned by `1, e₀, e₁, e₀e₁, e₁e₀` (`tl_mem_span`), for any `δ`.
* The Jimbo trace `τ` factors through `tlRep ∘ π ∘ θ`, and on those five words it takes the
  values `1, ε, ε, ε², ε²`, `ε = q/(q² + 1) = δ⁻¹` (the Jones trace of `e_i`).
* The Gram matrix of `τ` on the five words has entries in `{1, ε, ε²}` and determinant
  `(ε² − 1)⁴(2ε² − 1)`; both factors are nonzero iff `q⁴ + q² + 1 ≠ 0` and `q⁴ + 1 ≠ 0`.
  So under that hypothesis `x ∈ rad` forces `π(θ x) = 0` (`rad_le_tlKernel`).
* Conversely the element `w = [3] − δ(E₀ + E₁) + E₀E₁ + E₁E₀`, `E_i = q − σ_i`
  (`[3]` times the Jones–Wenzl projector), satisfies `ρ(w)ρ(y) = χ(y)ρ(w)`, has
  `τ(w) = (q⁴ + q² + 1)(q⁴ + 1)/(q²(q² + 1)²)`, and `ρ(w) ≠ 0` for every `q`
  (its `|001⟩,|100⟩` entry is `1`).  So when the product vanishes, `w` is in the radical
  and `θ w ∉ tlKernelPulled` (`exists_rad_not_tlKernel`).

Both failures are literature (Jones 1983; Goodman–de la Harpe–Jones): the Markov trace on
`TL` with `m` strands is nondegenerate iff `[k]_q ≠ 0` for `3 ≤ k ≤ m + 1`.  This file proves
`m = 3` by an explicit Gram determinant; every `m` is `TLKernelThreshold.rad_eq_tlKernel_iff`,
which re-derives this statement as `TLKernelThreshold.rad_eq_tlKernel_iff_two`.

-- Ref: [jones1983]; [wenzl1988]
-/

namespace QOU.IwahoriHecke.TLKernelThresholdThree

open QOU.SchurWeyl QOU.SchurWeyl.HeckeInclusion
open QOU.SchurWeyl.JimboActionKernel QOU.SchurWeyl.JimboKernelGeneric
open QOU.MathlibExt.TemperleyLieb QOU.MathlibExt.TemperleyLiebDimCatalan
open QOU.IwahoriHecke.TLCarrierBridge QOU.IwahoriHecke.TLKernelConvention
open QOU.IwahoriHecke.TLKernelEquality QOU.IwahoriHecke.TLKernelRootOfUnity
open QOU.MathlibExt.IwahoriHecke QOU.IwahoriHecke.TensorEmbed QOU.IwahoriHecke.RMatrix

variable {K : Type*} [Field K]

/-! ## `TL₃` is spanned by five words -/

section Span

variable (δ : K)

local notation "TL" => TLFin K δ 2
local notation "ee" => e K δ (adjFin (n := 2))

/-- The five words `1, e₀, e₁, e₀e₁, e₁e₀`. -/
noncomputable def tlw : Fin 5 → TL := ![1, ee 0, ee 1, ee 0 * ee 1, ee 1 * ee 0]

theorem e_sq' (i : Fin 2) : ee i * ee i = δ • ee i := by
  rw [e_sq_fin, Algebra.algebraMap_eq_smul_one, smul_mul_assoc, one_mul]

theorem e010 : ee 0 * ee 1 * ee 0 = ee 0 := e_adjacent_fin (Or.inl rfl)
theorem e101 : ee 1 * ee 0 * ee 1 = ee 1 := e_adjacent_fin (Or.inr rfl)

theorem e010' : ee 0 * (ee 1 * ee 0) = ee 0 := by rw [← mul_assoc, e010]
theorem e101' : ee 1 * (ee 0 * ee 1) = ee 1 := by rw [← mul_assoc, e101]

theorem tlw_mem (i : Fin 5) : tlw δ i ∈ Submodule.span K (Set.range (tlw δ)) :=
  Submodule.subset_span ⟨i, rfl⟩

theorem tlw_mul_e_mem (i : Fin 5) (j : Fin 2) :
    tlw δ i * ee j ∈ Submodule.span K (Set.range (tlw δ)) := by
  have m1 : ee 0 ∈ Submodule.span K (Set.range (tlw δ)) := tlw_mem δ 1
  have m2 : ee 1 ∈ Submodule.span K (Set.range (tlw δ)) := tlw_mem δ 2
  have m3 : ee 0 * ee 1 ∈ Submodule.span K (Set.range (tlw δ)) := tlw_mem δ 3
  have m4 : ee 1 * ee 0 ∈ Submodule.span K (Set.range (tlw δ)) := tlw_mem δ 4
  fin_cases i <;> fin_cases j
  · show (1 : TL) * ee 0 ∈ _; rw [one_mul]; exact m1
  · show (1 : TL) * ee 1 ∈ _; rw [one_mul]; exact m2
  · show ee 0 * ee 0 ∈ _; rw [e_sq']; exact Submodule.smul_mem _ _ m1
  · show ee 0 * ee 1 ∈ _; exact m3
  · show ee 1 * ee 0 ∈ _; exact m4
  · show ee 1 * ee 1 ∈ _; rw [e_sq']; exact Submodule.smul_mem _ _ m2
  · show ee 0 * ee 1 * ee 0 ∈ _; rw [e010]; exact m1
  · show ee 0 * ee 1 * ee 1 ∈ _; rw [mul_assoc, e_sq', mul_smul_comm]
    exact Submodule.smul_mem _ _ m3
  · show ee 1 * ee 0 * ee 0 ∈ _; rw [mul_assoc, e_sq', mul_smul_comm]
    exact Submodule.smul_mem _ _ m4
  · show ee 1 * ee 0 * ee 1 ∈ _; rw [e101]; exact m2

theorem tl_adjoin_eq_top : Algebra.adjoin K (Set.range ee) = ⊤ := by
  have h := congrArg (Subalgebra.map (RingQuot.mkAlgHom K (Rel K δ (adjFin (n := 2)))))
    (FreeAlgebra.adjoin_range_ι K (Fin 2))
  rw [AlgHom.map_adjoin, ← Set.range_comp, Algebra.map_top] at h
  rw [show ee = (RingQuot.mkAlgHom K (Rel K δ (adjFin (n := 2)))) ∘ FreeAlgebra.ι K from rfl, h,
    AlgHom.range_eq_top]
  exact RingQuot.mkAlgHom_surjective K _

/-- **Every element of `TL₃(δ)` is a combination of the five words.** -/
theorem tl_mem_span (t : TL) : t ∈ Submodule.span K (Set.range (tlw δ)) := by
  have key : ∀ M ∈ Submodule.span K (Set.range (tlw δ)),
      M * t ∈ Submodule.span K (Set.range (tlw δ)) := by
    have ht : t ∈ Algebra.adjoin K (Set.range ee) := by
      rw [tl_adjoin_eq_top]; exact Algebra.mem_top
    induction ht using Algebra.adjoin_induction with
    | mem y hy =>
      obtain ⟨j, rfl⟩ := hy
      intro M hM
      induction hM using Submodule.span_induction with
      | mem z hz => obtain ⟨i, rfl⟩ := hz; exact tlw_mul_e_mem δ i j
      | zero => simp
      | add a b _ _ ha hb => rw [add_mul]; exact Submodule.add_mem _ ha hb
      | smul r a _ ha => rw [smul_mul_assoc]; exact Submodule.smul_mem _ _ ha
    | algebraMap r =>
      intro M hM
      rw [Algebra.algebraMap_eq_smul_one, mul_smul_comm, mul_one]
      exact Submodule.smul_mem _ _ hM
    | add y z _ _ hy hz => intro M hM; rw [mul_add]; exact Submodule.add_mem _ (hy M hM) (hz M hM)
    | mul y z _ _ hy hz => intro M hM; rw [← mul_assoc]; exact hz _ (hy M hM)
  simpa using key 1 (tlw_mem δ 0)

end Span

/-! ## The Jimbo trace on `TL₃` -/

section Trace

variable (q : K) (hq : q ≠ 0)

local notation "TL" => TLFin K (q + q⁻¹) 2
local notation "ee" => e K (q + q⁻¹) (adjFin (n := 2))
local notation "Mat" => Matrix (Fin (2 + 1) → Fin 2) (Fin (2 + 1) → Fin 2) K

/-- `ε = q/(q² + 1) = δ⁻¹`, the Jones trace of `e_i`. -/
noncomputable def eps : K := q / (q ^ 2 + 1)

include hq in
theorem delta_mul_eps (hq21 : q ^ 2 + 1 ≠ 0) : (q + q⁻¹) * eps q = 1 := by
  rw [eps]; field_simp

include hq in
theorem eps_ne_zero (hq21 : q ^ 2 + 1 ≠ 0) : eps q ≠ 0 := div_ne_zero hq hq21

/-- The normalised weighted trace on matrices: `jimboTrace = Tm ∘ jimbo`. -/
noncomputable def Tm : Mat →ₗ[K] K := ((1 + q ^ 2) ^ (2 + 1))⁻¹ • qtrLin q (2 + 1)

theorem jimboTrace_eq_Tm (y : Hecke K q q⁻¹ 2) : jimboTrace q hq 2 y = Tm q (jimbo q hq 2 y) :=
  rfl

/-- `tlRep` at `n = 2`. -/
noncomputable def rep : TL →ₐ[K] Mat := tlRep (R := K) q q⁻¹ 2 (mul_inv_cancel₀ hq)

/-- `π ∘ θ`, the Temperley–Lieb quotient map `σ_i ↦ q − e_i`. -/
noncomputable def P : Hecke K q q⁻¹ 2 →ₐ[K] TL :=
  (skeinToTL hq 2 (δ := q + q⁻¹) (by field_simp)).comp (theta q hq 2)

theorem jimbo_eq_rep_P (y : Hecke K q q⁻¹ 2) : jimbo q hq 2 y = rep q hq (P q hq y) := by
  rw [jimbo_eq_tlRep_comp q hq 2]; rfl

theorem P_tlE (i : Fin 2) : P q hq (tlE q 2 i) = ee i := by
  simp only [P, AlgHom.comp_apply, tlE, map_sub, AlgHom.commutes]
  rw [skeinToTL_theta_σ hq 2 i, sub_sub_cancel]

/-- The trace functional on `TL₃`: `tv = Tm ∘ tlRep`. -/
noncomputable def tv : TL →ₗ[K] K := (Tm q).comp (rep q hq).toLinearMap

theorem tv_P (y : Hecke K q q⁻¹ 2) : tv q hq (P q hq y) = jimboTrace q hq 2 y := by
  rw [jimboTrace_eq_Tm, jimbo_eq_rep_P]; rfl

/-! Values of the Jimbo trace, by the Markov property. -/

theorem tlE_zero_eq_incl :
    tlE q 2 0 = heckeIncl K q q⁻¹ 1 (tlE q 1 (Fin.last 0)) := by
  rw [tlE, tlE, map_sub, AlgHom.commutes, heckeIncl_σ]; rfl

theorem tlE_one_eq : tlE q 2 1 = algebraMap K _ q - Hecke.σ K q q⁻¹ 2 (Fin.last 1) := rfl

include hq in
theorem jimboTrace_tlE (hq21 : q ^ 2 + 1 ≠ 0) :
    jimboTrace q hq 2 (tlE q 2 0) = eps q ∧ jimboTrace q hq 2 (tlE q 2 1) = eps q ∧
      jimboTrace q hq 2 (tlE q 2 0 * tlE q 2 1) = eps q * eps q ∧
      jimboTrace q hq 2 (tlE q 2 1 * tlE q 2 0) = eps q * eps q := by
  let T := jimboMarkov q hq hq21
  have hT : ∀ n x, jimboTrace q hq n x = T.tr n x := fun _ _ => rfl
  have hz : q - q ^ 3 / (q ^ 2 + 1) = eps q := by rw [eps]; field_simp; ring
  have hσ1 : T.tr 2 (Hecke.σ K q q⁻¹ 2 (Fin.last 1)) = q ^ 3 / (q ^ 2 + 1) := by
    have h := T.tr_markov 1 1
    rwa [map_one, one_mul, T.tr_one, mul_one] at h
  have halg : ∀ n, T.tr n (algebraMap K _ q) = q := fun n => by
    rw [Algebra.algebraMap_eq_smul_one, map_smul, T.tr_one, smul_eq_mul, mul_one]
  have hE1' : T.tr 1 (tlE q 1 (Fin.last 0)) = eps q := by
    rw [tlE, map_sub, halg, T.param_eq, hz]
  have hE0 : T.tr 2 (tlE q 2 0) = eps q := by rw [tlE_zero_eq_incl, T.tr_incl, hE1']
  have hE1 : T.tr 2 (tlE q 2 1) = eps q := by rw [tlE_one_eq, map_sub, halg, hσ1, hz]
  have hE01 : T.tr 2 (tlE q 2 0 * tlE q 2 1) = eps q * eps q := by
    rw [tlE_zero_eq_incl, tlE_one_eq, mul_sub, map_sub, T.tr_markov, Algebra.algebraMap_eq_smul_one,
      mul_smul_comm, mul_one, map_smul, T.tr_incl, hE1', smul_eq_mul, ← hz]
    ring
  refine ⟨hE0, hE1, hE01, ?_⟩
  rw [hT, T.tr_cyclic, ← hT]; exact hE01

/-! The rescaled words `f_i = ε e_i`, idempotent with polynomial-in-`ε` structure constants. -/

/-- `f_i = ε e_i`. -/
noncomputable def ff (i : Fin 2) : TL := eps q • ee i

include hq in
theorem ff_sq (hq21 : q ^ 2 + 1 ≠ 0) (i : Fin 2) : ff q i * ff q i = ff q i := by
  rw [ff, smul_mul_smul_comm, e_sq', smul_smul]
  congr 1
  linear_combination eps q * delta_mul_eps q hq hq21

theorem ff_010 : ff q 0 * ff q 1 * ff q 0 = (eps q * eps q) • ff q 0 := by
  rw [ff, ff, smul_mul_smul_comm, smul_mul_smul_comm, e010, smul_smul]

theorem ff_101 : ff q 1 * ff q 0 * ff q 1 = (eps q * eps q) • ff q 1 := by
  rw [ff, ff, smul_mul_smul_comm, smul_mul_smul_comm, e101, smul_smul]

include hq in
theorem ff_sq_mul (hq21 : q ^ 2 + 1 ≠ 0) (i : Fin 2) (X : TL) :
    ff q i * (ff q i * X) = ff q i * X := by rw [← mul_assoc, ff_sq q hq hq21]

theorem ff_010' : ff q 0 * (ff q 1 * ff q 0) = (eps q * eps q) • ff q 0 := by
  rw [← mul_assoc, ff_010]

theorem ff_101' : ff q 1 * (ff q 0 * ff q 1) = (eps q * eps q) • ff q 1 := by
  rw [← mul_assoc, ff_101]

theorem P_eps_tlE (i : Fin 2) : P q hq (eps q • tlE q 2 i) = ff q i := by
  rw [map_smul, P_tlE, ff]

include hq in
theorem tv_ff (hq21 : q ^ 2 + 1 ≠ 0) :
    tv q hq 1 = 1 ∧ tv q hq (ff q 0) = eps q ^ 2 ∧ tv q hq (ff q 1) = eps q ^ 2 ∧
      tv q hq (ff q 0 * ff q 1) = eps q ^ 4 ∧ tv q hq (ff q 1 * ff q 0) = eps q ^ 4 := by
  obtain ⟨h0, h1, h01, h10⟩ := jimboTrace_tlE q hq hq21
  have one : tv q hq 1 = 1 := by
    rw [← map_one (P q hq), tv_P]; exact (jimboMarkov q hq hq21).tr_one 2
  refine ⟨one, ?_, ?_, ?_, ?_⟩
  · rw [← P_eps_tlE q hq, tv_P, map_smul, h0, smul_eq_mul]; ring
  · rw [← P_eps_tlE q hq, tv_P, map_smul, h1, smul_eq_mul]; ring
  · rw [← P_eps_tlE q hq, ← P_eps_tlE q hq, ← map_mul, tv_P, smul_mul_smul_comm, map_smul, h01,
      smul_eq_mul]; ring
  · rw [← P_eps_tlE q hq, ← P_eps_tlE q hq, ← map_mul, tv_P, smul_mul_smul_comm, map_smul, h10,
      smul_eq_mul]; ring

/-- The rescaled five words. -/
noncomputable def flw : Fin 5 → TL := ![1, ff q 0, ff q 1, ff q 0 * ff q 1, ff q 1 * ff q 0]

include hq in
theorem tl_mem_span_flw (hq21 : q ^ 2 + 1 ≠ 0) (t : TL) :
    t ∈ Submodule.span K (Set.range (flw q)) := by
  have hε := eps_ne_zero q hq hq21
  have m : ∀ i, flw q i ∈ Submodule.span K (Set.range (flw q)) :=
    fun i => Submodule.subset_span ⟨i, rfl⟩
  have he : ∀ i : Fin 2, ee i = (eps q)⁻¹ • ff q i := fun i => by
    rw [ff, smul_smul, inv_mul_cancel₀ hε, one_smul]
  have key : Submodule.span K (Set.range (tlw (q + q⁻¹))) ≤
      Submodule.span K (Set.range (flw q)) := by
    rw [Submodule.span_le]
    rintro _ ⟨i, rfl⟩
    fin_cases i
    · exact m 0
    · show ee 0 ∈ _; rw [he]; exact Submodule.smul_mem _ _ (m 1)
    · show ee 1 ∈ _; rw [he]; exact Submodule.smul_mem _ _ (m 2)
    · show ee 0 * ee 1 ∈ _; rw [he, he, smul_mul_smul_comm]; exact Submodule.smul_mem _ _ (m 3)
    · show ee 1 * ee 0 ∈ _; rw [he, he, smul_mul_smul_comm]; exact Submodule.smul_mem _ _ (m 4)
  exact key (tl_mem_span _ t)

include hq in
/-- **The Gram matrix of the Jimbo trace on `TL₃` is nonsingular when
`(q⁴ + q² + 1)(q⁴ + 1) ≠ 0`.** -/
theorem eq_zero_of_tv (hq21 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0)
    (t : TL) (ht : ∀ s, tv q hq (t * s) = 0) : t = 0 := by
  obtain ⟨c, hc⟩ := (Submodule.mem_span_range_iff_exists_fun K).mp (tl_mem_span_flw q hq hq21 t)
  rw [Fin.sum_univ_five] at hc
  have ht' : t = c 0 • 1 + c 1 • ff q 0 + c 2 • ff q 1 + c 3 • (ff q 0 * ff q 1)
      + c 4 • (ff q 1 * ff q 0) := hc.symm
  obtain ⟨v1, v2, v3, v4, v5⟩ := tv_ff q hq hq21
  have e0 := ht 1
  have e1 := ht (ff q 0)
  have e2 := ht (ff q 1)
  have e3 := ht (ff q 0 * ff q 1)
  have e4 := ht (ff q 1 * ff q 0)
  rw [ht'] at e0 e1 e2 e3 e4
  simp only [add_mul, smul_mul_assoc, mul_smul_comm, smul_smul, one_mul, mul_one, mul_assoc, ff_sq q hq hq21,
    ff_sq_mul q hq hq21, ff_010', ff_101', map_add, map_smul,
    smul_eq_mul, v1, v2, v3, v4, v5] at e0 e1 e2 e3 e4
  set ε := eps q with hε
  have hε0 : ε ≠ 0 := eps_ne_zero q hq hq21
  have hA : ε ^ 2 - 1 ≠ 0 := by
    have : ε ^ 2 - 1 = -(q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 := by
      rw [hε, eps]; field_simp; ring
    rw [this]; exact div_ne_zero (neg_ne_zero.mpr h3) (pow_ne_zero _ hq21)
  have hB : 2 * ε ^ 2 - 1 ≠ 0 := by
    have : 2 * ε ^ 2 - 1 = -(q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 := by
      rw [hε, eps]; field_simp; ring
    rw [this]; exact div_ne_zero (neg_ne_zero.mpr h4) (pow_ne_zero _ hq21)
  have hD : ε ^ 4 * (ε ^ 2 - 1) * (2 * ε ^ 2 - 1) ≠ 0 :=
    mul_ne_zero (mul_ne_zero (pow_ne_zero _ hε0) hA) hB
  have c0 : c 0 = 0 := by
    have : c 0 * (ε ^ 4 * (ε ^ 2 - 1) * (2 * ε ^ 2 - 1)) = 0 := by
      linear_combination (-ε ^ 4 * (ε ^ 2 - 1)) * e0 - ε ^ 4 * e1 - ε ^ 4 * e2 + ε ^ 4 * e3
        + ε ^ 4 * e4
    exact (mul_eq_zero.mp this).resolve_right hD
  have c1 : c 1 = 0 := by
    have : c 1 * (ε ^ 4 * (ε ^ 2 - 1) * (2 * ε ^ 2 - 1)) = 0 := by
      linear_combination (-ε ^ 4) * e0 + ε ^ 2 * e1 + 2 * ε ^ 4 * e2 - ε ^ 2 * e3 - ε ^ 2 * e4
    exact (mul_eq_zero.mp this).resolve_right hD
  have c2 : c 2 = 0 := by
    have : c 2 * (ε ^ 4 * (ε ^ 2 - 1) * (2 * ε ^ 2 - 1)) = 0 := by
      linear_combination (-ε ^ 4) * e0 + 2 * ε ^ 4 * e1 + ε ^ 2 * e2 - ε ^ 2 * e3 - ε ^ 2 * e4
    exact (mul_eq_zero.mp this).resolve_right hD
  have c3 : c 3 = 0 := by
    have : c 3 * (ε ^ 4 * (ε ^ 2 - 1) * (2 * ε ^ 2 - 1)) = 0 := by
      linear_combination ε ^ 4 * e0 - ε ^ 2 * e1 - ε ^ 2 * e2 + ε ^ 2 * e3 - (ε ^ 2 - 1) * e4
    exact (mul_eq_zero.mp this).resolve_right hD
  have c4 : c 4 = 0 := by
    have : c 4 * (ε ^ 4 * (ε ^ 2 - 1) * (2 * ε ^ 2 - 1)) = 0 := by
      linear_combination ε ^ 4 * e0 - ε ^ 2 * e1 - ε ^ 2 * e2 - (ε ^ 2 - 1) * e3 + ε ^ 2 * e4
    exact (mul_eq_zero.mp this).resolve_right hD
  rw [ht', c0, c1, c2, c3, c4]
  simp

end Trace

/-! ## Both inclusions and the witness -/

section Threshold

variable (q : K) (hq : q ≠ 0)

local notation "TL" => TLFin K (q + q⁻¹) 2
local notation "ee" => e K (q + q⁻¹) (adjFin (n := 2))

theorem mem_tlKernelPulled_iff_P (x : Hecke K q q⁻¹ 2) :
    theta q hq 2 x ∈ tlKernelPulled hq 2 (δ := q + q⁻¹) (by field_simp) ↔ P q hq x = 0 := by
  rw [tlKernelPulled, TwoSidedIdeal.mem_ker]; rfl

/-- **`θ(ker π) ⊆ rad`, for every `q ≠ 0`.** -/
theorem rad_of_tlKernel (x : Hecke K q q⁻¹ 2) (hx : P q hq x = 0) (y : Hecke K q q⁻¹ 2) :
    jimboTrace q hq 2 (x * y) = 0 := by
  rw [← tv_P, map_mul, hx, zero_mul, map_zero]

include hq in
/-- **`rad ⊆ θ(ker π)` when `(q⁴ + q² + 1)(q⁴ + 1) ≠ 0`.** -/
theorem tlKernel_of_rad (hq21 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0)
    (x : Hecke K q q⁻¹ 2) (hx : ∀ y, jimboTrace q hq 2 (x * y) = 0) : P q hq x = 0 := by
  apply eq_zero_of_tv q hq hq21 h3 h4
  intro s
  have hs : s ∈ Submodule.span K (Set.range (flw q)) := tl_mem_span_flw q hq hq21 s
  induction hs using Submodule.span_induction with
  | mem z hz =>
    obtain ⟨i, rfl⟩ := hz
    have hpre : ∀ i, ∃ y, P q hq y = flw q i := by
      intro i
      fin_cases i
      · exact ⟨1, map_one _⟩
      · exact ⟨eps q • tlE q 2 0, P_eps_tlE q hq 0⟩
      · exact ⟨eps q • tlE q 2 1, P_eps_tlE q hq 1⟩
      · exact ⟨(eps q • tlE q 2 0) * (eps q • tlE q 2 1), by
          rw [map_mul, P_eps_tlE, P_eps_tlE]; rfl⟩
      · exact ⟨(eps q • tlE q 2 1) * (eps q • tlE q 2 0), by
          rw [map_mul, P_eps_tlE, P_eps_tlE]; rfl⟩
    obtain ⟨y, hy⟩ := hpre i
    rw [← hy, ← map_mul, tv_P, hx]
  | zero => rw [mul_zero, map_zero]
  | add a b _ _ ha hb => rw [mul_add, map_add, ha, hb, add_zero]
  | smul r a _ ha => rw [mul_smul_comm, map_smul, ha, smul_zero]

/-- The witness `w = [3] − δ(E₀ + E₁) + E₀E₁ + E₁E₀` (`[3]` times the Jones–Wenzl
projector), with `[3] = q² + 1 + q⁻²`, `δ = q + q⁻¹`, `E_i = q − σ_i`. -/
noncomputable def jw : Hecke K q q⁻¹ 2 :=
  (q ^ 2 + 1 + q⁻¹ ^ 2) • 1 - (q + q⁻¹) • (tlE q 2 0 + tlE q 2 1) + tlE q 2 0 * tlE q 2 1
    + tlE q 2 1 * tlE q 2 0

/-- Its image in `TL₃`. -/
noncomputable def jwT : TL :=
  (q ^ 2 + 1 + q⁻¹ ^ 2) • 1 - (q + q⁻¹) • (ee 0 + ee 1) + ee 0 * ee 1 + ee 1 * ee 0

theorem P_jw : P q hq (jw q) = jwT q := by
  rw [jw, jwT, map_add, map_add, map_sub, map_smul, map_smul, map_one, map_add, map_mul, map_mul,
    P_tlE, P_tlE]

include hq in
theorem jwT_mul_e (i : Fin 2) : jwT q * ee i = 0 := by
  fin_cases i <;>
  · simp only [jwT, add_mul, sub_mul, smul_mul_assoc, one_mul, mul_assoc, e_sq', e010', e101',
      mul_smul_comm, smul_add, smul_smul, Fin.zero_eta, Fin.mk_one]
    match_scalars <;> field_simp <;> ring

include hq in
theorem jwT_mul (t : TL) : ∃ c : K, jwT q * t = c • jwT q := by
  have ht : t ∈ Algebra.adjoin K (Set.range ee) := by
    rw [tl_adjoin_eq_top]; exact Algebra.mem_top
  induction ht using Algebra.adjoin_induction with
  | mem y hy => obtain ⟨i, rfl⟩ := hy; exact ⟨0, by rw [jwT_mul_e q hq, zero_smul]⟩
  | algebraMap r =>
    exact ⟨r, by rw [Algebra.algebraMap_eq_smul_one, mul_smul_comm, mul_one]⟩
  | add y z _ _ hy hz =>
    obtain ⟨a, ha⟩ := hy; obtain ⟨b, hb⟩ := hz
    exact ⟨a + b, by rw [mul_add, ha, hb, add_smul]⟩
  | mul y z _ _ hy hz =>
    obtain ⟨a, ha⟩ := hy; obtain ⟨b, hb⟩ := hz
    exact ⟨a * b, by rw [← mul_assoc, ha, smul_mul_assoc, hb, smul_smul]⟩

include hq in
theorem jimboTrace_jw (hq21 : q ^ 2 + 1 ≠ 0) :
    jimboTrace q hq 2 (jw q) = (q ^ 4 + q ^ 2 + 1) * (q ^ 4 + 1) / (q ^ 2 * (q ^ 2 + 1) ^ 2) := by
  obtain ⟨h0, h1, h01, h10⟩ := jimboTrace_tlE q hq hq21
  have h1' : jimboTrace q hq 2 1 = 1 := (jimboMarkov q hq hq21).tr_one 2
  rw [jw, map_add, map_add, map_sub, map_smul, map_smul, map_add, h0, h1, h01, h10]
  simp only [smul_eq_mul, h1', eps]
  field_simp
  ring

/-- **`ρ(w) ≠ 0` for every `q ≠ 0`**: its `|001⟩,|100⟩` entry is `1`. -/
theorem jimbo_jw_apply : jimbo q hq 2 (jw q) ![0, 0, 1] ![1, 0, 0] = 1 := by
  simp only [jw, tlE, map_add, map_sub, map_smul, map_mul, map_one, jimbo_σ,
    Algebra.algebraMap_eq_smul_one]
  simp [Matrix.mul_apply, sum_states, strandBraid, braidAt, embedPair_apply, rCheck_apply,
    Fin.sum_univ_two, Matrix.one_apply, Fin.forall_fin_succ]

include hq in
theorem P_jw_ne_zero : P q hq (jw q) ≠ 0 := by
  intro h
  have h1 := jimbo_jw_apply q hq
  rw [jimbo_eq_rep_P, h, map_zero, Matrix.zero_apply] at h1
  exact zero_ne_one h1

include hq in
/-- **When `(q⁴ + q² + 1)(q⁴ + 1) = 0` the radical is strictly larger**: `w` lies in it but
`θ w ∉ tlKernelPulled`. -/
theorem exists_rad_not_tlKernel (hq21 : q ^ 2 + 1 ≠ 0)
    (h : (q ^ 4 + q ^ 2 + 1) * (q ^ 4 + 1) = 0) :
    (∀ y, jimboTrace q hq 2 (jw q * y) = 0) ∧
      theta q hq 2 (jw q) ∉ tlKernelPulled hq 2 (δ := q + q⁻¹) (by field_simp) := by
  refine ⟨fun y => ?_, fun hx => P_jw_ne_zero q hq ((mem_tlKernelPulled_iff_P q hq _).mp hx)⟩
  obtain ⟨c, hc⟩ := jwT_mul q hq (P q hq y)
  rw [← tv_P q hq, map_mul, P_jw, hc, map_smul, ← P_jw q hq, tv_P q hq, jimboTrace_jw q hq hq21, h, zero_div,
    smul_zero]

include hq in
/-- **The exact threshold on three strands.**  For `q ≠ 0`, `q² + 1 ≠ 0`: the radical of
the Jimbo trace form on `H₃` equals `θ(ker π)` iff `q⁴ + q² + 1 ≠ 0` and `q⁴ + 1 ≠ 0`,
i.e. iff `[3]_q ≠ 0` and `[4]_q ≠ 0`. -/
theorem rad_eq_tlKernel_iff (hq21 : q ^ 2 + 1 ≠ 0) :
    (∀ x : Hecke K q q⁻¹ 2, (∀ y, jimboTrace q hq 2 (x * y) = 0) ↔
        theta q hq 2 x ∈ tlKernelPulled hq 2 (δ := q + q⁻¹) (by field_simp)) ↔
      (q ^ 4 + q ^ 2 + 1 ≠ 0 ∧ q ^ 4 + 1 ≠ 0) := by
  constructor
  · intro hall
    by_contra hne
    have h : (q ^ 4 + q ^ 2 + 1) * (q ^ 4 + 1) = 0 := by
      rcases not_and_or.mp hne with h | h <;> simp only [not_not] at h <;> simp [h]
    obtain ⟨hr, hn⟩ := exists_rad_not_tlKernel q hq hq21 h
    exact hn ((hall _).mp hr)
  · rintro ⟨h3, h4⟩ x
    rw [mem_tlKernelPulled_iff_P]
    exact ⟨tlKernel_of_rad q hq hq21 h3 h4 x, rad_of_tlKernel q hq x⟩

end Threshold

end QOU.IwahoriHecke.TLKernelThresholdThree
