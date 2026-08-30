---
# qou-3v8h
title: authorNotes is silently dropped on prose/equation/diagram/table — AGENTS.md 4d says every block kind accepts it
status: todo
type: task
priority: high
created_at: 2026-08-26T23:48:05Z
updated_at: 2026-08-26T23:48:53Z
---

## The defect

`folio-assistant/schemas/types.ts:686` declares `authorNotes?: AuthorNote[]` on
**`BlockBase`**. Four block interfaces do **not** extend `BlockBase` (nor
`ProvableBase`) — they are standalone and redeclare `kind`/`label`/`title`/
`uses`/`foreshadows`/`cites` by hand:

    ProseBlock      (types.ts:941)   STANDALONE
    EquationBlock                    STANDALONE
    DiagramBlock                     STANDALONE
    TableBlock                       STANDALONE

For comparison, these DO extend it and are fine: Algorithm, Conjecture,
Corollary, Definition, Example, Lemma, Proof, Proposition, Remark, Simulator,
Theorem.

So on those four kinds `authorNotes` is an unknown field. The validator does
catch it — *"Unknown field `authorNotes` — no schema declares it, so it was
silently dropped and carries no meaning"* — but as a **warning**, on a run that
exits 0 with 13 issues, where it reads as one more piece of pre-existing noise.

## Why this is worse than a normal schema gap

**AGENTS.md §4d actively instructs agents to do the thing that loses data.** It
says, verbatim:

> `BlockBase.authorNotes?: AuthorNote[]` — **every block kind accepts it**
> (builders pass through via `Omit<XBlock, "kind">`).

That is false for four kinds. And §4d's whole purpose is to migrate status
banners **out of `.md` prose into `authorNotes`**, with a migration table
mapping `> **Status: …**` → `authorNotes: [{kind: "status", body}]`. An agent
following that instruction on a `prose` block **deletes the banner from the
`.md` and writes it into a field that is discarded.** The note is gone from
both places.

The irony is load-bearing: `prose` is the kind whose name most suggests it
carries prose banners, and it is one of the four that cannot hold the
replacement.

## Live damage on main (3 blocks, measured)

Each currently carries an `authorNotes` entry that renders nowhere:

- `content/quantum-observable-universe/observations/fine-structure-data.ts`
- `content/quantum-observable-universe/appendix-transfer-matrices/tm-interaction-completeness.ts`
- `content/quantum-observable-universe/appendix-surreals/millennium-bounds-via-surreals-intro.ts`

Do **not** just delete the field from these — read what the note says first and
decide whether it should go back into the `.md` or wait for the schema fix.
The content is the thing being lost; the field is only where it was put.

## Two halves, in two different repos

1. **Schema fix — `litlfred/folio-assistant`, NOT this repo.**
   `folio-assistant/` here is a symlink to `../folio-assistant`, remote
   `https://github.com/litlfred/folio-assistant.git`. It is **outside the qou
   session's GitHub scope**, so it cannot be fixed from a qou branch. Either
   make `Prose`/`Equation`/`Diagram`/`Table` extend `BlockBase`, or add
   `authorNotes` to each. Prefer extending — the hand-redeclared field lists
   are exactly how this drifted.
2. **Doc fix — this repo.** AGENTS.md §4d's "every block kind accepts it" must
   be corrected. Worth doing even before the schema fix lands, since the wrong
   sentence is what makes agents lose notes.

## Why it was not fixed in the PR that found it

Surfaced while checking whether MY OWN `authorNotes` addition to
`algebraic-gns-embedding.ts` (PR #5864) had been silently dropped. It had not —
that block is a `proof`/`proposition` kind, which extends `BlockBase`, and it is
absent from the 13 validator warnings. So this is pre-existing on main, in a
different domain from #5864 (Q_β decay-channel algebra), and half of it is not
even in this repository. Queued rather than chased, per the bean policy.

## Note for whoever picks it up

The other 10 validator warnings are a DIFFERENT class and should not be swept in
with this one. `is_mathematics` (3 blocks), `consumers` (1) and `computation` (1)
are fields that do not exist anywhere in the schema — invented or misspelled.
`authorNotes` is real and declared; only its reachability is broken. Fixing the
schema will silence 3 of the 13 and must not be expected to silence the rest.

---

## 2026-08-29 — THE FIX EXISTS, and predates this bean by two days

`folio-assistant` commit `affcec4`, 2026-08-24: *"schema: grant authorNotes to
prose, equation, diagram and table"*. This bean was filed 2026-08-26 by someone
who did not know, which is the fourth independent rediscovery on this branch in
a week (the others: the `qa-agent-entry` evidence guard, the four
`generate-index.ts` defects, and this).

Recording it here so it is not found and fixed a **third** time.

### What the fix does, verified

Both halves, all four kinds — checked individually rather than assumed:

| kind | `schemas/types.ts` | `schemas/constraints.ts` (Zod) |
|---|---|---|
| `ProseBlock` / `ProseSchema` | ✅ | ✅ |
| `EquationBlock` / `EquationSchema` | ✅ | ✅ |
| `DiagramBlock` / `DiagramSchema` | ✅ | ✅ |
| `TableBlock` / `TableSchema` | ✅ | ✅ |

Both sides matter and the bean is right to imply it: declaring the TS field
alone would have kept the validator quiet while a **non-strict Zod object
silently strips the unknown key and still parses**, so the note would have been
lost with nothing said. `scripts/tests/schema-ts-zod-parity.test.ts` gained
three cases — every kind carries `authorNotes` in TS, the same in Zod, and a
round-trip proving the field *survives validation* rather than merely being
declared.

### Live impact: five blocks, and none of it was decoration

`run-validate` reports **zero** `authorNotes` warnings with the fix in place
(it reported them before). The five blocks that were silently losing content:

* `fine-structure-data` (prose) — *"`det G_q` disambiguated; α⁻¹ is
  convention-independent. This block previously wrote the Chern–Simons damping
  factor as κ = …"* — a correction record
* `tm-interaction-completeness` (prose) — a rigour caveat scoping what the
  single-crossing enumeration does and does not close
* `millennium-bounds-via-surreals-intro` (prose) — a re-scope of the
  Millennium-problem entries
* `hecke-log-decomposition-table-data` and
  `q-beta-form-a-n1-symbolic-table-data` (table) — both carrying **"This table
  has no source block"**, a provenance warning

Exactly the §4d material the convention exists to preserve, on exactly the
kinds where §4d's instruction destroyed it.

### AGENTS.md needs no edit

The bean notes §4d asserts *"every block kind accepts it"* and that this was
false. The fix makes it **true**, so the documentation is now correct as
written rather than needing a caveat.

### Still open, and what unblocks it

`affcec4` is on `claude/stalled-prs-scope-map-ufyvla` in folio-assistant
(merged with main, suite green: 1,214 pass / 0 fail, eslint clean) and has
**not landed on that repo's main**. Until it does, main still discards those
five notes.

NOT closing: the defect is fixed on a branch, not in the product. Closing on
"someone has a fix somewhere" is the failure mode this corpus keeps paying for.

