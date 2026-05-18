---
description: Dispatcher for the 3 integration watchers (proof / canonical / compute). With no arg, asks which to run; with args, dispatches the named watchers in parallel.
---

Run the **`local/integration-watch`** dispatcher skill against the
current branch / PR. The full protocol lives in
[`.claude/skills/local/integration-watch.md`](../skills/local/integration-watch.md);
this command is the user-invocable wrapper.

## Argument grammar

```
/integration-watch                      → ask which (no auto-pick)
/integration-watch proof                → proof-integration-watcher
/integration-watch canonical            → canonical-watcher
/integration-watch compute              → compute-integration-watcher
/integration-watch compute-integration  → same as `compute`
/integration-watch all                  → all three in parallel
/integration-watch proof,canonical      → those two in parallel
/integration-watch proof canonical      → same (space-separated)
/integration-watch <unknown>            → reject, re-prompt
```

## Watchers

- **proof** — `local/proof-integration-watcher`: no bare sorries,
  no axiom growth, naked-conjecture handling per §3b-cond.
- **canonical** — `local/canonical-watcher`: no 4th calibration,
  no numerology, no fits (per `prop:three-calibration-discipline`).
- **compute** — `local/compute-integration-watcher`: every `prop:`
  has a probe + production consumer (13-pattern I1-I13 audit).

## Role gating

- `reader`: `proof`, `canonical`, `both two` (compute hidden).
- `collaborator` / `owner`: all four chips including `compute` and
  `all three`.

## No-argument behaviour

Per `integration-watcher §0` + `§4e` (full-context preamble): emit
the preamble explaining the three QA axes, then `AskUserQuestion`
with role-gated chips (`multiSelect: true`). No silent default.

## Per-watcher dispatch sequence

For each resolved child watcher:

1. Run §5l Resume protocol — load persisted queue/ledger, compute
   unreviewed-commits list per criterion, surface a structured
   "resume" `AskUserQuestion` to the user.
2. Arm Monitor + subscribe to relevant PRs per
   `integration-watcher §2`.
3. The watcher runs continuously per §3-§5.

When multiple watchers run in parallel, each gets its OWN Monitor
task, its OWN `todos/<name>-queue.json` and
`todos/<name>-ledger.md`, and resume prompts surface one watcher
at a time (not bundled).

See the dispatcher skill for the full anti-pattern list — in
particular, no auto-pick on bare `/integration-watch`, no shared
state across watchers, no bundled resume prompts.
