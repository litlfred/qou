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

end QOU.MathlibExt.WenzlSchurElementBridge
