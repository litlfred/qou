---
# qou-20vg
title: 43 beans carry status 'done', which is off-vocabulary and reads as OPEN work
status: completed
type: bug
priority: high
tags:
    - beans-hygiene
created_at: 2026-09-26T10:51:09Z
updated_at: 2026-09-26T11:08:08Z
parent: qou-w3yy
---

**Measured 2026-09-26. This one has a live cost, not just untidiness.**

`beans create`/`update` accept exactly five statuses: `in-progress`, `todo`,
`draft`, `completed`, `scrapped` (from `beans update --help`). **43 beans carry
`done`**, which is not one of them — set by hand-editing the `.md` front matter
rather than through the CLI.

## Why it costs something

```
beans list --status completed  ->  2704
beans list --status done       ->    43
default `beans list`           ->  includes all 43
```

So the 43 are **excluded from the finished set and present in the default
listing**. `AGENTS.md` work-plan §4 (the 5-minute idle trigger) walks open beans
for backlog; these 43 are finished work sitting in that queue. Same shape as the
14,688-duplicate incident (`qou-2ryn`): the cost is not clutter, it is that the
policy reading the queue is reading noise.

Sample: `qou-7ylg` ("BUG: main is RED on validate"), `vrfw`, `vpth`, `qou-argp`,
`qou-rc7b`, `qou-c1wr`.

Also off-vocabulary: `open` (3 beans) and `''` (1 bean). The empty one will not
match any `--status` filter at all.

## The fix, and why it is safe

`beans update <id> --status completed` for the 43, `--status todo` for the 3
`open`, and the 1 empty needs a look before assigning. This is
**derived-from-corpus** (exemption 2 of the ASK-THE-OWNER rule): the CLI's own
`--help` fixes the vocabulary, and a reviewer checks it by re-running the two
counts above.

**But read each `done` bean before flipping it.** `done` and `completed` are
plainly the same intent, yet three of the six sampled titles are phrased as
open defects ("BUG: main is RED", "BUILD COVERAGE: lake build reaches only 853
of 1618"). If any of those describes a condition that is still true, the right
status is `todo`, not `completed` — and flipping it to `completed` would bury a
live bug. **Rule 13a** also applies: any of these tracking an open conjecture
must not be completed at all. So this is 47 individual reads, not one sed.

**Default if nobody acts:** the 43 stay in the open queue and the idle policy
keeps ranking them.



## FIXED 2026-09-26 — 47 statuses migrated, and 13 deliberately NOT closed

Off-vocabulary status count **47 → 0**. Final distribution: in-progress 578,
todo 1870, draft 1, completed 2738, scrapped 154.

Split **34 → completed, 13 → todo**, decided per-bean rather than by sed, exactly
as this bean's own caution demanded. The rule used: a bean whose body still
carries a live open-signal, and whose title does not itself declare closure, goes
to `todo` — because a bean wrongly left open costs one idle-pass glance while a
bean wrongly closed **buries work**.

Kept open: `fwr10`, `fwr6`, `htw2`, `qou-7ylg`, `qou-argp`, `qou-mlgp`,
`qou-pdgc`, `qou-rc7b`, `qou-slvl`, `qou-vbjg`, `qou-xdwp`, `qou-xzd5`,
`qou-yos9`.

### A blind spot worth recording, because it nearly closed live work

My first open-signal pattern matched only `still open|remains open|not done|open
conjecture|blocked on`. `qou-xzd5`'s tail reads *"An `n ≥ 2` instance **remains
unbuilt** anywhere in the tree, which is the real missing infra the manuscript
keeps citing"* — plainly open, and **invisible** to that pattern. It was in the
close set until a spot-check caught it. Widening to include `remains
unbuilt|remains missing|still missing|not yet proved|the real missing|what
remains open` moved it. One more instance of the detector-blindness class: an
unknown spelling, found by checking a positive rather than by trusting a zero.

I also tried a **positional** heuristic first (is the last open-signal in the
final 30% of the body?) and **rejected it**: it called `qou-xdwp` close-able when
line 34 of 59 is a live `## Still open` section *heading*. A numeric proxy for a
structural fact — taxonomy row 30.
