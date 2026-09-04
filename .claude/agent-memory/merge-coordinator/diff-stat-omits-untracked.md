# merge-coordinator — `git diff --stat` omits untracked files

Split out of `MEMORY.md` 2026-09-03; that file is at the 200-line cap.

## What happened

PR #6510 regenerated `library/INDEX.md` with its producer. Before committing I
read the diff and reported it — in the commit message, the PR body, and to the
author — as **"purely additive: 601 files, +616/−1"**.

GitHub then reported the PR as **635 files, +4251/−9**. The commit alone is
**634 files, +4223/−1**.

## Why

`git diff --stat` compares the working tree to the **index, for tracked files
only**. It says nothing about untracked files. `git add -A` then staged 33
untracked ones — the producer had created a new `summary.json` per newly-indexed
document, ~109 lines each, which is where the missing ~3,600 insertions were.

The change was correct, and in fact *more* complete than described: those 33
files are tier 2 of the corpus-grep checklist, so the documents gained all three
tiers rather than only the index row. **Only the reported figure was wrong** —
which is its own defect, because a stated diff is what a reviewer budgets
against and what the commit message leaves behind.

## The rule

**Before quoting a diff size, use a command that sees untracked files.** Any of:

```sh
git add -A && git diff --cached --shortstat      # after staging: the real thing
git status --porcelain | wc -l                   # counts '??' rows too
git diff --stat; git status --short | grep '^??' # or read both, deliberately
```

The habit worth keeping: **quote the diff from the staged state, never from the
pre-`add` state.** After `git add -A` the two agree, and `--cached` is then the
authoritative number.

## The generalisation, which is the expensive part

Twice in the same session I quoted a tool's number without checking what that
tool counts:

- `git diff --stat` — omits untracked files (this).
- a recalled fixtures list — nobody had ever run `ls` on the directory, and the
  real count was seven, not three. It produced a wrong *blocker* on a sibling
  PR (#6509) and had to be retracted in the body, the bean and a report.

Both are the same failure: **a count answers a narrower question than the one
you asked, and reports it in the units you expected.** An index row count omits
unindexed documents. A tracked-file diff omits untracked files. A remembered
list omits whatever nobody looked at. Ask what the number's denominator is
before you put it in a commit message.
