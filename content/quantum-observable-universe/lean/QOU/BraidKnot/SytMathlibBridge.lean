import QOU.BraidKnot.SytRowSuperstandard
import QOU.BraidKnot.StandardYoungTableau

/-!
# Bridge `QOU.Mathlib.StandardYoungTableau μ → QOU.BraidKnot.StandardYoungTableau μ`

Two standard-Young-tableau types live in this development:

* `QOU.Mathlib.StandardYoungTableau μ` — a refinement of Mathlib's
  `SemistandardYoungTableau`, whose entry map is a `Set.BijOn` onto `{1, …, |μ|}`
  (entries `1..|μ|`).  The row-superstandard witness `rowSuperstandardStd` and the
  `Nonempty` instance built in `SytRowSuperstandard.lean` are of this type.
* `QOU.BraidKnot.StandardYoungTableau μ` — the bespoke entry-based structure
  (`entry`, `lt_card`, `zero_off`, `inj_on`, `row_strict`, `col_strict`) with
  entries `0..|μ|-1`, used by the Jucys–Murphy / Okounkov–Vershik seminormal
  machinery (`JucysMurphy.lean`: `tableauCellEquiv`, `AdjacentSwapStep`,
  `syt_all_connect_to_some`).

This file is the **one-line-down conversion** `toBraidKnot` between them: shift
every entry down by one (`entry i j - 1`).  Off the diagram Mathlib's SSYT is
pinned to `0` (`zeros'`), and `0 - 1 = 0` in `ℕ`, so `zero_off` holds for free;
on the diagram the `Set.BijOn` bound `1 ≤ entry ≤ |μ|` makes the truncated
subtraction faithful (`omega`).  Consequently the JM/OV code has a concrete
`Nonempty (QOU.BraidKnot.StandardYoungTableau μ)` (`rowSuperstandardBraidKnot`),
supplying the base tableau `T₀` its exchange argument needs.

Scope: pure combinatorics on `ℕ`; §7c-clean (no `ℝ`, no ordering on `q`); no fit.
-/

namespace QOU.BraidKnot

open YoungDiagram

variable {μ : YoungDiagram}

/-- **The one-down conversion** `QOU.Mathlib.StandardYoungTableau μ →
`QOU.BraidKnot.StandardYoungTableau μ`: shift each entry down by one so the range
becomes `0..|μ|-1`.  Off-diagram entries (`= 0` by `zeros'`) stay `0`. -/
noncomputable def _root_.QOU.Mathlib.StandardYoungTableau.toBraidKnot
    (T : QOU.Mathlib.StandardYoungTableau μ) : QOU.BraidKnot.StandardYoungTableau μ where
  entry i j := T.entry i j - 1
  lt_card i j hij := by
    have hmap : T.entry i j ∈ Set.Icc 1 μ.cells.card :=
      T.mapsTo_cells (QOU.Mathlib.StandardYoungTableau.mem_coe_cells hij)
    rw [Set.mem_Icc] at hmap
    show T.entry i j - 1 < μ.cells.card
    omega
  zero_off i j hij := by
    show T.entry i j - 1 = 0
    have h0 : T.entry i j = 0 := T.toSsyt.zeros hij
    rw [h0]
  inj_on i j i' j' hij hij' heq := by
    have h1 : T.entry i j ∈ Set.Icc 1 μ.cells.card :=
      T.mapsTo_cells (QOU.Mathlib.StandardYoungTableau.mem_coe_cells hij)
    have h2 : T.entry i' j' ∈ Set.Icc 1 μ.cells.card :=
      T.mapsTo_cells (QOU.Mathlib.StandardYoungTableau.mem_coe_cells hij')
    rw [Set.mem_Icc] at h1 h2
    have heq' : T.entry i j = T.entry i' j' := by
      show T.entry i j = T.entry i' j'
      omega
    have hcell := T.injOn_cells (QOU.Mathlib.StandardYoungTableau.mem_coe_cells hij)
      (QOU.Mathlib.StandardYoungTableau.mem_coe_cells hij') heq'
    exact ⟨congrArg Prod.fst hcell, congrArg Prod.snd hcell⟩
  row_strict i j hcell := by
    have hij : (i, j) ∈ μ := μ.up_left_mem (le_refl i) (Nat.le_succ j) hcell
    have hlt : T.entry i j < T.entry i (j + 1) := T.row_strict (Nat.lt_succ_self j) hcell
    have hmap : T.entry i j ∈ Set.Icc 1 μ.cells.card :=
      T.mapsTo_cells (QOU.Mathlib.StandardYoungTableau.mem_coe_cells hij)
    rw [Set.mem_Icc] at hmap
    show T.entry i j - 1 < T.entry i (j + 1) - 1
    omega
  col_strict i j hcell := by
    have hij : (i, j) ∈ μ := μ.up_left_mem (Nat.le_succ i) (le_refl j) hcell
    have hlt : T.entry i j < T.entry (i + 1) j := T.toSsyt.col_strict (Nat.lt_succ_self i) hcell
    have hmap : T.entry i j ∈ Set.Icc 1 μ.cells.card :=
      T.mapsTo_cells (QOU.Mathlib.StandardYoungTableau.mem_coe_cells hij)
    rw [Set.mem_Icc] at hmap
    show T.entry i j - 1 < T.entry (i + 1) j - 1
    omega

/-- **The row-superstandard tableau as a `QOU.BraidKnot.StandardYoungTableau`** —
the base tableau `T₀` the Okounkov–Vershik exchange argument
(`syt_all_connect_to_some`) walks every SYT toward, in the exact type that
argument consumes. -/
noncomputable def rowSuperstandardBraidKnot (μ : YoungDiagram) :
    QOU.BraidKnot.StandardYoungTableau μ :=
  (rowSuperstandardStd μ).toBraidKnot

/-- **`QOU.BraidKnot.StandardYoungTableau μ` is nonempty (sorry-free).** Via the
bridge from the row-superstandard Mathlib SYT. -/
instance instNonemptyBraidKnotStandardYoungTableau :
    Nonempty (QOU.BraidKnot.StandardYoungTableau μ) :=
  ⟨rowSuperstandardBraidKnot μ⟩

end QOU.BraidKnot
