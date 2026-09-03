import QOU.BraidKnot.KeystoneModularTwist

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

end QOU.MathlibExt.ContentSumNStatistic
