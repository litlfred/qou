# Handoff → folio-assistant agent: finish the beans / work-plan migration

**Date:** 2026-06-19
**From:** qou session `claude/modest-carson-xoqwps` (PR
[#2495](https://github.com/litlfred/qou/pull/2495))
**Re:** Folio-Assistant Infrastructure Migration — the `miga` epic
(`.beans/miga--folio-migration-parent.md`)

This document is **instructions for the folio-assistant repo's agent**. It
describes the parts of the bean / work-plan migration that belong on the
**folio-assistant** side, because the `miga` goal is *"the final state of qou
must strictly contain only physics content, compute substrate, and math
simulators"* — generic agent infrastructure (the bean system, the MCP server,
provisioning) lives in `folio-assistant`.

## What "beans" are

`beans` ([hmans/beans](https://github.com/hmans/beans)) is a Go flat-file issue
tracker that stores issues as markdown under `.beans/`. It backs the agent
**session work-plan** (supersedes the old `TodoWrite` tool / `todos/*.json`).
Operational usage is documented in qou's
`.claude/skills/local/todo-manager.md`, `session-intent.md`, `pending-show.md`,
`idle-backlog.md`.

**Discipline:** `beans ≠ sidecars`. QA (`*.qa.json`) and witness
(`*.witness.json`) queues are content-state tracking and are **not** converted
into individual beans. Bulk QA queue JSON may be co-located under `.beans/` but
is never `beans create`-d per finding.

## What the qou side already did (PR #2495)

- Added `scripts/install-beans.sh` (idempotent `go install
  github.com/hmans/beans@latest` → `$HOME/.local/bin`). Verified: installs and
  `beans check` passes in a fresh cloud sandbox.
- Repaired `.claude/skills/local/bean-coordination.md` — it was a bare stub
  pointing at `folio-assistant/.claude/skills/local/bean-coordination.md`, a
  path that does **not** resolve inside the qou checkout. It now points at the
  live local spec and carries an ownership note deferring the *generic* skill to
  folio-assistant.
- Wired beans into `CLAUDE.md` discovery surfaces (work-plan policy, start-of-
  session step, skill-routing table, project-structure table) so fresh agents
  discover the system. A migration note redirects all remaining "TodoWrite"
  mentions to bean commands.

## Tasks for folio-assistant (in priority order)

### 1. Own the authoritative generic `bean-coordination` skill
The qou copy is now a thin local pointer. folio-assistant should host the
canonical **generic** coordinator/orchestrator bean-coordination skill (the part
with no physics content) and provide a vendor/sync path back to qou (the same
mechanism used for the other synced skill packages). **Acceptance:** qou's
`bean-coordination.md` can be regenerated from the folio-assistant source by the
nightly skill sync rather than hand-maintained.

### 2. Own / generalize `install-beans.sh`
The installer is generic infra. Either move it to folio-assistant and have qou
vendor it, or keep a copy in qou but treat folio-assistant's as canonical.
**Acceptance:** one source of truth for the installer; qou's copy is
identical-or-vendored.

### 3. Provision the `beans` CLI in the MCP Docker image
The deployed assistant must have `beans` on `PATH`. Add the `go install` (or a
prebuilt binary copy) to `.github/docker/Dockerfile.lean-mcp` (or wherever the
assistant image is built) so beans is baked in like the Lean oleans.
**Acceptance:** `beans list` works inside the running MCP container.

### 4. Repoint the `todos/` → `.beans/` runtime readers (the data migration)
The legacy `todos/*.json` queues are still read by **runtime code** that lives
in / is owned by the platform layer. These must be repointed before the queue
JSON is physically relocated, or the readers break:
- the MCP server `/api/todos` route + `/todos` HTML dashboard,
- `content/pipeline/qa-agent-drain-queue.ts`,
- the `check-todos.sh` SessionStart hook (if still present).

Note the `beans ≠ sidecars` rule: the **watcher** queues
(`compute-/detangler-/proof-/canonical-watcher-queue.json`, `qa-q-CAL-*`) are
QA-axis sidecar scope; if relocated they stay as **bulk JSON under `.beans/`**
(matching the existing `.beans/qa-agent-drain-queue.json`,
`simulator-qa-sidecar-queue.json` precedent) — they are NOT converted to beans.
The genuinely work-plan-scoped queues (`research-queue.json`,
`1ppq-qbeta-queue.json`, `lean-discharge-queue.json`) can become beans if
desired. **Acceptance:** `todos/` is empty (or removed) and every former reader
resolves against `.beans/`; `/api/todos` still serves; no watcher skill points
at a dead path.

### 5. Wire `beans prime` into the session-start surface
`beans prime` is designed to "output instructions for AI coding agents." Wire it
into the SessionStart hook (or the assistant's system-prompt assembly) so every
session is primed with current bean instructions automatically — instead of
relying on a static skill doc. (In this sandbox `beans prime` returned empty;
confirm the installed version populates it, or pin a version that does.)
**Acceptance:** a fresh session is primed with the bean instructions + current
bean list without manual `beans list`.

## Cross-repo coordination

When folio-assistant lands items 1–5, it should update qou's
`.claude/skills/local/bean-coordination.md` ownership note and close the
corresponding migration beans (`kpzd` finalize-workflows, `d9nu` repo-cleanup,
and any new bean tracking this handoff). Do **not** delete qou's `todos/`
queue files until item 4's readers are confirmed repointed.
