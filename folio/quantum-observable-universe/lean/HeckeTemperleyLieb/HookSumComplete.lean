import Mathlib.Tactic

/-!
# QOU.Common.HookSumComplete — the FULL hook-sum identity (leg-sum lemma closed)

Completes `HookSumGeneral` by closing the leg-sum step, giving the hook-sum
identity `Σ_c h(c) = b(λ) + b(λ') + n` for **every** partition (sorted list),
sorry-free — no conjugation-involutivity needed. The linchpin is the
*sorted-prefix* lemma: for a weakly-decreasing `λ`, the rows exceeding column
`j` form an initial segment `{0,…,colLen j − 1}`. Both `legSum` and `b(λ)`
collapse to `Σ_j C(colLen j, 2)` through it.

This file is self-contained (it re-declares the small `colLen`/`bStat` helpers)
so it compiles under `lean`-direct without the freshly-merged
`HookSumGeneral.olean` in the restored cache.

## The same identity is also proved over `YoungDiagram`

`QOU.BraidKnot.HookSum` proves it again in the other register: on Mathlib's
`YoungDiagram`, over `ℤ`, on `PieceAGeneral`'s `armZ`/`legZ`/`hookZ`, with no
sortedness hypothesis. That is not redundancy to be cleaned up — each register
has a native consumer. `TwistUnconditional` uses `hookSum_eq` HERE, in lists;
the Plancherel/`Λ*` argument needs the `2·Σ_h = p₂(λ) + p₂(λ')` form THERE, in
diagrams. Converting either consumer costs more than keeping both statements.

**The two are provably the same**, not merely similar:
`QOU.BraidKnot.HookSumRegisterBridge.hookSum_rowLens` identifies the two hook
sums, and `sum_hookZ_eq_bStat_via_list` re-derives the `YoungDiagram` closed
form from `hookSum_eq` below. So if either proof drifts, the bridge stops
compiling — which is the protection that retiring one of them would have bought.

If you change a statement in this file, expect to fix the bridge, and read its
docstring first: the registers agree only ON A CELL, because the truncated `ℕ`
subtraction here is exact exactly there.
-/

namespace QOU.HookSumComplete

open Finset

/-- A `≤`-downward-closed finite subset of `ℕ` is an initial segment. -/
theorem downward_closed_eq_range {S : Finset ℕ}
    (h : ∀ a b, a ≤ b → b ∈ S → a ∈ S) : S = Finset.range S.card := by
  ext a
  simp only [Finset.mem_range]
  constructor
  · intro ha
    have hsub : Finset.range (a + 1) ⊆ S := by
      intro x hx
      exact h x a (Nat.lt_succ_iff.mp (Finset.mem_range.mp hx)) ha
    have hc := Finset.card_le_card hsub
    rw [Finset.card_range] at hc
    omega
  · intro ha
    by_contra hn
    have hsub : S ⊆ Finset.range a := by
      intro x hx
      rw [Finset.mem_range]
      by_contra hx2
      push_neg at hx2
      exact hn (h a x hx2 hx)
    have hc := Finset.card_le_card hsub
    rw [Finset.card_range] at hc
    omega

/-- Column length `colLen λ j = #{ i : λ_i > j }`. -/
def colLen (l : List ℕ) (j : ℕ) : ℕ :=
  ((Finset.range l.length).filter (fun i => j < l.getD i 0)).card

/-- **Sorted-prefix lemma**: for a weakly-decreasing `λ`, the rows exceeding
column `j` are exactly `{0, …, colLen j − 1}`. -/
theorem sorted_prefix (l : List ℕ) (j : ℕ)
    (hsort : ∀ a b, a ≤ b → b < l.length → l.getD b 0 ≤ l.getD a 0) :
    (Finset.range l.length).filter (fun i => j < l.getD i 0)
      = Finset.range (colLen l j) := by
  apply downward_closed_eq_range
  intro a b hab hb
  simp only [Finset.mem_filter, Finset.mem_range] at hb ⊢
  obtain ⟨hblt, hbj⟩ := hb
  refine ⟨lt_of_le_of_lt hab hblt, ?_⟩
  exact lt_of_lt_of_le hbj (hsort a b hab hblt)

/-- `Σ_{i<len} λ_i = l.sum`. -/
theorem sum_range_getD (l : List ℕ) :
    ∑ i ∈ Finset.range l.length, l.getD i 0 = l.sum := by
  induction l with
  | nil => simp
  | cons a t ih =>
    rw [List.length_cons, Finset.sum_range_succ', List.sum_cons]
    simp only [List.getD_cons_succ, List.getD_cons_zero]
    rw [ih]; ring

/-- **Cell regrouping** (the workhorse): summing any `h i j` over the cells of a
sorted `λ` rows-first equals columns-first, `Σ_i Σ_{j<λ_i} h i j =
Σ_j Σ_{i<colLen j} h i j`. Both iterate the same cell set `{(i,j) : j < λ_i} =
{(i,j) : i < colLen j}` (sorted-prefix). -/
theorem sum_cells_group (l : List ℕ) (M : ℕ)
    (hsort : ∀ a b, a ≤ b → b < l.length → l.getD b 0 ≤ l.getD a 0)
    (hM : ∀ i ∈ Finset.range l.length, l.getD i 0 ≤ M)
    (h : ℕ → ℕ → ℕ) :
    ∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range (l.getD i 0), h i j
      = ∑ j ∈ Finset.range M, ∑ i ∈ Finset.range (colLen l j), h i j := by
  have e1 : ∀ i ∈ Finset.range l.length,
      (∑ j ∈ Finset.range (l.getD i 0), h i j)
        = ∑ j ∈ Finset.range M, (if j < l.getD i 0 then h i j else 0) := by
    intro i hi
    rw [Finset.sum_ite]
    simp only [Finset.sum_const_zero, add_zero]
    congr 1
    ext j
    simp only [Finset.mem_filter, Finset.mem_range]
    constructor
    · intro hj; exact ⟨lt_of_lt_of_le hj (hM i hi), hj⟩
    · intro hj; exact hj.2
  rw [Finset.sum_congr rfl e1, Finset.sum_comm]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [← Finset.sum_filter, sorted_prefix l j hsort]

/-- `Σ_{i<m} i = C(m,2)` reindex helper: `Σ_{i<m}(m-1-i) = Σ_{i<m} i`. -/
theorem sum_range_sub_rev (m : ℕ) :
    ∑ i ∈ Finset.range m, (m - 1 - i) = ∑ i ∈ Finset.range m, i := by
  rw [← Finset.sum_range_reflect]
  refine Finset.sum_congr rfl fun i hi => ?_
  have : i < m := Finset.mem_range.mp hi
  omega

/-- `b(λ) = Σ_i i · λ_i`. -/
def bStat (l : List ℕ) : ℕ := ∑ i ∈ Finset.range l.length, i * l.getD i 0

/-- `b(λ') = Σ_j (colLen j) · j` — `b` of the conjugate, as a column sum. -/
def colSum (l : List ℕ) (M : ℕ) : ℕ := ∑ j ∈ Finset.range M, (colLen l j) * j

/-- The arm part `Σ_c arm(c) = Σ_i Σ_{j<λ_i} (λ_i − 1 − j)`. -/
def armPart (l : List ℕ) : ℕ :=
  ∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range (l.getD i 0), (l.getD i 0 - 1 - j)

/-- The leg part `Σ_c leg(c) = Σ_i Σ_{j<λ_i} (colLen j − 1 − i)`. -/
def legPart (l : List ℕ) : ℕ :=
  ∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range (l.getD i 0), (colLen l j - 1 - i)

/-- The hook sum `Σ_c h(c) = Σ_i Σ_{j<λ_i} (arm + leg + 1)`. -/
def hookSum (l : List ℕ) : ℕ :=
  ∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range (l.getD i 0),
    ((l.getD i 0 - 1 - j) + (colLen l j - 1 - i) + 1)

/-- `Σ_c arm(c) = b(λ')` (the column sum). -/
theorem armPart_eq_colSum (l : List ℕ) (M : ℕ)
    (hsort : ∀ a b, a ≤ b → b < l.length → l.getD b 0 ≤ l.getD a 0)
    (hM : ∀ i ∈ Finset.range l.length, l.getD i 0 ≤ M) :
    armPart l = colSum l M := by
  have hrev : armPart l
      = ∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range (l.getD i 0), j := by
    unfold armPart; exact Finset.sum_congr rfl fun i _ => sum_range_sub_rev _
  have hswap : (∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range (l.getD i 0), j)
      = ∑ j ∈ Finset.range M, ∑ i ∈ Finset.range (colLen l j), j :=
    sum_cells_group l M hsort hM (fun _ j => j)
  have hcol : (∑ j ∈ Finset.range M, ∑ i ∈ Finset.range (colLen l j), j) = colSum l M := by
    unfold colSum
    exact Finset.sum_congr rfl fun j _ => by
      rw [Finset.sum_const, Finset.card_range, smul_eq_mul]
  rw [hrev, hswap, hcol]

/-- `Σ_c leg(c) = b(λ)`. Both collapse to `Σ_j C(colLen j, 2)`. -/
theorem legPart_eq_bStat (l : List ℕ) (M : ℕ)
    (hsort : ∀ a b, a ≤ b → b < l.length → l.getD b 0 ≤ l.getD a 0)
    (hM : ∀ i ∈ Finset.range l.length, l.getD i 0 ≤ M) :
    legPart l = bStat l := by
  have hleg : legPart l
      = ∑ j ∈ Finset.range M, ∑ i ∈ Finset.range (colLen l j), (colLen l j - 1 - i) := by
    unfold legPart; exact sum_cells_group l M hsort hM (fun i j => colLen l j - 1 - i)
  have hb : bStat l = ∑ j ∈ Finset.range M, ∑ i ∈ Finset.range (colLen l j), i := by
    have hbi : bStat l
        = ∑ i ∈ Finset.range l.length, ∑ _j ∈ Finset.range (l.getD i 0), i := by
      unfold bStat
      exact Finset.sum_congr rfl fun i _ => by
        rw [Finset.sum_const, Finset.card_range, smul_eq_mul]; ring
    rw [hbi]; exact sum_cells_group l M hsort hM (fun i _ => i)
  rw [hleg, hb]
  exact Finset.sum_congr rfl fun j _ => sum_range_sub_rev _

/-- **The full hook-sum identity**, for every sorted partition (leg-sum lemma
closed): `Σ_c h(c) = b(λ') + b(λ) + n`, with `b(λ')` the column sum. -/
theorem hookSum_eq (l : List ℕ) (M : ℕ)
    (hsort : ∀ a b, a ≤ b → b < l.length → l.getD b 0 ≤ l.getD a 0)
    (hM : ∀ i ∈ Finset.range l.length, l.getD i 0 ≤ M) :
    hookSum l = colSum l M + bStat l + l.sum := by
  have hsplit : hookSum l = armPart l + legPart l
      + ∑ i ∈ Finset.range l.length, ∑ _j ∈ Finset.range (l.getD i 0), 1 := by
    unfold hookSum armPart legPart
    rw [← Finset.sum_add_distrib, ← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [← Finset.sum_add_distrib, ← Finset.sum_add_distrib]
  have hn : (∑ i ∈ Finset.range l.length, ∑ _j ∈ Finset.range (l.getD i 0), 1) = l.sum := by
    simp only [Finset.sum_const, smul_eq_mul, mul_one, Finset.card_range]
    exact sum_range_getD l
  rw [hsplit, armPart_eq_colSum l M hsort hM, legPart_eq_bStat l M hsort hM, hn]

end QOU.HookSumComplete
