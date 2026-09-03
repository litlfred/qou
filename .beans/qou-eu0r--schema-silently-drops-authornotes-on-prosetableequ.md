---
# qou-eu0r
title: Schema silently drops authorNotes on prose/table/equation/diagram
status: todo
type: task
priority: high
created_at: 2026-08-30T09:26:51Z
updated_at: 2026-08-30T09:26:51Z
---

AGENTS.md §4d said `authorNotes` is on `BlockBase` and *"every block kind
accepts it"*. Measured 2026-08-30: false for four content-block kinds.

`prose`, `table`, `equation` and `diagram` have their zod schemas declared as
standalone `z.object({...})` in `folio-assistant/schemas/constraints.ts`
rather than `BlockBaseSchema.extend({...})`. They restate a subset of the base
fields; `authorNotes` is not among them. Zod strips unknown keys, so the note
validates clean and vanishes.

## Measured impact in qou — 6 dropped fields

| block | field |
|---|---|
| `braids-and-knots/hecke-log-decomposition-table-data` | `authorNotes` |
| `nuclear-interactions/q-beta-form-a-n1-symbolic-table-data` | `authorNotes` |
| `observations/fine-structure-data` | `authorNotes` |
| `appendix-surreals/millennium-bounds-via-surreals-intro` | `authorNotes` |
| `appendix-transfer-matrices/tm-interaction-completeness` | `authorNotes` |
| `appendix-knot-periodic-table/knot-periodic-table` | `computation` |

The first is not a formality: a multi-paragraph caveat recording that the
table has **no source block**, that its `uses[]` pointed at a label existing
nowhere in the corpus, and that the edge was dropped rather than guessed
because `uses[]` feeds the ordering metrics. That reasoning is written into a
field that goes nowhere.

Counted two ways that agree: walking `content/**/*.ts` for the four builders
and grepping the dropped field names, and independently from the validator's
own "Unknown field" warnings.

## The wider hazard is NOT authorNotes

The same four kinds also drop **`defines`**, and all but `prose` drop
**`cites`**. Zero blocks hit those today — but §4c *mandates* `defines` for
every glossary term, so the first `prose` or `table` block to register one
gets it silently discarded and the glossary gate reads an empty list rather
than firing. Latent, same defect, worse blast radius.

## Second class, same symptom, different cause

Five *invented* field names that no schema declares anywhere:
`is_mathematics` (×3), `probe`, `consumers`. Authoring errors, not a schema
gap, and dropped just as quietly.

## Why nobody saw it

The "Unknown field" check is recent, and a stale `folio-assistant` clone does
not have it: the same qou tree reported **1** validate issue before the clone
was fast-forwarded 273 commits and **14** after. A clean validate against a
stale clone is not evidence — worth knowing independently of this bug.

## Fix

Belongs in `folio-assistant` (outside this session's repo scope): make
`ProseSchema`, `TableSchema`, `EquationSchema` and `DiagramSchema` extend
`BlockBaseSchema` as the other six kinds do. Then re-validate qou and confirm
the six fields above take effect rather than being dropped.

Until then: do **not** put an author note on a `prose`, `table`, `equation` or
`diagram` block. Recorded in AGENTS.md §4d.
