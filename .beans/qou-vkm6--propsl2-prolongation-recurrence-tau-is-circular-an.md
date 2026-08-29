---
# qou-vkm6
title: 'prop:sl2-prolongation-recurrence: tau is circular, and its geometric growth is refuted past n=5'
status: todo
type: task
priority: normal
created_at: 2026-08-29T07:00:33Z
updated_at: 2026-08-29T07:01:31Z
---

## The defect (found 2026-08-29, bean qou-1xne, PR #5967)

`content/quantum-observable-universe/mass-theory/sl2-prolongation-recurrence.md`
is a live PROPOSITION block ending:

  "pinning theta is the last open number of the depth correspondence, and is
   solvable from three residue weights via tau = (a_D^(2) + a_D^(4))/a_D^(3)."

Two problems, both measured in computations/w3_closeability_audit.py (R2):

1. CIRCULAR. That formula is the n=2 instance of the block's own recurrence
   a_D^(n+2) = tau*a_D^(n+1) - a_D^(n) rearranged, so it CONSUMES a_D^(3) as an
   input rather than determining anything. Measured: define tau that way and the
   a_D^(4) residual is 0 to full working precision for EVERY value substituted
   for a_D^(3) -- 1.337, 0.668, 4.011, 1.0, 0.001 all give residual 0.0. It is an
   identity, not a solve. So "the last open number" is not pinned by it.

2. THE GROWTH CLASS IS REFUTED, and the block does not say so.
   docs/audits/2026-06-25-sw-jet-prolongation-explicit-and-fork.md settled the
   fork: a_D^(n) grows SUPER-EXPONENTIALLY (branch-point exponent 1/2 - n gives
   period ratios n - 1/2, unbounded), so the depth-2 SL2 form -- which is
   necessarily geometric, ratio -> lambda_+ -- is "an n<=4 effective fit".
   Re-measured at the proton pin, iterating from the true a_D^(2), a_D^(3):

     n=4   0.0%     (by construction -- tau was solved on it)
     n=5  -0.38%
     n=6 -14.31%
     n=7 -32.17%
     n=8 -52.21%

   grep'd: neither "super-exp" nor "effective fit" nor the fork appears in
   sl2-prolongation-recurrence.md or its -proof sibling. A reader of the block
   alone would take the recurrence as the live prolongation law.

## What to do

NOT a deletion -- the det B = 1 / Sp(2) polarisation argument stands, and the
depth-2 form is correct where it was solved (n <= 4). This needs SCOPING per
AGENTS.md "Before declaring refuted": record it as a scope-(a) n<=4 effective
form, drop or qualify the "solvable from three residue weights" sentence (it is
circular as written), and cite the 2026-06-25 fork audit. Check the .qa.json
sidecar and any downstream uses[] consumers before editing.
