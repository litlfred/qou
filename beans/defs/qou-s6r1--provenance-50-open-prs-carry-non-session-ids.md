---
# qou-s6r1
title: 'Provenance: 50 open batch PRs carry PR-body session links that are not claude.ai session ids'
status: todo
type: task
priority: normal
parent: qou-c20n
created_at: 2026-11-20T09:30:00Z
updated_at: 2026-11-20T09:30:00Z
---

Found by the 2026-11-20 session review (W6, `docs/coordination/2026-11-20-session-review.md`).

Measured from the open-PR list (412 open, REST, 2026-11-20 08:13Z): the `claude.ai/code/session_…` link in the body of
**48** open batch PRs (#8157 … #8510, heads `feat/qou-*` and `claude/qou-rtxm-*`) is `session_01E667391F74184786BF4B9D`,
and #8144 (`claude/round46-q-10v9-4`) carries `session_012EE90758AE4945AC814D43` (also on merged #8044, #7985). Both are
24 uppercase hex characters, not the base-58 `01…` form of every real session id on main (287 ids, all of that shape).
#8139 carries `session_01R46Ni4bTqcpColourTowerCP`, a readable word, not an id.
No commit on main carries any of the three. So the PRs cannot be traced back to a session transcript.

Owner workstream: w4 (batch PRs) for the 49, w5 for #8139. Mechanical: record the true producing session (or "unknown")
in each PR body or in the w4 triage table; do not invent one. No content change.
