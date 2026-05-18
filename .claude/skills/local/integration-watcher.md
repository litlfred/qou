---
name: integration-watcher
roles: [reader, collaborator, owner]
user_invocable: false
description: >
  Abstract parent skill for domain-specific **integration watchers**.
  Encodes the shared mechanics — Monitor on `origin/main`, PR
  subscriptions, per-event QA dispatch, queue + ledger, idle backlog
  sweep, idle author-ask dispatcher, watch-PRs-you-prepare protocol,
  one-voice on PR diff, witness-drift CI recovery, billing-quick-fail
  flake handling — that every concrete watcher inherits. Children
  fill nine domain-specific slots; everything else is shared here.
allowed-tools: Read Edit Write Bash Grep Glob Agent Monitor Skill
---

# integration-watcher (abstract parent)

A concrete watcher (this skill's child) **watches incoming activity**
on a focused content axis — proofs, canonical-derivation discipline,
compute-chain wiring, or any future domain — runs a domain QA
pipeline on every detected change, queues findings, attempts
auto-discharge where possible, and asks the author for the rest.

Three concrete children today:

| Child | Domain | Goal |
|-------|--------|------|
| [`proof-integration-watcher`](proof-integration-watcher.md) | Proof QA (narrative + Lean) | No bare sorries, no axiom growth, no naked conjectures with provable scaffolding |
| [`canonical-watcher`](canonical-watcher.md) | Canonical-derivation discipline | No 4th calibration, no numerology, no coefficient fits (per `prop:three-calibration-discipline`) |
| [`compute-integration-watcher`](compute-integration-watcher.md) | Cross-layer compute wiring | Every `prop:`/`thm:`/`lem:` block has a probe + production consumer (13-pattern I1-I13 audit) |

## Domain slots (every child must fill)

| Slot | Where in this parent | What the child provides |
|------|----------------------|-------------------------|
| **A. Goal statement** | top of child | One-paragraph driving function |
| **B. §3 trigger filter** | §3 | Domain-specific patterns: which file paths / commit subjects / PR comment keywords trigger the §4 pipeline |
| **C. §4b dispatch table** | §4b | Which specialist skills/scripts to invoke per event, in parallel |
| **D. §4c finding taxonomy** | §4c | The set of violation/finding kinds the domain recognizes |
| **E. §4d discharge bands** | §4d | Domain-specific examples of Auto-discharge / Author-assist / Defer findings |
| **F. §4e author-ask templates** | §4e | Domain-specific question forms (numbered choices, file/line citations) |
| **G. §5a backlog discovery** | §5a | What to enumerate from the codebase at backlog-sweep time |
| **H. §5b prioritisation** | §5b | Domain-specific ranking rule for the backlog |
| **I. §6 invariants** | §6 | Per-commit checks the watcher enforces on its own branch |

Everything else — §1, §2, §4a, §4f, §5c-§5h, §7-§9, anti-patterns,
checklist — is defined here and inherited verbatim.

## 1. Baseline + setup (run once per session)

```bash
# Repo identity — declared once, referenced everywhere below
OWNER=litlfred
REPO=qou

# Bootstrap the queue + ledger (gitignored under todos/)
mkdir -p todos
NAME="<your-watcher-name>"
[ -f "todos/${NAME}-queue.json" ] || \
  echo '{"items":[],"audited":{}}' > "todos/${NAME}-queue.json"
[ -f "todos/${NAME}-ledger.md" ] || cat > "todos/${NAME}-ledger.md" <<EOF
# ${NAME} — session ledger

| ts (UTC) | event | scope | findings | action |
|----------|-------|-------|----------|--------|
EOF

# Stash main baseline so §5f timeout-recovery can diff cleanly
git fetch origin main 2>/dev/null
git rev-parse origin/main > "/tmp/_${NAME}_main.sha"
```

Queue file shape (children may extend with extra fields but must
keep this core):

```json
{
  "items": [
    {
      "id": "<sha1-12 of block-or-script + finding-class>",
      "block_or_script": "<label or path>",
      "paths": { "ts": "...", "md": "...", "lean": "...", "py": "..." },
      "finding": "<domain-specific from Slot D>",
      "severity": "critical | major | minor",
      "source": "watch:main:<sha> | watch:pr:<N>:<event-ts> | backlog",
      "evidence": "<one paragraph: file:line + offending text>",
      "attempts": [ { "ts": "...", "tactic": "...", "outcome": "fail|partial|ok" } ],
      "status": "queued | in-progress | resolved | needs-author | wontfix",
      "asked_author_at": null
    }
  ],
  "audited": { "<block-or-script>": "<ISO-8601 ts>" }
}
```

`audited[]` is the per-block last-pass timestamp; the idle backlog
sweep (§5) skips blocks audited within the last 7 days unless their
source files have a newer mtime.

## 2. Active watching

### 2a. Watch `origin/main` (Monitor poll)

Arm exactly **one** persistent Monitor per session. Each new commit
line triggers the §4 per-event pipeline. **Emit every commit** — do
not cap with `head -N`, or fast bursts silently drop tail commits
past the cap.

```
Monitor:
  description: "origin/main new commits — <NAME>"
  persistent: true
  command: |
    last=$(git ls-remote origin main 2>/dev/null | cut -f1)
    while true; do
      cur=$(git ls-remote origin main 2>/dev/null | cut -f1)
      if [ -n "$cur" ] && [ "$cur" != "$last" ]; then
        git fetch origin main 2>/dev/null
        # Use %H (full SHA) so downstream `git diff-tree` / `git show`
        # calls don't risk abbreviation ambiguity in long-running sessions.
        git log --reverse --format='MAIN %H %s' "$last..$cur"
        last=$cur
      fi
      gh_now=$(date -u +%s)
      if [ -z "$last_pr_check" ] || [ $((gh_now - last_pr_check)) -gt 300 ]; then
        printf 'TICK %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
        last_pr_check=$gh_now
      fi
      sleep 300
    done
```

The `TICK` heartbeat (every 5 min) lets the foreground agent
(a) re-list open PRs and subscribe to any new ones, (b) pull a
backlog item if the queue was idle in the interval.

If the Monitor reports `[Monitor timed out — re-arm if needed]`,
apply **watch.md §5b** timeout-recovery (compare baseline SHA
against current `origin/main`, walk the missed range) before
re-arming.

### 2b. Subscribe to PRs

**At setup** subscribe to: (a) own PR (if pushed) and (b) every
open PR updated in the last 7 days.

```python
OWNER, REPO = "litlfred", "qou"
own = <PR number of HEAD branch>
mcp__github__subscribe_pr_activity(owner=OWNER, repo=REPO, pullNumber=own)

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

**Continuously:** at every `TICK` heartbeat, re-list open PRs and
subscribe to any new ones. Subscription is idempotent.

### 2c. Stop conditions

- User says *"stop watching"*, *"unsubscribe"*, or `/unwatch`.
- Branch merged or closed → unsubscribe own PR; keep sibling
  subscriptions if user still wants coordination.
- Session ends.

To stop: call `TaskStop` on the Monitor and
`mcp__github__unsubscribe_pr_activity` on every subscribed PR.
Record the stop event in the ledger.

## 3. Trigger filter — does this event match the domain?

Children fill **Slot B** with the domain-specific filter. The
parent only requires the filter return a boolean
`is_in_scope=true|false` and, if false, that the event be
recorded as a one-liner in the ledger and otherwise skipped.

Common shapes children typically check:

- **File path patterns** in the changed-files list
- **`.ts` block kind** of any touched `content/.../**/*.ts`
- **PR comment body keywords** (for review-comment events)

If `is_in_scope=false`, emit a one-liner to the ledger and return.

## 4. Per-event QA pipeline

When the trigger filter passes, fan out to the domain specialists
**in parallel**. The parent owns the orchestration; the child
provides the specialist list.

### 4a. Scope reduction

Compute the changed-block set / changed-script set / changed-witness
set from the event SHA:

```bash
SHA=<event sha>

# changed content blocks (label = kebab basename minus -proof suffix)
changed_blocks=$(git diff-tree --no-commit-id --name-only -r "$SHA" \
  | grep -E 'content/.*\.(md|ts|lean)$' \
  | sed -E 's|.*/||; s|\.[^.]+$||; s|-proof$||' \
  | sort -u)

# changed scripts
changed_py=$(git diff-tree --no-commit-id --name-only -r "$SHA" \
  | grep -E '^folio-assistant/computations/.*\.py$' | sort -u)

# changed witness JSONs
changed_witnesses=$(git diff-tree --no-commit-id --name-only -r "$SHA" \
  | grep -E '\.witness\.json$|\.derivation\.json$' | sort -u)
```

### 4b. Dispatch (parallel `Agent` calls)

Children fill **Slot C** with a table of `Specialist | When to run |
What it checks`. Launch all applicable specialists in a single
response with multiple `Agent` tool calls (NOT sequentially).

Cap each agent's report at ~400 words.

### 4c. Synthesize findings

Apply the `proof-editor` §3 "Synthesize" rules (same in every
domain):

1. **Deduplicate** across specialists.
2. **Cluster** by affected block/script.
3. **Severity rank**: critical / major / minor.
4. **Map to queue items** (one queue item per finding) — finding
   kind comes from the child's **Slot D**.

### 4d. Attempt fixes (collaborator+ only)

Every finding falls into one of three discharge bands. Children
fill **Slot E** with domain-specific examples; the band structure
itself is shared:

| Band | Shape | Action |
|------|-------|--------|
| **Auto-discharge** | Finding has a known mechanical fix (registry migration, tactic application, banner addition, cite move, …) | Apply the mechanical fix; re-run the relevant scanner / type-checker / validator to confirm; commit |
| **Author-assist** | Finding requires human judgement (semantic, architectural, scope) | Open one author ask per stuck block (see §4e) |
| **Defer** | Finding is acknowledged / opt-out / minor stylistic | Mark `wontfix` in queue with reason |

### 4e. Author asks — one ask per stuck block

When a finding lands in the **Author-assist** band, post one ask
either on the source PR (if the trigger was a PR event) or via
`AskUserQuestion` (if the trigger was a main commit and a
foreground user is present).

**Always lead with full context in chat, then ask a structured
question.** The user is busy and types slowly; they shouldn't have
to scroll back through old tool output or re-read the queue to
answer. Two-part pattern:

1. **Context preamble (chat text).** Before the `AskUserQuestion`
   call, write a short chat message:
   - the finding (one sentence, with severity);
   - the affected file (GitHub blob URL, `.md` preferred per
     CLAUDE.md "Always provide GitHub links");
   - evidence (a verbatim quote with line numbers, if applicable);
   - what was already attempted and what failed.
2. **Structured question.** Then call `AskUserQuestion` with a
   tight numbered-choice set (2-4 options), each option mapping
   directly to a queue-action. The question stem must be
   one sentence; the options carry the detail.

This guarantees the chat notification (which is what alerts the
user on their phone / desktop) carries enough context for them
to answer without digging.

Format (children fill Slot F with domain-specific question forms):

```markdown
**<watcher-name> ask — `<block-or-script>`** (from <source-pr-or-commit>)

- Finding: <one sentence, with severity>
- File: <github-blob-url to `.md` (or `.lean`/`.py` if domain-specific)>
- Evidence: `<file:line>` — `<verbatim quote of offending text>`
- Attempted: <which scanners/specialists/tactics were tried>
- Question: <one yes/no or numbered choice>
```

For PR comment escalations the same shape works; in foreground
sessions split it: preamble in chat text, structured `Question:`
in the `AskUserQuestion` call.

**One ask per stuck block, batched per round.** If the author
hasn't answered in 24 h (async setting), restate once and move on.
Do not block the queue on a single unanswered ask.

### 4f. Update the queue + ledger

After each event:

```bash
ts=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo "| $ts | <event> | <scope> | <N critical / N major / N minor> | <N auto / N asked / N deferred> |" \
  >> "todos/${NAME}-ledger.md"
```

Update `todos/${NAME}-queue.json` with new items + status changes
via `Edit`.

### 4g. Refresh spawned PRs against main

If the event was a new commit on `origin/main` AND §3 / §4
triage has completed (acted, deferred, or skipped — any
outcome), invoke **§5g step 7 (rebase spawned PRs on main
movement)**.  This keeps every PR the watcher has opened
current with main even when the per-event work itself was a
no-op.

The rebase runs in a worktree (no disturbance to the current
branch); witness-drift conflicts auto-resolve via §5f.
Substantive conflicts halt the rebase and surface as an author
ask per §4e.

## 5. Idle backlog sweep

When the queue has been quiescent for ≥ 10 minutes (no main
commits, no PR events, no in-flight discharge attempts), pull the
next backlog item.

### 5a. Discovery (run once at session start, refresh every 50 items)

Children fill **Slot G** with the domain's enumeration recipe
(typically a `find` + `grep` pipeline OR an existing aggregator
script).

### 5b. Prioritisation

Children fill **Slot H** with the domain's ranking rule. Common
factors:

1. Severity (critical > major > minor).
2. Downstream dependents (more dependents → earlier) via `uses[]`.
3. Last-audit recency (older → earlier) from `queue.audited[]`.
4. Alphabetical as tie-breaker.

### 5c. Per-item processing

Apply §4 — exactly the same pipeline as for incoming events. The
`source` field on each queue item becomes `backlog`.

### 5d. Quiescence + heartbeat

A backlog item is preempted by any incoming event. Resume the
backlog when the queue is quiescent again. Maintain at most one
in-flight backlog item.

If the session has been entirely quiescent for ≥ 60 minutes,
emit a one-liner:

> `<watcher-name>` idle — backlog at N items, queue at M items,
> next refresh in <next discovery time>.

…and keep the Monitor armed.

### 5e. Idle author-ask dispatcher

When the watcher enters an idle window AND the queue contains
items needing author input, batch the open asks and surface them
via `AskUserQuestion` (foreground) OR as a single consolidated
own-PR comment (PR-driven session) OR as a "Pending author asks"
section in the ledger (headless).

Triggers (in priority order):

1. Items with `status: needs-author` that have never been asked
   (`asked_author_at: null`).
2. Items with `status: queued` that have aged > 24 h without any
   discharge attempt and are in the **Author-assist** band.
3. Items with `status: needs-author` that were asked > 7 days ago
   and never resolved — **re-ask once**, then mark `wontfix` with
   `reason: author-unresponsive`.

Per round, pull **up to 3** asks, group by block, surface as one
consolidated message. After each ask, set `asked_author_at:
"<ISO ts>"`. Cap consecutive asks per block at 3; beyond that
mark `wontfix` with `reason: ask-fatigue`.

**Anti-pattern:** never auto-mark a `needs-author` item as
`resolved` based on inferred user assent (e.g. a thumbs-up
reaction). Only an explicit author reply or commit closes it.

### 5f. Witness-drift CI failure pattern (RECOVERY RECIPE)

The `witness-pipeline.yml > validate` job triggers on `.lean`
edits under `content/quantum-observable-universe/**/*.lean` AND
on any `*.witness.json` / `*.derivation.json` change. It re-runs
every Python computation, regenerates witnesses, and fires a
drift check.

**Failure mode** (observed repeatedly during 2026-05 main churn):
even a comment-only `.lean` edit triggers validate. Validate runs
many scripts; one regenerates a witness that has drifted on main
since the last refresh (e.g. `files_scanned: 516 → 517` when a
new probe lands without a witness refresh). The drift check fires.

**The pattern is endemic.** Main's own commit log shows repeated
`fix(witness-pipeline): post-rebase drift refresh` /
`post-push drift refresh` entries — author + sibling agents do
this routinely.

**Sub-case: quick-fail = billing.** If `validate` (or any CI job)
fails in **under ~60 seconds**, the runner almost never even
reached the Python validators. This is a billing / queue / quota
condition on the GitHub Actions account, **not** a content
failure. Treat as a flake: do NOT rebase, do NOT regenerate
witnesses, do NOT diagnose validators — they didn't run.
Document in ledger as `quick-fail / billing` and proceed per
§5g step 5(b).

**Recovery recipe** (apply IN ORDER, do not skip) for genuine
multi-minute validate failures:

1. **Pull fresh main.** `git fetch origin main`. If ≥ 5 commits
   landed, jump straight to step 2 — don't waste cycles re-running
   validators locally first.
2. **Rebase.** `git rebase origin/main`. Witness conflicts are
   expected on `compute-audit-scan.witness.json`,
   `derivation-chain-audit.witness.json` (rarely also
   `e0-calibration-audit.witness.json`).
3. **Take main's witnesses.** `git checkout --ours <witness>` for
   each conflicted file (in rebase context `--ours` = main).
   `git add <witness>`.
4. **Continue.** `git rebase --continue`. If the same conflict
   reappears on a later commit, repeat step 3.
5. **Force-push.** `git push --force-with-lease`.

**Do not** hand-edit witness JSON, do not regenerate witnesses
on your branch as a "fix" (by the time CI runs, main moves
again), and do not rebase reactively after every single CI
failure — only after exhausted local diagnosis.

### 5g. Watch PRs you prepare

When a watcher (or any skill it dispatches) **prepares a PR** —
i.e., creates a branch + opens a PR to consolidate a discharge,
a backlog fix, or a follow-up — the watcher **must** add the new
PR to its subscription set immediately and follow up on review
activity. Author oversight expectation: *"watch PRs you prepare
for review comments and respond if you can. if not ask author.
once done, ask author if they want to merge and provide link"*.

Per prepared PR:

1. **Subscribe.** Right after `create_pull_request`, call
   `mcp__github__subscribe_pr_activity` with the new PR number.
   Add to the ledger under "watching".
2. **Request automated reviews from both bots.** Call
   `mcp__github__request_copilot_review` to surface
   `copilot-pull-request-reviewer` feedback as actionable threads.
   `gemini-code-assist` runs separately (automatic on PR open in
   this repo); if it doesn't post within a few minutes, check
   for a quota-limit comment ("you have reached your daily
   quota") and document in the ledger. The two bots find
   different classes of issue (copilot — style + small bugs;
   gemini — semantic correctness, cross-file conventions),
   so request **both**. Don't wait for human review.
3. **Triage every review event** per coordinate §5a:
   - `accept` → fix the small thing, push
   - `accept-with-modification` → fix differently, reply
   - `reject-with-reason` → reply on the thread
   - `escalate` → ask the author via §4e
4. **Pre-push stale-base check.** Every fix-push triggers a fresh
   CI run. Before each fix-push, run `git fetch origin main` and
   check the delta per coordinate §8c. If main moved ≥ 3 commits
   and any touch your PR's diff scope, rebase first (per §5f).
5. **Done check + merge prompt.** When (a) every open review
   thread is resolved or replied to AND one-voice has been
   applied or noted n/a (§5h), (b) every CI check is green OR
   documented as a flake (§5f), (c) the diff still reflects the
   original intent, **ask the author**:

   > PR #N is ready for merge — N comments addressed, CI green
   > (or: documented as §5f drift/billing flake). Link: <PR URL>.
   > Merge to main?

   Use `AskUserQuestion` (foreground) or post the merge-prompt on
   the PR (PR-driven). Do **not** auto-merge.
6. **Stop on merge.** Once the author merges (or closes), call
   `mcp__github__unsubscribe_pr_activity`. Record outcome in
   ledger.

7. **Rebase spawned PRs on main movement.** Every time a new
   commit lands on `origin/main` and the §3 / §4 per-event triage
   completes (whether the event was acted on, deferred, or
   skipped), walk **every PR this watcher has opened that is
   still open** and ensure each one is current with
   `origin/main`.  The walk:

   ```bash
   # One `git fetch origin` outside the loop refreshes every
   # remote-tracking ref the loop will use.  Per-branch
   # `git fetch origin <name>` is fragile — it updates
   # FETCH_HEAD but only updates `refs/remotes/origin/<name>`
   # when the branch is covered by the remote's fetch refspec.
   git fetch origin

   # Extract branches under the "### Watching" subsection.  The
   # closing pattern is `^## ` (next top-level header), NOT
   # `^### ` — `/^### Watching/,/^### /` collapses to one line
   # (the opening line itself matches the closer).
   pr_branches=$(awk '/^### Watching/,/^## /' \
       "todos/${NAME}-ledger.md" \
       | grep -oE 'claude/iw-[a-z0-9-]+' | sort -u)

   for pr_branch in $pr_branches; do
     # Map branch → PR number explicitly.  Either via `gh`:
     pr_num=$(gh pr list --head "$pr_branch" --state open \
              --json number --jq '.[0].number')
     # ... or via the MCP equivalent:
     # mcp__github__list_pull_requests head="$pr_branch" state=open
     #   | jq '.[0].number'
     [ -n "$pr_num" ] || continue   # closed / no open PR; skip

     # Distance from main on the branch's tip.
     behind=$(git rev-list --count \
              "origin/$pr_branch..origin/main")

     # Diff-scope overlap: which files did MAIN change since the
     # branch diverged, intersected with files the BRANCH has
     # changed since divergence?  Diffing the two tips
     # (`git diff origin/main origin/$pr_branch`) mis-attributes
     # main's own movement to the PR's scope.  Use merge-base.
     base=$(git merge-base "origin/main" "origin/$pr_branch")
     # `xargs -r` skips the inner command entirely when the
     # piped file list is empty (otherwise an empty diff would
     # invoke `git log` once with no path filter and count all
     # main-commits, mis-firing the trigger on new branches).
     touches_diff=$(
       git diff --name-only "$base" "origin/$pr_branch" \
       | xargs -r -I {} git log --oneline \
           "$base..origin/main" -- {} \
       | wc -l
     )

     # Rebase trigger: ≥ 3 commits behind OR ≥ 1 file in the
     # intersection of (main-changed-since-base) ∩
     # (branch-changed-since-base).
     if [ "$behind" -lt 3 ] && [ "$touches_diff" -eq 0 ]; then
       continue
     fi

     # Rebase in a worktree.  Use a SUBSHELL so the per-iteration
     # `trap … EXIT` is scoped to this iteration; a `trap` set in
     # the outer shell is process-global, gets overwritten each
     # iteration, and only fires once at shell exit (worktrees
     # leak).
     (
       worktree=$(mktemp -d /tmp/iw-rebase.XXXXXX)
       trap 'git worktree remove --force "$worktree" 2>/dev/null; \
             rm -rf "$worktree"' EXIT

       git worktree add "$worktree" "origin/$pr_branch" >/dev/null

       # Explicit if/then/else so rebase-conflict and push-fail
       # are distinguishable (the classic `A && B || C` collapses
       # a push failure into the conflict branch — wrong).
       if ( cd "$worktree" && git rebase origin/main ); then
         if ( cd "$worktree" && git push --force-with-lease \
                origin "HEAD:$pr_branch" ); then
           echo "REBASED + PUSHED $pr_branch"
         else
           echo "PUSH FAILED on $pr_branch (lease rejected / remote moved) — retry next cycle"
         fi
       else
         # Conflict — abort so the worktree is in a known state
         # before the trap removes it.
         ( cd "$worktree" && git rebase --abort 2>/dev/null ) \
           || true
         echo "REBASE CONFLICT on $pr_branch — flag to author (§4e)"
       fi
       # trap fires on subshell exit, cleaning THIS iteration's
       # $worktree (NOT the last loop iteration's).
     )

     # Update ledger row with last-rebase-against-main SHA on
     # success (rebased + pushed lines above).
   done
   ```

   Witness-drift conflicts on the four auto-regen audit witnesses
   (compute-audit-scan, derivation-chain-audit, cross-check-trM-1ppb,
   e0-calibration-audit) auto-resolve via the §5f recipe.
   Substantive conflicts halt the rebase and surface as an author
   ask per §4e.

   This step keeps spawned PRs current **automatically** between
   main-event triages, so reviewers don't see a `dirty` /
   `behind by N commits` PR when they come back to review.  It
   subsumes the pre-push check of step 4 above — that one still
   runs before each fix-push, but step 7 also catches the case
   where main moves while the PR is idle waiting for review.

   Same rule applies to **newly-opened** PRs the watcher created
   in this session: subscribe (step 1) + rebase-on-main-move
   (step 7) are paired.

### 5j. Backlog-found issue — spin up your own PR

When the **idle backlog sweep** (§5) finds an issue that is NOT
already addressed by an open PR (sibling or otherwise), the
watcher's default action is to **create a PR on its own branch**
to resolve it, then follow §5g for that PR's lifecycle.

Workflow:

1. **Cluster.** Group nearby backlog items (same chapter, same
   file, same finding kind) so one PR addresses a coherent
   tranche, not a single one-line fix.
2. **Branch.** Create a new branch via
   `mcp__github__create_branch`, named using the **integration-watcher
   convention**:

   ```
   claude/iw-<TYPE>-<DESCRIPTIVE-STUB>
   ```

   - `<TYPE>` — short tag for which watcher is spinning up the PR.
     Canonical values:
     - `compute` — from `local/compute-integration-watcher`
     - `proof` — from `local/proof-integration-watcher`
     - `canonical` — from `local/canonical-watcher`
     - `meta` — for changes to the integration-watcher skill family
       itself (this parent + children + routing).
     A new sibling child watcher (e.g. `local/<foo>-integration-watcher`)
     uses `<TYPE> = foo` consistently.
   - `<DESCRIPTIVE-STUB>` — kebab-case slug naming the issue
     being addressed.  Aim for 3–6 words that read clearly in a
     `gh pr list` output.  Examples:

     | Watcher | Backlog item | Branch name |
     |---------|-------------|-------------|
     | compute | wire `prop:flavor-split-substrate` into 6-term sweep | `claude/iw-compute-wire-flavor-split-substrate` |
     | proof   | chase `prop:foo` 1 sorry + missing cite | `claude/iw-proof-foo-sorry-and-cite-hygiene` |
     | canonical | replace fitted κ with substrate-pure form | `claude/iw-canonical-kappa-substrate-derivation` |
     | meta | add new I-pattern to compute-integration-watcher | `claude/iw-meta-add-new-i-pattern` |

   The `iw-` infix is the **mandatory marker** that ties the branch
   back to the integration-watcher family; CI dashboards + the
   `/coordinate` skill use it to discover watcher-spawned PRs.

   Random suffixes (e.g. `-Xyz12`) are not part of the convention.
   If a branch name collides with an existing one, append a `-v2`
   / `-v3` discriminator rather than randomising.
3. **Apply fixes.** Use `mcp__github__push_files` or `git push`
   from a temp local branch to push the fixes. For most
   non-trivial work, use a local `git checkout -B <temp>
   origin/main` + edits + `git push origin <temp>:<target>` +
   delete temp.
4. **Open PR** via `mcp__github__create_pull_request` with a
   descriptive title + body citing the backlog source.
5. **Subscribe + request copilot review** per §5g step 1-2.
6. **Triage** review threads per §5g step 3.
7. **One-voice + done check + merge prompt** per §5h and §5g
   step 5.

**When to escalate to the user instead of opening a PR:**

| Condition | Action |
|-----------|--------|
| Backlog item is one quick fix (< 5 min, < 50 lines) and clearly mechanical | Open PR directly, don't ask first |
| Backlog item touches > 5 files OR introduces new content blocks OR makes a semantic claim | Surface to user via §4e first; only open PR after user confirms |
| **Backlog item is VERY large** (e.g. > 200 lines of edits, > 20 files, semantic refactor across chapters, requires deep knowledge of an unfamiliar domain) | **Do NOT open a PR.** Instead, write a **handover document** at `docs/audits/<YYYY-MM-DD>-<short-task>-handover.md` for a specialist agent. See §5k below. |

### 5k. Handover doc for very-large backlog issues

When a backlog issue exceeds the watcher's discharge capacity
(too large, too cross-cutting, requires specialist context),
produce a handover doc rather than attempt the fix.

Handover doc structure (commit to a sibling branch or to a
followup PR alongside your skill PR):

```markdown
# Handover: <issue title>

**Scope:** <one paragraph>
**Discovered by:** `<watcher-name>` backlog sweep on <date>
**Severity:** <critical | major | minor>
**Estimated effort:** <hours / days>

## Background

<context — why this matters, where the issue lives>

## What the watcher found

<verbatim queue items + evidence>

## Suggested approach

1. <step 1>
2. <step 2>
...

## Specialist skill recommended

`<skill-name>` (collaborator role)

## Acceptance criteria

- [ ] <criterion 1>
- [ ] <criterion 2>
- [ ] CI green (or §5f flake documented)
- [ ] One-voice sweep applied
```

Then surface to user via §5e: "I found a very-large issue
(<title>). Handover doc at `<url>`. Should I dispatch
`<specialist-skill>` to take it, hold for a future session,
or expand the watcher to attempt it?"

### 5i. Sibling-PR findings — post comment, don't fix

When a watcher detects an in-scope finding on **a PR it did not
create** (i.e., a sibling PR owned by another agent or a human
author), the watcher **must not** push a fix to the sibling
branch. Instead, post a single coordination comment on the
sibling PR so that PR's owning agent can review and act.

Format (mirrors §4e):

```markdown
**<watcher-name> sibling-PR ask — `<block-or-script>`**

- Finding: <one sentence, with severity>
- File: <github-blob-url to `.md` on the sibling PR head>
- Evidence: `<file:line>` — `<offending text>`
- Attempted: (none — not auto-fixing on sibling branches per
  `<watcher-name>` §5i)
- Suggested fix: <one-paragraph proposal, mechanical or
  semantic>
- Owner-agent action: address on your branch and reply with the
  commit SHA, or reply with rationale for skipping.
```

Rationale: cross-branch fixes silently diverge — the sibling
agent loses authority over their PR and may rewind / rebase /
force-push your "fix" into a state you didn't intend. The right
move is to surface the finding, suggest the fix, and let the
owner integrate.

**Rate-limit.** One sibling-PR comment per finding per round.
If a sibling PR accumulates ≥ 3 unaddressed findings, batch them
into a single follow-up comment (one round only); after that,
mark the PR's items as `wontfix-sibling-unresponsive` in the
queue and surface to the author per §5e on the next idle window.

**Exceptions** (when direct cross-branch action IS appropriate):
- Cherry-picking a sibling's commit into your branch (per
  `local/coordinate` §10) — that's pull, not push.
- The author explicitly authorises the cross-branch action.

### 5h. Post-completion one-voice review on prepared PRs

When a prepared PR (per §5g) lands its **last substantive fix**
(diff settles, no more code changes planned), run
`local/one-voice-audit` on the **diff scope** before the merge
prompt:

- **PR touches `.md` content** → run the §1 greps (status leaks,
  emoji, work-tracker words, first-person tone, unicode crashes)
  on the diff. Apply mechanical fixes (Category A/C/E per
  one-voice-audit §3). Push as `style: one-voice sweep on PR
  diff`. Then the §5g step 5 merge prompt.
- **PR is content-free** (only `.lean`, `.ts`, `.py`, witness
  JSON, or skill `.md`) → one-voice is a **no-op**; record that
  in the ledger and the merge-prompt reply ("one-voice: n/a, PR
  scope is X only"). The author still gets the merge prompt.

This rule extends §5g step 5(a).

## 6. Goal-driven invariants

Children fill **Slot I** with the domain's invariant checks.
The parent enforces this pattern: every invariant is checked
before every own-branch commit; failure blocks the commit,
queues the violation as `critical`, and asks the author.

## 7. Output style

- One line per event when nothing changed (`<sha>  no <domain> scope`).
- A short structured block when findings exist:

  ```
  <source> <sha> — <msg>
    findings: N critical, N major
    discharged: N  asked: N  deferred: N
    queue: M (K in-progress)
  ```
- An author ask when escalating (see §4e).
- End-of-session: tail of the ledger + queue stats.

## 8. Integration

- **Built on**: `local/watch` (Monitor scaffolding),
  `local/coordinate` (PR triage helpers).
- **Dispatches**: see each child's Slot C.
- **Produces**: `todos/${NAME}-queue.json` (live state) +
  `todos/${NAME}-ledger.md` (event log).
- **Complements** other watchers — each owns one axis (proof /
  canonical / wiring / …); coordinate via `/coordinate` if the
  user is running more than one.

## 9. Role gating

- **reader**: may run in audit-only mode (queue + ask; no edits,
  no commits, no PR comments).
- **collaborator**: may auto-discharge Auto-discharge band
  findings, may commit on this branch, may post asks on PRs.
- **owner**: same as collaborator plus may commit to main when
  explicitly requested (still requires per-commit user approval
  per CLAUDE.md "Executing actions with care").

## Anti-patterns (shared across all children)

- ❌ Re-implement scanner/analyser logic here. Always delegate
  to existing specialists / scripts.
- ❌ Subscribe to **every** open PR. Only last-7-day-active set
  + own PR + newly-opened (per TICK).
- ❌ Open > 1 ask per round on the same block. Batch findings.
- ❌ Edit `.ts` manifests to add a `status:` field (status is
  derived per CLAUDE.md §4).
- ❌ Touch protected files (`deploy/google-viewers.txt`, etc.).
- ❌ Hand-edit witness JSON to "fix" drift.
- ❌ Auto-merge a PR without explicit author approval.

Children add their own domain-specific anti-patterns.

## Checklist (shared across all children)

- [ ] Queue + ledger initialised under `todos/`
- [ ] Main baseline SHA stashed
- [ ] Monitor armed on `origin/main` with TICK heartbeat
- [ ] Subscribed to own PR + every sibling PR active in 7 days
- [ ] Auto-subscribe on every TICK for newly-opened PRs
- [ ] Per-event pipeline delegates to specialists in parallel
- [ ] Auto-discharge band uses scanner-verified mechanical fixes
- [ ] Author asks are one-per-block, batched per round
- [ ] Backlog sweep prioritised per Slot H
- [ ] Invariants checked before every own-branch commit
- [ ] GitHub blob URLs (`.md` first) included in every author ask
- [ ] Prepared PRs followed up per §5g (subscribe + copilot
      review + merge prompt)
- [ ] One-voice sweep applied or noted n/a on every prepared PR
      before merge prompt (§5h)
