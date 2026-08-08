---
# qou-med65
title: 'TASK: the 65 MED wall-side blocks — [LinearOrderedField R] vs ℝ, per block'
status: todo
type: task
priority: medium
tags: [lean, wall-side, 7c]
created_at: 2026-08-08T13:00:00Z
updated_at: 2026-08-08T13:00:00Z
---

The largest remaining `wall-side-correct` class. MED = the Lean carries
**ordering / `abs` / `linarith` only** — no `Real.*`, no `Complex`, no integral.
For many of these a `[LinearOrderedField R]` restatement is possible; for others
the ordering is on a genuinely measured quantity. It is a per-file call.

Now **67**: `demazure-fiber-markov-trace` and `mass-endomorphism-tower` move in
from WEAK — both carry `q > 1` in code, which #4709's ordering regex missed
because it matched `0 <`, `≤`, `abs`, `linarith`, `positivity` and **not bare
`>` / `<`**.

## Read protocol — learned the hard way, follow it

1. **Strip comments first.** Regexes over raw text match inside docstrings and
   identifiers (`deriv` inside `derivedLightIsotopeFormula`, `Real` inside
   `Mathlib.Data.Real.Basic`).
2. **Read the IMPORTS.** They are more decisive than the signature. A statement
   that looks generic (matrix idempotence; an additive decomposition) still
   needs `ℝ` if the proof runs the spectral theorem or the file imports
   `Analysis.*`/`Topology.*`.
3. **Read the file's own docstring.** Twice this session it named the exact
   missing condition (`"base ring of characteristic ≠ 2"` → the target was
   `[Field R] [CharZero R]`, not plain `Field`).
4. **Ask what the quantity MEANS.** A measured value, a hyperbolic volume, a
   norm, or a time parameter is `ℝ` by meaning — that is a §7c *note* on the
   referring block, not a Lean change.
5. **The verdict is a compile result, never a read.** Attempt the port; let the
   compiler adjudicate.

## Where the §7c note goes

On the **referring block's** `.md` / `.ts` `authorNotes` — never the `.lean`
docstring, which the checker does not read (#4703). Pattern: see the 21 notes
added in #4745.

## Baseline

`bun run scripts/check-wall-side.ts --sweep content/quantum-observable-universe`
was **1091/1188** after #4739. Re-measure before and after; do not quote a
stale number.

## Sizing

65+ per-file judgements. Batch into PRs of ≤ 49 files (the review limit) and
land incrementally. Do NOT bulk-generate acknowledgements to clear the count —
that clears the number while deciding nothing, which is the §1a audit-dodge the
whole queue exists to prevent.
