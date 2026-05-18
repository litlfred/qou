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
| `proof-narrative-lean-equivalence` | **Whenever `.lean` is touched OR exists for the block** — covers the four drift classes A/B/C/D plus the new **missing-narrative** check (`.lean` exists, `.md` absent or stub-only) |
| `lean-proof-review` | If `.lean` changed |
| `lean-completeness-audit` | If `.ts` `kind` requires Lean and `.lean` is missing |
| `remark-audit` | If kind is `remark` |
| `proof-triage` | Always — produces fresh sorry inventory for the queue |

**Lean ↔ narrative coupling rule (STRICT).** For every block where
`.lean` exists, the watcher checks:

1. **Presence.** Does the `.md` sibling exist and contain a non-trivial
   statement (not just the title + one-line placeholder)?
   - Missing `.md` → finding `missing-narrative` (major).
   - Stub `.md` (only frontmatter / heading) → finding
     `narrative-stub` (major).
2. **Semantic match.** Does the narrative statement (and proof, if
   present) describe the same theorem the Lean declaration proves?
   - Apply the four drift classes from
     `proof-narrative-lean-equivalence`:
     - Class A stub weakening (Lean is `trivial` / `True` while
       narrative claims something substantial)
     - Class B scope mismatch (Lean proves a special case)
     - Class C hypothesis drift (different number / strength)
     - Class D notation drift (symbol register mismatch)
   - Each drift class becomes a queue item with severity
     critical (A) / major (B, C) / minor (D).

When either check fails, the resulting queue item carries
`finding: "missing-narrative" | "narrative-stub" | "drift-class-A" |
"drift-class-B" | "drift-class-C" | "drift-class-D"` and the standard
queue shape. The §4e author-ask wording for these is:

> The Lean sibling at `<lean-url>` proves `<lean-statement>`.
> The narrative `.md` is `<missing | stub | claims X instead>`.
> Question: 1) write narrative to match Lean, 2) weaken Lean to
> match narrative, 3) split into two blocks?

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
2. **Lean-without-narrative** (any `.lean` block whose `.md` sibling
   is missing or stub-only — discovered via the dual-sibling
   enumeration step below). These are presumed-published Lean results
   with no human-readable statement.
3. **Downstream dependents** (more dependents → earlier): walk `uses[]`
   from every other block; count edges that point at this block.
4. **Last-audit recency** (older → earlier): from `queue.audited[]`.
5. **Alphabetical** as tie-breaker.

#### 5b′. Dual-sibling discovery (Lean ↔ narrative coupling)

Run alongside §5a:

```bash
# Lean files whose .md sibling is missing or "stub-only"
> /tmp/_pw_missing_narrative.txt
> /tmp/_pw_narrative_stub.txt
find content -name '*.lean' -type f 2>/dev/null \
  | grep -v '/lean/' \
  | while IFS= read -r lean; do
      md="${lean%.lean}.md"
      ts="${lean%.lean}.ts"
      [ ! -f "$ts" ] && continue  # not a content block
      if [ ! -f "$md" ]; then
        echo "$lean" >> /tmp/_pw_missing_narrative.txt
        continue
      fi
      # "Stub-only" heuristic: .md body (excluding frontmatter) has
      # fewer than 5 non-blank lines OR no $...$ / $$ math at all
      # Count body lines: if frontmatter (`---` ... `---`) exists, skip
      # to after the second `---`; otherwise count from the start. Many
      # block .md files have no frontmatter — handle both cases.
      if head -1 "$md" | grep -q '^---$'; then
        body_lines=$(awk '/^---$/{f++; next} f>=2 && NF' "$md" | wc -l)
      else
        body_lines=$(grep -c . "$md")  # non-blank lines from the start
      fi
      # Detect math: $...$, $$...$$, OR LaTeX environments (begin{equation},
      # begin{align}, begin{tikzcd}, etc.) — `\begin{equation}` is common
      # for cross-referenced display math.
      has_math=$(grep -cE '\$|\\begin\{(equation|align|tikzcd|gather|displaymath)' "$md")
      if [ "$body_lines" -lt 5 ] && [ "$has_math" -eq 0 ]; then
        echo "$lean" >> /tmp/_pw_narrative_stub.txt
      fi
    done

echo "Lean-only blocks (missing narrative): $(wc -l < /tmp/_pw_missing_narrative.txt)"
echo "Stub-narrative blocks (Lean + thin .md): $(wc -l < /tmp/_pw_narrative_stub.txt)"
```

Each line becomes a queue item with finding `missing-narrative` or
`narrative-stub`, severity `major`, source `backlog`.

For blocks WITH both siblings, the per-item §5c processing also
includes the four-drift-class equivalence check from
`proof-narrative-lean-equivalence`.

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

### 5e. Idle author-ask dispatcher

When the session is idle (no incoming events, no in-flight backlog
discharge) AND the queue contains items that need author input,
**pull one ask and surface it** rather than just sitting on the queue.

Triggers (in priority order):

1. Items with `status: "needs-author"` that have never been asked
   (`asked_author_at: null`).
2. Items with `status: "queued"` that have aged > 24 h without any
   discharge attempt and are in the **Author-assist** band of §4d
   (Class-A stubs, naked-conjectures without conditional-class
   scaffolding, hidden axioms, broken inter-proof chains, conjectural-
   propagation violations).
3. Items with `status: "needs-author"` that were asked > 7 days ago
   and never resolved — **re-ask once**, then mark `wontfix` with
   reason `author-unresponsive`.

Per round (every quiescent ≥ 10 min window), pull **up to 3** asks,
group by block, and surface them as a single consolidated message:

- **Foreground session present** (the user is in the conversation):
  use `AskUserQuestion` with a numbered list of items + options
  (e.g. "1) write narrative, 2) weaken Lean, 3) split block, 4) skip
  for now"). The user's reply updates the queue item's `status`.

- **PR-driven session** (the trigger was a sibling PR event and there
  is no foreground user): post a single consolidated coordination
  comment on **own PR** (never on sibling PRs — that would spam the
  other agent's review queue). Format follows §4e.

- **Headless / batch session**: append the asks to the ledger under
  a `## Pending author asks` section so the next interactive session
  picks them up immediately.

After each ask, set `asked_author_at: "<ISO ts>"` and increment a
per-block ask counter. Cap consecutive asks per block at 3 — beyond
that, mark `wontfix` with `reason: ask-fatigue` and let the author
manually re-open if needed.

**Anti-pattern:** never auto-mark a `needs-author` item as
`resolved` based on inferred user assent (e.g. a thumbs-up reaction
on a comment). Only an explicit author reply or commit closes the
item.

### 5g. Watch PRs you prepare

When this watcher (or any skill it dispatches) **prepares a PR** —
i.e., creates a branch + opens a PR to consolidate a discharge, a
backlog fix, or a follow-up like #698 — the watcher **must** add
the new PR to its subscription set immediately and follow up on
review activity. Author oversight expectation: *"you should watch
PRs you prepare for review comments and respond if you can. if not
ask author. once done, ask author if they want to merge and provide
link"*.

The protocol per prepared PR:

1. **Subscribe.** Right after `create_pull_request`, call
   `mcp__github__subscribe_pr_activity` with the new PR number. Add
   to the ledger under "watching".
2. **Request a copilot review.** Call `mcp__github__request_copilot_review`
   so gemini-code-assist / copilot-pull-request-reviewer surface
   their feedback as actionable threads. Don't wait for human review
   to start.
3. **Triage every review event** per coordinate §5a:
   - `accept` → fix the small thing, push (see §5g.4 below for the
     stale-base risk on small fix-pushes)
   - `accept-with-modification` → fix differently, reply with one
     paragraph explaining why
   - `reject-with-reason` → reply on the thread
   - `escalate` → ask the author via §4e
4. **Pre-push stale-base check.** Every fix-push on a prepared PR
   triggers a fresh CI run. If `main` has moved since you branched,
   the new validate run may hit drift. Before each fix-push, run
   `git fetch origin main` and check the delta per coordinate §8c.
   If main moved ≥ 3 commits and any of the new commits touch your
   PR's diff scope, rebase first (per §5f recovery recipe).
5. **Done check + merge prompt.** When (a) every open review thread
   on the PR is resolved or replied to, (b) every CI check is green
   OR documented as a stale-validate flake (§5f), and (c) the diff
   still reflects the original intent, **ask the author**:

   > PR #N is ready for merge — N comments addressed, CI green
   > (or: CI flake documented as §5f drift, manual override OK).
   > Link: <PR URL>. Merge to main?

   Use `AskUserQuestion` (foreground) or post the merge-prompt on
   the PR (PR-driven session). Do **not** auto-merge.
6. **Stop on merge.** Once the author merges (or closes), call
   `mcp__github__unsubscribe_pr_activity`. Record outcome in ledger.

This protocol covers the lifecycle of every PR this watcher opens —
including the cite-hygiene followup (#698), the future naked-
conjecture batch PRs, and any other spin-outs from the queue.

## 5f. Witness-drift CI failure pattern (RECOVERY RECIPE)

The `witness-pipeline.yml > validate` job triggers on `.lean` edits
under `content/quantum-observable-universe/**/*.lean` AND on any
`*.witness.json` / `*.derivation.json` change. The job re-runs every
Python computation, regenerates witnesses, and fires a drift check.

**Failure mode** (observed repeatedly during 2026-05 main churn):
even a comment-only `.lean` edit triggers validate. Validate runs
many scripts; one of them regenerates a witness that has drifted on
main since the last refresh (e.g. `files_scanned: 516 → 517` when a
new probe lands without a witness refresh). The drift check then
fires.

**The pattern is endemic.** Main's own commit log shows repeated
`fix(witness-pipeline): post-rebase drift refresh` / `post-push
drift refresh` entries — author + sibling agents do this routinely.

**Recovery recipe** (apply IN ORDER, do not skip):

1. **Pull fresh main.** `git fetch origin main`. If ≥ 5 commits
   landed, jump straight to step 2 — don't waste cycles re-running
   validators locally first.
2. **Rebase.** `git rebase origin/main`. Witness conflicts are
   expected on `compute-audit-scan.witness.json` and
   `derivation-chain-audit.witness.json` (rarely also
   `e0-calibration-audit.witness.json`).
3. **Take main's witnesses.** `git checkout --ours <witness>` for
   each conflicted witness file (in rebase context `--ours` = the
   branch being rebased onto = main). `git add <witness>`.
4. **Continue.** `git rebase --continue`. If the same conflict reappears
   on a later commit, repeat step 3.
5. **Force-push.** `git push --force-with-lease`. CI re-runs; the
   drift check should now pass because the witnesses match main's
   freshly-refreshed baseline.

**Do not** try to fix the drift by manually editing witness JSON.
**Do not** regenerate witnesses on your branch and commit them as a
"fix" — by the time CI runs, main has likely moved again, and your
fresh witnesses will be a new round of drift.

**Do not** auto-trigger this loop. The recovery is the right action
on a single CI failure with an exhausted "everything else is green"
local diagnosis — don't rebase + force-push reactively on every
single CI failure. If two consecutive rebase-and-refresh cycles fail,
escalate to the author per §4e.

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
