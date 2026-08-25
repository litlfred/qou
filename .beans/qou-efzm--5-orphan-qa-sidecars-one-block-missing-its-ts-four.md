---
# qou-efzm
title: '5 orphan QA sidecars: one block missing its .ts, four with no block at all'
status: todo
type: task
priority: normal
created_at: 2026-08-23T17:51:01Z
updated_at: 2026-08-23T17:51:28Z
---

Exposed by the 236-block pin-bump sweep on PR #5561 (they were its only two
`qa-sweep` failures). **Pre-existing; neither is caused by the pin bump.**

## 1. A block with no manifest

    content/quantum-observable-universe/mass-theory/q-clt-jsj-mass-scaling
      .md        present
      .qa.json   present
      .ts        MISSING

`qa-sweep` exits 2 with `root not found` — a block is identified by its `.ts`,
so this one cannot be swept, and its sidecar can never be refreshed. The error
is a path check that runs before any checker logic, so it fails identically at
the old pin (inferred from the error's nature, not tested — verifying would have
meant moving the platform clone mid-sweep).

Either the `.ts` was deleted and the `.md`/`.qa.json` left behind, or it was
never written. Someone who knows the block should decide which.

## 2. Four sidecars with no block at all

Neither `.ts` nor `.md` exists for:

    bach2013-double-slit/section-title-audit.qa.json
    fred2005-formal-groups/section-title-audit.qa.json
    unital-groebner-bases/section-title-audit.qa.json
    visualizer/section-title-audit.qa.json

Same stem in four different papers, which suggests a tool once wrote a
`section-title-audit` sidecar per paper and the producing block was later removed
(or never was a block).

## Why it matters, mildly

These are invisible to every staleness measure that starts from a block and looks
for its sidecar — the 3616-sidecar / 376-stale / 51-really-stale figures on
`qou-zjfs` all count *from* the sidecar side and so include the 4 orphans in the
denominator. Small, but it means "N sidecars" is not "N blocks".

Not urgent. The fix is a decision (restore the `.ts` vs delete the leftovers),
not a sweep.
