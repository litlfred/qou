import QOU.Mass.QuantumSl2Belt

/-!
# The clasp: closed forms

Stage 3 of deriving Zheng's tangle functions (van der Veen 2008, Lemma 1). The clasp tangle
has antiparallel strands, so it is the monodromy `M = Ř′Ř` turned through 90°:
`X = (cap ⊗ 1 ⊗ 1)(1 ⊗ M ⊗ 1)(1 ⊗ 1 ⊗ cup)`. Read at the output `v_j ⊗ v_0`, the eigenvalue
of `X` on `w_j` is a sum over the support `v_k ⊗ v_{j−k}` of `w_j`, and each summand is a
single product of `q`-integers equal to van der Veen's `k`-th term (checked exactly in
`computations/whitehead_clasp_rotated_monodromy_check.py`).

This file collects the closed forms that the term identity needs.

-- Ref: [vanderveen2008] van der Veen, AGT 8 (2008) 603–624, proof of Lemma 1
-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. VII, XIV
-/

namespace QOU.Mass.QuantumSl2

open Matrix
open scoped Kronecker

variable {𝕜 : Type*} [Field 𝕜]

theorem qfact_succ (q : 𝕜) (n : ℕ) : qfact q (n + 1) = qfact q n * qint q (n + 1) := by
  unfold qfact; rw [Finset.prod_range_succ]

/-- Rising product: `[a]! · Π_{i<k} [a+i+1] = [a+k]!`. -/
theorem qfact_mul_prod_up (q : 𝕜) (a k : ℕ) :
    qfact q a * ∏ i ∈ Finset.range k, qint q (a + i + 1) = qfact q (a + k) := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [Finset.prod_range_succ, ← mul_assoc, ih, ← Nat.add_assoc, qfact_succ]

/-- Falling product: `[m−k]! · Π_{i<k} [m−i] = [m]!` for `k ≤ m`. -/
theorem qfact_mul_prod_down (q : 𝕜) (m k : ℕ) (hk : k ≤ m) :
    qfact q (m - k) * ∏ i ∈ Finset.range k, qint q (m - i) = qfact q m := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [Finset.prod_range_succ, ← ih (by omega),
      show m - k = (m - (k + 1)) + 1 by omega, qfact_succ,
      show m - (k + 1) + 1 = m - k by omega]
    ring

/-- `Σ_{i<k} (m − 2(j−1−i)) = k (m − 2j + k + 1)` for `k ≤ j`. -/
theorem sum_wt_hw (m j k : ℕ) (hk : k ≤ j) :
    ∑ i ∈ Finset.range k, wt m (j - 1 - i) = (k : ℤ) * ((m : ℤ) - 2 * j + k + 1) := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [Finset.sum_range_succ, ih (by omega)]
    unfold wt
    rw [show j - 1 - k = j - (k + 1) by omega, Nat.cast_sub hk]
    push_cast; ring

/-- **Closed form of the highest-weight coefficients** in `V_{m+1} ⊗ V_{m+1}`:
`a_k^{(j)} [m]! [m−j]! = (−1)^k q^{−k(m−2j+k+1)} [m−k]! [m−j+k]!`. -/
theorem hwCoef_closed (q : 𝕜) (hq : q ≠ 0) (m j k : ℕ) (hkj : k ≤ j) (hjm : j ≤ m)
    (hint : ∀ i < k, qint q (m - i) ≠ 0) :
    hwCoef q m m j k * qfact q m * qfact q (m - j)
      = (-1) ^ k * q ^ (-((k : ℤ) * ((m : ℤ) - 2 * j + k + 1)))
          * qfact q (m - k) * qfact q (m - j + k) := by
  have h := hwCoef_mul_prod q hq m m j k hint
  rw [sum_wt_hw m j k hkj] at h
  have hd := qfact_mul_prod_down q m k (by omega)
  have hu := qfact_mul_prod_up q (m - j) k
  rw [← hd, ← hu]
  calc hwCoef q m m j k * (qfact q (m - k) * ∏ i ∈ Finset.range k, qint q (m - i)) * qfact q (m - j)
      = (hwCoef q m m j k * ∏ i ∈ Finset.range k, qint q (m - i)) * qfact q (m - k)
          * qfact q (m - j) := by ring
    _ = _ := by rw [h]; ring

/-- Entries of `Eⁿ`: `(Eⁿ)_{a,b} = Π_{l<n} [m−a−l]` when `b = a + n`. -/
theorem irrepE_pow_entry (q : 𝕜) (m n : ℕ) (a b : Fin (m + 1)) (hab : (b : ℕ) = a + n) :
    (irrepE q m ^ n) a b = ∏ l ∈ Finset.range n, qint q (m - a - l) := by
  induction n generalizing a with
  | zero =>
    have : a = b := by ext; omega
    subst this; simp
  | succ n ih =>
    have ha : (a : ℕ) + 1 < m + 1 := by omega
    rw [pow_succ', mul_apply, Finset.sum_eq_single ⟨a + 1, ha⟩]
    · rw [ih ⟨a + 1, ha⟩ (by simp; omega), Finset.prod_range_succ']
      simp only [irrepE, if_true]
      rw [mul_comm]
      congr 1
      · refine Finset.prod_congr rfl fun l _ => ?_
        congr 1; omega
      · congr 1; omega
    · intro x _ hx
      have : irrepE q m a x = 0 := by
        simp only [irrepE]; rw [if_neg]; intro h'; apply hx; ext; simp; omega
      rw [this, zero_mul]
    · simp

/-- Entries of `Fⁿ`: `(Fⁿ)_{b,a} = Π_{l<n} [a+l+1]` when `b = a + n`. -/
theorem irrepF_pow_entry (q : 𝕜) (m n : ℕ) (a b : Fin (m + 1)) (hab : (b : ℕ) = a + n) :
    (irrepF q m ^ n) b a = ∏ l ∈ Finset.range n, qint q (a + l + 1) := by
  induction n generalizing a with
  | zero =>
    have : a = b := by ext; omega
    subst this; simp
  | succ n ih =>
    have ha : (a : ℕ) + 1 < m + 1 := by omega
    rw [pow_succ, mul_apply, Finset.sum_eq_single ⟨a + 1, ha⟩]
    · rw [ih ⟨a + 1, ha⟩ (by simp; omega), Finset.prod_range_succ']
      simp only [irrepF]
      rw [if_pos (by simp)]
      congr 1
      refine Finset.prod_congr rfl fun l _ => ?_
      congr 1; simp; omega
    · intro x _ hx
      have : irrepF q m x a = 0 := by
        simp only [irrepF]; rw [if_neg]; intro h'; apply hx; ext; simp; omega
      rw [this, mul_zero]
    · simp

end QOU.Mass.QuantumSl2
