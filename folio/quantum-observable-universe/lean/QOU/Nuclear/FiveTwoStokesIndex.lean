import Mathlib.Tactic
import QOU.Nuclear.TetIndexTriality
import QOU.Nuclear.StokesIndexCount52
import QOU.Nuclear.FiveTwoDegree0
import QOU.Nuclear.FiveTwoDegree1
import QOU.Nuclear.FiveTwoDegree2

/-!
# QOU.QBeta.FiveTwoIndex — the 5₂ Stokes constants 4 and 3 from the m015 index

Bean `qou-vr3q`. The cross-knot companion of
`TetIndexTriality.stokes41_three_unconditional`. `StokesIndexCount52` proved
the gauge of GGM's 5₂ Stokes matrix (2012.00062 eq Sp-52):
`S⁺ = L · E·N·E⁻¹ · R`, with `L = gaugeL`, `R = gaugeR`, `E = diag((-q^k x²)^k)` and
`N_{ij} = Ind^rot(j-i, q^{(i+j)/2} x; q)` built from the 3d index of the SnapPy
triangulation m015. This file computes, in Lean and from tetrahedron indices
only, the `q⁰` coefficients at `x = 1` of the two entries that carry the
Stokes constants:

* `stokes52_12_from_index`: `[q⁰] S⁺₁₂(1;q) = 4`,
* `stokes52_31_from_index`: `[q⁰] S⁺₃₁(1;q) = -3`.

## The m015 index

`I(m,e) = Σ_{a,b} (-1)^{b+m} t^{-b} I_Δ(b-m, e-a) I_Δ(b, 2a-e-b) I_Δ(b+m, -a)`,
with `t = q^{1/2}`. This is the GHRS sum (1303.5278 §4) for SnapPy's m015 gluing
rows at half-longitude flux `m` (`computations/probes/half_class_3d_index.py`).
Substituting the two edge weights `(2a, 2b+m)` turns every half-integral
triple into an integral one. `term m e a b p` is the `(a,b)` summand's
`[t^p]`, from `tet3`, the coefficient of the product of three tetrahedron
indices. It vanishes below t-degree `fdeg m e a b` (`term_vanish`). For `|m| ≤ 2`
the bounds `fdeg_quad0/1/2` make the `(a,b)` sum finite at every degree, so
`idx m e p` is the honest coefficient `[t^p] I(m,e)` (`idx_eq`). `rot m s n`
is `[t^n] Ind^rot(m, t^s; q) = Σ_e [t^{n-se}] I(m,e)`, again an honest finite
sum (`rot_eq`, `rot_eq_idx`).

## The gauge at x = 1

The entries of `gaugeR` and `gaugeL` that enter are rational in `q`. `serC num den`
is the q-expansion of `num/den` (`serC_rec`: the Cauchy product with `den` is
`num`), and `R12_at1` … `L33_at1` show that each of the six entries is that
`num/den`.

## What is NOT proved here (named inputs, as in `StokesIndexCount52`)

* GGM's conjecture for the 5₂ region matrices (behind eq Sp-52).
* The block-to-index identity `𝒲₀(x⁻¹;q⁻¹)·𝒲₀(x;q)ᵀ = E·N·E⁻¹`, which the probe
  `computations/probes/qbeta_g3_stokes_from_3d_index_52.py` measures to 40 digits.

Granted those two, the 4 and the 3 come from tetrahedron-index coefficients by
finite exact arithmetic in this file.

No measured value enters. No fit.

-- Ref: [garoufalidis-gu-marino2023peacock] GGM 2012.00062 (eq Sp-52, WW52, S0px52)
-- Ref: [garoufalidis-hodgson-rubinstein-segerman2015] GHRS 1303.5278 (§4)
-- Ref: [garoufalidis2016-3d-index] Garoufalidis 1208.1663 (eq ID, Lemma lem.degID)
-/

namespace QOU.QBeta.FiveTwoIndex

open QOU.QBeta.TetIndexDegree QOU.QBeta.TetIndexTriality Finset

/-! ### Quadratic growth for `|m| ≤ 2` -/

theorem fdeg_quad {m : ℤ} (h0 : 0 ≤ m) (h2 : m ≤ 2) (e a b : ℤ) :
    a ^ 2 + b ^ 2 + e ^ 2 ≤ 12 * fdeg m e a b + 36 := by
  interval_cases m
  · linarith [fdeg_quad0 a b e]
  · linarith [fdeg_quad1 a b e]
  · linarith [fdeg_quad2 a b e]

theorem fdeg_growth {m : ℤ} (hm : |m| ≤ 2) (e a b : ℤ) :
    a ^ 2 + b ^ 2 + e ^ 2 ≤ 12 * fdeg m e a b + 36 ∨
      (a - e) ^ 2 + b ^ 2 + e ^ 2 ≤ 12 * fdeg m e a b + 36 := by
  rw [abs_le] at hm
  rcases le_or_gt 0 m with h | h
  · exact Or.inl (fdeg_quad h hm.2 e a b)
  · right
    have := fdeg_quad (m := -m) (by linarith) (by linarith) (-e) (a - e) b
    rw [show fdeg m e a b = fdeg (-(-m)) e a b by rw [neg_neg], fdeg_neg]
    have h3 : (-e) ^ 2 = e ^ 2 := by ring
    linarith

theorem abs_le_of_sq {x M : ℤ} (h : x ^ 2 ≤ M) : |x| ≤ M := by
  rcases eq_or_ne x 0 with rfl | hx
  · simp only [abs_zero]; nlinarith
  · have h1 : 1 ≤ |x| := Int.one_le_abs hx
    nlinarith [sq_abs x, abs_nonneg x]

/-- A summand reaching t-degree `p` lies in an explicit box. -/
theorem fdeg_bounds {m e a b p : ℤ} (hm : |m| ≤ 2) (h : fdeg m e a b ≤ p) :
    |a| ≤ |e| + 12 * |p| + 36 ∧ |b| ≤ 12 * |p| + 36 ∧ e ^ 2 ≤ 12 * p + 36 := by
  have hp := le_abs_self p
  rcases fdeg_growth hm e a b with g | g
  · have ha := abs_le_of_sq (show a ^ 2 ≤ 12 * |p| + 36 by nlinarith [sq_nonneg b, sq_nonneg e])
    have hb := abs_le_of_sq (show b ^ 2 ≤ 12 * |p| + 36 by nlinarith [sq_nonneg a, sq_nonneg e])
    refine ⟨by linarith [abs_nonneg e], hb, by nlinarith [sq_nonneg a, sq_nonneg b]⟩
  · have ha := abs_le_of_sq
      (show (a - e) ^ 2 ≤ 12 * |p| + 36 by nlinarith [sq_nonneg b, sq_nonneg e])
    have hb := abs_le_of_sq
      (show b ^ 2 ≤ 12 * |p| + 36 by nlinarith [sq_nonneg (a - e), sq_nonneg e])
    have hae := abs_sub_abs_le_abs_sub a e
    refine ⟨by linarith, hb, by nlinarith [sq_nonneg (a - e), sq_nonneg b]⟩

/-! ### The summand and the index coefficient -/

/-- `[t^K]` of `I_Δ(b-m, e-a) · I_Δ(b, 2a-e-b) · I_Δ(b+m, -a)`. Tetrahedron
coefficients vanish below degree `0` (`tet_degree_bound_proved`, `deg2_nonneg`),
so the convolution over `i, j ≥ 0`, `K-i-j ≥ 0` is exact. -/
def tet3 (m e a b K : ℤ) : ℤ :=
  ∑ i ∈ range (K.toNat + 1), ∑ j ∈ range (K.toNat + 1 - i),
    tetCoeff (b - m) (e - a) i * tetCoeff b (2 * a - e - b) j * tetCoeff (b + m) (-a) (K - i - j)

theorem tet3_vanish {m e a b K : ℤ}
    (h : K < deg2 (b - m) (e - a) + deg2 b (2 * a - e - b) + deg2 (b + m) (-a)) :
    tet3 m e a b K = 0 := by
  unfold tet3
  apply Finset.sum_eq_zero; intro i _
  apply Finset.sum_eq_zero; intro j _
  by_cases h1 : (i : ℤ) < deg2 (b - m) (e - a)
  · rw [tet_degree_bound_proved _ _ _ h1]; ring
  by_cases h2 : (j : ℤ) < deg2 b (2 * a - e - b)
  · rw [tet_degree_bound_proved _ _ _ h2]; ring
  push_neg at h1 h2
  rw [tet_degree_bound_proved _ _ (K - i - j) (by linarith)]; ring

/-- The `(a,b)` summand of `[t^p] I_{m015}(m,e)`. -/
def term (m e a b p : ℤ) : ℤ := (-1) ^ (b + m).natAbs * tet3 m e a b (p + b)

theorem term_vanish {m e a b p : ℤ} (h : p < fdeg m e a b) : term m e a b p = 0 := by
  unfold term; rw [tet3_vanish (by unfold fdeg at h; linarith), mul_zero]

theorem fdeg_of_term {m e a b p : ℤ} (h : term m e a b p ≠ 0) : fdeg m e a b ≤ p := by
  by_contra h'; exact h (term_vanish (by linarith))

/-- Box for the `(a,b)` sum of `[t^p] I(m,e)`. -/
def Nidx (e p : ℤ) : ℤ := |e| + 12 * |p| + 36

/-- **`[t^p] I_{m015}(m,e)`** (honest for `|m| ≤ 2`, `idx_eq`). -/
def idx (m e p : ℤ) : ℤ :=
  ∑ a ∈ Icc (-Nidx e p) (Nidx e p), ∑ b ∈ Icc (-Nidx e p) (Nidx e p), term m e a b p

theorem term_box {m e a b p : ℤ} (hm : |m| ≤ 2) (h : term m e a b p ≠ 0) :
    |a| ≤ Nidx e p ∧ |b| ≤ Nidx e p := by
  obtain ⟨ha, hb, -⟩ := fdeg_bounds hm (fdeg_of_term h)
  unfold Nidx; exact ⟨ha, by linarith [abs_nonneg e]⟩

/-- The box sum is the full `ℤ²` sum: any finite `T` holding every summand that
can reach degree `p` gives the same value. -/
theorem idx_eq {m e p : ℤ} (hm : |m| ≤ 2) (T : Finset (ℤ × ℤ))
    (hT : ∀ a b, fdeg m e a b ≤ p → (a, b) ∈ T) :
    idx m e p = ∑ x ∈ T, term m e x.1 x.2 p := by
  unfold idx
  rw [← Finset.sum_product' (f := fun a b => term m e a b p)]
  set B := Icc (-Nidx e p) (Nidx e p) ×ˢ Icc (-Nidx e p) (Nidx e p)
  have h1 : ∑ x ∈ B, term m e x.1 x.2 p = ∑ x ∈ B with x ∈ T, term m e x.1 x.2 p :=
    (Finset.sum_filter_of_ne fun x _ hx => hT _ _ (fdeg_of_term hx)).symm
  have h2 : ∑ x ∈ T, term m e x.1 x.2 p = ∑ x ∈ T with x ∈ B, term m e x.1 x.2 p := by
    refine (Finset.sum_filter_of_ne fun x _ hx => ?_).symm
    obtain ⟨ha, hb⟩ := term_box hm hx
    rw [abs_le] at ha hb
    simp only [B, Finset.mem_product, Finset.mem_Icc]; omega
  rw [h1, h2]
  congr 1; ext x; simp only [Finset.mem_filter]; tauto

/-! ### The rotated index `Ind^rot(m, t^s; q)` -/

def Mrot (n : ℤ) : ℤ := 12 * |n| + 100
def Nrot (n : ℤ) : ℤ := 40 * Mrot n + 12 * |n| + 100

/-- **`[t^n] Ind^rot(m, t^s; q) = Σ_e [t^{n-se}] I(m,e)`** at `x = 1`, as a box sum
(honest for `|m|, |s| ≤ 2`: `rot_eq`, `rot_eq_idx`). -/
def rot (m s n : ℤ) : ℤ :=
  ∑ e ∈ Icc (-Mrot n) (Mrot n), ∑ a ∈ Icc (-Nrot n) (Nrot n), ∑ b ∈ Icc (-Nrot n) (Nrot n),
    term m e a b (n - s * e)

theorem e_bound {e K : ℤ} (hK : 0 ≤ K) (h : e ^ 2 ≤ 24 * |e| + K) : |e| ≤ 24 + K := by
  by_contra hc; push_neg at hc
  nlinarith [sq_abs e, abs_nonneg e]

/-- A summand of `rot` that does not vanish lies in the box. -/
theorem rot_box {m s n e a b : ℤ} (hm : |m| ≤ 2) (hs : |s| ≤ 2)
    (h : term m e a b (n - s * e) ≠ 0) :
    |e| ≤ Mrot n ∧ |a| ≤ Nrot n ∧ |b| ≤ Nrot n := by
  obtain ⟨ha, hb, he⟩ := fdeg_bounds hm (fdeg_of_term h)
  have hse : |s * e| ≤ 2 * |e| := by
    rw [abs_mul]; exact mul_le_mul_of_nonneg_right hs (abs_nonneg e)
  have hp : |n - s * e| ≤ |n| + 2 * |e| := by
    have := abs_sub n (s * e); linarith
  have he' : e ^ 2 ≤ 24 * |e| + (12 * |n| + 36) := by
    have := neg_abs_le (s * e); have := le_abs_self n; nlinarith
  have hE := e_bound (by positivity) he'
  simp only [Nrot, Mrot]
  refine ⟨by linarith, by linarith [abs_nonneg e, abs_nonneg n], by linarith [abs_nonneg e]⟩

/-- `rot` as a sum over any finite set `P` of `(e,a,b)` holding every summand
with `fdeg + s·e ≤ n`. -/
theorem rot_eq {m s n : ℤ} (hm : |m| ≤ 2) (hs : |s| ≤ 2) (P : Finset (ℤ × ℤ × ℤ))
    (hP : ∀ e a b, fdeg m e a b + s * e ≤ n → (e, a, b) ∈ P) :
    rot m s n = ∑ x ∈ P, term m x.1 x.2.1 x.2.2 (n - s * x.1) := by
  set B := Icc (-Mrot n) (Mrot n) ×ˢ (Icc (-Nrot n) (Nrot n) ×ˢ Icc (-Nrot n) (Nrot n))
  have hB : rot m s n = ∑ x ∈ B, term m x.1 x.2.1 x.2.2 (n - s * x.1) := by
    unfold rot; rw [Finset.sum_product]
    refine Finset.sum_congr rfl fun e _ => ?_
    rw [Finset.sum_product]
  rw [hB]
  have h1 : ∑ x ∈ B, term m x.1 x.2.1 x.2.2 (n - s * x.1)
      = ∑ x ∈ B with x ∈ P, term m x.1 x.2.1 x.2.2 (n - s * x.1) :=
    (Finset.sum_filter_of_ne fun x _ hx => hP _ _ _ (by have := fdeg_of_term hx; linarith)).symm
  have h2 : ∑ x ∈ P, term m x.1 x.2.1 x.2.2 (n - s * x.1)
      = ∑ x ∈ P with x ∈ B, term m x.1 x.2.1 x.2.2 (n - s * x.1) := by
    refine (Finset.sum_filter_of_ne fun x _ hx => ?_).symm
    obtain ⟨he, ha, hb⟩ := rot_box hm hs hx
    rw [abs_le] at he ha hb
    simp only [B, Finset.mem_product, Finset.mem_Icc]; omega
  rw [h1, h2]
  congr 1; ext x; simp only [Finset.mem_filter]; tauto

/-- `rot` is the sum over charges of the index coefficients. -/
theorem rot_eq_idx {m s n : ℤ} (hm : |m| ≤ 2) (hs : |s| ≤ 2) :
    rot m s n = ∑ e ∈ Icc (-Mrot n) (Mrot n), idx m e (n - s * e) := by
  unfold rot
  apply Finset.sum_congr rfl
  intro e he
  have hT : ∀ a b, fdeg m e a b ≤ n - s * e →
      (a, b) ∈ Icc (-Nrot n) (Nrot n) ×ˢ Icc (-Nrot n) (Nrot n) := by
    intro a b hf
    obtain ⟨ha, hb, -⟩ := fdeg_bounds hm hf
    have hse : |s * e| ≤ 2 * |e| := by
      rw [abs_mul]; exact mul_le_mul_of_nonneg_right hs (abs_nonneg e)
    have hp : |n - s * e| ≤ |n| + 2 * |e| := by have := abs_sub n (s * e); linarith
    have heM : |e| ≤ Mrot n := by rw [Finset.mem_Icc] at he; rw [abs_le]; omega
    have ha' : |a| ≤ Nrot n := by simp only [Nrot, Mrot] at heM ⊢; linarith [abs_nonneg n]
    have hb' : |b| ≤ Nrot n := by simp only [Nrot, Mrot] at heM ⊢; linarith [abs_nonneg n]
    rw [abs_le] at ha' hb'
    simp only [Finset.mem_product, Finset.mem_Icc]; omega
  rw [idx_eq hm _ hT, Finset.sum_product]

/-- Below t-degree `-15` the rotated index vanishes (`|s| ≤ 2`). -/
theorem rot_low {m s n : ℤ} (hm : |m| ≤ 2) (hs : |s| ≤ 2) (hn : n < -15) : rot m s n = 0 := by
  rw [rot_eq hm hs ∅ ?_, Finset.sum_empty]
  intro e a b h
  exfalso
  obtain ⟨-, -, he⟩ := fdeg_bounds (p := n - s * e) hm (by linarith)
  have hs2 : s ^ 2 ≤ 4 := by nlinarith [sq_abs s, abs_nonneg s]
  nlinarith [sq_nonneg (e + 6 * s)]

/-! ### q-expansions of the gauge entries at `x = 1` -/

/-- First `r+1` coefficients of the q-expansion of `num/den` (`den₀ = 1`). -/
def serL (num den : List ℤ) : ℕ → List ℤ
  | 0 => [num.getD 0 0]
  | r + 1 => serL num den r ++
      [num.getD (r + 1) 0 - ∑ i ∈ range (r + 1), den.getD (r + 1 - i) 0 * (serL num den r).getD i 0]

/-- `[q^r] num/den`. -/
def serC (num den : List ℤ) (r : ℕ) : ℤ := (serL num den r).getD r 0

theorem serL_length (num den : List ℤ) (r : ℕ) : (serL num den r).length = r + 1 := by
  induction r with
  | zero => rfl
  | succ r ih => simp [serL, ih]

theorem serL_getD (num den : List ℤ) (r i : ℕ) (hi : i ≤ r) :
    (serL num den r).getD i 0 = serC num den i := by
  induction r with
  | zero => obtain rfl : i = 0 := by omega
            rfl
  | succ r ih =>
    rcases Nat.lt_or_ge i (r + 1) with h | h
    · rw [serL, List.getD_eq_getElem?_getD,
        List.getElem?_append_left (by rw [serL_length]; exact h), ← List.getD_eq_getElem?_getD,
        ih (by omega)]
    · obtain rfl : i = r + 1 := by omega
      rfl

/-- **`serC` is the q-expansion of `num/den`**: its Cauchy product with `den` is `num`. -/
theorem serC_rec (num den : List ℤ) (hden : den.getD 0 0 = 1) (r : ℕ) :
    ∑ i ∈ range (r + 1), den.getD (r - i) 0 * serC num den i = num.getD r 0 := by
  cases r with
  | zero =>
    rw [Finset.sum_range_one, Nat.sub_self, hden, one_mul]; rfl
  | succ r =>
    rw [Finset.sum_range_succ, Nat.sub_self, hden, one_mul]
    have hlast : serC num den (r + 1) = num.getD (r + 1) 0
        - ∑ i ∈ range (r + 1), den.getD (r + 1 - i) 0 * (serL num den r).getD i 0 := by
      unfold serC
      rw [serL, List.getD_eq_getElem?_getD, List.getElem?_append_right (by rw [serL_length])]
      simp [serL_length]
    rw [hlast]
    have : ∑ i ∈ range (r + 1), den.getD (r + 1 - i) 0 * (serL num den r).getD i 0
        = ∑ i ∈ range (r + 1), den.getD (r + 1 - i) 0 * serC num den i :=
      Finset.sum_congr rfl fun i hi => by
        rw [serL_getD _ _ _ _ (by simp at hi; omega)]
    rw [this]; ring

/-- `[t^k]` of a q-series (`q = t²`). -/
def tq (c : ℕ → ℤ) (k : ℤ) : ℤ := if 0 ≤ k ∧ k % 2 = 0 then c (k / 2).toNat else 0

/-- `R₁₂(1;q) = (2 - 2q - 2q² + q³)/((1-q)²(1+q))`. -/
def R12c : ℕ → ℤ := serC [2, -2, -2, 1] [1, -1, -1, 1]
/-- `R₂₂(1;q) = (-1 + 2q - q² + 2q³ - q⁴ + q⁵)/((1-q)(1-q³))`. -/
def R22c : ℕ → ℤ := serC [-1, 2, -1, 2, -1, 1] [1, -1, 0, -1, 1]
/-- `R₃₂(1;q) = -q⁴/((1-q²)(1-q³))`. -/
def R32c : ℕ → ℤ := serC [0, 0, 0, 0, -1] [1, 0, -1, -1, 0, 1]
/-- `L₃₁(1;q) = (-1 + q - q³)/((1-q)²(1+q))`. -/
def L31c : ℕ → ℤ := serC [-1, 1, 0, -1] [1, -1, -1, 1]
/-- `q · L₃₂(1;q) = (1 - 2q + 2q² - q³ + 3q⁴ - q⁵)/((1-q)(1-q³))`. -/
def L32c : ℕ → ℤ := serC [1, -2, 2, -1, 3, -1] [1, -1, 0, -1, 1]
/-- `L₃₃(1;q) = -q/((1-q²)(1-q³))`. -/
def L33c : ℕ → ℤ := serC [0, -1] [1, 0, -1, -1, 0, 1]

section gauge
variable {F : Type*} [Field F]
open QOU.QBeta.StokesIndexCount52 QOU.QBeta.StokesIndexCount52.M3

theorem L_row1 (x q : F) : (gaugeL x q).a₁₁ = 1 ∧ (gaugeL x q).a₁₂ = 0 ∧ (gaugeL x q).a₁₃ = 0 :=
  ⟨rfl, rfl, rfl⟩

theorem R_col1 (x q : F) : (gaugeR x q).a₁₁ = 1 ∧ (gaugeR x q).a₂₁ = 0 ∧ (gaugeR x q).a₃₁ = 0 :=
  ⟨rfl, rfl, rfl⟩

theorem R12_at1 (q : F) (h1 : 1 - q ≠ 0) (h2 : 1 + q ≠ 0) :
    (gaugeR 1 q).a₁₂ * (1 - q - q ^ 2 + q ^ 3) = 2 - 2 * q - 2 * q ^ 2 + q ^ 3 := by
  simp only [gaugeR, one_pow, mul_one]; field_simp; ring

theorem R22_at1 (q : F) (h1 : 1 - q ≠ 0) (h3 : 1 - q ^ 3 ≠ 0) :
    (gaugeR 1 q).a₂₂ * (1 - q - q ^ 3 + q ^ 4)
      = -1 + 2 * q - q ^ 2 + 2 * q ^ 3 - q ^ 4 + q ^ 5 := by
  simp only [gaugeR, one_pow, mul_one]; field_simp; ring

theorem R32_at1 (q : F) (h1 : 1 - q ≠ 0) (h2 : 1 + q ≠ 0) (h3 : 1 - q ^ 3 ≠ 0) :
    (gaugeR 1 q).a₃₂ * (1 - q ^ 2 - q ^ 3 + q ^ 5) = -q ^ 4 := by
  simp only [gaugeR, one_pow, mul_one]; field_simp; ring

theorem L31_at1 (q : F) (h1 : 1 - q ≠ 0) (h2 : 1 - q ^ 2 ≠ 0) :
    (gaugeL 1 q).a₃₁ * (1 - q - q ^ 2 + q ^ 3) = -1 + q - q ^ 3 := by
  simp only [gaugeL, one_pow, mul_one]; field_simp; ring

theorem L32_at1 (q : F) (hq : q ≠ 0) (h1 : 1 - q ≠ 0) (h3 : 1 - q ^ 3 ≠ 0) :
    (gaugeL 1 q).a₃₂ * (q * (1 - q - q ^ 3 + q ^ 4))
      = 1 - 2 * q + 2 * q ^ 2 - q ^ 3 + 3 * q ^ 4 - q ^ 5 := by
  simp only [gaugeL, one_pow, mul_one]; field_simp; ring

theorem L33_at1 (q : F) (h2 : 1 - q ^ 2 ≠ 0) (h3 : 1 - q ^ 3 ≠ 0) :
    (gaugeL 1 q).a₃₃ * (1 - q ^ 2 - q ^ 3 + q ^ 5) = -q := by
  simp only [gaugeL, one_pow, mul_one]; field_simp; ring

end gauge

/-! ### Where the low-degree summands sit -/

def P00 : Finset (ℤ × ℤ × ℤ) := {(0, 0, 0)}
def P11 : Finset (ℤ × ℤ × ℤ) :=
  {(-2, -2, -2), (-3, -2, -1), (-2, -2, -1), (-1, -1, -1), (0, 0, -1), (0, 0, 0), (1, 1, 0)}
def P22 : Finset (ℤ × ℤ × ℤ) := {(-3, -3, -3), (-4, -3, -2), (-3, -3, -2), (-2, -2, -2)}
def Pm11 : Finset (ℤ × ℤ × ℤ) :=
  {(-6, -3, 1), (-5, -3, 1), (-4, -2, 1), (-2, -1, 0), (-3, -1, 1), (-1, 0, 0)}
def Pm22 : Finset (ℤ × ℤ × ℤ) := {(-10, -5, 2), (-9, -5, 2), (-8, -4, 2)}

theorem sq_box {x k M : ℤ} (hk : 0 ≤ k) (h : x ^ 2 ≤ M) (hM : M < (k + 1) ^ 2) :
    -k ≤ x ∧ x ≤ k := by
  constructor <;> nlinarith

theorem hP00 : ∀ e a b, fdeg 0 e a b + 0 * e ≤ 0 → (e, a, b) ∈ P00 := by
  intro e a b h
  have q := fdeg_quad0 a b e
  have ha : a = 0 := by nlinarith [sq_nonneg a, sq_nonneg b, sq_nonneg e]
  have hb : b = 0 := by nlinarith [sq_nonneg a, sq_nonneg b, sq_nonneg e]
  have he : e = 0 := by nlinarith [sq_nonneg a, sq_nonneg b, sq_nonneg e]
  subst ha hb he; simp [P00]

set_option maxRecDepth 100000 in
theorem box11 : ∀ a ∈ Icc (-7 : ℤ) 7, ∀ b ∈ Icc (-7 : ℤ) 7, ∀ e ∈ Icc (-13 : ℤ) 1,
    fdeg 1 e a b + 1 * e ≤ 2 → (e, a, b) ∈ P11 := by decide +kernel

theorem hP11 : ∀ e a b, fdeg 1 e a b + 1 * e ≤ 2 → (e, a, b) ∈ P11 := by
  intro e a b h
  have q := fdeg_quad1 a b e
  have ha := sq_box (k := 7) (M := 60) (by norm_num) (show a ^ 2 ≤ 60 by
    nlinarith [sq_nonneg b, sq_nonneg (e + 6)]) (by norm_num)
  have hb := sq_box (k := 7) (M := 60) (by norm_num) (show b ^ 2 ≤ 60 by
    nlinarith [sq_nonneg a, sq_nonneg (e + 6)]) (by norm_num)
  have he := sq_box (k := 7) (M := 60) (by norm_num) (show (e + 6) ^ 2 ≤ 60 by
    nlinarith [sq_nonneg a, sq_nonneg b]) (by norm_num)
  exact box11 a (by simp; omega) b (by simp; omega) e (by simp; omega) h

set_option maxRecDepth 100000 in
theorem box22 : ∀ a ∈ Icc (-13 : ℤ) 13, ∀ b ∈ Icc (-13 : ℤ) 13, ∀ e ∈ Icc (-25 : ℤ) 1,
    fdeg 2 e a b + 2 * e ≤ 0 → (e, a, b) ∈ P22 := by decide +kernel

theorem hP22 : ∀ e a b, fdeg 2 e a b + 2 * e ≤ 0 → (e, a, b) ∈ P22 := by
  intro e a b h
  have q := fdeg_quad2 a b e
  have ha := sq_box (k := 13) (M := 180) (by norm_num) (show a ^ 2 ≤ 180 by
    nlinarith [sq_nonneg b, sq_nonneg (e + 12)]) (by norm_num)
  have hb := sq_box (k := 13) (M := 180) (by norm_num) (show b ^ 2 ≤ 180 by
    nlinarith [sq_nonneg a, sq_nonneg (e + 12)]) (by norm_num)
  have he := sq_box (k := 13) (M := 180) (by norm_num) (show (e + 12) ^ 2 ≤ 180 by
    nlinarith [sq_nonneg a, sq_nonneg b]) (by norm_num)
  exact box22 a (by simp; omega) b (by simp; omega) e (by simp; omega) h

set_option maxRecDepth 100000 in
theorem boxm11 : ∀ c ∈ Icc (-6 : ℤ) 6, ∀ b ∈ Icc (-6 : ℤ) 6, ∀ e ∈ Icc (-12 : ℤ) 0,
    fdeg (-1) e (c + e) b + 1 * e ≤ 0 → (e, c + e, b) ∈ Pm11 := by decide +kernel

theorem hPm11 : ∀ e a b, fdeg (-1) e a b + 1 * e ≤ 0 → (e, a, b) ∈ Pm11 := by
  intro e a b h
  have q := fdeg_quad1 (a - e) b (-e)
  rw [← fdeg_neg] at q
  have ha := sq_box (k := 6) (M := 36) (by norm_num) (show (a - e) ^ 2 ≤ 36 by
    nlinarith [sq_nonneg b, sq_nonneg (e + 6)]) (by norm_num)
  have hb := sq_box (k := 6) (M := 36) (by norm_num) (show b ^ 2 ≤ 36 by
    nlinarith [sq_nonneg (a - e), sq_nonneg (e + 6)]) (by norm_num)
  have he := sq_box (k := 6) (M := 36) (by norm_num) (show (e + 6) ^ 2 ≤ 36 by
    nlinarith [sq_nonneg (a - e), sq_nonneg b]) (by norm_num)
  have := boxm11 (a - e) (by simp; omega) b (by simp; omega) e (by simp; omega)
  simp only [sub_add_cancel] at this
  exact this h

set_option maxRecDepth 100000 in
theorem boxm22 : ∀ c ∈ Icc (-7 : ℤ) 7, ∀ b ∈ Icc (-7 : ℤ) 7, ∀ e ∈ Icc (-19 : ℤ) (-5),
    fdeg (-2) e (c + e) b + 2 * e ≤ -10 → (e, c + e, b) ∈ Pm22 := by decide +kernel

theorem hPm22 : ∀ e a b, fdeg (-2) e a b + 2 * e ≤ -10 → (e, a, b) ∈ Pm22 := by
  intro e a b h
  have q := fdeg_quad2 (a - e) b (-e)
  rw [← fdeg_neg] at q
  have ha := sq_box (k := 7) (M := 60) (by norm_num) (show (a - e) ^ 2 ≤ 60 by
    nlinarith [sq_nonneg b, sq_nonneg (e + 12)]) (by norm_num)
  have hb := sq_box (k := 7) (M := 60) (by norm_num) (show b ^ 2 ≤ 60 by
    nlinarith [sq_nonneg (a - e), sq_nonneg (e + 12)]) (by norm_num)
  have he := sq_box (k := 7) (M := 60) (by norm_num) (show (e + 12) ^ 2 ≤ 60 by
    nlinarith [sq_nonneg (a - e), sq_nonneg b]) (by norm_num)
  have := boxm22 (a - e) (by simp; omega) b (by simp; omega) e (by simp; omega)
  simp only [sub_add_cancel] at this
  exact this h

/-! ### The two Stokes entries at `q⁰`, `x = 1`

With `B = E·N·E⁻¹` at `x = 1`: `[t^n] B₁₁ = rot 0 0 n`, `[t^n] B₁₂ = -rot 1 1 (n+2)`,
`[t^n] B₁₃ = rot 2 2 (n+8)`, `[t^n] B₂₁ = -rot (-1) 1 (n-2)`, `[t^n] B₃₁ = rot (-2) 2 (n-8)`.
Row 1 of `L` is `(1,0,0)` and column 1 of `R` is `(1,0,0)ᵀ` (`L_row1`, `R_col1`), so
`S⁺₁₂ = B₁₁R₁₂ + B₁₂R₂₂ + B₁₃R₃₂` and `S⁺₃₁ = L₃₁B₁₁ + L₃₂B₂₁ + L₃₃B₃₁`.
The windows below hold every `n` that can contribute: `rot_low` cuts below `-15`,
and above the window the gauge factor has negative degree or one of its
vanishing low coefficients (`R32_low`, `L33_low`). -/

/-- `[t⁰] S⁺₁₂(1;q)` from the m015 index. -/
def stokes12 : ℤ :=
  ∑ n ∈ Icc (-15 : ℤ) 0, rot 0 0 n * tq R12c (-n)
    - ∑ n ∈ Icc (-15 : ℤ) 2, rot 1 1 n * tq R22c (2 - n)
    + ∑ n ∈ Icc (-15 : ℤ) 0, rot 2 2 n * tq R32c (8 - n)

/-- `[t⁰] S⁺₃₁(1;q)` from the m015 index. -/
def stokes31 : ℤ :=
  ∑ n ∈ Icc (-15 : ℤ) 0, tq L31c (-n) * rot 0 0 n
    - ∑ n ∈ Icc (-15 : ℤ) 0, tq L32c (-n) * rot (-1) 1 n
    + ∑ n ∈ Icc (-15 : ℤ) (-10), tq L33c (-n - 8) * rot (-2) 2 n

set_option maxRecDepth 100000 in
theorem R32_low : ∀ k ∈ Icc (0 : ℤ) 7, tq R32c k = 0 := by decide +kernel

set_option maxRecDepth 100000 in
theorem L33_low : ∀ k ∈ Icc (0 : ℤ) 1, tq L33c k = 0 := by decide +kernel

theorem rot00 (n : ℤ) (hn : n ≤ 0) :
    rot 0 0 n = ∑ x ∈ P00, term 0 x.1 x.2.1 x.2.2 (n - 0 * x.1) :=
  rot_eq (by norm_num) (by norm_num) P00 fun e a b h => hP00 e a b (by linarith)

theorem rot11 (n : ℤ) (hn : n ≤ 2) :
    rot 1 1 n = ∑ x ∈ P11, term 1 x.1 x.2.1 x.2.2 (n - 1 * x.1) :=
  rot_eq (by norm_num) (by norm_num) P11 fun e a b h => hP11 e a b (by linarith)

theorem rot22 (n : ℤ) (hn : n ≤ 0) :
    rot 2 2 n = ∑ x ∈ P22, term 2 x.1 x.2.1 x.2.2 (n - 2 * x.1) :=
  rot_eq (by norm_num) (by norm_num) P22 fun e a b h => hP22 e a b (by linarith)

theorem rotm11 (n : ℤ) (hn : n ≤ 0) :
    rot (-1) 1 n = ∑ x ∈ Pm11, term (-1) x.1 x.2.1 x.2.2 (n - 1 * x.1) :=
  rot_eq (by norm_num) (by norm_num) Pm11 fun e a b h => hPm11 e a b (by linarith)

theorem rotm22 (n : ℤ) (hn : n ≤ -10) :
    rot (-2) 2 n = ∑ x ∈ Pm22, term (-2) x.1 x.2.1 x.2.2 (n - 2 * x.1) :=
  rot_eq (by norm_num) (by norm_num) Pm22 fun e a b h => hPm22 e a b (by linarith)

set_option maxRecDepth 200000 in
/-- **The 5₂ Stokes constant 4 from the m015 index.** -/
theorem stokes52_12_from_index : stokes12 = 4 := by
  unfold stokes12
  have e1 : ∑ n ∈ Icc (-15 : ℤ) 0, rot 0 0 n * tq R12c (-n)
      = ∑ n ∈ Icc (-15 : ℤ) 0, (∑ x ∈ P00, term 0 x.1 x.2.1 x.2.2 (n - 0 * x.1)) * tq R12c (-n) :=
    Finset.sum_congr rfl fun n hn => by rw [rot00 n (by simp at hn; omega)]
  have e2 : ∑ n ∈ Icc (-15 : ℤ) 2, rot 1 1 n * tq R22c (2 - n)
      = ∑ n ∈ Icc (-15 : ℤ) 2, (∑ x ∈ P11, term 1 x.1 x.2.1 x.2.2 (n - 1 * x.1)) * tq R22c (2 - n) :=
    Finset.sum_congr rfl fun n hn => by rw [rot11 n (by simp at hn; omega)]
  have e3 : ∑ n ∈ Icc (-15 : ℤ) 0, rot 2 2 n * tq R32c (8 - n)
      = ∑ n ∈ Icc (-15 : ℤ) 0, (∑ x ∈ P22, term 2 x.1 x.2.1 x.2.2 (n - 2 * x.1)) * tq R32c (8 - n) :=
    Finset.sum_congr rfl fun n hn => by rw [rot22 n (by simp at hn; omega)]
  rw [e1, e2, e3]
  decide +kernel

set_option maxRecDepth 200000 in
/-- **The 5₂ Stokes constant 3 from the m015 index** (`S⁺₃₁ = -3`). -/
theorem stokes52_31_from_index : stokes31 = -3 := by
  unfold stokes31
  have e1 : ∑ n ∈ Icc (-15 : ℤ) 0, tq L31c (-n) * rot 0 0 n
      = ∑ n ∈ Icc (-15 : ℤ) 0, tq L31c (-n) * ∑ x ∈ P00, term 0 x.1 x.2.1 x.2.2 (n - 0 * x.1) :=
    Finset.sum_congr rfl fun n hn => by rw [rot00 n (by simp at hn; omega)]
  have e2 : ∑ n ∈ Icc (-15 : ℤ) 0, tq L32c (-n) * rot (-1) 1 n
      = ∑ n ∈ Icc (-15 : ℤ) 0, tq L32c (-n) * ∑ x ∈ Pm11, term (-1) x.1 x.2.1 x.2.2 (n - 1 * x.1) :=
    Finset.sum_congr rfl fun n hn => by rw [rotm11 n (by simp at hn; omega)]
  have e3 : ∑ n ∈ Icc (-15 : ℤ) (-10), tq L33c (-n - 8) * rot (-2) 2 n
      = ∑ n ∈ Icc (-15 : ℤ) (-10), tq L33c (-n - 8) * ∑ x ∈ Pm22, term (-2) x.1 x.2.1 x.2.2 (n - 2 * x.1) :=
    Finset.sum_congr rfl fun n hn => by rw [rotm22 n (by simp at hn; omega)]
  rw [e1, e2, e3]
  decide +kernel

/-- The same numbers as GGM's q⁰ matrix (eq S0px52) at `x = 1`. -/
theorem stokes52_matches_S0px52 :
    (stokes12 : ℚ) = (QOU.QBeta.StokesIndexCount52.splus0 (1 : ℚ)).a₁₂ ∧
      (stokes31 : ℚ) = (QOU.QBeta.StokesIndexCount52.splus0 (1 : ℚ)).a₃₁ := by
  obtain ⟨-, h12, h31, -⟩ := QOU.QBeta.StokesIndexCount52.splus_qzero_factorisation (1 : ℚ)
  rw [stokes52_12_from_index, stokes52_31_from_index, h12, h31]
  norm_num

end QOU.QBeta.FiveTwoIndex
