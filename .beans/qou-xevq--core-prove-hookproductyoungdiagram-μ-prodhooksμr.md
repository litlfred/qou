---
# qou-xevq
title: 'CORE: prove hookProduct(YoungDiagram μ) = prodHooks(μ.rowLens) — reconcile ∏_{c∈cells} hookLength (Finset) with the nested-list prodHooks; the one genuine formalization brick, no existing lemma'
status: in-progress
type: task
priority: normal
created_at: 2026-08-01T23:34:16Z
updated_at: 2026-08-08T07:06:22Z
---


## Progress 2026-08-08 — arm/leg/hook closed forms proved

Three lemmas added to `QOU/BraidKnot/StandardYoungTableau.lean`, all
**axiom-clean** (`#print axioms` shows only propext / Classical.choice /
Quot.sound — no `sorryAx`):

- `armCard_eq` — the cells strictly right of `(i,j)` in row `i` are
  exactly `{i} ×ˢ Ioo j (μ.rowLen i)`, so the arm is `μ.rowLen i - j - 1`.
- `legCard_eq` — dual, via `colLen`: the leg is `μ.colLen j - i - 1`.
- `hookLength_eq_rowLen_add_colLen` — for a genuine cell `(i,j) ∈ μ`,
  `hookLength μ i j = (μ.rowLen i - j) + (μ.colLen j - i) - 1`.

That third one **is the bridge this bean is about**: it converts the
`Finset`-of-cells hook used by `StandardYoungTableau.hookProduct` into the
`(λ_i − j) + (colLen j − i) − 1` form that the list-based `prodHooks`
uses. Both ℕ-subtractions are exact on genuine cells, which is why the
hypothesis `(i,j) ∈ μ` is needed and why `omega` closes it.

Needed `import Mathlib.Order.Interval.Finset.Nat` for `Nat.card_Ioo`.

### Remaining for this bean

The pointwise identity is done; what is left is the *indexing* half —
`hookProduct μ = prodHooks μ.rowLens`, i.e. matching a `Finset.prod` over
`μ.cells` with the nested `List.prod` over rows. Needs:

- `μ.cells` decomposed as a union/sigma over rows (Mathlib has
  `row_eq_prod : μ.row i = {i} ×ˢ Finset.range (μ.rowLen i)`);
- `colLen μ.rowLens j = μ.colLen j`, bridging the list-side
  `colLen l j = (l.filter (j < ·)).length` to the diagram's `colLen`;
- `μ.rowLens.getD i 0 = μ.rowLen i`.

None of these needs FRT itself — this bean stays strictly below the
hook-length theorem.
