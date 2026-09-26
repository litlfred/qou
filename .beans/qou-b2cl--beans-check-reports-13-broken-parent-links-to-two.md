---
# qou-b2cl
title: beans check reports 13 broken parent links to two deleted parents
status: todo
type: bug
priority: normal
tags:
    - beans-hygiene
created_at: 2026-09-26T10:51:41Z
updated_at: 2026-09-26T10:53:23Z
parent: qou-w3yy
---

**Measured 2026-09-26.** `beans check` exits with **13 issues**, all of one kind:

```
✗ qou-rhyp: broken link parent:0yqu
✗ qou-fivt: broken link parent:0yqu
✗ qou-mlbg: broken link parent:0yqu
✗ qou-8v3k: broken link parent:0yqu
✗ rvnc:     broken link parent:krvm
✗ qou-rstq: broken link parent:0yqu
✗ qou-trns: broken link parent:0yqu
✗ m015:     broken link parent:krvm
✗ qou-abel: broken link parent:0yqu
✗ qou-r7ml: broken link parent:0yqu
```

Two parents — `0yqu` and `krvm` — no longer exist, and 13 children still point at
them. Reproduce with `beans check`.

## Why it matters for the epic/story work

These are beans that WERE organised and lost their parent. So the 83% orphan rate
in sibling `qou-63fo` is not purely "never parented" — some fraction is
"parented, then orphaned by a deletion that took no children with it". Any
hierarchy work should fix these first, because they are the cases where the
intended grouping is known and only the target is missing.

## Fix

For each: identify what `0yqu` / `krvm` were (git log over `.beans/`), then either
re-point to the surviving successor epic or `--remove-parent`. Cheap — 13 beans —
and `beans check` going to 0 is the verification.

Not proposed here: which successor each should point at. That needs the deleted
parents' titles, which this measurement did not recover.
