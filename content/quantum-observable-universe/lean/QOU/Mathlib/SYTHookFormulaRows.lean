import QOU.BraidKnot.IdentityIContentDecomposition

/-!
# QOU.Mathlib.SYTHookFormulaRows — Frame–Robinson–Thrall hook-length formula, closed
in full generality for one- and two-row shapes (sorry-free).

The general HLF `numSYTenum l = dimHLF l` is **PROVED, sorry-free**, in
`QOU.Mathlib.SYTEnum.numSYTenum_eq_dimHLF` (`SYTHookGNW.lean`) via the
Greene–Nijenhuis–Wilf route — corner recursion plus the hook-summation identity,
combined by strong induction. **This header said "remains open in this corpus" until
2026-08-30**, long after that proof landed; it is a source-file status note that went
stale, and it misled a downstream consumer into writing the same false claim into
`QOU.Hecke.blockDim`, a PR body and a bean. Cite the theorem, not this file, for the
general case.  This file proves the **closed-form sub-cases** that
HLF specialises to on small shapes — worth having independently of the general
theorem, since they are explicit closed forms rather than an existence result — genuine `∀`-quantified theorems
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

/-! ## Reusable product helpers for the two-row case -/

/-- Split a `range a` product at `b ≤ a` into the `[0,b)` prefix and the `[b,a)` tail. -/
theorem prod_range_split (a b : ℕ) (hab : b ≤ a) (f : ℕ → ℕ) :
    ((List.range a).map f).prod
      = ((List.range b).map f).prod * ((List.range' b (a - b)).map f).prod := by
  rw [← List.prod_append, ← List.map_append]
  congr 1
  rw [List.range_eq_range', List.range_eq_range']
  have h : List.range' 0 b ++ List.range' (0 + b) (a - b) = List.range' 0 (b + (a - b)) :=
    List.range'_append_1
  simp only [Nat.zero_add] at h
  have hb : b + (a - b) = a := by omega
  rw [h, hb]

/-- The descending tail product `∏_{j ∈ [b,a)} (a − j) = (a − b)!`. -/
theorem prod_range'_descending (a b : ℕ) (_hab : b ≤ a) :
    ((List.range' b (a - b)).map (fun j => a - j)).prod = Nat.factorial (a - b) := by
  rw [List.range'_eq_map_range, List.map_map]
  have hcomp : ((fun j => a - j) ∘ (fun k => b + k)) = (fun k => (a - b) - k) := by
    funext k; simp only [Function.comp_apply]; omega
  rw [hcomp]
  exact prod_range_descending (a - b)

/-- Divisor-free ascending product: `(∏_{j < b} (N − j)) · (N − b)! = N!` for `b ≤ N`.
The `b` largest descending factors of `N!` times the rest. -/
theorem prod_desc_mul_factorial (N : ℕ) : ∀ b ≤ N,
    ((List.range b).map (fun j => N - j)).prod * Nat.factorial (N - b) = Nat.factorial N := by
  intro b
  induction b with
  | zero => intro _; simp
  | succ m ih =>
    intro hb
    rw [List.range_succ, List.map_append, List.prod_append]
    simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, mul_one]
    have hm : m ≤ N := by omega
    have hfac : (N - m) * Nat.factorial (N - (m + 1)) = Nat.factorial (N - m) := by
      have hsucc : N - m = (N - (m + 1)) + 1 := by omega
      rw [hsucc, Nat.factorial_succ]
    rw [mul_assoc, hfac]
    exact ih hm

/-! ## Two-row HLF: closed-form hook product `prodHooks [a,b]` -/

/-- Row-1 hook product of `[a,b]` (`a ≥ b`): cell `j < b` of the second row has hook
`(b − j) + (colLen j − 1) − 1 = b − j` (since `j < b ⟹ colLen = 2`), so the product is `b!`. -/
theorem prodHooks_pair_row1 (a b : ℕ) (hab : b ≤ a) :
    ((List.range b).map (fun j => ((b - j) + (colLen [a, b] j - 1) - 1))).prod
      = Nat.factorial b := by
  have hbody : ∀ j ∈ List.range b,
      ((b - j) + (colLen [a, b] j - 1) - 1) = b - j := by
    intro j hj
    rw [List.mem_range] at hj
    rw [colLen_pair a b j hab]
    simp [hj]
  rw [List.map_congr_left hbody]
  exact prod_range_descending b

/-- Row-0 hook product of `[a,b]` (`a ≥ b`) in divisor-free form:
`(∏_{j} h(0,j)) · (a + 1 − b)! = (a+1)! · (a − b)!`.  The row-0 hooks split as
`a + 1 − j` for `j < b` and `a − j` for `b ≤ j < a`; the first block contributes the
descending product `(a+1)!/(a+1−b)!`, the second `(a − b)!`. -/
theorem prodHooks_pair_row0_mul (a b : ℕ) (hab : b ≤ a) :
    ((List.range a).map (fun j => ((a - j) + (colLen [a, b] j - 0) - 1))).prod
        * Nat.factorial (a + 1 - b)
      = Nat.factorial (a + 1) * Nat.factorial (a - b) := by
  -- rewrite the body using colLen_pair: for j < b it is a+1-j, for b ≤ j < a it is a-j
  rw [prod_range_split a b hab]
  -- prefix product (j < b): body = a + 1 - j
  have hpre : ∀ j ∈ List.range b,
      ((a - j) + (colLen [a, b] j - 0) - 1) = (a + 1) - j := by
    intro j hj
    rw [List.mem_range] at hj
    rw [colLen_pair a b j hab]
    have : j < a := lt_of_lt_of_le hj hab
    simp only [hj, if_true, Nat.sub_zero]
    omega
  -- tail product (b ≤ j < a, i.e. j ∈ range' b (a-b)): body = a - j
  have htail : ∀ j ∈ List.range' b (a - b),
      ((a - j) + (colLen [a, b] j - 0) - 1) = a - j := by
    intro j hj
    rw [List.mem_range'] at hj
    obtain ⟨hjb, hja⟩ := hj
    have hja' : j < a := by omega
    rw [colLen_pair a b j hab]
    have hnb : ¬ j < b := by omega
    simp only [hnb, if_false, hja', if_true, Nat.sub_zero]
    omega
  rw [List.map_congr_left hpre, List.map_congr_left htail]
  rw [prod_range'_descending a b hab]
  -- now (∏_{j<b}(a+1-j)) * (a-b)! * (a+1-b)! = (a+1)! * (a-b)!
  rw [mul_assoc, mul_comm (Nat.factorial (a - b)) (Nat.factorial (a + 1 - b)),
    ← mul_assoc]
  have hN : ((List.range b).map (fun j => (a + 1) - j)).prod * Nat.factorial (a + 1 - b)
      = Nat.factorial (a + 1) := by
    have := prod_desc_mul_factorial (a + 1) b (by omega)
    simpa using this
  rw [hN]

/-- **Two-row hook product, divisor-free closed form (sorry-free).** For `a ≥ b ≥ 1`,
`prodHooks [a,b] · (a + 1 − b)! = (a+1)! · (a − b)! · b!`.  This is the Frame–Robinson–Thrall
hook product on a two-row shape, the denominator of the ballot-number dimension
`dimHLF [a,b] = (a+b)! · (a+1−b)! / ((a+1)! · (a−b)! · b!)` (equivalently the standard
`(a+b)!·(a−b+1)/((a+1)·a!·b!)`). -/
theorem prodHooks_pair_mul (a b : ℕ) (hab : b ≤ a) (_hb : 1 ≤ b) :
    prodHooks [a, b] * Nat.factorial (a + 1 - b)
      = Nat.factorial (a + 1) * Nat.factorial (a - b) * Nat.factorial b := by
  have hdecomp : prodHooks [a, b]
      = ((List.range a).map (fun j => ((a - j) + (colLen [a, b] j - 0) - 1))).prod *
        (((List.range b).map (fun j => ((b - j) + (colLen [a, b] j - 1) - 1))).prod) := by
    unfold prodHooks
    simp only [List.length_cons, List.length_nil, List.range_succ,
      List.range_zero, List.map_cons, List.map_nil, List.map_append, List.prod_cons,
      List.prod_nil, List.prod_append, List.getD_cons_zero, List.getD_cons_succ]
    ring_nf
  rw [hdecomp, prodHooks_pair_row1 a b hab]
  -- (row0 * b!) * (a+1-b)! = row0 * (a+1-b)! * b!
  rw [mul_assoc, mul_comm (Nat.factorial b) (Nat.factorial (a + 1 - b)), ← mul_assoc,
    prodHooks_pair_row0_mul a b hab]


/-! ## One column `[1,1,…,1]` — the transpose of the one-row case

Added 2026-08-30 for `qou-luq7` item 2: `QOU.Hecke.WedderburnDecomp` needs the block
dimension to be a *function of the partition*, and the all-ones partition is the shape
its rank-one witness is supported on. Together with `dimHLF_single` this closes both
extreme shapes: a single row and a single column each carry exactly one standard
tableau. -/

/-- `colLen` of a single column is `n` at column `0` and `0` beyond: every one of the `n`
parts exceeds `0`, and none exceeds `0 + 1`. -/
theorem colLen_column (n j : ℕ) :
    colLen (List.replicate n 1) j = if j < 1 then n else 0 := by
  unfold colLen
  by_cases hj : j < 1
  · have hj0 : j = 0 := by omega
    subst hj0
    simp
  · have hj' : ¬ (j < 1) := hj
    simp [hj']

/-- **The single-column hook product is `n!`.** The column `[1,1,…,1]` has one cell per
row, and the hook at row `i` is `(1 - 0) + (n - i) - 1 = n - i`, so the product over
`i < n` is the descending product `n · (n-1) ⋯ 1`. -/
theorem prodHooks_column (n : ℕ) : prodHooks (List.replicate n 1) = Nat.factorial n := by
  unfold prodHooks
  rw [List.length_replicate]
  have hbody : ∀ i ∈ List.range n,
      (let rowLen := (List.replicate n 1).getD i 0
       ((List.range rowLen).map fun j =>
         ((rowLen - j) + (colLen (List.replicate n 1) j - i) - 1)).prod) = n - i := by
    intro i hi
    have hi' : i < n := List.mem_range.mp hi
    simp [hi', colLen_column]
  rw [List.map_congr_left hbody]
  exact prod_range_descending n

/-- **`dimHLF` of a single column is `1`.** `n!/n! = 1`: there is exactly one standard
Young tableau of shape `[1,1,…,1]`, since the entries must ascend down the column. -/
theorem dimHLF_column (n : ℕ) : dimHLF (List.replicate n 1) = 1 := by
  unfold dimHLF
  rw [prodHooks_column]
  have hsz : sz (List.replicate n 1) = n := by simp [sz]
  rw [hsz]
  exact Nat.div_self (Nat.factorial_pos n)

end QOU.Mathlib.SYTHookRows
