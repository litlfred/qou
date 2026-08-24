---
# qou-v4ht
title: 'Vacuity audit UNDER-COUNTS: 76 agent-confirmed genuine defects are auto-exempted as ''type-matched projection, triage pending'''
status: completed
type: task
priority: normal
created_at: 2026-08-22T12:18:52Z
updated_at: 2026-08-22T20:34:09Z
---

Found on 2026-08-22 while re-seeding the ledger to pick the next drain tranche (successor to qou-h3ly).

## Two counts, both 'right', differing by 2x

Fresh full-corpus scan (3029 .lean): `total_defects = 64`.
Committed review ledger: **123 genuine**.

Reconciled by key (file::decl::category):

| | n |
|---|---|
| scanner flags, total | 186 |
| ...of which non-exempt | 64 |
| ...of which exempt | 122 |
| ledger genuine | 123 |
| genuine still flagged by scanner | **123 (all of them)** |
| genuine NOT flagged any more | **0** |
| genuine but marked EXEMPT by scanner | **76** |

So **no** ledger-genuine entry is stale — every one is still detected. But
**76 of the 123** are suppressed from `total_defects` by a single
exemption reason, verbatim:

> `type-matched projection (field name escapes CONCLUSION_FIELD; tracked, triage pending)`

i.e. the heuristic that recognises a self-assuming projection matched the
*type* but the field name fell outside the `CONCLUSION_FIELD` name list, so
the finding is auto-exempted and labelled 'triage pending'. An agent has
since adjudicated all 76 as **genuine**, but the exemption still fires.

## Why this matters

`total_defects = 64` under-counts the adjudicated backlog by **59** (123 vs
64). Anyone sizing the remaining vacuity work off the committed artifact —
which AGENTS.md and the arc-review bean both point at — plans for roughly
half the real queue. This is the same hazard qou-2z9j flagged ('do NOT trust
the committed audit JSON counts'), but in the opposite direction: previously
the artifact was stale-low because a file-scoped run clobbered it; now it is
low because an exemption suppresses confirmed defects.

**The ledger is the authoritative tracker** (per qou-2z9j) and should be
quoted for backlog size; `total_defects` should not.

## Fix options (not chosen here)

1. Once a ledger verdict of `genuine` exists for a key, stop applying the
   `exempt` heuristic to it — the adjudication outranks the heuristic.
2. Widen `CONCLUSION_FIELD` so the 76 stop escaping it (risks widening
   false positives; the exemption exists because the name test is weak).
3. Keep the exemption but report two numbers — `total_defects` and
   `total_adjudicated_genuine` — so the artifact cannot be read as the
   whole backlog.

Option 1 looks right: it is the smallest change and it makes the artifact
agree with the ledger by construction.

## FIXED 2026-08-22 — option 1 implemented

A ledger verdict of `genuine` now lifts a `triage pending` exemption, so the
artifact and the ledger can no longer disagree about the backlog.

**Measured, same tree:** total_defects **53 -> 129**, exempt 123 -> 47, with
**76 promoted** — exactly the gap this bean recorded.

**Scoped deliberately narrower than the bean's option 1.** Only exemptions
matching `LEDGER_TRACKED_EXEMPT` (/triage pending/) are liftable, not every
exemption. Those are the ones that *themselves say a verdict is owed*;
exemptions that ARE verdicts (shadow stub, `@marker` opt-out, iff-from-
directions) stay exempt regardless of the ledger. And only `genuine`
promotes — `legit`/`advisory` say the hit is not a defect, so lifting on
them would invert the ledger's meaning.

**This is the follow-up the original author asked for**, not a unilateral
change: the emit site's own comment calls the exemption 'tracked-not-counted
on landing' and names 'promoting these to hard failures' as 'a deliberate
follow-up'. The verdicts it was waiting on now exist.

**Not a new CI break.** The workflow gate fails on
`proof-no-trivial-type-mismatch,lean-import-after-content` — neither is a
promoted category. `--check-ledger` exits 1 both before and after (verified
by stashing the patch and re-running): 3 candidates carry stale verdicts on
current main, pre-existing and unrelated. Filed separately.

**Regression test:** `content/pipeline/lean-vacuity-ledger-promotion.test.ts`
— synthetic .lean + synthetic ledger, so it asserts the invariant rather than
a corpus count that legitimately moves. Covers both directions (genuine lifts;
legit/advisory do not).
