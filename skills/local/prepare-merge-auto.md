---
name: prepare-merge-auto
description: Full autonomous prepare-merge → resolve → merge pipeline. Coordinates with sibling PRs, resolves review comments, asks structured questions only when blocked, then merges.
roles:
  - collaborator
  - owner
---

# /prepare-merge-auto — Autonomous merge pipeline

Runs the full `/prepare-merge` workflow PLUS:

1. **Sibling coordination** (before starting)
2. **Review-comment resolution** (after reviews land)
3. **Structured user questions** (only when genuinely blocked)
4. **Merge** (after all comments resolved)

## Workflow

### Phase 0: Sibling coordination

Before starting the merge pipeline, identify sibling PRs whose scope
overlaps this branch's files:

```
mcp__github__list_pull_requests(owner, repo, state="open")
```

For each sibling PR that touches the same files or content domain:
- Post a brief coordination comment: "Starting prepare-merge on
  #<this-PR>; touches <files>. Review welcome if you'd like to
  check for conflicts before merge."
- Do NOT wait for responses — this is a courtesy notification, not
  a blocking request.

### Phase 1: /prepare-merge (steps 1–6)

Execute the full `/prepare-merge` skill (rebase, integrate, one-voice,
Lean build, final rebase, request reviews). All steps must succeed
before proceeding.

**🛑 If the branch touches any `.lean`, the Lean step is a SWEEP, not bare
`lean`-direct.** `/prepare-merge` §4 carries the reasoning; the short version is
that `lean`-direct against the restored olean cache verifies against a
**snapshot**, so a library signature that moved afterwards leaves the file green
and broken at once. That is not hypothetical — `descartesWtrace` recorded
`exit 0` and landed on `main` red (#6751).

```bash
scripts/lean-content-sweep.sh <changed content-block .lean ...>   # or no args
scripts/lean-library-sweep.py                                     # dirty closure
```

Both rebuild from source only the modules whose own olean predates their own
last source commit, and never invoke `lake`, so the restored cache is not
evicted. Library sweep is 122 s on a 74-module closure; the content sweep is
~50 min for all 261, so pass the changed files when you have them and
`SHADOW=<dir>` to reuse the shadow.

**Record which one ran, in the PR, in these words** — this is the Phase-4
verification gate's evidence and the distinction it turns on:

- *"`lean-library-sweep.py`: N/N dirty modules rebuilt from source, exit 0"* —
  source-verified.  Quote its `VERDICT:` line.  Exit **8** (`INCOMPLETE`) means
  no RED but some module TIMEOUT / UNVERIFIED / BLOCKED: that is **not** a
  green, so do not write "exit 0" for it (bean `qou-tpdg`).
- *"`lean`-direct against the restored cache, exit 0"* — snapshot-conditional.
  Say so, and say why the sweep was not run.

A sweep result is **container-scoped** (the dirty closure is computed against
this container's olean tree) and does **not** cover the UGB or Fred2005
packages. Do not write either limit out of the PR. Bean `qou-56qy`.

**Sidecar conflicts during the rebase.** Resolve `content/**/*.qa.json`
to either side as usual for the **script** entries, then restore the
other side's **agent** entries mechanically:

```bash
python3 scripts/qa-sidecar-agent-union.py --against <pre-rebase-ref> --apply
```

An agent verdict has no producer — `qa-sweep` regenerates script
candidates and never a judgement — so "let the pipeline re-run it" loses
those entries silently. The #5103 takeover dropped 7381 of them that
way (`qou-tqr9`). The script is additive and skips any entry whose
`field_hash.md` no longer certifies the merged `.md`.

### Phase 1b: Wait for reviews + status briefing

**Wait for the Copilot review to land** before proceeding.
Do NOT skip ahead — the review is the input to Phase 2.

> **Gemini is sunset — never wait on it (2026-08-07).** The consumer
> Gemini Code Assist GitHub integration has ceased all code-review
> activity; a `/gemini review` comment is answered only by a
> `[!CAUTION]` sunset notice, or by nothing at all. **Copilot is the
> only live external reviewer.** Waiting for a Gemini review that can
> never arrive is the documented stall mode (PR #4456).

> **🛑 CORRECTED 2026-08-30 (bean `qou-426q`) — READ THIS BEFORE THE BANNER
> BELOW. The banner is half right, and the wrong half is the operative one.**
>
> Measured on #6104, #6116, #6132:
>
> | claim | verdict |
> |---|---|
> | `get_check_runs` returns `total_count: 0` — no `copilot-pull-request-reviewer` run is ever created | **CONFIRMED** |
> | therefore **zero reviews arrive** | **FALSE** — Copilot reviewed #6104 and #6116 |
>
> **The mechanism is UNSETTLED — do not repeat my first explanation.** I
> wrote here that Copilot "delivers via webhook, not check run, so the poll is
> structurally blind". That is a *candidate*, not a finding, and it does not
> discriminate: `total_count: 0` is equally consistent with every other
> candidate, including simple quota exhaustion. The adjudicated write-up is
> [`docs/audits/2026-08-30-copilot-review-works-again.md`](../../../docs/audits/2026-08-30-copilot-review-works-again.md)
> (bean `qou-gwe9`, **reopened**), which weighs three and picks none:
> availability changed; Copilot reviews on its own trigger rather than on
> `request_copilot_review`; or a quota gates it, making the whole thing
> intermittent.
>
> **🛑 THERE IS A QUOTA, and it is easy to exhaust.** That audit measured five
> requests across two repos in ~30 minutes returning *"the user who requested
> the review has reached their quota limit"*. Copilot review is a **rationed**
> resource, not a binary available/unavailable one. **Do not re-request after
> every push** — nothing else in the repo's docs says this, and it is the
> operational rule that actually follows from the measurement.
>
> **Cost, on the record:** #6104 and #6116 were merged on the "do not wait"
> guidance and the reviews landed minutes later, carrying six findings — one a
> real correctness regression (a tautology introduced into a three-path
> cross-check, so its printed "should be ≈ 1.0" ratio read exactly 1.0 by
> construction). Fixed in #6132, after the merge.
>
> **What to do:** do NOT restore a blocking poll on check runs — that half of
> `qou-gwe9` stands and the poll would still see nothing. Instead, subscribe
> to the PR (`subscribe_pr_activity`) and expect the review to arrive as a
> wake. A merge is not gated on a check run that does not exist, but a
> subscribed session **must handle the review when it lands** — which, after a
> merge, means a follow-up PR rather than nothing. **Latency is unmeasured**
> (n=2, both within minutes); do not write a specific wait window into this
> skill on that basis.
>
> The original banner follows, and its check-run half remains accurate:
>
> **🛑 MEASURED 2026-08-23 — do NOT run this wait. Copilot never enqueues.**
> n=5 (bean `qou-gwe9`, AGENTS.md rule 10): on #5474, #5495, #5411, #5459 and
> #5482 the review was requested explicitly and **zero** arrived. Critically
> `get_check_runs` returns `total_count: 0` — there is no `queued` or
> `in_progress` `copilot-pull-request-reviewer` run, so step 1 below polls for
> an object that is never created and the 15-minute cap is the only exit.
> Re-requesting after a force-push does not help (#5459), and the cases span
> new Lean, a 20-file revert and a `.beans/`-only change, so the
> "did not trigger for this file type" reading in step 1 does not survive n=5.
>
> **Do this instead:** request the review once (cheap, keeps the record), then
> proceed immediately with 0 comments and say so in the briefing —
> "Copilot: not enqueued (measured, `qou-gwe9`)". With CI dispatch-only and
> Gemini sunset, there are **zero** live external gates; your own verification
> is the whole gate, so state what you ran.
>
> The protocol below is kept for the day a reviewer is reinstated.

**Wait protocol (15-minute window — extended 2026-05-31 per author):**

1. After requesting reviews in Phase 1, poll for Copilot's
   check-run status every 30 seconds (up to 15 minutes):
   ```
   mcp__github__pull_request_read(method="get_check_runs", ...)
   ```
   Look for the `copilot-pull-request-reviewer` check run:
   - `"status": "queued"` or `"status": "in_progress"` → reviewer
     has noticed the PR; keep polling every 30s
   - `"status": "completed"` → reviews are in, proceed immediately
   - No check run after 2 minutes → reviewer did not trigger for
     this file type (e.g. skill-only PRs with no code); proceed
     with 0 comments

2. **Check that Copilot reviewed the CURRENT head.** A review whose
   `commit_id` is an earlier commit is stale and does not count —
   re-request with `mcp__github__request_copilot_review` and keep
   polling. (PR #4456 carried a 13-file review against an 85-file
   head.)

3. **15-minute hard cap**: if Copilot has not completed after
   15 minutes, proceed with whatever comments have landed. Note
   "Copilot: timed out (15 min)" in the briefing.

Once reviews arrive (or the 15-minute cap is reached), give the
user a concise **status briefing**:

1. **PR identity**: "#N — title" with clickable URL
2. **Branch**: `branch-name` → `main`
3. **Scope**: files changed, additions/deletions, commits
4. **Review comments received**: total count, by reviewer, with
   1-line summary of each thread:
   ```
   Review comments (3 total — Copilot: 3):
     1. [Copilot] line 42 engine.py — threshold mismatch
     2. [Copilot] line 98 engine.py — unused variable
     3. [Copilot] line 173 engine.py — spelling fix
   ```
5. **Disposition plan**: for each comment, state the planned
   action (accept / modify / reject / escalate) BEFORE making
   changes — so the user can redirect:
   ```
   Plan: accept 1,2,3; accept-with-modification 4; reject 5
   (reason: "classical limit" is the standard term per §7a)
   ```
6. **CI status**: green / failing / pending

The user can reply with overrides (e.g. "reject 4", "skip 2,3").
If no override within ~30 seconds, proceed with the stated plan.

### Phase 2: Resolve review comments

After the briefing (and any user overrides), triage each thread:

| Classification | Action |
|---|---|
| **accept** | Apply the suggested fix, commit, push. |
| **accept-with-modification** | Apply a modified version, commit with explanation. |
| **reject-with-reason** | Reply on the thread with the reason (e.g. "intentional — see §X"). |
| **escalate** | Cannot resolve autonomously — proceed to Phase 3. |

For each resolved thread, commit the fix with message:
`fix(PR #N): address <reviewer> thread r<id> — <1-line summary>`

Push after each batch of resolutions.

### Phase 3: Structured user questions (only when blocked)

If any review comment requires a judgment call (ambiguous intent,
architectural decision, multiple valid approaches), use
`AskUserQuestion` with:

- **Rich context** per AGENTS.md user-accessibility rules:
  - Quote the exact comment + file path + line number
  - Show the current code vs proposed change (preview)
  - State trade-offs for each option
  - Default to `multiSelect: true` unless choices are mutually exclusive
  - Prefix with 🟡

- **Batch questions** — collect ALL blocked items into a single
  `AskUserQuestion` call (up to 4 questions) rather than asking
  one at a time.

### Phase 4: Merge

After all review comments are resolved (or the user has answered
all escalated questions):

1. Run `bun run scripts/run-validate.ts content/<paper>` one final time.
2. **If the branch touches any `.lean`, the sweep from Phase 1 must have run on
   the FINAL head, and its result must be in the PR.** A sweep on an earlier
   commit is not evidence about what is being merged — the final rebase in
   `/prepare-merge` §5 moves the branch onto a `main` whose library may have
   shifted underneath it, which is the exact mechanism this gate exists for.
   Re-run it after that rebase, not before.
3. Check CI status via `mcp__github__pull_request_read get_check_runs`.
   Expect `total_count: 0` — auto-triggers are disabled repo-wide, so this
   returns nothing and is **not** a gate. Never read it as green.
4. If all green: merge via `mcp__github__merge_pull_request` with
   `merge_method: "rebase"` (default per AGENTS.md §"Branch + PR
   workflow" rule 8 — replays the structured commits onto `main`
   linearly, no merge commit). Rule 8 is authoritative.
5. **CRITICAL:** DO NOT DELETE THE BRANCH EVER! If using the GitHub CLI, DO NOT pass `--delete-branch`. If using the GitHub API, ensure the branch is preserved.
6. Report the merge SHA + URL.

### Phase 5: Post-merge verification, then coordination

**Verify the merge replayed every commit — this phase had no check at all
until 2026-09-04, and the failure it misses is on the record.**

```bash
scripts/verify-merge-replay.py --branch origin/<branch> --merged <merge-sha>
```

A rebase-merge can land 7 of 8 commits and still report success through the
API. PR #5111 did exactly that; it was recovered as #5125, and only because
someone grepped `main` for the edited content.

**Do NOT verify with `git diff origin/main <merged-head>`.** After a
rebase-merge the PR's head *becomes* main's tip, so that command compares a
commit **to itself** and returns empty whether or not anything was dropped —
strongest-looking evidence, zero information. Whenever the PR is the last thing
merged (the normal case for this pipeline) it cannot fail. Ten PRs were merged
on 2026-08-15 under an instruction calling it *"the strongest check"*; bean
`qou-vtau`. Its mirror image misleads too: diffing main against the **pre-merge**
branch head shows every sibling PR that landed in between as though it were
yours.

The script compares **patch-ids** — a hash of each commit's diff, invariant
under rebase, where shas are not. Run `--selftest` if you want to confirm it can
still detect a drop; it synthesises one and asserts the patch-id check catches
what `git diff` misses.

Two behaviours to read correctly rather than "fix":
- a commit with an **empty diff** has no patch-id and is reported separately,
  not counted as replayed;
- a commit whose content **changed** during the rebase (a conflict resolved
  differently) reports MISSING by design — it did not replay, and the
  resolution deserves a look.

Then coordinate:
- Post a brief update on any sibling PRs that were notified in
  Phase 0: "PR #<N> merged; <files> updated on main. Please rebase
  if needed."
- Unsubscribe from the merged PR's activity.

## Error handling

- If `/prepare-merge` fails at any step, STOP and report the
  blocker. Do not request reviews on a broken branch.
- If CI fails after pushing review fixes, investigate and fix
  before merging.
- If the user doesn't respond to Phase 3 questions within the
  session, leave the PR open with a summary comment listing the
  unresolved items.

## Anti-patterns

- Do NOT merge without resolving review comments (even if CI is green).
- Do NOT squash unless the user explicitly says "squash" on this PR.
- Do NOT wait on a Gemini review — Gemini Code Assist is sunset.
- Do NOT **block** on a Copilot review — but do NOT skip reading it either.
  The "n=5, never enqueues" line that stood here is **refuted**; see the
  Phase 1b correction above. Reviews arrive (minutes), carry real findings,
  and are **rationed** — so request once, keep working, and read
  `get_reviews` before you merge. Never poll `get_check_runs`: it returns
  `total_count: 0` whether or not a review exists, so it cannot tell you.
- Do NOT verify a merge with `git diff origin/main <merged-head>` — after a
  rebase-merge that compares a commit to itself and can never fail. Run
  `scripts/verify-merge-replay.py` instead (Phase 5).
- Do NOT skip sibling coordination — it prevents post-merge conflicts.
- Do NOT ask trivial questions in Phase 3 — only genuinely ambiguous
  decisions warrant user input.
- **Do NOT delete the branch after merging.**
- Do NOT resolve a `.qa.json` conflict to one side and rely on
  `qa-sweep` to regenerate it — that is correct for script entries and
  drops agent verdicts (see Phase 1).
