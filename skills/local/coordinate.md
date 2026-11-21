---
name: coordinate
description: Coordinate work across multiple in-flight Claude PRs working toward a shared goal (e.g. 1ppb mass-prediction). Post intent + asks on related PRs, identify cherry-pickable work, respond to code-review comments on your own PR, periodically triage sibling PR activity (new comments, CI status, new commits), watch main + newly created branches/PRs, escalate inconsistent findings to the author, and keep a coordination ledger up to date.
roles: [reader, collaborator, owner]
user_invocable: true
---

# /coordinate — multi-agent / multi-PR coordination

> **Bib human-review axis (2026-06-09).** Coordination now tracks a
> **bib human-review** axis: every `references.ts` entry must be `validated`
> or `issue-open` (not `unreviewed`/stale). Run
> `cd content && bun run pipeline/validate-references-human-review.ts` in the sweep
> (`content/` is its own Bun package);
> route flagged refs through [`local/bib-human-review`](bib-human-review.md)
> (one physical-review issue per ref needing physical access, assigned
> `@litlfred`). A PR that adds references should not leave them `unreviewed`
> without flagging them for the workflow.

When several Claude branches are converging on the same long-term goal
(e.g. "reach 1 ppb on mass predictions", "close all §3b violators",
"compute-infrastructure overhaul"), each agent has only its own
context.  Without coordination they will:

- duplicate work (two agents both class-axiomatising
  `conj:knot-factor-frobenius-pairing`),
- silently diverge (one renames `HA → delta_q`, another keeps `HA`,
  the merge conflicts),
- miss cherry-picks (one agent already wrote the Lean class template
  the others need),
- accept inconsistent findings without flagging them to the author,
- accept review-tool feedback without checking it against the actual
  proof / sibling PR's framing (e.g. accepting an off-by-one "fix"
  that contradicts a definition another PR is also using),
- miss new sibling PRs that opened mid-session (new branches landing
  on `main` with overlapping scope).

> **Measured research-overlap is PERMITTED (owner relaxation, 2026-07-18).**
> The "duplicate work" item above is relaxed for **genuinely open research
> topics** — an unsolved math/physics question whose *outcome is unknown and
> multiple routes are viable* (α_EM per-loop measure, a Stokes-constant
> extraction, a Δ_λ closure, a c_k identification). A different agent context
> may crack the wall by a different route, so overlapping such a topic is
> acceptable even when a sibling is on it. **A small relax, not a licence to
> duplicate:** (1) only *open-outcome* research qualifies — *mechanical /
> settled* work (sweeps, witness/sidecar regen, refactors, wiring an
> already-derived result, migrations) still has one owner, do not overlap it;
> (2) still post intent naming the parallel attempt **and your distinct
> route** ("you're on the torsion determinant; I'm on the Bloch-group lift");
> (3) when one route lands, the other re-scopes to *verify / extend / refute*
> and cites it — two independent confirmations are valuable, two identical
> re-derivations are waste. Full text: AGENTS.md §"Coordinate intent with
> sibling branches".

`/coordinate` is the protocol that prevents this.  None of the agents
has all the answers; they look to the author for clarification on
inconsistencies, and they cherry-pick from each other.

## Workflow rule reminder (from AGENTS.md §Branch + PR workflow)

This skill assumes you've already created a branch + opened a PR for
the work tranche being coordinated. Per AGENTS.md (STRICT, supersedes
default "no auto-PR" guidance for this repo): **always create a
branch and open a PR at the start of every work tranche** — ASAP, and
**never ask the user "want me to open the PR?"** Branch + PR creation
is pre-authorized; the only git action needing explicit permission is
the *merge*. Commit early, commit often. Small structured commits
cherry-pick cleanly; big mixed commits do not. Exception:
integration-watcher batch audit-job sweeps may use a single bulk
commit.

## When to invoke

- Start of a session where the user mentioned **other branches/PRs**
  by name (e.g. "coordinate with `claude/foo` and `claude/bar`").
- Whenever you start a new substantive task in a multi-PR effort —
  before making code changes, post intent on the relevant PRs.
- When you finish a substantive task — post progress + concrete
  cherry-pickable artefacts (file paths, function names, Lean class
  templates, witness fixtures).
- **Periodic triage between substantive commits** (§7) — even with no
  external trigger, sibling PRs may have landed commits or comments
  that change your scope.  Run a quick triage every ~3–5 commits or
  when you finish a task and pick up the next one.
- **When `main` lands new commits** during your session — if any
  touch the same content blocks, conjectures, or compute scripts you
  are editing, treat as a sibling PR for §3 classification purposes.
- **When a code-review comment lands on your own PR**
  (copilot-pull-request-reviewer, codex, or human reviewers;
  gemini-code-assist is sunset)
  — see §5 *Responding to review comments*.
- When you encounter a **finding that contradicts another PR's
  framing** — write the disagreement up explicitly, post it to both
  PRs, and tag the author for resolution.

## Inputs

- The current PR number (your branch).
- A list of sibling branch names or PR numbers (the user gives this,
  or read `gh pr list --label "in-flight"`).
- The shared goal in 1–2 sentences (e.g. "reach 1 ppb on
  D…⁴⁰Ca masses without deriving Q_β").

## Protocol

### 1.  Read sibling PRs first

For each sibling PR:

```bash
gh pr view <N> --json number,title,body,state,headRefName,updatedAt
gh pr view <N> --json files --jq '.files[].path'
```

Use `gh`'s embedded `--jq` (don't pipe to an external `jq`; it
isn't a guaranteed dependency in every Claude Code environment).
Read the **full** file list, not a truncated head — partial scope
maps cause silent overlaps later. File paths are cheap.

Or via MCP: `mcp__github__list_pull_requests` /
`mcp__github__pull_request_read` (with paginated `get_files`).

Build a **scope map**: which PR owns which workplan phase,
which files, which conjectures, which compute scripts.

### 2.  Identify three relationships per sibling

For every sibling PR, classify yourself on three axes:

| Axis | Values |
|------|--------|
| **Overlap** | none / additive (different files, same goal) / conflicting (same file or same conjecture) |
| **Dependency** | independent / I depend on theirs / they depend on mine |
| **Cherry-pick opportunity** | none / I want X / they probably want Y |

A sibling that is `(none, independent, none)` doesn't need a
coordination comment.  Anything else does.

#### 2-bis.  Mass-and-Binding-Algorithms appendix sync

**If your PR touches any of the following — mass-identity (Step 9a),
per-isotope binding (Step 9b), confinement SDP (Step 10), Q_β
truncation (Step 11), or any sidecar algorithm (Δ_λ closure, c_k
ladder, LP/SDP dual emission, witness-JSON pipeline) — you MUST
update the matching `alg:`-block under
[`folio/quantum-observable-universe/appendix-mass-binding-algorithms/`](../../../folio/quantum-observable-universe/appendix-mass-binding-algorithms/)
in the same PR.**

The appendix is a *maintenance contract*, not a static document:
its `uses[]`, `computation.script`, `computation.witness`, and the
.md *Algorithm* / *Correctness* / *Python API* sections must stay
in sync with the actual compute. Reviewers diff the appendix
against the compute change.

When posting your intent comment on a sibling PR whose scope
overlaps mass / binding / compute, name the `alg:`-block(s) you
will touch alongside the script paths — e.g.
"will touch `confinement-operator-selection.py` + the matching
`alg:confinement-sdp` in `appendix-mass-binding-algorithms/`".

### 3.  Post intent before working

Use `mcp__github__add_issue_comment` (or `gh pr comment`) on each
sibling PR with non-trivial relationship.  Format:

```markdown
## Coordination from #NNN

**Picking up:** {one sentence — which workplan phase / task}

**Scope confirmation:**
- I will touch: `path/to/file:line-range`, `path/to/other`, …
- I will not touch: `{the sibling's territory}`

**Cherry-pick from you:**
- {what you need from them; e.g. "Lean class template you used for
  `conj:crystal-graph-realization`"}

**Cherry-pick for you:**
- {what you'll produce that they may want; e.g. "the witness reader
  for `term6-residues-at-roots.witness.json` is the same shape they
  need for the canonical T6 path"}

**Asks (small):** {questions they can answer in one line}

**Escalation to author:** {if any; see §6}
```

Keep it short.  One ask per ask.  No prose.

### 4.  Post progress at task boundaries

When you commit something cherry-pickable, post a follow-up:

```markdown
## Progress from #NNN · `{short-task-name}`

- Landed in `{commit-sha}`: {one sentence}
- Cherry-pick file pointers: `path/file.py:fn`, `path/file.lean:Decl`
- Updated [`{your-audit-or-plan-doc}.md`](…) §{section}: {what
  changed} — and/or appended a row to
  [`docs/coordination/{goal-slug}.md`](…)
- Next: {next task on your queue}
```

Cherry-pick file pointers are the load-bearing part — the sibling
agent should be able to copy/cite without reading your whole diff.

### 5.  Responding to review comments on your own PR

Code-review tools (`copilot-pull-request-reviewer[bot]`,
`codex[bot]`; `gemini-code-assist[bot]` is sunset) and human
reviewers leave comments on your PR.  **Do not silently accept or
silently dismiss.**  The same rules that govern cross-PR
inconsistencies (§6) govern review feedback.

#### 5a.  Triage every comment

For each comment, assign one of four verdicts:

| Verdict | When | Action |
|---------|------|--------|
| `accept` | Suggestion is correct and small | Apply the fix in a single commit citing the comment URL; mark the thread resolved if the tooling permits. |
| `accept-with-modification` | Intent is right but the suggested patch has its own issue (e.g. introduces a different off-by-one, or breaks a sibling-PR's convention) | Apply a corrected version; reply on the thread with one paragraph explaining what you did and why the original suggestion needed adjusting (cite `file:line` where the divergence matters). |
| `reject-with-reason` | Finding is mathematically/empirically wrong | Reply with the reasoning: cite the specific line, definition, or sibling-PR convention that contradicts the suggestion.  Never silent-dismiss. |
| `escalate` | Finding is correct but would cross a sibling-PR's territory, or two reviewers disagree, or the comment exposes an inconsistency in a sibling PR's audit | See §6.  Reply with an `⚠️` flag and tag the author. |

#### 5b.  Verify against the actual math / code before replying

Review-tool suggestions can be **subtly wrong**.  Common failure
modes:

- **Off-by-one fixes that flip-flop convention**:
  e.g. a reviewer says "$\nu^* = (1^p)$ not $(1^{p-1})$" without
  noticing that the boundary cells split across the $\mu$/$\nu$
  cut.  Read the proof, not just the suggested patch.
- **Cross-PR convention conflicts**: e.g. PR A names a witness
  field `active_set`, PR B names it `active_constraints`; a
  reviewer suggesting one without checking the other introduces
  a merge conflict downstream.  Check sibling PRs before applying.
- **Hallucinated context**: review tools sometimes reference PR
  numbers or comment IDs that don't exist.  If the reviewer
  references a comment you didn't write, treat it as a
  hallucination and ignore the cross-reference (but still
  evaluate the substantive content of the comment on its merits).

If you can't verify in &lt; 2 minutes, escalate (§6) rather than
guess.

#### 5c.  Post one consolidated status comment

After triaging all threads from one review pass, post a **single**
PR-level summary using `mcp__github__add_issue_comment`:

```markdown
Thanks @REVIEWER — addressed all {N} threads in [`{sha}`]({commit-url}).

| # | Issue | Verdict | Resolution |
|---|---|---|---|
| 1 | Off-by-one in $I = …$ | accept | Fixed: `σ_{n_1+p-2}` |
| 2 | … | accept-with-modification | Fixed differently — see note below |
| 3 | … | reject-with-reason | See reply on thread |
| 4 | … | escalate | ⚠️ tagged @AUTHOR |

**Re #2 (note):** {short paragraph explaining the modification}
```

This avoids per-thread reply storms while still giving a paper
trail for every verdict.  Threads marked `accept` /
`accept-with-modification` should be resolved (`mcp__github__resolve_review_thread`)
once the reviewer acknowledges or after a one-day cooling period.

#### 5d.  When the reviewer pushes back

Code-review bots often respond to your reply.  Keep the dialogue
**short** — re-state the math or the sibling-PR convention once,
ask for a yes/no on whether the reviewer agrees.  After the
second exchange, escalate (§6).  Loops with bots burn cycles
without converging.

### 6.  Inconsistent findings → escalate, do not paper over

If a sibling PR's finding contradicts yours (e.g. they say T6 is
already canonical, you say it consumes a non-canonical witness;
they say the framework has one calibration, you found three) —
**or** if a code-review comment claims a fact that contradicts a
sibling PR's audit (§5a `escalate`) — do NOT silently change your
framing.  Post on every affected PR:

```markdown
## ⚠️ Inconsistent finding — author input requested

- This PR's claim: {yours, file_path:line cited}
- Sibling #{N}'s claim: {theirs, file_path:line cited}  (or:
  Reviewer's claim in {comment-url})
- Likely cause: {best guess, ≤ 2 sentences}
- Resolution requested: {which framing to adopt going forward}

Tagging @AUTHOR.  Will hold downstream work blocked on this.
```

The author owns the resolution.  Do not "split the difference" or
guess.  Inconsistent findings — whether between sibling PRs, or
between a reviewer and a sibling PR — are an audit flag in the
same way that conjectures-not-class-axiomatised are.

**Escalation rate-limit.**  An author who wakes up to fifteen
`@<author>` pings is a useless arbiter.  Batch-escalate when
possible: one comment listing every disagreement found in a
review pass, with a short table.

### 7.  Periodic sibling-PR triage

Sibling PRs land commits and comments while you work.  Without
periodic triage you will:

- duplicate a fix the sibling already landed,
- miss a question they posted directing back at you,
- accept a review-comment that contradicts a finding the sibling
  just published.

Run a triage **every 3–5 of your own commits**, or whenever you
finish one substantive task and pick up the next.  Format:

```
## Sibling-PR triage report (#NNN, {timestamp})

| PR | New comments | New commits | CI | Asks for me | Action |
|----|:---:|:---:|:---:|---|---|
| #564 | 6 | 8 | ✅ | (none) | none |
| #565 | 5 | 3 | 🟡 | P6 scope check (3 Q) | answer in next round |
| #568 | 1 | 1 | ⚪ | (cherry-pick acked) | post drop-duplicate notice |
```

For each "Asks for me" with verdict `answer` or `escalate`, queue a
coordination response in the next coordination round.  For verdict
`none` or `acked`, no further action.

**Use a background subagent for triage when possible** —
`Agent(subagent_type=Explore, run_in_background=true, prompt=...)` reads sibling
PRs without blocking your foreground work.  Triage prompt template:

> Background triage of sibling PRs <list>. For each:
> 1. New comments since <my last coordination round timestamp>.
> 2. New commits + sha + 1-line message.
> 3. CI status.
> 4. Specifically flag asks/replies directed at <my PR> + any
>    inconsistent findings vs <my key audit/proof claims>.
> Report under 400 words; per-PR table.

### 8.  Watching `main` and newly-created branches

Sibling PRs are not the only thing that moves.  `main` lands merges,
and **new branches/PRs** sometimes open mid-session by the author or
other agents — these need to enter the scope map immediately.

#### 8a.  Watch `main` for new commits

Run `git fetch origin main` at each triage cycle.  If new commits
landed since your last fetch, run:

```bash
git log --oneline <last-fetched-main-sha>..origin/main \
  -- <files-or-paths-you-are-touching>
```

For each main-landed commit that touches **a file or content block
you are editing**, classify it like a sibling PR using §2: overlap /
dependency / cherry-pick.  Then choose:

- **Merge `origin/main` into your branch** if the changes are
  additive and you don't have local edits to the same files.
- **Cherry-pick the relevant commit** if main's branch tip has too
  much unrelated noise.
- **Escalate to the author (§6)** if main's change contradicts a
  finding you just published.

Do not silently rebase or force-push to incorporate `main` — those
are author-authorised actions, see [`.github/copilot-instructions.md`
§ Git Operations].

##### 8a-bis.  Watch for new skills landing on main

In the same `git fetch origin main` pass, additionally run:

```bash
git diff --name-only --diff-filter=A \
  <last-fetched-main-sha>..origin/main \
  -- '.claude/skills/local/*.md' '.claude/skills/*/*.md'
```

For each new skill file:

1. **Read its frontmatter** (`name`, `roles`, `description`,
   `inherits`).
2. **Decide relevance**: does the skill's description overlap your
   branch's scope?
   - Mention a file kind / domain / pattern you're editing (touched
     in `git diff origin/main..HEAD --name-only`), OR
   - Provide a new integration-watcher child (`inherits:
     local/integration-watcher`) and your branch is itself an
     integration-watcher PR, OR
   - Provide a new QA / sweep / audit skill (one-voice-*, proof-*,
     compute-*, etc.) and your branch touches the corresponding
     content blocks.
3. **Surface to the user via `AskUserQuestion`** with the standard
   3-chip pattern from `local/watch.md §3.Q3a`:
   - `Adopt now` — invoke the skill on the relevant subset
   - `Defer to follow-up branch` — record decision, don't change
     this branch
   - `Not relevant` — record so the watcher doesn't re-prompt
4. **Record the decision in the coordination ledger** under a
   new `## New skills detected on main` subsection so future
   sessions don't re-prompt.

This mirrors `local/watch.md §3.Q3a` and lets every coordinator
session pick up new infrastructure (audit watchers, scoring
heuristics, formalisation helpers) as it lands, without the user
having to manually announce skill additions to every in-flight PR.

#### 8c.  Pre-push stale-state check (MANDATORY)

**Trigger:** before every `git push` (whether new commits or force-
push). The watcher can lapse during long focused work — Monitor
timeouts, hooks-busy windows, or background-agent waits all silently
leave `origin/main` unfetched. Before any push, force a fresh fetch
and compute the upstream delta:

```bash
git fetch origin main 2>/dev/null
DELTA=$(git rev-list --count HEAD..origin/main)
SIBS=$(git log --oneline ${MERGE_BASE:-$(git merge-base HEAD origin/main)}..origin/main 2>/dev/null | wc -l)
echo "main is ${DELTA} commits ahead since branch base"
```

Decision matrix:

| Delta | Action |
|---|---|
| `0..2` | push freely |
| `3..10` | **fetch and triage**: list each new main commit; for any touching files in your branch's diff, classify per §2 (rebase-now, defer, escalate) BEFORE pushing |
| `> 10` | **stop**: announce to the user. Long-discharge sessions risk substantial divergence; offer prepare-merge rebase OR continue + flag |

Additionally, run `mcp__github__list_pull_requests` filtered to
`state:open updated since <session_start>` and check for sibling PRs
that opened mid-session. Each new sibling enters scope per §3.

This check is the difference between a clean fast-forward push and a
multi-conflict rebase storm. If you're discharging many small commits
in a row (axiom sweep, witness regen, content cleanup), invoke this
between every ~5 commits OR after every 30 min of foreground work.

#### 8d.  Long-task drift recovery

If you discover ≥ 5 new main commits AFTER a Monitor timeout or
hooks-busy window, do NOT just "re-arm and continue":

1. **Compare**: `git diff --name-only HEAD..origin/main` to find
   overlapping files.
2. **If overlap is empty**: re-arm watch (silent OK).
3. **If overlap exists**: invoke `local/coordinate` §2 classification
   on each overlap. Most common: another agent edited the same content
   block (`*.lean`, `*.md`, `*.ts` trio). Resolve BEFORE committing
   more work that will conflict.
4. **Notify the user** if ≥ 2 substantive overlaps: this is the
   signal that multiple agents are working in the same scope and the
   user should coordinate goals.

#### 8b.  Watch for newly-opened PRs / branches

Each triage cycle, list open PRs and branches:

```bash
gh pr list --state open --json number,title,headRefName,createdAt
gh api repos/<owner>/<repo>/branches --jq '.[].name'
```

If a **new** PR or branch appears since the last triage and its
title / branch-name overlaps any of your scope keywords (your
audit subjects, your changed files, your conjectures), **prompt
the author**:

```markdown
**Q from #NNN:** I see #{N} (`{branch}`) opened at
{timestamp}; should I add it to my coordination scope (§3) and
post intent?  Or is it independent of the {goal} goal-thread?
```

Do not silently add the new PR to scope — the author may have
opened it as an isolated probe.  Wait for confirmation before
posting coordination comments on the new PR.

### 9.  Coordination ledger

Maintain a single shared ledger at:

```
docs/coordination/<goal-slug>.md
```

Each PR appends a row (no rewrites of others' rows):

```markdown
| Date | PR | Phase | Status | Cherry-pick |
|------|----|-------|--------|-------------|
| 2026-05-08 | #564 | P4′ T6 wire-up | landed `{sha}` | `t6_canonical_MeV` reader |
| 2026-05-08 | #565 | F8 pickle migration | in-progress | — |
| 2026-05-08 | #567 | crystal R-matrix Sub-lemma 2.1 | landed `{sha}` | `conj:crystal-graph-realization` Lean class |
```

The ledger lives on the branch where the coordinator is currently
posting; final state can be merged to main when the goal completes.

### 10.  Cherry-picking

**Cherry-picking is fine — treat it as a low-friction default.**
When an in-flight sibling has infrastructure (a script, a witness,
a Lean class template, a content block) that you'd otherwise
duplicate, just cherry-pick it. The cross-PR ceremony in earlier
revisions of this skill (mandatory "inform the sibling before",
"byte-for-byte identical or post the adaptation back") was
over-engineered for a working norm where small structured commits
exist precisely so they can be picked up by anyone.

The remaining rules are minimal:

1. **Cite the source in your commit message.** Either
   `Cherry-pick of #<N>:<sha>` on the trailer line or a
   `Co-authored-by:` line. Attribution is cheap and lets
   `git log --grep` surface who originated the change. Optional
   but recommended — missing attribution is not a blocker.

2. **One-voice still applies.** Whatever you keep from the source
   should read as your own work; rewrite voice / framing if the
   sibling's tone clashes (AGENTS.md voice rules don't relax just
   because the source was a different agent).

3. **You may diverge.** If you adapt the cherry-picked file —
   rename imports, change a helper, tighten a tolerance — that's
   normal. No requirement to post the adaptation back on the
   source PR; the sibling will see your divergence in their own
   §7 triage if it matters to them.

4. **You may pre-empt main.** Cherry-picks from open sibling PRs
   are explicitly allowed; you do not need to wait for the source
   to land on `main`. When the source eventually merges, you'll
   either pick up the canonical version on your next rebase
   (witness drift handled by the standard §1·a auto-resolve) or
   keep a slight divergence (also fine).

5. **Pre-flagging is optional.** If you're picking something
   substantive (a whole module, a large script) and want to
   reduce the chance of duplicated work, posting a one-liner
   coord comment on the source PR before picking is courteous —
   but it is **not required**. For small picks (single helper, a
   witness JSON, a class declaration), just commit.

When the source PR lands on `main`, attribution stops being
necessary — the file is just upstream code. A fresh PR sourced
from a main-merged commit needs no `Cherry-pick of` line.

### 11.  Asks and responses

Asks are a first-class artefact.  Format every cross-PR ask as:

```markdown
**Q from #NNN:** {question}

(answers as inline replies on the destination PR)
```

If a sibling has not answered an ask after 1 calendar day in an
async setting, restate the ask in a fresh comment and tag the
author.  Do not block indefinitely.

## Output

After invocation, you should have:

- Read every sibling PR's body and changed-files list.
- Posted at most one coordination comment per sibling PR (intent +
  asks), unless you've made progress that warrants a separate
  progress comment.
- Triaged every open review-tool thread on your own PR (§5) and
  posted a single consolidated status comment.
- Run a §7 periodic triage every 3–5 of your own commits, capturing
  new sibling-PR comments + commits + CI status in one table.
- Run §8a (`git fetch origin main`) at each triage cycle and react
  to any main-landed changes that touch your scope.
- Run §8b (newly-opened PRs / branches) at each triage cycle and
  prompt the author when a new sibling overlaps your scope keywords.
- Identified the next concrete, non-overlapping task on your own
  workplan and started on it.
- (Optional) Created or updated `docs/coordination/<goal-slug>.md`
  with the current state.
- Escalated any inconsistencies via §6 with `@<author>` tagging.

## Anti-patterns

- ❌ Post a coordination comment that just summarises your own PR.
  Sibling agents already read your PR body.
- ❌ Pick the same task as a sibling without posting first.  Even
  if their PR has been quiet, the human author may have given them
  a verbal lead.
- ❌ "Resolve" an inconsistency by rewriting your finding.  Escalate
  to the author.
- ❌ Accept a review-tool fix without verifying it against the
  proof and sibling-PR conventions.  Bot suggestions can flip
  conventions silently.
- ❌ Reply per-thread on a 6-comment review pass.  Use one
  consolidated status comment + per-thread `accept` /
  `reject-with-reason` flags.
- ❌ Skip §7 triage between commits because "I would have heard if
  something landed" — you wouldn't.  Sibling agents work in parallel
  and rarely interrupt each other.  Run the triage anyway.
- ❌ Silently merge / cherry-pick from `main` without §8a
  classification.  Main commits can also be inconsistent findings.
- ❌ Add a newly-opened PR to your scope without prompting the
  author (§8b).  The author may want it independent.
- ❌ Long prose.  Coordination comments are tables, file pointers,
  and one-line asks.

## §11 STATUS.md + master ledger pattern (2026-05-31)

The 4× c_k flip-flop episode (PR #1580 history) prompted a more
structured coordination layer that overlays this skill:

- **Root [`STATUS.md`](../../../STATUS.md)** — single dashboard
  listing every goal + pointer to its master ledger + active PRs.
- **Master ledger per goal** — `docs/coordination/<goal>.md` holds
  the durable narrative: current canonical status, open probes,
  flip-flop history, sessions log.
- **Per-goal queue** — `todos/<goal>-queue.json` (committed, typed
  as `TodoItem[]` per `folio-assistant/schemas/types.ts`); each
  open probe is one entry.

When `/coordinate` runs, it now ALSO:

1. **Reads STATUS.md** to find which goal(s) the current PR
   touches.
2. **Reads the goal's master ledger** to identify the current
   canonical status — overrides recent commit claims if the
   ledger records a retraction.
3. **Reads the queue file** to find sibling probes in flight.
4. **References the ledger session log** when posting intent
   comments on sibling PRs, so the comment is grounded in the
   durable record, not just session memory.

See `local/session-intent` for the session-start / session-end
ledger + queue update protocol — `/coordinate` is the sibling-PR
arm; `/session-intent` is the durable-state arm. They are run
together at session start.

## §12 Multi-agent same-goal coordination (2026-05-31)

**Multiple agents MAY work the same goal in parallel.** The author's
2026-05-31 directive: "ok if multiple agents attack same goal at
once — the agents coordinate with user on goals."

Model:

- **Goal** = product (author's directive). User-level concern.
- **Queue** = per-goal item list (`todos/<goal>-queue.json`).
- **Probes** are NOT exclusively claimed. Two agents may attack the
  same probe with different methods (Habiro recursion vs PSLQ basis
  sweep) — both threads have value.
- **Coordination is with the USER** on goal-level decisions, not
  agent-to-agent on probe-level locks.

### When you detect a sibling agent on your probe

Signals:

- The queue entry has `co_assignees` populated, OR
- A sibling PR (from `mcp__github__list_pull_requests`) has commits
  touching your probe's scope files within the last 24h, OR
- The ledger session log shows another agent declared intent on
  the same probe ID.

Workflow:

1. **Do not silently abandon.** Your independent attack is valuable.
2. **Post intent** on the sibling PR (this skill §3) so the sibling
   sees you're also working it.
3. **Ask the user** with `AskUserQuestion` whether to keep both
   threads or have one stand down. Include rich context per AGENTS.md
   §User accessibility — quote what each agent is doing, what method,
   what's been found, cost of running both.
4. **If user says one stands down**, the standing-down agent appends
   partial results to the ledger and updates queue
   `status: "open"` (releasing the probe). The continuing agent
   may pick up the partial results.

### Watching for sibling-PR contradictions

Per §8 of this skill: at each triage cycle, look for sibling-PR
commits or comments that **contradict** your branch's framing. Per
§6: escalate inconsistent findings to the user. Do not silently
adopt the sibling's framing without an §6 conversation.

## Related skills

- `local/delivery-summary` — what to post **after** a feature lands
  (one PR scope).
- `local/watch` — passive monitoring of upstream branches.
- `local/diff` — per-block change report (one PR scope).
- `local/session-intent` — session-start / session-end ledger +
  queue update protocol (the durable-state arm of coordination).
- `local/pending-show` — read-only display of current session's
  pending work (todos, intent, queue assignments).
- `local/prepare-merge-auto` — autonomous merge pipeline (uses
  this skill's §0 sibling-coord pattern).

`/coordinate` complements them: it is the **active** cross-PR
protocol — including handling of code-review comments on your own
PR — not a passive watcher and not a single-PR summary.

## Flag-bearer reflections — step-9 binding cluster (2026-06-05)

Lessons from acting as flag-bearer across ~8 sibling PRs on a shared
goal (the binding-closure cluster). Apply when you hold the flag.

1. **Build the ledger hub FIRST, then post.** Create
   `docs/coordination/<goal>.md` with: the direction (one boxed
   identity), the *common infra everyone rows toward* (cheat-sheet step
   table, watcher queues, dashboards, a falsification anchor), and a
   per-PR "which way to row" roster with **report-back slots**. Post
   intent only after the hub exists, so every comment can link one
   canonical place. This is what makes "make sure all use common infra"
   actionable rather than a slogan.

2. **Tailor per-PR; then LISTEN.** A flag-bearer that only broadcasts is
   half-doing the job. Pull each sibling's current state (a background
   `Explore` agent reading PR bodies + last comments is ideal), and
   **fold their findings back as sharpenings** to your own plan. This
   session two sibling facts reshaped the workplan: #1839's precision
   floor (c_k unmeasurable) ⇒ the kernel must be *fibre-derived not
   data-extracted*; #1765's `λ(L)=(1/(c+1))Σ dim_q` ⇒ a lemma I planned
   was *already a zero-param rule*. Record sharpenings in the ledger and
   amend the workplan — do not silently keep the stale plan.

3. **Anchor the cluster to one falsifiable number.** Give every sibling a
   shared regression target (here: the magic-A ⁴He **+5.87%**). It turns
   "which way to row" into a checkable claim and prevents divergent
   re-derivations.

4. **Push-race coordination with background agents.** When a background
   sub-agent and you both push to the same branch, wrap every push in a
   `fetch → rebase → retry` loop:
   `for i in 1 2 3 4; do git push && break || { git fetch origin <br> -q;
   git rebase origin/<br>; sleep $((2**i)); }; done`. The agent's commits
   may already be in your local history (shared working dir) — check
   `git log` before assuming a divergence.

5. **Billing-CI is noise — do not let it derail coordination.** This
   cluster's CI failed setup-phase (≤5 s, simultaneous, no logs) on every
   push all session while local `validate`/`lake env lean` stayed green.
   Recognise the billing signature (AGENTS.md "CI billing failures"),
   note `[skip-ci: billing]`, and keep working; never re-diagnose it as a
   code problem or pause the cluster for it.
