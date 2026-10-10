---
# qou-avt3
title: 'ATTACK 3 (blocked upstream): c3^odd is not well-posed until (H1) is derived or dropped'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-26T04:14:19Z
updated_at: 2026-10-04T15:16:25Z
parent: qou-avtq
---

Recording WHY c3^odd should not be attacked directly yet, so the next agent does
not spend a session on it.

S := c_3 + Vol(4_1) is a DEFINED RESIDUAL, and AGENTS.md's own rule "Defined
residual != derived decomposition" applies verbatim. All three of its checks
fail here:

1. The bar-split is NOT empirically accessible. A bar-decomposition needs the
   function at both q and 1/q; every substrate anchor sits at q ~ 1.10998 and
   none supplies q ~ 0.901. So the split always comes from an assumed structural
   form.
2. The offset is NOT forced. The sign flip across the anchors is produced by
   ANY constant strictly between the two values -- a window of width 0.049,
   including 2 + 1/36, 63/31 and e^0.708. The flip restates "c_3 differs between
   anchors"; it says nothing about Vol(4_1).
3. (H1) c_3^even = -Vol(4_1) is NOT derived, and the corpus carries a DIFFERENT
   bar-even split of the same object (the exact Q(sqrt 3) u-ladder in KC21).

On top of that, every value-level fact is convention-C-frame and inherits
qou-cds1.

So "close c3^odd" currently asks for the odd half of a quantity whose SPLIT is
an assumption and whose FRAME is excised. The honest prerequisite is to derive
(H1) or drop it. What IS bankable and unaffected: S = h*D(u-tilde) with D
convergent, radius rho = u-tilde(q*_rho), closed form
D(w) = phi(w)log(1 - w/rho) + psi(w) with phi(rho) = 1/(2*h*_rho) pinned and no
free parameters, plus certified non-holonomicity across every tested class
including the log-closure.
