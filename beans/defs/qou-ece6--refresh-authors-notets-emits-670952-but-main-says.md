---
# qou-ece6
title: 'RETRACTED: there is no authors-note script/file divergence — do not commit generated stats from a branch'
status: completed
type: task
priority: low
created_at: 2026-08-09T12:05:00Z
updated_at: 2026-08-09T19:05:00Z
---

**This bean's original claim was wrong and is retracted.** Kept rather than
deleted so the wrong version does not get rediscovered and re-filed — it was
asserted in a pushed commit message and a PR body before being checked.

## What I claimed

That `scripts/refresh-authors-note.ts` had diverged from the committed file:
the script emitting **670/704 (95.2%)** while #4862 had **hand-corrected**
`authors-note.md` to **661/704 (93.9%)** without touching the script — making
`check-sidecars.sh`'s "run the refresh script" hint a booby trap that silently
reverts a landed correction.

## Why it is wrong

#4862 did **not** hand-edit anything. Its own commit message says so plainly:

> Scope is the two generated files only. No prose was hand-edited; both are
> `refresh-authors-note.ts` output.

The stale, overclaiming value was the **committed** one (684/704, 97.2%);
#4862 ran the script and committed its output (661/704). It even records that
the script returned **670/704 at an earlier commit** and 661 at its own — and
attributes the movement to the corpus growing, having explicitly ruled out a
platform path-resolution change by running two platform versions.

Verified independently here on the current corpus:

| | value |
|---|---|
| committed on `main` | 661 / 704 (93.9%) |
| script, run now | **662 / 705 (93.9%)** |

The script tracks the corpus. There is no generator/file disagreement, and
never was. My 670 was simply the same script run against an older tree.

## The one real (mild) residue

Dropping the chore commit from PR #4846 was still right, but for a duller
reason than claimed: **a regenerated statistic committed on a feature branch
goes stale against `main`, and rebasing produces no conflict**, so a
stale-but-later-looking number can quietly overwrite a fresher one.

Practice, not a defect to fix:

- **Do not commit `refresh-authors-note.ts` output from a feature branch.**
  It is a whole-corpus statistic; a branch is the wrong place to snapshot it.
- If `check-sidecars.sh` flags the note as stale on your branch, that is
  expected background noise from corpus movement — **ignore it** unless the
  note is your PR's actual subject.
- Refreshing it deserves its own small PR off current `main`, exactly as
  #4862 did.

## Lesson

Same shape as the `qou-kljb` miss earlier the same day: I inferred a mechanism
from circumstantial evidence (two numbers differing) instead of reading the
source of record (#4862's commit message, which answered it in one line).
Read the rationale before theorising about it.
