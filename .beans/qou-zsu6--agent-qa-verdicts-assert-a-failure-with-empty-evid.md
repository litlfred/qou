---
# qou-zsu6
title: 'Agent QA verdicts assert a failure with empty evidence: 275 live, 304 permanently unanchored'
status: completed
type: task
priority: normal
created_at: 2026-08-25T06:14:19Z
updated_at: 2026-08-25T07:42:00Z
---

## Measured (re-run: `bun run content/pipeline/qa-evidence-audit.ts`)

Of 3267 agent `fail`/`warn` entries in `content/**/*.qa.json`, **1302 carry no
evidence**. Bucketed by whether the entry can still be tied to the block it
judged:

| bucket | count | meaning |
|---|---|---|
| **live** | **261** (110 blocks) | block carries this failure NOW — needs re-adjudication |
| stale | 740 | superseded by a later block edit; history, no action |
| unhashed | 301 | no `field_hash` at all — never adjudicable (see `qou-pwut`) |

Live concentration is the devil's-advocate family — `da-referee-verdict` (98),
`da-lean-narrative-divergence` (74), `da-overclaim` (60) are **246 of 261
(94%)**. Whatever adjudication path those four `da-*` criteria run through
never records evidence; that path is the fix, not 261 individual judgements.

## DONE

- `qa-agent-entry.ts` exits 2 on `fail`/`warn` without non-empty evidence
  (9 tests, verified non-vacuous: 4 fail against the unguarded writer).
- `qa-evidence-audit.ts` + 9 tests makes the backlog re-measurable.
- PR #5745.

## OPEN — the 261

Re-adjudication of the live 261. Not attempted here: it is a genuine
drain, and the `da-*` path fix should land first or it will regenerate them.

## Corrects the prior session's report

A prior session measured this and its container was reclaimed before it
committed; its work was lost entirely and was redone here. Its figures do not
reproduce:

- It reported **303 empty / 1442 fail-warn**. Measured: **1302 / 3267**, or
  **261** live. Its scope was some narrower slice.
- It named `expo-milnor-clarity` (210/210) *"the single highest-leverage item
  left"*, on the theory that 210 blocks carry an unexplained major failure.
  **209 of the 210 are unhashed or stale; exactly 1 is live.** It is the
  lowest-leverage item, not the highest. The prior session flagged this exact
  check as worth doing ("worth checking first whether those 210 verdicts are
  even live") and did not do it.

## Limit

The agent clone is shallow (51 commits) and `git fetch --deepen` times out
against this remote, so no claim is made about WHEN any of this landed. All
figures are measured from the working tree.


---

## 🛑 RETRACTED (same session) — the verdicts are MISFILED, not silent. Corrected count: 0.

Everything above this line asserting that these verdicts "assert a failure and
say nothing" is **wrong**. Measured against the actual entries rather than key
presence:

| | count |
|---|---|
| agent fail/warn with empty `evidence` | 1302 |
| **…recording no reason under ANY key** | **0** |

All 1302 carry a substantive reason under `notes` (1302) and
`referee_argument` (97). Median 154 chars, only 4 under 40, citing file:line
as the schema asks — e.g. *"Referee verdict: open-objection. Lean sibling
.../molecular-braid.lean fails compilation: molecular-braid.lean:22:28:
error(lean.unknownIdentifier)"*.

**This is a schema-key mismatch, not an accountability void**, confined to one
writer family (reviewer id `local/qa-agent-drain`, which also emits `verdict` /
`agent_model`; it is neither `qa-agent-entry.ts` nor the ad-hoc scripts of
`qou-pwut`).

**How the error survived:** the finding was derived from key presence alone.
Nobody opened an entry — reading four overturned it. Every downstream number,
including all of mine above, inherited that.

## Revised OPEN item

NOT re-adjudication of 261 verdicts. The work is a **key migration**: move the
reason from `notes` to `evidence` for the misfiled entries, or amend the schema
to bless `notes` as a reason field for this writer. Far cheaper, and it does
not require re-judging anything.

The `da-*` concentration figure (246/261) stands as a *fact about which
criteria* are affected, but it no longer indicates a broken adjudication path —
that path records its reasoning correctly, just under the wrong key.

## What survives

- The `qa-agent-entry.ts` guard (PR #5745) stands on narrower grounds: the
  schema designates `evidence` as "what was found" and `notes` as "fix applied
  / scope note", so requiring `--evidence` on fail/warn keeps the canonical
  writer schema-correct and stops the misfiling spreading through it.
- `qa-evidence-audit.ts` now separates `misfiled` from `silent`; `--strict`
  gates on live-AND-silent (currently 0). Gating on `live` alone would have
  failed on 261 well-evidenced verdicts and been switched off within a day.


CLOSED by the qou-lqh3 migration: qa-evidence-audit now reports 0 empty-evidence
agent fail/warn entries, --strict exits 0. Schema conditional locking it in:
litlfred/folio-assistant#133.
