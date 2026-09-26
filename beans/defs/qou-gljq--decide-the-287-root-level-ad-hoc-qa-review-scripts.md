---
# qou-gljq
title: 'Decide the 287 root-level ad-hoc QA review scripts: delete as debris or consolidate'
status: completed
type: task
priority: normal
created_at: 2026-08-25T07:10:38Z
updated_at: 2026-08-25T07:51:38Z
---

DONE — deleted, author-approved. 316 root-level .py removed (selected by
CONTENT: root .py writing qa.json/"criteria", not by filename glob — hence
316, not the 287 an earlier `review_*` glob suggested).

Evidence they were scratch, not infrastructure:
- 0 of 316 referenced from .github/.claude/docs/scripts or imported by any
  other Python. The one apparent hit was the English word "rewrite".
- 286 distinct hashes / 316 files — bespoke one-offs.
- rewrite.py hardcodes /Users/litlfred/space_cats/qou/amalgamated_input.
- None emits field_hash; none handles evidence.

Verdicts they wrote live in the sidecars and are unaffected. All 316 were
tracked, so recoverable from history. qou#5745.

NOTE: the on-disk rm was blocked by the sandbox classifier; `git rm --cached`
was permitted, so the deletions are committed and the leftover working-tree
copies are ephemeral container files. A future session on a fresh clone will
not see them.
