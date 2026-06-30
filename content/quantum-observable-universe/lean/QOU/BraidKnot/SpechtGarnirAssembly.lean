import QOU.BraidKnot.SpechtGarnirWt
import QOU.BraidKnot.SpechtGarnirGeom
import QOU.BraidKnot.SpechtGarnirCore

/-!
# QOU.BraidKnot.SpechtGarnirAssembly — Garnir shuffle ⟹ colWt strictly drops

Connects the geometric Garnir set (`SpechtGarnirGeom`) and the supported-on-`X`
subgroup (`SpechtGarnirCore.suppSubgroup`) to the abstract column-dominance
machinery (`SpechtGarnirWt.colWt_lt_of_two_column`). The payoff:

> `colWt_lt_of_garnir` — for a column-monotone tableau with a row-violation at
> `(j, r)`, **every** Garnir shuffle `σ ∈ S_X ∖ C_t` (`X = garnirA ∪ garnirB`)
> strictly decreases the column-dominance measure: `colWt (σ·t) < colWt t`.

This is exactly the `hdom` input of
`SpechtGarnirReduction.polytabloid_mem_span_colWt_of_decrease`; only the violation
**existence** (non-standard ⟹ a violation) and the final span-lever wiring remain.
-/

namespace QOU.BraidKnot.SpechtGarnirAssembly

open QOU.BraidKnot.Specht
open QOU.BraidKnot.SpechtGarnirWt
open QOU.BraidKnot.SpechtGarnirGeom
open QOU.BraidKnot.SpechtGarnirCore
open Equiv (Perm)

variable {μ : YoungDiagram}

/-- A permutation supported on `X` (fixing the complement) preserves `X` setwise. -/
theorem suppSubgroup_stab {X : Finset (Fin (Specht.nOf μ))}
    {σ : Perm (Fin (Specht.nOf μ))}
    (hσ : ∀ i, i ∉ X → σ i = i) (l : Fin (Specht.nOf μ)) :
    σ l ∈ X ↔ l ∈ X := by
  constructor
  · intro hσl
    by_contra hl
    rw [hσ l hl] at hσl; exact hl hσl
  · intro hl
    by_contra hσl
    have heq := σ.injective (hσ (σ l) hσl)
    rw [heq] at hσl; exact hσl hl

/-- **Garnir shuffle ⟹ `colWt` strictly drops.** For a column-monotone `t` with a
row-violation at `(j, r)` (columns `j, j+1`, witnesses `ar, br` in row `r` with the
`(j+1)`-label `< ` the `j`-label), any `σ` supported on `X = garnirA ∪ garnirB` that
is **not** a column permutation strictly decreases `colWt`. -/
theorem colWt_lt_of_garnir {t : Tableau μ} (h : ColMono t) {j r : ℕ}
    {ar br : Fin (Specht.nOf μ)}
    (har : Specht.colPattern t ar = j) (harr : Specht.rowPattern t ar = r)
    (hbr : Specht.colPattern t br = j + 1) (hbrr : Specht.rowPattern t br = r)
    (hviol : (br : ℕ) < (ar : ℕ))
    {σ : Perm (Fin (Specht.nOf μ))}
    (hσ : ∀ i, i ∉ (garnirA t j r ∪ garnirB t j r) → σ i = i)
    (hne : σ ∉ Specht.colStab t) :
    colWt (σ • t) < colWt t := by
  set X := garnirA t j r ∪ garnirB t j r with hX
  have hXcol : ∀ l ∈ X, Specht.colPattern t l = j ∨ Specht.colPattern t l = j + 1 := by
    intro l hl
    rw [hX, Finset.mem_union, garnirA, garnirB, Finset.mem_filter, Finset.mem_filter] at hl
    rcases hl with ⟨_, hcj, _⟩ | ⟨_, hcj, _⟩
    · exact Or.inl hcj
    · exact Or.inr hcj
  have hstab_set := suppSubgroup_stab hσ
  apply colWt_lt_of_two_column (j := j)
  · -- hsupp
    intro l hl
    exact hσ l (fun hlX => hl (hXcol l hlX))
  · -- hstab
    intro l
    by_cases hlX : l ∈ X
    · exact ⟨fun _ => hXcol l hlX, fun _ => hXcol _ ((hstab_set l).mpr hlX)⟩
    · rw [hσ l hlX]
  · -- hbh
    intro m
    refine hbh_of_moved_top (fun l => Specht.colPattern t l = j) σ
      (garnirA t j r) (garnirB t j r) ?_ ?_ ?_ ?_ m
    · intro l hl; rw [garnirA, Finset.mem_filter] at hl; exact hl.2.1
    · intro l hcj hlA
      refine hσ l ?_
      rw [hX, Finset.mem_union]
      rintro (hA | hB)
      · exact hlA hA
      · rw [garnirB, Finset.mem_filter] at hB; omega
    · intro x hx
      rw [Finset.mem_image] at hx
      obtain ⟨l, hlA, rfl⟩ := hx
      exact (hstab_set l).mpr (by rw [hX, Finset.mem_union]; exact Or.inl hlA)
    · exact garnir_htop h har harr hbr hbrr hviol
  · -- hne
    rw [Specht.colPattern_smul]
    intro hc
    exact hne (Specht.mem_colStab.mpr hc)

end QOU.BraidKnot.SpechtGarnirAssembly
