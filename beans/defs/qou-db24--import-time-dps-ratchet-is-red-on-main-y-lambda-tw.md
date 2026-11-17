---
# qou-db24
title: 'import-time dps ratchet is RED on main: y_lambda_two_row_cap_gate.py builds mpf(''1e-30'') before dps is raised'
status: in-progress
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-28T15:18:36Z
updated_at: 2026-11-17T11:48:14Z
parent: qou-9nnz
---

## Found 2026-08-28, incidentally, on a clean main tree

Running `scripts/precision-gates.sh` on `origin/main` (cdbdc84af1) with no local
changes to any producer, the **import-time dps ratchet** reports:

    proven lossy (literal arg): 1
       L47: mpf('1e-30')  [literal]
    baseline literal / expr : 185 / 103
    now      literal / expr :   1 /  20
    NEW files (not baselined) : 1
       literal=1  expr=0   computations/audits/y_lambda_two_row_cap_gate.py

`new_not_baselined: 1` is a ratchet RED. The committed
`mpf-import-time-dps-audit.witness.json` still records `literal_findings: 0`
and `new_not_baselined: 0`, so the committed audit disagrees with a fresh run.

## Whose

`computations/audits/y_lambda_two_row_cap_gate.py` landed recently in
`25e8f8c1d9 gate(y_lambda): assert the convention-D two-row cap at the TABLE,
not per consumer`. Not the discoverer's file; recorded rather than fixed to
avoid widening an unrelated PR.

## The defect

Line 47 builds `mpf('1e-30')` at module scope, i.e. while `mp.dps` is still
mpmath's default 15. The ratchet's whole subject: string-sourcing is necessary
but not sufficient, the TIMING matters too. A tolerance constant built at dps 15
carries 15 digits no matter what the caller later sets.

For a bare tolerance like `1e-30` the practical impact is likely nil — the value
is exactly representable and used as a comparison threshold. **That is a reason
to check it, not a reason to leave it red**: a ratchet with one unexplained
entry is a ratchet people learn to ignore, which is the failure mode this gate
family's own comments keep returning to.

## Two honest options

1. **Fix at the literal** — move the constant inside the function, or build it
   after `set_compute_dps()`. Cheapest if the value is genuinely used at
   precision.
2. **Baseline it with a stated reason** — only if the value provably cannot
   lose anything. NOTE the standing rule: baselines DRAIN, never grow. Adding
   an entry needs an argument in the commit, not a `--rebaseline`.

Do not simply regenerate `mpf-import-time-dps-audit.witness.json` to make the
committed count match: that records the regression as the new normal, which is
the widening this repo forbids.


--------

## SECOND, independent red in the same run — `audits-tree raw-float64`

The same clean-tree run of `scripts/precision-gates.sh` reports a second
BLOCKING red, unrelated to the first:

    RED: import-time dps ratchet   audits-tree raw-float64

    audits-tree raw-float64  (scan root: docs/audits)
      NEW dirty witnesses : 1
      REGRESSED           : 0
             2  docs/audits/2026-08-26-kernel-defeq-sample.witness.json

Two raw float64 fields in a witness under `docs/audits`, dated 2026-08-26 and
landed on main. Also not the discoverer's file.

So the gate suite is red on `main` for TWO independent reasons, neither of them
belonging to any in-flight branch. Worth stating because a branch that runs the
suite and sees red will reasonably wonder whether it caused it — that costs a
cycle each time until one of these is drained.

Fix per the standing rule, for both: **at the producer**, carrying `mpmath.mpf`
end to end and serializing with `_precision.fmt`. Do not add either file to a
baseline and do not `--rebaseline`.

## Caveat on the numbers above

The gate suite was first run here against a tree that was being modified
concurrently (two audit witnesses regenerated then reverted mid-run), so that
run's per-gate counts were unreliable. Both reds were then re-established by
running the two audits individually against a tree whose only change was one
unrelated file, and each named its offending file explicitly — which is the
evidence quoted above, not the racing run.
