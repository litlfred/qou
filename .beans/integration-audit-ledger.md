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

### 2026-07-02T12:05Z — stale-refresh sweep (all axes, no invalidation)
- reason: user invocation `/integration-audit all`, narrowed mid-run to "only refresh stale ones / populate new ones" — blanket script-entry invalidation was reverted; plain staleness-gated `qa-sweep` (91 criteria) run instead
- scope: 2686 blocks scanned; 2353 sidecars refreshed (append-mode, history + human entries preserved); 333 new sidecars populated
- staleness cause: platform checker drift — folio-assistant HEAD 109a4ffe (2026-06-29) vs last corpus sweep 2026-06-21 (script_commit_sha / deps_hash drift on nearly every script entry)
- sweep findings (newly evaluated): 488 critical, 188 major, 6 minor; needs-agent 51810
- post-sweep delta (latest-entry open fails): 1983 → 2527 (+544); top: bib-cite-resolves 412, da-referee-verdict 368, da-lean-narrative-divergence 354, da-reproducibility 302, compute-witness-exists 218
- next: /integration-backlog <axis>
