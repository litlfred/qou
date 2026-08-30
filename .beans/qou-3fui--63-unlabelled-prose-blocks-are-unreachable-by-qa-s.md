---
# qou-3fui
title: 63 unlabelled prose blocks are unreachable by qa-sweep
status: completed
type: bug
created_at: 2026-08-16T02:28:07Z
updated_at: 2026-08-16T02:28:07Z
---

Audit: `docs/audits/2026-08-16-unlabelled-prose-coverage.md`.

Chapter manifests list **3571** slugs; `walkBlocks` yields **63 fewer**. Every
one of the 63 is listed in a chapter (so it renders into the paper), calls
`prose(...)`, has a `.md` narrative — **27,390 words** across them — and carries
a `.qa.json` sidecar.

They are the connective tissue: `outro-*`, `intro-*`, `chapter-overview`,
`authors-note`, `notation-register`, `definition-index`.

## Why

`readBlockManifest` requires a `label:`, and these genuinely have none —
`prose(data?)` makes it optional, so the runtime block has no label either.
Excluding them from the **dependency graph** is right; a block with no label
cannot be a node. But `walkBlocks` is also *every checker's* enumeration, and
`qa-sweep.ts` iterates it.

## The part that looks like coverage and is not

All 63 sidecars were written by a one-off bulk pass —
`chore(qa-sweep): populate trap-* sidecar entries across 3065 prose blocks`
(2026-08-15) — which enumerated differently from the sweep. Since `qa-sweep`
iterates `walkBlocks`, **nothing can refresh them.**

Right now their `source_hashes` match, so they read as current. The moment any
of those 27,390 words changes, the sidecar goes stale, no sweep will ever update
it, no criterion runs on the new text, and the block still shows a populated
`.qa.json`.

Same signature as `mcp1`, `pzdv` and `9giz`: an absent check indistinguishable
from a passing one.

## Not fixed here, because it is a design decision

1. **Label the 63.** 63 content edits; they become ordinary swept blocks, and
   gain graph identity they arguably should not have — nothing references a
   chapter outro, and a label invites `uses[]` entries pointing at connective
   tissue.
2. **Let `walkBlocks` yield unlabelled blocks** under a synthetic id. One
   platform change, no content edits — but subjects 27,390 words to every
   criterion at once, so the next sweep produces a large batch of findings on
   prose nobody has been checking.
3. **Split the enumeration** — `walkBlocks` stays label-only for the graph,
   `qa-sweep` gets a wider walk. Most honest to the two different questions;
   most work.

Option 2 is the smallest change and the loudest; option 1 the largest and
quietest. The number to weigh is how much of those 27,390 words is prose a
criterion would actually have an opinion about — that is worth measuring before
choosing, and is not measured here.

## How this was found

By asking the complement of the question that produced folio-assistant `#125`.
That one found `walkBlocks` **admitting** a non-block (an audit script with
manifest source in a template literal, walked as `prop:x`). This asks whether it
**misses** real ones. Both directions were worth checking; only one had been.

## 2026-08-16 — fixed in folio-assistant #127, and my prediction was wrong

Option 3 taken: `walkBlocks(root, { includeUnlabelled })`, default **false** so
the dependency graph is unchanged, and `qa-sweep` opts in. Unlabelled blocks are
yielded under their **slug** — the identity these sidecars already use, so the
sweep can now maintain files that already exist in exactly that shape.

**The prediction in this bean was wrong.** I wrote that widening the sweep was
"the smallest change and the loudest", on the assumption that 27,390 unchecked
words would produce a large batch of findings. Measured across the 63:

| | |
|---|---|
| applicable criterion runs | **1286** |
| skipped by `applies_to` | 819 |
| **failures** | **0** |

Cheap *and* quiet. The prose was clean; it could not be seen to be. Had I
weighed the options on the guess rather than measuring, the argument would have
pointed at the expensive one.

A first attempt measured **126** failures and would have supported the guess.
That was my error: I called the checkers directly and bypassed the `applies_to`
filter `qa-sweep` applies, so `compute-prop-has-probe` and `-has-consumer` fired
on prose that is not a proposition. The lesson is the one this whole arc keeps
producing in a new costume — a measurement taken through a different path than
the real one answers a different question.

Status: **completed**. The sidecars for these 63 are now refreshable, and the
next sweep will do it.
