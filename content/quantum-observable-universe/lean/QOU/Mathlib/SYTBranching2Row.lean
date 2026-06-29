import QOU.Mathlib.SYTDimHLFPair
import QOU.Mathlib.SYTBranchingRecursion

/-!
# QOU.Mathlib.SYTBranching2Row — the corner-removal recursion (A) on two rows

The general hook-length formula is reduced (in `SYTBranchingRecursion`) to the two corner-removal
recursions (A) `dimHLF_branching` and (B) `numSYTenum_branching`.  This file proves **(A) on two
rows**, sorry-free:

    dimHLF [a, b] = branchSum dimHLF [a, b]          (`dimHLF_branching_pair`,  a ≥ b ≥ 1)

i.e. `dimHLF[a,b] = dimHLF[a−1,b] + dimHLF[a,b−1]` (and `= dimHLF[a,b−1]` when `a = b`, the single
corner).  With the ballot-number form `dimHLF[a,b] = C(a+b,b) − C(a+b,b−1)` (`dimHLF_pair`) this is
pure **Pascal's rule** plus binomial monotonicity/symmetry — no floor-division.  Pure ℕ.
-/

namespace QOU.Mathlib.SYTEnum

open QOU.BraidKnot.IdentityI (dimHLF prodHooks sz colLen)
open QOU.Mathlib.SYTHookRows (dimHLF_pair prodHooks_pair_mul colLen_pair prod_range_descending)

/-- `prodHooks [a, 0] = a!` — the hook product of a shape with an empty second row. -/
theorem prodHooks_zero_row (a : ℕ) : prodHooks [a, 0] = Nat.factorial a := by
  unfold prodHooks
  rw [show (([a, 0] : List ℕ)).length = 2 from rfl, show List.range 2 = [0, 1] from rfl]
  simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, mul_one,
    List.getD_cons_zero, List.getD_cons_succ, List.range_zero]
  have hbody : ∀ j ∈ List.range a, ((a - j) + (colLen [a, 0] j - 0) - 1) = a - j := by
    intro j hj
    rw [List.mem_range] at hj
    rw [colLen_pair a 0 j (by omega)]; simp [hj]
  rw [List.map_congr_left hbody]
  exact prod_range_descending a

/-- `dimHLF [a, 0] = 1` — the empty second row carries the one-row dimension. -/
theorem dimHLF_zero_row (a : ℕ) : dimHLF [a, 0] = 1 := by
  unfold dimHLF
  rw [prodHooks_zero_row]
  have hsz : sz [a, 0] = a := by simp [sz]
  rw [hsz, Nat.div_self (Nat.factorial_pos a)]

/-- Decrement the first row of a two-row shape. -/
theorem decrementRow_pair0 (a b : ℕ) : decrementRow [a, b] 0 = [a - 1, b] := by
  unfold decrementRow; simp [List.set]

/-- Decrement the second row of a two-row shape. -/
theorem decrementRow_pair1 (a b : ℕ) : decrementRow [a, b] 1 = [a, b - 1] := by
  unfold decrementRow; simp [List.set]

/-- The removable corners of a two-row shape `[a, b]` with `b ≥ 1`: row `0` iff `b < a`, plus row `1`
always. -/
theorem removableCornerIdxs_pair (a b : ℕ) (hb : 1 ≤ b) :
    removableCornerIdxs [a, b] = if b < a then [0, 1] else [1] := by
  unfold removableCornerIdxs
  rw [show (([a, b] : List ℕ)).length = 2 from rfl, show List.range 2 = [0, 1] from rfl,
    List.filter_cons, List.filter_cons, List.filter_nil]
  simp only [List.getD_cons_zero, List.getD_cons_succ, List.getD_nil]
  rw [show decide (0 < b) = true from decide_eq_true_eq.mpr (by omega)]
  by_cases hba : b < a <;> simp [hba]

/-- Binomial monotonicity in the lower index up to the centre: `C(n, k−1) ≤ C(n, k)` whenever
`k ≤ n − k` (here applied with `n − k = a ≥ b = k`). -/
theorem choose_mono_pair (n k : ℕ) (hk : 1 ≤ k) (hkn : k ≤ n - k) :
    Nat.choose n (k - 1) ≤ Nat.choose n k := by
  have h := Nat.choose_succ_right_eq n (k - 1)
  rw [show k - 1 + 1 = k from by omega] at h
  have hp : 0 < Nat.choose n (k - 1) ∨ Nat.choose n (k - 1) = 0 := by
    rcases Nat.eq_zero_or_pos (Nat.choose n (k - 1)) with h0 | h0
    · right; exact h0
    · left; exact h0
  -- C(n,k)*k = C(n,k-1)*(n-(k-1)); n-(k-1) ≥ k since k ≤ n-k ⇒ n-k+1 ≥ k+1 > k
  have hge : k ≤ n - (k - 1) := by omega
  nlinarith [h, hge, Nat.choose_pos (show k - 1 ≤ n by omega)]

/-- Pascal's rule in subtraction-normalised form. -/
theorem pascal_sub (m k : ℕ) (hk : 1 ≤ k) (hkm : k ≤ m) :
    Nat.choose m k = Nat.choose (m - 1) (k - 1) + Nat.choose (m - 1) k := by
  have := Nat.choose_succ_succ (m - 1) (k - 1)
  simp only [Nat.succ_eq_add_one] at this
  rwa [show m - 1 + 1 = m from by omega, show k - 1 + 1 = k from by omega] at this

/-- **(A) corner-removal recursion on two rows (sorry-free).**
`dimHLF [a, b] = branchSum dimHLF [a, b]` for `a ≥ b ≥ 1`: the brute-force hook-length dimension of a
two-row shape equals the sum over removable corners of the dimensions of the corner-removed shapes —
the two-row instance of obligation (A) for the general hook-length formula. -/
theorem dimHLF_branching_pair (a b : ℕ) (hab : b ≤ a) (hb : 1 ≤ b) :
    dimHLF [a, b] = branchSum dimHLF [a, b] := by
  rw [branchSum, removableCornerIdxs_pair a b hb]
  by_cases hba : b < a
  · -- two corners: dimHLF[a,b] = dimHLF[a-1,b] + dimHLF[a,b-1]
    rw [if_pos hba]
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, add_zero,
      decrementRow_pair0, decrementRow_pair1]
    rw [dimHLF_pair a b hab hb, dimHLF_pair (a - 1) b (by omega) hb,
      show a - 1 + b = a + b - 1 from by omega]
    have p1 := pascal_sub (a + b) b (by omega) (by omega)
    by_cases hb1 : b = 1
    · subst hb1
      rw [dimHLF_zero_row]
      simp only [show (1 : ℕ) - 1 = 0 from rfl, show a + 1 - 1 = a from by omega,
        Nat.choose_one_right, Nat.choose_zero_right] at *
      omega
    · rw [dimHLF_pair a (b - 1) (by omega) (by omega),
        show a + (b - 1) = a + b - 1 from by omega, show b - 1 - 1 = b - 2 from by omega]
      have p2 := pascal_sub (a + b) (b - 1) (by omega) (by omega)
      rw [show b - 1 - 1 = b - 2 from by omega] at p2
      have m1 : Nat.choose (a + b - 1) (b - 1) ≤ Nat.choose (a + b - 1) b :=
        choose_mono_pair (a + b - 1) b (by omega) (by omega)
      have m2 : Nat.choose (a + b - 1) (b - 2) ≤ Nat.choose (a + b - 1) (b - 1) := by
        have := choose_mono_pair (a + b - 1) (b - 1) (by omega) (by omega)
        rwa [show b - 1 - 1 = b - 2 from by omega] at this
      omega
  · -- single corner (a = b): dimHLF[a,a] = dimHLF[a,a-1]
    rw [if_neg hba]
    have hba' : b = a := by omega
    subst hba'
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, add_zero,
      decrementRow_pair1]
    by_cases hb1 : b = 1
    · subst hb1
      rw [show ((1 : ℕ) - 1) = 0 from rfl, dimHLF_zero_row 1,
        dimHLF_pair 1 1 (le_refl 1) (le_refl 1)]
      decide
    · rw [dimHLF_pair b b (le_refl _) hb, dimHLF_pair b (b - 1) (by omega) (by omega),
        show b + (b - 1) = b + b - 1 from by omega, show b - 1 - 1 = b - 2 from by omega]
      have p1 := pascal_sub (b + b) b (by omega) (by omega)
      have p2 := pascal_sub (b + b) (b - 1) (by omega) (by omega)
      rw [show b - 1 - 1 = b - 2 from by omega] at p2
      have hsym : Nat.choose (b + b - 1) b = Nat.choose (b + b - 1) (b - 1) := by
        have h := Nat.choose_symm (show b ≤ b + b - 1 from by omega)
        rw [show b + b - 1 - b = b - 1 from by omega] at h
        exact h.symm
      have m2 : Nat.choose (b + b - 1) (b - 2) ≤ Nat.choose (b + b - 1) (b - 1) := by
        have := choose_mono_pair (b + b - 1) (b - 1) (by omega) (by omega)
        rwa [show b - 1 - 1 = b - 2 from by omega] at this
      omega

end QOU.Mathlib.SYTEnum
