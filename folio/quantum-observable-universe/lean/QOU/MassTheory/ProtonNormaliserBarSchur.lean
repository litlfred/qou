/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import BraidKnotOctonion.HeckeTrivialBlockWeight
import BraidKnotOctonion.CentralIdempotentSignTwist
import QOU.MassTheory.ProtonQ3SchurElement

/-!
# The bar-invariant Schur normaliser of `H₃(q)` is `[3]_q!`, so `k = 0`

Scope-(a) negative for `conj:proton-normaliser-kl-coordinate`
(audit `docs/audits/2026-11-21-proton-q3-kl-coordinate.md`, round 13).

`F_Bor` uses the normaliser `c_sign = [3]_q!·q⁻³` (`fBor_normaliser_eq_schurSign`), with the
balanced `[3]_q! = (q + q⁻¹)(q² + 1 + q⁻²)`. Write a normaliser of a linear block as
`[3]_q!·q^k`; production has `k = −3`. This file proves, inside the Hecke algebra
`H = Hecke K q q⁻¹ 2` itself, that the bar involution selects `k = 0`.

**Setting.** `K` is any field, `q ≠ 0`, and `q` is not a root of unity. The bar involution is
taken as a hypothesis, `IsBar q 2 τ φ` (`CentralIdempotentInvolution.IsBar`): `φ` is a ring
endomorphism of `H`, `τ`-semilinear with `τ q = q⁻¹`, and `φ σ_i = σ_i⁻¹`. No other property of
`φ` is used. No measured value enters any statement.

**Trivial block.** `x = a₀a₁a₀ − a₀` with `a_i = σ_i + q⁻¹` is the `q`-symmetriser
(`TLKernelRootOfUnity.symm3`).

* `a_bar_fixed`, `symm3_bar_fixed`: `φ a_i = a_i`, so `φ x = x`.
* `symm3_mul_self`: `x·x = [3]_q!·x`, because `χ(x) = [2][3] = [3]_q!`
  (`HeckeTrivialBlockWeight.chi_symm3`). No power of `q` appears.
* `trivial_line_bar_fixed_iff`: for `ε = ±1` and `m ∈ ℤ`, `ε q^m·x` is bar-fixed iff `m = 0`.
  Its square constant is `ε q^m [3]_q!` (`smul_symm3_mul_self`), so the bar-fixed integral
  generator has normaliser `±[3]_q!`: **`k = 0`**.

**Sign block.** `x' = #x`, where `#` is the sign twist `σ_i ↦ −σ_i⁻¹`
(`CentralIdempotentSignTwist.hashMap`). Then `#a_i = q − σ_i`, and

* `sign_line`: `σ_i x' = −q⁻¹ x'` and `χ_sign(x') = [3]_q! ≠ 0`, so `x'` spans the sign line.
  This formalises the step the round-3 audit left argued: the sign line contains a bar-fixed
  generator. (`hashSymm3_bar_fixed`: `φ x' = x'`.)
* `hashSymm3_mul_self`: `x'·x' = [3]_q!·x'`.
* `sign_line_bar_fixed_iff`: `ε q^m·x'` is bar-fixed iff `m = 0`.

**Comparison with production.**

* `production_generator_unique`: the only multiple `λ·x'` whose square constant is
  `c_sign = [3]_q!·q⁻³` is `λ = q⁻³`.
* `production_generator_not_bar_fixed`: `q⁻³·x'` is not bar-fixed.
* `tau_qFact`, `tau_schurSign`, `schurSign_not_bar_fixed`: `[3]_q!` is bar-symmetric, while
  `bar(c_sign) = q⁶·c_sign ≠ c_sign`.

So the production normaliser is the bar-invariant one times `q⁻³`, and the bar involution does
not select it. This is scope (a): the uniform "integral and bar-invariant" criterion gives
`k = 0`. It does not refute `F_Bor`, whose normaliser stays asserted. The identification
`x' = q³·x₋` with the identity-coefficient-1 element `x₋` of the audit is not formalised here;
the comparison above is stated through square constants instead, which does not need it.

-- Ref: [kazhdan-lusztig1979]; [geckpfeiffer2000]
-/

namespace QOU.MassTheory.ProtonNormaliserBarSchur

open QOU.SchurWeyl QOU.SchurWeyl.GenericParameter
open QOU.IwahoriHecke.TLKernelRootOfUnity QOU.IwahoriHecke.HeckeTrivialBlockWeight
open QOU.BraidKnot.CentralIdempotentInvolution
open QOU.MassTheory.PoincareCentering QOU.MassTheory.ProtonQ3Schur

variable {K : Type*} [Field K] {q : K}

local notation "H" => Hecke K q q⁻¹ 2

/-! ## Scalars: what `τ` fixes -/

section Scalars

variable {τ : K →+* K}

theorem tau_inv (hτ : τ q = q⁻¹) : τ q⁻¹ = q := by rw [map_inv₀, hτ, inv_inv]

theorem tau_zpow (hτ : τ q = q⁻¹) (m : ℤ) : τ (q ^ m) = q ^ (-m) := by
  rw [map_zpow₀, hτ, inv_zpow']

/-- `[3]_q!` (balanced) is bar-symmetric. -/
theorem tau_qFact (hτ : τ q = q⁻¹) : τ (qFactThreeBalanced q) = qFactThreeBalanced q := by
  unfold qFactThreeBalanced
  simp only [map_mul, map_add, map_pow, map_one, tau_inv hτ, hτ]
  ring

/-- `bar(c_sign) = q⁶·c_sign`. -/
theorem tau_schurSign (hq : q ≠ 0) (hτ : τ q = q⁻¹) : τ (schurSign q) = q ^ 6 * schurSign q := by
  rw [← fBor_normaliser_eq_schurSign q hq, map_div₀, tau_qFact hτ, map_pow, hτ]
  field_simp

/-- Under "not a root of unity", `q ^ m = 1` only for `m = 0`. -/
theorem zpow_eq_one_iff (hgen : NotRootOfUnity q) (m : ℤ) : q ^ m = 1 ↔ m = 0 := by
  refine ⟨fun h => ?_, fun h => by rw [h, zpow_zero]⟩
  by_contra hm
  have hpos : 0 < m.natAbs := Int.natAbs_pos.mpr hm
  apply hgen m.natAbs hpos
  rcases Int.natAbs_eq m with e | e
  · rw [← zpow_natCast, ← e, h]
  · rw [← zpow_natCast, ← inv_inj, ← zpow_neg, ← e, h, inv_one]

/-- `τ(ε q^m) = ε q^m` with `ε = ±1` iff `m = 0`. -/
theorem tau_unit_fixed_iff (hq : q ≠ 0) (hτ : τ q = q⁻¹) (hgen : NotRootOfUnity q) {ε : K}
    (hε : ε = 1 ∨ ε = -1) (m : ℤ) : τ (ε * q ^ m) = ε * q ^ m ↔ m = 0 := by
  have hε0 : ε ≠ 0 := by rcases hε with rfl | rfl <;> simp
  have hτε : τ ε = ε := by rcases hε with rfl | rfl <;> simp
  have h2 : (2 * m = 0 ↔ m = 0) := by omega
  rw [map_mul, hτε, tau_zpow hτ, mul_right_inj' hε0, ← h2, ← zpow_eq_one_iff hgen (2 * m)]
  constructor
  · intro h
    rw [two_mul, zpow_add₀ hq]
    nth_rewrite 1 [← h]
    rw [← zpow_add₀ hq, neg_add_cancel, zpow_zero]
  · intro h
    have h' : q ^ m * q ^ m = 1 := by rw [← zpow_add₀ hq, ← two_mul, h]
    rw [zpow_neg, inv_eq_of_mul_eq_one_right h']

end Scalars

/-! ## `[3]_q! ≠ 0` and nonvanishing characters -/

section NonZero


theorem sq_add_one_ne_zero' (hgen : NotRootOfUnity q) : q ^ 2 + 1 ≠ 0 := by
  intro h
  apply hgen 4 (by norm_num)
  rw [show (4 : ℕ) = 2 * 2 from rfl, pow_mul, eq_neg_of_add_eq_zero_left h]; norm_num

theorem quartic_ne_zero (hgen : NotRootOfUnity q) : q ^ 4 + q ^ 2 + 1 ≠ 0 := by
  intro h
  apply hgen 6 (by norm_num)
  linear_combination (q ^ 2 - 1) * h

theorem chi_symm3_eq_qFact (hq : q ≠ 0) : chi q hq (symm3 q) = qFactThreeBalanced q := by
  rw [chi_symm3]; unfold qFactThreeBalanced; field_simp; ring

theorem qFact_ne_zero (hq : q ≠ 0) (hgen : NotRootOfUnity q) : qFactThreeBalanced q ≠ 0 := by
  rw [← chi_symm3_eq_qFact hq]
  exact chi_symm3_ne_zero q hq (sq_add_one_ne_zero' hgen) (quartic_ne_zero hgen)

theorem symm3_ne_zero (hq : q ≠ 0) (hgen : NotRootOfUnity q) : symm3 q ≠ 0 := by
  intro h
  apply qFact_ne_zero hq hgen
  rw [← chi_symm3_eq_qFact hq, h, map_zero]

/-- `c_sign` is not bar-symmetric. -/
theorem schurSign_not_bar_fixed (hq : q ≠ 0) {τ : K →+* K} (hτ : τ q = q⁻¹) (hgen : NotRootOfUnity q) :
    τ (schurSign q) ≠ schurSign q := by
  have hs : schurSign q ≠ 0 := by
    rw [← fBor_normaliser_eq_schurSign q hq]
    exact div_ne_zero (qFact_ne_zero hq hgen) (pow_ne_zero _ hq)
  intro h
  rw [tau_schurSign hq hτ] at h
  apply hgen 6 (by norm_num)
  exact mul_right_cancel₀ hs (by rw [h, one_mul])

end NonZero

/-! ## The bar involution on `a_i` and `x` -/

section Bar

variable {τ : K →+* K} {bar : Hecke K q q⁻¹ 2 →+* Hecke K q q⁻¹ 2}

theorem bar_smul (hbar : IsBar q 2 τ bar) (c : K) (y : H) : bar (c • y) = τ c • bar y :=
  IsBar.map_smul q 2 hbar c y

/-- `a_i = σ_i + q⁻¹` is bar-fixed: it is the Kazhdan–Lusztig element `C'_{s_i}`. -/
theorem a_bar_fixed (hbar : IsBar q 2 τ bar) (i : Fin 2) : bar (a q i) = a q i := by
  rw [a, map_add, hbar.map_sigma, bar_smul hbar, map_one, tau_inv hbar.tau_q, Hecke.σInv]
  module

/-- **The `q`-symmetriser is bar-fixed.** -/
theorem symm3_bar_fixed (hbar : IsBar q 2 τ bar) : bar (symm3 q) = symm3 q := by
  rw [symm3, map_sub, map_mul, map_mul, a_bar_fixed hbar, a_bar_fixed hbar]

/-- A multiple `λ·y` of a bar-fixed `y ≠ 0` is bar-fixed iff `τ λ = λ`. -/
theorem smul_bar_fixed_iff (hbar : IsBar q 2 τ bar) {y : H} (hy : bar y = y) (hy0 : y ≠ 0) (c : K) :
    bar (c • y) = c • y ↔ τ c = c := by
  rw [bar_smul hbar, hy]
  exact ⟨fun h => smul_left_injective K hy0 h, fun h => by rw [h]⟩

end Bar

/-! ## Trivial block: the square constant is `[3]_q!`, and `k = 0` -/

section Trivial

/-- **`x·x = [3]_q!·x`.** The Schur normaliser of the trivial block, read off the bar-fixed
symmetriser, is `[3]_q!` with no power of `q`. -/
theorem symm3_mul_self (hq : q ≠ 0) : symm3 q * symm3 q = qFactThreeBalanced q • symm3 q := by
  rw [symm3_mul q hq, chi_symm3_eq_qFact hq]

/-- The square constant of `c·x` is `c·[3]_q!`. -/
theorem smul_symm3_mul_self (hq : q ≠ 0) (c : K) :
    (c • symm3 q) * (c • symm3 q) = (c * qFactThreeBalanced q) • (c • symm3 q) := by
  rw [smul_mul_smul_comm, symm3_mul_self hq, smul_smul, smul_smul]
  ring_nf

variable {τ : K →+* K} {bar : Hecke K q q⁻¹ 2 →+* Hecke K q q⁻¹ 2}

/-- **`k = 0` on the trivial line.** `ε q^m·x` (`ε = ±1`) is bar-fixed iff `m = 0`. -/
theorem trivial_line_bar_fixed_iff (hq : q ≠ 0) (hbar : IsBar q 2 τ bar) (hgen : NotRootOfUnity q) {ε : K}
    (hε : ε = 1 ∨ ε = -1) (m : ℤ) :
    bar ((ε * q ^ m) • symm3 q) = (ε * q ^ m) • symm3 q ↔ m = 0 := by
  rw [smul_bar_fixed_iff hbar (symm3_bar_fixed hbar) (symm3_ne_zero hq hgen)]
  exact tau_unit_fixed_iff hq hbar.tau_q hgen hε m

end Trivial

/-! ## Sign block, through the sign twist `#` -/

section Sign

/-- The sign-line generator `x' = #x`. -/
noncomputable def hashSymm3 (hq : q ≠ 0) : H := hashMap q hq 2 (symm3 q)

theorem hash_σ (hq : q ≠ 0) (i : Fin 2) :
    hashMap q hq 2 (Hecke.σ K q q⁻¹ 2 i) = -Hecke.σInv K q q⁻¹ 2 i := by
  simp [hashMap]

/-- `#a_i = q − σ_i`. -/
theorem hash_a (hq : q ≠ 0) (i : Fin 2) : hashMap q hq 2 (a q i) = q • 1 - Hecke.σ K q q⁻¹ 2 i := by
  rw [a, map_add, hash_σ, map_smul, map_one, Hecke.σInv]
  module

/-- The sign character `σ_i ↦ −q⁻¹`. -/
noncomputable def chiSign (hq : q ≠ 0) : H →ₐ[K] K :=
  Hecke.lift K q q⁻¹ 2 (fun _ => -q⁻¹)
    (fun _ => by simp only [smul_eq_mul, mul_one]; field_simp; ring)
    (fun _ _ => rfl) (fun _ _ _ => mul_comm _ _)

@[simp] theorem chiSign_σ (hq : q ≠ 0) (i : Fin 2) : chiSign hq (Hecke.σ K q q⁻¹ 2 i) = -q⁻¹ :=
  Hecke.lift_σ K q q⁻¹ 2 _ _ _ _ i

/-- `χ_sign ∘ # = χ`. -/
theorem chiSign_comp_hash (hq : q ≠ 0) : (chiSign hq).comp (hashMap q hq 2) = chi q hq := by
  apply Hecke.hom_ext
  intro i
  rw [AlgHom.comp_apply, hash_σ, chi_σ, map_neg, Hecke.σInv, map_sub, map_smul, map_one,
    chiSign_σ, smul_eq_mul, mul_one]
  ring

theorem chiSign_hashSymm3 (hq : q ≠ 0) : chiSign hq (hashSymm3 hq) = qFactThreeBalanced q := by
  rw [hashSymm3, ← AlgHom.comp_apply, chiSign_comp_hash, chi_symm3_eq_qFact]

theorem hashSymm3_ne_zero (hq : q ≠ 0) (hgen : NotRootOfUnity q) : hashSymm3 hq ≠ 0 := by
  intro h
  apply qFact_ne_zero hq hgen
  rw [← chiSign_hashSymm3 hq, h, map_zero]

/-- **`x'` lies in the sign line**: `σ_i x' = −q⁻¹ x'`. -/
theorem sign_line (hq : q ≠ 0) (i : Fin 2) :
    Hecke.σ K q q⁻¹ 2 i * hashSymm3 hq = -q⁻¹ • hashSymm3 hq := by
  have h := congrArg (hashMap q hq 2) (σ_mul_symm3 q hq i)
  rw [map_mul, map_smul, hash_σ, Hecke.σInv] at h
  change (-(Hecke.σ K q q⁻¹ 2 i - (q - q⁻¹) • 1)) * hashSymm3 hq = q • hashSymm3 hq at h
  rw [neg_sub, sub_mul, smul_mul_assoc, one_mul] at h
  have hq' : (q - q⁻¹) - q = -q⁻¹ := by ring
  rw [← hq', sub_smul, ← h]
  abel

/-- **`x'·x' = [3]_q!·x'`.** -/
theorem hashSymm3_mul_self (hq : q ≠ 0) :
    hashSymm3 hq * hashSymm3 hq = qFactThreeBalanced q • hashSymm3 hq := by
  rw [hashSymm3, ← map_mul, symm3_mul_self hq, map_smul]

theorem smul_hashSymm3_mul_self (hq : q ≠ 0) (c : K) :
    (c • hashSymm3 hq) * (c • hashSymm3 hq)
      = (c * qFactThreeBalanced q) • (c • hashSymm3 hq) := by
  rw [smul_mul_smul_comm, hashSymm3_mul_self hq, smul_smul, smul_smul]
  ring_nf

variable {τ : K →+* K} {bar : Hecke K q q⁻¹ 2 →+* Hecke K q q⁻¹ 2}

/-- **`x'` is bar-fixed**: `bar(q − σ_i) = q − σ_i`. -/
theorem hashSymm3_bar_fixed (hq : q ≠ 0) (hbar : IsBar q 2 τ bar) : bar (hashSymm3 hq) = hashSymm3 hq := by
  have hc : ∀ i : Fin 2, bar (hashMap q hq 2 (a q i)) = hashMap q hq 2 (a q i) := by
    intro i
    rw [hash_a, map_sub, bar_smul hbar, map_one, hbar.map_sigma, hbar.tau_q, Hecke.σInv]
    module
  rw [hashSymm3, symm3, map_sub, map_mul, map_mul, map_sub, map_mul, map_mul, hc, hc]

/-- **`k = 0` on the sign line.** `ε q^m·x'` (`ε = ±1`) is bar-fixed iff `m = 0`. -/
theorem sign_line_bar_fixed_iff (hq : q ≠ 0) (hbar : IsBar q 2 τ bar) (hgen : NotRootOfUnity q) {ε : K}
    (hε : ε = 1 ∨ ε = -1) (m : ℤ) :
    bar ((ε * q ^ m) • hashSymm3 hq) = (ε * q ^ m) • hashSymm3 hq ↔ m = 0 := by
  rw [smul_bar_fixed_iff hbar (hashSymm3_bar_fixed hq hbar) (hashSymm3_ne_zero hq hgen)]
  exact tau_unit_fixed_iff hq hbar.tau_q hgen hε m

/-! ## Comparison with the production normaliser `c_sign = [3]_q!·q⁻³` -/

/-- The only multiple of `x'` whose square constant is `c_sign` is `q⁻³·x'`. -/
theorem production_generator_unique (hq : q ≠ 0) (hgen : NotRootOfUnity q) (c : K) :
    c * qFactThreeBalanced q = schurSign q ↔ c = q ^ (-3 : ℤ) := by
  rw [← fBor_normaliser_eq_schurSign q hq, zpow_neg, zpow_ofNat, div_eq_mul_inv, mul_comm _ (_⁻¹)]
  exact mul_left_inj' (qFact_ne_zero hq hgen)

/-- **The production normaliser is not the bar-invariant one.** `q⁻³·x'`, the generator with
square constant `c_sign`, is not bar-fixed. -/
theorem production_generator_not_bar_fixed (hq : q ≠ 0) (hbar : IsBar q 2 τ bar) (hgen : NotRootOfUnity q) :
    bar (q ^ (-3 : ℤ) • hashSymm3 hq) ≠ q ^ (-3 : ℤ) • hashSymm3 hq := by
  have := sign_line_bar_fixed_iff hq hbar hgen (ε := 1) (Or.inl rfl) (-3)
  rw [one_mul] at this
  rw [ne_eq, this]; norm_num

/-- **Summary.** On the sign line, the bar-fixed generator `x'` squares with `[3]_q!`
(`k = 0`), which `τ` fixes; production uses `q⁻³·x'`, with constant `c_sign = q⁻³·[3]_q!`
(`k = −3`), which is neither bar-fixed nor bar-symmetric. -/
theorem bar_normaliser_vs_production (hq : q ≠ 0) (hbar : IsBar q 2 τ bar) (hgen : NotRootOfUnity q) :
    bar (hashSymm3 hq) = hashSymm3 hq ∧
    hashSymm3 hq * hashSymm3 hq = qFactThreeBalanced q • hashSymm3 hq ∧
    τ (qFactThreeBalanced q) = qFactThreeBalanced q ∧
    schurSign q = q ^ (-3 : ℤ) * qFactThreeBalanced q ∧
    bar (q ^ (-3 : ℤ) • hashSymm3 hq) ≠ q ^ (-3 : ℤ) • hashSymm3 hq ∧
    τ (schurSign q) ≠ schurSign q :=
  ⟨hashSymm3_bar_fixed hq hbar, hashSymm3_mul_self hq, tau_qFact hbar.tau_q,
    ((production_generator_unique hq hgen _).mpr rfl).symm,
    production_generator_not_bar_fixed hq hbar hgen, schurSign_not_bar_fixed hq hbar.tau_q hgen⟩

end Sign

end QOU.MassTheory.ProtonNormaliserBarSchur
