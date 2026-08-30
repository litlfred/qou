---
# qou-keu7
title: 'TRAP: checkout -B from origin/main silently discards beans committed on the old branch'
status: todo
type: task
priority: high
created_at: 2026-08-30T10:41:27Z
updated_at: 2026-08-30T10:42:09Z
---

## TRAP — measured, 2026-08-30, cost: two beans lost from main for ~40 minutes

The AGENTS.md merged-PR rule says to restart the designated branch from the
latest default branch:

    git checkout -B <branch> origin/<default>

That is correct for CODE and **destructive for `.beans/`**, because a bean
committed on the old branch but not yet merged is a TRACKED file absent from
`main`, so the checkout DELETES it from the worktree with no warning. It is not
an untracked file and it is not stashed; it is simply gone from the tree, and
`git status` afterwards is clean, which is what makes it invisible.

## What it cost here

Two bean files, both written and pushed on `claude/bring-surface-categorical-trace-wtrwtb`
at `9b8409bf2a9`, never merged, then erased from the worktree by a restart:

| bean | on main after the restart | actual state |
|---|---|---|
| `qou-jr5r` | 3495 bytes, `status: todo` | should be 7159 bytes, `scrapped` |
| `qou-s3zd` | **absent** | created, later `completed` |

`qou-jr5r` is the one that bites: main carried my FALSE finding as an open,
high-priority item, with the retraction stranded on an unmerged branch. A
sibling reading main would have found a live bug report for a defect that does
not exist. (It had already cost a wrong comment on PR #6162, corrected there.)

## The second-order failure, which is the real lesson

The next commit was `git add -A && git commit` on the new branch. It landed
**two files** — the ledger and the audit JSON — and no `.beans/` at all,
because there was nothing left to stage. `git add -A` cannot re-add a file the
checkout removed. So the merged PR #6177 cites `qou-s3zd` in its commit message
and body while that bean exists nowhere on main, and my own `beans update
qou-s3zd --status completed` earlier in that same command chain wrote a body
that was never committed and had to be reconstructed by hand.

**`git add -A` looks like a safety net and is not one.** It stages what is in
the worktree; it says nothing about what the worktree lost.

## Detection

    git log --oneline origin/main..<old-branch-tip>

before restarting. Non-empty means unmerged work. The stop-hook's "N unpushed
commits" DOES fire, but it reports against the stale remote branch pointer, so
the count is dominated by main's own commits (36 here, of which 1 was mine) and
reads as noise.

Sharper: `git merge-base --is-ancestor <old-remote-tip> HEAD`. Exit 1 means the
old tip carries something main does not. That is the check that found this.

## Fix

Land the beans BEFORE restarting the branch, or cherry-pick the bean commit
onto the new branch immediately after. Recovery here was
`git checkout <old-tip> -- .beans/<files>` onto a fresh branch off main, plus
rewriting the `completed` body that was never committed anywhere.

Worth considering as a guard: warn when `checkout -B`/`switch -C` would drop
`.beans/` files present on the outgoing branch and absent from the target —
same family as `scripts/precommit-ledger-shrink-warn.sh`, and the same
underlying hazard (an agent-authored record with no producer, silently lost).
