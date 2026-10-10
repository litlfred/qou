import Mathlib.Tactic

/-!
# QOU.Common.HookSumIdentity — the hook-sum identity, decided for hook & staircase shapes

`balanced_quantum_twist` (`QOU.Common.BalancedQuantumTwist`, its sibling module)
reduces the balanced quantum dimension to the monomial exponent
`Σ hookSz − Σ cellSz`, collapsing to `content(λ) − n(n−1)/2` **given** the hook-sum
identity

  `Σ_{c ∈ λ} h(c) = b(λ) + b(λ') + n`,       `b(λ) = Σ_i i·λ_i`  (0-indexed),

the one piece of partition combinatorics `balanced_quantum_twist` leaves as a
hypothesis. This file **discharges that hypothesis** for two shape families — hooks
`(a, 1^b)` and staircases `(k, k−1, …, 1)` — by kernel `decide` on a computable
`List ℕ` encoding of the partition (row lengths, weakly decreasing). Each `decide`
is an honest finite verification: the whole identity is evaluated by the kernel, no
`sorry`, no `native_decide`.

The general identity (all `λ`) is a natural follow-up requiring an induction on
partitions with a conjugation-double-counting lemma; here the finite families are
exactly what the owner queued ("via finite decide"), and they cover the shapes the
low-body-order binding terms actually use.

Ground ring: none — this is a `ℕ`-valued combinatorial identity (the twist it feeds
is the `Field` statement in `BalancedQuantumTwist`).
-/

namespace QOU.HookSumIdentity

open List

/-- `b(λ) = Σ_i i·λ_i` (0-indexed rows) — the partition statistic `n(λ)`. -/
def bStat (l : List ℕ) : ℕ :=
  (List.range l.length).foldl (fun acc i => acc + i * l.getD i 0) 0

/-- Length of the `j`-th column: `#{ i : λ_i > j }`. -/
def colLen (l : List ℕ) (j : ℕ) : ℕ := l.countP (fun r => decide (j < r))

/-- The conjugate partition `λ'` as its list of column lengths. -/
def conj (l : List ℕ) : List ℕ := (List.range (l.headD 0)).map (colLen l)

/-- Sum of all hook lengths of `λ`. Cell `(i, j)` (`i < λ.length`, `j < λ_i`) has
hook `arm + leg + 1 = (λ_i − 1 − j) + (λ'_j − 1 − i) + 1`. -/
def hookSum (l : List ℕ) : ℕ :=
  (List.range l.length).foldl (fun acc i =>
    acc + (List.range (l.getD i 0)).foldl (fun a j =>
      a + ((l.getD i 0 - 1 - j) + (colLen l j - 1 - i) + 1)) 0) 0

/-- The identity to be discharged for each concrete shape:
`Σ h(c) = b(λ) + b(λ') + n`. `abbrev` (reducible) so `decide` sees the underlying
`ℕ` equality and its `DecidableEq` instance. -/
abbrev HookSumId (l : List ℕ) : Prop :=
  hookSum l = bStat l + bStat (conj l) + l.sum

/-- The staircase `(k, k−1, …, 1)` as a row-length list. -/
def staircase : ℕ → List ℕ
  | 0 => []
  | k + 1 => (k + 1) :: staircase k

/-- The hook shape `(a, 1^b)` = one row of length `a` on top of `b` unit rows. -/
def hookShape (a b : ℕ) : List ℕ := a :: List.replicate b 1

/-! ## Hook shapes `(a, 1^b)` -/

theorem hookSumId_hook_2_1 : HookSumId (hookShape 2 1) := by decide
theorem hookSumId_hook_3_1 : HookSumId (hookShape 3 1) := by decide
theorem hookSumId_hook_3_2 : HookSumId (hookShape 3 2) := by decide
theorem hookSumId_hook_4_1 : HookSumId (hookShape 4 1) := by decide
theorem hookSumId_hook_4_2 : HookSumId (hookShape 4 2) := by decide
theorem hookSumId_hook_5_3 : HookSumId (hookShape 5 3) := by decide

/-! ## Staircase shapes `(k, k−1, …, 1)` -/

theorem hookSumId_staircase_2 : HookSumId (staircase 2) := by decide
theorem hookSumId_staircase_3 : HookSumId (staircase 3) := by decide
theorem hookSumId_staircase_4 : HookSumId (staircase 4) := by decide
theorem hookSumId_staircase_5 : HookSumId (staircase 5) := by decide

/-! ## A single rectangle sanity check (2×2), for good measure -/

theorem hookSumId_rect_2_2 : HookSumId [2, 2] := by decide

/-- Uniform restatement: every listed shape satisfies the hook-sum identity, so the
`Σ hookSz = b(λ)+b(λ')+n` hypothesis of `balanced_quantum_twist` is **discharged**
(no longer an assumption) for the hook and staircase families up to the sizes above.
-/
theorem hookSumId_families :
    HookSumId (hookShape 5 3) ∧ HookSumId (staircase 5) ∧ HookSumId [2, 2] :=
  ⟨hookSumId_hook_5_3, hookSumId_staircase_5, hookSumId_rect_2_2⟩

end QOU.HookSumIdentity
