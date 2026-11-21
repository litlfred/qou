---
# qou-ommr
title: 'refs-prose-mentions (#2): EXTEND validate-defterm.ts corpus-wide to flag prose mentions of a defterm/block-title whose definition is introduced LATER in reading order (prose forward-ref). Do NOT build a duplicate per-block checker — overlaps detangler-no-forward-ref + validate-defterm'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-08T02:05:14Z
updated_at: 2026-11-21T18:00:00Z
parent: qou-5vkl
---

## 2026-11-21 (thread: Design the remaining Lean vacuity detectors)

Implemented as warning-only rule defterm-forward-ref in litlfred/cat-harness-tools#2486 (issue #2485); glossary-chapter definitions exempt per owner ruling 2026-11-21. qou paper: 46 warnings in 41 blocks (43 bare, 3 :refterm). Correction: the earlier '45 :refterm' figure counted glossary targets; body-defined forward :refterm links are 3. Open until #2486 merges.
