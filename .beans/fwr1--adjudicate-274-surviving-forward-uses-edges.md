---
# fwr1
title: 'adjudicate the 274 surviving same-chapter forward uses[] edges'
status: completed
type: task
priority: normal
created_at: 2026-08-09T20:40:00Z
updated_at: 2026-08-09T21:35:00Z
---
**Outcome: 274 edges adjudicated — 236 `ordering`, 32 `spurious`, 6 `foreshadow`.**

Two passes. Eight reviewers adjudicated all 274; four adversarial verifiers then
re-reviewed the 58 destructive verdicts (deletions and exemptions — `ordering`
changes nothing and needs no defence). The second pass overturned **20 of 58**:

| | first pass | upheld | rejected |
|---|---|---|---|
| `spurious` (deletes an edge) | 35 | 32 | 3 |
| `foreshadow` (exempts it permanently) | 23 | 6 | 17 |

The foreshadow rate is the finding. Two reviewers used "the block names the
later target and cites it" as the bar; `BlockBase.foreshadows` requires the
prose to *frame the reference as deferred*. In `predicted-spectra` the citation
syntax does not distinguish backward from forward at all — one block cites a
target 10 positions back and one 60 positions forward in a single sentence with
identical parentheses — so naming carries no deferral signal and all ten of that
slice's declarations fell. Every survivor is a first-person hand-off ("we
establish this in X", "we work this out separately"). The sharpened rule, plus
the false-locator and mis-aimed-deferral traps, is now written into
`skills/folio-core/uses-editorial-review.md` upstream.

Verified: `uses[]` graph still acyclic (0 cycle failures over 3424 blocks);
`run-validate` ✓ Valid with the same 5 pre-existing issues; forward-ref count
274 → 236, matching the reconciliation exactly.

Follow-ups: `fwr2` (block moves), `fwr3` (transpositions), `fwr4` (mass-theory
long-range structure), `fwr5` (completeness gaps the review turned up).
Branch: `claude/uses-forward-ref-editorial-review-2026-08-09`

After the cycle-breaking work took the `uses[]` graph acyclic,
`detangler-no-forward-ref` still reports 274 same-chapter forward edges across
238 blocks in 19 chapters. These are not mechanically decidable — an earlier
pass established that a text heuristic misclassifies roughly half of them in
both directions — so this is the `uses-editorial-review` skill applied per edge,
reading each block's `.md` as a reader would.

Each edge gets one of three verdicts:

- **foreshadow** — the prose explicitly defers to the target (preview, promise
  to return, explicitly deferred result). Declare it in `foreshadows[]`; the
  edge stays in `uses[]` and stops being a finding.
- **spurious** — the prose never leans on the target. Drop the entry from
  `uses[]`.
- **ordering** — the reader genuinely needs the target first and it comes
  later. Leave it alone; it is a real ordering defect and a reorder decision
  for the owner, not something to paper over.

Bias is deliberately asymmetric: `spurious` requires positive evidence of
absence, `foreshadow` requires a verbatim quote of the deferral, and everything
else stays `ordering`. Deleting a true editorial edge silently corrupts every
ordering metric computed from the graph, and nothing downstream catches it.

Verdicts are cross-checked against the actual working-tree diff before commit —
an agent's self-report is not evidence that the edit it describes was made.
