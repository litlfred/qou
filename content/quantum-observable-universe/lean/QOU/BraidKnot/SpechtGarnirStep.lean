import QOU.BraidKnot.SpechtGarnirAssembly
import QOU.BraidKnot.SpechtGarnirReduction

/-!
# QOU.BraidKnot.SpechtGarnirStep — the one straightening step (modulo the row bound)

Wires the geometric Garnir decrease (`SpechtGarnirAssembly.colWt_lt_of_garnir`)
into the span reduction (`SpechtGarnirReduction.polytabloid_mem_span_colWt_of_decrease`),
discharging the `hdom` quantifier: for a column-monotone tableau with a row-violation
at `(j, r)`, the polytabloid lands in the span of strictly-smaller-`colWt`
polytabloids.

> `polytabloid_garnir_step` — `e_t ∈ span{e_s : colWt s < colWt t}` for a
> column-monotone `t` with a row-violation, **modulo** the pigeonhole row bound
> (`hcard`, `hbound`) on the Garnir set `X = garnirA ∪ garnirB`.

This isolates the *last two* obligations of the brick-4 straightening core into
named hypotheses: the **row bound** (the geometric `|X| > μ'_j` pigeonhole input,
item 2) and — outside this lemma — the **violation existence** (non-standard ⟹ a
row-violation, item 1). Everything else is sorry-free.
-/

namespace QOU.BraidKnot.SpechtGarnirStep

open QOU.BraidKnot.Specht
open QOU.BraidKnot.SpechtGarnirWt
open QOU.BraidKnot.SpechtGarnirGeom
open QOU.BraidKnot.SpechtGarnirAssembly
open QOU.BraidKnot.SpechtGarnirReduction
open Equiv (Perm)

variable {k : Type} [Field k] [CharZero k]
variable {μ : YoungDiagram}

/-- **One Garnir straightening step (modulo the row bound).** For a column-monotone
`t` with a row-violation at `(j, r)` (witnesses `ar, br`), and the pigeonhole row
bound on `X = garnirA ∪ garnirB`, the polytabloid `e_t` lies in the span of
strictly-smaller-`colWt` polytabloids. The `hdom` quantifier is discharged by
`colWt_lt_of_garnir`. -/
theorem polytabloid_garnir_step {t : Tableau μ} (h : ColMono t) {j r : ℕ}
    {ar br : Fin (Specht.nOf μ)}
    (har : Specht.colPattern t ar = j) (harr : Specht.rowPattern t ar = r)
    (hbr : Specht.colPattern t br = j + 1) (hbrr : Specht.rowPattern t br = r)
    (hviol : (br : ℕ) < (ar : ℕ)) {m : ℕ}
    (hcard : m < (garnirA t j r ∪ garnirB t j r).card)
    (hbound : ∀ π : Specht.colStab t, ∀ l ∈ (garnirA t j r ∪ garnirB t j r),
      Specht.rowPattern ((π : Perm (Fin (Specht.nOf μ))) • t) l < m) :
    polytabloid (k := k) t ∈ Submodule.span k
      {x | ∃ s : Tableau μ, colWt s < colWt t ∧ x = polytabloid (k := k) s} := by
  refine polytabloid_mem_span_colWt_of_decrease (k := k) hcard hbound ?_
  intro σ hσnotcol
  exact colWt_lt_of_garnir h har harr hbr hbrr hviol (fun i hi => σ.2 i hi) hσnotcol

end QOU.BraidKnot.SpechtGarnirStep
