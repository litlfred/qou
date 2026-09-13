---
# qou-metc
title: 'DETECTOR BLIND SPOT: the self-assuming-projection audit cannot see an APPLIED single projection — 26 counted becomes 42, and the tuple case was already fixed this way'
status: todo
type: bug
priority: normal
created_at: 2026-09-13T17:33:19Z
updated_at: 2026-09-13T17:33:39Z
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
