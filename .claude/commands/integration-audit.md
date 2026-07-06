---
description: Sidecar-invalidation maintenance — drops cached script-reviewer entries for one or more criteria (or whole axes) and auto re-runs qa-sweep. Use after a checker bug fix, a registry update, or a Mathlib bump. With no arg, asks which axis / criterion.
---

Run the **`local/integration-audit`** maintenance skill against the
current paper's QA sidecars. The full protocol lives in
[`.claude/skills/local/integration-audit.md`](../skills/local/integration-audit.md);
this command is the user-invocable wrapper.

## Argument grammar

```
/integration-audit                                 → ask which axis / criterion
/integration-audit one-voice                       → invalidate all one-voice entries
/integration-audit proof                           → invalidate all proof entries
/integration-audit canonical                       → invalidate all canonical entries
/integration-audit compute                         → invalidate all compute entries
/integration-audit detangler                       → invalidate all detangler entries
/integration-audit bibliography                    → invalidate all bibliography entries
/integration-audit all                             → invalidate every criterion across all axes
/integration-audit voice-emoji-content             → just that one criterion
/integration-audit voice-emoji-content,bib-cite-resolves
                                                   → multiple criteria, comma-separated
/integration-audit <unknown>                       → reject, re-prompt
```

Args are validated against `qa-criteria-registry.ts` and
`WATCHER_CRITERIA_BY_AXIS`. Unknown IDs are rejected with a list
of valid IDs.

## What it does

1. Walks every `.qa.json` sidecar under
   `content/<paper>/`.
2. For each criterion in the invalidation set:
   - Deletes every `kind: "script"` reviewer entry.
   - With `--include-agent`: also deletes `kind: "agent"` entries.
   - **Always preserves** `kind: "human"` entries.
3. Re-runs `qa-sweep --only <criterion-list>` as a child process
   to repopulate sidecars with fresh entries (unless `--no-sweep`
   or `--dry-run`).
4. Surfaces the delta (e.g. `voice-emoji-content: 8 → 11 fails`).
5. Appends a ledger entry to `.beans/integration-audit-ledger.md`.

## When to invoke

- After a checker bug fix (downstream "fresh" entries are now wrong)
- After a registry update (new criterion that existing sidecars
  don't include)
- After a Mathlib / Lean toolchain bump
- For periodic re-validation

## No-argument behaviour

Per AGENTS.md user-accessibility (multi-select default):
`AskUserQuestion` 🟡 with chips for each axis + `all`. Multi-select
so the user can pick e.g. `proof, canonical` in one go.

## Sibling commands

| Command | Direction | Mutates sidecars? |
|---------|-----------|-------------------|
| `/integration-watch` | read — monitor | no |
| `/integration-backlog` | write — drain findings | indirectly (via PR merges) |
| **`/integration-audit`** | **maintenance — invalidate + re-audit** | **directly** |

The three together form a closed loop: audit (invalidate + sweep)
→ watch (notice findings) → backlog (drain to PRs).

## CLI passthrough

For non-interactive use, invoke the CLI directly:

```bash
bun run pipeline/integration-audit.ts <content-root> --axis one-voice
bun run pipeline/integration-audit.ts <content-root> --criteria voice-emoji-content
bun run pipeline/integration-audit.ts <content-root> --all --dry-run
```

Flags: `--criteria ID,ID | --axis NAME,NAME | --all`, `--dry-run`,
`--include-agent`, `--json`, `--no-sweep`.
