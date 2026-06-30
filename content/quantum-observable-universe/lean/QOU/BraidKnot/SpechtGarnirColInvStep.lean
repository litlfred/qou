import QOU.BraidKnot.SpechtGarnirCore
import QOU.BraidKnot.SpechtGarnirMeasure

/-!
# QOU.BraidKnot.SpechtGarnirColInvStep — the case-1 (column-sort) straightening step

When a column-monotone tableau is *not* yet column-standard — there is an adjacent
column inversion `(a, b)` — swapping the pair is a column permutation `κ ∈ C_t`, so
`e_{κ·t} = sgn(κ)·e_t = −e_t` (column-alternating law). The swapped tableau `κ·t`
has the **same** `colWt` (`colWt_smul_colStab`) but strictly smaller `colInv`
(`colInv_swap_lt`), hence strictly smaller combined measure `garnirWt`. So:

> `polytabloid_colInv_step` — `e_t ∈ span{e_s : garnirWt s < garnirWt t}` for any
> adjacent column inversion. (No characteristic assumption.)

This is the case-1 leg of the brick-4 straightening, dual to the case-2 Garnir
step `SpechtGarnirStep.polytabloid_garnir_step`.
-/

namespace QOU.BraidKnot.SpechtGarnirColInvStep

open QOU.BraidKnot.Specht
open QOU.BraidKnot.SpechtGarnirCore
open QOU.BraidKnot.SpechtGarnirWt
open QOU.BraidKnot.SpechtColInv
open QOU.BraidKnot.SpechtGarnirMeasure

variable {k : Type} [CommRing k]
variable {μ : YoungDiagram}

/-- **Case-1 straightening step.** An adjacent column inversion `(a, b)` (same
column, `(a:ℕ) < (b:ℕ)`, `b` higher than `a` by one row) puts `e_t` in the span of
strictly-smaller-`garnirWt` polytabloids, via `e_t = −e_{κ·t}` with `κ = (a b)` and
`garnirWt (κ·t) < garnirWt t` (same `colWt`, smaller `colInv`). -/
theorem polytabloid_colInv_step {t : Tableau μ} {a b : Fin (Specht.nOf μ)}
    (hcol : Specht.colPattern t a = Specht.colPattern t b) (hab : (a : ℕ) < (b : ℕ))
    (hrow : Specht.rowPattern t b < Specht.rowPattern t a)
    (hadj : Specht.rowPattern t a = Specht.rowPattern t b + 1) :
    polytabloid (k := k) t ∈ Submodule.span k
      {x | ∃ s : Tableau μ, garnirWt s < garnirWt t ∧ x = polytabloid (k := k) s} := by
  have hab' : a ≠ b := fun h => by rw [h] at hab; exact lt_irrefl _ hab
  have hκ : Equiv.swap a b ∈ Specht.colStab t := swap_mem_colStab_of_sameCol hcol
  have hrel : polytabloid (k := k) (Equiv.swap a b • t) = -polytabloid (k := k) t := by
    rw [← rep_polytabloid, polytabloid_rep_colStab t hκ, Equiv.Perm.sign_swap hab']
    simp
  have het : polytabloid (k := k) t = -polytabloid (k := k) (Equiv.swap a b • t) := by
    rw [hrel, neg_neg]
  have hwt : garnirWt (Equiv.swap a b • t) < garnirWt t :=
    garnirWt_lt_of_colInv_lt (colWt_smul_colStab hκ) (colInv_swap_lt hcol hab hrow hadj)
  rw [het]
  exact Submodule.neg_mem _ (Submodule.subset_span ⟨Equiv.swap a b • t, hwt, rfl⟩)

end QOU.BraidKnot.SpechtGarnirColInvStep
