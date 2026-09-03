---
# qou-rpgi
title: Maintain the subagent MEMORY.md files as work lands
status: todo
type: task
priority: normal
created_at: 2026-08-29T10:24:44Z
updated_at: 2026-08-29T10:58:40Z
parent: qou-j5jq
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
