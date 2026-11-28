import Mathlib.RingTheory.Polynomial.Cyclotomic.Basic
import QOU.MassTheory.CyclotomicBoundaryCertified

/-!
# The cumulant criterion for products of cyclotomic polynomials

For `P ∈ ℚ[X]` with `P(1) ≠ 0` put `θ = X d/dX` and `m_j = (θ^j P)(1)`. The second cumulant
`κ₂ = m₂/m₀ − (m₁/m₀)²` is `(log P(e^t))''` at `t = 0`, computed without `exp`: it is defined
from `θ` alone, so it is purely algebraic.

* `κ2_mul`: `κ₂` is additive on products (`θ` is a derivation).
* `κ2_geom`: `κ₂(1 + X + ⋯ + X^{k-1}) = (k² − 1)/12`.
* `cyclotomic_κ2_int`: for `k ≥ 2`, `Φ_k(1) ≠ 0` and `12 κ₂(Φ_k) ∈ ℤ`, by strong induction from
  `∏_{1 < d ∣ k} Φ_d = 1 + X + ⋯ + X^{k-1}`.
* `cumulant_int_of_isCycloProduct`: if `P = c · X^j · ∏ Φ_k` and `P(1) ≠ 0`, then
  `12 κ₂(P) ∈ ℤ`.

This is the criterion behind `computations/cyclotomic_boundary_cumulant_integrality.py`
(`conj:cyclotomic-boundary-at-keystone`): a cleared Habiro tail with `12 κ₂ ∉ ℤ` is not a
product of cyclotomic polynomials. Pure algebra, no measured values.
-/

namespace QOU.Mass.CyclotomicCumulant
open Polynomial Finset

/-- The Euler operator `θ = X d/dX`. -/
noncomputable def θ (P : ℚ[X]) : ℚ[X] := X * derivative P

lemma θ_mul (P Q : ℚ[X]) : θ (P * Q) = θ P * Q + P * θ Q := by
  unfold θ; rw [derivative_mul]; ring

lemma θ_add (P Q : ℚ[X]) : θ (P + Q) = θ P + θ Q := by unfold θ; rw [derivative_add]; ring

lemma θ_sum {ι : Type*} (s : Finset ι) (f : ι → ℚ[X]) : θ (∑ i ∈ s, f i) = ∑ i ∈ s, θ (f i) := by
  unfold θ; rw [derivative_sum, mul_sum]

lemma θ_C_mul (c : ℚ) (P : ℚ[X]) : θ (C c * P) = C c * θ P := by
  unfold θ; rw [derivative_C_mul]; ring

lemma θ_X_pow (i : ℕ) : θ (X ^ i) = C (i : ℚ) * X ^ i := by
  unfold θ; rw [derivative_X_pow]
  rcases i with _ | i
  · simp
  · rw [Nat.add_sub_cancel, pow_succ]; push_cast; ring

lemma θ_C (c : ℚ) : θ (C c) = 0 := by unfold θ; simp

lemma θ_zero : θ 0 = 0 := by unfold θ; simp

lemma θ_one : θ 1 = 0 := by unfold θ; simp

/-- Moments at `q = 1`: `m₀ = P(1)`, `m₁ = (θP)(1)`, `m₂ = (θ²P)(1)`. -/
noncomputable def m0 (P : ℚ[X]) : ℚ := P.eval 1
noncomputable def m1 (P : ℚ[X]) : ℚ := (θ P).eval 1
noncomputable def m2 (P : ℚ[X]) : ℚ := (θ (θ P)).eval 1

/-- The second cumulant `κ₂ = m₂/m₀ − (m₁/m₀)²`; at `q = e^t` it is `(log P)''(0)`. -/
noncomputable def κ2 (P : ℚ[X]) : ℚ := m2 P / m0 P - (m1 P / m0 P) ^ 2

lemma m0_mul (P Q : ℚ[X]) : m0 (P * Q) = m0 P * m0 Q := by simp [m0]
lemma m1_mul (P Q : ℚ[X]) : m1 (P * Q) = m1 P * m0 Q + m0 P * m1 Q := by
  simp [m1, m0, θ_mul]
lemma m2_mul (P Q : ℚ[X]) : m2 (P * Q) = m2 P * m0 Q + 2 * (m1 P * m1 Q) + m0 P * m2 Q := by
  simp only [m2, m1, m0, θ_mul, θ_add, eval_add, eval_mul]; ring

theorem κ2_mul {P Q : ℚ[X]} (hP : m0 P ≠ 0) (hQ : m0 Q ≠ 0) : κ2 (P * Q) = κ2 P + κ2 Q := by
  unfold κ2; rw [m0_mul, m1_mul, m2_mul]; field_simp; ring

theorem κ2_prod {ι : Type*} [DecidableEq ι] (s : Finset ι) (f : ι → ℚ[X])
    (h : ∀ i ∈ s, m0 (f i) ≠ 0) :
    m0 (∏ i ∈ s, f i) ≠ 0 ∧ κ2 (∏ i ∈ s, f i) = ∑ i ∈ s, κ2 (f i) := by
  induction s using Finset.induction_on with
  | empty => simp [m0, κ2, m1, m2, θ_one, θ_zero]
  | insert a s ha ih =>
    have ih' := ih (fun i hi => h i (mem_insert_of_mem hi))
    have hA := h a (mem_insert_self a s)
    rw [prod_insert ha, sum_insert ha, m0_mul, κ2_mul hA ih'.1, ih'.2]
    exact ⟨mul_ne_zero hA ih'.1, rfl⟩

lemma sum_range_cast (k : ℕ) : ∑ i ∈ range k, (i : ℚ) = k * (k - 1) / 2 := by
  induction k with
  | zero => simp
  | succ k ih => rw [sum_range_succ, ih]; push_cast; ring

lemma sum_range_cast_sq (k : ℕ) : ∑ i ∈ range k, (i : ℚ) ^ 2 = (k - 1) * k * (2 * k - 1) / 6 := by
  induction k with
  | zero => simp
  | succ k ih => rw [sum_range_succ, ih]; push_cast; ring

/-- The geometric sum `[k] = 1 + X + ⋯ + X^{k-1}` has `κ₂ = (k² − 1)/12`. -/
theorem κ2_geom (k : ℕ) (hk : 0 < k) :
    m0 (∑ i ∈ range k, X ^ i) = k ∧ κ2 (∑ i ∈ range k, X ^ i) = ((k : ℚ) ^ 2 - 1) / 12 := by
  have e0 : m0 (∑ i ∈ range k, X ^ i) = k := by simp [m0]
  have e1 : m1 (∑ i ∈ range k, (X : ℚ[X]) ^ i) = k * (k - 1) / 2 := by
    simp only [m1, θ_sum, θ_X_pow, eval_finset_sum, eval_mul, eval_C, eval_pow, eval_X, one_pow,
      mul_one]
    exact sum_range_cast k
  have e2 : m2 (∑ i ∈ range k, (X : ℚ[X]) ^ i) = (k - 1) * k * (2 * k - 1) / 6 := by
    simp only [m2, θ_sum, θ_C_mul, θ_X_pow, eval_finset_sum, eval_mul, eval_C, eval_pow, eval_X,
      one_pow, mul_one]
    rw [← sum_range_cast_sq k]; exact sum_congr rfl (fun i _ => by ring)
  refine ⟨e0, ?_⟩
  have hk' : (k : ℚ) ≠ 0 := by exact_mod_cast hk.ne'
  unfold κ2; rw [e0, e1, e2]; field_simp; ring

lemma isInt_sum {ι : Type*} [DecidableEq ι] (s : Finset ι) (f : ι → ℚ)
    (h : ∀ i ∈ s, ∃ z : ℤ, f i = z) : ∃ z : ℤ, ∑ i ∈ s, f i = z := by
  induction s using Finset.induction_on with
  | empty => exact ⟨0, by simp⟩
  | insert a s ha ih =>
    obtain ⟨z, hz⟩ := ih (fun i hi => h i (mem_insert_of_mem hi))
    obtain ⟨y, hy⟩ := h a (mem_insert_self a s)
    exact ⟨y + z, by rw [sum_insert ha, hy, hz]; push_cast; ring⟩

/-- **`12 κ₂(Φ_k)` is an integer** for `k ≥ 2`, and `Φ_k(1) ≠ 0`. -/
theorem cyclotomic_κ2_int : ∀ k : ℕ, 2 ≤ k →
    m0 (cyclotomic k ℚ) ≠ 0 ∧ ∃ z : ℤ, 12 * κ2 (cyclotomic k ℚ) = z := by
  intro k
  induction k using Nat.strong_induction_on with
  | _ k ih =>
    intro hk
    have hk0 : 0 < k := by omega
    have hG := prod_cyclotomic_eq_geom_sum hk0 ℚ
    obtain ⟨g0, g2⟩ := κ2_geom k hk0
    have hk1 : k ≠ 1 := by omega
    have hkz : k ≠ 0 := by omega
    have hmem : k ∈ k.divisors.erase 1 := mem_erase.mpr ⟨hk1, Nat.mem_divisors_self k hkz⟩
    -- every factor is nonzero at 1, since the product is `k ≠ 0`
    have hall : ∀ d ∈ k.divisors.erase 1, m0 (cyclotomic d ℚ) ≠ 0 := by
      intro d hd
      have : m0 (∏ i ∈ k.divisors.erase 1, cyclotomic i ℚ) ≠ 0 := by
        rw [hG, g0]; exact_mod_cast hk0.ne'
      rw [m0, eval_prod, prod_ne_zero_iff] at this
      exact this d hd
    refine ⟨hall k hmem, ?_⟩
    obtain ⟨_, hκ⟩ := κ2_prod (k.divisors.erase 1) (fun d => cyclotomic d ℚ) hall
    rw [hG, g2, ← add_sum_erase _ _ hmem] at hκ
    obtain ⟨z, hz⟩ := isInt_sum ((k.divisors.erase 1).erase k) (fun d => 12 * κ2 (cyclotomic d ℚ))
      (fun d hd => by
        obtain ⟨hdk1, hd1⟩ := mem_erase.mp hd
        obtain ⟨hd11, hd2⟩ := mem_erase.mp hd1
        have hdk : d ≤ k := Nat.divisor_le hd2
        have hdp : 0 < d := Nat.pos_of_mem_divisors hd2
        exact (ih d (by omega) (by omega)).2)
    refine ⟨(k : ℤ) ^ 2 - 1 - z, ?_⟩
    rw [← mul_sum] at hz
    push_cast
    linarith [hκ, hz]

lemma κ2_C (c : ℚ) : κ2 (C c) = 0 := by simp [κ2, m2, m1, θ_C, θ_zero]

lemma κ2_X_pow (j : ℕ) : m0 (X ^ j) = 1 ∧ κ2 (X ^ j) = 0 := by
  have h1 : θ ((X : ℚ[X]) ^ j) = C (j : ℚ) * X ^ j := θ_X_pow j
  refine ⟨by simp [m0], ?_⟩
  simp only [κ2, m0, m1, m2, h1, θ_C_mul, eval_mul, eval_C, eval_pow, eval_X, one_pow]; ring

open QOU.Mass.CyclotomicBoundaryCertified in
/-- **Cumulant criterion.** If `P = c · X^j · ∏ Φ_k` and `P(1) ≠ 0`, then `12 κ₂(P) ∈ ℤ`. -/
theorem cumulant_int_of_isCycloProduct {P : ℤ[X]} (hP : IsCycloProduct P)
    (h1 : m0 (P.map (Int.castRingHom ℚ)) ≠ 0) :
    ∃ z : ℤ, 12 * κ2 (P.map (Int.castRingHom ℚ)) = z := by
  obtain ⟨c, j, s, rfl⟩ := hP
  simp only [Polynomial.map_mul, Polynomial.map_pow, map_X, map_C, Polynomial.map_multiset_prod,
    Multiset.map_map, Function.comp_def, map_cyclotomic_int] at h1 ⊢
  have hc : ((c : ℚ)) ≠ 0 := by
    intro e; apply h1; simp [m0, e]
  set R := (s.map fun k => cyclotomic k ℚ).prod
  have hR : m0 R ≠ 0 := by
    intro e; apply h1; rw [m0_mul, e, mul_zero]
  have hcX : m0 (C ((Int.castRingHom ℚ) c) * X ^ j) ≠ 0 := by
    rw [m0_mul, (κ2_X_pow j).1]; simpa [m0] using hc
  rw [κ2_mul hcX hR, κ2_mul (by simpa [m0] using hc) (by rw [(κ2_X_pow j).1]; exact one_ne_zero), κ2_C _,
    (κ2_X_pow j).2]
  -- the cyclotomic part, by induction on the multiset
  suffices H : ∀ t : Multiset ℕ, m0 (t.map fun k => cyclotomic k ℚ).prod ≠ 0 →
      ∃ z : ℤ, 12 * κ2 (t.map fun k => cyclotomic k ℚ).prod = z by
    obtain ⟨z, hz⟩ := H s hR; exact ⟨z, by rw [← hz]; ring⟩
  intro t
  induction t using Multiset.induction_on with
  | empty => intro _; exact ⟨0, by simp [κ2, m2, m1, θ_one, θ_zero]⟩
  | cons a t ih =>
    intro ht
    rw [Multiset.map_cons, Multiset.prod_cons, m0_mul] at ht
    have ha := left_ne_zero_of_mul ht
    have htt := right_ne_zero_of_mul ht
    obtain ⟨z, hz⟩ := ih htt
    rw [Multiset.map_cons, Multiset.prod_cons, κ2_mul ha htt, mul_add, hz]
    rcases Nat.lt_or_ge a 2 with h | h
    · interval_cases a
      · exact ⟨z, by simp [cyclotomic_zero, κ2, m2, m1, θ_one, θ_zero]⟩
      · exact absurd (by simp [m0, cyclotomic_one]) ha
    · obtain ⟨y, hy⟩ := (cyclotomic_κ2_int a h).2
      exact ⟨y + z, by rw [hy]; push_cast; ring⟩

end QOU.Mass.CyclotomicCumulant
