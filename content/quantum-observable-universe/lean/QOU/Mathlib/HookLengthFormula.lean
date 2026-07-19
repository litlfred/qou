import QOU.Mathlib.StandardYoungTableau
import QOU.Mathlib.SYTHookGNW
import QOU.Mathlib.ColLenRowLensBridge
import QOU.BraidKnot.SpechtClassification
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Nat.Factorial.Basic

/-!
# QOU.Mathlib.HookLengthFormula — arm / leg / hook lengths and the HLF target

Foundation for the **hook-length formula** (Frame–Robinson–Thrall 1954), the
Mathlib-gap infra that computes `#SYT(μ)` in closed form — the unlock for the
tabulated character coefficients `c_λ ∈ {1,3,8,10}` of `symbolic_character_table`
(bean `qou-tqab`; see `QOU.BraidKnot.SytSmallShapeCounts` for the hand-enumerated
`c_λ = 1` case that this generalises).

This file supplies the **definitional layer** — arm, leg, and hook lengths of a
cell, and the hook-length product over a diagram — plus the **geometric hook-length
formula itself, sorry-free**:

  `#SYT(μ) · ∏_{c ∈ μ} hook(c) = |μ|!`.

The proof does *not* re-derive the FRT/RSK bijection: the corpus already proves the
list-form HLF `QOU.Mathlib.SYTEnum.numSYTenum_mul_prodHooks` (via the GNW corner
recursion; axiom-clean). This file identifies the geometric cell-hook product with the
corpus list `prodHooks` (`hookLengthProduct_eq_prodHooks` — a pure-ℕ reindex of the cell
product by rows and columns, matching per-cell hooks via `hookLength_eq_of_mem` +
`ColLenRowLensBridge.colLen_rowLens`), wires through the count bridge
(`numSYTenum_eq_numStandardYoungTableaux`) and `SpechtClassification.card_eq_rowLens_sum`,
and thereby discharges the geometric HLF on the genuine `numStandardYoungTableaux` count.

## Main definitions

* `YoungDiagram.armLength` / `legLength` / `hookLength` — of a cell `(i,j)`.
* `YoungDiagram.hookLengthProduct` — `∏_{c ∈ μ} hook(c)`.

## Main statements

* `hookLength_pos`, `hookLengthProduct_pos` — positivity.
* `hookLength_eq_of_mem` — the closed `(rowLen−j)+(colLen−i)−1` form on cells.
* `hookLengthProduct_eq_prodHooks` — geometric cell product = corpus list `prodHooks`.
* `numStandardYoungTableaux_mul_hookLengthProduct` — **the geometric HLF, sorry-free**.

Reference: the Frame–Robinson–Thrall hook-length formula (1954); proved here via the
corpus GNW list-form HLF rather than re-deriving the bijection.
-/

open scoped BigOperators

namespace YoungDiagram

variable (μ : YoungDiagram)

/-- **Arm length** of cell `(i, j)`: the number of cells strictly to its right in
    row `i` (`rowLen i − j − 1`). -/
def armLength (i j : ℕ) : ℕ := μ.rowLen i - j - 1

/-- **Leg length** of cell `(i, j)`: the number of cells strictly below it in
    column `j` (`colLen j − i − 1`). -/
def legLength (i j : ℕ) : ℕ := μ.colLen j - i - 1

/-- **Hook length** of cell `(i, j)`: arm + leg + 1 (the cell, its arm, and its leg). -/
def hookLength (i j : ℕ) : ℕ := μ.armLength i j + μ.legLength i j + 1

/-- Hook lengths are always positive (the `+ 1` counts the cell itself). -/
theorem hookLength_pos (i j : ℕ) : 0 < μ.hookLength i j := Nat.succ_pos _

/-- On a **cell** `(i, j) ∈ μ`, the hook length is the closed form
    `(rowLen i − j) + (colLen j − i) − 1`. On a cell `j < rowLen i` and
    `i < colLen j`, so arm `= rowLen i − j − 1` and leg `= colLen j − i − 1`
    are the honest right/below counts. -/
theorem hookLength_eq_of_mem {i j : ℕ} (h : (i, j) ∈ μ) :
    μ.hookLength i j = (μ.rowLen i - j) + (μ.colLen j - i) - 1 := by
  have hj : j < μ.rowLen i := mem_iff_lt_rowLen.mp h
  have hi : i < μ.colLen j := mem_iff_lt_colLen.mp h
  simp only [hookLength, armLength, legLength]
  omega

/-- **The hook-length product** `∏_{c ∈ μ} hook(c)` — the denominator of the HLF. -/
def hookLengthProduct : ℕ := ∏ c ∈ μ.cells, μ.hookLength c.1 c.2

/-- The hook-length product is positive (a product of positive hook lengths). -/
theorem hookLengthProduct_pos : 0 < μ.hookLengthProduct := by
  rw [hookLengthProduct]
  exact Finset.prod_induction _ (0 < ·) (fun _ _ ha hb => Nat.mul_pos ha hb)
    Nat.zero_lt_one (fun c _ => μ.hookLength_pos c.1 c.2)

end YoungDiagram

namespace QOU.Mathlib

open YoungDiagram

/-- `List.prod` of a mapped range = `Finset.prod` over `Finset.range`. -/
private theorem list_prod_map_range (n : ℕ) (f : ℕ → ℕ) :
    ((List.range n).map f).prod = ∏ i ∈ Finset.range n, f i := by
  induction n with
  | zero => simp
  | succ k ih =>
      rw [List.range_succ, List.map_append, List.prod_append, ih, Finset.prod_range_succ]
      simp

/-- Cells partition into rows `{0, …, colLen 0 − 1}`. -/
private theorem cells_biUnion' (μ : YoungDiagram) :
    μ.cells = (Finset.range (μ.colLen 0)).biUnion μ.row := by
  ext ⟨i, j⟩
  simp only [mem_cells, Finset.mem_biUnion, Finset.mem_range, mem_row_iff]
  constructor
  · intro hij
    exact ⟨i, lt_of_lt_of_le (mem_iff_lt_colLen.mp hij)
      (μ.colLen_anti 0 j (Nat.zero_le j)), hij, rfl⟩
  · rintro ⟨i', _, hij, rfl⟩; exact hij

private theorem rows_disjoint (μ : YoungDiagram) (n : ℕ) :
    (↑(Finset.range n) : Set ℕ).PairwiseDisjoint μ.row := by
  intro i _ i' _ hne
  rw [Function.onFun, Finset.disjoint_left]
  rintro ⟨a, b⟩ hc hc'
  rw [mem_row_iff] at hc hc'
  exact hne (hc.2.symm.trans hc'.2)

/-- Product over a row = product over its column range. -/
private theorem row_prod (μ : YoungDiagram) (f : ℕ × ℕ → ℕ) (i : ℕ) :
    ∏ c ∈ μ.row i, f c = ∏ j ∈ Finset.range (μ.rowLen i), f (i, j) := by
  rw [show μ.row i = (Finset.range (μ.rowLen i)).image (fun j => (i, j)) from ?_,
    Finset.prod_image (fun a _ b _ h => by simpa using h)]
  ext ⟨a, b⟩
  simp only [mem_row_iff, Finset.mem_image, Finset.mem_range]
  constructor
  · rintro ⟨hab, rfl⟩; exact ⟨b, mem_iff_lt_rowLen.mp hab, rfl⟩
  · rintro ⟨j, hj, heq⟩
    obtain ⟨rfl, rfl⟩ := Prod.ext_iff.mp heq
    exact ⟨mem_iff_lt_rowLen.mpr hj, rfl⟩

/-- **The geometric↔list hook bridge** `∏_{c∈μ} hook(c) = prodHooks (rowLens μ)` (sorry-free).
    Reindexes the cell product by rows (`cells_biUnion'`) and columns (`row_prod`), converts the
    corpus list `prodHooks` product to a `Finset` product (`list_prod_map_range`), and identifies
    the per-cell hook `(rowLen i − j) + (colLen j − i) − 1` (`hookLength_eq_of_mem` +
    `ColLenRowLensBridge.colLen_rowLens`) with the corpus list term. Together with the proved
    list-form HLF (`QOU.Mathlib.SYTEnum.numSYTenum_mul_prodHooks`) this fully discharges the
    geometric Frame–Robinson–Thrall HLF below. -/
theorem hookLengthProduct_eq_prodHooks (μ : YoungDiagram) :
    μ.hookLengthProduct = QOU.BraidKnot.IdentityI.prodHooks μ.rowLens := by
  rw [YoungDiagram.hookLengthProduct, cells_biUnion' μ,
    Finset.prod_biUnion (rows_disjoint μ (μ.colLen 0)),
    QOU.BraidKnot.IdentityI.prodHooks, list_prod_map_range, ← length_rowLens]
  refine Finset.prod_congr rfl (fun i hi => ?_)
  rw [Finset.mem_range, length_rowLens] at hi
  rw [row_prod]
  have hgetD : μ.rowLens.getD i 0 = μ.rowLen i := by
    rw [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem (by rw [length_rowLens]; exact hi),
      Option.getD_some, get_rowLens]
  rw [hgetD, list_prod_map_range]
  refine Finset.prod_congr rfl (fun j hj => ?_)
  rw [Finset.mem_range] at hj
  rw [YoungDiagram.hookLength_eq_of_mem μ (mem_iff_lt_rowLen.mpr hj), colLen_rowLens]

/-- **The hook-length formula (target)**: for every Young diagram `μ` with
    `n = |μ|` cells, the number of standard Young tableaux times the hook-length
    product equals `n!`:

      `#SYT(μ) · ∏_{c ∈ μ} hook(c) = n!`.

    Equivalently `#SYT(μ) = n! / ∏ hook(c)`. This is the closed form that pins the
    per-shape counts (e.g. the hook `(2,1)`: hooks `3·1·1 = 3`, so
    `#SYT = 3!/3 = 2`, matching `SytSmallShapeCounts.card_SYT_mu21`).

    Stated as the infra target; the proof (RSK, or the
    Frame–Robinson–Thrall / Novelli–Pak–Stoyanovskii probabilistic bijection) is
    the tracked next step — a Mathlib-upstream-scale contribution. -/
theorem numStandardYoungTableaux_mul_hookLengthProduct (μ : YoungDiagram) :
    numStandardYoungTableaux μ * μ.hookLengthProduct = (μ.cells.card).factorial := by
  have hl : (μ.rowLens).Sorted (· ≥ ·) := μ.rowLens_sorted
  have hpos : ∀ a ∈ μ.rowLens, 0 < a := μ.pos_of_mem_rowLens
  -- the count bridge: the genuine #SYT equals the brute-force list count of `μ`'s row lengths
  have hcount : numStandardYoungTableaux μ = SYTEnum.numSYTenum μ.rowLens := by
    rw [SYTEnum.numSYTenum_eq_numStandardYoungTableaux μ.rowLens hl,
      YoungDiagram.ofRowLens_to_rowLens_eq_self]
  -- the size bridge: `sz (rowLens μ) = |μ|`
  have hsz : QOU.BraidKnot.IdentityI.sz μ.rowLens = μ.cells.card :=
    (QOU.BraidKnot.SpechtClassification.card_eq_rowLens_sum μ).symm
  -- the proven Frame–Robinson–Thrall HLF in list form: `#SYT · ∏hooks = n!`
  have hkey := SYTEnum.numSYTenum_mul_prodHooks μ.rowLens hl hpos
  rw [hcount, hookLengthProduct_eq_prodHooks μ, ← hsz]
  exact hkey

end QOU.Mathlib
