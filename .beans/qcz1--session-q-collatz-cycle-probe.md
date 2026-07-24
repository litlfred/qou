---
# qcz1
title: 'Session: q-Collatz status — content-bearing class, no-cycles re-scope, cycle census'
status: in-progress
type: milestone
priority: medium
created_at: 2026-07-18T21:14:00Z
updated_at: 2026-07-24T15:48:40Z
---

Branch claude/q-collatz-status-1v0pxv, PR #3996 (open, mergeable_state=clean,
sorry-free verified, no CI blockers). Scope is UNIQUE — no sibling PR touches
Collatz (checked 30 open PRs 2026-07-24).

DONE:
- (qcz2) content-bearing QCollatz class, fabricated instance dropped (closes cj317 dodge).
- no-cycles proof re-scoped to A=1 balanced sub-case + audit 2026-07-18.
- exact cycle census period<=18: only {q^-1,1+q^-1} (q-lift {1,2}) and -q^-2 (q-lift -1);
  no nontrivial positive cycle. computations/qcollatz_cycle_census.py + witness.
- domain finding: unknot 1 is NOT in C_q domain; true attractor is the 2-cycle.

COORDINATION (b9cj epic): PR #4007 excluded QCollatz from its mechanical
instance:=sorry restore, deferring to this content-bearing rework. OPEN epic
decision: template A (instance:=sorry) vs template B (content-bearing, no
instance, this PR). Owner-level call; non-blocking for #3996.

REMAINING: qcz3 (content clarification), qcz4 (divergence probe), qcz5 (template
coord + optional census extend). Post-merge: collatz-no-cycles-proof.qa.json
sidecar re-stales after the .md re-scope (main regen'd at 68736287) — refresh in
prepare-merge.
