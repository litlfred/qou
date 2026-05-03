---
name: watch
description: Background-watch a branch (default origin/main) or a GitHub PR for new activity while you work, and on every event report whether to integrate / whether it conflicts with the current branch / whether it lets you simplify exposition / proofs / computations
roles: [reader, collaborator, owner]
user_invocable: true
---

# /watch — background watcher with integration check

A unified watcher that handles **branches** (poll `git ls-remote`) and
**pull requests** (subscribe via the GitHub MCP).  On every event,
walk the §3 integration checklist and either act, defer, or flag the
user.

## Invocation

The user's request maps to one of three modes; pick the right one
without asking:

| user phrase | mode | how |
|-------------|------|-----|
| "watch main" / "watch upstream" / no target | **branch:main** | poll `origin/main` every 5 min |
| "watch PR 516" / "watch the PR" / "watch this PR" | **pr:N** | `mcp__github__subscribe_pr_activity` (event-driven) |
| "watch branch foo/bar" / "watch claude/x-y" | **branch:foo/bar** | poll `origin/foo/bar` every 5 min |
| "watch foo/bar PR 42" | **pr:42** + maybe **branch** | subscribe + poll |

If ambiguous, default to **branch:main**.

## 1.  Stash the baseline

Before arming anything, record the current state so the §3 review
compares cleanly:

```bash
git fetch origin <BRANCH> 2>/dev/null
git rev-parse origin/<BRANCH> > /tmp/_watch_baseline_<BRANCH>.sha
```

For PR mode, instead capture the latest PR head SHA:

```python
mcp__github__pull_request_read(method="get", pullNumber=N, owner=..., repo=...)
# stash result["head"]["sha"]
```

## 2.  Arm the watcher

### Branch mode — Monitor with poll loop

Use the `Monitor` tool, `persistent: true`, 5-minute poll:

```
Monitor:
  description: "origin/<BRANCH> new commits"
  persistent: true
  command: |
    BRANCH="<BRANCH>"
    last=$(git ls-remote origin "$BRANCH" | cut -f1)
    while true; do
      cur=$(git ls-remote origin "$BRANCH" 2>/dev/null | cut -f1)
      if [ -n "$cur" ] && [ "$cur" != "$last" ]; then
        git fetch origin "$BRANCH" 2>/dev/null
        # one line per new commit, oldest first
        git log --reverse --oneline "$last..$cur" | head -20
        last=$cur
      fi
      sleep 300
    done
```

Each new commit becomes one notification line.

### PR mode — GitHub MCP subscription

Use `mcp__github__subscribe_pr_activity` directly.  Already
event-driven — no polling needed.  The harness delivers
`<github-webhook-activity>` events for comments, CI status, reviews,
and merges.  See the existing PR-subscription guidance in the system
prompt for handling.

## 3.  Per-event integration checklist

For every notification (branch commit or PR event), run through these
**four questions in order** — stop at the first "no" or "no action":

### Q1 — Should we integrate?

- Is the change on a file we touch in this branch?  Quick check:
  `git diff --name-only HEAD <NEW_SHA> -- $(git diff --name-only $(git merge-base HEAD origin/main)..HEAD)`.
- If **yes** and the change is small, rebase / pull now.
- If **yes** but large, defer until the immediate task ships and add
  a TODO.
- If **no overlap**, skip Q2/Q3/Q4 and acknowledge with a one-liner.

### Q2 — Does it conflict?

- Try a dry rebase in a worktree:
  `git worktree add /tmp/rebase-probe HEAD && cd /tmp/rebase-probe && git rebase origin/<BRANCH>; cd - && git worktree remove --force /tmp/rebase-probe`.
- Conflicts → flag the user with the file list and a brief description
  of the conflicting hunks.  Do **not** auto-resolve unless trivial
  (whitespace, unrelated import-section reflow).

### Q3 — Can we reuse?

Apply the four reuse questions from `prepare-merge.md §2a`:

1. **Definitions / lemmas / simulators / witnesses** — does the new
   commit add something our branch is duplicating, paraphrasing, or
   reinventing?  Replace with `uses[]` / `\cite{}` and delete the
   local stand-in.
2. **Proofs** — does a new lemma or tactic discharge a hypothesis,
   collapse a `calc` chain, or close a `sorry`?  Apply via
   `local/proof-simplifier` (narrative) +
   `local/lean-build-fix` / `local/lean-completeness-audit` (Lean).
3. **Exposition** — does our `.md` re-derive what main now defines
   upstream?  Replace with a forward-reference; route through
   `local/scientific-accuracy` / `local/readability-editing`.
4. **Computation** — does a new script or witness in
   `folio-assistant/computations/` supersede a hand-rolled loop or
   stale witness in our branch?  Swap in and regenerate the witness
   JSON.

For witnesses specifically: if upstream regenerated `*.witness.json`
files our branch also touched, prefer **rebase-and-regenerate** over
hand-merging the JSON.  Witness drift is structural; merging is
fragile.

### Q4 — Report or act?

- **Acted** (made the change):  one-line summary + the new commit SHA.
- **Will act after current task**:  add a TODO with what + why.
- **Skipped**:  one-line reason ("no overlap", "blocked on $TASK").

## 4.  Stop the watcher

Stop when the branch ships (PR merged, or you switch branches):

- Branch mode:  call `TaskStop` on the Monitor task ID.
- PR mode:  the harness auto-unsubscribes when the PR merges/closes;
  otherwise call `mcp__github__unsubscribe_pr_activity`.

## 5.  Common upstream patterns (heuristics)

- **Witness drift**: upstream regenerated `*.witness.json` while we
  also modified them → rebase-and-regenerate, never hand-merge.
- **Lean version bumps**: a Mathlib hash changed in `lakefile.toml` →
  check `cat .lake/packages/mathlib/lean-toolchain` aligns with our
  branch's `lean-toolchain` before continuing the Lean build.
- **Schema migrations**: if `content/schema/` changed, run
  `cd content && bun run migrate-lean-refs` and `bun run validate`
  before continuing.
- **Routine review-cycle commits** (Gemini/Copilot fixes on unrelated
  PRs):  almost always Q1 = no overlap = skip with one-liner.

## 6.  Output style

Match user-accessibility note in CLAUDE.md:

- One sentence per commit / event by default
- Numbered choices when integration is non-obvious
- Run small fixes proactively; flag big ones
