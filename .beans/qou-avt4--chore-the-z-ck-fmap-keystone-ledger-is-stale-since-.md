---
# qou-avt4
title: 'CHORE: the z->c_k f-map keystone ledger is stale since 2026-07-11 and still states z_C as its upstream datum'
status: todo
type: task
priority: normal
created_at: 2026-08-26T04:14:19Z
updated_at: 2026-08-26T04:14:19Z
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
