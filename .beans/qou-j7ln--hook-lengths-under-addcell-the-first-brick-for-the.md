---
# qou-j7ln
title: Hook lengths under addCell — the first brick for the arbitrary-z corner identity
status: in-progress
type: task
priority: normal
created_at: 2026-08-24T13:03:43Z
updated_at: 2026-08-24T13:12:50Z
---

## Landed — PR #5645

`QOU/SchurWeyl/HookLengthAddCell.lean`, sorry-free, axiom-clean, pure ℕ × ℕ combinatorics.

- `rowLen_of_isAddableCell` / `colLen_of_isAddableCell` — an addable cell sits at the end of its
  row and the bottom of its column.
- `hookLength_addCell_self` — the added cell's own hook is `1`.
- `hookLength_addCell_of_mem` — every other cell gains `1` **iff** it shares the new cell's row or
  column, `0` otherwise.

**The statement is cleaner than the arm/leg case split I budgeted for.** For `x ∈ ν` the *order*
conditions come free: sharing `s`'s row forces `x.2 < rowLen ν x.1 = s.2` automatically, and
symmetrically for the column. So the hook grows by `1` on exactly the union of `s`'s row and
column, and those meet only at `s`, which is not in `ν` — one `if`, not two cases.

**Corpus-grepped before writing**: no hook-under-`addCell` or hook-under-`eraseCorner` lemma
existed. The `hookLength` infrastructure that does exist (`HookLengthFormula`, `QHookProduct`,
`WenzlSchurElement`, `YoungDiagramCells`) is about the hook-length *formula* and product
identities, not about how a hook moves under a shape change. `qou-68e1` is adjacent (consolidating
`schurElement`'s product form) but a different item; untouched.

### Next brick, and an honest estimate

The weight ratio itself:

    w_{ν+s} / w_ν = N(s) / [ (q²−1) · ∏_{x ∈ arm(s) ∪ leg(s)} (q^{2(h(x)+1)}−1)/(q^{2h(x)}−1) ]

The numerator half is free (per-cell, diagram-independent). The arm/leg product is the work, and it
has **no counterpart in the two-row case** — there `schurPrincipal_twoRow` telescoped the entire
hook-content product, which is exactly the shortcut arbitrary `z` does not get. I am not putting a
timeline on it. Nothing downstream is blocked: convention D is canonical per the 2026-08-15 ruling
and its identification is proved and merged (`91bf8fcb4`).
