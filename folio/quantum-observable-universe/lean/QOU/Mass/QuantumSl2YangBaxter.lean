import QOU.Mass.QuantumSl2RMatrix
import Mathlib.Algebra.BigOperators.Intervals

/-!
# Yang–Baxter for the `U_q(sl₂)` R-matrix: the q-binomial and q-exponential steps

Stage 1 of issue #8894 (Reshetikhin–Turaev invariance). The Yang–Baxter equation follows from
the hexagon identity `(Δ ⊗ 1) R = R₁₃ R₂₃`. Its polynomial part is the product formula for the
q-exponential: if `Y X = q⁻² X Y`, then `Σ c_n (X + Y)ⁿ = (Σ c_a Xᵃ)(Σ c_b Yᵇ)` with
`c_n = s^{n(n−1)} (q − q⁻¹)ⁿ / [n]!` (`rcoef`). This file proves that formula in any
`𝕜`-algebra.

-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. IV.2 (q-binomial) and VIII.2
-/

namespace QOU.Mass.QuantumSl2

variable {𝕜 : Type*} [Field 𝕜]

/-- The `p`-binomial coefficients, by the Pascal rule for `Y X = p X Y`. -/
def gauss (p : 𝕜) : ℕ → ℕ → 𝕜
  | 0, 0 => 1
  | 0, _ + 1 => 0
  | _ + 1, 0 => 1
  | n + 1, k + 1 => gauss p n k + p ^ (k + 1) * gauss p n (k + 1)

theorem gauss_zero_right (p : 𝕜) (n : ℕ) : gauss p n 0 = 1 := by
  cases n <;> rfl

theorem gauss_of_lt (p : 𝕜) {n k : ℕ} (h : n < k) : gauss p n k = 0 := by
  induction n generalizing k with
  | zero => obtain ⟨k, rfl⟩ : ∃ j, k = j + 1 := ⟨k - 1, by omega⟩; rfl
  | succ n ih =>
    obtain ⟨k, rfl⟩ : ∃ j, k = j + 1 := ⟨k - 1, by omega⟩
    simp only [gauss, ih (by omega : n < k), ih (by omega : n < k + 1), mul_zero, add_zero]

variable {A : Type*} [Ring A] [Algebra 𝕜 A]

/-- `Y Xᵏ = pᵏ Xᵏ Y`. -/
theorem comm_pow {X Y : A} {p : 𝕜} (h : Y * X = p • (X * Y)) (k : ℕ) :
    Y * X ^ k = p ^ k • (X ^ k * Y) := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [pow_succ, ← mul_assoc, ih, smul_mul_assoc, mul_assoc, h, mul_smul_comm, smul_smul,
      ← mul_assoc, pow_succ]

/-- **The q-binomial theorem** for `Y X = p X Y`. -/
theorem qbinom_pow {X Y : A} {p : 𝕜} (h : Y * X = p • (X * Y)) (n : ℕ) :
    (X + Y) ^ n = ∑ k ∈ Finset.range (n + 1), gauss p n k • (X ^ k * Y ^ (n - k)) := by
  induction n with
  | zero => simp [gauss]
  | succ n ih =>
    rw [pow_succ', ih, add_mul, Finset.mul_sum, Finset.mul_sum]
    simp only [mul_smul_comm, ← mul_assoc, comm_pow h, smul_mul_assoc, smul_smul]
    have e1 : ∀ k ∈ Finset.range (n + 1),
        gauss p n k • (X * X ^ k * Y ^ (n - k)) = gauss p n k • (X ^ (k + 1) * Y ^ (n - k)) := by
      intro k _; rw [← pow_succ']
    have e2 : ∀ k ∈ Finset.range (n + 1),
        (gauss p n k * p ^ k) • (X ^ k * Y * Y ^ (n - k))
          = (gauss p n k * p ^ k) • (X ^ k * Y ^ (n + 1 - k)) := by
      intro k hk; have := Finset.mem_range.mp hk
      rw [mul_assoc, ← pow_succ', show n - k + 1 = n + 1 - k by omega]
    rw [Finset.sum_congr rfl e1, Finset.sum_congr rfl e2,
      Finset.sum_range_succ' (fun k => gauss p (n + 1) k • (X ^ k * Y ^ (n + 1 - k))),
      Finset.sum_range_succ' (fun k => (gauss p n k * p ^ k) • (X ^ k * Y ^ (n + 1 - k)))]
    simp only [gauss, add_smul, Finset.sum_add_distrib, gauss_zero_right, pow_zero, mul_one,
      Nat.sub_zero, Nat.add_sub_add_right]
    rw [Finset.sum_range_succ (fun k => (p ^ (k + 1) * gauss p n (k + 1)) • _),
      gauss_of_lt p (Nat.lt_succ_self n), mul_zero, zero_smul, add_zero]
    have e3 : ∀ k ∈ Finset.range n, (gauss p n (k + 1) * p ^ (k + 1)) • (X ^ (k + 1) * Y ^ (n - k))
        = (p ^ (k + 1) * gauss p n (k + 1)) • (X ^ (k + 1) * Y ^ (n - k)) := by
      intro k _; rw [mul_comm]
    rw [Finset.sum_congr rfl e3]
    abel

theorem gauss_self (p : 𝕜) (n : ℕ) : gauss p n n = 1 := by
  induction n with
  | zero => rfl
  | succ n ih => simp only [gauss, ih, gauss_of_lt p (Nat.lt_succ_self n), mul_zero, add_zero]

/-- `q⁻¹ [a+b+2] = q^b [a+1] + q^{−(a+2)} [b+1]`. -/
theorem qint_split (q : 𝕜) (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0) (a b : ℕ) :
    q⁻¹ * qint q (a + b + 2) = q ^ b * qint q (a + 1) + q⁻¹ ^ (a + 2) * qint q (b + 1) := by
  have h1 : q ^ 2 - 1 ≠ 0 := by
    intro h; apply hq2; field_simp; linear_combination h
  unfold qint
  simp only [inv_pow]
  field_simp
  ring

theorem rcoef_zero (s : 𝕜) : rcoef s 0 = 1 := by simp [rcoef, qfact]

/-- **The q-exponential coefficients multiply by the `q⁻²`-binomial:**
`c_a c_b = [a+b choose a]_{q⁻²} c_{a+b}`, when `[k] ≠ 0` for `1 ≤ k ≤ a + b`. -/
theorem rcoef_mul (s : 𝕜) (hs : s ≠ 0) (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0) :
    ∀ (b a : ℕ), (∀ k, 0 < k → k ≤ a + b → qint (s ^ 2) k ≠ 0) →
      rcoef s a * rcoef s b = gauss ((s ^ 2)⁻¹ ^ 2) (a + b) a * rcoef s (a + b) := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  intro b
  induction b with
  | zero => intro a _; simp [rcoef_zero, gauss_self]
  | succ b ihb =>
    intro a
    induction a with
    | zero => intro _; simp [rcoef_zero, gauss_zero_right]
    | succ a iha =>
      intro hint
      have h1 := iha (fun k hk h => hint k hk (by omega))
      have h2 := ihb (a + 1) (fun k hk h => hint k hk (by omega))
      rw [show a + 1 + (b + 1) = (a + b + 1) + 1 by ring] at hint ⊢
      rw [show a + (b + 1) = a + b + 1 by ring] at h1
      rw [show a + 1 + b = a + b + 1 by ring] at h2
      rw [show gauss ((s ^ 2)⁻¹ ^ 2) (a + b + 1 + 1) (a + 1)
          = gauss ((s ^ 2)⁻¹ ^ 2) (a + b + 1) a
            + ((s ^ 2)⁻¹ ^ 2) ^ (a + 1) * gauss ((s ^ 2)⁻¹ ^ 2) (a + b + 1) (a + 1) from rfl]
      have ha := rcoef_succ s a (hint (a + 1) (by omega) (by omega))
      have hb := rcoef_succ s b (hint (b + 1) (by omega) (by omega))
      have hn := rcoef_succ s (a + b + 1) (hint (a + b + 1 + 1) (by omega) (by omega))
      have hA := hint (a + 1) (by omega) (by omega)
      have hB := hint (b + 1) (by omega) (by omega)
      have hN := hint (a + b + 1 + 1) (by omega) (by omega)
      have hsplit := qint_split (s ^ 2) hq hq2 a b
      rw [show a + b + 2 = a + b + 1 + 1 by ring] at hsplit
      -- express c_{a+1}, c_{b+1}, c_{a+b+2} through the lower ones
      have ea : rcoef s (a + 1) = rcoef s a * (s ^ 2) ^ a * (s ^ 2 - (s ^ 2)⁻¹) / qint (s ^ 2) (a + 1) :=
        by rw [eq_div_iff hA, ha]
      have eb : rcoef s (b + 1) = rcoef s b * (s ^ 2) ^ b * (s ^ 2 - (s ^ 2)⁻¹) / qint (s ^ 2) (b + 1) :=
        by rw [eq_div_iff hB, hb]
      have en : rcoef s (a + b + 1 + 1)
          = rcoef s (a + b + 1) * (s ^ 2) ^ (a + b + 1) * (s ^ 2 - (s ^ 2)⁻¹) / qint (s ^ 2) (a + b + 1 + 1) :=
        by rw [eq_div_iff hN, hn]
      rw [ea] at h2; rw [eb] at h1
      rw [en, ea, eb]
      set G1 := gauss ((s ^ 2)⁻¹ ^ 2) (a + b + 1) a
      set G2 := gauss ((s ^ 2)⁻¹ ^ 2) (a + b + 1) (a + 1)
      set C := rcoef s (a + b + 1)
      have e : (G1 + ((s ^ 2)⁻¹ ^ 2) ^ (a + 1) * G2) * (C * (s ^ 2) ^ (a + b + 1) * (s ^ 2 - (s ^ 2)⁻¹)
            / qint (s ^ 2) (a + b + 1 + 1))
          = (G1 * C + ((s ^ 2)⁻¹ ^ 2) ^ (a + 1) * (G2 * C)) * ((s ^ 2) ^ (a + b + 1)
            * (s ^ 2 - (s ^ 2)⁻¹) / qint (s ^ 2) (a + b + 1 + 1)) := by ring
      rw [e, ← h1, ← h2]
      set x := qint (s ^ 2) (a + 1)
      set y := qint (s ^ 2) (b + 1)
      set z := qint (s ^ 2) (a + b + 1 + 1)
      set Q := s ^ 2
      simp only [inv_pow] at hsplit ⊢
      field_simp
      field_simp at hsplit
      linear_combination (rcoef s a * rcoef s b * (Q ^ 2 - 1) ^ 2 * Q ^ (2 * a + b)) * hsplit

/-- A double sum over `a, b ≤ L` of terms vanishing unless `a, b ≤ M` reduces to `a, b ≤ M`. -/
theorem sum_tri_eq_sum_sq {B : Type*} [AddCommMonoid B] (g : ℕ → ℕ → B) (M L : ℕ) (hML : 2 * M ≤ L)
    (hg : ∀ a b, (M < a ∨ M < b) → g a b = 0) :
    ∑ a ∈ Finset.range (L + 1), ∑ b ∈ Finset.range (L + 1 - a), g a b
      = ∑ a ∈ Finset.range (M + 1), ∑ b ∈ Finset.range (M + 1), g a b := by
  have step1 : ∀ a ∈ Finset.range (L + 1),
      ∑ b ∈ Finset.range (L + 1 - a), g a b = ∑ b ∈ Finset.range (M + 1), g a b := by
    intro a ha
    by_cases haM : a ≤ M
    · refine (Finset.sum_subset (Finset.range_mono (by omega)) ?_).symm
      intro b _ hb
      exact hg a b (Or.inr (by simpa using hb))
    · rw [Finset.sum_eq_zero fun b _ => hg a b (Or.inl (by omega)),
        Finset.sum_eq_zero fun b _ => hg a b (Or.inl (by omega))]
  rw [Finset.sum_congr rfl step1]
  refine (Finset.sum_subset (Finset.range_mono (by omega)) ?_).symm
  intro a _ ha
  exact Finset.sum_eq_zero fun b _ => hg a b (Or.inl (by simpa using ha))

variable (s : 𝕜)

/-- **The q-exponential product formula.** If `Y X = q⁻² X Y` and `X^{M+1} = Y^{M+1} = 0`, then
`(Σ_{a ≤ M} c_a Xᵃ)(Σ_{b ≤ M} c_b Yᵇ) = Σ_{n ≤ 2M} c_n (X + Y)ⁿ`. -/
theorem qexp_mul (hs : s ≠ 0) (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0) {X Y : A}
    (h : Y * X = ((s ^ 2)⁻¹ ^ 2) • (X * Y)) (M : ℕ) (hX : X ^ (M + 1) = 0) (hY : Y ^ (M + 1) = 0)
    (hint : ∀ k, 0 < k → k ≤ 2 * M → qint (s ^ 2) k ≠ 0) :
    (∑ a ∈ Finset.range (M + 1), rcoef s a • X ^ a) * (∑ b ∈ Finset.range (M + 1), rcoef s b • Y ^ b)
      = ∑ n ∈ Finset.range (2 * M + 1), rcoef s n • (X + Y) ^ n := by
  have hterm : ∀ n ∈ Finset.range (2 * M + 1), rcoef s n • (X + Y) ^ n
      = ∑ k ∈ Finset.range (n + 1), (rcoef s k * rcoef s (n - k)) • (X ^ k * Y ^ (n - k)) := by
    intro n hn
    have hn' := Finset.mem_range.mp hn
    rw [qbinom_pow h, Finset.smul_sum]
    refine Finset.sum_congr rfl fun k hk => ?_
    have hk' := Finset.mem_range.mp hk
    rw [smul_smul, rcoef_mul s hs hq2 (n - k) k (fun j hj hjn => hint j hj (by omega)),
      show k + (n - k) = n by omega, mul_comm]
  rw [Finset.sum_congr rfl hterm,
    Finset.sum_range_diag_flip (2 * M + 1) (fun a b => (rcoef s a * rcoef s b) • (X ^ a * Y ^ b)),
    Finset.sum_mul_sum]
  rw [sum_tri_eq_sum_sq (fun a b => (rcoef s a * rcoef s b) • (X ^ a * Y ^ b)) M (2 * M) le_rfl]
  · refine Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun b _ => ?_
    rw [smul_mul_smul_comm]
  · intro a b hab
    rcases hab with hab | hab
    · rw [pow_eq_zero_of_le (by omega) hX, zero_mul, smul_zero]
    · rw [pow_eq_zero_of_le (by omega) hY, mul_zero, smul_zero]

end QOU.Mass.QuantumSl2
