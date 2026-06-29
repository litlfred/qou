<!--
READY-TO-FILE ISSUE for litlfred/folio-assistant.
Paste the title + body below into a new issue. Blob links point at the
qou branch claude/trusting-bell-ere7f6; repoint to main once merged.
This session is scoped to litlfred/qou only, so it could not file the
issue directly.
-->

# Title

Migrate platform skills out of `qou` into folio-assistant (core + paper-adapter bundles)

# Body

## Summary

`litlfred/qou` carries ~95 `.claude/skills/local/*.md` skills plus a typed
`framework / actors / capabilities / requirements / roles` layer. Per
`scripts/setup-folio-assistant.sh`, **qou is content-only** — the pipeline,
schemas, LaTeX renderer, viewer, and the paper adapter all live here in
folio-assistant. Most of those skills are therefore platform infrastructure
that belongs in folio-assistant and should be synced back into qou (and
ugb / fred2005), not maintained per-paper.

Full per-skill classification:
https://github.com/litlfred/qou/blob/claude/trusting-bell-ere7f6/docs/audits/2026-06-29-skills-folio-assistant-classification.md

## Why now

- The framework layer is already half-migrated: `framework/package-manifest.ts`
  re-exports from `folio-assistant/schemas/`.
- The 2026-06-19 folio-assistant handoff (§5.1) already committed to hosting
  the canonical generic `bean-coordination` skill here and syncing it back.
- The archived `qou` `FOLIO_MIGRATION_PLAN.md` Skills Audit is stale (predates
  ~70 current skills) and mis-files `content-validation` / `latex-validation` /
  `content-block-review` as content-repo skills — they invoke schema + renderer
  that live here, so they should move.

## Proposed buckets

**Tier 1 — folio-assistant CORE (content-agnostic):** bean-coordination,
todo-manager, session-intent, pending-show, idle-backlog, continual-progress,
coordinate, watch, pickup, prepare-merge(-auto), delivery-summary, diff,
integration-watch / -watcher / -audit / -backlog, deployment-auth, todo-review,
docs-generation, test-engineer, glossary-build, block-density, content-graph,
chapter-complexity-review, markdown-render-check, html-rendering-qc,
readability-editing, md-authoring, bib-qa / bib-human-review /
bib-photo-ingestion-watcher, one-voice-audit / -integration-watcher,
devils-advocate-watcher.

**Tier 2 — folio-assistant PAPER-ADAPTER (formal-math, domain-agnostic):**
all lean-* and proof-* skills, category-theory, content-validation,
content-block-review, latex-validation, latex-build-cache, rendering-auditor /
-fixes, critical-path-analysis, chapter-analysis, paper-importer,
document-intake, simulator / simulator-math-audit, definition-clarity-audit,
proposition-consolidation-audit, remark-audit.

**Tier 3 — stays in qou (QOU physics):** canonical-watcher,
production-vs-exploratory-discipline, compute-integration-watcher,
verify-local-substrate, q-usage-watcher, lean-q-substitution,
lean-substrate-numerics, witnessed-values.

**Hybrid (split mechanism→here / data→qou):** editor, scientific-accuracy,
ontologist, one-voice-style-guide, compute-author, compute-audit,
ffi-roundtrip-audit, detangler-integration-watcher, symbiotic-interaction,
groebner-basis.

**Framework layer → here:** `framework/types.ts`, `actors/`, `capabilities/`,
generic `requirements/` (`sorry-citation` → paper adapter). The `RoleAssignments`
*type* moves; qou keeps `registry.ts` + `roles/role-assignments.ts` as its
instance manifest.

## Mechanism

Host the canonical skills here; add two `mode:"sync"` packages
(`folio-core`, `folio-paper-adapter`) to qou's `skills-config.json`, synced
nightly into `.claude/skills/<pkg>/`. qou's `local/` then holds only Tier 3 +
hybrid shims.

## Source files (qou, branch `claude/trusting-bell-ere7f6`)

- Classification doc: https://github.com/litlfred/qou/blob/claude/trusting-bell-ere7f6/docs/audits/2026-06-29-skills-folio-assistant-classification.md
- Skill registry: https://github.com/litlfred/qou/blob/claude/trusting-bell-ere7f6/.claude/skills/registry.ts
- Framework types: https://github.com/litlfred/qou/blob/claude/trusting-bell-ere7f6/.claude/skills/framework/types.ts
- Package manifest (already re-exports folio): https://github.com/litlfred/qou/blob/claude/trusting-bell-ere7f6/.claude/skills/framework/package-manifest.ts
- Actors: https://github.com/litlfred/qou/tree/claude/trusting-bell-ere7f6/.claude/skills/actors
- Capabilities: https://github.com/litlfred/qou/tree/claude/trusting-bell-ere7f6/.claude/skills/capabilities
- Requirements: https://github.com/litlfred/qou/tree/claude/trusting-bell-ere7f6/.claude/skills/requirements
- Role assignments: https://github.com/litlfred/qou/blob/claude/trusting-bell-ere7f6/.claude/skills/roles/role-assignments.ts
- Local skills dir: https://github.com/litlfred/qou/tree/claude/trusting-bell-ere7f6/.claude/skills/local
- skills-config.json: https://github.com/litlfred/qou/blob/claude/trusting-bell-ere7f6/skills-config.json
- setup-folio-assistant.sh: https://github.com/litlfred/qou/blob/claude/trusting-bell-ere7f6/scripts/setup-folio-assistant.sh
