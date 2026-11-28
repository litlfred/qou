import Mathlib.Tactic
import QOU.Nuclear.StokesIndexCount41

/-!
# QOU.QBeta.TetIndexDegree — the minimal degree of the tetrahedron index

Bean `qou-vr3q`. Supplies the input that `QOU.QBeta.StokesIndexCount41` left
as computed: the two 4₁ index coefficients `[I₄₁(0,0)]_{q⁰} = 1`,
`[I₄₁(1,-2)]_{q^{1/2}} = -1`, and the fact that no other index coefficient
reaches q-degree 0 in the first row of the 4₁ index matrix.

## The tetrahedron index (Garoufalidis 1208.1663 eq ID, DGG)

`I_Δ(m,e) = Σ_{n ≥ (-e)₊} (-1)ⁿ t^{n(n+1) - (2n+e)m} / ((q)_n (q)_{n+e})`,
`t = q^{1/2}`. We work with its coefficients `tetCoeff m e k = [t^k] I_Δ(m,e)`,
defined below as an honest finite sum: the coefficient of `q^j` in `1/(q)_n` is
the number of partitions of `j` into parts `≤ n` (`pc`), and the `n`-sum is cut
off at a point past which every summand starts above `t^k`
(`summand_start_gt`).

## What is proved

* `tet_cone` — in the cone `m ≤ 0 ≤ e` the lowest coefficient is `1` at
  `t^{-me}` and everything below vanishes (1208.1663, proof of Lemma lem.degID).
* `tet_degree_bound` — **for all `(m,e)`**, `tetCoeff m e k = 0` for
  `k < deg2 m e`, with `deg2 = m₊(m+e)₊ + (-m)₊e₊ + (-e)₊(-e-m)₊ + max{0,m,-e}`
  (twice Garoufalidis's `δ`, Lemma lem.degID), given triality.
* `fourone_N11_support`, `fourone_N12_support` — in the 4₁ two-tetrahedron sum
  (DGG eq 4.18, `I₄₁(m,e) = Σ_{e₂} I_Δ(m-e₂, m+e-e₂) I_Δ(e-e₂, -e₂)`), the only
  term reaching `t⁰` in `N₁₁ = Ind^rot(0,x)` is `e = e₂ = 0`, and the only term
  reaching `t⁰` in `N₁₂ = -t·Ind^rot(1, t x)` is `e = -2, e₂ = 0`.
* `fourone_i00`, `fourone_i1` — those terms equal `1` and `-1`.
* `stokes41_inputs_proved` — so the two inputs `i00 = 1`, `i1 = -1` of
  `StokesIndexCount41.stokes_constant_three_from_index` are now theorems (given
  triality), and `stokes41_three_from_tetrahedra` restates the 4₁ Stokes
  constant 3 directly in tetrahedron-index coefficients.

## What is cited, not proved

* `Triality` — 1208.1663 Prop. prop.S3(b) with Thm 3.2(c):
  `I_Δ(m,e) = (-t)^{-e} I_Δ(e, -e-m)`. It is stated as a hypothesis on the
  concrete `tetCoeff`, and every theorem that needs it takes it as an argument.
  (Checked numerically on `|m|,|e| ≤ 5`, `k ≤ 24`: 3025 coefficients, 0 failures.)
  **Now proved:** `QOU.QBeta.TetIndexTriality.triality_holds : Triality`, from the
  two recursions of 1208.1663 (eq rec1, eq rec2) and a uniqueness argument. The
  unconditional forms of the theorems below are in that file
  (`tet_degree_bound_proved`, `stokes41_three_unconditional`, …).

No measured value enters. No fit.

-- Ref: [garoufalidis2016-3d-index] Garoufalidis 1208.1663 (eq ID, Lemma lem.degID, Prop prop.S3)
-- Ref: [dimofte-gaiotto-gukov2013] DGG 1112.5179 (eq 4.18)
-/

namespace QOU.QBeta.TetIndexDegree

open Finset

/-! ### Partition counts: the coefficients of `1/(q)_n` -/

/-- `pc n j` = number of partitions of `j` into parts `≤ n` = `[q^j] 1/(q)_n`. -/
def pc : ℕ → ℕ → ℕ
  | 0, j => if j = 0 then 1 else 0
  | n + 1, j => ∑ i ∈ range (j / (n + 1) + 1), pc n (j - i * (n + 1))

theorem pc_zero (n : ℕ) : pc n 0 = 1 := by
  induction n with
  | zero => simp [pc]
  | succ n ih => simp [pc, ih]

/-- `[q^j] 1/((q)_a (q)_b)`. -/
def conv (a b j : ℕ) : ℕ := ∑ i ∈ range (j + 1), pc a i * pc b (j - i)

theorem conv_zero (a b : ℕ) : conv a b 0 = 1 := by simp [conv, pc_zero]

/-! ### The tetrahedron index coefficients -/

/-- `t`-degree at which the `n`-th summand starts: `n(n+1) - (2n+e)m`. -/
def start (m e : ℤ) (n : ℕ) : ℤ := (n : ℤ) * (n + 1) - (2 * n + e) * m

/-- Contribution of the `n`-th summand to `[t^k]`. -/
def summand (m e k : ℤ) (n : ℕ) : ℤ :=
  if 0 ≤ (n : ℤ) + e ∧ start m e n ≤ k ∧ Even (k - start m e n) then
    (-1) ^ n * (conv n ((n : ℤ) + e).toNat ((k - start m e n) / 2).toNat : ℤ)
  else 0

/-- Cut-off for the `n`-sum. -/
def cut (m e k : ℤ) : ℕ := (2 * |m| + |k| + |e| * |m| + 2).toNat

/-- `tetCoeff m e k = [t^k] I_Δ(m,e)`. -/
def tetCoeff (m e k : ℤ) : ℤ := ∑ n ∈ range (cut m e k), summand m e k n

/-- The cut-off is honest: every summand past it starts strictly above `t^k`. -/
theorem summand_start_gt (m e k : ℤ) (n : ℕ) (hn : cut m e k ≤ n) :
    k < start m e n := by
  have hc : (2 * |m| + |k| + |e| * |m| + 2) ≤ (n : ℤ) := by
    have := Int.self_le_toNat (2 * |m| + |k| + |e| * |m| + 2)
    unfold cut at hn; omega
  have h1 : -(2 * (n : ℤ) * m) ≥ -(2 * n * |m|) := by
    have := le_abs_self m; have : (0 : ℤ) ≤ n := by positivity
    nlinarith
  have h2 : -(e * m) ≥ -(|e| * |m|) := by
    have : e * m ≤ |e * m| := le_abs_self _
    rw [abs_mul] at this; linarith
  have hk : k ≤ |k| := le_abs_self k
  have ha : 0 ≤ |m| := abs_nonneg m
  have hb : 0 ≤ |e| * |m| := by positivity
  have hn0 : (0 : ℤ) ≤ n := by positivity
  have hX : (|k| + |e| * |m| + 2) ≤ (n : ℤ) - 2 * |m| := by linarith
  have p1 := mul_le_mul_of_nonneg_left hX hn0
  have p2 : (0 : ℤ) ≤ ((n : ℤ) - 1) * (|k| + |e| * |m| + 2) := by
    apply mul_nonneg <;> nlinarith [abs_nonneg k]
  unfold start
  nlinarith

/-- **The cone `m ≤ 0 ≤ e`.** Below `t^{-me}` everything vanishes. -/
theorem tet_cone_zero (m e k : ℤ) (hm : m ≤ 0) (_he : 0 ≤ e) (hk : k < -(m * e)) :
    tetCoeff m e k = 0 := by
  unfold tetCoeff
  refine Finset.sum_eq_zero fun n _ => ?_
  unfold summand
  have : k < start m e n := by
    unfold start
    have : (0 : ℤ) ≤ n := by positivity
    nlinarith
  rw [if_neg]; omega

/-- **The cone `m ≤ 0 ≤ e`.** The coefficient of `t^{-me}` is `1`. -/
theorem tet_cone_lead (m e : ℤ) (hm : m ≤ 0) (he : 0 ≤ e) :
    tetCoeff m e (-(m * e)) = 1 := by
  unfold tetCoeff
  have hpos : 0 < cut m e (-(m * e)) := by
    unfold cut; have := abs_nonneg m; have := abs_nonneg (-(m * e))
    have : 0 ≤ |e| * |m| := by positivity
    omega
  rw [Finset.sum_eq_single 0]
  · unfold summand start
    simp only [Nat.cast_zero, zero_add, mul_zero, zero_mul, zero_sub, sub_neg_eq_add]
    rw [if_pos ⟨he, by linarith, ⟨0, by ring⟩⟩]
    have : (-(m * e) + e * m) / 2 = 0 := by ring_nf; simp
    rw [this]; simp [conv_zero]
  · intro n _ hn
    unfold summand
    have : -(m * e) < start m e n := by
      unfold start
      have : (1 : ℤ) ≤ n := by exact_mod_cast Nat.one_le_iff_ne_zero.mpr hn
      nlinarith
    rw [if_neg]; omega
  · intro h; exact absurd (Finset.mem_range.mpr hpos) h

/-! ### Triality (proved in `TetIndexTriality`) and the degree in every cone -/

/-- **Cited** (1208.1663 Prop. prop.S3(b), Thm 3.2(c)):
`I_Δ(m,e) = (-t)^{-e} I_Δ(e,-e-m)`, coefficientwise
`[t^k] I_Δ(m,e) = (-1)^e [t^{k+e}] I_Δ(e,-e-m)`. -/
def Triality : Prop :=
  ∀ m e k : ℤ, tetCoeff m e k = (-1) ^ e.natAbs * tetCoeff e (-e - m) (k + e)

/-- Twice Garoufalidis's degree `δ(m,e)` (Lemma lem.degID). -/
def deg2 (m e : ℤ) : ℤ :=
  max m 0 * max (m + e) 0 + max (-m) 0 * max e 0 + max (-e) 0 * max (-e - m) 0
    + max 0 (max m (-e))

theorem deg2_C0 {m e : ℤ} (hm : m ≤ 0) (he : 0 ≤ e) : deg2 m e = -(m * e) := by
  unfold deg2
  rw [max_eq_right hm, max_eq_left (neg_nonneg.mpr hm), max_eq_left he,
    max_eq_right (neg_nonpos.mpr he), max_eq_left (max_le hm (neg_nonpos.mpr he))]
  ring

theorem deg2_C1 {m e : ℤ} (he : e ≤ 0) (hme : e + m ≤ 0) :
    deg2 m e = e * (e + m) - e := by
  unfold deg2
  rw [max_eq_right (show m + e ≤ 0 by linarith), max_eq_right he,
    max_eq_left (show (0 : ℤ) ≤ -e by linarith), max_eq_left (show (0 : ℤ) ≤ -e - m by linarith),
    max_eq_right (show m ≤ -e by linarith), max_eq_right (show (0 : ℤ) ≤ -e by linarith)]
  ring

theorem deg2_C2 {m e : ℤ} (hm : 0 ≤ m) (hme : 0 ≤ e + m) :
    deg2 m e = m * (m + e) + m := by
  unfold deg2
  rw [max_eq_left hm, max_eq_left (show (0 : ℤ) ≤ m + e by linarith),
    max_eq_right (show -m ≤ 0 by linarith), max_eq_right (show -e - m ≤ 0 by linarith),
    max_eq_left (show -e ≤ m by linarith), max_eq_right hm]
  ring

/-- The three cones cover `ℤ²`, and on each `deg2` is one quadratic. -/
theorem deg2_cases (m e : ℤ) :
    (m ≤ 0 ∧ 0 ≤ e ∧ deg2 m e = -(m * e)) ∨
    (e ≤ 0 ∧ e + m ≤ 0 ∧ deg2 m e = e * (e + m) - e) ∨
    (0 ≤ m ∧ 0 ≤ e + m ∧ deg2 m e = m * (m + e) + m) := by
  rcases le_or_gt m 0 with hm | hm
  · rcases le_or_gt 0 e with he | he
    · exact Or.inl ⟨hm, he, deg2_C0 hm he⟩
    · exact Or.inr (Or.inl ⟨he.le, by linarith, deg2_C1 he.le (by linarith)⟩)
  · rcases le_or_gt 0 (e + m) with hme | hme
    · exact Or.inr (Or.inr ⟨hm.le, hme, deg2_C2 hm.le hme⟩)
    · exact Or.inr (Or.inl ⟨by linarith, hme.le, deg2_C1 (by linarith) hme.le⟩)

/-- **The degree of `I_Δ`, every cone** (1208.1663 Lemma lem.degID, lower bound):
`[t^k] I_Δ(m,e) = 0` for `k < deg2 m e`, given triality. -/
theorem tet_degree_bound (htri : Triality) (m e k : ℤ) (hk : k < deg2 m e) :
    tetCoeff m e k = 0 := by
  rcases deg2_cases m e with ⟨hm, he, hd⟩ | ⟨he, hme, hd⟩ | ⟨hm, hme, hd⟩
  · exact tet_cone_zero m e k hm he (by rw [hd] at hk; exact hk)
  · rw [htri m e k, tet_cone_zero e (-e - m) (k + e) he (by linarith)
      (by rw [hd] at hk; nlinarith), mul_zero]
  · rw [htri m e k, htri e (-e - m) (k + e)]
    have h1 : -(-e - m) - e = m := by ring
    have h2 : k + e + (-e - m) = k - m := by ring
    rw [h1, h2, tet_cone_zero (-e - m) m (k - m) (by linarith) hm
      (by rw [hd] at hk; nlinarith), mul_zero, mul_zero]

/-- Nonvanishing forces the degree bound. -/
theorem tet_deg_of_ne (htri : Triality) {m e k : ℤ} (h : tetCoeff m e k ≠ 0) :
    deg2 m e ≤ k := by
  by_contra hk; exact h (tet_degree_bound htri m e k (by omega))

theorem deg2_nonneg (m e : ℤ) : 0 ≤ deg2 m e := by
  rcases deg2_cases m e with ⟨hm, he, hd⟩ | ⟨he, hme, hd⟩ | ⟨hm, hme, hd⟩ <;>
    rw [hd] <;> nlinarith

/-! ### The 4₁ index (DGG eq 4.18) at q-degree 0

`I₄₁(m,e) = Σ_{e₂ ∈ ℤ} I_Δ(m-e₂, m+e-e₂) · I_Δ(e-e₂, -e₂)`, so
`[t^k] I₄₁(m,e) = Σ_{e₂, a} tetCoeff (m-e₂) (m+e-e₂) a · tetCoeff (e-e₂) (-e₂) (k-a)`.
In `N₁₁ = Ind^rot(0,x;q) = Σ_e I₄₁(0,e) xᵉ` the `t⁰` part takes `k = 0`. In
`N₁₂ = -t · Ind^rot(1, t x; q) = -Σ_e I₄₁(1,e) t^{1+e} xᵉ` it takes `k = -1-e`. -/

/-- The 4₁ summand of `[t^k] I₄₁(m,e)` at `(e₂, a)`. -/
def term41 (m e e₂ a k : ℤ) : ℤ :=
  tetCoeff (m - e₂) (m + e - e₂) a * tetCoeff (e - e₂) (-e₂) (k - a)

/-- **Support of `N₁₁` at `t⁰`.** Only `e = e₂ = a = 0` can contribute. -/
theorem fourone_N11_support (htri : Triality) (e e₂ a : ℤ)
    (h : term41 0 e e₂ a 0 ≠ 0) : e = 0 ∧ e₂ = 0 ∧ a = 0 := by
  unfold term41 at h
  have h1 := tet_deg_of_ne htri (left_ne_zero_of_mul h)
  have h2 := tet_deg_of_ne htri (right_ne_zero_of_mul h)
  simp only [zero_sub, zero_add] at h1 h2
  rcases deg2_cases (-e₂) (e - e₂) with ⟨p1, p2, d1⟩ | ⟨p1, p2, d1⟩ | ⟨p1, p2, d1⟩ <;>
  rcases deg2_cases (e - e₂) (-e₂) with ⟨r1, r2, d2⟩ | ⟨r1, r2, d2⟩ | ⟨r1, r2, d2⟩ <;>
  rw [d1] at h1 <;> rw [d2] at h2 <;>
  refine ⟨?_, ?_, ?_⟩ <;> nlinarith

/-- **Support of `N₁₂` at `t⁰`.** Only `e = -2, e₂ = 0, a = 1` can contribute. -/
theorem fourone_N12_support (htri : Triality) (e e₂ a : ℤ)
    (h : term41 1 e e₂ a (-1 - e) ≠ 0) : e = -2 ∧ e₂ = 0 ∧ a = 1 := by
  unfold term41 at h
  have h1 := tet_deg_of_ne htri (left_ne_zero_of_mul h)
  have h2 := tet_deg_of_ne htri (right_ne_zero_of_mul h)
  rcases deg2_cases (1 - e₂) (1 + e - e₂) with ⟨p1, p2, d1⟩ | ⟨p1, p2, d1⟩ | ⟨p1, p2, d1⟩ <;>
  rcases deg2_cases (e - e₂) (-e₂) with ⟨r1, r2, d2⟩ | ⟨r1, r2, d2⟩ | ⟨r1, r2, d2⟩ <;>
  rw [d1] at h1 <;> rw [d2] at h2 <;>
  refine ⟨?_, ?_, ?_⟩ <;> nlinarith

/-- **`[I₄₁(0,0)]_{q⁰} = 1`**: the single surviving term. -/
theorem fourone_i00 : term41 0 0 0 0 0 = 1 := by
  unfold term41
  have := tet_cone_lead 0 0 le_rfl le_rfl
  simp only [sub_zero, add_zero, neg_zero, mul_zero, neg_zero] at this ⊢
  rw [this]; norm_num

/-- **`[I₄₁(1,-2)]_{q^{1/2}} = -1`**: the single surviving term. -/
theorem fourone_i1 (htri : Triality) : term41 1 (-2) 0 1 (-1 - -2) = -1 := by
  unfold term41
  have hA : tetCoeff 1 (-1) 1 = -1 := by
    rw [htri 1 (-1) 1]
    have := tet_cone_lead (-1) 0 (by norm_num) le_rfl
    norm_num at this ⊢; rw [this]
  have hB : tetCoeff (-2) 0 0 = 1 := by
    have := tet_cone_lead (-2) 0 (by norm_num) le_rfl
    norm_num at this; exact this
  norm_num; rw [hA, hB]; norm_num

/-- **The 4₁ inputs, proved.** The two index coefficients that
`StokesIndexCount41` took as computed inputs are the surviving terms above. -/
theorem stokes41_inputs_proved (htri : Triality) :
    StokesIndexCount41.i00 = term41 0 0 0 0 0 ∧
      StokesIndexCount41.i1 = term41 1 (-2) 0 1 (-1 - -2) := by
  refine ⟨?_, ?_⟩
  · rw [fourone_i00]; rfl
  · rw [fourone_i1 htri]; rfl

/-- **The 4₁ Stokes constant 3 from two tetrahedron-index coefficients.**
`S⁺₁₂(1;0) = 2·[I₄₁(0,0)]_{q⁰} - [I₄₁(1,-2)]_{q^{1/2}} = 3`, with both
coefficients the unique surviving terms of the DGG sum (given triality). -/
theorem stokes41_three_from_tetrahedra (htri : Triality) :
    2 * term41 0 0 0 0 0 - term41 1 (-2) 0 1 (-1 - -2) = 3 := by
  rw [fourone_i00, fourone_i1 htri]; norm_num

end QOU.QBeta.TetIndexDegree
