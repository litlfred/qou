# Agent-ops traps: GitHub and git

Three TRAP entries moved here from their beans (bean drain wave 1, 2026-11-21) so
that the agent reading this directory finds them without grepping the beans
branch. Each one cost a turn or more when it was first met. Each entry names the
bean that holds the full measurement.

## TRAP — a behind-count on a shallow clone is not a main-advance count (`qou-lww5`)

Measured 2026-09-08. A branch cut from `origin/main` at 03:20 reported, 112
minutes later, "Origin/main is ahead by: 37121 commit(s)". That is months of
history, not a 112-minute advance. It looks like a force-push or a history
rewrite on `main`. It is neither. Agent clones here are shallow, and as each
`git fetch` deepens the history, `git rev-list --left-right --count
origin/main...HEAD` starts counting every merged side-branch commit it can newly
reach.

Tell the two cases apart before reacting, in seconds:

```sh
git merge-base --is-ancestor $(git rev-parse HEAD^) origin/main   # succeeds => no rewrite
[ -f .git/shallow ] && wc -l < .git/shallow                       # shallow, and how many cut points
git rev-list --count --first-parent BASE..origin/main             # the advance you actually wanted
```

`scripts/session-start-coord-sweep.sh` prints the raw figure at session start, so
this is the first number many agents read. Do not rebase in a panic or report a
rewrite on the strength of it. Changing what the sweep prints is not done here;
it is a script change and stays in `qou-lww5`.

## TRAP — the merge endpoint 500s every time on a rebase-merge of a branch that carries merge commits (`qou-md01`)

Measured 2026-09-13 on #7255. `merge_pull_request` with `merge_method: "rebase"`
returned `500 []` twice, about 15 minutes apart, on a PR that was otherwise
`mergeable_state: "clean"`. After each attempt, `git merge-base --is-ancestor
HEAD origin/main` was false, so nothing landed. The branch carried 6 merge-ups
of `origin/main` in 20 commits, and GitHub's rebase-merge cannot replay a merge
commit.

This is not the retryable 5xx of `qou-4w5b` (PR create or update with a long
body, which is intermittent and clears with a shorter body). Tell them apart by
reproducibility: this one is identical on every try, so a verbatim retry only
burns calls. The response is to change the history or the method:

- linearise the branch (`git rebase origin/main` dropped the 6 merge-ups with
  zero conflicts there, and the tree was byte-identical to the merge result),
  then rebase-merge; or
- use `merge_method: "merge"` and say so in the PR, as the 405 entry in
  `MEMORY.md` already advises.

Both still need the owner's merge permission. Neither is a squash.

## TRAP — GitHub strips bare `<angle-bracket>` placeholders from comment bodies (`qou-gaoa`)

Observed on #5419: a comment posted with `json.load(open("<main's version after
#5367>"))` inside a ```python fence was stored as `json.load(open(""))`. The
placeholder was gone from the stored body (read back through the API), so it was
removed before storage, and the code fence did not protect it. Backticked inline
spans did survive.

So in any text that becomes a GitHub comment, issue or PR body, write
placeholders as `#NNN`, `{one sentence}` or `COMMIT-SHA`, never `<...>`.
`local/coordinate`'s posted templates were converted to that form; the last bare
pair, in the §4 triage-report header, was converted with this note. Placeholders
in commands an agent runs itself (`gh pr view <N>`) are never posted and do not
need changing.

One observation and a plausible mechanism (HTML-tag sanitising on the raw body);
recorded as a trap, not as a measured rule about every endpoint.
