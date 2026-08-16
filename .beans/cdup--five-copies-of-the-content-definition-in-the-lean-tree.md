---
# cdup
title: The cell-content definition exists five times in the Lean tree, under four names
status: todo
type: task
priority: low
created_at: 2026-08-16T11:00:00Z
updated_at: 2026-08-16T13:12:12Z
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


---

## 2026-08-16 (drain, part 2) — bridges landed, and the "each is `rfl`" claim was wrong twice

`QOU/MathlibExt/YoungDiagramCellsBridges.lean` — **13 bridges, 12 `rfl` + 1
conditional.** Sorry-free, `lean`-direct exit 0, axiom-clean (the pure-`rfl`
ones depend on **no axioms at all**). Purely additive: no existing file changes.

I wrote the file specifically to **test** the claim I had been repeating here
and in two commit messages — *"eight copies, each is definitionally equal, so
every bridge is `rfl`"*. It falsified that in three ways:

1. **Two copies are unreachable, not merely un-drained.**
   `QOU.BraidsAndKnots.cellContent` (`y-lambda-recipe-from-partition.lean`) and
   `QOU.BraidKnot.cellContent` (`jucys-murphy-central-elements-qou.lean`) live
   in **standalone content-block siblings**, not library modules — nothing can
   import them, so no bridge is expressible. The second is *unbridgeable by
   construction*: it is the clash partner, and importing it alongside the
   library declaration is exactly the duplicate-name error the bridge would
   have to survive. Draining those two requires **promoting a content-block
   sibling to a library module first**, which is a different and larger task
   than a `rfl` lemma.
2. **`hookLength` is not `rfl`.** `TwoFiltrationBridge.hookLength` is `ℕ`-valued
   with **truncated** subtraction, so it agrees with the `ℤ`-valued `hook` only
   **on cells of the diagram** — off-diagram the `ℕ` version saturates at `0`
   while the `ℤ` one goes negative. It carries a hypothesis `c ∈ μ`.
3. **My own first docstring for the file miscounted**, saying "six of eight
   bridge by `rfl`" while **twelve** `rfl` bridges had just compiled — it
   conflated the 8 `content` copies with the two arm/leg/hook sets. Replaced
   with a table, since one number was hiding two different countings.

### Corrected migration budget

| | count | cost |
|---|---|---|
| `content` copies reachable + `rfl` | 6 | free |
| `arm`/`leg`/`hook` bridges | 6 lemmas | free |
| `hookLength` | 1 | conditional (`c ∈ μ`) |
| standalone siblings | 2 | **blocked** — needs library promotion |

So the remaining drain is not "eight `rfl` bridges". It is: rewrite call sites
in six library modules along the twelve bridges now available (mechanical, but
touches proofs, so one module per commit), and separately decide whether the
two content-block siblings should become library modules at all — the second of
which cannot coexist with `QOU.BraidKnot` as currently named regardless.
