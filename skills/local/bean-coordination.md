---
name: bean-coordination
roles: [reader, collaborator, owner]
description: >
  Pointer to the bean-based session work-plan system (the `beans` CLI
  flat-file issue tracker, data under `.beans/`). Operational usage lives in
  todo-manager.md / session-intent.md; the generic coordinator/orchestrator
  logic is owned upstream by the folio-assistant repository.
---

# Bean Coordination

The **bean-based work-plan system** — the [`beans`](https://github.com/hmans/beans)
CLI, a flat-file issue tracker storing issues as markdown under `.beans/` — is
how every session tracks its work-plan and how agents hand off across sessions.

**Operational spec (read these):**

- [`todo-manager.md`](todo-manager.md) — bean lifecycle: `beans create` /
  `update` / `list`, parent/child epics, status transitions. This is the
  authoritative *local* usage spec.
- [`session-intent.md`](session-intent.md) — session-start intent + session-end
  results protocol against the master ledger and the bean queue.
- [`pending-show.md`](pending-show.md) — read-only "what is this session
  working on?" display.
- [`idle-backlog.md`](idle-backlog.md) — pull right-scoped beans while idle.
- [`prepare-merge-auto.md`](prepare-merge-auto.md) & [`integration-watcher.md`](integration-watcher.md) §5g.6 — post-merge bean reconciliation onto `origin/cat/cat-harness/beans`.

**Install the CLI:** [`scripts/install-beans.sh`](../../scripts/install-beans.sh)
(idempotent; `go install github.com/hmans/beans@latest`).

## Post-Merge Bean Closure (`origin/cat/cat-harness/beans` — MANDATORY)

Because `beans` is stored on orphan branch `origin/cat/cat-harness/beans`
(checked out at `/private/tmp/qou-beans-latest` and symlinked from `beans/`),
merging a PR or Merge Train onto `origin/main` does **not** automatically mark
its beans `completed`. Every `merge-steward` landing (`Process_MergeToMain` /
`Process_MergeTrain` in `folio-assistant/cat-harness/sdlc/skills/sdlc-core/{merge-to-main,merge-queue,merge-manager-watcher}.md`)
MUST run:

```bash
# Single merged PR:
nice -n 10 python3 scripts/close-merged-pr-beans.py --pr <N>

# Multi-PR Merge Train:
nice -n 10 python3 scripts/close-merged-pr-beans.py --prs <N1>,<N2>,...
```

`scripts/close-merged-pr-beans.py` verifies `state == "MERGED"` and `origin/main`
ancestry, skips umbrella epics with open children, `OWNER CALL` / `OWNER DECISION`
beans, open-caveat mentions, and Rule-13a zero-instance `Conjecture` / `Hypothesis`
classes, updates completed leaf beans (plus any newly 100%-drained parent epics),
runs `beans check` + `scripts/check-beans.sh`, and commits + pushes
`origin/cat/cat-harness/beans`.

> **Ownership note — Folio-Assistant Infrastructure Migration.** The *generic*
> coordinator/orchestrator bean-coordination logic has been decoupled from this
> physics repo and migrated into the `folio-assistant` repository (epic `miga`).
> The canonical generic version is maintained upstream and synced here.

## Disambiguation (do not conflate)

- **beans** = the agent's *session work-plan* (`.beans/`, this skill).
- **sidecars** (`*.qa.json`, `*.witness.json`) = *content state tracking*.
  Beans ≠ sidecars. Do **not** convert QA / witness queue items into individual
  beans (see todo-manager.md disambiguation block).
