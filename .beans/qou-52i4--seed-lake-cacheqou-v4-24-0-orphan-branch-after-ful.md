---
# qou-52i4
title: Seed lake-cache/qou-v4-24-0 orphan branch after full build (preserve for next agent)
status: in-progress
type: task
created_at: 2026-07-13T15:55:00Z
updated_at: 2026-07-13T15:55:00Z
---


## Claimed 2026-08-08 — branch `claude/sorry-audit-joo5`, PR #4785

This container holds exactly what 9h6x says the reseed needs: a tree produced by
real `lake build` runs, so the `.trace` files exist.

`lake-cache.sh status` here:

```
oleans:  4459  (deps + own)
own pkg: 888
traced:  4459/4459 oleans  (100%)
```

Against the incumbent `lake-cache/qou-v4-24-0`, as recorded in
`folio-assistant/scripts/lake-cache.sh`'s own comments and bean 9h6x:

| | incumbent | candidate |
|---|---|---|
| oleans | 7268 | 4459 |
| **own `QOU.*` oleans** | **0** | **888** |
| traces | 775 (~11%) | **4459 (100%)** |

The candidate is smaller in raw dependency count and better on both dimensions
that decide whether a cache does anything: it carries the paper's own modules
(the incumbent carries none — the exact defect `cmd_seed`'s `own == 0` guard was
written for) and every olean has its trace, so Lake honours rather than evicts
them.

**Expected obstacle:** `would_shrink()` refuses a candidate below 90% of the
incumbent's olean count, and 4459 < 0.9 × 7268. That guard is right in general
and wrong here — it would block the fix for the defect it was written to catch,
because it counts oleans without asking whether Lake will trust them. Resolving
that (a `--force` with the reasoning recorded, or a guard that weights traced
oleans) is the decision this bean now turns on; not forcing it silently.
