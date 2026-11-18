---
# qou-og83
title: 'bean-dangling-path-audit: five FP classes, one of them a bug in the extractor'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T06:36:36Z
updated_at: 2026-10-04T15:11:59Z
parent: qou-5vkl
---

**Unclaimed when the work was done — opened after the fact.** The script landed
2026-09-06 with no bean, and this correction was written before anyone noticed.
Recording that, per the work-plan policy, rather than backdating a claim.

**The finding, against my own tool.** The 2026-09-06 run reported **61 dangling
path references across 43 open beans** as if they were findings. Five further
false-positive classes were then found by running the audit on its own output.
After PR #6998: **47 across 35**, and **8 paths it called missing now RESOLVE**.

**Class 5 is a defect in this script, not a property of the beans.** The
extension alternation carried no trailing boundary, so `foo.tsv` matched as
`foo.ts`, `x.jsonl` as `x.json`, `y.pyc` as `y.py` — six findings manufactured
by cutting the last letter off a real path. The fix needs BOTH a longest-first
alternation AND `(?![\w])`: without the boundary `.tsv` truncates; without
`tsv` before `ts` the boundary makes it vanish instead.

**Class 6 (PIN-HIDDEN) is the reusable one.** A path can exist in
`folio-assistant` and be absent here because it was added AFTER
`.folio-assistant-pin` (`428ca5c`). `scripts/check-mirror-drift.ts` was added
in `ae0a979`. Sound test: `git -C folio-assistant log --all --diff-filter=A`.
This subsumed a heuristic "the bean says folio-assistant near the path" filter
that would have MISSED one of the three.

**A measured negative on scope, worth not repeating.** Class 8
(reported-absent) needs a text scope, and the first two candidates were both
wrong: a ±220-char window fires on **10/10** live catches (suppressing four
real `moved?` findings), and the enclosing **paragraph** also fires 10/10
because bean paragraphs run 257–1373 chars. The working unit is the
**soft-wrap-joined sentence**.

**And a negative about method.** `git log --all --diff-filter=A` cannot settle
whether a path ever existed here: the clone is shallow with 7 of thousands of
remote branches, so "0 adds" means "not in fetched history". Same error class
as the `qou-7br7` retraction.

**STILL OPEN — the 47 rows are untriaged.** This bean stays open for that. Two
sub-populations:
- **23 with a `moved?` marker** — mechanically fixable, but a bean is a record,
  so prefer a body-append over silently rewriting the path.
- **~22 with no relocation** — the informative half. Includes
  `computations/wenzl-y-lambda-h9/h12.witness.json`, whose bean claims it
  *"feeds six live nuclear consumers"* while it is not in the tree, and the
  `brings-surface/` + `climax-volume-mass/` `.lean` sweep lists in `qou-pqmw` /
  `qou-hxzl`. Those are real claims about files that are not there.

**Known unfiltered class:** PROPOSALS (the bean asks for the file to be
created), measured 2 of 35. No sound test; do not guess from an imperative verb.

PR: https://github.com/litlfred/qou/pull/6998 — `--self-test` 16/16.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
