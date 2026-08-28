import QOU.MathlibExt.WenzlSchurElement
import QOU.QBeta.WenzlWeightVanishing

/-!
# Carrier bridge: List `schurElement` ↔ YoungDiagram `schurPrincipal`

The corpus carries **two** parallel Wenzl/Macdonald Schur-element developments on
different carriers:

* **List carrier** (`X` free) — `QOU.MathlibExt.WenzlSchurElement.schurElement Q X lam`
  on `Partition = List ℕ`, a nested fold over `(i, j)` with `j < lam[i]`. The
  Macdonald hook telescope is proved here only at `n ≤ 3`
  (`MacdonaldTelescope.telescope_one/two/three`), with a general **conditional**
  M1 (`jonesMarkov_normalisation_of_telescope`).
* **YoungDiagram carrier** (`X = Q^r`) — `QOU.QBeta.WenzlWeight.schurPrincipal r Q μ`
  on `YoungDiagram`, a `Finset.prod` over `μ.cells`. Here the **general** telescope
  is proved sorry-free (`QOU.SchurWeyl.sum_dim_wenzlWeight_eq_one`, general `n`,
  general level `r`).

The two `schurElement`/`schurPrincipal` objects are the *same* hook–content
formula `Q^{n(λ)} · ∏_x (1 − X·Q^{c(x)})/(1 − Q^{h(x)})`, but no Lean lemma
connects them. This file builds that bridge, so the List-carrier low-rank results
can be re-derived from — rather than duplicate — the already-proved general
YoungDiagram telescope.

## Correspondence (at `X = Q^r`, `μ = YoungDiagram.ofRowLens lam hl`)

| List side | YoungDiagram side | how they match |
|-----------|-------------------|----------------|
| `cellContent i j = j − i` | `content (i, j) = j − i` | definitional (this file, `content_eq_cellContent`) |
| `(lam[i]?).getD 0` | `(ofRowLens lam hl).rowLen i` | `rowLen_ofRowLens` |
| `Partition.hookLength lam i j` | `hook (ofRowLens lam hl) (i, j)` | arm `+1` / leg `+1`, needs `hl` sorted |
| `nLambda lam` | `nPart (ofRowLens lam hl)` | `∑ i · row-length i` |
| nested fold over `(i, j)` | `∏ x ∈ μ.cells` | `cells = ⋃ᵢ {i} ×ˢ range(rowLen i)` |

## Status

Scaffold + the content-carrier match (`content_eq_cellContent`). The remaining
bricks (hook-match, `nPart = nLambda`, product reindex, assembly) are the
substantial part and land incrementally; the final target is

`schurElement Q (Q^r) lam = schurPrincipal r Q (YoungDiagram.ofRowLens lam hl)`.

## References

- [wenzl1988] Wenzl, "Hecke algebras of type $A_n$ and subfactors," Invent. Math. 92.
- [macdonald1995] Macdonald, *Symmetric Functions and Hall Polynomials*, §I.3.
-/

namespace QOU.MathlibExt.WenzlSchurElementBridge

open QOU.MathlibExt.WenzlSchurElement
open QOU.MathlibExt.QPartitionCombinatorics

/-- **Content-carrier match.** The List-carrier cell content `cellContent i j =
j − i` and the YoungDiagram-carrier `content (i, j) = j − i` are the same
function of the cell coordinates — the first (and definitional) link between the
two developments. -/
theorem content_eq_cellContent (i j : ℕ) :
    QOU.QBeta.WenzlWeight.content (i, j)
      = QOU.MathlibExt.WenzlSchurElement.cellContent i j :=
  rfl

/-- **Row-length match.** The `i`-th row length of `ofRowLens lam hl` is the
`i`-th list entry (`0` past the end) — `(ofRowLens lam hl).rowLen i = (lam[i]?).getD 0`.
For `i` in range this is Mathlib's `rowLen_ofRowLens`; past the end both sides are
`0` (no cell `(i, 0)` exists, so the row length vanishes). -/
theorem rowLen_ofRowLens_getD (lam : List ℕ) (hl : lam.Sorted (· ≥ ·)) (i : ℕ) :
    (YoungDiagram.ofRowLens lam hl).rowLen i = (lam[i]?).getD 0 := by
  by_cases h : i < lam.length
  · have hr := YoungDiagram.rowLen_ofRowLens (w := lam) (hw := hl) ⟨i, h⟩
    rw [List.getElem?_eq_getElem h]
    simpa using hr
  · push_neg at h
    rw [List.getElem?_eq_none h, Option.getD_none]
    by_contra hne
    have hpos : 0 < (YoungDiagram.ofRowLens lam hl).rowLen i := Nat.pos_of_ne_zero hne
    have hmem : (i, 0) ∈ YoungDiagram.ofRowLens lam hl :=
      YoungDiagram.mem_iff_lt_rowLen.mpr hpos
    rw [YoungDiagram.mem_ofRowLens] at hmem
    obtain ⟨hlt, _⟩ := hmem
    omega

/-- A finite product of `List.map` over `List.range n` is the `Finset.range n`
product — the List↔Finset bridge used to move `schurElement`'s list folds onto
the Finset products `schurPrincipal` uses. -/
theorem list_range_map_prod {M : Type*} [CommMonoid M] (n : ℕ) (h : ℕ → M) :
    ((List.range n).map h).prod = ∏ j ∈ Finset.range n, h j := by
  induction n with
  | zero => simp
  | succ k ih =>
    rw [List.range_succ, List.map_append, List.prod_append, ih, Finset.prod_range_succ]
    simp

/-- **`schurElement` as a Finset double product.** Restates the List-fold
`schurElement` (via `schurElement_eq_prod`) as `Q^{n(λ)}` times a product over
rows `i ∈ range (length)` of a product over cells `j ∈ range (row length)` of
`cellFactor`. This is the shape that matches `schurPrincipal`'s `∏ x ∈ μ.cells`. -/
theorem schurElement_eq_finset_prod (Q X : ℝ) (lam : Partition) :
    schurElement Q X lam
      = Q ^ (nLambda lam)
          * ∏ i ∈ Finset.range lam.length,
              ∏ j ∈ Finset.range ((lam[i]?).getD 0), cellFactor Q X lam i j := by
  rw [schurElement_eq_prod, list_range_map_prod]
  have hrow : ∀ i ∈ Finset.range lam.length,
      rowFactor Q X lam i
        = ∏ j ∈ Finset.range ((lam[i]?).getD 0), cellFactor Q X lam i j := by
    intro i _
    simp only [rowFactor]
    exact list_range_map_prod _ _
  rw [Finset.prod_congr rfl hrow]

/-- **Cells of `ofRowLens` as a disjoint union of rows.** Each row `i < length`
contributes `{i} ×ˢ range(rowLenᵢ)`, and by `rowLen_ofRowLens_getD` the row
length is `(lam[i]?).getD 0`. -/
theorem cells_ofRowLens_eq_biUnion (lam : List ℕ) (hl : lam.Sorted (· ≥ ·)) :
    (YoungDiagram.ofRowLens lam hl).cells
      = (Finset.range lam.length).biUnion
          (fun i => {i} ×ˢ Finset.range ((lam[i]?).getD 0)) := by
  ext ⟨a, b⟩
  rw [YoungDiagram.mem_cells, YoungDiagram.mem_iff_lt_rowLen, rowLen_ofRowLens_getD]
  simp only [Finset.mem_biUnion, Finset.mem_range, Finset.mem_product,
    Finset.mem_singleton]
  constructor
  · intro hb
    refine ⟨a, ?_, rfl, hb⟩
    by_contra hge
    push_neg at hge
    rw [List.getElem?_eq_none hge, Option.getD_none] at hb
    omega
  · rintro ⟨i, _, rfl, hb⟩
    exact hb

/-- **Product reindex (B5).** A product over the cells of `ofRowLens lam hl`
equals the row-by-row double product over `range (length)` and
`range ((lam[i]?).getD 0)`. -/
theorem prod_cells_ofRowLens {M : Type*} [CommMonoid M]
    (lam : List ℕ) (hl : lam.Sorted (· ≥ ·)) (g : ℕ × ℕ → M) :
    ∏ x ∈ (YoungDiagram.ofRowLens lam hl).cells, g x
      = ∏ i ∈ Finset.range lam.length,
          ∏ j ∈ Finset.range ((lam[i]?).getD 0), g (i, j) := by
  rw [cells_ofRowLens_eq_biUnion]
  have hdisj : (↑(Finset.range lam.length) : Set ℕ).PairwiseDisjoint
      (fun i => ({i} ×ˢ Finset.range ((lam[i]?).getD 0)) : ℕ → Finset (ℕ × ℕ)) := by
    intro i _ i' _ hii
    simp only [Function.onFun, Finset.disjoint_left, Finset.mem_product,
      Finset.mem_singleton]
    rintro ⟨a, b⟩ ⟨rfl, -⟩ ⟨h2, -⟩
    exact absurd h2 hii
  rw [Finset.prod_biUnion hdisj]
  apply Finset.prod_congr rfl
  intro i _
  rw [Finset.prod_product, Finset.prod_singleton]

end QOU.MathlibExt.WenzlSchurElementBridge
