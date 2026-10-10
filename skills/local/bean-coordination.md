---
name: bean-coordination
roles: [reader, collaborator, owner]
description: >
  Pointer to the bean-based session work-plan system (the `beans` CLI
  flat-file issue tracker, data under `.beans/`). Operational usage lives in
  todo-manager.md / session-intent.md; the generic coordinator/orchestrator
  logic is owned upstream by the folio-assistant repository.
---

> **🟧 Beans are branch-mounted (issue #7642, owner 2026-10-10). This overrides every "commit the bean" instruction below.**
> `beans/` lives on `cat/cat-harness/beans` and is gitignored on main. The
> SessionStart hook mounts it at `beans/`; by hand:
> `bun folio-assistant/cat-harness/scripts/state-mount.ts`. `beans` CLI
> commands work on the mount unchanged. Write edits back with
> `bun folio-assistant/cat-harness/scripts/branch-store.ts push --id beans`, a
> non-forcing splice where `conflict` means re-read and retry. Bean edits are
> no longer part of a PR's commits. If the mount failed, an empty list means
> unreachable, not "no work".


> **🟧 Block-QA location (issue #7642, owner 2026-10-10). This overrides every `<block>.qa.json` path below.**
> The derived block report (`block-qa/v1`) is no longer beside its block. It is
> `test/results/block-qa/<repo-relative block path>.qa.json` (gitignored),
> published to `cat/cat-harness/qa-reports` keyed by commit. Fetch it first:
> `bun folio-assistant/cat-harness/scripts/qa-store.ts fetch --ref main`.
> Agent and human verdicts live on main in
> `test/attestations/block-qa/<same path>.attestations.json`. Read and write
> through `folio/pipeline/block-qa-io.ts` (Python: `scripts/lib/block_qa.py`);
> never build the sibling path by hand. An empty results tree means unfetched,
> not clean.


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
> coordinator/orchestrator bean-coordination logic has been decoupled from this
> physics repo and migrated into the `folio-assistant` repository (epic `miga`).
> The canonical generic version is maintained upstream and synced here.

## Disambiguation (do not conflate)

- **beans** = the agent's *session work-plan* (`.beans/`, this skill).
- **sidecars** (`*.qa.json`, `*.witness.json`) = *content state tracking*.
  Beans ≠ sidecars. Do **not** convert QA / witness queue items into individual
  beans (see todo-manager.md disambiguation block).
