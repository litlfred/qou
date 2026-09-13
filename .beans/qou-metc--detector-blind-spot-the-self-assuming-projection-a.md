---
# qou-metc
title: 'DETECTOR BLIND SPOT: the self-assuming-projection audit cannot see an APPLIED single projection — 26 counted becomes 42, and the tuple case was already fixed this way'
status: todo
type: bug
priority: normal
created_at: 2026-09-13T17:33:19Z
updated_at: 2026-09-13T18:26:53Z
---

## MEASURED 2026-09-13 on the QOU Lean tree (2870 .lean files)

    proof-no-self-assuming-projection, live detector      26
    same run, one regex added                             42
                                                      -------
    invisible to the live detector                        16

All 16 come out COUNTED, not exempt — so they pass the detector's own PRIMARY
signal (the `CONCLUSION_FIELD` name gate: the author named the field
`claim_*`, `*_eq`, `holds`, …). They are invisible for one reason only: no
pattern matches the body SHAPE.

## THE SHAPE, and why it is the one that matters

`detectSelfAssuming` recognises four bodies:

    ctx.field                      PROJECTION_BODY
    by exact ctx.field             EXACT_PROJECTION
    <ctx.a, ctx.b>                 TUPLE_PROJECTION
    <ctx.a x, ctx.b x>             APPLIED_TUPLE_PROJECTION

and not the fifth:

    ctx.field s t hst              -- an APPLIED SINGLE projection

`PROJECTION_BODY` is `/^([a-z][\w']*)\.([A-Za-z_][\w']*)\s*$/` — it ends at
the field name, so any argument after it kills the match. `pat` then stays
undefined and `detectSelfAssuming` RETURNS BEFORE reaching its own structural
fallback, `projectionTypeMatchesConclusion`, which exists precisely to catch a
projection whose field name escapes the convention. The strongest check the
detector has is unreachable for this shape.

**This is the subclass that matters, not a corner case.** A class field
carrying a conclusion is almost always `∀ … → …`; to produce the conclusion
the theorem MUST apply it to the binders. So a self-assuming projection whose
conclusion is universally quantified is invisible BY CONSTRUCTION, and a
universally quantified conclusion is the normal case.

## 🛑 AND THE SAME FIX WAS ALREADY MADE, ONE ARITY OVER

`APPLIED_TUPLE_PROJECTION` exists, and its own comment says why:

    // An *applied*-field tuple `<ctx.impl_x ctx.active, ctx.impl_y ctx.active>`:
    // each component is a field `word.field` optionally APPLIED to further
    // `word[.field]` arguments. The `TUPLE_PROJECTION` regex above rejects the
    // trailing argument, so these placeholder-canonical projections escaped the

So "the regex rejects the trailing argument" was diagnosed, understood, and
repaired — **for the tuple case only**. The one-field analogue of the same bug
was left. That is what makes this a taxonomy row rather than a bug report: the
author had the right model of the failure and applied it at one arity.

## HOW IT WAS FOUND — by fixing an instance the detector never reported

`QOU/BraidsKnots/mobius_frobenius_kernel.lean`, body
`ctx.classical_limit s t hst`, class field `classical_limit` stating the
theorem's conclusion verbatim, under a class docstring reading *"All fields
are inputs; none is the conclusion."* A textbook §3b-cond item 5 projection.
The audit reported **0 defect candidates** on that subtree BEFORE the fix as
well as after — measured by stashing the change and re-running, not assumed.

Its field name escapes `CONCLUSION_FIELD`, so had the shape matched it would
have landed EXEMPT via the structural gate rather than COUNTED. It is a 17th
case, of a different kind from the 16.

## CONSEQUENCE FOR qou-z9ws's SIZING

`qou-z9ws` sized the population from detector output: 112 entries, ~102
independent defects, 0 of 12 sampled legitimate. **That 112 is a floor, not a
count** — it cannot include any applied single projection. Do not quote it as
the size of the problem.

## WHAT IS NOT CLAIMED

That the 16 are 16 defects. They are candidates surfaced by a deliberately
loose probe regex
(`/^(?:by\s+exact\s+)?([a-z][\w']*)\.([A-Za-z_][\w']*)(?:\s+[A-Za-z_][\w'.]*)+\s*$/`)
and each still needs the agent adjudication the review ledger demands. The
measurement establishes that the detector cannot SEE them, which is a
statement about the detector; whether each is a genuine defect is a statement
about the file and has not been made.

Nor is a fix proposed here as a side effect. The detector's own comments say
promoting newly-covered patterns to hard failures is *"a deliberate follow-up,
not a silent side effect of closing the blindspot"*, and 26 → 42 is a 62 %
rise in a critical-severity criterion. The probe patch was applied in a
scratch copy and reverted; `git diff` on the detector is clean.


## LANDED 2026-09-13 — and finding the fix surfaced a WORSE defect

Both are now taxonomy rows: 42 (this one) and 43 (the ledger).

### Row 42 — the pattern, landed EXEMPT

APPLIED_PROJECTION added beside the tuple form it is the one-field analogue of.
Measured, QOU Lean tree, 2871 .lean:

  counted (total_defects)      34 -> 34     gate stays green
  this criterion, counted      26 -> 26
  total_exempt                 42 -> 58     +16
  files_flagged                61 -> 76
  applied-field-projection      0 -> 16

All 16 land EXEMPT, as the two prior coverage expansions did, and all 16 enter
the review ledger so --check-ledger demands an agent verdict on each.
Promoting them to hard failures is issue #7329 and is NOT done here.

No regression: no previously-counted finding moved into the new exempt bucket
(counted unchanged while exempt rose by exactly the 16 new entries).
--selftest-docstring-sorry passes.

### 🛑 Row 43 — I DESTROYED 106 COMMITTED ADJUDICATIONS FINDING IT

Seeding the ledger for those 16, scoped to
content/quantum-observable-universe/lean, rewrote
docs/audits/lean-vacuity-review-ledger.json -863/+67 and deleted 106 of 329
entries. Caught in the git diff and reverted; nothing committed. NO CHECK WOULD
HAVE CAUGHT IT -- the run prints only "N candidate(s)".

The deletion loop already carries a guard for the SAME confusion one axis over:
it distinguishes "fixed" from "not produced by this scanner", added 2026-08-30
after a run deleted 116 of 268 entries. It does not distinguish "fixed" from
"NOT SCANNED". All 106 were in categories this audit DOES produce, so that
guard preserved none of them. The ledger spans 22 roots across two papers; only
223 entries live under the subtree scanned.

And the --json path three hundred lines up ALREADY REFUSES a partial scan, in
those words. The ledger is the other write path of the same API and never got
the rule -- row 33 (qou-3ral) a second time.

Fixed by SCOPING the deletion, not refusing the run: a partial scan still
resolves stale entries inside what it looked at, and cannot touch what it did
not. Regression test: the exact destructive command now preserves 210
foreign-category and 45 unscanned-file entries.

### WHAT IS STILL OPEN

1. Adjudicating the 16. They are candidates from a deliberately conservative
   regex, not verdicts. qou-z9ws measured 0 of 12 legitimate on the PREVIOUSLY
   VISIBLE population -- evidence about that population, not this one.
2. Whether to promote applied-field-projection from EXEMPT to COUNTED. Issue
   #7329; an owner call, since it turns a critical gate red on 16 files.
3. Seeding the ledger for the 16. Needs a CORPUS-WIDE scan across all 22 roots,
   not the subtree scan that caused row 43. Deliberately not run here.
4. qou-z9ws's 112-entry sizing is a FLOOR. Not re-sized.
