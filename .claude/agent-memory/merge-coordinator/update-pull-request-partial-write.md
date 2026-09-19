# `update_pull_request` partial writes — the full case

Referenced from `MEMORY.md`. Measured on `litlfred/qou#6264`, 2026-08-31.

> **🛑 READ THE LAST SECTION FIRST — the diagnosis in §1-§3 below is WRONG and
> both of its prescriptions are retracted (settled 2026-09-12, `qou#7230`).**
> The draft toggle is not rate-limited and there is no wait to sit out: GraphQL
> is **403-blocked outright** from Claude Code sessions, and the 403 body names a
> REST replacement that works first try —
> **`POST /repos/{owner}/{repo}/pulls/{n}/ccr/ready_for_review`**. Do not wait,
> and do not close-and-reopen (owner ruling 2026-09-05, AGENTS.md §8a). What
> survives from §1 is only this: send the flip **alone** and **re-read** before
> reporting failure. Full measurement: §`qou#7230` at the end of this file.

## TRAP — `update_pull_request` is a PARTIAL write, and its rate-limit error lies

Measured on `qou#6264`, 2026-08-31. A single `update_pull_request` carrying
`title`, `body` and `draft: false` returned:

    Failed to find pull request: API rate limit already exceeded for user ID 662242

and I reported the update as failed. **It was not.** A later read showed the
**title and body had landed**; only `draft` had not. The call is split across
two APIs — REST `PATCH /pulls/:n` for title/body, GraphQL
`markPullRequestReadyForReview` for the draft toggle — and the two carry
**separate rate-limit budgets**. GraphQL was exhausted; REST was fine.

Three consequences, in order of how much time each saves:

1. **A rate-limit error on this tool is not evidence nothing was written.**
   Re-READ the PR before re-sending or reporting a failure. I re-sent the whole
   body four times against a limit that was never blocking it.
2. **Reads and REST writes can be fine while the draft toggle is dead.** Do not
   generalise "rate limited" across the whole API. Discriminate cheaply:
   `merge_pull_request` is REST, so attempting it returns a **real** error —
   `405 Pull Request is still a draft` — which proves REST is live and isolates
   the blocker to GraphQL.
3. **There is no REST path to un-draft.** `draft` is read-only on REST PATCH, so
   a GraphQL outage blocks the merge outright. Wait and re-arm a check-in.
   Do NOT close-and-reopen (forbidden, and it does not un-draft anyway) and do
   NOT open a fresh non-draft PR from the same branch — that abandons the
   review history and violates the one-branch-one-PR rule.

## TRAP — the SAME REST/GraphQL split blocks READS, and it has a REST way round

Measured 2026-09-04 across `qou#6528`, `#6576`, `#6602`, `#6627`, `#6651`:
`pull_request_read` with `method: "get_review_comments"` returned
*"API rate limit already exceeded for user ID 662242"* on **every** attempt for
**~10 hours**, while REST methods on the same tool answered instantly
throughout. Same two-budget split as the write case above, one tool over.

**Which method is which** — this is the part that saves the time:

| method | API | during the outage |
|---|---|---|
| `get_review_comments` (review **threads**) | GraphQL | dead |
| `get` (merge state, head sha, counts) | REST | fine |
| `get_reviews` | REST | fine |
| `get_comments` (issue-level) | REST | fine |
| `get_files`, `get_commits`, `get_diff` | REST | fine |

**So a GraphQL outage does NOT stop you answering "are there open review
threads?"** A review thread cannot exist outside a review, so `get_reviews`
returning `[]` proves there are none; `get_comments` covers the issue-level
ones. Together they settle it without GraphQL.

**Cost of not knowing this:** I reported "review threads remain unread" across
four consecutive PRs, correctly but needlessly — the answer was one REST call
away each time. Worse, the principle was **already in this very file** (point 2
above, *"do not generalise 'rate limited' across the whole API"*) and I
re-derived it instead of reading it. In this environment `MEMORY.md` and its
siblings are **not injected** into the prompt (see AGENTS.md); nothing reads
them for you.

**Also note the duration.** ~10 hours is far longer than a normal GitHub
rate-limit window (1 h), so do not plan on it clearing within a session — take
the REST route rather than waiting.

### Amendment 2026-09-14 (`qou#7383`) — there IS a direct REST twin, and the CCR route was 503 while it worked

Two things the table above does not say, measured in one check-in.

**1. `get_review_comments` has a plain-REST twin and it is not `ccr/`.** The
row marks it "dead" with no replacement, so the entry recommends *inferring*
the answer from `get_reviews == []`. The underlying endpoint answers directly:

```sh
curl -H "Authorization: Bearer $GITHUB_TOKEN" -H "Accept: application/vnd.github+json" \
  "https://api.github.com/repos/litlfred/qou/pulls/<n>/comments?per_page=100"
# -> HTTP 200, a JSON array of the line-level review comments
```

Measured on `#7383` at 19:56Z: `get_review_comments` → the usual
*"API rate limit already exceeded for user ID 662242"*; the curl above →
**HTTP 200, `[]`**. Same PR, same minute. The inference from `get_reviews` is
sound and stays the cheap first move; this is what to run when you want the
comments themselves rather than a proof of their absence.

**2. The `ccr/` route is NOT the fallback to reach for first — it has its own
outages.** `GET /repos/litlfred/qou/pulls/7383/ccr/review_threads` returned
**503** *"GitHub is temporarily unavailable. Retry shortly."* in the same
minute that plain REST returned 200. That is a second, independent instance of
the CCR-family outage window AGENTS.md §8a records from `#7350` earlier the
same day, and it sharpens the ordering: **plain REST first, `ccr/` only for
what plain REST genuinely cannot do** (the draft flip, thread resolve).

**And I re-derived this file's own lesson again.** I ran `get_reviews` → `[]`
in this check-in — the proof the TRAP above says is sufficient — and still
reported to the user that the thread state was unknown, then went hunting for
two more routes. That is the identical failure the TRAP was written to stop,
now at its second recorded occurrence. Read the file.

---

Related in kind to the CI-billing rule in AGENTS.md: an infrastructure error
whose surface message names the wrong cause. The tell here is the same one that
caught the ledger `source_hash` bug earlier in the same session — **the count
did not move**, so check whether the write landed before assuming it did not.


---

## `qou#6444` 2026-09-03 — corroboration, and two things still worth knowing

Same signature as above: `merge_pull_request` returned `405 Pull Request is still
a draft` while every `update_pull_request draft:false` returned *"API rate limit
already exceeded for user ID 662242"*. The `MEMORY.md` discriminator isolated the
blocker to GraphQL first try.

**My own recommendation here was WRONG, and the all-REST fix in `MEMORY.md`
supersedes it.** I wrote "the wait can be HOURS, so re-arm and wait"; the sibling
correction landed the same day (`ec96d89b1a`, from `qou#6439`/`#6466`/`#6468`)
and is right: **close the draft, re-create it with `draft=false` from the same
head, merge — all REST, 3/3 first try.** Do that instead of waiting.

Two notes that survive the correction:

**1. It really is ~4 h, measured independently.** 04:22Z -> 09:37Z on `#6444`,
>=7 attempts, clearing only at the end; the sibling measured ~4 h across three
other PRs the same day. Two independent measurements, same window, so the outage
is real and wide rather than one session's bad luck. That is why the all-REST
route matters — it is not a reason to wait it out.

**2. `create_pull_request` fails while the draft is still OPEN.** I tried the
re-create step *without* closing first, got *"A pull request already exists for
litlfred:<branch>"*, and wrongly concluded the whole route was closed. The close
is not bookkeeping — it is what frees the head. Skip it and you reproduce my dead
end and may write off a working fix.

**3. The git-native fallback in `api-down-and-shared-worktree.md` §"Merging with
git alone" is NOT always available.** Under Claude Code **auto mode** the
classifier denied `git push origin HEAD:refs/heads/main`, then denied even a bare
`git rebase origin/main`. That recipe is the other documented escape hatch, so an
agent will reach for it and find it closed; it needs an explicit Bash permission
rule from the author. Do not route around the denial.

**Corroborated from that recipe:** the FF proof
(`git merge-base --is-ancestor FETCH_HEAD HEAD`) is load-bearing, not ceremony.
`main` lands ~100 commits/hour here and it fired correctly — `main` moved during
the ~40 s Lean verification window between the branch push and the base push, and
the guard refused. Expect to lose that race repeatedly.

**And resolving a conflict with a merge commit costs you the rebase-merge.**
`merge_pull_request merge_method:"rebase"` then returns `405 This branch can't be
rebased`. On a branch you own, linearise with `git rebase origin/main` instead —
but note the rebase replays your ORIGINAL commit, so any fix you made while
resolving the earlier merge is silently dropped. Re-apply it and verify the file
after `--continue`; I lost this exact correction that way and nearly shipped text
contradicting the corrected `MEMORY.md` one file over.

---

## `qou#6433` 2026-09-03 — a THIRD measurement, and the datum that makes the all-REST route work

Same signature again, independently: `merge_pull_request` → `405 Pull Request is
still a draft`; every `update_pull_request draft:false` → *"API rate limit
already exceeded for user ID 662242"*. ~7 attempts across three turns.

**Window ≈ 2 h, not 4** — first refusal ~07:0xZ, cleared ~09:06Z on
`2026-09-03`. So across three sessions the outage is real and wide but its
LENGTH varies (≈2 h here, ≈4 h on `#6444` and on the sibling's three PRs).
**Do not quote a duration and wait it out** — that is what the all-REST route in
`MEMORY.md` exists to avoid, and it was not yet written when this happened
(it landed 12:38Z, after this PR cleared on its own).

**The observation that CORROBORATES the all-REST fix from the other side:**
during the outage I ran `update_pull_request` with `title` **and** `body` and it
**succeeded**, twice, in the same windows where `draft:false` was refused — and
`merge_pull_request` returned a real `405`, not a rate-limit. So REST reads
*and writes* and the merge endpoint were all healthy throughout; only the
GraphQL mutation was gated. That is the direct evidence that a route composed
entirely of REST calls will go through, rather than an inference from the
`MEMORY.md` discriminator.

**Also: `get_reviews` and `get_review_comments` are GraphQL** and were refused
in the same windows, while `get_status` and `get_check_runs` (REST) answered.
An empty review list obtained during the outage is therefore **not** evidence
that no review exists — re-check after it clears before concluding anything
about Copilot.

---

## `qou#7230` 2026-09-12 — SETTLED: it was never a rate limit, and one REST call fixes it

Everything above diagnosed a **rate-limited GraphQL budget** and prescribed either
waiting (~2-4 h, measured three times) or the all-REST close-and-recreate route.
**Both prescriptions are now retracted, and for the same reason: the premise was
wrong.** GraphQL is not rationed from here — it is **blocked outright**.

### What is actually happening

Three calls, one PR, one minute apart:

| call | result |
|---|---|
| `PATCH /pulls/7230` `{"draft": false}` | **200** — and the re-read says `draft: true`. REST accepts the field and **silently discards it**, no error, no warning. |
| `POST /graphql` `markPullRequestReadyForReview` (with the node_id already in hand, so **no** node lookup) | **403** — *"GitHub GraphQL is not available from Claude Code sessions; use the REST API … For review threads, auto-merge, and draft/ready-for-review use the CCR routes on api.github.com"* |
| `POST /pulls/7230/ccr/ready_for_review` | **200 `{"draft": false}`** — first try, no retry, no wait. |

So the *"API rate limit already exceeded for user ID 662242"* surfaced by the MCP
tool is a **misleading skin over a hard block**. That explains the one thing the
three earlier measurements could not: why the "limit" lasted 2 h on one PR and 4 h
on another with no consistent window. It was not a limiter draining — it was a
block, and the PRs that "cleared" cleared for some other reason.

Note the node-ID detail, because it kills the leading hypothesis: AGENTS.md §8a
attributes the failure to the **node-ID lookup** being rate-limited. The 403 above
was obtained *supplying* the node_id from a prior REST read, i.e. with the lookup
skipped entirely. The lookup is not the problem; the transport is.

### The routes, from the 403 body itself

    GET  /repos/{owner}/{repo}/pulls/{n}/ccr/review_threads
    POST /repos/{owner}/{repo}/pulls/{n}/ccr/comments/{comment_id}/resolve   (or /unresolve)
    PUT  /repos/{owner}/{repo}/pulls/{n}/ccr/auto_merge                      (or DELETE)
    POST /repos/{owner}/{repo}/pulls/{n}/ccr/ready_for_review
    POST /repos/{owner}/{repo}/pulls/{n}/ccr/convert_to_draft

`ccr/review_threads` is worth as much as the draft flip: the *"review threads are
GraphQL, therefore unreadable during an outage"* problem this file spends a whole
section routing around has a direct REST answer too.

**The generalisable habit: read the body of a 403 before believing its status
line.** This one contains its own fix, in full, and had been discarded unread
across at least five sessions — the cost was three multi-hour waits, one
close-and-recreate that destroyed a PR's review history, and a memory entry that
told the next agent to do it again.

### Still true from the sections above

- Send the flip **alone** and **re-READ** before reporting failure — the partial
  write on `qou#6264` (title and body landed, `draft` did not) is real and the
  CCR route does not change it.
- **Never close-and-reopen** — now on an owner ruling (2026-09-05, AGENTS.md §8a)
  as well as on the review-history argument.
