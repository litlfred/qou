---
# qou-tv74
title: The six-path corpus-grep checklist cannot see .qa.json agent verdicts — a prior analysis of the UIC table sat there for four weeks
status: todo
type: task
created_at: 2026-09-19T07:18:29Z
updated_at: 2026-11-20T09:55:00Z
---


## Found 2026-09-19, by running `qa-sweep` rather than by searching

Hunting the producer of `tbl:unified-iterative-correction-table-data` (bean
`qou-ypq6`, PR #7439), the six-path checklist was run to completion and came
back empty. It stays empty -- nothing in the repository emits those seven rows,
and that negative is unaffected by this bean.

But the block's **own QA sidecar** already carried an independent analysis of
the same table, and **no path in the checklist can reach it.**

`content/quantum-observable-universe/mass-theory/unified-iterative-correction-table-data.qa.json`,
criterion `trap-superlative`, `reviewer.kind: "agent"`,
`reviewed_at: 2026-08-22T05:24:08Z` -- four weeks before the hunt. Its
`evidence` field reaches the same conclusion by a different route:

> The reference column is right and the fourth column is unexplained. ...
> the column headed `sum_lambda B_lambda` has no legend, and the proof block's
> algorithm ends "B_unified = sum_lambda cumulative_lambda", which would make
> it identical to the `B_unif` column - it is identical only in the D row
> (-16.45). For He-4 the two read 16.67 and -13.67. I tested the obvious
> alternative readings and none fits: `B_unif - B_AME` gives ... and
> `B_unif - B_dedi` fits no row.

It also independently establishes that `B_dedi` tracks AME to better than
0.5 % on every row, which the PR measured separately.

## Why the checklist misses it, structurally

The six paths are: (1) `docs/audits/`, (2) `content/`, (3) `computations/`,
(4) `docs/coordination/`, (5) `library/`, (6) `.beans/`.

Path 2 is `content/`, and the sidecar **is** under `content/` -- so this is not
a directory gap. It is a **file-type and grep-shape** gap:

- Every worked example of path 2 in AGENTS.md greps for a *topic string*. The
  sidecar's analysis is inside a JSON string field (`criteria.<crit>[].evidence`),
  one line, heavily escaped, and is keyed by a criterion name
  (`trap-superlative`) that has nothing to do with the subject matter.
- `grep -rln "unified iterative correction" content/` does not match it, because
  the evidence text says "the fourth column", "B_unif", "He-4" -- it never uses
  the block's own label.
- A criterion name is not a topic. Nobody greps `trap-superlative` when hunting
  a binding table, and the verdict is filed under a **voice/style** criterion
  while its content is a **numerical** analysis. That mismatch is itself worth
  noting: an agent verdict lands in whichever criterion invoked it, not in the
  one its content belongs to.

## Why this is worth recording rather than shrugging at

The checklist's whole purpose is to stop an agent declaring something open or
unexamined that the corpus has already worked. Here the corpus HAD already
worked it, in the one file most specific to the block, and the checklist
returned clean. The finding corroborated rather than contradicted -- but the
next instance may not.

Scope this as **(a) scope-limited**: measured on one block. Whether agent
verdicts in sidecars routinely carry substantive analysis, or whether this is
one unusual entry, is **not measured**. That is the first thing to establish.

## What is open

1. **How common is this?** Count `.qa.json` entries with `reviewer.kind:
   "agent"` and an `evidence` field over, say, 400 characters. That is a cheap
   scan and it decides whether this is a checklist gap or a curiosity.
2. **If common: does the checklist get a seventh path?** That is an AGENTS.md
   edit to a STRICT section and is the owner's call -- not an agent's. Do not
   edit the checklist on the strength of this bean.
3. **A cheaper alternative to a seventh path:** when working a specific block,
   read *that block's own* `.qa.json` first. It is one file, it is always the
   most specific artifact about the block, and it costs nothing. That habit
   would have caught this instance without widening the corpus-wide checklist
   at all.

Recorded in the block's `authorNotes` as well, so a reader of the table meets
it without needing this bean.

## Ported to the authoritative store 2026-11-20, and re-verified before porting

This bean existed only on the branch of PR #7439, which was closed on 2026-11-15
during the cleanup of PRs left by idle sessions -- its closing comment gives the
reason ("it edits content/ files that have since moved") and invites exactly this:
"If beans qou-5eg1, kjik and tv74 are still wanted, they can be ported to
beans/defs/ separately." The bean store is now the branch-mounted
`cat/cat-harness/beans`, which is gitignored on main, so this is a store write
rather than a repo commit.

Paths in the body above predate the `content/` -> `folio/` tree rename
(2026-09-27) and the `.beans/` -> `beans/defs/` move; read `content/...` as
`folio/...`. The findings themselves were re-checked against main at
`cacbddcffb1` and hold.

The two owner-selected fixes this bean carried are re-landed in
https://github.com/litlfred/qou/pull/8560.

**Re-verified 2026-11-20:** the block's own sidecar
(`folio/quantum-observable-universe/mass-theory/unified-iterative-correction-table-data.qa.json`)
still carries the `trap-superlative` entry with `reviewer.kind: "agent"`,
`reviewed_at: 2026-08-22T05:24:08Z`.

**Checked for a pre-existing carrier before porting, and found none.**
`qou-vstf` ("agent-kind QA verdicts are never recomputed") and `qou-4sdp`
("agent QA verdicts go stale in the FIXED direction") are the nearest beans and
are about **staleness** of agent verdicts. This bean is about **discoverability**
-- that no path of the six-path checklist reaches the `.qa.json` surface at all.
Related, not duplicate.

**One thing has changed and it widens the bean rather than closing it.**
`qa-sweep` at platform pin `82b389982` no longer writes the beside-the-block
sidecar; it writes `test/results/block-qa/` and `test/attestations/block-qa/`,
and the derived QA corpus lives on the `qa-reports` branch (`run-validate` says
so in a warning). So the surface this bean is about has partly moved OFF the
committed tree, where a grep of any kind cannot reach it. The bean's first open
item -- the scan that would decide whether agent verdicts routinely carry
substantive analysis -- now has to be run against that branch.

**Stays open** per rule 13a. It still deliberately does NOT propose a seventh
checklist path: that is an AGENTS.md STRICT-section change and the owner's call.
