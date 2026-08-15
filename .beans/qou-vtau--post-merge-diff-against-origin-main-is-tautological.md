---
# qou-vtau
title: 'The post-merge check `git diff origin/main <merged-head>` is TAUTOLOGICAL — it cannot detect a dropped commit'
status: todo
type: task
priority: high
created_at: 2026-08-15T23:30:00Z
updated_at: 2026-08-15T23:30:00Z
---

## The trap

After a **rebase-merge**, your PR's head *becomes* `origin/main`'s tip. So

```bash
git diff origin/main <merged-head>      # ← passes trivially
```

compares a commit **to itself**. It returns empty whether or not anything was
dropped. Whenever your PR is the last thing to merge — the normal case for a
pipeline that merges what it just rebased — this check verifies **nothing** while
looking like the strongest possible evidence.

## Why this bean exists

This session (2026-08-15) landed **ten** PRs and instructed every merge agent to
use that check as *"the strongest check — stronger than grepping strings."*
That instruction was **wrong**, and it was wrong in the direction that matters:
it replaced a check that works with one that cannot fail.

The irony is on the record. The **real** dropped commit this session — #5111's
rebase-merge landing 7 of 8 commits, recovered as #5125 — was caught by
**grepping `main` for the edited content**. The diff check was then promoted
over the grep that actually did the work.

Caught by the #5161 merge agent, which ran the tautological check, noticed it
was comparing a commit to itself, and substituted a real one rather than
reporting the free pass.

## What to run instead

Two checks, neither tautological:

```bash
# 1. Did the merge replay MY hunks?  Compare the merged commit's own diff
#    against the diff my branch commit produced pre-merge.
git diff <merged-head>^ <merged-head>

# 2. Is the resulting content byte-identical?  Blob hashes on both sides.
git rev-parse <merged-head>:<path>  &&  git rev-parse <branch-head>:<path>
```

For a multi-commit PR, walk the range (`git log <base>..<merged-head>`) and
confirm every commit replayed — a count alone is not enough, since a rebase can
drop one and still report success via the API.

**Diffing `main` against your PRE-merge branch head is also misleading** in the
other direction: it shows every sibling PR that landed between your rebase base
and your merge as though it were your change. The #5161 agent saw 38 such files
and correctly traced them to #5118 landing mid-pipeline, rather than reporting a
drop.

## Where this needs to land

`.claude/skills/local/prepare-merge-auto.md`'s post-merge step, so the next
pipeline inherits the working check rather than the tautology. Until then, any
PR body from 2026-08-15 citing *"`git diff origin/main <head>` empty"* as
drop-verification should be read as **unverified on that point** — though for
this session's merges the substantive gates (probe counts, `lean`-direct exit 0,
byte-identical witnesses, content greps) were run independently and do stand.

## Generalisable form

A verification that **cannot fail** is not a verification. When a check passes
first time, every time, on every PR, that is evidence about the *check*, not
about the code. Ask what result would have failed it — and if the answer is
"none reachable from here," replace it.
