---
# qou-y8d0
title: The warn-only pre-commit hook WRITES the raw-float64 ratchet witness on every computations commit
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-06T09:19:43Z
updated_at: 2026-11-16T19:56:39Z
parent: qou-9nnz
---

## The finding (2026-09-06)

`scripts/precommit-precision-warn.sh` is a `PreToolUse` hook on `Bash` that fires
on any commit touching a witness or a `computations/` script. It runs
`witness_raw_float64_audit.py --strict`, and that script **WRITES**
`computations/witness-raw-float64-audit.witness.json` via `WitnessBuilder`
(`out.write_text`, line 1025).

So the sequence that bites is entirely ordinary and involves no gate run:

    git add -A && git commit ...     # hook fires, rewrites the ratchet witness
    <more work>
    git add -A && git commit ...     # silently commits the rewritten witness

**Isolated, not inferred.** On PR #6919 `git add -A` swept in four contended
audit witnesses; after reverting all four, the raw-float64 one came back dirty on
the very next commit, with `precision-gates.sh` not running.

## Why this is NOT covered by `qou-v0t8`, which is `completed`

`qou-v0t8` is about `precision-gates.sh` regenerating these files and then
advising you to commit one. Its guard (2026-08-30) changes that script's **banner
text** on non-main branches to "DO NOT COMMIT THESE". Good fix, wrong surface for
this: grep `qou-v0t8` for `precommit` / `hook` / `WitnessBuilder` and the count is
**zero**. Its advice is addressed to someone who has just *chosen* to run the
gate; on this path nobody makes that choice, so nobody is reading it.

Opened separately rather than reopening a sibling's closed bean.

## Three cheap mitigations, NONE APPLIED — this is a report

1. Run the ratchet in a read-only / temp-output mode. A hook documented as
   warn-only writing a tracked file is not warning; this is the principled fix.
2. Restore the witness after the hook runs.
3. Add these files to a commit-time exclusion.

Which of the three is the hook owner's call, not mine. (1) is my recommendation,
marked as judgement: it removes the class rather than the instance, and a
warn-only hook has no business mutating the tree at all.

## Workaround for agents until then

**Stage by path, not `git add -A`, on any branch that touches `computations/`.**
`git add -A` cannot tell a deliberate edit from one a hook made underneath it.

## Progress Update (Round 50 — PR #8178)

- Added `--no-write` flag to `computations/witness_raw_float64_audit.py` and passed `--no-write` from `scripts/precommit-precision-warn.sh` so the warn-only `PreToolUse` hook runs the ratchet in read-only mode without rewriting `computations/witness-raw-float64-audit.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8178 (`6465362ef2e7902778c4f8796f81286e3aeb81bc`)
