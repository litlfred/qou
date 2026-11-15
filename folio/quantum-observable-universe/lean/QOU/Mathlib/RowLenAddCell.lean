import QOU.Mathlib.ContentProductRows
import QOU.Mathlib.SYTBetaZeroPadding
import QOU.SchurWeyl.HookLengthAddCell

/-!
# QOU.Mathlib.RowLenAddCell — row lengths under `addCell`, and `rowLens` past its end

Two small facts the general-`r` branching assembly needs, both about *shape* rather than about
weights.

| | |
|---|---|
| `eq_of_lt_iff_lt` | two naturals with the same `<`-downset are equal |
| `rowLen_addCell` | `rowLen (addCell μ s) i = rowLen μ i + [i = s₁]` |
| `getD_rowLens` | `μ.rowLens.getD i 0 = μ.rowLen i` for **every** `i`, not only `i < |rowLens|` |

`getD_rowLens` is the one that is easy to get wrong: past the end of the list `getD` returns the
default `0`, and `rowLen` returns `0` too, so the identity holds unconditionally — but only because
`rowLens` has exactly `colLen 0` entries, which is what `rowLen_eq_zero_of_colLen_le` supplies.  It
is what lets the List-indexed hook side and the `range r`-indexed content side be compared
without a side condition on `i`.

`rowLen_addCell` is the `β ↦ β + e_a` step: adding a box at `s` raises row `s₁`'s length by one and
leaves every other row alone, hence raises `β_{s₁}` by one and fixes the rest — which is exactly the
single-node update `VandermondeUpdateRatio` is about.

## Base ring (§7c)

None — pure `ℕ` and `YoungDiagram` combinatorics.

LaTeX label: `lem:rowlen-addcell`
-/

namespace QOU.Mathlib.SYTBeta

open YoungDiagram QOU.SchurWeyl

/-- Two naturals with the same `<`-downset are equal. -/
theorem eq_of_lt_iff_lt {a b : ℕ} (h : ∀ j, j < a ↔ j < b) : a = b := by
  rcases Nat.lt_trichotomy a b with hlt | heq | hgt
  · exact absurd ((h a).mpr hlt) (Nat.lt_irrefl a)
  · exact heq
  · exact absurd ((h b).mp hgt) (Nat.lt_irrefl b)

/-- **Adding a box raises exactly one row length.** -/
theorem rowLen_addCell {μ : YoungDiagram} {s : ℕ × ℕ} (hs : IsAddableCell μ s) (i : ℕ) :
    (addCell μ s hs).rowLen i = μ.rowLen i + (if i = s.1 then 1 else 0) := by
  have hs2 : s.2 = μ.rowLen s.1 := rowLen_of_isAddableCell hs
  refine eq_of_lt_iff_lt fun j => ?_
  rw [← mem_iff_lt_rowLen, mem_addCell]
  by_cases hi : i = s.1
  · rw [if_pos hi]
    constructor
    · rintro (heq | hmem)
      · have hj : j = s.2 := by simpa using congrArg Prod.snd heq
        rw [hi]
        omega
      · exact lt_of_lt_of_le (mem_iff_lt_rowLen.mp hmem) (by omega)
    · intro hlt
      rcases Nat.lt_or_ge j (μ.rowLen i) with h | h
      · exact Or.inr (mem_iff_lt_rowLen.mpr h)
      · refine Or.inl ?_
        have hj : j = s.2 := by rw [hs2, ← hi]; omega
        rw [Prod.ext_iff]
        exact ⟨hi, hj⟩
  · rw [if_neg hi, Nat.add_zero]
    constructor
    · rintro (heq | hmem)
      · exact absurd (congrArg Prod.fst heq) hi
      · exact mem_iff_lt_rowLen.mp hmem
    · intro hlt
      exact Or.inr (mem_iff_lt_rowLen.mpr hlt)

/-- **`rowLens` agrees with `rowLen` at every index**, including past its end where both are `0`. -/
theorem getD_rowLens (μ : YoungDiagram) (i : ℕ) : μ.rowLens.getD i 0 = μ.rowLen i := by
  rcases lt_or_ge i μ.rowLens.length with hi | hi
  · rw [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem hi, Option.getD_some, get_rowLens]
  · rw [getD_eq_zero_of_le hi,
      rowLen_eq_zero_of_colLen_le (by rwa [length_rowLens] at hi)]

end QOU.Mathlib.SYTBeta
