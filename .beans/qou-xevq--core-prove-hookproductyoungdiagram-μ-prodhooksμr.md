---
# qou-xevq
title: 'CORE: prove hookProduct(YoungDiagram μ) = prodHooks(μ.rowLens) — reconcile ∏_{c∈cells} hookLength (Finset) with the nested-list prodHooks; the one genuine formalization brick, no existing lemma'
status: completed
type: task
priority: normal
created_at: 2026-08-01T23:34:16Z
updated_at: 2026-08-08T07:23:31Z
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

## Progress 2026-08-08 (cont) — indexing half proved

Four more lemmas, all **axiom-clean** (`#print axioms` → propext /
Classical.choice / Quot.sound only, no `sorryAx`):

- `cells_eq_biUnion` — `μ.cells = ⋃_{i < μ.colLen 0} μ.row i`, with the
  rows pairwise disjoint. Mathlib has `row_eq_prod` but **no**
  cells-as-union-of-rows lemma, so this is new.
- `hookProduct_eq_nested` — **the indexing half of this bean**:
  `hookProduct μ = ∏_{i < colLen 0} ∏_{j < rowLen i} ((rowLen i − j) + (colLen j − i) − 1)`.
  The `Finset` product over cells is now a nested product with the hook
  already in `prodHooks` form.
- `rowLens_getD` — `μ.rowLens.getD i 0 = μ.rowLen i` for every `i`,
  including past the last row where both sides are 0.
- `length_filter_rowLens` — counting rows longer than `j` in `μ.rowLens`
  gives `μ.colLen j`. This is the list-side `colLen` of
  `IdentityIContentDecomposition` matching the diagram's.

Needed one small counting fact absent upstream, proved by induction:
`countP_range_lt : (List.range n).countP (· < m) = min m n`.

Imports added: `Mathlib.Order.Interval.Finset.Nat` (`Nat.card_Ioo`),
`Mathlib.Data.List.GetD` (`getD_eq_getElem` / `getD_eq_default`).

### What remains

Every mathematical ingredient this bean names is now proved. What is left
is mechanical: converting the nested **Finset** product of
`hookProduct_eq_nested` into the nested **List** product of `prodHooks`,
and choosing where that statement lives — `prodHooks` sits in
`IdentityIContentDecomposition`, so stating `hookProduct μ =
prodHooks μ.rowLens` needs either a new bridge module importing both or
moving `prodHooks`. That is a placement decision, not a proof gap.

The FRT `sorry` is untouched — this bean stays strictly below it.

## Summary of Changes — RESOLVED

`hookProduct_eq_prodHooks (μ : YoungDiagram) : hookProduct μ = prodHooks μ.rowLens`
is proved and **axiom-clean** (`#print axioms` → propext / Classical.choice /
Quot.sound; no `sorryAx`). New module
`QOU/BraidKnot/HookProductBridge.lean`, wired into `QOU/BraidKnot.lean`;
`lake build QOU.BraidKnot` green at 3404 jobs.

The bean called this "the one genuine formalization brick, no existing
lemma". It decomposed into eight pieces, all proved:

**In `StandardYoungTableau.lean`** (the hook itself)
- `armCard_eq`, `legCard_eq` — arm and leg as `{i} ×ˢ Ioo j (rowLen i)`
  and its dual, giving `rowLen i - j - 1` and `colLen j - i - 1`.
- `hookLength_eq_rowLen_add_colLen` — for a genuine cell,
  `hookLength μ i j = (rowLen i - j) + (colLen j - i) - 1`. The membership
  hypothesis is what makes both ℕ-subtractions exact.
- `cells_eq_biUnion` — `μ.cells` as the disjoint union of its rows.
  Mathlib has `row_eq_prod` but no such decomposition.
- `hookProduct_eq_nested` — the cell product as `∏_i ∏_{j < rowLen i}`.
- `rowLens_getD` — `μ.rowLens.getD i 0 = μ.rowLen i` for every `i`,
  including past the last row where both sides are 0.
- `length_filter_rowLens` — rows longer than `j` number `μ.colLen j`.
- `countP_range_lt` — `(List.range n).countP (· < m) = min m n`, proved by
  induction; no upstream equivalent.

**In `HookProductBridge.lean`** (the indexing conversion)
- `prod_range_eq_list_prod` — a `Finset.range` product is the `List.range`
  product, via `Finset.range_val`.
- `colLen_rowLens` — `IdentityI.colLen μ.rowLens j = μ.colLen j`.
- `hookProduct_eq_prodHooks` — the theorem.

Imports added: `Mathlib.Order.Interval.Finset.Nat` (`Nat.card_Ioo`),
`Mathlib.Data.List.GetD`.

### Scope note

This does NOT prove FRT. `numSYT_mul_hookProduct` keeps its `sorry` and
is unchanged. What this removes is the definitional friction underneath
it: downstream results that mix the two hook products no longer have to
assume they agree.
