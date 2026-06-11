# Gemini CLI — Quantum Observable Universe

## Claude Infrastructure Integration

This repository uses a set of Claude-specific commands and skills for maintenance and QA. As the Gemini agent, I should be aware of these and know how to invoke them via the CLI.

### Integration Audit
**Command:** `/integration-audit [axis|criterion|all]`
**CLI:** `bun run content/pipeline/integration-audit.ts content/ --all [--include-agent]`
- **Purpose:** Invalidates cached script (and optionally agent) reviewer entries in `.qa.json` sidecars and re-runs `qa-sweep`.
- **Use when:** Checker logic changes, Mathlib/Lean version bumps, or periodic re-validation is needed.
- **Gemini Note:** Use `--include-agent` to invalidate reviews made by AI agents (including me).
- **Ledger:** Logs entries to `todos/integration-audit-ledger.md`.

### Agent Review Drain
**CLI:** `bun run content/pipeline/qa-agent-drain-queue.ts content/`
- **Purpose:** Generates a queue of missing agent/human reviews in `todos/qa-agent-drain-queue.json`.
- **Gemini Note:** After an audit with `--include-agent`, this queue will be large. Focus on `proof-narrative-lean-equiv` and `voice-*` axes.

### Integration Watch
**Command:** `/integration-watch`
- **Purpose:** Monitor QA sidecars for new findings or changes.

### Integration Backlog
**Command:** `/integration-backlog`
- **Purpose:** Drain QA findings into actionable PRs or todos.

### Compute Code Review (DEEP)
**Skill:** `local/compute-code-review`
- **Purpose:** Thorough code-review of assets (Lean, Python, Rust) + Paper Contextualization.
- **Workflow:** Narrative Check -> Code Review -> GitHub Issue (`gh`) -> QA Sidecar.
- **Model Preference:** Gemini 3.5 Pro Preview or greater (DO NOT use Flash).
- **Audit Depth:** Must verify both code correctness and alignment with the paper's mathematical claims.

### QOU Canonical Standards
**Skill:** `local/qou-canonical-code-review`
- **Purpose:** Strict enforcement of QOU engineering standards (precision, constants, traceability).
- **Key Rules:** No native floats, no hardcoded constants, mandatory `# Ref: prop:ID` links.

### Coordinate
**Command:** `/coordinate`
- **Purpose:** Manage branch and PR coordination across multiple agent sessions.

## Project Conventions

- **QA Sidecars:** Every content file (e.g., `chapter.md`) has a corresponding `chapter.qa.json` sidecar.
- **Reviewer Kinds:** `script` (automated checkers), `agent` (AI reviews), `human` (manual verification).
- **Accessibility:** The user types with difficulty. Prefer numbered choices, proactive action, and rich context for decisions.
- **Work-plan:** Maintain a prioritized work-plan in `todos/` (or as a session-start todo list).

## Useful Paths

- `.claude/commands/`: Command definitions (Markdown).
- `.claude/skills/`: Skill logic and registry.
- `pipeline/`: Implementation scripts for QA and audit tasks.
- `content/`: Authoritative source files.
- `docs/audits/`: Historical audit reports.
