/-
Copyright (c) 2026. All rights reserved.
-/
import QOU.Core.TarskiSign
import Mathlib.Algebra.Order.Archimedean.Basic

/-!
# Bernstein completeness: a polynomial positive on `[0, 1]` has a certificate

`bernstein_pos` (in `QOU.Core.TarskiSign`) is the soundness half: positive
Bernstein coefficients give positivity. This file proves the converse used by
the certificate generator. If `f(x) = ∑_{k ≤ n} aₖ xᵏ` satisfies `f ≥ δ > 0` on
`[0, 1]`, then for some degree `N ≥ n` all Bernstein coefficients of `f` are
positive, so `bernstein_pos` applies. The search for a certificate by degree
elevation therefore terminates.

* `elevate n N a j = ∑_{k ≤ n} aₖ · C(N − k, j − k)` (zero when `j < k`) is the
  degree-`N` Bernstein coefficient of `f` (`powPoly_eq_bernstein`), from
  `xᵏ = xᵏ (x + (1 − x))^{N−k}`.
* `elevate n N a j = C(N, j) · ∑ₖ aₖ C(j, k)/C(N, k)`, and
  `|C(j, k)/C(N, k) − (j/N)ᵏ| ≤ k²/N` (`ratio_err`), so the bracket is within
  `(∑ₖ |aₖ|) n²/N` of `f(j/N) ≥ δ`.

The hypothesis is a uniform `δ`, not pointwise positivity: over `ℚ` a rational
polynomial can be positive at every rational point of `[0, 1]` and vanish at an
irrational one, and then no certificate exists. Any ordered field with the
Archimedean property; no completeness, no axiom.
-/

namespace QOU.Core.TarskiSign

open Finset

section Elevation

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- A polynomial in the power basis: `∑_{k ≤ n} aₖ xᵏ`. -/
def powPoly (n : ℕ) (a : ℕ → K) (x : K) : K :=
  ∑ k ∈ range (n + 1), a k * x ^ k

/-- The degree-`N` Bernstein coefficient (binomial absorbed) of `powPoly n a`. -/
def elevate (n N : ℕ) (a : ℕ → K) (j : ℕ) : K :=
  ∑ k ∈ range (n + 1), a k * (if k ≤ j then ((N - k).choose (j - k) : K) else 0)

omit [LinearOrder K] [IsStrictOrderedRing K] in
/-- `xᵏ = ∑_{k ≤ j ≤ N} C(N − k, j − k) xʲ (1 − x)^{N−j}`. -/
theorem monomial_eq_bernstein (k N : ℕ) (hk : k ≤ N) (x : K) :
    x ^ k = ∑ j ∈ range (N + 1),
      (if k ≤ j then ((N - k).choose (j - k) : K) else 0) * (x - 0) ^ j * (1 - x) ^ (N - j) := by
  rw [← sum_range_add_sum_Ico _ (by omega : k ≤ N + 1)]
  have h0 : ∑ j ∈ range k,
      (if k ≤ j then ((N - k).choose (j - k) : K) else 0) * (x - 0) ^ j * (1 - x) ^ (N - j) = 0 := by
    apply sum_eq_zero; intro j hj
    have : ¬ k ≤ j := by simp at hj; omega
    simp [this]
  rw [h0, zero_add, sum_Ico_eq_sum_range]
  have h1 : (x + (1 - x)) ^ (N - k) = 1 := by simp
  calc x ^ k = x ^ k * (x + (1 - x)) ^ (N - k) := by rw [h1, mul_one]
    _ = _ := by
      rw [add_pow, mul_sum]
      have : N + 1 - k = N - k + 1 := by omega
      rw [this]
      apply sum_congr rfl; intro i hi
      simp only [mem_range] at hi
      have e1 : k + i - k = i := by omega
      have e2 : N - (k + i) = N - k - i := by omega
      simp only [Nat.le_add_right, if_true, e1, e2, sub_zero, pow_add]
      ring

omit [LinearOrder K] [IsStrictOrderedRing K] in
/-- **Degree elevation.** For `N ≥ n`, `powPoly n a` is the degree-`N`
Bernstein polynomial on `[0, 1]` with coefficients `elevate n N a`. -/
theorem powPoly_eq_bernstein (n N : ℕ) (hn : n ≤ N) (a : ℕ → K) (x : K) :
    powPoly n a x = bernstein 0 1 N (elevate n N a) x := by
  unfold powPoly bernstein elevate
  calc ∑ k ∈ range (n + 1), a k * x ^ k
      = ∑ k ∈ range (n + 1), ∑ j ∈ range (N + 1), a k *
          ((if k ≤ j then ((N - k).choose (j - k) : K) else 0) * (x - 0) ^ j * (1 - x) ^ (N - j)) := by
        apply sum_congr rfl; intro k hk
        simp only [mem_range] at hk
        rw [monomial_eq_bernstein k N (by omega), mul_sum]
    _ = _ := by
        rw [sum_comm]; apply sum_congr rfl; intro j _
        rw [sum_mul, sum_mul]; apply sum_congr rfl; intro k _; ring

end Elevation

section Ratio

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- The ratio `C(j, k) / C(N, k)`. -/
def ratio (N j k : ℕ) : K := (j.choose k : K) / (N.choose k : K)

omit [LinearOrder K] [IsStrictOrderedRing K] in
private theorem sq_cast (k : ℕ) : ((k + 1 : ℕ) : K) ^ 2 = (k : K) ^ 2 + k + (k + 1) := by
  push_cast; ring

private theorem sq_step (k N : ℕ) :
    (k : K) ^ 2 / N + (k : K) / N ≤ ((k + 1 : ℕ) : K) ^ 2 / N := by
  rw [sq_cast, ← add_div]
  have hk : (0 : K) ≤ (k : K) + 1 := by positivity
  have hN : (0 : K) ≤ (N : K) := Nat.cast_nonneg N
  exact div_le_div_of_nonneg_right (le_add_of_nonneg_right hk) hN

/-- **The ratio is close to `(j/N)ᵏ`.** For `j ≤ N` and `k ≤ N`,
`|C(j, k)/C(N, k) − (j/N)ᵏ| ≤ k²/N`. -/
theorem ratio_err (N j : ℕ) (hN : 0 < N) (hj : j ≤ N) :
    ∀ k ≤ N, |(ratio N j k : K) - ((j : K) / N) ^ k| ≤ (k : K) ^ 2 / N := by
  have hNK : (0 : K) < N := by exact_mod_cast hN
  intro k
  induction k with
  | zero => intro _; simp [ratio]
  | succ k ih =>
    intro hk
    have hkN : k < N := by omega
    have ih := ih (by omega)
    set v : K := (j : K) / N
    set u : K := ((j - k : ℕ) : K) / ((N - k : ℕ) : K)
    have hNk : (0 : K) < ((N - k : ℕ) : K) := by exact_mod_cast (by omega : 0 < N - k)
    have hCN : (0 : K) < (N.choose k : K) := by exact_mod_cast Nat.choose_pos (by omega)
    -- the recurrence `ratio (k+1) = ratio k * u`
    have hrec : (ratio N j (k + 1) : K) = ratio N j k * u := by
      have a1 := Nat.choose_succ_right_eq j k
      have a2 := Nat.choose_succ_right_eq N k
      have b1 : ((j.choose (k + 1) : ℕ) : K) * (k + 1) = (j.choose k : K) * ((j - k : ℕ) : K) := by
        exact_mod_cast a1
      have b2 : ((N.choose (k + 1) : ℕ) : K) * (k + 1) = (N.choose k : K) * ((N - k : ℕ) : K) := by
        exact_mod_cast a2
      have hk1 : (0 : K) < (k : K) + 1 := by positivity
      unfold ratio
      have hC1 : (N.choose (k + 1) : K) = (N.choose k : K) * ((N - k : ℕ) : K) / ((k : K) + 1) := by
        rw [eq_div_iff hk1.ne']; exact b2
      have hJ1 : (j.choose (k + 1) : K) = (j.choose k : K) * ((j - k : ℕ) : K) / ((k : K) + 1) := by
        rw [eq_div_iff hk1.ne']; exact b1
      rw [hC1, hJ1]; simp only [u]; field_simp
    have hv0 : 0 ≤ v := by positivity
    have hv1 : v ≤ 1 := by
      rw [div_le_one hNK]; exact_mod_cast hj
    have hu0 : 0 ≤ u := by positivity
    have huv : u ≤ v := by
      rcases le_or_gt k j with hkj | hjk
      · rw [div_le_div_iff₀ hNk hNK]
        have e1 : ((j - k : ℕ) : K) = j - k := by push_cast [Nat.cast_sub hkj]; ring
        have e2 : ((N - k : ℕ) : K) = N - k := by push_cast [Nat.cast_sub hkN.le]; ring
        rw [e1, e2]
        have : (j : K) * k ≤ N * k := by
          have : (j : K) ≤ N := by exact_mod_cast hj
          nlinarith [(Nat.cast_nonneg k : (0 : K) ≤ k)]
        nlinarith
      · have : j - k = 0 := by omega
        simp only [u, this, Nat.cast_zero, zero_div]; exact hv0
    have hvu : v - u ≤ (k : K) / N := by
      rcases le_or_gt k j with hkj | hjk
      · have e1 : ((j - k : ℕ) : K) = j - k := by push_cast [Nat.cast_sub hkj]; ring
        have hNle : ((N - k : ℕ) : K) ≤ N := by exact_mod_cast Nat.sub_le N k
        have hjk0 : (0 : K) ≤ (j : K) - k := by
          rw [sub_nonneg]; exact_mod_cast hkj
        have : ((j : K) - k) / N ≤ u := by
          simp only [u, e1]; exact div_le_div_of_nonneg_left hjk0 hNk hNle
        have : v - (k : K) / N = ((j : K) - k) / N := by simp only [v]; ring
        linarith
      · have : j - k = 0 := by omega
        simp only [u, this, Nat.cast_zero, zero_div, sub_zero, v]
        apply div_le_div_of_nonneg_right _ hNK.le
        exact_mod_cast hjk.le
    have hp0 : 0 ≤ v ^ k := pow_nonneg hv0 k
    have hp1 : v ^ k ≤ 1 := pow_le_one₀ hv0 hv1
    rw [hrec, pow_succ]
    have key : ratio N j k * u - v ^ k * v = (ratio N j k - v ^ k) * u + v ^ k * (u - v) := by ring
    rw [key]
    calc |(ratio N j k - v ^ k) * u + v ^ k * (u - v)|
        ≤ |(ratio N j k - v ^ k) * u| + |v ^ k * (u - v)| := abs_add_le _ _
      _ ≤ (k : K) ^ 2 / N + (k : K) / N := by
          refine add_le_add ?_ ?_
          · rw [abs_mul, abs_of_nonneg hu0]
            calc |ratio N j k - v ^ k| * u ≤ |ratio N j k - v ^ k| * 1 := by
                  gcongr; linarith
              _ ≤ _ := by rw [mul_one]; exact ih
          · rw [abs_mul, abs_of_nonneg hp0, abs_of_nonpos (by linarith)]
            calc v ^ k * -(u - v) ≤ 1 * -(u - v) := by gcongr; linarith
              _ ≤ _ := by linarith
      _ ≤ ((k + 1 : ℕ) : K) ^ 2 / N := sq_step k N

/-- `elevate n N a j = C(N, j) · ∑ₖ aₖ C(j, k)/C(N, k)` for `n ≤ N`, `j ≤ N`. -/
theorem elevate_eq (n N : ℕ) (hn : n ≤ N) (a : ℕ → K) (j : ℕ) (hj : j ≤ N) :
    elevate n N a j = (N.choose j : K) * ∑ k ∈ range (n + 1), a k * ratio N j k := by
  unfold elevate; rw [mul_sum]; apply sum_congr rfl; intro k hk
  simp only [mem_range] at hk
  have hCk : (0 : K) < (N.choose k : K) := by exact_mod_cast Nat.choose_pos (by omega)
  unfold ratio
  split_ifs with hkj
  · have h := Nat.choose_mul (n := N) (k := j) (s := k) hj hkj
    have h' : (N.choose j : K) * (j.choose k : K) = (N.choose k : K) * ((N - k).choose (j - k) : K) := by
      exact_mod_cast h
    field_simp; linear_combination a k * h'.symm
  · have : j.choose k = 0 := Nat.choose_eq_zero_of_lt (by omega)
    simp [this]

end Ratio

section Complete

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- **Bernstein completeness.** If `powPoly n a ≥ δ > 0` on `[0, 1]`, then at
some degree `N ≥ n` every Bernstein coefficient is positive. -/
theorem bernstein_complete [Archimedean K] (n : ℕ) (a : ℕ → K) {δ : K} (hδ : 0 < δ)
    (hf : ∀ x : K, 0 ≤ x → x ≤ 1 → δ ≤ powPoly n a x) :
    ∃ N, n ≤ N ∧ ∀ j ≤ N, 0 < elevate n N a j := by
  set A : K := ∑ k ∈ range (n + 1), |a k|
  have hA : 0 ≤ A := sum_nonneg (fun _ _ => abs_nonneg _)
  obtain ⟨M, hM⟩ := exists_nat_gt (A * (n : K) ^ 2 / δ)
  refine ⟨max (max n M) 1, by omega, ?_⟩
  set N := max (max n M) 1
  have hN : 0 < N := by omega
  have hNK : (0 : K) < N := by exact_mod_cast hN
  have hMN : (M : K) ≤ N := by exact_mod_cast (by omega : M ≤ N)
  intro j hj
  rw [elevate_eq n N (by omega) a j hj]
  have hC : (0 : K) < (N.choose j : K) := by exact_mod_cast Nat.choose_pos hj
  apply mul_pos hC
  set v : K := (j : K) / N
  have hv0 : 0 ≤ v := by positivity
  have hv1 : v ≤ 1 := by rw [div_le_one hNK]; exact_mod_cast hj
  have hfv := hf v hv0 hv1
  -- termwise: aₖ r ≥ aₖ vᵏ − |aₖ| n²/N
  have hterm : ∀ k ∈ range (n + 1),
      a k * v ^ k - |a k| * ((n : K) ^ 2 / N) ≤ a k * ratio N j k := by
    intro k hk
    simp only [mem_range] at hk
    have he := ratio_err (K := K) N j hN hj k (by omega)
    have hkn : (k : K) ^ 2 / N ≤ (n : K) ^ 2 / N := by
      apply div_le_div_of_nonneg_right _ hNK.le
      have : (k : K) ≤ n := by exact_mod_cast (by omega : k ≤ n)
      nlinarith [(Nat.cast_nonneg k : (0 : K) ≤ k)]
    have h1 : |a k * ratio N j k - a k * v ^ k| ≤ |a k| * ((n : K) ^ 2 / N) := by
      rw [← mul_sub, abs_mul]; gcongr; exact he.trans hkn
    have := neg_abs_le (a k * ratio N j k - a k * v ^ k)
    linarith
  have hsum := sum_le_sum hterm
  rw [sum_sub_distrib, ← sum_mul] at hsum
  have hpow : ∑ k ∈ range (n + 1), a k * v ^ k = powPoly n a v := rfl
  rw [hpow] at hsum
  -- A n²/N < δ
  have hsmall : A * ((n : K) ^ 2 / N) < δ := by
    have h1 : A * (n : K) ^ 2 / δ < N := lt_of_lt_of_le hM hMN
    rw [div_lt_iff₀ hδ] at h1
    rw [mul_div_assoc', div_lt_iff₀ hNK]; linarith
  linarith

/-- **Termination of the certificate search.** If `powPoly n a ≥ δ > 0` on
`[0, 1]`, some degree-`N` Bernstein certificate proves positivity there. -/
theorem exists_bernstein_certificate [Archimedean K] (n : ℕ) (a : ℕ → K) {δ : K}
    (hδ : 0 < δ) (hf : ∀ x : K, 0 ≤ x → x ≤ 1 → δ ≤ powPoly n a x) :
    ∃ N c, (∀ j ≤ N, 0 < c j) ∧ ∀ x, powPoly n a x = bernstein 0 1 N c x := by
  obtain ⟨N, hnN, hpos⟩ := bernstein_complete n a hδ hf
  exact ⟨N, elevate n N a, hpos, powPoly_eq_bernstein n N hnN a⟩

end Complete

end QOU.Core.TarskiSign
