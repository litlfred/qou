---
# cdup
title: The cell-content definition exists five times in the Lean tree, under four names
status: todo
type: task
priority: low
created_at: 2026-08-16T11:00:00Z
updated_at: 2026-08-16T11:32:35Z
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


---

## 2026-08-16 — corrected: nine copies, not five, and one is a real clash (#5205)

**I undercounted and mis-named.** The list above covers only the tuple form
`(c : ℕ × ℕ)`. The same arithmetic also appears **curried** as `(i j : _)` in
four more places, and two of the five names above are wrong.

| tuple `(c : ℕ × ℕ)` | curried `(i j : _)` |
|---|---|
| `QOU.BraidKnot.IdentityAArmLeg.content` | `QOU.MathlibExt.QPartitionCombinatorics.cellContent` |
| `QOU.BraidKnot.TableauContent.content` | `QOU.MathlibExt.WenzlSchurElement.cellContent` |
| `QOU.BraidKnot.JucysMurphy.cellContent` | `QOU.BraidsAndKnots.cellContent` (`y-lambda-recipe-from-partition`) |
| `QOU.BraidKnot.PieceA.contentZ` (in `PieceAGeneral.lean`) | `QOU.BraidKnot.cellContent` (`jucys-murphy-central-elements-qou`) |
| `QOU.BraidKnot.cellContent` (`TwoFiltrationBridge`) | |

Corrections to the original table: there is **no** `QOU.SchurWeyl.cellContent`
(the `HoefsmitRep` one is `QOU.BraidKnot.TableauContent.content`), and
`PieceA.contentZ` lives in `PieceAGeneral.lean`.

**"No name clash" was wrong.** The bottom row of each column is the *same
fully-qualified name* — `QOU.BraidKnot.cellContent` — at incompatible
signatures (`ℕ × ℕ → ℤ` vs `ℤ → ℤ → ℤ`): the library file
`BraidKnot/TwoFiltrationBridge.lean` and the standalone content-block sibling
`mass-theory/jucys-murphy-central-elements-qou.lean`. They compile today only
because the sibling is never co-imported; anything importing both is a **hard
duplicate-declaration error**, not a shadowing nuisance. My rename in
`84a9aefdc` created that while dodging the milder problem — I traded down.

## Drain progress

* **Home built.** `QOU.MathlibExt.YoungDiagramCells` — `content`, `arm`, `leg`,
  `hook` over `ℤ` with `hook_eq`, `arm_nonneg`, `leg_nonneg`, `one_le_hook`,
  `rowLen0_pos`, `colLen0_pos`, `sup_content`, `inf_content`,
  `content_spread_eq_corner`. Sorry-free, axiom-clean.
* **First migration done.** `TwoFiltrationBridge` now imports it; both the sixth
  copy and the clash are gone.
* **Eight copies remain.** Each is definitionally equal to
  `YoungDiagramCells.content`, so every bridge is `rfl`.

**Namespace warning for whoever drains the rest.** Do not use the obvious
`QOU.YoungDiagram` — a `QOU.YoungDiagram` namespace captures `open YoungDiagram`
inside any `QOU.*` namespace and silently redirects it away from Mathlib,
breaking `rowLen_anti` / `mem_iff_lt_rowLen` at every existing call site. Hence
`QOU.MathlibExt`.

**Adjacent, larger, not this bean.** `StandardYoungTableau` is defined **four**
times (`QOU/Mathlib/`, `QOU/BraidKnot/`, `QOU/Hecke/`, plus the `SYT` abbrev in
`SchurWeyl/YoungTableaux.lean`). Same pattern, higher stakes — these carry
proofs, not one-liners. Worth its own bean before anyone touches it.


### Correction to the paragraph immediately above (same day)

**"Worth its own bean before anyone touches it" is wrong — it already has one,
and a better one than I would have written.** The corpus-grep caught my own
over-claim. The `StandardYoungTableau` divergence is tracked as *"SUB-BRIDGE:
numSYT(BraidKnot) = numStandardYoungTableaux — the two StandardYoungTableau
structures differ (BraidKnot 0-indexed entry+zero_off+inj_on; SSYT-wrapper BijOn
Icc 1 card). Needs an SYT-type equiv (index shift + SSYT wrap), ~50-100 lines.
Blocks numSYT=numSYTenum∘rowLens (qou-ftmf)"*, plus several neighbours. Do not
open a second one.

**Naming trap worth recording.** That bean's phrase "Mathlib SSYT-wrapper" means
`QOU/Mathlib/StandardYoungTableau.lean` — the **in-repo** namespace that mimics
a Mathlib API — not upstream Mathlib, which has *zero* occurrences of
`StandardYoungTableau` at the pinned `rev f897ebcf72`. I misread it that way for
several minutes. A `QOU/Mathlib/` directory reads as "from Mathlib" to anyone
who has not checked, and that is exactly the wrong inference for deciding what
still has to be built.
