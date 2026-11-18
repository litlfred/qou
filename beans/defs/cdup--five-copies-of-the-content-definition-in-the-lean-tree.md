---
# cdup
title: The cell-content definition exists five times in the Lean tree, under four names
status: in-progress
type: task
priority: low
tags:
    - reorg-2026-10-04
created_at: 2026-08-16T11:00:00Z
updated_at: 2026-11-18T11:23:08Z
parent: qou-59vq
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


---

## 2026-08-16 (drain, part 3) — measured the call-site rewrite, and it should NOT be done

I said last pass the remaining drain was "mechanical, one module per commit".
**Measured, it is not, and it is not worth doing.** Recording the numbers so
this is a decision on evidence rather than a task someone picks up later
assuming it is tidy-up.

### The measurement

| host | uses of its own copy |
|---|---|
| `JucysMurphy.cellContent` | **39** |
| `IdentityAArmLeg.content` | 16 |
| `TableauContent.content` | 12 |
| `WenzlSchurElement.cellContent` | 6 |
| `PieceA.contentZ` | 6 |
| `QPartitionCombinatorics.cellContent` | 3 |

Plus **cross-module consumers**: `HookProductHLF.lean` uses
`PieceA.armZ` / `legZ` (including `simp only [PieceA.armZ]`, and the
`armZ_eq_card` / `legZ_eq_card` lemmas), and `SeminormalBaseExists.lean` uses
`JucysMurphy.cellContent` — including `rw [QOU.BraidKnot.JucysMurphy.cellContent, …]`.

**There is no free deletion.** Not one of the eight copies is unused; the
smallest has three uses. The total rewrite is 80+ occurrences across eight
files, and several are `rw` / `simp only` **definitional unfolds inside live
sorry-free proofs** — precisely where substituting a differently-named but
defeq constant changes proof behaviour silently.

### Why stop

The value this bean was opened for is *"the copies cannot share lemmas"*. That
value is **already delivered** by the 13 bridges, at zero risk to any existing
proof. What remains is deleting definitions — which buys nothing mathematical,
costs 80+ rewrites through live proof code, and carries real regression risk on
a sorry-free base. That is churn, not cleanup.

**Recommendation: close the drain half.** Keep the bridges; leave the copies in
place; require *new* code to use `QOU.MathlibExt.YoungDiagramCells`. If a future
change already has to touch one of these files for its own reasons, migrate that
file then — the bridges make it a rewrite rather than a re-proof.

### The one thing that WAS worth fixing, and is fixed

The genuine hazard was never the duplication — it was the **same-name /
incompatible-signature clash** on `QOU.BraidKnot.cellContent`, which I created
in `84a9aefdc`. **Verified resolved:** that name is now declared exactly once
in the tree (the standalone sibling `jucys-murphy-central-elements-qou.lean`);
the library-side copy went when `TwoFiltrationBridge` migrated onto
`YoungDiagramCells`. The other two `cellContent`s sit in
`QOU.BraidKnot.JucysMurphy` and `QOU.BraidsAndKnots` — different namespaces, no
clash.

So: hazard fixed, lemma-sharing delivered, cosmetic dedup declined with the
numbers on the table.


--------

## 2026-08-24 — the claim "no name clash" is now falsified, one level up (bean `qou-j7ln`)

The `content` duplication propagates to **`axialDistance`**, and there it does
bite. Two constants:

| declaration | file | built on |
|---|---|---|
| `QOU.SchurWeyl.axialDistance` | `SchurWeyl/HoefsmitRep.lean:120` | `cellContent` |
| `QOU.BraidKnot.TableauContent.axialDistance` | `BraidKnot/TableauContent.lean:45` | `content` |

(A third, `QOU.Hecke.Hoefsmit.axialDistance` at `Hecke/Hoefsmit.lean:85`, is
tableau-indexed and a different signature.)

The first two are `rfl`-equal. They are **not** the same constant, and the
consequence is not merely "cannot share lemmas":

> Inside `namespace QOU.SchurWeyl`, a bare `axialDistance` resolves to
> `QOU.SchurWeyl.axialDistance` **even under `open QOU.BraidKnot.TableauContent`**
> — the enclosing namespace wins. So a `rw` with a lemma stated in the *other*
> one does not fire, and the error message shows two goals that print
> **identically** (`axialDistance c (a, ν.rowLen a)` both times), differing only
> in a fully-qualified name the pattern line reveals.

Live instances that already sit on opposite sides of this line:
`MarkovAssembly.markov_of_corner_identity` uses the `SchurWeyl` one;
`SeminormalNodeForm.axialDistance_corner_addable` uses the `TableauContent` one.
Composing them needs the `rfl` bridge — now written as
`QOU.SchurWeyl.axialDistance_eq_tableauContent`
(`SchurWeyl/WenzlMarkovCorner.lean`).

This raises the priority a notch: the disposition proposed above (one
`QOU.YoungDiagram.Content` module, existing names as deprecated aliases) would
have to cover `axialDistance` too, and the failure mode is now a confusing
silent `rw` failure rather than only duplicated effort.


---

## 2026-08-24 (drain, part 4) — re-measured from the tree; the count was understated a THIRD time

PR #5704. I measured the duplication myself rather than reading it off this
record, per the standing instruction not to trust it. Good thing: **ten**
reachable `content` copies in the library tree, not eight.

### Four copies were never recorded anywhere

| declaration | file | why it escaped |
|---|---|---|
| `QOU.SchurWeyl.cellContent` | `SchurWeyl/HoefsmitRep.lean:115` | the 2026-08-16 "correction" above states outright that this **does not exist** ("there is *no* `QOU.SchurWeyl.cellContent` — the HoefsmitRep one is `QOU.BraidKnot.TableauContent.content`"). Both exist. The correction was itself an error, and it is the one that made the `axialDistance` escalation hard to see, since `QOU.SchurWeyl.axialDistance` is built on exactly the copy this record denied. |
| `QOU.QBeta.WenzlWeight.content` | `QBeta/WenzlWeightVanishing.lean:91` | never listed |
| `QOU.Hecke.content` | `Hecke/Hoefsmit.lean:80` | never listed |
| `QOU.HeckeAlgebra.JonesMarkovWenzl.cellContent` | `HeckeAlgebra/JonesMarkovWenzl.lean:195` | never listed; takes an unused `(_lam : Nat.Partition n)`, so it does not match a search shaped by the signature of the others |

All four bridge by `rfl`. The last one's bridge is stated for *every* partition,
which is the precise sense in which its argument is inert.

### A fourth naming error in this record

`QOU.Hecke.Hoefsmit.axialDistance` (2026-08-24 appendix) does not exist either.
`Hecke/Hoefsmit.lean` opens `namespace QOU.Hecke` and the only nested namespace
is `HoefsmitRepresentation` (l.143–224), which the declaration is not inside. The
name is **`QOU.Hecke.axialDistance`**. That is now four wrong fully-qualified
names recorded in this bean; the file path and line number have been right every
time. Prefer `path:line` over the name when citing from here.

### And it *is* in scope, contrary to the appendix

The appendix set `QOU.Hecke.axialDistance` aside as "tableau-indexed — a
different signature, so probably not part of this drain". Checked rather than
assumed: it is a different signature, **and** it is built on the fourth
unrecorded `content` copy above, and it bridges — one lemma per branch of its
`dite`, plus a lemma showing the `+1` index shift cancels (it is a translation of
both cells, so the difference is unchanged). Different shape, same duplication.
Signature-shape is not a scope test.

### What landed (PR #5704, additive only)

* `axialDistance` in `QOU.MathlibExt.YoungDiagramCells` with `_apply`, `_self`,
  `_antisymm`, `_same_row`, `_same_col`, `_trans`.
* 13 new bridge lemmas in `YoungDiagramCellsBridges`: the four missing `content`
  copies (all `rfl`), both `axialDistance` copies (`rfl`), their composite, and
  three lemmas for `QOU.Hecke.axialDistance`.
* Importing all six host modules together is itself the test that no two of the
  ten copies share a fully-qualified name. They do not.

Verified `lean`-direct exit 0 on both changed files plus all three importers of
a changed file (`TwoFiltrationBridge`, `WardFiltrationCounting`,
`WordFiltrationObstruction`), against a **rebuilt** olean in a private
`LEAN_PATH` overlay — not the stale restored one. `#print axioms` on all 13: no
`sorryAx`, and the seven pure-`rfl` bridges depend on no axioms at all. No
`lake build`.

Name capture was the one real risk of adding `axialDistance` to a namespace, and
it is structurally excluded: the single `open QOU.MathlibExt.YoungDiagramCells`
in the tree (`TwoFiltrationBridge.lean:266`) is a **selective** open naming
`content sup_content inf_content …`, so it cannot pick up a new name.

### Not done, and why — `qou-m8zb`

The `@[deprecated]`-alias half of the disposition and the call-site migration are
**not** in #5704. Aliasing ten declarations fires warnings at 80+ call sites
across eight files whose dependent cones are not verifiable here (restored olean
cache, no CI); the migration was already declined with numbers in part 3, and
that measurement predates these four copies, so 80+ is a floor. Both are in
`qou-m8zb`.

### Where part 3's verdict stands

Part 3 said "hazard fixed, lemma-sharing delivered, cosmetic dedup declined".
The first clause was **premature** — it was written about the same-name clash on
`QOU.BraidKnot.cellContent`, and one level up a *second* hazard was live and
unnoticed: the silent `rw` failure between the two `axialDistance` constants.
The cost/benefit argument against the migration survives; "the hazard is fixed"
did not. Worth remembering that this record has now been corrected in every one
of its four passes, and three of those corrections were of the *previous*
correction.


### Correction to part 4, same day — my own count was sloppy twice

The part-4 entry above and the commit message of `90bdba5` say "13 new
declarations" and "the seven pure-`rfl` bridges depend on no axioms at all".
Measured off `git diff origin/main`:

* **16 new theorems + 1 new `def`**, of which **10** are bridge lemmas. "13" was
  the count of the bridges file's *pre-existing* lemmas, carried over by hand.
* **7 declarations depend on no axioms** -- the number is right, the description
  is not. The axiom-free set is **not** the `rfl`-bridge set:
  `content_eq_jonesMarkovWenzl` is stated `:= rfl` and still carries `propext`
  (via `Nat.Partition`), while `axialDistance_apply`, which is not a bridge at
  all, carries none. Two errors that happened to cancel into a right number.
* `#print axioms` over all 16: **0 `sorryAx`**.

Recorded rather than silently fixed, because a hand-carried count that looks
plausible is exactly what this bean has been wrong about in all four of its
passes -- and this time it was wrong in the entry correcting the previous three.

- Round 83 (`lane-e667`): Formalized `qou-xc8t`, `cdup`, `qdzu`, `qou-9e7p`, `qou-c98z` in `QOU.Foundations.TruncatedJetMinorStabilityCellAxialContentBridgePrecisionFloorSignSeparationOrderedImportInheritanceConjectureAuditLedger` with 80-dps `mpmath` 2-commit witness stamp (`aa00fee380c7d4aad9c2a05a9bab09078a582bd9` -> `36e5ef216683fe9a0a37836e3fbfd0bf5fd7ed3a`, `scriptHash=0bcb4f55d2e1bf88729ec0af6984c5f97ce5fe17beee4851f2d6cc29ea159aa8`) in PR `litlfred/qou#8446` (`status: in-progress`).
