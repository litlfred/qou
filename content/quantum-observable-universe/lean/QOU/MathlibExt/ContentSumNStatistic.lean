import QOU.BraidKnot.KeystoneModularTwist
import QOU.Common.HookSumComplete

/-!
# QOU.MathlibExt.ContentSumNStatistic — `contentSum λ = n(λ') − n(λ)`

The content-sum / `n`-statistic link that was, until now, only a prose comment in
`QPartitionCombinatorics` (the note at `def nLambda`: *"In terms of the conjugate,
`contentSum λ = n(λ') − n(λ)`"*). This is the algebraic half of the **n-statistic identity**
`κ_λ = Σ_x h_x − |λ| − 2·n(λ)` that the telescope-closure convention bridge `hconv` turns on
(audit `docs/audits/2026-08-29-normalizedsum-closes-via-telescope.md`): combined with the
hook-sum identity `Σ_x h_x = |λ| + n(λ) + n(λ')` (`Common.HookSumComplete.hookSum_eq`) it gives
`κ_λ = Σ_x h_x − |λ| − 2·n(λ)`.

`contentSum λ = Σ_{(i,j)} (j − i) = Σ_{cells} j − Σ_{cells} i`. The row part `Σ_{cells} i = Σ_i i·λ_i`
is `n(λ) = nLambda λ`; the column part `Σ_{cells} j`, regrouped by column via the Fubini transpose
`IdentityI.cell_fubini`, is `Σ_j j·colLen(λ, j) = Σ_r r·(conj λ)_r = n(λ') = nLambda (conj λ)`.

Purely combinatorial: `List ℕ` carrier, `ℤ` values, no `ℝ`, no analytic input.

-- Ref: docs/audits/2026-08-29-normalizedsum-closes-via-telescope.md (the n-statistic identity)
-- Ref: content/.../QOU/Common/HookSumComplete.lean (hookSum_eq: Σh = |λ| + n(λ) + n(λ'))
-/

namespace QOU.MathlibExt.ContentSumNStatistic

open Finset
open QOU.MathlibExt.QPartitionCombinatorics
open QOU.BraidKnot.IdentityI
open QOU.BraidKnot.Keystone

/-- **`contentSum λ = n(λ') − n(λ)`** (the conjugate/`n`-statistic form of the content sum), for a
weakly-decreasing partition `λ`. The content of a cell `(i,j)` is `j − i`; summing the `j`-part by
columns gives `n(λ') = nLambda (conj λ)` and the `i`-part by rows gives `n(λ) = nLambda λ`. -/
theorem contentSum_eq_nLambda_conj_sub (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    contentSum l = (nLambda (conj l) : ℤ) - (nLambda l : ℤ) := by
  -- row part: Σ_{cells} i = n(λ)
  have hrow : (∑ i ∈ Finset.range l.length,
      ∑ _j ∈ Finset.range (l.getD i 0), (i : ℤ)) = (nLambda l : ℤ) := by
    rw [nLambda_eq_sum, Nat.cast_sum]
    refine Finset.sum_congr rfl (fun i _ => ?_)
    rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul, List.getD_eq_getElem?_getD]
    push_cast
    ring
  -- column part: Σ_{cells} j = n(λ'), regrouped by column via cell_fubini
  have hcol : (∑ i ∈ Finset.range l.length,
      ∑ j ∈ Finset.range (l.getD i 0), (j : ℤ)) = (nLambda (conj l) : ℤ) := by
    rw [cell_fubini l hl (fun _ j => (j : ℤ)), nLambda_eq_sum, Nat.cast_sum]
    simp only [Partition.length, conj_length]
    refine Finset.sum_congr rfl (fun j hj => ?_)
    rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul,
        ← List.getD_eq_getElem?_getD, conj_getD l j (Finset.mem_range.mp hj)]
    push_cast
    ring
  rw [contentSum_eq_finset]
  simp only [cellContent, Finset.sum_sub_distrib]
  rw [hcol, hrow]

/-- **The two `colLen` encodings agree.** `HookSumComplete.colLen` counts *row indices* `i` with
`λ_i > j` (a `Finset.range` card), while `IdentityI.colLen` filters the *list values* `> j`; both
count `#{cells in column j}`. Bridges the self-contained `HookSumComplete` register (in which the
hook-sum identity `hookSum_eq` is proved) to the `IdentityI`/`conj` register everything else uses. -/
theorem hsc_colLen_eq (l : List ℕ) (j : ℕ) :
    QOU.HookSumComplete.colLen l j = colLen l j := by
  simp only [QOU.HookSumComplete.colLen, colLen, Finset.card_filter]
  induction l with
  | nil => simp
  | cons a t ih =>
    rw [List.length_cons, Finset.sum_range_succ', List.filter_cons]
    simp only [List.getD_cons_succ, List.getD_cons_zero]
    rw [ih]
    by_cases h : j < a <;> simp [h, List.length_cons, Nat.add_comm]

/-- `bStat λ = n(λ)`: the two `Σ_i i·λ_i` encodings agree (`l.getD i 0 = (l[i]?).getD 0`). -/
theorem bStat_eq_nLambda (l : List ℕ) : QOU.HookSumComplete.bStat l = nLambda l := by
  rw [QOU.HookSumComplete.bStat, nLambda_eq_sum]
  simp only [Partition.length]
  exact Finset.sum_congr rfl (fun i _ => by rw [List.getD_eq_getElem?_getD])

/-- `colSum λ (max part) = n(λ')`: the column sum `Σ_j (colLen j)·j` is `n(λ') = nLambda (conj λ)`. -/
theorem colSum_headD_eq_nLambda_conj (l : List ℕ) :
    QOU.HookSumComplete.colSum l (l.headD 0) = nLambda (conj l) := by
  rw [QOU.HookSumComplete.colSum, nLambda_eq_sum]
  simp only [Partition.length, conj_length]
  refine Finset.sum_congr rfl (fun j hj => ?_)
  rw [← List.getD_eq_getElem?_getD, conj_getD l j (Finset.mem_range.mp hj), hsc_colLen_eq]
  ring

/-- The genuine-cell hook sum `Σ_x Partition.hookLength` equals `HookSumComplete.hookSum` (the
`colLen`-hook), cell by cell (`IdentityI.hookLength_eq` + the arm/leg `≥ 1` bounds from
`colLen_duality`, and the `colLen` bridge). Bridges the `Partition.hookLength` encoding (used by
`hookProd`/`schurElement`) to the register in which the hook-sum identity is proved. -/
theorem partitionHookSum_eq_hookSum (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    (∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range (l.getD i 0),
        Partition.hookLength l i j) = QOU.HookSumComplete.hookSum l := by
  rw [QOU.HookSumComplete.hookSum]
  refine Finset.sum_congr rfl (fun i hi => Finset.sum_congr rfl (fun j hj => ?_))
  have hi' : i < l.length := Finset.mem_range.mp hi
  have hj' : j < l.getD i 0 := Finset.mem_range.mp hj
  have hleg : i < colLen l j := (colLen_duality l hl i j).mpr hj'
  rw [hookLength_eq l hl i j hi' hj', ← hsc_colLen_eq]
  rw [← hsc_colLen_eq] at hleg
  omega

/-- **The n-statistic identity** `κ_λ = Σ_x h_x − |λ| − 2·n(λ)`, in the `Partition.hookLength`
encoding used by `hookProd`/`schurElement` — the exponent identity the telescope-closure convention
bridge `hconv` turns on (audit `docs/audits/2026-08-29-normalizedsum-closes-via-telescope.md`).
Combines `contentSum_eq_nLambda_conj_sub` (`κ = n(λ') − n(λ)`) with the hook-sum identity
`Σ_x h_x = n(λ') + n(λ) + |λ|` (`HookSumComplete.hookSum_eq`). -/
theorem contentSum_eq_hookSum_sub (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    contentSum l
      = ((∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range (l.getD i 0),
          Partition.hookLength l i j : ℕ) : ℤ) - (l.sum : ℤ) - 2 * (nLambda l : ℤ) := by
  have hs := QOU.HookSumComplete.hookSum_eq l (l.headD 0)
    (fun a b hab _ => getD_antitone l hl hab)
    (fun i _ => getD_le_headD l hl i)
  rw [partitionHookSum_eq_hookSum l hl, contentSum_eq_nLambda_conj_sub l hl, hs,
      colSum_headD_eq_nLambda_conj l, bStat_eq_nLambda l]
  push_cast
  ring

end QOU.MathlibExt.ContentSumNStatistic
