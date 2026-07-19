import QOU.BraidKnot.SeminormalCharacterConnector
import QOU.Mathlib.SYTEnumerationFintype

/-!
# Tabulated `c_λ` for the larger self-conjugate shapes → `{3, 8, 10}`

Completes the tabulated `c_λ` of `prop:symbolic-character-table` (bean `qou-tqab`)
begun in [`SytSmallShapeCounts`](SytSmallShapeCounts.lean) (which pinned `[2,1] →
c = 1`). Now that the hook-length / enumeration count
(`numSYTenum_eq_numStandardYoungTableaux`, all `n`, sorry-free) has landed, the
remaining three self-conjugate shapes are pinned by the **forward** route — no
explicit tableau construction:

* `#SYT(μ)` via the computable enumeration `numSYTenum` (`decide`) + the bridge to
  the structure count `numStandardYoungTableaux = Nat.card (StandardYoungTableau)`;
* `Fintype.card (StandardYoungTableau μ) = #SYT(μ)` (`Nat.card_eq_fintype_card`);
* `c_λ = |R_row| = #SYT(μ)/2` via `two_mul_card_rowClass_eq_card` (self-conjugacy).

| shape | `#SYT` | `c_λ = #SYT/2` |
|-------|--------|-----------------|
| `[3,1,1]`   | 6  | **3**  |
| `[3,2,1]`   | 16 | **8**  |
| `[4,1,1,1]` | 20 | **10** |

matching the manuscript's `[3,1,1] → 3`, `[3,2,1] → 8`, `[4,1,1,1] → 10`.

-- Ref: [sagan2001] The Symmetric Group, §3.10–3.11 (hook length formula)
-/

namespace QOU.BraidKnot.SytSmallShapeCountsLarger

open QOU.Mathlib QOU.Mathlib.SYTEnum YoungDiagram
open QOU.BraidKnot.SeminormalCharacterConnector

/-! ## `[3,1,1]` → `c_λ = 3` -/

/-- The self-conjugate shape `[3,1,1]` (`n = 5`). -/
def mu311 : YoungDiagram := YoungDiagram.ofRowLens [3, 1, 1] (by decide)

theorem mu311_transpose : mu311.transpose = mu311 := YoungDiagram.ext (by decide)

theorem card_ge_two_mu311 : 2 ≤ mu311.cells.card := by decide

/-- `#SYT([3,1,1]) = 6` — the computable enumeration bridged to the structure count. -/
theorem numSYT_mu311 : numStandardYoungTableaux mu311 = 6 := by
  have he : numSYTenum [3, 1, 1] = 6 := by decide
  have hb := numSYTenum_eq_numStandardYoungTableaux [3, 1, 1] (by decide)
  rw [he] at hb
  exact hb.symm

theorem card_SYT_mu311 : Fintype.card (StandardYoungTableau mu311) = 6 := by
  have h := numSYT_mu311
  unfold numStandardYoungTableaux at h
  rwa [Nat.card_eq_fintype_card] at h

/-- **`c_λ([3,1,1]) = 3`** — the σ₁ character coefficient `|R_row| = #SYT/2`. -/
theorem card_rowClass_mu311 : (rowClass mu311).card = 3 := by
  have hkey := two_mul_card_rowClass_eq_card mu311_transpose card_ge_two_mu311
  rw [card_SYT_mu311] at hkey
  omega

/-! ## `[3,2,1]` → `c_λ = 8` -/

/-- The self-conjugate staircase shape `[3,2,1]` (`n = 6`). -/
def mu321 : YoungDiagram := YoungDiagram.ofRowLens [3, 2, 1] (by decide)

theorem mu321_transpose : mu321.transpose = mu321 := YoungDiagram.ext (by decide)

theorem card_ge_two_mu321 : 2 ≤ mu321.cells.card := by decide

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
/-- `#SYT([3,2,1]) = 16`. -/
theorem numSYT_mu321 : numStandardYoungTableaux mu321 = 16 := by
  have he : numSYTenum [3, 2, 1] = 16 := by decide
  have hb := numSYTenum_eq_numStandardYoungTableaux [3, 2, 1] (by decide)
  rw [he] at hb
  exact hb.symm

theorem card_SYT_mu321 : Fintype.card (StandardYoungTableau mu321) = 16 := by
  have h := numSYT_mu321
  unfold numStandardYoungTableaux at h
  rwa [Nat.card_eq_fintype_card] at h

/-- **`c_λ([3,2,1]) = 8`** — the σ₁ character coefficient `|R_row| = #SYT/2`. -/
theorem card_rowClass_mu321 : (rowClass mu321).card = 8 := by
  have hkey := two_mul_card_rowClass_eq_card mu321_transpose card_ge_two_mu321
  rw [card_SYT_mu321] at hkey
  omega

/-! ## `[4,1,1,1]` → `c_λ = 10` -/

/-- The self-conjugate shape `[4,1,1,1]` (`n = 7`). -/
def mu4111 : YoungDiagram := YoungDiagram.ofRowLens [4, 1, 1, 1] (by decide)

theorem mu4111_transpose : mu4111.transpose = mu4111 := YoungDiagram.ext (by decide)

theorem card_ge_two_mu4111 : 2 ≤ mu4111.cells.card := by decide

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
/-- `#SYT([4,1,1,1]) = 20` — the `n = 7` enumeration (kernel `decide`, axiom-free). -/
theorem numSYT_mu4111 : numStandardYoungTableaux mu4111 = 20 := by
  have he : numSYTenum [4, 1, 1, 1] = 20 := by decide
  have hb := numSYTenum_eq_numStandardYoungTableaux [4, 1, 1, 1] (by decide)
  rw [he] at hb
  exact hb.symm

theorem card_SYT_mu4111 : Fintype.card (StandardYoungTableau mu4111) = 20 := by
  have h := numSYT_mu4111
  unfold numStandardYoungTableaux at h
  rwa [Nat.card_eq_fintype_card] at h

/-- **`c_λ([4,1,1,1]) = 10`** — the σ₁ character coefficient `|R_row| = #SYT/2`. -/
theorem card_rowClass_mu4111 : (rowClass mu4111).card = 10 := by
  have hkey := two_mul_card_rowClass_eq_card mu4111_transpose card_ge_two_mu4111
  rw [card_SYT_mu4111] at hkey
  omega

end QOU.BraidKnot.SytSmallShapeCountsLarger
