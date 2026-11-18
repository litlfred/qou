---
# qou-grph
title: qa-staleness never computes the `graph` hash, so all 9 graph-invalidated criteria are permanently stale by construction
status: in-progress
type: task
priority: high
tags:
    - close-candidate
    - reorg-2026-10-04
created_at: 2026-08-29T16:10:00Z
updated_at: 2026-10-04T15:15:02Z
parent: qou-5vkl
---

Found while draining `qou-g7z6`. Running `qa-sweep` over the
`mass-endomorphism` chapter moved the detangler family the WRONG way —
279 stale occurrences before, **1,134** after — while everything else
improved by 1,742. The regression is not a regression; it is a detector
that cannot report these criteria fresh under any circumstances.

## The mechanism, confirmed end to end

1. Nine criteria declare `also_invalidated_by: ["graph"]` —
   `detangler-no-forward-ref`, `-section-band`, `-no-xchapter-fwd`,
   `-archimedean-wall`, `-block-tanglement`, `-graph-energy`,
   `-topic-coherence`, `-no-dependency-cycle`, and
   `foreshadows-point-forward`.
2. `freshnessKeys(def)` returns `depends_on ∪ also_invalidated_by`, so
   for these it includes `"graph"`.
3. **`qa-sweep.ts` computes it**: imports `usesGraphHash` (line 129),
   calls it once for the walk root (line 286), and for
   `freshnessKeys(def).includes("graph")` writes the extra key into the
   entry's `field_hash` (lines 388–393). Verified on disk — a swept
   detangler entry carries
   `field_hash: {md, ts, lean, lean_statement, graph: "8dc1e98508e1"}`.
4. **`qa-staleness.ts` does not.** The string `graph` appears in that
   file **zero times**. It builds `const current = hashBlockFiles({md,
   ts, lean})`, with no `graph` key, and calls
   `summariseFreshness(report, current)`.
5. `entryIsFresh` then iterates `k = "graph"` and hits

       if (expected && !actual) return false; // file removed since audit

   `expected` is the hash the sweep just wrote; `actual` is `undefined`.
   Every such entry is read as *"the file was removed since the audit"*.

**9 criteria × 126 blocks = 1,134**, which is exactly the post-sweep count
measured. The arithmetic closes.

## Consequences

- **The detangler bucket cannot be drained by any number of sweeps.** A
  freshly-written, correct verdict is reported stale immediately.
- **Its count is not a backlog signal.** Any "N stale" figure for this
  chapter is inflated by 1,134 and always will be; a corpus-wide figure is
  inflated by 9 × (number of blocks).
- A reader comparing before/after a sweep sees the detangler family
  quadruple and reasonably concludes the sweep broke something. It did
  not: spot-checked at the entry, `detangler-no-forward-ref` moved
  `fail -> pass` on a genuine re-evaluation and `foreshadows-point-forward`
  went from ABSENT to a real `n/a`.

## The fix, and where it has to land

`qa-staleness.ts` should mirror what `qa-sweep.ts` already does: import
`usesGraphHash` from `./uses-graph-hash`, compute it once for the walk
root, and include `graph` in the `current` field-hash it passes to
`summariseFreshness`. A few lines, and the two tools then agree.

**It cannot be done from this repo.** `folio-assistant/` here is a symlink
to a sibling checkout and is gitignored (`.gitignore:10`); the file lives
in `litlfred/folio-assistant`, which is outside this session's repo scope.
Whoever picks this up needs that repo attached.

**Do not "fix" it on the qou side** by hand-editing sidecars, dropping the
`graph` key from entries, or removing `also_invalidated_by: ["graph"]` from
the registry. The graph dependency is correct — a detangler verdict really
is invalidated when the `uses[]` graph changes, which is why the sweep
records it. The defect is only that the *other* tool never learned to
compute it.
