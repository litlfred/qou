---
# hnd7
title: 'Handoff: agent-3702 QA drain — takeover status (f-bor + residual fails)'
status: todo
type: task
priority: normal
created_at: 2026-07-12T22:24:33Z
updated_at: 2026-07-12T22:24:33Z
---

Handoff bean for the stalled agent-3702 QA-drain session. Branch:
`claude/agent-3702-stalled-assessment-wwrei2`, pushed clean at
`2f4155be` (working tree empty; all sub-agent batches committed).

## Done (committed + pushed on this branch)

- **Molecular / mass / braids sub-agent:** completed — 7 QA fails fixed.
- **Brings / UGB sub-agent:** hit its session limit but reported
  near-completion; its working-tree edits were verified present and are
  committed in the batches on this branch.

## Remaining (for the takeover agent)

1. **`f-bor-borromean-observable`** (braids-and-knots) — fell through the
   sub-agent assignment (in braids-and-knots scope but not named in any
   agent's block list). Not fixed. Start here.
2. **Residual-fail enumeration** — the Brings/UGB agent self-reported
   "near-complete", not complete. Re-run the sweep to get the live fail
   list rather than trusting the report:
   `bun run content/pipeline/qa-sweep.ts <path> --only <crit>` per block,
   or `/integration-audit` for a whole axis. Treat any block it flags in
   brings-surface / unital-groebner-bases as possible leftovers from the
   truncated session.

## Notes

- Base is clean: takeover agent can branch from or continue
  `claude/agent-3702-stalled-assessment-wwrei2` directly.
- Prior related drain bean `z4no` (clarity-defterm-bold, 2026-06-26) is
  completed and unrelated to this pass — do not reopen.
