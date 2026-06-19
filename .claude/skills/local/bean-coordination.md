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

**Install the CLI:** [`scripts/install-beans.sh`](../../../scripts/install-beans.sh)
(idempotent; `go install github.com/hmans/beans@latest`).

> **Ownership note — Folio-Assistant Infrastructure Migration.** The *generic*
> coordinator/orchestrator bean-coordination logic is being decoupled from this
> physics repo and migrated into the `folio-assistant` repository (tracked by
> the `miga` epic — see `.beans/miga--folio-migration-parent.md`). The path
> `folio-assistant/.claude/skills/local/bean-coordination.md` referenced in
> older notes is the **upstream copy** and is NOT resolvable inside this
> checkout. Until folio-assistant vendors the generic skill back, treat
> `todo-manager.md` as the local source of truth.

## Disambiguation (do not conflate)

- **beans** = the agent's *session work-plan* (`.beans/`, this skill).
- **sidecars** (`*.qa.json`, `*.witness.json`) = *content state tracking*.
  Beans ≠ sidecars. Do **not** convert QA / witness queue items into individual
  beans (see todo-manager.md disambiguation block).
