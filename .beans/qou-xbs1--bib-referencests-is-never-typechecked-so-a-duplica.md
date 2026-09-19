---
# qou-xbs1
title: 'BIB: references.ts is never typechecked, so a duplicate object key silently clobbered a note'
status: todo
type: task
priority: normal
created_at: 2026-09-15T22:36:29Z
updated_at: 2026-09-15T22:37:05Z
---

## The defect, and how it was found

`content/schema/references.ts` entry `yekutieli2008` (on `origin/main`,
lines 1295-1296 before this fix) carried **two `note:` keys**:

```ts
    note: "arXiv:0801.3233",
    note: "PDF library/arxiv-0801.3233v4/0801.3233v4.pdf (ingested 2026-09-05, owner upload 8a730706). …",
```

In a JS/TS object literal the second wins, so the first was discarded at
load. Verified, not assumed: `getRef("yekutieli2008").note` returned the
long provenance string with no arXiv id in front.

**It is reader-visible.** `export-bibtex.ts:236` emits `note` straight into
BibTeX, so the printed bibliography for this entry carried a
~400-character provenance paragraph — an ingest date, an owner upload id,
and a bean number — in place of `arXiv:0801.3233`.

Found by accident: `folio-assistant`'s `tsc --noEmit` picked the file up
through the gitignored symlinks `content/schema/references.ts` and
`schemas/references.ts` (`.gitignore:57`, `:69`) and reported **TS1117 —
"An object literal cannot have multiple properties with the same name"**.
Nothing in qou's own gates reports it.

## Why nothing caught it

- **`validate-references.ts:101` passes by accident.** It asks
  `entry.note?.toLowerCase().includes("arxiv")` — and the *surviving* note
  happens to contain "arXiv:0905.0488" and the string "arxiv" in a path. So
  the one check that reads this field was satisfied by a different arXiv id
  than the one that was lost.
- **No typecheck runs over `content/schema/`.** TypeScript diagnoses this
  class exactly (TS1117, compile-time, zero false positives) and is never
  invoked on it here.

## Scope — measured, not estimated

`yekutieli2008` is the **only** entry in the file with a duplicated
top-level key. Measured by brace-depth scan over every `ref({ … })` block:
1 of them, 1 duplicated key. So this is a single-instance fix, not a drain.

## Fixed

Both facts kept, arXiv id first, matching the convention of the other **94**
entries whose note is an arXiv id. Corpus-derived (AGENTS.md exemption 2):
the entry's own `library.arxiv: "0801.3233v4"` and `URL` already fix the
value, and the 94 siblings fix the placement.

## Open — the gate, which is what actually matters

The fix removes the instance; nothing stops the next one. Options, none
enacted (§ASK THE OWNER):

1. **Add `content/schema/` to a qou typecheck gate.** Catches TS1117 and
   every other type error in the bibliography. Cost: a new gate and whatever
   pre-existing errors it surfaces on first run — unmeasured.
2. **Add a duplicate-key check to `validate-bib.ts`.** Narrow, cheap, no new
   tooling; catches only this class.
3. **Nothing.** The instance is fixed; the class recurs silently the next
   time an ingest run appends a `note` to an entry that has one. Given ingest
   *does* append notes (this one is dated 2026-09-05), this is the likely
   recurrence path.

Recommendation (judgement, not a finding): **2**. It is the cheap one, it
lives where bibliography rules already live, and it needs no answer to the
question option 1 opens.
