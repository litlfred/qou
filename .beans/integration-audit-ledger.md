---
# integration
title: ""
status: completed
type: task
priority: normal
created_at: 2026-06-21T12:22:34Z
updated_at: 2026-06-21T19:39:07Z
---

### 2026-06-21T12:20Z — proof
- reason: manual user invocation of /integration-audit proof
- scope: 2146 sidecars scanned
- entries invalidated: 19856 script-reviewer entries
- post-sweep delta: repopulated via qa-sweep
- next: /integration-backlog proof

### 2026-06-29T19:13Z — all (PR #3129, branch claude/integration-audit-qa-params-ikp76z)
- reason: user request "swarm /integration-audit all to refresh agent and mechanical
  QA params that are stale or unpopulated", after heavy main churn (atomization /
  lean-orphan / binding-probe sweeps). Branch fast-forwarded to current main first.
  folio-assistant platform (host of integration-audit.ts + qa-sweep.ts post-miga)
  cloned direct from github.com (scoped proxy blocked it; direct egress allowed).
- scope: 2742 blocks scanned; 1618 affected; all 91 MECHANICAL criteria across 6 axes
  (voice / wall / q-usage / proof / canonical / compute / detangler / bib)
- mode: include_agent=FALSE — only kind:"script" entries invalidated+re-swept.
  kind:"agent" (31170) and kind:"human" (3) reviewer entries PRESERVED (0 lost,
  verified by per-file JSON entry-count diff HEAD~1 vs HEAD).
- entries invalidated: 83307 script-reviewer entries; repopulated via qa-sweep
- delta: 332 NEW sidecars created (were unpopulated) + 2410 refreshed
- fresh-sweep criticals (pre-existing content, not introduced):
  bib-cite-resolves 430, compute-witness-exists 215, wall-side-correct 34,
  canonical-cal4-acknowledged 2, proof-no-bare-sorries 1
- agent axis NOT run: 37 distinct agent-kind criteria report needs-agent over
  51247 block-criterion pairs; qa-sweep cannot fill these (needs agent dispatch).
- agent-review model attribution (latest fresh agent entry per block-criterion,
  21409 fresh total): claude-opus-4-8 = 2898, gemini-3.1-pro = 71,
  claude-opus-4-7 = 62, no model recorded = 18378 (older drain runs pre-dating
  the agent_model stamp). 5732 agent entries are stale (source moved under them).
- next: /integration-backlog <axis> to refresh the agent axis (append-only).
