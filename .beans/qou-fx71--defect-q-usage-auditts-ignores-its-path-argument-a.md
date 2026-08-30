---
# qou-fx71
title: 'DEFECT: q-usage-audit.ts ignores its path argument and rewrites all 3573 sidecars'
status: todo
type: bug
priority: normal
created_at: 2026-08-30T12:08:48Z
updated_at: 2026-08-30T12:09:26Z
---

## What happened

Ran, intending to refresh ONE block's stale `q-usage-*` criteria:

    bun run folio-assistant/content/pipeline/q-usage-audit.ts \
      content/quantum-observable-universe/braids-and-knots/why-b3.md

It **ignored the path** and swept the whole tree: **3,573 sidecars modified**,
plus untracked `.qa.json` files created for blocks that had none, plus a witness
at `docs/audits/2026-08-30-q-usage-audit.witness.json`.

Reverted in full (`git checkout -- .`, removed the untracked sidecars and the
witness), then redid only the 7 sanctioned `qa-sweep` blocks.

## Two defects, and the second is the worse one

1. **The path argument is ignored** — a caller who scopes the run gets a
   corpus-wide rewrite. This is a mass-refresh, which AGENTS.md §4 forbids
   ("cap ≤ 10 sidecars / ≤ 3 witnesses per idle pass"; "Never mass-refresh").
   The tool makes the forbidden operation the *default* and gives no way to opt
   out.

2. **It audits vendored Mathlib.** The run reported findings against
   `content/quantum-observable-universe/lean/.lake/packages/mathlib/Mathlib/Algebra/CharP/*.lean`
   — e.g. *"wall-base-ring-minimal … Algebraic-side field/inverse marker"* — and
   said "…and 1474 more". `.lake/packages/` is a build artifact holding a
   third-party dependency; auditing it is meaningless and it inflates every
   count the witness reports.

## Why this matters beyond the annoyance

`q-usage-*` is the **largest stale-script family in the corpus** — 7 criteria ×
~1035 blocks ≈ 7,245 of the 42,873 stale script criterion entries (~17 %). And
**`qa-sweep` does not run them**: sweeping a block emits 0 mentions of
`q-usage`, and the criteria stay stale afterwards (verified on `why-b3`:
7 stale before a full sweep, 7 stale after).

So the AGENTS.md §4 instruction — *"refresh by … running `qa-sweep`"* — **cannot
drain 17 % of the backlog**, and the only tool that can is the one that ignores
its scope argument. That is the actual gap.

Note two writers exist for this family: `script:q-usage-audit` (6,188 entries in
a 900-sidecar sample) and `script:content/pipeline/qa-checkers-q-usage.ts` (7).
Why the pipeline checker wrote only 7 is not established here.

## Fix

Honour the path argument, and exclude `.lake/` from the walk. Until then, do
**not** run `q-usage-audit.ts` to drain a block — it is a corpus-wide operation
wearing a per-file interface.
