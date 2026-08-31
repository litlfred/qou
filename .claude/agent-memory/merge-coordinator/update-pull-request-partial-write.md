# `update_pull_request` partial writes — the full case

Referenced from `MEMORY.md`. Measured on `litlfred/qou#6264`, 2026-08-31.

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

Related in kind to the CI-billing rule in AGENTS.md: an infrastructure error
whose surface message names the wrong cause. The tell here is the same one that
caught the ledger `source_hash` bug earlier in the same session — **the count
did not move**, so check whether the write landed before assuming it did not.

