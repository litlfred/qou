---
# qou-ah1m
title: main regressed 2 witnesses on the raw-float64 ratchet (phase-transition-q-ideal-gas, seifert-volume-meson-n7-extension)
status: todo
type: task
priority: normal
created_at: 2026-08-30T09:54:37Z
updated_at: 2026-08-30T09:55:03Z
---

## Measured 2026-08-30 on `origin/main`

`computations/witness_raw_float64_audit.py` full sweep:

    NEW dirty witnesses : 0
    REGRESSED           : 2
         6 -> 11    computations/phase-transition-q-ideal-gas.witness.json
        51 -> 55    computations/seifert-volume-meson-n7-extension.witness.json

## Attribution — this is main's, not a branch's

Established without re-running on a clean checkout, which is unnecessary here:
the ratchet's verdict is a function of exactly three things — the two witnesses,
and `computations/raw-float64-baseline.json`. **None of the three is touched by
the branch that found it** (`claude/library-intake-6-uploads-2026-08-30`,
a library-intake PR), and the auditor itself is untouched too. So the verdict is
deterministic from main's own content.

Last commits on the two witnesses, both ancestors of `origin/main`
(`git merge-base --is-ancestor 13483c9b48 origin/main` -> true):

    13483c9b48  QOU(26f2): drain 2 - and the first one where the drained claim turned out false
    5a9bbf3350  QOU(26f2): drain 11 more - and two claims whose subjects have vanished

So a **draining** pass is what regressed them. Worth noting for its own sake: a
sweep whose purpose is to reduce raw float64 raised it on two files, and its own
commit messages record that it was already finding its claims turning out false.
Read those two commits before draining these — the fix may be a partial revert
rather than new work.

## Why it is not fixed in the PR that found it

Fixing it means re-running two producers and committing their witnesses, which
is unrelated to a library intake and would bury the finding where no reviewer
would look. The regenerated audit witnesses were deliberately **not** committed
either: their diffs carry an environment change (`sympy 1.12 -> 1.14.0`) and a
different invocation (`--strict`), so committing this container's copies would
replace main's environment stamp — exactly what `precision-gates.sh` warns
against for the drift-only cases it auto-reverts.

## Next

Diff each witness against the two named commits to see which fields gained raw
float64, then fix **at the producer** — never by widening
`raw-float64-baseline.json`. Baselines drain, never grow.
