---
# qou-fx71
title: 'DEFECT: q-usage-audit.ts ignores its path argument and rewrites all 3573 sidecars'
status: completed
type: bug
priority: normal
created_at: 2026-08-30T12:08:48Z
updated_at: 2026-08-30T12:50:05Z
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


## FIXED 2026-08-30 — litlfred/folio-assistant#157

The file lives in the **platform repo**, not qou (`folio-assistant/` is a
symlink to a separate checkout; 0 files tracked here). Attached that repo and
fixed it there.

### Defect 1 restated correctly

This bean said the tool *"ignores its path argument"*. Accurate in effect, but
the precise fact is sharper: **it has no positional interface and never has
had one.** Scoping is `--paper` / `--chapter` only; `args` is read solely via
`.includes()` / `.indexOf()`. The defect is not a mishandled path — it is that
an unrecognised argument is **silently discarded**, so a caller who believes
they scoped the run gets the corpus.

Fixed by rejecting unknown arguments with **`EX_USAGE` (64)** — not 2, because
this tool already exits 2 for "no content repo found" and a caller must be able
to tell those apart. Argument validation also moved above
`findContentRepoRoot()`, so it runs before any filesystem work.

### Defect 2 confirmed, with a real number

`listPackageLeanFiles` walked `.lake/`. Measured on qou, identical invocation,
`--no-write`, fix off vs on:

    files scanned   10,444  ->  2,431
    .lake findings      80  ->      0

The 8,013 difference is exactly the count of `*.lean` under `.lake/` — **77 %
of the Lake root**. This bean's "…and 1474 more" was the visible tip.

### A wrong turn of mine, recorded because it nearly buried defect 2

My first comparison held `--paper` fixed and showed **0 `.lake` paths with and
without the fix**, which reads as a refutation. The control cell was broken —
the fix-off run never emitted a `lean-tree-scanned` line, so I compared a real
0 against a run that had not completed the orphan scan. Only the full 2×2
separated them. *A control that produces no output is not a control.*

### What this does NOT fix

`qa-sweep` still does not run the `q-usage-*` criteria (0 mentions in its
output; 7 stale before a full sweep and 7 after). This PR makes the corpus-wide
tool safe to invoke and stops it auditing Mathlib; it does not give `qa-sweep`
a path to those criteria, so the ~17 % of the stale-script backlog they
represent still needs `q-usage-audit.ts --paper <name>` run deliberately.
