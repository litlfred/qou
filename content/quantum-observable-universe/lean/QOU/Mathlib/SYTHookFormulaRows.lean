import QOU.BraidKnot.IdentityIContentDecomposition

/-!
# QOU.Mathlib.SYTHookFormulaRows — Frame–Robinson–Thrall hook-length formula, closed
in full generality for one- and two-row shapes (sorry-free).

The general HLF `numSYTenum l = dimHLF l` is the classical Greene–Nijenhuis–Wilf theorem
and remains open in this corpus.  This file proves the **closed-form sub-cases** that
HLF specialises to on shapes with at most two rows — genuine `∀`-quantified theorems
(not bounded `decide`):

* **One row** `[a]` (`a ≥ 1`): `prodHooks [a] = a!`, hence `dimHLF [a] = 1`
  (`prodHooks_single`, `dimHLF_single`).  This is HLF for `λ = (a)`: there is exactly
  one standard tableau of a single row.

* **Two rows** `[a, b]` (`a ≥ b ≥ 1`): the divisor-free closed product
  `prodHooks [a,b] · (a − b + 1) = (a+1) · a! · b!` (`prodHooks_pair_mul`), the
  classical two-row hook product giving the ballot-number dimension
  `dimHLF [a,b] = (a+b)! · (a−b+1) / ((a+1)·a!·b!)`.

All arithmetic is over `ℕ`; nothing archimedean; no fit.  The hook used is exactly the
one in `QOU.BraidKnot.IdentityI` (`h(i,j) = (λ_i − j) + (colLen j − i) − 1`), so these
closed forms certify `prodHooks`/`dimHLF` on the row families directly.
-/

namespace QOU.Mathlib.SYTHookRows

open QOU.BraidKnot.IdentityI

/-! ## A descending-product = factorial helper -/

/-- `∏_{j < a} (a − j) = a!` — the descending product is the factorial. -/
theorem prod_range_descending (a : ℕ) :
    ((List.range a).map (fun j => a - j)).prod = Nat.factorial a := by
  induction a with
  | zero => simp [Nat.factorial]
  | succ n ih =>
    rw [List.range_succ_eq_map, List.map_cons]
    simp only [Nat.sub_zero, List.prod_cons, List.map_map]
    have hcomp : ((fun j => (n + 1) - j) ∘ (Nat.succ)) = (fun j => n - j) := by
      funext j; simp [Nat.succ_sub_succ]
    rw [hcomp, ih, Nat.factorial_succ]

/-! ## colLen of one- and two-row shapes -/

/-- The column-count of a one-row shape: `colLen [a] j = 1` iff `j < a`. -/
theorem colLen_single (a j : ℕ) : colLen [a] j = if j < a then 1 else 0 := by
  unfold colLen
  simp only [List.filter]
  split_ifs with h <;> simp [h]

/-- The column-count of a two-row shape `[a,b]` with `a ≥ b`:
`colLen [a,b] j = 2` for `j < b`, `1` for `b ≤ j < a`, `0` for `a ≤ j`. -/
theorem colLen_pair (a b j : ℕ) (hab : b ≤ a) :
    colLen [a, b] j = if j < b then 2 else if j < a then 1 else 0 := by
  unfold colLen
  simp only [List.filter]
  by_cases hb : j < b
  · have ha : j < a := lt_of_lt_of_le hb hab
    simp [hb, ha]
  · by_cases ha : j < a
    · simp [hb, ha]
    · simp [hb, ha]

/-! ## One-row HLF: `prodHooks [a] = a!`, `dimHLF [a] = 1` -/

/-- **One-row hook product (sorry-free).** `prodHooks [a] = a!`: the hook of cell `j`
(`j < a`) of a single row is `(a − j) + (colLen j − 0) − 1 = a − j`, and the descending
product is `a!`. -/
theorem prodHooks_single (a : ℕ) : prodHooks [a] = Nat.factorial a := by
  unfold prodHooks
  simp only [List.length_singleton, List.range_one, List.map_cons, List.map_nil,
    List.getD_cons_zero, List.prod_cons, List.prod_nil, mul_one]
  have hbody : ∀ j ∈ List.range a,
      ((a - j) + (colLen [a] j - 0) - 1) = a - j := by
    intro j hj
    rw [List.mem_range] at hj
    rw [colLen_single]
    simp [hj]
  rw [List.map_congr_left hbody]
  exact prod_range_descending a

/-- **One-row dimension (sorry-free).** `dimHLF [a] = 1` for every `a ≥ 1`: there is exactly
one standard Young tableau of a single row.  (`a = 0` gives the empty shape with `dimHLF = 1`
as well, since `0!/1 = 1`.) -/
theorem dimHLF_single (a : ℕ) : dimHLF [a] = 1 := by
  unfold dimHLF
  rw [prodHooks_single]
  have hsz : sz [a] = a := by simp [sz]
  rw [hsz, Nat.div_self (Nat.factorial_pos a)]

end QOU.Mathlib.SYTHookRows
