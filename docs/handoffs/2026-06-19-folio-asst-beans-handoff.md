# Handoff → folio-assistant agent: finish the beans / work-plan migration

**Date:** 2026-06-19 · **Updated:** 2026-06-20 (post #2495 + #2513 merge)
**From:** qou sessions `claude/modest-carson-xoqwps` (PR
[#2495](https://github.com/litlfred/qou/pull/2495)) +
`claude/beans-j8el-status-2026-06-20` (PR
[#2513](https://github.com/litlfred/qou/pull/2513))
**Re:** Folio-Assistant Infrastructure Migration — the `miga` epic
(`.beans/miga--folio-migration-parent.md`)
**Tracking beans:** `j8el` (qou-side `todos/`→`.beans/`, in-progress — closes
when the route-side lands), `bmwh` (this handoff finalize).

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

## Additional qou-side work (2026-06-20, owner override of the items 3–5 deferral)

The owner directed pulling the *systemic* enforcement into qou now (interim),
rather than waiting on the folio-assistant migration. Landed across PRs
[#2495](https://github.com/litlfred/qou/pull/2495) and
[#2513](https://github.com/litlfred/qou/pull/2513) (both **merged to `main`**):

- **Two SessionStart beans surfaces (both wired in `.claude/settings.json`)** —
  qou-side interim form of **item 5**:
  - `scripts/session-status.sh` — **CLI-based**: prints `beans list` (the rich
    tree) + the anti-stall directive. Falls back to "beans CLI not installed"
    when the CLI is absent.
  - `scripts/session-start-coord-sweep.sh` §4b — **CLI-independent**: parses
    `.beans/*.md` frontmatter directly (works in fresh cloud containers where
    the CLI is not installed) and prints the non-completed beans. Supports both
    bean file formats (`title:` field + filename id, and the older `id:` /
    `# Heading` shape). This pass also fixed two pre-existing bugs that aborted
    the whole coord-sweep hook once `main` was ahead (SIGPIPE on
    `git log | head`; errexit on a failing field grep).
  - **For folio-assistant:** these two overlap. Consolidate into the single
    permanent `beans prime` surface (item 5) and retire whichever interim
    surface is redundant. Keep a CLI-independent fallback — fresh containers
    routinely lack the CLI.
- **qa-drain writer repointed** (part of **item 4**) —
  `content/pipeline/qa-agent-drain-queue.ts` default `--out` moved `todos/` →
  `.beans/qa-agent-drain-queue.json` (tracked bulk JSON).
- **Watcher queues relocated** (the rest of **item 4**'s qou-side) — the 4
  committed `*-watcher-queue.json` files were `git mv`'d `todos/` → `.beans/`
  and **38 doc references repointed** across the integration-watcher skill
  family, `.claude/commands/*`, and CLAUDE.md's idle-trigger checklist.
  Verified **no `*.ts` code reads the watcher-queue paths**, so this did *not*
  touch the `/api/todos` route — disproving the route-coupling concern the
  original item 4 cited. `.gitignore` keeps `*-ledger.md` runtime logs ignored
  under `.beans/`; `*-queue.json` stay tracked.

Interim only — folio-assistant still owns the generic/permanent versions
(items 1–3, 5) per the `miga` "qou = physics-only" goal.

## Current state on `main` (2026-06-20, post #2495 + #2513) — read this first

The precise file inventory the folio-assistant agent inherits:

**`todos/` — 4 tracked files remain:**

| File | Class | Disposition |
|------|-------|-------------|
| `todos/1ppq-qbeta-queue.json` | work-plan goal queue | **may become beans** (item 4) |
| `todos/lean-discharge-queue.json` | work-plan goal queue | **may become beans** (item 4) |
| `todos/research-queue.json` | work-plan goal queue | **may become beans** (item 4) |
| `todos/qa-q-CAL-1-2-3-audit.json` | QA sidecar | **stays bulk JSON** (`beans ≠ sidecars`) — relocate to `.beans/` only if desired, never `beans create` |

These 4 are referenced by `coordinate.md` / `STATUS.md` via **live markdown
links**, so repointing their docs and relocating the files must happen in the
same change or the links break.

**`.beans/*.json` — 8 tracked bulk-JSON queues** (4 relocated watcher queues +
`paper-todos.json`, `qa-agent-drain-queue.json`, `simulator-qa-sidecar-queue.json`,
`status-section-audit.json`).

**Not present in the qou checkout** (so wholly folio-assistant-repo scope):
the MCP `/api/todos` route + `/todos` dashboard (no `todos/` reader found under
`folio-assistant/src/`), `check-todos.sh` (absent), and any Dockerfile.

**Still at `todos/` and deliberately NOT migrated here:** the `content-todos.ts`
TodoItem system (CLAUDE.md §4a keeps TodoItems in `todos/`; its `/api/todos`
route migration is folio-assistant's call).

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
(Confirmed 2026-06-20: there is **no Dockerfile in the qou repo** —
`**/Dockerfile*` matches nothing — so this is wholly folio-assistant's and
cannot be done qou-side.)

### 4. Repoint the `todos/` → `.beans/` runtime readers (the data migration)

**qou-side: DONE** (PRs #2495 / #2513). The 4 watcher queues are relocated to
`.beans/`, `qa-agent-drain-queue.ts` is repointed, and all 38 skill/command/
CLAUDE.md doc references were updated. Verified no `*.ts` code reads the watcher
paths.

**folio-assistant-side: remaining.** What is left lives in the platform layer
or needs an owner decision:

- **The MCP `/api/todos` route + `/todos` HTML dashboard** — not present in the
  qou checkout (no `todos/` reader under `folio-assistant/src/`), so this is
  entirely folio-assistant's. If/when the `content-todos.ts` TodoItem store
  moves, repoint this route. **Repoint the reader before relocating the data**,
  or the route 500s.
- **The 3 work-plan goal queues** still at `todos/` — `1ppq-qbeta-queue.json`,
  `lean-discharge-queue.json`, `research-queue.json`. These are work-plan scope
  and **may be converted to beans** (or relocated as bulk JSON). They are linked
  from `coordinate.md` / `STATUS.md`, so repoint those docs in the same change.
- **The 1 QA sidecar** `todos/qa-q-CAL-1-2-3-audit.json` — `beans ≠ sidecars`:
  keep as bulk JSON; relocate to `.beans/` only if you want co-location, never
  `beans create` it.
- **`check-todos.sh`** — absent from the qou repo; no action unless it exists in
  folio-assistant.

**Acceptance:** `todos/` holds only the `content-todos.ts` TodoItem store (or is
removed entirely if that store also moves); every former reader resolves against
`.beans/`; `/api/todos` still serves; `coordinate.md` / `STATUS.md` links are live.

### 5. Wire `beans prime` into the session-start surface
`beans prime` is designed to "output instructions for AI coding agents." Wire it
into the SessionStart hook (or the assistant's system-prompt assembly) so every
session is primed with current bean instructions automatically — instead of
relying on a static skill doc. (In this sandbox `beans prime` returned empty;
confirm the installed version populates it, or pin a version that does.)
**qou interim done 2026-06-20:** there are now **two** interim SessionStart
surfaces (see "Additional qou-side work" above) — `scripts/session-status.sh`
(CLI-based `beans list`) and `scripts/session-start-coord-sweep.sh` §4b
(CLI-independent `.beans/` parse). **Consolidate them** into the single
permanent `beans prime` surface and retire the redundant one, but **keep a
CLI-independent fallback** — fresh cloud containers routinely boot without the
`beans` CLI on `PATH`, and a surface that only runs `beans list` prints
"not installed" in exactly the sessions that most need the work-plan.
**Acceptance:** a fresh session — CLI present or not — is primed with the bean
instructions + current bean list without a manual `beans list`.

## Cross-repo coordination

When folio-assistant lands items 1–5, it should update qou's
`.claude/skills/local/bean-coordination.md` ownership note and close the
corresponding migration beans (`j8el` qou-side relocation, `bmwh` this handoff,
`kpzd` finalize-workflows, `d9nu` repo-cleanup). Do **not** delete qou's
remaining `todos/` files (the 3 goal queues, the QA sidecar, and the
`content-todos.ts` TodoItem store) until item 4's readers are confirmed
repointed — the goal queues are still linked from `coordinate.md` / `STATUS.md`.
