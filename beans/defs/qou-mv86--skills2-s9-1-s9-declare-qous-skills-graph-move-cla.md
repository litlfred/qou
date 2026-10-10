---
# qou-mv86
title: '[SKILLS2 S9] Declare qou''s skills graph'
status: completed
type: feature
priority: normal
tags:
    - migration
    - skills2
created_at: 2026-10-04T16:35:50Z
updated_at: 2026-10-04T17:00:40Z
parent: qou-7vh1
---

From the SKILLS2 migration analysis (2026-10-04), story S9. Full report: docs/audits/2026-10-04-workplan-and-migration/SKILLS2_report.md.

1. S9 Declare qou's skills graph. Move `.claude/skills/local/` by rename to `skills/` (package `qou`) and add a `kg` entry to `qou.json`. Done when: `skill_list` shows the `qou` package, and `sha256sum` of every moved file matches. Size S. Depends on nothing.

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.



## Summary of Changes

Done 2026-10-04 (commit 8d1c8b949): .claude/skills moved to skills/ by 136 pure renames (R100), .claude/skills is a symlink to ../skills so every old path still resolves. kg-export --judge on qou: 6 -> 99 nodes, 0 findings. No skill file content changed.
