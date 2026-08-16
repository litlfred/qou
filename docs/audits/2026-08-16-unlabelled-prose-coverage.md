# 63 prose blocks are in the paper, have QA sidecars, and cannot be swept

Generated 2026-08-16. Bean `qou/3fui`. **Nothing is changed by this document** —
the fix is a design decision, described at the end.

## What was measured

Chapter manifests list **3571** block slugs. `walkBlocks` — the enumeration every
per-block QA criterion runs on, and the one `qa-sweep` iterates — yields **63
fewer**. Every one of the 63:

- is **listed in a chapter manifest**, so it renders into the paper
- has a `.ts` on disk that calls **`prose(...)`**
- has a **`.md` narrative** — 27,390 words across the 63
- has a **`.qa.json` sidecar** carrying criteria results

They are the chapter connective tissue: `outro-*`, `intro-*`,
`chapter-overview`, `authors-note`, `notation-register`, `definition-index`.

## Why they are skipped

`readBlockManifest` requires a `label:`. These files do not have one:

```ts
import { prose } from "../../schema/builders";

export default prose({
  title: "Chapter close — Braids and Knots",
});
```

That is not a parse failure — the label is genuinely absent, and
`prose(data?)` makes it optional, so the runtime block has no label either.
Without one a block cannot be a node in the dependency graph, so excluding it
from the graph is right.

The problem is that `walkBlocks` is not only the graph's enumeration. It is
*every* checker's enumeration.

## The part that looks like coverage and is not

All 63 carry sidecars, written by a one-off bulk pass —
`chore(qa-sweep): populate trap-* sidecar entries across 3065 prose blocks`
(2026-08-15) — that enumerated differently from the sweep.

`qa-sweep.ts` iterates `walkBlocks`. So **nothing can refresh these sidecars.**
Today their `source_hashes` match the files, so they read as current. The moment
any of those 27,390 words changes:

- the sidecar goes stale and no sweep will ever update it,
- no criterion will run on the new text,
- and the block still shows a populated `.qa.json`, which is what a reader of
  the QA state sees.

That is the recurring shape in this codebase — an absent check that is
indistinguishable from a passing one. It is the same signature as `mcp1` (a
mis-parse that returned `pass`), `pzdv` (gates over an empty corpus) and `9giz`
(a stale ref that reported zero drift).

## RESOLVED 2026-08-16 — folio-assistant #127, option 3

`walkBlocks(root, { includeUnlabelled })`, default **false** so the dependency
graph is untouched; `qa-sweep` opts in. Unlabelled blocks are yielded under
their slug, the identity their sidecars already use.

**The prediction below was wrong and is left standing as written.** Measured
across the 63: **1286 applicable criterion runs, 819 skipped by `applies_to`,
and 0 failures.** Cheap *and* quiet — the prose was clean, it simply could not
be seen to be. Weighing the options on the guess instead of the measurement
would have argued for the most expensive one.

(A first attempt measured 126 failures, which would have supported the guess.
That was an error: the checkers were invoked directly, bypassing the
`applies_to` filter `qa-sweep` applies, so two compute criteria fired on prose
that is not a proposition.)

## The decision, as originally written

Three ways out, and they are not equivalent:

1. **Give the 63 blocks labels.** 63 content edits. They become ordinary blocks,
   swept and checkable, and gain graph identity they arguably should not have —
   nothing references a chapter outro, and a label invites `uses[]` entries
   pointing at connective tissue.
2. **Let `walkBlocks` yield unlabelled blocks** under a synthetic id. One
   platform change, no content edits — but it subjects 27,390 words to every
   per-block criterion at once, and the first sweep after it will produce a
   large batch of findings on prose nobody has been checking.
3. **Split the enumeration**: keep `walkBlocks` label-only for graph purposes,
   and give `qa-sweep` a wider walk that includes unlabelled prose. Most honest
   to the two different questions being asked, and the most work.

Option 2 is the smallest change and the loudest; option 1 is the largest change
and the quietest. Neither should be chosen on convenience — the number to weigh
is how much of those 27,390 words is prose a criterion would actually have an
opinion about.

## Re-derive

The `walkBlocks`-versus-manifest comparison is three lines over
`parseManifestStringArrays(chapterSrc, "blocks")`; there is no script for it
because it should not need to be run twice — either the enumeration is fixed or
this document explains why it was not.
