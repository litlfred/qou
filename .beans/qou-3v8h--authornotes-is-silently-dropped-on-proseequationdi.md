---
# qou-3v8h
title: authorNotes is silently dropped on prose/equation/diagram/table — AGENTS.md 4d says every block kind accepts it
status: completed
type: task
priority: high
created_at: 2026-08-26T23:48:05Z
updated_at: 2026-09-05T07:23:40Z
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


## CLOSED 2026-09-05 — the stated close-condition is now met

This bean was deliberately left open with the reason recorded in `qou-bstl`:
*"NOT closing: the defect is fixed on a branch, not in the product. Closing on
'someone has a fix somewhere' is the failure mode this corpus keeps paying
for."* That was the right call. **The fix is now in the product.**

**Evidence.** folio-assistant `a117daa` (2026-09-03, *"Four block kinds
restated BlockBase instead of extending it"*) is confirmed an ancestor of that
repo's `main` (`git merge-base --is-ancestor a117daa origin/main` -> yes).
`affcec4`, the branch commit this bean's predecessor named, is also on main.

**Verified by PARSE, not grep** — grep only shows the declaration changed;
parse shows the field survives. Each of `ProseSchema` / `EquationSchema` /
`DiagramSchema` / `TableSchema` `safeParse`s a block carrying
`authorNotes`, `defines`, `cites`, `computation`:

    prose:    authorNotes=KEPT  defines=KEPT  cites=KEPT  computation=KEPT
    equation: authorNotes=KEPT  defines=KEPT  cites=KEPT
    diagram:  authorNotes=KEPT  cites=KEPT
    table:    authorNotes=KEPT  cites=KEPT  computation=KEPT

**All six previously-dropped qou fields are now honored without anyone editing
them** — they were never removed from the blocks, only discarded at parse. That
includes the substantive one: `hecke-log-decomposition-table-data`'s
multi-paragraph caveat recording that the table has no source block, and
`prose:knot-periodic-table`'s `computation` link to its producer.

**The five invented field names are also gone** (`is_mathematics` x3, `probe`,
`consumers`): 0 top-level occurrences remain in `content/`. `positron-correction`
had them removed with an authorNote explaining why; both `phi-b-*` moved
`is_mathematics` into the declared `meta:` escape hatch. The other 7 grep hits
for those names are `consumers:` NESTED inside `computation:`, which is declared
and legitimate — do not "fix" those.

**Upstream now locks the mechanism, not the fields.** `a117daa` also adds
`scripts/tests/block-base-fields.test.ts` (fails when any block schema falls
behind the base) and `scripts/tests/schema-ts-zod-parity.test.ts`. The
2026-08-24 hand-grant fixed `authorNotes` and left `defines` / `cites` /
`simulator` / `computation` to be forgotten one kind at a time; that can no
longer happen silently.

## What this session actually changed (AGENTS.md 4d)

The schema was fine; **the instruction was not.** 4d opened with a bolded
stop-sign asserting the drops are live, retracted it nine lines down, and then
CLOSED by telling agents *"do not put an author note on a prose, table,
equation or diagram block"*. Top-down, an agent met the false claim first and a
directive to avoid a working field last. Fixed: live state leads, closing
advice withdrawn and inverted, clone-currency check added as a runnable command.

**A defect in the correction itself, recorded rather than quietly patched.**
The 2026-09-03 table states its measurement basis as folio-assistant
`93e476b` and marks two rows *"fixed — folio-assistant#164"*. `93e476b` is
dated 2026-08-31 and does **not** contain `a117daa`, so those rows were
forward-looking claims about a PR that had not landed. They are true today.
They were not when written — and that is exactly the move this bean refused to
close on, appearing inside the text correcting this bean's defect.

## Trap for the next agent — the clone, not the schema

Measured this session: the same qou tree, validated against a folio-assistant
clone **169 commits behind**, reports all six fields as dropped — a defect that
no longer exists. The validator you run is the validator in your checkout.
`bash scripts/setup-folio-assistant.sh` and check
`git -C folio-assistant log --oneline -1` before filing anything from a
validate run. My own first measurement this session was wrong for this reason.

Superseded by nothing; `qou-eu0r` is the duplicate and closes with this.
Sibling `qou-p7it` (in-progress) owns the upstream half — left to its owner.
