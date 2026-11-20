---
# qou-w6tr
title: 'Triage 590 dangling in-progress bean claims (propose-only; proposed W7)'
status: todo
type: task
priority: normal
created_at: 2026-11-20T07:50:00Z
updated_at: 2026-11-20T07:50:00Z
parent: qou-c20n
---

Found by W6 (session review, `docs/coordination/2026-11-20-session-review.{md,json}` on
`claude/session-review-2026-11-20`). Of 1,242 open beans last touched by an older session,
590 are `in-progress` with `updated_at` before 2026-11-13 and no open PR: nobody is working them.
Overall 1,814 of 5,779 beans say `in-progress`, so the status carries no information.

Task: for each, propose keep / back-to-`todo` / completed-with-commit. Propose only; the owner
or coordinator approves closures in batches. Never close a bean whose subject is an open
conjecture (AGENTS.md 13a). List: JSON `items[]` with `claim == "dangling-claim"`.
Owner decision D1 in the review doc (whether to stand up W7 for this).

Claude-Session: https://claude.ai/code/session_01VQDpPcM7ZXURrKoeUaqZaF
