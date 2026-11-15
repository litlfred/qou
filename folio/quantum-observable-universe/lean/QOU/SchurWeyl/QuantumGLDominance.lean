/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.QuantumGLSl2Pair
import QOU.SchurWeyl.QuantumGLWeights
import Mathlib.LinearAlgebra.Eigenspace.Minpoly

/-!
# Highest-weight vectors exist only at dominant weights

G3.4b (bean `qou-gl342`).

## The `U_q(sl₂)` lemma (any representation)

For `ρ : Rep q ι` and a vector `v` with `ρ.E v = 0` and `ρ.Kp v = x v`:

* `Kp_Fpow` — `F^k v` is a `Kp`-eigenvector with eigenvalue `x q^{-2k}`;
* `E_Fpow_succ` — `E F^{k+1} v = C(k+1) F^k v` with
  `C(k) = (a − a⁻¹)(x q a⁻¹ − a x⁻¹ q⁻¹)/(q − q⁻¹)²`, `a = q^k`, i.e. `C(k) = [k][h−k+1]` when
  `x = q^h`;
* `Fpow_eventually_zero` — `F^k v = 0` for some `k` (finitely many eigenvalues, `q` generic);
* `sq_eq_pow_of_highest` — if `v ≠ 0`, then `x² = q^{2M}` for some `M : ℕ`.

## Dominance (`gl_d`)

`hwSpace_eq_bot_of_not_dominant`: if `μ(i) > μ(i+1)` for some Chevalley pair, then
`hwSpace μ = ⊥`.  Here `E_i` raises `e_i ↦ e_{i+1}`, so the highest-weight vectors sit at weights
that are **non-decreasing in the index**: `μ(0) ≤ μ(1) ≤ … ≤ μ(d−1)`.  This is the usual
dominance `λ₁ ≥ … ≥ λ_d` with the letters read in the opposite order.

## Base ring (§7c)

Any field; `q` not a root of unity.

-- Ref: [kassel1995] C. Kassel, *Quantum Groups*, GTM 155, Ch. VI (highest-weight modules).
-/

namespace QOU.SchurWeyl.QuantumGL

open QOU.Mass.QuantumSl2 Matrix

variable {𝕜 : Type*} [Field 𝕜] {ι : Type*} [Fintype ι] [DecidableEq ι]

section Sl2

variable {q : 𝕜} (ρ : Rep q ι)

theorem Km_mulVec_of_Kp (hq : q ≠ 0) {x : 𝕜} (hx : x ≠ 0) {w : ι → 𝕜}
    (hw : ρ.Kp *ᵥ w = x • w) : ρ.Km *ᵥ w = x⁻¹ • w := by
  have h : w = x • (ρ.Km *ᵥ w) := by
    calc w = (ρ.Km * ρ.Kp) *ᵥ w := by rw [ρ.Km_Kp, one_mulVec]
      _ = x • (ρ.Km *ᵥ w) := by rw [← mulVec_mulVec, hw, mulVec_smul]
  calc ρ.Km *ᵥ w = x⁻¹ • (x • (ρ.Km *ᵥ w)) := by rw [smul_smul, inv_mul_cancel₀ hx, one_smul]
    _ = x⁻¹ • w := by rw [← h]

theorem Kp_F_mulVec (w : ι → 𝕜) : ρ.Kp *ᵥ (ρ.F *ᵥ w) = q⁻¹ ^ 2 • (ρ.F *ᵥ (ρ.Kp *ᵥ w)) := by
  rw [mulVec_mulVec, ρ.Kp_F, Matrix.smul_mulVec, ← mulVec_mulVec]

theorem E_F_mulVec (w : ι → 𝕜) :
    ρ.E *ᵥ (ρ.F *ᵥ w) = ρ.F *ᵥ (ρ.E *ᵥ w) + (q - q⁻¹)⁻¹ • (ρ.Kp *ᵥ w - ρ.Km *ᵥ w) := by
  have hEF : ρ.E * ρ.F = ρ.F * ρ.E + (q - q⁻¹)⁻¹ • (ρ.Kp - ρ.Km) := by
    rw [← ρ.EF]; abel
  rw [mulVec_mulVec, hEF, add_mulVec, Matrix.smul_mulVec, sub_mulVec, ← mulVec_mulVec]

/-- `F^k v` is a `Kp`-eigenvector with eigenvalue `x q^{-2k}`. -/
theorem Kp_Fpow {x : 𝕜} {v : ι → 𝕜} (hv : ρ.Kp *ᵥ v = x • v) :
    ∀ k : ℕ, ρ.Kp *ᵥ ((ρ.F ^ k) *ᵥ v) = (x * q⁻¹ ^ (2 * k)) • ((ρ.F ^ k) *ᵥ v)
  | 0 => by simp [hv]
  | k + 1 => by
      rw [pow_succ', ← mulVec_mulVec, Kp_F_mulVec, Kp_Fpow hv k, mulVec_smul, smul_smul]
      congr 1; ring

/-- The coefficient `C(k) = [k][h−k+1]` in multiplicative form, `a = q^k`, `x = q^h`. -/
noncomputable def coefC (q x : 𝕜) (k : ℕ) : 𝕜 :=
  (q ^ k - (q ^ k)⁻¹) * (x * q / q ^ k - q ^ k / (x * q)) / (q - q⁻¹) ^ 2

theorem coefC_one (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0) (x : 𝕜) (hx : x ≠ 0) :
    coefC q x 1 = (q - q⁻¹)⁻¹ * (x - x⁻¹) := by
  unfold coefC
  have hq2' : q ^ 2 - 1 ≠ 0 := by
    intro h; apply hq2; field_simp; linear_combination h
  field_simp

theorem coefC_succ (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0) (x : 𝕜) (hx : x ≠ 0) (k : ℕ) :
    coefC q x (k + 2) = coefC q x (k + 1)
      + (q - q⁻¹)⁻¹ * (x * q⁻¹ ^ (2 * (k + 1)) - (x * q⁻¹ ^ (2 * (k + 1)))⁻¹) := by
  unfold coefC
  have hq2' : q ^ 2 - 1 ≠ 0 := by
    intro h; apply hq2; field_simp; linear_combination h
  have e : q⁻¹ ^ (2 * (k + 1)) = ((q ^ (k + 1)) ^ 2)⁻¹ := by
    rw [inv_pow, ← pow_mul, mul_comm]
  rw [pow_succ q (k + 1), e]
  generalize q ^ (k + 1) = a
  by_cases ha : a = 0
  · subst ha; simp
  · field_simp
    ring

/-- **`E F^{k+1} v = C(k+1) F^k v`** for a highest-weight vector `v`. -/
theorem E_Fpow_succ (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0) {x : 𝕜} (hx : x ≠ 0) {v : ι → 𝕜}
    (hv : ρ.Kp *ᵥ v = x • v) (hE : ρ.E *ᵥ v = 0) :
    ∀ k : ℕ, ρ.E *ᵥ ((ρ.F ^ (k + 1)) *ᵥ v) = coefC q x (k + 1) • ((ρ.F ^ k) *ᵥ v)
  | 0 => by
      rw [pow_one, pow_zero, one_mulVec, E_F_mulVec, hE, mulVec_zero, zero_add, hv,
        Km_mulVec_of_Kp ρ hq hx hv, ← sub_smul, smul_smul, coefC_one hq hq2 x hx]
  | k + 1 => by
      have hxk : x * q⁻¹ ^ (2 * (k + 1)) ≠ 0 := mul_ne_zero hx (pow_ne_zero _ (inv_ne_zero hq))
      rw [pow_succ' ρ.F (k + 1), ← mulVec_mulVec, E_F_mulVec, E_Fpow_succ hq hq2 hx hv hE k,
        mulVec_smul, mulVec_mulVec, ← pow_succ', Kp_Fpow ρ hv (k + 1),
        Km_mulVec_of_Kp ρ hq hxk (Kp_Fpow ρ hv (k + 1)), ← sub_smul, smul_smul, ← add_smul,
        coefC_succ hq hq2 x hx k]

/-! ### `F` is nilpotent on a weight vector, and the highest weight is a power of `q` -/

theorem pow_injective_of_notRoot {q : 𝕜} (hq : q ≠ 0) (hgen : GenericParameter.NotRootOfUnity q)
    {a b : ℕ} (h : q ^ a = q ^ b) : a = b := by
  by_contra hab
  rcases lt_or_gt_of_ne hab with hlt | hlt
  · apply hgen (b - a) (by omega)
    have : q ^ a * q ^ (b - a) = q ^ a * 1 := by rw [← pow_add, Nat.add_sub_cancel' hlt.le, ← h,
      mul_one]
    exact mul_left_cancel₀ (pow_ne_zero _ hq) this
  · apply hgen (a - b) (by omega)
    have : q ^ b * q ^ (a - b) = q ^ b * 1 := by rw [← pow_add, Nat.add_sub_cancel' hlt.le, h,
      mul_one]
    exact mul_left_cancel₀ (pow_ne_zero _ hq) this

variable {q : 𝕜} (ρ : Rep q ι)

/-- **`F` is eventually zero on a `Kp`-eigenvector**: its iterates would otherwise give infinitely
many eigenvalues `x q^{-2k}` of `Kp`. -/
theorem Fpow_eventually_zero (hq : q ≠ 0) (hgen : GenericParameter.NotRootOfUnity q) {x : 𝕜}
    (hx : x ≠ 0) {v : ι → 𝕜} (hv : ρ.Kp *ᵥ v = x • v) : ∃ k : ℕ, (ρ.F ^ k) *ᵥ v = 0 := by
  by_contra h
  push_neg at h
  have hmem : ∀ k : ℕ, Module.End.HasEigenvalue (Matrix.toLin' ρ.Kp) (x * q⁻¹ ^ (2 * k)) := fun k =>
    Module.End.hasEigenvalue_of_hasEigenvector
      ⟨Module.End.mem_eigenspace_iff.mpr (by rw [Matrix.toLin'_apply, Kp_Fpow ρ hv k]), h k⟩
  have hinj : Function.Injective (fun k : ℕ => x * q⁻¹ ^ (2 * k)) := by
    intro k l hkl
    have h1 : (q ^ (2 * k))⁻¹ = (q ^ (2 * l))⁻¹ := by
      rw [← inv_pow, ← inv_pow]; exact mul_left_cancel₀ hx hkl
    have := pow_injective_of_notRoot hq hgen (inv_injective h1)
    omega
  exact (Set.infinite_range_of_injective hinj).mono (by rintro _ ⟨k, rfl⟩; exact hmem k)
    (Module.End.finite_hasEigenvalue _)

/-- **A nonzero highest-weight vector has `K`-eigenvalue a power of `q`**: `x² = q^{2M}` for some
`M ≥ 0` (`M + 1` is the length of its `F`-string). -/
theorem sq_eq_pow_of_highest (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0)
    (hgen : GenericParameter.NotRootOfUnity q) {x : 𝕜} (hx : x ≠ 0) {v : ι → 𝕜} (hv0 : v ≠ 0)
    (hv : ρ.Kp *ᵥ v = x • v) (hE : ρ.E *ᵥ v = 0) : ∃ M : ℕ, x ^ 2 = q ^ (2 * M) := by
  classical
  have hex := Fpow_eventually_zero ρ hq hgen hx hv
  set N := Nat.find hex with hN
  have hN0 : N ≠ 0 := by
    intro h0
    have := Nat.find_spec hex
    rw [← hN, h0, pow_zero, one_mulVec] at this
    exact hv0 this
  obtain ⟨M, hM⟩ := Nat.exists_eq_succ_of_ne_zero hN0
  have hzero : (ρ.F ^ (M + 1)) *ᵥ v = 0 := by
    rw [show M + 1 = N from hM.symm]; exact Nat.find_spec hex
  have hne : (ρ.F ^ M) *ᵥ v ≠ 0 := Nat.find_min hex (by omega)
  have hC : coefC q x (M + 1) = 0 := by
    have h := E_Fpow_succ ρ hq hq2 hx hv hE M
    rw [hzero, mulVec_zero] at h
    exact (smul_eq_zero.mp h.symm).resolve_right hne
  refine ⟨M, ?_⟩
  set a := q ^ (M + 1) with ha
  have ha0 : a ≠ 0 := pow_ne_zero _ hq
  have ha2 : a ^ 2 ≠ 1 := by
    rw [ha, ← pow_mul]; exact hgen _ (by omega)
  have haa : a - a⁻¹ ≠ 0 := by
    intro h; apply ha2
    have : a * (a - a⁻¹) = a ^ 2 - 1 := by field_simp
    rw [h, mul_zero] at this; linear_combination -this
  have hq2sq : (q - q⁻¹) ^ 2 ≠ 0 := pow_ne_zero _ hq2
  unfold coefC at hC
  rw [← ha] at hC
  have h2 : x * q / a - a / (x * q) = 0 := by
    rcases mul_eq_zero.mp ((div_eq_zero_iff.mp hC).resolve_right hq2sq) with h | h
    · exact absurd h haa
    · exact h
  have h3 : x ^ 2 * q ^ 2 = a ^ 2 := by
    field_simp at h2; linear_combination h2
  rw [ha, ← pow_mul, show (M + 1) * 2 = 2 * M + 2 by ring, pow_add] at h3
  exact mul_right_cancel₀ (pow_ne_zero 2 hq) h3

end Sl2

/-! ## Dominance for `gl_d` -/

section Dominance

variable {d : ℕ}

theorem prod_kap_pow (q : 𝕜) {i j : Fin d} (hij : i ≠ j) (μ : Fin d → ℕ) :
    ∏ y, kap q q⁻¹ i j y ^ μ y = q ^ μ j * q⁻¹ ^ μ i := by
  rw [Finset.prod_eq_mul j i (Ne.symm hij) (fun c _ hc => by
      simp [kap, hc.1, hc.2]) (fun h => absurd (Finset.mem_univ _) h)
    (fun h => absurd (Finset.mem_univ _) h)]
  simp only [kap, if_neg hij, eq_self_iff_true, if_true, inv_pow]

/-- **A nonzero highest-weight vector of weight `μ` forces `μ(i) ≤ μ(i+1)`** for every Chevalley
pair. -/
theorem le_of_mem_hwSpace (q : 𝕜) (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0)
    (hgen : GenericParameter.NotRootOfUnity q) (m : ℕ) (μ : Fin d → ℕ)
    {v : (Fin (m + 1) → Fin d) → 𝕜} (hv : v ∈ hwSpace q m μ) (hv0 : v ≠ 0)
    {i j : Fin d} (hij : (j : ℕ) = i + 1) : μ i ≤ μ j := by
  have hne : i ≠ j := fun h => by rw [h] at hij; omega
  set ρ := powRep q hq hq2 hne (m + 1)
  have hE : ρ.E *ᵥ v = 0 := by rw [powRep_E]; exact hv.2 i j hij
  set x : 𝕜 := q ^ μ j * q⁻¹ ^ μ i with hxdef
  have hx : x ≠ 0 := mul_ne_zero (pow_ne_zero _ hq) (pow_ne_zero _ (inv_ne_zero hq))
  have hK : ρ.Kp *ᵥ v = x • v := by
    rw [powRep_Kp, ← hv.1, mulVec_mulVec, cartan_mul_weightProj, Matrix.smul_mulVec, hv.1,
      prod_kap_pow q hne]
  obtain ⟨M, hM⟩ := sq_eq_pow_of_highest ρ hq hq2 hgen hx hv0 hK hE
  have h1 : q ^ (2 * μ j) = q ^ (2 * M + 2 * μ i) := by
    have : x ^ 2 * q ^ (2 * μ i) = q ^ (2 * μ j) := by
      rw [hxdef, mul_pow, ← pow_mul, ← pow_mul, inv_pow, mul_assoc, mul_comm (μ i) 2,
        inv_mul_cancel₀ (pow_ne_zero _ hq), mul_one, mul_comm (μ j) 2]
    rw [← this, hM, ← pow_add]
  have := pow_injective_of_notRoot hq hgen h1
  omega

/-- **`HW_μ = 0` unless `μ` is dominant**: if `μ(i) > μ(i+1)` for some Chevalley pair, the
highest-weight space of weight `μ` is zero. -/
theorem hwSpace_eq_bot_of_not_dominant (q : 𝕜) (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0)
    (hgen : GenericParameter.NotRootOfUnity q) (m : ℕ) (μ : Fin d → ℕ) {i j : Fin d}
    (hij : (j : ℕ) = i + 1) (hμ : μ j < μ i) : hwSpace q m μ = ⊥ := by
  rw [Submodule.eq_bot_iff]
  intro v hv
  by_contra hv0
  exact absurd (le_of_mem_hwSpace q hq hq2 hgen m μ hv hv0 hij) (not_le.mpr hμ)

end Dominance

end QOU.SchurWeyl.QuantumGL
