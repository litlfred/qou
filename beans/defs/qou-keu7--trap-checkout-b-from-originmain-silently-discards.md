---
# qou-keu7
title: 'TRAP: checkout -B from origin/main silently discards beans committed on the old branch'
status: completed
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T10:41:27Z
updated_at: 2026-10-04T15:15:08Z
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


## Recovered 2026-09-06 from a duplicate-ID file (`qou-keu7--trap-checkout-b-from-originmain-silently-discard.md`, no front matter; merged here and deleted)

## Guarded 2026-09-04 — the detection is now a hook, not a paragraph

This bean recorded a sharp detection rule and nothing ran it. That is the same
finding [`precommit-bean-id-warn.sh`](../scripts/precommit-bean-id-warn.sh)
states one directory over about `check-beans.sh`: **a gate nobody invokes is
documentation.** Six PreToolUse warn hooks now exist; this is the sixth.

[`scripts/prebranch-bean-loss-warn.sh`](../scripts/prebranch-bean-loss-warn.sh)
fires on a branch-creation tool call that names an explicit base, and prints the
beans that would vanish, the beans that would revert, and the recovery command
with the current sha already filled in.

### Two design choices worth keeping

**It matches `-b` as well as `-B`.** This bean names `checkout -B`, but `-B` is
not what does the damage — *moving the worktree to a commit lacking files HEAD
has* is. Plain `git checkout -b <new> origin/main` from a branch carrying
unmerged beans loses them identically, and that is the far more common shape in
practice: this session alone created five branches that way. A branch created
with **no** explicit base cannot lose anything and is ignored.

**It reports ADDED and MODIFIED separately.** An added bean *vanishes*; a
modified one silently *reverts to the base's version*, which is the subtler half
and is exactly what happened to `qou-jr5r` — main kept the stale `todo` body
while the retraction sat unmerged. A guard that only counted deletions would
have missed it.

### Verified four ways

- `--selftest` builds a throwaway repo and asserts all four behaviours: added
  bean reported, modified bean reported as a revert, silent on a branch with no
  bean delta, silent (not erroring) on an unknown base ref.
- Argument parsing checked on five realistic command strings, including the two
  that must **not** fire (`checkout -b` with no base, `git commit`).
- Fired against a real branch of this session and correctly named the single
  bean that would vanish, with the recovery sha.
- Silent on a control branch carrying no bean delta.

### It demonstrated the trap on itself

While testing, checking out another branch to reach a bean-carrying HEAD
**removed the guard script from the worktree** — it was committed on its own
branch and absent from the target — so the real-world case had to be re-run from
a copy outside the repo. Exactly the mechanism this bean documents, met while
building the thing that warns about it.

### What it does NOT do

It warns; it never blocks (always exits 0), per the posture the owner chose for
the precision hook on 2026-08-25 — warn-on-commit, push-side block offered and
declined. Do not upgrade it without asking. And it covers `.beans/` only:
**any** tracked file committed on an unmerged branch is lost the same way by the
same checkout. Beans are singled out because they are the case that has actually
cost this repo, and because a lost bean is silent in a way lost code is not — a
missing source file breaks a build.

### Follow-up the same session — the first matcher had a false positive

Re-reading the guard's own diff adversarially turned up a defect in it. The
matcher was a **substring** test, so a command that merely *quotes* the
invocation fired it. Measured:

    git commit -m 'docs: explains git checkout -b claude/foo origin/main and why'
    -> WARNED

and the commit documenting this very guard is exactly such a message. **A guard
that cries on the commit describing it is noise, and noise is what gets guards
ignored** — which would have reproduced this bean's own root failure (a check
that exists and is not heeded) by a different route.

Fixed by matching at a **command position**: split the string on separators
(`;`, `&&`, `||`, `|`, backtick, `$(`) and require the fragment to *begin* with
`git checkout|switch`. A quoted mention sits mid-fragment and is skipped. A base
ref that does not resolve now exits early too, so a prose placeholder like
`origin/<default>` cannot reach the git layer.

**The matcher is now covered by `--selftest`**, which previously exercised only
the diff logic. Nine rows: four true positives (`-b`, `-B`, `switch -C`, and a
compound `git fetch … && git checkout -b …`) and five that must stay silent
(no explicit base; the quoted-in-a-commit-message case; a `grep` for the string;
an `echo` of it; a plain `git commit`). A new class whose selftest does not cover
it is the trap this session kept finding elsewhere.

### Clarification: git DOES protect uncommitted work

While testing, `git checkout` **refused** to switch branches because the guard
script had uncommitted edits. That is the boundary of this trap and is worth
stating plainly: git blocks a checkout that would overwrite *uncommitted*
changes. The silent loss happens only for work that is **committed on the branch
and absent from the target** — which is why it is invisible, and why `git status`
is clean afterwards.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: [M] trap documented in f-a cat-harness/skills/sdlc/sdlc-core/bean-coordination.md:398 and pickup.md:121
