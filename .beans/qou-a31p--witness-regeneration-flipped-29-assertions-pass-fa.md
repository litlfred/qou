---
# qou-a31p
title: Witness regeneration flipped 29 assertions PASS->FAIL and every blocking gate stayed green
status: in-progress
type: task
priority: normal
created_at: 2026-08-23T14:00:03Z
updated_at: 2026-08-23T22:19:54Z
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


---

## MEASURED 2026-08-23 — both halves, and they separate cleanly

**Half 1: the 29 flips.** Resolved. Every one bisected to a STALE PASS, not a
regression. Detail in `93e24e23d`: the worst,
`m_n_matches_codata_within_10ppb` at 2.389 -> 501.43 ppb, is identical at
`QOU_COMPUTE_DPS` 50/60/70 so precision is exonerated, and its inputs were
corrected AFTER the witness was last computed (`codata_constants.py` 08-19,
"hand-typed and 7 of 11 were wrong"; `experimental_constants.py` 08-22).

My own error here is recorded in `1edde3a7b`: I reverted 20 witnesses on
suspicion, and bisecting afterwards showed 15 of 15 were already failing before
the sweep. The revert put 15 stale passes back for one commit. **Bisect, do not
revert.**

A second instance landed later on this branch and was handled the right way:
`qbeta-jacobi-anger-tower-general` flipped PASS -> FAIL, and the obvious bisect
misleads — running the whole tree at the pre-change commit DOES restore the
passing numbers, because that moves the producer and every dependency at once.
Holding the tree at HEAD and reverting only the single suspect line reproduced
HEAD bit for bit, exonerating this branch and pointing at the 2026-08-09
convention C -> D excision instead.

**Half 2: "and every blocking gate stayed green."** Confirmed, and now
quantified. `witness_failed_assertion_audit.py` is the gate that sees this, and
it is registered ADVISORY at `precision-gates.sh:145`.

    origin/main                   28 NEW + 1 GROWN   (--strict exits 1)
    claude/mass-table-...-triage  34 NEW + 1 GROWN   (--strict exits 1)

Diffing the NEW sets: **the branch adds exactly 6, clears 0.** Named,
with values, in bean **qou-60r9**.

The flip-to-blocking condition is already written into
`precision-gates.sh:118` — "when a plain run reports no witness outside the
baseline" — and it cannot be met from this branch alone, because 28 of the 34
are main's. Two separable jobs: resolve the branch's 6 (qou-60r9), and drain
main's 28 (existing triage, qou-ad4t), then flip.

So this bean's structural complaint is real, is not fixable by editing a gate
flag, and is now tracked with the exact count each side owns.
