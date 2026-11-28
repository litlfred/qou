import Mathlib.RingTheory.PowerSeries.Inverse
import Mathlib.Tactic
import QOU.Nuclear.TetIndexTriality

/-!
# QOU.QBeta.TetBlockFactorisation — the tetrahedron index is a product of two blocks

Bean `qou-vr3q`. The tetrahedron is the one-block case of the block-to-index
identity of Beem–Dimofte–Pasquetti, as quoted in GGM 2012.00062 eq (IndB):

`Ind^rot_Δ(m, ζ; q) = B_Δ(q^{m/2} ζ; q) · B_Δ(q^{m/2} ζ^{-1}; q^{-1})`,
`B_Δ(x; q) = (q x^{-1}; q)_∞`.

Read as formal series (`|q| < 1`), the `q^{-1}` block is `1/(x^{-1}; q)_∞`
(`(y; q^{-1})_∞ = 1/(q y; q)_∞`). With `I_Δ(m,e) = q^{-em/2} F(m,e)` this is

`Σ_e F(m,e) ζ^e = (q^{1-m} ζ^{-1}; q)_∞ · 1/(ζ; q)_∞`.

## What is proved

The infinite products are the limits of the finite ones. For `N` factors:

* `pN N n = [x^n] ∏_{i<N} (1 - q^i x)` (`pN_isCoeff`, a polynomial in `x`);
* `hN N n = [x^n] ∏_{i<N} 1/(1 - q^i x)` (`hN_isCoeff`, a power series in `x`).

Euler's two identities, in the form "the finite products converge":

* `X^N ∣ pN N n - (-1)^n q^{n(n-1)/2} / (q)_n` (`pN_conv`);
* `X^N ∣ hN N n - 1/(q)_n` (`hN_conv`);

and `q^{n(n-1)/2} ∣ pN N n` for every `N` (`pN_dvd`).

The main theorem `block_eq_Fc` says that the `[ζ^e q^j]` coefficient of the
`N`-factor block product, `blockF N M m e j`, equals `[q^j] F(m,e)` once
`N > |j| + cutF·(|m| + 1)` and `M ≥ cutF m j`. Here `M` truncates the sum over
`n` (the `x`-degree of the first block). Terms beyond `cutF` are zero for every
`N`, so `M` is not an approximation. `tet_block` restates it for `tetCoeff`.

Purely algebraic (formal power series over `ℤ`). No analysis, no measured value,
no fit.

-- Ref: [garoufalidis-gu-marino2023peacock] GGM 2012.00062 eq (IndB) (block form of the index, after Beem–Dimofte–Pasquetti)
-- Ref: [dimofte-gaiotto-gukov2013] DGG 1112.5179 (tetrahedron index as a ratio of q-Pochhammers)
-- Ref: [andrews1976] Andrews, The Theory of Partitions, Cor. 2.2 (Euler's identities)
-/

namespace QOU.QBeta.TetBlockFactorisation

open PowerSeries Finset QOU.QBeta.TetIndexTriality

/-! ### Finite product `∏_{i<N} (1 - q^i x)`, coefficient of `x^n` -/

/-- `pN N n = [x^n] ∏_{i<N} (1 - q^i x)`. -/
noncomputable def pN : ℕ → ℕ → PowerSeries ℤ
  | 0, n => if n = 0 then 1 else 0
  | N + 1, 0 => pN N 0
  | N + 1, n + 1 => pN N (n + 1) - X ^ N * pN N n

theorem pN_zero (N : ℕ) : pN N 0 = 1 := by
  induction N with
  | zero => simp [pN]
  | succ N ih => simp [pN, ih]

/-- Functional equation `P_N(x)(1 - q^N x) = (1 - x) P_N(qx)`, coefficient of `x^{n+1}`. -/
theorem pN_fe (N n : ℕ) :
    pN N (n + 1) * (1 - X ^ (n + 1)) = (X ^ N - X ^ n) * pN N n := by
  induction N generalizing n with
  | zero =>
    rcases n with _ | n
    · simp [pN]
    · simp [pN]
  | succ N ih =>
    rcases n with _ | n
    · simp only [pN, pN_zero]
      have h := ih 0
      simp only [pN_zero] at h
      linear_combination h
    · simp only [pN]
      have h1 := ih (n + 1)
      have h0 := ih n
      linear_combination h1 - X ^ (N + 1) * h0

/-! ### Cancelling a unit factor `1 - q^k` -/

theorem one_sub_cc {k : ℕ} (hk : 0 < k) :
    constantCoeff (1 - X ^ k : PowerSeries ℤ) = ((1 : ℤˣ) : ℤ) := by
  simp [map_sub, zero_pow hk.ne']

theorem one_sub_unit {k : ℕ} (hk : 0 < k) :
    (1 - X ^ k : PowerSeries ℤ) * invOfUnit (1 - X ^ k) 1 = 1 :=
  mul_invOfUnit _ _ (one_sub_cc hk)

theorem cancel {k : ℕ} (hk : 0 < k) {f g : PowerSeries ℤ}
    (h : f * (1 - X ^ k) = g * (1 - X ^ k)) : f = g := by
  have hu := one_sub_unit hk
  calc f = f * (1 - X ^ k) * invOfUnit (1 - X ^ k) 1 := by rw [mul_assoc, hu, mul_one]
    _ = g * (1 - X ^ k) * invOfUnit (1 - X ^ k) 1 := by rw [h]
    _ = g := by rw [mul_assoc, hu, mul_one]

theorem dvd_cancel {k a : ℕ} (hk : 0 < k) {f : PowerSeries ℤ}
    (h : X ^ a ∣ f * (1 - X ^ k)) : X ^ a ∣ f := by
  have hu := one_sub_unit hk
  have : f = f * (1 - X ^ k) * invOfUnit (1 - X ^ k) 1 := by rw [mul_assoc, hu, mul_one]
  rw [this]; exact dvd_mul_of_dvd_left h _

/-! ### Euler's first identity: `(x;q)_∞ = Σ_n (-1)^n q^{n(n-1)/2} x^n / (q)_n` -/

theorem pN_vanish (N n : ℕ) (h : N < n) : pN N n = 0 := by
  induction n with
  | zero => omega
  | succ n ih =>
    apply cancel (k := n + 1) (by omega)
    rw [pN_fe, zero_mul]
    rcases Nat.lt_or_ge N n with h' | h'
    · rw [ih h', mul_zero]
    · rw [show N = n by omega, sub_self, zero_mul]

theorem choose_two_succ (n : ℕ) : (n + 1).choose 2 = n + n.choose 2 := by
  rw [Nat.choose_succ_succ, Nat.choose_one_right]

/-- `q^{n(n-1)/2} ∣ [x^n] ∏_{i<N} (1 - q^i x)`, for every `N`. -/
theorem pN_dvd (N n : ℕ) : X ^ n.choose 2 ∣ pN N n := by
  induction n with
  | zero => simp
  | succ n ih =>
    rcases Nat.lt_or_ge N (n + 1) with h | h
    · rw [pN_vanish N (n + 1) h]; exact dvd_zero _
    · apply dvd_cancel (k := n + 1) (by omega)
      rw [pN_fe, choose_two_succ, pow_add]
      apply mul_dvd_mul _ ih
      rw [show X ^ N - X ^ n = (X : PowerSeries ℤ) ^ n * (X ^ (N - n) - 1) by
        rw [mul_sub, ← pow_add, show n + (N - n) = N by omega, mul_one]]
      exact dvd_mul_right _ _

/-- The `x^n` coefficient of `(x;q)_∞`: `(-1)^n q^{n(n-1)/2} / (q)_n`. -/
noncomputable def T (n : ℕ) : PowerSeries ℤ := (-1) ^ n * X ^ n.choose 2 * iqp n

theorem T_zero : T 0 = 1 := by simp [T, iqp_zero]

theorem T_fe (n : ℕ) : T (n + 1) * (1 - X ^ (n + 1)) = -X ^ n * T n := by
  unfold T
  rw [choose_two_succ, pow_add, iqp_pred n]
  ring

/-- **Euler's first identity, as convergence:** `X^N ∣ pN N n - T n`. -/
theorem pN_conv (N n : ℕ) : X ^ N ∣ pN N n - T n := by
  induction n with
  | zero => rw [pN_zero, T_zero, sub_self]; exact dvd_zero _
  | succ n ih =>
    apply dvd_cancel (k := n + 1) (by omega)
    have h : (pN N (n + 1) - T (n + 1)) * (1 - X ^ (n + 1))
        = X ^ N * pN N n - X ^ n * (pN N n - T n) := by
      rw [sub_mul, pN_fe, T_fe]; ring
    rw [h]
    exact dvd_sub (dvd_mul_right _ _) (dvd_mul_of_dvd_right ih _)

/-! ### Euler's second identity: `1/(x;q)_∞ = Σ_n x^n / (q)_n` -/

/-- `hN N n = [x^n] ∏_{i<N} 1/(1 - q^i x)`. -/
noncomputable def hN : ℕ → ℕ → PowerSeries ℤ
  | 0, n => if n = 0 then 1 else 0
  | N + 1, 0 => hN N 0
  | N + 1, n + 1 => hN N (n + 1) + X ^ N * hN (N + 1) n

theorem hN_zero (N : ℕ) : hN N 0 = 1 := by
  induction N with
  | zero => simp [hN]
  | succ N ih => simp [hN, ih]

/-- Functional equation `H_N(qx)(1 - q^N x) = (1 - x) H_N(x)`, coefficient of `x^{n+1}`. -/
theorem hN_fe (N n : ℕ) :
    hN N (n + 1) * (1 - X ^ (n + 1)) = hN N n * (1 - X ^ (N + n)) := by
  induction N generalizing n with
  | zero =>
    rcases n with _ | n
    · simp [hN]
    · simp [hN]
  | succ N ih =>
    have hA : ∀ n, hN (N + 1) n * (1 - X ^ N) = hN N n * (1 - X ^ (N + n)) := by
      intro n
      induction n with
      | zero => simp [hN_zero]
      | succ n ihn =>
        simp only [hN]
        have h := ih n
        linear_combination X ^ N * ihn - X ^ N * h
    simp only [hN]
    have h := ih n
    have hA' := hA n
    linear_combination h - hA'

/-- **Euler's second identity, as convergence:** `X^N ∣ hN N n - 1/(q)_n`. -/
theorem hN_conv (N n : ℕ) : X ^ N ∣ hN N n - iqp n := by
  induction n with
  | zero => rw [hN_zero, iqp_zero, sub_self]; exact dvd_zero _
  | succ n ih =>
    apply dvd_cancel (k := n + 1) (by omega)
    have h : (hN N (n + 1) - iqp (n + 1)) * (1 - X ^ (n + 1))
        = (hN N n - iqp n) - X ^ N * (X ^ n * hN N n) := by
      rw [sub_mul, hN_fe, ← iqp_pred n, pow_add]; ring
    rw [h]
    exact dvd_sub ih (dvd_mul_right _ _)

/-! ### The block product and the index -/

/-- `[ζ^e q^j]` of `(q^{1-m} ζ^{-1}; q)_N · 1/(ζ; q)_N`, the `n`-sum cut at `M`. -/
noncomputable def blockF (N M : ℕ) (m e j : ℤ) : ℤ :=
  ∑ n ∈ range M, if 0 ≤ (n : ℤ) + e then
    cz (pN N n * hN N ((n : ℤ) + e).toNat) (j - n + n * m) else 0

theorem choose_two_eq (n : ℕ) : ((n.choose 2 : ℕ) : ℤ) = tri n - n := by
  induction n with
  | zero => simp [tri]
  | succ n ih => rw [choose_two_succ]; simp only [tri]; push_cast; linarith

theorem cz_X_pow_mul (a : ℕ) (G : PowerSeries ℤ) (i : ℤ) :
    cz (X ^ a * G) i = cz G (i - a) := by
  unfold cz
  rw [mul_comm, coeff_mul_X_pow']
  by_cases hi : 0 ≤ i
  · by_cases ha : (a : ℤ) ≤ i
    · rw [if_pos hi, if_pos (by omega), if_pos (by omega),
        show (i - (a : ℤ)).toNat = i.toNat - a by omega]
    · rw [if_pos hi, if_neg (by omega), if_neg (by omega)]
  · rw [if_neg hi, if_neg (by omega)]

theorem cz_eq_of_dvd {N : ℕ} {F G : PowerSeries ℤ} (h : X ^ N ∣ F - G) {i : ℤ}
    (hi : i < N) : cz F i = cz G i := by
  unfold cz
  split_ifs with h0
  · have := (X_pow_dvd_iff.mp h) i.toNat (by omega)
    rw [map_sub] at this; linarith
  · rfl

/-- One term of the block sum agrees with the index term once `N` is past its degree. -/
theorem block_term (N : ℕ) (m j : ℤ) (n : ℕ) (k : ℕ) (hN' : j - n + n * m < N) :
    cz (pN N n * hN N k) (j - n + n * m)
      = (-1) ^ n * cz (iqp n * iqp k) (j - E m n) := by
  have hd : X ^ N ∣ pN N n * hN N k - T n * iqp k := by
    have : pN N n * hN N k - T n * iqp k
        = (pN N n - T n) * hN N k + T n * (hN N k - iqp k) := by ring
    rw [this]
    exact dvd_add (dvd_mul_of_dvd_left (pN_conv N n) _)
      (dvd_mul_of_dvd_right (hN_conv N k) _)
  rw [cz_eq_of_dvd hd hN']
  have hT : T n * iqp k = (-1) ^ n * (X ^ n.choose 2 * (iqp n * iqp k)) := by
    unfold T; ring
  rw [hT]
  have hc : cz ((-1) ^ n * (X ^ n.choose 2 * (iqp n * iqp k))) (j - n + n * m)
      = (-1) ^ n * cz (X ^ n.choose 2 * (iqp n * iqp k)) (j - n + n * m) := by
    unfold cz
    split_ifs
    · rw [show ((-1 : PowerSeries ℤ) ^ n) = C ((-1 : ℤ) ^ n) by simp, coeff_C_mul]
    · ring
  rw [hc, cz_X_pow_mul, choose_two_eq]
  unfold E
  congr 2; ring

/-- Past the cut-off, every block term vanishes, for every `N`. -/
theorem block_far (N : ℕ) (m j : ℤ) (n k : ℕ) (hn : cutF m j ≤ n) :
    cz (pN N n * hN N k) (j - n + n * m) = 0 := by
  have hj := E_gt m j n hn
  obtain ⟨g, hg⟩ := pN_dvd N n
  rw [hg, mul_assoc, cz_X_pow_mul, cz_neg]
  have := choose_two_eq n
  unfold E at hj
  omega

/-- **The tetrahedron index is the block product** (formal form of GGM eq (IndB) for
one tetrahedron): for `N > |j| + cutF·(|m|+1)` and `M ≥ cutF`, the `[ζ^e q^j]`
coefficient of `(q^{1-m} ζ^{-1}; q)_N / (ζ; q)_N` is `[q^j] F(m,e)`. -/
theorem block_eq_Fc (N M : ℕ) (m e j : ℤ)
    (hN : |j| + (cutF m j : ℤ) * (|m| + 1) < N) (hM : cutF m j ≤ M) :
    blockF N M m e j = Fc m e j := by
  rw [Fc_sum m e j M hM]
  unfold blockF
  apply Finset.sum_congr rfl
  intro n _
  unfold tm
  split_ifs with h
  · rcases Nat.lt_or_ge n (cutF m j) with hn | hn
    · apply block_term
      have h1 : (n : ℤ) * m ≤ n * |m| :=
        mul_le_mul_of_nonneg_left (le_abs_self m) (by positivity)
      have h2 : (n : ℤ) * |m| ≤ cutF m j * |m| :=
        mul_le_mul_of_nonneg_right (by exact_mod_cast hn.le) (abs_nonneg m)
      have h3 := le_abs_self j
      have h4 : (n : ℤ) < cutF m j := by exact_mod_cast hn
      have h5 : (cutF m j : ℤ) * (|m| + 1) = cutF m j * |m| + cutF m j := by ring
      have h6 : (0 : ℤ) ≤ n := by positivity
      linarith
    · rw [block_far N m j n _ hn, cz_neg _ (by have := E_gt m j n hn; omega), mul_zero]
  · rfl

open QOU.QBeta.TetIndexDegree in
/-- The same statement for `tetCoeff m e k = [t^k] I_Δ(m,e)`, `t = q^{1/2}`. -/
theorem tet_block (N M : ℕ) (m e k : ℤ)
    (hN : |(k + e * m) / 2| + (cutF m ((k + e * m) / 2) : ℤ) * (|m| + 1) < N)
    (hM : cutF m ((k + e * m) / 2) ≤ M) :
    tetCoeff m e k = if Even (k + e * m) then blockF N M m e ((k + e * m) / 2) else 0 := by
  rw [tetCoeff_eq, block_eq_Fc N M m e _ hN hM]

/-! ### `pN` and `hN` are the coefficients of the finite products -/

/-- `pN N n` is the `x^n` coefficient of the polynomial `∏_{i<N} (1 - q^i x)`. -/
theorem pN_isCoeff (N n : ℕ) :
    (∏ i ∈ range N, (1 - Polynomial.C ((PowerSeries.X : PowerSeries ℤ) ^ i)
      * Polynomial.X)).coeff n = pN N n := by
  induction N generalizing n with
  | zero => rcases n with _ | n <;> simp [pN, Polynomial.coeff_one]
  | succ N ih =>
    rw [prod_range_succ, mul_sub, mul_one, Polynomial.coeff_sub, mul_left_comm,
      Polynomial.coeff_C_mul]
    rcases n with _ | n
    · rw [Polynomial.coeff_mul_X_zero, mul_zero, sub_zero, ih]; rfl
    · rw [Polynomial.coeff_mul_X, ih, ih]; rfl

/-- `hN N` is the `x`-coefficient sequence of `1 / ∏_{i<N} (1 - q^i x)`. -/
theorem hN_isCoeff (N : ℕ) :
    PowerSeries.mk (hN N) * ∏ i ∈ range N, (1 - PowerSeries.C ((PowerSeries.X : PowerSeries ℤ) ^ i)
      * PowerSeries.X) = 1 := by
  induction N with
  | zero =>
    ext n; rcases n with _ | n <;> simp [hN, PowerSeries.coeff_one]
  | succ N ih =>
    have hs : PowerSeries.mk (hN (N + 1)) * (1 - PowerSeries.C ((PowerSeries.X : PowerSeries ℤ) ^ N)
        * PowerSeries.X) = PowerSeries.mk (hN N) := by
      ext n
      rw [mul_sub, mul_one, map_sub, mul_left_comm, PowerSeries.coeff_C_mul]
      rcases n with _ | n
      · rw [PowerSeries.coeff_zero_mul_X, mul_zero, sub_zero, PowerSeries.coeff_mk,
          PowerSeries.coeff_mk, hN_zero, hN_zero]
      · rw [PowerSeries.coeff_succ_mul_X, PowerSeries.coeff_mk, PowerSeries.coeff_mk,
          PowerSeries.coeff_mk]
        simp only [hN]; ring_nf
    rw [prod_range_succ, mul_comm (∏ i ∈ range N, _) _, ← mul_assoc, hs, ih]

end QOU.QBeta.TetBlockFactorisation
