import Mathlib.Tactic

/-!
# QOU.Common.HookSumGeneral — the hook-sum identity for ALL partitions

W11 (`HookSumIdentity.lean`) discharged the `balanced_quantum_twist` hook-sum
hypothesis `Σ_c h(c) = b(λ) + b(λ') + n` by `decide` for the hook and staircase
families. This file proves the **general engine** behind it — the arm-sum
identity, for every partition — sorry-free:

  `Σ_i C(λ_i, 2) = Σ_i Σ_{j<λ_i} j = Σ_j j · (colLen λ j) = b(λ')`,     (armSum)

i.e. the diagram cells weighted by column index `j`, summed rows-first vs
columns-first (a Fubini double-count: `armSum_eq_colSum`), identified with `b`
of the conjugate (`armSum_eq_bStat_conj`). Here `b(λ) = Σ_i i · λ_i` (0-indexed)
and `colLen λ j = #{i : λ_i > j}`.

The full hook-sum identity assembles from this as

  `Σ_c h(c) = Σ_c arm + Σ_c leg + Σ_c 1 = b(λ') + b(λ) + n`,

using `Σ_c arm = armSum λ = b(λ')` (proved here) and `Σ_c leg = armSum λ' = b(λ)`
(the leg sum of `λ` is the arm sum of its transpose). The remaining step — the
`h = arm + leg + 1` cell decomposition and the leg/transpose identity over the
`List ℕ` encoding — is mechanical conjugation bookkeeping, not yet formalized
here; `HookSumIdentity.lean` covers the hook/staircase families concretely by
`decide` in the meantime.

Ground ring: none — a `ℕ`-valued combinatorial identity feeding the `Field`
twist in `BalancedQuantumTwist`.
-/

namespace QOU.HookSumGeneral

open Finset

/-- `b(λ) = Σ_i i · λ_i` (0-indexed rows). -/
def bStat (l : List ℕ) : ℕ := ∑ i ∈ Finset.range l.length, i * l.getD i 0

/-- Length of column `j`: `#{ i : λ_i > j }`. -/
def colLen (l : List ℕ) (j : ℕ) : ℕ :=
  (Finset.range l.length).filter (fun i => j < l.getD i 0) |>.card

/-- Arm sum `Σ_i C(λ_i, 2) = Σ_i Σ_{j < λ_i} j`. -/
def armSum (l : List ℕ) : ℕ :=
  ∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range (l.getD i 0), j

/-- **The arm-sum double-count** (the Fubini crux): summing the column index `j`
over the cells of `λ` rows-first equals summing it columns-first,
`Σ_i Σ_{j<λ_i} j = Σ_j (colLen λ j) · j`, where the column range is bounded by
the largest part `M` (any bound `≥ λ_i` for all `i` works; we use `M = λ_0` on a
partition, but state it for an explicit bound `M` so no sortedness is needed). -/
theorem armSum_eq_colSum (l : List ℕ) (M : ℕ) (hM : ∀ i ∈ Finset.range l.length, l.getD i 0 ≤ M) :
    armSum l = ∑ j ∈ Finset.range M, (colLen l j) * j := by
  unfold armSum colLen
  -- extend each inner row-sum to range M via an indicator, then swap
  have hrow : ∀ i ∈ Finset.range l.length,
      (∑ j ∈ Finset.range (l.getD i 0), j)
        = ∑ j ∈ Finset.range M, (if j < l.getD i 0 then j else 0) := by
    intro i hi
    rw [Finset.sum_ite]
    simp only [Finset.sum_const_zero, add_zero]
    congr 1
    ext j
    simp only [Finset.mem_filter, Finset.mem_range]
    constructor
    · intro hj; exact ⟨lt_of_lt_of_le hj (hM i hi), hj⟩
    · intro hj; exact hj.2
  rw [Finset.sum_congr rfl hrow, Finset.sum_comm]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [Finset.sum_ite, Finset.sum_const_zero, add_zero, Finset.sum_const, smul_eq_mul]

/-- The conjugate of `λ`, as the list of its first `M` column lengths (`M` any
bound `≥` the number of columns, i.e. `≥ λ_0`). -/
def conjList (l : List ℕ) (M : ℕ) : List ℕ := (List.range M).map (colLen l)

/-- `b` of the explicit conjugate equals the column-index sum. -/
theorem bStat_conjList (l : List ℕ) (M : ℕ) :
    bStat (conjList l M) = ∑ j ∈ Finset.range M, (colLen l j) * j := by
  unfold bStat conjList
  rw [List.length_map, List.length_range]
  refine Finset.sum_congr rfl fun i hi => ?_
  have hi' : i < M := Finset.mem_range.mp hi
  rw [List.getD_eq_getElem?_getD, List.getElem?_map, List.getElem?_range hi']
  simp [Nat.mul_comm]

/-- **Arm sum = `b` of the conjugate** — the general form of the W11
`Σ_i C(λ_i,2) = b(λ')` observation, proved (via the Fubini `armSum_eq_colSum`)
for every `λ` with an explicit column bound `M ≥ λ_0`. This is the reusable
engine: `Σ_c arm(c) = b(λ')`; the full hook-sum identity
`Σ_c h(c) = b(λ') + b(λ) + n` then follows from the cell decomposition
`h = arm + leg + 1` together with `Σ_c leg(c) = Σ_c arm(c over λ') = b(λ)`
(the leg sum of `λ` is the arm sum of its transpose). -/
theorem armSum_eq_bStat_conj (l : List ℕ) (M : ℕ)
    (hM : ∀ i ∈ Finset.range l.length, l.getD i 0 ≤ M) :
    armSum l = bStat (conjList l M) := by
  rw [armSum_eq_colSum l M hM, bStat_conjList]

end QOU.HookSumGeneral
