---
# qou-qia8
title: 'EPIC: writhe level-of-definition -- (w-n) mod 2 is the link-level shadow'
status: completed
type: task
priority: normal
created_at: 2026-08-10T19:30:50Z
updated_at: 2026-08-15T22:31:26Z
---

OWNER RULINGS (2026-08-10), authoritative:
 1. GS normal forms ARE the states (reading 1). Reading 2 kept open, not working.
 2. 'The observable at a point is the trace on the LOWEST part of the substrate
    tower' -- a canonical SECTION of the vertical direction (destabilise via
    tr_M(x T_n) = z tr_M(x), evaluate at minimal level), NOT a quotient.
 3. Interpretation adopted: (w-n) mod 2.

PROVED (WritheMarkovInvariance.lean, sorry-free):
  Markov I  (conjugation, horizontal, fixed n): writhe PRESERVED  [writhe_conj]
  Markov II (stabilization, vertical):          writhe shifts +-1 [writhe_stabilize]
                                                on the SAME LINK
  (w,n) -> (w+-1, n+1); w, w-n, w+n all NON-invariant; (w-n) mod 2 IS the only one.

IDENTIFIED (6/6 machine-checked): (w-n) mod 2 = COMPONENT PARITY c mod 2, via the
permutation-sign identity sign(pi) = (-1)^(n-c) = (-1)^w. Verified on unknot,
trefoil, T(2,5), Hopf, gluon unit, Borromean.

Consequence: writhe-derived quantities (Q = w/2, I_3) are well-defined AT THE
BOTTOM OF THE TOWER / on normal forms, but are NOT functions on links. The
minimal level is the braid index (a link invariant) and the surviving moves there
are conjugation/exchange, which preserve the writhe -- so nothing numerical
changes; only the LEVEL at which claims are stated.


EPIC RESOLVED 2026-08-11 via PR #4961 (merged). All 18 commits landed. Children:
ap47 V7 done, cvoq V8 done, wqto V9 scope-(a) landed but the datum is still open,
rhfy V10 done, yz26 V11 done, owft V12 DECLINED (see that bean).
Bean was left at 'todo' after the merge; closed here on the reorientation pass.
