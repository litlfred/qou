---
description: Dispatcher for the 4 integration watchers (proof / canonical / compute / detangler). With no arg, asks which to run; with args, dispatches the named watchers in parallel.
---

Run the **`local/integration-watch`** dispatcher skill against the
current branch / PR. The full protocol lives in
[`.claude/skills/local/integration-watch.md`](../skills/local/integration-watch.md);
this command is the user-invocable wrapper.

## Argument grammar

```
/integration-watch                              → ask which (no auto-pick)
/integration-watch proof                        → proof-integration-watcher
/integration-watch canonical                    → canonical-watcher
/integration-watch compute                      → compute-integration-watcher
/integration-watch compute-integration          → same as `compute`
/integration-watch detangler                    → detangler-integration-watcher
/integration-watch detanglement                 → same as `detangler`
/integration-watch all                          → all four in parallel
/integration-watch proof,canonical              → those two in parallel
/integration-watch proof canonical              → same (space-separated)
/integration-watch proof detanglement canonical → three in parallel
/integration-watch <unknown>                    → reject, re-prompt
```

## Watchers

- **proof** — `local/proof-integration-watcher`: no bare sorries,
  no axiom growth, naked-conjecture handling per §3b-cond.
- **canonical** — `local/canonical-watcher`: no 4th calibration,
  no numerology, no fits (per `prop:three-calibration-discipline`).
- **compute** — `local/compute-integration-watcher`: every `prop:`
  has a probe + production consumer (13-pattern I1-I13 audit).
- **detangler** — `local/detangler-integration-watcher`: no new
  forward references (H1-H7), sections in 3-18 block band (R1-R3),
  no new cross-chapter forward edges, archimedean wall preserved.

## Role gating

The no-arg `/integration-watch` `AskUserQuestion` is capped at 4
chips. With 4 watchers (proof / canonical / compute / detangler) +
an "all" option totalling 5 logical choices, the chip set is
trimmed to fit:

- **`reader`**: 4 chips (compute hidden) — `proof`, `canonical`,
  `detangler`, `all readable three`.
- **`collaborator` / `owner`**: 4 chips — `proof`, `canonical`,
  `detangler`, `all four`. The individual `compute` chip is
  dropped; compute is still reachable via the `all four` chip
  (which includes it) or by typing `/integration-watch compute`
  directly with the argument grammar above.

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
task, its OWN `.beans/<name>-queue.json` and
`.beans/<name>-ledger.md`, and resume prompts surface one watcher
at a time (not bundled).

See the dispatcher skill for the full anti-pattern list — in
particular, no auto-pick on bare `/integration-watch`, no shared
state across watchers, no bundled resume prompts.
