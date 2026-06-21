---
description: Drain the integration-watcher backlog into reviewable PRs. Clusters open findings into ≤ 49-file batches (Gemini review limit), creates a PR per batch, runs prepare-merge, addresses comments, merges, repeats until the axis is clear. With no arg, asks which axis.
---

Run the **`local/integration-backlog`** dispatcher skill against the
current paper's QA sidecars. The full protocol lives in
[`.claude/skills/local/integration-backlog.md`](../skills/local/integration-backlog.md);
this command is the user-invocable wrapper.

## Argument grammar

```
/integration-backlog                              → ask which axis
/integration-backlog one-voice                    → drain voice + fit + framework + wall
/integration-backlog proof                        → drain 5+ proof criteria
/integration-backlog canonical                    → drain canonical-discipline
/integration-backlog compute                      → drain 13-pattern wiring
/integration-backlog detangler                    → drain structural
/integration-backlog bibliography                 → drain block-level bib QA
/integration-backlog all                          → drain every axis in priority order
/integration-backlog proof,canonical              → those two in sequence
/integration-backlog voice-emoji-content          → just that one criterion
/integration-backlog <unknown>                    → reject, re-prompt
```

## What it does

For each chosen axis:

1. **Read sidecars** — query every `.qa.json` whose criteria for
   this axis include a fresh `result: "fail"` entry. The fresh
   set is the open backlog.
2. **Cluster** — group fails into ≤ 49-file batches (Gemini's
   review limit). Prefer batches whose blocks share a chapter or
   theme; cap each batch at a reasonable scope.
3. **Per batch**:
   - Create a fresh branch `claude/qa-backlog-<axis>-<theme>-YYYY-MM-DD`.
   - Apply the mechanical fix (script-driven where possible; agent
     dispatch for the rest).
   - Run `/prepare-merge` (rebase + validation + push).
   - Open PR, request Gemini + Copilot review.
   - Address review comments using structured `AskUserQuestion`
     when author input is needed.
   - Merge once comments resolved.
4. **Repeat** the batch loop until the axis is clear (no fresh
   fails remain) OR the user halts.

## Loop coordination

- Each batch is its own PR. Multiple batches can be in flight at
  once, but only one is on the user-attention surface at a time.
- After each merge, `/integration-audit <axis>` is invoked
  automatically to refresh sidecar state.
- Progress is logged to `.beans/<axis>-integration-backlog-ledger.md`.

## Sibling commands

| Command | Direction | Mutates sidecars? |
|---------|-----------|-------------------|
| `/integration-watch` | read — monitor | no |
| **`/integration-backlog`** | **write — drain findings** | **indirectly (via PR merges)** |
| `/integration-audit` | maintenance — invalidate + re-audit | directly |

## No-argument behaviour

`AskUserQuestion` 🟡 with chips for each axis + `all`. Multi-select
so the user can pick e.g. `voice, proof` to drain both in
sequence.

## When NOT to use

- For a single one-off fix — just edit the file directly.
- When the backlog is < 5 fails per axis — too small to warrant
  the batch infrastructure; use `/integration-audit` to refresh
  + edit directly.
- When the user wants synchronous attention to each finding —
  this loop is asynchronous (multiple PRs).
