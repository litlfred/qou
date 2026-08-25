import QOU.BraidKnot.StandardYoungTableau
import QOU.Mathlib.StandardYoungTableau

/-!
# Bridging the two standard-Young-tableau encodings

The corpus carries **two** `StandardYoungTableau` structures, and the RSK sum-of-squares result is
stated in one while the hook-length chain lands in the other:

| structure | entries | packaging | counted by | carries |
|---|---|---|---|---|
| `QOU.BraidKnot.StandardYoungTableau μ` | `< μ.card` (0-indexed) | raw `entry` + `inj_on` / `row_strict` / `col_strict` / `zero_off` | `numSYT` | `OVTopAssembly.sum_numSYT_sq_eq_factorial` (RSK) |
| `QOU.Mathlib.StandardYoungTableau μ` | `Set.Icc 1 μ.cells.card` (1-indexed) | `SemistandardYoungTableau` + `Set.BijOn` | `numStandardYoungTableaux` | `numSYTenum_eq_numStandardYoungTableaux` (hook-length / `sytDim`) |

Because the two are distinct types, neither result transfers to the other. This file builds the
bridge, whose payoff is twofold:

* `RSKBurnsideTarget.RSKBurnsideHolds` — `∑_{p ⊢ n} dimSYT p ² = n!`, which the corpus records as
  *"not yet a theorem … the multi-session next step"*, becomes a reindexing of the (already proved)
  `OVTopAssembly.sum_numSYT_sq_eq_factorial`;
* the Plancherel normalisation `Σ_λ (f^λ)² = k!` in the `sytDim`/`partsOf` encoding, which is the
  single open premise of `YoungDiagramTailFirstInstance.nuV_top_closed_form`.

This is **not** the `burnside` roadmap's bridge (1) (`numSYT_mul_hookProduct`, the hook-length
formula inside the custom-`Partition` encoding) — that gap is orthogonal and stays open.

## This file

The `≤` direction: the 1-indexed encoding embeds into the 0-indexed one by `entry ↦ entry − 1`, so
`numStandardYoungTableaux μ ≤ numSYT μ`. The reverse inequality needs the pigeonhole
(`inj_on` + `lt_card` on an `n`-element cell set forces surjectivity onto `{1,…,n}`) together with
weak-row monotonicity from adjacent strictness; it is the remaining half of the bridge.

## Corrections (2026-08-23)

Three statements above describe the state of the corpus when this file was written and no longer
hold.  The text is left in place; each is superseded as follows.

* *"which the corpus records as 'not yet a theorem … the multi-session next step'"* —
  `RSKBurnsideTarget` no longer records that (it was corrected the same day), and
  `RSKBurnsideHolds` is a theorem for **every** `n`: `QOU.Mathlib.rskBurnsideHolds`, from the
  Robinson–Schensted correspondence.
* *"the single open premise of `YoungDiagramTailFirstInstance.nuV_top_closed_form`"* — discharged
  by `PlancherelNormalisation.nuV_top_closed_form_unconditional`.
* *"that gap is orthogonal and stays open"* — the orthogonality stands; the gap does not.
  `QOU.BraidKnot.numSYT_mul_hookProduct_partition` proves exactly the named bridge (1)
  (`numSYT (toYoungDiagram Λ) * Λ.hookProduct = n!`) and is axiom-clean, as is its payoff
  `dimIrrep_eq_numSYT`.

And in **This file** below, *"it is the remaining half of the bridge"*: the reverse inequality is
proved, as the equality `QOU.BraidKnot.numSYT_eq_numStandardYoungTableaux` in `NumSYTBridge`.  This
file still carries only the `≤` direction, which is what makes the sentence easy to miss.

-- Ref: [sagan2001] Sagan, The Symmetric Group §3 (standard tableaux; both entry conventions)
-/

namespace QOU.BraidKnot.SYTEncodingBridge

open QOU.BraidKnot

variable {μ : YoungDiagram}

/-- On a cell, a 1-indexed entry is positive. -/
theorem one_le_entry (T : QOU.Mathlib.StandardYoungTableau μ) {i j : ℕ} (h : (i, j) ∈ μ) :
    1 ≤ T.entry i j :=
  (Set.mem_Icc.mp (T.mapsTo_cells (QOU.Mathlib.StandardYoungTableau.mem_coe_cells h))).1

/-- On a cell, a 1-indexed entry is at most the cell count. -/
theorem entry_le_card (T : QOU.Mathlib.StandardYoungTableau μ) {i j : ℕ} (h : (i, j) ∈ μ) :
    T.entry i j ≤ μ.cells.card :=
  (Set.mem_Icc.mp (T.mapsTo_cells (QOU.Mathlib.StandardYoungTableau.mem_coe_cells h))).2

/-- Off the diagram a 1-indexed entry vanishes (the underlying semistandard tableau's `zeros`,
in `.entry` form). -/
theorem entry_zero_off (T : QOU.Mathlib.StandardYoungTableau μ) {i j : ℕ} (h : (i, j) ∉ μ) :
    T.entry i j = 0 :=
  T.toSsyt.zeros h

/-- **The 1-indexed encoding embeds into the 0-indexed one**: subtract one from every entry. All
six `QOU.BraidKnot` fields follow from the `Set.BijOn` packaging (`mapsTo_cells` for the bound,
`injOn_cells` for injectivity) plus the generalized `row_strict` and the underlying
semistandard tableau's `col_strict` / `zeros`. -/
noncomputable def toBraidKnot (T : QOU.Mathlib.StandardYoungTableau μ) :
    QOU.BraidKnot.StandardYoungTableau μ where
  entry i j := T.entry i j - 1
  lt_card i j h := by
    have h1 := one_le_entry T h
    have h2 := entry_le_card T h
    have hcard : 0 < μ.card := by
      have : (i, j) ∈ μ.cells := by rwa [YoungDiagram.mem_cells]
      exact Finset.card_pos.mpr ⟨(i, j), this⟩
    have hce : μ.card = μ.cells.card := rfl
    omega
  zero_off i j h := by
    rw [entry_zero_off T h]
  inj_on i j i' j' hc hc' heq := by
    have h1 := one_le_entry T hc
    have h2 := one_le_entry T hc'
    have hfull : T.entry i j = T.entry i' j' := by omega
    have := T.injOn_cells (QOU.Mathlib.StandardYoungTableau.mem_coe_cells hc)
      (QOU.Mathlib.StandardYoungTableau.mem_coe_cells hc') hfull
    exact ⟨congrArg Prod.fst this, congrArg Prod.snd this⟩
  row_strict i j h := by
    have hc : (i, j) ∈ μ := μ.up_left_mem (le_refl i) (Nat.le_succ j) h
    have hlt : T.entry i j < T.entry i (j + 1) := T.row_strict (Nat.lt_succ_self j) h
    have h1 := one_le_entry T hc
    have h2 := one_le_entry T h
    omega
  col_strict i j h := by
    have hc : (i, j) ∈ μ := μ.up_left_mem (Nat.le_succ i) (le_refl j) h
    have hlt : T.entry i j < T.entry (i + 1) j := T.toSsyt.col_strict (Nat.lt_succ_self i) h
    have h1 := one_le_entry T hc
    have h2 := one_le_entry T h
    omega

/-- The embedding is **injective**: entries agree on cells (both are `≥ 1`, so the `−1` is
invertible there) and vanish off cells, and a tableau is determined by its entries. -/
theorem toBraidKnot_injective :
    Function.Injective (toBraidKnot : QOU.Mathlib.StandardYoungTableau μ → _) := by
  intro T T' hTT'
  have hentry : ∀ i j, T.entry i j = T'.entry i j := by
    intro i j
    by_cases hc : (i, j) ∈ μ
    · have h1 := one_le_entry T hc
      have h2 := one_le_entry T' hc
      have hsub : T.entry i j - 1 = T'.entry i j - 1 := by
        have := congrArg (fun S : QOU.BraidKnot.StandardYoungTableau μ => S.entry i j) hTT'
        simpa [toBraidKnot] using this
      omega
    · rw [entry_zero_off T hc, entry_zero_off T' hc]
  have hssyt : T.toSsyt = T'.toSsyt := by
    ext i j
    exact hentry i j
  cases T with
  | mk ssyt bij =>
    cases T' with
    | mk ssyt' bij' =>
      simp only at hssyt
      subst hssyt
      rfl

/-- **One half of the bridge**: the 1-indexed count is at most the 0-indexed count. -/
theorem numStandardYoungTableaux_le_numSYT (μ : YoungDiagram) :
    QOU.Mathlib.numStandardYoungTableaux μ ≤ numSYT μ := by
  haveI : Finite (QOU.BraidKnot.StandardYoungTableau μ) :=
    Finite.of_injective _ QOU.BraidKnot.StandardYoungTableau.encode_injective
  unfold QOU.Mathlib.numStandardYoungTableaux numSYT
  exact Nat.card_le_card_of_injective _ toBraidKnot_injective

end QOU.BraidKnot.SYTEncodingBridge
