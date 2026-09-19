# Merging when the GitHub API is dead, in a shared working tree

Detail for three `MEMORY.md` TRAPs. Established 2026-08-31 merging `qou#6395`
and `qou#6396`; re-verify cheaply if surprising.

---

## 1. The GitHub API can be dead session-wide while `git` still works

**Symptom.** Every `mcp__github__*` tool returns *"No such tool available"*,
`gh` is not installed, and the REST API through the proxy returns **403**:

```
{"message":"GitHub access is not enabled for this session. An org admin must
connect the Claude GitHub App for this organization.",
 "documentation_url":"https://docs.anthropic.com/en/docs/claude-code/github-actions"}
```

**What it is.** An Anthropic-side *session* gate. It is **not** a repo
permission problem, **not** the `update_pull_request` partial-write trap, and
**not** rate limiting — so it does **not** clear on retry. Do not spend the
window polling.

**STANDING CONDITION, not an incident (3 sessions).** Measured identically on
#6395/#6396 and #6400/#6401 (both 2026-08-31), and again on **#6415
(2026-09-03)**. Every time, all `mcp__github__*` tools reported *"No such tool
available"* and REST returned the 403 above. **Assume the API is unavailable
when dispatched as a sub-agent here** and plan the merge git-natively from the
start rather than discovering it midway.

**Do NOT conflate an absent API with the Copilot quota (added 2026-09-03).**
`copilot-review-arrival.md` records that review requests are quota-rationed and
that a quota refusal returns a *message* — *"reached their quota limit"* — which
you can quote in the PR. That is a request that **was transmitted and refused**.
The session gate is the opposite: there is no reviewer channel at all, so the
request is **never transmitted**. The two look similar in a report and are not:

| | quota | session gate |
|---|---|---|
| request reaches GitHub | yes | **no** |
| evidence you hold | a refusal message | a 403 / absent tool |
| honest report | "requested; quota-refused" | "**not requested** — API unavailable" |

On #6415 the dispatching instructions anticipated the quota case and asked for
the quota message to be recorded. The correct answer was neither: writing
"quota" there would have invented a transmission that never happened. When Step
6 cannot run at all, say so and hand the review request to the parent.

The practical consequence is narrow and worth stating so it is not
over-read: **`git` over HTTPS works fine**, so merges, pushes and rebases all
succeed. What is lost is exactly the GitHub-object writes — **PR comments,
review requests, and reading PR state**. Report the missing comment as an
unfulfilled instruction rather than skipping it silently; the *parent* session
generally does have API access and can post it, so hand it the verification text
in the final report. That is what happened both times, and both times the
comments were posted afterwards from the parent.

**Discriminator.** `curl -i -H "Authorization: Bearer $GITHUB_TOKEN" \
https://api.github.com/repos/litlfred/qou/pulls/<n>`. A 403 carrying that exact
body is the session gate. (Rate limiting says *"API rate limit already
exceeded"*; a draft PR blocking merge says `405 Pull Request is still a draft`.)

**What still works.** `git` over HTTPS — a separate credential path, with
`GH_TOKEN`/`GITHUB_TOKEN` set and `GIT_CONFIG_*` injected. Confirmed working:
`ls-remote`, `fetch`, `push`, force-push, push to `main`.

**What does not.** PR bodies and comments, review requests,
`subscribe_pr_activity`, PR-state reads, merge via API. The repo's post-push
hook requires `list_pull_requests` + `subscribe_pr_activity`; it **cannot** be
satisfied and the failure is environmental. Say so in the report rather than
retrying.

### Merging with git alone

`merge_method: "rebase"` *is* "rebase the branch onto base, then fast-forward
base", so it reproduces exactly:

```sh
git fetch origin main <branch>
git rebase origin/main                       # skip if already 0 behind
# ... verification here ...
git push --force-with-lease=refs/heads/<branch>:<old-sha> \
         origin HEAD:refs/heads/<branch>     # branch FIRST
git fetch origin main
git merge-base --is-ancestor FETCH_HEAD HEAD # PROVE fast-forward before pushing
git push origin HEAD:refs/heads/main         # the merge
```

**Before any of this, verify the merge is actually clean — and not with the
check everyone reaches for.** `git merge-tree <base> <ours> <theirs> |
grep -c '^<<<<<<<'` **MEASURES NOTHING**: the old three-argument form emits no
line-start conflict markers, so that grep returns 0 whether or not the merge
conflicts. Use

```sh
git merge-tree --write-tree HEAD origin/main   # read the EXIT CODE: 0 clean
```

The API is a second false comfort: `mergeable_state: clean` can be computed
against a stale base (16 commits back, in the recorded case), and `unknown`
only means GitHub is recomputing — neither is evidence either way. Established
by the `qou-4dq1` / `qou-0hu2` arc, which reported a branch conflict-free twice
before catching it, with a real conflict hiding behind both signals. Added here
2026-09-04 from `qou-phir`, where it lived only in beans and I ran the useless
form myself before the sibling's own commit message caught it.

Two properties make this safe and faithful:

- **Push the branch first, then the *same SHA* to `main`.** The PR head SHA
  becomes reachable from base, so GitHub marks the PR **merged** rather than
  leaving it open. Pushing a *different* (e.g. locally re-rebased) SHA to main
  can leave the PR open forever.
- **A plain, non-force push to `main` is FF-only.** It is *rejected* rather than
  clobbering if `main` moved under you. Never add `--force` to the main push.

From a detached worktree you have no local branch, so push by refspec
(`HEAD:refs/heads/<branch>`) — this is also what lets you operate on a branch
that is checked out in the shared tree.

---

## 2. `/home/user/qou` is SHARED with concurrent sibling sessions

**The incident.** A sibling session was working on
`claude/gg-rank-is-z-not-basis-2026-08-31`. I ran `git checkout` to another
branch *in the same tree*. Their next `git commit` landed on **my** branch —
`ab38cdbf58`, a 265-line unrelated `qou-brng` probe, committed onto
`claude/kms-length-dynamics-...`. Pushing without looking would have shipped it
inside PR #6395.

**Symptom.** *`HEAD` is not what you set it to.* `git log --oneline -1`
immediately after checkout showed the expected SHA; minutes later
`git rev-parse HEAD` returned a different commit. The giveaway I actually
noticed first was subtler: a file reported by `git ls-files` as tracked and
present in `HEAD`, but absent from all three origin refs.

**The isolation works — verified 2026-08-31 on the very next dispatch.** With
`git worktree --detach` taken as the FIRST action, #6400/#6401 merged while a
sibling session worked concurrently in `/home/user/qou`, and neither touched the
other. This is a solved problem *provided the worktree is created before any
checkout*. Remove it when done: it costs ~1.2 G and this container has run to
92 K free.

**RESIDUAL, and it will look alarming to the sibling.** Isolation stops commits
crossing over, but a **rebase + force-push still moves `origin/<branch>` under a
sibling whose local ref points at the pre-rebase commit**. Their HEAD follows
`origin` on the next fetch; their *local branch ref* does not. So their
stop-hook / `git status` reports **"N unpushed commits"** on a branch where
nothing is unpushed — and if they act on that report by pushing, they force the
branch *backwards* over the rebase.

Say so explicitly in the hand-off report: name the pre-rebase SHA, the
post-rebase SHA, and that the fix is `git branch -f <branch> <new-sha>` — and do
**not** run it yourself, because writing to the shared tree is what caused the
incident above. Verified harmless both times: the rebased blob SHA was identical
and the old commit stayed in the sibling's reflog.

**Diagnosis.** `git reflog` — interleaved `checkout:` entries you did not make.
It names both sessions' movements in order.

**Prevention — work in an isolated worktree:**

```sh
git worktree add --detach "$SCRATCH/wt" <sha>
```

Detached because git refuses to check out a branch already checked out in
another worktree. Costs one full 46k-file checkout (~30 s), and it buys total
isolation from the sibling.

**Corollaries.**

- **Never `git add -A`.** You will sweep a sibling's in-flight file, and the
  tree-measuring audit witnesses (`witness-raw-float64-audit`,
  `q0-anchor-consistency-audit`, `never-raises-dps-audit`,
  `witness-provenance-audit`, `witness-float64-padding-audit`,
  `q0-value-drift-audit`, `mpf-float-source-audit` — bean `qou-v0t8`). Stage by
  explicit path and check `git diff --cached --name-only` before every commit.
- **Never `git checkout <ref> -- <path>`** to peek at another branch's file: it
  writes the working tree **and the index**, leaving a staged add you may not
  notice. Use `git show <ref>:<path> > "$SCRATCH/f"`. (I did this and had to
  back it out.)
- **Hand the shared tree back clean.** Save your edit with `git diff > patch`,
  `git checkout -- <path>` **by name**, then re-apply in the worktree.
- **Re-check `ls-remote` before "rescuing" anything.** In this incident the
  sibling pushed their own commit to their own branch unaided; a rescue branch
  would have been pure noise.

---

## 3. `probe-float64-guard` — marker placement and a real false-positive class

`scripts/probe-float64-guard.py --diff <paths>` is the cheap targeted gate for
probes; the full `scripts/precision-gates.sh` family measured ~3 min, this is
seconds. Use it on any `computations/` probe you are about to merge.

- **The `# float64-ok: <reason>` marker must sit ON the flagged line.**
  `ALLOW_MARKER` is matched per-line. A comment block *above* the import does
  not clear the hit — it only shifts the reported line numbers, which reads like
  the guard ignoring you. (Cost me one round trip.)
- **`from math import comb` / `factorial` flag as `[float64-module]` but return
  exact arbitrary-precision `int`.** Genuine false positive; the per-line marker
  is the sanctioned resolution. **Verify before annotating** — check
  `type(...) is int` and cross-check against a pure-integer implementation —
  and never widen a baseline instead (AGENTS.md forbids it; baselines drain,
  never grow).
- **It refuses to vouch for paths absent from the current worktree**, printing
  *"nothing was scanned for them, so this run proves nothing about"*. Honest and
  worth respecting: checking PR B's files from PR A's tree proves nothing.
- **A hand grep is not a substitute.** `math\.(sqrt|exp|log|pi)` misses
  `from math import ...` entirely — my own pre-scan was clean while the guard
  was red.

### Note on `precision-gates.sh --changed`

Reported red on clean unmodified `main` (`MAIN_EXIT=1`, pre-existing
`PROV_MISSING` witnesses, completeness 0.964) — i.e. it is **not** a signal
about your branch. Do not widen or edit a baseline to green it. Confirm main
alone is also red before treating any red as yours. Running the full family also
**dirties the tree-measuring audit witnesses** listed above; revert them by
name, never with a blanket `git checkout -- computations/`.

## Second instance, 2026-09-13 — and the concurrent writer was MY OWN SUB-AGENT

The shared-worktree TRAP is confirmed a second time, by a different mechanism
that is worth naming because it defeats the obvious assumption.

The first instance (#6395) was a **sibling session**. This one was an agent
**dispatched from the session it collided with** — `Agent(...)` on the
`qou-cds1` / #6233 adjudication, launched from the session then building
`qou-0fmb` step 1. A dispatched sub-agent runs in **the same clone**, so it can
`git commit` onto the parent's checked-out branch. Its own PR body (#7276)
records the collision verbatim: *"A concurrent session shares this clone and
moved `HEAD` mid-task, so the first commit landed on
`claude/markovtrace-colimit-bridge-2026-09-13`."*

**Do not assume a sub-agent you dispatched is isolated.** It is not, unless it
creates a worktree — which this one did, on its own initiative, after noticing.

**No damage, and the reason is worth keeping.** The agent never pushed the
stray commit, reset to the branch's *pushed* tip, and left the parent's
untracked file alone. The parent verified afterwards rather than assuming:
local `HEAD` = remote tip = `04c43df680`, the step-1 commit reachable from the
remote, the file present and committed, the working tree clean, and the file
re-compiled `exit 0`. **Run that check rather than trusting the report** — the
agent's note said it reset the branch to `cbd6804843`, which if read carelessly
sounds like the parent's later push was lost; it was not, because the reset
predated it.

**Practical rule for the parent.** After any dispatched agent reports touching
git, verify four things before continuing: `git rev-parse HEAD` against the
remote tip, your last commit reachable from the remote, `git status` clean, and
your changed files still compiling. All four are cheap; the failure they catch
is not.


## The CCR routes have outage windows — and a 503 there says nothing about REST

Measured on `qou#7393`, 2026-09-14. `POST …/ccr/ready_for_review` returned
**`503 {"message":"GitHub is temporarily unavailable. Retry shortly."}`** on
seven attempts spanning **19:15Z → 20:36Z (81 min)**, then `200 {"draft":false}`.

Throughout that window **ordinary REST was fine** — `GET /pulls/7393`,
`create_pull_request`, `update_pull_request` on title/body, and every `git push`
all succeeded. So a 503 on a CCR route is a statement about the **CCR family
only**; do not read it as the API being down, and do not escalate it.

**The two failure modes take OPPOSITE responses and the status code is the
discriminator:**

| code | route | meaning | response |
|---|---|---|---|
| `503` | `ccr/*` | transient outage, **clears** | retry spaced, off a check-in |
| `403` | GraphQL | session-wide block, **never clears** | do not retry; read the body for the CCR replacement |

AGENTS.md §8a records the window as "≥ 15 min" from one incident (#7350, ~70 min).
This is the second data point and it is **81 min**, so budget an hour-plus and
arm a check-in rather than blocking on it. `mcp__github__update_pull_request`
with `draft:false` is the 403 path and must not be retried at all.

**What it never justifies:** close-and-reopen (owner ruling 2026-09-05). Waiting
out an 81-minute window costs nothing; a replacement PR strands the review
threads, the Copilot request, and every commit/bean/ledger reference to the old
number.


## CCR `review_threads` 503 window, measured on qou#7395 (moved from MEMORY.md 2026-09-15 to keep it under the cap)

AGENTS.md §8a classifies a `503` from a `ccr/*` route as transient ("retry spaced;
measured windows of ≥ 15 min") and only a GraphQL `403` as a hard block. That
classification held, and the window is longer than the rule implies.

Measured on qou#7395, `GET /repos/litlfred/qou/pulls/7395/ccr/review_threads`:

| when | result |
|---|---|
| 2026-09-14 18:59Z | `503` "GitHub is temporarily unavailable" |
| 2026-09-14 20:02Z | `503`, same body |
| 2026-09-14 21:03Z | **`200`**, body `[]` |

~2 h from first 503 to success, with a failure at the 1 h mark. Meanwhile
`pull_request_read get_review_comments` returned *"API rate limit already exceeded
for user ID 662242"* throughout — the GraphQL-family block, which never clears.

**So do not conclude "review threads are unreadable" from two 503s an hour apart**,
and do not treat an unread thread list as an empty one: say it is unmeasured and
retry on the next check-in. A `200 []` is the only thing that establishes zero.
