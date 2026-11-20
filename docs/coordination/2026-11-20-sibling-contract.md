# Sibling contract (coordinator = parent session, merge manager)

Repo: litlfred/qou. Each workstream is its own Claude Code session; clone per the add_repo instructions (shallow, generous timeout).
`bun folio-assistant/cat-harness-tools/scripts/branch-store.ts push --id beans`; on `conflict`, re-read and retry).
`beans` CLI is not installed — edit bean .md files directly (append notes; never rewrite others' text). Check-before-create: grep the exact title first.

## Workspace
- Branch off origin/main as `claude/<theme>-2026-11-20`, or fetch an existing PR branch with `git fetch --depth=50 origin <branch>` and continue it.

- Git proxy allows only 2 concurrent fetch/push ops for this repo: on HTTP 429 sleep 5-20s and retry (max 3). Push with
  `git -c push.negotiate=true push -u origin <branch>`.
- GitHub: REST only via `gh api` (GraphQL is 403-blocked). PR create: `gh api repos/litlfred/qou/pulls -f title=.. -f head=.. -f base=main -f body=..`.
- PR bodies end with:
  🤖 Generated with [Claude Code](https://claude.com/claude-code)

  <your own session URL>
  Commits end with:
  Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
  Claude-Session: <your own session URL>

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

## Channel to the coordinator (separate-session mode)
Post your report (format above) as a comment on PR #8526 (`gh api repos/litlfred/qou/issues/8526/comments -f body=...`)
at each milestone: whenever a PR becomes READY-FOR-MERGE, whenever you need an owner decision, and at the end.
Start the comment with `[W<n> report]`. The coordinator is subscribed to #8526 and is the only one who merges.
