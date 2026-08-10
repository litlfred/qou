---
# qou-j6gb
title: mpf_import_time_dps_audit is NOT wired into precision-gates.sh — 288 findings, 185 proven lossy, gate silent
status: in-progress
type: bug
created_at: 2026-08-10T02:36:03Z
updated_at: 2026-08-10T02:36:03Z
---


## The finding

`computations/mpf_import_time_dps_audit.py` exists, is position-aware, runs, and
exits **1** under `--strict`:

    module-scope mpf built before precision is raised: 288  [witness-emitting scripts]
       proven lossy (literal arg):                     185
       position-risky (expr arg, not statically provable): 103
    files affected: 91

It is **not in `scripts/precision-gates.sh`'s `GATES` array.** The eight that are:

    q0-anchor flip            q0_anchor_consistency_audit.py
    mpf(<float>) source       mpf_float_source_audit.py
    float64-padding ratchet   witness_float64_padding_audit.py
    mp.dps no-op              mpf_context_dps_audit.py
    module-const precision    module_const_precision_audit.py
    raw-float64 ratchet       witness_raw_float64_audit.py
    q0-value drift ratchet    q0_value_drift_audit.py
    no-free-parameter cert    no_free_parameter_certificate.py   (advisory)

Per bean `qou-mnrd` and AGENTS.md §"QA is agent-owned; CI is a backup",
`precision-gates.sh` **is** the gate — `witness-staleness.yml` is dispatch-only
under the owner's 2026-06-30 Actions-billing directive, reaffirmed 2026-08-09.
So an audit outside that array is an audit nobody runs.

## Why this matters more than the raw count

The defect it detects hit **five times in the drain arc** (`qou-mnrd`), each time
found by accident when something happened to print at high dps, each time a
one-line fix:

    VOL_41              one_loop_c_sigma_tetrahedral_probe.py
    q0                  gram_qtrace_hutchinson_probe.py
    TOLERANCE_PPQ       cross_check_trM_1ppb.py
    REG_ZC / REG_ZD     y_lambda_su_n.py                      (two constants)

All five were caught by *other* gates (`module-const precision`,
`float64-padding`) reacting to downstream symptoms. The audit built specifically
for the cause was sitting right there, unrun. `qou-brkp` records that this same
audit was ALSO silent on two files its own remediation had broken — that bug is
fixed, but the audit went from "silent for a parse reason" to "silent because
nothing calls it", which is the same outcome by a different route.

## Why it is probably unwired, and what to do about it

Almost certainly because adding it blocking turns the gates red on day one: 288
findings is not a thing anyone drains in one sitting.

**Wire it as a ratchet, not as a pass/fail.** That is exactly the shape that took
`witness_raw_float64_audit.py` from red to green over this arc:

  1. baseline the current 288 into a `mpf-import-time-dps-baseline.json`, with
     the audit's own "do NOT add a file to the baseline to silence this" warning
     in its header;
  2. block only NEW and REGRESSED entries;
  3. add it to `GATES` with `blocking=yes`, and to the workflow's step list —
     `precision-gates.sh` carries an explicit instruction to keep those two in
     sync.

Then the 185 proven-lossy are a background drain like the float64 ones, and a
sixth instance cannot land.

**Do the 185 before the 103.** "Proven lossy (literal arg)" means a decimal
string was parsed at 15 dps and the digits are gone — statically certain, and the
fix is the idempotent `set_compute_dps()` above the constant. The 103
"position-risky (expr arg)" are not statically provable and some will be fine;
mixing them into the same ratchet dilutes a signal that is currently exact.

## Not done here

Not wired, not baselined. Wiring a new blocking gate changes what every agent's
pre-commit and `/prepare-merge` must pass, which is a scoped decision rather than
a drive-by — and the 288 number should be re-measured at the moment it is
baselined, not taken from this bean.
