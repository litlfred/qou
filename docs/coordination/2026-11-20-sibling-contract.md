# Sibling contract (coordinator = parent session, merge manager)

Repo: litlfred/qou. Children of the coordinator share one clone at /home/claude/qou (main) via git worktrees; separate sessions clone their own.
`cd /home/claude/qou && bun folio-assistant/cat-harness-tools/scripts/branch-store.ts push --id beans`; on `conflict`, re-read and retry).
`beans` CLI is not installed — edit bean .md files directly (append notes; never rewrite others' text). Check-before-create: grep the exact title first.

## Workspace
- NEVER clone. Make your own worktree: `git -C /home/claude/qou worktree add /home/claude/wt/<you> -b claude/<theme>-2026-11-20 origin/main`
  (or `git -C /home/claude/qou fetch --depth=50 origin <branch>` then worktree on it to continue an existing PR branch).
- Git proxy allows only 2 concurrent fetch/push ops for this repo: on HTTP 429 sleep 5-20s and retry (max 3). Push with
  `git -c push.negotiate=true push -u origin <branch>`.
- GitHub: REST only via `gh api` (GraphQL is 403-blocked). PR create: `gh api repos/litlfred/qou/pulls -f title=.. -f head=.. -f base=main -f body=..`.
- PR bodies end with:
  🤖 Generated with [Claude Code](https://claude.com/claude-code)

  https://claude.ai/code/session_01VQDpPdnjTBLBcPi6D5gj61
  Commits end with:
  Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01VQDpPdnjTBLBcPi6D5gj61

## Hard rules (from AGENTS.md — read the relevant .claude/skills/local/*.md before acting)
- NEVER merge. The coordinator is merge manager and gets explicit owner permission. You may push branches and open/update PRs.
- NO fitting except CAL-1/2/3. Rank routes by derivational cleanliness, never by accuracy. Empirical predictions never enter formal proofs.
- ASK-OWNER-BEFORE-CHANGING: no sweeps/migrations/refactors/mass witness refresh unless (1) increases precision or (2) derived from a corpus artifact you cite. Otherwise report the change + blast radius to the coordinator instead of doing it.
- NO-FLOAT64 in computations/ incl. probes; run scripts/precision-gates.sh --changed before committing compute.
- Lean: lean-direct exit 0 on changed files against the real import cone, `#print axioms` no sorryAx. Use the lean-verifier procedure (.claude/skills/local/lean-environment-setup.md); do not `lake build` from scratch.
- Corpus-grep checklist before declaring anything open/refuted (AGENTS.md §Before declaring "open"/"refuted").
- Long compute (>5 min): `python3 -u x.py 2>&1 | tee /tmp/<x>.log` with progress lines.
- Never force-push over someone else's branch; never delete branches; never close-and-reopen PRs.
- Stalled-claim takeover OK for in-progress beans whose branch had no commit >3h: append a takeover note with stale SHA.

## Reporting to the coordinator (your final message)
1. DONE: PRs opened/updated (number, branch, one-line what, verification actually run).
2. READY-FOR-MERGE candidates with evidence (which gate you ran).
3. DECISIONS FOR OWNER: each in the six-part frame (what it means / cost / risk / commits-to / default if no answer / recommendation marked as judgement). Do not ask the owner directly.
4. NEXT: remaining queue in priority order with bean ids.
5. Cross-workstream conflicts (files another sibling is likely touching).
Keep the report factual, numbers with commands. Do not stop at the first item: work your queue until done or blocked.

## Merge requests (cat-harness merge-manager-watcher / merge-request.bpmn)
The coordinator is the announced merge manager (comment on PR #8526). When a PR is ready:
1. `POST /repos/litlfred/qou/pulls/<n>/ccr/ready_for_review` (alone; re-read after), add label `ready-to-merge`.
2. Comment `ready: <full head sha>` on the PR with the six lines: PR URL + head SHA; session URL; 1–3 sentences on the change; preview / no preview + reason; what to look for; verification actually run (lean-library-sweep / lean-content-sweep / lean-direct -DautoImplicit=false, precision-gates, render-QA).
3. SendMessage to "main" with the same six lines. Never merge yourself.

## Predecessors (separate sessions, being stopped by the owner)
Sessions W1–W6 ran 08:30–~08:40 as separate sessions. Before starting: read every comment on PR #8526 (handoffs + any [Wn report]),
and list open PRs / remote branches matching your workstream (`gh api 'repos/litlfred/qou/pulls?state=open&per_page=100' --jq '.[]|select(.created_at>"2026-11-20")|"\(.number) \(.head.ref) \(.title)"'`).
Continue from any branch/PR they pushed (fetch with explicit refspec `git fetch origin B:refs/remotes/origin/B`); never force-push over it.
If a predecessor session is still pushing to the same branch (new commit < 10 min old), SendMessage "main" before touching it.

## Progress (dispatch-agent contract)
Your label is your workstream id (w1..w6). At each meaningful step emit a plain-text block:
### ⟦PROGRESS⟧ <label> · step N
DID: <evidence: paths, exit codes, shas, counts>
DOING: <live command + last log lines>
NEXT: <one action>
BLOCKERS: <none | precise>
Finish with ### ⟦DONE⟧ <label> plus the report above. The shared clone's .git/shallow.lock is contended: retry fetches with sleep.

## Shared Lean cache (ready 2026-11-20 ~08:55, by w1)
source /home/claude/qou/scripts/lean-direct-env.sh ; lean -DautoImplicit=false -s 65536 <file.lean>
Cache head a792c46d01b, 6492 oleans in /home/claude/qou/.lake + folio/*/lean/.lake. READ-ONLY.
- Never `lake build`; never write into /home/claude/qou/**/.lake.
- QOU modules edited since the seed are absent/stale in the cache — rebuild only your cone in a private hardlink mirror
  (scripts/lean-library-sweep.py --shadow /tmp/<label>-shadow, scripts/lean-shadow-verify.sh), pass only changed files,
  and `rm -rf` the shadow when done. Disk ~11 GB free shared by six children: check df first; tell main before anything > 1 GB.
- Missing Mathlib modules (HopfAlgebra.Basic, FiberBundle.Basic, UpperHalfPlane.Basic, GroupCohomology.LowDegree cone):
  scripts/lean-restore-gap-oleans.sh — ask main first so only one child runs it.
