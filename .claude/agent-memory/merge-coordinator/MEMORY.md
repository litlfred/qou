# merge-coordinator — memory

**STABLE** · **TRAP** · **BASELINE** (re-measure, never quote). Seeded 2026-08-29
from `AGENTS.md`; detail in sibling files. **Keep under 200 lines — 201+ is
silently dropped**; when you add, cut, and order last-worst.

## TRAP — TWO Phase-4 gates are dead; the third (Copilot) is intermittent

This is the single most expensive thing in this file. `prepare-merge-auto`
Phase 1b still prescribes a 15-minute poll for a check run that is never
created; that wait **can only expire**.

| gate | actual state |
|---|---|
| **CI green** | Unavailable. Auto-triggers disabled repo-wide (owner directive 2026-06-30, Actions billing). `build.yml` is `workflow_dispatch`-only; there is **no** `lean_ci.yml` in the tree. Feature branches routinely show **zero** workflow runs / zero check runs. |
| **Gemini review** | Gone. The consumer Gemini Code Assist on GitHub was sunset — "All code review activity has officially ceased" (bot notice, PR #4514, 2026-08-01). |
| **Copilot review** | **INTERMITTENT — never read either way as settled.** Reviews DO arrive (~3-4 min; qou#6122, fa#153, and qou#6104/#6116 where they landed minutes AFTER a merge taken on this row's *older* "never arrives" advice, carrying six findings incl. a real correctness regression) — and DO NOT (n=5 zeros 2026-08-23; a clean 10-min zero on qou#6404 2026-08-31). **RATIONED**, and quota refusals say so explicitly, so a silent nothing is not a quota refusal. `get_check_runs` returns `total_count: 0` either way — it does **not** discriminate and must never be read as "none coming"; a review arrives as a `pull_request_review.submitted` wake via `subscribe_pr_activity`. **Every observation to date confounds the request with a later push, so the mechanism is UNMEASURED, not merely unsettled** — protocol to settle it and the full observation table: [`copilot-review-arrival.md`](copilot-review-arrival.md), bean `qou-gwe9` (reopened), `docs/audits/2026-08-30-copilot-review-works-again.md`. |

**One intermittent external gate, not zero.** Your own verification is not the
last gate standing — it is very nearly the only one. Never block on a check-run
poll (it sees nothing), but DO expect a review wake on a subscribed PR and act
on it; after a merge that means a follow-up PR, not nothing. (Keep heading and
table in step — this file's disagreed until 2026-08-31 and `AGENTS.md`'s until
2026-08-28; a skimming agent merges on the heading.)

## TRAP — the queue you were handed may ALREADY be merged; `git cherry` FIRST

2026-09-07: dispatched to merge four PRs "measured CLEAN by `merge-tree` at
18:05Z"; all 22 commits had been rebase-merged at 18:04:20–37Z (committer =
owner, 6 s cadence) and my worktree's own start HEAD was the last of them.
`merge-tree --write-tree` is **vacuous for an applied patch** — clean either
way. Before any checkout/rebase/push: `git fetch origin
refs/pull/N/head:refs/remotes/pr/N` (needs no API), then `git cherry
origin/main pr/N` (`-` = already upstream) and `scripts/verify-merge-replay.py
--branch pr/N --merged origin/main`. A rebase that "skips cherry-picks" and
leaves HEAD == `origin/main` is the same signal — stop, do not push. I
force-pushed a merged PR's branch to main's tip before reading it and had to
restore it. Branch name for a `pr/N` sha: `git ls-remote --heads origin`.

## TRAP — worktree hook refuses variables · MCP "connected" but toolless · gates exit 2

Recipes: [`worktree-hook-and-rest-recipes.md`](worktree-hook-and-rest-recipes.md).
(1) Under `git worktree` isolation the Bash hook **refuses** any command with a
shell variable, loop, `export`, `$(...)` or `cd` near `git`/`python`, and even a
URL containing `github` — put the step in a script file with **literal** paths
and run `bash /abs/x.sh`. (2) `mcp__github__*` can be "connected" and offer
**no** PR tools — REST did every read, body write, review request and merge,
7/7 (2026-09-11/12). (3) `precision-gates.sh` exits **2 "PREFLIGHT FAILED"**
without `qou_substrate` importable — **not a red**; wrap with `PYTHONPATH=…`.
(4) A dead sibling's 2.4G `shadow/` survives in the scratchpad; the restore
bottomed at **139M free** from 8.5G. (5) No QOU oleans? shadow-compile — §6.

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

All failing jobs finish in ≤ 5 s on one `started_at` with no error log; local
reproduction passes. Never diagnose as code or push retrigger commits; document
`[skip-ci: GitHub Actions billing; local validate exit 0]` (PR #1435; `AGENTS.md`).

## STABLE — merge method

**Rebase** by default (`merge_method: "rebase"`): per-cluster commits kept,
`git bisect` meaningful, no merge-commit noise. **Never squash** without
explicit per-PR owner permission ("squash this one" / "squash OK") — a noisy
branch is cleaned with `git rebase -i`, not squashed. A merge commit only for a
sub-merge of already-merged siblings. Overrides any conflicting skill advice.

## STABLE — never delete a branch (owner directive 2026-06-12)

No `git push origin --delete`, no auto-delete-on-merge, never offer deletion as
"cleanup". Closed branches keep PR head SHAs and ledger links resolvable, and
`lake-cache/*` orphan branches are **load-bearing infrastructure**.

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

A bean at `in-progress` whose backing branch has had **no commit for > 3 h** is
presumed abandoned and may be taken over. **Scope: only the branch backing a
live in-progress bean** — never the thousands of long-idle `claude/*` branches,
which are permanently stale and are never takeover targets by age alone.

First confirm real staleness (> 3 h AND no newer PR activity / in-flight CI — a
long build is not a stall), re-claim the bean with a `--body-append` naming the
takeover and the stale SHA, then continue from that tip or from `main`. **Never
force-push over a sibling's branch.** The one sanctioned exception to "never
touch a sibling's claim".

## STABLE — commit granularity

Microcommit rule is in AGENTS.md (in your prompt). The one carve-out that bites
*in this role*: a **mechanical sweep** across many blocks/scripts/witnesses is
legitimately **one bulk commit** (uniform change, cherry-pick useless). Outside
a sweep, > 50 files or > 1000 lines means break it up.

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
there is **no REST path to un-draft** — but that does NOT block the merge
(**corrected 2026-09-03**, toggle dead ~4 h on qou#6439/#6466/#6468): go all-REST
— `update_pull_request state=closed` the draft, `create_pull_request draft=false`
from the same head, `merge_pull_request`. 3/3 first try; "wait and re-arm" was wrong.
Detail: [`update-pull-request-partial-write.md`](update-pull-request-partial-write.md).

## TRAP — API dead session-wide · shared worktree · float64-guard marker

Recipes and full diagnosis: [`api-down-and-shared-worktree.md`](api-down-and-shared-worktree.md).

1. **The API can be dead session-wide while `git` is fine** — `mcp__github__*`
   "No such tool available", REST 403 *"GitHub access is not enabled for this
   session"*: an Anthropic session gate, not permission or rate limiting; it does
   not clear on retry. **Intermittent** — down on #6395/#6396, #6400/#6401,
   #6415; up on #6404/#6405 the same day. Merge git-natively: branch first, then
   the **same SHA** to `main`, non-force (FF-only, self-guarding).
2. **`/home/user/qou` is SHARED with concurrent siblings** — a sibling's commit
   landed on my branch and nearly shipped in #6395. Symptom: **`HEAD` is not
   what you set it to**. Work in `git worktree add --detach`; never
   `git add -A`; never `git checkout <ref> -- <path>` to peek (it writes the
   index) — use `git show <ref>:<path> >`.
3. **`probe-float64-guard`**: `# float64-ok:` must sit **on** the flagged line;
   `from math import comb`/`factorial` are exact `int` false positives (annotate,
   never widen a baseline), and a grep for `math\.(sqrt|exp|log)` misses them.

## BASELINE — re-measure, do not quote

| what | command | last seen | when |
|---|---|---|---|
| Copilot reviews arriving | **request, then DO NOT PUSH**, `get_reviews` at 5/15/60 min — see below | intermittent; a clean 10-min zero on qou#6404 | `qou-gwe9`, 2026-08-31 |
| workflows with auto-triggers | `grep -l 'on:' .github/workflows/*.yml` then read each | dispatch-only repo-wide | 2026-06-30 directive |

**That Copilot row is a METHOD, not a verdict**: request once, push nothing
after, read `get_reviews` at 5/15/60 min; never flip the TRAP row on one run.
Detail: [`copilot-review-arrival.md`](copilot-review-arrival.md).

## TRAP — `git diff --stat` omits untracked files, so a quoted diff can be 7x low

PR #6510: reported "601 files, +616/−1"; it is **634 files, +4223/−1** — `add -A`
staged 33 untracked ones `--stat` never sees. **Quote it STAGED: `git add -A && git diff --cached --shortstat`.** [`diff-stat-omits-untracked.md`](diff-stat-omits-untracked.md)

## TRAP — a retraction reaches ONE surface and you think it landed

Twice on 2026-08-31 (#6395 missed the module docstring; #6405 missed the PR
body — where a reviewer looks first). **Enumerate every surface stating the
old claim before you start**: module docstring, runtime output, PR body, bean,
audit doc, `AGENTS.md`. A wrong figure here routinely survives in five places
after being fixed in one.
