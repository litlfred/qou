---
# qou-l790
title: Triage the 106 CRITICAL script-QA findings surfaced by the qou-z8x9 sweeper fix
status: completed
type: task
priority: normal
created_at: 2026-08-26T14:18:44Z
updated_at: 2026-08-26T14:30:31Z
---

## Triaged 2026-08-26 — and the headline number was wrong in my favour

`computations/audits/mpf_float_cast_triage.py`, an AST scan of the 106 files
the fixed sweeper flagged.

    files flagged critical      106
    files with a real cast      105
    TOTAL CASTS                 246   <- the sweep reports first_hit ONLY,
                                         so "106 findings" undercounts 2.3x
    checker false positives       1   float64_leak_audit.py -- its
                                      .set_description() prose contains the
                                      words "`float(...)` casts"

NONE are in `_deprecated/`. All live.

    75  other/assigned_to_a_name        <- largest real-risk bucket
    30  other/collected_into_list
    25  assertion_kwarg                 <- documented convention, mechanical
    25  display                         <- PERMITTED by AGENTS.md
    17  serialised
    15  other/arithmetic_operand        <- float64 COMPUTATION, forbidden
    14  evalf_discarded
    10  anchor_truncated
     9  other/passed_to_a_call
    ... tail: IfExp 7, returned 6, Lambda 4, compared 3, comprehensions 5, kwarg 1

## AST, because my regex pass was wrong in BOTH directions at once

The first classifier was regex and, in one run, called
`"abs_tr_M": float(mp.fabs(...))` a string literal -- it is a real cast on the
VALUE side, the leading quote being the dict KEY -- while MISSING the one
genuine string-literal false positive. A regex cannot separate code from prose
about code. Recorded because this is the third time today the same shape of
error has cost me a pass.

## What is NOT claimed

`anchor_truncated` and the `other/*` buckets are NOT automatically defects. A
numpy consumer may cast at its own boundary deliberately, which AGENTS.md
explicitly permits ("where the loss is visible"). Those need per-file
judgement. Only `assertion_kwarg` is mechanically safe.

## Deliberately NOT drained

The 25 `assertion_kwarg` fixes span ~15 producers, and each fix means
re-running that producer to regenerate its witness. AGENTS.md caps witness
refreshes at <= 3 per idle pass. Draining needs the owner's scoping, so this
bean measures and stops.
