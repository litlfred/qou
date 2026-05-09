---
description: Coordinate work across multiple in-flight Claude PRs working toward a shared goal — post intent + asks on sibling PRs, identify cherry-picks, respond to review comments, periodic triage, watch main + new branches, escalate inconsistent findings, maintain a coordination ledger
---

Run the **`local/coordinate`** skill against the current branch / PR.
The full protocol lives in
[`.claude/skills/local/coordinate.md`](../skills/local/coordinate.md);
this command is the user-invocable wrapper.

## Quick checklist (read the skill for details)

1. **Read sibling PRs first** — `gh pr view <N> --json …` (or
   `mcp__github__pull_request_read`); build a scope map.
2. **Classify each sibling** on three axes — overlap / dependency /
   cherry-pick (skill §2).
3. **Post intent** on every sibling with a non-trivial relationship
   (skill §3) — *one* coordination comment, not a stream.
4. **Triage review comments on your own PR** (skill §5) — every
   gemini/copilot/codex thread gets one of `accept` /
   `accept-with-modification` / `reject-with-reason` / `escalate`,
   followed by a single consolidated status comment.
5. **Periodic sibling triage** (skill §7) — every 3–5 of your own
   commits, pull new comments + commits + CI status across siblings;
   prefer a background `Agent(subagent_type=Explore,
   run_in_background=true)` so foreground work continues.
6. **Watch `main` + new branches** (skill §8) — `git fetch origin
   main` each cycle; classify any main-landed change touching your
   files; prompt the author before adding a freshly-opened sibling
   PR to your scope.
7. **Inconsistent findings → escalate** (skill §6) — never silently
   rewrite your framing.
8. **Cherry-pick under §10 rules** — cite the source PR in the
   commit message; match author voice.
9. **Append to the coordination ledger**
   `docs/coordination/<goal-slug>.md` (skill §9).

## Inputs

When invoked without arguments, infer the goal and sibling list from:

- The current branch's PR body (`gh pr view --json body`).
- Recently opened PRs in `litlfred/qou` (`gh pr list --state open
  --json number,title,headRefName`).
- The user's `/coordinate` arguments, e.g.
  `/coordinate goal="1 ppb mass" siblings=#564,#565,#567`.

If the user names sibling PRs, use those exactly. Otherwise propose a
short scope map (≤ 4 PRs) and ask for confirmation **once**, then
proceed without further interruption.

## Output

End the run with:

- A scope map (your PR + siblings + classification).
- The coordination comments you posted (links).
- Any §6 escalations (with `@<author>` tagging).
- The next concrete, non-overlapping task on your queue.

See the skill file for the full anti-pattern list — in particular,
do not "split the difference" on inconsistent findings, do not
silently merge `main`, and do not add a newly-opened PR to scope
without prompting the author.
