---
# qou-j3m4
title: '37 unknown-field warnings triaged: one chapter contradiction, five lost author notes'
status: in-progress
type: task
created_at: 2026-08-15T14:46:15Z
updated_at: 2026-08-15T14:46:15Z
---

`folio-assistant` #113 made `run-validate` warn when a block declares a key no
schema knows. Zod block schemas are non-strict, so such a key is **silently
stripped** — the data it carried never reaches the graph, and nothing said so.

qou surfaces **37** of them, over **7** distinct field names. This bean is the
triage: what each one is, whether it can be removed safely, and which need an
author decision.

## First, what it is NOT

My working hypothesis was TS/Zod drift — `BlockBase` grants a field, the Zod
object omits it — which is the class that bit `of` once before. **It is not
that.** `ProseBlock`, `TableBlock`, `EquationBlock` and `DiagramBlock` do
**not** extend `BlockBase` in `schemas/types.ts`; they are standalone
interfaces with deliberately small field sets, and `ProseSchema`/`TableSchema`
match them. The type and the schema agree. These are content declaring fields
the kind never had.

## Safe to remove — provably inert (15)

Every `md:` warning is in `eightfold-way`, declaring `md: "<name>.md"` at the
top level. The real field is `companions.md` — no block schema has a top-level
`md`.

Correcting my own first reading: these are **not** all prose. They are **8
`remark`, 6 `proposition`, 1 `prose`** — three kinds, two of which extend
`BlockBase`. So this is not a light-kind quirk at all; it is a chapter-wide
authoring habit, and the kind is irrelevant because no kind has the field.

Removal cannot change behaviour, and the argument does not rest on convention:
**the key is stripped before anything downstream sees it**, so it has never had
an effect. Checked anyway — all 15 name exactly the conventional sibling, and
all 15 siblings exist:

`a2-from-three-strands`, `baryon-octet-decomposition`,
`borromean-decuplet-derivation`, `color-su3-from-g2`, `decuplet-equal-spacing`,
`dictionary-flavor-layer`, `eightfold-intro`, `eightfold-open-problems`,
`flavor-charge-assignments`, `meson-mass-splitting`,
`meson-octet-decomposition`, `q-deformation-weight-lattice`,
`schur-weyl-eightfold`, `u-spin-coleman-glashow`, `vector-meson-nonet`.

One chapter authored end to end with a field that does nothing.

## Needs an author decision — five author notes are being DISCARDED (5)

`authorNotes` is real, and it is on `BlockBase` — so most of the 530 blocks
that declare it are fine. These five are **prose** and **table** blocks, whose
kinds do not carry it, so their notes are dropped:

| block | kind | note |
| --- | --- | --- |
| `fine-structure-data` | prose | dated `note` |
| `tm-interaction-completeness` | prose | long `status` note on closure-under-composition |
| `millennium-bounds-via-surreals-intro` | prose | `refined-framing`, 2026-06-08 |
| `hecke-log-decomposition-table-data` | table | — |
| `q-beta-form-a-n1-symbolic-table-data` | table | — |

**Do not delete these** — the text is real authored prose and deleting the key
destroys it. Two ways out, and it is a schema question rather than a content
one: either move each note into a `//` comment (lossless, but invisible to
tooling), or grant `authorNotes` to every kind. It is editorial metadata about
a block, not content, so there is no obvious reason prose cannot carry a status
note — but that is a schema change and an owner call.

## Needs an author decision — a chapter contradiction (11)

`chapter:` is on no schema; membership comes from the chapter manifest's
`blocks: [...]`. Ten of the eleven agree with the manifest that lists them and
are merely redundant.

**One does not.** `prop:baryon-product-from-alt` declares
`chapter: "archimedean-universe"` and is listed in **`predicted-spectra`**. It
was added in "…5 new blocks linking PL into mass-tower stack (**strict
archimedean split**)", so the declaration looks like intent that the placement
never carried out. Because the field is inert, nothing has ever flagged the
disagreement. The manifest is authoritative, so it renders in
`predicted-spectra` today; whether it should move is editorial.

## Report only (6)

- `computation` on `knot-periodic-table` — a **prose** block. `TableSchema`
  carries `computation`; `ProseSchema` does not, and the asymmetry looks
  deliberate (a table can be computed). Given the name, the block may want to
  be a `table`. Its computation binding is dropped today.
- `is_mathematics` on `prop:phi-b-bar-parity-decomposition`,
  `prop:phi-b-unitary-bar-odd`, `prop:toroidal-harmonics-delta-lambda`.
  **Zero consumers anywhere in either repo** — no schema, no script, no
  workflow. Inert, and the intent is not recoverable from the field name alone.
- `consumers` and `probe`, both on `prop:positron-correction`.

## Plan

- [x] Remove the 15 inert `md:` declarations — done; validate 42 -> 27 issues
- [ ] Put the `authorNotes` question (comment vs. grant it to every kind) to the
      owner
- [ ] Put `baryon-product-from-alt`'s chapter contradiction to the owner
- [ ] Leave the report-only six recorded here rather than guessed at

## Correction (2026-08-24, later the same day)

My first pass here reported that "there is **no** `archimedean-universe`
chapter — no directory, no manifest entry, and this was the only block naming
one". **That is wrong**, and the shallow clone is why: `git log` over the path
returned nothing because the history is truncated, and I read absence of
history as absence of the thing.

The chapter existed. The top manifest still carries the plan —

> Phase 4+5 (TBD) will split braids-and-knots and **archimedean-universe**
> into focused destination chapters.

— and `e32d978dbf` (2026-05-25) carried it out: **"restructure phase 5: split
archimedean-universe into brings-surface + predicted-spectra"**. The manifest
annotates `predicted-spectra` as *"split from archimedean-universe"*.

**The fix is unchanged and was right for a better reason.** The block is
already in one of the two destinations; the declaration is a pre-split
leftover, not a pointer at something imaginary. It survived because `chapter:`
is on no schema — the key is stripped before anything sees it, so no rename
pass and no validator ever touched it during the restructure.

That also makes the remaining ten `chapter:` declarations worth a second look
rather than dismissing them as merely redundant: any of them could be
pre-restructure too, and agreeing with today's manifest is not the same as
having been maintained.
