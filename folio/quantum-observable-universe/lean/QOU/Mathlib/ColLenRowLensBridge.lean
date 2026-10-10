import QOU.BraidKnot.IdentityIContentDecomposition
import Mathlib.Combinatorics.Young.YoungDiagram

/-!
# QOU.Mathlib.ColLenRowLensBridge — the list↔diagram column-length bridge

The corpus carries two column-length notions that the geometric hook-length formula must identify:

* the **diagram** `YoungDiagram.colLen μ j` (Mathlib) — the length of column `j` of `μ`;
* the **list** `QOU.BraidKnot.IdentityI.colLen l j := (l.filter (j < ·)).length` — used by the corpus
  `prodHooks`.

This file proves they agree on `l = μ.rowLens`:

    IdentityI.colLen μ.rowLens j = μ.colLen j.

This is the missing bridge for identifying the geometric cell-hook product
`∏_{c∈μ} h(c)` (`QOU.Mathlib.HookLengthFormula.hookLengthProduct`) with the corpus list product
`prodHooks μ.rowLens`, and hence for discharging the geometric Frame–Robinson–Thrall HLF against the
already-proved list-form HLF (`QOU.Mathlib.SYTEnum.numSYTenum_mul_prodHooks`).

Proof: `μ.rowLens = (range (colLen 0)).map μ.rowLen` (Mathlib `rowLens`), so the filtered length counts
`{i < colLen 0 : j < rowLen i}`; `j < rowLen i ↔ (i,j) ∈ μ ↔ i < colLen j` (Mathlib
`mem_iff_lt_rowLen` / `mem_iff_lt_colLen`), and `colLen j ≤ colLen 0` (`colLen_anti`) collapses the
count to `colLen j`.

Pure combinatorics on `ℕ`; nothing archimedean; no fit.
-/

namespace QOU.Mathlib

open YoungDiagram

/-- **The list↔diagram column-length bridge**: the corpus list `colLen (rowLens μ) j` equals the
    diagram `μ.colLen j`. -/
theorem colLen_rowLens (μ : YoungDiagram) (j : ℕ) :
    QOU.BraidKnot.IdentityI.colLen μ.rowLens j = μ.colLen j := by
  unfold QOU.BraidKnot.IdentityI.colLen
  rw [← List.countP_eq_length_filter, YoungDiagram.rowLens, List.countP_map]
  -- (range (colLen 0)).countP ((j < ·) ∘ rowLen) : rewrite the predicate to `· < colLen j`
  have hcongr : ∀ i ∈ List.range (μ.colLen 0),
      (((fun p => decide (j < p)) ∘ μ.rowLen) i = true) ↔ (decide (i < μ.colLen j) = true) := by
    intro i _
    simp only [Function.comp_apply, decide_eq_true_eq]
    exact mem_iff_lt_rowLen.symm.trans mem_iff_lt_colLen
  rw [List.countP_congr hcongr, List.countP_eq_length_filter]
  -- the prefix `[0, colLen j)` of `range (colLen 0)` — the rest exceeds `colLen j`
  have hsplit : (List.range (μ.colLen 0)).filter (fun i => decide (i < μ.colLen j))
      = List.range (μ.colLen j) := by
    have hsub : μ.colLen j ≤ μ.colLen 0 := μ.colLen_anti 0 j (Nat.zero_le j)
    conv_lhs => rw [show μ.colLen 0 = μ.colLen j + (μ.colLen 0 - μ.colLen j) by omega,
      List.range_add, List.filter_append]
    rw [List.filter_eq_self.mpr (fun a ha => by rw [List.mem_range] at ha; simp; omega),
      List.filter_eq_nil_iff.mpr (fun a ha => by
        rw [List.mem_map] at ha; obtain ⟨b, _, rfl⟩ := ha; simp), List.append_nil]
  rw [hsplit, List.length_range]

end QOU.Mathlib
