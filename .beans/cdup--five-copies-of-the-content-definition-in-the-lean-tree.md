---
# cdup
title: 'The cell-content definition exists five times in the Lean tree, under four names'
status: todo
type: task
priority: low
created_at: 2026-08-16T11:00:00Z
updated_at: 2026-08-16T11:00:00Z
---
Found while adding a sixth — caught in review of my own PR (#5205, bean `wpdb`).

`(c.2 : ℤ) - (c.1 : ℤ)` — the content / diagonal index of a Young-diagram cell —
is defined **verbatim** in five places under four names:

| declaration | file |
|---|---|
| `QOU.SchurWeyl.cellContent` | `SchurWeyl/HoefsmitRep.lean:115` |
| `QOU.BraidKnot.IdentityAArmLeg.content` | `BraidKnot/IdentityAArmLeg.lean:73` |
| `QOU.BraidKnot.JucysMurphy.cellContent` | `BraidKnot/JucysMurphy.lean:163` |
| `QOU.BraidKnot.PieceA.contentZ` | `BraidKnot/PieceAGeneral.lean:40` |
| `QOU.BraidKnot.cellContent` | `BraidKnot/TwoFiltrationBridge.lean` (mine, #5205) |

**No name clash** — each sits in its own sub-namespace, so nothing breaks and
this is not urgent. My first draft did take the bare `QOU.BraidKnot.content`
slot, which `open QOU.BraidKnot` would have shadowed against
`IdentityAArmLeg.content`; renamed before merge.

The cost is not compilation, it is that **five copies cannot share lemmas**.
`PieceAGeneral` proves `hookZ_eq`, `armZ_nonneg`, `legZ_nonneg` against its own
copy; `HoefsmitRep` builds `axialDistance` on another; `TwoFiltrationBridge`
proves `sup_content` / `inf_content` on a third. None of those results is
reachable from the others without a `rfl` bridge that nobody has written.

Same story one level up: `arm` / `leg` / `hook` are defined twice
(`IdentityAArmLeg` in ℤ, `PieceAGeneral` in ℤ) and a third time in ℕ as
`TwoFiltrationBridge.hookLength`.

**Suggested disposition.** One `QOU.YoungDiagram.Content` module carrying
`cellContent`, `arm`, `leg`, `hook` in ℤ plus the basic lemmas, with the
existing names as deprecated aliases. Low priority — nothing is wrong, it is
duplicated effort — but it will keep growing: this arc added one copy without
anybody noticing until a grep for something else turned it up.
