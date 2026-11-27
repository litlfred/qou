/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import BraidKnotOctonion.TLKernelEquality

/-!
# The Hecke radical and the Temperley–Lieb kernel at a root of unity

For generic `q`, `TLKernelEquality.mem_tlKernelPulled_iff` identifies the kernel of the
Temperley–Lieb quotient `π ∘ θ : H → TL` (`σ_i ↦ q − e_i`) with the radical of the
Ocneanu trace form.  This file shows that the identification **fails** at the first root of
unity, on three strands.

Let `q⁴ + q² + 1 = 0`, i.e. `q²` is a primitive cube root of unity, `[3]_q = 0`, `δ² = 1`.
The Ocneanu trace `wtrace` is not available there (its seminormal entries have `q^{2d} − 1`
denominators), but the Jimbo trace `jimboTrace` (the normalised quantum trace on
`V^{⊗3}`, `K = diag(1, q²)`) is defined for every `q ≠ 0` with `q² + 1 ≠ 0`, and agrees with
`wtrace` wherever both are defined (`jimboTrace_eq_wtrace`).

## The witness

Put `a_i = σ_i + q⁻¹`.  The quadratic relation gives `a_i σ_i = σ_i a_i = q a_i`, and the
braid relation is equivalent to `a₀a₁a₀ − a₀ = a₁a₀a₁ − a₁` (`a_braid`).  Call this element
`x` (`symm3`, the unnormalised `q`-symmetriser).  Then

* `x σ_i = q x` for both generators, hence `x y = χ(y) x` for every `y`, where `χ` is the
  character `σ_i ↦ q` (`symm3_mul`);
* `jimboTrace(x) = 0` when `q⁴ + q² + 1 = 0` (`jimboTrace_symm3`): by the Markov property
  `tr(a₀) = z + q⁻¹ = (q⁴ + q² + 1) / (q (q² + 1))` with `z = q³/(q²+1)`;
* so `x` is in the radical of the Jimbo trace form (`symm3_mem_rad`);
* but `ρ(x) ≠ 0`: its entry from `|100⟩` to `|001⟩` is `(q² + 1)/q` (`jimbo_symm3_ne_zero`);
* hence `π(θ x) ≠ 0` in `TL₃(δ)`, because `ρ = tlRep ∘ π ∘ θ` holds for every `q ≠ 0`
  (`jimbo_eq_tlRep_comp`).  Its image is the unnormalised Jones–Wenzl element
  `−e₀ − e₁ + e₀e₁ + e₁e₀` (at `δ = 1`).

The headline is `not_rad_le_tlKernel_rootOfUnity`.

## Scope

Only the first failure (`n = 2` generators, `q²` a primitive cube root of unity) is proved.
The general threshold (failure exactly when `[k]_q = 0` for some `2 ≤ k ≤ n + 1`) and the
identification of `H/rad` with the semisimple quotient of `TL` (Jones 1983; Goodman–de la
Harpe–Jones; Wenzl 1988) are not formalised here.

-- Ref: [jones1983]; [wenzl1988]
-/

namespace QOU.IwahoriHecke.TLKernelRootOfUnity

open QOU.SchurWeyl QOU.SchurWeyl.HeckeInclusion
open QOU.SchurWeyl.JimboActionKernel QOU.SchurWeyl.JimboKernelGeneric
open QOU.MathlibExt.TemperleyLieb QOU.MathlibExt.TemperleyLiebDimCatalan
open QOU.IwahoriHecke.TensorEmbed QOU.IwahoriHecke.RMatrix
open QOU.IwahoriHecke.TLCarrierBridge QOU.IwahoriHecke.TLKernelConvention
open QOU.MathlibExt.IwahoriHecke QOU.IwahoriHecke.TLKernelEquality

variable {K : Type*} [Field K]

section Algebra

variable (q : K) (hq : q ≠ 0)

local notation "H" => Hecke K q q⁻¹ 2

/-- `a_i = σ_i + q⁻¹`, the `q`-eigen-idempotent of `σ_i` up to scale. -/
noncomputable def a (i : Fin 2) : H := Hecke.σ K q q⁻¹ 2 i + q⁻¹ • 1

include hq in
theorem a_mul_σ (i : Fin 2) : a q i * Hecke.σ K q q⁻¹ 2 i = q • a q i := by
  have h := Hecke.σ_quadratic_qou K q q⁻¹ 2 (mul_inv_cancel₀ hq) i
  rw [a, add_mul, h, smul_mul_assoc, one_mul, smul_add, smul_smul, mul_inv_cancel₀ hq,
    one_smul]
  module

include hq in
theorem σ_mul_a (i : Fin 2) : Hecke.σ K q q⁻¹ 2 i * a q i = q • a q i := by
  have h := Hecke.σ_quadratic_qou K q q⁻¹ 2 (mul_inv_cancel₀ hq) i
  rw [a, mul_add, h, mul_smul_comm, mul_one, smul_add, smul_smul, mul_inv_cancel₀ hq,
    one_smul]
  module

include hq in
/-- The braid relation, rewritten in the `a_i`: `a₀a₁a₀ − a₀ = a₁a₀a₁ − a₁`. -/
theorem a_braid : a q 0 * a q 1 * a q 0 - a q 0 = a q 1 * a q 0 * a q 1 - a q 1 := by
  have hb := Hecke.σ_braid K q q⁻¹ 2 0 (by norm_num)
  have h0 := Hecke.σ_quadratic_qou K q q⁻¹ 2 (mul_inv_cancel₀ hq) 0
  have h1 := Hecke.σ_quadratic_qou K q q⁻¹ 2 (mul_inv_cancel₀ hq) 1
  have hb' : Hecke.σ K q q⁻¹ 2 0 * (Hecke.σ K q q⁻¹ 2 1 * Hecke.σ K q q⁻¹ 2 0)
      = Hecke.σ K q q⁻¹ 2 1 * (Hecke.σ K q q⁻¹ 2 0 * Hecke.σ K q q⁻¹ 2 1) := by
    simpa only [mul_assoc] using hb
  simp only [a, add_mul, mul_add, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, smul_smul,
    smul_add, mul_assoc]
  rw [hb', h0, h1]
  match_scalars <;> field_simp <;> ring

/-- `x = a₀a₁a₀ − a₀`, the unnormalised `q`-symmetriser of `H₃`. -/
noncomputable def symm3 : H := a q 0 * a q 1 * a q 0 - a q 0

include hq in
theorem symm3_mul_σ (i : Fin 2) : symm3 q * Hecke.σ K q q⁻¹ 2 i = q • symm3 q := by
  fin_cases i
  · show (a q 0 * a q 1 * a q 0 - a q 0) * Hecke.σ K q q⁻¹ 2 0 = _
    rw [sub_mul, mul_assoc (a q 0 * a q 1), a_mul_σ q hq, mul_smul_comm, symm3, smul_sub]
  · show (a q 0 * a q 1 * a q 0 - a q 0) * Hecke.σ K q q⁻¹ 2 1 = _
    rw [a_braid q hq, sub_mul, mul_assoc (a q 1 * a q 0), a_mul_σ q hq,
      mul_smul_comm, symm3, a_braid q hq, smul_sub]

/-- The character `σ_i ↦ q` of `H` (the trivial, one-row representation). -/
noncomputable def chi : H →ₐ[K] K :=
  Hecke.lift K q q⁻¹ 2 (fun _ => q)
    (fun _ => by
      simp only [smul_eq_mul, mul_one, sub_mul, inv_mul_cancel₀ hq, mul_inv_cancel₀ hq]
      ring)
    (fun _ _ => rfl) (fun _ _ _ => mul_comm _ _)

@[simp] theorem chi_σ (i : Fin 2) : chi q hq (Hecke.σ K q q⁻¹ 2 i) = q :=
  Hecke.lift_σ K q q⁻¹ 2 _ _ _ _ i

/-- **`x y = χ(y) x` for every `y`**: the symmetriser spans a one-dimensional right ideal. -/
theorem symm3_mul (y : H) : symm3 q * y = chi q hq y • symm3 q := by
  have hy : y ∈ Algebra.adjoin K (Set.range (Hecke.σ K q q⁻¹ 2)) := by
    rw [HeckeInclusion.adjoin_range_σ_eq_top]; exact Algebra.mem_top
  induction hy using Algebra.adjoin_induction with
  | mem y hy =>
    obtain ⟨i, rfl⟩ := hy
    rw [chi_σ, symm3_mul_σ q hq]
  | algebraMap r =>
    rw [AlgHom.commutes, Algebra.algebraMap_self, RingHom.id_apply,
      Algebra.algebraMap_eq_smul_one, mul_smul_comm, mul_one]
  | add y z _ _ hy hz => rw [mul_add, hy, hz, map_add, add_smul]
  | mul y z _ _ hy hz => rw [← mul_assoc, hy, smul_mul_assoc, hz, smul_smul, map_mul]

end Algebra

section Trace

variable (q : K) (hq : q ≠ 0)

/-- `q⁴ + q² + 1 = 0` forces `q² + 1 ≠ 0`. -/
theorem sq_add_one_ne_zero (hω : q ^ 4 + q ^ 2 + 1 = 0) : q ^ 2 + 1 ≠ 0 := by
  intro h
  have : q ^ 2 = -1 := by linear_combination h
  have h1 : q ^ 4 = 1 := by rw [show q ^ 4 = (q ^ 2) ^ 2 by ring, this]; ring
  rw [h1, this] at hω
  norm_num at hω

/-- `a₀` comes from the one-generator algebra. -/
theorem a_zero_eq_incl :
    a q 0 = heckeIncl K q q⁻¹ 1 (Hecke.σ K q q⁻¹ 1 (Fin.last 0) + q⁻¹ • 1) := by
  rw [map_add, map_smul, map_one, heckeIncl_σ]
  rfl

theorem a_one_eq : a q 1 = Hecke.σ K q q⁻¹ 2 (Fin.last 1) + q⁻¹ • 1 := rfl

include hq in
theorem a_mul_self (i : Fin 2) : a q i * a q i = (q + q⁻¹) • a q i := by
  conv_lhs => rw [show a q i = Hecke.σ K q q⁻¹ 2 i + q⁻¹ • 1 from rfl, mul_add]
  rw [← a, a_mul_σ q hq, mul_smul_comm, mul_one, add_smul]

include hq in
/-- **The Jimbo trace of the symmetriser vanishes at `q⁴ + q² + 1 = 0`.**  By the Markov
property, `tr(a₀) = z + q⁻¹ = (q⁴ + q² + 1)/(q(q² + 1))`, and every term of `tr(x)` carries
this factor. -/
theorem jimboTrace_symm3 (hω : q ^ 4 + q ^ 2 + 1 = 0) : jimboTrace q hq 2 (symm3 q) = 0 := by
  have hq21 := sq_add_one_ne_zero q hω
  let T := jimboMarkov q hq hq21
  have hT : ∀ n x, jimboTrace q hq n x = T.tr n x := fun _ _ => rfl
  set b : Hecke K q q⁻¹ 1 := Hecke.σ K q q⁻¹ 1 (Fin.last 0) + q⁻¹ • 1 with hb
  have hb0 : T.tr 1 b = 0 := by
    rw [hb, map_add, map_smul, T.param_eq, T.tr_one, smul_eq_mul, mul_one]
    field_simp
    linear_combination hω
  have ha0 : T.tr 2 (a q 0) = 0 := by rw [a_zero_eq_incl, ← hb, T.tr_incl, hb0]
  have ha01 : T.tr 2 (a q 0 * a q 1) = 0 := by
    rw [a_zero_eq_incl, ← hb, a_one_eq, mul_add, map_add, T.tr_markov, mul_smul_comm, mul_one,
      map_smul, T.tr_incl, hb0, mul_zero, smul_zero, add_zero]
  rw [hT, symm3, map_sub, T.tr_cyclic, ← mul_assoc, a_mul_self q hq, smul_mul_assoc, map_smul,
    ha01, ha0, smul_zero, sub_zero]

include hq in
/-- **The symmetriser lies in the radical of the Jimbo trace form at `q⁴ + q² + 1 = 0`.** -/
theorem symm3_mem_rad (hω : q ^ 4 + q ^ 2 + 1 = 0) (y : Hecke K q q⁻¹ 2) :
    jimboTrace q hq 2 (symm3 q * y) = 0 := by
  rw [symm3_mul q hq, map_smul, jimboTrace_symm3 q hq hω, smul_zero]

end Trace

section Matrix

variable (q : K) (hq : q ≠ 0)

/-- A sum over the basis states of `V^{⊗3}`, written out site by site. -/
theorem sum_states (f : (Fin 3 → Fin 2) → K) :
    ∑ c, f c = ∑ i : Fin 2, ∑ j : Fin 2, ∑ k : Fin 2, f ![i, j, k] := by
  rw [← (Fin.consEquiv fun _ : Fin 3 => Fin 2).sum_comp, Fintype.sum_prod_type]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [← (Fin.consEquiv fun _ : Fin 2 => Fin 2).sum_comp, Fintype.sum_prod_type]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [← (Fin.consEquiv fun _ : Fin 1 => Fin 2).sum_comp, Fintype.sum_prod_type]
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [Fintype.sum_unique]
  congr 1

theorem jimbo_a (i : Fin 2) :
    jimbo q hq 2 (a q i) = strandBraid q q⁻¹ i + q⁻¹ • 1 := by
  rw [a, map_add, map_smul, map_one, jimbo_σ]

/-- **The entry of `ρ(x)` from `|100⟩` to `|001⟩` is `q + q⁻¹`.** -/
theorem jimbo_symm3_apply :
    jimbo q hq 2 (symm3 q) ![0, 0, 1] ![1, 0, 0] = q + q⁻¹ := by
  rw [symm3, map_sub, map_mul, map_mul, jimbo_a, jimbo_a]
  simp [Matrix.mul_apply, sum_states, strandBraid, braidAt, embedPair_apply, rCheck_apply,
    Fin.sum_univ_two, Matrix.one_apply, Fin.forall_fin_succ]

include hq in
theorem jimbo_symm3_ne_zero (hω : q ^ 4 + q ^ 2 + 1 = 0) : jimbo q hq 2 (symm3 q) ≠ 0 := by
  intro h
  have h1 := jimbo_symm3_apply q hq
  rw [h, Matrix.zero_apply] at h1
  have h2 : q ^ 2 + 1 = 0 := by
    field_simp at h1
    linear_combination -h1
  exact sq_add_one_ne_zero q hω h2

end Matrix

section TL

variable (q : K) (hq : q ≠ 0)

/-- **The Jimbo action factors through `π ∘ θ` for every `q ≠ 0`**, roots of unity
included: `ρ = tlRep ∘ π ∘ θ`.  (`JimboKernelGeneric.jimbo_eq_comp` is the same statement
through `H/rad ≃ TL`, which needs `q` generic.) -/
theorem jimbo_eq_tlRep_comp (m : ℕ) :
    jimbo q hq m
      = (tlRep (R := K) q q⁻¹ m (mul_inv_cancel₀ hq)).comp
          ((skeinToTL hq m (δ := q + q⁻¹) (by field_simp)).comp (theta q hq m)) := by
  apply Hecke.hom_ext
  intro i
  rw [AlgHom.comp_apply, AlgHom.comp_apply, skeinToTL_theta_σ, map_sub, AlgHom.commutes,
    ← jimbo_tlE hq m i, tlE, map_sub, AlgHom.commutes, sub_sub_cancel]

/-- **At the first root of unity the Hecke radical is strictly larger than the
Temperley–Lieb kernel.**  Let `q⁴ + q² + 1 = 0` (`q²` a primitive cube root of unity).  The
symmetriser `x = a₀a₁a₀ − a₀ ∈ H₃` lies in the radical of the Jimbo trace form, yet
`π(θ x) ≠ 0` in `TL₃(q + q⁻¹)`, i.e. `θ x ∉ tlKernelPulled`.  For generic `q` these two
conditions are equivalent (`TLKernelEquality.theta_mem_tlKernelPulled_iff`). -/
theorem not_rad_le_tlKernel_rootOfUnity (hω : q ^ 4 + q ^ 2 + 1 = 0) :
    ∃ x : Hecke K q q⁻¹ 2, (∀ y, jimboTrace q hq 2 (x * y) = 0) ∧ jimbo q hq 2 x ≠ 0 ∧
      theta q hq 2 x ∉ tlKernelPulled hq 2 (δ := q + q⁻¹) (by field_simp) := by
  refine ⟨symm3 q, symm3_mem_rad q hq hω, jimbo_symm3_ne_zero q hq hω, fun hx => ?_⟩
  apply jimbo_symm3_ne_zero q hq hω
  rw [tlKernelPulled, TwoSidedIdeal.mem_ker] at hx
  rw [jimbo_eq_tlRep_comp q hq 2, AlgHom.comp_apply, AlgHom.comp_apply]
  exact (congrArg _ hx).trans (map_zero _)

end TL

end QOU.IwahoriHecke.TLKernelRootOfUnity
