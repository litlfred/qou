---
# qou-2zjp
title: 'GAP: alpha_high_precision is broken on main — bisection bracket no longer contains a root'
status: todo
type: task
priority: normal
created_at: 2026-08-24T14:53:43Z
updated_at: 2026-08-24T14:54:16Z
---

## What happens

    $ QOU_Q0_ANCHOR=proton python3 computations/alpha/alpha_high_precision.py
    HIGH-PRECISION alpha* DETERMINATION (dps=50)
      q_0 = 1.1099785827513808
      M_p = 938.27208943,  M_n = 939.56542179
      Bracket: err(0.3) = +1.074673%, err(0.32) = +0.649810%
      ERROR: no sign change in bracket
    (exit 1)

The mpmath bisection is hardcoded to the bracket [0.3, 0.32]. Both endpoints
now give a POSITIVE error, so there is no root inside it and the script exits
before writing anything.

## Not caused by the q0 migration

It fails identically at BOTH anchors -- the decomposition harness records
`FAIL(m=1,p=1)`, i.e. the muon leg (its own declared anchor, the state on
main) fails too. So this is pre-existing breakage on main, surfaced by the
migration sweep rather than introduced by it. Its witness cannot be migrated
until the producer runs at all.

## Why it looked silent

It reports the error on STDOUT, not stderr, so a harness capturing only stderr
records rc=1 with an empty message. Worth knowing for any other sweep.

## Next honest step

Someone who knows what alpha* is supposed to be needs to decide whether the
bracket is stale (widen/re-derive it) or whether the root genuinely left the
interval because an upstream constant moved -- in which case the interesting
question is which one, and the committed witness is asserting a value the
current code can no longer reproduce. Do NOT just widen the bracket until it
finds something; that would fit a number rather than derive it.
