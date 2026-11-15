/-
  THE INDEX BRIDGE: a `ℕ`-window around `k*` is a `ℤ`-window around `0`.

      ∑_{j ∈ [k−W, k+W]} F j  =  ∑_{n ∈ [−W, W]} F((k + n).toNat)

  Pure bookkeeping, and the only reason it needs a file of its own is that it
  is used twice with different `F` — once on `kashaevProd N ·` and once on the
  Gaussian model `e^{T(·)}` — and both have to be reindexed the SAME way or the
  comparison in `KashaevWindowSum` compares different sums.

  `W ≤ k` is required and is not free: the window must not run off the bottom
  of `ℕ`.  At the saddle `k* = ⌊5N/6⌋ ≈ 0.83N` and `W ≈ N^{0.6}`, so it holds
  comfortably for `N` past a small threshold — but it is a hypothesis, not a
  triviality, and `Int.toNat` would silently clamp instead of failing.

  -- Ref: [leitner2026] QOU/Knot/KashaevWindowSum.lean
  -- Ref: [leitner2026] QOU/MathlibExt/GaussianWindowSum.lean
-/
import QOU.Knot.KashaevWindowSum
import QOU.MathlibExt.GaussianWindowSum

namespace QOU.Knot.FigureEightVolume

open Real

/-- **The bridge.**  Reindexing a symmetric `ℕ`-window as a symmetric
`ℤ`-window. -/
theorem sum_Icc_shift_int {W k : ℕ} (hW : W ≤ k) (F : ℕ → ℝ) :
    ∑ j ∈ Finset.Icc (k - W) (k + W), F j
      = ∑ n ∈ Finset.Icc (-(W : ℤ)) (W : ℤ), F ((k : ℤ) + n).toNat := by
  -- `omega` cannot see through the un-beta-reduced lambdas `sum_nbij'` leaves
  -- in the goals, so every branch beta-reduces first (`simp only` does it).
  refine Finset.sum_nbij' (fun j => (j : ℤ) - (k : ℤ))
    (fun n => ((k : ℤ) + n).toNat) ?_ ?_ ?_ ?_ ?_
  · intro j hj
    simp only [Finset.mem_Icc] at hj ⊢
    omega
  · intro n hn
    simp only [Finset.mem_Icc] at hn ⊢
    omega
  · intro j hj
    simp only [Finset.mem_Icc] at hj
    simp only []
    omega
  · intro n hn
    simp only [Finset.mem_Icc] at hn
    simp only []
    omega
  · intro j hj
    simp only [Finset.mem_Icc] at hj
    simp only []
    congr 1
    omega

/-- The window's cardinality, for the record: `2W + 1` terms. -/
theorem card_Icc_shift {W k : ℕ} (hW : W ≤ k) :
    (Finset.Icc (k - W) (k + W)).card = 2 * W + 1 := by
  rw [Nat.card_Icc]
  omega

end QOU.Knot.FigureEightVolume
