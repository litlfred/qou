import Mathlib.RingTheory.PowerSeries.Inverse
import Mathlib.Tactic
import QOU.Nuclear.TetIndexDegree

/-!
# QOU.QBeta.TetIndexTriality — triality of the tetrahedron index, proved

Bean `qou-vr3q`. Removes the one cited input of `QOU.QBeta.TetIndexDegree`:
Garoufalidis's triality (1208.1663 Thm 3.2(c), Prop prop.S3)
`I_Δ(m,e) = (-q^{1/2})^{-e} I_Δ(e,-e-m)`.

## Route (1208.1663 §3–4, made elementary)

Write `I_Δ(m,e) = q^{-em/2} F(m,e)` with
`F(m,e) = Σ_{n ≥ (-e)₊} (-1)ⁿ q^{n(n+1)/2 - nm} / ((q)_n (q)_{n+e}) ∈ ℤ((q))`.
Coefficientwise (`Fc m e j = [q^j] F(m,e)`) the two recursions of the paper,
eq rec1 and eq rec2, read

* `Rec1`: `F(m,e) = F(m+1,e) + q^{-m} F(m,e+1)`,
* `Rec2`: `F(m,e) = q^{e} F(m-1,e) + F(m,e-1)`.

`Rec2` holds summand by summand. `Rec1` holds by telescoping, with certificate
`G(n) = (-1)^{n+1} q^{n(n+1)/2 - nm - n} / ((q)_{n-1} (q)_{n+e})`.

Then (i) a solution of both recursions is determined by `F(0,0)` and `F(0,1)`,
using only additions and shifts (`unique_of_rec`); (ii) the transform
`(SF)(m,e) = (-1)^e q^{e(e-1)/2 + em} F(e,-e-m)` maps solutions to solutions;
(iii) every solution has `F(0,1) = -F(1,-1)`, so `SF` and `F` agree at `(0,0)`
and `(0,1)`. Hence `SF = F`, which is triality.

No measured value enters. No fit.

-- Ref: [garoufalidis2016-3d-index] Garoufalidis 1208.1663 (eq ID, eq rec1, eq rec2, Thm 3.2, Prop prop.S3)
-/

namespace QOU.QBeta.TetIndexTriality

open PowerSeries Finset

/-! ### `(q)_n` and its inverse -/

/-- `(q)_n = ∏_{i=1}^n (1 - q^i)`. -/
noncomputable def qp : ℕ → PowerSeries ℤ
  | 0 => 1
  | n + 1 => qp n * (1 - X ^ (n + 1))

theorem qp_cc (n : ℕ) : constantCoeff (qp n) = 1 := by
  induction n with
  | zero => simp [qp]
  | succ n ih => simp [qp, ih]

/-- `1/(q)_n`. -/
noncomputable def iqp (n : ℕ) : PowerSeries ℤ := invOfUnit (qp n) 1

theorem qp_mul_iqp (n : ℕ) : qp n * iqp n = 1 :=
  mul_invOfUnit _ _ (by simp [qp_cc])

theorem iqp_zero : iqp 0 = 1 := by
  have h := qp_mul_iqp 0
  simpa [qp] using h

theorem iqp_pred (n : ℕ) : iqp n = iqp (n + 1) * (1 - X ^ (n + 1)) := by
  have h := qp_mul_iqp (n + 1)
  have h0 := qp_mul_iqp n
  simp only [qp] at h
  calc iqp n = iqp n * (qp n * (1 - X ^ (n + 1)) * iqp (n + 1)) := by rw [h, mul_one]
    _ = (qp n * iqp n) * (iqp (n + 1) * (1 - X ^ (n + 1))) := by ring
    _ = iqp (n + 1) * (1 - X ^ (n + 1)) := by rw [h0, one_mul]

/-! ### Coefficients at integer index -/

/-- `[q^i] G`, zero for `i < 0`. -/
noncomputable def cz (G : PowerSeries ℤ) (i : ℤ) : ℤ :=
  if 0 ≤ i then coeff i.toNat G else 0

theorem cz_neg (G : PowerSeries ℤ) {i : ℤ} (h : i < 0) : cz G i = 0 := by
  simp [cz, not_le.mpr h]

theorem cz_mul_sub (G : PowerSeries ℤ) (a : ℕ) (i : ℤ) :
    cz (G * (1 - X ^ a)) i = cz G i - cz G (i - a) := by
  unfold cz
  rw [mul_sub, mul_one, map_sub, coeff_mul_X_pow']
  by_cases hi : 0 ≤ i
  · by_cases ha : (a : ℤ) ≤ i
    · rw [if_pos hi, if_pos hi, if_pos (by omega), if_pos (by omega),
        show (i - (a : ℤ)).toNat = i.toNat - a by omega]
    · rw [if_pos hi, if_pos hi, if_neg (by omega), if_neg (by omega)]
  · rw [if_neg hi, if_neg hi, if_neg (by omega)]; ring

/-! ### The coefficient functions `Fc m e j = [q^j] F(m,e)` -/

/-- `n(n+1)/2`. -/
def tri : ℕ → ℤ
  | 0 => 0
  | n + 1 => tri n + (n + 1)

theorem two_tri (n : ℕ) : 2 * tri n = (n : ℤ) * (n + 1) := by
  induction n with
  | zero => simp [tri]
  | succ n ih => simp only [tri]; push_cast; nlinarith

/-- Exponent of the `n`-th summand of `F(m,e)`: `n(n+1)/2 - nm`. -/
def E (m : ℤ) (n : ℕ) : ℤ := tri n - n * m

/-- `[q^j]` of the `n`-th summand of `F(m,e)`. -/
noncomputable def tm (m e j : ℤ) (n : ℕ) : ℤ :=
  if 0 ≤ (n : ℤ) + e then (-1) ^ n * cz (iqp n * iqp ((n : ℤ) + e).toNat) (j - E m n) else 0

/-- Cut-off for the `n`-sum. -/
def cutF (m j : ℤ) : ℕ := (2 * |m| + |j| + 2).toNat

theorem E_gt (m j : ℤ) (n : ℕ) (hn : cutF m j ≤ n) : j < E m n := by
  have hc : 2 * |m| + |j| + 2 ≤ (n : ℤ) := by
    have := Int.self_le_toNat (2 * |m| + |j| + 2); unfold cutF at hn; omega
  have h2 := two_tri n
  have hm : -(↑n * m) ≥ -(↑n * |m|) := by
    have h1 := le_abs_self m
    have h3 : (0 : ℤ) ≤ n := by positivity
    nlinarith
  have hj := le_abs_self j
  have ha := abs_nonneg m
  have hjj := abs_nonneg j
  have hn0 : (0 : ℤ) ≤ n := by positivity
  have p1 := mul_le_mul_of_nonneg_left (show |j| + 2 ≤ (n : ℤ) - 2 * |m| by linarith) hn0
  unfold E; nlinarith

theorem tm_far (m e j : ℤ) (n : ℕ) (hn : cutF m j ≤ n) : tm m e j n = 0 := by
  unfold tm; split_ifs
  · rw [cz_neg _ (by have := E_gt m j n hn; omega), mul_zero]
  · rfl

/-- `Fc m e j = [q^j] F(m,e)`. -/
noncomputable def Fc (m e j : ℤ) : ℤ := ∑ n ∈ range (cutF m j), tm m e j n

theorem Fc_sum (m e j : ℤ) (N : ℕ) (hN : cutF m j ≤ N) :
    Fc m e j = ∑ n ∈ range N, tm m e j n := by
  unfold Fc
  apply Finset.sum_subset (Finset.range_mono hN)
  intro n hn hn'
  exact tm_far m e j n (by simpa using hn')

/-! ### Recursion `Rec2`, summand by summand -/

theorem E_pred (m : ℤ) (n : ℕ) : E (m - 1) n = E m n + n := by unfold E; ring

theorem tm_rec2 (m e j : ℤ) (n : ℕ) :
    tm m e j n = tm (m - 1) e (j - e) n + tm m (e - 1) j n := by
  unfold tm
  rw [E_pred]
  by_cases h0 : 0 ≤ (n : ℤ) + e
  · rw [if_pos h0, if_pos h0]
    by_cases h1 : 0 ≤ (n : ℤ) + (e - 1)
    · rw [if_pos h1]
      obtain ⟨N, hN⟩ : ∃ N : ℕ, ((n : ℤ) + e).toNat = N + 1 := ⟨((n : ℤ) + e).toNat - 1, by omega⟩
      have hN' : ((n : ℤ) + (e - 1)).toNat = N := by omega
      rw [hN, hN', iqp_pred N, ← mul_assoc, cz_mul_sub]
      have : j - e - (E m n + n) = j - E m n - ((N + 1 : ℕ) : ℤ) := by push_cast; omega
      rw [this]; ring
    · rw [if_neg h1, add_zero]
      congr 2; omega
  · rw [if_neg h0, if_neg h0, if_neg (by omega)]; ring

/-- **`Rec2`** (1208.1663 eq rec2): `F(m,e) = q^{e} F(m-1,e) + F(m,e-1)`. -/
theorem Fc_rec2 (m e j : ℤ) : Fc m e j = Fc (m - 1) e (j - e) + Fc m (e - 1) j := by
  set N := cutF m j + cutF (m - 1) (j - e)
  rw [Fc_sum m e j N (by omega), Fc_sum (m - 1) e (j - e) N (by omega),
    Fc_sum m (e - 1) j N (by omega), ← Finset.sum_add_distrib]
  exact Finset.sum_congr rfl fun n _ => tm_rec2 m e j n

/-! ### Recursion `Rec1`, by telescoping -/

theorem E_succ_m (m : ℤ) (n : ℕ) : E (m + 1) n = E m n - n := by unfold E; ring

theorem E_succ_n (m : ℤ) (n : ℕ) : E m (n + 1) = E m n + (n + 1) - m := by
  unfold E; simp only [tri]; push_cast; ring

/-- The telescoping certificate: `[q^j]` of
`G(n) = (-1)^{n+1} q^{n(n+1)/2 - nm - n} / ((q)_{n-1} (q)_{n+e})`. -/
noncomputable def gc (m e j : ℤ) (n : ℕ) : ℤ :=
  if 1 ≤ n ∧ 0 ≤ (n : ℤ) + e then
    (-1) ^ (n + 1) * cz (iqp (n - 1) * iqp ((n : ℤ) + e).toNat) (j - E m n + n)
  else 0

theorem gc_succ_val (m e j : ℤ) (n K : ℕ) (hK : ((n : ℤ) + 1 + e).toNat = K)
    (hA : 0 ≤ (n : ℤ) + 1 + e) :
    gc m e j (n + 1) = (-1) ^ n * cz (iqp n * iqp K) (j - E m n + m) := by
  unfold gc
  rw [if_pos ⟨by omega, by push_cast; omega⟩, Nat.add_sub_cancel,
    show (((n + 1 : ℕ) : ℤ) + e).toNat = K by omega,
    show j - E m (n + 1) + ((n + 1 : ℕ) : ℤ) = j - E m n + m by rw [E_succ_n]; push_cast; ring]
  ring

theorem tm_rec1 (m e j : ℤ) (n : ℕ) :
    tm (m + 1) e j n + tm m (e + 1) (j + m) n - tm m e j n = gc m e j (n + 1) - gc m e j n := by
  by_cases hA : 0 ≤ (n : ℤ) + e
  · obtain ⟨K, hK⟩ : ∃ K : ℕ, ((n : ℤ) + e).toNat = K := ⟨_, rfl⟩
    have key : ∀ i, cz (iqp n * iqp K) i
        = cz (iqp n * iqp (K + 1)) i - cz (iqp n * iqp (K + 1)) (i - ((K + 1 : ℕ) : ℤ)) := by
      intro i; rw [iqp_pred K, ← mul_assoc, cz_mul_sub]
    have t1 : tm (m + 1) e j n = (-1) ^ n * (cz (iqp n * iqp (K + 1)) (j - E m n + n)
        - cz (iqp n * iqp (K + 1)) (j - E m n + n - ((K + 1 : ℕ) : ℤ))) := by
      unfold tm; rw [if_pos hA, hK, key, E_succ_m, show j - (E m n - n) = j - E m n + n by ring]
    have t2 : tm m (e + 1) (j + m) n = (-1) ^ n * cz (iqp n * iqp (K + 1)) (j - E m n + m) := by
      unfold tm
      rw [if_pos (by omega), show ((n : ℤ) + (e + 1)).toNat = K + 1 by omega,
        show j + m - E m n = j - E m n + m by ring]
    have t3 : tm m e j n = (-1) ^ n * (cz (iqp n * iqp (K + 1)) (j - E m n)
        - cz (iqp n * iqp (K + 1)) (j - E m n - ((K + 1 : ℕ) : ℤ))) := by
      unfold tm; rw [if_pos hA, hK, key]
    have t4 := gc_succ_val m e j n (K + 1) (by omega) (by omega)
    rw [t1, t2, t3, t4]
    by_cases hn : n = 0
    · subst hn
      have : gc m e j 0 = 0 := by unfold gc; simp
      rw [this]; ring_nf
    · have hn1 : n - 1 + 1 = n := by omega
      have t5 : gc m e j n = (-1) ^ (n + 1) * (cz (iqp n * iqp (K + 1)) (j - E m n + n)
          - cz (iqp n * iqp (K + 1)) (j - E m n + n - ((K + 1 : ℕ) : ℤ))
          - cz (iqp n * iqp (K + 1)) (j - E m n + n - (n : ℤ))
          + cz (iqp n * iqp (K + 1)) (j - E m n + n - (n : ℤ) - ((K + 1 : ℕ) : ℤ))) := by
        unfold gc
        rw [if_pos ⟨by omega, hA⟩, hK, iqp_pred (n - 1), hn1, iqp_pred K,
          show iqp n * (1 - X ^ n) * (iqp (K + 1) * (1 - X ^ (K + 1)))
            = iqp n * iqp (K + 1) * (1 - X ^ (K + 1)) * (1 - X ^ n) by ring,
          cz_mul_sub, cz_mul_sub, cz_mul_sub]
        ring
      rw [t5]; ring_nf
  · have h1 : tm (m + 1) e j n = 0 := by unfold tm; rw [if_neg hA]
    have h3 : tm m e j n = 0 := by unfold tm; rw [if_neg hA]
    have h5 : gc m e j n = 0 := by unfold gc; rw [if_neg (by omega)]
    rw [h1, h3, h5]
    by_cases hB : (n : ℤ) + e = -1
    · have t2 : tm m (e + 1) (j + m) n = (-1) ^ n * cz (iqp n * iqp 0) (j - E m n + m) := by
        unfold tm
        rw [if_pos (by omega), show ((n : ℤ) + (e + 1)).toNat = 0 by omega,
          show j + m - E m n = j - E m n + m by ring]
      rw [t2, gc_succ_val m e j n 0 (by omega) (by omega)]; ring
    · have t2 : tm m (e + 1) (j + m) n = 0 := by unfold tm; rw [if_neg (by omega)]
      have t4 : gc m e j (n + 1) = 0 := by unfold gc; rw [if_neg (by push_cast; omega)]
      rw [t2, t4]; ring

/-- **`Rec1`** (1208.1663 eq rec1): `F(m,e) = F(m+1,e) + q^{-m} F(m,e+1)`. -/
theorem Fc_rec1 (m e j : ℤ) : Fc m e j = Fc (m + 1) e j + Fc m (e + 1) (j + m) := by
  set N := cutF m j + cutF (m + 1) j + cutF m (j + m) + 1
  rw [Fc_sum m e j N (by omega), Fc_sum (m + 1) e j N (by omega),
    Fc_sum m (e + 1) (j + m) N (by omega)]
  have htel : ∑ n ∈ range N, (tm (m + 1) e j n + tm m (e + 1) (j + m) n - tm m e j n)
      = gc m e j N - gc m e j 0 := Finset.sum_range_sub (gc m e j) N |>.symm ▸
        (Finset.sum_congr rfl fun n _ => tm_rec1 m e j n)
  have hg0 : gc m e j 0 = 0 := by unfold gc; simp
  have hgN : gc m e j N = 0 := by
    unfold gc; split_ifs
    · rw [cz_neg _ (by have := E_gt (m + 1) j N (by omega); rw [E_succ_m] at this; omega),
        mul_zero]
    · rfl
  rw [Finset.sum_sub_distrib, Finset.sum_add_distrib, hg0, hgN] at htel
  linarith

/-! ### Uniqueness of solutions of `Rec1` + `Rec2` -/

/-- `Rec1` for a coefficient table. -/
def R1 (f : ℤ → ℤ → ℤ → ℤ) : Prop := ∀ m e j, f m e j = f (m + 1) e j + f m (e + 1) (j + m)

/-- `Rec2` for a coefficient table. -/
def R2 (f : ℤ → ℤ → ℤ → ℤ) : Prop := ∀ m e j, f m e j = f (m - 1) e (j - e) + f m (e - 1) j

theorem Fc_R1 : R1 Fc := Fc_rec1
theorem Fc_R2 : R2 Fc := Fc_rec2

/-- The `m = 0` column three-term identity, both directions. -/
theorem col_up {h : ℤ → ℤ → ℤ → ℤ} (h1 : R1 h) (h2 : R2 h) (e j : ℤ) :
    h 0 (e + 1) j = 2 * h 0 e j - h 0 e (j - e) - h 0 (e - 1) j := by
  have a := h1 0 e j
  have b := h2 1 e j
  have c := h1 0 (e - 1) j
  simp only [zero_add, add_zero, sub_add_cancel, show (1 : ℤ) - 1 = 0 by norm_num] at a b c
  linarith

/-- A solution vanishing at `(0,0)` and `(0,1)` vanishes identically. -/
theorem unique_of_rec {h : ℤ → ℤ → ℤ → ℤ} (h1 : R1 h) (h2 : R2 h)
    (h00 : ∀ j, h 0 0 j = 0) (h01 : ∀ j, h 0 1 j = 0) : ∀ m e j, h m e j = 0 := by
  have col : ∀ e : ℤ, (∀ j, h 0 e j = 0) ∧ (∀ j, h 0 (e + 1) j = 0) := by
    intro e
    induction e using Int.induction_on with
    | zero => exact ⟨h00, by simpa using h01⟩
    | succ i ih =>
      refine ⟨ih.2, fun j => ?_⟩
      rw [col_up h1 h2, ih.2, ih.2, show (i : ℤ) + 1 - 1 = i by ring, ih.1]; ring
    | pred i ih =>
      refine ⟨fun j => ?_, by simpa using ih.1⟩
      have := col_up h1 h2 (-(i : ℤ)) j
      rw [show -(i : ℤ) + 1 = -i + 1 from rfl, ih.2, ih.1, ih.1] at this
      linarith
  intro m
  induction m using Int.induction_on with
  | zero => exact fun e j => (col e).1 j
  | succ i ih =>
    intro e j
    have := h1 i e j
    rw [ih, ih] at this; linarith
  | pred i ih =>
    intro e j
    have := h2 (-(i : ℤ)) e (j + e)
    rw [ih, ih, show j + e - e = j by ring] at this; linarith

/-! ### The transform `S` -/

/-- `e(e-1)/2`. -/
def triZ (e : ℤ) : ℤ := e * (e - 1) / 2

theorem two_triZ (e : ℤ) : 2 * triZ e = e * (e - 1) := by
  unfold triZ
  have : (2 : ℤ) ∣ e * (e - 1) := by
    rcases Int.even_or_odd e with ⟨k, hk⟩ | ⟨k, hk⟩ <;> subst hk <;>
      [exact ⟨k * (k + k - 1), by ring⟩; exact ⟨(2 * k + 1) * k, by ring⟩]
  exact Int.mul_ediv_cancel' this

/-- The exponent `σ(m,e) = e(e-1)/2 + em` of the transform. -/
def sig (m e : ℤ) : ℤ := triZ e + e * m

theorem sig_m_succ (m e : ℤ) : sig (m + 1) e = sig m e + e := by unfold sig; ring
theorem sig_m_pred (m e : ℤ) : sig (m - 1) e = sig m e - e := by unfold sig; ring
theorem sig_e_succ (m e : ℤ) : sig m (e + 1) = sig m e + e + m := by
  have a := two_triZ e; have b := two_triZ (e + 1); unfold sig; linarith
theorem sig_e_pred (m e : ℤ) : sig m (e - 1) = sig m e - (e - 1) - m := by
  have a := two_triZ e; have b := two_triZ (e - 1); unfold sig; linarith

theorem sgn_succ (e : ℤ) : (-1 : ℤ) ^ (e + 1).natAbs = -(-1) ^ e.natAbs := by
  rcases le_or_gt 0 e with h | h
  · rw [show (e + 1).natAbs = e.natAbs + 1 by omega, pow_succ]; ring
  · rw [show e.natAbs = (e + 1).natAbs + 1 by omega, pow_succ]; ring

theorem sgn_pred (e : ℤ) : (-1 : ℤ) ^ (e - 1).natAbs = -(-1) ^ e.natAbs := by
  have := sgn_succ (e - 1)
  rw [sub_add_cancel] at this
  rw [this]; ring

/-- `(Sf)(m,e,j) = (-1)^e f(e, -e-m, j - σ(m,e))`. -/
def S (f : ℤ → ℤ → ℤ → ℤ) (m e j : ℤ) : ℤ := (-1) ^ e.natAbs * f e (-e - m) (j - sig m e)

theorem S_R1 {f : ℤ → ℤ → ℤ → ℤ} (h1 : R1 f) : R1 (S f) := by
  intro m e j
  unfold S
  rw [sgn_succ, sig_m_succ, sig_e_succ]
  have := h1 e (-e - m - 1) (j - sig m e - e)
  ring_nf at this ⊢
  linear_combination -(-1 : ℤ) ^ e.natAbs * this

theorem S_R2 {f : ℤ → ℤ → ℤ → ℤ} (h2 : R2 f) : R2 (S f) := by
  intro m e j
  unfold S
  rw [sgn_pred, sig_m_pred, sig_e_pred]
  have := h2 e (-e - m + 1) (j - sig m e)
  ring_nf at this ⊢
  linear_combination -(-1 : ℤ) ^ e.natAbs * this

theorem Fc_one_neg (j : ℤ) : Fc 1 (-1) j = -Fc 0 1 j := by
  have a := Fc_rec2 1 0 j
  have b := Fc_rec1 0 0 j
  simp only [sub_self, sub_zero, zero_sub, zero_add, add_zero] at a b
  linarith

/-- **Triality, coefficientwise**: `F(m,e) = (-1)^e q^{σ(m,e)} F(e,-e-m)`. -/
theorem Fc_triality (m e j : ℤ) :
    Fc m e j = (-1) ^ e.natAbs * Fc e (-e - m) (j - sig m e) := by
  have key := unique_of_rec (h := fun m e j => S Fc m e j - Fc m e j)
    (fun m e j => by have a := S_R1 Fc_R1 m e j; have b := Fc_rec1 m e j; simp only; linarith)
    (fun m e j => by have a := S_R2 Fc_R2 m e j; have b := Fc_rec2 m e j; simp only; linarith)
    (fun j => by simp [S, sig, triZ])
    (fun j => by
      simp only [S, sig, triZ]
      norm_num
      rw [Fc_one_neg]; ring)
    m e j
  simp only [S] at key
  linarith

/-! ### Back to `TetIndexDegree.tetCoeff` -/

open QOU.QBeta.TetIndexDegree in
theorem pc_succ_rec (n j : ℕ) :
    pc (n + 1) j = pc n j + if n + 1 ≤ j then pc (n + 1) (j - (n + 1)) else 0 := by
  rw [pc, Finset.sum_range_succ']
  simp only [zero_mul, Nat.sub_zero]
  split_ifs with h
  · rw [pc, Nat.div_eq_sub_div (by omega) h, add_comm (pc n j)]
    congr 1
    apply Finset.sum_congr rfl
    intro i _
    congr 1
    rw [add_mul, one_mul]
    generalize i * (n + 1) = t
    omega
  · rw [Nat.div_eq_of_lt (by omega)]; simp

open QOU.QBeta.TetIndexDegree in
/-- The partition counts of `TetIndexDegree` are the coefficients of `1/(q)_n`. -/
theorem pc_eq (n j : ℕ) : (pc n j : ℤ) = coeff j (iqp n) := by
  induction n generalizing j with
  | zero => simp [pc, iqp_zero, coeff_one]
  | succ n ih =>
    induction j using Nat.strong_induction_on with
    | _ j ihj =>
      have hrel : coeff j (iqp (n + 1)) = coeff j (iqp n)
          + if n + 1 ≤ j then coeff (j - (n + 1)) (iqp (n + 1)) else 0 := by
        rw [iqp_pred n, mul_sub, mul_one, map_sub, coeff_mul_X_pow']
        split_ifs <;> ring
      rw [hrel, pc_succ_rec]
      push_cast
      rw [ih]
      split_ifs with h
      · rw [ihj _ (by omega)]
      · rfl

open QOU.QBeta.TetIndexDegree in
theorem conv_eq (a b j : ℕ) : (conv a b j : ℤ) = coeff j (iqp a * iqp b) := by
  unfold conv
  rw [coeff_mul, Finset.Nat.sum_antidiagonal_eq_sum_range_succ_mk]
  push_cast
  simp only [pc_eq]

open QOU.QBeta.TetIndexDegree in
theorem summand_eq (m e k : ℤ) (n : ℕ) :
    summand m e k n = if Even (k + e * m) then tm m e ((k + e * m) / 2) n else 0 := by
  have hst : k - start m e n = (k + e * m) - 2 * E m n := by
    unfold start E; linear_combination (two_tri n)
  unfold summand
  by_cases hp : Even (k + e * m)
  · rw [if_pos hp]
    obtain ⟨r, hr⟩ := hp
    have hr2 : (k + e * m) / 2 = r := by omega
    unfold tm
    rw [hr2]
    by_cases h1 : 0 ≤ (n : ℤ) + e ∧ start m e n ≤ k ∧ Even (k - start m e n)
    · rw [if_pos h1, if_pos h1.1, conv_eq]
      have hnn : 0 ≤ r - E m n := by omega
      unfold cz
      rw [if_pos hnn, show (k - start m e n) / 2 = r - E m n by omega]
    · rw [if_neg h1]
      by_cases hc : 0 ≤ (n : ℤ) + e
      · rw [if_pos hc]
        have hneg : r - E m n < 0 := by
          by_contra hh
          exact h1 ⟨hc, by omega, ⟨r - E m n, by omega⟩⟩
        rw [cz_neg _ hneg, mul_zero]
      · rw [if_neg hc]
  · rw [if_neg hp, if_neg]
    rintro ⟨_, _, t, ht⟩
    exact hp ⟨t + E m n, by omega⟩

open QOU.QBeta.TetIndexDegree in
theorem tetCoeff_eq (m e k : ℤ) :
    tetCoeff m e k = if Even (k + e * m) then Fc m e ((k + e * m) / 2) else 0 := by
  set N := cut m e k + cutF m ((k + e * m) / 2)
  have hT : tetCoeff m e k = ∑ n ∈ range N, summand m e k n := by
    unfold tetCoeff
    apply Finset.sum_subset (Finset.range_mono (by omega))
    intro n hn hn'
    simp only [Finset.mem_range, not_lt] at hn hn'
    have := summand_start_gt m e k n hn'
    unfold summand
    rw [if_neg (by omega)]
  rw [hT]
  simp only [summand_eq]
  split_ifs
  · rw [Fc_sum m e _ N (by omega)]
  · simp

open QOU.QBeta.TetIndexDegree in
/-- **Triality of the tetrahedron index, proved** (1208.1663 Prop prop.S3(b)):
`[t^k] I_Δ(m,e) = (-1)^e [t^{k+e}] I_Δ(e,-e-m)`. This discharges the cited
hypothesis `TetIndexDegree.Triality`. -/
theorem triality_holds : Triality := by
  intro m e k
  rw [tetCoeff_eq, tetCoeff_eq]
  have h2 := two_triZ e
  have hpar : Even (k + e * m) ↔ Even (k + e + (-e - m) * e) := by
    constructor
    · rintro ⟨r, hr⟩; exact ⟨r - e * m - triZ e, by linear_combination hr + h2⟩
    · rintro ⟨r, hr⟩; exact ⟨r + e * m + triZ e, by linear_combination hr - h2⟩
  by_cases hp : Even (k + e * m)
  · rw [if_pos hp, if_pos (hpar.mp hp), Fc_triality]
    obtain ⟨r, hr⟩ := hp
    congr 2
    unfold sig
    have a : (k + e * m) / 2 = r := by omega
    have b : (k + e + (-e - m) * e) / 2 = r - e * m - triZ e := by
      have : k + e + (-e - m) * e = (r - e * m - triZ e) + (r - e * m - triZ e) := by
        linear_combination hr + h2
      omega
    rw [a, b]; ring
  · rw [if_neg hp, if_neg (fun h => hp (hpar.mpr h))]; ring

/-! ### Unconditional corollaries: the cited hypothesis is gone -/

open QOU.QBeta.TetIndexDegree in
/-- **The degree of `I_Δ`, every cone, unconditionally** (1208.1663 Lemma lem.degID). -/
theorem tet_degree_bound_proved (m e k : ℤ) (hk : k < deg2 m e) : tetCoeff m e k = 0 :=
  tet_degree_bound triality_holds m e k hk

open QOU.QBeta.TetIndexDegree in
theorem fourone_N11_support_proved (e e₂ a : ℤ) (h : term41 0 e e₂ a 0 ≠ 0) :
    e = 0 ∧ e₂ = 0 ∧ a = 0 :=
  fourone_N11_support triality_holds e e₂ a h

open QOU.QBeta.TetIndexDegree in
theorem fourone_N12_support_proved (e e₂ a : ℤ) (h : term41 1 e e₂ a (-1 - e) ≠ 0) :
    e = -2 ∧ e₂ = 0 ∧ a = 1 :=
  fourone_N12_support triality_holds e e₂ a h

open QOU.QBeta.TetIndexDegree in
/-- **The 4₁ inputs, unconditionally.** -/
theorem stokes41_inputs_unconditional :
    StokesIndexCount41.i00 = term41 0 0 0 0 0 ∧
      StokesIndexCount41.i1 = term41 1 (-2) 0 1 (-1 - -2) :=
  stokes41_inputs_proved triality_holds

open QOU.QBeta.TetIndexDegree in
/-- **The 4₁ Stokes constant 3 from the tetrahedron index, with no cited input.** -/
theorem stokes41_three_unconditional :
    2 * term41 0 0 0 0 0 - term41 1 (-2) 0 1 (-1 - -2) = 3 :=
  stokes41_three_from_tetrahedra triality_holds

end QOU.QBeta.TetIndexTriality
