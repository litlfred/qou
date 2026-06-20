# Handoff → folio-assistant agent: beans / work-plan migration + session-setup consolidation

**Date:** 2026-06-19 · **Updated:** 2026-06-20 (post #2495 / #2513; + setup consolidation)
**From:** qou sessions `claude/modest-carson-xoqwps` ([#2495](https://github.com/litlfred/qou/pull/2495)),
`claude/beans-j8el-status-2026-06-20` ([#2513](https://github.com/litlfred/qou/pull/2513)),
`claude/folio-asst-beans-handoff-finalize-2026-06-20` ([#2515](https://github.com/litlfred/qou/pull/2515))
**Re:** Folio-Assistant Infrastructure Migration — the `miga` epic (`.beans/miga--folio-migration-parent.md`)
**Tracking beans:** `j8el` (qou-side `todos/`→`.beans/`), `bmwh` (handoff finalize), `17ht` (setup consolidation)

> **Canonical f-a-side doc:** the folio-assistant repo's
> [`docs/folio-assistant-migration.md`](https://github.com/litlfred/folio-assistant/blob/main/docs/folio-assistant-migration.md)
> §6 is the canonical home for the qou-side requirements (A/B/C) and the folio-assistant
> task list. **This file is the qou-side _record_** of what landed (the A/B/C gates are all
> met on `main` — see §4). It supersedes any earlier scattered qou handoff notes. Read
> top-to-bottom: §1–§3 are context + current state, §4 is what qou already did, §5 is your
> task list.

---

## 1. What "beans" are

`beans` ([hmans/beans](https://github.com/hmans/beans)) is a Go flat-file issue tracker that
stores issues as markdown under `.beans/`. It backs the agent **session work-plan** and
**supersedes** the old `TodoWrite` tool / `todos/*.json` mechanism. Operational usage lives in
qou's `.claude/skills/local/{todo-manager,bean-coordination,session-intent,pending-show,idle-backlog}.md`.

**Discipline — `beans ≠ sidecars`.** QA (`*.qa.json`) and witness (`*.witness.json`) queues are
content-state tracking, **not** work-plan items: never `beans create` them. Bulk queue JSON may be
co-located under `.beans/` but stays bulk JSON.

## 2. Why this migration exists (the `miga` goal)

*"The final state of qou must strictly contain only physics content, compute substrate, and math
simulators."* Generic agent infrastructure — the bean system, the MCP server, provisioning, the
session-start harness — belongs in **folio-assistant**, not qou. The qou side has done the *interim*
wiring (so agents discover beans today); folio-assistant owns the *permanent, generic* versions.

A recurring failure mode to watch for: the platform-code migration (qou commit `39fc90f6`,
*"remove platform code (migrated to folio-assistant)"*) deleted scripts but left their **hook
references dangling** in `.claude/settings.json`. When you own these surfaces, move the *wiring*
and the *script* together.

## 3. Current state on `main` (2026-06-20) — read before touching anything

**`todos/` — 1 tracked file remains** (after the goal-queue relocation):

| File | Class | Disposition |
|------|-------|-------------|
| `todos/qa-q-CAL-1-2-3-audit.json` | QA sidecar | stays bulk JSON (`beans ≠ sidecars`) |

The 3 work-plan goal queues (`1ppq-qbeta-queue`, `lean-discharge-queue`, `research-queue`) were
**relocated `todos/` → `.beans/` as bulk JSON** (`git mv` + a mechanical repoint of all readers,
including the live `STATUS.md` links) — they stay bulk JSON per `beans ≠ sidecars`, **not** exploded
into per-item beans. The `content-todos.ts` TodoItem store stays at `todos/` (AGENTS.md §4a).

**`.beans/*.json` — 11 tracked bulk-JSON queues:** the 4 relocated watcher queues
(`canonical-/compute-integration-/detangler-integration-/proof-integration-watcher-queue.json`)
+ `paper-todos.json`, `qa-agent-drain-queue.json`, `simulator-qa-sidecar-queue.json`,
`status-section-audit.json` + the 3 work-plan goal queues relocated from `todos/`
(`1ppq-qbeta-queue.json`, `lean-discharge-queue.json`, `research-queue.json`).

**Absent from the qou checkout (wholly folio-assistant scope):** the MCP `/api/todos` route +
`/todos` dashboard (no `todos/` reader under `folio-assistant/src/`), `check-todos.sh`, and any
Dockerfile.

## 4. What the qou side already did

### PR #2495 — discover + relocate
- Added `scripts/install-beans.sh` (idempotent `go install github.com/hmans/beans@latest` →
  `$HOME/.local/bin`). Verified in a fresh cloud sandbox.
- Repaired `.claude/skills/local/bean-coordination.md` (was a stub pointing at a non-resolvable
  folio-assistant path).
- Wired beans into AGENTS.md discovery surfaces (work-plan policy, skill-routing, project-structure).
- **Relocated the 4 watcher queues** `todos/` → `.beans/` (`git mv`) + repointed **38 doc
  references** across the integration-watcher skill family, `.claude/commands/*`, and AGENTS.md.
  Verified **no `*.ts` code reads the watcher-queue paths** — so this did *not* touch `/api/todos`.
- Repointed `content/pipeline/qa-agent-drain-queue.ts` default `--out` → `.beans/`.

### PR #2513 — durable bean status
- Marked bean `j8el` `in-progress` so the merged `.beans/` work-plan reflects the relocation.

### PR #2515 + #2526 — session-setup consolidation (the "frankenstein" cleanup)
Diagnosis: a 7-command SessionStart chain where some scripts were deleted by `39fc90f6` but still
referenced, the Lean hooks flood the transcript in firewalled containers, and two beans surfaces
overlap. qou-side fixes landed:

- **(A) Stripped 4 dangling hook references** from `.claude/settings.json` — `open-folio-assistant.sh`
  + `watch-main-prompt.sh` (SessionStart), `render-on-change.sh` (PostToolUse), and
  `greeting-task-selection.sh` (UserPromptSubmit) were all deleted by `39fc90f6` but still wired.
- **(B) Quieted the Lean hooks** — two layers: (#2515) the SessionStart hook redirects
  `lean-build-bg.sh` / `setup-lean-toolchain.sh` stdout to `${TMPDIR:-/tmp}/*.log`; (#2526) the
  hardened **in-script** port of folio-assistant PR #14 — B.1 adds a functional `lean --version`
  probe (so a non-empty-but-broken elan toolchain dir bails cleanly instead of retrying `lake`
  against the firewalled `release.lean-lang.org`), B.2 swaps `lake build … | tee` for
  `> log 2>&1`. Both the `timeout` and `curl` external calls are guarded behind `has`
  (`has timeout` / `has curl`) so a minimal container without them falls back gracefully rather
  than mis-reading exit 127. Result: no `elan` "failed to parse release data" backtrace flood on a
  firewalled resume. (Lean still builds where the host is reachable.)
- **(C) Deduped the SessionStart beans surface** — kept the **CLI-independent**
  `session-start-coord-sweep.sh §4b` (parses `.beans/` directly; works in fresh containers) and
  retired the redundant CLI-dependent `session-status.sh` surface.

These are **interim, qou-local**. folio-assistant owns the permanent/generic versions below.

## 5. Tasks for folio-assistant (priority order)

### 5.1 Own the generic `bean-coordination` skill
qou's copy is a thin local pointer. Host the canonical **generic** bean-coordination skill in
folio-assistant and sync it back to qou via the nightly skill-sync.
**Acceptance:** qou's `bean-coordination.md` regenerates from folio-assistant source, not hand-maintained.

### 5.2 Own / generalize `install-beans.sh`
One source of truth for the installer; qou vendors or mirrors it.
**Acceptance:** qou's copy is identical-or-vendored from folio-assistant.

### 5.3 Provision the `beans` CLI in the MCP Docker image
Bake `beans` onto `PATH` in the assistant image (like the Lean oleans), so the deployed assistant
always has it. (No Dockerfile exists in qou — this is wholly yours.)
**Acceptance:** `beans list` works inside the running MCP container.

### 5.4 Repoint the remaining `todos/` → `.beans/` runtime readers
qou-side is **done** (§4). What remains is platform-layer or needs an owner decision:
- **MCP `/api/todos` route + `/todos` dashboard** — repoint the reader *before* relocating the
  `content-todos.ts` store, or the route 500s.
- **The 3 work-plan goal queues** (`1ppq-qbeta`, `lean-discharge`, `research`) — **done:** relocated
  `todos/` → `.beans/` as bulk JSON, with a mechanical repoint of all readers incl. the live
  `STATUS.md` links (kept bulk JSON per `beans ≠ sidecars`, not exploded into per-item beans).
- **The 1 QA sidecar** (`qa-q-CAL-1-2-3-audit.json`) — keep as bulk JSON; never `beans create`.
**Acceptance:** `todos/` holds only the TodoItem store (or is removed if that moves too); every
reader resolves against `.beans/`; `/api/todos` still serves; `coordinate.md` / `STATUS.md` links live.

### 5.5 Own the permanent SessionStart surface — consolidate to `beans prime`
`beans prime` "outputs instructions for AI coding agents." Wire it into the SessionStart hook (or the
assistant's system-prompt assembly) as the **single** permanent surface, replacing both qou interim
surfaces. **Keep a CLI-independent fallback** — fresh cloud containers routinely boot without the CLI
on `PATH`, and a surface that only runs `beans list` prints "not installed" in exactly the sessions
that most need the work-plan. (In the sandbox `beans prime` returned empty — confirm the pinned
version populates it.)
**Acceptance:** a fresh session — CLI present or not — is primed with the bean instructions + current
bean list without a manual `beans list`.

### 5.6 Own the generic session-start harness (the rest of the consolidation)
The SessionStart / PostToolUse / UserPromptSubmit hook chain is generic agent infra. Own the canonical
`settings.json` hook set + scripts and sync to qou, so a future platform-code move can't leave dangling
references again. Migrate the platform-specific hooks that `39fc90f6` deleted (folio-assistant open,
main-watch prompt, render-on-change, greeting) if they are still wanted — as folio-assistant-owned
scripts, wired from a folio-assistant-owned hook config.
**Acceptance:** qou's `.claude/settings.json` contains only physics/qou-specific hooks; the generic
agent-harness hooks are folio-assistant-owned and synced.

## 6. Cross-repo coordination

When folio-assistant lands §5.1–§5.6, update qou's `.claude/skills/local/bean-coordination.md`
ownership note and close the tracking beans (`j8el`, `bmwh`, `17ht`, `kpzd` finalize-workflows,
`d9nu` repo-cleanup). The 3 goal queues are now relocated to `.beans/` with readers repointed
(§5.4); **do not delete qou's remaining `todos/` files** (the QA sidecar `qa-q-CAL-1-2-3-audit.json`
and the `content-todos.ts` store) until their own readers are confirmed repointed.
