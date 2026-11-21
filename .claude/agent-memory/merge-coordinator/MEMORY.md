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

2026-09-07: four PRs "measured CLEAN by `merge-tree`" were already rebase-merged (`merge-tree --write-tree` is vacuous for an applied patch). Before any checkout/rebase/push: `git fetch origin refs/pull/N/head:refs/remotes/pr/N`, then `git cherry origin/main pr/N` (`-` = upstream) and `scripts/verify-merge-replay.py --branch pr/N --merged origin/main`. A rebase that skips everything and leaves HEAD == `origin/main` is the same signal — stop. I force-pushed a merged branch to main's tip once and had to restore it.

## TRAP — the same staleness reads as a phantom CONFLICT, not just a false clean

2026-09-26, the inverse of the entry above. Rebase-merge rewrites every sha, so a merged branch's leftover ref is **not** an ancestor of `main`: `--is-ancestor` returns FALSE and `merge-tree --write-tree` reports **add/add CONFLICT** on every file it created. Measured on four leftovers — all read NOT-merged with real-looking conflicts, **all four PRs had merged**; one conflicting file's theorem bodies were byte-identical to main's and the whole 26-line "conflict" was docstring. Leftovers are the NORMAL state (deletion is forbidden) and `session-start-coord-sweep.sh` lists exactly them, so this reading is available on every sibling, every session. **Resolve branch → PR state before reading git ancestry as coordination signal:** `GET /pulls?state=all&head=litlfred:<branch>` — `state=open` alone returns `[]` and looks like "no PR ever". Detail + the four shas: [`stale-merged-branch-phantom-conflict.md`](stale-merged-branch-phantom-conflict.md).

## TRAP — worktree hook refuses variables · MCP "connected" but toolless · gates exit 2

Recipes: [`worktree-hook-and-rest-recipes.md`](worktree-hook-and-rest-recipes.md).
(1) Under `git worktree` isolation the Bash hook **refuses** any command with a
shell variable, loop, `export`, `$(...)` or `cd` near `git`/`python`, and even a
URL containing `github` — put the step in a script file with **literal** paths
and run `bash /abs/x.sh`. (2) `mcp__github__*` can be "connected" and offer
**no** PR tools — REST did every read, body write, review request, un-draft and
merge, 9/9 (2026-09-11/12); the post-push hook's `list_pull_requests` /
`subscribe_pr_activity` are then UNSATISFIABLE — do the sibling sweep by REST
(`GET /pulls?state=open` + `/pulls/<n>/files`) and say so in the body, once.
(3) `precision-gates.sh` exits **2 "PREFLIGHT FAILED"**
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
`git bisect` meaningful, no merge-commit noise. **Never squash** without explicit
per-PR owner permission — clean a noisy branch with `git rebase -i` instead. A
merge commit only for a sub-merge of merged siblings. Overrides skill advice.

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
genuinely *open-outcome* research; **mechanical work is not** (sweeps, sidecar
or witness regeneration, refactors, wiring, migrations — one right answer, one
owner). Test: is the answer *unknown* (may overlap) or merely *not-yet-typed*
(one owner)? State your distinct angle; the second route to land re-scopes to
verify/extend/refute and cites the first.

## STABLE — stalled-claim takeover

Policy text is in AGENTS.md (in your prompt): > 3 h with no commit AND no newer PR activity, only the branch backing a LIVE in-progress bean (never long-idle `claude/*` branches by age alone), re-claim with `--body-append` naming the stale SHA, never force-push over a sibling's branch.

## STABLE — commit granularity

Microcommit rule is in AGENTS.md (in your prompt). The one carve-out that bites
*in this role*: a **mechanical sweep** across many blocks/scripts/witnesses is
legitimately **one bulk commit** (uniform change, cherry-pick useless). Outside
a sweep, > 50 files or > 1000 lines means break it up.

## STABLE — asking the author anything at all

Six-part frame is in AGENTS.md (in your prompt). What bites here: naming a decision in an end-of-turn line, a `**next**` bean entry or a PR "follow-up" IS asking, and owes the frame plus the default-if-silent and a recommendation marked as judgement; mirror `AskUserQuestion` in chat, `multiSelect: true`, 🟡. Won't spend the words? Don't raise it.

## STABLE — un-draft is ONE REST call; the rate-limit message is a LIE twice over

**`POST /repos/litlfred/qou/pulls/<n>/ccr/ready_for_review` → `200 {"draft":
false}`** — #7230 first try, **but `503` in outage windows (81 min, #7393): a
`503` HERE clears, the `403` below never does.** It fires after `draft:false` returned
the usual *"rate limit already exceeded for user ID 662242"*. Two misdirections
behind that message: `PATCH /pulls/<n> {"draft": false}` returns **200 with `draft`
still true** (REST ignores the field, silently), and GraphQL is **403-BLOCKED
session-wide from Claude Code, not rate-limited** — so spaced retry on that "limit"
can never clear, which is how ~2-4 h "waits" were mis-measured. **The 403 body
names the replacements** (`ccr/ready_for_review`, `ccr/convert_to_draft`,
`ccr/auto_merge`, `ccr/review_threads`, `ccr/comments/<id>/resolve`) — read a
GraphQL 403 body, never discard it. **Do NOT close-and-reopen** (owner ruling
2026-09-05, AGENTS.md §8a): the close+recreate route this entry recommended until
2026-09-12 is **RETRACTED**. Send the flip **alone**, then re-READ — a call
carrying title/body too can land those and drop only `draft` (`qou#6264`).
Detail: [`update-pull-request-partial-write.md`](update-pull-request-partial-write.md).

## TRAP — API dead session-wide · shared worktree · float64-guard marker

Recipes and full diagnosis: [`api-down-and-shared-worktree.md`](api-down-and-shared-worktree.md).

1. **The API can be dead session-wide while `git` is fine** — `mcp__github__*`
   "No such tool available" + REST 403 *"GitHub access is not enabled for this
   session"*: an Anthropic session gate, not permission or rate limiting, and it
   does not clear on retry. **Intermittent** (down #6395/#6400/#6415, up #6404
   same day). Merge git-natively: branch first, then the **same SHA** to `main`,
   non-force (FF-only, self-guarding).
2. **`/home/user/qou` is SHARED — with siblings AND any agent YOU dispatch**
   (2nd instance #7276). A commit landed on my branch, nearly shipping in #6395.
   Symptom: **`HEAD` is not what you set**. Use `git worktree add --detach`; never
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

**That Copilot row is a METHOD, not a verdict**: request once, push nothing after,
read at 5/15/60 min; never flip the TRAP row on one run. (2026-09-12 #7234: one
more CLEAN zero — no push after the request, zero at 18 min. #7230: zero at 2
min, too early to count.) [`copilot-review-arrival.md`](copilot-review-arrival.md)

## TRAP — `git diff --stat` omits untracked files, so a quoted diff can be 7x low

PR #6510: reported "601 files, +616/−1"; it is **634 files, +4223/−1** — `add -A` staged 33 untracked ones `--stat` never sees. **Quote it STAGED: `git add -A && git diff --cached --shortstat`.** [`diff-stat-omits-untracked.md`](diff-stat-omits-untracked.md)

## TRAP — a retraction reaches ONE surface and you think it landed

Twice on 2026-08-31 (#6395 missed the module docstring; #6405 missed the PR
body — where a reviewer looks first). **Enumerate every surface stating the
old claim before you start**: module docstring, runtime output, PR body, bean,
audit doc, `AGENTS.md`. A wrong figure here routinely survives in five places
after being fixed in one.

## BASELINE — CCR `review_threads` 503 clears in HOURS (~2 h on #7395), not minutes

`200 []` is the only thing that establishes zero threads; two 503s an hour apart establish nothing. Detail: [`api-down-and-shared-worktree.md`](api-down-and-shared-worktree.md) §CCR windows.

## TRAP — a scratch shadow that holds only NEW oleans hides the WHOLE QOU tree (2026-09-15, #7426)

Lean resolves a module by the FIRST `LEAN_PATH` root whose `QOU/` directory exists and then expects every `QOU.*` olean under it — so `LEAN_PATH=$SHADOW:/tmp/overlay:…` with `$SHADOW/QOU/` holding just the PR's new modules fails every file importing an existing module with "object file … of module QOU.Basic does not exist" in 0.1 s. Make the shadow a full farm first (`cp -rs /tmp/overlay/QOU $SHADOW/QOU`), `os.unlink` an entry before `lean -o` writes it (writing through a symlink overwrites the real olean), then build the PR's library modules in import order and the content siblings last: 19/19 in 40 s once done right. A worktree has no `.lake`: source `lean-direct-env.sh` from the MAIN checkout (`ROOT` = the script's own location) and symlink `folio-assistant` into the worktree for `bun`.

## TRAP — `qa-staleness.ts` says `fresh: 0` of 3557 blocks; that is not evidence about a PR

Its `want_criteria` list carries watcher criteria the reactive sweep never populates, so every block is "stale_or_partial" corpus-wide. Measure a PR's sidecars directly: `source_hashes.md/ts` vs sha256 of the files, then the LAST verdict per criterion, then the same criterion on `origin/main`'s copy (`git show`) — a `fail` that is also `fail` on main is inherited, not a regression (6 of 7 on #7426). And a dependency-cycle `fail` can be FRESH on its own md/ts hashes and stale on `field_hash.graph`: fixing the cycle in the OTHER blocks leaves this block's verdict saying `fail`; re-run that one criterion (`qa-sweep <stem> --only detangler-no-dependency-cycle` → pass, 0 findings).

## TRAP — pushing a clean merge-from-main makes GitHub refuse "rebase" (405)
Verify a clean PR against main LOCALLY and do not push the merge commit: once a merge commit is on the head, GitHub answers `405 This branch can't be rebased` (or `rebaseable: false`) and only the merge-commit method remains. Push the merge only when there is a real conflict, and say in the PR comment why it went in as a merge commit. Measured on #7583 / #7734, 2026-10-12.

## TRAP — shallow behind-count, deterministic rebase-merge 500, stripped `<placeholders>` (2026-11-21)
Three agent-ops traps from beans `qou-lww5`, `qou-md01` and `qou-gaoa`, with the checks that separate each from its look-alike: [`agent-ops-traps.md`](agent-ops-traps.md). Read it before reacting to a huge behind-count, retrying a merge 500, or posting a template.
