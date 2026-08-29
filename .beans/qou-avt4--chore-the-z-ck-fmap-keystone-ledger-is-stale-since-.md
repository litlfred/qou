---
# qou-avt4
title: 'CHORE: the z->c_k f-map keystone ledger is stale since 2026-07-11 and still states z_C as its upstream datum'
status: completed
type: task
priority: normal
created_at: 2026-08-26T04:14:19Z
updated_at: 2026-08-26T04:25:59Z
---

docs/coordination/z-ck-fmap-keystone.md is the named ledger for the f-map
keystone. Its SESSION LOG STOPS AT 2026-07-11 -- before the 2026-08-09 and
2026-08-15 convention rulings -- and its section 2 "Proved inputs (do not
re-derive)" still lists

    z(q) = sqrt(q)/(1+q)   with its exact 3-term recursion

as the keystone's UPSTREAM DATUM. That is convention C, excised. Registry KC13
carries the correct scoping in prose and ZBarParity.lean now carries it in Lean
(zD_bar_twist, added 2026-08-26), but the ledger a reader is pointed at does not.

Also missing from it: the four-direction fence on c_3 = J_Hopf(1) = -2 landed
2026-08-21 (bar-odd scope-(b) by a proved parity invariant; bar-even by q=1
genericity; amplitude route C by 4*lambda_2^3 + lambda_3^2 = 6.088 != 0, a sum
of two positives). A reader working from this ledger would not know the keystone
had been fenced.

Low risk, docs-only, but it is the entry point for the whole f-map programme,
so a stale one costs a session.

## DONE 2026-08-26

Currency banner added at the head of `docs/coordination/z-ck-fmap-keystone.md`
(before §1, where a reader lands), naming three things the ledger did not say:

(a) §§1–4 carry convention C as the keystone's PROVED UPSTREAM DATUM, and the
    `ea56` class-`Z2` exclusion does NOT transfer -- its proof runs through
    "the bar-fixed locus is a subring and z lies in it", and `z_D` is not
    bar-fixed (`bar(z_D) = q^-4 z_D`, `QOU.QBeta.zD_bar_twist`).
(b) The keystone's target has been fenced from four directions since
    2026-08-21.
(c) Three further routes closed 2026-08-26.

Seven session-log rows appended covering 2026-08-09 -> 2026-08-26: the owner
rulings, KC13's re-scoping, the four-direction fence, the
alpha-not-a-function-of-the-weights result and PR #5187's TAUTOLOGICAL
retraction, the ZBarParity de-hard-coding, the three closed routes, and the live
residue (the affine-vs-cosine form clash).

Historical sections left INTACT and explicitly framed as the record of how the
keystone was worked, not as current status -- deleting them would lose the
derivation history, which is what a ledger is for.

Render-QA: hand grep battery CLEAN (delimiter balance, no \operatorname, no
list-parser hijack inside display math, no unfenced inner env, no crash-class
unicode, begin/end + bigl/bigr pairing); 13 log rows well-formed. NOT
machine-validated by the pipeline render -- folio-assistant is absent in this
container -- stated per AGENTS.md rather than reported as render-checked.
