---
# qou-b2cl
title: beans check reported 13 'broken links' — the parents EXIST; the hierarchy was ILLEGAL (task parenting task)
status: completed
type: bug
priority: normal
tags:
    - beans-hygiene
created_at: 2026-09-26T10:51:41Z
updated_at: 2026-09-26T11:08:08Z
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



## 🛑 CORRECTED AND FIXED 2026-09-26 — my own diagnosis above was WRONG

This bean said `0yqu` and `krvm` were **deleted parents** and that fixing it
needed `git log` archaeology. **Both parents exist on disk** and always did:

    .beans/qou-0yqu--gap-prove-the-5-saddle-sum-rule-σ-j-re-v-j-3π2.md
    .beans/qou-krvm--gap-discharge-optima-coincides-hypotheses-for-the.md

Two things were actually wrong, and `beans check`'s wording hid both:

1. **An ID-prefix mismatch.** The 13 children declared `parent: 0yqu` / `krvm`,
   bare, while the beans carry the `qou-` prefix.
2. **And the real blocker, which is a TYPE constraint, not a link at all.**
   Re-pointing to `qou-0yqu` still failed:

       Error: task beans can only have milestone, epic, or feature as parent, not task

   Both parents were `type: task`. The CLI forbids task→task parenting, so the
   hierarchy was **illegal**, not dangling.

**`beans check` calls both of these "broken link", which is why the diagnosis
went wrong.** A bean pointing at a real, resolvable parent of the wrong TYPE
reports identically to one pointing at nothing. That is a detector wording
problem in the upstream CLI, and it is the reusable lesson here — the same
shape as the taxonomy's row 30, a message that conflates two structural facts.

## The fix, applied

`qou-0yqu` → `feature` (it has **11** children) and `qou-krvm` → `feature`
(**2** children). A bean with eleven children is a story, not a task, so the
promotion is the semantically right move and not merely a constraint dodge. Then
all 13 children re-pointed to the prefixed IDs.

**Verified:** `beans check` → `✓ No link issues found / All checks passed`
(was `13 issues found`).
