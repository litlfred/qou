import Mathlib.Combinatorics.Young.YoungDiagram
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Ring

/-!
# Cell statistics of a Young diagram — one definition each

`content`, `arm`, `leg`, `hook` over `ℤ`, with the basic lemmas.

## Why this module exists

Each of these was defined independently in several places (bean `qou-cdup`).
The one-liner `(c.2 : ℤ) - (c.1 : ℤ)` — and its curried twin `(j : ℤ) - (i : ℤ)`
— appear **nine** times under four spellings, across two argument conventions:

| tuple `(c : ℕ × ℕ)` | curried `(i j : _)` |
|---|---|
| `QOU.BraidKnot.IdentityAArmLeg.content` | `QOU.MathlibExt.QPartitionCombinatorics.cellContent` |
| `QOU.BraidKnot.TableauContent.content` | `QOU.MathlibExt.WenzlSchurElement.cellContent` |
| `QOU.BraidKnot.JucysMurphy.cellContent` | `QOU.BraidsAndKnots.cellContent` (`y-lambda-recipe-from-partition`) |
| `QOU.BraidKnot.PieceA.contentZ` | `QOU.BraidKnot.cellContent` (`jucys-murphy-central-elements-qou`) |
| `QOU.BraidKnot.cellContent` (`TwoFiltrationBridge`) | |

Arm/leg/hook are defined twice over `ℤ` (`IdentityAArmLeg`, `PieceAGeneral`)
and once more over `ℕ` (`TwoFiltrationBridge.hookLength`).

**One of those pairs is a genuine clash, not merely a duplicate.** The last row
of each column is the *same fully-qualified name* — `QOU.BraidKnot.cellContent`
— declared twice, once in the library file `BraidKnot/TwoFiltrationBridge.lean`
and once in the standalone content-block sibling
`mass-theory/jucys-murphy-central-elements-qou.lean`, with incompatible
signatures (`ℕ × ℕ → ℤ` vs `ℤ → ℤ → ℤ`). They compile today only because the
sibling is standalone and is never imported alongside the library module; the
moment anything imports both, it is a hard duplicate-declaration error. Removing
the library-side copy in favour of this module is what clears it.

The rest cost no errors — each sits in its own namespace — but the copies
**cannot share lemmas**: `PieceAGeneral` proves `hookZ_eq` / `armZ_nonneg` /
`legZ_nonneg` against its copy, `HoefsmitRep` builds `axialDistance` on another,
`TwoFiltrationBridge` proves the content-spread results on a third, and none of
those is reachable from the others without a `rfl` bridge nobody wrote.

This module is the single home. `TwoFiltrationBridge` is migrated onto it;
the remaining eight are the drain half of `qou-cdup`. Each is definitionally
equal to the corresponding declaration here, so every bridge is `rfl`.

**Namespace note.** This lives under `QOU.MathlibExt` — the corpus's established
home for Mathlib extensions — rather than the more obvious `QOU.YoungDiagram`.
The obvious name is a trap: a `QOU.YoungDiagram` namespace captures `open
YoungDiagram` inside any `QOU.*` namespace, silently redirecting it away from
Mathlib's `YoungDiagram` and breaking `rowLen_anti`, `mem_iff_lt_rowLen` and the
rest at every existing call site.
-/

namespace QOU.MathlibExt.YoungDiagramCells

open Finset

variable (μ : YoungDiagram)

/-- **Content** (diagonal index) of a cell: `j - i`.

Contents are what the Jucys–Murphy elements measure — `L_k` acts on the
seminormal basis by a function of the content of the cell added at step `k` — so
this is the coordinate in which diagram statistics become algebra statements. -/
def content (c : ℕ × ℕ) : ℤ := (c.2 : ℤ) - (c.1 : ℤ)

/-- **Arm** of a cell: the cells strictly to its right in its row. -/
def arm (c : ℕ × ℕ) : ℤ := (μ.rowLen c.1 : ℤ) - (c.2 : ℤ) - 1

/-- **Leg** of a cell: the cells strictly below it in its column. -/
def leg (c : ℕ × ℕ) : ℤ := (μ.colLen c.2 : ℤ) - (c.1 : ℤ) - 1

/-- **Hook** of a cell: `arm + leg + 1`. -/
def hook (c : ℕ × ℕ) : ℤ := arm μ c + leg μ c + 1

variable {μ}

theorem hook_eq (c : ℕ × ℕ) :
    hook μ c = (μ.rowLen c.1 : ℤ) + (μ.colLen c.2 : ℤ) - (c.1 : ℤ) - (c.2 : ℤ) - 1 := by
  simp only [hook, arm, leg]; ring

theorem arm_nonneg {c : ℕ × ℕ} (hc : c ∈ μ) : 0 ≤ arm μ c := by
  have h : c.2 < μ.rowLen c.1 := by
    have := μ.mem_iff_lt_rowLen (i := c.1) (j := c.2); simpa using this.mp (by simpa using hc)
  have : (c.2 : ℤ) + 1 ≤ (μ.rowLen c.1 : ℤ) := by exact_mod_cast h
  simp only [arm]; omega

theorem leg_nonneg {c : ℕ × ℕ} (hc : c ∈ μ) : 0 ≤ leg μ c := by
  have h : c.1 < μ.colLen c.2 := by
    have := μ.mem_iff_lt_colLen (i := c.1) (j := c.2); simpa using this.mp (by simpa using hc)
  have : (c.1 : ℤ) + 1 ≤ (μ.colLen c.2 : ℤ) := by exact_mod_cast h
  simp only [leg]; omega

theorem one_le_hook {c : ℕ × ℕ} (hc : c ∈ μ) : 1 ≤ hook μ c := by
  have := arm_nonneg hc
  have := leg_nonneg hc
  simp only [hook]; omega

/-! ### The corner, and the content range -/

theorem rowLen0_pos (h : μ.cells.Nonempty) : 0 < μ.rowLen 0 := by
  obtain ⟨c, hc⟩ := h
  exact (YoungDiagram.mem_iff_lt_rowLen).mp
    (μ.up_left_mem (Nat.zero_le _) (Nat.zero_le _) hc)

theorem colLen0_pos (h : μ.cells.Nonempty) : 0 < μ.colLen 0 := by
  obtain ⟨c, hc⟩ := h
  exact (YoungDiagram.mem_iff_lt_colLen).mp
    (μ.up_left_mem (Nat.zero_le _) (Nat.zero_le _) hc)

/-- The largest content is the corner's arm, attained on the first row. -/
theorem sup_content (h : μ.cells.Nonempty) :
    μ.cells.sup' h content = (μ.rowLen 0 : ℤ) - 1 := by
  apply le_antisymm
  · refine Finset.sup'_le h _ fun c hc => ?_
    have hj : c.2 < μ.rowLen c.1 := (YoungDiagram.mem_iff_lt_rowLen).mp hc
    have hj0 : μ.rowLen c.1 ≤ μ.rowLen 0 :=
      YoungDiagram.rowLen_anti μ 0 c.1 (Nat.zero_le _)
    unfold content; omega
  · have hr := rowLen0_pos h
    have hmem : ((0 : ℕ), μ.rowLen 0 - 1) ∈ μ.cells :=
      (YoungDiagram.mem_iff_lt_rowLen).mpr (by omega)
    have hle := Finset.le_sup' (f := content) hmem
    have hcast : content ((0 : ℕ), μ.rowLen 0 - 1) = (μ.rowLen 0 : ℤ) - 1 := by
      show ((μ.rowLen 0 - 1 : ℕ) : ℤ) - ((0 : ℕ) : ℤ) = (μ.rowLen 0 : ℤ) - 1
      omega
    rw [hcast] at hle; exact hle

/-- The smallest content is minus the corner's leg, attained on the first column. -/
theorem inf_content (h : μ.cells.Nonempty) :
    μ.cells.inf' h content = -((μ.colLen 0 : ℤ) - 1) := by
  apply le_antisymm
  · have hc0 := colLen0_pos h
    have hmem : (μ.colLen 0 - 1, (0 : ℕ)) ∈ μ.cells :=
      (YoungDiagram.mem_iff_lt_colLen).mpr (by omega)
    have hle := Finset.inf'_le (f := content) hmem
    have hcast : content (μ.colLen 0 - 1, (0 : ℕ)) = -((μ.colLen 0 : ℤ) - 1) := by
      show ((0 : ℕ) : ℤ) - ((μ.colLen 0 - 1 : ℕ) : ℤ) = -((μ.colLen 0 : ℤ) - 1)
      omega
    rw [hcast] at hle; exact hle
  · refine Finset.le_inf' h _ fun c hc => ?_
    have hi : c.1 < μ.colLen c.2 := (YoungDiagram.mem_iff_lt_colLen).mp hc
    have hi0 : μ.colLen c.2 ≤ μ.colLen 0 :=
      YoungDiagram.colLen_anti μ 0 c.2 (Nat.zero_le _)
    unfold content; omega

/-- **The content spread is the corner hook.** The number of diagonals the
diagram meets equals `λ₁ + λ'₁ - 1`. -/
theorem content_spread_eq_corner (h : μ.cells.Nonempty) :
    μ.cells.sup' h content - μ.cells.inf' h content + 1
      = (μ.rowLen 0 : ℤ) + (μ.colLen 0 : ℤ) - 1 := by
  rw [sup_content h, inf_content h]; ring

end QOU.MathlibExt.YoungDiagramCells
