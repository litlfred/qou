---
# qou-efzm
title: '5 orphan QA sidecars: one block missing its .ts, four with no block at all'
status: completed
type: task
priority: normal
created_at: 2026-08-23T17:51:01Z
updated_at: 2026-08-30T02:37:07Z
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


## Corrected + partly closed 2026-08-29

**This bean named the wrong block.** `mass-theory/q-clt-jsj-mass-scaling` **gained its `.ts`** in
`6d4bb17ccc` ("restore two manifests the bulk import dropped") — fixed by a sibling. The surviving
`.md`-without-`.ts` case is `lean/AUDIT-REPORT`, which I dismissed at the time as a stray
non-block path; it is the same orphan class.

Remaining: 4 × `*/section-title-audit` (neither sibling) + `lean/AUDIT-REPORT`. See [docs/audits/2026-08-29-rsk-plancherel-arc-currency-review.md](docs/audits/2026-08-29-rsk-plancherel-arc-currency-review.md) §4.


## Resolved 2026-08-30 — 4 deleted, 1 deliberately kept

Owner instruction: delete the orphan sidecars. Done for **4 of 5**; the fifth is not an
orphan and deleting it would have destroyed data.

**Deleted (4)** — `*/section-title-audit.qa.json` in `bach2013-double-slit`,
`fred2005-formal-groups`, `unital-groebner-bases`, `visualizer`. Neither a `.ts` nor an
`.md` sibling, and **0 criteria each** — empty files with no block behind them.

**KEPT: `quantum-observable-universe/lean/AUDIT-REPORT.qa.json`.** It is not in the same
class. It has an `.md` sibling (a Lean formalization audit report), and it carries **10
criteria, every one an agent/human verdict**, including a substantive
`trap-superlative` **fail** with cited evidence. Deleting it destroys 10 adjudications
that only an agent can produce and that the sidecar system exists to preserve.

Its actual defect is narrower than 'orphan': a `.md` with no `.ts` manifest, so
`qa-sweep` reports `root not found` for it. Two honest dispositions, neither taken here:
give it a `.ts`, or accept that a working audit document under `lean/` is not a content
block and should not have acquired a sidecar. Owner call.
