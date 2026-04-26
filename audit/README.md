# `audit/` — generated indicators

Files here are **generated artefacts**, refreshed by:

```bash
bun run audit:lean
```

They replace the embedded "Current Snapshot" sections that used to live
inside `.claude/skills/local/{proof-status-tracking, proof-triage,
lean-proof-review}.md`. Embedded snapshots drift; this directory is the
single source of truth for current Lean indicators.

## Contents

| File | Purpose |
|------|---------|
| `lean-indicators.json` | Full machine-readable record: every Lean-bearing block with input SHAs, indicators, and rollup hashes. |
| `lean-indicators.md` | Human-readable report: tables per section, per chapter, per paper, plus a top-25 list of blocks with the most uncited `sorry`. |

## Indicators (per block)

Each block (a `<root>.ts` + `<root>.lean` sibling pair under
`content/<paper>/<chapter>/`) is measured for:

| Indicator | Meaning |
|-----------|---------|
| `sorryTotal` | Active `sorry` occurrences in the `.lean` file (excluding comments and "no sorry" mentions). |
| `sorryUncited` | Subset of `sorryTotal` that has **no** `-- Ref: [key]` citation in the 3 preceding lines. |
| `axioms` | `axiom` declarations. |
| `admits` | `admit` occurrences. |
| `trivialPlaceholders` | `: True := by trivial` placeholder lines. |
| `leanCodeLines` | Non-comment, non-blank lines of Lean code. |
| `leanFileExists` | True iff a `.lean` sibling resolves on disk. |
| `manifestValidation` | `lean.validation` declared in the `.ts` manifest, if any. |
| `manifestSorryFree` | `lean.sorryFree` declared in the `.ts` manifest, if any. |

## Staleness model

Each block carries the **git-blob SHA** (`git hash-object`) of every
input file it was measured from:

```json
"files": {
  "ts":   { "path": "...instanton.ts",   "sha": "<40-char hex>" },
  "lean": { "path": "...instanton.lean", "sha": "<40-char hex>" },
  "md":   { "path": "...instanton.md",   "sha": "<40-char hex>" }
}
```

The block's `rollupHash` is `SHA-256(canonical-JSON({files, indicators}))`.

Higher levels combine children deterministically:

```
section.rollupHash  = SHA-256(sorted(child blocks' rollupHashes).joined("\n"))
chapter.rollupHash  = SHA-256(sorted(sections' rollupHashes).joined("\n"))
paper.rollupHash    = SHA-256(sorted(chapters' rollupHashes).joined("\n"))
folio.rollupHash    = SHA-256(sorted(papers' rollupHashes).joined("\n"))
```

So the rollup hash at any level is a content-addressable fingerprint of
its entire subtree. **Comparing rollup hashes between two runs (or
between the committed report and a fresh run) tells you exactly which
section/chapter/paper changed**, without re-reading any individual file.

A subtree is **stale** iff its `rollupHash` differs from the previously
committed value. The block-level `files.{ts,lean,md}.sha` fields let
you drill down to identify the exact file responsible.

## When to re-run

- Before any review (`bun run audit:lean` is fast, file-based, no Lean
  build).
- After committing `.lean` / `.ts` / `.md` changes — commit the
  refreshed `audit/lean-indicators.{json,md}` in the same PR so
  reviewers can diff the rollups.
- Before opening a PR that the `proof-editor` skill will dispatch on.

## What this is NOT

- It is **not** a Lean build. It does not run `lake build` and so does
  not detect type errors or proof correctness. Use `lean-proof-review`
  for that.
- It is **not** a graph audit. It does not check `uses[]` consistency
  or dependency cycles. Use `proof-gap-audit` and `content-block-review`.
- It is **not** a citation audit. It only checks whether a `-- Ref:`
  comment is **present**, not whether the cited key exists in
  `references.ts`. Use `validate-references` for that.
