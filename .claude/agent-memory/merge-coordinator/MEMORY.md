# merge-coordinator — memory

Entry types: **STABLE** · **TRAP** · **BASELINE** (re-measure, never quote).
Seeded 2026-08-29 from `AGENTS.md`. Confirm entries as you use them. Detail
lives in sibling files; keep this file under 200 lines so it all gets injected.

## TRAP — ALL THREE Phase-4 external gates are dead. Do not wait on any.

This is the single most expensive thing in this file. `prepare-merge-auto`
Phase 1b still prescribes a 15-minute poll for a check run that is never
created; that wait **can only expire**.

| gate | actual state |
|---|---|
| **CI green** | Unavailable. Auto-triggers disabled repo-wide (owner directive 2026-06-30, Actions billing). `build.yml` is `workflow_dispatch`-only; there is **no** `lean_ci.yml` in the tree. Feature branches routinely show **zero** workflow runs / zero check runs. |
| **Gemini review** | Gone. The consumer Gemini Code Assist on GitHub was sunset — "All code review activity has officially ceased" (bot notice, PR #4514, 2026-08-01). |
| **Copilot review** | **TRAP — this row was wrong, corrected 2026-08-30.** Reviews DO arrive (~3-4 min; measured on qou#6122, folio-assistant#153, and on qou#6104/#6116 where they landed minutes AFTER a merge taken on this row's old advice, carrying six findings incl. a real correctness regression). **They are RATIONED** — five requests across two repos in ~30 min hit *"reached their quota limit"*, so never re-request after every push. `get_check_runs` really does return `total_count: 0`, but that does NOT discriminate and must not be read as "none coming"; the review arrives as a `pull_request_review.submitted` wake via `subscribe_pr_activity`. Mechanism for the historical zeros is UNSETTLED — see `docs/audits/2026-08-30-copilot-review-works-again.md`, bean `qou-gwe9` (reopened). Superseded text: Measured n=5, bean `qou-gwe9`: requested via `request_copilot_review` on #5474, #5495, #5411, #5459, #5482 — **zero** reviews every time, and `get_check_runs` returns `total_count: 0` rather than a queued `copilot-pull-request-reviewer` run, so nothing is ever enqueued. Re-requesting after a force-push does not help. The cases span new Lean, a 20-file revert and a beans-only change, so it is not file-type-conditional. |

**So the gate table has ONE intermittent external gate (Copilot, quota-limited), not zero.** The agent's own
verification is not the last gate standing — it is the *only* gate. Do not block on a check-run poll (it sees nothing), but DO expect a
review wake on a subscribed PR and handle it — after a merge that means a
follow-up PR, not nothing.

`AGENTS.md`'s heading over this table read "Two of the three" while the table
and its own closing paragraph both said three; an agent skimming the heading
waits forever. Corrected 2026-08-28.

## STABLE — the Phase-4 verification gate (what replaces "CI green")

State the evidence explicitly in the PR:

- **Lean changed** → `lean`-direct **exit 0** on every changed file, built
  against its **real import cone** (not a stubbed harness), plus
  `#print axioms` on the new declarations showing no `sorryAx`. A **library**
  file under `content/<paper>/lean/QOU/**` has no `.qa.json` sidecar and is
  **not** covered by `lean-content-siblings.yml` — nothing but the agent
  checks it.
- **Content blocks changed** → `scripts/check-sidecars.sh` clean +
  `qa-sweep` on the touched criteria; math-bearing `.md` also needs the
  render-QA gate.
- **Compute changed** → the producer re-run + witness refreshed, and
  `scripts/precision-gates.sh`.

**Never write "CI green" in a PR or merge rationale unless a run exists.**
Say which verification you ran. If a workflow *is* wanted for a specific PR,
kick it manually via `workflow_dispatch`.

## TRAP — a 2–3 second multi-job failure is billing, not code

Recognise it by: all failing jobs complete in ≤ 5 s (setup-phase only —
checkout / pip install alone take longer); multiple jobs fail together with
the same `started_at`; local reproduction passes; the webhook says
`conclusion: failure` but no error log exists because the job never started.
The MCP API does not expose job-startup-phase reasons.

Do **not** diagnose it as a code issue and do **not** push retrigger commits
— billing does not clear on retry. Notify the user, and document the skip in
the PR: `[skip-ci: GitHub Actions billing; local validate exit 0]`.
History: PR #1435, three consecutive failures with this exact pattern.

## STABLE — merge method

**Rebase** by default (`merge_method: "rebase"`). It preserves the
per-cluster commits, keeps `git bisect` meaningful, and leaves no empty
merge-commit noise.

**Never squash** without explicit per-PR permission from the owner ("squash
this one" / "squash OK"). "The branch looks noisy" is not sufficient
justification — clean it locally with `git rebase -i` and rebase-merge the
cleaned history. A merge commit is acceptable only when the PR is a
sub-merge of already-merged siblings and serves as a navigable boundary.

This overrides any conflicting merge-method advice in
`.claude/skills/local/*.md`.

## STABLE — never delete a branch (owner directive 2026-06-12)

No `git push origin --delete`, no auto-delete-on-merge, and never offer
branch deletion as a "cleanup" option. Closed branches are the historical
record: PR head SHAs stay resolvable, session links and coordination-ledger
references stay live, and `lake-cache/*` orphan branches are **load-bearing
infrastructure**.

## STABLE — sibling coordination

- List active siblings via `list_pull_requests` (open) + `list_branches`
  (recent `claude/*`).
- Post intent **only** on genuinely overlapping PRs — same chapter, same
  Python/Lean file, same domain. 1–3 sentences. Do not post on every sibling
  and do not make noise.
- Proactively comment when a finding on your branch is one a sibling is
  about to step on.

**Measured research-overlap is PERMITTED** (owner relaxation 2026-07-18) for
genuinely *open-outcome* research — a different agent context may reach the
solution by a different route. **Mechanical work is not**: sweeps, sidecar or
witness regeneration, refactors, wiring an already-derived result,
doc-currency, migrations have one right answer and **one owner**. The test:
is the answer *unknown* (research, may overlap) or merely *not-yet-typed*
(mechanical, one owner)? State your distinct angle when you do overlap, and
converge on landing — the second route re-scopes to verify/extend/refute,
citing the first.

## STABLE — stalled-claim takeover

A bean at `in-progress` whose backing branch has had **no new commit for
> 3 h** is presumed abandoned and may be taken over. **Scope:** only the
branch backing a *live in-progress bean* — **never** the thousands of
long-idle `claude/*` branches, which are permanently stale and are never
takeover targets by age alone.

Before taking over: confirm genuine staleness (last commit > 3 h AND no
newer PR activity / no in-flight CI — a long build is not a stall), re-claim
the bean with a `--body-append` noting the takeover and the stale branch's
last SHA, and continue from that branch's tip or from `main`. **Never
force-push over a sibling's branch.** This is the one sanctioned exception
to "never touch a sibling's claim".

## STABLE — commit granularity

Good: "scaffold module X" / "implement X.foo() — case B (braid relation)" /
"tests: cross-check vs reference at 50-dps" / "address review (5 comments)".
Bad: one giant "implement X" mixing scaffold + implementation + tests.

Exception — a **mechanical sweep** across many blocks/scripts/witnesses is
one bulk commit ("regenerate N sidecars after checker fix"): the change is
uniform, cherry-pick is rarely useful, and the audit doc plus the bulk
commit convey the intent. A single non-sweep commit > 50 files or > 1000
lines is a signal to break it up.

## STABLE — asking the author anything at all

Full six-part frame is in AGENTS.md §User accessibility, already in your system
prompt — do not re-derive it here. The parts that bite *in this role*: naming a
decision **is** asking a question even in an end-of-turn line, a `**next**` bean
entry, or a "suggested follow-up" in a PR body, and each owes options with
what-it-means / costs / risks / commits-to, **the default if they say nothing**,
and a recommendation marked as judgement. Mirror any `AskUserQuestion` as chat
prose above the call; default `multiSelect: true`, prefix 🟡. **Cheapest correct
move when you won't spend the words: don't raise it** — put it in a bean.

## TRAP — `update_pull_request` is a PARTIAL write, and its rate-limit error lies

It is split across two APIs with **separate rate-limit budgets**: REST for
title/body, GraphQL for the `draft` toggle. Measured on `qou#6264` 2026-08-31 —
one call returned *"API rate limit already exceeded"* while the **title and body
landed** and only `draft` did not. So: **re-READ the PR before re-sending or
reporting a failure** (I re-sent four times against a limit that was never
blocking it), do not generalise "rate limited" across the whole API, and know
there is **no REST path to un-draft** — a GraphQL outage blocks the merge
outright, so wait and re-arm rather than close-and-reopen or open a fresh PR.
Discriminator: `merge_pull_request` is REST, so it returns a *real* error
(`405 Pull Request is still a draft`), isolating the blocker to GraphQL.
Detail: [`update-pull-request-partial-write.md`](update-pull-request-partial-write.md).

## TRAP — API dead session-wide · shared worktree · float64-guard marker

2026-08-31, TWICE (#6395/#6396, then #6400/#6401 — the API gate is **2/2, a
STANDING condition**). Recipes: [`api-down-and-shared-worktree.md`](api-down-and-shared-worktree.md).

1. **API dead session-wide, `git` fine.** All `mcp__github__*` → *"No such tool
   available"*, no `gh`, REST **403 "GitHub access is not enabled for this
   session"** — an Anthropic *session gate*, not repo permission, not rate
   limiting, and it does **not** clear on retry. `git` over HTTPS is
   unaffected, so fetch/rebase/push/**merge** work while PR comments, review
   requests and `subscribe_pr_activity` do not (the post-push hook then cannot
   be satisfied — environmental, not a lapse). Merge = push the branch, then
   push that **same SHA** to `main` (so GitHub marks it merged); prove
   `merge-base --is-ancestor` first and keep the `main` push non-force, which
   makes it FF-only and self-guarding.
2. **`/home/user/qou` is SHARED with concurrent siblings.** I checked out a
   branch there mid-session; **their next commit landed on my branch** and would
   have shipped inside #6395. Symptom: **`HEAD` is not what you set it to**
   (`rev-parse` to verify, `reflog` to diagnose). Work in
   `git worktree add --detach`. Never `git add -A` (sweeps sibling files + the
   `qou-v0t8` audit witnesses); never `git checkout <ref> -- <path>` to peek —
   it writes the index — use `git show <ref>:<path> >`.
3. **`probe-float64-guard`**: `# float64-ok:` must sit **on** the flagged line
   (a block above only shifts line numbers). `from math import comb`/`factorial`
   flag but are exact `int` — a real false positive; verify, annotate, never
   widen a baseline. Grepping `math\.(sqrt|exp|log)` misses `from math import`.

## BASELINE — re-measure, do not quote

| what | command | last seen | when |
|---|---|---|---|
| Copilot reviews arriving | `request_copilot_review` then watch for a review wake | rationed; `get_check_runs` = 0 does not discriminate | `qou-gwe9`, 2026-08-30 |
| workflows with auto-triggers | `grep -l 'on:' .github/workflows/*.yml` then read each | dispatch-only repo-wide | 2026-06-30 directive |

## Session log — one entry per PR; prune this, never the TRAPs

- **#6395** `337dd658c7` / **#6396** `34f2352431` (2026-08-31, FF pushes, API
  403-gated so no PR comments). Both merged on agent verification alone: probes
  exit 0, float64 guard clean, stdout byte-identical across comment-only edits.
  Two defects caught that the hand-off said were absent — a **retraction that
  reached the runtime block but not the module docstring** (#6395, so the file
  asserted the retracted route where a reader looks first), and a **red
  float64 guard** (#6396, adjudicated a false positive on exact-int
  `math.comb`/`factorial`). *Re-run the gates; do not trust "already verified".*
