---
# qou-xssn
title: 'TRAP: a rebase-merged branch reads NOT-merged with phantom add/add conflicts — the complement of qou-6pd1''s false CLEAN'
status: todo
type: task
created_at: 2026-09-26T20:08:26Z
updated_at: 2026-09-26T20:08:26Z
parent: qou-weeq
---


## Measured 2026-09-26 (PR #7463)

`qou-6pd1` (completed) records the **false CLEAN** direction of this defect: *"The 18:05Z
merge-tree CLEAN reading was vacuous (an applied patch is always clean)."* This bean is its
**complement** — the same staleness read the other way, as a **false CONFLICT** — and an
agent holding only `qou-6pd1`'s lesson will not recognise it.

| probe | reads | truth |
|---|---|---|
| `git merge-base --is-ancestor <branch> origin/main` | non-zero — NOT an ancestor | the content IS on `main` |
| `git merge-tree --write-tree origin/main <branch>` | exit 1, `CONFLICT (add/add)` | nothing can conflict |

Cause: rebase-merge replays each commit onto `main`, minting new shas, so the branch tip is
reachable from nothing and every file the branch *created* looks created independently on
both sides.

**Measured on all four refs the SessionStart coord sweep listed as "recent sibling
branches"** — `markov-radical-tower-followups`, `trlim-faithfulness`, `p8yg-strict-growth`,
`6moa-markovweights-citation`. All four read NOT-merged with real-looking conflicts; **all
four PRs (#7460, #7458, #7456, #7459) had merged.**

**How thin the conflict was**, on the one inspected: 96 lines against main's 122, both
declaring `mem_rad_of_twoRow_blocks_vanish` and
`exists_nonzero_orthogonal_of_twoRow_blocks_vanish`, with the 45-line window carrying both
**byte-identical** under `diff`. The entire 26-line difference is docstring — including a
retraction block `main` gained *after* that merge. A "take theirs" resolution of the phantom
conflict would have silently deleted a correction.

**Structural, not bad luck.** AGENTS.md rule 9 forbids deleting merged feature branches, so
leftover refs are this repo's *normal* state, and `session-start-coord-sweep.sh` surfaces
exactly them every session. The false reading is available on every recently-merged sibling.

**Discriminator** — resolve branch → PR state before reading git ancestry as a coordination
signal: `GET /pulls?state=all&head=litlfred:<branch>`. **`state=all` is required**; with
`state=open` all four return `[]`, which reads as *"no PR was ever opened"* and (given
ALWAYS-PR) invites the opposite wrong conclusion. `mcp__github__search_pull_requests` with
`head:<branch>` returned `total_count: 0` for a branch that does have a PR, so it is not a
substitute.

**What it nearly cost:** one coordination comment on a merged PR, warning its author about
an add/add conflict that cannot occur and recommending a resolution for a merge that had
already happened. Caught by checking PR state before posting, not by any git probe.

Landed as a `merge-coordinator` memory TRAP + sibling file
`.claude/agent-memory/merge-coordinator/stale-merged-branch-phantom-conflict.md`
(`MEMORY.md` kept under its 200-line cap, at 192). Mechanical; the defect is understood and
recorded, so this bean is complete on landing — it carries no open conjecture.
