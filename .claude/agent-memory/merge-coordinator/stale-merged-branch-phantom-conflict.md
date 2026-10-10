# A rebase-merged branch reads as UNMERGED and CONFLICTING

Measured 2026-09-26 in `/home/user/qou` on branch
`claude/wtrace-radical-forward-tower-2026-09-26` (PR #7463), while doing the
sibling-coordination sweep AGENTS.md asks for.

## The claim

For a branch whose PR was **rebase-merged**, both of these are false readings:

| probe | reads | truth |
|---|---|---|
| `git merge-base --is-ancestor <branch> origin/main` | non-zero (NOT an ancestor) | the content IS on `main` |
| `git merge-tree --write-tree origin/main <branch>` | exit 1, `CONFLICT (add/add)` | nothing can conflict |

Cause: rebase-merge replays each commit onto `main`, minting new shas. The branch
tip is therefore reachable from nothing on `main`, and every file the branch
*created* is, from git's point of view, created independently on both sides.

## The measurement

Four leftover refs from the SessionStart coord sweep's "recent sibling branches",
all dated 2026-09-26:

| branch (`claude/…-2026-09-26`) | ancestry read | PR | actual |
|---|---|---|---|
| `markov-radical-tower-followups` | 25 behind / 3 ahead, NOT-merged | #7460 | **merged** |
| `trlim-faithfulness` | 46 / 4, NOT-merged | #7458 | **merged** |
| `p8yg-strict-growth` | —, NOT-merged | #7456 | **merged** |
| `6moa-markovweights-citation` | —, NOT-merged | #7459 | **merged** |

`git merge-tree --write-tree origin/main origin/claude/markov-radical-tower-followups-2026-09-26`
exited 1 with `CONFLICT (add/add)` on
`QOU/SchurWeyl/WtraceRadicalTwoRow.lean` and a content conflict on
`beans/defs/qou-s7z2--…md`.

**How thin the "conflict" was.** The branch's file is 96 lines, `main`'s 122. Both
declare the same two theorems, `mem_rad_of_twoRow_blocks_vanish` and
`exists_nonzero_orthogonal_of_twoRow_blocks_vanish`, and the 45-line window
carrying both is **byte-identical** (`diff` clean). The entire 26-line difference
is docstring — including a retraction block written after the merge. So a naive
"take theirs" resolution of that phantom conflict would have silently deleted a
correction.

## Why it is structural rather than bad luck

- AGENTS.md rule 9 forbids deleting merged feature branches, so leftover refs are
  the **normal** state of this repo, not an anomaly.
- `scripts/session-start-coord-sweep.sh` surfaces those very refs each session
  under the heading *"Recent sibling branches on origin (last 24h)"*, which is
  what invites treating them as live coordination targets.
- So the false reading is available on **every** recently-merged sibling, every
  session.

## The discriminator

Resolve the branch to its PR **state** before reading any git ancestry as a
coordination signal:

```sh
curl -sS -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  "https://api.github.com/repos/litlfred/qou/pulls?state=all&head=litlfred:<branch>"
```

Two notes on the query. **`state=all` is required** — with `state=open` the four
above return `[]`, which reads as *"no PR was ever opened"* and (given ALWAYS-PR)
invites the opposite wrong conclusion. And `mcp__github__search_pull_requests`
with `head:<branch>` returned `total_count: 0` for a branch that does have a PR,
so it does not substitute.

`git cherry origin/main <branch>` and `scripts/verify-merge-replay.py` are the
git-side answers the sibling TRAP in `MEMORY.md` already prescribes; they work
here too. The point of this file is that the *failure shape* is the opposite of
the one that entry describes — a false **conflict**, not a false **clean** — so an
agent that has internalised only "merge-tree is vacuous for an applied patch"
will not recognise it.

## What it nearly cost

One coordination comment on a **merged** PR, warning its author about an add/add
conflict that cannot occur, and recommending a resolution for a merge that had
already happened. Caught by checking PR state before posting, not by any git
probe.
