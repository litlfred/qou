---
description: Full pre-merge workflow — rebase onto upstream, integrate new content, one-voice review, 100% Lean, then request Gemini + Copilot reviews
---

Prepare the current branch's PR for merge. Execute the steps **in order** —
do not request external reviews until every earlier step has succeeded.

## 1. Rebase onto upstream HEAD, resolve conflicts

- `git fetch origin` and identify the upstream default branch (typically `main`).
- Rebase the current branch onto `origin/main`.
- If conflicts arise, resolve them (never discard the user's work; ask when
  a resolution is non-obvious). Re-run validation after each conflict fix.
- Continue until the rebase completes cleanly.

## 2. Integrate new content from upstream

- Pull in any new content blocks, glossary updates, or references that
  landed on `origin/main` during the branch's lifetime.
- Re-run `content-validation` to confirm cross-refs, `uses[]`, and
  `interprets` still resolve after integration.
- Run the `remark-audit` skill to catch any newly dangling remarks.

## 3. One-voice review

- Invoke the `one-voice` skill across every `.md` file touched on this
  branch. Fix voice / style inconsistencies before proceeding.

## 4. 100% Lean — build + resolutions

- Run `lake build` in `content/quantum-observable-universe/lean/`.
- If the build fails, route to `lean-build-fix` and resolve.
- Run `lean-completeness-audit`: every `sorry` must carry a `-- Ref:`
  citation, every `definition` block must have its `.lean` sibling,
  and every provable block kind (`theorem`/`lemma`/`proposition`/
  `corollary`) must have a Lean statement.
- Run `proof-simplifier` on any proofs that changed on this branch.
- The Lean build must be green and the audit must report 100%
  coverage before continuing.

## 5. Final rebase pass

- After all fixes above, rebase once more onto the current `origin/main`
  HEAD (upstream may have moved). Resolve any new conflicts. The branch
  tip must fast-forward onto `origin/main`.
- Push with `git push --force-with-lease -u origin <branch>`.

## 6. Request external reviews (only after 1–5 succeed)

- Find the open PR for the current branch in `litlfred/qou` using
  `mcp__github__list_pull_requests`. If none exists, tell the user
  and stop.
- Post a `/gemini review` comment on the PR using
  `mcp__github__add_issue_comment`.
- Request a Copilot review using `mcp__github__request_copilot_review`.
- Subscribe to PR activity with `mcp__github__subscribe_pr_activity`
  so CI failures and review comments are delivered to this session.
- Report the PR URL and confirm both review requests posted.

## Failure handling

If any step 1–5 fails and cannot be resolved automatically, **stop**
and report the blocker to the user. Do not request Gemini or Copilot
review on a branch that does not rebase cleanly, fails Lean build,
or has voice inconsistencies — it wastes reviewer attention.
