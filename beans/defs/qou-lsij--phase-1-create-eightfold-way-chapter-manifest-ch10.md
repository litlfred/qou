---
# qou-lsij
title: 'Phase 1: Create eightfold-way chapter manifest (Ch10)'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-arch
created_at: 2026-08-04T01:29:45Z
updated_at: 2026-10-10T07:16:23Z
parent: qou-8lxd
---

## COMPLETED — verified 2026-10-10 against the live tree

`folio/quantum-observable-universe/eightfold-way/` holds **16** content blocks,
and the chapter is wired into the paper manifest at
`folio/quantum-observable-universe/quantum-observable-universe.ts:97` as
`chapterRef({ dir: "eightfold-way" })`.

Bean was TITLE-ONLY and sat `todo` for ~9 weeks after its own task had landed.
Verified on the post-rename paths (`content/` -> `folio/`), not on a stale
checkout — an earlier pass of this cleanup read a tree 1245 commits behind and
got two other numbers wrong for exactly that reason.
