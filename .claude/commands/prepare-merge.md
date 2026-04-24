---
description: Request Gemini + Copilot reviews on the current PR and subscribe to PR activity
---

Prepare the current branch's PR for merge:

1. Find the open PR for the current branch in `litlfred/qou` using
   `mcp__github__list_pull_requests`. If none exists, tell the user and stop.
2. Post a `/gemini review` comment on the PR using
   `mcp__github__add_issue_comment`.
3. Request a Copilot review using `mcp__github__request_copilot_review`.
4. Subscribe to PR activity with `mcp__github__subscribe_pr_activity` so
   CI failures and review comments are delivered to this session.
5. Report the PR URL and confirm both review requests posted.
