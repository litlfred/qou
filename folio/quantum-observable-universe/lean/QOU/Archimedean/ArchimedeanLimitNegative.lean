import QOU.Archimedean.DilogPartAConvergence
import QOU.Archimedean.ArchimedeanLimitDomain

/-!
# `ArchimedeanLimit x` for `-1 < x < 0` (bean `qou-adgd`, issue #7942)

`ArchimedeanLimit x` was proved for `0 < x < 1` (`archimedeanLimit_Ioo`) and refuted
for `x < -1` (`not_archimedeanLimit_of_lt_neg_one`). This file proves it on `(-1, 0)`.

The proof transports the positive case through two duplication identities, one for
each side of the limit, and needs no new Riemann-sum estimate:

* **products.** `(1 - x qᵏ)(1 + x qᵏ) = 1 - x² (q²)ᵏ`, so
  `D_n(x; q) · D_n(-x; q) = D_n(x²; q²)` for the denominators
  (`denomPolyLocal_mul_neg`), hence
  `log Φ_n(-x; q) = log Φ_n(x²; q²) - log Φ_n(x; q)` when every factor is positive;
* **series.** `Li₂(x) + Li₂(-x) = ½ Li₂(x²)` for `|x| ≤ 1` (`LiTwo_add_LiTwo_neg`), the
  odd-index terms cancelling (the same reindexing as `LiTwo_neg_one`).

With `x ∈ (0,1)`, both `x` and `x²` lie in `(0,1)`, where the limit is known; the
scaling `q → 1`, `n(1-q) → ∞` implies the same for `q²`, and
`(1-q)/(1-q²) = 1/(1+q) → ½`.

The endpoint `x = -1` would need the limit at `x² = 1`, which is not proved; it stays
open, as do `x = 1` and the restatement for `x > 1` that the bean records.

-- Ref: [leitner2026] conj:dilogarithm-archimedean-limit
-/

namespace QOU.Archimedean

open QOU.QPochhammer

/-! ## The product side -/

theorem denomPolyLocal_mul_neg (q x : ℝ) (n : ℕ) :
    denomPolyLocal q x n * denomPolyLocal q (-x) n = denomPolyLocal (q ^ 2) (x ^ 2) n := by
  induction n with
  | zero => simp [denomPolyLocal]
  | succ n ih =>
    simp only [denomPolyLocal]
    rw [← ih, ← pow_mul, mul_comm 2 n, pow_mul]
    ring

/-- Every factor positive gives a positive denominator. -/
theorem denomPolyLocal_pos {q y : ℝ} (hq0 : 0 ≤ q) (hq1 : q ≤ 1) (hy : |y| < 1) (n : ℕ) :
    0 < denomPolyLocal q y n := by
  induction n with
  | zero => simp [denomPolyLocal]
  | succ n ih =>
    simp only [denomPolyLocal]
    refine mul_pos ?_ ih
    have hqn : q ^ n ≤ 1 := pow_le_one₀ hq0 hq1
    have hqn0 : 0 ≤ q ^ n := pow_nonneg hq0 n
    have : |y * q ^ n| < 1 := by
      rw [abs_mul, abs_of_nonneg hqn0]
      calc |y| * q ^ n ≤ |y| * 1 := mul_le_mul_of_nonneg_left hqn (abs_nonneg y)
        _ < 1 := by simpa using hy
    linarith [le_abs_self (y * q ^ n)]

theorem log_partialProduct_neg {q x : ℝ} (hq0 : 0 ≤ q) (hq1 : q ≤ 1) (hx : |x| < 1)
    (n : ℕ) :
    Real.log (partialProductLocal q (-x) n) =
      Real.log (partialProductLocal (q ^ 2) (x ^ 2) n) - Real.log (partialProductLocal q x n) := by
  have hx' : |-x| < 1 := by rwa [abs_neg]
  have hx2 : |x ^ 2| < 1 := by
    rw [abs_pow]; exact pow_lt_one₀ (abs_nonneg x) hx (by norm_num)
  have h1 := denomPolyLocal_pos hq0 hq1 hx n
  have h2 := denomPolyLocal_pos hq0 hq1 hx' n
  unfold partialProductLocal
  rw [Real.log_inv, Real.log_inv, Real.log_inv, ← denomPolyLocal_mul_neg,
    Real.log_mul h1.ne' h2.ne']
  ring

/-! ## The series side -/

theorem summable_LiTwo_terms {x : ℝ} (hx : |x| ≤ 1) :
    Summable (fun k : ℕ => x ^ (k + 1) / ((k : ℝ) + 1) ^ 2) := by
  have hone : Summable (fun k : ℕ => (1 : ℝ) / ((k : ℝ) + 1) ^ 2) := by
    have h := (summable_nat_add_iff (f := fun n : ℕ => (1 : ℝ) / (n : ℝ) ^ 2) 1).mpr
      (Real.summable_one_div_nat_pow.mpr (by norm_num))
    simpa using h
  refine Summable.of_norm_bounded hone (fun k => ?_)
  rw [norm_div, norm_pow, Real.norm_eq_abs, Real.norm_eq_abs,
    abs_of_pos (by positivity : (0 : ℝ) < ((k : ℝ) + 1) ^ 2)]
  have : |x| ^ (k + 1) ≤ 1 := pow_le_one₀ (abs_nonneg x) hx
  exact div_le_div_of_nonneg_right this (by positivity)

/-- **Duplication** `Li₂(x) + Li₂(-x) = ½ Li₂(x²)` for `|x| ≤ 1`. -/
theorem LiTwo_add_LiTwo_neg {x : ℝ} (hx : |x| ≤ 1) :
    LiTwo x + LiTwo (-x) = LiTwo (x ^ 2) / 2 := by
  have hxn : |-x| ≤ 1 := by rwa [abs_neg]
  have hx2 : |x ^ 2| ≤ 1 := by rw [abs_pow]; exact pow_le_one₀ (abs_nonneg x) hx
  have hs1 := (summable_LiTwo_terms hx).hasSum
  have hs2 := (summable_LiTwo_terms hxn).hasSum
  have hs3 := ((summable_LiTwo_terms hx2).hasSum).mul_left (1 / 2 : ℝ)
  have hsum := hs1.add hs2
  -- the combined summand vanishes on even `n` and reindexes on odd `n = 2k+1`
  have hinj : Function.Injective (fun k : ℕ => 2 * k + 1) := by
    intro a b hab; dsimp only at hab; omega
  have hg : HasSum (fun n : ℕ => x ^ (n + 1) / ((n : ℝ) + 1) ^ 2 +
      (-x) ^ (n + 1) / ((n : ℝ) + 1) ^ 2) (1 / 2 * LiTwo (x ^ 2)) := by
    rw [← hinj.hasSum_iff]
    · have hfun : (fun n : ℕ => x ^ (n + 1) / ((n : ℝ) + 1) ^ 2 +
          (-x) ^ (n + 1) / ((n : ℝ) + 1) ^ 2) ∘ (fun k : ℕ => 2 * k + 1)
          = fun k : ℕ => 1 / 2 * ((x ^ 2) ^ (k + 1) / ((k : ℝ) + 1) ^ 2) := by
        funext k
        simp only [Function.comp]
        have he : (-x) ^ (2 * k + 1 + 1) = x ^ (2 * k + 1 + 1) :=
          Even.neg_pow ⟨k + 1, by ring⟩ x
        have hk : ((k : ℝ) + 1) ≠ 0 := by positivity
        rw [he, ← pow_mul]
        push_cast
        field_simp
        ring_nf
      rw [hfun]; unfold LiTwo; exact hs3
    · intro m hm
      have hmeven : Even m := by
        rcases Nat.even_or_odd m with he | ho
        · exact he
        · obtain ⟨k, rfl⟩ := ho; exact absurd ⟨k, by ring⟩ hm
      have hodd : Odd (m + 1) := hmeven.add_one
      rw [hodd.neg_pow]; ring
  have := hsum.unique hg
  unfold LiTwo at this ⊢
  linarith

/-! ## The limit on `(-1, 0)` -/

/-- **`ArchimedeanLimit y` holds for every `-1 < y < 0`.** -/
theorem archimedeanLimit_neg_Ioo {y : ℝ} (hy0 : y < 0) (hy1 : -1 < y) :
    ArchimedeanLimit y := by
  set x := -y with hxdef
  have hx0 : 0 < x := by linarith
  have hx1 : x < 1 := by linarith
  have hyx : y = -x := by rw [hxdef, neg_neg]
  have hxabs : |x| < 1 := by rw [abs_of_pos hx0]; exact hx1
  have hx20 : 0 < x ^ 2 := by positivity
  have hx21 : x ^ 2 < 1 := by nlinarith
  have hA := (archimedeanLimit_Ioo hx0 hx1).faddeev_limit
  have hB := (archimedeanLimit_Ioo hx20 hx21).faddeev_limit
  refine ⟨fun ε hε => ?_⟩
  set M := |LiTwo (x ^ 2)| + 1 with hM
  have hM0 : 0 < M := by positivity
  obtain ⟨δ1, hδ1, hP1⟩ := hA (ε / 3) (by positivity)
  obtain ⟨δ2, hδ2, hP2⟩ := hB (ε / 3) (by positivity)
  refine ⟨min (min δ1 (δ2 / 2)) (min (ε / (3 * M)) 1), by positivity, ?_⟩
  rintro q n ⟨hq_lo, hq1, hn⟩
  set δ := min (min δ1 (δ2 / 2)) (min (ε / (3 * M)) 1) with hδdef
  have hδ0 : 0 < δ := by positivity
  have hδa : δ ≤ δ1 := le_trans (min_le_left _ _) (min_le_left _ _)
  have hδb : δ ≤ δ2 / 2 := le_trans (min_le_left _ _) (min_le_right _ _)
  have hδc : δ ≤ ε / (3 * M) := le_trans (min_le_right _ _) (min_le_left _ _)
  have hδd : δ ≤ 1 := le_trans (min_le_right _ _) (min_le_right _ _)
  have hq0 : 0 < q := by linarith
  -- the hypotheses for `x` at `q`
  have hinv : δ1⁻¹ ≤ δ⁻¹ := inv_anti₀ hδ0 hδa
  have h1 := hP1 q n ⟨by linarith, hq1, by linarith⟩
  -- the hypotheses for `x²` at `q²`
  have hq2lo : 1 - δ2 < q ^ 2 := by nlinarith
  have hq2hi : q ^ 2 < 1 := by nlinarith
  have hn2 : (n : ℝ) * (1 - q ^ 2) > δ2⁻¹ := by
    have hinv2 : δ2⁻¹ ≤ δ⁻¹ := inv_anti₀ hδ0 (by linarith)
    have hn0 : (0 : ℝ) ≤ n := Nat.cast_nonneg n
    have : (n : ℝ) * (1 - q) ≤ (n : ℝ) * (1 - q ^ 2) := by
      apply mul_le_mul_of_nonneg_left _ hn0; nlinarith
    linarith
  have h2 := hP2 (q ^ 2) n ⟨hq2lo, hq2hi, hn2⟩
  -- assemble
  rw [hyx, log_partialProduct_neg hq0.le hq1.le hxabs,
    show LiTwo (-x) = LiTwo (x ^ 2) / 2 - LiTwo x by linarith [LiTwo_add_LiTwo_neg hxabs.le]]
  set A1 := (1 - q) * Real.log (partialProductLocal q x n)
  set A2 := (1 - q ^ 2) * Real.log (partialProductLocal (q ^ 2) (x ^ 2) n)
  have h1q : (0 : ℝ) < 1 + q := by linarith
  have hsplit : (1 - q) * (Real.log (partialProductLocal (q ^ 2) (x ^ 2) n) -
      Real.log (partialProductLocal q x n)) - (LiTwo (x ^ 2) / 2 - LiTwo x)
      = (A2 - LiTwo (x ^ 2)) / (1 + q) + (1 - q) / (2 * (1 + q)) * LiTwo (x ^ 2)
        - (A1 - LiTwo x) := by
    simp only [A1, A2]; field_simp; ring
  rw [hsplit, Real.norm_eq_abs]
  rw [Real.norm_eq_abs] at h1 h2
  have t1 : |(A2 - LiTwo (x ^ 2)) / (1 + q)| < ε / 3 := by
    rw [abs_div, abs_of_pos h1q]
    calc |A2 - LiTwo (x ^ 2)| / (1 + q) ≤ |A2 - LiTwo (x ^ 2)| :=
          div_le_self (abs_nonneg _) (by linarith)
      _ < ε / 3 := h2
  have t2 : |(1 - q) / (2 * (1 + q)) * LiTwo (x ^ 2)| < ε / 3 := by
    have hc0 : 0 ≤ (1 - q) / (2 * (1 + q)) := div_nonneg (by linarith) (by positivity)
    have hc1 : (1 - q) / (2 * (1 + q)) ≤ 1 - q := by
      rw [div_le_iff₀ (by positivity)]; nlinarith
    rw [abs_mul, abs_of_nonneg hc0]
    calc (1 - q) / (2 * (1 + q)) * |LiTwo (x ^ 2)| ≤ (1 - q) * M := by
          apply mul_le_mul hc1 (by linarith) (abs_nonneg _) (by linarith)
      _ < δ * M := mul_lt_mul_of_pos_right (by linarith) hM0
      _ ≤ ε / (3 * M) * M := mul_le_mul_of_nonneg_right hδc hM0.le
      _ = ε / 3 := by field_simp
  calc |(A2 - LiTwo (x ^ 2)) / (1 + q) + (1 - q) / (2 * (1 + q)) * LiTwo (x ^ 2)
        - (A1 - LiTwo x)|
      ≤ |(A2 - LiTwo (x ^ 2)) / (1 + q)| + |(1 - q) / (2 * (1 + q)) * LiTwo (x ^ 2)|
        + |A1 - LiTwo x| := by
        refine le_trans (abs_sub _ _) ?_
        exact add_le_add_right (abs_add_le _ _) _
    _ < ε / 3 + ε / 3 + ε / 3 := by linarith
    _ = ε := by ring

end QOU.Archimedean
