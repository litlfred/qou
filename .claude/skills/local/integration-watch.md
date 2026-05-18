---
name: integration-watch
roles: [reader, collaborator, owner]
user_invocable: true
description: >
  Dispatcher for the `/integration-watch` slash command. Routes to
  one or more of the four concrete integration watchers
  (proof-integration-watcher, canonical-watcher,
  compute-integration-watcher, detangler-integration-watcher).
  With no argument, lists the available watchers and asks the user
  which to invoke. With arguments, dispatches the named watchers
  in parallel (each gets its own Monitor, queue, ledger, and
  PR-subscription set).
allowed-tools: Read Edit Write Bash Grep Glob Agent Monitor Skill
---

# /integration-watch — dispatcher for the 4 integration watchers

A thin dispatcher in front of [`local/integration-watcher`](integration-watcher.md)
§0 (Invocation). When the user types `/integration-watch` (with or
without arguments), this skill resolves the argument to one or
more concrete child watchers and invokes them.

## Argument grammar

```
/integration-watch                              → ask which (no auto-pick)
/integration-watch proof                        → just proof-integration-watcher
/integration-watch canonical                    → just canonical-watcher
/integration-watch compute                      → just compute-integration-watcher
/integration-watch compute-integration          → same as `compute`
/integration-watch detangler                    → just detangler-integration-watcher
/integration-watch detanglement                 → same as `detangler`
/integration-watch all                          → all four in parallel
/integration-watch proof,canonical              → those two in parallel
/integration-watch proof canonical              → same (space-separated)
/integration-watch proof detanglement canonical → three in parallel
/integration-watch <unknown>                    → reject, re-prompt
```

## No-argument behaviour (the common case)

Per `integration-watcher §0` + `§4e` (full-context preamble):

1. **Chat preamble** (always before the AskUserQuestion):

   > The four watchers each cover one QA axis. Run them
   > independently (one focused PR per watcher's domain) or all
   > four in parallel (more events but full coverage).
   >
   > - **proof** — proof-integration-watcher: no bare sorries,
   >   no axiom growth, naked-conjecture handling per §3b-cond.
   > - **canonical** — canonical-watcher: no 4th calibration,
   >   no numerology, no fits (per `prop:three-calibration-discipline`).
   > - **compute** — compute-integration-watcher: every `prop:`
   >   has a probe + production consumer (13-pattern I1-I13 audit).
   > - **detangler** — detangler-integration-watcher: no new
   >   forward refs (H1-H7), sections in 3-18 block band (R1-R3),
   >   no new cross-chapter forward edges, archimedean wall
   >   preserved.

2. **Role-gate the chip set.** Before composing the
   `AskUserQuestion`, detect the user's role (`reader` /
   `collaborator` / `owner`). The `compute` chip requires
   `collaborator`+ (the child skill's role gate); the `all` chip
   transitively requires `collaborator`+ because it includes
   compute. `detangler` is `reader`-accessible (read-only audit
   skill). For a `reader` invocation:

   - Either **hide** the `compute` chip and replace `all four`
     with `all readable three` (proof + canonical + detangler), OR
   - **Annotate** the chip with `(needs collaborator)` and reject
     the selection at dispatch time with a re-prompt explaining
     the role gate.

   Default behaviour: hide `compute` from `reader`s entirely;
   annotate for `collaborator`+ (no annotation needed; chips are
   already accessible). AskUserQuestion's 4-option cap means
   `reader` and `collaborator` chip sets are sized exactly to fit
   (3 individuals + 1 "all" each).

3. **AskUserQuestion** with up to 4 chips (role-gated):

   - Header `Which watcher`, question `Which integration watcher(s) to invoke?`
   - Options (when role ≥ collaborator) — pick 4 of 5:
     - `proof` — proof QA (any role)
     - `canonical` — canonical-derivation discipline (any role)
     - `detangler` — structural QA (graph + density)
     - `compute` — compute-wiring completeness (collaborator+)
     - `all four` — parallel dispatch (collaborator+ since all
       includes compute)
     - **Note**: when 5 candidates exceed the 4-cap, drop the
       individual `compute` chip in favour of `all four` (compute
       is reachable via `all four` or `/integration-watch compute`).
   - Options (when role = reader):
     - `proof` — proof QA
     - `canonical` — canonical-derivation discipline
     - `detangler` — structural QA
     - `all readable three` — parallel proof + canonical + detangler
     - (compute / all-four hidden)

   `multiSelect: true` so the user can pick any subset.

## Per-watcher dispatch sequence

For each resolved child watcher:

1. **Run §5l Resume protocol** (from the parent skill) — load
   the persisted queue/ledger, compute the unreviewed-commits
   list per criterion, surface a structured "resume" summary
   + AskUserQuestion to the user.
2. **Arm Monitor** + **subscribe to PRs** per `integration-watcher §2`.
3. The watcher runs continuously per §3-§5.

When multiple watchers are dispatched in parallel:
- Each gets its OWN Monitor task (so timeouts/restarts are
  independent).
- Each maintains its OWN `todos/<name>-queue.json` and
  `todos/<name>-ledger.md`.
- PR subscriptions are deduped across watchers (a sibling PR
  active in the last 7 days is subscribed only once per
  session).
- Resume suggestions are surfaced one watcher at a time (not
  bundled), so the user can answer each separately.

## Integration

- **Built on**: `local/integration-watcher` (the abstract parent)
- **Dispatches to**: `local/proof-integration-watcher`,
  `local/canonical-watcher`,
  `local/compute-integration-watcher`,
  `local/detangler-integration-watcher`
- **Inherits everything**: §0-§9 of the parent

## Examples

```
User: /integration-watch
→ Preamble + 4-chip AskUserQuestion; user picks one or more.

User: /integration-watch proof
→ Direct dispatch to proof-integration-watcher; resume protocol
  runs and surfaces "Triage unreviewed commits / Continue backlog
  / Dispatch chapter / Just watch" 4-chip AskUserQuestion.

User: /integration-watch detangler
→ Direct dispatch to detangler-integration-watcher; resume protocol
  runs (graph baseline cached, structural QA dispatch).

User: /integration-watch proof detanglement canonical
→ Parallel dispatch to three (detanglement charitably maps to
  detangler); each surfaces its own resume prompt sequentially,
  or one consolidated prompt when fresh-session state is identical.

User: /integration-watch all
→ Parallel dispatch to all four; each surfaces its own resume
  prompt sequentially (proof, canonical, detangler, compute).
```

## Anti-patterns

- ❌ Auto-pick on `/integration-watch` (no arg). The user must
  choose; defaulting silently hides which watcher started.
- ❌ Share state across watchers. Each domain is independent;
  cross-watcher state would create false-positive duplicate
  findings.
- ❌ Bundle the per-watcher resume prompts into a single mega-
  question. Each watcher's resume answers are independent and
  the AskUserQuestion 4-option cap means combining them loses
  resolution.
