---
# qou-md01
title: 'TRAP: merge endpoint 500s DETERMINISTICALLY when rebase-merging a branch that carries merge commits — not the retryable 5xx of qou-4w5b'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-13T10:32:43Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-nu9d
blocking:
    - qou-4w5b
---

## Measured 2026-09-13, merging #7255

`mcp__github__merge_pull_request` with `merge_method: "rebase"` returned
`PUT https://api.github.com/repos/litlfred/qou/pulls/7255/merge: 500 []`
**twice, ~15 minutes apart**, on a PR whose state was otherwise healthy
(`mergeable_state: "clean"`, no conflicts, `merged: false`).

Verified by ancestor check after each attempt that **nothing landed** —
`git merge-base --is-ancestor <head> origin/main` returned false both times. So
these were genuine no-ops, not the rule-8a shape where an error accompanies a
write that DID apply. (Check anyway; do not assume from this row.)

## The structural cause, and why "retry" is the wrong advice

The branch carried **6 merge commits inside 20 commits** — six
`Merge remote-tracking branch 'origin/main'` merge-ups, which is what the
owner's standing "rebase with merge so you are up to date" preference produces.
GitHub's rebase-merge replays commits one at a time onto the base and **cannot
replay a merge commit**.

This matters because the sibling bean **`qou-4w5b`** ("GitHub PR create AND
update both 5xx intermittently on long bodies — retry") documents a *different*
500 from the same MCP server whose correct response IS to retry with a different
body. **A 500 from the GitHub MCP is not one failure mode.** The discriminator:

| | `qou-4w5b` (create/update body) | this (merge endpoint) |
|---|---|---|
| reproducibility | intermittent; a short body succeeds | **deterministic** — identical twice, 15 min apart |
| correct response | retry / stub-then-update | **change the merge method or the history** |

Retrying this one verbatim can only burn calls.

## What worked, and the two routes

`git rebase origin/main` **linearises the six merge-ups away cleanly** — 14
commits, zero conflicts — and the resulting tree is **byte-identical** to what a
merge commit produces (verified twice, against two different `main` heads:
trees `fc848e2f770…` and `09de808c3e2…`). So no content is at stake; only the
shape of the history on `main`.

- **Route B (preferred, keeps the default method):** reset the branch to the
  linearised history, `--force-with-lease`, then rebase-merge normally. This is
  the remedy AGENTS.md rule 8 itself names — *"clean the branch locally with
  `git rebase -i` and rebase-merge the cleaned-up history instead."*
  **Blocked in this session:** the Claude Code auto-mode classifier denied the
  force-push as `[Git Destructive]`, twice. An agent without that permission
  cannot take this route.
- **Route A (what was used):** `merge_method: "merge"`. Rule 8's merge-commit
  exception applies — the PR *is* a sub-merge of several already-merged states.
  Landed as `3cb26d4b9f8`.

## Prevention, which is cheaper than either route

**Do not merge `main` into a feature branch six times.** The merge-ups are what
destroy rebase-merge. If the branch must stay current, prefer a rebase onto
`main` (no merge commit) — or accept that the merge will need rule 8's
exception and say so in the PR rather than discovering it at merge time.

## What is NOT established

- Whether the 500 is *caused* by the merge commits specifically, or by size
  (446 files, +63782 lines — a server-side timeout would also present as 500).
  **Confounded; not bisected.** What would separate them: a small PR carrying
  one merge commit. Fails -> merge commits. Succeeds -> size.
- Whether it is GitHub, the MCP github server, or the agent proxy.


## 2026-11-21 — status check (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`. Status unchanged.

- Recorded as a TRAP in the agent-memory files on branch `claude/agent-ops-traps-2026-11-21` (commit 64a3e7902), PR pending owner approval. Close this bean when that PR merges. Any script or producer fix named above stays open here.
