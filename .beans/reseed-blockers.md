# reseed-lake-cache-qou-v4-24-0
title: Reseed lake-cache/qou-v4-24-0 (currently zero-QOU-content defect, bean 5d7z)
status: blocked
type: task
---

## State (2026-08-21)
- Production `lake-cache/qou-v4-24-0` is the DEFECTIVE cache: 7268 oleans,
  ALL dependencies, ZERO QOU.* content + trace-less (hand-seeded via legacy
  scripts/lean-olean-cache-seed.sh). The service seed guard would refuse it.
- Toolchain v4.24.0 / mathlib pin f897ebcf UNCHANGED → slug still qou-v4-24-0,
  mathlib oleans still valid at pin.

## Proper reseed = real `lake build QOU` (trace+ir complete) → service seed
`folio-assistant/scripts/lake-cache.sh seed --lake-root content/quantum-observable-universe/lean \
  --package qou --branch lake-cache/qou-v4-24-0 --push`
Guards enforce it: refuses zero-own-package oleans AND <90% trace coverage.

## Why it CANNOT be done from the web sandbox (two HARD env blocks)
1. Authoritative CI path `.github/workflows/lake-cache-refresh.yml` (workflow_dispatch,
   package=qou) — the agent integration lacks actions:write → 403
   "Resource not accessible by integration". OWNER must dispatch.
2. Local build needs a trace-complete mathlib base first:
   - `lake exe cache get` → 403 CONNECT-tunnel firewalled on every shard (7335).
   - Restoring a service-seeded branch → the ~1GB split-tar branches time out
     even to `git ls-tree`; a from-source mathlib build (5000+ modules) exceeds
     sandbox lifetime.

## Owner handoff (one action)
Dispatch the workflow (runners are NOT firewalled; `cache get` works there):
  gh workflow run lake-cache-refresh.yml -f package=qou   # (or Actions UI → Run workflow)
Requires repo Actions billing active (auto-triggers were disabled 2026-06-30;
this workflow has never run — total_count 0).
Alternatively: run the seed locally in any env where `lake exe cache get` is
reachable, then the lake-cache.sh seed line above.
