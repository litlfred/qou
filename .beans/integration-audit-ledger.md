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

### 2026-07-02T12:25Z — compute-witness-exists + 5 path-anchored criteria (checker-environment fix)
- reason: false-positive class found during /integration-backlog compute — `qa-checkers-extended.ts` anchors `REPO_ROOT` at the platform clone (post-miga), so `computations/*.witness.json` lookups and the I1/I2 audit maps (`computations/audits/i{1,2}-*.witness.json`, checker path also missing the `audits/` segment) all missed. Env-level fix: symlinks in the local folio-assistant clone pointing `computations/` + I1/I2 paths back into the qou checkout; durable fix belongs in folio-assistant (REPO_ROOT env override + audits/ path) — out of this session's push scope, flagged for a platform session
- scope: 2686 blocks; 12697 script entries invalidated across 6 criteria; qa-sweep repopulated
- post-sweep delta (latest-entry open fails): compute-witness-exists 218 → 5; compute-lp-dual-present → 1; canonical-witness-pinned 28 → 0; canonical-script-not-deprecated → 0; compute-prop-has-probe 147 → 150; compute-prop-has-consumer 147 → 150 (I1/I2 audit map now authoritative instead of heuristic fallback)
- overall open fails: 2527 → 2300
- next: drain the genuine compute backlog (306 items) per /integration-backlog compute
