---
# qou-wf9n
title: 'RSK: prove skew_le_straight by the explicit skew-SYT into straight-SYT injection'
status: completed
type: task
created_at: 2026-08-08T17:40:00Z
updated_at: 2026-08-08T17:40:00Z
---

Branch: `claude/sorry-audit-joo5` (qou).
File: `content/quantum-observable-universe/lean/QOU/BraidKnot/YoungTableauStandard.lean`.

## Why it was closeable when its two siblings are not

`skew_le_straight` is an **inequality** between two counts, and an inequality
needs only an *injection*. `branching_two_one` and `sum_dimSYT_eq_involution` are
**equalities** and genuinely need the RSK bijection. The file's scope note had
lumped all three together as "discharged by the RSK correspondence", which
overstated the first one's difficulty — it needs no RSK at all.

## The injection

For `(2,1) ⊆ Y`, extend a skew SYT of shape `Y/(2,1)` to a straight SYT of `Y`:

* fill `(2,1)` with the fixed standard tableau `κ = 1, 2, 3`;
* shift every skew value into `{4, …, |Y|}` (`+4`, not `+3`: the target
  `QOU.Mathlib.StandardYoungTableau` is 1-indexed via `Set.BijOn … (Icc 1 |Y|)`,
  while `SkewStandardYoungTableau` is 0-indexed via `content = range d`);
* `0` off `Y`.

Row/column monotonicity splits three ways in each direction — both cells in
`(2,1)`, one in one out, both skew — and the "one in one out" case is free
(`κ ≤ 3 < 4 ≤ shifted`). The lower-set property of `(2,1)` rules out the fourth
combination. Injectivity of the extension is recovered by subtracting the shift.

Shapes not containing `(2,1)` contribute `0` on the left via the `fDimSkew`
guard (qou-2tkh), so they need nothing.

## Todo

- [x] `mu21_cells`, `mu21_card`, `mem_mu21` — the three cells, by `decide`
- [x] `kappa21` + `_pos` / `_le` / `_row` / `_col` / `_injOn` / `_surj`
- [x] `skew_entry_lt` / `_surj` / `_injOn` from the `content` field
- [x] `straightEntry`, `straightSsyt`, `straightOfSkew`
- [x] `straightEntry_mapsTo` / `_injOn` / `_surjOn` — the `Set.BijOn`
- [x] `straightOfSkew_injective`, `card_skew_le_card_straight`
- [x] `skew_le_straight` proved
- [x] scope notes updated (four places said "the three cited sorries")

## Summary of Changes

`skew_le_straight` is proved; the file is down from three cited `sorry`s to two.

One incidental fix worth keeping: `fDimSkew`'s guard originally needed
`Classical` for `Decidable (inner ≤ outer)`, and an ambient `open scoped
Classical` made the `\` in `Y.cells \ mu21.cells` pick a *different*
`DecidableEq (ℕ × ℕ)` instance than the one baked into
`SkewStandardYoungTableau.content` — so the two would not rewrite against each
other. Replaced by a real instance, `decidableLEYoungDiagram`, built from
`YoungDiagram.cells_subset_iff` (which is `Iff.rfl`; instance search just cannot
see through the `Preorder` wrapper). No `Classical` anywhere now.

Also: `Finset.card_sdiff` at this Mathlib rev is `#(s \ t) = #s - #(t ∩ s)` with
no subset hypothesis — the subset-hypothesis form no longer exists under that
name.
