/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import BraidKnotOctonion.TLKernelRootOfUnity

/-!
# The weight of the isospin-3/2 block under the Jimbo trace

On `H₃` the q-symmetriser `x = a₀a₁a₀ − a₀` (`a_i = σ_i + q⁻¹`,
`TLKernelRootOfUnity.symm3`) spans the trivial (one-row, `(3)`) block: `x y = y x = χ(y) x`
for the character `χ : σ_i ↦ q`. When `[3]_q ≠ 0`, `p₃ = x / χ(x)` is the central
idempotent of that block, and the Jimbo (convention-D Ocneanu) trace gives

  `τ(p₃) = (q⁴ + 1)/(q² + 1)²`   (`jimboTrace_p3`).

This is the convention-D value of `y₃`, the weight that the Q_β reduction
(`QBetaChiralityReduction`, audit 2026-11-20 §10) reads off a functional's isospin-3/2
block. The audit measured it with a Python probe over `ℚ(q)`; this file proves it over any
field. It equals `1/2` at `q = 1`.

No measured value enters this file. The comparison with the y₃ the CODATA Q_β would
need lives in the audit and bean, not here.

-- Ref: [jimbo1986]; [wenzl1988]
-/

namespace QOU.IwahoriHecke.HeckeTrivialBlockWeight

open QOU.SchurWeyl QOU.SchurWeyl.HeckeInclusion
open QOU.SchurWeyl.JimboActionKernel
open QOU.IwahoriHecke.TLKernelRootOfUnity

variable {K : Type*} [Field K] (q : K) (hq : q ≠ 0)

local notation "H" => Hecke K q q⁻¹ 2

include hq in
theorem σ_mul_symm3 (i : Fin 2) : Hecke.σ K q q⁻¹ 2 i * symm3 q = q • symm3 q := by
  fin_cases i
  · show Hecke.σ K q q⁻¹ 2 0 * (a q 0 * a q 1 * a q 0 - a q 0) = _
    rw [mul_sub, ← mul_assoc, ← mul_assoc, σ_mul_a q hq, smul_mul_assoc, smul_mul_assoc,
      symm3, smul_sub]
  · show Hecke.σ K q q⁻¹ 2 1 * (a q 0 * a q 1 * a q 0 - a q 0) = _
    rw [a_braid q hq, mul_sub, ← mul_assoc, ← mul_assoc, σ_mul_a q hq, smul_mul_assoc,
      smul_mul_assoc, symm3, a_braid q hq, smul_sub]

/-- **`y x = χ(y) x`**: together with `symm3_mul`, `x` spans a two-sided ideal on which `H`
acts by the character `χ`. -/
theorem mul_symm3 (y : H) : y * symm3 q = chi q hq y • symm3 q := by
  have hy : y ∈ Algebra.adjoin K (Set.range (Hecke.σ K q q⁻¹ 2)) := by
    rw [HeckeInclusion.adjoin_range_σ_eq_top]; exact Algebra.mem_top
  induction hy using Algebra.adjoin_induction with
  | mem y hy =>
    obtain ⟨i, rfl⟩ := hy
    rw [chi_σ, σ_mul_symm3 q hq]
  | algebraMap r =>
    rw [AlgHom.commutes, Algebra.algebraMap_self, RingHom.id_apply,
      Algebra.algebraMap_eq_smul_one, smul_mul_assoc, one_mul]
  | add y z _ _ hy hz => rw [add_mul, hy, hz, map_add, add_smul]
  | mul y z _ _ hy hz => rw [mul_assoc, hz, mul_smul_comm, hy, smul_smul, map_mul, mul_comm]

theorem chi_a (i : Fin 2) : chi q hq (a q i) = q + q⁻¹ := by
  rw [a, map_add, chi_σ, map_smul, map_one, smul_eq_mul, mul_one]

/-- `χ(x) = δ³ − δ = [2][3]`, `δ = q + q⁻¹`. -/
theorem chi_symm3 : chi q hq (symm3 q) = (q + q⁻¹) ^ 3 - (q + q⁻¹) := by
  rw [symm3, map_sub, map_mul, map_mul, chi_a, chi_a]; ring

/-- `χ(x) ≠ 0` iff `[2][3] ≠ 0`; in closed form `χ(x) = (q² + 1)(q⁴ + q² + 1)/q³`. -/
theorem chi_symm3_eq : chi q hq (symm3 q) = (q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1) / q ^ 3 := by
  rw [chi_symm3]; field_simp; ring

include hq in
/-- **`τ(x) = (q⁴ + q² + 1)(q⁴ + 1)/(q³(q² + 1))`** for every `q ≠ 0` with `q² + 1 ≠ 0`. -/
theorem jimboTrace_symm3_eq (hq21 : q ^ 2 + 1 ≠ 0) :
    jimboTrace q hq 2 (symm3 q) = (q ^ 4 + q ^ 2 + 1) * (q ^ 4 + 1) / (q ^ 3 * (q ^ 2 + 1)) := by
  let T := jimboMarkov q hq hq21
  have hT : ∀ n x, jimboTrace q hq n x = T.tr n x := fun _ _ => rfl
  set b : Hecke K q q⁻¹ 1 := Hecke.σ K q q⁻¹ 1 (Fin.last 0) + q⁻¹ • 1 with hb
  set u : K := q ^ 3 / (q ^ 2 + 1) + q⁻¹ with hu
  have hb0 : T.tr 1 b = u := by
    rw [hb, map_add, map_smul, T.param_eq, T.tr_one, smul_eq_mul, mul_one]
  have ha0 : T.tr 2 (a q 0) = u := by rw [a_zero_eq_incl, ← hb, T.tr_incl, hb0]
  have ha01 : T.tr 2 (a q 0 * a q 1) = u * u := by
    rw [a_zero_eq_incl, ← hb, a_one_eq, mul_add, map_add, T.tr_markov, mul_smul_comm, mul_one,
      map_smul, T.tr_incl, hb0, smul_eq_mul, hu]
    ring
  rw [hT, symm3, map_sub, T.tr_cyclic, ← mul_assoc, a_mul_self q hq, smul_mul_assoc, map_smul,
    ha01, ha0, smul_eq_mul, hu]
  field_simp
  ring

/-- The central idempotent of the `(3)` block, `p₃ = x / χ(x)`. -/
noncomputable def p3 : H := (chi q hq (symm3 q))⁻¹ • symm3 q

include hq in
theorem chi_symm3_ne_zero (hq21 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    chi q hq (symm3 q) ≠ 0 := by
  rw [chi_symm3_eq]
  exact div_ne_zero (mul_ne_zero hq21 h3) (pow_ne_zero _ hq)

include hq in
theorem p3_mul_p3 (hq21 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    p3 q hq * p3 q hq = p3 q hq := by
  have hc := chi_symm3_ne_zero q hq hq21 h3
  rw [p3, smul_mul_smul_comm, symm3_mul q hq, smul_smul]
  congr 1
  field_simp

/-- `p₃` is central: `p₃ y = y p₃ = χ(y) p₃`. -/
theorem p3_mul (y : H) : p3 q hq * y = chi q hq y • p3 q hq := by
  rw [p3, smul_mul_assoc, symm3_mul q hq, smul_comm]

theorem mul_p3 (y : H) : y * p3 q hq = chi q hq y • p3 q hq := by
  rw [p3, mul_smul_comm, mul_symm3 q hq, smul_comm]

include hq in
/-- **The convention-D weight of the isospin-3/2 block: `τ(p₃) = (q⁴ + 1)/(q² + 1)²`.** -/
theorem jimboTrace_p3 (hq21 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    jimboTrace q hq 2 (p3 q hq) = (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 := by
  rw [p3, map_smul, jimboTrace_symm3_eq q hq hq21, chi_symm3_eq, smul_eq_mul, inv_div,
    div_mul_div_comm, div_eq_div_iff (mul_ne_zero (mul_ne_zero hq21 h3)
      (mul_ne_zero (pow_ne_zero _ hq) hq21)) (pow_ne_zero _ hq21)]
  ring

end QOU.IwahoriHecke.HeckeTrivialBlockWeight
