---
# qou-ahxm
title: 'Migration: Lean as compiled content nodes'
status: in-progress
type: epic
tags:
    - migration
created_at: 2026-10-04T16:35:37Z
updated_at: 2026-10-04T16:35:37Z
parent: qou-5vkl
---

Every lean.ref lands in a CI-built Lake target by lakefile edits only; no .lean file is changed. Source: LEANNODES analysis 2026-10-04 (938 sibling files, 654/1,309 lean.refs compiled today).

Owner hard rule: no math or physics content is changed; every story ends with a content-parity check.

In-progress in Round 100 PR litlfred/qou#8447.
