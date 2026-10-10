---
# qou-pt9b
title: 'INFRA (measured): 4 of 4 changed-file collectors were narrower than the branch'
status: completed
type: task
priority: normal
created_at: 2026-08-22T20:49:54Z
updated_at: 2026-08-22T21:22:18Z
---

Recorded from PR #5474 so the finding survives the branch.

Swept every script in the repo that computes a changed-file set from git.
There are exactly four, and ALL FOUR collected something narrower than
"what this branch changed":

  scripts/precision-gates.sh      working tree only  -> false all-clear post-commit
  scripts/check-sidecars.sh       working tree only  -> same, AND it is the
                                                        Phase-4 merge gate, where
                                                        changes are always committed
  scripts/staleness-gates.sh      working tree only  -> same
  scripts/lean-verify-changed.sh  HEAD~1             -> verifies the last commit only

All four fixed on #5474. Measured under-coverage for the Lean one across six
live sibling branches (HEAD~1 vs merge-base):

  q407-self-assuming-projections   12 commits    0  vs  26
  cat3-decl-relocation              3 commits    3  vs   9
  schensted-qside-corners          33 commits    2  vs   9
  fivetwo-level7-ladder            25 commits    2  vs   9
  prefix-self-similarity           11 commits    0  vs   1
  two-particle-yang-baxter          8 commits    0  vs   0

Five of six under-covered. On q407 it prints "no .lean files to check" and
exits 0 over TWENTY-SIX changed Lean files.

WHY THIS IS A BEAN RATHER THAN JUST A FIX. The four were written at
different times by different agents and every one independently chose a
working-tree or last-commit read. That is not four mistakes; it is a
default that looks right when you write it and is wrong given
AGENTS.md rule 3 (one commit per logically distinct change) and rule 0
(commit early, commit often). Any NEW gate script will reach for the same
idiom.

Suggested follow-up (not done): a shared helper — scripts/lib/changed-files.sh
— so the next gate cannot get it wrong, and so the merge-base fallback
(origin/main unfetched) is handled in one place instead of four.
