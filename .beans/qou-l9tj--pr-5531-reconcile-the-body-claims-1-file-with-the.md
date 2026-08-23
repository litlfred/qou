---
# qou-l9tj
title: 'PR #5531: reconcile the body (claims 1 file) with the 11-file diff; 10 sibling bean files rode along'
status: completed
type: task
priority: normal
created_at: 2026-08-23T13:04:35Z
updated_at: 2026-08-23T13:23:27Z
---


## DONE 2026-08-23 — 10 duplicates removed, diff now matches the body

All ten verified recoverable from main IN BETTER FORM before removal:
five strictly contained in main's counterpart; both `s5bb` files contained
in main's consolidated 217-line version; `sp06` superseded by main's
titled copy (which carries a note naming this duplicate as the stale one);
`qou-mpq5` malformed (front-matter appended at end); `qou-x4qm` re-issued
by main as `qou-5isd` to break an id collision.

Keeping them would have been actively wrong, not untidy — re-landing
`qou-x4qm` undoes main's fix. Removed as a NEW commit (`63ec71df`), not an
amend, so the branch stays fast-forward.

PR now reports `changed_files: 1`, `+58/-1`, `mergeable_state: clean`.
Root cause opened as `qou-uoad` (beans CLI slug drift).
