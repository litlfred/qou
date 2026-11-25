---
name: integration-watch
roles: [reader, collaborator, owner]
user_invocable: true
description: >
  Dispatcher for the `/integration-watch` slash command. Routes to
  one or more of the six concrete integration watchers / audits
  (proof-integration-watcher, canonical-watcher,
  compute-integration-watcher, detangler-integration-watcher,
  one-voice-integration-watcher, proposition-consolidation-audit).
  With no argument, lists the available watchers and asks the user
  which to invoke. With arguments, dispatches the named watchers
  in parallel (each gets its own Monitor, queue, ledger, and
  PR-subscription set).
allowed-tools: Read Edit Write Bash Grep Glob Agent Monitor Skill
---

# /integration-watch — dispatcher for the 5 integration watchers

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
/integration-watch one-voice                    → just one-voice-integration-watcher
/integration-watch voice                        → same as `one-voice`
/integration-watch consolidation                → proposition-consolidation-audit (find similar props)
/integration-watch dedupe                       → same as `consolidation`
/integration-watch bibliography                 → bibliography watcher (block-level bib QA)
/integration-watch bib                          → same as `bibliography`
/integration-watch q-usage                      → q-usage watcher (per-block q regime + chapter-mismatch)
/integration-watch q                            → same as `q-usage`
/integration-watch devils-advocate              → devils-advocate-watcher (adversarial "why is this wrong" review)
/integration-watch da                           → same as `devils-advocate`
/integration-watch adversarial                  → same as `devils-advocate`
/integration-watch all                          → all watchers in parallel
/integration-watch proof,canonical              → those two in parallel
/integration-watch proof canonical              → same (space-separated)
/integration-watch proof detanglement canonical → three in parallel
/integration-watch <unknown>                    → reject, re-prompt
```

## No-argument behaviour (the common case)

Per `integration-watcher §0` + `§4e` (full-context preamble):

1. **Chat preamble** (always before the AskUserQuestion):

   > The five watchers each cover one QA axis. Run them
   > independently (one focused PR per watcher's domain) or all
   > five in parallel (more events but full coverage).
   >
   > - **proof** — proof-integration-watcher: no bare sorries,
   >   no axiom growth, lean-lsp compile check, naked-conjecture
   >   handling per §3b-cond.
   > - **canonical** — canonical-watcher: no 4th calibration,
   >   no numerology, no fits (per `prop:three-calibration-discipline`).
   > - **compute** — compute-integration-watcher: every `prop:`
   >   has a probe + production consumer (13-pattern I1-I13 audit).
   > - **detangler** — detangler-integration-watcher: no new
   >   forward refs (H1-H7), sections in 3-18 block band (R1-R3),
   >   no new cross-chapter forward edges, archimedean wall
   >   preserved.
   > - **one-voice** — one-voice-integration-watcher: scholarly
   >   voice (narrative + proof bodies), no AI slop, block fit
   >   to section/chapter, canonical-vs-deprecated notation,
   >   archimedean/algebraic wall placement. Persists per-block
   >   `<block>.qa.json` audit reports (multi-reviewer, hash-keyed
   >   staleness).
   > - **consolidation** — proposition-consolidation-audit: find
   >   similar propositions/theorems/lemmas that should be merged or
   >   demoted to corollaries (H1: explicit "specialisation of"
   >   wording; H2: same boxed equation under different
   >   parametrisations; H3: uses-overlap > 70%). Helps keep
   >   exposition tight (simply-stated theorems + simple corollaries
   >   rather than a forest of overlapping special-case props).
   > - **q-usage** — q-usage-watcher: per-block q-regime detector
   >   (symbolic / generic-R / real-positive / q > 1 / |q| > 1 /
   >   unit-circle / root-of-unity / fixed q_0 / n/a) + chapter-
   >   mismatch flagger. Catches: fixed-q_0 leak into a categorical
   >   chapter, `Real.*` archimedean leak into a generic-R block,
   >   `Real.sqrt q` without `0 < q` hypothesis, root-of-unity
   >   construction without declaration, formal-power-series prose
   >   using `q > 1` instead of `|q| > 1`. Emits per-block sidecars
   >   (`q-usage-*` criteria) and a global witness JSON.
   > - **devils-advocate** — devils-advocate-watcher: for every
   >   block + Lean sibling, construct the strongest case it is
   >   WRONG (the objection a hostile-but-competent referee raises),
   >   fanning out four adversarial-lens agents (formalist /
   >   skeptical physicist / algebraist / reproducibility-citation)
   >   + an adjudicator that scores each objection
   >   surviving/rebutted/partial. Emits per-block `da-*` sidecars
   >   (12 finding kinds + `da-referee-verdict`). Gated by the
   >   (a)/(b) refutation-scope rule + corpus-grep checklist so it
   >   predicts real referee objections without crying wolf on
   >   settled items.

2. **Role-gate the chip set.** Before composing the
   `AskUserQuestion`, detect the user's role (`reader` /
   `collaborator` / `owner`). The `compute` and `one-voice`
   chips require `collaborator`+ (the child skills' role gates);
   the `all` chip transitively requires `collaborator`+ because
   it includes compute + one-voice. `proof`, `canonical`, and
   `detangler` are `reader`-accessible (read-only audit skills).

   AskUserQuestion has a 4-option cap. With six candidates
   (`proof`, `canonical`, `detangler`, `compute`, `one-voice`,
   `all`), the chip set is composed as:

   - **reader**: `proof`, `canonical`, `detangler`,
     `all readable three` — `compute`, `one-voice`, and `all`
     hidden (each requires collaborator+).
   - **collaborator / owner**: prefer the umbrella + the two
     read-only watchers most relevant to the current session
     (`proof`, `canonical`, `one-voice`, `all`). `compute` and
     `detangler` reachable via direct slash invocation or via
     `all`. The dispatcher MAY rotate which two individual
     watchers are surfaced based on session context (e.g. when
     a `.lean` change just landed, surface `proof` + `one-voice`;
     when a `prop:` block was added, surface `compute` +
     `canonical`).

3. **AskUserQuestion** with up to 4 chips (role-gated):

   - Header `Which watcher`, question `Which integration watcher(s) to invoke?`
   - Options (collaborator / owner default chip set):
     - `proof` — proof QA (any role)
     - `canonical` — canonical-derivation discipline (any role)
     - `one-voice` — scholarly voice + AI-slop + fit + framework + wall (collaborator+)
     - `all five` — parallel dispatch (collaborator+ since all
       includes compute + one-voice)
     - **Note**: `compute` and `detangler` reachable via direct
       invocation (`/integration-watch compute`) or via `all five`.
   - Options (when role = reader):
     - `proof` — proof QA
     - `canonical` — canonical-derivation discipline
     - `detangler` — structural QA
     - `all readable three` — parallel proof + canonical + detangler
     - (compute / one-voice / all-five hidden)

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
- Each maintains its OWN `.beans/<name>-queue.json` and
  `.beans/<name>-ledger.md`.
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
  `local/detangler-integration-watcher`,
  `local/one-voice-integration-watcher`,
  `local/proposition-consolidation-audit`,
  `local/devils-advocate-watcher`
- **Inherits everything**: §0-§9 of the parent
- **Write-side counterpart**: [`local/integration-backlog`](integration-backlog.md)
  — same argument grammar, but DRAINS the open findings into
  review-sized PRs instead of monitoring for new events.

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
