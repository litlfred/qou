---
# qou-lww5
title: 'TRAP: a behind-count on a shallow clone is not a main-advance count'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-08T05:16:03Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-nu9d
---

**Measured 2026-09-08 03:20→05:12 UTC. Cost me most of a check-in turn, and the misleading figure is printed to EVERY agent by the session-start hook.**

A branch created from `origin/main` at 03:20 reported, 112 minutes later:

    Origin/main is ahead by: 37121 commit(s)

That is six months of history (March–September 2026), not a 112-minute advance. It looks exactly like a force-push or a history rewrite on `main`, and reacting to it that way — panic-rebasing, or reporting a rewrite — is the wrong move.

**It is a SHALLOW-CLONE artifact.** AGENTS.md already records that agent clones here are shallow (in the `scriptCommitSha` / `rewritten` discussion, where it explains why ~half of witness `commitSha`s resolve to nothing). What it does not say is that the shallowness also **corrupts the behind-count**: as successive `git fetch` calls deepen the history, `git rev-list --left-right --count origin/main...HEAD` begins counting every merged side-branch commit it can suddenly reach, not the first-parent distance along `main`.

**How to tell the two apart — three commands, seconds:**

```sh
git merge-base --is-ancestor $(git rev-parse HEAD^) origin/main   # rewritten? NO if this succeeds
[ -f .git/shallow ] && wc -l < .git/shallow                       # shallow? how many cut points
git rev-list --count --first-parent <base>..origin/main           # the number you actually wanted
```

Measured here: ancestor check **YES** (so no rewrite), `.git/shallow` present with **2** cut points, first-parent distance **20**, and 32 commits genuinely landed on main in the preceding 3 hours. All normal.

**Why this is worth a bean rather than a shrug.** `scripts/session-start-coord-sweep.sh` prints the raw figure at the top of every session — it is the first number an agent reads. An agent that treats it as a main-advance count will either waste a turn diagnosing a non-event (what happened here) or, worse, take a destructive corrective action against a rewrite that did not occur. The honest reading is *"this number is only meaningful on a full clone"*.

**Not fixed here.** Changing the sweep script's reported figure to first-parent, or having it print the shallow caveat, is a change to shared session infrastructure that every agent sees — it is neither a precision increase nor corpus-derived, so under §"ASK THE OWNER BEFORE CHANGING THINGS" it waits. The cheap version is one line in the sweep output: use `--first-parent`, or append "(shallow clone — count may include merged side-branch history)".

**Recommendation (my judgement, not a finding):** make the sweep print the first-parent count. It is a one-line change to a script nothing else consumes, it makes the most-read number in the session correct rather than alarming, and the current figure has now demonstrably cost an agent turn. But it is the owner's call.


## 2026-11-21 — status check (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`. Status unchanged.

- Recorded as a TRAP in the agent-memory files on branch `claude/agent-ops-traps-2026-11-21` (commit 64a3e7902), PR pending owner approval. Close this bean when that PR merges. Any script or producer fix named above stays open here.
