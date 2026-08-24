---
# qou-efzm
title: '5 orphan QA sidecars: one block missing its .ts, four with no block at all'
status: completed
type: task
priority: normal
created_at: 2026-08-23T17:51:01Z
updated_at: 2026-08-24T13:24:05Z
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

## Resolved 2026-08-24 — and item 2 was misdiagnosed

### Item 1 — fixed on `main`, not by me

`content/quantum-observable-universe/mass-theory/q-clt-jsj-mass-scaling.ts`
now exists. Someone wrote the manifest rather than deleting the leftovers,
which was the right call — the `.md` was live content.

### Item 2 — NOT orphans. They were never blocks.

This bean guessed: *"a tool once wrote a `section-title-audit` sidecar per
paper and the producing block was later removed (or never was a block)."* The
file shape settles it, and the guess was wrong in the way that matters.

A block sidecar opens `{"$schema": "block-qa/v1", "label": …, "kind": …,
"paths": …}`. These open:

```json
{ "criterion": "voice-section-title-coherence", "paper": "visualizer",
  "chapters": { "overview": { "manifest_hash": …, "machine": { … } } } }
```

Keyed by **paper and chapter**, with no `$schema` and no block anywhere in the
shape. And they are **live**: the producer is
`folio-assistant/content/pipeline/qa-section-title-audit.ts`, with entries in
`qa-criteria-registry.ts` and the `local/one-voice-audit` skill behind it.

So the remedy the error message advises — *"delete the sidecar (git history
keeps it)"* — would have destroyed live audit state that the tool rewrites on
its next run. Had I executed this bean as written, that is what I would have
done.

### What was actually fixed

`folio-assistant@8835ee6`: `no-orphan-sidecar` now discriminates on the block
sidecar's own `$schema` (`isBlockSidecar`), so a paper-level artefact sharing
the `.qa.json` extension is not read as an orphaned block.

Unparseable returns **true** on purpose — a corrupt sidecar should be
reported, and treating unreadable as "not a block's" would let a real orphan
hide behind a truncated write.

Three tests; two fail against the unfixed checker, verified by stashing the fix
rather than assumed. The third pins the failure direction of the helper.

### Why these escaped notice

The check is **non-recursive** and these live at the paper root, not in a
chapter dir — so they were never flagged, only counted. That is luck rather
than design, and it is why the bean's "invisible to block-first measures but
present in sidecar-first denominators" framing was right about the *symptom*
while wrong about the *cause*.
