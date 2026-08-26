---
# qou-569e
title: main's committed witnesses are stale against main's own import cone (23% value move)
status: todo
type: task
priority: normal
created_at: 2026-08-26T13:38:21Z
updated_at: 2026-08-26T13:39:11Z
---

## The measurement

Two committed witnesses on `main` do not reproduce when their producer is
re-run **on a clean `main` worktree**. This is not branch drift; it is `main`
disagreeing with itself.

### 1. `qbeta-hoefsmit-stage-b-per-block-ck-probe.witness.json` — 23 % value move

    main COMMITTED at_q0        0.01189678602591702641115153
    clean-main REGENERATED      0.01459788064126113670087499
    my branch REGENERATED       0.01459788064126113670087499   (identical)

The two regenerations agreeing, on trees that differ only by a guard that is a
no-op on this data, is what makes the attribution airtight: the move is `main`'s.

The `symbolic` field also collapses from a large unsimplified rational into
`(3*q**12 - 14*q**10 + 31*q**8 - 40*q**6 + 31*q**4 - 14*q**2 + 3)/(4*q**5 + 4*q**3)`,
which is the shape of the change — a symbolic path that now returns a reduced
form.

### 2. `all-nuclides-wedderburn-spectral-v2.witness.json` — a FAILING assertion
that now passes

    committed   "computed": 0.5958883193268535    "passed": false   allPassed: false
    fresh run   "computed": 2.0603103745727144e-15 "passed": true    allPassed: true

So the corpus currently records a failed assertion for a check that passes.

## Probable cause — named, not established

`main` landed `fbc0858af feat(qou-3xk6): chi_lambda_braid(precision='symbolic_q')
now RETURNS, not raises`, plus the convention-C excisions in #5821 / #5815, in
the same window. Both are in these producers' import cone. Each producer's own
`scriptHash` still matches its witness, so **the producers did not change** —
this is import-cone drift, the class AGENTS.md describes.

I have not bisected to the specific commit. Do not state the cause as
established without doing so.

## Why this is filed rather than fixed

It was found while landing the `qou-cm7l` REFUSE guards (PR #5823). Running
those producers to verify the guards are silent on good data regenerated the
witnesses, and the regenerations carry the move.

Committing them there would have put a **23 % change in a recorded value, and an
assertion flipping false → true**, inside a PR titled "vacuous-pass guards".
That is how a real number change gets rubber-stamped. They were reverted and
the PR carries only the three `.py` guards; the omission is stated in that
commit message rather than left silent.

## Also stale, same cause, lower stakes

Three audit witnesses move on every gate run because their committed copies
predate main's recent landings:

    q0-anchor-consistency-audit    Q0_OK 978 -> 980, Q0_COMPARISON 1 -> 2
    witness-provenance-audit       total_scanned 2790 -> 2793, prov_missing 96 -> 82
    q0-value-drift-audit           proton-pin 1695 -> 1698

These deltas are counts OF witnesses, and a diff that adds no witness file
cannot move them — which is how they were excluded without a second worktree
run.

## What someone should do

Re-run both producers on `main` and commit the results there, saying which
number moved and why. The `at_q0` value in particular is a recorded quantity
that something downstream may read; leaving a 23 %-stale copy committed is
worse than the vacuous assertions this arc has been chasing, because this one
is a wrong number rather than an untested claim.
