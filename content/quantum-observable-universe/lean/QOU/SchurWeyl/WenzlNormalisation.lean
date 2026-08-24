import QOU.SchurWeyl.AddableCellIndexing
import QOU.Mathlib.StandardYoungTableauBot
import QOU.Mathlib.SYTBranchingRule

/-!
# QOU.SchurWeyl.WenzlNormalisation — `∑_{|μ|=n} f^μ w_μ = 1`, at every level

`MarkovNormalisation` proves the normalisation at `r = 2`, over `ℝ`, at convention D.  This is the
same argument at every level `r` for the normalised Wenzl weight, over any field.

| | |
|---|---|
| `colLen_zero_le_addCell` | adding a box never lowers the row count |
| `sum_addable_wenzlWeight_all` | branching **with no row-count hypothesis** |
| `sum_dim_wenzlWeight_succ` | the weighted dimension sum does not depend on `n` |
| `sum_dim_wenzlWeight_eq_one` | **`∑_{|μ|=n} f^μ w_μ = 1`** |

**The row-count hypothesis has to go first, and that is not bookkeeping.**  The induction sums over
*every* diagram of size `n`, including those with more than `r` rows, where
`sum_addable_wenzlWeight` does not apply.  There the identity still holds, but for the opposite
reason: both sides are `0` — the diagram's weight vanishes, and so does every diagram obtained from
it, since adding a box cannot reduce the row count.  Missing this would leave the induction stuck on
exactly the diagrams the level-`r` cap is about.

Together with `wenzlWeight_eq_zero_iff` and `sum_wenzlWeight_addCellOrSelf`, both defining properties
of the level-`r` weight system are now proved at every level: the weights vanish above `r` rows, they
are consistent under restriction, and they sum to `1`.

## Base ring (§7c)

Generic `[Field F]` — the `r = 2` chain is `ℝ` only because `markovWeight` is.  No ordering.

LaTeX label: `thm:wenzl-normalisation`
-/

namespace QOU.SchurWeyl

open YoungDiagram Finset QOU.Mathlib

variable {F : Type*} [Field F]

/-- Adding a box never lowers the row count. -/
theorem colLen_zero_le_addCell {μ : YoungDiagram} {s : ℕ × ℕ} (hs : IsAddableCell μ s) :
    μ.colLen 0 ≤ (addCell μ s hs).colLen 0 := by
  rcases Nat.eq_zero_or_pos (μ.colLen 0) with h0 | hp
  · omega
  · have hmem : ((μ.colLen 0 - 1, 0) : ℕ × ℕ) ∈ μ := mem_iff_lt_colLen.mpr (by omega)
    have hmem' : ((μ.colLen 0 - 1, 0) : ℕ × ℕ) ∈ addCell μ s hs :=
      (mem_addCell _ hs _).mpr (Or.inr hmem)
    have := mem_iff_lt_colLen.mp hmem'
    omega

/-- **Branching, with no row-count hypothesis.**  Above `r` rows both sides are `0`. -/
theorem sum_addable_wenzlWeight_all (Q : F) (hQ0 : Q ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) {r : ℕ} (hbr : levelBracket r Q ≠ 0) (hQ1 : Q ≠ 1)
    (μ : YoungDiagram) :
    (∑ s : {s : ℕ × ℕ // IsAddableCell μ s}, wenzlWeight r Q (addCellOrSelf μ s.1))
      = wenzlWeight r Q μ := by
  rcases le_or_gt (μ.colLen 0) r with hle | hgt
  · exact sum_addable_wenzlWeight Q hQ0 hgen hbr hQ1 hle
  · rw [(wenzlWeight_eq_zero_iff hQ0 hgen hbr μ).mpr hgt]
    refine Finset.sum_eq_zero fun s _ => ?_
    rw [addCellOrSelf_of s.2]
    refine (wenzlWeight_eq_zero_iff hQ0 hgen hbr _).mpr ?_
    have := colLen_zero_le_addCell s.2
    omega

/-- **The weighted dimension sum does not depend on `n`.** -/
theorem sum_dim_wenzlWeight_succ (Q : F) (hQ0 : Q ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) {r : ℕ} (hbr : levelBracket r Q ≠ 0) (hQ1 : Q ≠ 1)
    (n : ℕ) :
    (∑ L : {ρ : YoungDiagram // ρ.cells.card = n + 1},
        (numStandardYoungTableaux L.1 : F) * wenzlWeight r Q L.1)
      = ∑ ν : {ν : YoungDiagram // ν.cells.card = n},
          (numStandardYoungTableaux ν.1 : F) * wenzlWeight r Q ν.1 := by
  classical
  set G : {ν : YoungDiagram // ν.cells.card = n} → (ℕ × ℕ) → F :=
    fun ν c => (numStandardYoungTableaux ν.1 : F) * wenzlWeight r Q (addCellOrSelf ν.1 c) with hG
  have step : ∀ L : {ρ : YoungDiagram // ρ.cells.card = n + 1},
      (numStandardYoungTableaux L.1 : F) * wenzlWeight r Q L.1
        = ∑ c : {c : ℕ × ℕ // IsCornerCell L.1 c},
            G ⟨eraseCorner L.1 c.1 c.2, by
              have := card_eraseCorner L.1 c.1 c.2
              have := L.2
              omega⟩ c.1 := by
    intro L
    have hpos : 0 < L.1.cells.card := by rw [L.2]; omega
    rw [numStandardYoungTableaux_branching hpos, Nat.cast_sum, Finset.sum_mul]
    refine Finset.sum_congr rfl fun c _ => ?_
    rw [hG]
    have hadd : addCellOrSelf (eraseCorner L.1 c.1 c.2) c.1 = L.1 := by
      rw [addCellOrSelf_of (isAddableCell_eraseCorner c.1 c.2), addCell_eraseCorner]
    simp only [hadd]
  calc (∑ L : {ρ : YoungDiagram // ρ.cells.card = n + 1},
        (numStandardYoungTableaux L.1 : F) * wenzlWeight r Q L.1)
      = ∑ L : {ρ : YoungDiagram // ρ.cells.card = n + 1},
          ∑ c : {c : ℕ × ℕ // IsCornerCell L.1 c},
            G ⟨eraseCorner L.1 c.1 c.2, by
              have := card_eraseCorner L.1 c.1 c.2
              have := L.2
              omega⟩ c.1 := Finset.sum_congr rfl fun L _ => step L
    _ = ∑ ν : {ν : YoungDiagram // ν.cells.card = n},
          ∑ s : {s : ℕ × ℕ // IsAddableCell ν.1 s}, G ν s.1 :=
        sum_corner_eq_sum_addable n G
    _ = ∑ ν : {ν : YoungDiagram // ν.cells.card = n},
          (numStandardYoungTableaux ν.1 : F) * wenzlWeight r Q ν.1 := by
        refine Finset.sum_congr rfl fun ν _ => ?_
        rw [hG]
        simp only
        rw [← Finset.mul_sum, sum_addable_wenzlWeight_all Q hQ0 hgen hbr hQ1 ν.1]

theorem eq_bot_of_card_zero' (ν : YoungDiagram) (h : ν.cells.card = 0) : ν = ⊥ := by
  have hc : ν.cells = ∅ := Finset.card_eq_zero.mp h
  ext c
  rw [hc]
  simp [YoungDiagram.cells_bot]

theorem sum_dim_wenzlWeight_zero (Q : F) (r : ℕ) :
    (∑ ν : {ν : YoungDiagram // ν.cells.card = 0},
        (numStandardYoungTableaux ν.1 : F) * wenzlWeight r Q ν.1) = 1 := by
  have hb : (⊥ : YoungDiagram).cells.card = 0 := by rw [YoungDiagram.cells_bot]; rfl
  rw [Fintype.sum_eq_single (⟨⊥, hb⟩ : {ν : YoungDiagram // ν.cells.card = 0})
    (fun x hx => absurd (Subtype.ext (eq_bot_of_card_zero' x.1 x.2)) hx)]
  rw [wenzlWeight_bot, numStandardYoungTableaux_bot]
  norm_num

/-- **The normalisation, at every `n` and every level `r`.** -/
theorem sum_dim_wenzlWeight_eq_one (Q : F) (hQ0 : Q ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) {r : ℕ} (hbr : levelBracket r Q ≠ 0) (hQ1 : Q ≠ 1)
    (n : ℕ) :
    (∑ ν : {ν : YoungDiagram // ν.cells.card = n},
        (numStandardYoungTableaux ν.1 : F) * wenzlWeight r Q ν.1) = 1 := by
  induction n with
  | zero => exact sum_dim_wenzlWeight_zero Q r
  | succ n ih => rw [sum_dim_wenzlWeight_succ Q hQ0 hgen hbr hQ1 n]; exact ih

end QOU.SchurWeyl
