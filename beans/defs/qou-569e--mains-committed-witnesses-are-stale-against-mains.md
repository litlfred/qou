---
# qou-569e
title: main's committed witnesses are stale against main's own import cone (23% value move)
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-26T13:38:21Z
updated_at: 2026-10-04T15:21:25Z
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


## 2026-08-26, second instance — and this one is a stale RESULT, not a stale value

Found the same way: running a producer to verify an unrelated guard.

`v_hat_to_delta_lambda_bridge` — assertion `one_dim_universal_product_formula_closes`

    committed              computed=12  expected=12  allPassed=TRUE
    clean-main regenerated computed= 4  expected=12  allPassed=FALSE
    this branch            computed= 4  expected=12  allPassed=FALSE   (identical)

Clean `main` and this branch agree exactly, on trees differing only by an
if/else that cannot alter an assertion's outcome when the else fires. So the
move is `main`'s.

**This is worse than the 23 % `at_q0` move recorded above.** That was a number
drifting. This is a claim: the corpus currently records that a *universal
product formula closes* — 12 of 12 channels — when re-running the producer on
main today gives **4 of 12**. Whatever changed in the cone, two-thirds of the
channels stopped matching and the committed witness still says they all do.

I have not investigated why 8 channels stopped matching. That is the actual
question and it is not this bean's — this bean only establishes that the
committed witness disagrees with main.

### Not the same as its neighbour

`delta_lambda_v_hat_z_transfer_phase5d_4` was checked at the same time and is
**not** an instance: committed `allPassed=False`, fresh run `allPassed=False`.
It was already failing and still is. Worth stating so nobody re-derives it as a
third case.

### Running total for this bean

    qbeta-hoefsmit-stage-b-per-block-ck   at_q0 0.011896786 -> 0.014597880   (23%)
    all-nuclides-wedderburn-spectral-v2   allPassed false -> true
    v-hat-to-delta-lambda-bridge          12/12 TRUE -> 4/12 FALSE           <- NEW

Three witnesses now, and the third inverts a positive result. All were
regenerated during verification of PRs #5823's guards and all were reverted
rather than committed, for the reason stated above: a two-thirds drop in a
match count does not belong in a PR about assertion guards.


## A SECOND, DIFFERENT staleness on the same tree (measured 2026-08-26, prepare-merge for PR #5842)

Recorded here rather than as a new bean because it is the same claim family
("main's committed witnesses are stale against main"), but the MECHANISM is not
the import-cone one above and should not be conflated with it.

`scripts/precision-gates.sh --changed`, run on a branch touching ONLY two .lean
files and one Python script — zero `computations/` changes — reported three
stale committed audit witnesses:

  computations/audits/q0-anchor-consistency-audit.witness.json
  computations/audits/witness-provenance-audit.witness.json
  computations/q0-value-drift-audit.witness.json

All blocking gates were green (rc=0); this is the advisory report, not a block.

**The drift is main's, and it is COUNT drift, not value drift.** Attribution
checked before claiming it, per the gate's own instruction:

  q0-anchor-consistency:  Q0_OK 986 -> 994, Q0_ANCHOR_MISSING 1661 -> 1659,
                          Q0_AMBIGUOUS_NO_REASON 14 -> 13
  witness-provenance:     total_scanned 2797 -> 2802, prov_missing 98 -> 83,
                          prov_exempt_no_reader 251 -> 272
  q0-value-drift:         proton-pin 1708 -> 1724

The newly-listed entries name `mpf-float-cast-triage.witness.json` (PR #5831,
merged to main today as 84109e9502) and
`chi-deuteron-h6-at-qinv-50dps-colour-weighted.witness.json`. So: witnesses
landed on main, and the audits that count them were not re-run in the same PR.

**I did NOT commit the regenerated copies, deliberately.** Two reasons:

1. Not mine to fix on a two-file Lean PR — it would mix an unrelated main-side
   refresh into an unrelated change.
2. More importantly, committing them would have written THIS container's
   environment into main's audit records: the regenerated copies dropped
   `"numpy": "2.4.6"` (numpy is not installed here) and changed
   `pyhecke_native_build` c85ef99ee89ce1c3 -> 47b406d9ba6e343f. That is not a
   drift refresh, it is stamping a degraded environment block onto a record
   whose whole job is to describe the producing environment.

Whoever drains this should re-run the three audits in an environment that has
numpy and the matching pyhecke_native build, and check the env block before
committing.



## Reasons for Scrapping

Duplicate of `qou-7tr2` (work-plan reorganisation 2026-10-04). Evidence: [B] main witnesses stale against import cone - same audit
Content is untouched; only this work item is closed.
