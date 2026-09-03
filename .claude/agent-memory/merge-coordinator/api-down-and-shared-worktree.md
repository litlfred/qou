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
