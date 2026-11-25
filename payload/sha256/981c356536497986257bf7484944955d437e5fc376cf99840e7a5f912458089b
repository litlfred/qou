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

> **Merge Steward vs Sibling Watcher Routing (`STRICT`):**
> - If you hold the active **`merge-steward`** lane watching the merge queue, follow [`folio-assistant/cat-harness/sdlc/skills/sdlc-core/merge-manager-watcher.md`](../../folio-assistant/cat-harness/sdlc/skills/sdlc-core/merge-manager-watcher.md), [`merge-queue.md`](../../folio-assistant/cat-harness/sdlc/skills/sdlc-core/merge-queue.md) (`Process_MergeTrain` + `merge-overlap`), [`merge-to-main.md`](../../folio-assistant/cat-harness/sdlc/skills/sdlc-core/merge-to-main.md) (`Process_MergeToMain`), and [`prepare-merge-auto.md`](prepare-merge-auto.md) — **never** poll in an intra-turn loop.
> - If you are a **`sibling-session`** watching your submitted Ready PR in the queue, follow `merge-queue.md` §"After submitting: do not spend CI you do not need yet": **never self-merge onto `main`**, and stand still (do not churn rebases on non-overlapping `main` advances) unless your PR conflicts or the `merge-steward` notifies you that your PR is in the next train.

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
# Sanitize branch name for use in a file path: replace `/` with `_`
# (e.g. `feature/foo` → `feature_foo`).  Without this, branches with
# slashes silently land in non-existent directory trees.
SAFE_BRANCH=$(printf '%s' "<BRANCH>" | tr '/' '_')
git rev-parse "origin/<BRANCH>" > "/tmp/_watch_baseline_${SAFE_BRANCH}.sha"
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

- Try a dry rebase in a fresh worktree.  Use `mktemp -d` so the
  path is unique (avoids collisions with previous failed runs and
  with parallel `/watch` invocations) and clean up unconditionally
  via `trap`:

  ```bash
  PROBE=$(mktemp -d /tmp/rebase-probe.XXXXXX)
  trap 'git worktree remove --force "$PROBE" 2>/dev/null; rm -rf "$PROBE"' EXIT
  git worktree add "$PROBE" HEAD >/dev/null
  ( cd "$PROBE" && git rebase "origin/<BRANCH>" )
  status=$?
  # trap fires on EXIT
  ```

- Conflicts (`status != 0`) → first attempt **auto-resolve** for
  the recurring drift-conflict pattern (see §2a below); only flag
  the user if auto-resolve fails or the conflict is non-trivial
  (overlapping logic edits, schema rewrites, etc.).

#### §2a — Auto-resolve drift-conflict pattern (`qou-v0t8`: Contended Tree-Measuring Audit Witnesses)

> **🛑 `qou-v0t8` RULE (OVERRIDES OLD REGEN-ON-BRANCH ADVICE):** Tree-measuring audit witnesses count properties across the whole working tree and are regenerated on `main`'s own cadence. **NEVER regenerate or commit any of the contended tree-measuring audit witnesses from a feature branch** — doing so either walks a drain-only ratchet backwards (if behind `main`) or immediately re-acquires a merge conflict on the next `main` landing:
> - `computations/audits/q0-anchor-consistency-audit.witness.json`
> - `computations/mpf-float-source-audit.witness.json`
> - `computations/mpf-import-time-dps-audit.witness.json`
> - `computations/never-raises-dps-audit.witness.json`
> - `computations/witness-float64-padding-audit.witness.json`
> - `computations/witness-raw-float64-audit.witness.json`
> - `computations/q0-value-drift-audit.witness.json`
> - `computations/no-free-parameter-certificate.witness.json`
> - `computations/codata-truncation-audit.witness.json` (plus `witness-value-copy-audit`, `compute-audit-scan`, `derivation-chain-audit`, `e0-calibration-audit`)

The recipe when `git rebase origin/<BRANCH>` halts on any contended audit witness (run on the **real** branch, not the probe worktree):

```bash
# 1. If the conflicting commit ONLY touched contended audit witnesses, drop/skip it:
git diff --name-only --cached | grep -qE '\.witness\.json$' && \
  ! git diff --name-only --cached | grep -vE '(q0-anchor-consistency-audit|mpf-float-source-audit|mpf-import-time-dps-audit|never-raises-dps-audit|witness-float64-padding-audit|witness-raw-float64-audit|q0-value-drift-audit|no-free-parameter-certificate|codata-truncation-audit|witness-value-copy-audit|compute-audit-scan|derivation-chain-audit|e0-calibration-audit)\.witness\.json$' && \
  git rebase --skip

# 2. If a mixed commit accidentally included a contended audit witness alongside real work,
#    take origin/main's copy (--ours during rebase onto origin/main) so your commit drops the diff:
git checkout --ours -- <contended-audit-witness.json>
git add <contended-audit-witness.json>
git rebase --continue
```

And whenever you run `scripts/compute-qa.py` or `scripts/precision-gates.sh` locally on a feature branch, always revert any dirtied contended audit witnesses before staging (`git checkout -- computations/audits/ computations/*.witness.json`).

For `.qa.json` sidecar conflicts during rebase, resolve script entries to `origin/main` and restore agent verdicts mechanically via:
`python3 scripts/qa-sidecar-agent-union.py --against <pre-rebase-ref> --apply`.

Only flag the user if:

- The conflict is in a **source file** (`.py`, `.lean`, `.ts`,
  `.md`) — those are real semantic conflicts that need human
  judgment.
- The conflict is in a witness **other than** the three audit
  witnesses above (e.g. `markov-trace-axiomatic-multi-atom.witness.json`
  has a substantive numerical drift — that means a CI-run script
  on main produced different numerical output, which deserves a
  closer look before blindly accepting).
- The auto-resolve recipe itself fails (regen script errors out,
  push rejected for non-fast-forward reasons, etc.).

For witnesses specifically: if upstream regenerated `*.witness.json`
files our branch also touched, prefer **rebase-and-regenerate** over
hand-merging the JSON.  Witness drift is structural; merging is
fragile.

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
   `computations/` supersede a hand-rolled loop or
   stale witness in our branch?  Swap in and regenerate the witness
   JSON. (See §2a for the routine compute-audit-scan / derivation-
   chain-audit / e0-calibration-audit drift-conflict pattern.)
   - When the upstream commit adds or modifies a `prop:` / `thm:` /
     `lem:` / `cor:` block (or its `.lean` sibling), delegate to
     `local/compute-integration-watcher` to check whether the new
     claim is wired into the production compute chain. The watcher
     runs the I1–I12 wiring checklist and returns a verdict
     (WIRED / PROBE-ONLY / NOT-WIRED) plus a concrete fix
     recommendation. Capture the verdict here and feed it into Q4.

### Q3a — Did upstream land a new skill file?

For each main-refresh, check whether `.claude/skills/local/*.md` (or
`.claude/skills/<pkg>/*.md`) gained a new file between this branch's
prior baseline and the new `origin/main`:

```bash
git diff --name-only --diff-filter=A "$LAST_BASE..origin/main" \
  -- '.claude/skills/local/*.md' '.claude/skills/*/*.md'
```

For each new skill file:

1. **Read its frontmatter** — extract `name`, `roles`, `description`,
   and any `inherits` field.
2. **Match against branch scope** — does the skill's description
   overlap with what this branch is doing? Heuristics:
   - skill description mentions a file kind / domain / pattern
     that appears in this branch's `git diff origin/main..HEAD
     --name-only`, OR
   - skill is a new integration-watcher child (`inherits:
     local/integration-watcher`) and your branch is itself an
     integration-watcher PR, OR
   - skill is a content-block QA skill (e.g. `one-voice-*`,
     `proof-*`, `compute-*`) and your branch touches `.md` /
     `.ts` / `.lean` content blocks.
3. **Surface to the user via `AskUserQuestion`** with the standard
   3-chip pattern:

   > New skill `<name>` landed on main:
   > > `<one-line description from frontmatter>`
   >
   > This branch's scope overlaps because `<one-line match
   > rationale + file paths>`.
   >
   > 1) **Adopt now** — invoke the skill on the relevant subset of
   >    this branch's diff before continuing.
   > 2) **Defer to follow-up branch** — record the decision and
   >    note for the next branch; don't change this branch.
   > 3) **Not relevant** — record so the watcher doesn't re-prompt
   >    on future main-refreshes.

4. **Record the decision** in the watcher's ledger
   (`.beans/<watcher-name>-ledger.md` for integration-watcher
   children, or chat-only for the bare `/watch` flow) so subsequent
   main-refreshes don't re-prompt for the same skill.

This rule applies to **skill files only** (`.claude/skills/local/*.md`
and `.claude/skills/<pkg>/*.md`). Skills landing on sibling PRs that
haven't merged yet do NOT trigger this check — only `main` commits
count, mirroring the §2 "watch origin/main" scope.

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
- **Schema migrations**: if `folio/schema/` changed, run
  `cd content && bun run migrate-lean-refs` and `bun run validate`
  before continuing.
- **Routine review-cycle commits** (Gemini/Copilot fixes on unrelated
  PRs):  almost always Q1 = no overlap = skip with one-liner.

## 5b.  Monitor-timeout recovery (MANDATORY when re-arming)

Background Monitors time out (`[Monitor timed out — re-arm if needed]`).
**Do not just re-arm and continue** — between the last event and the
timeout, main may have moved substantially. Mandatory steps on
timeout-recovery:

```bash
# Compare current baseline against actual main HEAD
git fetch origin main 2>/dev/null
SAFE=$(echo "<BRANCH>" | tr '/' '_')
LAST=$(cat /tmp/_watch_baseline_${SAFE}.sha 2>/dev/null || echo "")
CUR=$(git rev-parse origin/<BRANCH>)
if [ "$LAST" != "$CUR" ]; then
  MISSED=$(git log --oneline "$LAST..$CUR" 2>/dev/null | wc -l)
  echo "MISSED $MISSED commits while watcher was down"
  git log --oneline "$LAST..$CUR" | head -10
  # Update baseline AFTER reporting
  git rev-parse origin/<BRANCH> > /tmp/_watch_baseline_${SAFE}.sha
fi
```

If `MISSED >= 5` OR any missed commit touches a file in your branch's
diff, run the §3 integration checklist on the missed range BEFORE
arming a fresh monitor.

This catches the failure mode where a focused work session (axiom
discharge sweep, content authoring marathon, witness regeneration
loop) silently lets main move 10+ commits ahead while the watcher
is timed out.

## 6.  Output style

Match user-accessibility note in AGENTS.md:

- One sentence per commit / event by default
- Numbered choices when integration is non-obvious
- Run small fixes proactively; flag big ones
