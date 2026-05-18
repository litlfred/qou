---
name: proof-integration-watcher
roles: [reader, collaborator, owner]
description: >
  Watch incoming activity (origin/main + open active PRs + newly-opened
  PRs) for narrative-proof (`.md`) or Lean-proof (`.lean`) content; run
  the proof QA skill suite on every detected change; queue gaps;
  attempt easy discharges (sorries, naked conjectures with provable
  scaffolding); ask the author for help on the rest. When idle, sweep
  the existing content backlog with the same pipeline. Drive toward the
  goal — no bare sorries, no axiom growth, no conjecture placeholders
  for derivable results.
allowed-tools: Read Edit Write Bash Grep Glob Agent Monitor Skill
user_invocable: true
---

# /proof-integration-watcher

A proof-focused superset of `/watch` + `/coordinate`. Combines:

| Capability | Skill it builds on |
|------------|--------------------|
| Background watch of `origin/main` (Monitor poll) | `local/watch` §1–§2 |
| Subscribe to **own PR** and **all sibling PRs with activity in the last 7 days** | `mcp__github__subscribe_pr_activity` |
| Auto-subscribe to **newly-opened PRs** as they appear | `mcp__github__list_pull_requests` + subscribe |
| Per-event **proof QA pipeline** (narrative + Lean) | `proof-editor` (coordinator) |
| Gap **queue** + **author escalation** | this skill |
| Idle **backlog sweep** of existing content | this skill |

**Goal (driving function):** no bare `sorry`, no new axioms beyond
the accepted set, and no naked `conjecture` blocks whose downstream
scaffolding is actually provable. Conjectures that genuinely need
axiomatisation as Lean classes (CLAUDE.md §3b-cond) are fine.

## When to invoke

- User says: *"watch proofs"*, *"watch for proof integration"*,
  *"proof watcher"*, *"keep checking for proof gaps"*,
  *"chase down sorries"*.
- Automatically at session start when the branch name contains
  `proof-integration` (this skill's home branch).
- As a sibling-task launched by `/coordinate` when the session also
  needs multi-PR awareness.
- **Do not** invoke for one-shot reviews — use `proof-editor` directly.

## Inputs

- The user's PR number (own PR) — if the branch isn't pushed yet,
  push and open it first, then re-enter the §3 subscription step.
- (Optional) explicit list of PRs to watch. Default: every open PR in
  `litlfred/qou` updated in the last 7 calendar days.
- (Optional) explicit content scope for the idle backlog sweep.
  Default: every block under `content/**/*.{ts,md,lean}` not audited
  by this skill in the last 7 days.

## 1. Baseline + setup (run once per session)

```bash
# Repo identity — declared once, referenced everywhere below
OWNER=litlfred
REPO=qou

# Bootstrap the queue + ledger (gitignored)
mkdir -p todos
[ -f todos/proof-integration-queue.json ] || echo '{"items":[],"audited":{}}' > todos/proof-integration-queue.json
[ -f todos/proof-integration-watcher-ledger.md ] || cat > todos/proof-integration-watcher-ledger.md <<'EOF'
# Proof Integration Watcher — session ledger

| ts (UTC) | event | scope | findings | action |
|----------|-------|-------|----------|--------|
EOF

# Stash main baseline so §5 timeout-recovery can diff cleanly
git fetch origin main 2>/dev/null
git rev-parse origin/main > /tmp/_proof_watcher_main.sha
```

The queue file shape:

```json
{
  "items": [
    {
      "id": "<sha1-12 of block-label + finding-class>",
      "block": "prop:foo-bar",
      "paths": { "ts": "...", "md": "...", "lean": "..." },
      "finding": "uncited-sorry | hidden-axiom | class-A-stub | naked-conjecture | gap-existence | gap-uniqueness | inter-proof-bridge | drift-class-B | drift-class-C | drift-class-D",
      "severity": "critical | major | minor",
      "source": "watch:main:<sha> | watch:pr:<N>:<event-ts> | backlog",
      "attempts": [ { "ts": "...", "tactic": "lean_multi_attempt:[simp,ring,linarith]", "outcome": "fail|partial|ok" } ],
      "status": "queued | in-progress | resolved | needs-author | wontfix",
      "asked_author_at": null
    }
  ],
  "audited": {
    "<block-label>": "<ISO-8601 ts of last audit pass>"
  }
}
```

`audited[]` is the per-block last-pass timestamp; the idle backlog
sweep skips blocks audited within the last 7 days unless their
`.{ts,md,lean}` siblings have a newer mtime.

## 2. Active watching

### 2a. Watch `origin/main` (Monitor poll)

Arm exactly **one** persistent Monitor per session. Each new commit
line triggers the §4 per-event pipeline.

```
Monitor:
  description: "origin/main new commits — proof-integration-watcher"
  persistent: true
  command: |
    last=$(git ls-remote origin main | cut -f1)
    while true; do
      cur=$(git ls-remote origin main 2>/dev/null | cut -f1)
      if [ -n "$cur" ] && [ "$cur" != "$last" ]; then
        git fetch origin main 2>/dev/null
        # Emit every new commit — never `head -N` here, or we silently
        # drop the tail of a fast burst and lose audit events. Use a
        # tight grep --line-buffered filter downstream if needed.
        git log --reverse --format='MAIN %H %s' "$last..$cur"
        last=$cur
      fi
      # Every 5 min — also re-list open PRs to catch new ones
      gh_now=$(date -u +%s)
      if [ -z "$last_pr_check" ] || [ $((gh_now - last_pr_check)) -gt 300 ]; then
        printf 'TICK %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
        last_pr_check=$gh_now
      fi
      sleep 300
    done
```

The `TICK` line is intentional — it gives the foreground agent a
heartbeat to (a) re-list open PRs and subscribe to any new ones, and
(b) pull an idle-backlog item if the queue had no incoming events
in the last interval.

If the Monitor reports `[Monitor timed out — re-arm if needed]`, apply
the **watch.md §5b** timeout-recovery procedure (compare baseline SHA
against current `origin/main`, walk the missed range) before re-arming.

### 2b. Subscribe to PRs

**At setup:** subscribe to (a) own PR (if pushed) and (b) every open PR
in the repo updated in the last 7 days.

```python
# OWNER/REPO declared once in §1 — referenced everywhere below
OWNER, REPO = "litlfred", "qou"

# 1. Own PR (after the branch is pushed and a PR exists)
own = <PR number of HEAD branch>
mcp__github__subscribe_pr_activity(owner=OWNER, repo=REPO, pullNumber=own)

# 2. Sibling PRs active in the last 7 days
prs = mcp__github__list_pull_requests(
  owner=OWNER, repo=REPO,
  state="open", sort="updated", direction="desc", perPage=40
)
cutoff = now() - 7d
for pr in prs:
  if parse(pr["updated_at"]) >= cutoff and pr["number"] != own:
    mcp__github__subscribe_pr_activity(
      owner=OWNER, repo=REPO, pullNumber=pr["number"]
    )
```

**Continuously:** at every `TICK` heartbeat from the main monitor,
re-list open PRs. If the PR list contains a number not in the
subscription set, subscribe to it and run §4 against the diff between
its base SHA and head SHA.

PR subscription is **idempotent**, so duplicate calls are safe.

### 2c. Stop conditions

- User says *"stop watching"*, *"unsubscribe"*, or `/unwatch`.
- Branch merged or closed → unsubscribe own PR; keep sibling
  subscriptions if user still wants coordination.
- Session ends.

To stop: call `TaskStop` on the Monitor and
`mcp__github__unsubscribe_pr_activity` on every subscribed PR. Record
the stop event in the ledger.

## 3. Trigger filter — does this event touch a proof?

Before invoking the full §4 pipeline, decide whether the event is
proof-relevant. **Skip** events that don't pass any of these filters.

For a `MAIN <sha> <msg>` line (or a PR commit event):

```bash
SHA=<the new commit sha>
# Files touched by this commit
changed=$(git diff-tree --no-commit-id --name-only -r "$SHA")

is_proof_event=false
echo "$changed" | grep -qE '(^|/)proof.*\.md$|(-proof|_proof)\.md$' && is_proof_event=true
echo "$changed" | grep -qE '\.lean$'                              && is_proof_event=true
echo "$changed" | grep -qE 'content/.*\.md$' && {
  # An .md without "proof" in its name still counts if its block-kind
  # in the sibling .ts is theorem/lemma/proposition/corollary/conjecture/definition
  for md in $(echo "$changed" | grep -E 'content/.*\.md$'); do
    ts="${md%.md}.ts"
    [ -f "$ts" ] && grep -qE 'kind:\s*"(theorem|lemma|proposition|corollary|conjecture|definition)"' "$ts" && is_proof_event=true
  done
}

# PR review-comment events: pass through if comment body mentions
# 'sorry', 'axiom', 'proof', 'conjecture' OR cites a content block label
```

If `is_proof_event=false`, emit a one-liner to the ledger and return.

## 4. Per-event proof QA pipeline (delegates to `proof-editor`)

When the trigger filter passes, fan out to the proof QA skills
**in parallel**. This skill does not re-implement gap detection —
it dispatches to the specialists.

### 4a. Scope reduction

Compute the **changed-block set**:

```bash
SHA=<event sha>
# Block label = the kebab-case basename of the touched .md/.ts/.lean
changed_blocks=$(git diff-tree --no-commit-id --name-only -r "$SHA" \
  | grep -E 'content/.*\.(md|ts|lean)$' \
  | sed -E 's|.*/||; s|\.[^.]+$||; s|-proof$||' \
  | sort -u)
```

### 4b. Dispatch (parallel `Agent` calls)

For each changed block, launch the relevant subset of:

| Specialist | When to run |
|------------|-------------|
| `proof-gap-audit` | Always (intra + inter gaps) |
| `proof-narrative-lean-equivalence` | If both `.md` and `.lean` siblings exist |
| `lean-proof-review` | If `.lean` changed |
| `lean-completeness-audit` | If `.ts` `kind` requires Lean and `.lean` is missing |
| `remark-audit` | If kind is `remark` |
| `proof-triage` | Always — produces fresh sorry inventory for the queue |

Use parallel `Agent` launches (single response, multiple tool calls).
Cap each agent's report at ~400 words.

### 4c. Synthesize findings

Apply the `proof-editor` §3 "Synthesize" rules:

1. **Deduplicate** across specialists.
2. **Cluster** by affected block.
3. **Severity rank**: critical / major / minor.
4. **Map to queue items** (one queue item per finding).

### 4d. Attempt fixes (collaborator+ only)

For each finding, classify into one of three discharge bands:

| Band | Finding shape | Action |
|------|---------------|--------|
| **Auto-discharge** | Uncited sorry with goal pattern matching the tactic cheat-sheet (positivity / ring / linarith / aesop / norm_num) | `lean_multi_attempt` with the canonical tactic set; if any succeeds, edit the `.lean`, re-run `lean_diagnostic_messages` to confirm, `lean_verify` for axiom audit, commit |
| **Author-assist** | Class A stub-weakening, hidden axiom, naked conjecture without conditional-class scaffolding, broken inter-proof chain, conjectural-propagation violation | Open one author ask (see §4e) |
| **Defer** | Minor stylistic gap, sorry already carrying `-- Ref:`, conjecture correctly class-axiomatised per §3b-cond | Mark `wontfix` in queue with reason |

**Naked conjecture special case:** When a `conjecture` block has a
fully-defined `uses[]` cone and the Lean stub is `sorry`, the watcher
**should attempt** to discharge it via `local/formalizer` +
`local/lean-generation` before defaulting to author-assist. If the
attempt fails after one round, escalate. This is the *"if a conjecture
is a placeholder for something to be proved, try"* clause of the
skill's mission.

### 4e. Author asks — one ask per stuck item

When a finding lands in the **Author-assist** band, post one ask
either on the source PR (if the trigger was a PR event) or via
`AskUserQuestion` (if the trigger was a main commit and a foreground
user is present). Format:

```markdown
**Proof watcher ask — `<block-label>`** (from <source-pr-or-commit>)

- Finding: <one sentence, with severity>
- File: <github-blob-url to `.md` (or `.lean` if Lean-specific)>
- Attempted: <which tactics / specialists were tried>
- Question: <one yes/no or a numbered choice>
```

**One ask per stuck item, batched per round.** If the author hasn't
answered an ask in 24 h (async setting), restate once and move on.
Do not block the queue on a single unanswered ask.

### 4f. Update the queue + ledger

After each event:

```bash
# Append a ledger row
ts=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo "| $ts | <event> | <scope> | <N critical / N major / N minor> | <N auto / N asked / N deferred> |" \
  >> todos/proof-integration-watcher-ledger.md

# Update queue with new items + status changes
# (use Edit on todos/proof-integration-queue.json — the JSON shape is small)
```

## 5. Idle backlog sweep

When the queue has been quiescent for ≥ 10 minutes (no main commits,
no PR events, no in-flight discharge attempts), pull the next backlog
item.

### 5a. Discovery (run once at session start, refresh after every 50
backlog items)

```bash
# Enumerate every content block under content/
find content -type d -name 'lean' -prune -o -type f \
  \( -name '*.ts' -o -name '*.md' -o -name '*.lean' \) -print \
  | grep -E 'content/[^/]+/[^/]+/' \
  | sed -E 's|/[^/]+$||' \
  | sort -u > /tmp/_pw_all_blocks.txt

# Filter to blocks whose .ts kind is theorem/lemma/proposition/
# corollary/conjecture/definition (proof-relevant)
> /tmp/_pw_proof_blocks.txt
while IFS= read -r dir; do
  for ts in "$dir"/*.ts; do
    [ -f "$ts" ] || continue
    if grep -qE 'kind:\s*"(theorem|lemma|proposition|corollary|conjecture|definition)"' "$ts"; then
      echo "${ts%.ts}" >> /tmp/_pw_proof_blocks.txt
    fi
  done
done < /tmp/_pw_all_blocks.txt
```

### 5b. Prioritisation

Order the backlog by:

1. **Sorry count** (more sorries → earlier): `grep -c '^[^-]*sorry' <block>.lean`
2. **Downstream dependents** (more dependents → earlier): walk `uses[]`
   from every other block; count edges that point at this block.
3. **Last-audit recency** (older → earlier): from `queue.audited[]`.
4. **Alphabetical** as tie-breaker.

### 5c. Per-item processing

Apply §4 — exactly the same pipeline as for incoming events. The
"source" field on each queue item becomes `backlog`.

### 5d. Quiescence + heartbeat

A backlog item is preempted by any incoming event. Resume the backlog
when the queue is quiescent again. Maintain at most one in-flight
backlog item.

If the session has been entirely quiescent for ≥ 60 minutes (no
events, no findings, queue empty), emit a one-liner:

> Proof watcher idle — backlog at N items, queue at M items,
> next refresh in <next discovery time>.

…and keep the Monitor armed.

## 6. Goal-driven invariants

The skill **enforces** these invariants on every commit it makes (own
branch only — never on others' branches):

| Invariant | Check |
|-----------|-------|
| Every `sorry` has `-- Ref:` | `grep -B1 '^[^-]*sorry' <file>.lean \| grep -qE -- '-- Ref:'` |
| No new `axiom` declarations | `git diff origin/main -- <file>.lean \| grep -E '^\+axiom '` is empty |
| Naked conjectures attempted | Every `conjecture` block touched in this branch has a `formalizer` attempt log in the queue (status `resolved` or `needs-author`) |
| No conjectural propagation regressions | `cd content && bun run pipeline/conjectural-propagation-audit.ts` reports no new violations vs. main |

If any invariant fails on a proposed commit, **block the commit**,
queue the violation as `critical`, and ask the author.

## 7. Output style

- One line per event when nothing changed (`<sha>  no proof scope`).
- A short structured block when findings exist:

  ```
  origin/main <sha> — <msg>
    findings: 1 critical, 2 major
    discharged: 1  asked: 1  deferred: 1
    queue: 14 (3 in-progress)
  ```
- An author ask when escalating (see §4e).
- End-of-session: tail of the ledger + queue stats.

## 8. Integration

- **Built on**: `local/watch` (main poll), `local/coordinate` (PR
  triage helpers), `proof-editor` (per-event QA dispatch).
- **Dispatches**: `proof-gap-audit`, `proof-narrative-lean-equivalence`,
  `lean-proof-review`, `lean-completeness-audit`, `proof-triage`,
  `proof-simplifier`, `formalizer`, `lean-generation`, `remark-audit`.
- **Produces**: `todos/proof-integration-queue.json` (live state) +
  `todos/proof-integration-watcher-ledger.md` (event log).
- **Complements** but does **not** replace `/coordinate` — when the
  user is running both, this skill owns the proof-QA dimension and
  `/coordinate` owns cross-PR scope.

## 9. Role gating

- **reader**: may run the watcher in audit-only mode (queue + ask,
  no edits, no commits, no PR comments).
- **collaborator**: may auto-discharge `Auto-discharge` band findings
  via `formalizer` / `lean-generation` / `proof-triage`, may commit
  on this branch, may post asks on PRs.
- **owner**: same as collaborator plus may commit to main when
  explicitly requested (still requires per-commit user approval per
  CLAUDE.md "Executing actions with care").

## Anti-patterns

- ❌ Re-implement gap detection here. Always delegate to
  `proof-editor` + the specialists.
- ❌ Subscribe to **every** open PR. Only the last-7-day-active set
  + own PR + newly-opened (per heartbeat re-check).
- ❌ Discharge a sorry without `lean_verify` post-check (axiom audit).
  An "easy fix" that adds `Decidable.em` is not a fix.
- ❌ Open >1 ask per round on the same block. Batch findings per
  block; ask one consolidated question.
- ❌ Auto-fix conjecture statements (turning a `conjecture` block
  into a `theorem` block) without explicit author approval. The
  conjectural-propagation rules (CLAUDE.md §3b) are author-owned.
- ❌ Edit `.ts` manifests to add a `status:` field. Status is
  derived per CLAUDE.md §4.
- ❌ Touch protected files (`deploy/google-viewers.txt`, etc.).

## Checklist

- [ ] Queue + ledger initialised under `todos/`
- [ ] Main baseline SHA stashed
- [ ] Monitor armed on `origin/main` with TICK heartbeat
- [ ] Subscribed to own PR (if pushed) and every sibling PR active
      in the last 7 days
- [ ] Auto-subscribe on every TICK for newly-opened PRs
- [ ] Per-event pipeline delegates to `proof-editor` specialists in
      parallel
- [ ] Auto-discharge band uses `lean_multi_attempt` + `lean_verify`
- [ ] Author asks are one-per-block, batched per round
- [ ] Backlog sweep prioritises by sorry count + downstream dependents
- [ ] Invariants checked before every own-branch commit
- [ ] GitHub blob URLs (`.md` first) included in every author ask
