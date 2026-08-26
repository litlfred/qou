---
# qou-ckwt
title: 'DEFECT: canonical c_k producer is convention D, its committed witness is C (471x regression pending)'
status: todo
type: task
priority: high
created_at: 2026-08-26T03:28:36Z
updated_at: 2026-08-26T03:28:36Z
---

Parent: `qou-cds1`. CONFIRMED 2026-08-26 by decisive test.

`computations/qbeta/qbeta_ck_cache.py` line 85 is `z = q**3 / (q**2 + 1)`
(convention D, single z assignment, verified at HEAD). Its committed witness
`qbeta-ck-cache.witness.json` carries the convention-C
`c_3 = -2.06934257711516783787971951725`.

MEASURED (producer run on main, tree restored after; git status clean):

    quantity              committed (C)     re-run today (D)
    c_3                   -2.0693425771     -974.4318877
    derived-tier Q_N2 err  1278.6 ppb        602433.2 ppb     <- 471x regression

So the framework's HEADLINE DERIVED Q_beta number is one
`python3 qbeta_ck_cache.py` away from regressing 471x.

HARNESS CALIBRATED FIRST: a verbatim mpmath re-implementation at 60 dps
reproduces the committed witness at z_C to 1.8e-31, and reproduces all three of
qou-cds1's recorded numbers (-2.0693 / -974.43 / -86.08; implied c_2
-1.0176 / -9.2989 / -1.7331). Only then was the producer run.

ALREADY A CANDIDATE, NOT ALREADY CONFIRMED. `convention-frame-staleness-audit`
(155 D-form producers, 47 suspects) already LISTS this witness in `candidates`.
Only 2 of the 47 had a `confirmed_by_decisive_test` entry and this was not one.
This bean upgrades it candidate -> confirmed and measures the magnitude. Do not
re-report the class as new.

WHY THE DETECTORS MISS IT. It is the OPPOSITE polarity from the three live C
sites qou-cds1 tracks: not a C site awaiting migration, but a producer ALREADY
on D whose witness was never regenerated. The C->D detectors hunt C spellings
and are looking the wrong way. The witness declares no `markov_convention`,
exactly as substrate_ladder_quantities' docstring predicted (0 of 278 c_k
witnesses declare a frame).

DISPOSITION IS A JUDGEMENT CALL AND IS DELIBERATELY NOT TAKEN. Regenerating
publishes -974 as canonical; reverting the producer to C re-introduces an
excised convention. Both are wrong. The right fix is whatever qou-cds1
concludes. INTERIM ASK: a guard so the producer cannot be run into the cache by
accident.

Audit: docs/audits/2026-08-26-three-gap-assessment-and-ck-cache-convention-confirm.md
