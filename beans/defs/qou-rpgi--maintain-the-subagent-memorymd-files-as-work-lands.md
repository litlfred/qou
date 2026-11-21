---
# qou-rpgi
title: Maintain the subagent MEMORY.md files as work lands
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T10:24:44Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-nu9d
---

Standing obligation created by `qou-j5jq`, not a scheduled task.

The eight MEMORY.md files decay the way any hand-kept record here decays. Two
rules, both stated in AGENTS.md §"Subagents with persistent memory":

1. A session that establishes a durable fact in one of these areas — a detector
   blind spot, a producer that refuses by design, a gate that cannot fire —
   adds it as a **TRAP** in the same PR.
2. A session that re-measures a **BASELINE** updates that entry with the fresh
   number and date rather than leaving the old one beside it.

A memory file that only accretes becomes the thing it exists to prevent.

Keep MEMORY.md under 200 lines — it is the injected entry point. Split detail
into sibling files the agent reads on demand;
`.claude/agent-memory/compute-precision-auditor/producer-health.md` is the
worked example.

**First firing, 2026-08-29** — one turn after this bean was created.

`qou-961o` landed (`ae8098c3`), renaming the three convention-C `markovZ`.
That staled `convention-auditor`'s markovZ BASELINE exactly as designed. Re-ran
`scripts/lean-markov-convention-audit.py` rather than copying main's prose, and
the re-measurement found something the rename's own resolution note missed:

**`markovZC` (upper C) is convention C; `markovZc` (lower c) is convention D.**
One letter's case, opposite meanings, `0.4993203342` vs `0.6126880371` at the
proton q₀. `AGENTS.md` line 2060 claimed "one convention, no collision" — that
is measurably false and is corrected on this branch.

Recorded as a TRAP; baseline refreshed; `q0-pin-migration.md` split out to keep
MEMORY.md inside the 200-line injection cap.

Merged as #6010 (5ed07e4). Bean returns to `todo` — this is a standing obligation, not a task that completes.

Left open for the author: whether `markovZc` or `markovZC` is the one to rename. Flagged on #5999, not actioned.

── 2026-09-03: measured — FOUR of FIVE MEMORY.md exceed the 200-line rule, and I cannot tell whether that loses anything ──

Two TRAPs added this session (below) pushed me to check the caps. Measured
directly on `.claude/agent-memory/*/MEMORY.md`:

| agent | lines | bytes | over 200? | over 25 KB? |
|---|---|---|---|---|
| `lean-verifier` | **374** | 22,538 | **+174** | no |
| `compute-precision-auditor` | **237** | 13,628 | **+37** | no |
| `convention-auditor` | **235** | 13,674 | **+35** | no |
| `merge-coordinator` | 200 → **200** | 12,369 | at cap | no |
| `corpus-grepper` | 237 → **195** | 10,331 | under | no |

(This bean says *"the eight MEMORY.md files"*; there are **five** in this repo.)

### 🛑 The part I could NOT settle, and did not guess

AGENTS.md §"Subagents with persistent memory" says *"the first 200 lines **(or
25 KB)**"* are injected. **Every one of the five is under 25 KB.** So:

- if the **line** limit binds, `lean-verifier` silently loses **174 lines** —
  nearly half its memory — and two more agents lose ~36 each;
- if the **byte** limit binds, nothing is lost and 200 lines is a soft
  authoring convention.

`merge-coordinator/MEMORY.md` line 5 asserts the strong reading — *"line 201+
is silently dropped"* — but that is an agent's claim, not a verified
observation of the injector, and I did not verify it either. **I am recording
the measurement and the ambiguity, not a defect**, because guessing which
limit binds is the exact error class the two new TRAPs are about.

**Next step is one cheap experiment, not a sweep:** put a unique sentinel
string past line 200 of one MEMORY.md, start that subagent, and ask whether it
can see the sentinel. That settles it in one run. Until it is settled, do not
mass-restructure the three over-cap files — and do not assume they are fine
either.

### What I did do

Brought the two files I touched into compliance with the stricter reading,
since staying under both limits is unambiguously safe:

- **`corpus-grepper`** 237 → **195**. Moved the 2026-09-02 Markov/Ocneanu
  span-rank resolved-topic entry (which sat past line 200) into
  `resolved-topics.md`, and the three-tier library procedure into
  `library-and-staleness-traps.md`, leaving pointers. **No `##` heading was
  lost** — verified by diffing the heading sets before and after across all
  three files.
- **`merge-coordinator`** 200 → **200**, by cutting to pay for what I added:
  compressed a block quote that documented the section's *own past wording*
  (a defect since fixed, so the least load-bearing lines in the file, per that
  file's own "order last-worst" rule).

### The two TRAPs

- `corpus-grepper` — **an inherited "X is unavailable" is HALF a
  measurement.** The corpus said *"the ptolemy DB is firewalled; only
  4₁/5₂/3₁ ship fixtures"*. Firewall real (403, re-verified two ways); fixture
  list wrong — **seven** manifolds ship, nobody had run `ls`. The shape to
  watch: a claim bundling an **environment** fact with a **corpus** fact.
- `merge-coordinator` — **`git diff --stat` omits untracked files.** Reported
  PR #6510 as "601 files, +616/−1"; it is **634 files, +4223/−1**. Detail in
  the new sibling `diff-stat-omits-untracked.md`.

Both are the same root, which is why they are worth keeping together: **a
tool's count answers a narrower question than the one you asked, and reports
it in the units you expected.**

### Same-day update (2026-09-03, ~2 h later)

Two things moved, both reinforcing rather than settling:

- **`lean-verifier` grew 374 → 419 lines** while this session worked (main
  moved). The over-cap files are **accreting**, not draining, so whatever the
  answer to the line-vs-byte question, the trend is the wrong way. It is now
  **+219 over** the documented rule and 22.5 KB — still under 25 KB, so the
  ambiguity is unchanged.
- **A sibling independently treated the cap as binding**: `ec96d89b1a`
  *"memory(merge-coordinator): tighten the draft-toggle correction back under
  the 200-line cap"* — 4 insertions, 7 deletions, purely to fit. So two
  sessions today have paid the cap cost. **That is agreement about practice,
  not evidence about the injector**; the sentinel experiment above is still
  the only thing that settles it, and it is still not done.

### 2026-09-03, SETTLED (the sentinel experiment, run) — nothing is injected at all

The experiment filed above was run, and the answer is not the one the question
assumed. **It is not truncation. `memory: project` injects NOTHING** for
subagents launched via the Agent tool in this environment.

- `lean-verifier` (419-line MEMORY.md) and `corpus-grepper` (195) were each
  asked, independently and with tools forbidden, what their own prompt
  contained. Both: **zero** `MEMORY.md` content.
- **Objective corroboration, no self-report needed:** four `see memory` /
  `see the memory entry` cross-references in three agent definitions are
  **dangling pointers** into content that never arrives.
- Frontmatter is correct (`memory: project` on all five), files exist. So it
  is harness behaviour here, not misconfiguration, and may differ elsewhere.

**Consequence for the 200-line cap: it is a convention, not a live
constraint.** Nothing is truncated because nothing is sent. Keep files under it
anyway — it bounds what an agent must *read* — but never treat "under 200" as
evidence an agent has the content. The three over-cap files are no more broken
than the two under it.

### 🛑 The repair is UNVERIFIED, and its own delivery failed once

Each agent definition now opens with `## FIRST ACTION — read your memory` plus
a required **compliance line** (files read, `MEMORY.md` line count, its last
commit sha) so a memory-informed run is distinguishable from a memory-less one.

**A third agent, launched after that edit, did not receive it** — it quoted its
prompt going straight past where the section sits on disk. So agent definitions
appear **snapshotted** (committed `HEAD`, or cached at session start). Test
after commit: relaunch and ask a subagent to quote the heading back. **Until
one does, this is not done.**

**`AGENTS.md` is therefore the load-bearing carrier** — both agents quoted it
back in full — so the instruction lives there too.

### Three corrections the consuming agent made to me

1. **"2,520 lines across 16 files" is the whole tree**, quoted in each agent's
   own definition — overstating its burden ~6×. Per agent: `MEMORY.md`
   195–419 lines, directory 412–657, ~3–7k tokens. Fixed to per-agent figures.
   My third wrong-denominator error of the day.
2. It reported my new TRAP missing from its memory. **It was right about the
   tree it saw and I was right that I wrote it** — I had switched to the other
   branch. Worth recording: a subagent reads the working tree, so it sees
   whatever branch the launcher is standing on.
3. It rejected "launcher pastes the relevant entries" for a reason worth
   keeping: the launcher cannot know which TRAPs apply — *if it did, it would
   not need the agent* — and it makes memory **write-only**, so a new
   resolved-topic row would never reach anyone. Read-when-relevant fails the
   same way: deciding a TRAP is irrelevant requires already knowing it.


## 2026-11-21 — status check (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`. Status unchanged.

- Ongoing by nature. This session added TRAP entries to `merge-coordinator/` and `compute-precision-auditor/MEMORY.md` on branch `claude/agent-ops-traps-2026-11-21` (PR pending owner approval).
