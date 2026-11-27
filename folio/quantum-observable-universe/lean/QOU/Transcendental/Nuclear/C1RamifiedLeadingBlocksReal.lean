/-
  Archimedean Part 4 of `QOU.Nuclear.C1RamifiedLeadingBlocks`: the leading
  blocks as `±Real.sqrt ((p²−1)/p³)`.  Same namespace, original names kept.
-/
import QOU.Nuclear.C1RamifiedLeadingBlocks

namespace QOU.QBeta.C1Ramified

/-! ## Part 4 — solving over `ℝ`

The square root is the one archimedean step (§7c). -/

/-- **The leading blocks.** For `p > 0` with `p² ≥ 1`, the solutions of the
twisted edge equation are `B₁,₂ = ±√((p²−1)/p³)`. In the unramified variable
`q = p²` that is `±√(q−1)/q^{3/4}` — **not** `±√(q−1)/q`. -/
theorem leading_blocks (p T : ℝ) (hp : 0 < p) (hp1 : 1 ≤ p ^ 2) :
    p ^ 3 * T ^ 2 = p ^ 2 - 1 ↔
      T = Real.sqrt ((p ^ 2 - 1) / p ^ 3) ∨ T = -Real.sqrt ((p ^ 2 - 1) / p ^ 3) := by
  have hp3 : (0 : ℝ) < p ^ 3 := by positivity
  have hnn : (0 : ℝ) ≤ (p ^ 2 - 1) / p ^ 3 := by
    apply div_nonneg (by linarith) hp3.le
  constructor
  · intro h
    have hT2 : T ^ 2 = (p ^ 2 - 1) / p ^ 3 := by
      field_simp
      linarith [h]
    have habs : |T| = Real.sqrt ((p ^ 2 - 1) / p ^ 3) := by
      rw [← Real.sqrt_sq_eq_abs, hT2]
    rcases (abs_eq (Real.sqrt_nonneg _)).mp habs with h' | h'
    · exact Or.inl h'
    · exact Or.inr h'
  · intro h
    have hT2 : T ^ 2 = (p ^ 2 - 1) / p ^ 3 := by
      rcases h with h | h <;> subst h <;>
        [skip; rw [neg_pow, neg_one_pow_two, one_mul]] <;>
        rw [Real.sq_sqrt hnn]
    rw [hT2]
    field_simp

/-- **The two sectors are distinct exactly when `p ≠ 1`.** At `p = 1` the blocks
collide — the classical, non-`q`-deformed limit, which is also the only place
the untwisted convention would have agreed. -/
theorem blocks_distinct_iff (p : ℝ) (hp : 0 < p) (hp1 : 1 ≤ p ^ 2) :
    Real.sqrt ((p ^ 2 - 1) / p ^ 3) ≠ -Real.sqrt ((p ^ 2 - 1) / p ^ 3) ↔ p ≠ 1 := by
  have hp3 : (0 : ℝ) < p ^ 3 := by positivity
  have hnn : (0 : ℝ) ≤ (p ^ 2 - 1) / p ^ 3 := div_nonneg (by linarith) hp3.le
  constructor
  · intro h hq
    apply h
    subst hq
    norm_num
  · intro hq hcontra
    have h0 : Real.sqrt ((p ^ 2 - 1) / p ^ 3) = 0 := by linarith
    have hle : (p ^ 2 - 1) / p ^ 3 ≤ 0 := Real.sqrt_eq_zero'.mp h0
    have : p ^ 2 - 1 ≤ 0 := by
      by_contra hc
      push_neg at hc
      exact absurd hle (not_le.mpr (by positivity))
    have hp2 : p ^ 2 = 1 := by linarith
    have : (p - 1) * (p + 1) = 0 := by linarith [hp2]
    rcases mul_eq_zero.mp this with h | h
    · exact hq (by linarith [sub_eq_zero.mp h])
    · linarith

/-- **The Stokes space is two-dimensional** at `p ≠ 1`: exactly two roots, hence
exactly two sectors. -/
theorem stokes_sector_count (p : ℝ) (hp : 0 < p) (hp1 : 1 < p) :
    ({Real.sqrt ((p ^ 2 - 1) / p ^ 3),
      -Real.sqrt ((p ^ 2 - 1) / p ^ 3)} : Finset ℝ).card = 2 := by
  have hp2 : (1 : ℝ) ≤ p ^ 2 := by nlinarith
  rw [Finset.card_insert_of_notMem, Finset.card_singleton]
  simp only [Finset.mem_singleton]
  exact (blocks_distinct_iff p hp hp2).mpr (by linarith)

end QOU.QBeta.C1Ramified
