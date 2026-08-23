---
# qou-z36p
title: 'PR #5517 follow-through: attribute every further sublemma-2-1 witness move to the PR or to pre-existing staleness'
status: in-progress
type: task
created_at: 2026-08-23T13:22:15Z
updated_at: 2026-08-23T13:22:15Z
---

Continues the stalled #5517 session (container reclaimed; the diagnostics were
never committed). Two further `sublemma-2-1-*` witnesses sit downstream of
`char_fast._compiled_sigmas` and neither was covered by the PR.

Method: three-way — committed blob vs a fresh run at the PR's BRANCH POINT
(9e85a43628) vs a fresh run at the PR head (ed36cf64c1), same venv, both in
detached worktrees restored after every run. Comparing against `origin/main`'s
tip would have been wrong: main has moved 5 commits since the branch point,
two of them on adjacent compute.

Findings recorded on the branch; see the audit doc.
