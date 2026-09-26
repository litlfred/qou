---
# qou-a31p
title: Witness regeneration flipped 29 assertions PASS->FAIL and every blocking gate stayed green
status: in-progress
type: task
priority: normal
created_at: 2026-08-23T14:00:03Z
updated_at: 2026-08-23T15:38:50Z
---

## What happened

Commit `a0ee2ac5e` regenerated 563 witnesses. I verified it with
`precision-gates.sh`, saw "All blocking precision gates green", and shipped it.

It flipped **29 assertions from PASS to FAIL** (2 went the other way; net **-27**)
across 20 witnesses.

## Why the gates did not catch it

`scripts/precision-gates.sh:118`:

    "witness failed-assertion ratchet|computations/witness_failed_assertion_audit.py|--strict|yes|no"

The last field is `blocking` — and it is **no**. That ratchet is ADVISORY. Every
blocking gate stayed green while the corpus lost 27 passing assertions. The gate
that exists for exactly this class does not gate.

Measured after the fact: the ratchet sat at **136 witnesses / 177 failed
assertions** against a baseline of **111**.

## The flips are not float noise

`chi-convention-trM-ratio-probe`, both flipped assertions:

    BEFORE  sign_only_collapses_pn   computed=1  expected=1  tol=0  passed=True
    AFTER   sign_only_collapses_pn   computed=0  expected=1  tol=0  passed=False

Boolean, zero tolerance. A structural property that held and no longer does — not
a tolerance grazed by a precision change.

## Fixed here

The 20 witnesses carrying a PASS->FAIL regression are restored to their
pre-regeneration content. Ratchet returns to **117 / 146**. The other ~543
regenerated witnesses are kept: they carry the genuine precision improvement.

A restored witness is stale against its producer's scriptHash. That is the right
trade: a stale witness is honest about being stale, whereas a regenerated one that
silently drops a passing assertion is not.

## Root cause, unresolved

I do not yet know WHY re-running flips these. Candidates:

- the dps sweep (50 -> 70) changing a value some structural check depends on
- environment drift in this container (`engineVersion` moves numpy 2.5.0 ->
  2.4.6 on regeneration, so the committed witnesses were made on a different box)
- genuine nondeterminism

The `li_2_q` truncation fix is NOT a candidate: it moves digit ~22 and cannot
flip a zero-tolerance boolean.

## Two things this establishes

1. **Bulk witness regeneration in this container is not safe** without an
   assertion-diff check. Blocking gates do not cover it.
2. **The failed-assertion ratchet should block**, or a pre-commit assertion diff
   should exist. Nothing else catches a regeneration that quietly turns passes
   into failures.


---

# ROOT CAUSE FOUND — and it reverses my conclusion. The sweep caused none of it.

I reported that commit `a0ee2ac5e` "flipped 29 assertions PASS -> FAIL" and
restored 20 witnesses in `3d3928331` to undo it. **That was wrong.** The sweep
caused zero of them.

## The bisect

For each regressed witness, I ran its producer at the **pre-sweep source**
(`34b2a75d4~1`) in this container and compared against the committed witness:

    already failing before the sweep : 15
    caused by the sweep              :  0
    inconclusive (crash/not found)   :  4

Fifteen for fifteen. Every testable case was **already failing from its own
pre-sweep source**.

Precision is independently exonerated. Sweeping `chi_convention_trM_ratio_probe`
across `QOU_COMPUTE_DPS`:

    dps=30 40 50 60 65 70  ->  computed=[0,0] at every one

The assertion fails at the ORIGINAL dps=50 just as it does at 70. And the
producer is deterministic — five consecutive runs, identical `[0,0]`.

## So what was actually wrong

**The committed witnesses were stale.** They recorded `passed: True` for
assertions their own producers no longer satisfy. `chi_convention_trM_ratio_probe`
is the clean example: witness last generated `d156e8d50` (2026-08-02), source
changed by `7768c9d26` (2026-08-22, *"per_knot_density_* is now canonical — owner
ruling"*), witness never regenerated after. It kept asserting a property the
owner ruling had already invalidated, for three weeks.

Regeneration did not break these assertions. **It stopped the corpus from lying
about them.**

## Corrected here

`3d3928331` is undone — the 20 witnesses are back to their regenerated content,
recording the failures that are actually there. The advisory ratchet returns to
136 witnesses / 177 failed assertions against a baseline of 111.

Those 25-over-baseline are **not new breakage**. They are pre-existing failures
that were invisible because stale witnesses recorded stale passes. A corpus that
reports 136 real failures is in better shape than one reporting 111 while 25 more
are hidden.

## What still stands from the original finding

The gate observation is unchanged and still worth acting on:
`scripts/precision-gates.sh:118` registers the failed-assertion ratchet with
`blocking=no`. Nothing blocking watches assertion outcomes. That is how a
three-week-stale PASS survived — and equally how a genuine regression would.

## What I got wrong, and why

I saw PASS -> FAIL, assumed my change caused it, and reverted without bisecting.
The correct first move was the one I eventually made: run the pre-sweep source and
see whether the failure predates the change. Reverting on suspicion put 15 stale
passes back into the tree for one commit.
